# Petit Planet Terminology Database — Per-Language Indexes (`_master/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds the **category indexes** for all fifteen language editions of the Petit Planet terminology database, together with the existing detailed notes for each language edition. The actual glossary data lives in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
_master/
├── zh-CN__index.csv   # category index and counts for Simplified Chinese
├── zh-CN__README.md   # the existing detailed notes for that language
├── zh-TW__...         # the other 14 languages use the same naming
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── fr-FR__...
├── de-DE__...
├── es-ES__...
├── ru-RU__...
├── pt-PT__...
├── it-IT__...
├── tr-TR__...
├── th-TH__...
├── vi-VN__...
└── id-ID__...
```

15 languages × 2 files = **30 files**.

## File Formats

| File | Columns | Description |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | Category index, one row per category; the file has **no `TOTAL` row** and no rows other than the header and the categories |
| `<lang>__README.md` | — | The existing detailed notes for that language, kept as-is |

In `__index.csv`, `term_count` is the number of terms in that category and `glossary_count` is the number of alignment rows; `glossary_file` / `terms_file` give the corresponding CSV paths under the sibling folder `../<lang>/`.

## Scale per Language

"Data rows" is the number of category rows in `<lang>__index.csv`. `en-US` covers 18 categories while every other language covers 7, so the language editions are not of equal size.

| Language | Category rows | Total terms | Total alignment rows |
| --- | ---: | ---: | ---: |
| `zh-CN` | 7 | 125 | 1363 |
| `zh-TW` | 7 | 123 | 1358 |
| `en-US` | 18 | 2073 | 3306 |
| `ja-JP` | 7 | 114 | 1303 |
| `ko-KR` | 7 | 114 | 1304 |
| `fr-FR` | 7 | 113 | 1298 |
| `de-DE` | 7 | 114 | 1311 |
| `es-ES` | 7 | 113 | 1298 |
| `ru-RU` | 7 | 112 | 1296 |
| `pt-PT` | 7 | 114 | 1308 |
| `it-IT` | 7 | 112 | 1296 |
| `tr-TR` | 7 | 113 | 1298 |
| `th-TH` | 7 | 114 | 1304 |
| `vi-VN` | 7 | 114 | 1304 |
| `id-ID` | 7 | 113 | 1298 |

## Notes

- Every CSV is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.
- The 11 extra categories in `en-US` (`03_item`, `04_material`, `05_furniture`, `07_cooking`, `08_fish`, `09_bugs`, `10_plants`, `11_shore`, `12_shop`, `13_neighbor_interaction`, `15_event`) currently hold English names only, without official multilingual counterparts.
- The fifteen-language side-by-side table is in `../multilingual/`; the game-level overview is in `../README.md` / `../README_EN.md` / `../README_JP.md`.
