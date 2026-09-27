# 崩坏：星穹铁道（Honkai: Star Rail）多语言术语库

本目录按目标语言存放《崩坏：星穹铁道》（Honkai: Star Rail / HSR）术语表。
每个 CSV 文件严格只有三列：`source`、`target`、`tgt_lng`。

- 记录总数：**4,085,059**
- 去重术语键（concept）：**42,126**
- 目标语言：**13**
- 分类：**26**
- 客户端数据版本：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`

`source` 是同一个游戏文本键在其它语言的官方本地化文本，`target` 是本目录语言的官方本地化文本，
两者通过 TextMap Hash / 实体 ID 对齐，不使用机器翻译。

文件使用仓库统一的 CSV 形式（`source,target,tgt_lng` 三列，UTF-8 含 BOM、CRLF）。
如需制表符分隔的同内容文件，可用 `python ../tools/build_hsr_glossary.py --format tsv` 生成
同名 `.tsv` 文件（列结构完全一致，仅分隔符不同）。

重新生成与校验：

```bash
python ../tools/build_hsr_glossary.py
python ../tools/build_hsr_history.py
python ../tools/build_hsr_curated.py
python ../tools/validate_hsr_glossary.py
python ../tools/make_hsr_docs.py
```

## 各语言规模

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

## 分类规模

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

## 其它目录

- `historical/` — 与旧版本客户端（2.3.0 / 4.0）比对得到的历史译名变化。
- `curated/` — 少量人工核对条目（如开拓者/主角），全部在客户端文本中验证存在。

## 质量校验

最近一次校验结果（`../tools/_validation.json`）：

| 检查项 | 结果 |
| --- | ---: |
| 空 source / 空 target | 0 / 0 |
| 语言代码错误 | 0 |
| 重复记录 | 0 |
| HTML 标签 | 0 |
| 开发变量 | 0 |
| Hash / 内部 ID | 0 / 0 |
| N/A 等占位符 | 0 |
| 目标文本未出现在客户端文本中 | 0 |
| 机器翻译记录 | 0 |
