# Blue Archive Multilingual Terminology Database

## [中文](README.md) [日本語](README_JP.md)

Split into separate folders by **target language**, with flat CSV files stored directly by **category** inside each folder.

## Data Product

This directory is the data-product container of the Blue Archive terminology database, covering the following **6 target languages**:

| Language folder | Language |
| --- | --- |
| `zh-CN/` | Simplified Chinese |
| `zh-TW/` | Traditional Chinese |
| `en-US/` | English |
| `ja-JP/` | 日本語 |
| `ko-KR/` | 한국어 |
| `th-TH/` | ภาษาไทย |

The 15 category CSVs inside each language folder are all stored **flat**, with no category subdirectories; the file name is the category name.

## Directory Structure

```text
blue-archive-glossary/
├── README.md
├── _master/
│   ├── zh-CN__all_glossary.csv      # Merged master table of all aligned rows for that language
│   ├── zh-CN__all_terms.csv         # Complete term list for that language
│   ├── zh-CN__index.csv             # Category index and entry counts
│   ├── zh-CN__README.md             # The existing detailed description of that language library
│   ├── zh-TW__...                   # The remaining 5 languages use the same naming
│   └── ...
├── zh-CN/
│   ├── README.md                    # Description of this language library
│   ├── character.csv                # Category glossary (source,target,tgt_lng)
│   ├── character__terms.csv         # Term list for this language (id,term,src_table)
│   └── ...                          # 15 categories in total, 2 CSVs each
├── zh-TW/
├── en-US/
├── ja-JP/
├── ko-KR/
├── th-TH/
└── multilingual/                   # Six-language side-by-side master table, retaining the original subdirectory structure
```

`_master/<lang>__<original-name>` holds the index, master table and description that were originally under each language's `00_master/`; all category CSVs have been lifted to the root level of the language folder. The original `00_master/` is no longer kept inside each language directory.

## File Format

The category glossaries (`<category>.csv`) are all **UTF-8 (with BOM)** encoded, **CRLF** line endings, with a header row, and fields containing commas or quotation marks are escaped with quotes per RFC 4180. The CSV format is fixed at three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

Meaning: for the target language specified by `tgt_lng`, `target` is the translation and `source` is the original text in **any of the other languages**. Inside each language folder, the same entry appears as one row for each of the other target languages as `source` (duplicate rows and identical-form rows have been merged).

`<category>__terms.csv` is the term list for this language, with the format `id,term,src_table`, used for proofreading and lookup.

## Categories

| Category | Glossary file | Term list file |
| --- | --- | --- |
| Character names | `character.csv` | `character__terms.csv` |
| Schools | `school.csv` | `school__terms.csv` |
| Clubs | `club.csv` | `club__terms.csv` |
| Story titles | `story_title.csv` | `story_title__terms.csv` |
| Favorite items | `favor_item.csv` | `favor_item__terms.csv` |
| Place names | `location.csv` | `location__terms.csv` |
| Terminology | `terminology.csv` | `terminology__terms.csv` |
| Events | `event.csv` | `event__terms.csv` |
| Story characters | `scenario_character.csv` | `scenario_character__terms.csv` |
| Enemies | `enemy.csv` | `enemy__terms.csv` |
| Skills | `skill.csv` | `skill__terms.csv` |
| Items | `item.csv` | `item__terms.csv` |
| Equipment | `equipment.csv` | `equipment__terms.csv` |
| Furniture | `furniture.csv` | `furniture__terms.csv` |
| Stages | `stage.csv` | `stage__terms.csv` |

## File Counts and Data Rows by Language

"Files" is the number of CSV files inside that language folder (15 category glossaries + 15 term lists); "glossary data rows" is the total data rows of the 15 `<category>.csv` files; "term list data rows" is the total data rows of the 15 `<category>__terms.csv` files.

| Language | Files | Glossary data rows | Term list data rows |
| --- | ---: | ---: | ---: |
| `zh-CN` | 30 | 29463 | 7477 |
| `zh-TW` | 30 | 27453 | 6036 |
| `en-US` | 30 | 26623 | 5909 |
| `ja-JP` | 30 | 29216 | 7534 |
| `ko-KR` | 30 | 29009 | 7310 |
| `th-TH` | 30 | 26478 | 5908 |

## Generation and Maintenance

This directory is rebuilt by the scripts under `../tools/`:

```bash
python tools/build_glossary.py
```

The script is located in the game directory's `tools/`, and outputs this data product by default; the environment variables `BA_INPUT_DIR` / `BA_OUTPUT_DIR` can be used to override the input and output directories.