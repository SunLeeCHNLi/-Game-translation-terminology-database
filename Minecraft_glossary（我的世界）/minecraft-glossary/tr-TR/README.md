# 我的世界（Minecraft） terim sözlüğü — Türkçe (`tr-TR`)

[← Oyunun genel açıklamasına dön](../../README.md) · [简体中文](README_zh-CN.md)

Bu dizin, **hedef dili Türkçe (`tr-TR`) olan** terim sözlüğüdür.
**34 CSV dosyasında** (34 kategori: 19'u dizin kökünde, 15'i `extra-` içinde) toplam
**101,665 karşılık satırı** bulunur; `tgt_lng` sütunu her zaman `tr-TR`, `source` sütunu ise diğer
13 dildeki yazımları içerir. Hedef çeviriler **Minecraft Java Edition'ın resmî dil dosyalarından**
alınmıştır; yeniden çeviri değildir.

## Dosyalar

- `<kategori>.csv` (19 dosya) — `source,target,tgt_lng` olmak üzere üç sütun; CAT ve terim yönetimi araçlarına doğrudan aktarılabilir
- `extra-<kategori>.csv` (15 dosya) — aynı üç sütun; sistem ve metin kategorileri için

## Kategoriler ve sayılar

| Kategori | Konu | Dosya | Satır |
| --- | --- | --- | --- |
| `blocks` | Bloklar | `blocks（Bloklar）.csv` | 25,426 |
| `items` | Eşyalar | `items（Eşyalar）.csv` | 9,115 |
| `entities` | Varlıklar | `entities（Varlıklar）.csv` | 2,592 |
| `biomes` | Biyomlar | `biomes（Biyomlar）.csv` | 835 |
| `enchantments` | Büyüler | `enchantments（Büyüler）.csv` | 553 |
| `effects` | Durum etkileri | `effects（Durum etkileri）.csv` | 514 |
| `instruments` | Enstrümanlar | `instruments（Enstrümanlar）.csv` | 98 |
| `materials` | Süsleme malzemeleri | `materials（Zırh süsleme malzemeleri）.csv` | 143 |
| `paintings` | Tablolar | `paintings（Tablolar）.csv` | 315 |
| `attributes` | Nitelikler | `attributes（Nitelikler）.csv` | 590 |
| `item-groups` | Eşya grupları | `item-groups（Eşya grupları）.csv` | 198 |
| `jukebox-songs` | Müzik kutusu parçaları | `jukebox-songs（Müzik kutusu şarkıları）.csv` | 42 |
| `trim-patterns` | Süsleme desenleri | `trim-patterns（Zırh süsleme desenleri）.csv` | 234 |
| `colors` | Renkler | `colors（Renkler）.csv` | 184 |
| `statistics` | İstatistikler | `statistics（İstatistikler）.csv` | 1,143 |
| `maps` | Haritalar | `maps（Haritalar）.csv` | 422 |
| `music` | Müzik parçaları | `music（Müzik）.csv` | 192 |
| `sound-categories` | Ses kategorileri | `sound-categories（Ses kategorileri）.csv` | 133 |
| `game-modes` | Oyun modları | `game-modes（Oyun modları）.csv` | 77 |

### `extra-` (sistem ve metin)

| Kategori | Konu | Dosya | Satır |
| --- | --- | --- | --- |
| `subtitles` | Alt yazılar | `extra-subtitles（Altyazılar）.csv` | 12,431 |
| `death-messages` | Ölüm mesajları | `extra-death-messages（Ölüm mesajları）.csv` | 1,354 |
| `advancement-titles` | Başarım adları | `extra-advancement-titles（İlerleme başlıkları）.csv` | 1,603 |
| `advancement-descriptions` | Başarım açıklamaları | `extra-advancement-descriptions（İlerleme açıklamaları）.csv` | 1,650 |
| `gamerules` | Oyun kuralları | `extra-gamerules（Oyun kuralları）.csv` | 1,490 |
| `commands` | Komutlar ve argümanlar | `extra-commands（Komutlar ve argümanlar）.csv` | 10,765 |
| `gui` | Arayüz metinleri | `extra-gui（Arayüz metinleri）.csv` | 6,751 |
| `options` | Ayarlar ve tuşlar | `extra-options（Ayarlar ve tuşlar）.csv` | 8,174 |
| `multiplayer` | Çok oyunculu | `extra-multiplayer（Çok oyunculu）.csv` | 2,021 |
| `realms` | Realms | `extra-realms（Realms）.csv` | 5,054 |
| `world-management` | Dünya yönetimi | `extra-world-management（Dünya yönetimi）.csv` | 3,581 |
| `resource-packs` | Kaynak ve veri paketleri | `extra-resource-packs（Kaynak ve veri paketleri）.csv` | 761 |
| `telemetry` | Telemetri | `extra-telemetry（Telemetri）.csv` | 897 |
| `dev-tools` | Geliştirme ve test araçları | `extra-dev-tools（Geliştirme ve test araçları）.csv` | 1,811 |
| `misc` | Diğer | `extra-misc（Diğer）.csv` | 516 |

