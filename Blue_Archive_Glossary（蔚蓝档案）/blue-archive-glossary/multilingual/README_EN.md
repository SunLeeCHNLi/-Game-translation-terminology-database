# Blue Archive Six-Language Side-by-Side Table (`multilingual/`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory lays out all **7535** Blue Archive terms one per row, side by side in six languages, for easy cross-language comparison and further processing. Per-target-language splits live in the sibling folders `../zh-CN/`, `../en-US/` and so on.

## Directory Structure

```text
multilingual/
├── 00_master/
│   ├── all_terms_multilingual.csv   all 15 categories, six languages side by side (7535 rows)
│   └── README.md                    this document
├── 01_character/                    01_character_multilingual.csv             408 rows
├── 02_school/                       02_school_multilingual.csv                 26 rows
├── 03_club/                         03_club_multilingual.csv                   43 rows
├── 04_story_title/                  04_story_title_multilingual.csv          1144 rows
├── 05_favor_item/                   05_favor_item_multilingual.csv             51 rows
├── 06_location/                     06_location_multilingual.csv               90 rows
├── 07_terminology/                  07_terminology_multilingual.csv          1402 rows
├── 08_event/                        08_event_multilingual.csv                  72 rows
├── 09_scenario_character/           09_scenario_character_multilingual.csv    945 rows
├── 10_enemy/                        10_enemy_multilingual.csv                 351 rows
├── 11_skill/                        11_skill_multilingual.csv                1069 rows
├── 12_item/                         12_item_multilingual.csv                  649 rows
├── 13_equipment/                    13_equipment_multilingual.csv             155 rows
├── 14_furniture/                    14_furniture_multilingual.csv             472 rows
└── 15_stage/                        15_stage_multilingual.csv                 658 rows
```

## File Format

The master table and the per-category files share the same columns, all **UTF-8 (with BOM)**, **CRLF** line endings, with a header row.

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

## Counts per Category

| Category | Topic | Rows |
| --- | --- | ---: |
| `01_character` | Character names | 408 |
| `02_school` | Schools | 26 |
| `03_club` | Clubs | 43 |
| `04_story_title` | Story titles | 1144 |
| `05_favor_item` | Favor items | 51 |
| `06_location` | Place names | 90 |
| `07_terminology` | Terminology | 1402 |
| `08_event` | Events | 72 |
| `09_scenario_character` | Scenario characters | 945 |
| `10_enemy` | Enemies | 351 |
| `11_skill` | Skills | 1069 |
| `12_item` | Items | 649 |
| `13_equipment` | Equipment | 155 |
| `14_furniture` | Furniture | 472 |
| `15_stage` | Stages | 658 |
| **Total** | | **7535** |

## Notes

- One term per row, six languages side by side; an empty cell means no equivalent was found in that language.
- To use a single target language, take the category CSVs under the sibling folders `../<lang>/` directly — there is no need to split this directory.
- Three levels of documentation: this directory (six-language table), `../<lang>/` (single-language glossary), and `../` (game-level overview).
