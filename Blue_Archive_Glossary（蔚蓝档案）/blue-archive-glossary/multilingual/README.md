# 蔚蓝档案（Blue Archive）六语并排总表（`multilingual/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录把《蔚蓝档案》术语库的全部 **7535** 条词条按「一条一行」摊开，六种语言并排展示，便于横向比对与二次加工。以单一语言为目标语言的拆分结果在上一层目录的 `../zh-CN/`、`../en-US/` 等语言文件夹中。

## 目录结构

```text
multilingual/
├── 00_master/
│   ├── all_terms_multilingual.csv   全部 15 个分类的六语并排总表（7535 行）
│   └── README.md                    本说明
├── 01_character/                    01_character_multilingual.csv            408 行
├── 02_school/                       02_school_multilingual.csv                26 行
├── 03_club/                         03_club_multilingual.csv                  43 行
├── 04_story_title/                  04_story_title_multilingual.csv        1144 行
├── 05_favor_item/                   05_favor_item_multilingual.csv            51 行
├── 06_location/                     06_location_multilingual.csv              90 行
├── 07_terminology/                  07_terminology_multilingual.csv         1402 行
├── 08_event/                        08_event_multilingual.csv                 72 行
├── 09_scenario_character/           09_scenario_character_multilingual.csv   945 行
├── 10_enemy/                        10_enemy_multilingual.csv                351 行
├── 11_skill/                        11_skill_multilingual.csv               1069 行
├── 12_item/                         12_item_multilingual.csv                 649 行
├── 13_equipment/                    13_equipment_multilingual.csv            155 行
├── 14_furniture/                    14_furniture_multilingual.csv            472 行
└── 15_stage/                        15_stage_multilingual.csv                658 行
```

## 文件格式

总表与各分类文件的列相同，均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。

| 列 | 说明 |
| --- | --- |
| `category` | 分类编号，例如 `01_character` |
| `category_label` | 分类中文名 |
| `id` | 词条 ID（对应官方数据的 Id / 键名） |
| `zh-CN` | 简体中文 |
| `ja-JP` | 日文 |
| `zh-TW` | 繁体中文 |
| `en-US` | 英文 |
| `ko-KR` | 韩文 |
| `th-TH` | 泰文 |
| `src_table` | 该词条来自哪张表 |

## 各分类条数

| 分类 | 主题 | 条数 |
| --- | --- | ---: |
| `01_character` | 角色名称 | 408 |
| `02_school` | 学校 | 26 |
| `03_club` | 社团 | 43 |
| `04_story_title` | 剧情标题 | 1144 |
| `05_favor_item` | 爱用品 | 51 |
| `06_location` | 地名 | 90 |
| `07_terminology` | 术语 | 1402 |
| `08_event` | 活动 | 72 |
| `09_scenario_character` | 剧情角色 | 945 |
| `10_enemy` | 敌人 | 351 |
| `11_skill` | 技能 | 1069 |
| `12_item` | 道具 | 649 |
| `13_equipment` | 装备 | 155 |
| `14_furniture` | 家具 | 472 |
| `15_stage` | 关卡 | 658 |
| **合计** | | **7535** |

## 说明

- 每条词条一行，六种语言并排；空单元格表示该词条在该语言下没有找到对应写法。
- 若只想取某一目标语言的术语库，请直接使用上一层目录 `../<lang>/` 下的分类 CSV，无需从本目录拆分。
- 三个目录层级的说明：本目录（六语并排总表）、`../<lang>/`（单语言术语库）、`../`（游戏级总说明）。
