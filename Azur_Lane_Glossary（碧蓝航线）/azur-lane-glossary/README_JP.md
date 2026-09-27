# 『アズールレーン』多言語用語集（`azur-lane-glossary`）

## [中文](README.md) [English](README_EN.md)

本サブライブラリは、『アズールレーン』（Azur Lane）の**多言語対訳用語データ製品**です。**目標言語**ごとに独立したフォルダーに分割し、
各言語フォルダー内では**分類**ごとにフラットな CSV ファイルを格納しています。ほかにソースデータ、調和名の対照、ソース言語別に分割したビュー、取得元ディレクトリを収録しています。

## ディレクトリ構造

```text
azur-lane-glossary/
├── README.md
├── zh-CN/                        目標言語 = 簡体字中国語
│   ├── glossary.csv
│   ├── glossary-detailed.csv
│   ├── ship-characters.csv
│   ├── ship-characters-detailed.csv
│   ├── terms.csv
│   ├── terms-detailed.csv
│   ├── ambiguous.csv             （zh-CN のみ）
│   ├── ships-and-terms.csv       （zh-CN のみ）
│   ├── README.md
│   └── README_zh-CN.md           （本言語ディレクトリの簡体字中国語説明）
├── en-US/                        目標言語 = English（上記と同じ 6 分類 CSV + README.md / README_zh-CN.md）
├── ja-JP/                        目標言語 = 日本語（同上）
├── ko-KR/                        目標言語 = 한국어（同上）
├── harmonized/                   五言語総表、調和名と別称の対照、ソースデータ
├── by-language/                  ソース言語別に分割した艦船サブテーブル、`target` はすべて簡体字中国語
└── sources/                      萌娘百科の名称対照表の取得結果
```

## 目標言語

| 言語ディレクトリ | 言語 | `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | 簡体字中国語 | `zh-CN` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |

## 分類とファイル名

各目標言語ディレクトリはいずれも以下の**統一されたファイル名**を使用します。実際に存在する分類のみを残します。

| 分類 | ファイル名 | 説明 |
| --- | --- | --- |
| 艦船名（標準名） | `glossary.csv` | 3 列の主表 |
| 艦船名（標準名）詳細 | `glossary-detailed.csv` | 主表 + 艦船メタデータ |
| 艦船キャラクター名（調和名） | `ship-characters.csv` | 3 列の主表 |
| 艦船キャラクター名（調和名）詳細 | `ship-characters-detailed.csv` | 主表 + 艦船メタデータ |
| 航海 / 軍事 / ゲーム用語 | `terms.csv` | 3 列の主表 |
| 用語詳細 | `terms-detailed.csv` | 主表 + 分類と複数解 |
| 一語多解のソース語彙 | `ambiguous.csv` | `zh-CN` のみ |
| 艦船 + 用語の統合版 | `ships-and-terms.csv` | `zh-CN` のみ |

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）**、**CRLF** 改行、先頭行がヘッダーで、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従い引用符でエスケープします。

| ファイル群 | 実際のヘッダー |
| --- | --- |
| `glossary.csv` / `ship-characters.csv` / `terms.csv` / `ships-and-terms.csv` / `harmonized/equipment-harmonized.csv` / `harmonized/ship-names-harmonized.csv` / `by-language/glossary_*.csv` | `source,target,tgt_lng` |
| `glossary-detailed.csv`（`zh-CN`） | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant` |
| `glossary-detailed.csv`（`en-US` / `ja-JP` / `ko-KR`） | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `ship-characters-detailed.csv`（`zh-CN`） | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,zh_CN_standard,zh_CN_target,same_source_alternatives` |
| `ship-characters-detailed.csv`（`en-US` / `ja-JP` / `ko-KR`） | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `terms-detailed.csv` | `source,target,tgt_lng,src_lng,category,category_zh,same_source_alternatives` |
| `ambiguous.csv` | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,english_name,role` |
| `harmonized/harmonized-names-detailed.csv` | `source,target,tgt_lng,src_lng,name_code_id,kind,ship_type,ship_id,en,ja,zh_TW,wiki_note` |
| `harmonized/ijn-codename-aliases.csv` | `source,target,tgt_lng,src_lng,name_code_id` |
| `harmonized/ship-names-multilingual.csv` | `ship_id,zh_CN,en,ja,zh_TW,ko,english_name,ship_type_zh,ship_type_en,nation_zh,nation_en,variant` |

3 列の主表について：`tgt_lng` は目標言語を指定し、`target` はその言語の訳名、`source` は他言語の原文です。
同じソース文字列は同じ主表に 1 件の訳文だけを保持します。複数の読み方がある場合は、そのすべてを対応する詳細表の
`same_source_alternatives` 列に書き出し、`zh-CN` の一語多解のソース語彙は別途 `ambiguous.csv` に記載します。

