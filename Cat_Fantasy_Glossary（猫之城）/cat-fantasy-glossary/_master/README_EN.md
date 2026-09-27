# Cat Fantasy Terminology Database — Per-Language Indexes (`_master/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds the **category indexes** for all seven language editions of the Cat Fantasy terminology database, together with the existing detailed notes for each language edition. The actual glossary data lives in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
_master/
├── zh-CN__index.csv   # category index and counts for Simplified Chinese
├── zh-CN__README.md   # the existing detailed notes for that language
├── zh-TW__...         # the other 6 languages use the same naming
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── th-TH__...
└── id-ID__...
```

7 languages × 2 files = **14 files**. `<lang>` is one of `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `th-TH`, `id-ID`.

## File Formats

| File | Columns | Description |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | Category index: 16 category rows + 1 `TOTAL` row, 17 data rows in total |
| `<lang>__README.md` | — | The existing detailed notes for that language, kept as-is |

In `__index.csv`, `term_count` is the number of terms in that category and `glossary_count` is the number of alignment rows; `glossary_file` / `terms_file` give the corresponding CSV file names under the sibling folder `../<lang>/`.

## Scale per Language

"Terms" is the `term_count` of the `TOTAL` row; "alignment rows" is its `glossary_count`.

| Language | Categories | Terms | Alignment rows |
| --- | ---: | ---: | ---: |
| `zh-CN` | 16 | 102213 | 196870 |
| `zh-TW` | 16 | 101915 | 196972 |
| `en-US` | 16 | 101692 | 197404 |
| `ja-JP` | 16 | 101621 | 196919 |
| `ko-KR` | 16 | 101760 | 197663 |
| `th-TH` | 16 | 99978 | 191726 |
| `id-ID` | 16 | 9916 | 28827 |

## Notes

- Every CSV is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.
- For `id-ID`, the other 15 category files keep only a header and have no data rows, because the official release provides Indonesian for the interface text only.
- The seven-language side-by-side table is in `../multilingual/`; the game-level overview is in `../README.md` / `../README_EN.md` / `../README_JP.md`.
