# Azur Lane Multilingual Terminology Database (`azur-lane-glossary`)

## [中文](README.md) [日本語](README_JP.md)

This sub-library is a **multilingual translation terminology data product** for *Azur Lane*, split into separate folders by **target language**,
with flat CSV files stored by **category** inside each language folder; it also contains source data, harmonised-name mappings, views split by source language, and a crawl-source directory.

## Directory Structure

```text
azur-lane-glossary/
├── README.md
├── zh-CN/                        Target language = Simplified Chinese
│   ├── glossary.csv
│   ├── glossary-detailed.csv
│   ├── ship-characters.csv
│   ├── ship-characters-detailed.csv
│   ├── terms.csv
│   ├── terms-detailed.csv
│   ├── ambiguous.csv             (zh-CN only)
│   ├── ships-and-terms.csv       (zh-CN only)
│   ├── README.md
│   └── README_zh-CN.md           (Simplified Chinese description of this language directory)
├── en-US/                        Target language = English (same 6 category CSVs + README.md / README_zh-CN.md)
├── ja-JP/                        Target language = 日本語 (same as above)
├── ko-KR/                        Target language = 한국어 (same as above)
├── harmonized/                   Five-language master table, harmonised names and alias mappings, source data
├── by-language/                  Ship sub-tables split by source language, `target` is always Simplified Chinese
└── sources/                      Crawl results of the Moegirlpedia name comparison table
```

## Target Languages

| Language directory | Language | `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | Simplified Chinese | `zh-CN` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |

## Categories and File Names

Every target-language directory uses the following **identical file names**; only categories that actually exist are kept.

| Category | File name | Description |
| --- | --- | --- |
| Ship names (standard names) | `glossary.csv` | Three-column main table |
| Ship names (standard names) details | `glossary-detailed.csv` | Main table + ship metadata |
| Ship character names (harmonised names) | `ship-characters.csv` | Three-column main table |
| Ship character names (harmonised names) details | `ship-characters-detailed.csv` | Main table + ship metadata |
| Naval / military / game terms | `terms.csv` | Three-column main table |
| Term details | `terms-detailed.csv` | Main table + category and multiple readings |
| Source entries with multiple readings | `ambiguous.csv` | `zh-CN` only |
| Ships + terms merged version | `ships-and-terms.csv` | `zh-CN` only |

## File Format

All CSVs are **UTF-8 (with BOM)**, **CRLF** line endings, with a header row; fields containing commas or quotation marks are escaped with quotes per RFC 4180.

| File family | Actual header |
| --- | --- |
| `glossary.csv` / `ship-characters.csv` / `terms.csv` / `ships-and-terms.csv` / `harmonized/equipment-harmonized.csv` / `harmonized/ship-names-harmonized.csv` / `by-language/glossary_*.csv` | `source,target,tgt_lng` |
| `glossary-detailed.csv` (`zh-CN`) | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant` |
| `glossary-detailed.csv` (`en-US` / `ja-JP` / `ko-KR`) | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `ship-characters-detailed.csv` (`zh-CN`) | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,zh_CN_standard,zh_CN_target,same_source_alternatives` |
| `ship-characters-detailed.csv` (`en-US` / `ja-JP` / `ko-KR`) | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `terms-detailed.csv` | `source,target,tgt_lng,src_lng,category,category_zh,same_source_alternatives` |
| `ambiguous.csv` | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,english_name,role` |
| `harmonized/harmonized-names-detailed.csv` | `source,target,tgt_lng,src_lng,name_code_id,kind,ship_type,ship_id,en,ja,zh_TW,wiki_note` |
| `harmonized/ijn-codename-aliases.csv` | `source,target,tgt_lng,src_lng,name_code_id` |
| `harmonized/ship-names-multilingual.csv` | `ship_id,zh_CN,en,ja,zh_TW,ko,english_name,ship_type_zh,ship_type_en,nation_zh,nation_en,variant` |

For the three-column main tables: `tgt_lng` specifies the target language, `target` is the translation in that language and `source` is the original text in another language.
The same source string keeps only one translation in the same main table; if there are multiple readings, all of them are written into the
`same_source_alternatives` column of the corresponding detail table, and the multi-reading source entries of `zh-CN` are additionally listed in `ambiguous.csv`.

## Actual Counts

All of the following are results counted directly from the actual files after this round of organisation.

