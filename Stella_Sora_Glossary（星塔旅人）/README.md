# 《星塔旅人》Stella Sora 翻译术语库 / Stella Sora Terminology Database / ステラソラ 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库收录手游《星塔旅人》（Stella Sora / ステラソラ）的专有名词对照表，覆盖角色名称、技能、潜能、唱片、道具、装备、敌人、关卡、活动、系统术语、UI 用语、剧情专有名词、阵营、地点、游戏机制共 15 个分类，五语并排总表合计 **12,292** 条词条。词条按目标语言拆分为 **5** 套独立术语库（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR`），每套各有 15 个分类文件与一份合并总表。译文取自游戏官方多语言文本（CN / EN / JP / KR / TW 五区客户端文本），各语言按同一文本键对齐，属于**官方本地化**而非二次翻译。

## 使用方法

1. **单文件下载**：进入 `stella-sora-glossary/` 下对应语言目录（例如 `stella-sora-glossary/zh-CN/`），下载 `character.csv` 之类的分类术语表，直接导入沉浸式翻译等术语工具即可，无需任何转换。
2. **整个语言目录打包下载**：若需要全部 15 个分类，下载该语言目录下的全部分类文件；各语言的合并总表位于 `stella-sora-glossary/_master/<lang>__all_glossary.csv`。
3. **克隆整个仓库自行复现**：`git clone` 本仓库后，配合已收录在 `tools/` 下的生成脚本，以及脚本文档字符串里引用的上游仓库源码，即可从原始数据重新生成全部 CSV。注意这两个脚本使用**外部绝对路径**，详见下方「生成与复现」。

## 目录结构

```text
Stella_Sora_Glossary（星塔旅人）/
  stella-sora-glossary/     单语言术语库容器
    README.md               子库说明、分类清单与数量
    zh-CN/                  以简体中文为目标语言的术语库
      README.md             本语言库说明（简体中文）
      character.csv         角色名称术语表（source,target,tgt_lng）
      character__terms.csv  本语言词条清单（id,term,src_table）
      skill.csv / skill__terms.csv
      ...                   共 15 组平铺分类 CSV
    zh-TW/                  同上结构（以繁體中文为目标语言）
    en-US/                  同上结构（以 English 为目标语言）
    ja-JP/                  同上结构（以日本語为目标语言）
    ko-KR/                  同上结构（以한국어为目标语言）
    _master/                各语言合并总表、索引与既有语言说明
      zh-CN__all_glossary.csv
      zh-CN__all_terms.csv
      zh-CN__index.csv
      zh-CN__README.md
      ...                   其余四种语言按 <lang>__<原文件名> 命名
    multilingual/           五语并排总表（内部结构保持不变）
      00_master/
        index.csv
        README.md
        source_mapping.csv
        StellaSora_all_terms.csv
      01_character/ … 15_terminology/
      StellaSora_Glossary.xlsx
  tools/                    生成脚本
    build_glossary.py       五语并排总表生成脚本（Python，读取外部数据目录）
    split_by_language.py    按目标语言拆分脚本（Python，读取外部总表目录）
  README.md                 本说明（简体中文）
  README_EN.md              英文说明
  README_JP.md              日文说明
```

每个语言目录的 15 个分类 CSV **直接平铺在该语言目录下**：`<cat>.csv` 为术语表，`<cat>__terms.csv` 为该语言的词条清单；语言目录内不再有 `NN_xxx/` 子目录。`stella-sora-glossary/multilingual/` 下的 `NN_xxx/` 保留五语并排原始总表的既有结构。
## 数据概览

各语言词条数与对照行数（取自各语言 `stella-sora-glossary/_master/<lang>__index.csv` 的 `TOTAL` 行，并与全部 15 个分类 CSV 的实际数据行数、`stella-sora-glossary/_master/<lang>__all_terms.csv` / `<lang>__all_glossary.csv` 的行数逐项核对一致）：

| 文件夹 | 语言 | 词条数 | 对照行数 |
| --- | --- | ---: | ---: |
| `stella-sora-glossary/zh-CN/` | 简体中文 | 12292 | 46279 |
| `stella-sora-glossary/zh-TW/` | 繁體中文 | 12292 | 46052 |
| `stella-sora-glossary/en-US/` | English | 12288 | 46032 |
| `stella-sora-glossary/ja-JP/` | 日本語 | 12289 | 46426 |
| `stella-sora-glossary/ko-KR/` | 한국어 | 12292 | 45950 |
| **合计（各语言目录简单相加）** | | **61453** | **230739** |

分类 × 目标语言的**词条数**矩阵（单元格为该语言目录下实际存在的词条数，取自各语言 `stella-sora-glossary/_master/<lang>__index.csv`）：

