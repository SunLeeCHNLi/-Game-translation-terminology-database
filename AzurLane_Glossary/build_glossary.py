# -*- coding: utf-8 -*-
"""Build the Azur Lane (碧蓝航线) CN/EN/JA/KO translation glossary from game data.

Data sources: AzurLaneData-main, sharecfgdata for CN / EN / JP / KR / TW.

Ship identity comes from ship_skin_template.json -> ship_group, which is the
authoritative "shipgirl" grouping; ship_data_statistics.json additionally holds
enemy / NPC / event copies that share a ship's name but are not obtainable.
"""
import csv, json, os, re
from collections import OrderedDict, defaultdict
from terms_data import TERMS, CATEGORY_ZH

BASE = r'E:\Download\BT\Codex_input\AzurLaneData-main\AzurLaneData-main'
OUT = r'E:\Download\BT\Codex_input\AzurLane_Glossary'
SPLIT = os.path.join(OUT, 'by_language')
CN = os.path.join(OUT, 'zh-CN')       # Simplified-Chinese termbases
LANGS = OrderedDict([('zh-CN', 'CN'), ('en', 'EN'), ('ja', 'JP'), ('zh-TW', 'TW'), ('ko', 'KR')])
JUNK_EN = {'simulation', 'none', 'null', '-'}
# Han-script characters: their presence in a Latin/Hangul client name means the
# client fell back to the Chinese string instead of shipping a translation.
HAN = re.compile(r'[\u2e80-\u2eff\u3005\u3400-\u9fff\uf900-\ufaff]')
HULL = re.compile(r'^(USS|HMS|KMS|IJN|MNF|FFNF|RN|HDN|SN|KM|SMS)\s+')


def load(path):
    with open(path, encoding='utf-8-sig') as fh:
        return json.load(fh)


def clean(value):
    if not isinstance(value, str):
        return ''
    return ' '.join(value.replace('\u3000', ' ').split()).strip()


def good_english_name(name):
    """Keep real hull designations; drop skin/event placeholders such as 'qipao'."""
    if not name or name.lower() in JUNK_EN or not re.search(r'[A-Za-z]', name):
        return False
    return not name.split(' ')[0][0].islower()


# ---------------------------------------------------------------- hull types
type_names = {}
for lng, folder in LANGS.items():
    data = load(os.path.join(BASE, folder, 'ShareCfg', 'ship_data_by_type.json'))
    type_names[lng] = {int(k): clean(v.get('type_name', ''))
                       for k, v in data.items() if isinstance(v, dict)}

NATION = {
    0: ('', ''), 1: ('白鹰', 'Eagle Union'), 2: ('皇家', 'Royal Navy'),
    3: ('重樱', 'Sakura Empire'), 4: ('铁血', 'Iron Blood'), 5: ('东煌', 'Dragon Empery'),
    6: ('撒丁帝国', 'Sardegna Empire'), 7: ('北方联合', 'Northern Parliament'),
    8: ('自由鸢尾', 'Iris Libre'), 9: ('维希教廷', 'Vichya Dominion'),
    11: ('郁金王国', 'Kingdom of Tulipa'), 96: ('飓风船团', 'Tempesta'),
    97: ('META', 'META'), 98: ('通用', 'Universal'), 99: ('塞壬', 'Siren'),
}

VALID_IDS = {int(k) for k in load(os.path.join(BASE, 'CN', 'sharecfgdata', 'ship_data_template.json'))}
SKIN_GROUP = {int(k): v.get('ship_group') for k, v
              in load(os.path.join(BASE, 'CN', 'ShareCfg', 'ship_skin_template.json')).items()
              if isinstance(v, dict)}

# ---------------------------------------------------------------- gather records
ships = {}
for lng, folder in LANGS.items():
    for sid, rec in load(os.path.join(BASE, folder, 'sharecfgdata', 'ship_data_statistics.json')).items():
        if not isinstance(rec, dict):
            continue
        entry = ships.setdefault(int(sid), {})
        name = clean(rec.get('name'))
        if name:
            entry[lng] = name
        entry.setdefault('type_id', rec.get('type'))
        entry.setdefault('nationality', rec.get('nationality'))
        entry.setdefault('skin_id', rec.get('skin_id'))

# english_name comes from the EN client only - CN/JP/KR/TW carry stale values
for sid, rec in load(os.path.join(BASE, 'EN', 'sharecfgdata', 'ship_data_statistics.json')).items():
    entry = ships.get(int(sid))
    if entry is None or not isinstance(rec, dict):
        continue
    full = clean(rec.get('english_name'))
    if good_english_name(full):
        entry['english_name'] = full


def variant_of(rec):
    joined = ' '.join(str(rec.get(k, '')) for k in LANGS)
    tags = []
    if re.search(r'META|メタ', joined, re.I):
        tags.append('META')
    if re.search(r'[μµ]', joined):
        tags.append('μ兵装')
    if re.search(r'Ⅱ|(?<![A-Za-z])II$|II型|MKII$', joined):
        tags.append('II型')
    return '+'.join(tags)


