# Genshin Impact Terminology (Supplement) — Extra Categories (`ja-JP/extra`)

## [日本語](README.md) [简体中文](README_zh-CN.md)

This directory holds the **extra categories** of the supplement whose target language is Japanese. It covers the 10 categories that sit outside the main categories of the main glossary and supplement, all as "term in another language → Japanese" alignments with `tgt_lng` fixed to `ja-JP`. This directory contains **10 CSV files, 5,690 alignment rows**.

## Directory Structure

```text
ja-JP/extra/
├── archives（書庫）.csv          382 rows
├── dialogue（会話）.csv          121 rows
├── events（イベント）.csv        1796 rows
├── facilities（施設）.csv        236 rows
├── objects（オブジェクト）.csv   472 rows
├── organizations（組織）.csv     209 rows
├── quests（任務）.csv           1753 rows
├── sereniteapot（塵歌壺）.csv      32 rows
├── story（ストーリー）.csv        302 rows
└── system（システム）.csv         387 rows
```

## File Format

Every file is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row and exactly three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師の矢羽 | ja-JP |
| Berserker's Battle Mask | 狂戦士の仮面 | ja-JP |

## Categories and Counts

| Category | File | Description | Rows |
| --- | --- | --- | ---: |
| quests | `quests（任務）.csv` | Quest names (Archon / World / Story / Daily / Tribal, etc.) | 1,753 |
| events | `events（イベント）.csv` | Event names | 1,796 |
| objects | `objects（オブジェクト）.csv` | Scene objects | 472 |
| system | `system（システム）.csv` | System and gameplay terms | 387 |
| archives | `archives（書庫）.csv` | Archive material | 382 |
| story | `story（ストーリー）.csv` | Story and chapters | 302 |
| facilities | `facilities（施設）.csv` | Facilities and buildings | 236 |
| organizations | `organizations（組織）.csv` | Organizations and factions | 209 |
| dialogue | `dialogue（会話）.csv` | Dialogue wording | 121 |
| sereniteapot | `sereniteapot（塵歌壺）.csv` | Serenitea Pot | 32 |
| **Total** | 10 files | — | **5,690** |

## Notes

- In each row, `source` is the term as written in **one of the other three languages** (`zh-CN`, `zh-TW`, `en-US`) and `target` is the Japanese name.
- The data comes from [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata), a community collection of the game's **official localized text** — not a retranslation or machine output.
- This directory can be stacked on top of the 9 main-category CSVs and the alias file in `../`; for the full language-level notes see `../README.md`.
- The game-level overview is in `../../README.md` / `../../README_EN.md` / `../../README_JP.md`.
