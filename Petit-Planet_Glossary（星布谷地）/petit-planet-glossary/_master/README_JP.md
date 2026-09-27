# 『プチプラネット』用語集 — 言語別索引（`_master/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『プチプラネット』用語集 15 言語分の**分類索引**と、各言語ライブラリの既存の詳細説明を保存するものです。実際の用語データは `../zh-CN/`、`../en-US/` などの言語フォルダーにあります。

## ディレクトリ構造

```text
_master/
├── zh-CN__index.csv   # 簡体字中国語の分類索引と件数
├── zh-CN__README.md   # その言語ライブラリの既存の詳細説明
├── zh-TW__...         # 残り 14 言語も同じ命名
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── fr-FR__...
├── de-DE__...
├── es-ES__...
├── ru-RU__...
├── pt-PT__...
├── it-IT__...
├── tr-TR__...
├── th-TH__...
├── vi-VN__...
└── id-ID__...
```

15 言語 × 2 ファイル = **30 ファイル**。

## ファイル形式

| ファイル | 列 | 説明 |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | 分類索引。1 行 1 分類。ファイル内に **`TOTAL` 行はなく**、ヘッダーと分類行以外はありません |
| `<lang>__README.md` | — | その言語ライブラリの既存の詳細説明（そのまま保持） |

`__index.csv` の `term_count` はその分類の語彙数、`glossary_count` は対照行数です。`glossary_file` / `terms_file` は一つ上の `../<lang>/` にある対応 CSV のパスを示します。

## 言語別の規模

「データ行」は `<lang>__index.csv` の分類行数です。`en-US` は 18 分類、それ以外の言語は 7 分類のため、本ライブラリは言語ごとに規模が異なります。

| 言語 | 分類行数 | 語彙数合計 | 対照行合計 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 7 | 125 | 1363 |
| `zh-TW` | 7 | 123 | 1358 |
| `en-US` | 18 | 2073 | 3306 |
| `ja-JP` | 7 | 114 | 1303 |
| `ko-KR` | 7 | 114 | 1304 |
| `fr-FR` | 7 | 113 | 1298 |
| `de-DE` | 7 | 114 | 1311 |
| `es-ES` | 7 | 113 | 1298 |
| `ru-RU` | 7 | 112 | 1296 |
| `pt-PT` | 7 | 114 | 1308 |
| `it-IT` | 7 | 112 | 1296 |
| `tr-TR` | 7 | 113 | 1298 |
| `th-TH` | 7 | 114 | 1304 |
| `vi-VN` | 7 | 114 | 1304 |
| `id-ID` | 7 | 113 | 1298 |

## 説明

- すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。
- `en-US` の追加 11 分類（`03_item`、`04_material`、`05_furniture`、`07_cooking`、`08_fish`、`09_bugs`、`10_plants`、`11_shore`、`12_shop`、`13_neighbor_interaction`、`15_event`）は現在英語名のみで、公式の多言語対照がありません。
- 十五言語の並列総表は `../multilingual/`、ゲーム全体の説明は `../README.md` / `../README_EN.md` / `../README_JP.md` を参照してください。
