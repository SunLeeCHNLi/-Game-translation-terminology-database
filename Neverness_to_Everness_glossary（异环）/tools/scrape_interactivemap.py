#!/usr/bin/env python3
"""Download named NTE entities from InteractiveMap's public database pages.

InteractiveMap embeds server-rendered records in Next.js flight payloads. Raw
HTML and intermediate records stay in the external work area; only the builder
outputs are intended for the Git repository.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://interactivemap.app/neverness-to-everness/database"
DEFAULT_CACHE = Path(r"E:\Download\BT\Codex_input\nte_cache\interactivemap")

LOCALES = {
    "en": "en-US",
    "es": "es-ES",
    "de": "de-DE",
    "fr": "fr-FR",
    "ja": "ja-JP",
    "ko": "ko-KR",
    "ru": "ru-RU",
    "zh-Hans": "zh-CN",
    "zh-Hant": "zh-TW",
}

CATEGORIES = (
    "espers",
    "arcs",
    "cartridges",
    "modules",
    "groups",
    "monsters",
    "bosses",
    "quests",
    "vehicles",
    "furniture",
    "properties",
    "items",
    "achievements",
    "cycles",
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/142.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

PUSH_RE = re.compile(
    r"self\.__next_f\.push\(\[1,(\"(?:[^\"\\]|\\.)*\")\]\)</script>"
)
SLUG_RE = re.compile(r'"slug"\s*:\s*"')


def flight_payload(html: str) -> str:
    chunks = [json.loads(match.group(1)) for match in PUSH_RE.finditer(html)]
    if not chunks:
        raise ValueError("no Next.js flight payload found")
    return "".join(chunks)


def find_object_end(text: str, start: int) -> int | None:
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index + 1
    return None


def extract_records(payload: str) -> list[dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for match in SLUG_RE.finditer(payload):
        start = payload.rfind("{", 0, match.start())
        if start < 0:
            continue
        end = find_object_end(payload, start)
        if end is None:
            continue
        try:
            obj = json.loads(payload[start:end])
        except json.JSONDecodeError:
            continue
        slug = obj.get("slug")
        name = obj.get("name")
        if not isinstance(slug, str) or not isinstance(name, str):
            continue
        name = name.strip()
        if not name or name in {"$undefined", "undefined", "null"}:
            continue
        records.setdefault(slug.strip(), obj)
    return list(records.values())


def extract_dicts(payload: str) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for match in re.finditer(r'"dict"\s*:\s*\{', payload):
        start = payload.find("{", match.start())
        end = find_object_end(payload, start)
        if end is None:
            continue
        try:
            obj = json.loads(payload[start:end])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            merged.update(obj)
    return merged


def fetch(url: str, path: Path, refresh: bool, delay: float) -> str:
    if path.exists() and not refresh and path.stat().st_size > 0:
        return path.read_text(encoding="utf-8")
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=60) as response:
        body = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    time.sleep(delay)
    return body.decode("utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--langs", default="all", help="comma-separated page locales or all")
    parser.add_argument("--categories", default="all", help="comma-separated categories or all")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--delay", type=float, default=0.35)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    locales = list(LOCALES) if args.langs == "all" else args.langs.split(",")
    categories = list(CATEGORIES) if args.categories == "all" else args.categories.split(",")
    datasets: dict[str, dict[str, list[dict[str, Any]]]] = {}
    dicts: dict[str, dict[str, dict[str, Any]]] = {}
    for locale in locales:
        if locale not in LOCALES:
            raise SystemExit(f"unknown locale: {locale}")
        datasets[locale] = {}
        dicts[locale] = {}
        for category in categories:
            if category not in CATEGORIES:
                raise SystemExit(f"unknown category: {category}")
            url = f"{BASE_URL}/{locale}/{category}/"
            html_path = args.cache / "html" / locale / f"{category}.html"
            html = fetch(url, html_path, args.refresh, args.delay)
            try:
                payload = flight_payload(html)
                records = extract_records(payload)
                locale_dict = extract_dicts(payload)
            except Exception as exc:
                raise RuntimeError(f"failed to parse {url}: {exc}") from exc
            datasets[locale][category] = records
            dicts[locale][category] = locale_dict
            print(f"{locale:8} {category:12} {len(records):5}")
    out = args.cache / "records.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(
            {
                "source": f"{BASE_URL}/",
                "locales": LOCALES,
                "categories": list(CATEGORIES),
                "datasets": datasets,
                "dicts": dicts,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
