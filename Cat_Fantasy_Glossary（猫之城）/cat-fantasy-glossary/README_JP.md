# 『キャットファンタジー』多言語用語集

## [中文](README.md) [English](README_EN.md)

**目標言語**ごとに独立したフォルダーに分割し、各言語フォルダー内では**分類**ごとにフラットな CSV ファイルで格納しています。
`NN_xxx/` サブディレクトリは使用しません。

## データソース

- テキストの主ソース：[PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy)
  - `Setting/Data/`：公式多言語データテーブル。テキストキーで各言語を対応付け
  - `Setting/I18N/`：インターフェーステキストテーブル。Id で 7 言語を対応付け
- 構造確認：[Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1)（バージョン 2.18.1）
- 参考形式：本リポジトリの `Wuthering_Waves_glossary（鸣潮）/wuwa-glossary/` のフラットな多言語データ製品レイアウト

## ディレクトリ構造

```text
cat-fantasy-glossary/
├── README.md                     本説明
├── zh-CN/                       目標言語 = 簡体字中国語
│   ├── character.csv           用語対照表（source,target,tgt_lng）
│   ├── character__terms.csv    語彙リスト（id,term,src_table）
│   └── ...                      全 16 分類、32 の CSV
├── zh-TW/ ... id-ID/            全 7 言語フォルダー、構造は同一
├── _master/                     各言語の元の索引と説明
│   ├── zh-CN__index.csv         元名 00_master/index.csv
│   └── zh-CN__README.md         元名 00_master/README.md
└── multilingual/                七言語の並列総表（元 multilingual/、変更なし）
    ├── all_languages_master.csv 七言語の並列総表
    └── 00_master/               総表の説明、分類定義、出典マッピング
```

各言語フォルダーでは、`<category>.csv` は `source,target,tgt_lng` の 3 列の用語対照表、
`<category>__terms.csv` はその言語の `id,term,src_table` 語彙リストです。`_master/<lang>__index.csv`
はその言語の各分類の件数と対照行数を記録し、`_master/<lang>__README.md` は各言語の元の説明を保持します。

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。

| source | target | tgt_lng |
| --- | --- | --- |
| Asura | 非天 | zh-CN |
| アスラ | 非天 | zh-CN |

意味：`tgt_lng` で指定された目標言語において、`target` は訳文、`source` は他のいずれかの言語の原文です。
同じ項目は目標言語フォルダー内で、残りの利用可能な言語それぞれを `source` とする 1 行ずつとして現れます。

`<category>__terms.csv` は語彙リストで、列は `id,term,src_table`：`id` は
`ソーステーブル名.主キー.フィールド名` の形で、`src_table` は公式データパッケージ内の出典テーブルの相対パスです。

## 言語コード

