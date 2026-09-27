# 『ブルーアーカイブ』六言語並列総表（`multilingual/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『ブルーアーカイブ』用語集の全 **7535** 語を「1 語 1 行」で並べ、6 言語を横並びで表示するものです。言語間の比較や二次加工に便利です。単一の目標言語に分割した結果は、一つ上の `../zh-CN/`、`../en-US/` などの言語フォルダーにあります。

## ディレクトリ構造

```text
multilingual/
├── 00_master/
│   ├── all_terms_multilingual.csv   全 15 分類の六言語並列総表（7535 行）
│   └── README.md                    本説明
├── 01_character/                    01_character_multilingual.csv             408 行
├── 02_school/                       02_school_multilingual.csv                 26 行
├── 03_club/                         03_club_multilingual.csv                   43 行
├── 04_story_title/                  04_story_title_multilingual.csv          1144 行
├── 05_favor_item/                   05_favor_item_multilingual.csv             51 行
├── 06_location/                     06_location_multilingual.csv               90 行
├── 07_terminology/                  07_terminology_multilingual.csv          1402 行
├── 08_event/                        08_event_multilingual.csv                  72 行
├── 09_scenario_character/           09_scenario_character_multilingual.csv    945 行
├── 10_enemy/                        10_enemy_multilingual.csv                 351 行
├── 11_skill/                        11_skill_multilingual.csv                1069 行
├── 12_item/                         12_item_multilingual.csv                  649 行
├── 13_equipment/                    13_equipment_multilingual.csv             155 行
├── 14_furniture/                    14_furniture_multilingual.csv             472 行
└── 15_stage/                        15_stage_multilingual.csv                 658 行
```

## ファイル形式

総表と各分類ファイルは同じ列構成で、すべて **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。

| 列 | 説明 |
| --- | --- |
| `category` | 分類コード。例：`01_character` |
| `category_label` | 分類の中国語名 |
| `id` | 語彙 ID（公式データの Id / キー名に対応） |
| `zh-CN` | 簡体字中国語 |
| `ja-JP` | 日本語 |
| `zh-TW` | 繁体字中国語 |
| `en-US` | 英語 |
| `ko-KR` | 韓国語 |
| `th-TH` | タイ語 |
| `src_table` | その語彙の取得元テーブル |

## 分類別の件数

| 分類 | テーマ | 件数 |
| --- | --- | ---: |
| `01_character` | キャラクター名 | 408 |
| `02_school` | 学校 | 26 |
| `03_club` | サークル | 43 |
| `04_story_title` | ストーリータイトル | 1144 |
| `05_favor_item` | 愛用品 | 51 |
| `06_location` | 地名 | 90 |
| `07_terminology` | 用語 | 1402 |
| `08_event` | イベント | 72 |
| `09_scenario_character` | ストーリーキャラクター | 945 |
| `10_enemy` | 敵 | 351 |
| `11_skill` | スキル | 1069 |
| `12_item` | アイテム | 649 |
| `13_equipment` | 装備 | 155 |
| `14_furniture` | 家具 | 472 |
| `15_stage` | ステージ | 658 |
| **合計** | | **7535** |

## 説明

- 1 語 1 行で 6 言語を並べています。空欄は、その言語に対応する表記が見つからなかったことを示します。
- 特定の目標言語のみを使う場合は、一つ上の `../<lang>/` にある分類 CSV をそのまま利用してください。本ディレクトリから分割する必要はありません。
- 3 階層の説明：本ディレクトリ（六言語並列総表）、`../<lang>/`（単一言語用語集）、`../`（ゲーム全体の説明）。
