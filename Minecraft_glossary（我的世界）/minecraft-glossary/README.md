# 我的世界（Minecraft）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放；系统与文本类目统一放在各语言的 `extra/` 子文件夹内。

## 数据来源

- 主词库：**Minecraft Java 版官方语言文件**，取自 [misode/mcmeta](https://github.com/misode/mcmeta) 的 `assets` 分支（`assets/minecraft/lang/<locale>.json`），覆盖全部 14 种目标语言。
- 类目结构参照 [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) 中 `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` 等分类方式划分；该库中的 `particles`、`sounds` 在官方语言文件中只有内部 ID、没有本地化名称，故未单独成类。
- 补充词库：见同级目录 `minecraft-glossary-supplement/`（来源 [Minecraft Wiki 译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)），额外提供 Wiki 标准译名，覆盖简体中文 / 繁体中文。
- 图片资源库 [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) 按版本分支存放材质，本词库以其语言文件结构作为校对参考。

## 目录结构

```
minecraft-glossary/
├── zh-CN/                    # 目标语言 = 简体中文
│   ├── blocks.csv
│   ├── items.csv
│   ├── ...
│   └── extra/                # 系统与文本类目
│       ├── subtitles.csv
│       └── ...
├── zh-TW/
├── en-US/ ... vi-VN/         # 共 14 个语言文件夹
└── _counts.json              # 各语言、各类目的条目数统计
```

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Enterprise | 企业 | zh-CN |
| エンタープライズ | 企业 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它任一语言**的原文。
即每个语言文件夹内，同一条目会以其余 13 种语言分别作为 `source` 各出现一行（重复行与同形行已合并）。

## 语言代码

| 语言文件夹 | 语言 | Minecraft 语言文件 |
| --- | --- | --- |
| 语言文件夹 | 语言 | locale |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `zh_cn` |
| `zh-TW` | 繁體中文 | `zh_tw` |
| `en-US` | English | `en_us` |
| `ja-JP` | 日本語 | `ja_jp` |
| `ko-KR` | 한국어 | `ko_kr` |
| `fr-FR` | Français | `fr_fr` |
| `de-DE` | Deutsch | `de_de` |
| `es-ES` | Español | `es_es` |
| `ru-RU` | Русский | `ru_ru` |
| `pt-BR` | Português | `pt_br` |
| `it-IT` | Italiano | `it_it` |
| `tr-TR` | Türkçe | `tr_tr` |
| `th-TH` | ภาษาไทย | `th_th` |
| `vi-VN` | Tiếng Việt | `vi_vn` |

## 类目与条目数

「条目」指该分类下的**去重词条数**（一个词条 = 游戏中的一个名称对象）；「行数」为简体中文文件夹内该类目 CSV 的数据行数。

### 主类目（游戏内容）

| 类目 | 文件 | 说明 | 词条数 | 每语言行数（zh-CN） |
| --- | --- | --- | --- | --- |
| blocks | `blocks.csv` | 方块 | 1975 | 25426 |
| items | `items.csv` | 物品 | 803 | 9061 |
| entities | `entities.csv` | 实体 | 219 | 2582 |
| biomes | `biomes.csv` | 生物群系 | 67 | 835 |
| enchantments | `enchantments.csv` | 魔咒 | 54 | 553 |
| effects | `effects.csv` | 状态效果 | 42 | 514 |
| instruments | `instruments.csv` | 乐器 | 8 | 98 |
| materials | `materials.csv` | 盔甲纹饰材料 | 11 | 143 |
| paintings | `paintings.csv` | 画 | 104 | 315 |
| attributes | `attributes.csv` | 属性 | 83 | 555 |
| item-groups | `item-groups.csv` | 物品栏分类 | 16 | 198 |
| jukebox-songs | `jukebox-songs.csv` | 唱片曲目 | 22 | 42 |
| trim-patterns | `trim-patterns.csv` | 盔甲纹饰图案 | 18 | 234 |
| colors | `colors.csv` | 颜色 | 16 | 184 |
| statistics | `statistics.csv` | 统计 | 88 | 1143 |
| maps | `maps.csv` | 地图 | 33 | 422 |
| music | `music.csv` | 音乐曲目 | 70 | 192 |
| sound-categories | `sound-categories.csv` | 声音分类 | 11 | 133 |
| game-modes | `game-modes.csv` | 游戏模式 | 6 | 77 |

### `extra/` 类目（系统与文本）

| 类目 | 文件 | 说明 | 词条数 | 每语言行数（zh-CN） |
| --- | --- | --- | --- | --- |
| subtitles | `extra/subtitles.csv` | 字幕 | 1023 | 12407 |
| death-messages | `extra/death-messages.csv` | 死亡消息 | 106 | 1334 |
| advancement-titles | `extra/advancement-titles.csv` | 进度标题 | 127 | 1603 |
| advancement-descriptions | `extra/advancement-descriptions.csv` | 进度描述 | 127 | 1641 |
| gamerules | `extra/gamerules.csv` | 游戏规则 | 117 | 1490 |
| commands | `extra/commands.csv` | 命令与参数 | 856 | 10758 |
| gui | `extra/gui.csv` | 界面文本 | 581 | 6604 |
| options | `extra/options.csv` | 设置与按键 | 754 | 8165 |
| multiplayer | `extra/multiplayer.csv` | 多人游戏 | 173 | 2013 |
| realms | `extra/realms.csv` | Realms | 426 | 4962 |
| world-management | `extra/world-management.csv` | 世界管理 | 294 | 3578 |
| resource-packs | `extra/resource-packs.csv` | 资源包与数据包 | 62 | 761 |
| telemetry | `extra/telemetry.csv` | 遥测 | 70 | 897 |
| dev-tools | `extra/dev-tools.csv` | 开发与测试工具 | 144 | 1811 |
| misc | `extra/misc.csv` | 其他 | 53 | 516 |

## 各语言总行数

| 语言 | 语言（名称） | 文件数 | 数据行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 34 | 101,247 |
| `zh-TW` | 繁體中文 | 34 | 101,215 |
| `en-US` | English | 34 | 101,550 |
| `ja-JP` | 日本語 | 34 | 101,553 |
| `ko-KR` | 한국어 | 34 | 101,279 |
| `fr-FR` | Français | 34 | 101,569 |
| `de-DE` | Deutsch | 34 | 101,431 |
| `es-ES` | Español | 34 | 101,647 |
| `ru-RU` | Русский | 34 | 101,629 |
| `pt-BR` | Português | 34 | 101,489 |
| `it-IT` | Italiano | 34 | 101,580 |
| `tr-TR` | Türkçe | 34 | 101,665 |
| `th-TH` | ภาษาไทย | 34 | 101,264 |
| `vi-VN` | Tiếng Việt | 34 | 101,325 |
| **合计** |  | **476** | **1,420,443** |

## 数据清洗说明

| 处理项 | 处理方式 |
| --- | --- |
| 与目标语言完全同形的行 | 删除（例如各语言均未翻译的曲名、专有名词） |
| 同一条目产生的重复行 | 合并 |
| 空值 / 缺失翻译 | 跳过该语言，不生成空行 |
| 格式化占位符（`%s`、`%1$s`、`%%`） | 原样保留 |
| 同一键在不同语言下的重复译文 | 按 `source`+`target` 去重 |

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）时，选择对应目标语言的 CSV 直接作为术语库导入即可。
- 文件名即类目名，可按需合并；如需「全部类目合并为单一文件」或增加 `src_lng`（源语言）列，可随时生成。
- 重新生成词库：先准备官方语言文件（`lang/<locale>.json`），再运行 `tools/build_glossary.py`；前缀到类目的完整映射见该脚本中的 `CATEGORIES` 表。
- 官方语言文件共有 144 种语言变体，本词库按需选取其中 14 种；若需其它语言，在 `tools/build_glossary.py` 的 `LANG_FILES` 中补充后重新生成即可。
