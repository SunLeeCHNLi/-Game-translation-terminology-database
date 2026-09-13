# 原神术语库（补充词库） — 简体中文（`zh-CN`）

[← 返回游戏总说明](../../README.md)

本目录是**以 `zh-CN`（简体中文）为目标语言**的原神术语库**补充词库**：全局 `genshin-glossary/` 主词库按 27 个类目统计共 **8,186** 条词条，本补充库收录主词库未包含的词条，本语言共 **12,237** 行对照（另有别名 `_variants.csv` **333** 行）。`tgt_lng` 列固定为 `zh-CN`；每行的 `source` 是同一词条在**其余 3 种语言（`zh-TW`、`en-US`、`ja-JP`）中的某一种**的写法，`target` 是简体中文译名。

> 本目录即为该语言的说明文件（`README.md`），因此不再另建 `README_zh-CN.md`。

## 与主词库的关系

- 本库只包含**主词库中没有的** `source/target/tgt_lng` 组合，因此可与 `genshin-glossary/zh-CN/` 直接**叠加使用**，不会产生重复条目。
- 数据来源与主词库不同（见下文「说明」），同一词条的写法可能与主词库存在细微差异（用词、标点等）。
- 本库覆盖 4 种目标语言：`zh-CN`、`zh-TW`、`en-US`、`ja-JP`；主词库覆盖 14 种。

## 文件

- 主类目文件（9 个，与主词库同名）：`characters.csv`、`materials.csv`、`geographies.csv`、`enemies.csv`、`foods.csv`、`animals.csv`、`domains.csv`、`artifacts.csv`、`weapons.csv`
- 别名文件：`_variants.csv` — 别名/俗称/常见误写，作为额外 `source` 补充
- 额外类目文件（`extra/` 下 10 个）：`extra/quests.csv`、`extra/events.csv`、`extra/objects.csv`、`extra/system.csv`、`extra/archives.csv`、`extra/story.csv`、`extra/facilities.csv`、`extra/organizations.csv`、`extra/dialogue.csv`、`extra/sereniteapot.csv`

合计 **20 个 CSV 文件**（9 个主类目 + 1 个别名 + 10 个额外类目），格式统一为三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Blackmarrow Lantern | 鸟髄孑灯 | zh-CN |
| Ultimate Overlord's Mega Magic Sword | 究极霸王超级魔剑 | zh-CN |

目录结构：

```text
zh-CN/
├── characters.csv
├── materials.csv
├── geographies.csv
├── enemies.csv
├── foods.csv
├── animals.csv
├── domains.csv
├── artifacts.csv
├── weapons.csv
├── _variants.csv
└── extra/
    ├── quests.csv
    ├── events.csv
    ├── objects.csv
    ├── system.csv
    ├── archives.csv
    ├── story.csv
    ├── facilities.csv
    ├── organizations.csv
    ├── dialogue.csv
    └── sereniteapot.csv
```

## 分类与条数

本库的每个类目都对应上游数据中的**一个来源表**，因此「主题」列标明该文件的词条来自哪里。所有数字均为本目录该文件的实际数据行数。

### 主类目（对应主词库的同名类目）

| 分类 | 文件 | 主题（上游来源） | 行数 |
| --- | --- | --- | ---: |
| characters（角色） | `characters.csv` | characters-*（蒙德/璃月/稻妻/须弥/枫丹/纳塔/挪德卡莱/至冬/坎瑞亚/愚人众等） | 3,873 |
| materials（材料） | `materials.csv` | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials | 691 |
| geographies（地理） | `geographies.csv` | locations | 1,104 |
| enemies（敌人） | `enemies.csv` | enemies | 480 |
| foods（食物） | `foods.csv` | foods | 209 |
| animals（生物） | `animals.csv` | living-beings | 157 |
| domains（秘境） | `domains.csv` | domains | 216 |
| artifacts（圣遗物） | `artifacts.csv` | artifacts | 28 |
| weapons（武器） | `weapons.csv` | weapons | 56 |
| **小计** | 9 个文件 | — | **6,814** |

### 别名（`_variants.csv`）

| 文件 | 说明 | 行数 |
| --- | --- | ---: |
| `_variants.csv` | 别名/俗称/常见误写，作为额外 `source` 补充 | 333 |

### 额外类目（`extra/`）

| 分类 | 文件 | 说明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `extra/quests.csv` | 任务名称（魔神/世界/传说/每日/部族等） | 1,664 |
| events（活动） | `extra/events.csv` | 活动名称 | 1,715 |
| objects（物件） | `extra/objects.csv` | 场景物件 | 459 |
| system（系统） | `extra/system.csv` | 系统与玩法术语 | 357 |
| archives（档案） | `extra/archives.csv` | 档案资料 | 345 |
| story（剧情） | `extra/story.csv` | 剧情与章节 | 286 |
| facilities（设施） | `extra/facilities.csv` | 设施与建筑 | 234 |
| organizations（组织） | `extra/organizations.csv` | 组织与势力 | 213 |
| dialogue（对白） | `extra/dialogue.csv` | 对白用语 | 117 |
| sereniteapot（尘歌壶） | `extra/sereniteapot.csv` | 尘歌壶 | 33 |
| **小计** | 10 个文件 | — | **5,423** |

**本目录合计：20 个文件、12,237 行对照（含别名 333 行）。**

## 说明

- **译文来源与对齐方式**：数据来自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，是社区整理的**游戏官方本地化文本**汇总，不是二次翻译或机器生成。对齐以词条为单位：`target` 为目标语言译名，`source` 为其余语言的写法；本库已在生成时扣除主词库已有的组合，因此可与主词库叠加。
- **语言标签**：本目录 `tgt_lng` 固定为 `zh-CN`，表示目标语言；`source` 可能是 `zh-TW`、`en-US`、`ja-JP` 中的任意一种。
- **编码**：全部 CSV 为 **UTF-8 with BOM** 编码、**CRLF** 换行，首行为表头，含逗号或引号的字段按 RFC 4180 转义（例如 `"""Big Sis"""`）；Excel 可直接双击打开，无需调整编码。
- **已知限制**：本库按上游来源表拆分文件，各类目的覆盖范围与主词库并不一一对应；`characters.csv` 体量最大，因其包含 NPC 与出场角色。部分词的英/日/中写法与主词库略有差异，属正常现象。
- **词条数与行数说明**：本库未提供独立于行数的「去重词条数」统计，故本页只给出实际数据行数，不作估算。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
