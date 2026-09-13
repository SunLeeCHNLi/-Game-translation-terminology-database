# Wuthering Waves Terminology Database / 《鸣潮》翻译术语库 / 鳴潮 用語集

## [中文](README.md) [日本語](README_JP.md)

This repository section holds a proper-noun mapping table for the open-world action RPG **Wuthering Waves** (鳴潮). It covers **23 categories**: character names, weapons, echoes, skills, resonant chains, quests, dungeons, regions, factions, items, monsters, NPCs, achievements, activities, buffs, voice lines, archives, terms, system text, UI text, tutorials, story text and others. The categories together hold **123,230** de-duplicated entries, split into **10** independent termbases by target language (`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `fr-FR` / `de-DE` / `es-ES` / `pt-BR` / `th-TH`) — **230 CSV files / 6,480,146 mapping rows** in total (about 638.6 MiB). Every translation is taken from the official client's multilingual text and aligned on the same text key, so it is **official localisation**, not machine translation.

## Usage

1. **Download a single file.** Open the target-language folder under `wuwa-glossary/` (for example `zh-CN/`) and download the category files you need — `characters.csv`, `items.csv`, and so on. They import directly into Immersive Translate, Trados, memoQ, Phrase or any other terminology tool; no conversion is required.
2. **Download a whole language folder.** If you need every category for one language, download the 23 CSVs in that folder (about 55–92 MiB).
3. **Clone the whole repository and regenerate.** After `git clone`, use the generators in `tools/` together with the two upstream data repositories they read (`WutheringWaves_Data`, `WutheringData`) to rebuild every CSV from the original data.

> The file name is the category name, so files can be merged as needed. Splitting the import by domain (for example only `characters.csv` + `weapons.csv` + `skills.csv`) noticeably improves term-matching precision.

## Directory Structure

```text
Wuthering_Waves_glossary（鸣潮）/
  README.md                Chinese documentation (this file's sibling)
  README_EN.md             English documentation (this file)
  README_JP.md             Japanese documentation
  wuwa-glossary/           the termbase data (10 sets, split by target language)
    README.md              detailed sub-library notes (categories, cleaning, regenerate commands)
    zh-CN/                 target language Simplified Chinese, 23 category CSVs
    zh-TW/                 target language Traditional Chinese
    en-US/                 target language English
    ja-JP/                 target language Japanese
    ko-KR/                 target language Korean
    fr-FR/                 target language French
    de-DE/                 target language German
    es-ES/                 target language Spanish
    pt-BR/                 target language Portuguese
    th-TH/                 target language Thai
  tools/                   batch scripts and generation metadata
    build_wuwa_glossary.py main generator (text keys -> category CSVs)
    wuwa_classify.py       assigns text keys to categories
    wuwa_config.py         category thresholds and parameters
    _counts.json           entry-count and size statistics per language and category
    _cfgmap_cache.pkl      text-key -> category cache (rebuild with --rebuild-cache)
```

Every language folder has the same shape: **23 category CSVs** and no subdirectories. Each language folder also carries two notes files — `README.md` (in that language) and `README_zh-CN.md` (Simplified Chinese).

## Data Overview

### Size per language

| Code | Language | Files | Data rows | Size |
| --- | --- | ---: | ---: | ---: |
| `zh-CN` | Simplified Chinese | 23 | 645,946 | 55.6 MiB |
| `zh-TW` | Traditional Chinese | 23 | 645,529 | 55.7 MiB |
| `en-US` | English | 23 | 645,837 | 58.6 MiB |
| `ja-JP` | Japanese | 23 | 648,414 | 63.4 MiB |
| `ko-KR` | Korean | 23 | 646,888 | 63.4 MiB |
| `fr-FR` | French | 23 | 654,776 | 63.8 MiB |
| `de-DE` | German | 23 | 652,349 | 63.0 MiB |
| `es-ES` | Spanish | 23 | 646,691 | 61.8 MiB |
| `pt-BR` | Portuguese | 23 | 648,957 | 62.0 MiB |
| `th-TH` | Thai | 23 | 644,759 | 91.4 MiB |
| **Total** | | **230** | **6,480,146** | **638.6 MiB** |

> The figures come from `tools/_counts.json` and were re-counted per language with an RFC 4180-compliant CSV parser; all ten matched.

### Categories and entry counts

"Entries" is the number of de-duplicated **text keys** bucketed into that category (one entry = one text key in the game, independent of target language). "Rows" is the number of data rows of that category's CSV inside the **zh-CN** folder.

| Category | File | Contents | Entries | zh-CN rows |
| --- | --- | --- | ---: | ---: |
| Characters | `characters.csv` | Character names, Rover identities, character profile fields | 1,230 | 5,181 |
| Weapons | `weapons.csv` | Weapon names and weapon archive text | 820 | 3,072 |
| Echoes | `echoes.csv` | Echo (Phantom) names, archive and echo-battle text | 1,000 | 6,091 |
| Skills | `skills.csv` | Resonance skills, skill descriptions, skill trees | 5,344 | 30,340 |
| Resonant Chains | `resonant-chains.csv` | Resonant chain node names and descriptions | 784 | 6,116 |
| Quests | `quests.csv` | Quest/chapter names, quest descriptions, dailies | 2,807 | 14,529 |
| Dungeons | `dungeons.csv` | Domains, Tower of Adversity, Holo, challenge names and notes | 1,910 | 12,157 |
| Regions | `regions.csv` | Regions, map markers, geography archive | 2,229 | 16,143 |
| Factions | `factions.csv` | Nation and faction names | 8 | 44 |
| Items | `items.csv` | Items, materials, synthesis/cooking/forging recipes, shops | 8,384 | 54,388 |
| Monsters | `monsters.csv` | Monster and creature archive | 685 | 4,542 |
| NPCs | `npcs.csv` | NPC and speaker names | 14,172 | 64,138 |
| Achievements | `achievements.csv` | Achievement names and descriptions | 2,563 | 22,173 |
| Activities | `activities.csv` | Events, roguelike, fishing, trap defence and other gameplay text | 9,531 | 63,487 |
| Buffs | `buffs.csv` | Buff/debuff names and descriptions | 270 | 2,034 |
| Voice Lines | `voice-lines.csv` | Character voice lines and bond stories | 7,374 | 31,692 |
| Archives | `archives.csv` | Archives, readable items, investigation records | 839 | 6,574 |
| Terms | `terms.csv` | In-game glossary, attributes and elemental reactions | 1,672 | 12,387 |
| System | `system.csv` | System prompts, error codes, dialogs, menus | 9,756 | 65,502 |
| UI | `ui.csv` | Prefab interface text, hotkeys, dynamic tabs | 13,866 | 78,131 |
| Tutorials | `tutorials.csv` | Tutorials, guidance, combat tips | 6,253 | 31,741 |
| Story | `story.csv` | Story titles, quest objectives, scene narration | 29,841 | 102,144 |
| Other | `other.csv` | Uncategorised text | 1,892 | 13,340 |
| **Total** | | | **123,230** | **645,946** |

> The same text can belong to several categories at once (a weapon description may appear in both `weapons` and `items`, for example), so the category row counts sum to more than the globally de-duplicated entry count. This is expected.

### File format

Every category CSV has three columns and is **UTF-8 (with BOM)**, **CRLF**, with comma/quote/newline-bearing fields quoted per RFC 4180 (Excel opens them directly on double-click).

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

- `target` — the translation in this folder's target language;
- `tgt_lng` — the target-language tag, equal to the folder name;
- `source` — how the same text key is written in each of the **other 9 languages**, so one entry appears once per source language (duplicate and identical rows are merged).

### Languages not included

`ru-RU` (Russian), `id-ID` (Indonesian) and `vi-VN` (Vietnamese) are **empty placeholder files** in both upstream repositories (in 3.6.0 and 3.1.0 alike), so they cannot be provided; `it-IT` and `tr-TR` are not text languages officially supported by Wuthering Waves. If upstream fills them in later, re-running the generator picks them up automatically.

## Related Sources

| Source | Purpose |
| --- | --- |
| [Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) | Primary text source (game 3.6.0): `Textmaps/<lang>/multi_text/MultiText.json`, the all-language text table indexed by text key; category assignments come from its `BinData/` |
| [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) | Text backfill (game 3.1.0): `TextMap/<lang>/MultiText.json`, restoring a few text keys removed in 3.6.0; category assignments also reference its `ConfigDB/` |
| [My-Denia/wuwa-translate-bot](https://github.com/My-Denia/wuwa-translate-bot) | Reference implementation: category field mapping and text-cleaning rules |
| [CM-Edelweiss/WutheringWavesUID](https://github.com/CM-Edelweiss/WutheringWavesUID) | Reference implementation: entry verification |

## Regeneration

First place the two upstream data repositories under `E:\Download\BT\Codex_input`, or point the `WUWA_DATA_ROOT` environment variable somewhere else.

```bash
# Full generation (default; writes into wuwa-glossary/)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary

# Only some categories (smaller, more precise matching)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --only characters,weapons,echoes,skills,resonant-chains

# Shorten long text (e.g. keep short terms only; about one third the size)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --len-scale 0.5

# Also emit per-line story dialogue dialogue.csv (very large, about +170 MiB per language; off by default)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --with-dialogue
```

Other flags: `--dry-run` (count only, write nothing), `--rebuild-cache` (re-scan `BinData`/`ConfigDB`; the result is cached in `tools/_cfgmap_cache.pkl` by default).

The run writes the statistics metadata `_counts.json`; the copy kept in this repository is `tools/_counts.json`.

## Notes

### Text cleaning

The following patterns in the source data are handled at generation time:

| Source pattern | Handling | Example |
| --- | --- | --- |
| Rich-text tags such as `<color=...>`, `<size=...>`, `<i>`, `<b>` | Tags stripped | `<color=Highlight>共鸣解放</color>` → `共鸣解放` |
| `{Male=…;Female=…}` gender branches | Male form taken | `{Male=大哥哥;Female=大姐姐}` → `大哥哥` |
| `{M#…}{F#…}` gender variants | Male form taken | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| Literal `\n` | Restored as a line break | `第一行\n第二行` → two lines |
| `dnt/` prefix (do not translate) | Prefix removed | `dnt/测试` → `测试` |
| Rows where source and target are identical | Not emitted | — |

### Coverage

- **Per-line story dialogue is not included by default** (speaker lines and subtitles, roughly 170,000 entries per language); including it would raise a single language from about 60 MiB to about 230 MiB.
- Over-long text is truncated at a per-category threshold defined by `MAX_LEN` in `tools/wuwa_config.py` (for example 60 characters for `ui`, 200 for `story`, 250 for `items`, 400 for `archives`).
- Text-key to category assignment comes from field references in the game config tables; the few keys no config table references fall back to name-pattern rules.

### Known limitations

- Categories are assigned automatically from config-table fields, so a few entries may land in a neighbouring category;
- Coverage is determined by the upstream repository versions (3.6.0 / 3.1.0); a game update requires regeneration;
- Translations can differ between regional builds; this database follows the upstream data versions it cites.

## Disclaimer

This directory is an **unofficial** terminology collection compiled and maintained by an individual, intended solely for personal study, research and terminology matching in AI translation software (including but not limited to Immersive Translate). It is not affiliated with, authorised by, partnered with, represented by or otherwise officially connected to the developers, publishers, distributors, operators or rights holders of Wuthering Waves; the translations here do not represent any official position, are not guaranteed to be accurate, complete or consistent with the current game version, and **must not be treated as an official glossary or official localisation file for this game**. All rights to game names, character names, proper nouns and trademarks belong to their respective holders, and this project claims no rights over that third-party intellectual property. Any responsibility arising from the use of this project or of translations produced from it rests with the user. Rights holders who consider any content inappropriate are welcome to make contact through GitHub Issues or a Pull Request; the maintainer will verify and then amend or remove it. The full terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and is not affiliated with, endorsed by, sponsored by, or officially connected with Wuthering Waves or its developers, publishers, distributors, or rights holders.**
