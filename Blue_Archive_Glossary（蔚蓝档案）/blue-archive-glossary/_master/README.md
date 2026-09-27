# 蔚蓝档案（Blue Archive）术语库 — 各语言总表（`_master/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《蔚蓝档案》六种语言术语库的**原始总表、词条清单与分类索引**，是语言目录 `../zh-CN/`、`../en-US/` 等的上游快照，不直接作为 CAT 术语库导入。

## 目录结构

```text
_master/
├── zh-CN__all_glossary.csv   # 简体中文全部对照行
├── zh-CN__all_terms.csv      # 简体中文全部词条清单
├── zh-CN__index.csv          # 简体中文分类索引与条数
├── zh-CN__README.md          # 简体中文语言库的原有详细说明
├── zh-TW__...                # 其余 5 种语言使用相同命名
├── en-US__...
├── ja-JP__...
├── ko-KR__...
└── th-TH__...
```

共 6 种语言 × 4 个文件 = **24 个文件**。`<lang>` 取值为 `zh-CN`、`zh-TW`、`en-US`、`ja-JP`、`ko-KR`、`th-TH`。

## 文件格式

| 文件 | 列 | 说明 |
| --- | --- | --- |
| `<lang>__all_glossary.csv` | `category,source,target,tgt_lng` | 该语言全部 15 个分类的对照行合并总表，`tgt_lng` 固定为该语言 |
| `<lang>__all_terms.csv` | `category,category_label,id,term,src_table` | 该语言全部词条清单，`id` 为可溯源文本键 |
| `<lang>__index.csv` | `category,label,term_count,glossary_file,terms_file,target_language` | 分类索引，15 个分类行 + 1 行 `TOTAL` |
| `<lang>__README.md` | — | 该语言库的原有详细说明，保持原样 |

## 各语言规模

「词条数」为 `<lang>__all_terms.csv` 的数据行数；「对照行数」为 `<lang>__all_glossary.csv` 的数据行数。

| 语言 | 词条数 | 对照行数 |
| --- | ---: | ---: |
| `zh-CN` | 7477 | 29463 |
| `zh-TW` | 6036 | 27453 |
| `en-US` | 5909 | 26623 |
| `ja-JP` | 7534 | 29216 |
| `ko-KR` | 7310 | 29009 |
| `th-TH` | 5908 | 26478 |

## 说明

- 所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。
- 各语言目录 `../<lang>/` 下的分类 CSV 由本目录的总表展开生成；本目录保留原始索引与说明以便回查。
- 六语并排总表见 `../multilingual/`，游戏级总说明见 `../README.md` / `../README_EN.md` / `../README_JP.md`。
