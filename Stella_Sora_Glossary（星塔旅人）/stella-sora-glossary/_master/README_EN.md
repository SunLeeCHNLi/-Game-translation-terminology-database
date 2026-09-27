# Stella Sora Terminology Database — Per-Language Master Tables (`_master/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds the **original master tables, term lists and category indexes** for all five language editions of the Stella Sora terminology database. It is the upstream snapshot for the language folders `../zh-CN/`, `../en-US/` and so on, and is not meant to be imported directly as a CAT glossary.

## Directory Structure

```text
_master/
├── zh-CN__all_glossary.csv   # all Simplified Chinese alignment rows
├── zh-CN__all_terms.csv      # all Simplified Chinese terms
├── zh-CN__index.csv          # category index and counts for Simplified Chinese
├── zh-CN__README.md          # the existing detailed notes for that language
├── zh-TW__...                # the other 4 languages use the same naming
├── en-US__...
├── ja-JP__...
└── ko-KR__...
```

5 languages × 4 files = **20 files**. `<lang>` is one of `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`.

## File Formats

| File | Columns | Description |
| --- | --- | --- |
| `<lang>__all_glossary.csv` | `category,source,target,tgt_lng` | All 15 categories of alignment rows merged; `tgt_lng` is fixed to that language |
| `<lang>__all_terms.csv` | `category,category_label,id,term,src_table` | All terms of that language; `id` is the traceable text key |
| `<lang>__index.csv` | `category,label,term_count,glossary_file,terms_file,target_language` | Category index: 15 category rows + 1 `TOTAL` row |
| `<lang>__README.md` | — | The existing detailed notes for that language, kept as-is |

## Scale per Language

"Terms" is the data-row count of `<lang>__all_terms.csv`; "alignment rows" is the data-row count of `<lang>__all_glossary.csv`.

| Language | Terms | Alignment rows |
| --- | ---: | ---: |
| `zh-CN` | 12292 | 46279 |
| `zh-TW` | 12292 | 46052 |
| `en-US` | 12288 | 46032 |
| `ja-JP` | 12289 | 46426 |
| `ko-KR` | 12292 | 45950 |

## Notes

- Every CSV is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.
- The five languages have almost the same number of terms, differing only in the `11_ui` category; the alignment-row totals differ because the number of variant spellings per term is not the same in every language.
- The five-language side-by-side table is in `../multilingual/`; the game-level overview is in `../README.md` / `../README_EN.md` / `../README_JP.md`.
