# 星布谷地（Petit Planet）术语库 — 各语言索引（`_master/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《星布谷地》十五种语言术语库的**分类索引**，以及各语言语言库的原有详细说明。语言目录 `../zh-CN/`、`../en-US/` 等存放实际的术语数据。

## 目录结构

```text
_master/
├── zh-CN__index.csv   # 简体中文分类索引与条数
├── zh-CN__README.md   # 简体中文语言库的原有详细说明
├── zh-TW__...         # 其余 14 种语言使用相同命名
├── en-US__...
├── ja-JP__...
├── ko-KR__...
├── fr-FR__...
├── de-DE__...
├── es-ES__...
├── ru-RU__...
├── pt-PT__...
├── it-IT__...
├── tr-TR__...
├── th-TH__...
├── vi-VN__...
└── id-ID__...
```

共 15 种语言 × 2 个文件 = **30 个文件**。

## 文件格式

| 文件 | 列 | 说明 |
| --- | --- | --- |
| `<lang>__index.csv` | `category,label,term_count,glossary_count,glossary_file,terms_file,target_language` | 分类索引，每行一个分类；文件内**没有 `TOTAL` 行**，也没有表头之外的空行 |
| `<lang>__README.md` | — | 该语言库的原有详细说明，保持原样 |

`__index.csv` 中的 `term_count` 为该分类词条数，`glossary_count` 为对照行数；`glossary_file` / `terms_file` 给出上一层 `../<lang>/` 中对应的 CSV 路径。

## 各语言规模

「数据行」为 `<lang>__index.csv` 的分类行数。`en-US` 收录 18 个分类，其余语言各收录 7 个分类，因此本库各语言规模并不一致。

| 语言 | 分类行数 | 词条数合计 | 对照行合计 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 7 | 125 | 1363 |
| `zh-TW` | 7 | 123 | 1358 |
| `en-US` | 18 | 2073 | 3306 |
| `ja-JP` | 7 | 114 | 1303 |
| `ko-KR` | 7 | 114 | 1304 |
| `fr-FR` | 7 | 113 | 1298 |
| `de-DE` | 7 | 114 | 1311 |
| `es-ES` | 7 | 113 | 1298 |
| `ru-RU` | 7 | 112 | 1296 |
| `pt-PT` | 7 | 114 | 1308 |
| `it-IT` | 7 | 112 | 1296 |
| `tr-TR` | 7 | 113 | 1298 |
| `th-TH` | 7 | 114 | 1304 |
| `vi-VN` | 7 | 114 | 1304 |
| `id-ID` | 7 | 113 | 1298 |

## 说明

- 所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。
- `en-US` 的额外 11 个分类（`03_item`、`04_material`、`05_furniture`、`07_cooking`、`08_fish`、`09_bugs`、`10_plants`、`11_shore`、`12_shop`、`13_neighbor_interaction`、`15_event`）目前只有英文名称，缺少官方多语言对照。
- 十五语并排总表见 `../multilingual/`，游戏级总说明见 `../README.md` / `../README_EN.md` / `../README_JP.md`。
