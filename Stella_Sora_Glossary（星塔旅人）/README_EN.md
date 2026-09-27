# Stella Sora Terminology Database / 《星塔旅人》翻译术语库 / ステラソラ 用語集

## [中文](README.md) [日本語](README_JP.md)

This database collects proper-noun tables for the mobile game *Stella Sora* (《星塔旅人》/ ステラソラ), covering 15 categories: character names, skills, potentials, discs, items, equipment, enemies, stages, events, system terms, UI wording, story proper nouns, factions, locations, and gameplay mechanics — **12,292** entries in total in the five-language side-by-side master table. The entries are split by target language into **5** independent termbases (`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR`), each with 15 category files plus one merged master table. Translations come from the game's official multilingual client texts (CN / EN / JP / KR / TW regions), aligned across languages by the same text key, so they are **official localizations** rather than second-hand translations.

## Usage

1. **Download a single file**: open the matching language directory under `stella-sora-glossary/` (for example `stella-sora-glossary/zh-CN/`) and download a category glossary such as `character.csv`. It can be imported into terminology tools such as Immersive Translation with no conversion.
2. **Download a whole language directory**: if you need all 15 categories, download every category file in that language directory. Each language's merged table is at `stella-sora-glossary/_master/<lang>__all_glossary.csv`.
3. **Clone the whole repository and reproduce it yourself**: after `git clone`, use the generation scripts kept in `tools/` together with the upstream repositories referenced in the scripts' docstrings to regenerate every CSV from the raw data. Note that both scripts use **external absolute paths** — see “Regeneration” below.

## Directory Structure

```text
Stella_Sora_Glossary（星塔旅人）/
  stella-sora-glossary/     data container for the single-language termbases
    README.md               sub-library description, category list and counts
    zh-CN/                  termbase whose target language is Simplified Chinese
      README.md             language-level readme (Simplified Chinese)
      character.csv         character-name glossary (source,target,tgt_lng)
      character__terms.csv  this language's entry list (id,term,src_table)
      skill.csv / skill__terms.csv
      ...                   15 pairs of flat category CSVs in total
    zh-TW/                  same structure (target language 繁體中文)
    en-US/                  same structure (target language English)
    ja-JP/                  same structure (target language 日本語)
    ko-KR/                  same structure (target language 한국어)
    _master/                per-language merged tables, indexes and existing language notes
      zh-CN__all_glossary.csv
      zh-CN__all_terms.csv
      zh-CN__index.csv
      zh-CN__README.md
      ...                   other languages follow <lang>__<original-name>
    multilingual/           five-language side-by-side master table (internal layout unchanged)
      00_master/
        index.csv
        README.md
        source_mapping.csv
        StellaSora_all_terms.csv
      01_character/ … 15_terminology/
      StellaSora_Glossary.xlsx
  tools/                    generation scripts
    build_glossary.py       builds the five-language side-by-side master table (Python, reads an external data directory)
    split_by_language.py    splits it by target language (Python, reads an external master-table directory)
  README.md                 this readme (Simplified Chinese)
  README_EN.md              English readme
  README_JP.md              Japanese readme
```

The 15 category CSVs are **flat inside each language directory**: `<cat>.csv` is the glossary and `<cat>__terms.csv` is that language's entry list. There are no `NN_xxx/` subdirectories under a language directory. The `NN_xxx/` directories under `stella-sora-glossary/multilingual/` keep the raw five-language master-table layout.
## Data Overview

