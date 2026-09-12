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
├── zh-CN/
│   ├── blocks.csv
│   ├── items.csv
│   └── ...
├── zh-TW/
└── _counts.json
```

## 文件格式

与主词库一致：**UTF-8（含 BOM）**、**CRLF**、首行表头。

| source | target | tgt_lng |
| --- | --- | --- |
| Chest | 箱子 | zh-CN |
| 儲物箱 | 箱子 | zh-CN |

## 类目与条目数

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

- Wiki 采用「台灣正體」用词（例如 `Chest` = 儲物箱、`Slab` = 半磚、`Stairs` = 階梯），与游戏内繁体中文语言文件可能存在差异，两份资料**建议按需取用**。
- 标注为「不翻译」的条目（如 `Mojang`、`Minecraft`）不会收入本词库。
- 同一英文名对应多个中文写法时，使用 Wiki 的写法并以 ` / ` 连接（例如 `Boolean` = 布林值 / 布林型）。

## 使用提示

- 重新生成：先抓取该页面的 `zh-cn` / `zh-tw` 两种变体（`action=parse&prop=text&variant=...`），再运行 `tools/build_wiki_supplement.py`。