| 言語フォルダー | 言語 | 目標言語タグ `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | 簡体字中国語 | `zh-CN` |
| `zh-TW` | 繁體中文 | `zh-TW` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |
| `th-TH` | ภาษาไทย | `th-TH` |
| `id-ID` | Bahasa Indonesia | `id-ID` |

## 分類とファイル名

| 分類 | 対照表ファイル | 語彙リストファイル | 説明 |
| --- | --- | --- | --- |
| キャラクターとカード | `character.csv` | `character__terms.csv` | 元 `01_character/` 分類 |
| スキルと戦闘効果 | `skill.csv` | `skill__terms.csv` | 元 `02_skill/` 分類 |
| 天賦と覚醒 | `talent.csv` | `talent__terms.csv` | 元 `03_talent/` 分類 |
| 装備と専用武器 | `equipment.csv` | `equipment__terms.csv` | 元 `04_equipment/` 分類 |
| アイテムと素材 | `item.csv` | `item__terms.csv` | 元 `05_item/` 分類 |
| 敵と BOSS | `enemy.csv` | `enemy__terms.csv` | 元 `06_enemy/` 分類 |
| ステージと章 | `stage.csv` | `stage__terms.csv` | 元 `07_stage/` 分類 |
| イベント玩法 | `event.csv` | `event__terms.csv` | 元 `08_event/` 分類 |
| ガチャと交換 | `gacha.csv` | `gacha__terms.csv` | 元 `09_gacha/` 分類 |
| ショップとパック | `shop.csv` | `shop__terms.csv` | 元 `10_shop/` 分類 |
| ホームと猫カフェ | `homeland.csv` | `homeland__terms.csv` | 元 `11_homeland/` 分類 |
| システムと任務 | `system.csv` | `system__terms.csv` | 元 `12_system/` 分類 |
| UI とインターフェーステキスト | `ui.csv` | `ui__terms.csv` | 元 `13_ui/` 分類 |
| ストーリー固有名詞 | `story.csv` | `story__terms.csv` | 元 `14_story/` 分類 |
| 地点と地域 | `location.csv` | `location__terms.csv` | 元 `15_location/` 分類 |
| ゲームメカニクス用語 | `terminology.csv` | `terminology__terms.csv` | 元 `16_terminology/` 分類 |

## 言語別データ量

以下の数値は今回の整理後のファイルから 1 行ずつ集計したものです。「語彙数」は `<category>__terms.csv` のデータ行合計、
「対照行数」は `<category>.csv` のデータ行合計です。

| 言語 | CSV ファイル数 | 語彙数 | 対照行数 | データ行合計 |
| --- | ---: | ---: | ---: | ---: |
| `zh-CN` | 32 | 102,213 | 196,870 | 299,083 |
| `zh-TW` | 32 | 101,915 | 196,972 | 298,887 |
| `en-US` | 32 | 101,692 | 197,404 | 299,096 |
| `ja-JP` | 32 | 101,621 | 196,919 | 298,540 |
| `ko-KR` | 32 | 101,760 | 197,663 | 299,423 |
| `th-TH` | 32 | 99,978 | 191,726 | 291,704 |
| `id-ID` | 32 | 9,916 | 28,827 | 38,743 |
| **合計** | **224** | **619,095** | **1,206,381** | **1,825,476** |

> 各言語フォルダーには 16 個の `<category>.csv` と 16 個の `<category>__terms.csv`、計 32 個の CSV が固定で入ります。
> `id-ID` の残り 15 分類のファイルはヘッダーのみを保持しデータ行はありません。公式がインドネシア語のインターフェーステキストしか提供していないためです。

## 再生成

本データ製品には **`tools/` ディレクトリも生成スクリプトもありません**。ディレクトリ整理とパス書き換えは一度きりの移動/リネームで行いました。
上流からデータを再生成するには、以下の流れを実装する必要があります：

```text
# 1. PackageInstaller/DataTable · game/CatFantasy から Setting/Data と Setting/I18N を取得する。
# 2. Setting/Data 内で _zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH 接尾辞を持つフィールドを走査し、
#    基準列（接尾辞なし）を zh-CN とする。出典テーブルごとに 16 分類へマッピングする。
# 3. Setting/I18N から Id で 7 言語を対応付け、ui 分類を生成する。
# 4. NewChapter のストーリーテーブルからはキャラクター名やシーン名などの固有名詞のみを抽出し、ストーリー本文の会話は収録しない。
# 5. (source, target) で重複除去し、原文と訳文が同一の場合は対照行を生成しない。
# 6. 結果を <lang>/<category>.csv と <lang>/<category>__terms.csv として書き出す。
#    いずれも UTF-8 BOM + CRLF。同時に _master/<lang>__index.csv を生成する。
```

上流出典テーブル → 分類のマッピングは `multilingual/00_master/source_mapping.csv`（379 テーブル）を参照してください。
分類定義は `multilingual/00_master/categories.csv`（16 分類）を参照してください。

## 使用のヒント

- CAT ツール（Trados、memoQ、Phrase など）や没入型翻訳系ソフトにインポートする際は、目標言語フォルダーの
  `<category>.csv` を選んでそのまま用語集としてインポートするだけで済みます。
- ファイル名がそのまま分類名なので、必要に応じて統合できます。領域ごとに分割してインポートする（例えば `character.csv` + `skill.csv` のみ）
  と、マッチング精度が大幅に向上します。
- `__terms.csv` は校正と出典テーブルの照合に用いるもので、CAT ツールに直接インポートする対照表ではありません。