Entry counts and alignment-row counts per language (taken from the `TOTAL` row of each language's `stella-sora-glossary/_master/<lang>__index.csv`, and cross-checked against the actual data-row counts of all 15 category CSVs and of `stella-sora-glossary/_master/<lang>__all_terms.csv` / `<lang>__all_glossary.csv`):

| Folder | Language | Entries | Alignment rows |
| --- | --- | ---: | ---: |
| `stella-sora-glossary/zh-CN/` | Simplified Chinese | 12292 | 46279 |
| `stella-sora-glossary/zh-TW/` | Traditional Chinese | 12292 | 46052 |
| `stella-sora-glossary/en-US/` | English | 12288 | 46032 |
| `stella-sora-glossary/ja-JP/` | Japanese | 12289 | 46426 |
| `stella-sora-glossary/ko-KR/` | Korean | 12292 | 45950 |
| **Sum (simple addition of the five directories)** | | **61453** | **230739** |

Category × target language **entry-count** matrix (each cell is the number of entries actually present in that language directory, taken from each language's `stella-sora-glossary/_master/<lang>__index.csv`):

| Category | Topic | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | Character names | 287 | 287 | 287 | 287 | 287 |
| `skill.csv` | Skills | 628 | 628 | 628 | 628 | 628 |
| `potential.csv` | Potentials | 1457 | 1457 | 1457 | 1457 | 1457 |
| `disc.csv` | Discs | 234 | 234 | 234 | 234 | 234 |
| `item.csv` | Items | 558 | 558 | 558 | 558 | 558 |
| `equipment.csv` | Equipment | 15 | 15 | 15 | 15 | 15 |
| `enemy.csv` | Enemies | 399 | 399 | 399 | 399 | 399 |
| `stage.csv` | Stages | 1019 | 1019 | 1019 | 1019 | 1019 |
| `event.csv` | Events | 581 | 581 | 581 | 581 | 581 |
| `system.csv` | System terms | 1055 | 1055 | 1055 | 1055 | 1055 |
| `ui.csv` | UI wording | 4248 | 4248 | 4244 | 4245 | 4248 |
| `story.csv` | Story proper nouns | 527 | 527 | 527 | 527 | 527 |
| `faction.csv` | Factions | 21 | 21 | 21 | 21 | 21 |
| `location.csv` | Locations | 27 | 27 | 27 | 27 | 27 |
| `terminology.csv` | Gameplay mechanics | 1236 | 1236 | 1236 | 1236 | 1236 |
| **Total** | | **12292** | **12292** | **12288** | **12289** | **12292** |

Category × target language **alignment-row** matrix (data rows of `<cat>.csv`):

| Category | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 979 | 977 | 973 | 1021 | 968 |
| `skill.csv` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `potential.csv` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `disc.csv` | 893 | 896 | 896 | 893 | 893 |
| `item.csv` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `equipment.csv` | 58 | 58 | 58 | 58 | 58 |
| `enemy.csv` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `stage.csv` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `event.csv` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `system.csv` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `ui.csv` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `story.csv` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `faction.csv` | 81 | 78 | 78 | 78 | 78 |
| `location.csv` | 98 | 98 | 98 | 96 | 96 |
| `terminology.csv` | 4660 | 4637 | 4630 | 4661 | 4649 |
| **Total** | **46279** | **46052** | **46032** | **46426** | **45950** |

The five-language side-by-side master table `stella-sora-glossary/multilingual/` (one entry per row, five languages side by side):

| File | Rows |
| --- | ---: |
| `stella-sora-glossary/multilingual/00_master/StellaSora_all_terms.csv` | 12292 |
| `stella-sora-glossary/multilingual/00_master/source_mapping.csv` | 219 |
| 15 × `stella-sora-glossary/multilingual/NN_xxx/<cat>__terms.csv`, combined | 12292 |
| 15 × `stella-sora-glossary/multilingual/NN_xxx/<cat>.csv`, combined | 147462 |

> The 15 categories have **identical entry counts** except for `ui.csv`: a few official UI strings have no separate translation in some regions, so `en-US` has 4 entries fewer than `zh-CN` and `ja-JP` has 3 fewer. Alignment-row counts are generally lower than “entries × 4” because duplicate rows are removed.

## Related Sources

| Source | Purpose |
| --- | --- |
| [Hiro420/StellaSoraData](https://github.com/Hiro420/StellaSoraData) | The game's official multilingual text library (CN / EN / JP / KR / TW region `language/*` text tables and `bin/` config tables). `tools/build_glossary.py` reads only this dataset; it is the main source of this database |
| [JforPlay/sstoy](https://github.com/JforPlay/sstoy) | Stella Sora data-unpacking / tooling reference (an upstream project also listed in the repository root readme; it is not an input to the generation scripts here) |

The per-category mapping of each individual source table is documented in `stella-sora-glossary/multilingual/00_master/source_mapping.csv` and `stella-sora-glossary/multilingual/00_master/README.md`.

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
> - `tools/split_by_language.py`: input/output root `E:\Download\BT\Codex_input\StellaSora_Glossary`; it reads the `multilingual/` inside it and writes the sibling `zh-CN/`, `zh-TW/`, `en-US/`, `ja-JP/`, `ko-KR/` directories, and writes `_summary.json` into that external root (**not** into this repository).
>
> In other words: the CSVs in this repository are a **snapshot copied in** after that external pipeline ran; executing the scripts as they are will not update this repository. To reproduce, first place the upstream repository at the external path above (or edit the two path constants in the scripts) and copy the results back afterwards. As of the latest check, `E:\Download\BT\Codex_input\` is an empty directory and neither upstream directory exists.
>
> In addition, `stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx` and `stella-sora-glossary/multilingual/00_master/source_mapping.csv` come from one-off steps outside that pipeline: **neither script in `tools/` generates them.**

## Notes

- The translations come from the game's official multilingual text library `StellaSoraData-main` (official CN / EN / JP / KR / TW region texts); all languages are aligned by the same text key, so they are official localizations, not hand-made second translations.
- The five language tags are `zh-CN` Simplified Chinese, `zh-TW` Traditional Chinese, `en-US` English, `ja-JP` Japanese and `ko-KR` Korean. A given entry has exactly the same original text key (`id`) in all five languages.
- The two files inside each termbase have the following formats.

  **`<cat>.csv` — terminology table (`source` / `target` / `tgt_lng`)**

  `tgt_lng` is fixed for that language and `source` holds the wording of the other four languages, so the file can be imported directly into terminology tools:

  | source | target | tgt_lng |
  | --- | --- | --- |
  | Amber | 琥珀 | zh-CN |
  | コハク | 琥珀 | zh-CN |
  | 코하쿠 | 琥珀 | zh-CN |

  **`<cat>__terms.csv` — this language's entry list (`id` / `term` / `src_table`)**

  | id | term | src_table |
  | --- | --- | --- |
  | Character.103.1 | 琥珀 | Character.json |

  `stella-sora-glossary/_master/<lang>__all_glossary.csv` adds a `category` column before `source,target,tgt_lng`; `stella-sora-glossary/_master/<lang>__all_terms.csv` is `category,category_label,id,term,src_table`; `stella-sora-glossary/_master/<lang>__index.csv` is `category,label,term_count,glossary_file,terms_file,target_language`.
- `stella-sora-glossary/multilingual/` keeps the raw five-language side-by-side master table: `<cat>__terms.csv` is `id,zh-CN,en-US,ja-JP,ko-KR,zh-TW,src_table` with one entry per row, while `<cat>.csv` pairs the four languages zh-CN / en-US / ja-JP / ko-KR in every ordered combination, expanding each entry into at most 12 rows (4×3 ordered language pairs) so that any language can be used as the source. The same data is also available as the Excel workbook `stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx` (index sheet + 15 category sheets, 16 sheets in total; its existence has been verified).
- **Extraction and filtering rules** (the full rules are in `stella-sora-glossary/multilingual/00_master/README.md`):
  - only “name / label” fields are extracted (usually `.1`; the disc tables use `.1/.2/.3`); descriptions, numeric values and dialogue bodies are **not** included;
  - `Item.json` is routed into items, potentials, discs, emblems and avatars by the `Type`/`Stype` columns of the config table;
  - interface texts (`UIText` and friends) keep only short terms (Simplified Chinese ≤24 characters and without sentence-ending punctuation), filtering out full-sentence prompts;
  - entries whose five-language content is completely identical within a category are merged into one (keeping the source-table ID of the first occurrence);
  - placeholders and deprecated entries such as `【不要翻译】`, `【废弃】` and `[no trans]` have been removed;
  - rich-text markup such as `<color=…>` and `<sprite …>` has been stripped;
  - when splitting into single-language directories, a `source` identical to the target wording, and any `source`→`target` row already seen inside the same category, are dropped — hence alignment rows number fewer than “entries × 4”.
- **Known limitations**:
  - dialogue, story bodies and item descriptions are long-form content outside the scope of this database; export them separately as a translation memory (TMX / bilingual alignment) if needed;
  - apart from `DatingLandmark` and `StarTower`, the place names in `location.csv` have no dedicated table in the game data; they were manually curated from officially aligned texts such as character archive addresses, achievements and story titles, and are marked with the source `curated (aligned in-game text)`;
  - `equipment.csv` has only 15 entries: this game has no traditional weapon/armour table, and the equipment slot is taken by the “Disc”;
  - every language directory contains cases where one `source` maps to several `target` values (`zh-CN` 1133 such sources, `zh-TW` 962, `en-US` 826, `ja-JP` 1269, `ko-KR` 700); these mostly come from short words that name different things (for example the English `Amber` corresponds to both 「琥珀」 and 「暖黄」 in `zh-CN`). Tools that deduplicate by `source` will keep only one of them; use the `id` and `src_table` columns of `__terms.csv` to look up the context when you need to tell them apart.
- All CSVs are UTF-8 with BOM and CRLF line endings, so Excel displays CJK text correctly on a double-click; the `.md` readmes are UTF-8 (without BOM).

## Disclaimer

This directory is an **unofficial** translation terminology database compiled and maintained by an individual, intended only for personal study, research and terminology matching in AI translation software (including but not limited to Immersive Translation). It has no affiliation, authorization, partnership, agency or official-representation relationship with the developers, publishers, distributors, operators or rights holders of *Stella Sora*; the translations herein do not represent any official position, are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be regarded as the official terminology list or official localization file of any game**. Intellectual property such as game titles, character names, proper nouns and trademarks belongs to their respective rights holders. This database claims no rights over that third-party intellectual property. All responsibility arising from the use of this project and of translations produced from it rests with the user. If a rights holder considers any content inappropriate, please make contact through GitHub Issues / Pull Requests and the maintainer will verify and amend or remove it. The complete terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and is not affiliated with, authorized by, partnered with, or acting as an agent for this game or its developer, publisher, distributor or rights holder.**