| Language | Files | Data rows |
| --- | --- | --- |
| `zh-CN` | 8 | 19,855 |
| `en-US` | 6 | 12,600 |
| `ja-JP` | 6 | 15,519 |
| `ko-KR` | 6 | 15,511 |

| `zh-CN` file | Data rows | Entries after deduplicating `target` |
| --- | --- | --- |
| `glossary.csv` | 3,514 | 877 |
| `glossary-detailed.csv` | 3,592 | 877 |
| `ship-characters.csv` | 3,804 | 875 |
| `ship-characters-detailed.csv` | 3,890 | 877 |
| `terms.csv` | 449 | 170 |
| `terms-detailed.csv` | 459 | 175 |
| `ambiguous.csv` | 162 | — (all are multi-reading source rows) |
| `ships-and-terms.csv` | 3,985 | — (merged, deduplicated table) |

`by-language/` is the **source-language-side view** of the same batch of ships:

| File | Data rows |
| --- | --- |
| `glossary_en-zh-CN.csv` | 1,544 |
| `glossary_ja-zh-CN.csv` | 696 |
| `glossary_ko-zh-CN.csv` | 814 |
| `glossary_zh-TW-zh-CN.csv` | 538 |

`harmonized/`:

| File | Data rows |
| --- | --- |
| `ship-names-multilingual.csv` | 891 |
| `ship-names-harmonized.csv` | 1,187 |
| `harmonized-names-detailed.csv` | 1,259 |
| `equipment-harmonized.csv` | 8 |
| `ijn-codename-aliases.csv` | 1,082 |

The five term categories (counted by the `category` of `zh-CN/terms-detailed.csv`):

| `category` | Topic | Aligned rows |
| --- | --- | --- |
| `hull_type` | Hull type | 97 |
| `naval_term` | Naval / military terms | 198 |
| `navy_prefix` | Faction and ship-name prefixes | 59 |
| `rank` | Military ranks | 44 |
| `game_term` | Game terms | 61 |

Ship variants (counted by the `variant` of `zh-CN/ship-characters-detailed.csv`):

| Variant | Aligned rows |
| --- | --- |
| Base form (no variant marker) | 3,466 |
| META | 280 |
| μ-equipment | 101 |
| Type II | 43 |

## Data Sources

- Ship names: official CN / EN / JP / KR / TW client configurations (`ship_data_statistics.json`,
  `ship_data_template.json`, `ship_skin_template.json`, `ship_data_by_type.json`).
- Harmonised names and single-character aliases: `name_code.json`, cross-checked against Moegirlpedia's "Azur Lane / Name Comparison Table";
  the crawl results are located in `sources/moegirl_name_table.json`.
- Terms: compiled by hand and checked one by one against each server's client configuration; the data source is `tools/terms_data.py` in the root directory.

## Regeneration

Run the scripts in the root directory's `tools/` from the game directory, in the following order:

```bash
# 1) Ship glossary (Simplified Chinese standard names) + five-language master table + by-language + ambiguity table + IJN single-character aliases
python tools/build_glossary.py

# 2) Harmonised-name comparison table (depends on the five-language master table produced by 1))
python tools/build_harmonized.py

# 3) Ship character terminology table (Simplified Chinese harmonised names)
python tools/build_ship_character_glossary.py

# 4) en-US / ja-JP / ko-KR versions of the ships (depend on the five-language master table produced by 1))
python tools/build_multilang_glossaries.py

# 5) zh-CN / en-US / ja-JP / ko-KR versions of the terminology table (data is in tools/terms_data.py)
python tools/build_terms_glossaries.py
```

The `BASE` / `OUT` path constants inside the scripts point to the upstream client configuration directory and the generation working directory outside the repository, so they must be adjusted for the local machine before rerunning.
What this repository stores is a release snapshot of the generated results.

## Usage Tips

- When importing into CAT tools (Trados, memoQ, Phrase, etc.) or immersive-translation software, simply choose
  `glossary.csv`, `ship-characters.csv` or `terms.csv` under the corresponding target-language directory as the terminology base.
- Use `*-detailed.csv` when ship metadata is needed; `zh-CN` can import ships and terms in one go with `ships-and-terms.csv`.
- `by-language/` is suited to restricting the matching scope by source language; `harmonized/` is suited to obtaining the five-language comparison and harmonised-name mappings.