# ---------------------------------------------------------------- one entry per shipgirl
by_group = OrderedDict()
for sid in sorted(ships):
    if not ships[sid].get('zh-CN'):
        continue
    if not re.search(r'[0-9A-Za-z\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]', ships[sid]['zh-CN']):
        continue                       # placeholder names such as "?????"
    gid = SKIN_GROUP.get(ships[sid].get('skin_id'))
    by_group.setdefault(gid if gid is not None else 'single:%d' % sid, []).append(sid)

canonical, npc_only_groups = [], 0
for gid, ids in by_group.items():
    valid = [i for i in ids if i in VALID_IDS]
    if valid:
        canonical.append(min(valid))
    else:
        canonical.append(min(ids))
        npc_only_groups += 1

records = []
for sid in canonical:
    rec = ships[sid]
    target = rec['zh-CN']
    type_id = rec.get('type_id')
    nat_id = rec.get('nationality')
    nation_zh, nation_en = NATION.get(nat_id, ('', ''))
    if nat_id in range(101, 120):
        nation_zh, nation_en = '联动阵营', 'Collab'
    item = {
        'id': sid, 'zh_CN': target, 'en': rec.get('en', ''), 'ja': rec.get('ja', ''),
        'zh_TW': rec.get('zh-TW', ''), 'ko': rec.get('ko', ''),
        'english_name': rec.get('english_name', ''),
        'type_zh': type_names['zh-CN'].get(type_id, ''),
        'type_en': type_names['en'].get(type_id, ''),
        'nation_zh': nation_zh, 'nation_en': nation_en, 'variant': variant_of(rec),
    }
    # A name byte-identical to the Chinese name is an untranslated fallback - but only
    # in clients that do not write in Han script.  Japanese and Traditional-Chinese
    # names legitimately coincide with the Simplified string (吹雪, 杜威, Z1, ...), so
    # they are kept verbatim.
    for field in ('en', 'ko'):
        if item[field] and item[field] == item['zh_CN'] and HAN.search(item[field]):
            item[field] = ''
    # the EN client ships no name at all for a handful of hulls - use its own
    # hull designation (english_name) instead of showing them without an EN name
    if not item['en'] and item['english_name'] and item['id'] in VALID_IDS:
        item['en'] = HULL.sub('', item['english_name']).replace('.META', ' META')
    records.append(item)

# NPC copies in the 900xxx space sometimes borrow a name with the wrong hull
# type / faction - drop those that disagree with the real ship of that name
profile = defaultdict(lambda: defaultdict(int))
for item in records:
    if item['id'] < 900000:
        profile[item['zh_CN']][(item['type_zh'], item['nation_zh'])] += 1
kept = []
for item in records:
    if item['id'] >= 900000 and profile.get(item['zh_CN']):
        best = max(profile[item['zh_CN']].items(), key=lambda kv: kv[1])[0]
        if (item['type_zh'], item['nation_zh']) != best:
            continue
    kept.append(item)
records = kept

# collapse leftovers that describe the identical ship (main record + event copy)
final, index = [], {}
for item in sorted(records, key=lambda x: x['id']):
    key = (item['zh_CN'], item['en'], item['type_zh'], item['nation_zh'], item['variant'])
    if key in index:
        old = index[key]
        for field in ('ja', 'zh_TW', 'ko', 'english_name'):
            if not old[field] and item[field]:
                old[field] = item[field]
        continue
    index[key] = item
    final.append(item)
records = final

# ---------------------------------------------------------------- glossary pairs
pairs = defaultdict(list)
for rec in records:
    for lng, src in (('en', rec['en']), ('ja', rec['ja']), ('zh-TW', rec['zh_TW']),
                     ('ko', rec['ko']), ('en', rec['english_name'])):
        src = src.strip()
        if src and src != rec['zh_CN']:
            pairs[(lng, src, rec['zh_CN'])].append(rec)

by_source = defaultdict(list)
for (lng, src, tgt), recs in pairs.items():
    by_source[(lng, src)].append((tgt, recs))

rows, amb_rows = [], []
for (lng, src), options in by_source.items():
    options.sort(key=lambda o: (-len(o[1]), o[1][0]['id']))
    for rank, (tgt, recs) in enumerate(options):
        rep = min(recs, key=lambda r: r['id'])
        row = (src, tgt, 'zh-CN', lng, rep['id'], rep['type_zh'], rep['nation_zh'], rep['variant'])
        if len(options) == 1:
            rows.append(row)
        elif rank == 0:
            rows.append(row)                       # dominant reading stays in the glossary
            amb_rows.append(row + (rep['english_name'], 'dominant'))
        else:
            amb_rows.append(row + (rep['english_name'], 'alternative'))

rows.sort(key=lambda r: (r[3], r[0].lower(), r[1]))
amb_rows.sort(key=lambda r: (r[3], r[0].lower(), r[1]))

