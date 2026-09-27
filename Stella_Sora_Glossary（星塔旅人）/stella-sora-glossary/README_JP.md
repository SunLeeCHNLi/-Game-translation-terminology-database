# 『ステラソラ』（星塔旅人）単一言語用語集

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『ステラソラ』（Stella Sora / 星塔旅人）翻訳用語集のデータ製品 `stella-sora-glossary` であり、**対象言語**ごとに 5 つの独立したディレクトリに分割されています：`zh-CN`（簡体字中国語）、`zh-TW`（繁体字中国語）、`en-US`（English）、`ja-JP`（日本語）、`ko-KR`（한국어）。

各言語ディレクトリにある 15 の分類 CSV は、いずれも**言語ディレクトリ直下にフラットに配置**され、`NN_xxx/` サブディレクトリは使用しません。`<cat>.csv` は用語集で、形式は `source,target,tgt_lng`；`<cat>__terms.csv` はその言語の語句リストで、形式は `id,term,src_table` です。`_master/` には各言語の統合総合表・索引・既存の説明を保存し、`multilingual/` には 5 言語並列の原本総合表を保持しています。

## ディレクトリ構造

```text
stella-sora-glossary/
├── zh-CN/                    # 対象言語 = 簡体字中国語
│   ├── README.md
│   ├── character.csv
│   ├── character__terms.csv
│   └── ...                   # 計 15 組の分類 CSV
├── zh-TW/
├── en-US/
├── ja-JP/
├── ko-KR/
├── _master/
│   ├── zh-CN__all_glossary.csv
│   ├── zh-CN__all_terms.csv
│   ├── zh-CN__index.csv
│   └── ...
└── multilingual/             # 5 言語並列の原本総合表。内部構造は変更しません
```

## ファイル形式

単一言語の分類 CSV は、以下の固定 3 列のヘッダーを使用します：

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| コハク | 琥珀 | zh-CN |

`<cat>.csv` のファイルエンコードは **UTF-8 BOM**、改行は **CRLF** です。`target` は `tgt_lng` で指定された言語の訳文、`source` は他の言語の原文です。`<cat>__terms.csv` は `id,term,src_table` でその言語の語句リストを記録します。

## 分類と数量

| 分類 | ファイル | 説明 |
| --- | --- | --- |
| キャラクター名 | `character.csv` | Character names |
| スキル名 | `skill.csv` | Skills |
| 潜在能力名 | `potential.csv` | Potentials |
| ディスク | `disc.csv` | Discs |
| アイテム | `item.csv` | Items |
| 装備 | `equipment.csv` | Equipment |
| 敵 | `enemy.csv` | Enemies |
| ステージ | `stage.csv` | Stages |
| イベント | `event.csv` | Events |
| システム用語 | `system.csv` | System terms |
| UI 用語 | `ui.csv` | UI wording |
| ストーリー固有名詞 | `story.csv` | Story proper nouns |
| 勢力 | `faction.csv` | Factions |
| 地名 | `location.csv` | Locations |
| ゲームシステム用語 | `terminology.csv` | Gameplay mechanics |

### 言語別ファイルとデータ行数

| 言語 | 分類用語集ファイル数 | 分類語句リストファイル数 | 用語集データ行数 | 語句リストデータ行数 |
| --- | ---: | ---: | ---: | ---: |
| `zh-CN` | 15 | 15 | 46,279 | 12,292 |
| `zh-TW` | 15 | 15 | 46,052 | 12,292 |
| `en-US` | 15 | 15 | 46,032 | 12,288 |
| `ja-JP` | 15 | 15 | 46,426 | 12,289 |
| `ko-KR` | 15 | 15 | 45,950 | 12,292 |

### 分類 × 言語別の用語集データ行数

| 分類 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 979 | 977 | 973 | 1021 | 968 |
| `skill.csv` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `potential.csv` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `disc.csv` | 893 | 896 | 896 | 893 | 893 |
| `item.csv` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `equipment.csv` | 58 | 58 | 58 | 58 | 58 |
| `enemy.csv` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `stage.csv` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `event.csv` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `system.csv` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `ui.csv` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `story.csv` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `faction.csv` | 81 | 78 | 78 | 78 | 78 |
| `location.csv` | 98 | 98 | 98 | 96 | 96 |
| `terminology.csv` | 4660 | 4637 | 4630 | 4661 | 4649 |

## 再生成

本ディレクトリのデータは `../tools/` 配下のスクリプトで再生成します：

```bash
python ../tools/build_glossary.py
python ../tools/split_by_language.py
```

`build_glossary.py` は上流の多言語テキストライブラリから 5 言語並列の総合表を生成し、`split_by_language.py` は対象言語ごとに分割して各言語の分類 CSV を生成します。具体的な外部入力パスとスクリプトの動作は、ゲームルートの `README.md` / `README_EN.md` / `README_JP.md` を参照してください。
