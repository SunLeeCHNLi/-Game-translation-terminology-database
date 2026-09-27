# Petit Planet (`星布谷地` / `プチプラネット`) Terminology Database

## [中文](README.md) [日本語](README_JP.md)

This folder is an unofficial terminology database for the HoYoverse life-simulation game
**Petit Planet** (`星布谷地` / `プチプラネット`), covering **15 target languages**:
Simplified Chinese, Traditional Chinese, English, Japanese, Korean, French, German, Spanish,
Russian, Portuguese, Italian, Turkish, Thai, Vietnamese and Indonesian.

| Name | Text |
| --- | --- |
| Simplified Chinese | 星布谷地 |
| Traditional Chinese | 星布谷地 |
| English | Petit Planet |
| Japanese | プチプラネット |
| Korean | 쁘띠플래닛 |
| French | P'tite Planète |

Every translation comes from the game's **official multilingual localization text** — the official
website localization file uses the **same localization key across all 15 languages** — together with
**official HoYoLAB announcements** (`gids=10`, also in 15 languages). Rows are aligned by the same
text key or the same official name, so this is official localization rather than a second-hand
translation. No machine translation is used.

## How to use

1. **Single file** — open a language folder (for example `zh-CN/`) and download a category file such as
   `01_neighbor/01_neighbor_glossary.csv`. It can be imported into terminology tools such as
   Immersive Translate without any conversion.
2. **Whole language folder** — download every category file in that language folder.
3. **All languages side by side** — `multilingual/all_languages_master.csv`, one column per language.

## Directory layout

```text
Petit-Planet_Glossary（星布谷地）/
  zh-CN/                    glossary targeting Simplified Chinese
    README.md               per-language readme
    00_master/
      index.csv             category index and counts
      README.md             per-language readme
    00_game_title/  01_neighbor/  02_location/  03_item/  04_material/
    05_furniture/   06_test_version/  07_cooking/  08_fish/  09_bugs/
    10_plants/      11_shore/  12_shop/  13_neighbor_interaction/
    15_event/       18_ui/  21_world_term/  22_title_tag/
  zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
  multilingual/all_languages_master.csv
  README.md  README_EN.md  README_JP.md
```

## File format

`*_glossary.csv` has exactly three columns:

```text
source,target,tgt_lng
Petit Planet,星布谷地,zh-CN
プチプラネット,星布谷地,zh-CN
Petit Planet,星布谷地,zh-TW
Starsea,星海,zh-CN
```

- `source` — the original localized string (never an internal ID)
- `target` — the official name in the target language
- `tgt_lng` — target language code

`*_terms.csv` is the entry list for that language (`id,term,src_table`), for proofreading and lookup.

## Languages and counts

| Target language | Language | Entries | Alignment rows |
| --- | --- | ---: | ---: |
| `zh-CN` | Simplified Chinese (zh-CN) | 125 | 1,363 |
| `zh-TW` | Traditional Chinese (zh-TW) | 123 | 1,358 |
| `en-US` | English (en-US) | 2,073 | 3,306 |
| `ja-JP` | Japanese (ja-JP) | 114 | 1,303 |
| `ko-KR` | Korean (ko-KR) | 114 | 1,304 |
| `fr-FR` | French (fr-FR) | 113 | 1,298 |
| `de-DE` | German (de-DE) | 114 | 1,311 |
| `es-ES` | Spanish (es-ES) | 113 | 1,298 |
| `ru-RU` | Russian (ru-RU) | 112 | 1,296 |
| `pt-PT` | Portuguese (pt-PT) | 114 | 1,308 |
| `it-IT` | Italian (it-IT) | 112 | 1,296 |
| `tr-TR` | Turkish (tr-TR) | 113 | 1,298 |
| `th-TH` | Thai (th-TH) | 114 | 1,304 |
| `vi-VN` | Vietnamese (vi-VN) | 114 | 1,304 |
| `id-ID` | Indonesian (id-ID) | 113 | 1,298 |
| **Total** | | **3,681** | **21,645** |

> The official site uses **`pt-PT`** for Portuguese and **`id-ID`** for Bahasa Indonesia (never `in-ID`).
> The official site also offers `pl-pl` and `hi-in`, which are outside this database's language scope.

## Sources and reliability

| Tier | Source | Notes |
| --- | --- | --- |
| Highest | `planet.hoyoverse.com` official localization file | 443 keys shared by all 15 languages, so key-to-key alignment is exact |
| Highest | HoYoLAB official announcements (`gids=10`) | Coziness / Stardrift / Final Beta Test text, 15 languages, 81 posts |
| Third | [petitplanet.life](https://petitplanet.life/) | Community database, **English names only**, no official localized strings |
| Tool | [c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) | Used only to locate the official news source (`Game.PLANET = 10`, section `planet`); its language field is not game localization data |
| Index | [petitplanet-life/petitplanet-resources](https://github.com/petitplanet-life/petitplanet-resources) | An index of petitplanet.life pages only, not an official data repository |

## Test phases

| Phase | Official Chinese | Date (per official announcements) |
| --- | --- | --- |
| Final Beta Test | 连接测试 | from 2026-09-22 |
| Stardrift Test | 星旅测试 | from 2026-04-21 |
| Coziness Test | 居心地测试 | from 2025-11 |
| Official Release | — | not yet released (Winter 2026) |
| Unknown | — | recorded as `Version: Unknown` when unverifiable, never guessed |

## Known limitations

- **The game client's multilingual strings are not public.** Official translations here come from the
  official website localization file and official announcements; website wording may be **Web Only**,
  and in-game text should be confirmed against the client.
- Items, furniture, fish, bugs, recipes and shop entries currently exist **only as English names** in the
  petitplanet.life community database. With no official multilingual counterpart they are recorded as
  `source = target` (both English) and labelled `community_database`. **No name has been invented.**
- Image links and empty values in the official localization file were filtered out.
- This is a **pure data product**: there is no `tools/` directory and no runnable script in the game folder.

## Quality checks

- **Round 1 (structure)** — empty source/target, wrong language codes, duplicate rows, HTML tags,
  JSON residue, internal IDs and escape residue: all clean.
- **Round 2 (language direction)** — the writing system of every target column matches its `tgt_lng`: all clean.
- **Round 3 (cross-verification)** — game title, neighbour names, UI wording, world terms and test names
  checked term by term against the official localization file and official announcements: all clean.

## Disclaimer

This folder is an **unofficial** terminology database compiled and maintained by an individual, intended
only for personal study, research and terminology matching in AI translation software (including but not
limited to Immersive Translate). It has no affiliation, authorization, partnership, agency or
official-representation relationship with *Petit Planet* or its developer, publisher, distributor or
rights holder; the translations herein do not represent any official position, are not guaranteed to be
accurate, complete or consistent with the game's current version, and **must not be regarded as the
official terminology list or official localization file of any game**. Intellectual property such as game
titles, character names, proper nouns and trademarks belongs to their respective rights holders.
All responsibility arising from the use of this database rests with the user. The complete terms are in
the repository root `README.md` / `README_EN.md` / `README_JP.md`.
