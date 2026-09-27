# 『原神』多言語用語集

## [中文](README.md) [English](README_EN.md)

**目標言語**ごとに独立したフォルダーに分割し、各フォルダー内では**分類**ごとにファイルを分けて格納しています。

## データソース

- メイン用語集：[theBowja/genshin-db](https://github.com/theBowja/genshin-db)（データバージョン 7.0、全 14 言語を収録）
- 補完用語集：同階層の `genshin-glossary-supplement/` を参照（出典 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)、zh-CN / zh-TW / en-US / ja-JP を収録）

## ディレクトリ構造

```
genshin-glossary/
├── zh-CN/                    # 目標言語 = 簡体字中国語
│   ├── characters.csv
│   ├── talents.csv
│   ├── ...
│   └── TCG/                  # TCG 分類はサブタイプごとに細分
│       ├── action-cards.csv
│       └── ...
├── zh-TW/
├── en-US/ ... vi-VN/         # 全 14 言語フォルダー
└── （生成メタデータは同階層の ../tools/glossary_counts.json に移動済み）
```

> 本ディレクトリは同階層の `tools/build_main_glossary.js` が生成し、ビルドメタデータ（各言語・各分類の項目数と行数の統計）
> は同階層の `tools/glossary_counts.json` に保存され、本ディレクトリ内にはありません。

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従い引用符でエスケープします。

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | 艾尔海森 | zh-CN |
| Alhaitham | 艾尔海森 | zh-CN |

意味：`tgt_lng` で指定された目標言語において、`target` は訳文、`source` は**他のいずれかの言語**の原文です。
つまり各言語フォルダー内では、同じ項目が残りの 13 言語それぞれを `source` とする 1 行ずつとして現れます（重複行と同形行は統合済み）。

## 言語コード

| 言語フォルダー | 言語 | genshin-db 内部名 |
| --- | --- | --- |
| `zh-CN` | 簡体字中国語 | ChineseSimplified |
| `zh-TW` | 繁體中文 | ChineseTraditional |
| `en-US` | English | English |
| `ja-JP` | 日本語 | Japanese |
| `ko-KR` | 한국어 | Korean |
| `fr-FR` | Français | French |
| `de-DE` | Deutsch | German |
| `es-ES` | Español | Spanish |
| `ru-RU` | Русский | Russian |
| `pt-BR` | Português | Portuguese |
| `it-IT` | Italiano | Italian |
| `tr-TR` | Türkçe | Turkish |
| `th-TH` | ภาษาไทย | Thai |
| `vi-VN` | Tiếng Việt | Vietnamese |

## 分類と項目数

「項目」とはその分類下の**重複を除いた語彙数**（1 語彙 = ゲーム内の 1 つの名称オブジェクト）を指します。「行数」は各言語フォルダー内のその分類 CSV のデータ行数です。

### メイン分類

| 分類 | ファイル | 語彙数 | 言語あたりの行数（約） |
| --- | --- | --- | --- |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2,823 |
| materials | `materials.csv` | 919 | 10,637 |
| foods | `foods.csv` | 398 | 4,541 |
| crafts | `crafts.csv` | 295 | 3,522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3,636 |
| enemies | `enemies.csv` | 346 | 4,104 |
| animals | `animals.csv` | 223 | 2,647 |
| outfits | `outfits.csv` | 150 | 1,869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3,606 |
| geographies | `geographies.csv` | 268 | 3,389 |
| achievements | `achievements.csv` | 1,548 | 19,463 |
| adventureranks | `adventureranks.csv` | 21 | 158 |
| TCG | `TCG/*.csv` | 2,743 | 26,304 |

### TCG サブ分類

| サブ分類 | ファイル | 語彙数 |
| --- | --- | --- |
| action-cards | `TCG/action-cards.csv` | 927 |
| character-cards | `TCG/character-cards.csv` | 149 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 |
| summons | `TCG/summons.csv` | 152 |
| status-effects | `TCG/status-effects.csv` | 1,159 |
| keywords | `TCG/keywords.csv` | 139 |
| card-backs | `TCG/card-backs.csv` | 39 |
| card-boxes | `TCG/card-boxes.csv` | 7 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 |
| level-rewards | `TCG/level-rewards.csv` | 26 |

## 言語別の総行数

| 言語 | ファイル数 | データ行数 |
| --- | --- | --- |
| `zh-CN` | 27 | 89,790 |
| `zh-TW` | 27 | 89,434 |
| `en-US` | 27 | 89,412 |
| `ja-JP` | 27 | 89,490 |
| `ko-KR` | 27 | 89,460 |
| `fr-FR` | 27 | 89,613 |
| `de-DE` | 27 | 89,362 |
| `es-ES` | 27 | 89,411 |
| `ru-RU` | 27 | 89,418 |
| `pt-BR` | 27 | 89,444 |
| `it-IT` | 27 | 89,437 |
| `tr-TR` | 27 | 89,423 |
| `th-TH` | 27 | 89,468 |
| `vi-VN` | 27 | 89,530 |
| **合計** | **378** | **1,252,692** |

> 分類をまたいで同名の語彙が存在する場合があります（例えばある武器名が `weapons` と `TCG` の両方に現れる）。そのため各ファイルの行数を合計すると、全体で重複を除いた語彙数より多くなりますが正常です。全体で一意な `source/target/tgt_lng` の組み合わせ数は 1,069,738 です。

## データクリーニングの説明

ソースデータ内の以下のマークは生成時に処理済みです：

| ソースでの表記 | 処理方法 | 例 |
| --- | --- | --- |
| `{M#...}{F#...}` が隣接する性別バリアント | 男性形を採用 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 単独の `{M#…}` / `{F#…}` | その内容を採用 | `#Искатель{F#ница}` → `Искательница` |
| 名称先頭の `#`（性別関連マーク） | 除去 | `#Éclaireuse 100%` → `Éclaireuse 100%` |
| `{NON_BREAK_SPACE}`、`{SPACE}` | 通常の空白に置換 | `PB{NON_BREAK_SPACE}-{NON_BREAK_SPACE}Retorno` → `PB - Retorno` |
| その他のプレースホルダー（そのまま保持） | `{NICKNAME}`、`{REALNAME[…]} `、`{MATEAVATAR#SEXPRO[…]} ` | 各 1 件のみ |

同名同訳文の重複行（例えば英/仏/独で同形の人名）は統合済みです。

## 使用のヒント

- CAT ツール（Trados、memoQ、Phrase など）にインポートする際は、対応する目標言語の CSV を選んでそのまま用語集としてインポートするだけで済みます。
- ファイル名がそのまま分類名なので、必要に応じて統合できます。「全分類を 1 ファイルに統合」したい場合や `src_lng`（ソース言語）列を追加したい場合は、いつでも生成できます。

## 生成の説明

本ディレクトリは同階層の `tools/build_main_glossary.js` が [genshin-db](https://github.com/theBowja/genshin-db) のソースから生成します：

```bash
node tools/build_main_glossary.js
```

このスクリプトは出力ディレクトリに全 14 言語フォルダー、27 個の CSV、および統計メタデータ `glossary_counts.json` を書き出します。
リポジトリ内に保存されている統計メタデータは `tools/glossary_counts.json` にあります。本 README の表は `tools/readme_main.js` が生成します。