## 実数

以下はいずれも今回の整理後にファイルから直接集計した結果です。

| 言語 | ファイル数 | データ行数 |
| --- | --- | --- |
| `zh-CN` | 8 | 19,855 |
| `en-US` | 6 | 12,600 |
| `ja-JP` | 6 | 15,519 |
| `ko-KR` | 6 | 15,511 |

| `zh-CN` ファイル | データ行数 | `target` 重複除去後の件数 |
| --- | --- | --- |
| `glossary.csv` | 3,514 | 877 |
| `glossary-detailed.csv` | 3,592 | 877 |
| `ship-characters.csv` | 3,804 | 875 |
| `ship-characters-detailed.csv` | 3,890 | 877 |
| `terms.csv` | 449 | 170 |
| `terms-detailed.csv` | 459 | 175 |
| `ambiguous.csv` | 162 | —（すべてソース文字列の複数解行） |
| `ships-and-terms.csv` | 3,985 | —（統合・重複除去表） |

`by-language/` は同一の艦船群の**ソース言語側ビュー**です：

| ファイル | データ行数 |
| --- | --- |
| `glossary_en-zh-CN.csv` | 1,544 |
| `glossary_ja-zh-CN.csv` | 696 |
| `glossary_ko-zh-CN.csv` | 814 |
| `glossary_zh-TW-zh-CN.csv` | 538 |

`harmonized/`：

| ファイル | データ行数 |
| --- | --- |
| `ship-names-multilingual.csv` | 891 |
| `ship-names-harmonized.csv` | 1,187 |
| `harmonized-names-detailed.csv` | 1,259 |
| `equipment-harmonized.csv` | 8 |
| `ijn-codename-aliases.csv` | 1,082 |

用語の 5 分類（`zh-CN/terms-detailed.csv` の `category` で集計）：

| `category` | テーマ | 対照行 |
| --- | --- | --- |
| `hull_type` | 艦種 | 97 |
| `naval_term` | 航海 / 軍事用語 | 198 |
| `navy_prefix` | 陣営と艦名の接頭辞 | 59 |
| `rank` | 軍階 | 44 |
| `game_term` | ゲーム用語 | 61 |

艦船のバリアント（`zh-CN/ship-characters-detailed.csv` の `variant` で集計）：

| バリアント | 対照行 |
| --- | --- |
| 本体（バリアント表記なし） | 3,466 |
| META | 280 |
| μ兵装 | 101 |
| II 型 | 43 |

## データソース

- 艦船名：公式 CN / EN / JP / KR / TW の 5 サーバーのクライアント設定（`ship_data_statistics.json`、
  `ship_data_template.json`、`ship_skin_template.json`、`ship_data_by_type.json`）。
- 調和名と一字代称：`name_code.json`。萌娘百科「碧蓝航线/名称对照表」でクロスチェック済みで、
  取得結果は `sources/moegirl_name_table.json` にあります。
- 用語：人手で整理し、各サーバーのクライアント設定と 1 件ずつ照合。データソースはルートディレクトリの `tools/terms_data.py`。

## 再生成

ゲームディレクトリでルートディレクトリ `tools/` のスクリプトを以下の順に実行します：

```bash
# 1) 艦船用語集（簡体字中国語の標準名）+ 五言語総表 + by-language + 曖昧表 + IJN 一字代称
python tools/build_glossary.py

# 2) 調和名対照表（1) が出力する五言語総表に依存）
python tools/build_harmonized.py

# 3) 艦船キャラクター用語表（簡体字中国語の調和名）
python tools/build_ship_character_glossary.py

# 4) 艦船の en-US / ja-JP / ko-KR 版（1) が出力する五言語総表に依存）
python tools/build_multilang_glossaries.py

# 5) 用語表の zh-CN / en-US / ja-JP / ko-KR 版（データは tools/terms_data.py）
python tools/build_terms_glossaries.py
```

スクリプト内の `BASE` / `OUT` パス定数はリポジトリ外の上流クライアント設定ディレクトリと生成作業ディレクトリを指すため、再実行前に本機の状況に合わせて調整する必要があります。
本リポジトリが保存しているのは生成結果のリリーススナップショットです。

## 使用のヒント

- CAT ツール（Trados、memoQ、Phrase など）や没入型翻訳系ソフトにインポートする際は、対応する目標言語ディレクトリの
  `glossary.csv`、`ship-characters.csv`、`terms.csv` を用語集として選ぶだけで済みます。
- 艦船メタデータが必要な場合は `*-detailed.csv` を使用します。`zh-CN` は `ships-and-terms.csv` で艦船と用語を一度にインポートできます。
- `by-language/` は原文言語でマッチング範囲を限定するのに適し、`harmonized/` は五言語対照と調和名の対応を取得するのに適します。