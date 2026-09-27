# 星塔旅人（Stella Sora）术语库 — 各语言总表（`_master/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《星塔旅人》五种语言术语库的**原始总表、词条清单与分类索引**，是语言目录 `../zh-CN/`、`../en-US/` 等的上游快照，不直接作为 CAT 术语库导入。

## 目录结构

```text
_master/
├── zh-CN__all_glossary.csv   # 简体中文全部对照行
├── zh-CN__all_terms.csv      # 简体中文全部词条清单
├── zh-CN__index.csv          # 简体中文分类索引与条数
├── zh-CN__README.md          # 简体中文语言库的原有详细说明
├── zh-TW__...                # 其余 4 种语言使用相同命名
├── en-US__...
├── ja-JP__...
└── ko-KR__...
```

共 5 种语言 × 4 个文件 = **20 个文件**。`<lang>` 取值为 `zh-CN`、`zh-TW`、`en-US`、`ja-JP`、`ko-KR`。

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
| `zh-CN` | 12292 | 46279 |
| `zh-TW` | 12292 | 46052 |
| `en-US` | 12288 | 46032 |
| `ja-JP` | 12289 | 46426 |
| `ko-KR` | 12292 | 45950 |

## 说明

- 所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。
- 五种语言的词条数基本一致，差异出现在 `11_ui` 分类；各语言对照行数不同的原因是同一词条在不同语言下的写法数量不等。
- 五语并排总表见 `../multilingual/`，游戏级总说明见 `../README.md` / `../README_EN.md` / `../README_JP.md`。
