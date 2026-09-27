# 《碧蓝航线》多语言术语库（`azur-lane-glossary`）

本子库是《碧蓝航线》（Azur Lane）的**多语言翻译术语数据产品**，按**目标语言**拆分为独立文件夹，
每个语言文件夹内按**类目**存放扁平的 CSV 文件；另有源数据、和谐名对照、按源语言拆分的视图与抓取来源目录。

## 目录结构

```text
azur-lane-glossary/
├── README.md
├── zh-CN/                        目标语言 = 简体中文
│   ├── glossary.csv
│   ├── glossary-detailed.csv
│   ├── ship-characters.csv
│   ├── ship-characters-detailed.csv
│   ├── terms.csv
│   ├── terms-detailed.csv
│   ├── ambiguous.csv             （仅 zh-CN）
│   ├── ships-and-terms.csv       （仅 zh-CN）
│   ├── README.md
│   └── README_zh-CN.md           （本语言目录的简体中文说明）
├── en-US/                        目标语言 = English（同上 6 个类目 CSV + README.md / README_zh-CN.md）
├── ja-JP/                        目标语言 = 日本語（同上）
├── ko-KR/                        目标语言 = 한국어（同上）
├── harmonized/                   五语总表、和谐名与别称对照、源数据
├── by-language/                  按源语言拆分的舰船子表，`target` 一律为简中
└── sources/                      萌娘百科名称对照表抓取结果
```

## 目标语言

