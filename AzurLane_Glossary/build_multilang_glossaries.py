# -*- coding: utf-8 -*-
"""Target-language variants of the Azur Lane ship termbases.

For every target language (en-US / ja-JP / ko-KR) a termbase is produced in which
`target` holds the ship name in that language and `source` holds the ship name in
every other language, including the Simplified-Chinese standard name and (for the
harmonised family) the CN-server harmonised name.

Output layout:
    AzurLane_Glossary/<tag>/azur_lane_glossary.csv
    AzurLane_Glossary/<tag>/azur_lane_glossary_detailed.csv
    AzurLane_Glossary/<tag>/azur_lane_ship_character_glossary.csv
    AzurLane_Glossary/<tag>/azur_lane_ship_character_glossary_detailed.csv
"""
import csv, io, json, os, re, sys
from collections import OrderedDict, defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'E:\Download\BT\Codex_input\AzurLaneData-main\AzurLaneData-main'
OUT = r'E:\Download\BT\Codex_input\AzurLane_Glossary'
TARGETS = OrderedDict([('en-US', 'en'), ('ja-JP', 'ja'), ('ko-KR', 'ko')])

load = lambda p: json.load(open(p, encoding='utf-8-sig'))
clean = lambda v: ' '.join(v.replace('\u3000', ' ').split()).strip() if isinstance(v, str) else ''

# ---------------------------------------------------------------- harmonised names
nc = load(os.path.join(BASE, 'CN', 'ShareCfg', 'name_code.json'))
hmap = {}
for v in nc.values():
    if v.get('type') != 1:
        continue
    o, h = clean(v['name']), clean(v['code'])
    if o and h and o != h:
        hmap.setdefault(o, h)

SUFFIX = re.compile(r'^(?P<base>.*?)\s*[（(](?P<sfx>[^）)]*)[)）]$')


def harmonise(name):
    """Return the CN-server harmonised name, or '' when the ship is unchanged."""
    if name in hmap:
        return hmap[name]
    m = SUFFIX.match(name)
    if m and hmap.get(m.group('base')):
        return '%s（%s）' % (hmap[m.group('base')], m.group('sfx'))
    if name.endswith('改') and not name.endswith('.改'):
        return hmap.get(name[:-1] + '.改', '')
    if name.endswith('.改'):
        return hmap.get(name[:-2] + '改', '')
    return ''


# ---------------------------------------------------------------- ship table
rows_in = list(csv.DictReader(open(os.path.join(OUT, 'azur_lane_ship_names_multilingual.csv'),
                                  encoding='utf-8-sig')))
ships, by_id = [], {}
for r in rows_in:
    std = r['zh_CN']
    if not re.search(r'[0-9A-Za-z\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]', std):
        continue
    s = {
        'id': r['ship_id'], 'std': std, 'hx': harmonise(std),
        'en': clean(r['en']), 'en_full': clean(r['english_name']), 'ja': clean(r['ja']),
        'tw': clean(r['zh_TW']), 'ko': clean(r['ko']),
        'type_zh': r['ship_type_zh'], 'type_en': r['ship_type_en'],
        'nation_zh': r['nation_zh'], 'nation_en': r['nation_en'], 'variant': r['variant'],
    }
    ships.append(s)
    by_id[s['id']] = s
print('ship characters:', len(ships), '| with a harmonised CN name:',
      sum(1 for s in ships if s['hx']))

# (language tag, field) - every non-target language becomes a `source` reading.
# `std` is the plain zh-CN name, `hx` the CN-server harmonised name.
SOURCE_FIELDS = [('zh-TW', 'tw'), ('en-US', 'en'), ('en-US', 'en_full'),
                 ('ja-JP', 'ja'), ('ko-KR', 'ko'), ('zh-CN', 'std'), ('zh-CN', 'hx')]
CN_FORMS = {'std': 'standard', 'hx': 'harmonised'}


def build(target_lang, target_field, harmonised_family):
    fields = SOURCE_FIELDS[:5] + ([('zh-CN', 'std'), ('zh-CN', 'hx')] if harmonised_family
                                  else [('zh-CN', 'std')])
    rows = []
    for s in ships:
        target = s[target_field]
        if not target:
            continue
        seen = set()
        for lang, key in fields:
            if lang == target_lang:
                continue
            src = s[key]
            if not src or src == target or (src, lang) in seen:
                continue
            seen.add((src, lang))
            rows.append((src, target, target_lang, lang, s['id'], key))

    # one reading per source string: the lowest ship id wins, the rest are recorded
    by_source = defaultdict(list)
    for r in rows:
        by_source[r[0]].append(r)
    primary, alt_note = [], {}
    for src, group in by_source.items():
        group.sort(key=lambda r: int(r[4]))
        targets = OrderedDict()
        for r in group:
            targets.setdefault(r[1], r)
        primary.append(group[0])
        if len(targets) > 1:
            alt_note[src] = ' | '.join(
                '%s [%s %s]' % (t, by_id[d[4]]['nation_zh'], by_id[d[4]]['type_zh'])
                for t, d in targets.items())

    main_rows, seen_m = [], set()
    for src, tgt, tl, sl, sid, key in sorted(primary, key=lambda r: (r[3], r[0].lower())):
        if (src, tgt, tl) not in seen_m:
            seen_m.add((src, tgt, tl))
            main_rows.append((src, tgt, tl))

    detail_rows, seen_d = [], set()
    for src, tgt, tl, sl, sid, key in sorted(rows, key=lambda r: (r[3], r[0].lower())):
        if (src, tgt, tl) in seen_d:
            continue
        seen_d.add((src, tgt, tl))
        s = by_id[sid]
        detail_rows.append((src, tgt, tl, sl, sid, s['type_zh'], s['type_en'], s['nation_zh'],
                            s['nation_en'], s['variant'], CN_FORMS.get(key, ''), s['std'],
                            s['hx'], alt_note.get(src, '')))
    return main_rows, detail_rows


def write_csv(path, header, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)
    os.replace(tmp, path)


STD_HEADER = ['source', 'target', 'tgt_lng', 'src_lng', 'ship_id', 'ship_type_zh',
              'ship_type_en', 'nation_zh', 'nation_en', 'variant', 'zh_CN_form',
              'zh_CN_standard', 'zh_CN_harmonised', 'same_source_alternatives']
summary = []
for tag, field in TARGETS.items():
    folder = os.path.join(OUT, tag)
    for family, harmonised in (('glossary', False), ('ship_character_glossary', True)):
        main, detail = build(tag, field, harmonised)
        write_csv(os.path.join(folder, 'azur_lane_%s.csv' % family), ['source', 'target', 'tgt_lng'], main)
        write_csv(os.path.join(folder, 'azur_lane_%s_detailed.csv' % family), STD_HEADER, detail)
        summary.append((tag, family, len(main), len(detail)))

for t in summary:
    print('  %-6s %-26s main=%d detail=%d' % t)