### Dosya listesi

```text
minecraft-glossary/
<lang>/                       # 14 dil klasörü
|   blocks（Bloklar）.csv
|   items（Eşyalar）.csv
|   entities（Varlıklar）.csv
|   biomes（Biyomlar）.csv
|   enchantments（Büyüler）.csv
|   effects（Durum etkileri）.csv
|   instruments（Enstrümanlar）.csv
|   materials（Zırh süsleme malzemeleri）.csv
|   paintings（Tablolar）.csv
|   attributes（Nitelikler）.csv
|   item-groups（Eşya grupları）.csv
|   jukebox-songs（Müzik kutusu şarkıları）.csv
|   trim-patterns（Zırh süsleme desenleri）.csv
|   colors（Renkler）.csv
|   statistics（İstatistikler）.csv
|   maps（Haritalar）.csv
|   music（Müzik）.csv
|   sound-categories（Ses kategorileri）.csv
|   game-modes（Oyun modları）.csv
|   +-- extra-               # sistem ve metin kategorileri
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

## Notlar

- **Kaynak ve hizalama.** Terimler Minecraft Java Edition'ın resmî dil dosyalarından çıkarılmıştır
  (`assets/minecraft/lang/tr_tr.json`, [misode/mcmeta](https://github.com/misode/mcmeta) üzerinden);
  yani resmî yerelleştirmedir. Her dosyada `target` Türkçe metni, `source` ise **diğer 13 dilden
  herhangi birindeki** karşılığı gösterir; aynı terim her kaynak dil için bir kez yer alır (aynı
  satırlar ve `source` = `target` olan satırlar birleştirilmiştir).

- **Dil etiketi.** `tgt_lng` her zaman `tr-TR` olup resmî `tr_tr` yerel ayarına karşılık gelir.

- **Kodlama.** Tüm CSV dosyaları **BOM'lu UTF-8**, satır sonları **CRLF** ve ilk satır başlıktır;
  virgül, tırnak veya satır sonu içeren alanlar RFC 4180'e göre kaçışlanmıştır. BOM ve CRLF sayesinde
  dosyalar Excel'de çift tıklamayla doğru açılır. Dikkat: bazı uzun metin alanları tırnak içinde satır
  sonu içerir (dil başına yaklaşık 2.000 alan); bu yüzden ham satır saymak yerine RFC 4180 uyumlu bir
  CSV ayrıştırıcı kullanın.

- **Bilinen sınırlamalar.** "Karşılık satırı sayısı" "terim sayısı" değildir — 34 kategorinin `entries`
  toplamı 8,559'dur; bu, resmî dil dosyalarında kategorilere atanan oyun adı nesnelerinin sayısıdır
  (o dilde çevrilmemiş kayıtlar dahil). Tam tanım, oyun kökündeki `../../README.md` dosyasının
  «Data Overview» bölümündedir. Satırların bir kısmı terim değil arayüz metnidir (GUI, çok oyunculu,
  Realms vb.). Resmî yerelleştirmede çevrilmemiş terimler satır üretmez. 14 dil klasörünün satır sayıları
  biraz farklıdır, çünkü her dilin çeviri kapsamı farklıdır.

- **Yeniden üretim.** `python tools/build_glossary.py` (oyun kökünden); betik harici bir veri dizinini
  okur. Önek–kategori eşlemesinin tamamı betikteki `CATEGORIES` tablosundadır.

## Yasal uyarı

Bu dizin, kişisel olarak derlenen ve sürdürülen **resmî olmayan** bir çeviri terim sözlüğüdür;
yalnızca kişisel öğrenme, araştırma ve yapay zekâ çeviri yazılımlarında terim eşleştirmeyi destekleme
amacı taşır. Oyunun geliştiricileri, yayıncıları, dağıtıcıları, operatörleri veya hak sahipleriyle
hiçbir bağlılık, yetkilendirme, iş birliği veya resmî temsil ilişkisi yoktur; buradaki terimler resmî
görüşü yansıtmaz ve hiçbir oyunun resmî terim sözlüğü sayılmamalıdır. Oyun adları, karakter adları ve
ticari markalar üzerindeki fikrî mülkiyet hakları ilgili hak sahiplerine aittir. Bu projenin ve ondan
üretilen çevirilerin kullanımından doğan tüm sorumluluk kullanıcıya aittir. Tam koşullar depo kökündeki
`README.md` / `README_EN.md` / `README_JP.md` dosyalarındadır.
