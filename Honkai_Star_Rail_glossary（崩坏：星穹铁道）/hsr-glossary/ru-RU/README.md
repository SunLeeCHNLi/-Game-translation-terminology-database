# Глоссарий Honkai: Star Rail — Русский (`ru-RU`)

[← Вернуться к общему описанию](../../README.md) ｜ [← подбиблиотека hsr-glossary](../README.md)

В этом каталоге находится глоссарий Honkai: Star Rail с **целевым языком `ru-RU` (Русский)**: **26** CSV по категориям и **313,470** строк сопоставления. Столбец `tgt_lng` всегда равен `ru-RU`, а `source` содержит официальную локализацию остальных языков.

## Файлы

Каталог **плоский**: все 26 CSV по категориям лежат здесь.

| Файл | Категория | Строк на этом языке |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,905 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,136 |
| `05_trace.csv` | Traces | 3,051 |
| `06_eidolon.csv` | Eidolons | 5,484 |
| `07_light_cone.csv` | Light Cones | 3,217 |
| `08_relic.csv` | Relics | 2,743 |
| `09_item.csv` | Items | 19,870 |
| `10_material.csv` | Materials | 6,090 |
| `11_enemy.csv` | Enemies | 9,445 |
| `12_location.csv` | Locations | 11,741 |
| `13_faction.csv` | Factions | 358 |
| `14_quest.csv` | Quests | 65,981 |
| `15_stage.csv` | Stages | 1,987 |
| `16_event.csv` | Events | 14,775 |
| `17_achievement.csv` | Achievements | 21,564 |
| `18_simulated_universe.csv` | Simulated Universe | 20,302 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,739 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,210 |
| `22_book.csv` | Books | 11,524 |
| `23_dialogue.csv` | Dialogue | 60,416 |
| `24_system.csv` | System | 21,987 |
| `25_ui.csv` | UI | 11,146 |
| `26_other.csv` | Other | 2,230 |

## Примечания

- Тексты взяты из клиентской локализации (TextMap / ExcelOutput) и сопоставлены по одному и тому же текстовому ключу — это не вторичный перевод.
- Если в целевом языке текст отсутствует, строка не создаётся и машинный перевод не подставляется.
- Один и тот же ключ может иметь несколько официальных формулировок; сохраняются все.
- Сгенерировано с помощью `../../tools/build_hsr_glossary.py`, воспроизводимо.
