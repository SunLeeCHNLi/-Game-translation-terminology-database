# คลังศัพท์ Genshin Impact — ภาษาไทย (`th-TH`)

[← กลับไปยังคำอธิบายรวมของเกม](../../README.md) · [简体中文](README_zh-CN.md)

ไดเรกทอรีนี้เป็นคลังศัพท์ของ *Genshin Impact* ที่**ใช้ภาษาไทย (`th-TH`) เป็นภาษาเป้าหมาย** โดยคลังศัพท์ทั้งชุดมี **8,186 คำศัพท์** เมื่อรวมทั้ง 27 หมวดหมู่ และภาษาไทยมี **89,468 บรรทัดเทียบคำ** คอลัมน์ `tgt_lng` เป็น `th-TH` เสมอ ในแต่ละบรรทัด `source` คือรูปเขียนของคำเดียวกันใน**หนึ่งในอีก 13 ภาษาที่เหลือ** และ `target` คือคำแปลภาษาไทย ไฟล์ถูกแบ่งตาม**หมวดหมู่** หนึ่งหมวดหมู่ต่อหนึ่งไฟล์ CSV

## ไฟล์

- `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv` — 17 ไฟล์หมวดหมู่หลัก
- `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv` — 10 ไฟล์หมวดหมู่ย่อย TCG (เกมเรียกเทพทั้งเจ็ด)

รวม **27 ไฟล์ CSV** ทุกไฟล์มีรูปแบบเดียวกันคือสามคอลัมน์:

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | Alhaitham | th-TH |
| Аль-Хайтам | Alhaitham | th-TH |

โครงสร้างไดเรกทอรี:

```text
th-TH/
├── characters.csv
├── talents.csv
├── constellations.csv
├── weapons.csv
├── materials.csv
├── foods.csv
├── crafts.csv
├── artifacts.csv
├── domains.csv
├── enemies.csv
├── animals.csv
├── outfits.csv
├── windgliders.csv
├── namecards.csv
├── geographies.csv
├── achievements.csv
├── adventureranks.csv
└── TCG/
    ├── action-cards.csv
    ├── character-cards.csv
    ├── enemy-cards.csv
    ├── summons.csv
    ├── status-effects.csv
    ├── keywords.csv
    ├── card-backs.csv
    ├── card-boxes.csv
    ├── detailed-rules.csv
    └── level-rewards.csv
```

## หมวดหมู่และจำนวน

**คำศัพท์** คือจำนวนคำที่ไม่ซ้ำของหมวดนั้นในทั้ง 14 ภาษา (ค่าเดียวกันทุกภาษา) ส่วน **บรรทัด** คือจำนวนบรรทัดข้อมูลของไฟล์นั้นในภาษา `th-TH`

### หมวดหมู่หลัก

| หมวดหมู่ | ไฟล์ | คำศัพท์ | บรรทัด |
| --- | --- | ---: | ---: |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2,823 |
| materials | `materials.csv` | 919 | 10,636 |
| foods | `foods.csv` | 398 | 4,541 |
| crafts | `crafts.csv` | 295 | 3,522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3,636 |
| enemies | `enemies.csv` | 346 | 4,104 |
| animals | `animals.csv` | 223 | 2,647 |
| outfits | `outfits.csv` | 150 | 1,869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3,606 |
| geographies | `geographies.csv` | 268 | 3,389 |
| achievements | `achievements.csv` | 1,548 | 19,464 |
| adventureranks | `adventureranks.csv` | 21 | 157 |
| **รวมย่อย** | 17 ไฟล์ | — | **63,173** |

### หมวดหมู่ย่อย TCG (`TCG/`)

| หมวดหมู่ย่อย | ไฟล์ | คำศัพท์ | บรรทัด |
| --- | --- | ---: | ---: |
| action-cards | `TCG/action-cards.csv` | 927 | 9,609 |
| character-cards | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 | 1,126 |
| summons | `TCG/summons.csv` | 152 | 1,150 |
| status-effects | `TCG/status-effects.csv` | 1,159 | 11,220 |
| keywords | `TCG/keywords.csv` | 139 | 1,511 |
| card-backs | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards | `TCG/level-rewards.csv` | 26 | 169 |
| **รวมย่อย** | 10 ไฟล์ | — | **26,295** |

**รวมทั้งไดเรกทอรี: 27 ไฟล์ 89,468 บรรทัด**

## หมายเหตุ

