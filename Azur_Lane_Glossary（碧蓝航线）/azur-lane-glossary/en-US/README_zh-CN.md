# 碧蓝航线 术语库 — English（`en-US`）

[← 返回游戏总说明](../README.md)

本目录是**以英文（`en-US`）为目标语言**的《碧蓝航线》术语库：`target` 列固定为英文写法，
`source` 列收录简体中文、日文、繁体中文与韩文的写法。共 **6 个 CSV、12 600 行对照**，
其中 3 个主表合计 **6 283 行 / 821 + 855 + 154 条去重词条**。
英文舰名直接取自官方 EN 服客户端配置（缺失时以该服 `english_name` 的舷号全称补位），
属**官方本地化文本**，**不是机器翻译**。

## 文件

- `azur_lane_glossary.csv` — `source,target,tgt_lng` 三列，2795 行；舰船名（标准名表），可直接导入 CAT / 术语管理工具
- `azur_lane_glossary_detailed.csv` — 2809 行；追加 `src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives`
- `azur_lane_ship_character_glossary.csv` — `source,target,tgt_lng` 三列，3084 行；`target` 为英文舰名，`source` 含简中服实际显示名（含和谐名）
- `azur_lane_ship_character_glossary_detailed.csv` — 3104 行；额外列同上
- `azur_lane_terms.csv` — `source,target,tgt_lng` 三列，404 行；航海／军事／游戏术语
- `azur_lane_terms_detailed.csv` — 404 行；追加 `src_lng,category,category_zh,same_source_alternatives`

同级的 `by_language/` 提供按源语言拆分的舰船子表（`target` 一律为简中），
`sources/` 保存萌娘百科《碧蓝航线/名称对照表》的抓取结果，用于和谐名交叉校验。

## 分类与条数

| 表 | 对照行 | 词条数（`target` 去重） |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 2795 | 821 |
| `azur_lane_glossary_detailed.csv` | 2809 | 823 |
| `azur_lane_ship_character_glossary.csv` | 3084 | 855 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3104 | 857 |
| `azur_lane_terms.csv` | 404 | 154 |
| `azur_lane_terms_detailed.csv` | 404 | 154 |

舰船变体（按 `azur_lane_ship_character_glossary_detailed.csv` 的 `variant` 统计）：

| 变体 | 舰船数（`ship_id` 去重） | 对照行 |
| --- | --- | --- |
| 本体（无变体标记） | 788 | 2760 |
| META | 60 | 225 |
| μ兵装 | 19 | 82 |
| II 型 | 10 | 37 |
| **合计** | **877** | **3104** |

（同一表的 `target` 去重后为 **857** 条 —— 个别舰船在不同 id 下使用同一英文显示名。）

术语五类（按 `azur_lane_terms_detailed.csv` 的 `category` 统计）：

| `category` | 主题 | 词条数 | 对照行 |
| --- | --- | --- | --- |
| `hull_type` | 舰种 | 29 | 78 |
| `naval_term` | 航海／军事术语 | 67 | 186 |
| `navy_prefix` | 阵营与舰名前缀 | 23 | 56 |
| `rank` | 军衔 | 13 | 27 |
| `game_term` | 游戏术语 | 22 | 57 |
| **合计** | — | **154** | **404** |

## 说明

- **译文来源与对齐方式**：舰船名取自官方 CN / EN / JP / KR / TW 五服客户端配置；
  舰船唯一性以 `ship_skin_template.json` 的 `ship_group` 归一，并按 `ship_data_template.json`
  过滤敌方／NPC 副本。EN 服个别舰船完全没有英文名，此时以该服 `english_name`
  （去掉 `USS`/`HMS` 等舷号前缀）补位，可能与游戏内实际显示名不完全一致。
  术语表为人工整理并逐条与各服配置校对。每个源串在本目录主表只保留一条译文，
  多解时取**舰船 id 最小者**，全部读法记入明细表的 `same_source_alternatives`。
- **语言标签**：本目录所有 CSV 的 `tgt_lng` 列固定为 `en-US`；明细表的 `src_lng` 取值为
  `zh-CN` / `ja-JP` / `zh-TW` / `ko-KR`（术语表为 `zh-CN` / `ja-JP` / `ko-KR`）。
  注意 `zh-CN` 目录的舰船明细表改用 `en` / `ja` / `ko` / `zh-TW` 这类短标签，
  标签风格在各目录之间并不统一，但不影响任何译文内容。
  同名的 `by_language/azur_lane_glossary_en-zh-CN.csv` 是同一批英文源串以简中为目标语言的视图。
- **编码**：所有 CSV 均为 **UTF-8 with BOM + CRLF**，Excel 可直接打开；`.md` 为 UTF-8 无 BOM。
- **已知限制**：
  - 部分舰船在 EN 服配置中没有英文名，只能用 `english_name` 的舷号全称补位，因此可能与游戏内显示名不同。
  - EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），与本服 `english_name`
    的 `Ark Royal.META` 不符 —— 为游戏原始数据问题，未作人工改写。
  - 只有亚尔薇特（Alvitr，铁血战巡，ship_id 404061）一名铁血角色无简中和谐名。
  - 本目录不含 `azur_lane_ambiguous.csv` 与 `azur_lane_combined_ships_and_terms.csv`，这两个文件仅在 `zh-CN` 提供。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件
（包括但不限于沉浸式翻译）的术语匹配，**不应被视为《碧蓝航线》的官方术语表或官方本地化文件**。
库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致；游戏名称、角色名称、专有名词、
商标等知识产权均归各自权利人所有，本库不主张任何相关权利，使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
