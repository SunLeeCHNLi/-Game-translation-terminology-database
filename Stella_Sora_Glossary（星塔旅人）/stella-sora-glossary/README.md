# 星塔旅人（Stella Sora）单语言术语库

本目录是《星塔旅人》（Stella Sora / ステラソラ）翻译术语库的数据产品 `stella-sora-glossary`，按**目标语言**拆分为 5 个独立目录：`zh-CN`（简体中文）、`zh-TW`（繁體中文）、`en-US`（English）、`ja-JP`（日本語）、`ko-KR`（한국어）。

每个语言目录中的 15 个分类 CSV 均**直接平铺在语言目录下**，不再使用 `NN_xxx/` 子目录。`<cat>.csv` 是术语表，格式为 `source,target,tgt_lng`；`<cat>__terms.csv` 是该语言的词条清单，格式为 `id,term,src_table`。`_master/` 保存各语言的合并总表、索引与既有说明；`multilingual/` 保留五语并排原始总表。

## 目录结构

```text
stella-sora-glossary/
├── zh-CN/                    # 目标语言 = 简体中文
│   ├── README.md
│   ├── character.csv
│   ├── character__terms.csv
│   └── ...                   # 共 15 组分类 CSV
├── zh-TW/
├── en-US/
├── ja-JP/
├── ko-KR/
├── _master/
│   ├── zh-CN__all_glossary.csv
│   ├── zh-CN__all_terms.csv
│   ├── zh-CN__index.csv
│   └── ...
└── multilingual/             # 五语并排原始总表，内部结构保持不变
```

## 文件格式

单语言分类 CSV 使用以下固定 3 列表头：

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| コハク | 琥珀 | zh-CN |

`<cat>.csv` 的文件编码为 **UTF-8 BOM**，换行为 **CRLF**；`target` 是 `tgt_lng` 指定语言的译文，`source` 是其它语言的原文。`<cat>__terms.csv` 则按 `id,term,src_table` 记录该语言的词条清单。

## 分类与数量

| 分类 | 文件 | 说明 |
| --- | --- | --- |
| 角色名称 | `character.csv` | Character names |
| 技能名称 | `skill.csv` | Skills |
| 潜能名称 | `potential.csv` | Potentials |
| 唱片 / Disc | `disc.csv` | Discs |
| 道具 | `item.csv` | Items |
| 装备 | `equipment.csv` | Equipment |
| 敌人 | `enemy.csv` | Enemies |
| 关卡 | `stage.csv` | Stages |
| 活动 | `event.csv` | Events |
| 系统术语 | `system.csv` | System terms |
| UI术语 | `ui.csv` | UI wording |
| 剧情专有名词 | `story.csv` | Story proper nouns |
| 阵营 | `faction.csv` | Factions |
| 地点 | `location.csv` | Locations |
| 游戏机制术语 | `terminology.csv` | Gameplay mechanics |

### 各语言文件与数据行数

| 语言 | 分类术语表文件数 | 分类词条清单文件数 | 术语表数据行数 | 词条清单数据行数 |
| --- | ---: | ---: | ---: | ---: |
| `zh-CN` | 15 | 15 | 46,279 | 12,292 |
| `zh-TW` | 15 | 15 | 46,052 | 12,292 |
| `en-US` | 15 | 15 | 46,032 | 12,288 |
| `ja-JP` | 15 | 15 | 46,426 | 12,289 |
| `ko-KR` | 15 | 15 | 45,950 | 12,292 |

### 分类 × 语言的术语表数据行数

| 分类 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 979 | 977 | 973 | 1021 | 968 |
| `skill.csv` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `potential.csv` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `disc.csv` | 893 | 896 | 896 | 893 | 893 |
| `item.csv` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `equipment.csv` | 58 | 58 | 58 | 58 | 58 |
| `enemy.csv` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `stage.csv` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `event.csv` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `system.csv` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `ui.csv` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `story.csv` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `faction.csv` | 81 | 78 | 78 | 78 | 78 |
| `location.csv` | 98 | 98 | 98 | 96 | 96 |
| `terminology.csv` | 4660 | 4637 | 4630 | 4661 | 4649 |

## 重新生成

本目录的数据由 `../tools/` 下的脚本重新生成：

```bash
python ../tools/build_glossary.py
python ../tools/split_by_language.py
```

`build_glossary.py` 从上游多语言文本库生成五语并排总表；`split_by_language.py` 按目标语言拆分并生成各语言分类 CSV。具体的外部输入路径与脚本行为见游戏根目录的 `README.md` / `README_EN.md` / `README_JP.md`。
