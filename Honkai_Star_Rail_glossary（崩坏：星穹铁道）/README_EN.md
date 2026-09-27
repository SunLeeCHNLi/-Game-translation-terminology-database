# Honkai: Star Rail Multilingual Terminology Database

## [简体中文](README.md) ｜ [日本語](README_JP.md)

Client-localized terminology for *Honkai: Star Rail* (HSR): characters, Paths, elements, skills,
traces, Eidolons, Light Cones, Relics, items, materials, enemies, locations, factions, quests,
stages, events, achievements, Simulated Universe, Forgotten Hall, story proper nouns, world lore,
books, dialogue speakers, system and UI text.

- Total rows: **4,085,059** (`source,target,tgt_lng`)
- Unique concept keys: **42,126**
- Target languages: **13** — zh-CN, zh-TW, en-US, ja-JP, ko-KR, fr-FR, de-DE, es-ES, ru-RU, pt-PT, id-ID, th-TH, vi-VN
- Categories: **26**
- Client data version: `4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`
- Every target string comes from the official client localization — **no machine translation**

## Layout

```text
Honkai_Star_Rail_glossary（崩坏：星穹铁道）/
├─ README.md / README_EN.md / README_JP.md
├─ hsr-glossary/
│  ├─ zh-CN/ … vi-VN/      one folder per target language, 26 category CSVs each
│  ├─ historical/          names that changed between client versions (2.3.0 / 4.0 vs 4.5.0)
│  └─ curated/             small manually reviewed block (Trailblazer and similar)
├─ Sources/                source records
├─ Metadata/               statistics and validation results
└─ tools/                  build and validation scripts
```

## File format

Three columns only, UTF-8 with BOM, CRLF, RFC 4180 escaping:

```text
source,target,tgt_lng
Honkai: Star Rail,崩坏：星穹铁道,zh-CN
崩壊：スターレイル,崩坏：星穹铁道,zh-CN
```

`source` is the same localization key in another language, `target` is the target language string.
Rows are aligned by **shared TextMap hash / entity id**, never by fuzzy string matching.

## Data sources

- Primary: `DimbreathBot/TurnBasedGameData` 4.5.0 (commit `4ce30f69b`) — client TextMap ×13 + ExcelOutput
- Structured cross-check: `Mar-7th/StarRailRes` 4.5.0 (commit `d226bef`)
- Historical comparison: `VizualAbstract/StarRailStaticAPI` 2.3.0, `nathacks/HSR-Mapping-DATA` 4.0
- Story/dialogue support: `mrzjy/StarrailDialog`, `M1k0t0/StarRail_Dialogue_Browser`
- Reviewed but not used for generation: `iuyangyuc/homdgcat`, `kel-z/HSR-Data`, `simon300000/starrail-voice`

See [`Sources/README.md`](Sources/README.md) for the full record.

## Validation

Round 1 (structure) covers all 338 CSV files and 4,085,059 rows:
empty values, wrong language codes, duplicates, HTML tags, dev variables, hashes, internal ids, N/A,
and whether each target string exists in the client TextMap.

| Check | Result |
| --- | ---: |
| Empty source / target | 0 / 0 |
| Wrong language code | 0 |
| Duplicate rows | 0 |
| HTML tags | 0 |
| Dev variables | 0 |
| Hash / internal id leak | 0 / 0 |
| N/A placeholders | 0 |
| Target not found in client data | 0 |
| Machine-translated rows | 0 |

Round 2 samples every category and cross-checks against the independent StarRailRes index.

## Statistics

See [`Metadata/statistics.md`](Metadata/statistics.md): totals, per-language, per-category,
confirmed/unconfirmed, historical and multi-translation counts.

- Historical entries: 166
- Curated entries: 117
- Multi-translation groups: 41,475

## Rebuild

```bash
python tools/build_hsr_glossary.py
python tools/build_hsr_history.py
python tools/build_hsr_curated.py
python tools/validate_hsr_glossary.py
python tools/make_hsr_docs.py
```

## Disclaimer

Unofficial personal project for study, research and translation assistance. It is not affiliated with,
endorsed by, or connected to miHoYo / HoYoverse. Game names, characters and related assets belong to
their respective rights holders.
