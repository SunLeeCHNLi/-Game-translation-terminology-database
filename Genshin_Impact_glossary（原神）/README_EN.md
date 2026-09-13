# Genshin Impact Terminology Database / 《原神》翻译术语库 / Genshin Impact 用語集

## [中文](README.md) [日本語](README_JP.md)

This directory contains a multilingual terminology database for *Genshin Impact*, made of two parts: a **main glossary** covering in-game name data across **14 target languages** (zh-CN / zh-TW / en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-BR / it-IT / tr-TR / th-TH / vi-VN), 27 category CSVs per language, and a **supplement glossary** covering NPCs, place names, quests, events and other terms missing from the main glossary, for 4 target languages (zh-CN / zh-TW / en-US / ja-JP).

The main glossary holds **8,186** distinct terms (all 27 categories combined), **1,252,692** alignment rows and **1,069,738** globally distinct `source/target/tgt_lng` pairs; the supplement glossary adds **51,581** alignment rows and **1,343** alias rows. The two can be used directly on top of each other, because the supplement contains only pairs that the main glossary does not have.

Every translation is taken from the game's own official localized text (the game data files collected by genshin-db / genshin-langdata); **nothing here is a second-hand or machine translation**.

## Usage

1. Single-file download: open `genshin-glossary/<lang-code>/` and download the category CSV you need (TCG categories are in the `TCG/` subdirectory), then import it into terminology tools such as Immersive Translation. Supplement terms live in `genshin-glossary-supplement/<lang-code>/`.
2. Whole-language-directory download: on GitHub, open `genshin-glossary/<lang-code>/` and use the directory download option to get every category file for that target language; the same applies to the supplement glossary.
3. Clone the whole repository, use the scripts under `tools/`, and download the referenced upstream source repositories (genshin-db, genshin-langdata) in advance to reproduce all CSVs yourself.

## Directory Structure

```text
Genshin_Impact_glossary（原神）/
├── README.md                     # Simplified Chinese
├── README_EN.md                  # This file (English)
├── README_JP.md                  # 日本語
├── genshin-glossary/             # Main glossary (genshin-db, 14 target languages, 27 CSVs each)
│   ├── README.md                 # Main glossary notes (generated)
│   ├── zh-CN/                    # Target language = Simplified Chinese
│   │   ├── characters.csv
│   │   ├── talents.csv
│   │   ├── ...                   # 17 top-level category CSVs in total
│   │   └── TCG/                  # TCG categories, split into 10 sub-type CSVs
│   │       ├── action-cards.csv
│   │       └── ...
│   ├── zh-TW/
│   ├── en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
│   ├── pt-BR/  it-IT/  tr-TR/  th-TH/  vi-VN/     # 14 language directories in total
├── genshin-glossary-supplement/  # Supplement glossary (genshin-langdata, 4 target languages)
│   ├── README.md                 # Supplement glossary notes (generated)
│   ├── zh-CN/
│   │   ├── characters.csv        # 9 top-level categories sharing names with the main glossary
│   │   ├── _variants.csv         # Aliases / nicknames / common misspellings, added as extra sources
│   │   └── extra/                # 10 additional categories
│   │       ├── quests.csv
│   │       └── ...
│   ├── zh-TW/  en-US/  ja-JP/    # 4 language directories in total, 20 CSVs each
└── tools/
    ├── build_main_glossary.js    # Builds the main glossary from genshin-db
    ├── build_supplement.mjs      # Builds the supplement from genshin-langdata (needs the main glossary output)
    ├── readme_main.js            # Generates genshin-glossary/README.md
    ├── readme_sup.js             # Generates genshin-glossary-supplement/README.md
    ├── glossary_counts.json      # Main glossary build metadata (entry and row counts per language/category)
    └── supplement_counts.json    # Supplement glossary build metadata
```

## Data Overview

### Main glossary: alignment rows per language

"Alignment rows" = the data rows (header excluded) of all 27 CSVs in that language directory; "CSV files" is the number of CSVs in that language directory.

