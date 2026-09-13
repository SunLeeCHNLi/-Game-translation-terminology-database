# Arknights Terminology Database / 《明日方舟》翻译术语库 / アークナイツ 用語集

## [中文](README.md) [日本語](README_JP.md)

*Arknights* is a tower-defense strategy mobile game developed by Hypergryph.

This directory is a multilingual terminology database extracted and organised from the **official client
data tables of every regional server** (`cn` / `tw` / `en` / `jp` / `kr` — five servers in total). It
contains **23,840** aligned entries and **266,111** glossary rows, split by **target language** into
**5** independent glossaries (Simplified Chinese, Traditional Chinese, English, Japanese, Korean),
each of which is further divided into **20** categories and holds **13,000–14,100** distinct terms.

> **23,840** is the category-level aligned entry count (the sum, over categories, of the unique IDs
> aligned across the five regions); **266,111** is the total number of CSV data rows across 5 language
> directories × 20 categories. The two figures use different units — do not mix them.

Every translation is taken from the official client localisation and aligned entry by entry on the same
item ID, so it is **not a second-hand or machine translation**.

## Usage

1. **Download a single file**: open `glossary/<language code>/` and download the `NN_<category>.csv`
   you need. Each file has three columns (`source,target,tgt_lng`) and can be imported directly into
   terminology tools such as Immersive Translation. For an English→Chinese list, download
   `glossary/zh-CN/01_干员名称.csv`.
2. **Download a whole language folder**: open `glossary/<language code>/` and download the entire
   directory, or grab the `_all.json` inside it (all 20 categories of that language merged into one
   UTF-8 JSON file without BOM).
3. **Clone the whole repository and reproduce it**: clone this repository, download the upstream
   repositories listed under “Related Sources”, and regenerate everything with the scripts in `tools/`
   (see “Regeneration”).

## Directory Structure

```text
Arknights_glossary（明日方舟）/
├── README.md                 # This file's Chinese original
├── README_EN.md              # English readme
├── README_JP.md              # Japanese readme
├── glossary/                 # The terminology data product
│   ├── README.md             # Detailed glossary notes (categories / sources / method)
│   ├── zh-CN/                # Target language = Simplified Chinese
│   │   ├── README.md         # Simplified Chinese notes
│   │   ├── 01_干员名称.csv
│   │   ├── 02_干员异格.csv
│   │   ├── ...
│   │   ├── 20_游戏机制.csv
│   │   └── _all.json         # The 20 categories above merged into JSON
│   ├── zh-TW/                # Target language = Traditional Chinese (same layout as zh-CN)
│   ├── en-US/                # Target language = English (same layout as zh-CN)
│   ├── ja-JP/                # Target language = Japanese (same layout as zh-CN)
│   └── ko-KR/                # Target language = Korean (same layout as zh-CN)
└── tools/                    # Build scripts and metadata
    ├── build_glossary.py     # Reads the external _data/gamedata, writes glossary/
    ├── write_readme.py       # Generates glossary/README.md from _summary.json
    └── _summary.json         # Entry counts, all-5-language counts and per-language row counts
```

Every language directory (`glossary/zh-TW/`, `glossary/en-US/`, `glossary/ja-JP/`, `glossary/ko-KR/`)
is exactly parallel to `zh-CN/`: one `README.md` in that language, one `README_zh-CN.md` in Simplified
Chinese, 20 category CSVs and one `_all.json`.

## Data Overview

### Rows and entries per language

“Entries” means the number of **distinct target-language terms** in that language directory
(the 20 categories pooled together and de-duplicated).

| Language code | Language | Categories | Glossary rows | Entries (sum over categories) | Entries (de-duplicated) | Download |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `zh-CN` | Simplified Chinese | 20 | 53,207 | 14,101 | 13,054 | [`glossary/zh-CN/`](glossary/zh-CN/) |
| `zh-TW` | Traditional Chinese | 20 | 53,145 | 14,080 | 13,040 | [`glossary/zh-TW/`](glossary/zh-TW/) |
| `en-US` | English | 20 | 53,269 | 13,965 | 12,886 | [`glossary/en-US/`](glossary/en-US/) |
| `ja-JP` | Japanese | 20 | 53,262 | 13,920 | 12,893 | [`glossary/ja-JP/`](glossary/ja-JP/) |
| `ko-KR` | Korean | 20 | 53,228 | 13,950 | 12,861 | [`glossary/ko-KR/`](glossary/ko-KR/) |
| **Total** | | | **266,111** | | | |

