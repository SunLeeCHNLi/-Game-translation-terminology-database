# Minecraft Multilingual Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

Split into separate folders by **target language**, with files stored by **category** inside each folder; system and text categories are kept together in the `extra/` subfolder of each language.

## Data Sources

- Main glossary: the **official Minecraft Java Edition language files**, taken from the `assets` branch of [misode/mcmeta](https://github.com/misode/mcmeta) (`assets/minecraft/lang/<locale>.json`), covering all 14 target languages.
- The category structure follows the classification used in [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) for `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` and so on; the `particles` and `sounds` in that library have only internal IDs and no localized names in the official language files, so they are not separate categories here.
- Supplement glossary: see the `minecraft-glossary-supplement/` directory at the same level (source: [Minecraft Wiki 译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)), which additionally provides the Wiki standard translations, covering Simplified Chinese / Traditional Chinese.
- Image asset library [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) stores textures by version branch; this glossary uses its language file structure as a proofreading reference.

## Directory Structure

```
minecraft-glossary（我的世界）/
├── minecraft-glossary/       # Main glossary: 14 target languages × 34 categories
│   ├── zh-CN/                # Target language = Simplified Chinese
│   │   ├── blocks.csv        # Main categories (game content), 19 files
│   │   ├── items.csv
│   │   ├── ...
│   │   └── extra/            # System and text categories, 15 files
│   │       ├── subtitles.csv
│   │       └── ...
│   ├── zh-TW/
│   ├── en-US/ ... vi-VN/     # 14 language folders in total
│   └── README.md             # This file
├── minecraft-glossary-supplement/   # Supplement glossary (Wiki standard translations), 2 languages × 13 categories
└── tools/                    # Build scripts and metadata
    ├── build_glossary.py
    ├── build_wiki_supplement.py
    ├── make_readme.py
    ├── verify_output.py
    ├── glossary_counts.json      # Entry counts per language and per category for the main glossary
    └── supplement_counts.json    # Entry counts per language and per category for the supplement glossary
```

## File Format

All CSVs are encoded in **UTF-8 (with BOM)**, use **CRLF** line endings, and have a header row; fields containing commas or quotes are escaped with quotes according to RFC 4180.

| source | target | tgt_lng |
| --- | --- | --- |
| Abbaueffizienz | 挖掘效率 | zh-CN |
| 採掘効率 | 挖掘效率 | zh-CN |

Meaning: for the target language specified by `tgt_lng`, `target` is the translation and `source` is the original text **in any of the other languages**.
That is, within each language folder, the same entry appears once for each of the other 13 languages used as the `source` (duplicate rows and identical rows have been merged).

## Language Codes

| Language folder | Language | Minecraft language file locale |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `zh_cn` |
| `zh-TW` | 繁體中文 | `zh_tw` |
| `en-US` | English | `en_us` |
| `ja-JP` | 日本語 | `ja_jp` |
| `ko-KR` | 한국어 | `ko_kr` |
| `fr-FR` | Français | `fr_fr` |
| `de-DE` | Deutsch | `de_de` |
| `es-ES` | Español | `es_es` |
| `ru-RU` | Русский | `ru_ru` |
| `pt-BR` | Português | `pt_br` |
| `it-IT` | Italiano | `it_it` |
| `tr-TR` | Türkçe | `tr_tr` |
| `th-TH` | ภาษาไทย | `th_th` |
| `vi-VN` | Tiếng Việt | `vi_vn` |

## Categories and Entry Counts

"Entry count" means the number of **game name objects** corresponding to that classification in the official language files (the number of keys in that classification, including a small number of keys the official files leave untranslated),
i.e. the total number of entries in that classification that participate in the comparison for this target language; "row count" is the number of data rows of that category's CSV inside the language folder.
The two numbers differ: one entry generates one row for each of the other 13 languages used as the `source`.

### Main Categories (game content)

| Category | File | Description | Entry count | Rows per language (zh-CN) |
| --- | --- | --- | --- | --- |
| blocks | `blocks.csv` | Blocks | 1975 | 25426 |
| items | `items.csv` | Items | 803 | 9061 |
| entities | `entities.csv` | Entities | 219 | 2582 |
| biomes | `biomes.csv` | Biomes | 67 | 835 |
| enchantments | `enchantments.csv` | Enchantments | 54 | 553 |
| effects | `effects.csv` | Status effects | 42 | 514 |
| instruments | `instruments.csv` | Instruments | 8 | 98 |
| materials | `materials.csv` | Armor trim materials | 11 | 143 |
| paintings | `paintings.csv` | Paintings | 104 | 315 |
| attributes | `attributes.csv` | Attributes | 83 | 555 |
| item-groups | `item-groups.csv` | Inventory categories | 16 | 198 |
| jukebox-songs | `jukebox-songs.csv` | Music disc tracks | 22 | 42 |
| trim-patterns | `trim-patterns.csv` | Armor trim patterns | 18 | 234 |
| colors | `colors.csv` | Colors | 16 | 184 |
| statistics | `statistics.csv` | Statistics | 88 | 1143 |
| maps | `maps.csv` | Maps | 33 | 422 |
| music | `music.csv` | Music tracks | 70 | 192 |
| sound-categories | `sound-categories.csv` | Sound categories | 11 | 133 |
| game-modes | `game-modes.csv` | Game modes | 6 | 77 |

### `extra/` Categories (system and text)

| Category | File | Description | Entry count | Rows per language (zh-CN) |
| --- | --- | --- | --- | --- |
| subtitles | `extra/subtitles.csv` | Subtitles | 1023 | 12407 |
| death-messages | `extra/death-messages.csv` | Death messages | 106 | 1334 |
| advancement-titles | `extra/advancement-titles.csv` | Advancement titles | 127 | 1603 |
| advancement-descriptions | `extra/advancement-descriptions.csv` | Advancement descriptions | 127 | 1641 |
| gamerules | `extra/gamerules.csv` | Game rules | 117 | 1490 |
| commands | `extra/commands.csv` | Commands and arguments | 856 | 10758 |
| gui | `extra/gui.csv` | Interface text | 581 | 6604 |
| options | `extra/options.csv` | Settings and key bindings | 754 | 8165 |
| multiplayer | `extra/multiplayer.csv` | Multiplayer | 173 | 2013 |
| realms | `extra/realms.csv` | Realms | 426 | 4962 |
| world-management | `extra/world-management.csv` | World management | 294 | 3578 |
| resource-packs | `extra/resource-packs.csv` | Resource packs and data packs | 62 | 761 |
| telemetry | `extra/telemetry.csv` | Telemetry | 70 | 897 |
| dev-tools | `extra/dev-tools.csv` | Development and testing tools | 144 | 1811 |
| misc | `extra/misc.csv` | Other | 53 | 516 |

## Total Rows per Language

| Language | Language (name) | Files | Data rows |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 34 | 101,247 |
| `zh-TW` | 繁體中文 | 34 | 101,215 |
| `en-US` | English | 34 | 101,550 |
| `ja-JP` | 日本語 | 34 | 101,553 |
| `ko-KR` | 한국어 | 34 | 101,279 |
| `fr-FR` | Français | 34 | 101,569 |
| `de-DE` | Deutsch | 34 | 101,431 |
| `es-ES` | Español | 34 | 101,647 |
| `ru-RU` | Русский | 34 | 101,629 |
| `pt-BR` | Português | 34 | 101,489 |
| `it-IT` | Italiano | 34 | 101,580 |
| `tr-TR` | Türkçe | 34 | 101,665 |
| `th-TH` | ภาษาไทย | 34 | 101,264 |
| `vi-VN` | Tiếng Việt | 34 | 101,325 |
| **Total** |  | **476** | **1,420,443** |

## Data Cleaning Notes

| Item | Handling |
| --- | --- |
| Rows identical to the target language | Removed (e.g. track names or proper nouns left untranslated in every language) |
| Duplicate rows produced by the same entry | Merged |
| Empty / missing translations | The language is skipped and no empty row is generated |
| Formatting placeholders (`%s`, `%1$s`, `%%`) | Preserved verbatim |
| Duplicate translations of the same key across languages | Deduplicated by `source`+`target` |

## Usage Tips

- When importing into CAT tools (Trados, memoQ, Phrase, etc.), simply select the CSV for the corresponding target language and import it as a term base.
- The file name is the category name; categories can be merged as needed. If you need "all categories merged into a single file" or an added `src_lng` (source language) column, it can be generated at any time.
- To regenerate the glossary: first prepare the official language files (`lang/<locale>.json`), then run `tools/build_glossary.py`; the complete mapping from prefix to category is in the `CATEGORIES` table of that script.
- The official language files contain 144 language variants in total; this glossary selects 14 of them as needed. If you need others, add them to `LANG_FILES` in `tools/build_glossary.py` and regenerate.
- This README is generated by `tools/make_readme.py`, and the numbers on this page come from `tools/glossary_counts.json`; please do not edit the numbers by hand.

## Disclaimer

This directory is an **unofficial** translation terminology database compiled and maintained by an individual, intended only for personal study, research, and term matching to assist AI translation software (including but not limited to Immersive Translation). This database has no affiliation, authorization, cooperation, agency, or official representation relationship with the developer, publisher, distributor, operator, or copyright holder of *Minecraft*; the translations in the database do not represent an official position and are not guaranteed to always be accurate, complete, or consistent with the game's current version, and **should not be regarded as an official glossary or official localization file of any game**. Intellectual property such as game names, character names, proper nouns, and trademarks belongs to their respective rights holders. This database claims no rights over the aforementioned third-party intellectual property. All responsibility arising from the use of this project and the translation results produced based on it is borne by the user. If a rights holder considers any content inappropriate, you are welcome to contact us via GitHub Issues / Pull Request, and the maintainer will verify and modify or remove it. For the complete terms, see `README.md` / `README_EN.md` / `README_JP.md` in the repository root.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorization, cooperation, or agency relationship with this game or its developer, publisher, distributor, or copyright holder.**