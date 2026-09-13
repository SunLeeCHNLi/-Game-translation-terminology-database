# Wuthering Waves（鸣潮）Terminology Database — English（`en-US`）

[← Back to the game overview](../../README.md) ｜ [← wuwa-glossary sub-library description](../README.md)

This directory is the Wuthering Waves terminology database with **`en-US` (English) as the target language**. It holds **123,230** unique terms and **645,837** aligned rows (the data rows of the 23 CSV files in this directory, about **58.6 MiB**). The `tgt_lng` column is always `en-US`, and the `source` column stores the wording in each of the other 9 languages (`zh-CN` (简体中文), `zh-TW` (繁體中文), `ja-JP` (日本語), `ko-KR` (한국어), `fr-FR` (Français), `de-DE` (Deutsch), `es-ES` (Español), `pt-BR` (Português), `th-TH` (ภาษาไทย)), so one and the same game text key can be matched from any of them.

## Files

This directory uses a **flat layout**: the 23 category CSV files sit directly in this directory and there is no additional subdirectory:

- `characters.csv` — Character names
- `weapons.csv` — Weapon names
- `echoes.csv` — Echoes
- `skills.csv` — Skills
- `resonant-chains.csv` — Resonance Chains
- `quests.csv` — Quests
- `dungeons.csv` — Dungeons and challenges
- `regions.csv` — Regions and map
- `factions.csv` — Factions and powers
- `items.csv` — Items and materials
- `monsters.csv` — Monsters and creatures
- `npcs.csv` — NPCs and speakers
- `achievements.csv` — Achievements
- `activities.csv` — Events and gameplay modes
- `buffs.csv` — Buffs and effects
- `voice-lines.csv` — Character voice lines
- `archives.csv` — Archives and readings
- `terms.csv` — Terms and encyclopedia
- `system.csv` — System text
- `ui.csv` — UI text
- `tutorials.csv` — Tutorials
- `story.csv` — Story text
- `other.csv` — Other

Every file has exactly three columns, `source,target,tgt_lng`, with a header row: for the target language given by `tgt_lng`, `target` is the translation and `source` is the wording in **one of the other languages**. A single entry therefore appears once per remaining language as a `source` row (duplicate and identical rows have been merged, so the row count is not nine times the number of terms). The files can be imported directly into CAT tools or terminology-matching software such as Immersive Translate.

## Categories and counts

| Category | Theme | Terms | Aligned rows |
| --- | --- | --- | --- |
| `characters.csv` | Character names | 1,230 | 5,236 |
| `weapons.csv` | Weapon names | 820 | 3,105 |
| `echoes.csv` | Echoes | 1,000 | 6,112 |
| `skills.csv` | Skills | 5,344 | 30,869 |
| `resonant-chains.csv` | Resonance Chains | 784 | 6,174 |
| `quests.csv` | Quests | 2,807 | 14,563 |
| `dungeons.csv` | Dungeons and challenges | 1,910 | 12,137 |
| `regions.csv` | Regions and map | 2,229 | 16,209 |
| `factions.csv` | Factions and powers | 8 | 44 |
| `items.csv` | Items and materials | 8,384 | 54,937 |
| `monsters.csv` | Monsters and creatures | 685 | 4,531 |
| `npcs.csv` | NPCs and speakers | 14,172 | 62,992 |
| `achievements.csv` | Achievements | 2,563 | 22,174 |
| `activities.csv` | Events and gameplay modes | 9,531 | 64,118 |
| `buffs.csv` | Buffs and effects | 270 | 2,091 |
| `voice-lines.csv` | Character voice lines | 7,374 | 31,693 |
| `archives.csv` | Archives and readings | 839 | 6,695 |
| `terms.csv` | Terms and encyclopedia | 1,672 | 12,570 |
| `system.csv` | System text | 9,756 | 65,620 |
| `ui.csv` | UI text | 13,866 | 77,362 |
| `tutorials.csv` | Tutorials | 6,253 | 32,017 |
| `story.csv` | Story text | 29,841 | 101,237 |
| `other.csv` | Other | 1,892 | 13,351 |
| **Total** | **23 categories** | **123,230** | **645,837** |

**Terms** is the number of de-duplicated terms (one term = one game text key). It comes from the `concepts` field of `tools/_counts.json` and is **shared by the whole database and independent of the target language**. **Aligned rows** is the actual number of data rows in that category CSV inside this directory. The same text may belong to more than one category, so per-category rows add up to more than the de-duplicated term count.

## Notes

- **Source of the translations**: the `target` column is taken verbatim from the localisation files of the game itself ([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data), `Textmaps/<lang>/multi_text/MultiText.json`, game 3.6.0; a few keys are backfilled from [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData), `TextMap/<lang>/MultiText.json`, game 3.1.0). These are the official in-game terms, not a second-hand translation.
- **Alignment**: rows are aligned through the game text key (e.g. `RoleInfo_1402_Name`) — the same key as written in another language becomes the `source` row of the `target` in this directory.
- **Language tag**: `tgt_lng` is fixed to the language code of this directory and matches its directory name.
- **Encoding**: every CSV is **UTF-8 with BOM**, uses **CRLF** line endings and a header row; fields containing commas or quotes are escaped per RFC 4180, so the files open directly in Excel.
- **Known limits**: sentence-by-sentence story dialogue (about 170,000 lines per language) is not included by default; how to add it with the `--with-dialogue` option is described in `../README.md`. Over-long texts are truncated per category by `MAX_LEN` in `tools/wuwa_config.py`. `ru-RU`, `id-ID` and `vi-VN` are empty placeholders upstream and are therefore missing, while `it-IT` and `tr-TR` are not text languages supported by the game.

## Disclaimer

This directory is an **unofficial** terminology database compiled and maintained privately, intended only for personal study, research and terminology matching in AI translation tools (including but not limited to Immersive Translate). It has no subordinate, licensed, cooperative, agency or official-representative relationship with the developers, publishers, distributors, operators or rights holders of the games concerned; the translations here do not represent an official position, are not guaranteed to be accurate, complete or consistent with the current game version, and **must not be regarded as an official glossary or official localisation file of any game**. Game names, character names, proper nouns and trademarks remain the property of their respective rights holders, and this project claims no rights over them. If a rights holder considers any content inappropriate, please make contact through GitHub Issues / Pull Requests and it will be reviewed and amended or removed. Full terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.
