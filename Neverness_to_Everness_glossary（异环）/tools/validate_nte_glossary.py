#!/usr/bin/env python3
"""Validate generated NTE CSV files and cross-check sampled strings."""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path(r"E:\Download\BT\Codex_input\nte_upstream\NTE_Assets")
LANGS = {
    "en-US": "Localization/en/game.json",
    "zh-CN": "Localization/zh-CN/game.json",
    "zh-TW": "Localization/zh-Hant/game.json",
    "ja-JP": "Localization/ja/game.json",
    "ko-KR": "Localization/ko/game.json",
    "de-DE": "Localization/de/game.json",
    "fr-FR": "Localization/fr/game.json",
    "es-ES": "Localization/es/game.json",
    "ru-RU": "Localization/ru/game.json",
}
CATEGORIES = (
    "characters",
    "skills",
    "weapons",
    "equipment",
    "combat",
    "buffs",
    "specials",
    "quests",
    "dungeons",
    "regions",
    "factions",
    "enemies",
    "npcs",
    "items",
    "vehicles",
    "furniture",
    "achievements",
    "terms",
    "story",
    "ui",
    "system",
)
BAD_PATTERNS = (
    "<",
    ">",
    "$undefined",
    "undefined",
    "<!>",
    "{0}",
    "{1}",
    "{PlayerName}",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--glossary", type=Path, default=ROOT / "nte-glossary")
    parser.add_argument("--assets-root", type=Path, default=DEFAULT_ASSETS)
    parser.add_argument("--sample-per-category", type=int, default=12)
    return parser.parse_args()


def collect_values(assets_root: Path) -> dict[str, set[str]]:
    values: dict[str, set[str]] = {}
    for lang, relpath in LANGS.items():
        data = json.loads((assets_root / relpath).read_text(encoding="utf-8"))
        rows: set[str] = set()
        for table in data.values():
            if not isinstance(table, dict):
                continue
            for value in table.values():
                text = html.unescape(str(value))
                text = re.sub(r"<[^>]+>", "", text)
                text = re.sub(r"\s+", " ", text).strip()
                if text:
                    rows.add(text)
        values[lang] = rows
    return values


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    source_targets: dict[tuple[str, str], set[str]] = defaultdict(set)
    category_rows: dict[str, int] = {}
    total_rows = 0
    random.seed(20260927)
    source_values = collect_values(args.assets_root)

    for lang_dir in sorted(path for path in args.glossary.iterdir() if path.is_dir()):
        target_lang = lang_dir.name
        if target_lang not in LANGS:
            warnings.append(f"unexpected language directory: {target_lang}")
            continue
        present = {path.stem for path in lang_dir.glob("*.csv")}
        for category in CATEGORIES:
            if category not in present:
                errors.append(f"{lang_dir}: missing category {category}.csv")
        for csv_path in sorted(lang_dir.glob("*.csv")):
            category = csv_path.stem
            sampled = 0
            if csv_path.stat().st_size == 0:
                errors.append(f"{csv_path}: empty file")
                continue
            with csv_path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                header = next(reader, None)
                if header != ["source", "target", "tgt_lng"]:
                    errors.append(f"{csv_path}: invalid header {header!r}")
                    continue
                seen: set[tuple[str, str, str]] = set()
                for line_number, row in enumerate(reader, start=2):
                    if len(row) != 3:
                        errors.append(f"{csv_path}:{line_number}: expected 3 columns")
                        continue
                    source, target, row_lang = (part.strip() for part in row)
                    if not source or not target:
                        errors.append(f"{csv_path}:{line_number}: empty source/target")
                    if row_lang != target_lang:
                        errors.append(f"{csv_path}:{line_number}: tgt_lng={row_lang!r}")
                    if source == target:
                        errors.append(f"{csv_path}:{line_number}: source equals target")
                    if any(pattern in source or pattern in target for pattern in BAD_PATTERNS):
                        errors.append(f"{csv_path}:{line_number}: forbidden markup or placeholder")
                    triple = (source, target, row_lang)
                    if triple in seen:
                        errors.append(f"{csv_path}:{line_number}: duplicate row")
                    seen.add(triple)
                    source_targets[(target_lang, source)].add(target)
                    total_rows += 1
                    if sampled < args.sample_per_category:
                        if source not in source_values.get("en-US", set()) and not any(
                            source in values for values in source_values.values()
                        ):
                            errors.append(f"{csv_path}:{line_number}: source not found in game data")
                        if target not in source_values[target_lang]:
                            errors.append(f"{csv_path}:{line_number}: target not found in {target_lang} game data")
                        sampled += 1
            if len(seen) == 0:
                errors.append(f"{csv_path}: no data rows")
            category_rows[category] = category_rows.get(category, 0) + len(seen)

    conflicts = {
        f"{target_lang}\t{source}": sorted(targets)
        for (target_lang, source), targets in source_targets.items()
        if len(targets) > 1
    }
    report = {
        "total_rows": total_rows,
        "category_rows": category_rows,
        "errors": errors,
        "warnings": warnings,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
    }
    report_path = ROOT / "tools" / "_validation.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"rows={total_rows} errors={len(errors)} warnings={len(warnings)} conflicts={len(conflicts)}")
    if errors:
        for error in errors[:30]:
            print("ERROR", error)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
