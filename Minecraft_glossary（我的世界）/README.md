# 《我的世界》Minecraft 翻译术语库 / Minecraft Terminology Database / Minecraft 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本目录是《我的世界》（Minecraft）的多语言翻译术语库，取自 **Minecraft Java 版官方语言文件**，覆盖方块、物品、实体、生物群系、魔咒、状态效果、进度、字幕、界面与设置等 34 个类目，共 **14 种目标语言**、**1,420,443** 行对照；另有 Wiki 译名标准化补充词库 2 种目标语言、**10,314** 行对照。主词库译文即游戏内官方本地化文本，属于**官方本地化资料而非二次翻译**；补充词库取自 Minecraft Wiki 的译名标准化页面，与 Crowdin 上已确定的官方方案保持一致，可对照取用。全部术语以 `source,target,tgt_lng` 三列 CSV 存放，可直接导入沉浸式翻译等术语工具。

## 使用方法

1. **单文件下载**：进入对应语言目录（例如 `minecraft-glossary/zh-CN/`，系统与文本类目在该语言目录的 `extra/` 子文件夹内），下载所需的 `blocks.csv` / `items.csv` / `extra/subtitles.csv` 等单个类目文件，即可直接导入沉浸式翻译等支持术语表的工具。
2. **整个语言目录打包下载**：把某一个语言目录（如 `minecraft-glossary/ja-JP/`）整体下载下来，按需选用其中的类目文件；补充词库则在 `minecraft-glossary-supplement/zh-CN/`、`minecraft-glossary-supplement/zh-TW/` 两个目录中。
3. **克隆整个仓库自行复现**：配合 `tools/` 下的脚本与本文档「使用的相关内容」中列出的上游仓库，可自行重新生成全部 CSV 与元数据（见「生成与复现」）。

## 目录结构

```text
Minecraft_glossary（我的世界）/
├── README.md                     # 本文件（简体中文）
├── README_EN.md                  # English
├── README_JP.md                  # 日本語
├── minecraft-glossary/           # 主词库：14 种目标语言 × 34 个类目
│   ├── README.md                 # 主词库中文说明（由 tools/make_readme.py 生成）
│   ├── zh-CN/                    # 目标语言 = 简体中文
│   │   ├── blocks.csv            # 主类目（游戏内容），19 个文件
│   │   ├── items.csv
│   │   ├── ...
│   │   └── extra/                # 系统与文本类目，15 个文件
│   │       ├── subtitles.csv
│   │       └── ...
│   ├── zh-TW/                    # 目标语言 = 繁體中文
│   ├── en-US/                    # English
│   ├── ja-JP/                    # 日本語
│   ├── ko-KR/                    # 한국어
│   ├── fr-FR/                    # Français
│   ├── de-DE/                    # Deutsch
│   ├── es-ES/                    # Español
│   ├── ru-RU/                    # Русский
│   ├── pt-BR/                    # Português
│   ├── it-IT/                    # Italiano
│   ├── tr-TR/                    # Türkçe
│   ├── th-TH/                    # ภาษาไทย
│   └── vi-VN/                    # Tiếng Việt
├── minecraft-glossary-supplement/   # 补充词库（Wiki 译名标准化）：2 种目标语言 × 13 个类目
│   ├── README.md                 # 补充词库中文说明（由 tools/make_readme.py 生成）
│   ├── zh-CN/                    # 目标语言 = 简体中文
│   └── zh-TW/                    # 目标语言 = 繁體中文
└── tools/                        # 生成脚本与生成元数据
    ├── build_glossary.py         # 由官方语言文件生成主词库
    ├── build_wiki_supplement.py  # 由 Wiki 译名标准化页面生成补充词库
    ├── make_readme.py            # 生成两个子库的 README.md
    ├── verify_output.py          # 校验 CSV 表头、重复行与行数统计
    ├── glossary_counts.json      # 主词库各语言、各类目条目数统计
    └── supplement_counts.json    # 补充词库各语言、各类目条目数统计
```

每个语言目录下除 19 个主类目 CSV 外，都有一个 `extra/` 子文件夹存放 15 个系统与文本类目 CSV（共 34 个 CSV / 语言），CSV 文件名即类目名。

## 数据概览

### 语料规模

| 术语库 | 目标语言 | 类目 | CSV 文件 | 数据行数（词条 × 源语言） |
| --- | --- | --- | --- | --- |
| 主词库 `minecraft-glossary/` | 14 | 34 | 476 | 1,420,443 |
| 补充词库 `minecraft-glossary-supplement/` | 2 | 13 | 26 | 10,314 |
| **合计** | **16 个语言目录** |  | **502** | **1,430,757** |

### 主词库各语言行数（每语言 34 个文件）

