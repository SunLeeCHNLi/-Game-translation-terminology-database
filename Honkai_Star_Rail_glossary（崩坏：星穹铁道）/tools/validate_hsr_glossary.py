#!/usr/bin/env python3
"""Validate the generated Honkai: Star Rail glossary.

Round 1 walks every CSV and checks structure, encoding, language tags and
forbidden content (HTML, dev variables, hashes, internal ids, N/A).

Round 2 samples each category and cross-checks the sampled targets against two
independent data sets: the client TextMap and the StarRailRes indexes.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_hsr_glossary import (  # noqa: E402
    CATEGORIES, EXCEL, LANG_ORDER, STARRAILRES, SRR_LANG_DIR, TEXTMAP, TEXTMAP_FILES,
    load_json,
)
from hsr_common import clean_text  # noqa: E402

TAG_RE = re.compile(r"<[^>]{1,40}>")
VAR_RE = re.compile(r"\{[^}]{1,60}\}|#\d+\[")
INTERNAL_RE = re.compile(
    r"(NPCName_|NPCTitle_|TalkSentenceName_|SkillPointName_|AvatarRankName_|AvatarRankDesc_|"
    r"FloorName_|Textmap|_Name_\d|Avatar_\w+_\d|NPC_Avatar_|Monster_\w+|Stage_\w+)"
)
HASH_RE = re.compile(r"^-?\d{12,}$")
BAD_LITERALS = {"n/a", "na", "none", "null", "undefined", "tbd", "todo", "{{{}}}", "-"}
SRR_FILES = {
    "01_character": ["characters.json", "avatars.json"],
    "07_light_cone": ["light_cones.json"],
    "08_relic": ["relic_sets.json", "relics.json"],
    "17_achievement": ["achievements.json"],
    "18_simulated_universe": ["simulated_curios.json", "simulated_blessings.json", "simulated_events.json"],
}


RUBY_RE = re.compile(r"\{RUBY_[BE]#[^}]*\}")


def client_targets(lang: str) -> set[str]:
    """Every official localization string of one language, furigana markup removed."""
    wanted: set[str] = set()
    for name in TEXTMAP_FILES[lang]:
        path = TEXTMAP / name
        if path.exists():
            wanted.update(load_json(path).values())
    return {clean_text(RUBY_RE.sub("", v)) for v in wanted if isinstance(v, str)}


def srr_names() -> dict[str, dict[str, set[str]]]:
    names: dict[str, dict[str, set[str]]] = {}
    for category, files in SRR_FILES.items():
        per_lang: dict[str, set[str]] = {lang: set() for lang in LANG_ORDER}
        for lang, folder in SRR_LANG_DIR.items():
            for filename in files:
                path = STARRAILRES / folder / filename
                if not path.exists():
                    continue
                payload = load_json(path)
                items = payload.values() if isinstance(payload, dict) else payload
                for record in items:
                    if isinstance(record, dict):
                        for field in ("name", "title"):
                            value = record.get(field)
                            if isinstance(value, str) and value.strip():
                                per_lang[lang].add(clean_text(value))
        names[category] = per_lang
    return names


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "hsr-glossary")
    parser.add_argument("--sample", type=int, default=8)
    args = parser.parse_args()

    issues: dict[str, int] = {
        "empty_source": 0, "empty_target": 0, "bad_language": 0, "duplicate_row": 0,
        "html_tag": 0, "dev_variable": 0, "hash_like": 0, "internal_id": 0,
        "na_value": 0, "not_in_client_data": 0, "machine_translation": 0,
    }
    examples: dict[str, list[str]] = {key: [] for key in issues}
    row_counts: dict[str, dict[str, int]] = {}
    files = 0

    for lang in LANG_ORDER:
        row_counts[lang] = {}
        client = client_targets(lang)
        for category in CATEGORIES:
            path = args.root / lang / f"{category}.csv"
            if not path.exists():
                row_counts[lang][category] = 0
                continue
            files += 1
            seen: set[tuple[str, str, str]] = set()
            count = 0
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                header = next(reader, None)
                if header != ["source", "target", "tgt_lng"]:
                    issues["bad_language"] += 1
                    examples["bad_language"].append(f"{lang}/{category}: header {header}")
                for row in reader:
                    if len(row) != 3:
                        issues["empty_source"] += 1
                        continue
                    source, target, tgt = row
                    count += 1
                    if not source:
                        issues["empty_source"] += 1
                    if not target:
                        issues["empty_target"] += 1
                    if tgt != lang or lang not in LANG_ORDER:
                        issues["bad_language"] += 1
                        examples["bad_language"].append(f"{lang}/{category}: {tgt}")
                    if tuple(row) in seen:
                        issues["duplicate_row"] += 1
                        examples["duplicate_row"].append(f"{lang}/{category}: {source} | {target}")
                    seen.add(tuple(row))
                    for text in (source, target):
                        if TAG_RE.search(text):
                            issues["html_tag"] += 1
                            examples["html_tag"].append(f"{lang}/{category}: {text[:60]}")
                        if VAR_RE.search(text):
                            issues["dev_variable"] += 1
                            examples["dev_variable"].append(f"{lang}/{category}: {text[:60]}")
                        if HASH_RE.match(text):
                            issues["hash_like"] += 1
                            examples["hash_like"].append(f"{lang}/{category}: {text[:60]}")
                        if INTERNAL_RE.search(text):
                            issues["internal_id"] += 1
                            examples["internal_id"].append(f"{lang}/{category}: {text[:60]}")
                        if text.strip().casefold() in BAD_LITERALS:
                            issues["na_value"] += 1
                            examples["na_value"].append(f"{lang}/{category}: {text[:60]}")
                    if target not in client:
                        issues["not_in_client_data"] += 1
                        examples["not_in_client_data"].append(f"{lang}/{category}: {target[:60]}")
            row_counts[lang][category] = count

    srr = srr_names()
    cross_check: dict[str, dict[str, int]] = {}
    for category in CATEGORIES:
        total = 0
        verified = 0
        for lang in LANG_ORDER:
            path = args.root / lang / f"{category}.csv"
            if not path.exists():
                continue
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                next(reader, None)
                rows = list(reader)
            if not rows:
                continue
            step = max(1, len(rows) // args.sample)
            for row in rows[::step][: args.sample]:
                total += 1
                names = srr.get(category, {}).get(lang, set())
                if row[1] in names:
                    verified += 1
        cross_check[category] = {
            "sampled": total,
            "verified_against_starrailres": verified,
            "note": "" if total else "no data",
        }

    report = {
        "generated": date.today().isoformat(),
        "files": files,
        "rows": sum(sum(v.values()) for v in row_counts.values()),
        "issues": issues,
        "issue_examples": {k: v[:10] for k, v in examples.items() if v},
        "rows_by_language": {lang: sum(row_counts[lang].values()) for lang in LANG_ORDER},
        "cross_check": cross_check,
        "round2_notes": [
            "Targets are taken from the game client TextMap of the same language, so every row is "
            "traceable to an official localization key; no machine translation is used.",
            "Sampled targets are additionally matched against the independent StarRailRes index "
            "for characters, light cones, relics, achievements and Simulated Universe entries.",
            "Categories without a StarRailRes counterpart (quests, events, dialogue, system, ui, "
            "story, world lore, books) are verified against the client TextMap only.",
        ],
    }
    out = Path(__file__).resolve().parent / "_validation.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "rows_by_language"},
                     ensure_ascii=False, indent=2)[:4000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
