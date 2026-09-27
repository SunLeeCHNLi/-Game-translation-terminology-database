# 崩坏：星穹铁道（Honkai: Star Rail）术语库 — Tiếng Việt（`vi-VN`）

[← 返回游戏总说明](../../README.md) ｜ [← hsr-glossary 子库说明](../README.md)

本目录是**以 `vi-VN`（Tiếng Việt）为目标语言**的星穹铁道术语库，共 **26** 个分类 CSV、**317,104** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `vi-VN`；`source` 列收录其余语言的官方本地化写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，26 个分类 CSV 直接放在本目录下：

| 文件 | 分类 | 本语言记录数 |
| --- | --- | ---: |
| `01_character（Nhân vật & NPC）.csv` | 角色与 NPC | 2,905 |
| `02_path（Vận mệnh）.csv` | 命途 | 206 |
| `03_element（Nguyên tố）.csv` | 属性 | 149 |
| `04_skill（Kỹ năng）.csv` | 技能 | 5,239 |
| `05_trace（Dấu vết）.csv` | 行迹 | 3,065 |
| `06_eidolon（Tinh hồn）.csv` | 星魂 | 5,563 |
| `07_light_cone（Nón ánh sáng）.csv` | 光锥 | 3,219 |
| `08_relic（Di vật）.csv` | 遗器 | 2,743 |
| `09_item（Vật phẩm）.csv` | 道具 | 19,918 |
| `10_material（Nguyên liệu）.csv` | 材料 | 6,090 |
| `11_enemy（Kẻ địch）.csv` | 敌人 | 9,701 |
| `12_location（Địa điểm）.csv` | 地点 | 11,786 |
| `13_faction（Phe phái & tổ chức）.csv` | 阵营与组织 | 361 |
| `14_quest（Nhiệm vụ）.csv` | 任务 | 67,938 |
| `15_stage（Ải & bí cảnh）.csv` | 关卡与副本 | 2,021 |
| `16_event（Sự kiện）.csv` | 活动 | 14,762 |
| `17_achievement（Thành tựu）.csv` | 成就 | 21,842 |
| `18_simulated_universe（Vũ trụ mô phỏng）.csv` | 模拟宇宙 | 20,586 |
| `19_forgotten_hall（Sảnh bị lãng quên）.csv` | 忘却之庭 | 9,772 |
| `20_story（Cốt truyện）.csv` | 剧情 | 214 |
| `21_world_lore（Thế giới quan）.csv` | 世界观 | 1,206 |
| `22_book（Sách）.csv` | 书籍 | 11,337 |
| `23_dialogue（Hội thoại）.csv` | 对话 | 60,386 |
| `24_system（Hệ thống）.csv` | 系统 | 22,148 |
| `25_ui（Giao diện）.csv` | 界面 | 11,731 |
| `26_other（Khác）.csv` | 其他 | 2,216 |

## 说明

- 译文来源：游戏客户端本地化文本（TextMap / ExcelOutput），按同一文本键对齐，不是二次翻译。
- 目标语言缺少该文本键时不会生成记录，也不会用机器翻译补全。
- 同一文本键在不同语境下可能出现多种译法，全部保留，不做人工取舍。
- 数据由 `../../tools/build_hsr_glossary.py` 生成，可重新运行复现。
