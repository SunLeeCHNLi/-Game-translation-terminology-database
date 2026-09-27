# Kho thuật ngữ 我的世界（Minecraft） — Tiếng Việt (`vi-VN`)

[← Quay lại phần giới thiệu chung của game](../../README.md) · [简体中文](README_zh-CN.md)

Thư mục này là kho thuật ngữ có **ngôn ngữ đích là tiếng Việt (`vi-VN`)**.
Gồm **101,325 dòng đối chiếu** trong **34 tệp CSV** (34 hạng mục: 19 tệp ở thư mục gốc và
15 tệp trong `extra-`); cột `tgt_lng` luôn là `vi-VN`, cột `source` chứa cách viết của 13 ngôn ngữ
còn lại. Bản dịch đích lấy từ **tệp ngôn ngữ chính thức của Minecraft Java Edition**, không phải
bản dịch lại.

## Tệp

- `<hạng mục>.csv` (19 tệp) — ba cột `source,target,tgt_lng`, nhập trực tiếp vào công cụ CAT hoặc hệ thống quản lý thuật ngữ
- `extra-<hạng mục>.csv` (15 tệp) — cùng ba cột, dành cho hạng mục hệ thống và văn bản

## Danh mục và số lượng

| Hạng mục | Chủ đề | Tệp | Số dòng |
| --- | --- | --- | --- |
| `blocks` | Khối | `blocks（Khối）.csv` | 25,426 |
| `items` | Vật phẩm | `items（Vật phẩm）.csv` | 9,103 |
| `entities` | Thực thể | `entities（Thực thể）.csv` | 2,582 |
| `biomes` | Quần xã sinh vật | `biomes（Quần xã sinh vật）.csv` | 835 |
| `enchantments` | Phù phép | `enchantments（Phù phép）.csv` | 553 |
| `effects` | Hiệu ứng trạng thái | `effects（Hiệu ứng trạng thái）.csv` | 514 |
| `instruments` | Nhạc cụ | `instruments（Nhạc cụ）.csv` | 98 |
| `materials` | Vật liệu trang trí | `materials（Nguyên liệu trang trí giáp）.csv` | 143 |
| `paintings` | Tranh | `paintings（Tranh）.csv` | 315 |
| `attributes` | Thuộc tính | `attributes（Thuộc tính）.csv` | 578 |
| `item-groups` | Nhóm vật phẩm | `item-groups（Nhóm vật phẩm）.csv` | 198 |
| `jukebox-songs` | Bài hát trong máy hát | `jukebox-songs（Bài hát máy hát）.csv` | 42 |
| `trim-patterns` | Hoa văn trang trí | `trim-patterns（Hoa văn trang trí giáp）.csv` | 234 |
| `colors` | Màu sắc | `colors（Màu sắc）.csv` | 184 |
| `statistics` | Thống kê | `statistics（Thống kê）.csv` | 1,143 |
| `maps` | Bản đồ | `maps（Bản đồ）.csv` | 422 |
| `music` | Bản nhạc | `music（Âm nhạc）.csv` | 192 |
| `sound-categories` | Loại âm thanh | `sound-categories（Phân loại âm thanh）.csv` | 133 |
| `game-modes` | Chế độ chơi | `game-modes（Chế độ chơi）.csv` | 77 |

### `extra-` (hệ thống và văn bản)

| Hạng mục | Chủ đề | Tệp | Số dòng |
| --- | --- | --- | --- |
| `subtitles` | Phụ đề | `extra-subtitles（Phụ đề）.csv` | 12,416 |
| `death-messages` | Thông báo tử vong | `extra-death-messages（Thông báo tử vong）.csv` | 1,334 |
| `advancement-titles` | Tên tiến trình | `extra-advancement-titles（Tiêu đề tiến trình）.csv` | 1,603 |
| `advancement-descriptions` | Mô tả tiến trình | `extra-advancement-descriptions（Mô tả tiến trình）.csv` | 1,641 |
| `gamerules` | Luật chơi | `extra-gamerules（Luật chơi）.csv` | 1,490 |
| `commands` | Lệnh và đối số | `extra-commands（Lệnh và tham số）.csv` | 10,738 |
| `gui` | Văn bản giao diện | `extra-gui（Văn bản giao diện）.csv` | 6,609 |
| `options` | Cài đặt và phím | `extra-options（Cài đặt và phím）.csv` | 8,152 |
| `multiplayer` | Nhiều người chơi | `extra-multiplayer（Nhiều người chơi）.csv` | 2,024 |
| `realms` | Realms | `extra-realms（Realms）.csv` | 4,996 |
| `world-management` | Quản lý thế giới | `extra-world-management（Quản lý thế giới）.csv` | 3,565 |
| `resource-packs` | Gói tài nguyên và dữ liệu | `extra-resource-packs（Gói tài nguyên và dữ liệu）.csv` | 761 |
| `telemetry` | Dữ liệu từ xa | `extra-telemetry（Đo từ xa）.csv` | 897 |
| `dev-tools` | Công cụ phát triển và kiểm thử | `extra-dev-tools（Công cụ phát triển và thử nghiệm）.csv` | 1,811 |
| `misc` | Khác | `extra-misc（Khác）.csv` | 516 |

