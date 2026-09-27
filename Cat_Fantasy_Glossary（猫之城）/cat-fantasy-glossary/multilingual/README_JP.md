# 『キャットファンタジー』七言語並列総表（`multilingual/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『キャットファンタジー』用語集の全 **102,213** 語を「1 語 1 行」で並べ、7 言語を横並びで表示するものです。全体検索や二次加工に便利です。単一の目標言語に分割した結果は、一つ上の `../zh-CN/`、`../en-US/` などの言語フォルダーにあります。

## ディレクトリ構造

```text
multilingual/
├── all_languages_master.csv   七言語並列総表（102213 データ行）
└── 00_master/
    ├── categories.csv         16 分類の定義（category,label,description）
    ├── source_mapping.csv     取得元テーブル → 分類 の対応と語彙数（379 テーブル）
    └── README.md              本説明
```

## ファイル形式

`all_languages_master.csv` は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。

| 列 | 説明 |
| --- | --- |
| `id` | 語彙 ID。形式は `取得元テーブル名.主キー.フィールド名` で、各言語の `*__terms.csv` の `id` と対応します |
| `category` | 所属分類（`00_master/categories.csv` を参照） |
| `src_table` | 公式データパッケージ内の取得元テーブルの相対パス |
| `zh-CN` | 簡体字中国語 |
| `zh-TW` | 繁体字中国語 |
| `en-US` | 英語 |
| `ja-JP` | 日本語 |
| `ko-KR` | 韓国語 |
| `th-TH` | タイ語 |
| `id-ID` | インドネシア語 |

## 補助ファイル

| ファイル | 列 | 説明 |
| --- | --- | --- |
| `00_master/categories.csv` | `category,label,description` | 16 分類のコード・名称・テーマ説明 |
| `00_master/source_mapping.csv` | `src_table,category,entry_count` | 379 の取得元テーブルと 16 分類の対応、および語彙数 |

## 説明

- 本表は各言語版の**上流総表**であり、各言語フォルダー内の `*_glossary.csv` はここから展開して生成されます。
- 英語が `en_UK` と `en_US` の 2 系統ある場合、総表は `en_US` を優先し、欠落時は `en_UK` にフォールバックします。`../en-US/` フォルダーと整合しています。
- 空欄は、その言語で当該語彙が欠落していることを示します。分類ごとに利用する場合は、`../<lang>/` のファイルをそのまま使ってください。
