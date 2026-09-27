# Genshin Impact Terminology (Supplement) — Extra Categories (`zh-CN/extra`)

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds the **extra categories** for the Simplified Chinese edition of the supplement. It covers the 10 categories that sit outside the main categories of the main glossary and supplement, all as "term in another language → Simplified Chinese" alignments with `tgt_lng` fixed to `zh-CN`. This directory contains **10 CSV files, 5,423 alignment rows**.

## Directory Structure

```text
zh-CN/extra/
├── archives（档案）.csv          345 rows
├── dialogue（对话）.csv          117 rows
├── events（活动）.csv          1715 rows
├── facilities（设施）.csv        234 rows
├── objects（物件）.csv           459 rows
├── organizations（组织）.csv     213 rows
├── quests（任务）.csv          1664 rows
├── sereniteapot（尘歌壶）.csv      33 rows
├── story（剧情）.csv             286 rows
└── system（系统）.csv            357 rows
```

## File Format

Every file is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row and exactly three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴师的箭羽 | zh-CN |
| Berserker's Battle Mask | 战狂的鬼面 | zh-CN |

## Categories and Counts

| Category | File | Description | Rows |
| --- | --- | --- | ---: |
| quests（任务） | `quests（任务）.csv` | Quest names (Archon / World / Story / Daily / Tribal, etc.) | 1,664 |
| events（活动） | `events（活动）.csv` | Event names | 1,715 |
| objects（物件） | `objects（物件）.csv` | Scene objects | 459 |
| system（系统） | `system（系统）.csv` | System and gameplay terms | 357 |
| archives（档案） | `archives（档案）.csv` | Archive material | 345 |
| story（剧情） | `story（剧情）.csv` | Story and chapters | 286 |
| facilities（设施） | `facilities（设施）.csv` | Facilities and buildings | 234 |
| organizations（组织） | `organizations（组织）.csv` | Organizations and factions | 213 |
| dialogue（对话） | `dialogue（对话）.csv` | Dialogue wording | 117 |
| sereniteapot（尘歌壶） | `sereniteapot（尘歌壶）.csv` | Serenitea Pot | 33 |
| **Total** | 10 files | — | **5,423** |

## Notes

- In each row, `source` is the term as written in **one of the other three languages** (`zh-TW`, `en-US`, `ja-JP`) and `target` is the Simplified Chinese name.
- The data comes from [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata), a community collection of the game's **official localized text** — not a retranslation or machine output.
- This directory can be stacked on top of the 9 main-category CSVs and the alias file in `../`; for the full language-level notes see `../README.md`.
- The game-level overview is in `../../README.md` / `../../README_EN.md` / `../../README_JP.md`.
