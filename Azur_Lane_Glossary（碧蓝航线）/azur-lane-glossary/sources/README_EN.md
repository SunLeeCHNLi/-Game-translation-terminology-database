# Azur Lane terminology sources (`sources`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory stores the **captured external sources** used while generating the Azur Lane
termbase. There is currently one file, used to verify the CN client's ship-name harmonisation mapping.

## Layout

```text
sources/
├── README.md                this document (Simplified Chinese)
├── README_EN.md             English document
├── README_JP.md             Japanese document
└── moegirl_name_table.json  capture of the Moegirlpedia "Azur Lane / name comparison table"
```

## File details

| File | Type | Size | Purpose |
| --- | --- | ---: | --- |
| `moegirl_name_table.json` | JSON array | 8,449 bytes | A hand-maintained original-name → harmonised-name table, used to cross-check `ShareCfg/name_code.json` |

### Structure of `moegirl_name_table.json`

The file is a JSON array in which every element is a triple `[ID, 原名, 和谐名]`, i.e. the CSV table
written row by row:

```json
[["ID", "原名", "和谐名"], ["1", "峰风", "樱"], ["2", "吹雪", "桐"], ["3", "白雪", "杉"]]
```

| Position | Field | Meaning |
| --- | --- | --- |
| `[0]` | `ID` | Row number in the Moegirlpedia comparison table (a string, **not** the in-game `ship_id`) |
| `[1]` | `原名` | The ship's original name |
| `[2]` | `和谐名` | The name after the CN client's replacement |

## Content size

| Item | Count |
| --- | ---: |
| Array elements in total | 365 |
| Header rows (`["ID", "原名", "和谐名"]`) | 3 (at indices 0, 232 and 348) |
| Data rows | 362 |
| Distinct IDs after de-duplication | 360 |

The three header rows split the data into three segments: from index 0 the main ship table, from
index 232 the 400–500 range (German / other nations), and from index 348 supplementary entries in the
194–230 range. IDs `225` and `226` each appear twice because of overlap between segments. The capture
is kept exactly as retrieved, without de-duplication.

## Notes

- This directory is only a **snapshot of a reference source** and does not feed the termbase output
  directly; the authoritative harmonised-name mapping is the game file `ShareCfg/name_code.json`,
  and this table is used for cross-checking.
- `ID` is the Moegirlpedia page's numbering and is **not the same numbering scheme** as the
  `ship_id` / `name_code_id` used by other files in this repository — do not join across them.
- The upstream page is updated with game versions; this snapshot reflects the state at the time of
  this compilation.