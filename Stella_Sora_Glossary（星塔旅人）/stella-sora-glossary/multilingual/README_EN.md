# Stella Sora Five-Language Side-by-Side Table (`multilingual/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory is the **raw five-language side-by-side master table** of the Stella Sora terminology database. It lays out all **12292** terms one per row in five languages, for easy cross-language comparison and further processing. Per-target-language splits live in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
multilingual/
├── 00_master/
│   ├── index.csv                  category index and term counts (15 categories + 1 TOTAL row)
│   ├── source_mapping.csv         source-table → category mapping (219 rows)
│   ├── StellaSora_all_terms.csv   merged master table of all categories (12292 rows)
│   └── README.md                  this document
├── 01_character/ … 15_terminology/   15 category folders, each with a terms and a glossary CSV
└── StellaSora_Glossary.xlsx       the same data as an Excel workbook (16 worksheets)
```

Each category folder holds two files: `NN_xxx_terms.csv` (side-by-side) and `NN_xxx_glossary.csv` (the `source,target,tgt_lng` alignment table).

## File Formats

**1. `NN_xxx_terms.csv` — multilingual master**

| id | zh-CN | en-US | ja-JP | ko-KR | zh-TW | src_table |
| --- | --- | --- | --- | --- | --- | --- |
| Character.103.1 | 琥珀 | Amber | コハク | 코하쿠 | 琥珀 | Character.json |

**2. `NN_xxx_glossary.csv` — glossary (`source,target,tgt_lng`)**

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| 琥珀 | Amber | en-US |

**3. `00_master/StellaSora_all_terms.csv` — merged master**

| Column | Description |
| --- | --- |
| `category` | Category code, e.g. `01_character` |
| `category_label` | Chinese category name |
| `id` | Term ID (the original in-game text key) |
| `zh-CN` | Simplified Chinese |
| `en-US` | English |
| `ja-JP` | Japanese |
| `ko-KR` | Korean |
| `zh-TW` | Traditional Chinese |
| `src_table` | The data table the term came from |

## Counts per Category

| Category | Topic | Terms | Alignment rows |
| --- | --- | ---: | ---: |
| `01_character` | Character names | 287 | 3444 |
| `02_skill` | Skill names | 628 | 7536 |
| `03_potential` | Potential names | 1457 | 17484 |
| `04_disc` | Discs | 234 | 2808 |
| `05_item` | Items | 558 | 6696 |
| `06_equipment` | Equipment | 15 | 180 |
| `07_enemy` | Enemies | 399 | 4788 |
| `08_stage` | Stages | 1019 | 12228 |
| `09_event` | Events | 581 | 6972 |
| `10_system` | System terms | 1055 | 12660 |
| `11_ui` | UI terms | 4248 | 50934 |
| `12_story` | Story proper nouns | 527 | 6324 |
| `13_faction` | Factions | 21 | 252 |
| `14_location` | Locations | 27 | 324 |
| `15_terminology` | Gameplay terminology | 1236 | 14832 |
| **Total** | | **12292** | **147462** |

## Notes

- Every CSV is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.
- The term IDs are identical across languages, so the five spellings are official counterparts of one another and have not been retranslated by hand; the `glossary` tables are expanded into `source/target/tgt_lng` rows, at most 12 per term.
- `StellaSora_Glossary.xlsx`, `00_master/index.csv` and `00_master/source_mapping.csv` come from one-off steps outside the generation pipeline.
- The game-level overview is in `../README.md` / `../README_EN.md` / `../README_JP.md`; the language-level notes are in `../<lang>/README.md`.
