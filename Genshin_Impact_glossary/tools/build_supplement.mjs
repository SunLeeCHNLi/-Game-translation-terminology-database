import fs from 'node:fs';
import path from 'node:path';

const LD = 'E:/Download/BT/Codex_input/repos/genshin-langdata/dataset/dictionary/';
const MAIN = 'E:/Download/BT/Codex_input/genshin-glossary';
const OUT = 'E:/Download/BT/Codex_input/genshin-glossary-supplement';

const LANG_FIELD = [['zh-CN','zhCN'],['zh-TW','zhTW'],['en-US','en'],['ja-JP','ja']];
const CODES = LANG_FIELD.map(x=>x[0]);

// langdata file -> [category, folder]
const MAP = {
  'artifacts':                 ['artifacts',    ''],
  'characters-fatui':          ['characters',   ''],
  'characters-fontaine':       ['characters',   ''],
  'characters-general':        ['characters',   ''],
  'characters-inazuma':        ['characters',   ''],
  'characters-khaenriah':      ['characters',   ''],
  'characters-liyue':          ['characters',   ''],
  'characters-mondstadt':      ['characters',   ''],
  'characters-natlan':         ['characters',   ''],
  'characters-nodkrai':        ['characters',   ''],
  'characters-snezhnaya':      ['characters',   ''],
  'characters-sumeru':         ['characters',   ''],
  'domains':                   ['domains',      ''],
  'drops-boss':                ['materials',    ''],
  'drops':                     ['materials',    ''],
  'gemstones':                 ['materials',    ''],
  'items':                     ['materials',    ''],
  'specialties':               ['materials',    ''],
  'talent-materials':          ['materials',    ''],
  'weapon-materials':          ['materials',    ''],
  'enemies':                   ['enemies',      ''],
  'foods':                     ['foods',        ''],
  'living-beings':             ['animals',      ''],
  'locations':                 ['geographies',  ''],
  'weapons':                   ['weapons',      ''],
  'dialogue':                  ['dialogue',     'extra'],
  'facilities':                ['facilities',   'extra'],
  'objects':                   ['objects',      'extra'],
  'organizations':             ['organizations','extra'],
  'quests':                    ['quests',       'extra'],
  'sereniteapot':              ['sereniteapot', 'extra'],
  'story':                     ['story',        'extra'],
  'system':                    ['system',       'extra'],
  'y-events':                  ['events',       'extra'],
  'z-archives':                ['archives',     'extra'],
};

function clean(s) {
  if (typeof s !== 'string') return null;
  const t = s.replace(/[\r\n\t]+/g, ' ').replace(/ {2,}/g, ' ').trim();
  return t === '' ? null : t;
}
function csvField(s) { return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }
function sortRows(rows){ return rows.sort((a,b)=> a[0]<b[0]?-1:a[0]>b[0]?1:a[1]<b[1]?-1:a[1]>b[1]?1:0); }
function writeCsv(file, rows) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const lines = ['source,target,tgt_lng'];
  for (const r of rows) lines.push(csvField(r[0]) + ',' + csvField(r[1]) + ',' + r[2]);
  fs.writeFileSync(file, '\ufeff' + lines.join('\r\n') + '\r\n', 'utf8');
}

// ---- existing rows from the main glossary (dedupe base) ----
const known = new Set();
(function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith('.csv')) {
      const txt = fs.readFileSync(p, 'utf8').replace(/^\ufeff/, '');
      for (const l of txt.split('\r\n')) if (l && l !== 'source,target,tgt_lng') known.add(l);
    }
  }
})(MAIN);
console.log('existing main rows:', known.size.toLocaleString());

// ---- load langdata ----
const words = [];
for (const name of Object.keys(MAP)) {
  const mod = await import('file:///' + LD + name + '.ts');
  for (const w of mod.default) words.push({ file: name, w });
}
console.log('langdata entries:', words.length);

const out = new Map();          // "cat/folder" -> code -> rows[]
const variantRows = new Map();  // code -> rows[]
for (const c of CODES) { variantRows.set(c, []); }
const seenOut = new Set(), seenVar = new Set();
let skippedDup = 0, added = 0;

for (const { file, w } of words) {
  const [cat, folder] = MAP[file];
  const terms = {};
  for (const [code, field] of LANG_FIELD) { const v = clean(w[field]); if (v) terms[code] = v; }
  const present = Object.keys(terms);
  if (present.length < 2) continue;
  for (const [tCode, tTerm] of Object.entries(terms)) {
    for (const [sCode, sTerm] of Object.entries(terms)) {
      if (sCode === tCode || sTerm === tTerm) continue;
      const line = csvField(sTerm) + ',' + csvField(tTerm) + ',' + tCode;
      const key = (folder ? folder + '/' : '') + cat + '\u0000' + tCode + '\u0000' + sCode + '\u0000' + sTerm + '\u0000' + tTerm;
      if (known.has(line)) { skippedDup++; continue; }
      const bucketKey = (folder ? folder + '/' : '') + cat;
      if (!out.has(bucketKey)) { const m = new Map(); for (const c of CODES) m.set(c, []); out.set(bucketKey, m); }
      if (seenOut.has(key)) continue;
      seenOut.add(key);
      out.get(bucketKey).get(tCode).push([sTerm, tTerm, tCode]);
      added++;
    }
  }
  // variants as extra source terms
  const v = w.variants || {};
  for (const [sCode, field] of LANG_FIELD) {
    const list = v[field];
    if (!Array.isArray(list)) continue;
    for (const raw of list) {
      const sTerm = clean(raw);
      if (!sTerm) continue;
      for (const [tCode, tTerm] of Object.entries(terms)) {
        if (sCode === tCode || sTerm === tTerm) continue;
        const line = csvField(sTerm) + ',' + csvField(tTerm) + ',' + tCode;
        if (known.has(line)) continue;
        const key = tCode + '\u0000' + sCode + '\u0000' + sTerm + '\u0000' + tTerm;
        if (seenVar.has(key)) continue;
        seenVar.add(key);
        variantRows.get(tCode).push([sTerm, tTerm, tCode]);
      }
    }
  }
}
console.log('new rows added:', added.toLocaleString(), '| skipped as duplicates of main:', skippedDup.toLocaleString());

// ---- write ----
if (fs.existsSync(OUT)) fs.rmSync(OUT, { recursive: true, force: true });
const report = [];
for (const code of CODES) {
  const perCat = {}; let total = 0;
  for (const [bucket, m] of out) {
    const rows = sortRows(m.get(code));
    if (rows.length === 0) continue;
    writeCsv(path.join(OUT, code, bucket + '.csv'), rows);
    perCat[bucket] = rows.length; total += rows.length;
  }
  const vrows = sortRows(variantRows.get(code));
  writeCsv(path.join(OUT, code, '_variants.csv'), vrows);
  report.push({ code, categories: perCat, variantRows: vrows.length, rows: total });
  console.log(code.padEnd(6), String(total).padStart(8), 'rows |', Object.keys(perCat).length, 'files | variants', vrows.length);
}
fs.writeFileSync(path.join(OUT, '_counts.json'), JSON.stringify({ source: 'xicri/genshin-langdata', languages: report }, null, 2), 'utf8');
console.log('DONE');
