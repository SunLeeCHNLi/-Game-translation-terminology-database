# 『キャットファンタジー』用語集 — 言語別索引（`_master/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『キャットファンタジー』用語集 7 言語分の**分類索引**と、各言語ライブラリの既存の詳細説明を保存するものです。実際の用語データは `../zh-CN/`、`../en-US/` などの言語フォルダーにあります。

## ディレクトリ構造

```text
_master/
├── zh-CN__index.csv   # 簡体字中国語の分類索引と件数
├── zh-CN__README.md   # その言語ライブラリの既存の詳細説明
├── zh-TW__...         # 残り 6 言語も同じ命名
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── th-TH__...
└── id-ID__...
```

7 言語 × 2 ファイル = **14 ファイル**。`<lang>` は `zh-CN`、`zh-TW`、`en-US`、`ja-JP`、`ko-KR`、`th-TH`、`id-ID` のいずれかです。

## ファイル形式

| ファイル | 列 | 説明 |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | 分類索引。16 分類の行 + 1 行の `TOTAL`、計 17 データ行 |
| `<lang>__README.md` | — | その言語ライブラリの既存の詳細説明（そのまま保持） |

`__index.csv` の `term_count` はその分類の語彙数、`glossary_count` は対照行数です。`glossary_file` / `terms_file` は一つ上の `../<lang>/` にある対応 CSV のファイル名を示します。

## 言語別の規模

「語彙数」は `TOTAL` 行の `term_count`、「対照行数」は `TOTAL` 行の `glossary_count` です。

| 言語 | 分類数 | 語彙数 | 対照行数 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 16 | 102213 | 196870 |
| `zh-TW` | 16 | 101915 | 196972 |
| `en-US` | 16 | 101692 | 197404 |
| `ja-JP` | 16 | 101621 | 196919 |
| `ko-KR` | 16 | 101760 | 197663 |
| `th-TH` | 16 | 99978 | 191726 |
| `id-ID` | 16 | 9916 | 28827 |

## 説明

- すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。
- `id-ID` の残り 15 分類のファイルはヘッダーのみでデータ行がありません。公式がインドネシア語を提供しているのはインターフェーステキストのみのためです。
- 七言語の並列総表は `../multilingual/`、ゲーム全体の説明は `../README.md` / `../README_EN.md` / `../README_JP.md` を参照してください。
