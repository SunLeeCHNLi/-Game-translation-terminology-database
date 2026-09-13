# Basis Data Terminologi Cat Fantasy — Bahasa Indonesia (`id-ID`)

[← Kembali ke penjelasan umum game](../README.md)

Direktori ini adalah basis data terminologi yang **menjadikan `id-ID` sebagai bahasa sasaran**: setiap baris
adalah pemetaan "entri bahasa lain → Bahasa Indonesia". Direktori ini memuat **9,916** entri dan **28,827**
baris padanan, dengan kolom `tgt_lng` tetap `id-ID`; kolom `source` memuat penulisan enam bahasa lain
(Tionghoa Sederhana, Tionghoa Tradisional, Inggris, Jepang, Korea, Thai). Semua terjemahan diambil dari teks
pelokalan yang sudah resmi tersedia di dalam game dan diselaraskan dengan kunci teks yang sama — tidak ada
terjemahan mesin.

**Penting — hanya kategori `13_ui` yang berisi data.** Tabel data game tidak menyediakan nama entitas
(chara, skill, item, stage, dan seterusnya) dalam Bahasa Indonesia; satu-satunya tabel resmi berbahasa
Indonesia adalah tabel teks antarmuka I18N. Karena itu 15 kategori lain di direktori ini hanya berisi baris
judul tanpa baris data. Rinciannya ada di bawah.

## Berkas

- `13_ui/13_ui_glossary.csv` — `source,target,tgt_lng` (tiga kolom), siap diimpor ke alat CAT / manajemen
  terminologi seperti Immersive Translation; **ini satu-satunya berkas padanan yang berisi data**;
- `13_ui/13_ui_terms.csv` — daftar entri untuk bahasa ini (`id,term,src_table`);
- `01_character/` … `16_terminology/` — 15 kategori lain berisi `NN_xxx_glossary.csv` dan
  `NN_xxx_terms.csv` dengan baris judul saja (0 baris data), disediakan agar struktur direktori sama dengan
  bahasa lain;
- `00_master/index.csv` — indeks kategori dan jumlah entri untuk bahasa ini;
- `00_master/README.md` — catatan direktori data bahasa ini (dalam bahasa Tionghoa).
- Tabel induk tujuh bahasa: `../multilingual/all_languages_master.csv` (102,213 entri × 10 kolom).

## Kategori dan jumlah

| Kategori | Tema | Entri | Baris padanan |
| --- | --- | --- | --- |
| `01_character` | Karakter dan kartu | 0 | 0 |
| `02_skill` | Skill dan efek pertarungan | 0 | 0 |
| `03_talent` | Talent dan awakening | 0 | 0 |
| `04_equipment` | Peralatan dan senjata khusus | 0 | 0 |
| `05_item` | Item dan material | 0 | 0 |
| `06_enemy` | Musuh dan boss | 0 | 0 |
| `07_stage` | Stage dan bab | 0 | 0 |
| `08_event` | Event dan mode permainan | 0 | 0 |
| `09_gacha` | Gacha dan penukaran | 0 | 0 |
| `10_shop` | Toko dan paket | 0 | 0 |
| `11_homeland` | Rumah dan kafe kucing | 0 | 0 |
| `12_system` | Sistem dan misi | 0 | 0 |
| `13_ui` | UI dan teks antarmuka | 9,916 | 28,827 |
| `14_story` | Nama khusus cerita | 0 | 0 |
| `15_location` | Lokasi dan wilayah | 0 | 0 |
| `16_terminology` | Terminologi mekanika game | 0 | 0 |
| **Total** | | **9,916** | **28,827** |

