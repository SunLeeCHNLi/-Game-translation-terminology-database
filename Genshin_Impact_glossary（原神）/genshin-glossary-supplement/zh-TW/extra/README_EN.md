# Genshin Impact Terminology (Supplement) — Extra Categories (`zh-TW/extra`)

## [繁體中文](README.md) [日本語](README_JP.md)

This directory holds the **extra categories** for the Traditional Chinese edition of the supplement. It covers the 10 categories that sit outside the main categories of the main glossary and supplement, all as "term in another language → Traditional Chinese" alignments with `tgt_lng` fixed to `zh-TW`. This directory contains **10 CSV files, 5,354 alignment rows**.

## Directory Structure

```text
zh-TW/extra/
├── archives（檔案）.csv          347 rows
├── dialogue（對話）.csv          115 rows
├── events（活動）.csv           1705 rows
├── facilities（設施）.csv        226 rows
├── objects（物件）.csv           447 rows
├── organizations（組織）.csv     205 rows
├── quests（任務）.csv           1652 rows
├── sereniteapot（塵歌壺）.csv      32 rows
├── story（劇情）.csv             282 rows
└── system（系統）.csv            343 rows
```

## File Format

Every file is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row and exactly three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師的箭羽 | zh-TW |
| Berserker's Battle Mask | 戰狂的鬼面 | zh-TW |

## Categories and Counts

| Category | File | Description | Rows |
| --- | --- | --- | ---: |
| quests（任務） | `quests（任務）.csv` | Quest names (Archon / World / Story / Daily / Tribal, etc.) | 1,652 |
| events（活動） | `events（活動）.csv` | Event names | 1,705 |
| objects（物件） | `objects（物件）.csv` | Scene objects | 447 |
| system（系統） | `system（系統）.csv` | System and gameplay terms | 343 |
| archives（檔案） | `archives（檔案）.csv` | Archive material | 347 |
| story（劇情） | `story（劇情）.csv` | Story and chapters | 282 |
| facilities（設施） | `facilities（設施）.csv` | Facilities and buildings | 226 |
| organizations（組織） | `organizations（組織）.csv` | Organizations and factions | 205 |
| dialogue（對話） | `dialogue（對話）.csv` | Dialogue wording | 115 |
| sereniteapot（塵歌壺） | `sereniteapot（塵歌壺）.csv` | Serenitea Pot | 32 |
| **Total** | 10 files | — | **5,354** |

## Notes

- In each row, `source` is the term as written in **one of the other three languages** (`zh-CN`, `en-US`, `ja-JP`) and `target` is the Traditional Chinese name.
- The data comes from [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata), a community collection of the game's **official localized text** — not a retranslation or machine output.
- This directory can be stacked on top of the 9 main-category CSVs and the alias file in `../`; for the full language-level notes see `../README.md`.
- The game-level overview is in `../../README.md` / `../../README_EN.md` / `../../README_JP.md`.