| Language | Language name | CSV files | Alignment rows |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 27 | 89,790 |
| `zh-TW` | 繁體中文 | 27 | 89,434 |
| `en-US` | English | 27 | 89,412 |
| `ja-JP` | 日本語 | 27 | 89,490 |
| `ko-KR` | 한국어 | 27 | 89,460 |
| `fr-FR` | Français | 27 | 89,613 |
| `de-DE` | Deutsch | 27 | 89,362 |
| `es-ES` | Español | 27 | 89,411 |
| `ru-RU` | Русский | 27 | 89,418 |
| `pt-BR` | Português | 27 | 89,444 |
| `it-IT` | Italiano | 27 | 89,437 |
| `tr-TR` | Türkçe | 27 | 89,423 |
| `th-TH` | ภาษาไทย | 27 | 89,468 |
| `vi-VN` | Tiếng Việt | 27 | 89,530 |
| **Total** | **14 languages** | **378** | **1,252,692** |

> All 14 language directories together contain **1,069,738** globally distinct `source/target/tgt_lng` pairs (after cross-language deduplication).
> Within one language directory, each entry appears once with every one of the other 13 languages as `source` (duplicate and identical rows have been merged).

### Main glossary: top-level categories and entry counts

"Entries" is the number of **distinct terms** in that category (one entry = one named object in the game, counted on the Simplified Chinese side); "Rows per language" is the mean data-row count of that category's CSV across the 14 languages (rounded).

| Category | File | Entries | Rows per language |
| --- | --- | --- | --- |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2,823 |
| materials | `materials.csv` | 919 | 10,637 |
| foods | `foods.csv` | 398 | 4,541 |
| crafts | `crafts.csv` | 295 | 3,522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3,636 |
| enemies | `enemies.csv` | 346 | 4,104 |
| animals | `animals.csv` | 223 | 2,647 |
| outfits | `outfits.csv` | 150 | 1,869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3,606 |
| geographies | `geographies.csv` | 268 | 3,389 |
| achievements | `achievements.csv` | 1,548 | 19,463 |
| adventureranks | `adventureranks.csv` | 21 | 158 |
| **TCG (10 sub-categories combined)** | `TCG/*.csv` | **2,743** | **26,304** |

### Main glossary: TCG sub-categories

| Sub-category | File | Entries |
| --- | --- | --- |
| action-cards | `TCG/action-cards.csv` | 927 |
| character-cards | `TCG/character-cards.csv` | 149 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 |
| summons | `TCG/summons.csv` | 152 |
| status-effects | `TCG/status-effects.csv` | 1,159 |
| keywords | `TCG/keywords.csv` | 139 |
| card-backs | `TCG/card-backs.csv` | 39 |
| card-boxes | `TCG/card-boxes.csv` | 7 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 |
| level-rewards | `TCG/level-rewards.csv` | 26 |

### Supplement glossary: newly added rows per language

| Language | Language name | Top-level category CSVs | Alignment rows | Alias rows (`_variants.csv`) |
| --- | --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 19 | 12,237 | 333 |
| `zh-TW` | 繁體中文 | 19 | 12,221 | 332 |
| `en-US` | English | 19 | 13,815 | 395 |
| `ja-JP` | 日本語 | 19 | 13,308 | 283 |
| **Total** | **4 languages** | **76** | **51,581** | **1,343** |

> Each supplement language directory holds 20 CSVs: 9 top-level categories sharing names with the main glossary, 10 additional categories under `extra/`, and 1 `_variants.csv`.

### Supplement glossary: categories and newly added rows

| Category | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | Total |
| --- | --- | --- | --- | --- | --- |
| artifacts | 28 | 29 | 31 | 32 | 120 |
| characters | 3,873 | 3,796 | 4,609 | 4,221 | 16,499 |
| domains | 216 | 212 | 240 | 226 | 894 |
| materials | 691 | 738 | 741 | 789 | 2,959 |
| enemies | 480 | 518 | 525 | 697 | 2,220 |
| foods | 209 | 259 | 233 | 246 | 947 |
| animals | 157 | 158 | 172 | 175 | 662 |
| geographies | 1,104 | 1,082 | 1,235 | 1,163 | 4,584 |
| weapons | 56 | 75 | 56 | 69 | 256 |
| extra/dialogue | 117 | 115 | 123 | 121 | 476 |
| extra/facilities | 234 | 226 | 270 | 236 | 966 |
| extra/objects | 459 | 447 | 508 | 472 | 1,886 |
| extra/organizations | 213 | 205 | 243 | 209 | 870 |
| extra/quests | 1,664 | 1,652 | 1,769 | 1,753 | 6,838 |
| extra/sereniteapot | 33 | 32 | 37 | 32 | 134 |
| extra/story | 286 | 282 | 348 | 302 | 1,218 |
| extra/system | 357 | 343 | 447 | 387 | 1,534 |
| extra/events | 1,715 | 1,705 | 1,842 | 1,796 | 7,058 |
| extra/archives | 345 | 347 | 386 | 382 | 1,460 |

