# 崩坏：星穹铁道（Honkai: Star Rail）术语库 — Español（`es-ES`）

[← 返回游戏总说明](../../README.md) ｜ [← hsr-glossary 子库说明](../README.md)

本目录是**以 `es-ES`（Español）为目标语言**的星穹铁道术语库，共 **26** 个分类 CSV、**307,652** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `es-ES`；`source` 列收录其余语言的官方本地化写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，26 个分类 CSV 直接放在本目录下：

| 文件 | 分类 | 本语言记录数 |
| --- | --- | ---: |
| `01_character（Personajes y PNJ）.csv` | 角色与 NPC | 2,883 |
| `02_path（Caminos）.csv` | 命途 | 206 |
| `03_element（Elementos）.csv` | 属性 | 149 |
| `04_skill（Habilidades）.csv` | 技能 | 5,147 |
| `05_trace（Rastros）.csv` | 行迹 | 3,073 |
| `06_eidolon（Eidolones）.csv` | 星魂 | 5,442 |
| `07_light_cone（Conos de luz）.csv` | 光锥 | 3,217 |
| `08_relic（Reliquias）.csv` | 遗器 | 2,712 |
| `09_item（Objetos）.csv` | 道具 | 19,704 |
| `10_material（Materiales）.csv` | 材料 | 6,090 |
| `11_enemy（Enemigos）.csv` | 敌人 | 9,118 |
| `12_location（Lugares）.csv` | 地点 | 11,729 |
| `13_faction（Facciones y organizaciones）.csv` | 阵营与组织 | 365 |
| `14_quest（Misiones）.csv` | 任务 | 62,709 |
| `15_stage（Etapas y dominios）.csv` | 关卡与副本 | 1,991 |
| `16_event（Eventos）.csv` | 活动 | 14,651 |
| `17_achievement（Logros）.csv` | 成就 | 21,011 |
| `18_simulated_universe（Universo simulado）.csv` | 模拟宇宙 | 20,076 |
| `19_forgotten_hall（Salón del olvido）.csv` | 忘却之庭 | 9,748 |
| `20_story（Historia）.csv` | 剧情 | 214 |
| `21_world_lore（Trasfondo）.csv` | 世界观 | 1,196 |
| `22_book（Libros）.csv` | 书籍 | 11,239 |
| `23_dialogue（Diálogos）.csv` | 对话 | 60,320 |
| `24_system（Sistema）.csv` | 系统 | 20,801 |
| `25_ui（Interfaz）.csv` | 界面 | 11,646 |
| `26_other（Otros）.csv` | 其他 | 2,215 |

## 说明

- 译文来源：游戏客户端本地化文本（TextMap / ExcelOutput），按同一文本键对齐，不是二次翻译。
- 目标语言缺少该文本键时不会生成记录，也不会用机器翻译补全。
- 同一文本键在不同语境下可能出现多种译法，全部保留，不做人工取舍。
- 数据由 `../../tools/build_hsr_glossary.py` 生成，可重新运行复现。
