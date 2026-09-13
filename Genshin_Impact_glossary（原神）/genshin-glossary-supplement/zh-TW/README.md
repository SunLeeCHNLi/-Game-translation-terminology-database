# 原神術語庫（補充詞庫） — 繁體中文（`zh-TW`）

[← 返回遊戲總說明](../../README.md) · [简体中文](README_zh-CN.md)

本目錄是**以 `zh-TW`（繁體中文）為目標語言**的原神術語庫**補充詞庫**：全局 `genshin-glossary/` 主詞庫按 27 個類目統計共 **8,186** 條詞條，本補充庫收錄主詞庫未包含的詞條，本語言共 **12,221** 行對照（另有別名 `_variants.csv` **332** 行）。`tgt_lng` 欄固定為 `zh-TW`；每行的 `source` 是同一詞條在**其餘 3 種語言（`zh-CN`、`en-US`、`ja-JP`）中的某一種**的寫法，`target` 是繁體中文譯名。

## 與主詞庫的關係

- 本庫只包含**主詞庫中沒有的** `source/target/tgt_lng` 組合，因此可與 `genshin-glossary/zh-TW/` 直接**疊加使用**，不會產生重複條目。
- 資料來源與主詞庫不同（見下文「說明」），同一詞條的寫法可能與主詞庫存在細微差異（用詞、標點等）。
- 本庫涵蓋 4 種目標語言：`zh-CN`、`zh-TW`、`en-US`、`ja-JP`；主詞庫涵蓋 14 種。

## 檔案

- 主類目檔案（9 個，與主詞庫同名）：`characters.csv`、`materials.csv`、`geographies.csv`、`enemies.csv`、`foods.csv`、`animals.csv`、`domains.csv`、`artifacts.csv`、`weapons.csv`
- 別名檔案：`_variants.csv` — 別名／俗稱／常見誤寫，作為額外 `source` 補充
- 額外類目檔案（`extra/` 下 10 個）：`extra/quests.csv`、`extra/events.csv`、`extra/objects.csv`、`extra/system.csv`、`extra/archives.csv`、`extra/story.csv`、`extra/facilities.csv`、`extra/organizations.csv`、`extra/dialogue.csv`、`extra/sereniteapot.csv`

合計 **20 個 CSV 檔案**（9 個主類目 + 1 個別名 + 10 個額外類目），格式統一為三欄：

| source | target | tgt_lng |
| --- | --- | --- |
| Blackcliff Agate | 黑巖緋玉 | zh-TW |
| Blackcliff Longsword | 黑巖長劍 | zh-TW |

目錄結構：

```text
zh-TW/
├── characters.csv
├── materials.csv
├── geographies.csv
├── enemies.csv
├── foods.csv
├── animals.csv
├── domains.csv
├── artifacts.csv
├── weapons.csv
├── _variants.csv
└── extra/
    ├── quests.csv
    ├── events.csv
    ├── objects.csv
    ├── system.csv
    ├── archives.csv
    ├── story.csv
    ├── facilities.csv
    ├── organizations.csv
    ├── dialogue.csv
    └── sereniteapot.csv
```

## 分類與條數

本庫的每個類目都對應上游資料中的**一個來源表**，因此「主題」欄標明該檔案的詞條來自哪裡。所有數字均為本目錄該檔案的實際資料行數。

### 主類目（對應主詞庫的同名類目）

| 分類 | 檔案 | 主題（上游來源） | 行數 |
| --- | --- | --- | ---: |
| characters（角色） | `characters.csv` | characters-*（蒙德／璃月／稻妻／須彌／楓丹／納塔／挪德卡萊／至冬／坎瑞亞／愚人眾等） | 3,796 |
| materials（材料） | `materials.csv` | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials | 738 |
| geographies（地理） | `geographies.csv` | locations | 1,082 |
| enemies（敵人） | `enemies.csv` | enemies | 518 |
| foods（食物） | `foods.csv` | foods | 259 |
| animals（生物） | `animals.csv` | living-beings | 158 |
| domains（秘境） | `domains.csv` | domains | 212 |
| artifacts（聖遺物） | `artifacts.csv` | artifacts | 29 |
| weapons（武器） | `weapons.csv` | weapons | 75 |
| **小計** | 9 個檔案 | — | **6,867** |

