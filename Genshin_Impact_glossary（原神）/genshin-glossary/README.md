# 原神（Genshin Impact）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放。

## 数据来源

- 主词库：[theBowja/genshin-db](https://github.com/theBowja/genshin-db)（数据版本 7.0，覆盖全部 14 种语言）
- 补充词库：见同级目录 `genshin-glossary-supplement/`（来源 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，覆盖 zh-CN / zh-TW / en-US / ja-JP）

## 目录结构

```
genshin-glossary/
├── zh-CN/                    # 目标语言 = 简体中文
│   ├── characters.csv
│   ├── talents.csv
│   ├── ...
│   └── TCG/                  # TCG 类目按子类型细分
│       ├── action-cards.csv
│       └── ...
├── zh-TW/
├── en-US/ ... vi-VN/         # 共 14 个语言文件夹
└── （生成元数据已移至同级 ../tools/glossary_counts.json）
```

> 本目录由同级 `tools/build_main_glossary.js` 生成，构建元数据（各语言、各类目的条目数与行数统计）
> 存放于同级 `tools/glossary_counts.json`，不在本目录内。

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | 艾尔海森 | zh-CN |
| Alhaitham | 艾尔海森 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它任一语言**的原文。
即每个语言文件夹内，同一条目会以其余 13 种语言分别作为 `source` 各出现一行（重复行与同形行已合并）。

## 语言代码

| 语言文件夹 | 语言 | genshin-db 内部名 |
| --- | --- | --- |
| `zh-CN` | 简体中文 | ChineseSimplified |
| `zh-TW` | 繁體中文 | ChineseTraditional |
| `en-US` | English | English |
| `ja-JP` | 日本語 | Japanese |
| `ko-KR` | 한국어 | Korean |
| `fr-FR` | Français | French |
| `de-DE` | Deutsch | German |
| `es-ES` | Español | Spanish |
| `ru-RU` | Русский | Russian |
| `pt-BR` | Português | Portuguese |
| `it-IT` | Italiano | Italian |
| `tr-TR` | Türkçe | Turkish |
| `th-TH` | ภาษาไทย | Thai |
| `vi-VN` | Tiếng Việt | Vietnamese |

## 类目与条目数

「条目」指该分类下的**去重词条数**（一个词条 = 游戏中的一个名称对象）；「行数」为每个语言文件夹内该类目 CSV 的数据行数。

### 主类目

| 类目 | 文件 | 词条数 | 每语言行数（约） |
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
| TCG | `TCG/*.csv` | 2,743 | 26,304 |

### TCG 子类目

| 子类目 | 文件 | 词条数 |
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

## 各语言总行数

| 语言 | 文件数 | 数据行数 |
| --- | --- | --- |
| `zh-CN` | 27 | 89,790 |
| `zh-TW` | 27 | 89,434 |
| `en-US` | 27 | 89,412 |
| `ja-JP` | 27 | 89,490 |
| `ko-KR` | 27 | 89,460 |
| `fr-FR` | 27 | 89,613 |
| `de-DE` | 27 | 89,362 |
| `es-ES` | 27 | 89,411 |
| `ru-RU` | 27 | 89,418 |
| `pt-BR` | 27 | 89,444 |
| `it-IT` | 27 | 89,437 |
| `tr-TR` | 27 | 89,423 |
| `th-TH` | 27 | 89,468 |
| `vi-VN` | 27 | 89,530 |
| **合计** | **378** | **1,252,692** |

> 跨类目存在同名词条（例如某武器名同时出现在 `weapons` 与 `TCG` 中），因此各文件行数相加会大于全局去重后的词条数，属正常现象。全局唯一 `source/target/tgt_lng` 组合数为 1,069,738。

## 数据清洗说明

源数据中的以下标记已在生成时处理：

| 源数据写法 | 处理方式 | 示例 |
| --- | --- | --- |
| `{M#...}{F#...}` 相邻的性别变体 | 取男性形态 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 单独的 `{M#…}` / `{F#…}` | 取其内容 | `#Искатель{F#ница}` → `Искательница` |
| 名称开头的 `#`（性别相关标记） | 去除 | `#Éclaireuse 100%` → `Éclaireuse 100%` |
| `{NON_BREAK_SPACE}`、`{SPACE}` | 替换为普通空格 | `PB{NON_BREAK_SPACE}-{NON_BREAK_SPACE}Retorno` → `PB - Retorno` |
| 其它占位符（保留原样） | `{NICKNAME}`、`{REALNAME[…]} `、`{MATEAVATAR#SEXPRO[…]} ` | 各仅 1 条 |

同名同译文的重复行（例如英/法/德同形的人名）已合并。

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）时，选择对应目标语言的 CSV 直接作为术语库导入即可。
- 文件名即类目名，可按需合并；如需「全部类目合并为单一文件」或增加 `src_lng`（源语言）列，可随时生成。

## 生成说明

本目录由同级 `tools/build_main_glossary.js` 从 [genshin-db](https://github.com/theBowja/genshin-db) 源码生成：

```bash
node tools/build_main_glossary.js
```

该脚本会在输出目录写出全部 14 个语言文件夹、27 个 CSV，以及统计元数据 `glossary_counts.json`；
仓库内保存的那一份统计元数据位于 `tools/glossary_counts.json`。本 README 的表格由 `tools/readme_main.js` 生成。
