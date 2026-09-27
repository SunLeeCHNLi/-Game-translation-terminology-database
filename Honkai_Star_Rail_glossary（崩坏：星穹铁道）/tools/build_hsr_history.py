#!/usr/bin/env python3
"""Collect legacy (renamed) Honkai: Star Rail terminology.

Compares the current StarRailRes index (4.5.0) with two older structured sources:

* StarRailStaticAPI 2.3.0  (2024-07-05)
* nathacks/HSR-Mapping-DATA 4.0 (2026-07-17)

Only entries whose id matches but whose name changed are written, so historical
names stay reproducible instead of being mixed into the live glossary.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from datetime import date
from pathlib import Path

DATA_ROOT = Path(r"E:\Download\BT\Codex_input")
CURRENT_ROOT = DATA_ROOT / "StarRailRes" / "index_min"
LEGACY_SOURCES = [
    {
        "label": "StarRailStaticAPI 2.3.0",
        "version": "2.3.0",
        "commit": "e039e51",
        "root": DATA_ROOT / "StarRailStaticAPI" / "db",
        "langs": {"zh-CN": "cn", "zh-TW": "cht", "en-US": "en", "ja-JP": "jp", "ko-KR": "kr",
                  "fr-FR": "fr", "de-DE": "de", "es-ES": "es", "ru-RU": "ru", "pt-PT": "pt",
                  "id-ID": "id", "th-TH": "th", "vi-VN": "vi"},
    },
    {
        "label": "HSR-Mapping-DATA 4.0",
        "version": "4.0.0",
        "commit": "245f286",
        "root": DATA_ROOT / "HSR-Mapping-DATA" / "output" / "index_new",
        "langs": {"zh-CN": "chs", "zh-TW": "cht", "en-US": "en", "ja-JP": "jp", "ko-KR": "kr",
                  "fr-FR": "fr", "de-DE": "de", "es-ES": "es", "ru-RU": "ru", "pt-PT": "pt",
                  "id-ID": "id", "th-TH": "th", "vi-VN": "vi"},
    },
]

CURRENT_LANGS = {"zh-CN": "cn", "zh-TW": "cht", "en-US": "en", "ja-JP": "jp", "ko-KR": "kr",
                 "fr-FR": "fr", "de-DE": "de", "es-ES": "es", "ru-RU": "ru", "pt-PT": "pt",
                 "id-ID": "id", "th-TH": "th", "vi-VN": "vi"}

FILES = [
    "characters.json",
    "light_cones.json",
    "relic_sets.json",
    "relics.json",
    "simulated_curios.json",
    "simulated_blessings.json",
    "simulated_events.json",
    "paths.json",
    "elements.json",
    "achievements.json",
]
NAME_FIELDS = ("name", "title")

_RUBY_RE = re.compile(r"\{RUBY_[BE]#[^}]*\}")
_TAG_RE = re.compile(r"<[^>]*>")
_QUOTES = "\"\u201c\u201d\u2018\u2019\u300c\u300d"


def normalize(value: str) -> str:
    """Strip markup/furigana so only genuine wording changes are reported."""
    if not value:
        return ""
    text = _TAG_RE.sub("", value)
    text = _RUBY_RE.sub("", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.strip(_QUOTES).strip()


def load(path: Path):
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload if isinstance(payload, dict) else {}


def name_of(record) -> str:
    if not isinstance(record, dict):
        return ""
    for field in NAME_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            return normalize(value)
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path,
                        default=Path(__file__).resolve().parents[1] / "hsr-glossary" / "historical")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows: list[tuple[str, str, str]] = []
    stats: dict[str, dict[str, int]] = {}

    for source in LEGACY_SOURCES:
        source_rows = 0
        stats[source["label"]] = {}
        for lang, legacy_dir in source["langs"].items():
            current_dir = CURRENT_LANGS[lang]
            lang_rows = 0
            for filename in FILES:
                legacy = load(source["root"] / legacy_dir / filename)
                current = load(CURRENT_ROOT / current_dir / filename)
                if not legacy or not current:
                    continue
                for entity_id, record in legacy.items():
                    old = name_of(record)
                    new = name_of(current.get(entity_id))
                    if old and new and old != new:
                        rows.append((old, new, lang))
                        lang_rows += 1
            stats[source["label"]][lang] = lang_rows
            source_rows += lang_rows
        stats[source["label"]]["total"] = source_rows

    seen: set[tuple[str, str, str]] = set()
    unique: list[tuple[str, str, str]] = []
    for row in rows:
        if row in seen:
            continue
        seen.add(row)
        unique.append(row)
    unique.sort()

    out_file = args.out / "historical_names.csv"
    with out_file.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\r\n")
        writer.writerow(["source", "target", "tgt_lng"])
        writer.writerows(unique)

    meta = {
        "generated": date.today().isoformat(),
        "current_source": "StarRailRes index_min 4.5.0 (commit d226bef)",
        "sources": {k: v for k, v in stats.items()},
        "rows": len(unique),
        "raw_rows": len(rows),
    }
    (args.out / "_history_counts.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
