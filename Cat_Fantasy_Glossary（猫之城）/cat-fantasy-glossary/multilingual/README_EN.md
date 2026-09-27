# Cat Fantasy Seven-Language Side-by-Side Table (`multilingual/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory lays out all **102,213** Cat Fantasy terms one per row, side by side in seven languages, for overall searching and further processing. Per-target-language splits live in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
multilingual/
├── all_languages_master.csv   seven languages side by side (102213 data rows)
└── 00_master/
    ├── categories.csv         definitions of the 16 categories (category,label,description)
    ├── source_mapping.csv     source-table → category mapping with term counts (379 tables)
    └── README.md              this document
```

## File Format

`all_languages_master.csv` is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.

| Column | Description |
| --- | --- |
| `id` | Term ID in the form `source_table.primary_key.field`, matching the `id` in each language's `*__terms.csv` |
| `category` | Category it belongs to (see `00_master/categories.csv`) |
| `src_table` | Relative path of the source table in the official data package |
| `zh-CN` | Simplified Chinese |
| `zh-TW` | Traditional Chinese |
| `en-US` | English |
| `ja-JP` | Japanese |
| `ko-KR` | Korean |
| `th-TH` | Thai |
| `id-ID` | Indonesian |

## Auxiliary Files

| File | Columns | Description |
| --- | --- | --- |
| `00_master/categories.csv` | `category,label,description` | Codes, names and topic descriptions of the 16 categories |
| `00_master/source_mapping.csv` | `src_table,category,entry_count` | Mapping of 379 source tables to the 16 categories, with term counts |

## Notes

- This table is the **upstream master** for the per-language editions; the `*_glossary.csv` files under each language folder are expanded from it.
- Of the two English variants `en_UK` and `en_US`, the master table prefers `en_US` and falls back to `en_UK` when missing, consistent with the `../en-US/` folder.
- An empty cell means the term is missing in that language. To work category by category, take the files under `../<lang>/` directly.
