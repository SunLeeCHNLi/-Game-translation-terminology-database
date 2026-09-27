# 《碧蓝航线》按源语言拆分的术语子表（`by-language`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录是《碧蓝航线》（Azur Lane）舰船术语库的**源语言侧视图**：把同一个舰船名称表按
`src_lng`（原文语言）拆成多份子表，所有文件的 `target` 一律为**简体中文（`zh-CN`）**译名。
它等价于 `zh-CN/glossary.csv` 的按原文语言分组版本，用于在 CAT 工具中**限定匹配范围**——
只让某一种语言的原文参与匹配。

## 目录结构

```text
by-language/
├── README.md                  本说明（简体中文）
├── README_EN.md               英文说明
├── README_JP.md               日文说明
├── glossary_en-zh-CN.csv      source = 英文原名
├── glossary_ja-zh-CN.csv      source = 日文原名
├── glossary_ko-zh-CN.csv      source = 韩文原名
└── glossary_zh-TW-zh-CN.csv   source = 繁体中文原名
```

## 文件格式

全部文件为 **UTF-8（含 BOM）**、**CRLF** 换行、首行表头，列结构与主表完全一致：

```csv
source,target,tgt_lng
Abercrombie,阿贝克隆比,zh-CN
Abukuma,阿武隈,zh-CN
Acasta,阿卡司塔,zh-CN
```

| 列 | 含义 |
| --- | --- |
| `source` | 该原文语言下的舰船名（英文 / 日文 / 韩文 / 繁体中文） |
| `target` | 对应的简体中文译名 |
| `tgt_lng` | 恒为 `zh-CN` |

## 文件说明

| 文件 | 原文语言 | 数据行数 | `source` 去重后 | `target` 去重后 |
| --- | --- | ---: | ---: | ---: |
| `glossary_en-zh-CN.csv` | 英文 | 1,544 | 1,544 | 856 |
| `glossary_ja-zh-CN.csv` | 日文 | 696 | 696 | 695 |
| `glossary_ko-zh-CN.csv` | 韩文 | 814 | 814 | 811 |
| `glossary_zh-TW-zh-CN.csv` | 繁体中文 | 538 | 538 | 538 |

合计 **3,592** 条对照行。英文表的 `target` 去重后只有 856 条，是因为一舰多名的现象主要集中在
英文侧（同一译名对应多个英文写法），其余三张表的原文与译文基本一一对应。

## 说明

- 本目录只收录**舰船名**，不含航海 / 军事 / 游戏术语；术语表见 `../zh-CN/terms.csv`。
- 四张子表是同一批舰船的**不同切分**，互相之间存在重复的 `target`，请勿简单合并去重后使用。
- 需要一次性导入全部原文语言时，直接用 `../zh-CN/glossary.csv`，不必使用本目录。
- 生成脚本为 `tools/build_glossary.py`（输出常量 `SPLIT`），本目录是其产出的发布快照。