| 分类 | 主题 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 角色名称 | 287 | 287 | 287 | 287 | 287 |
| `skill.csv` | 技能名称 | 628 | 628 | 628 | 628 | 628 |
| `potential.csv` | 潜能名称 | 1457 | 1457 | 1457 | 1457 | 1457 |
| `disc.csv` | 唱片 / Disc | 234 | 234 | 234 | 234 | 234 |
| `item.csv` | 道具 | 558 | 558 | 558 | 558 | 558 |
| `equipment.csv` | 装备 | 15 | 15 | 15 | 15 | 15 |
| `enemy.csv` | 敌人 | 399 | 399 | 399 | 399 | 399 |
| `stage.csv` | 关卡 | 1019 | 1019 | 1019 | 1019 | 1019 |
| `event.csv` | 活动 | 581 | 581 | 581 | 581 | 581 |
| `system.csv` | 系统术语 | 1055 | 1055 | 1055 | 1055 | 1055 |
| `ui.csv` | UI术语 | 4248 | 4248 | 4244 | 4245 | 4248 |
| `story.csv` | 剧情专有名词 | 527 | 527 | 527 | 527 | 527 |
| `faction.csv` | 阵营 | 21 | 21 | 21 | 21 | 21 |
| `location.csv` | 地点 | 27 | 27 | 27 | 27 | 27 |
| `terminology.csv` | 游戏机制术语 | 1236 | 1236 | 1236 | 1236 | 1236 |
| **合计** | | **12292** | **12292** | **12288** | **12289** | **12292** |

分类 × 目标语言的**对照行数**矩阵（`<cat>.csv` 的数据行数）：

| 分类 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 979 | 977 | 973 | 1021 | 968 |
| `skill.csv` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `potential.csv` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `disc.csv` | 893 | 896 | 896 | 893 | 893 |
| `item.csv` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `equipment.csv` | 58 | 58 | 58 | 58 | 58 |
| `enemy.csv` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `stage.csv` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `event.csv` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `system.csv` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `ui.csv` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `story.csv` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `faction.csv` | 81 | 78 | 78 | 78 | 78 |
| `location.csv` | 98 | 98 | 98 | 96 | 96 |
| `terminology.csv` | 4660 | 4637 | 4630 | 4661 | 4649 |
| **合计** | **46279** | **46052** | **46032** | **46426** | **45950** |

五语并排总表 `stella-sora-glossary/multilingual/`（词条一条一行、五语并排）：

| 文件 | 行数 |
| --- | ---: |
| `stella-sora-glossary/multilingual/00_master/StellaSora_all_terms.csv` | 12292 |
| `stella-sora-glossary/multilingual/00_master/source_mapping.csv` | 219 |
| 15 个 `stella-sora-glossary/multilingual/NN_xxx/<cat>__terms.csv` 合计 | 12292 |
| 15 个 `stella-sora-glossary/multilingual/NN_xxx/<cat>.csv` 合计 | 147462 |

> 15 个分类的**词条数完全相同**（除 `ui.csv` 外），差异只出现在 `ui.csv`：官方 UI 文本里有个别条目在某个语区没有独立译文，因此 `en-US` 比 `zh-CN` 少 4 条、`ja-JP` 少 3 条。对照行数则因去重而普遍少于「词条数 × 4」。

## 使用的相关内容

