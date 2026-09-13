# Cat Fantasy Terminology Database — English (`en-US`)

[← Back to the game overview](../README.md)

This directory is the terminology database whose **target language is `en-US`**: every row is an
"entry in another language → English" mapping. It holds **101,692** terms and **197,404** aligned rows,
with the `tgt_lng` column fixed to `en-US`; the `source` column carries the wordings of the other six
languages (Simplified Chinese, Traditional Chinese, Japanese, Korean, Thai, Indonesian). All translations
come from localisation text the game officially ships and are aligned by the same text key — there is no
machine translation.

## Files

- `01_character/01_character_glossary.csv` … `16_terminology/16_terminology_glossary.csv`
  — three columns (`source,target,tgt_lng`), ready to import into CAT / terminology tools such as
  Immersive Translation;
- `01_character/01_character_terms.csv` … `16_terminology/16_terminology_terms.csv`
  — the term list for this language (`id,term,src_table`), handy for proofreading and tracing entries back
  to the original data tables;
- `00_master/index.csv` — the category index and counts for this language;
- `00_master/README.md` — notes for this language's data directory (in Chinese).
- Upstream seven-language master table: `../multilingual/all_languages_master.csv` (102,213 entries × 10 columns).

## Categories and counts

| Category | Theme | Terms | Aligned rows |
| --- | --- | --- | --- |
| `01_character` | Characters and cards | 19,904 | 33,839 |
| `02_skill` | Skills and combat effects | 9,056 | 14,991 |
| `03_talent` | Talents and awakening | 2,536 | 4,165 |
| `04_equipment` | Equipment and signature weapons | 6,388 | 2,197 |
| `05_item` | Items and materials | 4,650 | 13,062 |
| `06_enemy` | Enemies and bosses | 27 | 124 |
| `07_stage` | Stages and chapters | 7,144 | 20,904 |
| `08_event` | Events and game modes | 17,339 | 21,547 |
| `09_gacha` | Gacha and exchange | 53 | 140 |
| `10_shop` | Shop and bundles | 4,589 | 1,688 |
| `11_homeland` | Homeland and cat café | 8,913 | 25,211 |
| `12_system` | Systems and quests | 6,027 | 18,834 |
| `13_ui` | UI and interface text | 9,923 | 29,542 |
| `14_story` | Story proper nouns | 3,060 | 5,435 |
| `15_location` | Locations and regions | 449 | 1,616 |
| `16_terminology` | Gameplay mechanics terminology | 1,634 | 4,109 |
| **Total** | | **101,692** | **197,404** |

> "Terms" is the number of unique text keys (the data-row count of `*_terms.csv`); "aligned rows" is the
> data-row count of `*_glossary.csv`. The two numbers mean different things and are not interchangeable.
> Every figure above can be re-checked against `00_master/index.csv`.

## Notes

- **Translation source and alignment**: all text is taken from the English already shipped in the game's
  official multilingual data tables (`Setting/Data`) and I18N interface text table (`Setting/I18N`),
  aligned by the same text key — not a re-translation.
- **A note on the English columns**: the game data tables carry a single English column, `en_UK`, while
  the I18N text table carries both `en_UK` and `en_US`. In this directory, entity names come from `en_UK`;
  interface text prefers `en_US` and falls back to `en_UK` when missing. Both variants' raw text is kept
  in the corresponding columns of `../multilingual/all_languages_master.csv`.
- **Language tag**: `tgt_lng` is fixed to `en-US`; `source` may hold the wording of any other language,
  with one row per available wording of the same entry.
- **Encoding**: every CSV is **UTF-8 with BOM + CRLF**, so Excel displays it correctly on a double-click.
- **Known limitations**:
  - categories are assigned automatically by data table, so a few entries shared across game modes may
    land in an adjacent category;
  - enemy names have no multilingual columns in the official data tables, so `06_enemy` holds only 27
    entries;
  - placeholders in the text (such as `_name_`, `_num_`, `\n`) are kept exactly as the official text has
    them and are not substituted;
  - the text keys covered differ between languages (for example `en-US` covers 521 fewer entries than
    `zh-CN`), so counts differ from language to language;
  - wording may differ between regional versions and game versions; this database follows the versions of
    the data packages referenced above.
- **Updating and reproducing**: this database is a pure data product. There is **no `tools/` folder and no
  script of any kind** under the game directory; the generation procedure is recorded as prose in the
  "Regeneration" section of `../README.md`, and there is no runnable command.

## Disclaimer

This directory is an **unofficial** English translation terminology database compiled and maintained by an
individual. It is intended solely for personal study, research, and terminology matching in AI translation
software (including but not limited to Immersive Translation). This database has no affiliation,
authorisation, partnership, agency, or official representation relationship with the developers,
publishers, distributors, operators, or rights holders of *Cat Fantasy*; the translations in it do not
represent any official position, are not guaranteed to be always accurate, complete, or consistent with the
game's current version, and **must not be regarded as the official glossary or official localisation file**.
Intellectual property such as game titles, character names, proper nouns, and trademarks belongs to their
respective rights holders, and this database claims no rights over that third-party intellectual property.
All responsibility arising from the use of this project, or of translation results produced from it, rests
with the user. For the complete terms, see the repository root
`README.md` / `README_EN.md` / `README_JP.md`.
