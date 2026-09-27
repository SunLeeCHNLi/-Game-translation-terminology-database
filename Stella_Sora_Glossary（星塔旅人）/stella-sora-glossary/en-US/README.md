# Stella Sora Terminology Base — English (`en-US`)

[← Back to the game overview](../README.md)

This directory is the termbase **whose target language is `en-US` (English)**: every row aligns the wording of another language with English, giving **12288** entries and **46032** alignment rows. The `tgt_lng` column is always `en-US`, and the `source` column holds the wording of the same entry in `zh-CN` / `zh-TW` / `ja-JP` / `ko-KR`. For the complete five-language side-by-side view of each entry, see `00_master/README.md` and `../multilingual/00_master/`.

## Files

- `NN_xxx/NN_xxx_glossary.csv` — three columns `source,target,tgt_lng`; ready to import into CAT / terminology management tools
- `NN_xxx/NN_xxx_terms.csv` — this language's entry list (`id,term,src_table`), handy for proofreading and lookups
- `00_master/all_glossary.csv` — all 15 categories' alignment rows merged (`category,source,target,tgt_lng`)
- `00_master/all_terms.csv` — every entry of this language (`category,category_label,id,term,src_table`)
- `00_master/index.csv` — category index and counts (`category,label,term_count,glossary_file,terms_file,target_language`)
- `00_master/README.md` — the pre-existing detailed readme for this language

`NN_xxx/` are the 15 category directories, each containing only the two files above. One data row of `terms.csv` is one entry; each row of `glossary.csv` is one `source → target` alignment.

## Categories and Counts

The figures come from `00_master/index.csv` and were cross-checked against the actual data-row counts of all 15 category CSVs, `00_master/all_terms.csv` and `00_master/all_glossary.csv`.

| Category | Topic | Entries | Alignment rows |
| --- | --- | ---: | ---: |
| `01_character` | Character names | 287 | 973 |
| `02_skill` | Skills | 628 | 2279 |
| `03_potential` | Potentials | 1457 | 5553 |
| `04_disc` | Discs | 234 | 896 |
| `05_item` | Items | 558 | 2172 |
| `06_equipment` | Equipment | 15 | 58 |
| `07_enemy` | Enemies | 399 | 1547 |
| `08_stage` | Stages | 1019 | 3856 |
| `09_event` | Events | 581 | 2231 |
| `10_system` | System terms | 1055 | 4108 |
| `11_ui` | UI wording | 4244 | 15529 |
| `12_story` | Story proper nouns | 527 | 2024 |
| `13_faction` | Factions | 21 | 78 |
| `14_location` | Locations | 27 | 98 |
| `15_terminology` | Gameplay mechanics | 1236 | 4630 |
| **Total** | | **12288** | **46032** |

## Notes

- **Source of translations and alignment**: every translation comes from the game's official multilingual text library `StellaSoraData-main` (the official CN / EN / JP / KR / TW client texts), aligned across languages by the same text key — an **official localization**, not a second-hand translation. Each entry expands the wording of the other four languages into alignment rows, so this directory also works in reverse as “English → other languages”.
- **Language tags**: the five tags used in this database are `zh-CN` Simplified Chinese, `zh-TW` Traditional Chinese, `en-US` English, `ja-JP` Japanese and `ko-KR` Korean; `tgt_lng` in this directory is always `en-US`.
- **Encoding**: all CSVs are UTF-8 with BOM and CRLF line endings, so Excel displays CJK text correctly on a double-click; this readme is UTF-8 (without BOM).
- **Why there are fewer alignment rows than “entries × 4”**: the split script drops a `source` identical to the target wording, as well as any `source` → `target` row already seen inside the same category (which is why `06_equipment` has only 15 entries but 58 alignment rows).
- **Known limitations**:
  - dialogue, story bodies and item descriptions are long-form content outside the scope of this termbase;
  - apart from `DatingLandmark` and `StarTower`, the place names in `14_location` were manually curated (marked with the source `curated (aligned in-game text)`);
  - `06_equipment` has only 15 entries: this game has no traditional weapon/armour table, and the equipment slot is taken by the “Disc”;
  - this directory contains 826 `source` values that map to several `target` values, mostly short words naming different things (for example the Simplified Chinese `薇洛` corresponds to both `Suntide Willow` and `Willow`). Tools that deduplicate by `source` will keep only one of them; use the `id` and `src_table` columns of `terms.csv` to look up the context when you need to tell them apart;
  - this directory has 12288 entries, 4 fewer than `zh-CN`: the difference lies entirely in `11_ui`, where a few official UI strings have no separate English translation.
- **Regeneration**: this directory is produced by `tools/split_by_language.py` splitting `multilingual/`. The script uses a hard-coded external absolute path (`E:\Download\BT\Codex_input\StellaSora_Glossary`) and **does not read or write this repository**; see “Regeneration” in the game root `README.md`.

## Disclaimer

This directory is an **unofficial** English translation terminology database compiled and maintained by an individual, intended only for personal study, research and terminology matching in AI translation software (including but not limited to Immersive Translation). It has no affiliation, authorization, partnership, agency or official-representation relationship with *Stella Sora* or its developer, publisher, distributor or rights holder; the translations herein do not represent any official position, are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be regarded as the official terminology list or official localization file of any game**. Intellectual property such as game titles, character names, proper nouns and trademarks belongs to their respective rights holders. All responsibility arising from the use of this database and of translations produced from it rests with the user. If a rights holder considers any content inappropriate, please make contact through GitHub Issues / Pull Requests and the maintainer will verify and amend or remove it. The complete terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and is not affiliated with, authorized by, partnered with, or acting as an agent for this game or its developer, publisher, distributor or rights holder.**
