# 猫之城（Cat Fantasy）多语言术语库

按**目标语言**拆分为独立文件夹，每个语言文件夹内按**类目**以扁平 CSV 文件存放；
不再使用 `NN_xxx/` 子目录。

## 数据来源

- 文本主源：[PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy)
  - `Setting/Data/`：官方多语言数据表，按文本键对齐各语言
  - `Setting/I18N/`：界面文本表，按 Id 对齐七种语言
- 结构核对：[Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1)（版本 2.18.1）
- 参考格式：本仓库 `Wuthering_Waves_glossary（鸣潮）/wuwa-glossary/` 的扁平多语言数据产品布局

## 目录结构

```text
cat-fantasy-glossary/
├── README.md                     本说明
├── zh-CN/                       目标语言 = 简体中文
│   ├── character.csv           术语对照表（source,target,tgt_lng）
│   ├── character__terms.csv    词条清单（id,term,src_table）
│   └── ...                      共 16 个类目、32 个 CSV
├── zh-TW/ ... id-ID/            共 7 个语言文件夹，结构相同
├── _master/                     各语言原始索引与说明
│   ├── zh-CN__index.csv         原名 00_master/index.csv
│   └── zh-CN__README.md         原名 00_master/README.md
└── multilingual/                七语并排总表（原 multilingual/，未改动）
    ├── all_languages_master.csv 七语并排总表
    └── 00_master/               总表说明、分类定义、来源映射
```

每个语言文件夹中，`<category>.csv` 是 `source,target,tgt_lng` 三列术语对照表；
`<category>__terms.csv` 是该语言的 `id,term,src_table` 词条清单。`_master/<lang>__index.csv`
记录该语言各类目的条数与对照行数，`_master/<lang>__README.md` 保留各语言原始说明。

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。

| source | target | tgt_lng |
| --- | --- | --- |
| Asura | 非天 | zh-CN |
| アスラ | 非天 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是其他任一语言的原文。
同一条目会在目标语言文件夹内以其余可用语言分别作为 `source` 各出现一行。

`<category>__terms.csv` 为词条清单，列为 `id,term,src_table`：`id` 形如
`源表名.主键.字段名`，`src_table` 是官方数据包中的来源表相对路径。

## 语言代码

| 语言文件夹 | 语言 | 目标语言标签 `tgt_lng` |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `zh-CN` |
| `zh-TW` | 繁體中文 | `zh-TW` |
| `en-US` | English | `en-US` |
| `ja-JP` | 日本語 | `ja-JP` |
| `ko-KR` | 한국어 | `ko-KR` |
| `th-TH` | ภาษาไทย | `th-TH` |
| `id-ID` | Bahasa Indonesia | `id-ID` |

## 类目与文件名

| 类目 | 对照表文件 | 词条清单文件 | 说明 |
| --- | --- | --- | --- |
| 角色与卡牌 | `character.csv` | `character__terms.csv` | 原 `01_character/` 分类 |
| 技能与战斗效果 | `skill.csv` | `skill__terms.csv` | 原 `02_skill/` 分类 |
| 天赋与觉醒 | `talent.csv` | `talent__terms.csv` | 原 `03_talent/` 分类 |
| 装备与专属武器 | `equipment.csv` | `equipment__terms.csv` | 原 `04_equipment/` 分类 |
| 道具与材料 | `item.csv` | `item__terms.csv` | 原 `05_item/` 分类 |
| 敌人与BOSS | `enemy.csv` | `enemy__terms.csv` | 原 `06_enemy/` 分类 |
| 关卡与章节 | `stage.csv` | `stage__terms.csv` | 原 `07_stage/` 分类 |
| 活动玩法 | `event.csv` | `event__terms.csv` | 原 `08_event/` 分类 |
| 抽卡与兑换 | `gacha.csv` | `gacha__terms.csv` | 原 `09_gacha/` 分类 |
| 商店与礼包 | `shop.csv` | `shop__terms.csv` | 原 `10_shop/` 分类 |
| 家园与猫咖 | `homeland.csv` | `homeland__terms.csv` | 原 `11_homeland/` 分类 |
| 系统与任务 | `system.csv` | `system__terms.csv` | 原 `12_system/` 分类 |
| UI与界面文本 | `ui.csv` | `ui__terms.csv` | 原 `13_ui/` 分类 |
| 剧情专有名词 | `story.csv` | `story__terms.csv` | 原 `14_story/` 分类 |
| 地点与区域 | `location.csv` | `location__terms.csv` | 原 `15_location/` 分类 |
| 游戏机制术语 | `terminology.csv` | `terminology__terms.csv` | 原 `16_terminology/` 分类 |

## 各语言数据量

以下数字由本次整理后的文件逐行统计得出；「词条数」为 `<category>__terms.csv` 数据行合计，
「对照行数」为 `<category>.csv` 数据行合计。

| 语言 | CSV 文件数 | 词条数 | 对照行数 | 数据行合计 |
| --- | ---: | ---: | ---: | ---: |
| `zh-CN` | 32 | 102,213 | 196,870 | 299,083 |
| `zh-TW` | 32 | 101,915 | 196,972 | 298,887 |
| `en-US` | 32 | 101,692 | 197,404 | 299,096 |
| `ja-JP` | 32 | 101,621 | 196,919 | 298,540 |
| `ko-KR` | 32 | 101,760 | 197,663 | 299,423 |
| `th-TH` | 32 | 99,978 | 191,726 | 291,704 |
| `id-ID` | 32 | 9,916 | 28,827 | 38,743 |
| **合计** | **224** | **619,095** | **1,206,381** | **1,825,476** |

> 每个语言文件夹固定 16 个 `<category>.csv` 和 16 个 `<category>__terms.csv`，共 32 个 CSV。
> `id-ID` 的其余 15 个类目文件保留表头、没有数据行，因为官方仅提供界面文本的印尼语。

## 重新生成

本数据产品**没有 `tools/` 目录、也没有生成脚本**；目录整理与路径改写由一次性移动/重命名完成。
若要从上游重新生成数据，需要按以下流程实现：

```text
# 1. 从 PackageInstaller/DataTable · game/CatFantasy 获取 Setting/Data 与 Setting/I18N。
# 2. 扫描 Setting/Data 中含 _zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH 后缀的字段，
#    基准列（无后缀）为 zh-CN；按来源表映射到 16 个类目。
# 3. 从 Setting/I18N 按 Id 对齐七种语言，生成 ui 类目。
# 4. NewChapter 剧情表仅提取角色名、场景名等专有名词，不收录剧情正文对话。
# 5. 按 (source, target) 去重，原文与译文相同时不生成对照行。
# 6. 将结果写为 <lang>/<category>.csv 与 <lang>/<category>__terms.csv，
#    均为 UTF-8 BOM + CRLF；同时生成 _master/<lang>__index.csv。
```

上游来源表 → 类目映射见 `multilingual/00_master/source_mapping.csv`（379 张表）；
类目定义见 `multilingual/00_master/categories.csv`（16 个类目）。

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）或沉浸式翻译类软件时，选择目标语言文件夹中的
  `<category>.csv` 直接作为术语库导入即可。
- 文件名即类目名，可按需合并；按领域拆分导入（如仅 `character.csv` + `skill.csv`）
  可显著提升匹配精度。
- `__terms.csv` 用于校对和回查来源表，不是直接导入 CAT 工具的对照表。
