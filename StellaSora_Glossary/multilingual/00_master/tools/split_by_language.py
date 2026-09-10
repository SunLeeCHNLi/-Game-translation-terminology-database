# -*- coding: utf-8 -*-
"""Regenerate the per-target-language termbases with duplicate-pair removal."""
import csv, os

ROOT = r"E:\Download\BT\Codex_input\StellaSora_Glossary"
MULTI = os.path.join(ROOT, "multilingual")
LANGS = ["zh-CN", "en-US", "ja-JP", "ko-KR", "zh-TW"]
CATS = [
    ("01_character", "角色名称"), ("02_skill", "技能名称"), ("03_potential", "潜能名称"),
    ("04_disc", "唱片 / Disc"), ("05_item", "道具"), ("06_equipment", "装备"),
    ("07_enemy", "敌人"), ("08_stage", "关卡"), ("09_event", "活动"),
    ("10_system", "系统术语"), ("11_ui", "UI术语"), ("12_story", "剧情专有名词"),
    ("13_faction", "阵营"), ("14_location", "地点"), ("15_terminology", "游戏机制术语"),
]

tables = {}
for cat, label in CATS:
    with open(os.path.join(MULTI, cat, cat + "_terms.csv"), encoding="utf-8-sig") as f:
        tables[cat] = list(csv.DictReader(f))

summary = {}
for lang in LANGS:
    lang_dir = os.path.join(ROOT, lang)
    counts, all_g, all_t = {}, [], []
    for cat, label in CATS:
        d = os.path.join(lang_dir, cat)
        os.makedirs(d, exist_ok=True)
        n_terms, n_pairs = 0, 0
        seen_pairs = set()
        with open(os.path.join(d, cat + "_glossary.csv"), "w", encoding="utf-8-sig", newline="") as gf, \
             open(os.path.join(d, cat + "_terms.csv"), "w", encoding="utf-8-sig", newline="") as tf:
            gw = csv.writer(gf); tw = csv.writer(tf)
            gw.writerow(["source", "target", "tgt_lng"])
            tw.writerow(["id", "term", "src_table"])
            for r in tables[cat]:
                tgt = r[lang]
                if not tgt:
                    continue
                n_terms += 1
                tw.writerow([r["id"], tgt, r["src_table"]])
                all_t.append([cat, label, r["id"], tgt, r["src_table"]])
                emitted = set()
                for s in LANGS:
                    if s == lang:
                        continue
                    srcv = r[s]
                    if not srcv or srcv == tgt or srcv in emitted:
                        continue
                    if (srcv, tgt) in seen_pairs:
                        continue
                    seen_pairs.add((srcv, tgt))
                    emitted.add(srcv)
                    gw.writerow([srcv, tgt, lang])
                    all_g.append([cat, srcv, tgt, lang])
                    n_pairs += 1
        counts[cat] = n_terms
    md = os.path.join(lang_dir, "00_master")
    os.makedirs(md, exist_ok=True)
    with open(os.path.join(md, "all_glossary.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(["category", "source", "target", "tgt_lng"]); w.writerows(all_g)
    with open(os.path.join(md, "all_terms.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(["category", "category_label", "id", "term", "src_table"]); w.writerows(all_t)
    with open(os.path.join(md, "index.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["category", "label", "term_count", "glossary_file", "terms_file", "target_language"])
        for cat, label in CATS:
            w.writerow([cat, label, counts[cat], "%s/%s_glossary.csv" % (cat, cat),
                        "%s/%s_terms.csv" % (cat, cat), lang])
        w.writerow(["TOTAL", "", sum(counts.values()), "", "", lang])
    summary[lang] = {"terms": sum(counts.values()), "rows": len(all_g), "counts": counts}
    print("%-6s terms=%-6d pairs=%d" % (lang, sum(counts.values()), len(all_g)))

import json
open(os.path.join(ROOT, "_summary.json"), "w", encoding="utf-8").write(json.dumps(summary, ensure_ascii=False))
