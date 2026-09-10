# 《星塔旅人》Stella Sora 术语库 — 한국어（韩文）（`ko-KR`）

本文件夹是**以 `ko-KR` 为目标语言**的术语库：每一条都是「其他语言词条 → 한국어（韩文）」的对照，
共 **12292** 条词条、45950 行对照（`tgt_lng` 列固定为 `ko-KR`）。

## 文件

- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 格式，可直接导入 CAT / 术语管理工具
- `NN_xxx/NN_xxx_terms.csv` — 本语言词条清单（`id, term, src_table`），适合校对与回查
- `00_master/all_glossary.csv` — 全部 15 个分类的合并术语表
- `00_master/all_terms.csv` — 本语言全部词条清单
- `00_master/index.csv` — 分类索引与条数

## 分类与条数

| 分类 | 主题 | 条数 |
| --- | --- | --- |
| `01_character` | 角色名称 | 287 |
| `02_skill` | 技能名称 | 628 |
| `03_potential` | 潜能名称 | 1457 |
| `04_disc` | 唱片 / Disc | 234 |
| `05_item` | 道具 | 558 |
| `06_equipment` | 装备 | 15 |
| `07_enemy` | 敌人 | 399 |
| `08_stage` | 关卡 | 1019 |
| `09_event` | 活动 | 581 |
| `10_system` | 系统术语 | 1055 |
| `11_ui` | UI术语 | 4248 |
| `12_story` | 剧情专有名词 | 527 |
| `13_faction` | 阵营 | 21 |
| `14_location` | 地点 | 27 |
| `15_terminology` | 游戏机制术语 | 1236 |
| **合计** | | **12292** |

## 说明

- 译文来自游戏官方多语言文本库 `StellaSoraData-main`，各语言按同一文本键对齐，非二次翻译；
- 每条词条会把其他四种语言全部展开为对照行（4 行），因此也可反向当作「ko-KR → 其他语言」查询；
- 文件编码为 UTF-8 with BOM，Excel 双击即可正确显示中日韩文字。
