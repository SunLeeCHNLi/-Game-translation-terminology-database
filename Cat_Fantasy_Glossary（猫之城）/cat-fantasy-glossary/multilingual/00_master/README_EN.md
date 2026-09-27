# Seven-Language Side-by-Side Master Table

## [简体中文](README.md) [日本語](README_JP.md)

`all_languages_master.csv` lays out all **102,213** terms one per row, side by side in seven languages, for overall searching and further processing.

| Column | Description |
| --- | --- |
| `id` | Term ID in the form `source_table.primary_key.field`, matching the `id` in each language's `*_terms.csv` |
| `category` | Category it belongs to (see `source_mapping.csv`) |
| `src_table` | Relative path of the source table in the official data package |
| `zh-CN` ~ `id-ID` | The official text of the term in each language; empty if missing |

## Contents

- `all_languages_master.csv` — seven-language side-by-side master table
- `00_master/source_mapping.csv` — source-table → category mapping with term counts, 379 tables in total

## Notes

- This table is the **upstream master** for the per-language editions; the `*_glossary.csv` files under each language folder are expanded from it;
- Of the two English variants `en_UK` and `en_US`, the master table prefers `en_US` and falls back to `en_UK` when missing, consistent with the `en-US` folder;
- To split by category, take the category files under each language folder directly.
