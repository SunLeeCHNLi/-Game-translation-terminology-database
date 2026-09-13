# 鳴潮（Wuthering Waves）術語庫 — 繁體中文（`zh-TW`）

[← 返回遊戲總說明](../../README.md) ｜ [← wuwa-glossary 子庫說明](../README.md)

本目錄是**以 `zh-TW`（繁體中文）為目標語言**的鳴潮（Wuthering Waves）術語庫。共 **123,230** 條詞條、**645,529** 行對照（本目錄 23 個 CSV 的資料列合計），目錄體積約 **55.7 MiB**。所有 CSV 的 `tgt_lng` 欄固定為 `zh-TW`；`source` 欄收錄其餘 9 種語言（`zh-CN`（简体中文）、`en-US`（English）、`ja-JP`（日本語）、`ko-KR`（한국어）、`fr-FR`（Français）、`de-DE`（Deutsch）、`es-ES`（Español）、`pt-BR`（Português）、`th-TH`（ภาษาไทย））的寫法，因此同一條遊戲文字可以從任一種語言對應到本語言的譯名。

## 檔案

本目錄為**扁平結構**，23 個類目 CSV 直接放在本目錄下，沒有額外的子目錄：

- `characters.csv` — 角色名稱
- `weapons.csv` — 武器名稱
- `echoes.csv` — 聲骸
- `skills.csv` — 技能
- `resonant-chains.csv` — 共鳴鏈
- `quests.csv` — 任務
- `dungeons.csv` — 關卡與挑戰
- `regions.csv` — 地區與地圖
- `factions.csv` — 陣營與勢力
- `items.csv` — 道具與材料
- `monsters.csv` — 怪物與生物
- `npcs.csv` — NPC 與說話人
- `achievements.csv` — 成就
- `activities.csv` — 活動與玩法
- `buffs.csv` — 增益與效果
- `voice-lines.csv` — 角色語音
- `archives.csv` — 檔案與讀物
- `terms.csv` — 術語與百科
- `system.csv` — 系統文字
- `ui.csv` — UI 文字
- `tutorials.csv` — 教學與引導
- `story.csv` — 劇情文字
- `other.csv` — 其他

每個檔案都是 `source,target,tgt_lng` 三欄（首列為表頭）：對 `tgt_lng` 指定的目標語言，`target` 是譯文，`source` 是**其它某一語言**的原文。因此同一條目會以其餘 9 種語言分別作為 `source` 各出現一列（重複列與同形列已合併，故實際列數並非詞條數的 9 倍）。檔案可直接匯入 CAT 工具或沉浸式翻譯等術語比對軟體。

## 分類與條數

| 分類 | 主題 | 條數 | 對照行 |
| --- | --- | --- | --- |
| `characters.csv` | 角色名稱 | 1,230 | 5,158 |
| `weapons.csv` | 武器名稱 | 820 | 3,080 |
| `echoes.csv` | 聲骸 | 1,000 | 6,058 |
| `skills.csv` | 技能 | 5,344 | 30,367 |
| `resonant-chains.csv` | 共鳴鏈 | 784 | 6,121 |
| `quests.csv` | 任務 | 2,807 | 14,421 |
| `dungeons.csv` | 關卡與挑戰 | 1,910 | 12,130 |
| `regions.csv` | 地區與地圖 | 2,229 | 16,147 |
| `factions.csv` | 陣營與勢力 | 8 | 44 |
| `items.csv` | 道具與材料 | 8,384 | 54,602 |
| `monsters.csv` | 怪物與生物 | 685 | 4,532 |
| `npcs.csv` | NPC 與說話人 | 14,172 | 63,586 |
| `achievements.csv` | 成就 | 2,563 | 22,173 |
| `activities.csv` | 活動與玩法 | 9,531 | 63,531 |
| `buffs.csv` | 增益與效果 | 270 | 2,040 |
| `voice-lines.csv` | 角色語音 | 7,374 | 31,724 |
| `archives.csv` | 檔案與讀物 | 839 | 6,627 |
| `terms.csv` | 術語與百科 | 1,672 | 12,396 |
| `system.csv` | 系統文字 | 9,756 | 65,636 |
| `ui.csv` | UI 文字 | 13,866 | 77,979 |
| `tutorials.csv` | 教學與引導 | 6,253 | 31,806 |
| `story.csv` | 劇情文字 | 29,841 | 102,076 |
| `other.csv` | 其他 | 1,892 | 13,295 |
| **合計** | **23 個類目** | **123,230** | **645,529** |

「條數」為去重後的詞條數（一個詞條 = 遊戲中的一條文字鍵），取自 `tools/_counts.json` 的 `concepts` 欄位，**全庫共用同一套、與目標語言無關**；「對照行」為本目錄該類目 CSV 的實際資料列數。同一段文字可能同時屬於多個類目，各類目列數相加會大於去重詞條數，屬正常現象。

## 說明

- **譯文來源**：`target` 欄直接取自遊戲本身的在地化文字（[Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) 的 `Textmaps/<lang>/multi_text/MultiText.json`，遊戲 3.6.0；少量鍵由 [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) 的 `TextMap/<lang>/MultiText.json`，遊戲 3.1.0 補齊），是遊戲內官方譯名，不是二次翻譯。
- **對齊方式**：以遊戲文字鍵（如 `RoleInfo_1402_Name`）對齊——同一文字鍵在其它語言的寫法，即成為本目錄該 `target` 的 `source` 列。
- **語言標籤**：`tgt_lng` 固定為本目錄的語言代碼，與目錄名一致。
- **編碼**：全部 CSV 為 **UTF-8（含 BOM）**、**CRLF** 換行、首列為表頭；欄位含逗號或引號時依 RFC 4180 轉義，Excel 可直接開啟。
- **已知限制**：預設不收錄逐句劇情對白（約 17 萬條/語言），需要時可用 `--with-dialogue` 選項另外產生，方法見 `../README.md`；過長文字依 `tools/wuwa_config.py` 的 `MAX_LEN` 按類目截斷；上游資料倉庫中 `ru-RU`、`id-ID`、`vi-VN` 為空佔位檔案故未收錄，`it-IT`、`tr-TR` 並非遊戲支援的文字語言。

## 免責聲明

本目錄為個人整理與維護的**非官方**翻譯術語資料庫，僅用於個人學習、研究及輔助 AI 翻譯軟體（包括但不限於沉浸式翻譯）的術語比對。本庫與相關遊戲的開發商、發行商、代理商、營運商、版權方不存在任何從屬、授權、合作、代理或官方代表關係；庫中譯名不代表官方立場，不保證始終準確、完整或與遊戲當前版本一致，**不應被視為任何遊戲的官方術語表或官方在地化檔案**。遊戲名稱、角色名稱、專有名詞、商標等智慧財產權均歸各自權利人所有，本庫不主張對上述第三方智慧財產權的任何權利；如權利人認為內容不當，歡迎透過 GitHub Issues / Pull Request 聯繫，維護者將核實後修改或刪除。完整條款見倉庫根目錄 `README.md` / `README_EN.md` / `README_JP.md`。
