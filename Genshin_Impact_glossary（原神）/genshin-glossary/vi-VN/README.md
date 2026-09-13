# Từ điển thuật ngữ Genshin Impact — Tiếng Việt (`vi-VN`)

[← Quay lại phần giới thiệu chung của game](../../README.md) · [简体中文](README_zh-CN.md)

Thư mục này là phần từ điển thuật ngữ *Genshin Impact* **lấy tiếng Việt (`vi-VN`) làm ngôn ngữ đích**: xét theo 27 phân loại thì có **8.186 thuật ngữ**, trong đó tiếng Việt có **89.530 dòng đối chiếu**. Cột `tgt_lng` luôn là `vi-VN`; trong mỗi dòng, `source` là cách viết của cùng một thuật ngữ bằng **một trong 13 ngôn ngữ còn lại**, còn `target` là bản dịch tiếng Việt. Các tệp được chia theo **phân loại**, mỗi phân loại một tệp CSV.

## Tệp

- `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv` — 17 tệp phân loại chính
- `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv` — 10 tệp phân loại con TCG (Thất Thánh Triệu Hồi)

Tổng cộng **27 tệp CSV**. Tất cả đều có cùng định dạng ba cột:

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | Alhaitham | vi-VN |
| Аль-Хайтам | Alhaitham | vi-VN |

Cấu trúc thư mục:

```text
vi-VN/
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

## Phân loại và số lượng

**Thuật ngữ** là số thuật ngữ không trùng lặp của phân loại đó trong toàn bộ 14 ngôn ngữ (giống nhau ở mọi ngôn ngữ); **dòng** là số dòng dữ liệu của tệp đó trong `vi-VN`.

### Phân loại chính

| Phân loại | Tệp | Thuật ngữ | Dòng |
| --- | --- | ---: | ---: |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2.823 |
| materials | `materials.csv` | 919 | 10.648 |
| foods | `foods.csv` | 398 | 4.541 |
| crafts | `crafts.csv` | 295 | 3.522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3.636 |
| enemies | `enemies.csv` | 346 | 4.104 |
| animals | `animals.csv` | 223 | 2.647 |
| outfits | `outfits.csv` | 150 | 1.869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3.606 |
| geographies | `geographies.csv` | 268 | 3.389 |
| achievements | `achievements.csv` | 1.548 | 19.464 |
| adventureranks | `adventureranks.csv` | 21 | 156 |
| **Tổng phụ** | 17 tệp | — | **63.184** |

### Phân loại con TCG (`TCG/`)

| Phân loại con | Tệp | Thuật ngữ | Dòng |
| --- | --- | ---: | ---: |
| action-cards | `TCG/action-cards.csv` | 927 | 9.628 |
| character-cards | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 | 1.114 |
| summons | `TCG/summons.csv` | 152 | 1.157 |
| status-effects | `TCG/status-effects.csv` | 1.159 | 11.257 |
| keywords | `TCG/keywords.csv` | 139 | 1.511 |
| card-backs | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards | `TCG/level-rewards.csv` | 26 | 169 |
| **Tổng phụ** | 10 tệp | — | **26.346** |

**Tổng cộng thư mục này: 27 tệp, 89.530 dòng.**

## Ghi chú

- **Nguồn bản dịch và cách đối chiếu.** Dữ liệu lấy từ [theBowja/genshin-db](https://github.com/theBowja/genshin-db) (phiên bản dữ liệu 7.0, bao gồm cả 14 ngôn ngữ). Đây là **văn bản bản địa hóa chính thức của game**, không phải bản dịch lại hay văn bản do máy tạo. Việc đối chiếu theo đơn vị thuật ngữ: một đối tượng trong game sinh ra một dòng cho mỗi ngôn ngữ nguồn, vì vậy số dòng lớn hơn nhiều so với số thuật ngữ.
- **Nhãn ngôn ngữ.** Trong thư mục này `tgt_lng` luôn là `vi-VN`, chỉ ngôn ngữ đích; `source` có thể là bất kỳ ngôn ngữ nào trong 13 ngôn ngữ còn lại (`zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`).
- **Mã hóa.** Toàn bộ CSV dùng **UTF-8 có BOM**, xuống dòng **CRLF**, dòng đầu là tiêu đề; các trường chứa dấu phẩy hoặc dấu ngoặc kép được thoát theo RFC 4180. Excel mở trực tiếp được, không cần chỉnh mã hóa.
- **Hạn chế đã biết.** Số dòng theo phân loại có khác biệt nhỏ giữa các ngôn ngữ (ví dụ một số mục `achievements` và `adventureranks` không có ở mọi ngôn ngữ). Cùng một thuật ngữ có thể xuất hiện ở nhiều phân loại (ví dụ tên vũ khí cũng có trong `TCG`), nên tổng số dòng của các tệp lớn hơn số thuật ngữ không trùng lặp. Những tên chưa được bản địa hóa chính thức sẽ giữ nguyên dạng gốc.
- **Từ điển bổ sung.** Thư mục cùng cấp `genshin-glossary-supplement/` tập hợp các thuật ngữ chưa có trong từ điển chính này và có thể dùng chồng lên nhau; xem `README.md` của thư mục đó để biết chi tiết.

## Miễn trừ trách nhiệm

Thư mục này là một cơ sở dữ liệu thuật ngữ dịch thuật **không chính thức**, do một cá nhân biên soạn và duy trì, chỉ dùng cho việc học tập, nghiên cứu cá nhân và hỗ trợ khớp thuật ngữ cho phần mềm dịch bằng AI (bao gồm nhưng không giới hạn ở Immersive Translate). Cơ sở dữ liệu này không có bất kỳ quan hệ trực thuộc, cấp phép, hợp tác, đại diện hay đại diện chính thức nào với nhà phát triển, nhà phát hành, nhà phân phối, đơn vị vận hành hoặc chủ sở hữu bản quyền của các game liên quan; các bản dịch ở đây không thể hiện lập trường chính thức và không bảo đảm luôn chính xác, đầy đủ hoặc phù hợp với phiên bản hiện tại của game — **không nên coi đây là từ điển thuật ngữ chính thức hay tệp bản địa hóa chính thức của bất kỳ game nào**. Tên game, tên nhân vật, thuật ngữ riêng và nhãn hiệu thuộc quyền của các chủ sở hữu tương ứng. Mọi trách nhiệm phát sinh từ việc sử dụng thuộc về người dùng.

Điều khoản đầy đủ nằm trong `README.md` / `README_EN.md` / `README_JP.md` ở thư mục gốc của kho lưu trữ.

---

**Game-translation-terminology-database là một dự án cá nhân độc lập, không có bất kỳ quan hệ trực thuộc, ủy quyền, hợp tác hay đại diện nào với game này, nhà phát triển, nhà phát hành, nhà phân phối hay chủ sở hữu bản quyền của game.**
