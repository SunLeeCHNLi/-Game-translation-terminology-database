# 原神術語庫 — 繁體中文（`zh-TW`）

[← 返回遊戲總說明](../../README.md) · [简体中文](README_zh-CN.md)

本目錄是**以 `zh-TW`（繁體中文）為目標語言**的原神術語庫：按 27 個類目統計，全局共 **8,186** 條詞條，本語言共 **89,434** 行對照。`tgt_lng` 欄固定為 `zh-TW`；每行的 `source` 是同一詞條在**其餘 13 種語言中的某一種**的寫法，`target` 是繁體中文譯文。檔案按**類目**分列，每個類目一個 CSV。

## 檔案

- `characters.csv`、`talents.csv`、`constellations.csv`、`weapons.csv`、`materials.csv`、`foods.csv`、`crafts.csv`、`artifacts.csv`、`domains.csv`、`enemies.csv`、`animals.csv`、`outfits.csv`、`windgliders.csv`、`namecards.csv`、`geographies.csv`、`achievements.csv`、`adventureranks.csv` — 17 個主類目檔案
- `TCG/action-cards.csv`、`TCG/character-cards.csv`、`TCG/enemy-cards.csv`、`TCG/summons.csv`、`TCG/status-effects.csv`、`TCG/keywords.csv`、`TCG/card-backs.csv`、`TCG/card-boxes.csv`、`TCG/detailed-rules.csv`、`TCG/level-rewards.csv` — 10 個 TCG（七聖召喚）子類目檔案

合計 **27 個 CSV 檔案**，格式統一為三欄：

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | 空 | zh-TW |
| Leer | 空 | zh-TW |

目錄結構：

```text
zh-TW/
├── characters.csv
├── talents.csv
├── constellations.csv
├── weapons.csv
├── materials.csv
├── foods.csv
├── crafts.csv
├── artifacts.csv
├── domains.csv
├── enemies.csv
├── animals.csv
├── outfits.csv
├── windgliders.csv
├── namecards.csv
├── geographies.csv
├── achievements.csv
├── adventureranks.csv
└── TCG/
    ├── action-cards.csv
    ├── character-cards.csv
    ├── enemy-cards.csv
    ├── summons.csv
    ├── status-effects.csv
    ├── keywords.csv
    ├── card-backs.csv
    ├── card-boxes.csv
    ├── detailed-rules.csv
    └── level-rewards.csv
```

## 分類與條數

「詞條」為該類目在全部 14 種語言中的**去重詞條數**（同一類目各語言相同）；「行數」為本目錄該檔案的資料行數。

### 主類目

| 分類 | 檔案 | 詞條數 | 行數 |
| --- | --- | ---: | ---: |
| characters（角色） | `characters.csv` | 122 | 577 |
| talents（天賦） | `talents.csv` | 125 | 632 |
| constellations（命之座） | `constellations.csv` | 125 | 632 |
| weapons（武器） | `weapons.csv` | 249 | 2,823 |
| materials（材料） | `materials.csv` | 919 | 10,636 |
| foods（食物） | `foods.csv` | 398 | 4,541 |
| crafts（合成物） | `crafts.csv` | 295 | 3,522 |
| artifacts（聖遺物） | `artifacts.csv` | 63 | 727 |
| domains（秘境） | `domains.csv` | 284 | 3,636 |
| enemies（敵人） | `enemies.csv` | 346 | 4,104 |
| animals（生物） | `animals.csv` | 223 | 2,647 |
| outfits（裝扮） | `outfits.csv` | 150 | 1,869 |
| windgliders（風之翼） | `windgliders.csv` | 18 | 211 |
| namecards（名片） | `namecards.csv` | 289 | 3,606 |
| geographies（地理） | `geographies.csv` | 268 | 3,389 |
| achievements（成就） | `achievements.csv` | 1,548 | 19,464 |
| adventureranks（冒險等階） | `adventureranks.csv` | 21 | 157 |
| **小計** | 17 個檔案 | — | **63,173** |

### TCG 子類目（`TCG/`）

| 子類目 | 檔案 | 詞條數 | 行數 |
| --- | --- | ---: | ---: |
| action-cards（行動牌） | `TCG/action-cards.csv` | 927 | 9,608 |
| character-cards（角色牌） | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards（敵人牌） | `TCG/enemy-cards.csv` | 134 | 1,114 |
| summons（召喚物） | `TCG/summons.csv` | 152 | 1,139 |
| status-effects（狀態效果） | `TCG/status-effects.csv` | 1,159 | 11,210 |
| keywords（關鍵詞） | `TCG/keywords.csv` | 139 | 1,511 |
| card-backs（牌背） | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes（牌盒） | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules（詳細規則） | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards（等級獎勵） | `TCG/level-rewards.csv` | 26 | 169 |
| **小計** | 10 個檔案 | — | **26,261** |

**本目錄合計：27 個檔案、89,434 行。**

## 說明

- **譯文來源與對齊方式**：資料來自 [theBowja/genshin-db](https://github.com/theBowja/genshin-db)（資料版本 7.0，涵蓋全部 14 種語言），是**遊戲官方在地化文本**，不是二次翻譯或機器生成。對齊以詞條為單位：同一詞條會以其餘每一種語言作為 `source` 各出一行，因此行數遠大於詞條數。
- **語言標籤**：本目錄 `tgt_lng` 固定為 `zh-TW`，表示目標語言；`source` 可能是其餘 13 種語言（`zh-CN`、`en-US`、`ja-JP`、`ko-KR`、`fr-FR`、`de-DE`、`es-ES`、`ru-RU`、`pt-BR`、`it-IT`、`tr-TR`、`th-TH`、`vi-VN`）中的任意一種。
- **編碼**：全部 CSV 為 **UTF-8 with BOM** 編碼、**CRLF** 換行，首列為表頭，含逗號或引號的欄位依 RFC 4180 轉義；Excel 可直接雙擊開啟，無需調整編碼。
- **已知限制**：各類目行數在不同語言間略有差異（例如部分 `achievements`、`adventureranks` 條目並非每種語言都存在）。跨類目存在同名詞條（例如某武器名同時出現在 `weapons` 與 `TCG` 中），因此各檔案行數相加會大於全局去重後的詞條數。官方未翻譯的名稱保留原文形態。
- **補充詞庫**：同級目錄 `genshin-glossary-supplement/` 收錄主詞庫未包含的詞條，可與本庫疊加使用，詳見該庫的 `README.md`。

## 免責聲明

本目錄為個人整理與維護的**非官方**翻譯術語資料庫，僅用於個人學習、研究及輔助 AI 翻譯軟體（包括但不限於沉浸式翻譯）的術語匹配。本庫與相關遊戲的開發商、發行商、代理商、營運商、版權方不存在任何從屬、授權、合作、代理或官方代表關係；庫中譯名不代表官方立場，不保證始終準確、完整或與遊戲當前版本一致，**不應被視為任何遊戲的官方術語表或官方在地化檔案**。遊戲名稱、角色名稱、專有名詞、商標等智慧財產權均歸各自權利人所有。使用本專案所引發的一切責任由使用者自行承擔。

完整條款見倉庫根目錄 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一個獨立的個人專案，與本遊戲及其開發商、發行商、代理商、版權方不存在任何隸屬、授權、合作或代理關係。**