### 別名（`_variants.csv`）

| 檔案 | 說明 | 行數 |
| --- | --- | ---: |
| `_variants.csv` | 別名／俗稱／常見誤寫，作為額外 `source` 補充 | 332 |

### 額外類目（`extra/`）

| 分類 | 檔案 | 說明 | 行數 |
| --- | --- | --- | ---: |
| quests（任務） | `extra/quests.csv` | 任務名稱（魔神／世界／傳說／每日／部族等） | 1,652 |
| events（活動） | `extra/events.csv` | 活動名稱 | 1,705 |
| objects（物件） | `extra/objects.csv` | 場景物件 | 447 |
| system（系統） | `extra/system.csv` | 系統與玩法術語 | 343 |
| archives（檔案） | `extra/archives.csv` | 檔案資料 | 347 |
| story（劇情） | `extra/story.csv` | 劇情與章節 | 282 |
| facilities（設施） | `extra/facilities.csv` | 設施與建築 | 226 |
| organizations（組織） | `extra/organizations.csv` | 組織與勢力 | 205 |
| dialogue（對白） | `extra/dialogue.csv` | 對白用語 | 115 |
| sereniteapot（塵歌壺） | `extra/sereniteapot.csv` | 塵歌壺 | 32 |
| **小計** | 10 個檔案 | — | **5,354** |

**本目錄合計：20 個檔案、12,221 行對照（含別名 332 行）。**

## 說明

- **譯文來源與對齊方式**：資料來自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，是社群整理的**遊戲官方在地化文本**彙總，不是二次翻譯或機器生成。對齊以詞條為單位：`target` 為目標語言譯名，`source` 為其餘語言的寫法；本庫已在生成時扣除主詞庫既有的組合，因此可與主詞庫疊加。
- **語言標籤**：本目錄 `tgt_lng` 固定為 `zh-TW`，表示目標語言；`source` 可能是 `zh-CN`、`en-US`、`ja-JP` 中的任意一種。
- **編碼**：全部 CSV 為 **UTF-8 with BOM** 編碼、**CRLF** 換行，首列為表頭，含逗號或引號的欄位依 RFC 4180 轉義（例如 `"""Big Sis"""`）；Excel 可直接雙擊開啟，無需調整編碼。
- **已知限制**：本庫依上游來源表拆分檔案，各類目的涵蓋範圍與主詞庫並不一一對應；`characters.csv` 體量最大，因其包含 NPC 與出場角色。部分詞的英／日／中寫法與主詞庫略有差異，屬正常現象。
- **詞條數與行數說明**：本庫未提供獨立於行數的「去重詞條數」統計，故本頁只給出實際資料行數，不作估算。

## 免責聲明

本目錄為個人整理與維護的**非官方**翻譯術語資料庫，僅用於個人學習、研究及輔助 AI 翻譯軟體（包括但不限於沉浸式翻譯）的術語匹配。本庫與相關遊戲的開發商、發行商、代理商、營運商、版權方不存在任何從屬、授權、合作、代理或官方代表關係；庫中譯名不代表官方立場，不保證始終準確、完整或與遊戲當前版本一致，**不應被視為任何遊戲的官方術語表或官方在地化檔案**。遊戲名稱、角色名稱、專有名詞、商標等智慧財產權均歸各自權利人所有。使用本專案所引發的一切責任由使用者自行承擔。

完整條款見倉庫根目錄 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一個獨立的個人專案，與本遊戲及其開發商、發行商、代理商、版權方不存在任何隸屬、授權、合作或代理關係。**
