# 《崩坏：星穹铁道》术语库统计

生成日期：2026-09-27
客户端数据版本：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`

## 总量

| 指标 | 数值 |
| --- | ---: |
| 总记录数（所有语言 `source,target,tgt_lng` 行） | 4,085,059 |
| 去重术语键（concept）总数 | 42,126 |
| 目标语言数 | 13 |
| 分类数 | 26 |
| 已确认条目（目标文本可在客户端 TextMap 中逐字验证） | 4,085,059 |
| 未确认条目（未生成 / 未猜测） | 0 |
| 机器翻译条目 | 0 |
| 历史词条（旧版本译名变化） | 166 |
| 人工核对条目（curated） | 117 |
| 多译名冲突组（同一 source 在同一语言同一分类下对应多个 target） | 41,475 |

## 各语言数量

| 目标语言 | 语言 | 记录数 |
| --- | --- | ---: |
| `zh-CN` | 简体中文 | 319,693 |
| `zh-TW` | 繁體中文 | 320,157 |
| `en-US` | English | 313,831 |
| `ja-JP` | 日本語 | 317,716 |
| `ko-KR` | 한국어 | 319,228 |
| `fr-FR` | Français | 306,045 |
| `de-DE` | Deutsch | 307,905 |
| `es-ES` | Español | 307,652 |
| `ru-RU` | Русский | 313,470 |
| `pt-PT` | Português | 311,326 |
| `id-ID` | Bahasa Indonesia | 313,603 |
| `th-TH` | ไทย | 317,329 |
| `vi-VN` | Tiếng Việt | 317,104 |

## 各分类数量

| 分类 | 中文名 | English | 独立术语键 | 全语言记录数 |
| --- | --- | --- | ---: | ---: |
| `01_character` | 角色与 NPC | Characters & NPCs | 513 | 37,756 |
| `02_path` | 命途 | Paths | 18 | 2,678 |
| `03_element` | 属性 | Elements | 14 | 1,937 |
| `04_skill` | 技能 | Skills | 825 | 67,089 |
| `05_trace` | 行迹 | Traces | 1,380 | 39,786 |
| `06_eidolon` | 星魂 | Eidolons | 840 | 71,475 |
| `07_light_cone` | 光锥 | Light Cones | 338 | 41,840 |
| `08_relic` | 遗器 | Relics | 918 | 35,527 |
| `09_item` | 道具 | Items | 2,101 | 258,055 |
| `10_material` | 材料 | Materials | 604 | 79,033 |
| `11_enemy` | 敌人 | Enemies | 1,899 | 123,140 |
| `12_location` | 地点 | Locations | 2,315 | 152,554 |
| `13_faction` | 阵营与组织 | Factions | 61 | 4,618 |
| `14_quest` | 任务 | Quests | 10,378 | 866,645 |
| `15_stage` | 关卡与副本 | Stages | 211 | 25,915 |
| `16_event` | 活动 | Events | 2,145 | 192,044 |
| `17_achievement` | 成就 | Achievements | 1,928 | 281,679 |
| `18_simulated_universe` | 模拟宇宙 | Simulated Universe | 3,010 | 264,638 |
| `19_forgotten_hall` | 忘却之庭 | Forgotten Hall | 962 | 126,858 |
| `20_story` | 剧情 | Story | 24 | 2,826 |
| `21_world_lore` | 世界观 | World Lore | 175 | 15,998 |
| `22_book` | 书籍 | Books | 1,100 | 147,763 |
| `23_dialogue` | 对话 | Dialogue | 6,258 | 784,728 |
| `24_system` | 系统 | System | 2,373 | 281,948 |
| `25_ui` | 界面 | UI | 1,315 | 149,681 |
| `26_other` | 其他 | Other | 421 | 28,848 |

## 历史词条来源

| 对比基线 | 版本 | 检出差异记录数 |
| --- | --- | ---: |
| StarRailStaticAPI | 2.3.0 | 189 |
| HSR-Mapping-DATA | 4.0 | 42 |
| 去重后 | — | 166 |

## 第二轮抽样核对

| 分类 | 抽样条数 | 在 StarRailRes 独立索引中命中 |
| --- | ---: | ---: |
| `01_character` | 104 | 81 |
| `02_path` | 104 | 0 |
| `03_element` | 104 | 0 |
| `04_skill` | 104 | 0 |
| `05_trace` | 104 | 0 |
| `06_eidolon` | 104 | 0 |
| `07_light_cone` | 104 | 66 |
| `08_relic` | 104 | 93 |
| `09_item` | 104 | 0 |
| `10_material` | 104 | 0 |
| `11_enemy` | 104 | 0 |
| `12_location` | 104 | 0 |
| `13_faction` | 104 | 0 |
| `14_quest` | 104 | 0 |
| `15_stage` | 104 | 0 |
| `16_event` | 104 | 0 |
| `17_achievement` | 104 | 104 |
| `18_simulated_universe` | 104 | 82 |
| `19_forgotten_hall` | 104 | 0 |
| `20_story` | 104 | 0 |
| `21_world_lore` | 104 | 0 |
| `22_book` | 104 | 0 |
| `23_dialogue` | 104 | 0 |
| `24_system` | 104 | 0 |
| `25_ui` | 104 | 0 |
| `26_other` | 104 | 0 |

> StarRailRes 与客户端 TextMap 属于同一份数据的两种整理方式，用于交叉验证名称与 ID 的对应关系；
> 没有 StarRailRes 对应文件的门类（任务、活动、剧情、系统、UI、书籍等）以客户端 TextMap 逐字验证为准。
