# 碧蓝航线 术语库 — 한국어 韩文（`ko-KR`）

[← 返回游戏总说明](../README.md)

本目录是**以韩文（`ko-KR`）为目标语言**的《碧蓝航线》术语库：`target` 列固定为韩文写法，
`source` 列收录简体中文、英文、繁体中文与日文的写法。共 **6 个 CSV、15 511 行对照**，
其中 3 个主表合计 **7 709 行 / 850 + 850 + 165 条去重词条**。
韩文舰名中，舰种、阵营名与游戏内用语取自官方 KR 服客户端配置，其余为通用韩文标准译名，
**不是机器翻译**。

## 文件

- `azur_lane_glossary.csv` — `source,target,tgt_lng` 三列，3481 行；舰船名（标准名表），可直接导入 CAT / 术语管理工具
- `azur_lane_glossary_detailed.csv` — 3525 行；追加 `src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives`
- `azur_lane_ship_character_glossary.csv` — `source,target,tgt_lng` 三列，3769 行；`target` 为韩文舰名，`source` 含简中服实际显示名（含和谐名）
- `azur_lane_ship_character_glossary_detailed.csv` — 3818 行；额外列同上
- `azur_lane_terms.csv` — `source,target,tgt_lng` 三列，459 行；航海／军事／游戏术语
- `azur_lane_terms_detailed.csv` — 459 行；追加 `src_lng,category,category_zh,same_source_alternatives`

同级的 `by_language/` 提供按源语言拆分的舰船子表（`target` 一律为简中），
`sources/` 保存萌娘百科《碧蓝航线/名称对照表》的抓取结果，用于和谐名交叉校验。

## 分类与条数

| 表 | 对照行 | 词条数（`target` 去重） |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 3481 | 850 |
| `azur_lane_glossary_detailed.csv` | 3525 | 850 |
| `azur_lane_ship_character_glossary.csv` | 3769 | 850 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3818 | 850 |
| `azur_lane_terms.csv` | 459 | 165 |
| `azur_lane_terms_detailed.csv` | 459 | 165 |

舰船变体（按 `azur_lane_ship_character_glossary_detailed.csv` 的 `variant` 统计）：

| 变体 | 舰船数（`ship_id` 去重） | 对照行 |
| --- | --- | --- |
| 本体（无变体标记） | 770 | 3398 |
| META | 58 | 276 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合计** | **857** | **3818** |

（同一表的 `target` 去重后为 **850** 条 —— 个别舰船在不同 id 下使用同一韩文显示名。）

术语五类（按 `azur_lane_terms_detailed.csv` 的 `category` 统计）：

| `category` | 主题 | 词条数 | 对照行 |
| --- | --- | --- | --- |
| `hull_type` | 舰种 | 31 | 97 |
| `naval_term` | 航海／军事术语 | 72 | 198 |
| `navy_prefix` | 阵营与舰名前缀 | 24 | 59 |
| `rank` | 军衔 | 14 | 44 |
| `game_term` | 游戏术语 | 24 | 61 |
| **合计** | — | **165** | **459** |

## 说明

- **译文来源与对齐方式**：舰船名取自官方 CN / EN / JP / KR / TW 五服客户端配置；舰船唯一性以
  `ship_skin_template.json` 的 `ship_group` 归一，并按 `ship_data_template.json` 过滤敌方／NPC 副本。
  术语表为人工整理并逐条与各服配置校对。
  每个源串在本目录主表只保留一条译文，多解时取**舰船 id 最小者**，全部读法记入明细表的
  `same_source_alternatives`。例：韩文 `대령` 既指「海军上校」也指「大佐」，主表保留首个概念。
- **韩文来源**：舰种、阵营名、游戏内用语取自 KR 服自身配置
  （`ship_data_by_type` → `구축/경순/중순/…`、`fleet_tech_group` → `이글 유니온`/`메탈 블러드`、
  `world_port_data`、`medal_template`、`emoji_template` → `한계돌파`、`enemy_data_statistics` →
  `특장형 부린` 等），其余航海与军衔用语为通用韩文标准译名。游戏内舰种显示为缩写
  （구축 / 경순 / …），术语表统一使用完整形式（구축함 / 경순양함 / …）。
- **语言标签**：本目录所有 CSV 的 `tgt_lng` 列固定为 `ko-KR`；明细表的 `src_lng` 取值为
  `zh-CN` / `en-US` / `zh-TW` / `ja-JP`（术语表为 `zh-CN` / `en-US` / `ja-JP`）。
  注意 `zh-CN` 目录的舰船明细表改用 `en` / `ja` / `ko` / `zh-TW` 这类短标签，
  标签风格在各目录之间并不统一，但不影响任何译文内容。
  同名的 `by_language/azur_lane_glossary_ko-zh-CN.csv` 是同一批韩文源串以简中为目标语言的视图。
- **编码**：所有 CSV 均为 **UTF-8 with BOM + CRLF**，Excel 可直接打开；`.md` 为 UTF-8 无 BOM。
- **已知限制**：
  - 韩文译名中舰种、阵营与游戏内用语有 KR 服配置依据，其余航海／军衔用语为通用标准译名，
    不保证与游戏内实际用词完全一致。
  - 部分舰船在 KR 服配置中沿用简中字符串（视为未翻译）而无韩文名，因此本目录的舰船词条数
    （850 条）少于简中目录（877 条）。
  - EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），为游戏原始数据问题，未作人工改写。
  - 只有亚尔薇特（Alvitr，铁血战巡，ship_id 404061）一名铁血角色无简中和谐名。
  - 本目录不含 `azur_lane_ambiguous.csv` 与 `azur_lane_combined_ships_and_terms.csv`，这两个文件仅在 `zh-CN` 提供。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件
（包括但不限于沉浸式翻译）的术语匹配，**不应被视为《碧蓝航线》的官方术语表或官方本地化文件**。
库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致；游戏名称、角色名称、专有名词、
商标等知识产权均归各自权利人所有，本库不主张任何相关权利，使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
