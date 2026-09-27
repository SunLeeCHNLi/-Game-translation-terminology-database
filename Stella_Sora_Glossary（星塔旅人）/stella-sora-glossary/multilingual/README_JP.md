# 『ステラソラ』五言語並列総表（`multilingual/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『ステラソラ』用語集の**五言語並列の元総表**です。全 **12292** 語を「1 語 1 行」で並べ、5 言語を横並びで表示します。言語間の比較や二次加工に便利です。単一の目標言語に分割した結果は、一つ上の `../zh-CN/`、`../en-US/` などの言語フォルダーにあります。

## ディレクトリ構造

```text
multilingual/
├── 00_master/
│   ├── index.csv                  分類索引と語彙数（15 分類 + 1 行の TOTAL）
│   ├── source_mapping.csv         取得元テーブル → 分類 の対応明細（219 行）
│   ├── StellaSora_all_terms.csv   全分類の統合総表（12292 行）
│   └── README.md                  本説明
├── 01_character/ … 15_terminology/   15 の分類ディレクトリ。各々 terms と glossary の 2 CSV を格納
└── StellaSora_Glossary.xlsx       同じデータの Excel ブック（16 ワークシート）
```

各分類ディレクトリには `NN_xxx_terms.csv`（多言語並列）と `NN_xxx_glossary.csv`（`source,target,tgt_lng` 対照表）の 2 ファイルがあります。

## ファイル形式

**1. `NN_xxx_terms.csv` — 多言語対照総表**

| id | zh-CN | en-US | ja-JP | ko-KR | zh-TW | src_table |
| --- | --- | --- | --- | --- | --- | --- |
| Character.103.1 | 琥珀 | Amber | コハク | 코하쿠 | 琥珀 | Character.json |

**2. `NN_xxx_glossary.csv` — 用語集（`source,target,tgt_lng`）**

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| 琥珀 | Amber | en-US |

**3. `00_master/StellaSora_all_terms.csv` — 統合総表**

| 列 | 説明 |
| --- | --- |
| `category` | 分類コード。例：`01_character` |
| `category_label` | 分類の中国語名 |
| `id` | 語彙 ID（ゲーム内の元テキストキー） |
| `zh-CN` | 簡体字中国語 |
| `en-US` | 英語 |
| `ja-JP` | 日本語 |
| `ko-KR` | 韓国語 |
| `zh-TW` | 繁体字中国語 |
| `src_table` | その語彙の取得元テーブル |

## 分類別の件数

| 分類 | テーマ | 語彙数 | 対照行数 |
| --- | --- | ---: | ---: |
| `01_character` | キャラクター名 | 287 | 3444 |
| `02_skill` | スキル名 | 628 | 7536 |
| `03_potential` | 潜在能力名 | 1457 | 17484 |
| `04_disc` | ディスク / Disc | 234 | 2808 |
| `05_item` | アイテム | 558 | 6696 |
| `06_equipment` | 装備 | 15 | 180 |
| `07_enemy` | 敵 | 399 | 4788 |
| `08_stage` | ステージ | 1019 | 12228 |
| `09_event` | イベント | 581 | 6972 |
| `10_system` | システム用語 | 1055 | 12660 |
| `11_ui` | UI 用語 | 4248 | 50934 |
| `12_story` | ストーリー固有名詞 | 527 | 6324 |
| `13_faction` | 陣営 | 21 | 252 |
| `14_location` | 地点 | 27 | 324 |
| `15_terminology` | ゲーム機制用語 | 1236 | 14832 |
| **合計** | | **12292** | **147462** |

## 説明

- すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。
- 語彙 ID は各言語で完全に一致しており、互いに公式訳です。人手による再翻訳は行っていません。`glossary` 表は `source/target/tgt_lng` に展開され、1 語あたり最大 12 行です。
- `StellaSora_Glossary.xlsx`、`00_master/index.csv`、`00_master/source_mapping.csv` は生成パイプライン外の一度限りの手順で作成したものです。
- ゲーム全体の説明は `../README.md` / `../README_EN.md` / `../README_JP.md`、言語別の説明は `../<lang>/README.md` を参照してください。
