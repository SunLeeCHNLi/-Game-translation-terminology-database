# 蔚蓝档案（Blue Archive）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**直接存放扁平 CSV 文件。

## 数据产品

本目录是《蔚蓝档案》术语库的数据产品容器，收录以下 **6 种目标语言**：

| 语言文件夹 | 语言 |
| --- | --- |
| `zh-CN/` | 简体中文 |
| `zh-TW/` | 繁体中文 |
| `en-US/` | English |
| `ja-JP/` | 日本語 |
| `ko-KR/` | 한국어 |
| `th-TH/` | ภาษาไทย |

每个语言文件夹内的 15 个分类 CSV 均为**扁平存放**，不设分类子目录；文件名即类目名。

## 目录结构

```text
blue-archive-glossary/
├── README.md
├── _master/
│   ├── zh-CN__all_glossary.csv      # 该语言全部对照行合并总表
│   ├── zh-CN__all_terms.csv         # 该语言全部词条清单
│   ├── zh-CN__index.csv             # 分类索引与条数
│   ├── zh-CN__README.md             # 该语言库的既有详细说明
│   ├── zh-TW__...                   # 其余 5 种语言使用相同命名
│   └── ...
├── zh-CN/
│   ├── README.md                    # 本语言库说明
│   ├── character.csv                # 分类术语表（source,target,tgt_lng）
│   ├── character__terms.csv         # 本语言词条清单（id,term,src_table）
│   └── ...                          # 共 15 个分类，每类 2 个 CSV
├── zh-TW/
├── en-US/
├── ja-JP/
├── ko-KR/
├── th-TH/
└── multilingual/                   # 六语并排总表，保留原有子目录结构
```

`_master/<lang>__<original-name>` 保存各语言原 `00_master/` 下的索引、总表与说明；分类 CSV 已全部提升到语言文件夹根层。原 `00_master/` 不再保留在各语言目录内。

## 文件格式

分类术语表（`<category>.csv`）均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。CSV 格式固定为三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它任一语言**的原文。每个语言文件夹内，同一条目会以其余目标语言分别作为 `source` 出现一行（重复行与同形行已合并）。

`<category>__terms.csv` 为本语言词条清单，格式为 `id,term,src_table`，用于校对与回查。

## 类目

| 类目 | 术语表文件 | 词条清单文件 |
| --- | --- | --- |
| 角色名称 | `character.csv` | `character__terms.csv` |
| 学校 | `school.csv` | `school__terms.csv` |
| 社团 | `club.csv` | `club__terms.csv` |
| 剧情标题 | `story_title.csv` | `story_title__terms.csv` |
| 爱用品 | `favor_item.csv` | `favor_item__terms.csv` |
| 地名 | `location.csv` | `location__terms.csv` |
| 术语 | `terminology.csv` | `terminology__terms.csv` |
| 活动 | `event.csv` | `event__terms.csv` |
| 剧情角色 | `scenario_character.csv` | `scenario_character__terms.csv` |
| 敌人 | `enemy.csv` | `enemy__terms.csv` |
| 技能 | `skill.csv` | `skill__terms.csv` |
| 道具 | `item.csv` | `item__terms.csv` |
| 装备 | `equipment.csv` | `equipment__terms.csv` |
| 家具 | `furniture.csv` | `furniture__terms.csv` |
| 关卡 | `stage.csv` | `stage__terms.csv` |

## 各语言文件数与数据行数

「文件数」为该语言文件夹内的 CSV 文件数（15 个分类术语表 + 15 个词条清单）；「术语表数据行数」为 15 个 `<category>.csv` 的数据行合计；「词条清单数据行数」为 15 个 `<category>__terms.csv` 的数据行合计。

| 语言 | 文件数 | 术语表数据行数 | 词条清单数据行数 |
| --- | ---: | ---: | ---: |
| `zh-CN` | 30 | 29463 | 7477 |
| `zh-TW` | 30 | 27453 | 6036 |
| `en-US` | 30 | 26623 | 5909 |
| `ja-JP` | 30 | 29216 | 7534 |
| `ko-KR` | 30 | 29009 | 7310 |
| `th-TH` | 30 | 26478 | 5908 |

## 生成与维护

本目录由 `../tools/` 下的脚本重建：

```bash
python tools/build_glossary.py
```

脚本位于游戏目录的 `tools/`，默认输出本数据产品；可用环境变量 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` 覆盖输入与输出目录。
