# คลังศัพท์ 我的世界（Minecraft） — ภาษาไทย (`th-TH`)

[← กลับไปยังคำอธิบายรวมของเกม](../../README.md)

ไดเรกทอรีนี้เป็นคลังศัพท์ที่**ใช้ภาษาไทย (`th-TH`) เป็นภาษาปลายทาง**
มี **101,264 บรรทัดเทียบเคียง** ใน **ไฟล์ CSV 34 ไฟล์** (34 หมวดหมู่: 19 ไฟล์ในรากไดเรกทอรี
และ 15 ไฟล์ใน `extra/`) โดยคอลัมน์ `tgt_lng` เป็น `th-TH` เสมอ และคอลัมน์ `source` เก็บรูปเขียน
ของอีก 13 ภาษาที่เหลือ คำแปลปลายทางมาจาก**ไฟล์ภาษาทางการของ Minecraft Java Edition**
ไม่ใช่การแปลซ้ำ

## ไฟล์

- `<หมวดหมู่>.csv` (19 ไฟล์) — สามคอลัมน์ `source,target,tgt_lng` นำเข้าเครื่องมือ CAT หรือระบบจัดการศัพท์ได้โดยตรง
- `extra/<หมวดหมู่>.csv` (15 ไฟล์) — สามคอลัมน์เดียวกัน สำหรับหมวดหมู่ระบบและข้อความ

## หมวดหมู่และจำนวน

| หมวดหมู่ | หัวข้อ | ไฟล์ | บรรทัด |
| --- | --- | --- | --- |
| `blocks` | บล็อก | `blocks.csv` | 25,426 |
| `items` | ไอเทม | `items.csv` | 9,061 |
| `entities` | เอนทิตี | `entities.csv` | 2,581 |
| `biomes` | ไบโอม | `biomes.csv` | 835 |
| `enchantments` | คาถาเสริม | `enchantments.csv` | 553 |
| `effects` | เอฟเฟกต์สถานะ | `effects.csv` | 514 |
| `instruments` | เครื่องดนตรี | `instruments.csv` | 98 |
| `materials` | วัสดุตกแต่ง | `materials.csv` | 143 |
| `paintings` | ภาพวาด | `paintings.csv` | 315 |
| `attributes` | ค่าคุณลักษณะ | `attributes.csv` | 555 |
| `item-groups` | กลุ่มไอเทม | `item-groups.csv` | 198 |
| `jukebox-songs` | เพลงในตู้jukebox | `jukebox-songs.csv` | 42 |
| `trim-patterns` | ลวดลายตกแต่ง | `trim-patterns.csv` | 234 |
| `colors` | สี | `colors.csv` | 184 |
| `statistics` | สถิติ | `statistics.csv` | 1,143 |
| `maps` | แผนที่ | `maps.csv` | 422 |
| `music` | เพลงประกอบ | `music.csv` | 192 |
| `sound-categories` | หมวดหมู่เสียง | `sound-categories.csv` | 133 |
| `game-modes` | โหมดเกม | `game-modes.csv` | 77 |

### `extra/` (ระบบและข้อความ)

| หมวดหมู่ | หัวข้อ | ไฟล์ | บรรทัด |
| --- | --- | --- | --- |
| `subtitles` | คำบรรยาย | `extra/subtitles.csv` | 12,402 |
| `death-messages` | ข้อความเมื่อตาย | `extra/death-messages.csv` | 1,336 |
| `advancement-titles` | ชื่อความก้าวหน้า | `extra/advancement-titles.csv` | 1,603 |
| `advancement-descriptions` | คำอธิบายความก้าวหน้า | `extra/advancement-descriptions.csv` | 1,641 |
| `gamerules` | กฎของเกม | `extra/gamerules.csv` | 1,490 |
| `commands` | คำสั่งและอาร์กิวเมนต์ | `extra/commands.csv` | 10,750 |
| `gui` | ข้อความส่วนติดต่อผู้ใช้ | `extra/gui.csv` | 6,649 |
| `options` | การตั้งค่าและปุ่มกด | `extra/options.csv` | 8,162 |
| `multiplayer` | ผู้เล่นหลายคน | `extra/multiplayer.csv` | 2,010 |
| `realms` | Realms | `extra/realms.csv` | 4,964 |
| `world-management` | การจัดการโลก | `extra/world-management.csv` | 3,574 |
| `resource-packs` | ทรัพยากรและดาต้าแพ็ก | `extra/resource-packs.csv` | 761 |
| `telemetry` | การส่งข้อมูลเทเลเมทรี | `extra/telemetry.csv` | 897 |
| `dev-tools` | เครื่องมือพัฒนาและทดสอบ | `extra/dev-tools.csv` | 1,803 |
| `misc` | อื่น ๆ | `extra/misc.csv` | 516 |

### รายการไฟล์

