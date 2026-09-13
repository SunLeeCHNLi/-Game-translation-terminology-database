# 《原神》术语库（主词库）— 意大利文（`it-IT`）

[← 返回游戏总说明](../../README.md)

本目录是原神（Genshin Impact）术语库中**以 `it-IT` 为目标语言**的主词库：共 **8,186** 条去重词条、**89,437** 行对照（其中 17 个主类目 **63,173** 行，TCG 10 个子类目 **26,264** 行）。27 个 CSV 的 `tgt_lng` 列固定为 `it-IT`，`source` 列收录其余 13 种语言中某一种的写法，`target` 列为该语言的游戏内译名。

## 文件

本语言目录下共有 **27 个 CSV 文件**，分两层存放：

- **17 个主类目**（直接位于本目录）：
  `characters.csv`、`talents.csv`、`constellations.csv`、`weapons.csv`、`materials.csv`、`foods.csv`、`crafts.csv`、`artifacts.csv`、`domains.csv`、`enemies.csv`、`animals.csv`、`outfits.csv`、`windgliders.csv`、`namecards.csv`、`geographies.csv`、`achievements.csv`、`adventureranks.csv`
- **10 个 TCG 子类目**（位于 `TCG/` 子目录）：
  `TCG/action-cards.csv`、`TCG/character-cards.csv`、`TCG/enemy-cards.csv`、`TCG/summons.csv`、`TCG/status-effects.csv`、`TCG/keywords.csv`、`TCG/card-backs.csv`、`TCG/card-boxes.csv`、`TCG/detailed-rules.csv`、`TCG/level-rewards.csv`

每个文件只有三列：

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Alhacén | Alhaitham | it-IT |

`source` = 同一游戏对象在其余 13 种语言中某一种的写法，`target` = 本目录目标语言的名称，`tgt_lng` = 目标语言标签（本目录恒为 `it-IT`）。这些文件可直接作为术语库导入 CAT 工具（Trados、memoQ、Phrase 等）或沉浸式翻译等术语匹配插件。

## 分类与条数

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `characters.csv` | 角色 | 122 | 577 |
| `talents.csv` | 天赋 | 125 | 632 |
| `constellations.csv` | 命之座 | 125 | 632 |
| `weapons.csv` | 武器 | 249 | 2,823 |
| `materials.csv` | 材料 | 919 | 10,636 |
| `foods.csv` | 食物 | 398 | 4,541 |
| `crafts.csv` | 合成材料 | 295 | 3,522 |
| `artifacts.csv` | 圣遗物 | 63 | 727 |
| `domains.csv` | 秘境 | 284 | 3,636 |
| `enemies.csv` | 敌人 | 346 | 4,104 |
| `animals.csv` | 生物 | 223 | 2,647 |
| `outfits.csv` | 衣装 | 150 | 1,869 |
| `windgliders.csv` | 风之翼 | 18 | 211 |
| `namecards.csv` | 名片 | 289 | 3,606 |
| `geographies.csv` | 地名 | 268 | 3,389 |
| `achievements.csv` | 成就 | 1,548 | 19,464 |
| `adventureranks.csv` | 冒险等阶说明 | 21 | 157 |
| `TCG/action-cards.csv` | 行动牌 | 927 | 9,618 |
| `TCG/character-cards.csv` | 角色牌 | 149 | 929 |
| `TCG/enemy-cards.csv` | 敌人牌 | 134 | 1,114 |
| `TCG/summons.csv` | 召唤物 | 152 | 1,139 |
| `TCG/status-effects.csv` | 状态效果 | 1,159 | 11,203 |
| `TCG/keywords.csv` | 关键词 | 139 | 1,511 |
| `TCG/card-backs.csv` | 牌背 | 39 | 407 |
| `TCG/card-boxes.csv` | 牌盒 | 7 | 32 |
| `TCG/detailed-rules.csv` | 详细规则 | 11 | 142 |
| `TCG/level-rewards.csv` | 等级奖励 | 26 | 169 |
| **主类目（17 个文件）** | — | **5,443** | **63,173** |
| **TCG（10 个文件）** | — | **2,743** | **26,264** |
| **合计（27 个文件）** | — | **8,186** | **89,437** |

## 说明

- **译文来源与对齐方式**：`target` 列为 [genshin-db](https://github.com/theBowja/genshin-db) 7.0 收录的游戏内**官方本地化**译名，非机器翻译、非二次翻译；`source` 列为同一游戏对象在其余 13 种语言中某一种的写法；对齐单位为「游戏中的一个名称对象」，同名同译文的重复行已合并。
- **语言标签**：本目录所有文件的 `tgt_lng` 列固定为 `it-IT`（genshin-db 内部名 `Italian`）。
- **编码**：全部 CSV 为 **UTF-8（含 BOM）+ CRLF**，含逗号或引号的字段按 RFC 4180 转义，Excel 可直接双击打开且不乱码。
- **条数与对照行的区别**：「条数」为该类目**去重后的名称对象数**（整库口径，各语言相同）；「对照行」为本目录该类目 CSV 的实际数据行数。同一条目还会以其余 13 种语言各占一行，因此行数是条数的数倍；同名条目也可能出现在多个类目中。
- **已知限制**：数据快照为 genshin-db 7.0（覆盖 14 种语言），可能落后于游戏当前版本；个别类目在不同语言下相差数行（如 `adventureranks`、`achievements`、`enemies`）。本目录只含主词库，补充词库见 `../../genshin-glossary-supplement/`，本子库总览见 `../README.md`。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有，本库不主张对上述第三方知识产权的任何权利；使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。完整条款见仓库根目录的 `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md))。

---

**Game-translation-terminology-database 是一个独立的个人项目，与上述任何游戏及其相关企业、组织无关。**
