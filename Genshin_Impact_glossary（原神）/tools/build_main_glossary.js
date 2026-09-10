const fs = require('fs');
const path = require('path');

const SRC = 'E:/Download/BT/Codex_input/repos/genshin-db/src/data';
const IDX = SRC + '/index';
const OUT = 'E:/Download/BT/Codex_input/genshin-glossary';

const LANGS = [
  ['ChineseSimplified',  'zh-CN', '简体中文'],
  ['ChineseTraditional', 'zh-TW', '繁體中文'],
  ['English',            'en-US', 'English'],
  ['Japanese',           'ja-JP', '日本語'],
  ['Korean',             'ko-KR', '한국어'],
  ['French',             'fr-FR', 'Français'],
  ['German',             'de-DE', 'Deutsch'],
  ['Spanish',            'es-ES', 'Español'],
  ['Russian',            'ru-RU', 'Русский'],
  ['Portuguese',         'pt-BR', 'Português'],
  ['Italian',            'it-IT', 'Italiano'],
  ['Turkish',            'tr-TR', 'Türkçe'],
  ['Thai',               'th-TH', 'ภาษาไทย'],
  ['Vietnamese',         'vi-VN', 'Tiếng Việt'],
];

const CATS = [
  ['characters',      'characters'],
  ['talents',         'talents'],
  ['constellations',  'constellations'],
  ['weapons',         'weapons'],
  ['materials',       'materials'],
  ['foods',           'foods'],
  ['crafts',          'crafts'],
  ['artifacts',       'artifacts'],
  ['domains',         'domains'],
  ['enemies',         'enemies'],
  ['animals',         'animals'],
  ['outfits',         'outfits'],
  ['windgliders',     'windgliders'],
  ['namecards',       'namecards'],
  ['geographies',     'geographies'],
  ['achievements',    'achievements'],
  ['adventureranks',  'adventureranks'],
];

const TCG = [
  ['action-cards',    'tcgactioncards'],
  ['character-cards', 'tcgcharactercards'],
  ['enemy-cards',     'tcgenemycards'],
  ['summons',         'tcgsummons'],
  ['status-effects',  'tcgstatuseffects'],
  ['keywords',        'tcgkeywords'],
  ['card-backs',      'tcgcardbacks'],
  ['card-boxes',      'tcgcardboxes'],
  ['detailed-rules',  'tcgdetailedrules'],
  ['level-rewards',   'tcglevelrewards'],
];

// categories whose localizable text lives in the per-item detail files
const SPECIAL = [
  ['adventureranks',   'adventureranks',   ['unlockDescription']],
  ['level-rewards',    'tcglevelrewards',  ['unlockdescription']],
];

const stats = { gender: 0, hashOnly: 0, leftover: new Set() };

