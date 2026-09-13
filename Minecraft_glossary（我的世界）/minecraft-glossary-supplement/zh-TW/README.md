# 我的世界（Minecraft） Wiki 譯名標準化補充詞庫 — 繁體中文（`zh-TW`）

[← 返回遊戲總說明](../../README.md)

本目錄是 `minecraft-glossary/` 的**補充詞庫**，**以繁體中文（`zh-TW`）為目標語言**，
共 **13 個 CSV 檔案**（13 個分類）、**5,157 行對照**。詞條取自
[Minecraft Wiki:譯名標準化](https://zh.minecraft.wiki/w/Minecraft_Wiki:譯名標準化) 頁面，
用於補充官方語言檔案未涵蓋、或與 Wiki 標準不一致的譯名；`tgt_lng` 欄固定為 `zh-TW`。

## 檔案

- `<分類>.csv`（13 個）— `source,target,tgt_lng` 三欄，可直接匯入 CAT / 術語管理工具；本補充庫**沒有** `extra/` 子目錄

## 分類與條數

| 分類 | 主題 | 檔案 | 對照行 |
| --- | --- | --- | --- |
| `advancements` | 進度 | `advancements.csv` | 242 |
| `biomes` | 生物群系 | `biomes.csv` | 117 |
| `blocks` | 方塊 | `blocks.csv` | 2,561 |
| `effects` | 狀態效果 | `effects.csv` | 73 |
| `enchantments` | 附魔 | `enchantments.csv` | 82 |
| `entities` | 實體 | `entities.csv` | 289 |
| `environment` | 環境 | `environment.csv` | 205 |
| `game-content` | 遊戲內容 | `game-content.csv` | 113 |
| `game-modes` | 遊戲模式 | `game-modes.csv` | 31 |
| `game-versions` | 遊戲版本 | `game-versions.csv` | 101 |
| `items` | 物品 | `items.csv` | 1,178 |
| `other` | 其他 | `other.csv` | 64 |
| `technical` | 技術性內容 | `technical.csv` | 101 |

### 檔案清單

```text
minecraft-glossary-supplement/
+-- zh-CN/
|   |-- advancements.csv
|   |-- biomes.csv
|   |-- blocks.csv
|   |-- effects.csv
|   |-- enchantments.csv
|   |-- entities.csv
|   |-- environment.csv
|   |-- game-content.csv
|   |-- game-modes.csv
|   |-- game-versions.csv
|   |-- items.csv
|   |-- other.csv
|   \-- technical.csv
+-- zh-TW/
|   |-- advancements.csv
|   |-- biomes.csv
|   |-- blocks.csv
|   |-- effects.csv
|   |-- enchantments.csv
|   |-- entities.csv
|   |-- environment.csv
|   |-- game-content.csv
|   |-- game-modes.csv
|   |-- game-versions.csv
|   |-- items.csv
|   |-- other.csv
|   \-- technical.csv
```

## 說明

- **譯文來源與對齊方式。** 詞條來自 Minecraft Wiki「譯名標準化」頁面（分別抓取 `zh-cn` 與 `zh-tw`
  兩種變體後合併）。頁面中的譯名與 Crowdin 上已確定的官方在地化方案保持一致，未確定時暫用遊戲內
  原文。同一詞條會以 `en-US` 與另一中文變體分別作為 `source` 各出現一行。

- **語言標籤。** `tgt_lng` 固定為 `zh-TW`。本補充庫**僅涵蓋繁體中文與簡體中文**兩種目標語言，
  其餘語言請使用主詞庫 `minecraft-glossary/`。

- **編碼說明。** 所有 CSV 均為 **UTF-8（含 BOM）**、**CRLF** 換行、首列為表頭；含逗號、引號或換行的
  欄位依 RFC 4180 加引號跳脫。與主詞庫不同，本目錄的 CSV **不含**引號內換行，實體行數即等於對照
  行數（13 個檔案共 5,170 行 = 5,157 行對照 + 13 列表頭）。

- **與主詞庫的差異。** Wiki 採用「台灣正體」用詞（例如 `Chest` = 儲物箱、`Slab` = 半磚、
  `Stairs` = 階梯），與遊戲內繁體中文語言檔案可能存在差異，兩份資料建議按需取用。標註為「不翻譯」
  的詞條（如 `Mojang`、`Minecraft`）不收錄於本詞庫。同一英文名對應多個中文寫法時，使用 Wiki 的
  寫法並以 ` / ` 連接（例如 `Boolean` = 布林值 / 布林型）。

- **已知限制。** 「詞條數」指按英文名去重後的標準中文名條數（13 個分類合計 2,772 條），與
  「對照行數」（5,157 行）不是同一個數字：同一詞條會因 `source` 不同而重複出現。該口徑與遊戲根目錄
  `../../README.md`「數據概覽」中補充詞庫的定義一致。本庫不是官方語言檔案的替代品，二者建議搭配使用。

- **複現方式。** 先抓取該頁面的 `zh-cn` / `zh-tw` 兩種變體（`action=parse&prop=text&variant=...`），
  再執行 `python tools/build_wiki_supplement.py`（在遊戲根目錄下執行，腳本讀取外部資料目錄）。

## 免責聲明

本目錄為個人整理與維護的**非官方**翻譯術語資料庫，僅用於個人學習、研究及輔助 AI 翻譯軟體的
術語匹配。本庫與遊戲的開發商、發行商、代理商、營運商、版權方不存在任何從屬、授權、合作、代理或
官方代表關係；庫中譯名不代表官方立場，不應被視為任何遊戲的官方術語表或官方在地化檔案。遊戲名稱、
角色名稱、專有名詞、商標等智慧財產權均歸各自權利人所有。使用本專案及基於其產生的翻譯結果所引發
的一切責任由使用者自行承擔。完整條款見倉庫根目錄 `README.md` / `README_EN.md` / `README_JP.md`。
