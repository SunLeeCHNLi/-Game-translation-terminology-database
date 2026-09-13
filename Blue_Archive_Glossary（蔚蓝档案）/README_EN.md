# Blue Archive Terminology Database / 《蔚蓝档案》翻译术语库 / ブルーアーカイブ 用語集

## [中文](README.md) [日本語](README_JP.md)

This repository section is a proper-noun terminology database for the mobile game *Blue Archive* (ブルーアーカイブ). It covers 15 categories: character names, schools, clubs, story titles, gifts (favor items), locations, terminology, events, scenario characters, enemies, skills, items, equipment, furniture and stages. All 15 categories together hold **7535** entries, split into **6** independent termbases by target language (`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `th-TH`), each with its own 15 category files plus a merged master table. All translations are taken from the official client's multilingual text and aligned on the same text keys, so they are **official localizations** rather than second-hand translations; the small number of entries the official data does not cover are filled in from a community story-translation table.

## Usage

1. **Single-file download** — open the language folder you need (for example `zh-CN/`) and download a category glossary such as `01_character/01_character_glossary.csv`. It can be imported directly into terminology tools such as Immersive Translate, with no conversion needed.
2. **Whole-language download** — if you need all 15 categories, download every category folder under that language, or simply take `00_master/all_glossary.csv`, the merged table of every aligned row for that language.
3. **Clone the whole repository and regenerate** — after `git clone`, use the generation scripts kept in `tools/` together with the three upstream repositories named in the script's docstring to rebuild every CSV from the original data.

## Directory Structure

```text
Blue_Archive_Glossary（蔚蓝档案）/
  zh-CN/                    termbase targeting Simplified Chinese
    00_master/              index + merged master tables + documentation
      all_glossary.csv      merged aligned rows of all 15 categories
      all_terms.csv         the complete term list of this language
      index.csv             category index and counts (authoritative per-category counts)
      README.md             detailed notes for this language termbase
    01_character/           character names
    02_school/              schools
    03_club/                clubs
    04_story_title/         story titles
    05_favor_item/          favor items (gifts)
    06_location/            locations
    07_terminology/         terminology
    08_event/               events
    09_scenario_character/  scenario characters
    10_enemy/               enemies
    11_skill/               skills
    12_item/                items
    13_equipment/           equipment
    14_furniture/           furniture
    15_stage/               stages
  zh-TW/                    same layout (target language: Traditional Chinese)
  en-US/                    same layout (target language: English)
  ja-JP/                    same layout (target language: Japanese)
  ko-KR/                    same layout (target language: Korean)
  th-TH/                    same layout (target language: Thai)
  multilingual/             six-language side-by-side master table
    00_master/
      all_terms_multilingual.csv   every entry, one row, six languages side by side
      README.md                    notes and column definitions
    01_character/           01_character_multilingual.csv
    02_school/              02_school_multilingual.csv
    03_club/                03_club_multilingual.csv
    04_story_title/         04_story_title_multilingual.csv
    05_favor_item/          05_favor_item_multilingual.csv
    06_location/            06_location_multilingual.csv
    07_terminology/         07_terminology_multilingual.csv
    08_event/               08_event_multilingual.csv
    09_scenario_character/  09_scenario_character_multilingual.csv
    10_enemy/               10_enemy_multilingual.csv
    11_skill/               11_skill_multilingual.csv
    12_item/                12_item_multilingual.csv
    13_equipment/           13_equipment_multilingual.csv
    14_furniture/           14_furniture_multilingual.csv
    15_stage/               15_stage_multilingual.csv
  tools/                    generation scripts and generation metadata
    build_glossary.py       termbase generator (Python)
    extract_ts_titles.mjs   story-title extractor (requires Node.js)
    ts_titles.json          extracted story titles (cache for `extract_ts_titles.mjs`, read directly by `build_glossary.py`)
  README.md                 this file set: Simplified Chinese
  README_EN.md              English
  README_JP.md              Japanese
```

Every `NN_xxx/` folder under a language directory contains exactly two files, `NN_xxx_glossary.csv` and `NN_xxx_terms.csv`; under `multilingual/` it contains a single `NN_xxx_multilingual.csv`.

## Data Overview

Entry counts and aligned-row counts per language (`00_master/index.csv`, verified against the actual CSV data rows):

| Folder | Language | Terms | Aligned rows |
| --- | --- | ---: | ---: |
| `zh-CN/` | Simplified Chinese | 7477 | 29463 |
| `zh-TW/` | Traditional Chinese | 6036 | 27453 |
| `en-US/` | English | 5909 | 26623 |
| `ja-JP/` | Japanese | 7534 | 29216 |
| `ko-KR/` | Korean | 7310 | 29009 |
| `th-TH/` | Thai | 5908 | 26478 |

Category × target language (each cell is the number of entries that actually exist in that language, taken from each language's `00_master/index.csv`):

| Category | Topic | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` | `th-TH` |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `01_character` | Character names | 408 | 408 | 204 | 408 | 408 | 204 |
| `02_school` | Schools | 26 | 26 | 26 | 26 | 26 | 26 |
| `03_club` | Clubs | 43 | 43 | 43 | 43 | 43 | 43 |
| `04_story_title` | Story titles | 1086 | 680 | 665 | 1144 | 1051 | 664 |
| `05_favor_item` | Favor items | 51 | 51 | 51 | 51 | 51 | 51 |
| `06_location` | Locations | 90 | 8 | 8 | 90 | 8 | 8 |
| `07_terminology` | Terminology | 1402 | 1379 | 1379 | 1401 | 1379 | 1379 |
| `08_event` | Events | 72 | 45 | 45 | 72 | 45 | 45 |
| `09_scenario_character` | Scenario characters | 945 | 134 | 134 | 945 | 945 | 134 |
| `10_enemy` | Enemies | 351 | 349 | 351 | 351 | 351 | 351 |
| `11_skill` | Skills | 1069 | 1069 | 1069 | 1069 | 1069 | 1069 |
| `12_item` | Items | 649 | 649 | 649 | 649 | 649 | 649 |
| `13_equipment` | Equipment | 155 | 155 | 155 | 155 | 155 | 155 |
| `14_furniture` | Furniture | 472 | 472 | 472 | 472 | 472 | 472 |
| `15_stage` | Stages | 658 | 568 | 658 | 658 | 658 | 658 |
| **Total** | | **7477** | **6036** | **5909** | **7534** | **7310** | **5908** |

> `multilingual/00_master/all_terms_multilingual.csv` is the **de-duplicated union** of all entries: **7535** rows, one entry per row with six languages side by side. That number is larger than any single language's term count because it also includes entries that exist in only one language.

## Related Sources

| Source | Purpose |
| --- | --- |
| [RedBeanN/BlueArchive](https://github.com/RedBeanN/BlueArchive) | Official client multilingual data tables (`students` / `items` / `equipment` / `enemies` / `furniture` / `localization` / `stages`), aligned across the six languages by Id and text key; the backbone of this database |
| [ba-archive/blue-archive](https://github.com/ba-archive/blue-archive) | Story-viewer index (main story / other / regional event titles, MomoTalk conversation titles) and the story editor's name table (scenario characters) |
| [HePudding/ba-storybook](https://github.com/HePudding/ba-storybook) | Community-maintained Japanese→Chinese story translation table (story titles / locations / events / scenario characters), used to fill in entries the official tables do not cover |

## Regeneration

```bash
# Reads the three upstream repositories under E:\Download\BT\Codex_input by default,
# and writes into this game directory
python tools/build_glossary.py

# Override the input / output directories
# PowerShell (Windows):
$env:BA_INPUT_DIR="D:\src"; $env:BA_OUTPUT_DIR="D:\out"; python tools/build_glossary.py
# bash (Linux / macOS):
BA_INPUT_DIR="/data/src" BA_OUTPUT_DIR="/data/out" python tools/build_glossary.py

# Story-title cache: requires Node.js, writes tools/ts_titles.json
node tools/extract_ts_titles.mjs
```

## Notes

- The six language tags: `zh-CN` Simplified Chinese (CN server), `zh-TW` Traditional Chinese (global server), `en-US` English, `ja-JP` Japanese, `ko-KR` Korean, `th-TH` Thai.
- Translations come from the official client's multilingual text, aligned on the same text keys; they are official localizations, not second-hand translations.
- `zh-CN` and `zh-TW` are two distinct official localizations, so their names do not always differ only by simplified/traditional script, and a single word may differ between a school's short name and full name (for example `Gehenna`: the Simplified Chinese short name is 格黑娜 and the full name 歌赫娜, while the Traditional Chinese full name is 格黑娜學園).
- The same name occasionally differs in spelling between sources; this database follows the official data tables, and the community tables are used only to fill in entries the official tables lack.
- The character category also carries "full name" entries (surname + given name) for the CJK languages only: English and Thai reverse the CJK name order, and the official data provides no directly concatenable spelling for them.
- `04_story_title`, `06_location` and `09_scenario_character` are based on story and community material, and are auto-completed for other languages from the official tables only on exactly matching spellings, so they are not complete in all six languages for every entry. The CJK student names inside `09_scenario_character` likewise come from the official tables; only NPCs missing from those tables use the client name table.
- When the same name has several data rows (for example same-named enemies at different levels) they are merged into one entry, and entries whose spelling is identical to the target language are not written into the glossary.
- A very small share of entries (roughly 1%–3%) produce one `source` mapping to several `target` values **inside a single target-language file**. These mostly come from short words that name different things (for example `Normal` is both an armor type and an item rarity), or from Simplified and Traditional client spellings coexisting. Tools that de-duplicate by `source` keep only one of them; use the `id` and `src_table` columns in `_terms.csv` to recover the context when you need to tell them apart.
- A per-category file `NN_xxx_glossary.csv` has the three columns `source,target,tgt_lng`; `00_master/all_glossary.csv` adds a leading `category` column; `all_terms.csv` has `category,category_label,id,term,src_table`; `index.csv` has `category,label,term_count,glossary_file,terms_file,target_language`.
- All CSVs are UTF-8 with BOM and CRLF line endings, so Excel shows CJK and Thai text correctly on a double click. The `.md` documentation files are UTF-8 (no BOM).
- Regeneration: `python tools/build_glossary.py` (reads `E:\Download\BT\Codex_input` by default; override with the `BA_INPUT_DIR` / `BA_OUTPUT_DIR` environment variables. The script lives in `tools/`, so the command line must include the `tools/` prefix).

## Disclaimer

This directory is a **non-official** translation terminology database compiled and maintained by an individual, intended only for personal study, research, and terminology matching in AI translation software (including but not limited to Immersive Translate). It has no affiliation, authorization, cooperation, agency or official-representation relationship with the developers, publishers, distributors, operators or rights holders of *Blue Archive*. The names in it do not represent any official position, are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be treated as an official glossary or official localization file of any game**. Intellectual property such as game names, character names, proper nouns and trademarks belongs to their respective owners; this database claims no rights over that third-party intellectual property. All responsibility arising from the use of this project and of translations produced from it rests with the user. Rights holders who consider any content inappropriate are welcome to make contact through GitHub Issues / Pull Requests, and the maintainer will verify and then amend or remove it. The complete terms are in the repository root's `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorization, cooperation or agency relationship with this game or its developers, publishers, distributors or rights holders.**
