# Arknights Glossary — English (`en-US`)

[← Back to the game readme](../README.md)

This directory is the glossary whose **target language is `en-US` (English)**: every row is a mapping
from a term in another language to its English counterpart. It holds **13,965** entries (the sum over
the 20 categories; **12,886** unique terms after de-duplicating across categories) and **53,269**
glossary rows. The `tgt_lng` column is always `en-US`, and the `source` column holds the same entry as
written in the other four languages (`zh-CN` / `zh-TW` / `ja-JP` / `ko-KR`).

## Files

- `NN_<category>.csv` — 20 files, from `01_干员名称.csv` to `20_游戏机制.csv`. Three columns
  (`source,target,tgt_lng`), ready to import into CAT / terminology tools such as Immersive Translation.
- `_all.json` — all 20 CSVs merged into one UTF-8 JSON file (no BOM), shaped as
  `{"tgt_lng": "en-US", "categories": {"<category>": [{"source","target","tgt_lng"}, …]}}`.
  It contains the same 53,269 mappings as the 20 CSVs.
- This readme (`README.md`) and its Simplified Chinese counterpart (`README_zh-CN.md`).

> Category file names stay in Chinese in every language directory (e.g. `01_干员名称.csv`, “operator
> names”) so that categories line up across languages and scripts can treat them uniformly.

## Categories and counts

| Category | Topic | Entries | Glossary rows |
| --- | --- | ---: | ---: |
| `01_干员名称` | Operator names | 416 | 1,451 |
| `02_干员异格` | Operator alters | 34 | 130 |
| `03_职业与分支` | Classes & branches | 81 | 284 |
| `04_技能名称` | Skill names | 1,304 | 4,913 |
| `05_技能描述关键术语` | Skill description terms | 267 | 1,067 |
| `06_天赋` | Talents | 565 | 2,114 |
| `07_潜能` | Potential | 115 | 439 |
| `08_模组` | Modules | 843 | 3,303 |
| `09_敌人` | Enemies | 1,350 | 5,088 |
| `10_BOSS` | Bosses | 203 | 709 |
| `11_关卡` | Stages | 2,085 | 7,799 |
| `12_地区` | Regions | 195 | 716 |
| `13_阵营` | Factions | 44 | 167 |
| `14_活动` | Events | 215 | 836 |
| `15_道具` | Items | 517 | 2,007 |
| `16_装备` | Equipment | 1,333 | 5,045 |
| `17_材料` | Materials | 674 | 2,494 |
| `18_剧情专有名词` | Story proper nouns | 1,333 | 4,961 |
| `19_UI与系统术语` | UI & system terms | 2,152 | 8,822 |
| `20_游戏机制` | Game mechanics | 239 | 924 |
| **Total** | | **13,965** | **53,269** |

- **Entries** is the number of **distinct values in the `target` column** of that category's CSV
  (the same English term counted once).
- **Glossary rows** is the number of **CSV data rows** (header excluded). One entry expands into
  several rows — one per source language — and a row whose `source` is identical to its `target` is not
  written at all, so the row count is slightly below “entries × 4”.
- The total is the plain sum over the 20 categories. The same English term can occur in several
  categories at once (same-named stages, same-named enemies of different levels), and pooling and
  de-duplicating all 20 categories yields **12,886** unique terms.

## Notes

- **Translation source and alignment**: every term comes from the unpacked data tables of the official
  regional clients (the `en` region of the upstream `ArknightsGamedata` repository). All tables are
  keyed by entry ID (`char_002_amiya`, `skchr_amiya_2`, …) and aligned across the five servers, so this
  is an **entry-by-entry mapping of official localisation text, not a second-hand translation**.
- **Language tag**: `en-US` = English (global / EN client). The `target` column here is always the
  official English name; `source` may come from `zh-CN`, `zh-TW`, `ja-JP` or `ko-KR`. To keep only a
  Chinese→English list, simply filter the rows whose `source` contains CJK characters.
- **Encoding**: UTF-8 with BOM + CRLF, so Excel opens the files correctly by double-clicking with no
  mojibake; `_all.json` is UTF-8 without BOM.
- **Known limitations**:
  - `05_技能描述关键术语` and `20_游戏机制` are mined automatically from text (placeholder segmentation
    plus corpus-wide voting); a few of their rows are still phrase fragments rather than strict terms
    and are worth reviewing by hand;
  - heavily duplicated names (stages, events) each get their own row — no cross-entry merging is done;
  - `02_干员异格` contains only the alter forms themselves; the base operators are in `01_干员名称`;
  - content that is not yet live on a given server cannot appear here (an ID must exist in at least two
    languages), which is why some categories of `en-US` have fewer rows than `zh-CN`.

## Disclaimer

This directory is an **unofficial** terminology resource compiled and maintained by an individual, for
personal study, research, and terminology matching in AI translation software only. It has no
affiliation, authorisation, partnership or agency relationship with *Arknights* or its developer,
publisher, distributor, operator or rights holders. The terms here do not represent any official
position, are not guaranteed to be accurate, complete or consistent with the current version of the
game, and **must not be regarded as the official glossary or localisation file**. Game titles,
character names, proper nouns and trademarks belong to their respective rights holders. The complete
terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.
