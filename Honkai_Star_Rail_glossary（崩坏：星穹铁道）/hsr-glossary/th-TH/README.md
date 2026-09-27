# ฐานข้อมูลคำศัพท์ Honkai: Star Rail — ไทย (`th-TH`)

[← กลับไปยังคำอธิบายเกม](../../README.md) ｜ [← คำอธิบาย hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

ไดเรกทอรีนี้เป็นฐานข้อมูลคำศัพท์ Honkai: Star Rail ที่**ใช้ `th-TH` (ไทย) เป็นภาษาปลายทาง** มีไฟล์ CSV **26** หมวดหมู่ และ **317,329** แถวเทียบเคียง คอลัมน์ `tgt_lng` เป็น `th-TH` เสมอ ส่วนคอลัมน์ `source` เก็บข้อความโลคัลไลซ์ทางการของภาษาอื่น

## ไฟล์

ไดเรกทอรีนี้เป็น**โครงสร้างแบน**: ไฟล์ CSV 26 หมวดหมู่วางอยู่ที่นี่โดยตรง

| ไฟล์ | หมวดหมู่ | จำนวนแถวในภาษานี้ |
| --- | --- | ---: |
| `01_character（ตัวละครและ NPC）.csv` | Characters & NPCs | 2,910 |
| `02_path（เส้นทาง）.csv` | Paths | 206 |
| `03_element（ธาตุ）.csv` | Elements | 149 |
| `04_skill（สกิล）.csv` | Skills | 5,176 |
| `05_trace（ร่องรอย）.csv` | Traces | 3,062 |
| `06_eidolon（อิดอลอน）.csv` | Eidolons | 5,485 |
| `07_light_cone（โคนแสง）.csv` | Light Cones | 3,219 |
| `08_relic（โบราณวัตถุ）.csv` | Relics | 2,737 |
| `09_item（ไอเทม）.csv` | Items | 19,867 |
| `10_material（วัสดุ）.csv` | Materials | 6,082 |
| `11_enemy（ศัตรู）.csv` | Enemies | 9,525 |
| `12_location（สถานที่）.csv` | Locations | 11,717 |
| `13_faction（ฝ่ายและองค์กร）.csv` | Factions | 356 |
| `14_quest（เควสต์）.csv` | Quests | 68,863 |
| `15_stage（ด่านและดันเจียน）.csv` | Stages | 1,991 |
| `16_event（กิจกรรม）.csv` | Events | 14,833 |
| `17_achievement（ความสำเร็จ）.csv` | Achievements | 21,915 |
| `18_simulated_universe（จักรวาลจำลอง）.csv` | Simulated Universe | 20,271 |
| `19_forgotten_hall（หอหลงลืม）.csv` | Forgotten Hall | 9,739 |
| `20_story（เนื้อเรื่อง）.csv` | Story | 214 |
| `21_world_lore（โลกทัศน์）.csv` | World Lore | 1,202 |
| `22_book（หนังสือ）.csv` | Books | 11,455 |
| `23_dialogue（บทสนทนา）.csv` | Dialogue | 60,451 |
| `24_system（ระบบ）.csv` | System | 21,913 |
| `25_ui（อินเทอร์เฟซ）.csv` | UI | 11,769 |
| `26_other（อื่น ๆ）.csv` | Other | 2,222 |

## หมายเหตุ

- คำแปลมาจากข้อความโลคัลไลซ์ของตัวเกม (TextMap / ExcelOutput) จับคู่ด้วยคีย์ข้อความเดียวกัน ไม่ใช่การแปลซ้ำ
- หากภาษาปลายทางไม่มีข้อความสำหรับคีย์นั้น จะไม่สร้างแถวและไม่เติมด้วยการแปลด้วยเครื่อง
- คีย์เดียวกันอาจมีคำแปลทางการได้หลายแบบตามบริบท ทั้งหมดจะถูกเก็บไว้
- สร้างด้วย `../../tools/build_hsr_glossary.py` ทำซ้ำได้
