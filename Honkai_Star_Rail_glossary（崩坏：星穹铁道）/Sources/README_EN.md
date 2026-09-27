# Data Source Records / Source Records

## [简体中文](README.md) [日本語](README_JP.md)

The data sources used for generating, cross-validating and historically comparing the *Honkai: Star Rail* terminology database.
`Retrieved Date` is 2026-09-27 (locally cloned to `E:\Download\BT\Codex_input`).

## 1. Sources Actually Used in Generation

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DimbreathBot/TurnBasedGameData | https://github.com/DimbreathBot/TurnBasedGameData | Game Data / TextMap | CHS CHT EN JP KR DE ES FR ID PT RU TH VI (13) | 4.5.0 (OSPRODWin4.5.0_D16545211_A16445860_L16502768) | `4ce30f69b` (2026-09-16) | Primary data: `ExcelOutput` (2185 configs) + `TextMap` (13 languages) | Every `target` comes from the localized text of the same TextMap Key in this data source; the string key of name fields is hashed with xxHash64 |
| Mar-7th/StarRailRes | https://github.com/Mar-7th/StarRailRes | Structured Data | cn cht en jp kr fr de es ru pt id th vi (13) | 4.5.0 (info.json timestamp 1787993304) | `d226bef` (2026-08-29) | Structured supplement + cross-validation: Paths, Elements, Relic entries, Relics/Sets, Simulated Universe Blessings/Curios/Events | `index_min` (the condensed version) is used to supplement entries named by ID that TextMap cannot locate directly; every entry written is checked back against the client TextMap, and strings that do not match are not written |
| VizualAbstract/StarRailStaticAPI | https://github.com/VizualAbstract/StarRailStaticAPI | Historical / Structured Data | cn cht en jp kr fr de es ru pt id th vi (13) | 2.3.0 (timestamp 1718980131) | `e039e51` (2024-07-05) | Baseline for historical translation comparison (older version) | Compared entity by entity by ID against 4.5.0; only entries whose **names changed** are written to `hsr-glossary/historical/` |
| nathacks/HSR-Mapping-DATA | https://github.com/nathacks/HSR-Mapping-DATA | Historical / Structured Data | chs cht en jp kr fr de es ru pt id th vi (13) | 4.0 (README: Last Update 4.0) | `245f286` (2026-07-17) | Baseline for historical translation comparison (previous version) | Same as above; only differences are written, current translations are not overwritten |
| mrzjy/StarrailDialog | https://github.com/mrzjy/StarrailDialog | Community / Story | CHS EN | 2024-07 (CHS/EN only) | `149dd8e` (2024-07-12) | Auxiliary cross-checking of story/dialogue text structure | Covers only Chinese and English and is relatively old, so it was not used to generate formal terminology; used to confirm how story-type text is organized |
| M1k0t0/StarRail_Dialogue_Browser | https://github.com/M1k0t0/StarRail_Dialogue_Browser | Tool / Community | Depends on the upstream submodule | 2026-04 | `99f27a6` (2026-04-11) | Story/dialogue browsing tool and structural reference | Its data comes from the `TurnBasedGameData` submodule; this database pulls data directly from the primary source |

## 2. Sources Inspected but Not Used in Generation

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| iuyangyuc/homdgcat | https://github.com/iuyangyuc/homdgcat | Wiki / Tool | Site provides CH EN JP KR RU | 2026-02 | `7d418f5` (2026-02-13) | Reference material (not written) | The repository itself is a mirror/download script for homdgcat.wiki (including a manifest of 15357 files) and requires separately scraping the site data; it was not used as a terminology source in this round |
| kel-z/HSR-Data | https://github.com/kel-z/HSR-Data | Structured Data | EN | 2.7 | `bbffd99` (2024-12-03) | Reference material (not written) | English only and relatively old (2.7); used only for manually cross-checking character/light cone/relic structure |
| simon300000/starrail-voice | https://github.com/simon300000/starrail-voice | Voice / Tool | Multilingual audio | 2026-07 | `9478716` (2026-07-17) | Reference material (not written) | A voice extraction tool and audio index, used to confirm character name/speaker naming conventions; contains no alignable text term keys |
| miHoYo *Honkai: Star Rail* official website | https://sr.mihoyo.com/ | Official | zh-CN | 4.5.0 cycle | — | 2026-09-27 | Verification of official wording (Simplified Chinese) | Used to confirm the official Simplified Chinese translations and event name spellings |
| HoYoverse HSR global site | https://hsr.hoyoverse.com/ | Official | en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-PT / id-ID / th-TH / vi-VN | 4.5.0 cycle | — | 2026-09-27 | Verification of official wording (multilingual) | Used to confirm the official translations in each language and the scope of language support; not used as a bulk data source |

## 3. Language Code Mapping

| This database's `tgt_lng` | Client / TextMap identifier | StarRailRes directory | Official language |
| --- | --- | --- | --- |
| `zh-CN` | CHS | cn | 简体中文 |
| `zh-TW` | CHT | cht | 繁體中文 |
| `en-US` | EN | en | English |
| `ja-JP` | JP | jp | 日本語 |
| `ko-KR` | KR (`TextMapKR_0/1`) | kr | 한국어 |
| `fr-FR` | FR | fr | Français |
| `de-DE` | DE | de | Deutsch |
| `es-ES` | ES | es | Español |
| `ru-RU` | RU (`TextMapRU_0/1`) | ru | Русский |
| `pt-PT` | PT | pt | Português |
| `id-ID` | ID | id | Bahasa Indonesia |
| `th-TH` | TH (`TextMapTH_0/1`) | th | ไทย |
| `vi-VN` | VI | vi | Tiếng Việt |

> Note: this database only includes the languages actually supported by the current *Honkai: Star Rail* client.
> Languages supported by other HoYoverse games (such as `it-IT`, `tr-TR`) are not applied to this title.

## 4. Upstream Data Is Not Distributed with the Repository

The upstream repositories are fairly large (raw TextMap, ExcelOutput, story, audio, etc.), and all of them are kept locally
under `E:\Download\BT\Codex_input` and are not copied into this repository. To regenerate, simply clone the corresponding versions using the URLs in the table above.