| 语言 | 语言（名称） | 数据行数 |
| --- | --- | --- |
| `zh-CN` | 简体中文 | 101,247 |
| `zh-TW` | 繁體中文 | 101,215 |
| `en-US` | English | 101,550 |
| `ja-JP` | 日本語 | 101,553 |
| `ko-KR` | 한국어 | 101,279 |
| `fr-FR` | Français | 101,569 |
| `de-DE` | Deutsch | 101,431 |
| `es-ES` | Español | 101,647 |
| `ru-RU` | Русский | 101,629 |
| `pt-BR` | Português | 101,489 |
| `it-IT` | Italiano | 101,580 |
| `tr-TR` | Türkçe | 101,665 |
| `th-TH` | ภาษาไทย | 101,264 |
| `vi-VN` | Tiếng Việt | 101,325 |
| **合计** |  | **1,420,443** |

### 主词库主类目（游戏内容，19 个）

「词条数」指该分类在官方语言文件里对应的**游戏名称对象数**；「行数」为简体中文目录内该类目 CSV 的数据行数。一个条目会以其余 13 种语言分别作为 `source` 各生成一行，因此两个数字不同。

| 类目 | 文件 | 说明 | 词条数 | zh-CN 行数 |
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

### 主词库 `extra/` 类目（系统与文本，15 个）

| 类目 | 文件 | 说明 | 词条数 | zh-CN 行数 |
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

### 补充词库类目（Wiki 译名标准化，13 个）

数字取自 `tools/supplement_counts.json`。「词条数」= 按英文名去重后的标准中文名条数；「行数」= 该语言目录内该类目 CSV 的数据行数。

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

补充词库两个语言目录各 13 个 CSV、各 **5,157** 行；其分类体系按 Wiki 页面章节划分，与主词库的 34 个类目名称与口径都不同，两边不能按类目名直接合并。

## 使用的相关内容

| 来源仓库 / 页面 | 用途 |
| --- | --- |
| [misode/mcmeta](https://github.com/misode/mcmeta) | 主词库数据源：`assets` 分支的 `assets/minecraft/lang/<locale>.json`，即 Minecraft Java 版官方语言文件，14 种目标语言全部取自这里 |
| [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) | 参考其 `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` 等分类方式划分类目；该库的 `particles`、`sounds` 在官方语言文件中只有内部 ID、没有本地化名称，故未单独成类 |
| [Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) | 补充词库数据源：Wiki 标准译名（简体中文 / 繁体中文两种变体分别抓取后合并），与 Crowdin 上已确定的官方本地化方案保持一致，未确定时暂用游戏内原文 |
| [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) | 按版本分支存放的材质资源库，本库以其语言文件结构作为校对参考 |

## 生成与复现

```bash
# 1) 主词库：由官方语言文件生成 14 种语言 × 34 个类目的 CSV
python tools/build_glossary.py

# 2) 补充词库：由 Wiki 译名标准化页面的两种变体生成 zh-CN / zh-TW 的 13 个类目
python tools/build_wiki_supplement.py

# 3) 由两个元数据文件重新生成两份中文子库 README
python tools/make_readme.py

# 4) 校验：逐行检查表头、tgt_lng、空值、重复行，并核对元数据里的行数
python tools/verify_output.py
```

说明：

- 两个生成脚本都**读取脚本外的源数据目录**（脚本默认 `SRC_DIR = E:\Download\BT\Codex_input`，可用文本编辑器改成自己的路径）：
  `build_glossary.py` 需要 `mcmeta_lang/<locale>.json`（从 mcmeta 的 `assets` 分支取得），
  `build_wiki_supplement.py` 需要源目录下的 wiki_std_cn.json / wiki_std_tw.json（该页面的 `action=parse&prop=text&variant=zh-cn|zh-tw` 渲染结果，文件名见 `tools/build_wiki_supplement.py` 的 `SRC_DIR` 定义）。
  这些源数据不属于本仓库，需自行准备。
- 生成元数据写在 `tools/glossary_counts.json` 与 `tools/supplement_counts.json`，脚本**不会**再把元数据写进术语库数据目录。
- 全流程为**纯 Python 标准库**（`json` / `os` / `csv` / `re` / `html` / `collections`），无需 Node.js、无需第三方包，Python 3.8+ 即可。
- 脚本通过自身位置推导游戏根目录，执行时一律带 `tools/` 前缀，例如在游戏目录下运行 `python tools/verify_output.py`。
- CSV 一律为 **UTF-8（含 BOM）**、**CRLF** 换行、首行表头 `source,target,tgt_lng`，字段含逗号或引号时按 RFC 4180 转义；说明用的 Markdown 文件为 UTF-8（无 BOM）。
- 数据清洗规则：与目标语言完全同形的行删除（例如各语言均未翻译的曲名、专有名词）；同一条目产生的重复行合并；空值 / 缺失翻译不生成空行；格式化占位符（`%s`、`%1$s`、`%%`）原样保留；同一键在不同语言下的重复译文按 `source`+`target` 去重。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
