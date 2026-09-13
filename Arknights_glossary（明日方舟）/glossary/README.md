# 明日方舟 (Arknights) 多语言术语库

按**目标语言**分文件夹、按**20 个分类**分文件的翻译术语库，覆盖简体中文、繁体中文、英文、日文、韩文。

## 目录结构

```
Arknights_glossary（明日方舟）/
├── glossary/                 # 术语库数据产品
│   ├── README.md             # 本说明（由 tools/write_readme.py 生成）
│   ├── zh-CN/                # 目标语言 = 简体中文
│   │   ├── 01_干员名称.csv
│   │   ├── 02_干员异格.csv
│   │   ├── ...
│   │   ├── 20_游戏机制.csv
│   │   └── _all.json         # 上述 20 个文件的合并版（JSON）
│   ├── zh-TW/   (同结构)
│   ├── en-US/   (同结构)
│   ├── ja-JP/   (同结构)
│   └── ko-KR/   (同结构)
├── tools/                    # 生成脚本与元数据
│   ├── build_glossary.py     # 读取 _data/gamedata，输出 glossary/
│   ├── write_readme.py       # 依据 _summary.json 生成 glossary/README.md
│   └── _summary.json         # 各分类词条数与覆盖率统计
└── README.md                 # 游戏总说明（中文）
```

## 文件格式

每个 CSV 均为三列，UTF-8 BOM 编码（Excel 可直接打开）：

| source | target | tgt_lng |
| ------ | ------ | ------- |
| Amiya | 阿米娅 | zh-CN |
| アーミヤ | 阿米娅 | zh-CN |
| 阿米婭 | 阿米娅 | zh-CN |
| 아미야 | 阿米娅 | zh-CN |

- `target`：该文件所属目标语言的官方译名。
- `tgt_lng`：目标语言标签，等于所在文件夹名。
- `source`：同一词条在**其他 4 种语言**中的写法（因此同一词条会出现在多行中）。
  例如 `zh-CN/01_干员名称.csv` 中「阿米娅」会分别以 `Amiya`(en-US)、`アーミヤ`(ja-JP)、
  `阿米婭`(zh-TW)、`아미야`(ko-KR) 作为 source 出现 4 行。

> 只想保留「英→中」这类单向词表时，按 `source` 所在语言筛选即可，例如只保留 source 为拉丁字母的行。

## 分类与数据来源

| 分类 | 词条数 | 五语齐全 | 数据来源 |
| ---- | -----: | -------: | -------- |
| 01_干员名称 | 436 | 434 | character_table.json — 全部可获取干员（八大职业） |
| 02_干员异格 | 34 | 34 | character_table.json — 异格干员（char_1xxx 编号） |
| 03_职业与分支 | 83 | 83 | i18n/string_map.txt（八大职业）+ uniequip_table.subProfDict（职业分支） |
| 04_技能名称 | 1,630 | 1,599 | skill_table.json — 全部技能（含通用技能与干员技能） |
| 05_技能描述关键术语 | 350 | 296 | skill_table / character_table 天赋描述，按占位符对齐后全语料投票提取术语 |
| 06_天赋 | 586 | 583 | character_table.talents[].name — 天赋名 |
| 07_潜能 | 2,068 | 2,058 | character_table.potentialRanks[].description + 潜能提升信物名称 |
| 08_模组 | 863 | 856 | uniequip_table.equipDict.uniEquipName + equipTypeInfos（模组类型） |
| 09_敌人 | 1,361 | 1,327 | enemy_handbook_table.enemyData — NORMAL / ELITE 级敌人 |
| 10_BOSS | 229 | 229 | enemy_handbook_table.enemyData — BOSS 级敌人 |
| 11_关卡 | 3,306 | 3,263 | stage_table.stages[].name — 关卡名 |
| 12_地区 | 419 | 414 | zone_table.zones（章节/地区）+ activity_table 活动区域名 |
| 13_阵营 | 46 | 46 | handbook_team_table — 势力/阵营名 |
| 14_活动 | 299 | 291 | activity_table.basicInfo + crisis_v2 赛季 + climb_tower 赛季 + 集成战略主题 |
| 15_道具 | 691 | 677 | item_table.items — 非材料类道具（凭证、票券、补给、纪念品等） |
| 16_装备 | 5,723 | 5,718 | climb_tower_table 战术装备 + sandbox_table 生息演算装备 + 集成战略收藏品 |
| 17_材料 | 676 | 674 | item_table.items — MATERIAL 类材料（已剔除信物） |
| 18_剧情专有名词 | 2,314 | 2,303 | story_review_table 剧情名 + handbook_info_table NPC 名与档案名 |
| 19_UI与系统术语 | 2,479 | 2,459 | i18n/string_map.txt — 客户端全部界面文本 |
| 20_游戏机制 | 247 | 236 | tip_table 战斗提示 + GUIDE 任务 + 基建房间 + 特性/模组描述术语 |

合计 **23,840** 个词条，导出 **266,111** 行**（5 个语言文件夹 × 20 个分类）

