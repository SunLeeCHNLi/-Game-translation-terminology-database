# Minecraft Glossary（我的世界）— English（`en-US`）

[← Back to the game overview](../../README.md) · [zh-CN](README_zh-CN.md)

This directory is the Minecraft terminology glossary whose **target language is English (`en-US`)**: **7,854** terms deduplicated by `target` and **101,550** comparison rows in **34** CSV files. The `tgt_lng` column is always `en-US`; `source` holds the same term as written in **one of the other 13 languages**, and `target` holds the English wording. Files are split by **category**, one CSV per category, with system and text categories kept in the `extra/` subfolder.

## Files

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 19 main category files
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — 15 system and text category files under `extra/`

**34 CSV files** in total. Every one of them uses the same three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| A cidade no fim do jogo | The City at the End of the Game | en-US |
| A colpo d'occhio | Eye Spy | en-US |

Directory structure:

```text
en-US/
├── blocks.csv
├── items.csv
├── entities.csv
├── biomes.csv
├── enchantments.csv
├── effects.csv
├── instruments.csv
├── materials.csv
├── paintings.csv
├── attributes.csv
├── item-groups.csv
├── jukebox-songs.csv
├── trim-patterns.csv
├── colors.csv
├── statistics.csv
├── maps.csv
├── music.csv
├── sound-categories.csv
├── game-modes.csv
└── extra/  # system and text categories
    ├── subtitles.csv
    ├── death-messages.csv
    ├── advancement-titles.csv
    ├── advancement-descriptions.csv
    ├── gamerules.csv
    ├── commands.csv
    ├── gui.csv
    ├── options.csv
    ├── multiplayer.csv
    ├── realms.csv
    ├── world-management.csv
    ├── resource-packs.csv
    ├── telemetry.csv
    ├── dev-tools.csv
    └── misc.csv
```

## Categories and Counts

The Terms column gives the number of **name objects from the official language files** (language-file keys, including entries that are untranslated in this language) bucketed into a category; it is therefore identical in every language folder, comes from `tools/glossary_counts.json`, and the 34 categories add up to 8,559 `entries`. The Rows column is the number of rows that **this folder** actually contains in that file. The two figures follow different definitions and must not be mixed.

### Main categories (game content)

| Category | Theme | Terms | Rows |
| --- | --- | ---: | ---: |
| `blocks.csv` | Blocks | 1,975 | 25,426 |
| `items.csv` | Items | 803 | 9,304 |
| `entities.csv` | Entities | 219 | 2,582 |
| `biomes.csv` | Biomes | 67 | 835 |
| `enchantments.csv` | Enchantments | 54 | 553 |
| `effects.csv` | Status Effects | 42 | 514 |
| `instruments.csv` | Instruments | 8 | 98 |
| `materials.csv` | Armor Trim Materials | 11 | 143 |
| `paintings.csv` | Paintings | 104 | 315 |
| `attributes.csv` | Attributes | 83 | 555 |
| `item-groups.csv` | Item Groups | 16 | 198 |
| `jukebox-songs.csv` | Jukebox Songs | 22 | 42 |
| `trim-patterns.csv` | Armor Trim Patterns | 18 | 234 |
| `colors.csv` | Colors | 16 | 184 |
| `statistics.csv` | Statistics | 88 | 1,143 |
| `maps.csv` | Maps | 33 | 422 |
| `music.csv` | Music Tracks | 70 | 192 |
| `sound-categories.csv` | Sound Categories | 11 | 133 |
| `game-modes.csv` | Game Modes | 6 | 77 |
| **Subtotal** | 19 files | **3,646** | **42,950** |

### Categories under `extra/` (system and text)

