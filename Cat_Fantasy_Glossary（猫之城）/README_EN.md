# Cat Fantasy Terminology Database / 《猫之城》翻译术语库 / Cat Fantasy 用語集

## [中文](README.md) [日本語](README_JP.md)

This database compiles the official multilingual texts of the mobile game *Cat Fantasy* (《猫之城》),
extracted and aligned from the game's official multilingual data tables and its I18N interface text table.
It contains **102,213** unique entries, split by target language into **7** independent terminology sets
(**619,095** entry records, **1,206,381** language-pair rows), each further organised into 16 categories.
Every translation is **taken from localisation text the game itself ships** and aligned by the same text
key — there is no machine translation or manual re-translation. Six of the sets
(`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `th-TH`) cover all 16 categories, while `id-ID` contains
only `13_ui`, because Indonesian is officially shipped for interface text only.

## Usage

1. **Download a single file** — open `cat-fantasy-glossary/<language>/`, open the `<category>.csv` you
   want (for example `zh-CN/character.csv`), and download it from its file detail page. The file has three
   columns (`source,target,tgt_lng`) and can be imported directly into the terminology feature of AI
   translation software such as Immersive Translation.
2. **Download one whole language directory** — the 16 category CSVs in `cat-fantasy-glossary/<language>/`
   together form the complete term list for that language (see
   `cat-fantasy-glossary/_master/<language>__index.csv` for the index and counts).
3. **Clone the whole repository** — use `cat-fantasy-glossary/_master/<language>__index.csv` and
   `cat-fantasy-glossary/multilingual/all_languages_master.csv` to search, split, or further process the
   data yourself; see "Related Sources" below for the upstream repositories. **Note:** this database ships
   no generation scripts (see "Regeneration").

## Directory Structure

```text
Cat_Fantasy_Glossary（猫之城）/
├── README.md                          This document (Simplified Chinese)
├── README_EN.md                       This document (English)
├── README_JP.md                       This document (日本語)
└── cat-fantasy-glossary/              Multilingual terminology data product
    ├── README.md                      Sub-library description
    ├── zh-CN/                         Simplified Chinese (same layout as the other languages)
    │   ├── character.csv              Characters and cards (`source,target,tgt_lng`)
    │   ├── character__terms.csv       Characters and cards term list (`id,term,src_table`)
    │   └── ...                        16 categories × 2 flat CSVs
    ├── zh-TW/                         繁體中文
    ├── en-US/                         English
    ├── ja-JP/                         日本語
    ├── ko-KR/                         한국어
    ├── th-TH/                         ภาษาไทย
    ├── id-ID/                         Bahasa Indonesia (only ui has content; the other 15 are header-only)
    ├── _master/                       Per-language indexes and original notes
    │   ├── zh-CN__index.csv           formerly `zh-CN/00_master/index.csv`
    │   └── zh-CN__README.md           formerly `zh-CN/00_master/README.md`
    └── multilingual/                  Seven-language side-by-side master table (unchanged layout)
        ├── all_languages_master.csv   Master table (102,213 entries × 10 columns)
        └── 00_master/
            ├── README.md              Master table notes
            ├── source_mapping.csv     Source table → category mapping (379 tables)
            └── categories.csv         Definitions of the 16 categories
```

Every language directory contains exactly 16 `<category>.csv` aligned-terminology files and 16
`<category>__terms.csv` term-list files; there are no category subdirectories. The category slug is the
old `NN_xxx/` directory name without its numeric prefix, so `01_character/01_character_glossary.csv` is now
`character.csv` and `01_character/01_character_terms.csv` is now `character__terms.csv`.

## Data Overview

### Entry counts by language

| Language code | Language | Terms | Aligned rows |
| --- | --- | --- | --- |
| `zh-CN` | Simplified Chinese | 102,213 | 196,870 |
| `zh-TW` | Traditional Chinese | 101,915 | 196,972 |
| `en-US` | English | 101,692 | 197,404 |
| `ja-JP` | Japanese | 101,621 | 196,919 |
| `ko-KR` | Korean | 101,760 | 197,663 |
| `th-TH` | Thai | 99,978 | 191,726 |
| `id-ID` | Indonesian | 9,916 | 28,827 |
| **Total** | **7 sets** | **619,095** | **1,206,381** |

> "Terms" is the number of unique text keys (the data-row count of each language's `*_terms.csv` records;
> together they represent 102,213 unique entries across the languages' coverage). "Aligned rows" is the
> data-row count of each language's `*_glossary.csv`, i.e. the sum of its 16 categories. The two numbers
> mean different things and are not interchangeable.
>
> Indonesian (`id-ID`) is officially shipped for interface text (the I18N table) only, and the game data
> tables provide no Indonesian entity names. That set therefore contains just the `13_ui` category — the
> other 15 category CSVs hold a header row and no data — and its counts are far lower than the others'.

### Official language support

The target languages in this database are **limited to text the game officially ships**; nothing is
machine-translated afterwards:

| Language | Status |
| --- | --- |
| `zh-CN` Simplified Chinese | ✅ Officially shipped (source language) |
| `zh-TW` Traditional Chinese | ✅ Officially shipped |
| `en-US` English | ✅ Officially shipped (see the note below) |
| `ja-JP` Japanese | ✅ Officially shipped |
| `ko-KR` Korean | ✅ Officially shipped |
| `th-TH` Thai | ✅ Officially shipped |
| `id-ID` Indonesian | ✅ Officially shipped (interface text only) |
| `fr-FR` / `de-DE` / `es-ES` / `ru-RU` / `pt-BR` / `it-IT` / `tr-TR` / `vi-VN` | ❌ Not officially shipped; not provided here |

**A note on English:** the game data tables carry a single English column, `en_UK`, whereas the I18N text
table carries both `en_UK` and `en_US`. In this database's `en-US` directory, entity names come from the
`en_UK` column, while interface text prefers `en_US` and falls back to `en_UK` when missing. The raw text
of both English variants is preserved in the corresponding columns of
`multilingual/all_languages_master.csv`.

### Categories and counts (using `zh-CN` as the example)

| Category | Theme | Terms | Aligned rows | Content |
| --- | --- | --- | --- | --- |
| `01_character` | Characters and cards | 19,983 | 33,652 | Playable cat-girl (card) names, cat forms, classes, races, skins, signature voice lines and character profiles |
| `02_skill` | Skills and combat effects | 9,228 | 15,059 | Skill names, skill keywords, passive/awakening skills and effect descriptions |
| `03_talent` | Talents and awakening | 2,536 | 4,169 | Character talent names and talent effects |
| `04_equipment` | Equipment and signature weapons | 6,388 | 2,197 | Equipment, signature weapons, gear slots and filter categories |
| `05_item` | Items and materials | 4,650 | 13,090 | Names and descriptions of consumables, gifts, materials, currencies and other items |
| `06_enemy` | Enemies and bosses | 27 | 124 | Enemy targets and related descriptive text |
| `07_stage` | Stages and chapters | 7,278 | 20,995 | Main-story chapters, daily dungeons, mazes, tower climbing and challenge stages |
| `08_event` | Events and game modes | 17,339 | 21,613 | Time-limited events, seasonal events, leaderboards, world bosses and other modes |
| `09_gacha` | Gacha and exchange | 53 | 140 | Banner descriptions, summon missions and exchange rules |
| `10_shop` | Shop and bundles | 4,589 | 1,688 | Shop, battle pass, fashion contracts and various bundles |
| `11_homeland` | Homeland and cat café | 8,913 | 25,223 | Cat café/restaurant, fishing, club, homeland talents and other casual modes |
| `12_system` | Systems and quests | 6,041 | 18,849 | Feature toggles, tutorials, quests, compendium, regional gameplay, check-in, etc. |
| `13_ui` | UI and interface text | 9,923 | 28,822 | Client interface text (taken from the I18N text table) |
| `14_story` | Story proper nouns | 3,180 | 5,480 | Story character names, scene names, subtitles and short skits |
| `15_location` | Locations and regions | 449 | 1,649 | Maps, regions, battle scenes, telephone area codes, etc. |
| `16_terminology` | Gameplay mechanics terminology | 1,636 | 4,120 | Attributes, elements, counter relationships, buffs/debuffs and other mechanical terms |
| **Total** | | **102,213** | **196,870** | |

Per-category counts for every language are in `cat-fantasy-glossary/_master/<language>__index.csv`; the category
definitions are in `cat-fantasy-glossary/multilingual/00_master/categories.csv`.

### File format

Both files in each category folder are saved as **UTF-8 with BOM + CRLF**, so Excel opens them correctly
on a double-click without specifying an encoding.

**`<category>.csv` — aligned terminology table (`source` / `target` / `tgt_lng`)**

The `tgt_lng` column is fixed for a given language, and `source` holds the wording in the other languages
(one row per available language wording of the same entry). It can be imported directly into terminology
tools such as Immersive Translation:

| source | target | tgt_lng |
| --- | --- | --- |
| Asura | 非天 | zh-CN |
| アスラ | 非天 | zh-CN |
| 아수라 | 非天 | zh-CN |

**`<category>__terms.csv` — term list for that language (`id` / `term` / `src_table`)**

| id | term | src_table |
| --- | --- | --- |
| Card.101002.name | 非天 | Card/Card.txt |
| Card.101002.desc | 非天 | Card/Card.txt |

- `id` = `source table name.primary key.field name`, which lets you trace an entry back to the original
  game data table;
- `src_table` = the relative path of that entry inside the official data package
  (under `MasterData\Setting\Data\`).

**`_master/<language>__index.csv`** is the category index and counts for that language (columns:
`category,label,term_count,glossary_count,glossary_file,terms_file,target_language`). Merging all 16
categories in it yields the complete term list for that language.

## Related Sources

| Source repository | Purpose |
| --- | --- |
| [PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy) | Official multilingual data tables (`Setting/Data`) and the I18N text table (`Setting/I18N`), version 2.14.0 |
| [Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1) | Cross-checking the game's data structures (version 2.18.1) |
| [Simplified Chinese site](https://cat.fantanggame.com/) / [Traditional Chinese site](https://tw.catfantasygame.com/) / [English site](https://cat.elex.com/) / [Japanese site](https://jp.catfantasygame.com/) / [Korean site](https://kr.catfantasygame.com/) / [Southeast Asia site](https://catfantasysea.bonfiregathering.com/en/) | Verifying language support |

## Regeneration

**This directory ships no scripts and has no `tools/` folder.** It is a **pure data product**: the
repository contains no generation pipeline code, so there is no runnable command to reproduce it. The
procedure is recorded below as prose so that anyone who wants to reproduce the data can do so against the
upstream packages:

```text
# This database has no scripts and no tools/ directory, so there is no runnable command.
# Generation procedure (data-compilation record):
1. Scan every data table under Setting/Data and identify multilingual field suffixes
   (_zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH); the base column (no suffix) is the zh-CN source text.
2. Map each data table to one of 16 categories by the gameplay module it belongs to (see
   cat-fantasy-glossary/multilingual/00_master/source_mapping.csv — 379 source tables in total).
3. The 13_ui category comes from the Setting/I18N hashed text table, aligned across seven languages by Id.
4. For NewChapter (the story table) only proper nouns such as appearing character and scene names are
   extracted; story dialogue body text is not included in the term database.
5. Within a category, rows are de-duplicated by (source, target); no aligned row is produced when the
   source and target wordings are identical.
6. Each language's `<category>.csv` is expanded from cat-fantasy-glossary/multilingual/all_languages_master.csv by category.

# Data acquisition for reproduction:
#   See "Related Sources" above for the upstream packages; download their Setting/Data and Setting/I18N.
# To verify this database directly, read only (do not modify):
#   cat-fantasy-glossary/_master/zh-CN__index.csv  per-language category index and counts
#   multilingual/all_languages_master.csv     seven-language side-by-side master table
#   cat-fantasy-glossary/multilingual/00_master/source_mapping.csv source table -> category mapping
```

Every set is **aligned by the same text key** and consists of official text rather than re-translation.
Because each entry expands the other languages' wordings into aligned rows, the data also works in reverse
as a "`zh-CN` → other languages" lookup table.

## Known Limitations

- Categories are assigned automatically by data table, so a few entries (such as text shared across game
  modes) may land in an adjacent category.
- Enemy names have no multilingual columns in the game data tables, so the `06_enemy` category is very
  small (only 27 entries in `zh-CN`).
- `id-ID` contains only the `13_ui` category; the other 15 CSVs have a header row and no data.
- Placeholders in the text (such as `_name_`, `_num_`, `#num_percent_0_1_1_`, `\n`) are kept exactly as the
  official text has them and are not substituted.
- The text keys covered differ between languages (for example `th-TH` covers 99,978 entries, and `id-ID`
  covers interface text only), so both term counts and aligned-row counts differ from language to
  language. This is expected.
- Wording may differ between regional versions and game versions; this database follows the versions of
  the data packages referenced above.

## Disclaimer

This directory is an **unofficial** translation terminology database compiled and maintained by an
individual. It is intended solely for personal study, research, and terminology matching in AI translation
software (including but not limited to Immersive Translation). This database has no affiliation,
authorisation, partnership, agency, or official representation relationship with the developers,
publishers, distributors, operators, or rights holders of the games concerned; the translations in it do
not represent any official position, are not guaranteed to be always accurate, complete, or consistent
with the game's current version, and **must not be regarded as the official glossary or official
localisation file of any game**. Intellectual property such as game titles, character names, proper nouns,
and trademarks belongs to their respective rights holders. This database claims no rights over that
third-party intellectual property. All responsibility arising from the use of this project, or of
translation results produced from it, rests with the user. If a rights holder considers any content
inappropriate, please make contact via GitHub Issues / Pull Request and the maintainer will review it and
modify or remove it as appropriate. For the complete terms, see the repository root
`README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation with, authorisation from, partnership with, or agency relationship with this game, its developer, publisher, distributor, or rights holders.**