> The same term (for example same-named stages or enemies of different levels) appears in several
> categories at once, so the de-duplicated figure is lower than the plain sum. **266,111 rows** is the
> total of all CSV data rows across 5 language directories × 20 categories.

### Categories × rows

Category names stay in Chinese in every language directory (so that they line up across languages);
the English and Japanese titles are given below for convenience.

| Category file | Topic | 日本語 | zh-CN | zh-TW | en-US | ja-JP | ko-KR |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `01_干员名称` | Operator names | オペレーター名 | 1,452 | 1,446 | 1,451 | 1,452 | 1,451 |
| `02_干员异格` | Operator alters | 異格オペレーター | 130 | 130 | 130 | 130 | 130 |
| `03_职业与分支` | Classes & branches | 職業と分岐 | 285 | 285 | 284 | 285 | 284 |
| `04_技能名称` | Skill names | スキル名 | 4,913 | 4,868 | 4,913 | 4,913 | 4,912 |
| `05_技能描述关键术语` | Skill description terms | スキル説明の重要用語 | 1,174 | 1,171 | 1,067 | 1,134 | 1,138 |
| `06_天赋` | Talents | 天賦 | 2,114 | 2,105 | 2,114 | 2,114 | 2,114 |
| `07_潜能` | Potential | 潜在能力 | 443 | 443 | 439 | 439 | 439 |
| `08_模组` | Modules | モジュール | 3,304 | 3,283 | 3,303 | 3,304 | 3,303 |
| `09_敌人` | Enemies | 敵 | 4,986 | 5,088 | 5,088 | 5,088 | 5,088 |
| `10_BOSS` | Bosses | BOSS | 709 | 709 | 709 | 709 | 709 |
| `11_关卡` | Stages | ステージ | 7,817 | 7,784 | 7,799 | 7,821 | 7,826 |
| `12_地区` | Regions | 地域 | 702 | 702 | 716 | 702 | 707 |
| `13_阵营` | Factions | 陣営 | 167 | 167 | 167 | 167 | 167 |
| `14_活动` | Events | イベント | 839 | 824 | 836 | 835 | 835 |
| `15_道具` | Items | アイテム | 2,013 | 1,984 | 2,007 | 2,011 | 2,007 |
| `16_装备` | Equipment | 装備（戦術・生息演算・秘録） | 4,971 | 4,991 | 5,045 | 4,954 | 4,949 |
| `17_材料` | Materials | 素材 | 2,494 | 2,488 | 2,494 | 2,494 | 2,494 |
| `18_剧情专有名词` | Story proper nouns | ストーリー固有名詞 | 4,961 | 4,934 | 4,961 | 4,958 | 4,962 |
| `19_UI与系统术语` | UI & system terms | UI・システム用語 | 8,789 | 8,799 | 8,822 | 8,813 | 8,777 |
| `20_游戏机制` | Game mechanics | ゲームシステム | 944 | 944 | 924 | 939 | 936 |
| **Total** | | | **53,207** | **53,145** | **53,269** | **53,262** | **53,228** |

> The figures are **CSV data rows** (header excluded). One entry expands into several rows — one per
> source language — and a row whose `source` is identical to its `target` is not written at all, which
> is why the per-language totals differ slightly. Category-level **unique ID counts** and
> “present in all 5 languages” counts are in [`glossary/README.md`](glossary/README.md).

### File format

Every CSV has three columns and is stored as **UTF-8 with BOM + CRLF** (Excel opens it correctly by
double-clicking, with no mojibake):

| source | target | tgt_lng |
| --- | --- | --- |
| Amiya | 阿米娅 | zh-CN |
| アーミヤ | 阿米娅 | zh-CN |
| 阿米婭 | 阿米娅 | zh-CN |
| 아미야 | 阿米娅 | zh-CN |

- `target` — the official localised term in the target language of that file;
- `tgt_lng` — the target language tag, identical to the containing directory name;
- `source` — the same entry as written in the **other four languages**.

## Related Sources