## 各语言分布

| 分类 | zh-CN | zh-TW | en-US | ja-JP | ko-KR |
| ---- | ----: | ----: | ----: | ----: | ----: |
| 01_干员名称 | 1,452 | 1,446 | 1,451 | 1,452 | 1,451 |
| 02_干员异格 | 130 | 130 | 130 | 130 | 130 |
| 03_职业与分支 | 285 | 285 | 284 | 285 | 284 |
| 04_技能名称 | 4,913 | 4,868 | 4,913 | 4,913 | 4,912 |
| 05_技能描述关键术语 | 1,174 | 1,171 | 1,067 | 1,134 | 1,138 |
| 06_天赋 | 2,114 | 2,105 | 2,114 | 2,114 | 2,114 |
| 07_潜能 | 443 | 443 | 439 | 439 | 439 |
| 08_模组 | 3,304 | 3,283 | 3,303 | 3,304 | 3,303 |
| 09_敌人 | 4,986 | 5,088 | 5,088 | 5,088 | 5,088 |
| 10_BOSS | 709 | 709 | 709 | 709 | 709 |
| 11_关卡 | 7,817 | 7,784 | 7,799 | 7,821 | 7,826 |
| 12_地区 | 702 | 702 | 716 | 702 | 707 |
| 13_阵营 | 167 | 167 | 167 | 167 | 167 |
| 14_活动 | 839 | 824 | 836 | 835 | 835 |
| 15_道具 | 2,013 | 1,984 | 2,007 | 2,011 | 2,007 |
| 16_装备 | 4,971 | 4,991 | 5,045 | 4,954 | 4,949 |
| 17_材料 | 2,494 | 2,488 | 2,494 | 2,494 | 2,494 |
| 18_剧情专有名词 | 4,961 | 4,934 | 4,961 | 4,958 | 4,962 |
| 19_UI与系统术语 | 8,789 | 8,799 | 8,822 | 8,813 | 8,777 |
| 20_游戏机制 | 944 | 944 | 924 | 939 | 936 |

（「词条数」= 同一分类下参与对齐的**唯一 ID 数**；「五语齐全」= 5 个区服都取到文本的 ID 数；
「各语言分布」表内为 **CSV 数据行数**——同一词条会因多语言 source 产生多行，且 source 与 target
写法完全相同的行不会写入，因此各语言行数略有差异。）

## 数据来源与版本

- 主数据：[ArknightsAssets/ArknightsGamedata](https://github.com/ArknightsAssets/ArknightsGamedata)
  —— 各区服官方客户端解包表格，`cn` / `tw` / `en` / `jp` / `kr` 五区并存且表结构一致，是本词库的基础。
- 交叉校验：[ArchyCillp/ArknightsTranslationContrast](https://github.com/ArchyCillp/ArknightsTranslationContrast)
  —— 用于抽样核对干员/技能译名。
- 结构参考：[flandia/ArknightsGameDataComposite](https://github.com/flandia/ArknightsGameDataComposite)
  —— 仅 4 语（无繁中）且条目少于主数据，未作为数据源，仅用于比对。

各服版本（`data_version.txt`）：

- 简中 `rel77.0`（2026/08/31）
- 英文 `51.4.0`
- 繁中 `50.8.0`

> 由于各区服进度不同，最新内容在日/英/韩/繁中可能尚未实装，这些词条不会出现在词库中
> （生成时要求至少两种语言同时存在）。

## 生成方法

1. **按 ID 对齐**：所有表格以条目 ID（如 `char_002_amiya`、`skchr_amiya_2`）为键，
   把 5 个区服的同一 ID 值配成一组，保证是同一个概念的官方译名。
2. **名称类分类**直接取官方字段（干员名、技能名、关卡名、敌人名等）。
3. **描述类分类**（技能描述关键术语、部分游戏机制）采用**占位符分段 + 全语料投票**：
   游戏文本中的 `<@ba.vup>`、`{atk:0%}` 等标记在各语言完全一致，以标记切分文本即可得到
   结构对齐的片段；再对同一中文片段统计各语言出现最多的写法，消除语序差异带来的错配。
4. **清洗**：去除富文本标签、换行、成对引号与书名号，过滤纯数字/纯符号片段。

## 已知限制

- 描述类术语（05、20）由文本自动挖掘，少数条目仍是短语片段而非严格术语，建议按需人工复核。
- 关卡、活动等词条大量同名的（如「标准实战环境」）会各自成行，未做跨条目合并。
- 干员异格仅收录异格形态本身；基础干员见 `01_干员名称`。

## 复现

```
python tools/build_glossary.py     # 读取 <游戏根>/_data/gamedata，输出 <游戏根>/glossary/
python tools/write_readme.py       # 依据 tools/_summary.json 重新生成本文件
```

> `_data/gamedata` 是外部数据目录（各服官方客户端解包表格），**未随仓库分发**，
> 需先按「数据来源与版本」一节自行准备后才能复现。