> "Entri" adalah jumlah kunci teks yang unik (jumlah baris data `*_terms.csv`); "baris padanan" adalah
> jumlah baris data `*_glossary.csv`. Kedua angka itu berbeda makna dan tidak dapat dipertukarkan.
> Semua angka di atas dapat diperiksa ulang pada `00_master/index.csv`.
>
> Mengapa 15 kategori kosong: permintaan bahasa Indonesia hanya diterapkan pada tabel teks antarmuka
> (I18N). Tabel data game (`Setting/Data`) tidak memiliki kolom berakhiran `_id_ID`, sehingga nama karakter,
> skill, item, stage, dan entitas lain tidak tersedia dalam Bahasa Indonesia dan tidak dapat dikumpulkan
> tanpa menerjemahkan sendiri — sesuatu yang sengaja tidak dilakukan oleh basis data ini.

## Catatan

- **Sumber dan penyelarasan terjemahan**: diambil dari teks Bahasa Indonesia yang sudah tersedia di tabel
  teks antarmuka I18N resmi game (`Setting/I18N`), diselaraskan dengan kunci teks yang sama (kolom `Id`);
  bukan terjemahan ulang.
- **Label bahasa**: kolom `tgt_lng` tetap `id-ID`; kolom `source` berisi penulisan bahasa lain, satu baris
  untuk setiap bahasa yang tersedia pada entri yang sama.
- **Pengodean**: semua CSV disimpan sebagai **UTF-8 with BOM + CRLF**, sehingga Excel menampilkannya dengan
  benar saat diklik dua kali.
- **Keterbatasan yang diketahui**:
  - cakupan bahasa ini hanya teks antarmuka, jadi tidak dapat dipakai untuk menerjemahkan nama entitas;
  - nama musuh tidak memiliki kolom multibahasa pada tabel data resmi, sehingga `06_enemy` hanya 27 entri
    pada bahasa lain;
  - Placeholder dalam teks (seperti `_name_`, `_num_`, `\n`) dipertahankan persis seperti teks resmi dan
    tidak diganti;
  - cakupan kunci teks berbeda antar bahasa (misalnya `zh-CN` mencakup 102,213 entri, `id-ID` hanya 9,916),
    sehingga jumlah tiap bahasa berbeda-beda. Ini wajar;
  - penulisan nama dapat berbeda antar versi regional dan versi game; basis data ini mengikuti versi paket
    data yang dirujuk di atas.
- **Pembaruan dan reproduksi**: basis data ini adalah produk data murni. Di direktori game **tidak ada
  folder `tools/` dan tidak ada skrip apa pun**; prosedur pembuatannya dicatat sebagai uraian teks pada
  bagian "Regeneration" di `../README.md`, dan tidak ada perintah yang dapat dijalankan.

## Penafian

Direktori ini adalah basis data terminologi terjemahan Bahasa Indonesia yang **tidak resmi**, disusun dan
dipelihara oleh perorangan, dan hanya ditujukan untuk pembelajaran pribadi, penelitian, serta bantuan
pencocokan terminologi pada perangkat lunak terjemahan AI (termasuk namun tidak terbatas pada Immersive
Translation). Basis data ini tidak memiliki hubungan afiliasi, izin, kemitraan, keagenan, maupun
keterwakilan resmi dengan pengembang, penerbit, distributor, operator, atau pemegang hak atas *Cat Fantasy*;
terjemahan di dalamnya tidak mewakili sikap resmi, tidak dijamin selalu akurat, lengkap, atau sesuai dengan
versi game saat ini, dan **tidak boleh dianggap sebagai daftar istilah resmi atau berkas pelokalan resmi**.
Kekayaan intelektual seperti nama game, nama karakter, nama khusus, dan merek dagang adalah milik
pemegang hak masing-masing, dan basis data ini tidak mengklaim hak apa pun atas kekayaan intelektual pihak
ketiga tersebut. Segala tanggung jawab yang timbul dari penggunaan proyek ini, atau dari hasil terjemahan
yang dihasilkan darinya, menjadi tanggungan pengguna. Untuk ketentuan lengkap, lihat
`README.md` / `README_EN.md` / `README_JP.md` di akar repositori.