| Repository | Purpose |
| --- | --- |
| [ArknightsAssets/ArknightsGamedata](https://github.com/ArknightsAssets/ArknightsGamedata) | **Primary data**: unpacked tables of the official clients of every region (`character_table` / `skill_table` / `stage_table` / `enemy_handbook_table` / `uniequip_table` / `item_table` / `i18n/string_map.txt` etc.). The `cn` / `tw` / `en` / `jp` / `kr` regions — five servers in total — coexist with identical table structures and form the basis of this glossary |
| [ArchyCillp/ArknightsTranslationContrast](https://github.com/ArchyCillp/ArknightsTranslationContrast) | **Cross-checking**: used for spot-checking operator and skill name translations |
| [flandia/ArknightsGameDataComposite](https://github.com/flandia/ArknightsGameDataComposite) | **Structural reference**: covers only 4 languages (no Traditional Chinese) and has fewer entries, so it was not used as a data source — comparison only |

Data versions per server (upstream `data_version.txt`):

| Server | Version |
| --- | --- |
| Simplified Chinese (`cn`) | `rel77.0` (2026-08-31) |
| English (`en`) | `51.4.0` |
| Traditional Chinese (`tw`) | `50.8.0` |
| Japanese (`jp`) | no separate version number is published upstream; follows the unpacking batch |
| Korean (`kr`) | no separate version number is published upstream; follows the unpacking batch |

> Because the servers are at different points of the release schedule, the newest content may not yet
> be live in the Japanese / English / Korean / Traditional Chinese clients, and such entries do not
> appear here (an ID must exist in at least two languages, and produce at least two distinct rows).

## Regeneration

```bash
# 1) Build the glossary for all 5 language directories
#    (reads <game root>/_data/gamedata, writes <game root>/glossary/)
python tools/build_glossary.py

# 2) Regenerate glossary/README.md from tools/_summary.json
python tools/write_readme.py
```

**Directory check** (make sure the scripts write to the right place):

```bash
python tools/build_glossary.py    # must output to glossary/, not tools/glossary/
python tools/write_readme.py      # must update glossary/README.md
```

> `_data/gamedata` is an **external data directory** (the five-server unpacked output of the upstream
> `ArknightsGamedata` repository). It is **not distributed with this repository**, so you must download
> it yourself as described under “Related Sources” before you can reproduce the build.

Method (summary; the full description is in [`glossary/README.md`](glossary/README.md)):

1. **Align by ID** — every table is keyed by its entry ID (`char_002_amiya`, `skchr_amiya_2`, …), and the
   values of the same ID across the five servers are grouped together;
2. **Name-like categories** take official fields directly (operator, skill, stage, enemy names, …);
3. **Description-like categories** (`05_技能描述关键术语` and part of `20_游戏机制`) use
   **placeholder segmentation + corpus-wide voting**: markers such as `<@ba.vup>` or `{atk:0%}` are
   byte-identical in every language, so splitting on them yields structurally aligned fragments; the
   most frequent rendering of each Chinese fragment is then chosen across the corpus, which cancels out
   word-order differences;
4. **Cleaning** — rich-text tags, line breaks, paired quotation marks and CJK title marks are removed,
   and purely numeric or purely symbolic fragments are dropped;
5. Rows are de-duplicated per category on `(source, target)`, and rows whose source equals their target
   are not written.

## Disclaimer

This directory is an **unofficial** translation terminology database compiled and maintained by an
individual. It is intended only for personal study, research, and terminology matching in AI translation
software (including but not limited to Immersive Translation). It has no affiliation, authorisation,
partnership, agency or official-representation relationship with the developers, publishers,
distributors, operators or rights holders of the games concerned; the translations in it do not
represent any official position, are not guaranteed to be accurate, complete or consistent with the
current game version, and **must not be regarded as the official glossary or official localisation file
of any game**. Game titles, character names, proper nouns, trademarks and other intellectual property
belong to their respective rights holders, and this project claims no rights over them. All
responsibility arising from the use of this project and of translations produced from it rests with the
user. Rights holders who consider any content inappropriate are welcome to make contact through GitHub
Issues / Pull Requests, and the maintainer will verify and then amend or remove it. The complete terms
are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation,
authorisation, partnership or agency relationship with this game or its developer, publisher,
distributor or rights holders.**
