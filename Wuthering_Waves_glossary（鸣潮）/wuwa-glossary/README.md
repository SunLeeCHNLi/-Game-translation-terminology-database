# 鸣潮（Wuthering Waves）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放。

## 数据来源

- 文本主源：[Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data)（游戏 3.6.0）
  - `Textmaps/<lang>/multi_text/MultiText.json`：以文本键（如 `RoleInfo_1402_Name`）索引的全语言文本表
- 文本补充：[Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData)（游戏 3.1.0）
  - `TextMap/<lang>/MultiText.json`：补齐少量 3.6 版已移除的文本键
- 类目划分：Arikatsu `BinData/` + Dimbreath `ConfigDB/` 中的字段引用（文本键 → 实体表 → 类目）
- 参考实现：[My-Denia/wuwa-translate-bot](https://github.com/My-Denia/wuwa-translate-bot)（类目字段与文本清洗）、[CM-Edelweiss/WutheringWavesUID](https://github.com/CM-Edelweiss/WutheringWavesUID)（词条核对）

## 目录结构

```
wuwa-glossary/
├── zh-CN/                    # 目标语言 = 简体中文
│   ├── characters.csv
│   ├── items.csv
│   └── ...                   # 共 23 个类目文件
├── zh-TW/
├── en-US/ ... th-TH/         # 共 10 个语言文件夹
└── _counts.json              # 各语言、各类目的条目数统计
```

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它任一语言**的原文。
即每个语言文件夹内，同一条目会以其余 9 种语言分别作为 `source` 各出现一行（重复行与同形行已合并）。

## 语言代码

| 语言文件夹 | 语言 | 游戏文本目录 |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `Textmaps/zh-Hans/` |
| `zh-TW` | 繁體中文 | `Textmaps/zh-Hant/` |
| `en-US` | English | `Textmaps/en/` |
| `ja-JP` | 日本語 | `Textmaps/ja/` |
| `ko-KR` | 한국어 | `Textmaps/ko/` |
| `fr-FR` | Français | `Textmaps/fr/` |
| `de-DE` | Deutsch | `Textmaps/de/` |
| `es-ES` | Español | `Textmaps/es/` |
| `pt-BR` | Português | `Textmaps/pt/` |
| `th-TH` | ภาษาไทย | `Textmaps/th/` |

> **未收录的语言**：`ru-RU`（Русский）、`id-ID`（Bahasa Indonesia）、`vi-VN`（Tiếng Việt）在上游两个数据仓库中均为**空占位文件**（3.6.0 与 3.1.0 版均是如此），本词库无法提供；`it-IT`、`tr-TR` 并非鸣潮官方支持的文本语言。
> 若后续上游补齐，执行下方「重新生成」命令即可自动纳入。

## 类目与条目数

「条目」指该分类下去重后的词条数（一个词条 = 游戏中的一条文本键）；「行数」为 **zh-CN** 文件夹内该类目 CSV 的数据行数。

| 类目 | 文件 | 说明 | 条目数 | zh-CN 行数 |
| --- | --- | --- | --- | --- |
| 角色名称 | `characters.csv` | 角色、漂泊者身份、角色档案字段 | 1,230 | 5,181 |
| 武器名称 | `weapons.csv` | 武器名称与武器图鉴文本 | 820 | 3,072 |
| 声骸 | `echoes.csv` | 声骸（残象）名称、图鉴与声骸对战文本 | 1,000 | 6,091 |
| 技能 | `skills.csv` | 共鸣技能、技能描述、技能树 | 5,344 | 30,340 |
| 共鸣链 | `resonant-chains.csv` | 共鸣链节点名称与描述 | 784 | 6,116 |
| 任务 | `quests.csv` | 任务/章节名称、任务描述、每日委托 | 2,807 | 14,529 |
| 关卡与挑战 | `dungeons.csv` | 副本、深塔、全息、挑战关卡名称与说明 | 1,910 | 12,157 |
| 地区与地图 | `regions.csv` | 地区、地图标记、地理图鉴 | 2,229 | 16,143 |
| 阵营与势力 | `factions.csv` | 国家与阵营名称 | 8 | 44 |
| 道具与材料 | `items.csv` | 道具、材料、合成/烹饪/锻造配方、商店 | 8,384 | 54,388 |
| 怪物与生物 | `monsters.csv` | 怪物与生物图鉴 | 685 | 4,542 |
| NPC 与说话人 | `npcs.csv` | NPC 与说话人名称 | 14,172 | 64,138 |
| 成就 | `achievements.csv` | 成就名称与描述 | 2,563 | 22,173 |
| 活动与玩法 | `activities.csv` | 活动、肉鸽、钓鱼、陷阱防御等玩法文本 | 9,531 | 63,487 |
| 增益与效果 | `buffs.csv` | 增益/减益效果名称与描述 | 270 | 2,034 |
| 角色语音 | `voice-lines.csv` | 角色语音台词与羁绊故事 | 7,374 | 31,692 |
| 档案与读物 | `archives.csv` | 档案、读物、调查记录 | 839 | 6,574 |
| 术语与百科 | `terms.csv` | 游戏内术语表、属性与元素反应 | 1,672 | 12,387 |
| 系统文本 | `system.csv` | 系统提示、错误码、确认框、功能菜单 | 9,756 | 65,502 |
| UI 文本 | `ui.csv` | 界面预制文本、快捷键、动态页签 | 13,866 | 78,131 |
| 教程与引导 | `tutorials.csv` | 教程、引导、战斗提示 | 6,253 | 31,741 |
| 剧情文本 | `story.csv` | 剧情标题、任务目标、场景叙事文本 | 29,841 | 102,144 |
| 其他 | `other.csv` | 未归类文本 | 1,892 | 13,340 |

## 各语言总行数

| 语言 | 文件数 | 数据行数 | 体积 |
| --- | --- | --- | --- |
| `zh-CN` | 23 | 645,946 | 55.6 MiB |
| `zh-TW` | 23 | 645,529 | 55.7 MiB |
| `en-US` | 23 | 645,837 | 58.6 MiB |
| `ja-JP` | 23 | 648,414 | 63.4 MiB |
| `ko-KR` | 23 | 646,888 | 63.4 MiB |
| `fr-FR` | 23 | 654,776 | 63.8 MiB |
| `de-DE` | 23 | 652,349 | 63.0 MiB |
| `es-ES` | 23 | 646,691 | 61.8 MiB |
| `pt-BR` | 23 | 648,957 | 62.0 MiB |
| `th-TH` | 23 | 644,759 | 91.4 MiB |
| **合计** | **230** | **6,480,146** | **638.6 MiB** |

> 同一文本可能同时属于多个类目（例如某武器说明同时出现在 `weapons` 与 `items`），因此各类目行数相加会大于全局去重后的条目数，属正常现象。

## 数据清洗说明

源数据中的以下内容已在生成时处理：

| 源数据写法 | 处理方式 | 示例 |
| --- | --- | --- |
| `<color=...>`、`<size=...>`、`<te href=...>`、`<i>`、`<b>` 等富文本标签 | 剔除标签 | `<color=Highlight>共鸣解放</color>` → `共鸣解放` |
| `{Male=…;Female=…}` 性别分支 | 取男性形态 | `{Male=大哥哥;Female=大姐姐}` → `大哥哥` |
| `{M#…}{F#…}` 性别变体 | 取男性形态 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 字面量 `\n` | 还原为换行 | `第一行\n第二行` → 两行 |
| `dnt/` 前缀（do not translate） | 去除前缀 | `dnt/测试` → `测试` |
| 原文与译文完全相同的行 | 不输出 | — |

## 收录范围说明

- **默认不收录逐句剧情对白**（说话人台词、字幕，约 17 万条/语言），否则单语言体积会从约 60 MiB 增至约 230 MiB。
  需要台词库时执行：`python tools/build_wuwa_glossary.py --out <目录> --with-dialogue`（会额外生成 `dialogue.csv`）。
- 超长文本按类目阈值截断，阈值定义在 `tools/wuwa_config.py` 的 `MAX_LEN`（例如 `ui` 60 字、`story` 200 字、`items` 250 字、`archives` 400 字）。
- 文本键到类目的归属来自游戏配置表的字段引用；少量未被任何配置表引用的键按命名规则兜底归类。

## 重新生成

需要先准备两个数据仓库（`WutheringWaves_Data`、`WutheringData`）到 `E:\Download\BT\Codex_input`，或通过环境变量 `WUWA_DATA_ROOT` 指定其他位置。

```bash
# 全量生成（默认）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary

# 只生成部分类目（体积更小、匹配更精准）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --only characters,weapons,echoes,skills,resonant-chains

# 压缩长文本阈值（例如只保留短词条，体积约为默认的 1/3）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --len-scale 0.5

# 额外生成逐句剧情对白 dialogue.csv（体积很大，约 +170 MiB/语言）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --with-dialogue
```

其他参数：`--dry-run`（只统计不写文件）、`--rebuild-cache`（重新扫描 `BinData`/`ConfigDB`，默认结果会缓存到 `tools/_cfgmap_cache.pkl`）。

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）或沉浸式翻译类软件时，选择对应目标语言的 CSV 直接作为术语库导入即可。
- 文件名即类目名，可按需合并；按领域拆分（如仅导入 `characters.csv` + `weapons.csv` + `skills.csv`）可显著提升匹配精度。
