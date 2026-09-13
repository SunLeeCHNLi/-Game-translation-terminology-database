"""Build the Wuthering Waves multilingual glossary from datamined text maps.

Output layout (one folder per target language, one CSV per category):

    <--out>/                       # repository copy: wuwa-glossary/
    |-- zh-CN/characters.csv
    |-- zh-CN/items.csv
    |-- ...
    `-- th-TH/...

The per-language/category counts report is written next to this script so the
repository copy lives at ``tools/_counts.json`` (override with ``--counts``);
without ``--counts`` it falls back to ``<--out>/_counts.json``.

Every CSV uses the shared ``source,target,tgt_lng`` schema: for the target
language each entry is emitted once per *other* language carrying the same text
key, so the files plug straight into translation-memory / term-matching tools.

Line-by-line story dialogue is classified as ``dialogue`` and left out by
default (it dwarfs every other category); pass ``--with-dialogue`` to emit it.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wuwa_classify import classify  # noqa: E402
from wuwa_config import (  # noqa: E402
    CATEGORIES,
    DEFAULT_MAX_LEN,
    LANGS,
    MAX_LEN,
    config_key_map,
    load_multitext,
    normalize_text,
)

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(TOOLS_DIR, "_cfgmap_cache.pkl")

# The repository's metadata copy lives beside the scripts, not inside the
# glossary output tree (it was moved from wuwa-glossary/ to tools/ together
# with the build scripts).
DEFAULT_COUNTS = os.path.join(TOOLS_DIR, "_counts.json")


def write_csv(path: str, rows, code: str) -> int:
    with open(path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh, lineterminator="\r\n", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["source", "target", "tgt_lng"])
        for src, tgt in rows:
            writer.writerow([src, tgt, code])
    return os.path.getsize(path)


def collect_rows(keys, target_code, maps):
    rows = set()
    for key in keys:
        target = maps[target_code].get(key)
        if not target:
            continue
        for src_code, src_map in maps.items():
            if src_code == target_code:
                continue
            src = src_map.get(key)
            if src and src != target:
                rows.add((src, target))
    return sorted(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="output glossary root")
    parser.add_argument("--counts", default=DEFAULT_COUNTS,
                        help="where to write the counts report "
                             "(default: tools/_counts.json next to this script)")
    parser.add_argument("--with-dialogue", action="store_true",
                        help="also emit the dialogue category (very large)")
    parser.add_argument("--rebuild-cache", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", default="",
                        help="comma separated category slugs to build (default: all)")
    parser.add_argument("--len-scale", type=float, default=1.0,
                        help="multiply every per-category length cap (<1 = smaller output)")
    args = parser.parse_args()

    started = time.time()
    print("scanning data tables for text keys ...", flush=True)
    refs = config_key_map(CACHE, rebuild=args.rebuild_cache)
    print(f"  {len(refs)} text keys referenced by tables", flush=True)

    print("loading text maps ...", flush=True)
    raw = {}
    for game_lang, code, _ in LANGS:
        raw[code] = load_multitext(game_lang)
    print(f"  {len(raw)} languages, {len(raw['en-US'])} keys each", flush=True)

    skip = {"dialogue"} if not args.with_dialogue else set()
    if args.only:
        wanted = {c.strip() for c in args.only.split(",") if c.strip()}
        skip |= {slug for slug, _ in CATEGORIES if slug not in wanted}
    keep: dict[str, str] = {}
    for key, value in raw["zh-CN"].items():
        if not value or not value.strip():
            continue
        if not any(m.get(key) for m in raw.values()):
            continue
        category = classify(key, refs.get(key, []))
        if category in skip:
            continue
        limit = int(MAX_LEN.get(category, DEFAULT_MAX_LEN) * args.len_scale)
        longest = 0
        for lang_map in raw.values():
            other_value = lang_map.get(key)
            if other_value:
                longest = max(longest, len(normalize_text(other_value)))
                if longest > limit:
                    break
        if longest > limit:
            continue
        keep[key] = category

    keep_set = set(keep)
    maps = {}
    for code in list(raw):
        maps[code] = {}
        for key, value in raw[code].items():
            if key in keep_set and value:
                text = normalize_text(value)
                if text:
                    maps[code][key] = text
        del raw[code]
    del raw

    print("writing rows ...", flush=True)
    report = []
    total_bytes = 0
    for _, code, native in LANGS:
        per_category = {}
        language_rows = 0
        language_bytes = 0
        for slug, _label in CATEGORIES:
            if slug in skip:
                continue
            keys = [k for k, c in keep.items() if c == slug]
            if not keys:
                continue
            rows = collect_rows(keys, code, maps)
            if not rows:
                continue
            per_category[slug] = len(rows)
            language_rows += len(rows)
            if not args.dry_run:
                path = os.path.join(args.out, code, slug + ".csv")
                os.makedirs(os.path.dirname(path), exist_ok=True)
                language_bytes += write_csv(path, rows, code)
        total_bytes += language_bytes
        report.append({
            "code": code,
            "language": native,
            "categories": per_category,
            "rows": language_rows,
            "bytes": language_bytes,
        })
        suffix = "" if args.dry_run else f"  {language_bytes / 1048576:7.1f} MiB"
        print(f"  {code:6s} {language_rows:9d} rows{suffix}", flush=True)

    concepts = {slug: sum(1 for c in keep.values() if c == slug) for slug, _ in CATEGORIES}
    print("\nentries per category:")
    for slug, label in CATEGORIES:
        if concepts.get(slug):
            print(f"  {slug:16s} {concepts[slug]:7d}  {label}")

    if not args.dry_run:
        payload = {
            "generated": time.strftime("%Y-%m-%d"),
            "sources": {
                "text": "Arikatsu/WutheringWaves_Data Textmaps/<lang>/multi_text/MultiText.json (game 3.6.0)",
                "backfill": "Dimbreath/WutheringData TextMap/<lang>/MultiText.json (game 3.1.0)",
                "categories": "Arikatsu/WutheringWaves_Data BinData + Dimbreath/WutheringData ConfigDB",
            },
            "with_dialogue": args.with_dialogue,
            "languages": report,
            "concepts": concepts,
        }
        counts_path = args.counts or os.path.join(args.out, "_counts.json")
        counts_dir = os.path.dirname(os.path.abspath(counts_path))
        if counts_dir:
            os.makedirs(counts_dir, exist_ok=True)
        with open(counts_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"counts report: {counts_path}")
        print(f"\ntotal written: {total_bytes / 1048576:.1f} MiB")
    print(f"done in {time.time() - started:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
