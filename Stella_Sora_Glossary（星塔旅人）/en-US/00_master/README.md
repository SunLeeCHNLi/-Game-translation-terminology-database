# 《星塔旅人》Stella Sora 术语库 — English（`en-US`）

> 本文件位于 `en-US/00_master/`，描述的是**上级语言目录 `en-US/`**（以 English 为目标语言的整套术语库）。
> 语言级说明见 `../README.md`（English）与 `../README_zh-CN.md`（简体中文），游戏级总说明见 `../../README.md`。

本语言目录是**以 `en-US` 为目标语言**的术语库：每一条都是「其他语言词条 → English」的对照，
共 **12288** 条词条、**46032** 行对照（`tgt_lng` 列固定为 `en-US`）。

## 文件

- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 格式，可直接导入 CAT / 术语管理工具
- `NN_xxx/NN_xxx_terms.csv` — 本语言词条清单（`id, term, src_table`），适合校对与回查
- `00_master/all_glossary.csv` — 全部 15 个分类的合并术语表（`category,source,target,tgt_lng`）
- `00_master/all_terms.csv` — 本语言全部词条清单（`category,category_label,id,term,src_table`）
- `00_master/index.csv` — 分类索引与条数（`category,label,term_count,glossary_file,terms_file,target_language`）

## 分类与条数

数字取自 `00_master/index.csv`，并与 15 个分类 CSV、`all_terms.csv`、`all_glossary.csv` 的实际数据行数核对一致。
「条数」是词条数（`terms.csv` 的数据行），「对照行」是 `glossary.csv` 的 `source → target` 对照行数，两者不是同一个数字。

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `01_character` | 角色名称 | 287 | 973 |
| `02_skill` | 技能名称 | 628 | 2279 |
| `03_potential` | 潜能名称 | 1457 | 5553 |
| `04_disc` | 唱片 / Disc | 234 | 896 |
| `05_item` | 道具 | 558 | 2172 |
| `06_equipment` | 装备 | 15 | 58 |
| `07_enemy` | 敌人 | 399 | 1547 |
| `08_stage` | 关卡 | 1019 | 3856 |
| `09_event` | 活动 | 581 | 2231 |
| `10_system` | 系统术语 | 1055 | 4108 |
| `11_ui` | UI术语 | 4244 | 15529 |
| `12_story` | 剧情专有名词 | 527 | 2024 |
| `13_faction` | 阵营 | 21 | 78 |
| `14_location` | 地点 | 27 | 98 |
| `15_terminology` | 游戏机制术语 | 1236 | 4630 |
| **合计** | | **12288** | **46032** |

本语言目录共 12288 条词条，比 `zh-CN` 少 4 条，差异全部落在 `11_ui`（4244 对 4248）：
官方 UI 文本里有个别条目在英文语区没有独立译文。

## 说明

- 译文来自游戏官方多语言文本库 `StellaSoraData-main`，各语言按同一文本键对齐，非二次翻译；
- 每条词条会把其他四种语言（`zh-CN` / `zh-TW` / `ja-JP` / `ko-KR`）的写法展开为对照行，
  **最多 4 行**：与目标语言写法完全相同的 `source`、以及同一分类内已经出现过的 `source → target` 对照行会被去掉，
  因此对照行总数少于「条数 × 4」（例如 `06_equipment` 15 条词条只有 58 行对照）；
  也可反向当作「en-US → 其他语言」查询；
- 文件编码为 UTF-8 with BOM、CRLF 换行，Excel 双击即可正确显示中日韩文字。
