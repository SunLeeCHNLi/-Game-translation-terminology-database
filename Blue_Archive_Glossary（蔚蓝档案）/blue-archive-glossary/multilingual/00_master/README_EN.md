# Six-Language Side-by-Side Master Table

## [简体中文](README.md) [日本語](README_JP.md)

All **7535** terms from the 15 categories are laid out one per row, for easy cross-language comparison and further processing.

## Files

- `00_master/all_terms_multilingual.csv` — all terms
- `NN_xxx/NN_xxx_multilingual.csv` — the terms of a single category

## Columns

| Column | Description |
| --- | --- |
| `category` | Category code, e.g. `01_character` |
| `category_label` | Chinese category name |
| `id` | Term ID (matching the official data Id / key) |
| `zh-CN` | Simplified Chinese |
| `ja-JP` | Japanese |
| `zh-TW` | Traditional Chinese |
| `en-US` | English |
| `ko-KR` | Korean |
| `th-TH` | Thai |
| `src_table` | The table the term came from |

An empty cell means no equivalent was found for that term in that language. To use a single target language,
take the corresponding language folder in the parent directory directly.
