# 原神术语库 — 繁体中文（`zh-TW`）

[← 返回游戏总说明](../../README.md) · [繁體中文](README.md)

本目录是**以 `zh-TW`（繁体中文）为目标语言**的原神术语库：按 27 个类目统计，全局共 **8,186** 条词条，本语言共 **89,434** 行对照。`tgt_lng` 列固定为 `zh-TW`；每行的 `source` 是同一词条在**其余 13 种语言中的某一种**的写法，`target` 是繁体中文译文。文件按**类目**分列，每个类目一个 CSV。

## 文件

- `characters.csv`、`talents.csv`、`constellations.csv`、`weapons.csv`、`materials.csv`、`foods.csv`、`crafts.csv`、`artifacts.csv`、`domains.csv`、`enemies.csv`、`animals.csv`、`outfits.csv`、`windgliders.csv`、`namecards.csv`、`geographies.csv`、`achievements.csv`、`adventureranks.csv` — 17 个主类目文件
- `TCG/action-cards.csv`、`TCG/character-cards.csv`、`TCG/enemy-cards.csv`、`TCG/summons.csv`、`TCG/status-effects.csv`、`TCG/keywords.csv`、`TCG/card-backs.csv`、`TCG/card-boxes.csv`、`TCG/detailed-rules.csv`、`TCG/level-rewards.csv` — 10 个 TCG（七圣召唤）子类目文件

合计 **27 个 CSV 文件**，格式统一为三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | 空 | zh-TW |
| Leer | 空 | zh-TW |

目录结构：

```text
zh-TW/
├── characters.csv
├── talents.csv
├── constellations.csv
├── weapons.csv
├── materials.csv
├── foods.csv
├── crafts.csv
├── artifacts.csv
├── domains.csv
├── enemies.csv
├── animals.csv
├── outfits.csv
├── windgliders.csv
├── namecards.csv
├── geographies.csv
├── achievements.csv
├── adventureranks.csv
└── TCG/
    ├── action-cards.csv
    ├── character-cards.csv
    ├── enemy-cards.csv
    ├── summons.csv
    ├── status-effects.csv
    ├── keywords.csv
    ├── card-backs.csv
    ├── card-boxes.csv
    ├── detailed-rules.csv
    └── level-rewards.csv
```

## 分类与条数

「词条」为该类目在全部 14 种语言中的**去重词条数**（同一类目各语言相同）；「行数」为本目录该文件的数据行数。

### 主类目

| 分类 | 文件 | 词条数 | 行数 |
| --- | --- | ---: | ---: |
| characters（角色） | `characters.csv` | 122 | 577 |
| talents（天赋） | `talents.csv` | 125 | 632 |
| constellations（命之座） | `constellations.csv` | 125 | 632 |
| weapons（武器） | `weapons.csv` | 249 | 2,823 |
| materials（材料） | `materials.csv` | 919 | 10,636 |
| foods（食物） | `foods.csv` | 398 | 4,541 |
| crafts（合成物） | `crafts.csv` | 295 | 3,522 |
| artifacts（圣遗物） | `artifacts.csv` | 63 | 727 |
| domains（秘境） | `domains.csv` | 284 | 3,636 |
| enemies（敌人） | `enemies.csv` | 346 | 4,104 |
| animals（生物） | `animals.csv` | 223 | 2,647 |
| outfits（装扮） | `outfits.csv` | 150 | 1,869 |
| windgliders（风之翼） | `windgliders.csv` | 18 | 211 |
| namecards（名片） | `namecards.csv` | 289 | 3,606 |
| geographies（地理） | `geographies.csv` | 268 | 3,389 |
| achievements（成就） | `achievements.csv` | 1,548 | 19,464 |
| adventureranks（冒险等阶） | `adventureranks.csv` | 21 | 157 |
| **小计** | 17 个文件 | — | **63,173** |

### TCG 子类目（`TCG/`）

| 子类目 | 文件 | 词条数 | 行数 |
| --- | --- | ---: | ---: |
| action-cards（行动牌） | `TCG/action-cards.csv` | 927 | 9,608 |
| character-cards（角色牌） | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards（敌人牌） | `TCG/enemy-cards.csv` | 134 | 1,114 |
| summons（召唤物） | `TCG/summons.csv` | 152 | 1,139 |
| status-effects（状态效果） | `TCG/status-effects.csv` | 1,159 | 11,210 |
| keywords（关键词） | `TCG/keywords.csv` | 139 | 1,511 |
| card-backs（牌背） | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes（牌盒） | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules（详细规则） | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards（等级奖励） | `TCG/level-rewards.csv` | 26 | 169 |
| **小计** | 10 个文件 | — | **26,261** |

**本目录合计：27 个文件、89,434 行。**

## 说明

- **译文来源与对齐方式**：数据来自 [theBowja/genshin-db](https://github.com/theBowja/genshin-db)（数据版本 7.0，覆盖全部 14 种语言），是**游戏官方本地化文本**，不是二次翻译或机器生成。对齐以词条为单位：同一词条会以其余每一种语言作为 `source` 各出一行，因此行数远大于词条数。
- **语言标签**：本目录 `tgt_lng` 固定为 `zh-TW`，表示目标语言；`source` 可能是其余 13 种语言（`zh-CN`、`en-US`、`ja-JP`、`ko-KR`、`fr-FR`、`de-DE`、`es-ES`、`ru-RU`、`pt-BR`、`it-IT`、`tr-TR`、`th-TH`、`vi-VN`）中的任意一种。
- **编码**：全部 CSV 为 **UTF-8 with BOM** 编码、**CRLF** 换行，首行为表头，含逗号或引号的字段按 RFC 4180 转义；Excel 可直接双击打开，无需调整编码。
- **已知限制**：各类目行数在不同语言间略有差异（例如部分 `achievements`、`adventureranks` 条目并非每种语言都存在）。跨类目存在同名词条（例如某武器名同时出现在 `weapons` 与 `TCG` 中），因此各文件行数相加会大于全局去重后的词条数。官方未翻译的名称保留原文形态。
- **补充词库**：同级目录 `genshin-glossary-supplement/` 收录主词库未包含的词条，可与本库叠加使用，详见该库的 `README.md`。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