```text
minecraft-glossary/
<lang>/                       # 14 โฟลเดอร์ภาษา
|   blocks.csv
|   items.csv
|   entities.csv
|   biomes.csv
|   enchantments.csv
|   effects.csv
|   instruments.csv
|   materials.csv
|   paintings.csv
|   attributes.csv
|   item-groups.csv
|   jukebox-songs.csv
|   trim-patterns.csv
|   colors.csv
|   statistics.csv
|   maps.csv
|   music.csv
|   sound-categories.csv
|   game-modes.csv
|   +-- extra/               # หมวดหมู่ระบบและข้อความ
|       |-- subtitles.csv
|       |-- death-messages.csv
|       |-- advancement-titles.csv
|       |-- advancement-descriptions.csv
|       |-- gamerules.csv
|       |-- commands.csv
|       |-- gui.csv
|       |-- options.csv
|       |-- multiplayer.csv
|       |-- realms.csv
|       |-- world-management.csv
|       |-- resource-packs.csv
|       |-- telemetry.csv
|       |-- dev-tools.csv
|       \-- misc.csv
+-- de-DE/ en-US/ ... vi-VN/
```

## หมายเหตุ

- **ที่มาและการจับคู่.** คำศัพท์ดึงมาจากไฟล์ภาษาทางการของ Minecraft Java Edition
  (`assets/minecraft/lang/th_th.json` ผ่าน [misode/mcmeta](https://github.com/misode/mcmeta))
  จึงเป็นคำแปลทางการ ในแต่ละไฟล์ `target` คือข้อความภาษาไทย และ `source` คือข้อความใน
  **ภาษาใดก็ได้จากอีก 13 ภาษา** คำเดียวกันจะปรากฏหนึ่งครั้งต่อภาษาต้นทาง (บรรทัดที่เหมือนกัน
  รวมถึงกรณี `source` เท่ากับ `target` ถูกยุบรวมแล้ว)

- **ป้ายภาษา.** `tgt_lng` เป็น `th-TH` เสมอ ซึ่งตรงกับโลแคลทางการ `th_th`

- **การเข้ารหัส.** ไฟล์ CSV ทั้งหมดเป็น **UTF-8 with BOM** ขึ้นบรรทัดใหม่แบบ **CRLF** และมีหัวตารางใน
  บรรทัดแรก ฟิลด์ที่มีจุลภาค เครื่องหมายคำพูด หรือขึ้นบรรทัดใหม่ จะถูก escape ตาม RFC 4180
  BOM และ CRLF ทำให้เปิดไฟล์ใน Excel ได้ทันที ข้อควรระวัง: ฟิลด์ข้อความยาวบางฟิลด์มีขึ้นบรรทัดใหม่
  อยู่ภายในเครื่องหมายคำพูด (ประมาณ 2,000 ฟิลด์ต่อภาษา) จึงควรใช้ตัวแยกวิเคราะห์ CSV ที่รองรับ
  RFC 4180 แทนการนับบรรทัดดิบ

- **ข้อจำกัดที่ทราบ.** "จำนวนบรรทัดเทียบเคียง" ไม่ใช่ "จำนวนคำศัพท์" — ผลรวม `entries` ของ 34 หมวดหมู่
  เท่ากับ 8,559 ซึ่งหมายถึงจำนวนออบเจ็กต์ชื่อในเกมที่จัดอยู่ในแต่ละหมวดหมู่ของไฟล์ภาษาทางการ
  (รวมรายการที่ยังไม่ได้แปลในภาษานั้น) คำจำกัดความฉบับเต็มอยู่ในหัวข้อ «Data Overview»
  ของ `../../README.md` ที่รากของเกม บางบรรทัดเป็นเพียงข้อความส่วนติดต่อผู้ใช้ (GUI, โหมดผู้เล่นหลายคน,
  Realms ฯลฯ) ไม่ใช่คำศัพท์โดยตรง คำศัพท์ที่ฉบับทางการไม่ได้แปลจะไม่สร้างบรรทัด ทั้ง 14 โฟลเดอร์ภาษา
  มีจำนวนบรรทัดต่างกันเล็กน้อย เนื่องจากความครอบคลุมการแปลของแต่ละภาษาไม่เท่ากัน

- **การสร้างซ้ำ.** `python tools/build_glossary.py` (รากของเกม) สคริปต์อ่านไดเรกทอรีข้อมูลภายนอก
  ตารางจับคู่คำนำหน้ากับหมวดหมู่ทั้งหมดอยู่ใน `CATEGORIES` ของสคริปต์นั้น

## ข้อจำกัดความรับผิด

ไดเรกทอรีนี้เป็นคลังศัพท์การแปล**อย่างไม่เป็นทางการ** จัดทำและดูแลในระดับบุคคล ใช้เพื่อการศึกษา
ค้นคว้า และช่วยจับคู่ศัพท์ในโปรแกรมแปลด้วย AI เท่านั้น ไม่มีความสัมพันธ์ในลักษณะสังกัด ได้รับอนุญาต
ร่วมมือ หรือเป็นตัวแทนอย่างเป็นทางการกับผู้พัฒนา ผู้จัดจำหน่าย ผู้ให้บริการ หรือผู้ถือลิขสิทธิ์ของเกม
คำศัพท์ในคลังไม่ถือเป็นจุดยืนทางการ และไม่ควรใช้เป็นคลังศัพท์ทางการของเกมใด ๆ สิทธิ์ในทรัพย์สินทาง
ปัญญาของชื่อเกม ชื่อตัวละคร และเครื่องหมายการค้าเป็นของผู้ถือสิทธิ์แต่ละราย ผู้ใช้รับผิดชอบเอง
ต่อผลที่เกิดจากการใช้โครงการนี้ ข้อกำหนดฉบับเต็มอยู่ใน `README.md` / `README_EN.md` / `README_JP.md`
ที่รากของรีโพซิทอรี
