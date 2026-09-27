# Cơ sở thuật ngữ Honkai: Star Rail — Tiếng Việt (`vi-VN`)

[← Quay lại phần giới thiệu game](../../README.md) ｜ [← thư mục con hsr-glossary](../README.md)

Thư mục này chứa cơ sở thuật ngữ Honkai: Star Rail với **`vi-VN` (Tiếng Việt) là ngôn ngữ đích**: **26** tệp CSV theo hạng mục và **317,104** dòng đối chiếu. Cột `tgt_lng` luôn là `vi-VN`, cột `source` chứa bản địa hóa chính thức của các ngôn ngữ khác.

## Tệp

Thư mục có **cấu trúc phẳng**: 26 tệp CSV hạng mục nằm trực tiếp tại đây.

| Tệp | Hạng mục | Số dòng của ngôn ngữ này |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,905 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,239 |
| `05_trace.csv` | Traces | 3,065 |
| `06_eidolon.csv` | Eidolons | 5,563 |
| `07_light_cone.csv` | Light Cones | 3,219 |
| `08_relic.csv` | Relics | 2,743 |
| `09_item.csv` | Items | 19,918 |
| `10_material.csv` | Materials | 6,090 |
| `11_enemy.csv` | Enemies | 9,701 |
| `12_location.csv` | Locations | 11,786 |
| `13_faction.csv` | Factions | 361 |
| `14_quest.csv` | Quests | 67,938 |
| `15_stage.csv` | Stages | 2,021 |
| `16_event.csv` | Events | 14,762 |
| `17_achievement.csv` | Achievements | 21,842 |
| `18_simulated_universe.csv` | Simulated Universe | 20,586 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,772 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,206 |
| `22_book.csv` | Books | 11,337 |
| `23_dialogue.csv` | Dialogue | 60,386 |
| `24_system.csv` | System | 22,148 |
| `25_ui.csv` | UI | 11,731 |
| `26_other.csv` | Other | 2,216 |

## Ghi chú

- Bản dịch lấy từ bản địa hóa của client (TextMap / ExcelOutput), căn theo cùng một khóa văn bản — không phải dịch lại.
- Nếu ngôn ngữ đích thiếu văn bản cho một khóa, sẽ không tạo dòng nào và không dùng dịch máy để bù.
- Một khóa văn bản có thể có nhiều cách diễn đạt chính thức tùy ngữ cảnh; tất cả đều được giữ lại.
- Được tạo bởi `../../tools/build_hsr_glossary.py`, có thể tái lập.
