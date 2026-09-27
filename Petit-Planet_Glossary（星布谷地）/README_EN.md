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
   `neighbor.csv`. It can be imported into terminology tools such as
   Immersive Translate without any conversion.
2. **Whole language folder** — download every category file in that language folder.
3. **All languages side by side** — `petit-planet-glossary/multilingual/all_languages_master.csv`, one column per language.

## Directory layout

```text
Petit-Planet_Glossary（星布谷地）/
  README.md                Chinese
  README_EN.md             English
  README_JP.md             Japanese
  petit-planet-glossary/   glossary data (15 sets, split by target language)
    README.md              sub-library description (categories, cleanup rules)
    zh-CN/                 targeting Simplified Chinese (flat category CSVs)
    zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/
    ru-RU/  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
    _master/               per-language index.csv and notes (<lang>__index.csv)
    multilingual/          all 15 languages side by side
```

## File format

`<类目>.csv` has exactly three columns:

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

`*__terms.csv` is the entry list for that language (`id,term,src_table`), for proofreading and lookup.

## Languages and counts

| Target language | Language | Entries | Alignment rows |
| --- | --- | ---: | ---: |
| `zh-CN` | 简体中文 | 125 | 1,363 |
| `zh-TW` | 繁體中文 | 123 | 1,358 |
| `en-US` | English | 2,073 | 3,306 |
| `ja-JP` | 日本語 | 114 | 1,303 |
| `ko-KR` | 한국어 | 114 | 1,304 |
| `fr-FR` | Français | 113 | 1,298 |
| `de-DE` | Deutsch | 114 | 1,311 |
| `es-ES` | Español | 113 | 1,298 |
| `ru-RU` | Русский | 112 | 1,296 |
| `pt-PT` | Português | 114 | 1,308 |
| `it-IT` | Italiano | 112 | 1,296 |
| `tr-TR` | Türkçe | 113 | 1,298 |
| `th-TH` | ภาษาไทย | 114 | 1,304 |
| `vi-VN` | Tiếng Việt | 114 | 1,304 |
| `id-ID` | Bahasa Indonesia | 113 | 1,298 |
| **Total** | | **3,681** | **21,645** |

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
