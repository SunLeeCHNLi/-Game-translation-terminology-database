# 《鸣潮》Wuthering Waves 翻译术语库 / Wuthering Waves Terminology Database / 鳴潮 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库收录开放世界动作 RPG《鸣潮》（Wuthering Waves / 鳴潮）的专有名词对照表，覆盖角色名称、武器、声骸、技能、共鸣链、任务、关卡、地区、阵营、道具、怪物、NPC、成就、活动、增益、角色语音、档案、术语、系统文本、UI 文本、教程、剧情文本、其他共 **23 个类目**。全部类目合计 **123,230** 条去重词条，按目标语言拆分为 **10** 套独立术语库（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `fr-FR` / `de-DE` / `es-ES` / `pt-BR` / `th-TH`），合计 **230 个 CSV / 6,480,146 行对照**（约 638.6 MiB）。译文全部取自官方客户端多语言文本，按同一文本键对齐，属于**官方本地化**而非二次翻译。

## 使用方法

1. **单文件下载**：进入 `wuwa-glossary/` 下对应语言目录（例如 `zh-CN/`），按需要下载 `characters.csv`、`items.csv` 等类目文件，直接导入沉浸式翻译、Trados、memoQ、Phrase 等术语工具即可，无需转换。
2. **整个语言目录打包下载**：若需要某语言的全部类目，下载该语言目录下的 23 个 CSV（约 55–92 MiB）。
3. **克隆整个仓库自行复现**：`git clone` 本仓库后，配合 `tools/` 下的生成脚本，以及脚本引用的两个上游数据仓库（`WutheringWaves_Data`、`WutheringData`）源码，即可从原始数据重新生成全部 CSV。

> 文件名即类目名，可按需合并使用；按领域拆分导入（例如只导入 `characters.csv` + `weapons.csv` + `skills.csv`）可显著提升术语匹配精度。

## 目录结构

```text
Wuthering_Waves_glossary（鸣潮）/
  README.md                本说明（简体中文）
  README_EN.md             English
  README_JP.md             日本語
  wuwa-glossary/           术语库数据（10 套，按目标语言拆分）
    README.md              子库详细说明（类目表、清洗规则、重新生成命令）
    zh-CN/                 以简体中文为目标语言，23 个类目 CSV
    zh-TW/                 以繁體中文为目标语言
    en-US/                 以 English 为目标语言
    ja-JP/                 以日本語为目标语言
    ko-KR/                 以한국어为目标语言
    fr-FR/                 以 Français 为目标语言
    de-DE/                 以 Deutsch 为目标语言
    es-ES/                 以 Español 为目标语言
    pt-BR/                 以 Português 为目标语言
    th-TH/                 以ภาษาไทย为目标语言
  tools/                   批处理脚本与生成元数据
    build_wuwa_glossary.py 主生成脚本（文本键 → 类目 CSV）
    wuwa_classify.py       文本键归类到类目
    wuwa_config.py         类目阈值与参数配置
    _counts.json           各语言、各类目的条目数与体积统计
    _cfgmap_cache.pkl      文本键 → 类目映射缓存（可由 --rebuild-cache 重建）
```

每个语言目录的结构完全一致，均为 **23 个类目 CSV**，不含子目录；每个语言目录另有 `README.md`（该语言）与 `README_zh-CN.md`（简体中文）两份说明。

## 数据概览

### 各语言规模

| 语言代码 | 语言 | 文件数 | 数据行数 | 体积 |
| --- | --- | ---: | ---: | ---: |
| `zh-CN` | 简体中文 | 23 | 645,946 | 55.6 MiB |
| `zh-TW` | 繁體中文 | 23 | 645,529 | 55.7 MiB |
| `en-US` | English | 23 | 645,837 | 58.6 MiB |
| `ja-JP` | 日本語 | 23 | 648,414 | 63.4 MiB |
| `ko-KR` | 한국어 | 23 | 646,888 | 63.4 MiB |
| `fr-FR` | Français | 23 | 654,776 | 63.8 MiB |
| `de-DE` | Deutsch | 23 | 652,349 | 63.0 MiB |
| `es-ES` | Español | 23 | 646,691 | 61.8 MiB |
| `pt-BR` | Português | 23 | 648,957 | 62.0 MiB |
| `th-TH` | ภาษาไทย | 23 | 644,759 | 91.4 MiB |
| **合计** | | **230** | **6,480,146** | **638.6 MiB** |

> 数字取自 `tools/_counts.json`，并已逐语言用符合 RFC 4180 的 CSV 解析器重新统计核对一致。

### 类目与条目数

「条目」指该语言文件中归入该类目的**去重文本键**（一个条目 = 游戏中的一条文本键，与目标语言无关）；「行数」为 **zh-CN** 目录内该类目 CSV 的数据行数。

