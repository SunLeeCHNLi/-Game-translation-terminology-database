# 『アズールレーン』調和名対照と 5 言語艦船名総表（`harmonized`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは『アズールレーン』（Azur Lane）の**調和名（中国本土版で差し替えられた名称）の
対応関係**と**5 言語の艦船名総表**を保存します。いわゆる「調和名」とは、中国本土版クライアントが
一部の艦船原名を植物・動物系の代称に差し替えた後に表示する名称で、例として `峰风` → `樱`、
`吹雪` → `桐` があります。対応関係はゲームファイル `ShareCfg/name_code.json`
（`name` = 原名、`code` = 調和名）に由来し、萌娘百科「碧蓝航线/名称对照表」と突き合わせて検証済みです。

## 構成

```text
harmonized/
├── README.md                        本説明（簡体字中国語）
├── README_EN.md                     英語説明
├── README_JP.md                     日本語説明
├── ship-names-multilingual.csv      5 言語の艦船名総表（唯一の複数列ファイル）
├── ship-names-harmonized.csv        原名 → 調和名 の対応（3列）
├── harmonized-names-detailed.csv    メタデータ付きの詳細対応（12列）
├── equipment-harmonized.csv         装備の調和名対応（3列）
└── ijn-codename-aliases.csv         旧日本海軍の一文字代称・別称表（5列）
```

## ファイル一覧

| ファイル | データ行数 | 用途 |
| --- | ---: | --- |
| `ship-names-multilingual.csv` | 891 | 5 言語の総表。以降のすべての派生表の基準データ |
| `ship-names-harmonized.csv` | 1,187 | 艦船原名 → 調和名 のフラットな対応。一括置換に使用 |
| `harmonized-names-detailed.csv` | 1,259 | 原名 → 調和名 に言語／艦種／ID／多言語対照を付加 |
| `equipment-harmonized.csv` | 8 | 装備名の調和名対応 |
| `ijn-codename-aliases.csv` | 1,082 | 一文字代称・別称 → 正式訳名。照応解決に使用 |

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）**、**CRLF**、先頭行がヘッダーです。

| ファイル | 実際のヘッダー |
| --- | --- |
| `ship-names-multilingual.csv` | `ship_id,zh_CN,en,ja,zh_TW,ko,english_name,ship_type_zh,ship_type_en,nation_zh,nation_en,variant` |
| `ship-names-harmonized.csv` | `source,target,tgt_lng` |
| `harmonized-names-detailed.csv` | `source,target,tgt_lng,src_lng,name_code_id,kind,ship_type,ship_id,en,ja,zh_TW,wiki_note` |
| `equipment-harmonized.csv` | `source,target,tgt_lng` |
| `ijn-codename-aliases.csv` | `source,target,tgt_lng,src_lng,name_code_id` |

### 3 列表の読み方

`source,target,tgt_lng` 系（`ship-names-harmonized.csv`、`equipment-harmonized.csv`）では
`tgt_lng` は常に `zh-CN`、`source` がクライアントの原名、`target` が調和名です。

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| 峰风 | 樱 | zh-CN |
| 吹雪 | 桐 | zh-CN |
| Fubuki | 桐 | zh-CN |

### `harmonized-names-detailed.csv` の `kind` 分布

| `kind` | 行数 | 意味 |
| --- | ---: | --- |
| `ship` | 1,251 | 艦船 |
| `equipment` | 8 | 装備 |

`src_lng` 分布：`zh-CN` 436、`en` 255、`ko` 253、`ja` 172、`zh-TW` 143。
1 つの調和名が複数の原名に対応するため、1,259 行は 1,195 件の異なる `source` と 424 件の異なる
`target` にしか対応しません。

### `ijn-codename-aliases.csv`

`src_lng` 分布：`zh-CN` 434、`en` 383、`ja` 265。`name_code_id` は
`ShareCfg/name_code.json` の項目 ID を指し、一文字代称（例：「貃」）を正式な艦船名（例：「阿武隈」）に
結び付けます。

## 注意事項

- 調和名は**中国本土版クライアントが実際に表示する**テキストであり、訳者による書き換えではないため、
  簡体字中国語の公式訳名としてそのまま使用できます。
- 一部の艦船は艦種／陣営／改造などの次元で多態（META、μ兵装、II 型など）を持ち、`variant` 列が
  それを示します。
- 繁体字中国語はここでは `zh_TW`（アンダースコア）で、3 列表の `zh-TW`（ハイフン）とは表記が
  異なります。変換時に混同しないでください。
- 生成スクリプトは `tools/build_harmonized.py` で、`ship-names-multilingual.csv` などの上流成果物に
  依存します。