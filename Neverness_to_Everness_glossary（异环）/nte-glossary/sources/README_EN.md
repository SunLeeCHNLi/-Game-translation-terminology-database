# NTE Sources / NTE 数据来源记录

## [简体中文](README.md) [日本語](README_JP.md)

Generation date: `2026-09-27`

## Sources used for this terminology generation

| Source | URL | Type | Version / Commit | Usage | Confidence |
| --- | --- | --- | --- | --- | --- |
| NTE_Assets Localization | https://github.com/Waifus-Grace/NTE_Assets | Game Data / Localization | `ae1f348c35378184a9e14b56593f43854b7ce575` / `1.4.7 (CN extraction)` | Primary data source; extracts official multilingual game text under the same text key | High |
| NTE official international site | https://nte.perfectworld.com/en/index.html | Official | 2026-09-27 visited | Verifies the game title, basic terminology, region names and language support | High |
| Steam official store | https://store.steampowered.com/app/4508340/ | Official | 2026-09-27 visited | Verifies the nine text languages and the voice-language scope | High |

## Sources checked but not used as primary terminology sources

| Source | Classification | Conclusion |
| --- | --- | --- |
| https://github.com/SolicenTEAM/UEExtractor | Unreal Engine extraction tool | A tool repository, not terminology data; no direct extraction of local .pak/.locres |
| https://github.com/NTE-ASIA/NTE-Internal | Teleport/coordinate data | Contains only TP coordinate files; classified as map helper data and not included in the termbase |
| https://github.com/indrasundanese/Neverness-to-Everness-Localization | Community localization corpus | Contains only an older `en_US.json`; usable as a reference for the English key structure, but not used to generate multilingual terminology |
| https://interactivemap.app/neverness-to-everness/database/en/ | Third-party database | Used for categorisation and spot-checking; does not override client-first data |
| https://thegameswiki.com/nte/wiki/localization | AI-assisted community wiki | Used to check the language-support scope; not used as a word-by-word terminology source |
| https://github.com/topics/neverness-to-everness | GitHub topic index | Surveyed; most repositories are automation, mod, cheat, gacha or map tools |

## Language code mapping

| Code in this repo | Upstream directory | Notes |
| --- | --- | --- |
| `zh-CN` | `Localization/zh-CN/game.json` | Simplified Chinese text |
| `zh-TW` | `Localization/zh-Hant/game.json` | Traditional Chinese text, mapped uniformly to `zh-TW` |
| `en-US` | `Localization/en/game.json` | English |
| `ja-JP` | `Localization/ja/game.json` | 日本語 |
| `ko-KR` | `Localization/ko/game.json` | 한국어 |
| `de-DE` | `Localization/de/game.json` | Deutsch |
| `fr-FR` | `Localization/fr/game.json` | Français |
| `es-ES` | `Localization/es/game.json` | Español |
| `ru-RU` | `Localization/ru/game.json` | Русский |

## Alignment rules

Each record comes from the same text key under the upstream `namespace + key`. The generator never
uses string similarity to guess correspondences and never machine-translates missing languages. If
the same `source + tgt_lng` has several `target` values, all of them are kept and the conflicts are
counted in `tools/_validation.json`.