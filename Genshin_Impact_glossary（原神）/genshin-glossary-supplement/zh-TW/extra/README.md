# 原神術語庫（補充詞庫）—— 額外類目（`zh-TW/extra`）

## [English](README_EN.md) [日本語](README_JP.md)

本目錄是以繁體中文為目標語言的**額外類目**詞庫：收錄主詞庫與補充詞庫主類目之外的 10 個類目，均為「其他語言詞條 → 繁體中文」的對照，`tgt_lng` 欄固定為 `zh-TW`。本目錄共 **10 個 CSV 檔案、5,354 行對照**。

## 目錄結構

```text
zh-TW/extra/
├── archives（檔案）.csv          347 行
├── dialogue（對話）.csv          115 行
├── events（活動）.csv           1705 行
├── facilities（設施）.csv        226 行
├── objects（物件）.csv           447 行
├── organizations（組織）.csv     205 行
├── quests（任務）.csv           1652 行
├── sereniteapot（塵歌壺）.csv      32 行
├── story（劇情）.csv             282 行
└── system（系統）.csv            343 行
```

## 檔案格式

所有檔案均為 **UTF-8（含 BOM）** 編碼、**CRLF** 換行、首行為表頭，固定三欄：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師的箭羽 | zh-TW |
| Berserker's Battle Mask | 戰狂的鬼面 | zh-TW |

## 類目與行數

| 分類 | 檔案 | 說明 | 行數 |
| --- | --- | --- | ---: |
| quests（任務） | `quests（任務）.csv` | 任務名稱（魔神/世界/傳說/每日/部族等） | 1,652 |
| events（活動） | `events（活動）.csv` | 活動名稱 | 1,705 |
| objects（物件） | `objects（物件）.csv` | 場景物件 | 447 |
| system（系統） | `system（系統）.csv` | 系統與玩法術語 | 343 |
| archives（檔案） | `archives（檔案）.csv` | 檔案資料 | 347 |
| story（劇情） | `story（劇情）.csv` | 劇情與章節 | 282 |
| facilities（設施） | `facilities（設施）.csv` | 設施與建築 | 226 |
| organizations（組織） | `organizations（組織）.csv` | 組織與勢力 | 205 |
| dialogue（對話） | `dialogue（對話）.csv` | 對白用語 | 115 |
| sereniteapot（塵歌壺） | `sereniteapot（塵歌壺）.csv` | 塵歌壺 | 32 |
| **合計** | 10 個檔案 | — | **5,354** |

## 說明

- 每行的 `source` 是同一詞條在**其餘 3 種語言（`zh-CN`、`en-US`、`ja-JP`）中的某一種**的寫法，`target` 是繁體中文譯名。
- 資料來自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，為社群整理的**遊戲官方在地化文本**，不是二次翻譯或機器生成。
- 本目錄可與 `../` 下的 9 個主類目 CSV 與別名檔案疊加使用；完整語言級說明請見 `../README.md`。
- 遊戲級總說明見 `../../README.md` / `../../README_EN.md` / `../../README_JP.md`。
