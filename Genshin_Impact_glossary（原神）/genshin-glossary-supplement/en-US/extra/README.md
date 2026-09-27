# Genshin Impact Terminology (Supplement) — Extra Categories (`en-US/extra`)

## [简体中文](README_zh-CN.md) [日本語](README_JP.md)

This directory holds the **extra categories** for the English edition of the supplement. It covers the 10 categories that sit outside the main categories of the main glossary and supplement, all as "term in another language → English" alignments with `tgt_lng` fixed to `en-US`. This directory contains **10 CSV files, 5,973 alignment rows**.

## Directory Structure

```text
en-US/extra/
├── archives.csv          386 rows
├── dialogue.csv          123 rows
├── events.csv           1842 rows
├── facilities.csv        270 rows
├── objects.csv           508 rows
├── organizations.csv     243 rows
├── quests.csv           1769 rows
├── sereniteapot.csv       37 rows
├── story.csv             348 rows
└── system.csv            447 rows
```

## File Format

Every file is **UTF-8 (with BOM)**, **CRLF** line endings, with a header row and exactly three columns:

| source | target | tgt_lng |
| --- | --- | --- |
| フィナーレの時計 | Concert's Final Hour | en-US |
| 不動 | Unyielding | en-US |

## Categories and Counts

| Category | File | Description | Rows |
| --- | --- | --- | ---: |
| quests | `quests.csv` | Quest names (Archon / World / Story / Daily / Tribal, etc.) | 1,769 |
| events | `events.csv` | Event names | 1,842 |
| objects | `objects.csv` | Scene objects | 508 |
| system | `system.csv` | System and gameplay terms | 447 |
| archives | `archives.csv` | Archive material | 386 |
| story | `story.csv` | Story and chapters | 348 |
| facilities | `facilities.csv` | Facilities and buildings | 270 |
| organizations | `organizations.csv` | Organizations and factions | 243 |
| dialogue | `dialogue.csv` | Dialogue wording | 123 |
| sereniteapot | `sereniteapot.csv` | Serenitea Pot | 37 |
| **Total** | 10 files | — | **5,973** |

## Notes

- In each row, `source` is the term as written in **one of the other three languages** (`zh-CN`, `zh-TW`, `ja-JP`) and `target` is the English name.
- The data comes from [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata), a community collection of the game's **official localized text** — not a retranslation or machine output.
- This directory can be stacked on top of the 9 main-category CSVs and the alias file in `../`; for the full language-level notes see `../README.md`.
- The game-level overview is in `../../README.md` / `../../README_EN.md` / `../../README_JP.md`.
