#!/usr/bin/env python3
"""Round-2 spot check: verify known official pairs and sample every category."""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "hsr-glossary"

CHECKS = [
    ("01_character", "March 7th", "三月七"),
    ("01_character", "Kafka", "卡芙卡"),
    ("01_character", "Dan Heng", "丹恒"),
    ("02_path", "Destruction", "毁灭"),
    ("02_path", "The Hunt", "巡猎"),
    ("02_path", "Erudition", "智识"),
    ("02_path", "Harmony", "同谐"),
    ("02_path", "Nihility", "虚无"),
    ("02_path", "Preservation", "存护"),
    ("02_path", "Abundance", "丰饶"),
    ("03_element", "Physical", "物理"),
    ("03_element", "Fire", "火"),
    ("03_element", "Ice", "冰"),
    ("03_element", "Lightning", "雷"),
    ("03_element", "Wind", "风"),
    ("03_element", "Quantum", "量子"),
    ("03_element", "Imaginary", "虚数"),
    ("12_location", "Herta Space Station", "空间站「黑塔」"),
    ("12_location", "Jarilo-VI", "雅利洛-Ⅵ"),
    ("12_location", "Xianzhou Luofu", "仙舟「罗浮」"),
    ("12_location", "Penacony", "匹诺康尼"),
    ("12_location", "Amphoreus", "翁法罗斯"),
    ("18_simulated_universe", "Simulated Universe", "模拟宇宙"),
    ("21_world_lore", '"Abundance" — Yaoshi', "「丰饶」，药师"),
]


def load(category: str):
    rows = []
    path = ROOT / "zh-CN" / f"{category}.csv"
    if not path.exists():
        return rows
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        rows.extend(reader)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", type=int, default=5)
    args = parser.parse_args()

    failures = []
    for category, source, target in CHECKS:
        rows = load(category)
        found = any(r[0] == source and r[1] == target for r in rows)
        print(f"[{'OK ' if found else 'MISS'}] {category}: {source} -> {target}")
        if not found:
            alt = [r for r in rows if r[1] == target][:2]
            failures.append((category, source, target, alt))

    curated = ROOT / "curated" / "curated_terms.csv"
    if curated.exists():
        with curated.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))[1:]
        found = any(r[0] == "Trailblazer" and r[1] == "开拓者" and r[2] == "zh-CN" for r in rows)
        print(f"[{'OK ' if found else 'MISS'}] curated: Trailblazer -> 开拓者 (zh-CN)")
        if not found:
            failures.append(("curated", "Trailblazer", "开拓者", []))

    print()
    rng = random.Random(20260927)
    for path in sorted((ROOT / "zh-CN").glob("*.csv")):
        rows = load(path.stem)
        if not rows:
            continue
        picks = rng.sample(rows, min(args.sample, len(rows)))
        print(f"--- {path.stem} ({len(rows):,} rows)")
        for source, target, _ in picks:
            print(f"    {source[:70]}  =>  {target[:70]}")

    print()
    print("SPOT CHECK FAILURES:", len(failures))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
