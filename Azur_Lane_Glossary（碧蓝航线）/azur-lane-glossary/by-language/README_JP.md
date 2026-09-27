# 『アズールレーン』原文言語別の用語サブテーブル（`by-language`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは『アズールレーン』（Azur Lane）艦船用語集の**原文言語側ビュー**です。同一の
艦船名テーブルを `src_lng`（原文言語）ごとに分割したもので、各ファイルの `target` は常に
**簡体字中国語（`zh-CN`）**の訳名です。`zh-CN/glossary.csv` を原文言語別にグループ化した版に
当たり、CAT ツールで**一致範囲を限定する**用途、すなわち 1 つの原文言語だけを一致対象にする
用途に使います。

## 構成

```text
by-language/
├── README.md                  本説明（簡体字中国語）
├── README_EN.md               英語説明
├── README_JP.md               日本語説明
├── glossary_en-zh-CN.csv      source = 英語の原名
├── glossary_ja-zh-CN.csv      source = 日本語の原名
├── glossary_ko-zh-CN.csv      source = 韓国語の原名
└── glossary_zh-TW-zh-CN.csv   source = 繁体字中国語の原名
```

## ファイル形式

すべてのファイルは **UTF-8（BOM 付き）**、**CRLF**、先頭行がヘッダーで、列構成は主テーブルと
完全に同一です。

```csv
source,target,tgt_lng
Abercrombie,阿贝克隆比,zh-CN
Abukuma,阿武隈,zh-CN
Acasta,阿卡司塔,zh-CN
```

| 列 | 意味 |
| --- | --- |
| `source` | その原文言語での艦船名（英語／日本語／韓国語／繁体字中国語） |
| `target` | 対応する簡体字中国語の訳名 |
| `tgt_lng` | 常に `zh-CN` |

## ファイル一覧

| ファイル | 原文言語 | データ行数 | `source` の重複除去後 | `target` の重複除去後 |
| --- | --- | ---: | ---: | ---: |
| `glossary_en-zh-CN.csv` | 英語 | 1,544 | 1,544 | 856 |
| `glossary_ja-zh-CN.csv` | 日本語 | 696 | 696 | 695 |
| `glossary_ko-zh-CN.csv` | 韓国語 | 814 | 814 | 811 |
| `glossary_zh-TW-zh-CN.csv` | 繁体字中国語 | 538 | 538 | 538 |

合計 **3,592** 行の対訳です。英語テーブルの `target` が重複除去後に 856 件しかないのは、
1 隻に複数の呼称がある事例が英語側に集中しているためです（複数の英語表記が 1 つの中国語名を
共有）。残り 3 つのテーブルはほぼ 1 対 1 で対応します。

## 注意事項

- 本ディレクトリは**艦船名のみ**を収録し、航海／軍事／ゲーム用語は含みません。用語は
  `../zh-CN/terms.csv` を参照してください。
- 4 つのサブテーブルは同一の艦船集合を**別の切り口で分割したもの**であり、`target` が互いに
  重複します。単純に結合して重複除去しないでください。
- すべての原文言語を一度に取り込む場合は、本ディレクトリではなく `../zh-CN/glossary.csv` を
  使用してください。
- 生成スクリプトは `tools/build_glossary.py`（出力定数 `SPLIT`）で、本ディレクトリはその
  出力の公開スナップショットです。