# 『プチプラネット』（星布谷地）多言語用語集

## [简体中文](README.md) [English](README_EN.md)

**対象言語**ごとに独立したフォルダへ分割し、各フォルダ内では**カテゴリ**ごとにファイルを分けて格納しています（**フラット構造**で、分類用のサブディレクトリはありません）。

## データ出典

- 公式ローカライズファイル：[planet.hoyoverse.com](https://planet.hoyoverse.com/zh-cn/home) 公式サイトの多言語ローカライズファイル
  —— 15 言語が**同一のローカライズキー**を使用しており（計 443 キー）、言語間でそのまま一対一に対応付けできます
- 公式お知らせ：HoYoLAB 公式お知らせ（`gids=10`）—— Coziness Test / Stardrift Test / Final Beta Test、これも 15 言語
- コミュニティデータベース：[petitplanet.life](https://petitplanet.life/) —— **英語名のみ**を提供し、`source = target`（いずれも英語）として記録。訳名の創作はしていません
- ニュース源の確認：[c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) —— 公式ニュース源（`Game.PLANET = 10`）の特定のみに使用。その言語フィールドはゲームのローカライズデータではありません

## ディレクトリ構造

```text
petit-planet-glossary/
├── zh-CN/                    # 対象言語 = 簡体字中国語（フラット：CSV は言語ディレクトリ直下）
├── zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/
├── ru-RU/  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
├── _master/                  # 各言語の index.csv と説明（<lang>__index.csv）
├── multilingual/             # 15 言語並列の総合表
└── README.md
```

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行はヘッダーで、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従って引用符でエスケープしています。

| source | target | tgt_lng |
| --- | --- | --- |
| Petit Planet | 星布谷地 | zh-CN |
| プチプラネット | 星布谷地 | zh-CN |

意味：`tgt_lng` で指定された対象言語において、`target` は訳文、`source` は**他のいずれかの言語**の原文です。
また各カテゴリには `*__terms.csv`（`id,term,src_table`）があり、`id` は追跡可能な公式ローカライズキーです。

## カテゴリ

`bugs`、`cooking`、`event`、`fish`、`furniture`、`game_title`、`item`、`location`、`material`、`neighbor`、`neighbor_interaction`、`plants`、`shop`、`shore`、`test_version`、`title_tag`、`ui`、`world_term`

## 言語と規模

| 言語フォルダ | 言語 | カテゴリ数 | 対照行 |
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
| **合計** | | | **25,326** |

## 既知の制限

- ゲームクライアントの多言語文字列はまだ公開されていないため、公式訳は公式サイトのローカライズファイルと公式お知らせに基づきます。公式サイトの文言は **Web Only** の階層に属する可能性があります。
- アイテム、家具、魚、昆虫、レシピ、ショップなどは現在 petitplanet.life の英語名のみで、公式の多言語対照がありません。
- 『プチプラネット』はまだテスト段階にあり、本データベースは現行バージョン（Final Beta Test、连接测试）に準拠しています。
