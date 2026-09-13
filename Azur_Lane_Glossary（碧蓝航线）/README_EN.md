# Azur Lane Terminology Database / 《碧蓝航线》翻译术语库 / Azur Lane 用語集

## [中文](README.md) [日本語](README_JP.md)

This repository collects ship names and naval / military / in-game terminology for the mobile game
*Azur Lane* (《碧蓝航线》) in **4 target languages**: Simplified Chinese (`zh-CN`), English (`en-US`),
日本語 (`ja-JP`) and 한국어 (`ko-KR`).
It covers **891 ships** (base hulls as well as META, μ-equipment, Type-II and collab ships, i.e.
**884 shipgirls** in the generated tables) and **176 terminology concepts** (175 of which have
counterpart readings in the other languages).
Every ship name is extracted directly from the official multilingual client data
(CN / EN / JP / KR / TW `sharecfgdata` / `ShareCfg`; Simplified-Chinese client data version 9.6.667 at
extraction time), so the translations are **official localisation text** — neither machine translated
nor re-translated from English; the terminology table is curated by hand and checked entry by entry
against each client, and the harmonised (和谐) names are additionally cross-checked against a
community reference table.

## Usage

1. **Single-file download**: open the language directory you need (e.g. `en-US/`) and download
   `azur_lane_glossary.csv`, `azur_lane_ship_character_glossary.csv` or `azur_lane_terms.csv`;
   these can be imported directly into terminology tools such as Immersive Translate.
2. **Whole-directory download**: get every ship-name and terminology entry for one language at once
   (including the `*_detailed.csv` detail tables).
3. **Clone the whole repository and reproduce**: rerun the generation pipeline with the scripts under
   `tools/` together with the upstream `AzurLaneData` client data (see "Related Sources").

## Directory Structure

```text
Azur_Lane_Glossary（碧蓝航线）/
├─ zh-CN/                                  Simplified-Chinese termbase (target = zh-CN)
│     azur_lane_glossary.csv                   ship names (Simplified-Chinese standard name as source)
│     azur_lane_glossary_detailed.csv          same + ship_id / hull type / faction / variant
│     azur_lane_ship_character_glossary.csv    ship names (Simplified-Chinese harmonised name as source)
│     azur_lane_ship_character_glossary_detailed.csv
│     azur_lane_terms.csv                      naval / military / in-game terminology
│     azur_lane_terms_detailed.csv             same + category / same_source_alternatives
│     azur_lane_ambiguous.csv                  source strings with more than one reading (zh-CN only)
│     azur_lane_combined_ships_and_terms.csv   ships + terminology merged (zh-CN only)
│     README.md                                documentation for this directory (Simplified Chinese)
├─ en-US/                                  the same 6 CSVs + README.md / README_zh-CN.md
├─ ja-JP/                                  the same 6 CSVs + README.md / README_zh-CN.md
├─ ko-KR/                                  the same 6 CSVs + README.md / README_zh-CN.md
├─ by_language/                            ship sub-tables split by source language, target is always zh-CN
│     azur_lane_glossary_en-zh-CN.csv
│     azur_lane_glossary_ja-zh-CN.csv
│     azur_lane_glossary_ko-zh-CN.csv
│     azur_lane_glossary_zh-TW-zh-CN.csv
├─ sources/
│     moegirl_name_table.json              scrape of the Moegirlpedia “Azur Lane / name table”, used for cross-checking
├─ tools/                                  generation scripts and statistics metadata
│     build_glossary.py                        ship termbase (zh-CN standard names) + 5-language master table + by_language + ambiguity table + IJN code aliases
│     build_harmonized.py                      harmonised-name mapping
│     build_ship_character_glossary.py         shipgirl termbase (zh-CN harmonised names)
│     build_multilang_glossaries.py            en-US / ja-JP / ko-KR variants of the ship tables
│     build_terms_glossaries.py                4-language variants of the terminology tables
│     terms_data.py                            terminology source data (curated by hand)
│     build_stats.json                         generation statistics (output of the last build)
├─ azur_lane_ship_names_multilingual.csv   5-language master table of 891 ships (zh / en / ja / zh-TW / ko, source data)
├─ azur_lane_harmonized_ship_names.csv     harmonised-name mapping (original → harmonised, 1187 rows)
├─ azur_lane_harmonized_names_detailed.csv harmonised-name detail (1259 rows, with Moegirlpedia check notes)
├─ azur_lane_harmonized_equipment.csv      8 harmonised aircraft / equipment names
├─ azur_lane_ijn_codename_aliases.csv      IJN single-character code-name mapping (柚 → 绫波, 1082 rows)
└─ README.md / README_EN.md / README_JP.md Chinese / English / Japanese documentation
```

