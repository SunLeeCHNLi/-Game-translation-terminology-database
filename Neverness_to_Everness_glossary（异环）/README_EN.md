# Neverness to Everness (NTE / 异环) Translation Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

A multi-language terminology glossary for *Neverness to Everness* (NTE / 异环), covering 21 categories: characters, skills, weapons, combat, quests, regions, factions, items, vehicles, furniture, achievements, UI, system, story terms, and more. Split into 9 language sets.

> **Current status**: Initial scaffolding only. Confirmed term count is small pending `.locres` / TextMap extraction from the game client. See [`tools/SOURCES.md`](tools/SOURCES.md).

## File Format

All CSVs: **UTF-8 (BOM)**, **CRLF**, RFC 4180, three columns.

| source | target | tgt_lng |
| --- | --- | --- |
| Hethereau | 海特洛市 | zh-CN |
| Anomaly Hunter | 异象猎人 | zh-CN |

## Language Coverage

| Code | Language | Files | Rows |
| --- | --- | ---: | ---: |
| `zh-CN` | 简体中文 | 21 | 6 |
| `zh-TW` | 繁體中文 (unconfirmed) | 21 | 0 |
| `en-US` | English | 21 | 5 |
| `ja-JP` | 日本語 (unconfirmed) | 21 | 0 |
| `ko-KR` | 한국어 (unconfirmed) | 21 | 0 |
| `de-DE` | Deutsch (unconfirmed) | 21 | 0 |
| `fr-FR` | Français (unconfirmed) | 21 | 0 |
| `es-ES` | Español (unconfirmed) | 21 | 0 |
| `ru-RU` | Русский (unconfirmed) | 21 | 0 |

## NTE-specific categories

`vehicles.csv` and `furniture.csv` cover the game's city driving system and housing/furniture system respectively.

## Disclaimer

Unofficial personal project. Not affiliated with, endorsed by, or officially connected with *Neverness to Everness*, Perfect World, or any related entity.
