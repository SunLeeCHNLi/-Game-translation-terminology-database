# 猫之城（Cat Fantasy）术语库 — 各语言索引（`_master/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《猫之城》七种语言术语库的**分类索引**，以及各语言语言库的原有详细说明。语言目录 `../zh-CN/`、`../en-US/` 等存放实际的术语数据。

## 目录结构

```text
_master/
├── zh-CN__index.csv    # 简体中文分类索引与条数
├── zh-CN__README.md    # 简体中文语言库的原有详细说明
├── zh-TW__...          # 其余 6 种语言使用相同命名
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── th-TH__...
└── id-ID__...
```

共 7 种语言 × 2 个文件 = **14 个文件**。`<lang>` 取值为 `zh-CN`、`zh-TW`、`en-US`、`ja-JP`、`ko-KR`、`th-TH`、`id-ID`。

## 文件格式

| 文件 | 列 | 说明 |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | 分类索引：16 个分类行 + 1 行 `TOTAL`，共 17 行数据 |
| `<lang>__README.md` | — | 该语言库的原有详细说明，保持原样 |

`__index.csv` 中的 `term_count` 为该分类词条数，`glossary_count` 为对照行数；`glossary_file` / `terms_file` 给出上一层 `../<lang>/` 中对应的 CSV 文件名。

## 各语言规模

「词条数」为 `TOTAL` 行的 `term_count`，「对照行数」为 `TOTAL` 行的 `glossary_count`。

| 语言 | 分类数 | 词条数 | 对照行数 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 16 | 102213 | 196870 |
| `zh-TW` | 16 | 101915 | 196972 |
| `en-US` | 16 | 101692 | 197404 |
| `ja-JP` | 16 | 101621 | 196919 |
| `ko-KR` | 16 | 101760 | 197663 |
| `th-TH` | 16 | 99978 | 191726 |
| `id-ID` | 16 | 9916 | 28827 |

## 说明

- 所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。
- `id-ID` 的其余 15 个类目文件保留表头、没有数据行，因为官方仅提供界面的印尼语。
- 七语并排总表见 `../multilingual/`，游戏级总说明见 `../README.md` / `../README_EN.md` / `../README_JP.md`。
