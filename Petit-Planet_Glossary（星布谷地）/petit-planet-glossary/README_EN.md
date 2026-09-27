# Petit Planet (星布谷地) Multilingual Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

Split into independent folders by **target language**; within each folder, files are stored by **category** (**flat structure**, no more category subdirectories).

## Data Sources

- Official localization files: [planet.hoyoverse.com](https://planet.hoyoverse.com/zh-cn/home) official website multilingual localization files
  —— all 15 languages use the **same localization keys** (443 keys in total), so the languages can be aligned directly one-to-one
- Official announcements: HoYoLAB official announcements (`gids=10`) —— Coziness Test / Stardrift Test / Final Beta Test, likewise in 15 languages
- Community database: [petitplanet.life](https://petitplanet.life/) —— provides **English names only**, recorded as `source = target` (both English), with no invented translations
- News source confirmation: [c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) —— used only to locate the official news source (`Game.PLANET = 10`); its language field is not game localization data

## Directory Structure

```text
petit-planet-glossary/
├── zh-CN/                    # target language = Simplified Chinese (flat: CSVs sit directly in the language directory)
├── zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/
├── ru-RU/  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
├── _master/                  # per-language index.csv and notes (<lang>__index.csv)
├── multilingual/             # all fifteen languages side by side
└── README.md
```

## File Format

All CSVs are **UTF-8 (with BOM)** encoded, use **CRLF** line endings and a header row, and escape fields containing commas or quotation marks with quotes per RFC 4180.

| source | target | tgt_lng |
| --- | --- | --- |
| Petit Planet | 星布谷地 | zh-CN |
| プチプラネット | 星布谷地 | zh-CN |

Meaning: for the target language specified by `tgt_lng`, `target` is the translation and `source` is the original text in **some other language**.
Each category also has a `*__terms.csv` (`id,term,src_table`), where `id` is a traceable official localization key.

## Categories

`bugs`, `cooking`, `event`, `fish`, `furniture`, `game_title`, `item`, `location`, `material`, `neighbor`, `neighbor_interaction`, `plants`, `shop`, `shore`, `test_version`, `title_tag`, `ui`, `world_term`

## Languages and Scale

| Language folder | Language | Categories | Alignment rows |
| --- | --- | ---: | ---: |
| `zh-CN` | 简体中文 | 7 | 1,488 |
| `zh-TW` | 繁體中文 | 7 | 1,481 |
| `en-US` | English | 18 | 5,379 |
| `ja-JP` | 日本語 | 7 | 1,417 |
| `ko-KR` | 한국어 | 7 | 1,418 |
| `fr-FR` | Français | 7 | 1,411 |
| `de-DE` | Deutsch | 7 | 1,425 |
| `es-ES` | Español | 7 | 1,411 |
| `ru-RU` | Русский | 7 | 1,408 |
| `pt-PT` | Português | 7 | 1,422 |
| `it-IT` | Italiano | 7 | 1,408 |
| `tr-TR` | Türkçe | 7 | 1,411 |
| `th-TH` | ภาษาไทย | 7 | 1,418 |
| `vi-VN` | Tiếng Việt | 7 | 1,418 |
| `id-ID` | Bahasa Indonesia | 7 | 1,411 |
| **Total** | | | **25,326** |

## Known Limitations

- The game client's multilingual strings are not yet public, so the official translations come from the official website localization files and official announcements; the official website wording may belong to a **Web Only** layer.
- Items, furniture, fish, insects, recipes, shops and the like currently have only the English names from petitplanet.life and lack an official multilingual mapping.
- *Petit Planet* is still in testing, and this database follows the current version (Final Beta Test, 连接测试).
