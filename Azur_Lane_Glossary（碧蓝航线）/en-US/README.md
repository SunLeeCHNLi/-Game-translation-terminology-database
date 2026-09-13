# Azur Lane Terminology Database — English (`en-US`)

[← Back to the game overview](../README.md)

This directory is the *Azur Lane* termbase with **English (`en-US`) as the target language**: the
`target` column always holds the English reading, while `source` holds the readings in Simplified
Chinese, Japanese, Traditional Chinese and Korean. It contains **6 CSV files, 12 600 comparison rows**,
of which the three main tables hold **6 283 rows / 821 + 855 + 154 distinct entries**.
The English names are extracted directly from the official EN client data (with the EN client's own
`english_name` hull designation used as a fallback) — they are **official localisation text, not
machine translation**.

## Files

- `azur_lane_glossary.csv` — columns `source,target,tgt_lng`, 2795 rows; ship names, standard-name table, ready for CAT / terminology tools
- `azur_lane_glossary_detailed.csv` — 2809 rows; adds `src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives`
- `azur_lane_ship_character_glossary.csv` — columns `source,target,tgt_lng`, 3084 rows; `target` is the name the Simplified-Chinese client actually displays (harmonised name where one exists)
- `azur_lane_ship_character_glossary_detailed.csv` — 3104 rows; same extra columns as above
- `azur_lane_terms.csv` — columns `source,target,tgt_lng`, 404 rows; naval / military / in-game terminology
- `azur_lane_terms_detailed.csv` — 404 rows; adds `src_lng,category,category_zh,same_source_alternatives`

The sibling `by_language/` directory holds the ship sub-tables split by source language (their `target`
is always Simplified Chinese), and `sources/` holds the scrape of the Moegirlpedia
“Azur Lane / name table” used for cross-checking harmonised names.

## Categories and counts

| File | Rows | Entries (distinct `target`) |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 2795 | 821 |
| `azur_lane_glossary_detailed.csv` | 2809 | 823 |
| `azur_lane_ship_character_glossary.csv` | 3084 | 855 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3104 | 857 |
| `azur_lane_terms.csv` | 404 | 154 |
| `azur_lane_terms_detailed.csv` | 404 | 154 |

Ship variants (grouped by the `variant` column of `azur_lane_ship_character_glossary_detailed.csv`):

| Variant | Ships (distinct `ship_id`) | Rows |
| --- | --- | --- |
| Base hull (no variant tag) | 788 | 2760 |
| META | 60 | 225 |
| μ-equipment | 19 | 82 |
| Type II | 10 | 37 |
| **Total** | **877** | **3104** |

(“Ships” counts distinct `ship_id` values; the same table has **857** distinct `target` values, because a
few ships share one displayed English name under different ids.)

Terminology categories (grouped by the `category` column of `azur_lane_terms_detailed.csv`):

| `category` | Topic | Entries | Rows |
| --- | --- | --- | --- |
| `hull_type` | Hull / ship types | 29 | 78 |
| `naval_term` | Naval and military terms | 67 | 186 |
| `navy_prefix` | Factions and hull prefixes | 23 | 56 |
| `rank` | Ranks | 13 | 27 |
| `game_term` | In-game terminology | 22 | 57 |
| **Total** | — | **154** | **404** |

## Notes

- **Translation source and alignment**: ship names come from the official CN / EN / JP / KR / TW client
  data (`ship_data_statistics.json` and friends); ship identity is normalised through `ship_group` in
  `ship_skin_template.json` and enemy / NPC copies are filtered with `ship_data_template.json`. A few
  ships ship no English name at all in the EN client; for those the EN client's own `english_name` is
  used with the `USS`/`HMS` hull prefix stripped. Terminology entries are curated by hand and checked
  against each client. Each source string keeps exactly one translation in the main table of this
  directory; when it has several readings the one with the **lowest ship id** wins and every reading is
  recorded in the `same_source_alternatives` column of the detail table.
- **Language tags**: `tgt_lng` is fixed to `en-US` in every CSV here. `src_lng` in the detail tables is
  one of `zh-CN`, `ja-JP`, `zh-TW`, `ko-KR` (four-letter tags), and one of `en-US`, `ja-JP`, `ko-KR`,
  `zh-CN` in the terminology detail table. Note that the `zh-CN` directory uses the short tags
  `en` / `ja` / `ko` / `zh-TW` instead — the tag style is inconsistent between directories, and no
  translation is affected by it. The `by_language/azur_lane_glossary_en-zh-CN.csv` sibling is the same
  English source strings viewed with Simplified Chinese as the target.
- **Encoding**: every CSV is **UTF-8 with BOM + CRLF**, so Excel opens them directly; the `.md` files are
  UTF-8 without BOM.
- **Known limitations**:
  - English names are missing for some ships because the EN client itself has no name for them; those
    rows fall back to the client's `english_name` hull designation (e.g. `Enterprise META` style
    entries) and may look different from the in-game display name.
  - In the EN client the ship name of `皇家方舟·META` is stored as `Royal.META` (the `Ark` is missing),
    contradicting that client's own `english_name`, `Ark Royal.META`. This is an original game-data flaw
    and has not been rewritten.
  - 亚尔薇特 (Alvitr, an Iron Blood battlecruiser, ship_id 404061) is the only Iron Blood shipgirl
    without a Simplified-Chinese harmonised name.
  - The count of distinct `ship_id` values (877) is higher than the count of distinct `target` values
    (857), because a few English names are shared by more than one ship id (event / NPC copies).
  - Only the `zh-CN` directory provides an ambiguity table and a merged ships+terms table; this directory
    deliberately does not duplicate them.

## Disclaimer

This directory is an **unofficial** translation-terminology resource compiled and maintained by an
individual, intended only for personal study and research and for terminology matching in AI translation
software (including but not limited to Immersive Translate). It **must not be regarded as the official
glossary or official localisation file of *Azur Lane***. The translations here do not represent any
official position and are not guaranteed to be accurate, complete or consistent with the current game
version; all intellectual property in game names, character names, proper nouns and trademarks belongs
to its respective owners, and no claim is made to any such rights. Any liability arising from the use of
this project rests with the user.

The full terms are in the repository root `README.md` / `README_EN.md` / `README_JP.md`.
