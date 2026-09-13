# 《猫之城》Cat Fantasy 翻译术语库 / Cat Fantasy Terminology Database / Cat Fantasy 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库整理手机游戏《猫之城》（Cat Fantasy）的官方多语文本，从官方多语言数据表与 I18N 界面文本表中
抽取对齐，共 **102,213** 条唯一词条，按目标语言拆分为 **7** 套独立术语库（**619,095** 条词条记录、
**1,206,381** 行语言对照），每套内部再按 16 个分类归档。译文**全部取自游戏官方已实装的本地化文本**，
按同一文本键对齐，不含任何二次机翻或人工转译。其中 6 套（`zh-CN`／`zh-TW`／`en-US`／`ja-JP`／`ko-KR`／`th-TH`）
为完整 16 分类词库，`id-ID` 因官方仅在界面文本中提供印尼语，只有 `13_ui` 一个分类。

## 使用方法

1. **单文件下载**：进入对应语言目录（如 `zh-CN/`），打开所需分类的 `NN_xxx_glossary.csv`，
   在文件详情页直接下载。该文件为 `source,target,tgt_lng` 三列格式，可直接导入沉浸式翻译等
   AI 翻译软件的术语库功能；
2. **整个语言目录打包下载**：语言目录内 16 个分类合起来即是该语言的完整术语表
   （分类索引与条数见该目录的 `00_master/index.csv`）；
3. **克隆整个仓库**：配合各语言目录的 `00_master/index.csv` 与 `multilingual/all_languages_master.csv`
   自行检索、拆分或二次加工；数据来源仓库见下文「使用的相关内容」。
   **注意**：本库不含生成脚本（详见「生成与复现」）。

## 目录结构

```text
Cat_Fantasy_Glossary（猫之城）/
├── README.md                          本说明（简体中文）
├── README_EN.md                       本说明（English）
├── README_JP.md                       本说明（日本語）
├── zh-CN/                             简体中文
│   ├── 00_master/                     索引与说明（index.csv、README.md）
│   ├── 01_character/                  角色与卡牌
│   ├── 02_skill/                      技能与战斗效果
│   ├── 03_talent/                     天赋与觉醒
│   ├── 04_equipment/                  装备与专属武器
│   ├── 05_item/                       道具与材料
│   ├── 06_enemy/                      敌人与BOSS
│   ├── 07_stage/                      关卡与章节
│   ├── 08_event/                      活动玩法
│   ├── 09_gacha/                      抽卡与兑换
│   ├── 10_shop/                       商店与礼包
│   ├── 11_homeland/                   家园与猫咖
│   ├── 12_system/                     系统与任务
│   ├── 13_ui/                         UI与界面文本
│   ├── 14_story/                      剧情专有名词
│   ├── 15_location/                   地点与区域
│   └── 16_terminology/                游戏机制术语
├── zh-TW/                             繁體中文（结构与 zh-CN 相同）
├── en-US/                             English（结构与 zh-CN 相同）
├── ja-JP/                             日本語（结构与 zh-CN 相同）
├── ko-KR/                             한국어（结构与 zh-CN 相同）
├── th-TH/                             ภาษาไทย（结构与 zh-CN 相同）
├── id-ID/                             Bahasa Indonesia（仅 13_ui 有内容，见下文说明）
└── multilingual/                      七语并排总表
    ├── all_languages_master.csv       七语并排总表（102,213 条 × 10 列）
    └── 00_master/
        ├── README.md                  总表说明
        ├── source_mapping.csv         来源表 → 分类 映射（379 张表）
        └── categories.csv             16 个分类的定义
```

除 `00_master/` 外，每个分类目录内固定两个文件：`NN_xxx_glossary.csv`（术语对照表）与
`NN_xxx_terms.csv`（本语言词条清单）。每个语言目录另有 `README.md`（该语言）与
`README_zh-CN.md`（简体中文）两个说明文件（`zh-CN/` 只有 `README.md`）。

## 数据概览

### 各语言条数

| 语言代码 | 语言 | 词条数 | 对照行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 102,213 | 196,870 |
| `zh-TW` | 繁體中文 | 101,915 | 196,972 |
| `en-US` | English | 101,692 | 197,404 |
| `ja-JP` | 日本語 | 101,621 | 196,919 |
| `ko-KR` | 한국어 | 101,760 | 197,663 |
| `th-TH` | ภาษาไทย | 99,978 | 191,726 |
| `id-ID` | Bahasa Indonesia | 9,916 | 28,827 |
| **合计** | **7 套** | **619,095** | **1,206,381** |