- **ที่มาของคำแปลและการเทียบคำ** ข้อมูลมาจาก [theBowja/genshin-db](https://github.com/theBowja/genshin-db) (เวอร์ชันข้อมูล 7.0 ครอบคลุมทั้ง 14 ภาษา) เป็น**ข้อความที่ทีมโลคัลไลซ์ของเกมใช้จริง** ไม่ใช่การแปลซ้ำหรือข้อความที่สร้างโดยเครื่อง การเทียบคำทำในระดับคำศัพท์ คำหนึ่งจะปรากฏหนึ่งบรรทัดต่อหนึ่งภาษาต้นทาง จึงทำให้จำนวนบรรทัดมากกว่าจำนวนคำศัพท์มาก
- **ป้ายภาษ** ในไดเรกทอรีนี้ `tgt_lng` เป็น `th-TH` เสมอ หมายถึงภาษาเป้าหมาย ส่วน `source` อาจเป็นหนึ่งในอีก 13 ภาษา (`zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `vi-VN`)
- **การเข้ารหัส** ไฟล์ CSV ทั้งหมดเป็น **UTF-8 with BOM** ขึ้นบรรทัดใหม่แบบ **CRLF** บรรทัดแรกเป็นหัวตาราง ฟิลด์ที่มีจุลภาคหรือเครื่องหมายคำพูดใช้การ escape ตาม RFC 4180 เปิดใน Excel ได้ทันทีโดยไม่ต้องตั้งค่าการเข้ารหัส
- **ข้อจำกัดที่ทราบ** จำนวนบรรทัดของแต่ละหมวดแตกต่างกันเล็กน้อยระหว่างภาษา (เช่น บางรายการใน `achievements` และ `adventureranks` ไม่มีในทุกภาษา) คำเดียวกันอาจปรากฏในหลายหมวด (เช่น ชื่ออาวุธที่อยู่ใน `TCG` ด้วย) ดังนั้นผลรวมบรรทัดของทุกไฟล์จึงมากกว่าจำนวนคำศัพท์ที่ไม่ซ้ำ ชื่อที่ทางการไม่ได้แปลจะคงรูปเดิมไว้
- **คลังศัพท์เสริม** ไดเรกทอรีข้างเคียง `genshin-glossary-supplement/` รวบรวมคำที่ไม่มีในคลังหลักนี้ และใช้ซ้อนกับคลังนี้ได้ ดูรายละเอียดใน `README.md` ของคลังนั้น

## ข้อจำกัดความรับผิด

ไดเรกทอรีนี้เป็นคลังศัพท์เพื่อการแปลที่**ไม่เป็นทางการ** จัดทำและดูแลโดยบุคคลคนเดียว ใช้เพื่อการศึกษา การวิจัยส่วนบุคคล และช่วยจับคู่ศัพท์ให้ซอฟต์แวร์แปลด้วย AI (รวมถึงแต่ไม่จำกัดเพียง Immersive Translate) เท่านั้น คลังนี้ไม่มีความสัมพันธ์ใด ๆ ในด้านการสังกัด การอนุญาต การร่วมมือ การเป็นตัวแทน หรือการเป็นผู้แทนอย่างเป็นทางการ กับผู้พัฒนา ผู้จัดจำหน่าย ผู้ให้บริการ หรือผู้ถือลิขสิทธิ์ของเกมที่เกี่ยวข้อง คำแปลในคลังไม่ถือเป็นจุดยืนทางการ และไม่รับประกันว่าถูกต้อง ครบถ้วน หรือตรงกับเวอร์ชันปัจจุบันของเกมเสมอไป **ไม่ควรถือเป็นคลังศัพท์ทางการหรือไฟล์โลคัลไลซ์ทางการของเกมใด ๆ** ชื่อเกม ชื่อตัวละคร คำเฉพาะ และเครื่องหมายการค้าเป็นทรัพย์สินทางปัญญาของเจ้าของแต่ละราย ผู้ใช้รับความเสี่ยงและความรับผิดชอบทั้งหมดจากการใช้งาน

ดูข้อกำหนดฉบับเต็มได้ที่ `README.md` / `README_EN.md` / `README_JP.md` ในรากของรีโพซิทอรี

---

**Game-translation-terminology-database เป็นโครงการส่วนบุคคลที่เป็นอิสระ ไม่มีความเกี่ยวข้องด้านการสังกัด การอนุญาต การร่วมมือ หรือการเป็นตัวแทนใด ๆ กับเกมนี้ ผู้พัฒนา ผู้จัดจำหน่าย ผู้ให้บริการ หรือผู้ถือลิขสิทธิ์**
