# 碧蓝航线 术语库 — 日本語（`ja-JP`）

[← 返回游戏总说明](../README.md)

本目录是**以日文（`ja-JP`）为目标语言**的《碧蓝航线》术语库：`target` 列固定为日文写法，
`source` 列收录简体中文、英文、繁体中文与韩文的写法。共 **6 个 CSV、15 519 行对照**，
其中 3 个主表合计 **7 677 行 / 877 + 877 + 125 条去重词条**。
日文舰名直接取自官方 JP 服客户端配置，属**官方本地化文本**，**不是机器翻译**。

## 文件

- `azur_lane_glossary.csv` — `source,target,tgt_lng` 三列，3516 行；舰船名（标准名表），可直接导入 CAT / 术语管理工具
- `azur_lane_glossary_detailed.csv` — 3596 行；追加 `src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives`
- `azur_lane_ship_character_glossary.csv` — `source,target,tgt_lng` 三列，3805 行；`target` 为日文舰名，`source` 含简中服实际显示名（含和谐名）
- `azur_lane_ship_character_glossary_detailed.csv` — 3890 行；额外列同上
- `azur_lane_terms.csv` — `source,target,tgt_lng` 三列，356 行；航海／军事／游戏术语
- `azur_lane_terms_detailed.csv` — 356 行；追加 `src_lng,category,category_zh,same_source_alternatives`

同级的 `by_language/` 提供按源语言拆分的舰船子表（`target` 一律为简中），
`sources/` 保存萌娘百科《碧蓝航线/名称对照表》的抓取结果，用于和谐名交叉校验。

## 分类与条数

| 表 | 对照行 | 词条数（`target` 去重） |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 3516 | 877 |
| `azur_lane_glossary_detailed.csv` | 3596 | 879 |
| `azur_lane_ship_character_glossary.csv` | 3805 | 877 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3890 | 879 |
| `azur_lane_terms.csv` | 356 | 125 |
| `azur_lane_terms_detailed.csv` | 356 | 125 |

舰船变体（按 `azur_lane_ship_character_glossary_detailed.csv` 的 `variant` 统计）：

| 变体 | 舰船数（`ship_id` 去重） | 对照行 |
| --- | --- | --- |
| 本体（无变体标记） | 795 | 3466 |
| META | 60 | 280 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合计** | **884** | **3890** |

（同一表的 `target` 去重后为 **879** 条 —— 个别舰船在不同 id 下使用同一日文显示名。）

术语五类（按 `azur_lane_terms_detailed.csv` 的 `category` 统计）：

| `category` | 主题 | 词条数 | 对照行 |
| --- | --- | --- | --- |
| `hull_type` | 舰种 | 22 | 77 |
| `naval_term` | 航海／军事术语 | 62 | 178 |
| `navy_prefix` | 阵营与舰名前缀 | 11 | 32 |
| `rank` | 军衔 | 12 | 20 |
| `game_term` | 游戏术语 | 18 | 49 |
| **合计** | — | **125** | **356** |

## 说明

- **译文来源与对齐方式**：舰船名取自官方 CN / EN / JP / KR / TW 五服客户端配置；
  舰船唯一性以 `ship_skin_template.json` 的 `ship_group` 归一，并按 `ship_data_template.json`
  过滤敌方／NPC 副本。术语表为人工整理并逐条与各服配置校对。
  每个源串在本目录主表只保留一条译文，多解时取**舰船 id 最小者**，全部读法记入明细表的
  `same_source_alternatives`。例：`HMS Belfast` 同时对应 `ベルファスト`（id 202121）与
  `ベルちゃん`（id 202181），主表保留 `ベルファスト`。
- **语言标签**：本目录所有 CSV 的 `tgt_lng` 列固定为 `ja-JP`；明细表的 `src_lng` 取值为
  `zh-CN` / `en-US` / `zh-TW` / `ko-KR`（术语表为 `zh-CN` / `en-US` / `ko-KR`）。
  注意 `zh-CN` 目录的舰船明细表改用 `en` / `ja` / `ko` / `zh-TW` 这类短标签，
  标签风格在各目录之间并不统一，但不影响任何译文内容。
  同名的 `by_language/azur_lane_glossary_ja-zh-CN.csv` 是同一批日文源串以简中为目标语言的视图。
- **编码**：所有 CSV 均为 **UTF-8 with BOM + CRLF**，Excel 可直接打开；`.md` 为 UTF-8 无 BOM。
- **已知限制**：
  - 与简中同形的汉字舰名（`吹雪`、`雷`、`杜威`、`Z1` 等）属正常情况，一律保留；
    只有不使用汉字的服（EN、KR）沿用简中字符串时才视为未翻译并剔除。
  - EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），为游戏原始数据问题，未作人工改写。
  - 只有亚尔薇特（Alvitr，铁血战巡，ship_id 404061）一名铁血角色无简中和谐名。
  - 本目录不含 `azur_lane_ambiguous.csv` 与 `azur_lane_combined_ships_and_terms.csv`，这两个文件仅在 `zh-CN` 提供。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件
（包括但不限于沉浸式翻译）的术语匹配，**不应被视为《碧蓝航线》的官方术语表或官方本地化文件**。
库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致；游戏名称、角色名称、专有名词、
商标等知识产权均归各自权利人所有，本库不主张任何相关权利，使用本项目所引发的一切责任由使用者自行承担。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