> 表中的「词条数」= 唯一文本键的数量（各语言 `*_terms.csv` 的数据行数，合计即 102,213 条唯一词条 ×
> 各语言覆盖情况）；「对照行数」= 各语言 `*_glossary.csv` 的数据行数，是 16 个分类相加的结果。
> 两个数字含义不同，不可互换。
>
> `id-ID` 仅有官方 UI 文本（I18N 表）为印尼语，游戏数据表未提供印尼语实体名称，
> 因此该套术语库只包含 `13_ui` 一个分类（另外 15 个分类只有表头、没有数据行），条数明显少于其他语言。

### 官方语言支持说明

本库整理的目标语言**以游戏官方已经实装的文本为准**，不做二次机翻：

| 语言 | 状态 |
| --- | --- |
| `zh-CN` 简体中文 | ✅ 官方实装（原始语言） |
| `zh-TW` 繁體中文 | ✅ 官方实装 |
| `en-US` English | ✅ 官方实装（见下方说明） |
| `ja-JP` 日本語 | ✅ 官方实装 |
| `ko-KR` 한국어 | ✅ 官方实装 |
| `th-TH` ภาษาไทย | ✅ 官方实装 |
| `id-ID` Bahasa Indonesia | ✅ 官方实装（仅界面文本） |
| `fr-FR` / `de-DE` / `es-ES` / `ru-RU` / `pt-BR` / `it-IT` / `tr-TR` / `vi-VN` | ❌ 官方未实装，本库不提供 |

**关于英文**：游戏数据表中英文只有一列 `en_UK`，而 I18N 文本表同时存在 `en_UK` 与 `en_US` 两套英文。
本库的 `en-US` 目录中，实体名称取自 `en_UK` 列，界面文本优先取 `en_US`、缺失时回退 `en_UK`；
两套英文的原始文本都保留在 `multilingual/all_languages_master.csv` 的对应列中。

### 分类与条数（以 `zh-CN` 为例）

| 分类 | 主题 | 词条数 | 对照行数 | 内容 |
| --- | --- | --- | --- | --- |
| `01_character` | 角色与卡牌 | 19,983 | 33,652 | 可战斗猫娘（卡牌）名称、猫形、职业、种族、皮肤、专属台词与角色档案 |
| `02_skill` | 技能与战斗效果 | 9,228 | 15,059 | 技能名称、技能关键词、被动/觉醒技能与效果说明 |
| `03_talent` | 天赋与觉醒 | 2,536 | 4,169 | 角色天赋名称与天赋效果 |
| `04_equipment` | 装备与专属武器 | 6,388 | 2,197 | 装备、专属武器、装备部位与筛选分类 |
| `05_item` | 道具与材料 | 4,650 | 13,090 | 消耗品、礼物、素材、货币等道具名称与说明 |
| `06_enemy` | 敌人与BOSS | 27 | 124 | 敌方目标及相关说明文本 |
| `07_stage` | 关卡与章节 | 7,278 | 20,995 | 主线章节、日常副本、迷宫、爬塔、挑战关卡 |
| `08_event` | 活动玩法 | 17,339 | 21,613 | 限时活动、节日活动、排行榜、世界BOSS等玩法 |
| `09_gacha` | 抽卡与兑换 | 53 | 140 | 卡池说明、召唤任务与兑换规则 |
| `10_shop` | 商店与礼包 | 4,589 | 1,688 | 商店、通行证、时装合约与各类礼包 |
| `11_homeland` | 家园与猫咖 | 8,913 | 25,223 | 猫咖/餐厅、钓鱼、俱乐部、家园天赋等休闲玩法 |
| `12_system` | 系统与任务 | 6,041 | 18,849 | 功能开关、新手引导、任务、图鉴、地区玩法、签到等 |
| `13_ui` | UI与界面文本 | 9,923 | 28,822 | 客户端界面文本（取自 I18N 文本表） |
| `14_story` | 剧情专有名词 | 3,180 | 5,480 | 剧情登场角色名、场景名、字幕与小剧场 |
| `15_location` | 地点与区域 | 449 | 1,649 | 地图、区域、战斗场景、电话区号等 |
| `16_terminology` | 游戏机制术语 | 1,636 | 4,120 | 属性、元素、克制关系、增益/减益等机制用语 |
| **合计** | | **102,213** | **196,870** | |

各语言的逐分类条数见该语言目录下的 `00_master/index.csv`，分类定义见
`multilingual/00_master/categories.csv`。

### 文件格式

每个分类文件夹内的两个文件均使用 **UTF-8 with BOM + CRLF** 保存（Excel 双击可直接打开，
不需要额外指定编码）。

