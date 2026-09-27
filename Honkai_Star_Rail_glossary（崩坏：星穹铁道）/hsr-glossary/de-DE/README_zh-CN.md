# 崩坏：星穹铁道（Honkai: Star Rail）术语库 — Deutsch（`de-DE`）

[← 返回游戏总说明](../../README.md) ｜ [← hsr-glossary 子库说明](../README.md)

本目录是**以 `de-DE`（Deutsch）为目标语言**的星穹铁道术语库，共 **26** 个分类 CSV、**307,905** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `de-DE`；`source` 列收录其余语言的官方本地化写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，26 个分类 CSV 直接放在本目录下：

| 文件 | 分类 | 本语言记录数 |
| --- | --- | ---: |
| `01_character（Charaktere & NPCs）.csv` | 角色与 NPC | 2,910 |
| `02_path（Pfade）.csv` | 命途 | 206 |
| `03_element（Elemente）.csv` | 属性 | 149 |
| `04_skill（Fähigkeiten）.csv` | 技能 | 5,136 |
| `05_trace（Spuren）.csv` | 行迹 | 3,073 |
| `06_eidolon（Eidolons）.csv` | 星魂 | 5,463 |
| `07_light_cone（Lichtkegel）.csv` | 光锥 | 3,217 |
| `08_relic（Relikte）.csv` | 遗器 | 2,712 |
| `09_item（Gegenstände）.csv` | 道具 | 19,739 |
| `10_material（Materialien）.csv` | 材料 | 6,071 |
| `11_enemy（Gegner）.csv` | 敌人 | 9,100 |
| `12_location（Orte）.csv` | 地点 | 11,728 |
| `13_faction（Fraktionen & Organisationen）.csv` | 阵营与组织 | 361 |
| `14_quest（Aufträge）.csv` | 任务 | 61,758 |
| `15_stage（Ebenen & Domänen）.csv` | 关卡与副本 | 1,987 |
| `16_event（Events）.csv` | 活动 | 14,772 |
| `17_achievement（Erfolge）.csv` | 成就 | 21,785 |
| `18_simulated_universe（Simulierte Universum）.csv` | 模拟宇宙 | 20,307 |
| `19_forgotten_hall（Vergessene Halle）.csv` | 忘却之庭 | 9,738 |
| `20_story（Handlung）.csv` | 剧情 | 214 |
| `21_world_lore（Weltwissen）.csv` | 世界观 | 1,196 |
| `22_book（Bücher）.csv` | 书籍 | 11,305 |
| `23_dialogue（Dialoge）.csv` | 对话 | 60,353 |
| `24_system（System）.csv` | 系统 | 20,847 |
| `25_ui（Oberfläche）.csv` | 界面 | 11,567 |
| `26_other（Sonstiges）.csv` | 其他 | 2,211 |

## 说明

- 译文来源：游戏客户端本地化文本（TextMap / ExcelOutput），按同一文本键对齐，不是二次翻译。
- 目标语言缺少该文本键时不会生成记录，也不会用机器翻译补全。
- 同一文本键在不同语境下可能出现多种译法，全部保留，不做人工取舍。
- 数据由 `../../tools/build_hsr_glossary.py` 生成，可重新运行复现。