All four language directories share exactly the same entry files (`zh-CN` additionally ships
`azur_lane_ambiguous.csv` and `azur_lane_combined_ships_and_terms.csv`): `target` holds the name in
that language and `tgt_lng` is fixed to `zh-CN` / `en-US` / `ja-JP` / `ko-KR` respectively, while
`source` holds the readings of all the other languages.
`by_language/` is the **source-language view** of the same ships (English 1544 rows, Japanese 696,
Korean 814, Traditional Chinese 538 — 3592 rows in total, equal to the row count of
`zh-CN/azur_lane_glossary_detailed.csv`).

## Data Overview

### Entry counts and comparison rows

| Language | Ship names · zh-CN standard as source<br>entries / rows | Ship names · zh-CN harmonised as source<br>entries / rows | Terminology<br>entries / rows |
| --- | --- | --- | --- |
| `zh-CN` | 877 / 3514 | 875 / 3804 | 170 / 449 |
| `en-US` | 821 / 2795 | 855 / 3084 | 154 / 404 |
| `ja-JP` | 877 / 3516 | 877 / 3805 | 125 / 356 |
| `ko-KR` | 850 / 3481 | 850 / 3769 | 165 / 459 |

- **Entries** = distinct values of the `target` column in that language directory's `azur_lane_*.csv`
  (i.e. how many ships / terms have a name in that language); **rows** = CSV data rows excluding the
  header (UTF-8 with BOM + CRLF, so Excel opens them directly).
- Detail tables: `azur_lane_glossary_detailed.csv` has 3592 (zh-CN) / 2809 (en-US) / 3596 (ja-JP) /
  3525 (ko-KR) rows; `azur_lane_ship_character_glossary_detailed.csv` has 3890 / 3104 / 3890 / 3818 rows.
- Two extra tables exist in `zh-CN` only: `azur_lane_ambiguous.csv` with 162 rows (covering 77 source
  strings that have more than one reading) and `azur_lane_combined_ships_and_terms.csv` with 3985 rows
  (3592 ship rows + 475 terminology rows, merged and de-duplicated).

### Categories and counts

Ship variants (measured on `zh-CN/azur_lane_ship_character_glossary_detailed.csv`, **884 shipgirls**):

| Variant | Ships | Rows |
| --- | --- | --- |
| Base hull (no variant tag) | 795 | 3466 |
| META | 60 | 280 |
| μ-equipment | 19 | 101 |
| Type II | 10 | 43 |
| **Total** | **884** | **3890** |

Terminology categories (measured on `zh-CN/azur_lane_terms_detailed.csv`):

| `category` | Topic | Concepts | Rows |
| --- | --- | --- | --- |
| `hull_type` | Hull / ship types | 31 | 97 |
| `naval_term` | Naval and military terms | 72 | 198 |
| `navy_prefix` | Factions and hull prefixes | 24 | 59 |
| `rank` | Ranks | 24 | 44 |
| `game_term` | In-game terminology | 24 | 61 |
| **Total** | — | **175** | **459** |

`tools/terms_data.py` holds **478** curated source forms (English 175, Japanese 127, Korean 176);
they are de-duplicated on `(source, target, src_lng)` when written out. The `META` concept
(category `navy_prefix`) is dropped because its source string equals its Chinese target string, which
is why only 175 concepts end up with comparison rows in the generated tables.

### Shipgirl termbase

| File | zh-CN | en-US | ja-JP | ko-KR |
| --- | --- | --- | --- | --- |
| `azur_lane_glossary.csv` (zh-CN standard name as source) | 3514 | 2795 | 3516 | 3481 |
| `azur_lane_ship_character_glossary.csv` (zh-CN harmonised name as source) | 3804 | 3084 | 3805 | 3769 |

- Covers **891 ships / 884 shipgirls**, including META, μ-equipment, Type-II and collab ships.
- The `target` of `azur_lane_ship_character_glossary` is always the name **actually displayed by the
  Simplified-Chinese client**: the harmonised name where one exists (**295 shipgirls**), otherwise the
  standard Chinese name. The other language variants use that language's ship name as `target`.