**`NN_xxx_glossary.csv` —— 术语对照表（`source` / `target` / `tgt_lng`）**

该语言的 `tgt_lng` 列固定，`source` 列是其余语言的写法（同一条词条的多个语言写法各占一行），
可直接导入沉浸式翻译等术语工具：

| source | target | tgt_lng |
| --- | --- | --- |
| Asura | 非天 | zh-CN |
| アスラ | 非天 | zh-CN |
| 아수라 | 非天 | zh-CN |

**`NN_xxx_terms.csv` —— 本语言词条清单（`id` / `term` / `src_table`）**

| id | term | src_table |
| --- | --- | --- |
| Card.101002.name | 非天 | Card/Card.txt |
| Card.101002.desc | 非天 | Card/Card.txt |

- `id` = `源表名.主键.字段名`，可据此回查游戏原始数据表；
- `src_table` = 该词条在官方数据包中的相对路径（`MasterData\Setting\Data\` 之下）。

**`00_master/index.csv`** 为该语言的分类索引与条数（列为
`category,label,term_count,glossary_count,glossary_file,terms_file,target_language`），
合并其中全部 16 个分类即可得到该语言的完整术语表。

## 使用的相关内容

| 来源仓库 | 用途 |
| --- | --- |
| [PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy) | 官方多语言数据表（`Setting/Data`）与 I18N 文本表（`Setting/I18N`），版本 2.14.0 |
| [Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1) | 交叉核对游戏数据结构（版本 2.18.1） |
| [简体中文官网](https://cat.fantanggame.com/) / [繁中官网](https://tw.catfantasygame.com/) / [英文官网](https://cat.elex.com/) / [日文官网](https://jp.catfantasygame.com/) / [韩文官网](https://kr.catfantasygame.com/) / [东南亚官网](https://catfantasysea.bonfiregathering.com/en/) | 语言支持情况核对 |

## 生成与复现

**本目录不含任何脚本，也没有 `tools/` 目录**：这是一个**纯数据产品**，仓库内不提供生成管线代码，
因此没有可以直接执行的复现命令。生成过程如下（如实记录，供需要复现者对照上游数据包自行实现）：

```text
# 本库无脚本、无 tools/ 目录，故没有可执行的复现命令。
# 生成流程（数据整理记录）：
1. 扫描 Setting/Data 下全部数据表，识别带 _zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH 后缀的
   多语言字段；基准列（无后缀）即 zh-CN 原文；
2. 按数据表所属玩法模块划分到 16 个分类（映射关系见 multilingual/00_master/source_mapping.csv，
   共 379 张来源表）；
3. 13_ui 分类取自 Setting/I18N 哈希文本表，按 Id 键对齐七种语言；
4. 对 NewChapter（剧情表）只提取登场角色名与场景名等专有名词，剧情正文对话不纳入术语库；
5. 同一分类内按 (source, target) 去重；源语言与目标语言写法完全相同时不生成对照行；
6. 各语言目录下的 *_glossary.csv 由 multilingual/all_languages_master.csv 按分类展开生成。

# 需要复现时的数据获取：
#   上游数据包见上表「使用的相关内容」，需自行下载对应仓库的 Setting/Data 与 Setting/I18N。
# 需要校验本库数据时可直接读取（只读，不修改）：
#   zh-CN/00_master/index.csv           各语言分类索引与条数
#   multilingual/all_languages_master.csv  七语并排总表
#   multilingual/00_master/source_mapping.csv  来源表 → 分类 映射
```

每套术语库都是**按同一文本键对齐**的官方文本，非二次翻译；同一条词条会把其余语言的写法全部展开为
对照行，因此也可以反向当作「`zh-CN` → 其他语言」的查询表使用。

## 已知限制

- 分类为按数据表自动归类，个别词条（如跨玩法的通用文本）可能归入相邻分类；
- 游戏数据表中敌人类名称未提供多语言列，`06_enemy` 分类条数很少（`zh-CN` 仅 27 条）；
- `id-ID` 只有 `13_ui` 一个分类，另外 15 个分类的 CSV 仅有表头、无数据行；
- 文本中的占位符（如 `_name_`、`_num_`、`#num_percent_0_1_1_`、`\n`）保留官方原样，未做替换；
- 各语言覆盖的文本键并不完全一致（例如 `th-TH` 仅覆盖 99,978 条、`id-ID` 仅覆盖界面文本），
  因此各语言的词条数与对照行数均不相同，属正常现象；
- 不同地区版本、游戏版本之间可能存在译名差异，本库以所引用的数据包版本为准。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件
（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、
版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，
不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。
游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方
知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。
如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。
完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
