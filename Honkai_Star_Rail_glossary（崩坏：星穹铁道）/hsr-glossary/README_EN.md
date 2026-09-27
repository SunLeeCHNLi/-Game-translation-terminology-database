# Honkai: Star Rail Multilingual Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds the glossary for *Honkai: Star Rail* (HSR), organized by target language.
Every CSV file has exactly three columns: `source`, `target`, `tgt_lng`.

- Total records: **4,085,059**
- Deduplicated term keys (concept): **42,126**
- Target languages: **13**
- Categories: **26**
- Client data version: `4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`

`source` is the official localization of the same game text key in another language, while `target` is the official localization in this directory's language.
The two are aligned through the TextMap Hash / entity ID; machine translation is not used.

Files use the repository's unified CSV form (`source,target,tgt_lng` three columns, UTF-8 with BOM, CRLF).
If you need tab-separated files with the same content, run `python ../tools/build_hsr_glossary.py --format tsv` to generate
identically named `.tsv` files (the column structure is exactly the same, only the separator differs).

Regeneration and validation:

```bash
python ../tools/build_hsr_glossary.py
python ../tools/build_hsr_history.py
python ../tools/build_hsr_curated.py
python ../tools/validate_hsr_glossary.py
python ../tools/make_hsr_docs.py
```

## Scale by Language

| Target language | Language | Records |
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

## Scale by Category

| Category | Chinese name | English | Unique term keys | Records across all languages |
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

## Other Directories

- `historical/` — historical translation changes obtained by comparing against older client versions (2.3.0 / 4.0).
- `curated/` — a small number of manually reviewed entries (such as the Trailblazer/protagonist); all of them have been verified to exist in the client text.

## Quality Validation

Most recent validation results (`../tools/_validation.json`):

| Check | Result |
| --- | ---: |
| Empty source / empty target | 0 / 0 |
| Invalid language codes | 0 |
| Duplicate records | 0 |
| HTML tags | 0 |
| Development variables | 0 |
| Hash / internal ID | 0 / 0 |
| Placeholders such as N/A | 0 |
| Target text not present in the client text | 0 |
| Machine-translated records | 0 |