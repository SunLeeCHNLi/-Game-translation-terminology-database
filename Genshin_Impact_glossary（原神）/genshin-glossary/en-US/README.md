# Genshin Impact Glossary（原神）— English（`en-US`）

[← Back to the game overview](../../README.md)

This directory is the main glossary of the Genshin Impact terminology database **with `en-US` as the target language**: **8,186** deduplicated terms and **89,412** parallel rows in total — **63,172** rows in the 17 main categories and **26,240** rows in the 10 TCG sub-categories. In all 27 CSV files `tgt_lng` is fixed to `en-US`, `source` holds the spelling used by one of the other 13 languages, and `target` holds the name in this target language.

## Files

This language directory contains **27 CSV files** on two levels:

- **17 main categories** (directly in this directory):
  `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv`
- **10 TCG sub-categories** (in the `TCG/` subfolder):
  `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv`

Every file has exactly three columns:

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Alhacén | Alhaitham | en-US |

`source` = the name of the same game object in one of the other 13 languages, `target` = the name in this directory’s target language, `tgt_lng` = the language tag of the target file (always `en-US` here). The files can be imported directly as a terminology database into CAT tools (Trados, memoQ, Phrase, …) or into term-matching extensions such as Immersive Translate.

## Categories and Counts

| Category | Theme | Terms | Rows |
| --- | --- | ---: | ---: |
| `characters.csv` | Characters | 122 | 577 |
| `talents.csv` | Talents | 125 | 632 |
| `constellations.csv` | Constellations | 125 | 632 |
| `weapons.csv` | Weapons | 249 | 2,823 |
| `materials.csv` | Materials | 919 | 10,636 |
| `foods.csv` | Food | 398 | 4,541 |
| `crafts.csv` | Crafting materials | 295 | 3,522 |
| `artifacts.csv` | Artifacts | 63 | 727 |
| `domains.csv` | Domains | 284 | 3,636 |
| `enemies.csv` | Enemies | 346 | 4,104 |
| `animals.csv` | Wildlife | 223 | 2,647 |
| `outfits.csv` | Outfits | 150 | 1,869 |
| `windgliders.csv` | Wind Gliders | 18 | 211 |
| `namecards.csv` | Namecards | 289 | 3,606 |
| `geographies.csv` | Place names | 268 | 3,389 |
| `achievements.csv` | Achievements | 1,548 | 19,463 |
| `adventureranks.csv` | Adventure Rank texts | 21 | 157 |
| `TCG/action-cards.csv` | Action Cards | 927 | 9,593 |
| `TCG/character-cards.csv` | Character Cards | 149 | 929 |
| `TCG/enemy-cards.csv` | Enemy Cards | 134 | 1,114 |
| `TCG/summons.csv` | Summons | 152 | 1,139 |
| `TCG/status-effects.csv` | Status Effects | 1,159 | 11,204 |
| `TCG/keywords.csv` | Keywords | 139 | 1,511 |
| `TCG/card-backs.csv` | Card Backs | 39 | 407 |
| `TCG/card-boxes.csv` | Card Boxes | 7 | 32 |
| `TCG/detailed-rules.csv` | Detailed Rules | 11 | 142 |
| `TCG/level-rewards.csv` | Level Rewards | 26 | 169 |
| **Main categories (17 files)** | — | **5,443** | **63,172** |
| **TCG (10 files)** | — | **2,743** | **26,240** |
| **Total (27 files)** | — | **8,186** | **89,412** |

## Notes

- **Source and alignment**: the `target` column holds the **official localized** in-game names contained in [genshin-db](https://github.com/theBowja/genshin-db) 7.0 — not machine translation and not second-hand translation. `source` holds the same game object in one of the other 13 languages; alignment is by the name of the game object, and rows with the same name and the same translation have been merged.
- **Language tag**: the `tgt_lng` column is fixed to `en-US` in every file of this directory (internal name in genshin-db: `English`).
- **Encoding**: all CSV files are **UTF-8 with BOM** and **CRLF**; fields containing commas or quotes are escaped per RFC 4180. Excel opens them by double-click without mojibake.
- **Terms ≠ rows**: “Terms” is the **deduplicated number of name objects** per category (identical across the whole collection); “Rows” is the actual number of data rows of that CSV file in this directory. The same term also appears once for each of the other 13 languages as `source`, so the row count is a multiple of the term count; names may also appear in more than one category.
- **Known limitations**: the data snapshot is genshin-db 7.0 (14 languages) and may lag behind the current game version; a few categories differ by a handful of rows between languages (e.g. `adventureranks`, `achievements`, `enemies`). This directory covers the main glossary only; the supplementary glossary lives in `../../genshin-glossary-supplement/`, and the overview of this sub-library is `../README.md`.

## Disclaimer

This directory is an **unofficial** terminology collection maintained by an individual, intended only for personal study, research, and assisting the term matching of AI translation tools (including but not limited to Immersive Translate). It has no affiliation, authorization, cooperation, agency, or official-representation relationship with the developers, publishers, distributors, operators, or rights holders of the relevant games; the translations here do not represent any official position and are not guaranteed to be accurate, complete, or consistent with the current game version, and **must not be regarded as the official glossary or official localization file of any game**. All intellectual property in game names, character names, proper nouns, and trademarks belongs to their respective owners, and this project claims no rights over such third-party intellectual property. All responsibility arising from the use of this project and of translations produced with it rests with the user. Full terms: `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) in the repository root.

---

**Game-translation-terminology-database is an independent personal project and is not affiliated with any of the games mentioned above or their related companies and organizations.**
