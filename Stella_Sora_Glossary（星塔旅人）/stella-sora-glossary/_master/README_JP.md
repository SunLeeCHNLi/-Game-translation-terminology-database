# 『ステラソラ』用語集 — 言語別総表（`_master/`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『ステラソラ』用語集 5 言語分の**元の総表・語彙リスト・分類索引**を保存するものです。言語フォルダー `../zh-CN/`、`../en-US/` などの上流スナップショットであり、CAT 用語集として直接インポートするものではありません。

## ディレクトリ構造

```text
_master/
├── zh-CN__all_glossary.csv   # 簡体字中国語の全対照行
├── zh-CN__all_terms.csv      # 簡体字中国語の全語彙リスト
├── zh-CN__index.csv          # 簡体字中国語の分類索引と件数
├── zh-CN__README.md          # その言語ライブラリの既存の詳細説明
├── zh-TW__...                # 残り 4 言語も同じ命名
├── en-US__...
├── ja-JP__...
└── ko-KR__...
```

5 言語 × 4 ファイル = **20 ファイル**。`<lang>` は `zh-CN`、`zh-TW`、`en-US`、`ja-JP`、`ko-KR` のいずれかです。

## ファイル形式

| ファイル | 列 | 説明 |
| --- | --- | --- |
| `<lang>__all_glossary.csv` | `category,source,target,tgt_lng` | その言語の 15 分類すべての対照行を統合した総表。`tgt_lng` はその言語で固定 |
| `<lang>__all_terms.csv` | `category,category_label,id,term,src_table` | その言語の全語彙リスト。`id` は追跡可能なテキストキー |
| `<lang>__index.csv` | `category,label,term_count,glossary_file,terms_file,target_language` | 分類索引。15 分類の行 + 1 行の `TOTAL` |
| `<lang>__README.md` | — | その言語ライブラリの既存の詳細説明（そのまま保持） |

## 言語別の規模

「語彙数」は `<lang>__all_terms.csv` のデータ行数、「対照行数」は `<lang>__all_glossary.csv` のデータ行数です。

| 言語 | 語彙数 | 対照行数 |
| --- | ---: | ---: |
| `zh-CN` | 12292 | 46279 |
| `zh-TW` | 12292 | 46052 |
| `en-US` | 12288 | 46032 |
| `ja-JP` | 12289 | 46426 |
| `ko-KR` | 12292 | 45950 |

## 説明

- すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーです。
- 5 言語の語彙数はほぼ一致しており、差異は `11_ui` 分類に現れます。対照行数が言語ごとに異なるのは、同じ語彙でも言語によって表記のバリエーション数が異なるためです。
- 五言語の並列総表は `../multilingual/`、ゲーム全体の説明は `../README.md` / `../README_EN.md` / `../README_JP.md` を参照してください。
