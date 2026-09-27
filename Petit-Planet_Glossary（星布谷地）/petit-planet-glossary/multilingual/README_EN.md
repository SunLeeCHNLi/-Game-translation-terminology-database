# Petit Planet Fifteen-Language Side-by-Side Table (`multilingual/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory lays out all **3606** Petit Planet terms one per row, side by side in fifteen languages, for easy cross-language comparison and further processing. Per-target-language splits live in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
multilingual/
└── all_languages_master.csv   fifteen languages side by side (3606 data rows)
```

## File Format

`all_languages_master.csv` is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.

| Column | Description |
| --- | --- |
| `category` | Category code, e.g. `00_game_title` |
| `term` | Term identifier; for entries that only have an English name, the English spelling is used as the identifier |
| `zh-CN` | Simplified Chinese |
| `zh-TW` | Traditional Chinese |
| `en-US` | English |
| `ja-JP` | Japanese |
| `ko-KR` | Korean |
| `fr-FR` | French |
| `de-DE` | German |
| `es-ES` | Spanish |
| `ru-RU` | Russian |
| `pt-PT` | Portuguese |
| `it-IT` | Italian |
| `tr-TR` | Turkish |
| `th-TH` | Thai |
| `vi-VN` | Vietnamese |
| `id-ID` | Indonesian |

## Non-Empty Entries per Language

| Language | Non-empty entries | Language | Non-empty entries |
| --- | ---: | --- | ---: |
| `zh-CN` | 125 | `pt-PT` | 114 |
| `zh-TW` | 123 | `it-IT` | 112 |
| `en-US` | 2312 | `tr-TR` | 113 |
| `ja-JP` | 114 | `th-TH` | 114 |
| `ko-KR` | 114 | `vi-VN` | 114 |
| `fr-FR` | 113 | `id-ID` | 113 |
| `de-DE` | 114 | | |
| `es-ES` | 113 | | |
| `ru-RU` | 112 | | |

## Notes

- One term per row, fifteen languages side by side; an empty cell means the term is missing in that language.
- `en-US` has noticeably more non-empty entries than the other languages, because the item, furniture, fish, bug, cooking and shop categories currently hold English names only and lack official multilingual counterparts.
- To use a single target language, take the category CSVs under the sibling folders `../<lang>/` directly — there is no need to split this directory.
- The game-level overview is in `../README.md` / `../README_EN.md` / `../README_JP.md`.
