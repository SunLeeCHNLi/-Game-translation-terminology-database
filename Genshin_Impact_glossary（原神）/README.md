# 《原神》Genshin Impact 翻译术语库 / Genshin Impact Terminology Database / Genshin Impact 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本目录收录《原神》（Genshin Impact）的多语言对照术语库，由**主词库**与**补充词库**两部分组成：主词库以 **14 种目标语言**（zh-CN / zh-TW / en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-BR / it-IT / tr-TR / th-TH / vi-VN）各 27 个类目 CSV 覆盖游戏内名称类数据，补充词库以 4 种目标语言（zh-CN / zh-TW / en-US / ja-JP）补充 NPC、地名、任务、活动等主词库未收录的词条。

主词库共 **8,186** 个去重词条（27 个类目合计）、**1,252,692** 行对照、**1,069,738** 个全局唯一 `source/target/tgt_lng` 组合；补充词库另有 **51,581** 行对照与 **1,343** 行别名。两部分可直接叠合使用（补充词库只含主词库中没有的组合）。

译文全部取自游戏本身的官方本地化文本（genshin-db / genshin-langdata 收录的游戏数据文件），**不是二次翻译或机器翻译**。

## 使用方法

1. 单文件下载：进入 `genshin-glossary/<语言代码>/` 选择需要的类目 CSV（TCG 类目在 `TCG/` 子目录内）直接下载，即可导入沉浸式翻译等术语工具；补充词条进入 `genshin-glossary-supplement/<语言代码>/`。
2. 整个语言目录打包下载：在 GitHub 上进入 `genshin-glossary/<语言代码>/`，使用「下载目录」取得该目标语言的全部类目文件；补充词库同理。
3. 克隆整个仓库，配合 `tools/` 下的脚本，并预先下载所引用的上游数据仓库（genshin-db、genshin-langdata）源码，即可自行复现全部 CSV。

## 目录结构

```text
Genshin_Impact_glossary（原神）/
├── README.md                     # 本文件（简体中文）
├── README_EN.md                  # English
├── README_JP.md                  # 日本語
├── genshin-glossary/             # 主词库（genshin-db，14 种目标语言，每语言 27 个 CSV）
│   ├── README.md                 # 主词库说明（生成物）
│   ├── zh-CN/                    # 目标语言 = 简体中文
│   │   ├── characters.csv
│   │   ├── talents.csv
│   │   ├── ...                   # 共 17 个主类目 CSV
│   │   └── TCG/                  # TCG 类目，按子类型细分为 10 个 CSV
│   │       ├── action-cards.csv
│   │       └── ...
│   ├── zh-TW/
│   ├── en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
│   ├── pt-BR/  it-IT/  tr-TR/  th-TH/  vi-VN/     # 合计 14 个语言目录
├── genshin-glossary-supplement/  # 补充词库（genshin-langdata，4 种目标语言）
│   ├── README.md                 # 补充词库说明（生成物）
│   ├── zh-CN/
│   │   ├── characters.csv        # 9 个与主词库同名的主类目
│   │   ├── _variants.csv         # 别名/俗称/常见误写，作为额外 source 补充
│   │   └── extra/                # 10 个额外类目
│   │       ├── quests.csv
│   │       └── ...
│   ├── zh-TW/  en-US/  ja-JP/    # 合计 4 个语言目录，每语言 20 个 CSV
└── tools/
    ├── build_main_glossary.js    # 从 genshin-db 生成主词库
    ├── build_supplement.mjs      # 从 genshin-langdata 生成补充词库（依赖主词库产物）
    ├── readme_main.js            # 生成 genshin-glossary/README.md
    ├── readme_sup.js             # 生成 genshin-glossary-supplement/README.md
    ├── glossary_counts.json      # 主词库构建元数据（各语言/类目条目数与行数）
    └── supplement_counts.json    # 补充词库构建元数据
```

## 数据概览

### 主词库：各语言对照行数

「对照行数」= 该语言目录下全部 27 个 CSV 的数据行数（不含表头）；「文件数」为该语言目录内的 CSV 个数。

