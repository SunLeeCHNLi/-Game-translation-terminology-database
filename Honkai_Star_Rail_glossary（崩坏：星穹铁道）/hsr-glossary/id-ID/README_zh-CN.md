# 崩坏：星穹铁道（Honkai: Star Rail）术语库 — Bahasa Indonesia（`id-ID`）

[← 返回游戏总说明](../../README.md) ｜ [← hsr-glossary 子库说明](../README.md)

本目录是**以 `id-ID`（Bahasa Indonesia）为目标语言**的星穹铁道术语库，共 **26** 个分类 CSV、**313,603** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `id-ID`；`source` 列收录其余语言的官方本地化写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，26 个分类 CSV 直接放在本目录下：

| 文件 | 分类 | 本语言记录数 |
| --- | --- | ---: |
| `01_character.csv` | 角色与 NPC | 2,910 |
| `02_path.csv` | 命途 | 206 |
| `03_element.csv` | 属性 | 149 |
| `04_skill.csv` | 技能 | 5,208 |
| `05_trace.csv` | 行迹 | 3,051 |
| `06_eidolon.csv` | 星魂 | 5,515 |
| `07_light_cone.csv` | 光锥 | 3,219 |
| `08_relic.csv` | 遗器 | 2,734 |
| `09_item.csv` | 道具 | 19,858 |
| `10_material.csv` | 材料 | 6,082 |
| `11_enemy.csv` | 敌人 | 9,244 |
| `12_location.csv` | 地点 | 11,728 |
| `13_faction.csv` | 阵营与组织 | 352 |
| `14_quest.csv` | 任务 | 66,247 |
| `15_stage.csv` | 关卡与副本 | 1,987 |
| `16_event.csv` | 活动 | 14,803 |
| `17_achievement.csv` | 成就 | 21,896 |
| `18_simulated_universe.csv` | 模拟宇宙 | 20,414 |
| `19_forgotten_hall.csv` | 忘却之庭 | 9,772 |
| `20_story.csv` | 剧情 | 214 |
| `21_world_lore.csv` | 世界观 | 1,196 |
| `22_book.csv` | 书籍 | 11,394 |
| `23_dialogue.csv` | 对话 | 60,182 |
| `24_system.csv` | 系统 | 21,247 |
| `25_ui.csv` | 界面 | 11,777 |
| `26_other.csv` | 其他 | 2,218 |

## 说明

- 译文来源：游戏客户端本地化文本（TextMap / ExcelOutput），按同一文本键对齐，不是二次翻译。
- 目标语言缺少该文本键时不会生成记录，也不会用机器翻译补全。
- 同一文本键在不同语境下可能出现多种译法，全部保留，不做人工取舍。
- 数据由 `../../tools/build_hsr_glossary.py` 生成，可重新运行复现。
