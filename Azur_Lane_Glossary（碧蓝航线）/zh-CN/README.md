# 碧蓝航线 术语库 — 简体中文（`zh-CN`）

[← 返回游戏总说明](../README.md)

本目录是**以简体中文（`zh-CN`）为目标语言**的《碧蓝航线》术语库：`target` 列固定为简中写法，
`source` 列收录英文、日文、繁体中文、韩文以及简中标准名／和谐名的写法。共 **8 个 CSV、19 855 行对照**，
其中 3 个主表合计 **7 767 行**、去重后的词条数为 **877 条舰船名（标准名源）+ 875 条舰船名（和谐名源）+ 170 条术语**。
舰船名与术语的译文均抽取自官方五服客户端配置或多语言社区对照表，**不是机器翻译**。

## 文件

- `azur_lane_glossary.csv` — `source,target,tgt_lng` 三列，3514 行；舰船名，源为简中标准名及其他语言的舰名，可直接导入 CAT / 术语管理工具
- `azur_lane_glossary_detailed.csv` — 3592 行；追加 `src_lng,ship_id,ship_type,nation,variant`
- `azur_lane_ship_character_glossary.csv` — `source,target,tgt_lng` 三列，3804 行；`target` 为简中服**实际显示名**（有和谐名用和谐名）
- `azur_lane_ship_character_glossary_detailed.csv` — 3890 行；追加 `src_lng,ship_id,ship_type,nation,variant,zh_CN_standard,zh_CN_target,same_source_alternatives`
- `azur_lane_terms.csv` — `source,target,tgt_lng` 三列，449 行；航海／军事／游戏术语
- `azur_lane_terms_detailed.csv` — 459 行；追加 `src_lng,category,category_zh,same_source_alternatives`
- `azur_lane_ambiguous.csv` — 162 行（**仅本目录**）；一个源串对应多个简中译名时的全部读法，带 `english_name` 与 `role`（`dominant` / `alternative`）列
- `azur_lane_combined_ships_and_terms.csv` — 3985 行（**仅本目录**）；`azur_lane_glossary.csv` 与术语表的合并去重版，`source,target,tgt_lng` 三列，适合一次性导入

同级的 `by_language/` 提供按源语言拆分的舰船子表（`target` 一律为简中），
`sources/` 保存萌娘百科《碧蓝航线/名称对照表》的抓取结果，用于和谐名交叉校验。

## 分类与条数

| 表 | 对照行 | 词条数（`target` 去重） |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 3514 | 877 |
| `azur_lane_glossary_detailed.csv` | 3592 | 877 |
| `azur_lane_ship_character_glossary.csv` | 3804 | 875 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3890 | 877 |
| `azur_lane_terms.csv` | 449 | 170 |
| `azur_lane_terms_detailed.csv` | 459 | 175 |

舰船变体（按 `azur_lane_ship_character_glossary_detailed.csv` 的 `variant` 统计）：

| 变体 | 舰船数 | 对照行 |
| --- | --- | --- |
| 本体（无变体标记） | 795 | 3466 |
| META | 60 | 280 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合计** | **884** | **3890** |

（「舰船数」按 `ship_id` 去重；同一表的 `target` 去重后为 **877** 条 —— 个别舰船在不同 id 下使用同一显示名。）

术语五类（按 `azur_lane_terms_detailed.csv` 的 `category` 统计）：

| `category` | 主题 | 词条数 | 对照行 |
| --- | --- | --- | --- |
| `hull_type` | 舰种 | 31 | 97 |
| `naval_term` | 航海／军事术语 | 72 | 198 |
| `navy_prefix` | 阵营与舰名前缀 | 24 | 59 |
| `rank` | 军衔 | 24 | 44 |
| `game_term` | 游戏术语 | 24 | 61 |
| **合计** | — | **175** | **459** |

## 说明

- **译文来源与对齐方式**：舰船名取自官方 CN / EN / JP / KR / TW 五服客户端配置（`ship_data_statistics.json` 等），
  舰船唯一性以 `ship_skin_template.json` 的 `ship_group` 归一，并按 `ship_data_template.json` 过滤敌方／NPC 副本；
  和谐名来自 `name_code.json` 并经萌娘百科对照表校验；术语表为人工整理并逐条与各服配置校对。
  每个源串在本目录主表只保留一条译文，多解时取**舰船 id 最小者**，全部读法记入明细表的 `same_source_alternatives`。
- **语言标签**：本目录所有 CSV 的 `tgt_lng` 列固定为 `zh-CN`；明细表的 `src_lng` 取值，
  舰船表为 `en` / `ja` / `ko` / `zh-TW`（`azur_lane_ship_character_glossary_detailed.csv` 另有 `zh-CN`，
  表示「简中标准名 → 简中和谐名」），术语表为 `en-US` / `ja-JP` / `ko-KR`。
  另外三个语言目录的舰船明细表改用 `en-US` / `ja-JP` / `ko-KR` / `zh-TW` 这类四字母标签，
  标签风格在各目录之间并不统一，但不影响任何译文内容。
  同名的 `by_language/` 子表（`azur_lane_glossary_{en,ja,ko,zh-TW}-zh-CN.csv`）是同一批舰船按源语言切分的视图，
  `target` 仍为简中。
- **编码**：所有 CSV 均为 **UTF-8 with BOM + CRLF**，Excel 可直接打开；`.md` 为 UTF-8 无 BOM。
- **已知限制**：
  - 本目录是「外语 → 简中」方向，因此不含繁体中文（`zh-TW`）与韩文以外的目标语言版本；
    `azur_lane_ambiguous.csv` 与 `azur_lane_combined_ships_and_terms.csv` 同样只存在于本目录。
  - EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），为游戏原始数据问题，未作人工改写。
  - 只有亚尔薇特（Alvitr，铁血战巡，ship_id 404061）一名铁血角色无和谐名。
  - EN / KR 服直接沿用简中字符串的舰名视为未翻译并剔除；JP / TW 服与简中相同的汉字名属正常情况，一律保留。
  - `azur_lane_ambiguous.csv` 中 162 行涉及 77 个一名多解的源串（77 行为 `dominant`、85 行为 `alternative`）。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件
（包括但不限于沉浸式翻译）的术语匹配，**不应被视为《碧蓝航线》的官方术语表或官方本地化文件**。
库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致；游戏名称、角色名称、专有名词、
商标等知识产权均归各自权利人所有，本库不主张任何相关权利，使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