| Category | Theme | Terms | Rows |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | Subtitles | 1,023 | 12,415 |
| `extra/death-messages.csv` | Death Messages | 106 | 1,354 |
| `extra/advancement-titles.csv` | Advancement Titles | 127 | 1,603 |
| `extra/advancement-descriptions.csv` | Advancement Descriptions | 127 | 1,641 |
| `extra/gamerules.csv` | Game Rules | 117 | 1,490 |
| `extra/commands.csv` | Commands and Arguments | 856 | 10,733 |
| `extra/gui.csv` | GUI Text | 581 | 6,607 |
| `extra/options.csv` | Options and Key Binds | 754 | 8,169 |
| `extra/multiplayer.csv` | Multiplayer | 173 | 2,015 |
| `extra/realms.csv` | Realms | 426 | 5,016 |
| `extra/world-management.csv` | World Management | 294 | 3,572 |
| `extra/resource-packs.csv` | Resource and Data Packs | 62 | 761 |
| `extra/telemetry.csv` | Telemetry | 70 | 897 |
| `extra/dev-tools.csv` | Developer and Test Tools | 144 | 1,811 |
| `extra/misc.csv` | Miscellaneous | 53 | 516 |
| **Subtotal** | 15 files | **4,913** | **58,600** |

**Total: 34 files, 7,854 distinct terms (deduplicated by `target`), 101,550 comparison rows.**

## Notes

- **Translation source and alignment.** All text comes from the **official Minecraft: Java Edition language files** (mirrored by [misode/mcmeta](https://github.com/misode/mcmeta), branch `assets`, path `assets/minecraft/lang/<locale>.json`; this language uses `en_us.json`). These are **official localizations**, not re-translations or machine output. Alignment works through the language-file key: each term is emitted once per *other* language, so the row count is far larger than the term count.
- **Language tags.** `tgt_lng` is always `en-US` in this folder and marks the target language; `source` may be any of the other 13 languages: `zh-CN`, `zh-TW`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`.
- **Encoding.** Every CSV is **UTF-8 with BOM** and uses **CRLF** line endings with a header row; fields containing commas or quotes are escaped per RFC 4180. Excel opens them directly with no encoding adjustment; this README itself is UTF-8 without BOM.
- **Known limitations.** Row counts differ slightly between languages, because a term is skipped when a language has no translation for it or when its wording is identical to the target language. Comparison rows and terms are not the same thing: the 34 categories add up to 8,559 `entries`, the number of name objects from the official language files bucketed into those categories, including entries that are untranslated in this language. This folder's `target`-deduplicated count is 7,854 and follows a different definition. The full definition is in the Data Overview section of `../../README.md` at the game root. The same wording may occur in more than one category, and terminology follows the official localization, including names the developers left untranslated.
- **Supplement.** The sibling directory `../../minecraft-glossary-supplement/` adds the Minecraft Wiki standard names, for Simplified and Traditional Chinese only; it can be stacked on top of this glossary.
- **Reproduction.** From the game root, `python tools/build_glossary.py` rebuilds this glossary from the official language files (the script reads an external material directory holding `mcmeta_lang/<locale>.json` and writes to `minecraft-glossary/`); `python tools/verify_output.py` re-checks every row count against `tools/glossary_counts.json`, and `python tools/make_readme.py` regenerates the library READMEs.

## Disclaimer

This directory is an **unofficial** terminology database maintained by an individual for personal study, research and terminology matching in AI-assisted translation tools (including but not limited to Immersive Translate). It has no affiliation, authorization, cooperation, agency or official-representation relationship with the developers, publishers, distributors, operators or rights holders of Minecraft; the names here do not represent any official position, are not guaranteed to be accurate, complete or consistent with the current game version, and **must not be treated as the official glossary or official localization files of any game**.

Game names, character names, proper nouns and trademarks remain the property of their respective owners, and this project claims no rights over them. Responsibility for using this project and any translation produced from it rests entirely with the user. Rights holders who object to any content are welcome to get in touch through GitHub Issues / Pull Request, and the maintainer will verify the report and amend or remove the content.

The full terms are in `README.md` / `README_EN.md` / `README_JP.md` at the repository root.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorization, cooperation or agency relationship with this game, its developers, publishers, distributors or rights holders.**
