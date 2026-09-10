# -*- coding: utf-8 -*-
"""Harmonized (和谐) Chinese names used by the Azur Lane CN server.

The CN client replaced Sakura-Empire / Iron-Blood and later a few other ship
names with plant- and animal-based names.  The mapping lives in the game file
ShareCfg/name_code.json:  name = original name, code = harmonised name.
Entries are cross-checked against the community reference table on
zh.moegirl.org.cn (碧蓝航线/名称对照表).
"""
import csv, json, os, re
from collections import OrderedDict, defaultdict

BASE = r'E:\Download\BT\Codex_input\AzurLaneData-main\AzurLaneData-main'
OUT = r'E:\Download\BT\Codex_input\AzurLane_Glossary'
LANGS = OrderedDict([('zh-CN', 'CN'), ('en', 'EN'), ('ja', 'JP'), ('zh-TW', 'TW'), ('ko', 'KR')])


def load(path):
    with open(path, encoding='utf-8-sig') as fh:
        return json.load(fh)


def clean(v):
    return ' '.join(v.replace('\u3000', ' ').split()).strip() if isinstance(v, str) else ''


# ---------------------------------------------------------------- ship records
type_names = {}
for lng, folder in LANGS.items():
    data = load(os.path.join(BASE, folder, 'ShareCfg', 'ship_data_by_type.json'))
    type_names[lng] = {int(k): clean(v.get('type_name', '')) for k, v in data.items() if isinstance(v, dict)}

ships = {}
for lng, folder in LANGS.items():
    for sid, rec in load(os.path.join(BASE, folder, 'sharecfgdata', 'ship_data_statistics.json')).items():
        if not isinstance(rec, dict):
            continue
        e = ships.setdefault(int(sid), {})
        n = clean(rec.get('name'))
        if n:
            e[lng] = n
        e.setdefault('type_id', rec.get('type'))
        e.setdefault('nationality', rec.get('nationality'))
        e.setdefault('skin_id', rec.get('skin_id'))

skin_group = {int(k): v.get('ship_group') for k, v in
              load(os.path.join(BASE, 'CN', 'ShareCfg', 'ship_skin_template.json')).items()
              if isinstance(v, dict)}
valid_ids = {int(k) for k in load(os.path.join(BASE, 'CN', 'sharecfgdata', 'ship_data_template.json'))}

by_group = OrderedDict()
for sid in sorted(ships):
    if ships[sid].get('zh-CN'):
        by_group.setdefault(skin_group.get(ships[sid].get('skin_id'), 'x%d' % sid), []).append(sid)

records = []
for ids in by_group.values():
    ok = [i for i in ids if i in valid_ids] or ids
    sid = min(ok)
    r = ships[sid]
    records.append({
        'id': sid, 'zh_CN': r['zh-CN'], 'en': r.get('en', ''), 'ja': r.get('ja', ''),
        'zh_TW': r.get('zh-TW', ''), 'ko': r.get('ko', ''),
        'type': type_names['zh-CN'].get(r.get('type_id'), ''),
        'type_en': type_names['en'].get(r.get('type_id'), ''),
    })

index = defaultdict(list)
for r in records:
    index[r['zh_CN']].append(r)


def norm(name):
    n = name
    for pat in (r'[（(]μ兵装[)）]', r'[·.]META', r'[·.]meta'):
        n = re.sub(pat, '', n)
    n = re.sub(r'[·.]改$', '', n)
    n = re.sub(r'改$', '', n)
    return n.strip()


def find_ship(original):
    for cand in (original, norm(original)):
        if index.get(cand):
            return min(index[cand], key=lambda r: r['id'])
    return None


# ---------------------------------------------------------------- harmonized names
nc = load(os.path.join(BASE, 'CN', 'ShareCfg', 'name_code.json'))
entries = sorted((v for v in nc.values()), key=lambda v: v['id'])

# community reference table (parsed from zh.moegirl.org.cn) for cross-checking
wiki = {}
wiki_path = os.path.join(OUT, 'sources', 'moegirl_name_table.json')
if os.path.exists(wiki_path):
    for row in json.load(open(wiki_path, encoding='utf-8')):
        if row[0].isdigit():
            wiki.setdefault(row[1], set()).add(row[2])

ships_rows, equip_rows, detailed = [], [], []
for v in entries:
    original, harmonized = clean(v['name']), clean(v['code'])
    if not original or not harmonized or original == harmonized:
        continue
    kind = 'equipment' if v.get('type') == 2 else 'ship'
    note = ''
    if kind == 'ship' and original in wiki and harmonized not in wiki[original]:
        note = 'wiki: ' + '/'.join(sorted(wiki[original]))
    rec = None if kind == 'equipment' else find_ship(original)
    if kind == 'equipment':
        equip_rows.append((original, harmonized, 'zh-CN', 'zh-CN'))
        detailed.append((original, harmonized, 'zh-CN', 'zh-CN', v['id'], kind, '', '', '', '', '', note))
        continue
    ships_rows.append((original, harmonized, 'zh-CN', 'zh-CN'))
    detailed.append((original, harmonized, 'zh-CN', 'zh-CN', v['id'], kind,
                     rec['type'] if rec else '', rec['id'] if rec else '',
                     rec['en'] if rec else '', rec['ja'] if rec else '',
                     rec['zh_TW'] if rec else '', note))
    # only borrow the foreign names when the entry is that exact ship - retrofit
    # and mass-production entries share the base ship's foreign name, which would
    # produce a misleading "Fusou -> 魟.改" style row
    if rec and rec['zh_CN'] == original:
        for lng, src in (('en', rec['en']), ('ja', rec['ja']), ('zh-TW', rec['zh_TW']), ('ko', rec['ko'])):
            src = clean(src)
            if src and src != original and src != harmonized:
                ships_rows.append((src, harmonized, 'zh-CN', lng))
                detailed.append((src, harmonized, 'zh-CN', lng, v['id'], kind,
                                 rec['type'], rec['id'], rec['en'], rec['ja'], rec['zh_TW'], note))


def write_csv(path, header, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)
    os.replace(tmp, path)


def plain(seq):
    """Project to the requested source/target/tgt_lng shape, de-duplicated."""
    out, seen = [], set()
    for s, t, tl, _sl in seq:
        if (s, t, tl) not in seen:
            seen.add((s, t, tl))
            out.append((s, t, tl))
    return out


write_csv(os.path.join(OUT, 'azur_lane_harmonized_ship_names.csv'), ['source', 'target', 'tgt_lng'],
          plain(ships_rows))
write_csv(os.path.join(OUT, 'azur_lane_harmonized_equipment.csv'), ['source', 'target', 'tgt_lng'],
          plain(equip_rows))
write_csv(os.path.join(OUT, 'azur_lane_harmonized_names_detailed.csv'),
          ['source', 'target', 'tgt_lng', 'src_lng', 'name_code_id', 'kind', 'ship_type',
           'ship_id', 'en', 'ja', 'zh_TW', 'wiki_note'], detailed)

pr = plain(ships_rows)
print('ship harmonised pairs (original -> harmonised):', len({(s, t) for s, t, _l, _s in ships_rows if _s == 'zh-CN'}))
print('  rows incl. EN/JA/TW/KO sources:', len(pr))
print('equipment harmonised entries:', len(equip_rows))
print('entries with a community-table variant:', sum(1 for d in detailed if d[11]))
print('ships matched to a game record:', len({d[7] for d in detailed if d[7]}))



