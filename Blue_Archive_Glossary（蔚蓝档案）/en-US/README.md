# Blue Archive Terminology Database — English (`en-US`)

[← Back to the game-level documentation](../README.md)

This folder is the termbase **targeting `en-US` (English)**: every row pairs a spelling from another language with the English spelling of the same entry. It holds **5909** entries and **26623** aligned rows, the `tgt_lng` column is always `en-US`, and the `source` column carries the spellings found in `zh-CN` / `zh-TW` / `ja-JP` / `ko-KR` / `th-TH`. For the full six-language side-by-side view of each entry, see `00_master/README.md` and `../multilingual/00_master/`.

## Files

- `01_xxx/01_xxx_glossary.csv` — three columns `source,target,tgt_lng`, ready to import into CAT / terminology tools
- `01_xxx/01_xxx_terms.csv` — this language's term list (`id,term,src_table`), suited to proofreading and lookups
- `00_master/all_glossary.csv` — the merged aligned rows of all 15 categories (`category,source,target,tgt_lng`)
- `00_master/all_terms.csv` — the complete term list of this language (`category,category_label,id,term,src_table`)
- `00_master/index.csv` — category index and counts (`category,label,term_count,glossary_file,terms_file,target_language`)
- `00_master/README.md` — the existing detailed notes for this termbase

`01_xxx/` are the 15 category folders; each contains exactly the two files listed above.

## Categories and Counts

The numbers come from `00_master/index.csv` and were checked row by row against the actual data rows of each category CSV.

| Category | Topic | Terms | Aligned rows |
| --- | --- | ---: | ---: |
| `01_character` | Character names | 204 | 979 |
| `02_school` | Schools | 26 | 116 |
| `03_club` | Clubs | 43 | 193 |
| `04_story_title` | Story titles | 665 | 3237 |
| `05_favor_item` | Favor items | 51 | 248 |
| `06_location` | Locations | 8 | 38 |
| `07_terminology` | Terminology | 1379 | 5817 |
| `08_event` | Events | 45 | 184 |
| `09_scenario_character` | Scenario characters | 134 | 618 |
| `10_enemy` | Enemies | 351 | 1631 |
| `11_skill` | Skills | 1069 | 5086 |
| `12_item` | Items | 649 | 2999 |
| `13_equipment` | Equipment | 155 | 722 |
| `14_furniture` | Furniture | 472 | 1825 |
| `15_stage` | Stages | 658 | 2930 |
| **Total** | | **5909** | **26623** |

## Notes

- **Translation source and alignment**: every translation is taken from the official client's multilingual text (CN / global / JP / KR / TH servers) and a community story-translation table, aligned on the same text key (the official data's Id or key name). These are **official localizations**, not second-hand translations. Each entry expands the spellings of all other languages into aligned rows, so this folder can also be queried in reverse as "English → other languages".
- **Language tags**: the six tags used in this database are `zh-CN` Simplified Chinese (CN server), `zh-TW` Traditional Chinese (global server), `en-US` English, `ja-JP` Japanese, `ko-KR` Korean and `th-TH` Thai; every `tgt_lng` in this folder is `en-US`.
- **Encoding**: all CSVs are UTF-8 with BOM and CRLF line endings, so Excel shows CJK and Thai text correctly on a double click. This documentation file is UTF-8 (no BOM).
- **Known limitations**:
  - `04_story_title`, `06_location` and `09_scenario_character` are based on story and community material and auto-complete other languages only on exactly matching spellings in the official tables, so not every entry is present in all six languages (this folder has 8 `06_location` entries and 45 `08_event` entries, while some other languages cover 90 and 72).
  - The character category also carries "full name" entries (surname + given name) for the CJK languages only: English and Thai reverse the CJK name order, and the official data provides no directly concatenable spelling.
  - Entries whose spelling matches the target language exactly are not written into the glossary, and several data rows for one name (for example same-named enemies at different levels) are merged into a single entry.
  - A very small share of entries (roughly 1%–3%) produce one `source` mapping to several `target` values inside this single target-language file, mostly from short words that name different things (for example `Normal` is both an armor type and an item rarity). Tools that de-duplicate by `source` keep only one of them; use the `id` and `src_table` columns in `_terms.csv` to recover the context when you need to tell them apart.

## Disclaimer

This folder is a **non-official** English translation terminology database compiled and maintained by an individual, intended only for personal study, research, and terminology matching in AI translation software (including but not limited to Immersive Translate). It has no affiliation, authorization, cooperation, agency or official-representation relationship with *Blue Archive* or its developers, publishers, distributors or rights holders. The names in it do not represent any official position, are not guaranteed to be accurate, complete or consistent with the game's current version, and **must not be treated as an official glossary or official localization file of any game**. Intellectual property such as game names, character names, proper nouns and trademarks belongs to their respective owners. All responsibility arising from the use of this database and of translations produced from it rests with the user. Rights holders who consider any content inappropriate are welcome to make contact through GitHub Issues / Pull Requests, and the maintainer will verify and then amend or remove it. The complete terms are in the repository root's `README.md` / `README_EN.md` / `README_JP.md`.

---

**Game-translation-terminology-database is an independent personal project and has no affiliation, authorization, cooperation or agency relationship with this game or its developers, publishers, distributors or rights holders.**