- Source languages include: Simplified-Chinese standard name, Simplified-Chinese harmonised name,
  English name, English full hull designation (e.g. `IJN Fubuki`), Japanese name, Traditional-Chinese
  name and Korean name.
- Examples (actual rows from every language directory, `azur_lane_glossary.csv`):

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| Enterprise                | 企业               | zh-CN   |
| エンタープライズ                 | 企业               | zh-CN   |
| Sheffield META            | 谢菲尔德·META        | zh-CN   |
| シェフィールド(META)             | 谢菲尔德·META        | zh-CN   |
| Illustrious μ             | 光辉(μ兵装)          | zh-CN   |
| イラストリアス(μ兵装)              | 光辉(μ兵装)          | zh-CN   |
```

- Examples (`azur_lane_ship_character_glossary.csv`, harmonised zh-CN name as source; `柚` is the
  Simplified-Chinese harmonised name of `绫波`):

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| 柚                         | Ayanami           | en-US   |
| 柚                         | 綾波                | ja-JP   |
| 柚                         | 아야나미               | ko-KR   |
| 绫波                        | Ayanami           | en-US   |
```

- Each source string keeps exactly one translation in the main table; when a source string has several
  readings the one with the **lowest ship id** wins and every reading is recorded in the
  `same_source_alternatives` column of the detail table. For example, in
  `ja-JP/azur_lane_glossary_detailed.csv` the source `HMS Belfast` maps to both `ベルファスト`
  (id 202121) and `ベルちゃん` (id 202181); the main table keeps `ベルファスト`, and both readings
  appear in `same_source_alternatives`. On the `zh-CN` side they are `贝尔法斯特` / `小贝法`.
- **亚尔薇特 (Alvitr, an Iron Blood battlecruiser, ship_id 404061)** is the only Iron Blood shipgirl
  without a harmonised name — neither the game data nor the community table has an entry for it.

### Naval / military / in-game terminology

`azur_lane_terms.csv`: **176 curated concepts** (175 of which get comparison rows in the generated
tables), from 478 curated source forms (English 175, Japanese 127, Korean 176).

| Target language | Entries |
| --- | --- |
| `zh-CN/azur_lane_terms.csv` | 449 |
| `en-US/azur_lane_terms.csv` | 404 |
| `ja-JP/azur_lane_terms.csv` | 356 |
| `ko-KR/azur_lane_terms.csv` | 459 |

- Five categories: `hull_type` 31, `naval_term` 72, `navy_prefix` 24, `rank` 24, `game_term` 24
  (the detail table carries `category` / `category_zh` columns).
- When one source word covers several concepts (e.g. the Korean `대령` is both "naval captain" and
  "colonel"), the main table keeps the first concept and the other readings are written into the
  `same_source_alternatives` column of the detail table.
- Examples (`ko-KR/azur_lane_terms.csv`):

```
| source         | target   | tgt_lng |
| -------------- | -------- | ------- |
| 驱逐舰            | 구축함      | ko-KR   |
| Destroyer      | 구축함      | ko-KR   |
| 駆逐艦            | 구축함      | ko-KR   |
| 铁血             | 메탈 블러드   | ko-KR   |
| Iron Blood     | 메탈 블러드   | ko-KR   |
| 海军上将           | 대장       | ko-KR   |
```

- **Korean sources**: hull types, faction names and in-game wording come from the KR client itself
  (`ship_data_by_type` → `구축/경순/중순/…`, `fleet_tech_group` → `이글 유니온`/`메탈 블러드`,
  `world_port_data`, `medal_template`, `emoji_template` → `한계돌파`, `enemy_data_statistics` →
  `특장형 부린`, …); the remaining naval and rank words are the standard Korean equivalents. The game
  itself displays abbreviated hull types (구축 / 경순 / …), while the terminology table always uses the
  full form (구축함 / 경순양함 / …).

### Fields and data cleaning

- `source` = source term, `target` = term in the target language, `tgt_lng` = target language,
  `src_lng` = source language (detail tables only).
- The extraction already handles: misplaced English names (`english_name` is unreliable in the
  CN/JP/KR/TW clients and is always taken from the EN client), festival skin codes
  (`qipao`/`shengdan`/`xinnian` …) leaking into names, duplicates between a ship and its skin / event
  copies, enemy and NPC copies (filtered with `ship_data_template`), and `？？？？？` placeholder names.