# ---------------------------------------------------------------- IJN code aliases
cn_codes = load(os.path.join(BASE, 'CN', 'ShareCfg', 'name_code.json'))
aliases = []
for cid, rec in cn_codes.items():
    code, name = clean(rec.get('code')), clean(rec.get('name'))
    if code and name and code != name:
        aliases.append((code, name, 'zh-CN', 'zh-CN', cid))
for folder, lng in (('EN', 'en'), ('JP', 'ja')):
    for cid, rec in load(os.path.join(BASE, folder, 'ShareCfg', 'name_code.json')).items():
        nm, cd = clean(rec.get('name')), clean(rec.get('code'))
        cn = clean(cn_codes.get(cid, {}).get('name'))
        if nm and cn and cd == nm and nm != cn:
            aliases.append((nm, cn, 'zh-CN', lng, cid))
seen_a, uniq_a = set(), []
for a in aliases:
    if (a[0], a[1], a[3]) not in seen_a:
        seen_a.add((a[0], a[1], a[3]))
        uniq_a.append(a)
aliases = sorted(uniq_a, key=lambda r: (r[3], r[0].lower()))


def write_csv(path, header, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)
    import time
    for attempt in range(8):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(0.4)
    print('WARNING: %s stayed locked, wrote %s instead' % (path, tmp))


# ---------------------------------------------------------------- outputs
def plain(seq):
    """3-column projection, de-duplicated (a JP and a TW name can be identical)."""
    out, seen = [], set()
    for s, t, l in seq:
        if (s, t, l) not in seen:
            seen.add((s, t, l))
            out.append((s, t, l))
    return out


write_csv(os.path.join(CN, 'azur_lane_glossary.csv'), ['source', 'target', 'tgt_lng'],
          plain([(s, t, l) for s, t, l, *_ in rows]))
write_csv(os.path.join(CN, 'azur_lane_glossary_detailed.csv'),
          ['source', 'target', 'tgt_lng', 'src_lng', 'ship_id', 'ship_type', 'nation', 'variant'], rows)
write_csv(os.path.join(OUT, 'azur_lane_ship_names_multilingual.csv'),
          ['ship_id', 'zh_CN', 'en', 'ja', 'zh_TW', 'ko', 'english_name', 'ship_type_zh',
           'ship_type_en', 'nation_zh', 'nation_en', 'variant'],
          [[r['id'], r['zh_CN'], r['en'], r['ja'], r['zh_TW'], r['ko'], r['english_name'],
            r['type_zh'], r['type_en'], r['nation_zh'], r['nation_en'], r['variant']]
           for r in sorted(records, key=lambda x: x['id'])])
write_csv(os.path.join(CN, 'azur_lane_ambiguous.csv'),
          ['source', 'target', 'tgt_lng', 'src_lng', 'ship_id', 'ship_type', 'nation',
           'variant', 'english_name', 'role'], amb_rows)
write_csv(os.path.join(OUT, 'azur_lane_ijn_codename_aliases.csv'),
          ['source', 'target', 'tgt_lng', 'src_lng', 'name_code_id'], aliases)

term_rows, seen_t = [], set()
for src_lng, src, tgt, cat in TERMS:
    if (src, tgt, src_lng) in seen_t:
        continue
    seen_t.add((src, tgt, src_lng))
    term_rows.append((src, tgt, 'zh-CN', src_lng, cat, CATEGORY_ZH.get(cat, cat)))
term_rows.sort(key=lambda r: (r[4], r[3], r[0].lower()))
write_csv(os.path.join(CN, 'azur_lane_combined_ships_and_terms.csv'), ['source', 'target', 'tgt_lng'],
          plain([(r[0], r[1], r[2]) for r in rows] + [(r[0], r[1], r[2]) for r in term_rows]))
for lng in ('en', 'ja', 'zh-TW', 'ko'):
    write_csv(os.path.join(SPLIT, 'azur_lane_glossary_%s-zh-CN.csv' % lng),
              ['source', 'target', 'tgt_lng'],
              plain([(s, t, l) for s, t, l, sl, *_ in rows if sl == lng]))

# ---------------------------------------------------------------- report
counts = defaultdict(int)
for r in rows:
    counts[r[3]] += 1
stats = OrderedDict([
    ('ship records in game data', len(ships)),
    ('ship groups in skin table', len(by_group)),
    ('shipgirls in glossary', len(records)),
    ('glossary source strings (EN/JA/TW/KO -> zh-CN)', len(rows)),
    ('rows per source language', dict(counts)),
    ('ambiguous source strings flagged', len({(r[3], r[0]) for r in amb_rows})),
    ('META shipgirls', sum(1 for r in records if 'META' in r['variant'])),
    ('mu-equipment shipgirls', sum(1 for r in records if 'μ兵装' in r['variant'])),
    ('IJN code-name aliases', len(aliases)),
    ('terminology entries', len(term_rows)),
])
with open(os.path.join(OUT, 'build_stats.json'), 'w', encoding='utf-8') as fh:
    json.dump(stats, fh, ensure_ascii=False, indent=2)
for k, v in stats.items():
    print('%s: %s' % (k, v))




