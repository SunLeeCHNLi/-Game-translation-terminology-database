# 《原神》术语库（主词库）— 韩文（`ko-KR`）

[← 返回游戏总说明](../../README.md)

本目录是原神（Genshin Impact）术语库中**以 `ko-KR` 为目标语言**的主词库：共 **8,186** 条去重词条、**89,460** 行对照（其中 17 个主类目 **63,180** 行，TCG 10 个子类目 **26,280** 行）。27 个 CSV 的 `tgt_lng` 列固定为 `ko-KR`，`source` 列收录其余 13 种语言中某一种的写法，`target` 列为该语言的游戏内译名。

## 文件

本语言目录下共有 **27 个 CSV 文件**，分两层存放：

- **17 个主类目**（直接位于本目录）：
  `characters（캐릭터）.csv`、`talents（특성）.csv`、`constellations（별자리）.csv`、`weapons（무기）.csv`、`materials（재료）.csv`、`foods（음식）.csv`、`crafts（제작 재료）.csv`、`artifacts（성유물）.csv`、`domains（비경）.csv`、`enemies（적）.csv`、`animals（동물）.csv`、`outfits（의상）.csv`、`windgliders（바람의 날개）.csv`、`namecards（명함）.csv`、`geographies（지명）.csv`、`achievements（업적）.csv`、`adventureranks（모험 등급 설명）.csv`
- **10 个 TCG 子类目**（位于 `tcg-` 前缀）：
  `tcg-action-cards（행동 카드）.csv`、`tcg-character-cards（캐릭터 카드）.csv`、`tcg-enemy-cards（적 카드）.csv`、`tcg-summons（소환물）.csv`、`tcg-status-effects（상태 효과）.csv`、`tcg-keywords（키워드）.csv`、`tcg-card-backs（카드 뒷면）.csv`、`tcg-card-boxes（카드 상자）.csv`、`tcg-detailed-rules（상세 규칙）.csv`、`tcg-level-rewards（레벨 보상）.csv`

每个文件只有三列：

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Aether | 아이테르 | ko-KR |

`source` = 同一游戏对象在其余 13 种语言中某一种的写法，`target` = 本目录目标语言的名称，`tgt_lng` = 目标语言标签（本目录恒为 `ko-KR`）。这些文件可直接作为术语库导入 CAT 工具（Trados、memoQ、Phrase 等）或沉浸式翻译等术语匹配插件。

## 分类与条数

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `characters（캐릭터）.csv` | 角色 | 122 | 577 |
| `talents（특성）.csv` | 天赋 | 125 | 632 |
| `constellations（별자리）.csv` | 命之座 | 125 | 632 |
| `weapons（무기）.csv` | 武器 | 249 | 2,823 |
| `materials（재료）.csv` | 材料 | 919 | 10,636 |
| `foods（음식）.csv` | 食物 | 398 | 4,541 |
| `crafts（제작 재료）.csv` | 合成材料 | 295 | 3,522 |
| `artifacts（성유물）.csv` | 圣遗物 | 63 | 727 |
| `domains（비경）.csv` | 秘境 | 284 | 3,636 |
| `enemies（적）.csv` | 敌人 | 346 | 4,104 |
| `animals（동물）.csv` | 生物 | 223 | 2,647 |
| `outfits（의상）.csv` | 衣装 | 150 | 1,869 |
| `windgliders（바람의 날개）.csv` | 风之翼 | 18 | 211 |
| `namecards（명함）.csv` | 名片 | 289 | 3,606 |
| `geographies（지명）.csv` | 地名 | 268 | 3,389 |
| `achievements（업적）.csv` | 成就 | 1,548 | 19,461 |
| `adventureranks（모험 등급 설명）.csv` | 冒险等阶说明 | 21 | 167 |
| `tcg-action-cards（행동 카드）.csv` | 行动牌 | 927 | 9,636 |
| `tcg-character-cards（캐릭터 카드）.csv` | 角色牌 | 149 | 929 |
| `tcg-enemy-cards（적 카드）.csv` | 敌人牌 | 134 | 1,114 |
| `tcg-summons（소환물）.csv` | 召唤物 | 152 | 1,139 |
| `tcg-status-effects（상태 효과）.csv` | 状态效果 | 1,159 | 11,201 |
| `tcg-keywords（키워드）.csv` | 关键词 | 139 | 1,511 |
| `tcg-card-backs（카드 뒷면）.csv` | 牌背 | 39 | 407 |
| `tcg-card-boxes（카드 상자）.csv` | 牌盒 | 7 | 32 |
| `tcg-detailed-rules（상세 규칙）.csv` | 详细规则 | 11 | 142 |
| `tcg-level-rewards（레벨 보상）.csv` | 等级奖励 | 26 | 169 |
| **主类目（17 个文件）** | — | **5,443** | **63,180** |
| **TCG（10 个文件）** | — | **2,743** | **26,280** |
| **合计（27 个文件）** | — | **8,186** | **89,460** |

## 说明

- **译文来源与对齐方式**：`target` 列为 [genshin-db](https://github.com/theBowja/genshin-db) 7.0 收录的游戏内**官方本地化**译名，非机器翻译、非二次翻译；`source` 列为同一游戏对象在其余 13 种语言中某一种的写法；对齐单位为「游戏中的一个名称对象」，同名同译文的重复行已合并。
- **语言标签**：本目录所有文件的 `tgt_lng` 列固定为 `ko-KR`（genshin-db 内部名 `Korean`）。
- **编码**：全部 CSV 为 **UTF-8（含 BOM）+ CRLF**，含逗号或引号的字段按 RFC 4180 转义，Excel 可直接双击打开且不乱码。
- **条数与对照行的区别**：「条数」为该类目**去重后的名称对象数**（整库口径，各语言相同）；「对照行」为本目录该类目 CSV 的实际数据行数。同一条目还会以其余 13 种语言各占一行，因此行数是条数的数倍；同名条目也可能出现在多个类目中。
- **已知限制**：数据快照为 genshin-db 7.0（覆盖 14 种语言），可能落后于游戏当前版本；个别类目在不同语言下相差数行（如 `adventureranks`、`achievements`、`enemies`）。本目录只含主词库，补充词库见 `../../genshin-glossary-supplement/`，本子库总览见 `../README.md`。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有，本库不主张对上述第三方知识产权的任何权利；使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。完整条款见仓库根目录的 `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md))。

---

**Game-translation-terminology-database 是一个独立的个人项目，与上述任何游戏及其相关企业、组织无关。**