| 类目 | 文件 | 说明 | 条目数 | zh-CN 行数 |
| --- | --- | --- | ---: | ---: |
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
| **合计** | | | **123,230** | **645,946** |

> 同一文本可能同时属于多个类目（例如某武器说明同时出现在 `weapons` 与 `items`），因此各类目行数相加会大于全局去重后的条目数，属正常现象。

### 文件格式

每个类目 CSV 均为三列，**UTF-8（含 BOM）** 编码、**CRLF** 换行，含逗号/引号/换行的字段按 RFC 4180 加引号转义（Excel 双击可直接打开）。

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

- `target`：该语言目录对应的目标语言译文；
- `tgt_lng`：目标语言标签，等于所在目录名；
- `source`：同一文本键在**其余 9 种语言**中的写法，因此同一条目会以每种源语言各出现一行（重复行与同形行已合并）。

### 未收录的语言

`ru-RU`（Русский）、`id-ID`（Bahasa Indonesia）、`vi-VN`（Tiếng Việt）在上游两个数据仓库中均为**空占位文件**（3.6.0 与 3.1.0 版均是如此），无法提供；`it-IT`、`tr-TR` 并非鸣潮官方支持的文本语言。若上游后续补齐，重新执行生成命令即可自动纳入。

## 使用的相关内容

| 来源 | 用途 |
| --- | --- |
| [Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) | 文本主源（游戏 3.6.0）：`Textmaps/<lang>/multi_text/MultiText.json`，以文本键索引的全语言文本表；类目划分取自其 `BinData/` |
| [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) | 文本补充（游戏 3.1.0）：`TextMap/<lang>/MultiText.json`，补齐少量 3.6 版已移除的文本键；类目划分参考其 `ConfigDB/` |
| [My-Denia/wuwa-translate-bot](https://github.com/My-Denia/wuwa-translate-bot) | 参考实现：类目字段映射与文本清洗规则 |
| [CM-Edelweiss/WutheringWavesUID](https://github.com/CM-Edelweiss/WutheringWavesUID) | 参考实现：词条核对 |

## 生成与复现

需先把两个上游数据仓库准备到 `E:\Download\BT\Codex_input`，或通过环境变量 `WUWA_DATA_ROOT` 指定其他位置。

```bash
# 全量生成（默认，输出到 wuwa-glossary/）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary

# 只生成部分类目（体积更小、匹配更精准）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --only characters,weapons,echoes,skills,resonant-chains

# 压缩长文本阈值（例如只保留短词条，体积约为默认的 1/3）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --len-scale 0.5

# 额外生成逐句剧情对白 dialogue.csv（体积很大，约 +170 MiB/语言；默认不生成）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --with-dialogue
```

其他参数：`--dry-run`（只统计不写文件）、`--rebuild-cache`（重新扫描 `BinData`/`ConfigDB`，默认结果缓存到 `tools/_cfgmap_cache.pkl`）。

生成后会写出统计元数据 `_counts.json`；仓库内保存的那一份位于 `tools/_counts.json`。

## 说明

### 数据清洗

源数据中的以下内容已在生成时处理：

| 源数据写法 | 处理方式 | 示例 |
| --- | --- | --- |
| `<color=...>`、`<size=...>`、`<i>`、`<b>` 等富文本标签 | 剔除标签 | `<color=Highlight>共鸣解放</color>` → `共鸣解放` |
| `{Male=…;Female=…}` 性别分支 | 取男性形态 | `{Male=大哥哥;Female=大姐姐}` → `大哥哥` |
| `{M#…}{F#…}` 性别变体 | 取男性形态 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 字面量 `\n` | 还原为换行 | `第一行\n第二行` → 两行 |
| `dnt/` 前缀（do not translate） | 去除前缀 | `dnt/测试` → `测试` |
| 原文与译文完全相同的行 | 不输出 | — |

### 收录范围

- **默认不收录逐句剧情对白**（说话人台词、字幕，约 170,000 条/语言），否则单语言体积会从约 60 MiB 增至约 230 MiB；
- 超长文本按类目阈值截断，阈值定义在 `tools/wuwa_config.py` 的 `MAX_LEN`（例如 `ui` 60 字、`story` 200 字、`items` 250 字、`archives` 400 字）；
- 文本键到类目的归属来自游戏配置表的字段引用；少量未被任何配置表引用的键按命名规则兜底归类。

### 已知限制

- 类目为按配置表字段自动归类，个别词条可能归入相邻类目；
- 上游数据仓库的版本（3.6.0 / 3.1.0）决定收录范围，游戏更新后需重新生成；
- 不同地区版本之间可能存在译名差异，本库以所引用的上游数据版本为准。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《鸣潮》的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为本游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有，本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与《鸣潮》及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
