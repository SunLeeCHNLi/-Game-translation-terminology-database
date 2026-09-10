# -*- coding: utf-8 -*-
"""Complete Azur Lane shipgirl termbase using the CN-server harmonised names.

Targets are the names shown by the Simplified-Chinese client: where the game
applies a harmonised (植物/动物) name it is used, otherwise the standard name.
The harmonisation source of truth is ShareCfg/name_code.json (name = original,
code = harmonised).
"""
import csv, json, os, re, io, sys
from collections import OrderedDict, defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'E:\Download\BT\Codex_input\AzurLaneData-main\AzurLaneData-main'
OUT = r'E:\Download\BT\Codex_input\AzurLane_Glossary'
CN = os.path.join(OUT, 'zh-CN')       # Simplified-Chinese termbases
LANGS = ('zh-CN', 'en', 'ja', 'zh-TW', 'ko')

load = lambda p: json.load(open(p, encoding='utf-8-sig'))
clean = lambda v: ' '.join(v.replace('\u3000', ' ').split()).strip() if isinstance(v, str) else ''

# ---------------------------------------------------------------- harmonisation map
nc = load(os.path.join(BASE, 'CN', 'ShareCfg', 'name_code.json'))
hmap = {}
for v in nc.values():
    if v.get('type') != 1:
        continue                                  # type 2 = aircraft / equipment
    orig, harm = clean(v['name']), clean(v['code'])
    if orig and harm and orig != harm:
        hmap.setdefault(orig, harm)

# ---------------------------------------------------------------- ship characters
ships = list(csv.DictReader(open(os.path.join(OUT, 'azur_lane_ship_names_multilingual.csv'),
                                encoding='utf-8-sig')))
print('ship characters loaded:', len(ships))

SUFFIX = re.compile(r'^(?P<base>.*?)\s*[（(](?P<sfx>[^）)]*)[)）]$')


def harmonise(name):
    """Return the CN-server harmonised name, or '' when the ship is unchanged."""
    if name in hmap:
        return hmap[name]
    # NPC-style suffix such as 比叡·META（前排） -> harmonise the base and re-append
    m = SUFFIX.match(name)
    if m:
        base = hmap.get(m.group('base'))
        if base:
            return '%s（%s）' % (base, m.group('sfx'))
    # retrofit written without the dot: 扶桑改 -> 扶桑.改
    if name.endswith('改') and not name.endswith('.改'):
        return hmap.get(name[:-1] + '.改', '')
    if name.endswith('.改'):
        return hmap.get(name[:-2] + '改', '')
    return ''


info = {s['ship_id']: s for s in ships}
rows, detailed = [], []
changed = 0
for s in ships:
    std = s['zh_CN']
    if not re.search(r'[0-9A-Za-z\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]', std):
        continue                                  # placeholder such as ？？？？？
    harm = harmonise(std)
    target = harm or std
    if harm:
        changed += 1

    sources = []
    if harm:
        sources.append(('zh-CN', std))            # original name -> harmonised name
    for lng, key in (('en', 'en'), ('ja', 'ja'), ('zh-TW', 'zh_TW'), ('ko', 'ko'),
                     ('en', 'english_name')):
        src = clean(s.get(key, ''))
        if src and src != target and (lng, src) not in sources:
            sources.append((lng, src))

    for lng, src in sources:
        rows.append((src, target, 'zh-CN', lng, s['ship_id']))
        detailed.append((src, target, 'zh-CN', lng, s['ship_id'], s['ship_type_zh'],
                         s['nation_zh'], s['variant'], std, target))

# ---------------------------------------------------------------- de-duplicate
by_source = defaultdict(list)
for r in rows:
    by_source[(r[0], r[2])].append(r)
for key, group in by_source.items():
    group.sort(key=lambda r: (r[3], int(r[4]) if r[4].isdigit() else 0))

primary, alternates = [], []
for (src, tgt), group in by_source.items():
    targets = OrderedDict()
    for r in group:
        targets.setdefault(r[1], r)
    if len(targets) == 1:
        primary.append(group[0])
    else:
        primary.append(group[0])
        alt = ' | '.join('%s [%s %s]' % (t, info[d[4]]['nation_zh'], info[d[4]]['ship_type_zh']) for t, d in targets.items())
        alternates.append((src, alt))

seen, main_rows = set(), []
for src, tgt, tl, sl, *_ in sorted(primary, key=lambda r: (r[3], r[0].lower(), r[1])):
    if (src, tgt, tl) not in seen:
        seen.add((src, tgt, tl))
        main_rows.append((src, tgt, tl))

alt_note = dict(alternates)


def write_csv(path, header, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)
    os.replace(tmp, path)


write_csv(os.path.join(CN, 'azur_lane_ship_character_glossary.csv'),
          ['source', 'target', 'tgt_lng'], main_rows)

detail_rows, seen_d = [], set()
for src, tgt, tl, sl, sid, stype, nation, variant, std, harm in sorted(
        detailed, key=lambda r: (r[3], r[0].lower(), r[1])):
    if (src, tgt, tl) in seen_d:
        continue
    seen_d.add((src, tgt, tl))
    detail_rows.append((src, tgt, tl, sl, sid, stype, nation, variant, std, harm,
                        alt_note.get(src, '')))
write_csv(os.path.join(CN, 'azur_lane_ship_character_glossary_detailed.csv'),
          ['source', 'target', 'tgt_lng', 'src_lng', 'ship_id', 'ship_type', 'nation',
           'variant', 'zh_CN_standard', 'zh_CN_target', 'same_source_alternatives'],
          detail_rows)

print('shipgirls in termbase      :', len({r[4] for r in detail_rows}))
print('shipgirls with a harmonised target:', changed)
print('rows (main)                :', len(main_rows))
print('rows (detailed)            :', len(detail_rows))
print('source strings with more than one reading:', len(alt_note))
for a in list(alt_note.items())[:10]:
    print('   ', a[0], '->', a[1])




