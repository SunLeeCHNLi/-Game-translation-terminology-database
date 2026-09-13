# Genshin Impact Terim Sözlüğü — Türkçe (`tr-TR`)

[← Oyunun genel açıklamasına dön](../../README.md) · [简体中文](README_zh-CN.md)

Bu dizin, *Genshin Impact* terminoloji sözlüğünün **hedef dili Türkçe (`tr-TR`) olan** bölümüdür: genel katalogda 27 kategorinin toplamı **8.186 terimdir** ve bunların **89.423 karşılık satırı** bu dile aittir. `tgt_lng` sütunu her zaman `tr-TR` değerini taşır; her satırda `source`, aynı terimin **diğer 13 dilden birindeki** yazımını, `target` ise Türkçe karşılığını içerir. Dosyalar **kategorilere** göre ayrılmıştır: her kategori için bir CSV.

## Dosyalar

- `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv` — 17 ana kategori dosyası
- `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv` — 10 TCG (Yedi Kutsal Çağrı) alt kategori dosyası

Toplam **27 CSV dosyası**. Tümü aynı üç sütunlu biçimdedir:

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | Alhaitham | tr-TR |
| Аль-Хайтам | Alhaitham | tr-TR |

Dizin yapısı:

```text
tr-TR/
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

## Kategoriler ve sayılar

**Terim**, o kategorinin 14 dilin tamamındaki benzersiz terim sayısıdır (her dilde aynıdır); **satır** ise bu dosyanın `tr-TR` için veri satırı sayısıdır.

### Ana kategoriler

| Kategori | Dosya | Terim | Satır |
| --- | --- | ---: | ---: |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2.823 |
| materials | `materials.csv` | 919 | 10.636 |
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
| achievements | `achievements.csv` | 1.548 | 19.463 |
| adventureranks | `adventureranks.csv` | 21 | 169 |
| **Ara toplam** | 17 dosya | — | **63.184** |

### TCG alt kategorileri (`TCG/`)

| Alt kategori | Dosya | Terim | Satır |
| --- | --- | ---: | ---: |
| action-cards | `TCG/action-cards.csv` | 927 | 9.592 |
| character-cards | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 | 1.114 |
| summons | `TCG/summons.csv` | 152 | 1.139 |
| status-effects | `TCG/status-effects.csv` | 1.159 | 11.204 |
| keywords | `TCG/keywords.csv` | 139 | 1.511 |
| card-backs | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards | `TCG/level-rewards.csv` | 26 | 169 |
| **Ara toplam** | 10 dosya | — | **26.239** |

**Bu dizinin toplamı: 27 dosya, 89.423 satır.**

## Notlar

- **Çeviri kaynağı ve hizalama.** Veriler [theBowja/genshin-db](https://github.com/theBowja/genshin-db) deposundan alınmıştır (veri sürümü 7.0, 14 dilin tamamı). Bunlar **oyunun resmî yerelleştirme metinleridir**; yeniden çeviri veya makine üretimi metin değildir. Hizalama terim düzeyindedir: bir oyun nesnesi, her kaynak dil için bir satır üretir; bu yüzden satır sayısı terim sayısından çok daha büyüktür.
- **Dil etiketleri.** Bu dizinde `tgt_lng` her zaman `tr-TR` olup hedef dili belirtir; `source` ise diğer 13 dilden (`zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `th-TH`, `vi-VN`) herhangi biri olabilir.
- **Kodlama.** Tüm CSV dosyaları **UTF-8 (BOM'lu)** kodlamada ve **CRLF** satır sonlarıyla kaydedilmiştir; ilk satır başlıktır ve virgül ya da tırnak içeren alanlar RFC 4180'e göre kaçışlanmıştır. Excel dosyaları doğrudan açabilir, kodlama ayarı gerekmez.
- **Bilinen sınırlar.** Kategori başına satır sayıları diller arasında küçük farklar gösterir (örneğin bazı `achievements` ve `adventureranks` kayıtları her dilde bulunmaz). Aynı terim birden fazla kategoride yer alabilir (örneğin bir silah adı `TCG` içinde de bulunur); bu nedenle dosya satırlarının toplamı benzersiz terim sayısından büyüktür. Resmî yerelleştirmede çevrilmemiş adlar özgün biçiminde kalır.
- **Tamamlayıcı sözlük.** Kardeş dizin `genshin-glossary-supplement/`, bu ana katalogda bulunmayan terimleri toplar ve bununla birlikte kullanılabilir; ayrıntılar o dizinin `README.md` dosyasındadır.

## Yasal uyarı

Bu dizin, tek bir kişi tarafından hazırlanıp bakımı yapılan **resmî olmayan** bir çeviri terminolojisi veri tabanıdır; yalnızca kişisel öğrenme, araştırma ve yapay zekâ çeviri yazılımlarının (Immersive Translate dâhil ancak bununla sınırlı olmamak üzere) terim eşleştirmesine yardımcı olmak için kullanılır. İlgili oyunların geliştiricileri, yayıncıları, dağıtıcıları, işletmecileri veya hak sahipleriyle hiçbir bağlılık, lisans, iş birliği, temsil veya resmî temsil ilişkisi yoktur; buradaki çeviriler resmî görüşü yansıtmaz ve her zaman doğru, eksiksiz ya da oyunun güncel sürümüyle uyumlu olduğu garanti edilmez — **bu materyal hiçbir oyunun resmî terim sözlüğü veya resmî yerelleştirme dosyası olarak görülmemelidir**. Oyun adları, karakter adları, özel terimler ve ticari markalar ilgili hak sahiplerine aittir. Kullanımdan doğan tüm sorumluluk kullanıcıya aittir.

Tam koşullar için depo kökündeki `README.md` / `README_EN.md` / `README_JP.md` dosyalarına bakın.

---

**Game-translation-terminology-database bağımsız bir kişisel projedir; bu oyunla, geliştiricileriyle, yayıncılarıyla, dağıtıcılarıyla veya hak sahipleriyle hiçbir bağlılık, yetkilendirme, iş birliği veya temsil ilişkisi içinde değildir.**
