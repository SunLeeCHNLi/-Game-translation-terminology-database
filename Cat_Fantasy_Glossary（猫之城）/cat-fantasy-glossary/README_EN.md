# Cat Fantasy Multilingual Terminology Database

## [中文](README.md) [日本語](README_JP.md)

Split into separate folders by **target language**, with flat CSV files stored by **category** inside each language folder;
`NN_xxx/` subdirectories are no longer used.

## Data Sources

- Main text source: [PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy)
  - `Setting/Data/`: official multilingual data tables, aligned across languages by text key
  - `Setting/I18N/`: interface text tables, aligned across seven languages by Id
- Structure check: [Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1) (version 2.18.1)
- Reference format: the flat multilingual data-product layout of this repository's `Wuthering_Waves_glossary（鸣潮）/wuwa-glossary/`

## Directory Structure

```text
cat-fantasy-glossary/
├── README.md                     This description
├── zh-CN/                       Target language = Simplified Chinese
│   ├── character.csv           Glossary (source,target,tgt_lng)
│   ├── character__terms.csv    Term list (id,term,src_table)
│   └── ...                      16 categories, 32 CSVs in total
├── zh-TW/ ... id-ID/            7 language folders in total, same structure
├── _master/                     Original index and description for each language
│   ├── zh-CN__index.csv         Original name 00_master/index.csv
│   └── zh-CN__README.md         Original name 00_master/README.md
└── multilingual/                Seven-language side-by-side master table (original multilingual/, unchanged)
    ├── all_languages_master.csv Seven-language side-by-side master table
    └── 00_master/               Master table description, category definitions, source mappings
```

In each language folder, `<category>.csv` is a `source,target,tgt_lng` three-column term comparison table;
`<category>__terms.csv` is that language's `id,term,src_table` term list. `_master/<lang>__index.csv`
records the entry counts and aligned-row counts of each category in that language, and `_master/<lang>__README.md` preserves each language's original description.

## File Format

All CSVs are **UTF-8 (with BOM)** encoded, **CRLF** line endings, with a header row.

| source | target | tgt_lng |
| --- | --- | --- |
| Asura | 非天 | zh-CN |
| アスラ | 非天 | zh-CN |

Meaning: for the target language specified by `tgt_lng`, `target` is the translation and `source` is the original text in any of the other languages.
The same entry appears in the target-language folder as one row for each of the other available languages as `source`.

`<category>__terms.csv` is a term list whose columns are `id,term,src_table`: `id` has the form
`source-table-name.primary-key.field-name`, and `src_table` is the relative path of the source table in the official data package.

## Language Codes

| Language folder | Language | Target-language tag `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | Simplified Chinese | `zh-CN` |
| `zh-TW` | 繁體中文 | `zh-TW` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |
| `th-TH` | ภาษาไทย | `th-TH` |
| `id-ID` | Bahasa Indonesia | `id-ID` |

## Categories and File Names

| Category | Comparison table file | Term list file | Description |
| --- | --- | --- | --- |
| Characters and cards | `character.csv` | `character__terms.csv` | Original `01_character/` category |
| Skills and combat effects | `skill.csv` | `skill__terms.csv` | Original `02_skill/` category |
| Talents and awakening | `talent.csv` | `talent__terms.csv` | Original `03_talent/` category |
| Equipment and exclusive weapons | `equipment.csv` | `equipment__terms.csv` | Original `04_equipment/` category |
| Items and materials | `item.csv` | `item__terms.csv` | Original `05_item/` category |
| Enemies and BOSS | `enemy.csv` | `enemy__terms.csv` | Original `06_enemy/` category |
| Stages and chapters | `stage.csv` | `stage__terms.csv` | Original `07_stage/` category |
| Event gameplay | `event.csv` | `event__terms.csv` | Original `08_event/` category |
| Gacha and exchange | `gacha.csv` | `gacha__terms.csv` | Original `09_gacha/` category |
| Shop and bundles | `shop.csv` | `shop__terms.csv` | Original `10_shop/` category |
| Homeland and cat café | `homeland.csv` | `homeland__terms.csv` | Original `11_homeland/` category |
| System and missions | `system.csv` | `system__terms.csv` | Original `12_system/` category |
| UI and interface text | `ui.csv` | `ui__terms.csv` | Original `13_ui/` category |
| Story proper nouns | `story.csv` | `story__terms.csv` | Original `14_story/` category |
| Places and regions | `location.csv` | `location__terms.csv` | Original `15_location/` category |
| Game mechanic terms | `terminology.csv` | `terminology__terms.csv` | Original `16_terminology/` category |

## Data Volume by Language

The figures below are counted row by row from the files after this round of organisation; "entries" is the total data rows of `<category>__terms.csv`,
and "aligned rows" is the total data rows of `<category>.csv`.

| Language | CSV files | Entries | Aligned rows | Total data rows |
| --- | ---: | ---: | ---: | ---: |
| `zh-CN` | 32 | 102,213 | 196,870 | 299,083 |
| `zh-TW` | 32 | 101,915 | 196,972 | 298,887 |
| `en-US` | 32 | 101,692 | 197,404 | 299,096 |
| `ja-JP` | 32 | 101,621 | 196,919 | 298,540 |
| `ko-KR` | 32 | 101,760 | 197,663 | 299,423 |
| `th-TH` | 32 | 99,978 | 191,726 | 291,704 |
| `id-ID` | 32 | 9,916 | 28,827 | 38,743 |
| **Total** | **224** | **619,095** | **1,206,381** | **1,825,476** |

> Each language folder has exactly 16 `<category>.csv` and 16 `<category>__terms.csv`, 32 CSVs in total.
> The other 15 category files of `id-ID` keep only the header and have no data rows, because the official data provides Indonesian only for interface text.

## Regeneration

This data product **has no `tools/` directory and no generation script**; the directory organisation and path rewriting were done by one-off moves/renames.
To regenerate the data from upstream, the following process must be implemented:

```text
# 1. Obtain Setting/Data and Setting/I18N from PackageInstaller/DataTable · game/CatFantasy.
# 2. Scan Setting/Data for fields with the _zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH suffixes;
#    the base column (no suffix) is zh-CN; map to the 16 categories by source table.
# 3. Align the seven languages by Id from Setting/I18N and generate the ui category.
# 4. Extract only proper nouns such as character names and scene names from the NewChapter story tables; do not include the story dialogue text.
# 5. Deduplicate by (source, target); do not generate a comparison row when the source and target are identical.
# 6. Write the results as <lang>/<category>.csv and <lang>/<category>__terms.csv,
#    both UTF-8 BOM + CRLF; also generate _master/<lang>__index.csv.
```

Upstream source table → category mappings are in `multilingual/00_master/source_mapping.csv` (379 tables);
category definitions are in `multilingual/00_master/categories.csv` (16 categories).

## Usage Tips

- When importing into CAT tools (Trados, memoQ, Phrase, etc.) or immersive-translation software, simply choose
  `<category>.csv` in the target-language folder and import it directly as a terminology base.
- The file name is the category name, and they can be merged as needed; importing split by domain (for example only `character.csv` + `skill.csv`)
  can significantly improve matching accuracy.
- `__terms.csv` is used for proofreading and looking up the source table; it is not a comparison table for direct import into CAT tools.