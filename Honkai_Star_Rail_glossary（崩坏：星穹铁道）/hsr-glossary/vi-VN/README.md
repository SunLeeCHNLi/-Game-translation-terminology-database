# Cơ sở thuật ngữ Honkai: Star Rail — Tiếng Việt (`vi-VN`)

[← Quay lại phần giới thiệu game](../../README.md) ｜ [← thư mục con hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Thư mục này chứa cơ sở thuật ngữ Honkai: Star Rail với **`vi-VN` (Tiếng Việt) là ngôn ngữ đích**: **26** tệp CSV theo hạng mục và **317,104** dòng đối chiếu. Cột `tgt_lng` luôn là `vi-VN`, cột `source` chứa bản địa hóa chính thức của các ngôn ngữ khác.

## Tệp

Thư mục có **cấu trúc phẳng**: 26 tệp CSV hạng mục nằm trực tiếp tại đây.

| Tệp | Hạng mục | Số dòng của ngôn ngữ này |
| --- | --- | ---: |
| `01_character（Nhân vật & NPC）.csv` | Characters & NPCs | 2,905 |
| `02_path（Vận mệnh）.csv` | Paths | 206 |
| `03_element（Nguyên tố）.csv` | Elements | 149 |
| `04_skill（Kỹ năng）.csv` | Skills | 5,239 |
| `05_trace（Dấu vết）.csv` | Traces | 3,065 |
| `06_eidolon（Tinh hồn）.csv` | Eidolons | 5,563 |
| `07_light_cone（Nón ánh sáng）.csv` | Light Cones | 3,219 |
| `08_relic（Di vật）.csv` | Relics | 2,743 |
| `09_item（Vật phẩm）.csv` | Items | 19,918 |
| `10_material（Nguyên liệu）.csv` | Materials | 6,090 |
| `11_enemy（Kẻ địch）.csv` | Enemies | 9,701 |
| `12_location（Địa điểm）.csv` | Locations | 11,786 |
| `13_faction（Phe phái & tổ chức）.csv` | Factions | 361 |
| `14_quest（Nhiệm vụ）.csv` | Quests | 67,938 |
| `15_stage（Ải & bí cảnh）.csv` | Stages | 2,021 |
| `16_event（Sự kiện）.csv` | Events | 14,762 |
| `17_achievement（Thành tựu）.csv` | Achievements | 21,842 |
| `18_simulated_universe（Vũ trụ mô phỏng）.csv` | Simulated Universe | 20,586 |
| `19_forgotten_hall（Sảnh bị lãng quên）.csv` | Forgotten Hall | 9,772 |
| `20_story（Cốt truyện）.csv` | Story | 214 |
| `21_world_lore（Thế giới quan）.csv` | World Lore | 1,206 |
| `22_book（Sách）.csv` | Books | 11,337 |
| `23_dialogue（Hội thoại）.csv` | Dialogue | 60,386 |
| `24_system（Hệ thống）.csv` | System | 22,148 |
| `25_ui（Giao diện）.csv` | UI | 11,731 |
| `26_other（Khác）.csv` | Other | 2,216 |

## Ghi chú

- Bản dịch lấy từ bản địa hóa của client (TextMap / ExcelOutput), căn theo cùng một khóa văn bản — không phải dịch lại.
- Nếu ngôn ngữ đích thiếu văn bản cho một khóa, sẽ không tạo dòng nào và không dùng dịch máy để bù.
- Một khóa văn bản có thể có nhiều cách diễn đạt chính thức tùy ngữ cảnh; tất cả đều được giữ lại.
- Được tạo bởi `../../tools/build_hsr_glossary.py`, có thể tái lập.
