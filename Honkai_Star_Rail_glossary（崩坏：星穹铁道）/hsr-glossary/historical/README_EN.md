# Historical names / 历史译名

## [简体中文](README.md) [日本語](README_JP.md)

This directory records the terminology changes that happened between **older client versions**
and the current version (4.5.0), for version tracing and matching of legacy text. The current
version's wording is always the regular entry under `hsr-glossary/<lang>/`.

## Files

- `historical_names.csv` — three columns `source,target,tgt_lng`
  - `source`: the wording in the older client (2.3.0 or 4.0)
  - `target`: the wording in the current 4.5.0 client
  - `tgt_lng`: the language of that wording
- `_history_counts.json` — number of differences detected per source and per language

## Comparison baselines

| Baseline | Version | Commit |
| --- | --- | --- |
| VizualAbstract/StarRailStaticAPI | 2.3.0 | `e039e51` |
| nathacks/HSR-Mapping-DATA | 4.0 | `245f286` |
| Current version | Mar-7th/StarRailRes 4.5.0 | `d226bef` |

Compared entities (aligned by entity ID): `characters`, `light_cones`, `relic_sets`, `relics`,
`simulated_curios`, `simulated_blessings`, `simulated_events`, `paths`, `elements`, `achievements`.

## Processing rules

1. Only names of the **same entity ID** are compared; no string-similarity matching is performed.
2. Before comparison, HTML tags such as `<i>`, ruby annotations such as `{RUBY_B#…}`, and leading
   or trailing quotes are stripped, so that "markup-only changes" are not falsely reported as
   name changes.
3. Real differences in case, spaces and punctuation are preserved (for example
   `Deja Vu` → `Déjà Vu`).
4. All differences are kept as-is; no attempt is made to decide which one is more "correct".
   Regular entries always follow the current version.

Regenerate:

```bash
python ../tools/build_hsr_history.py
```