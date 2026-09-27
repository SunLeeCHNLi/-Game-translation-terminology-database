# Глоссарий Honkai: Star Rail — Русский (`ru-RU`)

[← Вернуться к общему описанию](../../README.md) ｜ [← подбиблиотека hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

В этом каталоге находится глоссарий Honkai: Star Rail с **целевым языком `ru-RU` (Русский)**: **26** CSV по категориям и **313,470** строк сопоставления. Столбец `tgt_lng` всегда равен `ru-RU`, а `source` содержит официальную локализацию остальных языков.

## Файлы

Каталог **плоский**: все 26 CSV по категориям лежат здесь.

| Файл | Категория | Строк на этом языке |
| --- | --- | ---: |
| `01_character（Персонажи и NPC）.csv` | Characters & NPCs | 2,905 |
| `02_path（Пути）.csv` | Paths | 206 |
| `03_element（Элементы）.csv` | Elements | 149 |
| `04_skill（Навыки）.csv` | Skills | 5,136 |
| `05_trace（Следы）.csv` | Traces | 3,051 |
| `06_eidolon（Эйдолоны）.csv` | Eidolons | 5,484 |
| `07_light_cone（Световые конусы）.csv` | Light Cones | 3,217 |
| `08_relic（Реликвии）.csv` | Relics | 2,743 |
| `09_item（Предметы）.csv` | Items | 19,870 |
| `10_material（Материалы）.csv` | Materials | 6,090 |
| `11_enemy（Противники）.csv` | Enemies | 9,445 |
| `12_location（Локации）.csv` | Locations | 11,741 |
| `13_faction（Фракции и организации）.csv` | Factions | 358 |
| `14_quest（Задания）.csv` | Quests | 65,981 |
| `15_stage（Этапы и подземелья）.csv` | Stages | 1,987 |
| `16_event（События）.csv` | Events | 14,775 |
| `17_achievement（Достижения）.csv` | Achievements | 21,564 |
| `18_simulated_universe（Симулированная вселенная）.csv` | Simulated Universe | 20,302 |
| `19_forgotten_hall（Зал забвения）.csv` | Forgotten Hall | 9,739 |
| `20_story（Сюжет）.csv` | Story | 214 |
| `21_world_lore（Лор мира）.csv` | World Lore | 1,210 |
| `22_book（Книги）.csv` | Books | 11,524 |
| `23_dialogue（Диалоги）.csv` | Dialogue | 60,416 |
| `24_system（Система）.csv` | System | 21,987 |
| `25_ui（Интерфейс）.csv` | UI | 11,146 |
| `26_other（Прочее）.csv` | Other | 2,230 |

## Примечания

- Тексты взяты из клиентской локализации (TextMap / ExcelOutput) и сопоставлены по одному и тому же текстовому ключу — это не вторичный перевод.
- Если в целевом языке текст отсутствует, строка не создаётся и машинный перевод не подставляется.
- Один и тот же ключ может иметь несколько официальных формулировок; сохраняются все.
- Сгенерировано с помощью `../../tools/build_hsr_glossary.py`, воспроизводимо.