| 语言目录 | 语言 | `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `zh-CN` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |

## 类目与文件名

每个目标语言目录均使用以下**一致的文件名**；只有实际存在的类目才保留。

| 类目 | 文件名 | 说明 |
| --- | --- | --- |
| 舰船名（标准名） | `glossary.csv` | 三列主表 |
| 舰船名（标准名）明细 | `glossary-detailed.csv` | 主表 + 舰船元数据 |
| 舰船角色名（和谐名） | `ship-characters.csv` | 三列主表 |
| 舰船角色名（和谐名）明细 | `ship-characters-detailed.csv` | 主表 + 舰船元数据 |
| 航海 / 军事 / 游戏术语 | `terms.csv` | 三列主表 |
| 术语明细 | `terms-detailed.csv` | 主表 + 分类与多解 |
| 一名多解源词条 | `ambiguous.csv` | 仅 `zh-CN` |
| 舰船 + 术语合并版 | `ships-and-terms.csv` | 仅 `zh-CN` |

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）**、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| 文件家族 | 实际表头 |
| --- | --- |
| `glossary.csv` / `ship-characters.csv` / `terms.csv` / `ships-and-terms.csv` / `harmonized/equipment-harmonized.csv` / `harmonized/ship-names-harmonized.csv` / `by-language/glossary_*.csv` | `source,target,tgt_lng` |
| `glossary-detailed.csv`（`zh-CN`） | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant` |
| `glossary-detailed.csv`（`en-US` / `ja-JP` / `ko-KR`） | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `ship-characters-detailed.csv`（`zh-CN`） | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,zh_CN_standard,zh_CN_target,same_source_alternatives` |
| `ship-characters-detailed.csv`（`en-US` / `ja-JP` / `ko-KR`） | `source,target,tgt_lng,src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` |
| `terms-detailed.csv` | `source,target,tgt_lng,src_lng,category,category_zh,same_source_alternatives` |
| `ambiguous.csv` | `source,target,tgt_lng,src_lng,ship_id,ship_type,nation,variant,english_name,role` |
| `harmonized/harmonized-names-detailed.csv` | `source,target,tgt_lng,src_lng,name_code_id,kind,ship_type,ship_id,en,ja,zh_TW,wiki_note` |
| `harmonized/ijn-codename-aliases.csv` | `source,target,tgt_lng,src_lng,name_code_id` |
| `harmonized/ship-names-multilingual.csv` | `ship_id,zh_CN,en,ja,zh_TW,ko,english_name,ship_type_zh,ship_type_en,nation_zh,nation_en,variant` |

对于三列主表：`tgt_lng` 指定目标语言，`target` 是该语言的译名，`source` 是其它语言的原文。
同一源串在同一主表只保留一条译文；若有多种读法，全部读法写入相应明细表的
`same_source_alternatives` 列，`zh-CN` 的多解源词条另见 `ambiguous.csv`。

## 实际计数

以下均为本次整理后直接从文件实际统计的结果。

| 语言 | 文件数 | 数据行数 |
| --- | --- | --- |
| `zh-CN` | 8 | 19,855 |
| `en-US` | 6 | 12,600 |
| `ja-JP` | 6 | 15,519 |
| `ko-KR` | 6 | 15,511 |

| `zh-CN` 文件 | 数据行数 | `target` 去重后条数 |
| --- | --- | --- |
| `glossary.csv` | 3,514 | 877 |
| `glossary-detailed.csv` | 3,592 | 877 |
| `ship-characters.csv` | 3,804 | 875 |
| `ship-characters-detailed.csv` | 3,890 | 877 |
| `terms.csv` | 449 | 170 |
| `terms-detailed.csv` | 459 | 175 |
| `ambiguous.csv` | 162 | —（全部为源串多解行） |
| `ships-and-terms.csv` | 3,985 | —（合并去重表） |

`by-language/` 是同一批舰船的**源语言侧视图**：

| 文件 | 数据行数 |
| --- | --- |
| `glossary_en-zh-CN.csv` | 1,544 |
| `glossary_ja-zh-CN.csv` | 696 |
| `glossary_ko-zh-CN.csv` | 814 |
| `glossary_zh-TW-zh-CN.csv` | 538 |

`harmonized/`：

| 文件 | 数据行数 |
| --- | --- |
| `ship-names-multilingual.csv` | 891 |
| `ship-names-harmonized.csv` | 1,187 |
| `harmonized-names-detailed.csv` | 1,259 |
| `equipment-harmonized.csv` | 8 |
| `ijn-codename-aliases.csv` | 1,082 |

术语五类（以 `zh-CN/terms-detailed.csv` 的 `category` 统计）：

| `category` | 主题 | 对照行 |
| --- | --- | --- |
| `hull_type` | 舰种 | 97 |
| `naval_term` | 航海 / 军事术语 | 198 |
| `navy_prefix` | 阵营与舰名前缀 | 59 |
| `rank` | 军衔 | 44 |
| `game_term` | 游戏术语 | 61 |

舰船变体（以 `zh-CN/ship-characters-detailed.csv` 的 `variant` 统计）：

| 变体 | 对照行 |
| --- | --- |
| 本体（无变体标记） | 3,466 |
| META | 280 |
| μ兵装 | 101 |
| II型 | 43 |

## 数据来源

- 舰船名：官方 CN / EN / JP / KR / TW 五服客户端配置（`ship_data_statistics.json`、
  `ship_data_template.json`、`ship_skin_template.json`、`ship_data_by_type.json`）。
- 和谐名与单字代称：`name_code.json`，并经萌娘百科《碧蓝航线/名称对照表》交叉校验，
  抓取结果位于 `sources/moegirl_name_table.json`。
- 术语：人工整理并逐条与各服客户端配置校对，数据源为根目录 `tools/terms_data.py`。

## 重新生成

在游戏目录下执行根目录 `tools/` 的脚本，按以下顺序运行：

```bash
# 1) 舰船词库（简中标准名）+ 五语总表 + by-language + 歧义表 + IJN 单字代称
python tools/build_glossary.py

# 2) 和谐名对照表（依赖 1) 产出的五语总表）
python tools/build_harmonized.py

# 3) 舰船角色术语表（简中和谐名）
python tools/build_ship_character_glossary.py

# 4) 舰船的 en-US / ja-JP / ko-KR 版本（依赖 1) 产出的五语总表）
python tools/build_multilang_glossaries.py

# 5) 术语表的 zh-CN / en-US / ja-JP / ko-KR 版本（数据在 tools/terms_data.py）
python tools/build_terms_glossaries.py
```

脚本内的 `BASE` / `OUT` 路径常量指向仓库外的上游客户端配置目录与生成工作目录，重跑前需按本机情况调整。
本仓库保存的是生成结果的发布快照。

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）或沉浸式翻译类软件时，选择对应目标语言目录下的
  `glossary.csv`、`ship-characters.csv` 或 `terms.csv` 作为术语库即可。
- 需要舰船元数据时使用 `*-detailed.csv`；`zh-CN` 可用 `ships-and-terms.csv` 一次性导入舰船与术语。
- `by-language/` 适合按原文语言限定匹配范围；`harmonized/` 适合获取五语对照与和谐名映射。
