# 我的世界（Minecraft）Wiki 译名标准化 补充词库

本目录是 `minecraft-glossary/` 的**补充词库**，收录 [Minecraft Wiki 译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) 页面中的标准译名，用于补充官方语言文件未覆盖或与 Wiki 标准不一致的译名。

## 数据来源

- [Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)（简体中文 / 繁体中文两种变体分别抓取后合并）
- 该页面同时是 Wiki 的译名规范来源，其译名与 Crowdin 上已确定的官方本地化方案保持一致，未确定时暂用游戏内原文。

## 覆盖范围

- 本补充词库**仅覆盖 `zh-CN`（简体中文）与 `zh-TW`（繁体中文）**两种目标语言，其余语言请使用主词库 `minecraft-glossary/`。
- 每个语言文件夹内，同一条目会以 `en-US` 与另一中文变体分别作为 `source` 各出现一行。

## 目录结构

```
minecraft-glossary-supplement/
├── zh-CN/                    # 目标语言 = 简体中文，13 个类目文件
│   ├── blocks.csv
│   ├── items.csv
│   └── ...
├── zh-TW/                    # 目标语言 = 繁體中文，同样的 13 个类目
└── README.md                 # 本文件

（各语言的条目数统计见上级目录 `tools/supplement_counts.json`）
```

## 文件格式

与主词库一致：**UTF-8（含 BOM）**、**CRLF**、首行表头。

| source | target | tgt_lng |
| --- | --- | --- |
| Chest | 箱子 | zh-CN |
| 儲物箱 | 箱子 | zh-CN |

## 类目与条目数

下表数字取自 `tools/supplement_counts.json`。

### 各语言的条目数

| 语言 | 语言（名称） | 文件数 | 数据行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 13 | 5,157 |
| `zh-TW` | 繁體中文 | 13 | 5,157 |

### 各分类明细

「词条数」= 该分类下按英文名去重后的标准中文名条数；
「行数」= 该语言文件夹内该类目 CSV 的数据行数（每个条目最多由 `en-US` 与另一中文变体两种 `source` 各生成一行，
因此行数约为词条数的 2 倍；当两种中文写法相同、或英文名本身就是译名时，该 source 行不会生成）。

| 类目 | 文件 | 词条数 | zh-CN 行数 | zh-TW 行数 |
| --- | --- | --- | --- | --- |
| advancements | `advancements.csv` | 126 | 242 | 242 |
| biomes | `biomes.csv` | 67 | 117 | 117 |
| blocks | `blocks.csv` | 1345 | 2561 | 2561 |
| effects | `effects.csv` | 40 | 73 | 73 |
| enchantments | `enchantments.csv` | 43 | 82 | 82 |
| entities | `entities.csv` | 161 | 289 | 289 |
| environment | `environment.csv` | 119 | 205 | 205 |
| game-content | `game-content.csv` | 67 | 113 | 113 |
| game-modes | `game-modes.csv` | 18 | 31 | 31 |
| game-versions | `game-versions.csv` | 64 | 101 | 101 |
| items | `items.csv` | 626 | 1178 | 1178 |
| other | `other.csv` | 38 | 64 | 64 |
| technical | `technical.csv` | 58 | 101 | 101 |

## 与主词库的差异

- 分类体系不同：本补充词库按 Wiki 页面的**章节**分为 13 个类目（`advancements`、`biomes`、`blocks`、`effects`、`enchantments`、`entities`、`environment`、`game-content`、`game-modes`、`game-versions`、`items`、`other`、`technical`），与主词库 `minecraft-glossary/` 的 34 个类目（19 个主类目 + 15 个 `extra/` 类目）**名称与口径都不相同**，两边不能按类目名直接合并。
- 只覆盖中文：`zh-CN` 行以 `en-US` 与 `zh-TW` 为 `source`，`zh-TW` 行以 `en-US` 与 `zh-CN` 为 `source`；不包含其它语言的写法。
- Wiki 采用「台灣正體」用词（例如 `Chest` = 儲物箱、`Slab` = 半磚、`Stairs` = 階梯），与游戏内繁体中文语言文件可能存在差异，两份资料**建议按需取用**。
- 标注为「不翻译」的条目（如 `Mojang`、`Minecraft`）不会收入本词库。
- 同一英文名对应多个中文写法时，使用 Wiki 的写法并以 ` / ` 连接（例如 `Boolean` = 布林值 / 布林型）。

## 使用提示

- 重新生成：先抓取该页面的 `zh-cn` / `zh-tw` 两种变体（`action=parse&prop=text&variant=...`），再运行 `tools/build_wiki_supplement.py`。
- 本 README 由 `tools/make_readme.py` 生成，本页数字取自 `tools/supplement_counts.json`；请勿手工改动数字。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《我的世界》（Minecraft）的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
