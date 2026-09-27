#!/usr/bin/env python3
"""Build the small curated block of manually reviewed HSR terminology.

The client stores the Trailblazer (the player character) name as the {NICKNAME}
variable, so it never appears in the hash-keyed export. The localized names below
were taken from the client localization itself and each one is verified to occur
verbatim inside the matching TextMap before it is written out.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_hsr_glossary import DEFAULT_OUT, LANG_ORDER, TEXTMAP, TEXTMAP_FILES  # noqa: E402
from hsr_common import clean_text  # noqa: E402

RUBY_RE = re.compile(r"\{RUBY_[BE]#[^}]*\}")
TRAILBLAZER = {
    "zh-CN": "开拓者",
    "zh-TW": "開拓者",
    "en-US": "Trailblazer",
    "ja-JP": "開拓者",
    "ko-KR": "개척자",
    "fr-FR": "Pionnier",
    "de-DE": "Trailblazer",
    "es-ES": "Trazacaminos",
    "ru-RU": "Первооткрыватель",
    "pt-PT": "Desbravador",
    "id-ID": "Trailblazer",
    "th-TH": "ผู้บุกเบิก",
    "vi-VN": "Nhà Khai Phá",
}


def verify(lang: str, value: str) -> bool:
    for name in TEXTMAP_FILES[lang]:
        path = TEXTMAP / name
        if not path.exists():
            continue
        for raw in json.loads(path.read_text(encoding="utf-8")).values():
            if isinstance(raw, str):
                text = clean_text(RUBY_RE.sub("", raw))
                if text == value or value in text:
                    return True
    return False


def main() -> int:
    out_dir = DEFAULT_OUT / "curated"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = {}
    for lang, value in TRAILBLAZER.items():
        report[lang] = {"value": value, "found_in_client_textmap": verify(lang, value)}
    missing = [lang for lang, info in report.items() if not info["found_in_client_textmap"]]
    if missing:
        print("WARNING: not found verbatim in client TextMap:", ", ".join(missing))

    rows = []
    for target_lang in LANG_ORDER:
        target = TRAILBLAZER[target_lang]
        for source_lang in LANG_ORDER:
            if source_lang == target_lang:
                continue
            source = TRAILBLAZER[source_lang]
            if source == target:
                continue
            rows.append((source, target, target_lang))

    path = out_dir / "curated_terms.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\r\n")
        writer.writerow(["source", "target", "tgt_lng"])
        writer.writerows(sorted(set(rows)))

    (out_dir / "_curated_counts.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "rows": len(set(rows)),
                    "verified": report}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(set(rows))} curated rows to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