### File format

The main and supplement glossaries share exactly the same CSV format: three columns `source,target,tgt_lng`, encoded in **UTF-8 with BOM**, **CRLF** line endings, a header row first, and RFC 4180 quoting whenever a field contains a comma or a quote. `target` is the rendering in the language named by `tgt_lng`, and `source` is the same entry as written in **any one of the other languages**.

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | 空 | zh-CN |
| Alhaitham | 艾尔海森 | zh-CN |
| Harbinger of Dawn | 黎明神剑 | zh-CN |

### Data cleaning notes

The following markers in the source data were handled during generation:

| Source form | Handling | Example |
| --- | --- | --- |
| Adjacent `{M#...}{F#...}` gender variants | Keep the masculine form | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| Standalone `{M#…}` / `{F#…}` | Keep the inner text | `#Искатель{F#ница}` → `Искательница` |
| Leading `#` (gender marker) | Removed | `#Éclaireuse 100%` → `Éclaireuse 100%` |
| `{NON_BREAK_SPACE}`, `{SPACE}` | Replaced with a normal space | `PB{NON_BREAK_SPACE}-{NON_BREAK_SPACE}Retorno` → `PB - Retorno` |
| Other placeholders (kept as-is) | `{NICKNAME}`, `{REALNAME[…]}` and `{MATEAVATAR#SEXPRO[…]} ` | 1 row each |

Duplicate rows with the same source and target (for example personal names that look identical in English, French and German) have been merged.

## Related Sources

| Source repository | Purpose |
| --- | --- |
| [theBowja/genshin-db](https://github.com/theBowja/genshin-db) | The only data source for the main glossary `genshin-glossary/`; supplies official in-game name mappings in 14 languages (data version 7.0) |
| [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) | The only data source for the supplement glossary `genshin-glossary-supplement/`; supplies NPC, location, enemy, quest, event and system terms plus aliases, covering en / ja / zh-CN / zh-TW |

## Regeneration

The scripts read **external data directories outside this repository** (local copies of the genshin-db and genshin-langdata sources) and write the CSVs to an external working directory; what this repository keeps is that output plus the build metadata `tools/glossary_counts.json` and `tools/supplement_counts.json`. Run the following from the game directory, in order:

```bash
# 1. Build the main glossary (source: genshin-db); writes 14 language directories + glossary_counts.json
node tools/build_main_glossary.js

# 2. Build the supplement (source: genshin-langdata; also reads the main glossary CSVs from step 1 to deduplicate)
node tools/build_supplement.mjs

# 3. Regenerate both sub-glossary READMEs from the build metadata (written into the external output directory above)
node tools/readme_main.js
node tools/readme_sup.js
```

Dependency order: step 2 reads the output of step 1 (every CSV under `genshin-glossary/`) as its deduplication baseline, so **step 1 must run first**; the two scripts in step 3 only read their own glossary's `_counts.json` build metadata and are independent of each other.
Before reproducing, obtain the sources of [genshin-db](https://github.com/theBowja/genshin-db) and
[xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) and point the path constants at the top of the scripts to your local copies
(`SRC`/`LD`/`OUT` in `build_main_glossary.js` / `build_supplement.mjs`, and `MAIN`/`SUP` in the two readme scripts).

## Disclaimer

This directory is a personal, **unofficial** translation terminology collection, intended only for personal study, research, and terminology matching in AI translation software (including but not limited to Immersive Translation). It has no affiliation, authorization, cooperation, agency or official-representation relationship with the developer, publisher, distributor, operator or rights holder of *Genshin Impact*; the translations here do not represent any official position and are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be treated as the game's official glossary or official localization files**. Intellectual property such as game names, character names, proper nouns and trademarks belongs to their respective rights holders, and this project claims no rights over that third-party intellectual property. Any consequences arising from the use of this project or of translation output based on it are borne solely by the user. If a rights holder considers any content inappropriate, please reach out via GitHub Issues / Pull Request and the maintainer will verify and modify or remove it.

Full terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorization, cooperation or agency relationship with this game or its developer, publisher, distributor or rights holder.**
