# 『ブルーアーカイブ』多言語用語集

## [中文](README.md) [English](README_EN.md)

**目標言語**ごとに独立したフォルダーに分割し、各フォルダー内では**分類**ごとにフラットな CSV ファイルを直接格納しています。

## データ製品

本ディレクトリは『ブルーアーカイブ』用語集のデータ製品コンテナで、以下の **6 種類の目標言語**を収録しています：

| 言語フォルダー | 言語 |
| --- | --- |
| `zh-CN/` | 簡体字中国語 |
| `zh-TW/` | 繁体字中国語 |
| `en-US/` | English |
| `ja-JP/` | 日本語 |
| `ko-KR/` | 한국어 |
| `th-TH/` | ภาษาไทย |

各言語フォルダー内の 15 分類の CSV はすべて**フラットに格納**し、分類サブディレクトリは設けません。ファイル名がそのまま分類名です。

## ディレクトリ構造

```text
blue-archive-glossary/
├── README.md
├── _master/
│   ├── zh-CN__all_glossary.csv      # その言語の全対照行を統合した総表
│   ├── zh-CN__all_terms.csv         # その言語の全語彙リスト
│   ├── zh-CN__index.csv             # 分類索引と件数
│   ├── zh-CN__README.md             # その言語ライブラリの既存の詳細説明
│   ├── zh-TW__...                   # 残り 5 言語も同じ命名
│   └── ...
├── zh-CN/
│   ├── README.md                    # 本言語ライブラリの説明
│   ├── character.csv                # 分類用語集（source,target,tgt_lng）
│   ├── character__terms.csv         # 本言語の語彙リスト（id,term,src_table）
│   └── ...                          # 全 15 分類、各分類 2 つの CSV
├── zh-TW/
├── en-US/
├── ja-JP/
├── ko-KR/
├── th-TH/
└── multilingual/                   # 六言語の並列総表、元のサブディレクトリ構造を保持
```

`_master/<lang>__<original-name>` は各言語の元 `00_master/` にあった索引・総表・説明を保存したものです。分類 CSV はすべて言語フォルダーの直下に移動済みで、元の `00_master/` は各言語ディレクトリ内には残していません。

## ファイル形式

分類用語集（`<category>.csv`）はすべて **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従い引用符でエスケープします。CSV 形式は 3 列で固定です：

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

意味：`tgt_lng` で指定された目標言語において、`target` は訳文、`source` は**他のいずれかの言語**の原文です。各言語フォルダー内では、同じ項目が残りの目標言語それぞれを `source` とする行として現れます（重複行と同形行は統合済み）。

`<category>__terms.csv` は本言語の語彙リストで、形式は `id,term,src_table`、校正と照合に用います。

## 分類

| 分類 | 用語集ファイル | 語彙リストファイル |
| --- | --- | --- |
| キャラクター名 | `character.csv` | `character__terms.csv` |
| 学校 | `school.csv` | `school__terms.csv` |
| サークル | `club.csv` | `club__terms.csv` |
| ストーリータイトル | `story_title.csv` | `story_title__terms.csv` |
| 愛用品 | `favor_item.csv` | `favor_item__terms.csv` |
| 地名 | `location.csv` | `location__terms.csv` |
| 用語 | `terminology.csv` | `terminology__terms.csv` |
| イベント | `event.csv` | `event__terms.csv` |
| ストーリーキャラクター | `scenario_character.csv` | `scenario_character__terms.csv` |
| 敵 | `enemy.csv` | `enemy__terms.csv` |
| スキル | `skill.csv` | `skill__terms.csv` |
| アイテム | `item.csv` | `item__terms.csv` |
| 装備 | `equipment.csv` | `equipment__terms.csv` |
| 家具 | `furniture.csv` | `furniture__terms.csv` |
| ステージ | `stage.csv` | `stage__terms.csv` |

## 言語別のファイル数とデータ行数

「ファイル数」はその言語フォルダー内の CSV ファイル数（15 分類の用語集 + 15 の語彙リスト）、「用語集データ行数」は 15 個の `<category>.csv` のデータ行合計、「語彙リストデータ行数」は 15 個の `<category>__terms.csv` のデータ行合計です。

| 言語 | ファイル数 | 用語集データ行数 | 語彙リストデータ行数 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 30 | 29463 | 7477 |
| `zh-TW` | 30 | 27453 | 6036 |
| `en-US` | 30 | 26623 | 5909 |
| `ja-JP` | 30 | 29216 | 7534 |
| `ko-KR` | 30 | 29009 | 7310 |
| `th-TH` | 30 | 26478 | 5908 |

## 生成と保守

本ディレクトリは `../tools/` 配下のスクリプトで再構築します：

```bash
python tools/build_glossary.py
```

スクリプトはゲームディレクトリの `tools/` にあり、既定で本データ製品を出力します。環境変数 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` で入力・出力ディレクトリを上書きできます。