- Ship identity follows `ship_group` in `ship_skin_template.json`.
- **Untranslated fallback**: when a client simply reuses the Simplified-Chinese string the name counts
  as untranslated, but it is dropped only for clients that do **not** write in Han script (EN, KR).
  Japanese and Traditional-Chinese names legitimately coincide with the Simplified string
  (e.g. `吹雪`, `雷`, `杜威`, `Z1`) and are always kept.
- A handful of ships have no English name at all in the EN client (e.g. `企业·META`); for those the
  EN client's own `english_name` is used instead (with the `USS`/`HMS` hull prefix stripped).
- Detail-table column names differ slightly between `zh-CN` and the other three languages: `zh-CN`
  uses `ship_type` / `nation`, while the others use `ship_type_zh` / `ship_type_en` / `nation_zh` /
  `nation_en` and additionally carry `zh_CN_form` / `zh_CN_standard` / `zh_CN_harmonised`.

### Known data flaws

- In the EN client the ship name of `皇家方舟·META` is stored as `Royal.META` (the `Ark` is missing),
  which contradicts that client's own `english_name`, `Ark Royal.META`. This is a flaw in the original
  game data and has not been rewritten by hand.

## Related Sources

| Source | Purpose |
| --- | --- |
| [AzurLaneTools/AzurLaneData](https://github.com/AzurLaneTools/AzurLaneData) | Client data for the CN / EN / JP / KR / TW servers: `sharecfgdata/ship_data_statistics.json` (ship names per server), `sharecfgdata/ship_data_template.json` (ship identity filter), `ShareCfg/ship_skin_template.json` (`ship_group` normalisation), `ShareCfg/ship_data_by_type.json` (hull-type names), `ShareCfg/name_code.json` (harmonised names and IJN code names) |
| Moegirlpedia, [碧蓝航线/名称对照表](https://zh.moegirl.org.cn/碧蓝航线/名称对照表) | Cross-checking of harmonised names; the scrape is stored in `sources/moegirl_name_table.json` and any mismatch is noted in the `wiki_note` column of `azur_lane_harmonized_names_detailed.csv` |

## Regeneration

The scripts live in `tools/` and are always invoked with the `tools/` prefix (run them from the game
directory):

```bash
# 1) ship termbase (zh-CN standard names) + 5-language master table + by_language + ambiguity table + IJN code aliases
python tools/build_glossary.py

# 2) harmonised-name mapping (needs the 5-language master table from step 1)
python tools/build_harmonized.py

# 3) shipgirl termbase (zh-CN harmonised names)
python tools/build_ship_character_glossary.py

# 4) en-US / ja-JP / ko-KR variants of the ship tables (needs the master table from step 1)
python tools/build_multilang_glossaries.py

# 5) zh-CN / en-US / ja-JP / ko-KR variants of the terminology tables (data in tools/terms_data.py)
python tools/build_terms_glossaries.py
```

After a game-data update simply rerun the steps in this order (`build_harmonized.py` and
`build_multilang_glossaries.py` depend on the `azur_lane_ship_names_multilingual.csv` produced by
`build_glossary.py`).
Terminology entries are maintained in `tools/terms_data.py` and the four language variants are
generated by `build_terms_glossaries.py`; the generation statistics are written to `build_stats.json`
(the copy inside this repository is `tools/build_stats.json`).
Note: the `BASE` / `OUT` path constants inside the scripts point to an upstream client-data directory
and a build working directory that live **outside** this repository, so adjust them for your machine
before rerunning (see the constants at the top of each script); this repository holds the published
snapshot of the generated results.

## Disclaimer

This directory is an **unofficial** translation-terminology resource compiled and maintained by an
individual. It is intended only for personal study and research and for assisting terminology matching
in AI translation software (including but not limited to Immersive Translate). This repository has no
affiliation, authorisation, cooperation, agency or official-representation relationship whatsoever with
the developers, publishers, distributors, operators or copyright holders of the games involved; the
translations here do not represent any official position and are not guaranteed to be accurate,
complete or consistent with the current game version, and **must not be regarded as the official
glossary or official localisation file of any game**. All intellectual property in game names,
character names, proper nouns and trademarks belongs to its respective owners; no claim is made to any
such third-party intellectual property. Any and all liability arising from the use of this project or
of translation results derived from it rests with the user. If a rights holder considers any content
inappropriate, please contact us through GitHub Issues / Pull Request and the maintainers will verify
and amend or remove it.

The full terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorisation, cooperation or agency relationship with the games involved or their developers, publishers, distributors or copyright holders.**
