# 我的世界（Minecraft） Wiki 译名标准化补充词库 — 繁体中文（`zh-TW`）

[← 返回游戏总说明](../../README.md)

本目录是 `minecraft-glossary/` 的**补充词库**，**以繁体中文（`zh-TW`）为目标语言**，
共 **13 个 CSV 文件**（13 个分类）、**5,157 行对照**。词条取自
[Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) 页面，
用于补充官方语言文件未涵盖、或与 Wiki 标准不一致的译名；`tgt_lng` 列固定为 `zh-TW`。

> 本文件是同一目录下 `README.md`（繁体中文）的**简体中文对照说明**，内容与数字完全一致。

## 文件

- `<分类>.csv`（13 个）— `source,target,tgt_lng` 三列，可直接导入 CAT / 术语管理工具；本补充库**没有** `extra/` 子目录

## 分类与条数

| 分类 | 主题 | 文件 | 对照行 |
| --- | --- | --- | --- |
| `advancements` | 进度 | `advancements.csv` | 242 |
| `biomes` | 生物群系 | `biomes.csv` | 117 |
| `blocks` | 方块 | `blocks.csv` | 2,561 |
| `effects` | 状态效果 | `effects.csv` | 73 |
| `enchantments` | 附魔 | `enchantments.csv` | 82 |
| `entities` | 实体 | `entities.csv` | 289 |
| `environment` | 环境 | `environment.csv` | 205 |
| `game-content` | 游戏内容 | `game-content.csv` | 113 |
| `game-modes` | 游戏模式 | `game-modes.csv` | 31 |
| `game-versions` | 游戏版本 | `game-versions.csv` | 101 |
| `items` | 物品 | `items.csv` | 1,178 |
| `other` | 其他 | `other.csv` | 64 |
| `technical` | 技术性内容 | `technical.csv` | 101 |

### 文件清单

```text
minecraft-glossary-supplement/
+-- zh-CN/
|   |-- advancements.csv
|   |-- biomes.csv
|   |-- blocks.csv
|   |-- effects.csv
|   |-- enchantments.csv
|   |-- entities.csv
|   |-- environment.csv
|   |-- game-content.csv
|   |-- game-modes.csv
|   |-- game-versions.csv
|   |-- items.csv
|   |-- other.csv
|   \-- technical.csv
+-- zh-TW/
|   |-- advancements.csv
|   |-- biomes.csv
|   |-- blocks.csv
|   |-- effects.csv
|   |-- enchantments.csv
|   |-- entities.csv
|   |-- environment.csv
|   |-- game-content.csv
|   |-- game-modes.csv
|   |-- game-versions.csv
|   |-- items.csv
|   |-- other.csv
|   \-- technical.csv
```

## 说明

- **译文来源与对齐方式。** 词条来自 Minecraft Wiki「译名标准化」页面（分别抓取 `zh-cn` 与 `zh-tw`
  两种变体后合并）。页面中的译名与 Crowdin 上已确定的官方本地化方案保持一致，未确定时暂用游戏内
  原文。同一词条会以 `en-US` 与另一中文变体分别作为 `source` 各出现一行。

- **语言标签。** `tgt_lng` 固定为 `zh-TW`。本补充库**仅涵盖繁体中文与简体中文**两种目标语言，
  其余语言请使用主词库 `minecraft-glossary/`。

- **编码说明。** 所有 CSV 均为 **UTF-8（含 BOM）**、**CRLF** 换行、首行为表头；含逗号、引号或换行的
  字段按 RFC 4180 加引号转义。与主词库不同，本目录的 CSV **不含**引号内换行，物理行数即等于对照
  行数（13 个文件共 5,170 行 = 5,157 行对照 + 13 行表头）。

- **与主词库的差异。** Wiki 采用「台湾正体」用词（例如 `Chest` = 储物箱、`Slab` = 半砖、
  `Stairs` = 阶梯），与游戏内繁体中文语言文件可能存在差异，两份数据建议按需取用。标注为「不翻译」
  的词条（如 `Mojang`、`Minecraft`）不收录于本词库。同一英文名对应多个中文写法时，使用 Wiki 的
  写法并以 ` / ` 连接（例如 `Boolean` = 布林值 / 布林型）。

- **已知限制。** 「词条数」指按英文名去重后的标准中文名条数（13 个分类合计 2,772 条），与
  「对照行数」（5,157 行）不是同一个数字：同一词条会因 `source` 不同而重复出现。该口径与游戏根目录
  `../../README.md`「数据概览」中补充词库的定义一致。本库不是官方语言文件的替代品，二者建议搭配使用。

- **复现方式。** 先抓取该页面的 `zh-cn` / `zh-tw` 两种变体（`action=parse&prop=text&variant=...`），
  再执行 `python tools/build_wiki_supplement.py`（在游戏根目录下执行，脚本读取外部数据目录）。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件的
术语匹配。本库与游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或
官方代表关系；库中译名不代表官方立场，不应被视为任何游戏的官方术语表或官方本地化文件。游戏名称、
角色名称、专有名词、商标等知识产权均归各自权利人所有。使用本项目及基于其产生的翻译结果所引发的
一切责任由使用者自行承担。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