### Danh sách tệp

```text
minecraft-glossary/
<lang>/                       # 14 thư mục ngôn ngữ
|   blocks（Khối）.csv
|   items（Vật phẩm）.csv
|   entities（Thực thể）.csv
|   biomes（Quần xã sinh vật）.csv
|   enchantments（Phù phép）.csv
|   effects（Hiệu ứng trạng thái）.csv
|   instruments（Nhạc cụ）.csv
|   materials（Nguyên liệu trang trí giáp）.csv
|   paintings（Tranh）.csv
|   attributes（Thuộc tính）.csv
|   item-groups（Nhóm vật phẩm）.csv
|   jukebox-songs（Bài hát máy hát）.csv
|   trim-patterns（Hoa văn trang trí giáp）.csv
|   colors（Màu sắc）.csv
|   statistics（Thống kê）.csv
|   maps（Bản đồ）.csv
|   music（Âm nhạc）.csv
|   sound-categories（Phân loại âm thanh）.csv
|   game-modes（Chế độ chơi）.csv
|   +-- extra-               # hạng mục hệ thống và văn bản
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

## Ghi chú

- **Nguồn và cách đối chiếu.** Thuật ngữ được trích từ tệp ngôn ngữ chính thức của Minecraft Java
  Edition (`assets/minecraft/lang/vi_vn.json` qua [misode/mcmeta](https://github.com/misode/mcmeta)),
  tức là bản địa hóa chính thức. Trong mỗi tệp, `target` là văn bản tiếng Việt còn `source` là văn bản
  tương ứng ở **một trong 13 ngôn ngữ còn lại**; mỗi thuật ngữ xuất hiện một lần cho mỗi ngôn ngữ
  nguồn (các dòng trùng nhau, kể cả khi `source` bằng `target`, đã được gộp).

- **Nhãn ngôn ngữ.** `tgt_lng` luôn là `vi-VN`, tương ứng locale chính thức `vi_vn`.

- **Mã hóa.** Mọi tệp CSV đều là **UTF-8 kèm BOM**, xuống dòng **CRLF**, dòng đầu là tiêu đề; các
  trường chứa dấu phẩy, dấu ngoặc kép hoặc xuống dòng được thoát theo RFC 4180. Nhờ BOM và CRLF,
  Excel mở tệp đúng ngay khi nhấp đúp. Lưu ý: một số trường văn bản dài chứa ký tự xuống dòng bên
  trong dấu ngoặc kép (khoảng 2.000 trường mỗi ngôn ngữ), nên hãy dùng trình phân tích CSV tương
  thích RFC 4180 thay vì đếm số dòng thô.

- **Hạn chế đã biết.** "Số dòng đối chiếu" không phải "số mục từ" — tổng `entries` của 34 hạng mục là
  8,559, tức số đối tượng tên trong game được xếp vào từng hạng mục trong tệp ngôn ngữ chính thức
  (bao gồm cả mục chưa được dịch trong ngôn ngữ đó). Định nghĩa đầy đủ nằm ở mục «Data Overview»
  trong `../../README.md` tại thư mục gốc của game. Một phần số dòng chỉ là văn bản giao diện (GUI,
  nhiều người chơi, Realms…), không phải thuật ngữ. Thuật ngữ chưa được bản địa hóa chính thức sẽ
  không tạo dòng nào. Số dòng của 14 thư mục ngôn ngữ khác nhau đôi chút vì mức độ dịch của mỗi
  ngôn ngữ khác nhau.

- **Tái tạo.** `python tools/build_glossary.py` (chạy từ thư mục gốc của game); script đọc một thư mục
  dữ liệu bên ngoài. Bảng ánh xạ tiền tố sang hạng mục đầy đủ nằm trong `CATEGORIES` của script.

## Tuyên bố miễn trừ trách nhiệm

Thư mục này là kho thuật ngữ dịch **không chính thức**, do cá nhân biên soạn và duy trì, chỉ dùng
cho việc học tập, nghiên cứu và hỗ trợ đối chiếu thuật ngữ trong phần mềm dịch bằng AI. Kho này không
có bất kỳ quan hệ trực thuộc, cấp phép, hợp tác hay đại diện chính thức nào với nhà phát triển, nhà
phát hành, nhà phân phối, đơn vị vận hành hoặc chủ sở hữu bản quyền của game; các thuật ngữ ở đây
không đại diện cho lập trường chính thức và không được coi là kho thuật ngữ chính thức của bất kỳ game
nào. Quyền sở hữu trí tuệ đối với tên game, nhân vật và nhãn hiệu thuộc về chủ sở hữu tương ứng.
Người dùng tự chịu mọi trách nhiệm phát sinh từ việc sử dụng dự án này. Điều khoản đầy đủ có trong
`README.md` / `README_EN.md` / `README_JP.md` ở thư mục gốc của kho.
