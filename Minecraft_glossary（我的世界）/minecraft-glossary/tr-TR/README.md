# 我的世界（Minecraft） terim sözlüğü — Türkçe (`tr-TR`)

[← Oyunun genel açıklamasına dön](../../README.md)

Bu dizin, **hedef dili Türkçe (`tr-TR`) olan** terim sözlüğüdür.
**34 CSV dosyasında** (34 kategori: 19'u dizin kökünde, 15'i `extra/` içinde) toplam
**101,665 karşılık satırı** bulunur; `tgt_lng` sütunu her zaman `tr-TR`, `source` sütunu ise diğer
13 dildeki yazımları içerir. Hedef çeviriler **Minecraft Java Edition'ın resmî dil dosyalarından**
alınmıştır; yeniden çeviri değildir.

## Dosyalar

- `<kategori>.csv` (19 dosya) — `source,target,tgt_lng` olmak üzere üç sütun; CAT ve terim yönetimi araçlarına doğrudan aktarılabilir
- `extra/<kategori>.csv` (15 dosya) — aynı üç sütun; sistem ve metin kategorileri için

## Kategoriler ve sayılar

| Kategori | Konu | Dosya | Satır |
| --- | --- | --- | --- |
| `blocks` | Bloklar | `blocks.csv` | 25,426 |
| `items` | Eşyalar | `items.csv` | 9,115 |
| `entities` | Varlıklar | `entities.csv` | 2,592 |
| `biomes` | Biyomlar | `biomes.csv` | 835 |
| `enchantments` | Büyüler | `enchantments.csv` | 553 |
| `effects` | Durum etkileri | `effects.csv` | 514 |
| `instruments` | Enstrümanlar | `instruments.csv` | 98 |
| `materials` | Süsleme malzemeleri | `materials.csv` | 143 |
| `paintings` | Tablolar | `paintings.csv` | 315 |
| `attributes` | Nitelikler | `attributes.csv` | 590 |
| `item-groups` | Eşya grupları | `item-groups.csv` | 198 |
| `jukebox-songs` | Müzik kutusu parçaları | `jukebox-songs.csv` | 42 |
| `trim-patterns` | Süsleme desenleri | `trim-patterns.csv` | 234 |
| `colors` | Renkler | `colors.csv` | 184 |
| `statistics` | İstatistikler | `statistics.csv` | 1,143 |
| `maps` | Haritalar | `maps.csv` | 422 |
| `music` | Müzik parçaları | `music.csv` | 192 |
| `sound-categories` | Ses kategorileri | `sound-categories.csv` | 133 |
| `game-modes` | Oyun modları | `game-modes.csv` | 77 |

### `extra/` (sistem ve metin)

| Kategori | Konu | Dosya | Satır |
| --- | --- | --- | --- |
| `subtitles` | Alt yazılar | `extra/subtitles.csv` | 12,431 |
| `death-messages` | Ölüm mesajları | `extra/death-messages.csv` | 1,354 |
| `advancement-titles` | Başarım adları | `extra/advancement-titles.csv` | 1,603 |
| `advancement-descriptions` | Başarım açıklamaları | `extra/advancement-descriptions.csv` | 1,650 |
| `gamerules` | Oyun kuralları | `extra/gamerules.csv` | 1,490 |
| `commands` | Komutlar ve argümanlar | `extra/commands.csv` | 10,765 |
| `gui` | Arayüz metinleri | `extra/gui.csv` | 6,751 |
| `options` | Ayarlar ve tuşlar | `extra/options.csv` | 8,174 |
| `multiplayer` | Çok oyunculu | `extra/multiplayer.csv` | 2,021 |
| `realms` | Realms | `extra/realms.csv` | 5,054 |
| `world-management` | Dünya yönetimi | `extra/world-management.csv` | 3,581 |
| `resource-packs` | Kaynak ve veri paketleri | `extra/resource-packs.csv` | 761 |
| `telemetry` | Telemetri | `extra/telemetry.csv` | 897 |
| `dev-tools` | Geliştirme ve test araçları | `extra/dev-tools.csv` | 1,811 |
| `misc` | Diğer | `extra/misc.csv` | 516 |

### Dosya listesi

```text
minecraft-glossary/
<lang>/                       # 14 dil klasörü
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
|   +-- extra/               # sistem ve metin kategorileri
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
