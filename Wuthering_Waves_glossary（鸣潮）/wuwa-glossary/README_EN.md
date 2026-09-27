# Wuthering Waves (鸣潮) Multilingual Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

Split into independent folders by **target language**; within each folder, files are stored by **category**.

## Data Sources

- Primary text source: [Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) (game 3.6.0)
  - `Textmaps/<lang>/multi_text/MultiText.json`: an all-language text table indexed by text key (such as `RoleInfo_1402_Name`)
- Text supplement: [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) (game 3.1.0)
  - `TextMap/<lang>/MultiText.json`: fills in the small number of text keys removed in version 3.6
- Category assignment: field references in Arikatsu `BinData/` + Dimbreath `ConfigDB/` (text key → entity table → category)
- Reference implementations: [My-Denia/wuwa-translate-bot](https://github.com/My-Denia/wuwa-translate-bot) (category fields and text cleanup), [CM-Edelweiss/WutheringWavesUID](https://github.com/CM-Edelweiss/WutheringWavesUID) (entry verification)

## Directory Structure

```
wuwa-glossary/
├── zh-CN/                    # target language = Simplified Chinese
│   ├── characters.csv
│   ├── items.csv
│   └── ...                   # 23 category files in total
├── zh-TW/
├── en-US/ ... th-TH/         # 10 language folders in total
└── _counts.json              # entry-count statistics per language and category
```

## File Format

All CSVs are **UTF-8 (with BOM)** encoded, use **CRLF** line endings and a header row, and escape fields containing commas or quotation marks with quotes per RFC 4180.

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

Meaning: for the target language specified by `tgt_lng`, `target` is the translation and `source` is the original text in **any other language**.
That is, inside each language folder, the same entry appears once for each of the other 9 languages as `source` (duplicate rows and identical-form rows have been merged).

## Language Codes

| Language folder | Language | Game text directory |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `Textmaps/zh-Hans/` |
| `zh-TW` | 繁體中文 | `Textmaps/zh-Hant/` |
| `en-US` | English | `Textmaps/en/` |
| `ja-JP` | 日本語 | `Textmaps/ja/` |
| `ko-KR` | 한국어 | `Textmaps/ko/` |
| `fr-FR` | Français | `Textmaps/fr/` |
| `de-DE` | Deutsch | `Textmaps/de/` |
| `es-ES` | Español | `Textmaps/es/` |
| `pt-BR` | Português | `Textmaps/pt/` |
| `th-TH` | ภาษาไทย | `Textmaps/th/` |

> **Languages not included**: `ru-RU` (Русский), `id-ID` (Bahasa Indonesia) and `vi-VN` (Tiếng Việt) are all **empty placeholder files** in both upstream data repositories (this is the case for versions 3.6.0 and 3.1.0 alike), so this termbase cannot provide them; `it-IT` and `tr-TR` are not text languages officially supported by Wuthering Waves.
> If upstream fills them in later, simply run the "Regeneration" command below and they will be included automatically.

## Categories and Entry Counts

"Entries" means the number of de-duplicated entries in that category (one entry = one text key in the game); "rows" is the number of data rows of that category's CSV inside the **zh-CN** folder.

| Category | File | Notes | Entries | zh-CN rows |
| --- | --- | --- | --- | --- |
| Character names | `characters.csv` | Characters, Rover identities, character profile fields | 1,230 | 5,181 |
| Weapon names | `weapons.csv` | Weapon names and weapon archive text | 820 | 3,072 |
| Echoes | `echoes.csv` | Echo (residual) names, archive text and echo battle text | 1,000 | 6,091 |
| Skills | `skills.csv` | Resonance skills, skill descriptions, skill trees | 5,344 | 30,340 |
| Resonant chains | `resonant-chains.csv` | Resonant chain node names and descriptions | 784 | 6,116 |
| Quests | `quests.csv` | Quest/chapter names, quest descriptions, daily commissions | 2,807 | 14,529 |
| Dungeons and challenges | `dungeons.csv` | Names and descriptions of instances, Tower of Adversity, holograms and challenge stages | 1,910 | 12,157 |
| Regions and maps | `regions.csv` | Regions, map markers, geography archive | 2,229 | 16,143 |
| Factions and forces | `factions.csv` | Country and faction names | 8 | 44 |
| Items and materials | `items.csv` | Items, materials, synthesis/cooking/forging recipes, shops | 8,384 | 54,388 |
| Monsters and creatures | `monsters.csv` | Monster and creature archive | 685 | 4,542 |
| NPCs and speakers | `npcs.csv` | NPC and speaker names | 14,172 | 64,138 |
| Achievements | `achievements.csv` | Achievement names and descriptions | 2,563 | 22,173 |
| Activities and gameplay | `activities.csv` | Gameplay text such as events, roguelike, fishing and tower defense | 9,531 | 63,487 |
| Buffs and effects | `buffs.csv` | Buff/debuff effect names and descriptions | 270 | 2,034 |
| Character voice lines | `voice-lines.csv` | Character voice lines and bond stories | 7,374 | 31,692 |
| Archives and readings | `archives.csv` | Archives, readings, investigation records | 839 | 6,574 |
| Terms and encyclopedia | `terms.csv` | In-game glossary, attributes and elemental reactions | 1,672 | 12,387 |
| System text | `system.csv` | System prompts, error codes, confirmation dialogs, function menus | 9,756 | 65,502 |
| UI text | `ui.csv` | Interface prefab text, shortcut keys, dynamic tabs | 13,866 | 78,131 |
| Tutorials and guides | `tutorials.csv` | Tutorials, guides, combat tips | 6,253 | 31,741 |
| Story text | `story.csv` | Story titles, quest objectives, scene narrative text | 29,841 | 102,144 |
| Other | `other.csv` | Unclassified text | 1,892 | 13,340 |

## Total Rows per Language

| Language | Files | Data rows | Size |
| --- | --- | --- | --- |
| `zh-CN` | 23 | 645,946 | 55.6 MiB |
| `zh-TW` | 23 | 645,529 | 55.7 MiB |
| `en-US` | 23 | 645,837 | 58.6 MiB |
| `ja-JP` | 23 | 648,414 | 63.4 MiB |
| `ko-KR` | 23 | 646,888 | 63.4 MiB |
| `fr-FR` | 23 | 654,776 | 63.8 MiB |
| `de-DE` | 23 | 652,349 | 63.0 MiB |
| `es-ES` | 23 | 646,691 | 61.8 MiB |
| `pt-BR` | 23 | 648,957 | 62.0 MiB |
| `th-TH` | 23 | 644,759 | 91.4 MiB |
| **Total** | **230** | **6,480,146** | **638.6 MiB** |

> The same text may belong to multiple categories at once (for example, a weapon description may appear in both `weapons` and `items`), so the sum of the rows across categories exceeds the globally de-duplicated entry count; this is normal.

## Data Cleanup Notes

The following content in the source data was handled at generation time:

| Source-data form | Handling | Example |
| --- | --- | --- |
| Rich-text tags such as `<color=...>`, `<size=...>`, `<te href=...>`, `<i>`, `<b>` | Strip the tags | `<color=Highlight>共鸣解放</color>` → `共鸣解放` |
| `{Male=…;Female=…}` gender branches | Take the male form | `{Male=大哥哥;Female=大姐姐}` → `大哥哥` |
| `{M#…}{F#…}` gender variants | Take the male form | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| Literal `\n` | Restore to a newline | `第一行\n第二行` → two lines |
| `dnt/` prefix (do not translate) | Remove the prefix | `dnt/测试` → `测试` |
| Rows where the source and target are exactly the same | Not output | — |

## Scope Notes

- **By default, sentence-by-sentence story dialogue is not included** (speaker lines and subtitles, about 170,000 per language), otherwise the size per language would grow from about 60 MiB to about 230 MiB.
  To get a dialogue library, run: `python tools/build_wuwa_glossary.py --out <目录> --with-dialogue` (this additionally generates `dialogue.csv`).
- Overly long text is truncated according to category thresholds; the thresholds are defined in `MAX_LEN` in `tools/wuwa_config.py` (for example `ui` 60 characters, `story` 200 characters, `items` 250 characters, `archives` 400 characters).
- The assignment of text keys to categories comes from field references in the game configuration tables; the small number of keys not referenced by any configuration table are fallback-classified by naming rule.

## Regeneration

You need to first place the two data repositories (`WutheringWaves_Data`, `WutheringData`) under `E:\Download\BT\Codex_input`, or specify another location via the `WUWA_DATA_ROOT` environment variable.

```bash
# Full generation (default)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary

# Generate only some categories (smaller size, more precise matching)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --only characters,weapons,echoes,skills,resonant-chains

# Compress the long-text thresholds (for example keep only short entries, about 1/3 the default size)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --len-scale 0.5

# Additionally generate sentence-by-sentence story dialogue dialogue.csv (very large, about +170 MiB per language)
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --with-dialogue
```

Other parameters: `--dry-run` (only count, do not write files), `--rebuild-cache` (rescan `BinData`/`ConfigDB`; by default the result is cached to `tools/_cfgmap_cache.pkl`).

## Usage Tips

- When importing into CAT tools (Trados, memoQ, Phrase, etc.) or immersive-translation software, simply choose the CSV of the corresponding target language and import it directly as a termbase.
- The file name is the category name, so files can be merged as needed; splitting by domain (for example importing only `characters.csv` + `weapons.csv` + `skills.csv`) can significantly improve matching precision.
