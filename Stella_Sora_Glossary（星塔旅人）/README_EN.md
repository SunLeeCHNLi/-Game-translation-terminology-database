# Stella Sora Terminology Database / 《星塔旅人》翻译术语库 / ステラソラ 用語集

## [中文](README.md) [日本語](README_JP.md)

This database collects proper-noun tables for the mobile game *Stella Sora* (《星塔旅人》/ ステラソラ), covering 15 categories: character names, skills, potentials, discs, items, equipment, enemies, stages, events, system terms, UI wording, story proper nouns, factions, locations, and gameplay mechanics — **12,292** entries in total in the five-language side-by-side master table. The entries are split by target language into **5** independent termbases (`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR`), each with 15 category files plus one merged master table. Translations come from the game's official multilingual client texts (CN / EN / JP / KR / TW regions), aligned across languages by the same text key, so they are **official localizations** rather than second-hand translations.

## Usage

1. **Download a single file**: open a language directory (for example `zh-CN/`) and download a category glossary such as `01_character/01_character_glossary.csv`. It can be imported into terminology tools such as Immersive Translation with no conversion.
2. **Download a whole language directory**: if you need all 15 categories, download every category file in that language directory, or simply take `00_master/all_glossary.csv` (that language's merged table of all alignment rows).
3. **Clone the whole repository and reproduce it yourself**: after `git clone`, use the generation scripts kept in `tools/` together with the upstream repositories referenced in the scripts' docstrings to regenerate every CSV from the raw data. Note that both scripts use **external absolute paths** — see “Regeneration” below.

## Directory Structure

```text
Stella_Sora_Glossary（星塔旅人）/
  zh-CN/                    termbase whose target language is Simplified Chinese
    README.md               language-level readme (Simplified Chinese)
    00_master/              index + merged tables + notes
      all_glossary.csv      all 15 categories' alignment rows, merged
      all_terms.csv         every entry of this language
      index.csv             category index and entry counts (authoritative source for per-category counts)
      README.md             pre-existing detailed readme for this language
    01_character/           character names
    02_skill/               skills
    03_potential/           potentials
    04_disc/                discs
    05_item/                items
    06_equipment/           equipment
    07_enemy/               enemies
    08_stage/               stages
    09_event/               events
    10_system/              system terms
    11_ui/                  UI wording
    12_story/               story proper nouns
    13_faction/             factions
    14_location/            locations
    15_terminology/         gameplay mechanics
  zh-TW/                    same structure (target language 繁體中文), plus README_zh-CN.md
  en-US/                    same structure (target language English), plus README_zh-CN.md
  ja-JP/                    same structure (target language 日本語), plus README_zh-CN.md
  ko-KR/                    same structure (target language 한국어), plus README_zh-CN.md
  multilingual/             five-language side-by-side master table (not a single-language directory, hence no language readme)
    00_master/
      index.csv                       category index and counts
      README.md                       master-table notes, column definitions, per-category sources
      source_mapping.csv              source table → category mapping detail (219 rows)
      StellaSora_all_terms.csv        every entry, one per row, five languages side by side
    01_character/                     01_character_glossary.csv + 01_character_terms.csv
    02_skill/                         02_skill_glossary.csv + 02_skill_terms.csv
    03_potential/                     03_potential_glossary.csv + 03_potential_terms.csv
    04_disc/                          04_disc_glossary.csv + 04_disc_terms.csv
    05_item/                          05_item_glossary.csv + 05_item_terms.csv
    06_equipment/                     06_equipment_glossary.csv + 06_equipment_terms.csv
    07_enemy/                         07_enemy_glossary.csv + 07_enemy_terms.csv
    08_stage/                         08_stage_glossary.csv + 08_stage_terms.csv
    09_event/                         09_event_glossary.csv + 09_event_terms.csv
    10_system/                        10_system_glossary.csv + 10_system_terms.csv
    11_ui/                            11_ui_glossary.csv + 11_ui_terms.csv
    12_story/                         12_story_glossary.csv + 12_story_terms.csv
    13_faction/                       13_faction_glossary.csv + 13_faction_terms.csv
    14_location/                      14_location_glossary.csv + 14_location_terms.csv
    15_terminology/                   15_terminology_glossary.csv + 15_terminology_terms.csv
    StellaSora_Glossary.xlsx          the same data as an Excel workbook (index sheet + 15 category sheets, 16 sheets in total)
  tools/                    generation scripts
    build_glossary.py       builds the five-language side-by-side master table (Python, reads an external data directory)
    split_by_language.py    splits it by target language (Python, reads an external master-table directory)
  README.md                 this readme (Simplified Chinese)
  README_EN.md              English readme
  README_JP.md              Japanese readme
```

Each `NN_xxx/` directory inside a language directory contains exactly two files: `NN_xxx_glossary.csv` and `NN_xxx_terms.csv`. The `NN_xxx/` directories under `multilingual/` use the same two filenames but hold the raw five-language side-by-side tables instead (see “Notes” below).

## Data Overview

Entry counts and alignment-row counts per language (taken from the `TOTAL` row of each language's `00_master/index.csv`, and cross-checked against the actual data-row counts of all 15 category CSVs and of `00_master/all_terms.csv` / `all_glossary.csv`):

| Folder | Language | Entries | Alignment rows |
| --- | --- | ---: | ---: |
| `zh-CN/` | Simplified Chinese | 12292 | 46279 |
| `zh-TW/` | Traditional Chinese | 12292 | 46052 |
| `en-US/` | English | 12288 | 46032 |
| `ja-JP/` | Japanese | 12289 | 46426 |
| `ko-KR/` | Korean | 12292 | 45950 |
| **Sum (simple addition of the five directories)** | | **61453** | **230739** |

Category × target language **entry-count** matrix (each cell is the number of entries actually present in that language directory, taken from each language's `00_master/index.csv`):

| Category | Topic | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `01_character` | Character names | 287 | 287 | 287 | 287 | 287 |
| `02_skill` | Skills | 628 | 628 | 628 | 628 | 628 |
| `03_potential` | Potentials | 1457 | 1457 | 1457 | 1457 | 1457 |
| `04_disc` | Discs | 234 | 234 | 234 | 234 | 234 |
| `05_item` | Items | 558 | 558 | 558 | 558 | 558 |
| `06_equipment` | Equipment | 15 | 15 | 15 | 15 | 15 |
| `07_enemy` | Enemies | 399 | 399 | 399 | 399 | 399 |
| `08_stage` | Stages | 1019 | 1019 | 1019 | 1019 | 1019 |
| `09_event` | Events | 581 | 581 | 581 | 581 | 581 |
| `10_system` | System terms | 1055 | 1055 | 1055 | 1055 | 1055 |
| `11_ui` | UI wording | 4248 | 4248 | 4244 | 4245 | 4248 |
| `12_story` | Story proper nouns | 527 | 527 | 527 | 527 | 527 |
| `13_faction` | Factions | 21 | 21 | 21 | 21 | 21 |
| `14_location` | Locations | 27 | 27 | 27 | 27 | 27 |
| `15_terminology` | Gameplay mechanics | 1236 | 1236 | 1236 | 1236 | 1236 |
| **Total** | | **12292** | **12292** | **12288** | **12289** | **12292** |

Category × target language **alignment-row** matrix (data rows of `NN_xxx_glossary.csv`):

| Category | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `01_character` | 979 | 977 | 973 | 1021 | 968 |
| `02_skill` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `03_potential` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `04_disc` | 893 | 896 | 896 | 893 | 893 |
| `05_item` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `06_equipment` | 58 | 58 | 58 | 58 | 58 |
| `07_enemy` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `08_stage` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `09_event` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `10_system` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `11_ui` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `12_story` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `13_faction` | 81 | 78 | 78 | 78 | 78 |
| `14_location` | 98 | 98 | 98 | 96 | 96 |
| `15_terminology` | 4660 | 4637 | 4630 | 4661 | 4649 |
| **Total** | **46279** | **46052** | **46032** | **46426** | **45950** |

The five-language side-by-side master table `multilingual/` (one entry per row, five languages side by side):

| File | Rows |
| --- | ---: |
| `multilingual/00_master/StellaSora_all_terms.csv` | 12292 |
| `multilingual/00_master/source_mapping.csv` | 219 |
| 15 × `multilingual/NN_xxx/NN_xxx_terms.csv`, combined | 12292 |
| 15 × `multilingual/NN_xxx/NN_xxx_glossary.csv`, combined | 147462 |

> The 15 categories have **identical entry counts** except for `11_ui`: a few official UI strings have no separate translation in some regions, so `en-US` has 4 entries fewer than `zh-CN` and `ja-JP` has 3 fewer. Alignment-row counts are generally lower than “entries × 4” because duplicate rows are removed.

## Related Sources

| Source | Purpose |
| --- | --- |
| [Hiro420/StellaSoraData](https://github.com/Hiro420/StellaSoraData) | The game's official multilingual text library (CN / EN / JP / KR / TW region `language/*` text tables and `bin/` config tables). `tools/build_glossary.py` reads only this dataset; it is the main source of this database |
| [JforPlay/sstoy](https://github.com/JforPlay/sstoy) | Stella Sora data-unpacking / tooling reference (an upstream project also listed in the repository root readme; it is not an input to the generation scripts here) |

The per-category mapping of each individual source table is documented in `multilingual/00_master/source_mapping.csv` and `multilingual/00_master/README.md`.

## Regeneration

```bash
# 1) build the five-language side-by-side master table from the upstream multilingual text library
python tools/build_glossary.py

# 2) split it by target language, producing the 5 single-language termbases
#    (duplicate source→target rows inside the same category are removed)
python tools/split_by_language.py

# syntax check
python -m py_compile tools/build_glossary.py tools/split_by_language.py
```

> **Important: both scripts use hard-coded external absolute paths and never read or write this repository.** Moving the scripts (from the former `multilingual/00_master/tools/` to the game root's `tools/`) **does not affect how they run**, because neither script depends on its own directory:
>
> - `tools/build_glossary.py`: input `E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main` (the upstream text library), output `E:\Download\BT\Codex_input\StellaSora_Glossary`;
> - `tools/split_by_language.py`: input/output root `E:\Download\BT\Codex_input\StellaSora_Glossary`; it reads the `multilingual/` inside it, writes the sibling `zh-CN/`, `zh-TW/`, `en-US/`, `ja-JP/`, `ko-KR/` directories, and writes `_summary.json` into that external root (**not** into this repository).
>
> In other words: the CSVs in this repository are a **snapshot copied in** after that external pipeline ran; executing the scripts as they are will not update this repository. To reproduce, first place the upstream repository at the external path above (or edit the two path constants in the scripts) and copy the results back afterwards. As of the latest check, `E:\Download\BT\Codex_input\` is an empty directory and neither upstream directory exists.
>
> In addition, `multilingual/StellaSora_Glossary.xlsx` and `multilingual/00_master/source_mapping.csv` come from one-off steps outside that pipeline: **neither script in `tools/` generates them.**

## Notes

- The translations come from the game's official multilingual text library `StellaSoraData-main` (official CN / EN / JP / KR / TW region texts); all languages are aligned by the same text key, so they are official localizations, not hand-made second translations.
- The five language tags are `zh-CN` Simplified Chinese, `zh-TW` Traditional Chinese, `en-US` English, `ja-JP` Japanese and `ko-KR` Korean. A given entry has exactly the same original text key (`id`) in all five languages.
- The two files inside each termbase have the following formats.

  **`NN_xxx_glossary.csv` — terminology table (`source` / `target` / `tgt_lng`)**

  `tgt_lng` is fixed for that language and `source` holds the wording of the other four languages, so the file can be imported directly into terminology tools:

  | source | target | tgt_lng |
  | --- | --- | --- |
  | Amber | 琥珀 | zh-CN |
  | コハク | 琥珀 | zh-CN |
  | 코하쿠 | 琥珀 | zh-CN |

  **`NN_xxx_terms.csv` — this language's entry list (`id` / `term` / `src_table`)**

  | id | term | src_table |
  | --- | --- | --- |
  | Character.103.1 | 琥珀 | Character.json |

  `00_master/all_glossary.csv` adds a `category` column before `source,target,tgt_lng`; `00_master/all_terms.csv` is `category,category_label,id,term,src_table`; `00_master/index.csv` is `category,label,term_count,glossary_file,terms_file,target_language`.
- `multilingual/` keeps the raw five-language side-by-side master table: `NN_xxx_terms.csv` is `id,zh-CN,en-US,ja-JP,ko-KR,zh-TW,src_table` with one entry per row, while `NN_xxx_glossary.csv` pairs the four languages zh-CN / en-US / ja-JP / ko-KR in every ordered combination, expanding each entry into at most 12 rows (4×3 ordered language pairs) so that any language can be used as the source. The same data is also available as the Excel workbook `multilingual/StellaSora_Glossary.xlsx` (index sheet + 15 category sheets, 16 sheets in total; its existence has been verified).
- **Extraction and filtering rules** (the full rules are in `multilingual/00_master/README.md`):
  - only “name / label” fields are extracted (usually `.1`; the disc tables use `.1/.2/.3`); descriptions, numeric values and dialogue bodies are **not** included;
  - `Item.json` is routed into items, potentials, discs, emblems and avatars by the `Type`/`Stype` columns of the config table;
  - interface texts (`UIText` and friends) keep only short terms (Simplified Chinese ≤24 characters and without sentence-ending punctuation), filtering out full-sentence prompts;
  - entries whose five-language content is completely identical within a category are merged into one (keeping the source-table ID of the first occurrence);
  - placeholders and deprecated entries such as `【不要翻译】`, `【废弃】` and `[no trans]` have been removed;
  - rich-text markup such as `<color=…>` and `<sprite …>` has been stripped;
  - when splitting into single-language directories, a `source` identical to the target wording, and any `source`→`target` row already seen inside the same category, are dropped — hence alignment rows number fewer than “entries × 4”.
- **Known limitations**:
  - dialogue, story bodies and item descriptions are long-form content outside the scope of this database; export them separately as a translation memory (TMX / bilingual alignment) if needed;
  - apart from `DatingLandmark` and `StarTower`, the place names in `14_location` have no dedicated table in the game data; they were manually curated from officially aligned texts such as character archive addresses, achievements and story titles, and are marked with the source `curated (aligned in-game text)`;
  - `06_equipment` has only 15 entries: this game has no traditional weapon/armour table, and the equipment slot is taken by the “Disc”;
  - every language directory contains cases where one `source` maps to several `target` values (`zh-CN` 1133 such sources, `zh-TW` 962, `en-US` 826, `ja-JP` 1269, `ko-KR` 700); these mostly come from short words that name different things (for example the English `Amber` corresponds to both 「琥珀」 and 「暖黄」 in `zh-CN`). Tools that deduplicate by `source` will keep only one of them; use the `id` and `src_table` columns of `_terms.csv` to look up the context when you need to tell them apart.
- All CSVs are UTF-8 with BOM and CRLF line endings, so Excel displays CJK text correctly on a double-click; the `.md` readmes are UTF-8 (without BOM).

## Disclaimer

This directory is an **unofficial** translation terminology database compiled and maintained by an individual, intended only for personal study, research and terminology matching in AI translation software (including but not limited to Immersive Translation). It has no affiliation, authorization, partnership, agency or official-representation relationship with the developers, publishers, distributors, operators or rights holders of *Stella Sora*; the translations herein do not represent any official position, are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be regarded as the official terminology list or official localization file of any game**. Intellectual property such as game titles, character names, proper nouns and trademarks belongs to their respective rights holders. This database claims no rights over that third-party intellectual property. All responsibility arising from the use of this project and of translations produced from it rests with the user. If a rights holder considers any content inappropriate, please make contact through GitHub Issues / Pull Requests and the maintainer will verify and amend or remove it. The complete terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and is not affiliated with, authorized by, partnered with, or acting as an agent for this game or its developer, publisher, distributor or rights holder.**
