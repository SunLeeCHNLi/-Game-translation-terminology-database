# -*- coding: utf-8 -*-
"""Naval / military / game terminology as per-language termbases.

terms_data.TERMS stores one row per language for each concept
(``(src_lng, form, chinese_concept, category)``).  This script pivots that table so
that every target language gets its own termbase: ``target`` holds the term in that
language, ``source`` holds the term in each of the other three.

Output, for the folders zh-CN / en-US / ja-JP / ko-KR:
    azur_lane_terms.csv           source,target,tgt_lng
    azur_lane_terms_detailed.csv  + src_lng, category, same-source alternatives
"""
import csv, io, os, sys
from collections import OrderedDict, defaultdict

from terms_data import TERMS, CATEGORY_ZH

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT = r'E:\Download\BT\Codex_input\AzurLane_Glossary'
# internal language key -> folder name / tgt_lng tag
TAGS = OrderedDict([('zh-CN', 'zh-CN'), ('en', 'en-US'), ('ja', 'ja-JP'), ('ko', 'ko-KR')])

# ---------------------------------------------------------------- concepts
concepts = OrderedDict()          # chinese concept -> {language key: [forms]}
category = {}
for lng, form, zh, cat in TERMS:
    slot = concepts.setdefault(zh, OrderedDict())
    slot.setdefault('zh-CN', [zh])          # the concept key *is* the Chinese term
    forms = slot.setdefault(lng, [])
    if form and form not in forms:
        forms.append(form)
    category.setdefault(zh, cat)
print('term concepts:', len(concepts))


def build(target_key):
    """Return (main rows, detailed rows) for one target language."""
    target_tag = TAGS[target_key]
    rows = []                                  # built in concept order
    for zh, forms in concepts.items():
        target = forms.get(target_key, [None])[0]
        if not target:
            continue                           # concept has no term in this language
        for lng, items in forms.items():
            if lng == target_key:
                continue
            for src in items:
                if not src or src == target:
                    continue
                rows.append((src, target, target_tag, TAGS[lng], zh, category[zh]))

    # One reading per source string: the earliest concept wins and is the row kept in
    # the three-column table; every other reading is listed in the detailed file, e.g.
    # Korean 대령 is both 海军上校 and 大佐（上校）.
    primary = OrderedDict()
    for r in rows:
        primary.setdefault(r[0], r)
    alt_note = {}
    by_source = defaultdict(OrderedDict)
    for r in rows:
        by_source[r[0]].setdefault(r[1], r)
    for src, readings in by_source.items():
        if len(readings) > 1:
            alt_note[src] = ' | '.join('%s [%s %s]' % (t, r[3], CATEGORY_ZH.get(r[5], r[5]))
                                       for t, r in readings.items())

    main = [(r[0], r[1], r[2]) for r in
            sorted(primary.values(), key=lambda r: (r[3], r[0].lower(), r[1]))]
    detail_rows, seen = [], set()
    for r in sorted(rows, key=lambda r: (r[3], r[0].lower(), r[1])):
        if (r[0], r[1], r[2]) in seen:
            continue
        seen.add((r[0], r[1], r[2]))
        detail_rows.append((r[0], r[1], r[2], r[3], r[5], CATEGORY_ZH.get(r[5], r[5]),
                            alt_note.get(r[0], '')))
    return main, detail_rows


def write_csv(path, header, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)
    os.replace(tmp, path)


DETAILED_HEADER = ['source', 'target', 'tgt_lng', 'src_lng', 'category', 'category_zh',
                   'same_source_alternatives']
for key, tag in TAGS.items():
    folder = os.path.join(OUT, tag)
    main, detail = build(key)
    write_csv(os.path.join(folder, 'azur_lane_terms.csv'), ['source', 'target', 'tgt_lng'], main)
    write_csv(os.path.join(folder, 'azur_lane_terms_detailed.csv'), DETAILED_HEADER, detail)
    print('  %-6s terms  main=%d detail=%d  ambiguous_sources=%d'
          % (tag, len(main), len(detail), sum(1 for d in detail if d[6]) // 2))
