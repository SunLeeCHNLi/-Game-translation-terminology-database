# 猫之城（Cat Fantasy）七语并排总表（`multilingual/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录把《猫之城》术语库的全部 **102,213** 条词条按「一条一行」摊开，七种语言并排展示，便于整体检索与二次加工。以单一语言为目标语言的拆分结果在上一层目录的 `../zh-CN/`、`../en-US/` 等语言文件夹中。

## 目录结构

```text
multilingual/
├── all_languages_master.csv   七语并排总表（102213 行数据）
└── 00_master/
    ├── categories.csv         16 个类目的定义（category,label,description）
    ├── source_mapping.csv     来源表 → 类目 的映射与词条数（379 张表）
    └── README.md              本说明
```

## 文件格式

`all_languages_master.csv` 为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。

| 列 | 说明 |
| --- | --- |
| `id` | 词条编号，格式为 `源表名.主键.字段名`，可与各语言 `*__terms.csv` 的 `id` 对应 |
| `category` | 所属分类（见 `00_master/categories.csv`） |
| `src_table` | 官方数据包中的来源表相对路径 |
| `zh-CN` | 简体中文 |
| `zh-TW` | 繁体中文 |
| `en-US` | 英文 |
| `ja-JP` | 日文 |
| `ko-KR` | 韩文 |
| `th-TH` | 泰文 |
| `id-ID` | 印尼文 |

## 辅助文件

| 文件 | 列 | 说明 |
| --- | --- | --- |
| `00_master/categories.csv` | `category,label,description` | 16 个类目的编号、名称与主题描述 |
| `00_master/source_mapping.csv` | `src_table,category,entry_count` | 379 张来源表到 16 个类目的映射与词条数 |

## 说明

- 本表是各语言分库的**上游总表**，各语言目录下的 `*_glossary.csv` 由它展开生成。
- `en_UK` 与 `en_US` 两套英文中，总表采用 `en_US` 优先、缺失回退 `en_UK` 的取值，与 `../en-US/` 目录一致。
- 空单元格表示该词条在该语言下缺失。若需按分类拆分，请直接使用 `../<lang>/` 下的分类文件。
