# 《星塔旅人》Stella Sora 術語庫 — 繁體中文（`zh-TW`）

[← 返回遊戲總說明](../README.md)

本目錄是**以 `zh-TW`（繁體中文）為目標語言**的術語庫：每一條都是「其他語言寫法 → 繁體中文」的對照，共 **12292** 條詞條、**46052** 行對照，`tgt_lng` 欄固定為 `zh-TW`，`source` 欄收錄 `zh-CN` / `en-US` / `ja-JP` / `ko-KR` 四種語言裡同一詞條的寫法。需要每一條目五語並排的完整檢視，請見 `00_master/README.md` 與 `../multilingual/00_master/`。

## 檔案

- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 三欄，可直接匯入 CAT / 術語管理工具
- `NN_xxx/NN_xxx_terms.csv` — 本語言詞條清單（`id,term,src_table`），適合校對與回查
- `00_master/all_glossary.csv` — 全部 15 個分類的對照列合併總表（`category,source,target,tgt_lng`）
- `00_master/all_terms.csv` — 本語言全部詞條清單（`category,category_label,id,term,src_table`）
- `00_master/index.csv` — 分類索引與條數（`category,label,term_count,glossary_file,terms_file,target_language`）
- `00_master/README.md` — 本語言庫既有的詳細說明

`NN_xxx/` 是 15 個分類目錄，每個目錄下只有上面兩個檔案。`terms.csv` 的一條資料列對應一條詞條，`glossary.csv` 的每一列是一條 `source → target` 對照。

## 分類與條數

數字取自 `00_master/index.csv`，並與 15 個分類 CSV、`00_master/all_terms.csv`、`00_master/all_glossary.csv` 的實際資料列數逐項核對一致。

| 分類 | 主題 | 條數 | 對照列 |
| --- | --- | ---: | ---: |
| `01_character` | 角色名稱 | 287 | 977 |
| `02_skill` | 技能名稱 | 628 | 2273 |
| `03_potential` | 潛能名稱 | 1457 | 5545 |
| `04_disc` | 唱片 / Disc | 234 | 896 |
| `05_item` | 道具 | 558 | 2176 |
| `06_equipment` | 裝備 | 15 | 58 |
| `07_enemy` | 敵人 | 399 | 1547 |
| `08_stage` | 關卡 | 1019 | 3856 |
| `09_event` | 活動 | 581 | 2228 |
| `10_system` | 系統術語 | 1055 | 4121 |
| `11_ui` | UI術語 | 4248 | 15540 |
| `12_story` | 劇情專有名詞 | 527 | 2022 |
| `13_faction` | 陣營 | 21 | 78 |
| `14_location` | 地點 | 27 | 98 |
| `15_terminology` | 遊戲機制術語 | 1236 | 4637 |
| **合計** | | **12292** | **46052** |

## 說明

- **譯文來源與對齊方式**：譯文全部取自遊戲官方多語言文本庫 `StellaSoraData-main`（官方 CN / EN / JP / KR / TW 五區客戶端文本），各語言按同一文本鍵對齊，屬於**官方在地化**而非二次翻譯；每條詞條會把其餘四種語言的寫法展開為對照列，因此本目錄也可反向當作「繁體中文 → 其他語言」查詢。
- **語言標籤**：本庫出現的五種標籤為 `zh-CN` 簡體中文、`zh-TW` 繁體中文、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어；本目錄的 `tgt_lng` 一律為 `zh-TW`。
- **編碼**：所有 CSV 為 UTF-8 with BOM、CRLF 換行，Excel 按兩下即可正確顯示中日韓文字；本說明檔為 UTF-8（無 BOM）。
- **對照列為何少於「條數 × 4」**：拆分腳本會去掉與目標語言寫法完全相同的 `source`，以及同一分類內已經出現過的 `source` → `target` 對照列（`06_equipment` 只有 15 條詞條、58 列對照即由此而來）。
- **已知限制**：
  - 台詞、劇情正文、道具描述等長篇內容不在術語庫範圍內；
  - `14_location` 中除 `DatingLandmark` 與 `StarTower` 外，其餘地名由人工校訂補入（來源標註為 `curated (aligned in-game text)`）；
  - `06_equipment` 僅 15 條：本作沒有傳統武器 / 防具表，裝備位由「秘紋（Disc）」承擔；
  - 本目錄內有 962 個 `source` 對應多個 `target`，多來自同名不同物的短詞（例如韓文 `윌로` 同時對應「沐夏薇洛」與「薇洛」）；按 `source` 去重的工具只會保留其中一條，需要區分時請用 `terms.csv` 裡的 `id` 與 `src_table` 回查上下文。
- **重新產生**：本目錄由 `tools/split_by_language.py` 從 `multilingual/` 拆分得到，腳本使用寫死的外部絕對路徑（`E:\Download\BT\Codex_input\StellaSora_Glossary`），**不會讀寫本倉庫**；詳見遊戲根目錄 `README.md` 的「生成與複現」。

## 免責聲明

本目錄為個人整理與維護的**非官方**繁體中文翻譯術語資料庫，僅用於個人學習、研究及輔助 AI 翻譯軟體（包括但不限於沉浸式翻譯）的術語匹配。本庫與《星塔旅人》及其開發商、發行商、代理商、版權方不存在任何從屬、授權、合作、代理或官方代表關係；庫中譯名不代表官方立場，不保證始終準確、完整或與遊戲當前版本一致，**不應被視為任何遊戲的官方術語表或官方在地化檔案**。遊戲名稱、角色名稱、專有名詞、商標等智慧財產權均歸各自權利人所有。使用本庫及基於其產生的翻譯結果所引發的一切責任由使用者自行承擔。如權利人認為內容不當，歡迎透過 GitHub Issues / Pull Request 聯繫，維護者將核實後修改或刪除。完整條款見倉庫根目錄 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一個獨立的個人專案，與本遊戲及其開發商、發行商、代理商、版權方不存在任何隸屬、授權、合作或代理關係。**