| 语言 | 语言名称 | CSV 文件数 | 对照行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 27 | 89,790 |
| `zh-TW` | 繁體中文 | 27 | 89,434 |
| `en-US` | English | 27 | 89,412 |
| `ja-JP` | 日本語 | 27 | 89,490 |
| `ko-KR` | 한국어 | 27 | 89,460 |
| `fr-FR` | Français | 27 | 89,613 |
| `de-DE` | Deutsch | 27 | 89,362 |
| `es-ES` | Español | 27 | 89,411 |
| `ru-RU` | Русский | 27 | 89,418 |
| `pt-BR` | Português | 27 | 89,444 |
| `it-IT` | Italiano | 27 | 89,437 |
| `tr-TR` | Türkçe | 27 | 89,423 |
| `th-TH` | ภาษาไทย | 27 | 89,468 |
| `vi-VN` | Tiếng Việt | 27 | 89,530 |
| **合计** | **14 种语言** | **378** | **1,252,692** |

> 全部 14 个语言目录共 **1,069,738** 个全局唯一 `source/target/tgt_lng` 组合（跨语言去重后）。
> 每个语言目录内，同一条目会以其余 13 种语言分别作为 `source` 各出现一行（重复行与同形行已合并）。

### 主词库：主类目与条目数

「条目」指该类目下的**去重词条数**（一个词条 = 游戏中的一个名称对象，统计口径为简体中文侧）；
「每语言行数」为该语言目录内该类目 CSV 数据行数在 14 种语言上的平均值（四舍五入）。

| 类目 | 文件 | 条目数 | 每语言行数 |
| --- | --- | --- | --- |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2,823 |
| materials | `materials.csv` | 919 | 10,637 |
| foods | `foods.csv` | 398 | 4,541 |
| crafts | `crafts.csv` | 295 | 3,522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3,636 |
| enemies | `enemies.csv` | 346 | 4,104 |
| animals | `animals.csv` | 223 | 2,647 |
| outfits | `outfits.csv` | 150 | 1,869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3,606 |
| geographies | `geographies.csv` | 268 | 3,389 |
| achievements | `achievements.csv` | 1,548 | 19,463 |
| adventureranks | `adventureranks.csv` | 21 | 158 |
| **TCG（10 个子类目合计）** | `TCG/*.csv` | **2,743** | **26,304** |

### 主词库：TCG 子类目

| 子类目 | 文件 | 条目数 |
| --- | --- | --- |
| action-cards | `TCG/action-cards.csv` | 927 |
| character-cards | `TCG/character-cards.csv` | 149 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 |
| summons | `TCG/summons.csv` | 152 |
| status-effects | `TCG/status-effects.csv` | 1,159 |
| keywords | `TCG/keywords.csv` | 139 |
| card-backs | `TCG/card-backs.csv` | 39 |
| card-boxes | `TCG/card-boxes.csv` | 7 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 |
| level-rewards | `TCG/level-rewards.csv` | 26 |

### 补充词库：各语言新增行数

| 语言 | 语言名称 | 主类目 CSV | 对照行数 | 别名行数（`_variants.csv`） |
| --- | --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 19 | 12,237 | 333 |
| `zh-TW` | 繁體中文 | 19 | 12,221 | 332 |
| `en-US` | English | 19 | 13,815 | 395 |
| `ja-JP` | 日本語 | 19 | 13,308 | 283 |
| **合计** | **4 种语言** | **76** | **51,581** | **1,343** |

> 补充词库每个语言目录共 20 个 CSV：9 个与主词库同名的主类目 + `extra/` 下 10 个额外类目 + 1 个 `_variants.csv`。

### 补充词库：类目与新增行数

