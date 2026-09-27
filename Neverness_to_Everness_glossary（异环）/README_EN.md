# Neverness to Everness Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

This repository contains **498,495** `source,target,tgt_lng` rows extracted from the NTE 1.4.7 localization files, covering **9** target languages and **21** categories.

All targets come from aligned game localization keys. Missing values are omitted rather than filled with machine translation.

## Language Coverage

| Target language | Rows |
| --- | ---: |
| `en-US` | 55,226 |
| `zh-CN` | 55,559 |
| `zh-TW` | 55,530 |
| `ja-JP` | 55,582 |
| `ko-KR` | 55,393 |
| `de-DE` | 55,259 |
| `fr-FR` | 55,391 |
| `es-ES` | 55,275 |
| `ru-RU` | 55,280 |


## Data Source

- Repository: https://github.com/Waifus-Grace/NTE_Assets
- Commit: `ae1f348c35378184a9e14b56593f43854b7ce575`
- Game version: `1.4.7 (CN extraction)`
- Generated: `2026-09-27`
- Sources used / checked: `3` / `9`
- Unique text keys: `10,340`
- Concepts across categories: `10,573`
- Client-localization-confirmed concepts: `10,340`
- Unconfirmed / machine-translated rows: `0` / `0`
- Multi-target conflict groups: `6,169`

## Rebuild

```bash
python tools/build_nte_glossary.py
python tools/validate_nte_glossary.py
```

This is an unofficial personal project and is not affiliated with Hotta Studio, Perfect World Games, or NTE.
