# 《蔚蓝档案》Blue Archive 术语库 — English（`en-US`）

本文件夹是**以 `en-US` 为目标语言**的术语库：每一条都是「其他语言词条 → English」的对照，
共 **5909** 条词条、26623 行对照（`tgt_lng` 列固定为 `en-US`）。

## 文件

- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 格式，可直接导入 CAT / 术语管理工具
- `NN_xxx/NN_xxx_terms.csv` — 本语言词条清单（`id, term, src_table`），适合校对与回查
- `00_master/all_glossary.csv` — 全部 15 个分类的合并术语表
- `00_master/all_terms.csv` — 本语言全部词条清单
- `00_master/index.csv` — 分类索引与条数

## 分类与条数

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `01_character` | 角色名称 | 204 | 979 |
| `02_school` | 学校 | 26 | 116 |
| `03_club` | 社团 | 43 | 193 |
| `04_story_title` | 剧情标题 | 665 | 3237 |
| `05_favor_item` | 爱用品 | 51 | 248 |
| `06_location` | 地名 | 8 | 38 |
| `07_terminology` | 术语 | 1379 | 5817 |
| `08_event` | 活动 | 45 | 184 |
| `09_scenario_character` | 剧情角色 | 134 | 618 |
| `10_enemy` | 敌人 | 351 | 1631 |
| `11_skill` | 技能 | 1069 | 5086 |
| `12_item` | 道具 | 649 | 2999 |
| `13_equipment` | 装备 | 155 | 722 |
| `14_furniture` | 家具 | 472 | 1825 |
| `15_stage` | 关卡 | 658 | 2930 |
| **合计** | | **5909** | **26623** |

## 说明

- 译文全部取自官方客户端多语言文本（国服 / 国际服 / 日服 / 韩服 / 泰服）与社区剧情对照表，按同一文本键对齐，非二次翻译；
- 每条词条会把其他语言的写法全部展开为对照行，因此也可反向当作「en-US → 其他语言」查询；
- 六种语言的标签：`zh-CN` 简体中文、`zh-TW` 繁体中文、`en-US` 英文、`ja-JP` 日文、`ko-KR` 韩文、`th-TH` 泰文；
- 极少数词条会出现一条 `source` 对应多个 `target` 的情况（多为同名不同物的短词，或简繁两套客户端写法并存）；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `_terms.csv` 里的 `id` 与 `src_table` 回查上下文；
- 文件编码为 UTF-8 with BOM，Excel 双击即可正确显示中日韩泰文字。