| 类目 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | 合计 |
| --- | --- | --- | --- | --- | --- |
| artifacts | 28 | 29 | 31 | 32 | 120 |
| characters | 3,873 | 3,796 | 4,609 | 4,221 | 16,499 |
| domains | 216 | 212 | 240 | 226 | 894 |
| materials | 691 | 738 | 741 | 789 | 2,959 |
| enemies | 480 | 518 | 525 | 697 | 2,220 |
| foods | 209 | 259 | 233 | 246 | 947 |
| animals | 157 | 158 | 172 | 175 | 662 |
| geographies | 1,104 | 1,082 | 1,235 | 1,163 | 4,584 |
| weapons | 56 | 75 | 56 | 69 | 256 |
| extra/dialogue | 117 | 115 | 123 | 121 | 476 |
| extra/facilities | 234 | 226 | 270 | 236 | 966 |
| extra/objects | 459 | 447 | 508 | 472 | 1,886 |
| extra/organizations | 213 | 205 | 243 | 209 | 870 |
| extra/quests | 1,664 | 1,652 | 1,769 | 1,753 | 6,838 |
| extra/sereniteapot | 33 | 32 | 37 | 32 | 134 |
| extra/story | 286 | 282 | 348 | 302 | 1,218 |
| extra/system | 357 | 343 | 447 | 387 | 1,534 |
| extra/events | 1,715 | 1,705 | 1,842 | 1,796 | 7,058 |
| extra/archives | 345 | 347 | 386 | 382 | 1,460 |

### 文件格式

主词库与补充词库的 CSV 格式完全一致：三列 `source,target,tgt_lng`，**UTF-8（含 BOM）** 编码、**CRLF** 换行，首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。`target` 为 `tgt_lng` 指定语言的译文，`source` 为该条目在**其它任一语言**中的写法。

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | 空 | zh-CN |
| Alhaitham | 艾尔海森 | zh-CN |
| Harbinger of Dawn | 黎明神剑 | zh-CN |

### 数据清洗说明

源数据中的以下标记已在生成时处理：

| 源数据写法 | 处理方式 | 示例 |
| --- | --- | --- |
| `{M#...}{F#...}` 相邻的性别变体 | 取男性形态 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 单独的 `{M#…}` / `{F#…}` | 取其内容 | `#Искатель{F#ница}` → `Искательница` |
| 名称开头的 `#`（性别相关标记） | 去除 | `#Éclaireuse 100%` → `Éclaireuse 100%` |
| `{NON_BREAK_SPACE}`、`{SPACE}` | 替换为普通空格 | `PB{NON_BREAK_SPACE}-{NON_BREAK_SPACE}Retorno` → `PB - Retorno` |
| 其它占位符（保留原样） | `{NICKNAME}`、`{REALNAME[…]}`、`{MATEAVATAR#SEXPRO[…]} ` | 各仅 1 条 |

同名同译文的重复行（例如英/法/德同形的人名）已合并。

## 使用的相关内容

| 来源仓库 | 用途 |
| --- | --- |
| [theBowja/genshin-db](https://github.com/theBowja/genshin-db) | 主词库 `genshin-glossary/` 的唯一数据源，提供游戏内 14 种语言的官方名称映射（数据版本 7.0） |
| [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) | 补充词库 `genshin-glossary-supplement/` 的唯一数据源，提供 NPC、地名、敌人、任务、活动、系统等词条及别名，覆盖 en / ja / zh-CN / zh-TW |

## 生成与复现

脚本读取**仓库外的外部数据目录**（genshin-db / genshin-langdata 的源码副本），并把 CSV 输出到外部工作目录；
本仓库保存的是这些输出结果，以及构建元数据 `tools/glossary_counts.json`、`tools/supplement_counts.json`。
在游戏目录下依次执行：

```bash
# 1. 生成主词库（数据源：genshin-db），输出 14 个语言目录 + glossary_counts.json
node tools/build_main_glossary.js

# 2. 生成补充词库（数据源：genshin-langdata，并读取上一步生成的主词库 CSV 去重）
node tools/build_supplement.mjs

# 3. 依据构建元数据重新生成两份子词库 README（写入上面的外部输出目录）
node tools/readme_main.js
node tools/readme_sup.js
```

依赖关系：步骤 2 读取步骤 1 的产物（`genshin-glossary/` 下全部 CSV）作为去重基准，**必须先完成步骤 1**；
步骤 3 的两个脚本只读各自词库的 `_counts.json` 构建元数据，相互独立。
复现前需先取得 [genshin-db](https://github.com/theBowja/genshin-db) 与
[xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) 的源码，并把脚本顶部的路径常量指向本地副本
（`build_main_glossary.js` / `build_supplement.mjs` 顶部的 `SRC`/`LD`/`OUT`，以及两个 readme 脚本顶部的 `MAIN`/`SUP`）。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《原神》的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为本游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