| 来源 | 用途 |
| --- | --- |
| [Hiro420/StellaSoraData](https://github.com/Hiro420/StellaSoraData) | 游戏官方多语言文本库（CN / EN / JP / KR / TW 五区 `language/*` 文本表与 `bin/` 配置表）。`tools/build_glossary.py` 只读取这一份数据，是本库的主体来源 |
| [JforPlay/sstoy](https://github.com/JforPlay/sstoy) | 星塔旅人相关的数据解包 / 工具参考（仓库根 README 中一并列出的上游项目，非本库生成脚本的输入） |

各分类逐张来源表的映射明细见 `stella-sora-glossary/multilingual/00_master/source_mapping.csv` 与 `stella-sora-glossary/multilingual/00_master/README.md`。

## 生成与复现

```bash
# 1) 从上游多语言文本库生成五语并排总表
python tools/build_glossary.py

# 2) 按目标语言拆分，生成 5 套单语言术语库（同分类内重复的 source→target 对照行会被去重）
python tools/split_by_language.py

# 语法自检
python -m py_compile tools/build_glossary.py tools/split_by_language.py
```

> **重要：这两个脚本使用写死的外部绝对路径，不会读写本仓库。** 移动脚本目录（从原 `multilingual/00_master/tools/` 移到游戏根的 `tools/`）**不影响其运行**，因为两个脚本都不依赖自身所在目录：
>
> - `tools/build_glossary.py`：输入 `E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main`（上游文本库），输出 `E:\Download\BT\Codex_input\StellaSora_Glossary`；
> - `tools/split_by_language.py`：输入 / 输出根目录为 `E:\Download\BT\Codex_input\StellaSora_Glossary`，读取其中的 `multilingual/`，写出同级的 `zh-CN/`、`zh-TW/`、`en-US/`、`ja-JP/`、`ko-KR/`，并把 `_summary.json` 写到该外部根目录（**不是**本仓库）。
>
> 也就是说：本仓库里的 CSV 是那套外部生成管线跑完后**复制进来的快照**，用当前脚本原样执行不会更新本仓库；要复现，需要先把上游仓库放到上述外部路径（或按需修改脚本里的两个路径常量），跑完后再把结果复制回本仓库。截至最近一次核对，`E:\Download\BT\Codex_input\` 为空目录，两个上游目录都不存在。
>
> 另外，`stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx` 与 `stella-sora-glossary/multilingual/00_master/source_mapping.csv` 由管线之外的一次性步骤产出，**`tools/` 下的两个脚本都不会生成它们**。

## 说明

- 译文来自游戏官方多语言文本库 `StellaSoraData-main`（官方 CN / EN / JP / KR / TW 五区文本），各语言按同一文本键对齐，属于官方本地化，未经人工二次翻译；
- 五种语言的标签：`zh-CN` 简体中文、`zh-TW` 繁體中文、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어；同一个词条在五种语言中的原始文本键（`id`）完全一致；
- 每套术语库内的两个文件格式如下。

  **`<cat>.csv` —— 术语表（`source` / `target` / `tgt_lng`）**

  该语言的 `tgt_lng` 固定，`source` 是其余四种语言的写法，可直接导入术语工具：

  | source | target | tgt_lng |
  | --- | --- | --- |
  | Amber | 琥珀 | zh-CN |
  | コハク | 琥珀 | zh-CN |
  | 코하쿠 | 琥珀 | zh-CN |

  **`<cat>__terms.csv` —— 本语言词条清单（`id` / `term` / `src_table`）**

  | id | term | src_table |
  | --- | --- | --- |
  | Character.103.1 | 琥珀 | Character.json |

  `stella-sora-glossary/_master/<lang>__all_glossary.csv` 在 `source,target,tgt_lng` 前三列之前多一列 `category`；`stella-sora-glossary/_master/<lang>__all_terms.csv` 为 `category,category_label,id,term,src_table`；`stella-sora-glossary/_master/<lang>__index.csv` 为 `category,label,term_count,glossary_file,terms_file,target_language`；
- `stella-sora-glossary/multilingual/` 保留了五语并排的原始总表：`<cat>__terms.csv` 为 `id,zh-CN,en-US,ja-JP,ko-KR,zh-TW,src_table` 一条一行，`<cat>.csv` 则把 zh-CN / en-US / ja-JP / ko-KR 四种语言两两成对，每条词条最多展开成 12 行（4×3 有序语言对），因此无论以哪种语言作为源语言都能直接检索；同一份数据另有 Excel 工作簿 `stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx`（目录 + 15 个分类，共 16 个工作表，已核对存在）；
- **提取与筛选规则**（完整规则见 `stella-sora-glossary/multilingual/00_master/README.md`）：
  - 仅提取「名称 / 标签」字段（通常为 `.1`，唱片表取 `.1/.2/.3`），**不收录**描述、数值、台词正文等长文本；
  - `Item.json` 依据配置表的 `Type`/`Stype` 精确分流道具、潜能、唱片、纹章、头像等类别；
  - 界面文本（`UIText` 等）只保留短术语（简中 ≤24 字且不含句末标点），过滤掉整句提示；
  - 同一分类内如出现五语内容完全一致的重复词条，会合并为一条（保留首次出现的来源表 ID）；
  - 已剔除 `【不要翻译】`、`【废弃】`、`[no trans]` 等占位与废弃条目；
  - 已清除 `<color=…>`、`<sprite …>` 等富文本标记；
  - 拆分到单语言目录时，与目标语言写法完全相同的 `source`、以及同一分类内已经出现过的 `source`→`target` 对照行会被去掉，因此对照行数少于「词条数 × 4」；
- **已知限制**：
  - 台词、剧情正文、道具描述等长篇内容不在术语库范围内，如需可另行导出为翻译记忆库（TMX / 双语对照）；
  - `location.csv` 中除 `DatingLandmark` 与 `StarTower` 外，其余地名在游戏数据里没有独立表，已从角色档案地址、成就、故事标题等官方对齐文本中人工校订补入，并标注来源为 `curated (aligned in-game text)`；
  - `equipment.csv` 仅 15 条：本作没有传统武器 / 防具表，装备位由「秘纹（Disc）」承担；
  - 每个语言目录都存在「同一个 `source` 对应多个 `target`」的情况（`zh-CN` 有 1133 个这样的 `source`、`zh-TW` 962 个、`en-US` 826 个、`ja-JP` 1269 个、`ko-KR` 700 个），多来自同名不同物的短词（例如英文 `Amber` 在 `zh-CN` 下同时对应「琥珀」与「暖黄」）；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `__terms.csv` 里的 `id` 与 `src_table` 回查上下文；
- 全部 CSV 为 UTF-8 with BOM、CRLF 换行，Excel 双击即可正确显示中日韩文字；`.md` 说明文件为 UTF-8（无 BOM）。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《星塔旅人》的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
