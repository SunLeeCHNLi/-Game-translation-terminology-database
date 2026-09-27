# 星布谷地（Petit Planet）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放（**扁平结构**，不再有分类子目录）。

## 数据来源

- 官方本地化文件：[planet.hoyoverse.com](https://planet.hoyoverse.com/zh-cn/home) 官方网站多语言本地化文件
  —— 15 种语言使用**同一本地化 Key**（共 443 个 Key），各语言之间可直接一一对齐
- 官方公告：HoYoLAB 官方公告（`gids=10`）—— Coziness Test / Stardrift Test / Final Beta Test，同为 15 种语言
- 社区数据库：[petitplanet.life](https://petitplanet.life/) —— 仅提供**英文名称**，以 `source = target`（均为英文）记录，未编造译名
- 新闻源确认：[c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) —— 仅用于定位官方新闻源（`Game.PLANET = 10`），其语言字段不是游戏本地化数据

## 目录结构

```text
petit-planet-glossary/
├── zh-CN/                    # 目标语言 = 简体中文（扁平：CSV 直接放在语言目录下）
├── zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/
├── ru-RU/  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
├── _master/                  # 各语言的 index.csv 与说明（<lang>__index.csv）
├── multilingual/             # 十五语并排总表
└── README.md
```

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Petit Planet | 星布谷地 | zh-CN |
| プチプラネット | 星布谷地 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它某一语言**的原文。
另每个类目还有一个 `*__terms.csv`（`id,term,src_table`），`id` 为可溯源的官方本地化 Key。

## 类目

`bugs`、`cooking`、`event`、`fish`、`furniture`、`game_title`、`item`、`location`、`material`、`neighbor`、`neighbor_interaction`、`plants`、`shop`、`shore`、`test_version`、`title_tag`、`ui`、`world_term`

## 语言与规模

| 语言文件夹 | 语言 | 类目数 | 对照行 |
| --- | --- | ---: | ---: |
| `zh-CN` | 简体中文 | 7 | 1,488 |
| `zh-TW` | 繁體中文 | 7 | 1,481 |
| `en-US` | English | 18 | 5,379 |
| `ja-JP` | 日本語 | 7 | 1,417 |
| `ko-KR` | 한국어 | 7 | 1,418 |
| `fr-FR` | Français | 7 | 1,411 |
| `de-DE` | Deutsch | 7 | 1,425 |
| `es-ES` | Español | 7 | 1,411 |
| `ru-RU` | Русский | 7 | 1,408 |
| `pt-PT` | Português | 7 | 1,422 |
| `it-IT` | Italiano | 7 | 1,408 |
| `tr-TR` | Türkçe | 7 | 1,411 |
| `th-TH` | ภาษาไทย | 7 | 1,418 |
| `vi-VN` | Tiếng Việt | 7 | 1,418 |
| `id-ID` | Bahasa Indonesia | 7 | 1,411 |
| **合计** | | | **25,326** |

## 已知限制

- 游戏客户端多语言字符串尚未公开，官方译文来自官方网站本地化文件与官方公告；官方网站文案可能属于 **Web Only** 层级。
- 道具、家具、鱼类、昆虫、食谱、商店等目前仅有 petitplanet.life 的英文名称，缺少官方多语言对照。
- 《星布谷地》仍在测试阶段，本库以当前版本（Final Beta Test，连接测试）为准。
