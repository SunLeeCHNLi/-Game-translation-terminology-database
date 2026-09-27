# 原神（Genshin Impact）多言語用語集 - 補助用語集

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは `genshin-glossary/` の**補助集**であり、主用語集に収録されていない項目（特に NPC、地名、敵、任務など）を補完するためのものです。

## データ出典

- [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)（en / ja / zh-CN / zh-TW の 4 言語を収録）

## 主用語集との関係

- **主用語集に存在しない** `source/target/tgt_lng` の組み合わせのみを含むため、主用語集と直接**重ねて使用**でき、重複項目は発生しません。
- 対象言語は 4 言語のみです：`zh-CN`、`zh-TW`、`en-US`、`ja-JP`。
- 出典が異なるため、同一項目の英/日/中の表記が主用語集と細かく異なる場合があります（用語や句読点など）。

## ディレクトリ構成

```
genshin-glossary-supplement/
├── zh-CN/
│   ├── characters.csv        # 主用語集と同名の主カテゴリ
│   ├── _variants.csv         # 別名/俗称/よくある誤記。追加の source として補完
│   └── extra/                # 主カテゴリ以外の、原神翻訳でよく使う追加カテゴリ
│       ├── quests.csv
│       └── ...
├── zh-TW/  en-US/  ja-JP/
└── （生成メタデータは同階層の ../tools/supplement_counts.json に移動済み）
```

> 本ディレクトリは同階層の `tools/build_supplement.mjs` によって生成されます。ビルドメタデータ（各言語・各カテゴリの行数統計）は
> 同階層の `tools/supplement_counts.json` に保存されており、本ディレクトリ内にはありません。

## ファイル形式

主用語集と完全に同一です（UTF-8（BOM 付き）、CRLF、RFC 4180 エスケープ）：

| source | target | tgt_lng |
| --- | --- | --- |
| Blackmarrow Lantern | 鸟髄孑灯 | zh-CN |
| 鳥髄の狐灯 | 鸟髄孑灯 | zh-CN |

## カテゴリ

### 主用語集に対応する主カテゴリ

| カテゴリ | 項目の出典 |
| --- | --- |
| artifacts | artifacts |
| characters | characters-*（モンド/璃月/稲妻/スメール/フォンテーヌ/ナタ/ナド・クライ/スネージナヤ/カーンルイア/ファデュイなど） |
| domains | domains |
| materials | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials |
| enemies | enemies |
| foods | foods |
| animals | living-beings |
| geographies | locations |
| weapons | weapons |

### 追加カテゴリ（`extra/`）

| カテゴリ | 説明 |
| --- | --- |
| extra/dialogue | セリフ用語 |
| extra/facilities | 施設と建築 |
| extra/objects | 情景オブジェクト |
| extra/organizations | 組織と勢力 |
| extra/quests | 任務名（魔神/世界/伝説/デイリー/部族など） |
| extra/sereniteapot | 塵歌壺 |
| extra/story | ストーリーと章節 |
| extra/system | システムと玩法の用語 |
| extra/events | イベント名 |
| extra/archives | アーカイブ資料 |

## 行数統計

| 言語 | 主カテゴリファイル | データ行数 | 別名行数 |
| --- | --- | --- | --- |
| `zh-CN` | 19 | 12,237 | 333 |
| `zh-TW` | 19 | 12,221 | 332 |
| `en-US` | 19 | 13,815 | 395 |
| `ja-JP` | 19 | 13,308 | 283 |

> 行数は重ね合わせ前の新規行数を指します。実際に使用する際は主用語集と統合するだけで構いません。
> 「主カテゴリファイル」＝ 主用語集と同名の主カテゴリ 9 個 ＋ `extra/` 以下の追加カテゴリ 10 個、合計 19 個の CSV、さらに `_variants.csv` が 1 個あります。

## 生成について

本ディレクトリは同階層の `tools/build_supplement.mjs` によって生成されます。このスクリプトは 2 つの入力を読み取ります：`xicri/genshin-langdata` のデータセット、
および**主用語集 `genshin-glossary/` で既に生成されたすべての CSV**（重複行の除去に使用）：

```bash
node tools/build_main_glossary.js   # 先に主用語集を生成
node tools/build_supplement.mjs     # 次に補助用語集を生成（前の手順の成果物に依存）
```

このスクリプトは出力ディレクトリに 4 つの言語フォルダと統計メタデータ `supplement_counts.json` を書き出します；
リポジトリ内に保存されている統計メタデータは `tools/supplement_counts.json` にあります。本 README の表は `tools/readme_sup.js` によって生成されます。