# 《崩坏：星穹铁道》术语库统计与校验（`Metadata`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《崩坏：星穹铁道》（Honkai: Star Rail / HSR）术语库的**统计报告**。它是
`hsr-glossary/` 各语言术语表的汇总视图，不存放术语数据本身，只用于检查规模、分布与校验结果。

## 目录结构

```text
Metadata/
├── README.md          本说明（简体中文）
├── README_EN.md       英文说明
├── README_JP.md       日文说明
└── statistics.md      术语库统计报告
```

## 文件说明

| 文件 | 类型 | 用途 |
| --- | --- | --- |
| `statistics.md` | Markdown | 术语库统计：总量、各语言、各分类、历史词条来源、抽样核对 |

### `statistics.md` 包含的章节

| 章节 | 内容 |
| --- | --- |
| 总量 | 总记录数、去重术语键、目标语言数、分类数、已确认 / 未确认条目、机器翻译条目数、历史与人工核对条目数、多译名冲突组数 |
| 各语言数量 | 13 个目标语言（`zh-CN` … `vi-VN`）各自的记录数 |
| 各分类数量 | 26 个分类（`01_character` … `26_other`）的独立术语键数与本语言记录数 |
| 历史词条来源 | 与 StarRailStaticAPI 2.3.0、HSR-Mapping-DATA 4.0 比对检出的差异记录数 |
| 第二轮抽样核对 | 每个分类抽 104 条，在 StarRailRes 独立索引中的命中数 |

## 关键数字

| 指标 | 数值 |
| --- | ---: |
| 总记录数（所有语言 `source,target,tgt_lng` 行） | 4,085,059 |
| 去重术语键（concept）总数 | 42,126 |
| 目标语言数 | 13 |
| 分类数 | 26 |
| 机器翻译条目 | 0 |
| 已确认条目 | 4,085,059 |
| 历史词条 | 166 |
| 人工核对条目（curated） | 117 |

数据版本：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`，生成日期 `2026-09-27`。

## 说明

- 本目录**不参与术语生成**，只汇总结果；术语本体在 `../hsr-glossary/<lang>/` 下。
- 「已确认条目」指目标文本可在客户端 TextMap 中逐字验证；「未确认条目」与「机器翻译条目」均为 0。
- 抽样核对用 StarRailRes 与客户端 TextMap 两份同源数据交叉验证名称与 ID 的对应关系；
  没有 StarRailRes 对应文件的门类以客户端 TextMap 逐字验证为准。
- 报告由 `tools/make_hsr_docs.py` 生成，`statistics.md` 的输出路径为 `ROOT / "Metadata"`。