# Genshin Impact Terminology (Supplement) — English (`en-US`)

[← Back to the game overview](../../README.md) · [简体中文](README_zh-CN.md)

This directory is the **supplement** to the *Genshin Impact* terminology database, with **English (`en-US`) as the target language**. The main glossary in `genshin-glossary/` holds **8,186 terms** across its 27 categories; this supplement adds only the terms the main glossary lacks — for English, **13,815 alignment rows**, plus **395 rows** of aliases in `_variants.csv`. The `tgt_lng` column is always `en-US`; `source` holds the same term as written in **one of the other three languages** (`zh-CN`, `zh-TW`, `ja-JP`), and `target` holds the English name.

## Relationship to the main glossary

- Only `source/target/tgt_lng` combinations **absent from the main glossary** are included, so this supplement can be **merged directly** with `genshin-glossary/en-US/` without creating duplicate entries.
- The upstream data source differs from the main glossary (see Notes), so a given term may be spelled slightly differently (wording, punctuation).
- This supplement covers 4 target languages — `zh-CN`, `zh-TW`, `en-US`, `ja-JP`; the main glossary covers 14.

## Files

- Main categories (9 files, sharing their names with the main glossary): `characters.csv`, `materials.csv`, `geographies.csv`, `enemies.csv`, `foods.csv`, `animals.csv`, `domains.csv`, `artifacts.csv`, `weapons.csv`
- Alias file: `_variants.csv` — aliases, colloquial names and common misspellings, added as extra `source` entries
- Extra categories (10 files under `extra/`): `extra/quests.csv`, `extra/events.csv`, `extra/objects.csv`, `extra/system.csv`, `extra/archives.csv`, `extra/story.csv`, `extra/facilities.csv`, `extra/organizations.csv`, `extra/dialogue.csv`, `extra/sereniteapot.csv`

**20 CSV files** in total (9 main categories + 1 alias file + 10 extra categories), all sharing the same three-column format:

| source | target | tgt_lng |
| --- | --- | --- |
| スーパーアルティメット覇王魔剣 | Ultimate Overlord's Mega Magic Sword | en-US |
| タイダル・シャドー | Tidal Shadow | en-US |

Directory structure:

```text
en-US/
├── characters.csv
├── materials.csv
├── geographies.csv
├── enemies.csv
├── foods.csv
├── animals.csv
├── domains.csv
├── artifacts.csv
├── weapons.csv
├── _variants.csv
└── extra/
    ├── quests.csv
    ├── events.csv
    ├── objects.csv
    ├── system.csv
    ├── archives.csv
    ├── story.csv
    ├── facilities.csv
    ├── organizations.csv
    ├── dialogue.csv
    └── sereniteapot.csv
```

## Categories and counts

Every category here corresponds to **one upstream source table**, so the Theme column states where that file's entries come from. All numbers are the actual data-row counts of the files in this directory.

### Main categories (matching the main glossary)

| Category | File | Theme (upstream source) | Rows |
| --- | --- | --- | ---: |
| characters | `characters.csv` | characters-* (Mondstadt / Liyue / Inazuma / Sumeru / Fontaine / Natlan / Nod-Krai / Snezhnaya / Khaenri'ah / Fatui, etc.) | 4,609 |
| materials | `materials.csv` | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials | 741 |
| geographies | `geographies.csv` | locations | 1,235 |
| enemies | `enemies.csv` | enemies | 525 |
| foods | `foods.csv` | foods | 233 |
| animals | `animals.csv` | living-beings | 172 |
| domains | `domains.csv` | domains | 240 |
| artifacts | `artifacts.csv` | artifacts | 31 |
| weapons | `weapons.csv` | weapons | 56 |
| **Subtotal** | 9 files | — | **7,842** |

### Aliases (`_variants.csv`)

| File | Description | Rows |
| --- | --- | ---: |
| `_variants.csv` | Aliases, colloquial names and common misspellings, added as extra `source` entries | 395 |

### Extra categories (`extra/`)

| Category | File | Description | Rows |
| --- | --- | --- | ---: |
| quests | `extra/quests.csv` | Quest names (Archon / World / Story / Daily / Tribal, etc.) | 1,769 |
| events | `extra/events.csv` | Event names | 1,842 |
| objects | `extra/objects.csv` | Scene objects | 508 |
| system | `extra/system.csv` | System and gameplay terminology | 447 |
| archives | `extra/archives.csv` | Archive material | 386 |
| story | `extra/story.csv` | Story and chapters | 348 |
| facilities | `extra/facilities.csv` | Facilities and buildings | 270 |
| organizations | `extra/organizations.csv` | Organizations and factions | 243 |
| dialogue | `extra/dialogue.csv` | Dialogue expressions | 123 |
| sereniteapot | `extra/sereniteapot.csv` | Serenitea Pot | 37 |
| **Subtotal** | 10 files | — | **5,973** |

**Total for this directory: 20 files, 13,815 alignment rows (plus 395 alias rows).**

## Notes

- **Translation source and alignment.** The data comes from [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata), a community compilation of the game's **official localized text** — not a re-translation and not machine-generated. Alignment is per term: `target` is the name in the target language and `source` is the spelling in another language. Combinations already present in the main glossary were removed when this supplement was generated, which is what makes the two safe to stack.
- **Language tags.** `tgt_lng` is always `en-US` here and marks the target language; `source` is one of `zh-CN`, `zh-TW` or `ja-JP`.
- **Encoding.** All CSVs are **UTF-8 with BOM** and use **CRLF** line endings, with a header row first; fields containing commas or quotes are escaped per RFC 4180 (for example `"""Big Sis"""`). Excel opens the files directly, with no encoding adjustment needed.
- **Known limitations.** Files are split by upstream source table, so their coverage does not map one-to-one onto the main glossary's categories; `characters.csv` is by far the largest because it includes NPCs and on-screen characters. Some English/Japanese/Chinese spellings differ slightly from the main glossary, which is expected.
- **Term counts versus row counts.** This library publishes no deduplicated "term count" separate from its row counts, so only measured data-row counts are reported here — nothing is estimated.

## Disclaimer

This directory is an **unofficial** translation-terminology database compiled and maintained by one individual, intended solely for personal study, research and term matching in AI translation software (including but not limited to Immersive Translate). It has no affiliation, licence, partnership, agency or official-representation relationship with the developers, publishers, distributors, operators or rights holders of the games concerned; the translations here represent no official position and are not guaranteed to be accurate, complete or consistent with the game's current version — **this material must not be treated as any game's official glossary or official localization file**. Game names, character names, proper nouns and trademarks belong to their respective owners. All responsibility arising from use rests with the user.

Complete terms are in `README.md` / `README_EN.md` / `README_JP.md` at the repository root.

---

**Game-translation-terminology-database is an independent personal project with no affiliation, authorization, cooperation or agency relationship with this game, its developers, publishers, distributors or rights holders.**