function normalize(raw) {
  let s = raw;
  const had = /\{[MF]#[^{}]*\}/.test(s);
  if (had) stats.gender++;
  s = s.replace(/\{M#([^{}]*)\}\{F#[^{}]*\}/g, '$1').replace(/\{F#[^{}]*\}\{M#([^{}]*)\}/g, '$1');
  s = s.replace(/\{[MF]#([^{}]*)\}/g, '$1');
  s = s.replace(/\{NON_BREAK_SPACE\}|\{SPACE\}/g, ' ');
  if (s.startsWith('#')) { s = s.slice(1); if (!had) stats.hashOnly++; }
  s = s.replace(/[ \t]{2,}/g, ' ').trim();
  for (const m of s.match(/\{[^{}]*\}/g) || []) stats.leftover.add(m);
  return s;
}

const namemapCache = new Map();
function maps(folder) {
  if (!namemapCache.has(folder)) {
    const m = {};
    for (const [lang, code] of LANGS) {
      const p = path.join(IDX, lang, folder + '.json');
      if (!fs.existsSync(p)) { m[code] = null; continue; }
      const nm = JSON.parse(fs.readFileSync(p, 'utf8')).namemap || {};
      const out = new Map();
      for (const [k, v] of Object.entries(nm)) {
        if (typeof v !== 'string') continue;
        const n = normalize(v);
        if (n) out.set(k, n);
      }
      m[code] = out;
    }
    namemapCache.set(folder, m);
  }
  return namemapCache.get(folder);
}

/** description-based categories: {code: {id: [term, ...]}} */
const specialCache = new Map();
function specialMaps(folder, fields) {
  if (!specialCache.has(folder)) {
    const res = {};
    for (const [lang, code] of LANGS) {
      const dir = path.join(SRC, lang, folder);
      const per = {};
      if (fs.existsSync(dir)) {
        for (const f of fs.readdirSync(dir)) {
          if (!f.endsWith('.json')) continue;
          const j = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
          const terms = [];
          for (const fld of fields) {
            if (typeof j[fld] !== 'string') continue;
            for (const piece of j[fld].split(/[\n;；]+/)) {
              const n = normalize(piece);
              if (n) terms.push(n);
            }
          }
          const uniq = [...new Set(terms)];
          if (uniq.length) per[f.replace(/\.json$/, '')] = uniq;
        }
      }
      res[code] = per;
    }
    specialCache.set(folder, res);
  }
  return specialCache.get(folder);
}

function csvField(s) { return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }
function writeCsv(file, rows) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const lines = ['source,target,tgt_lng'];
  for (const r of rows) lines.push(csvField(r[0]) + ',' + csvField(r[1]) + ',' + r[2]);
  fs.writeFileSync(file, '\ufeff' + lines.join('\r\n') + '\r\n', 'utf8');
}
const sortRows = rows => rows.sort((a,b) => a[0]<b[0]?-1:a[0]>b[0]?1:a[1]<b[1]?-1:a[1]>b[1]?1:0);

function buildFromMap(folder, targetCode) {
  const m = maps(folder), tgt = m[targetCode];
  if (!tgt) return [];
  const seen = new Set(), rows = [];
  for (const [slug, target] of tgt) {
    for (const [srcCode, srcMap] of Object.entries(m)) {
      if (srcCode === targetCode || !srcMap) continue;
      const src = srcMap.get(slug);
      if (!src || src === target) continue;
      const k = src + '\u0000' + target;
      if (seen.has(k)) continue;
      seen.add(k); rows.push([src, target, targetCode]);
    }
  }
  return rows;
}

function buildFromSpecial(folder, fields, targetCode) {
  const m = specialMaps(folder, fields), tgt = m[targetCode] || {};
  const seen = new Set(), rows = [];
  for (const [id, terms] of Object.entries(tgt)) {
    terms.forEach((target, i) => {
      for (const [srcCode, per] of Object.entries(m)) {
        if (srcCode === targetCode) continue;
        const src = (per[id] || [])[i];
        if (!src || src === target) continue;
        const k = src + '\u0000' + target;
        if (seen.has(k)) continue;
        seen.add(k); rows.push([src, target, targetCode]);
      }
    });
  }
  return rows;
}

function conceptCount(folder, kind) {
  if (kind === 'special') {
    const m = specialMaps(folder, SPECIAL.find(s => s[1] === folder)[2]);
    return (m['zh-CN'] ? Object.values(m['zh-CN']).reduce((a, t) => a + t.length, 0) : 0);
  }
  const m = maps(folder)['zh-CN'];
  return m ? m.size : 0;
}

if (fs.existsSync(OUT)) fs.rmSync(OUT, { recursive: true, force: true });
const concepts = {};
for (const [cat, folder] of CATS) {
  const sp = SPECIAL.find(s => s[0] === cat);
  concepts[cat] = sp ? conceptCount(folder, 'special') : conceptCount(folder, 'namemap');
}
for (const [cat, folder] of TCG) {
  const sp = SPECIAL.find(s => s[0] === cat);
  concepts[cat] = sp ? conceptCount(folder, 'special') : conceptCount(folder, 'namemap');
}

const report = [];
for (const [, code, native] of LANGS) {
  let total = 0; const perCat = {}; const tcgPer = {};
  for (const [cat, folder] of CATS) {
    const sp = SPECIAL.find(s => s[0] === cat);
    const rows = sortRows(sp ? buildFromSpecial(folder, sp[2], code) : buildFromMap(folder, code));
    writeCsv(path.join(OUT, code, cat + '.csv'), rows);
    perCat[cat] = rows.length; total += rows.length;
  }
  let tcgTotal = 0;
  for (const [name, folder] of TCG) {
    const sp = SPECIAL.find(s => s[0] === name);
    const rows = sortRows(sp ? buildFromSpecial(folder, sp[2], code) : buildFromMap(folder, code));
    writeCsv(path.join(OUT, code, 'TCG', name + '.csv'), rows);
    tcgPer[name] = rows.length; tcgTotal += rows.length;
  }
  report.push({ code, language: native, categories: perCat, TCG: tcgPer, tcgRows: tcgTotal, rows: total + tcgTotal });
  console.log(code.padEnd(6), String(total + tcgTotal).padStart(9), 'rows | TC G', String(tcgTotal).padStart(6), '| adventureranks', perCat['adventureranks'], '| level-rewards', tcgPer['level-rewards']);
}
fs.writeFileSync(path.join(OUT, '_counts.json'), JSON.stringify({ languages: report, concepts }, null, 2), 'utf8');
console.log('\nnormalize: gender', stats.gender, '| # without gender', stats.hashOnly, '| leftover', [...stats.leftover].join(' | '));
console.log('DONE');
