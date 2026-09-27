# 崩坏：星穹铁道（Honkai: Star Rail）术语库 — Français（`fr-FR`）

[← 返回游戏总说明](../../README.md) ｜ [← hsr-glossary 子库说明](../README.md)

本目录是**以 `fr-FR`（Français）为目标语言**的星穹铁道术语库，共 **26** 个分类 CSV、**306,045** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `fr-FR`；`source` 列收录其余语言的官方本地化写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，26 个分类 CSV 直接放在本目录下：

| 文件 | 分类 | 本语言记录数 |
| --- | --- | ---: |
| `01_character（Personnages et PNJ）.csv` | 角色与 NPC | 2,894 |
| `02_path（Voies）.csv` | 命途 | 206 |
| `03_element（Éléments）.csv` | 属性 | 149 |
| `04_skill（Compétences）.csv` | 技能 | 5,139 |
| `05_trace（Traces）.csv` | 行迹 | 3,126 |
| `06_eidolon（Eidolons）.csv` | 星魂 | 5,517 |
| `07_light_cone（Cônes de lumière）.csv` | 光锥 | 3,219 |
| `08_relic（Reliques）.csv` | 遗器 | 2,712 |
| `09_item（Objets）.csv` | 道具 | 19,645 |
| `10_material（Matériaux）.csv` | 材料 | 6,036 |
| `11_enemy（Ennemis）.csv` | 敌人 | 9,157 |
| `12_location（Lieux）.csv` | 地点 | 11,713 |
| `13_faction（Factions et organisations）.csv` | 阵营与组织 | 361 |
| `14_quest（Quêtes）.csv` | 任务 | 61,136 |
| `15_stage（Niveaux et domaines）.csv` | 关卡与副本 | 1,987 |
| `16_event（Événements）.csv` | 活动 | 14,624 |
| `17_achievement（Succès）.csv` | 成就 | 21,176 |
| `18_simulated_universe（Univers simulé）.csv` | 模拟宇宙 | 20,352 |
| `19_forgotten_hall（Salle de l’oubli）.csv` | 忘却之庭 | 9,838 |
| `20_story（Histoire）.csv` | 剧情 | 214 |
| `21_world_lore（Univers）.csv` | 世界观 | 1,206 |
| `22_book（Livres）.csv` | 书籍 | 11,223 |
| `23_dialogue（Dialogues）.csv` | 对话 | 60,349 |
| `24_system（Système）.csv` | 系统 | 20,371 |
| `25_ui（Interface）.csv` | 界面 | 11,491 |
| `26_other（Autres）.csv` | 其他 | 2,204 |

## 说明

- 译文来源：游戏客户端本地化文本（TextMap / ExcelOutput），按同一文本键对齐，不是二次翻译。
- 目标语言缺少该文本键时不会生成记录，也不会用机器翻译补全。
- 同一文本键在不同语境下可能出现多种译法，全部保留，不做人工取舍。
- 数据由 `../../tools/build_hsr_glossary.py` 生成，可重新运行复现。
