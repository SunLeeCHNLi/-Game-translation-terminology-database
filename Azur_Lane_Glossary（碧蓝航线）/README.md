# 《碧蓝航线》Azur Lane 翻译术语库 / Azur Lane Terminology Database / Azur Lane 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库收录手机游戏《碧蓝航线》（Azur Lane）的舰船名与航海／军事／游戏术语，覆盖 **4 套目标语言**：
简体中文（`zh-CN`）、English（`en-US`）、日本語（`ja-JP`）、한국어（`ko-KR`）。
共收录 **891 艘舰船**（含本体、META、μ兵装、II 型与联动舰船，生成表中 **884 名舰船角色**）
与 **176 个术语概念**（其中 175 个在其他语言中存在可对照写法）。
舰船名全部直接抽取自官方多语言客户端配置（CN / EN / JP / KR / TW 五服 `sharecfgdata` / `ShareCfg`，抽取时简中服配置版本 9.6.667），
属**官方本地化文本**，既非机器翻译、也非由英文二次转译；术语表为人工整理并逐条与各服配置校对，和谐名另经社区对照表交叉校验。

## 使用方法

1. **单文件下载**：进入对应语言目录（如 `en-US/`），下载 `azur_lane_glossary.csv`、`azur_lane_ship_character_glossary.csv` 或 `azur_lane_terms.csv`，即可直接导入沉浸式翻译等术语工具。
2. **整个语言目录打包下载**：一次取得该语言的舰船名与术语全部条目（含 `*_detailed.csv` 明细表）。
3. **克隆整个仓库自行复现**：配合 `tools/` 下的脚本与上游 `AzurLaneData` 配置（见「使用的相关内容」）重跑生成流程。

## 目录结构

```text
Azur_Lane_Glossary（碧蓝航线）/
├─ zh-CN/                                  简体中文术语库（target = 简中）
│     azur_lane_glossary.csv                   舰船名（简中标准名为源）
│     azur_lane_glossary_detailed.csv          同上 + ship_id / 舰种 / 阵营 / 变体
│     azur_lane_ship_character_glossary.csv    舰船名（简中和谐名为源）
│     azur_lane_ship_character_glossary_detailed.csv
│     azur_lane_terms.csv                      航海 / 军事 / 游戏术语
│     azur_lane_terms_detailed.csv             同上 + category / same_source_alternatives
│     azur_lane_ambiguous.csv                  一名多解的源词条（仅 zh-CN）
│     azur_lane_combined_ships_and_terms.csv   舰船 + 术语合并版（仅 zh-CN）
│     README.md                                本目录说明（简体中文）
├─ en-US/                                  同上 6 个 CSV + README.md / README_zh-CN.md
├─ ja-JP/                                  同上 6 个 CSV + README.md / README_zh-CN.md
├─ ko-KR/                                  同上 6 个 CSV + README.md / README_zh-CN.md
├─ by_language/                            按源语言拆分的舰船子表，target 一律为简中
│     azur_lane_glossary_en-zh-CN.csv
│     azur_lane_glossary_ja-zh-CN.csv
│     azur_lane_glossary_ko-zh-CN.csv
│     azur_lane_glossary_zh-TW-zh-CN.csv
├─ sources/
│     moegirl_name_table.json              萌娘百科《碧蓝航线/名称对照表》抓取结果，用于交叉校验
├─ tools/                                  生成脚本与统计元数据
│     build_glossary.py                        舰船词库（简中标准名）+ 五语总表 + by_language + 歧义表 + 单字代称
│     build_harmonized.py                      和谐名对照表
│     build_ship_character_glossary.py         舰船角色术语表（简中和谐名）
│     build_multilang_glossaries.py            舰船的 en-US / ja-JP / ko-KR 版本
│     build_terms_glossaries.py                术语表的四语版本
│     terms_data.py                            术语词条数据源（人工维护）
│     build_stats.json                         生成统计元数据（上次构建输出）
├─ azur_lane_ship_names_multilingual.csv   891 艘舰船的中/英/日/繁/韩五语总表（源数据）
├─ azur_lane_harmonized_ship_names.csv     和谐名对照（原名 → 和谐名，1187 行）
├─ azur_lane_harmonized_names_detailed.csv 和谐名明细（1259 行，含萌娘百科校验注记）
├─ azur_lane_harmonized_equipment.csv      舰载机等装备和谐名 8 条
├─ azur_lane_ijn_codename_aliases.csv      旧日本海军单字代称对照（柚 → 绫波，1082 行）
└─ README.md / README_EN.md / README_JP.md 中文 / English / 日本語说明
```

四个语言目录的入口文件结构完全一致（`zh-CN` 另有 `azur_lane_ambiguous.csv` 与
`azur_lane_combined_ships_and_terms.csv` 两个文件）：`target` 为该语言的名称，
`tgt_lng` 相应固定为 `zh-CN` / `en-US` / `ja-JP` / `ko-KR`；`source` 收录其余所有语言的写法。
`by_language/` 是同一批舰船的**源语言侧视图**（英语 1544 行、日语 696 行、韩语 814 行、繁体 538 行，
合计 3592 行 = `zh-CN/azur_lane_glossary_detailed.csv` 的行数）。

## 数据概览

### 词条数与对照行数

| 语言 | 舰船名·标准简中名为源<br>词条 / 对照行 | 舰船名·和谐简中名为源<br>词条 / 对照行 | 术语<br>词条 / 对照行 |
| --- | --- | --- | --- |
| `zh-CN` | 877 / 3514 | 875 / 3804 | 170 / 449 |
| `en-US` | 821 / 2795 | 855 / 3084 | 154 / 404 |
| `ja-JP` | 877 / 3516 | 877 / 3805 | 125 / 356 |
| `ko-KR` | 850 / 3481 | 850 / 3769 | 165 / 459 |

- **词条数** = 该语言目录的 `azur_lane_*.csv` 中 `target` 列去重后的条数（即该语言有译名的舰船／术语数）；
  **对照行数** = CSV 数据行数，不含表头（UTF-8 with BOM + CRLF，Excel 可直接打开）。
- 同名明细表：`azur_lane_glossary_detailed.csv` 行数为 3592（zh-CN）/ 2809（en-US）/ 3596（ja-JP）/ 3525（ko-KR）；
  `azur_lane_ship_character_glossary_detailed.csv` 行数为 3890 / 3104 / 3890 / 3818。
- 仅 `zh-CN` 提供的两个附加表：`azur_lane_ambiguous.csv` 162 行（涉及 77 个一名多解的源串）、
  `azur_lane_combined_ships_and_terms.csv` 3985 行（舰船 3592 行与术语 475 行合并去重后）。

### 分类 × 条数

舰船变体（以 `zh-CN/azur_lane_ship_character_glossary_detailed.csv` 统计，共 **884 名舰船角色**）：

| 变体 | 舰船数 | 对照行 |
| --- | --- | --- |
| 本体（无变体标记） | 795 | 3466 |
| META | 60 | 280 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合计** | **884** | **3890** |

术语五类（以 `zh-CN/azur_lane_terms_detailed.csv` 统计）：

| `category` | 主题 | 概念数 | 对照行 |
| --- | --- | --- | --- |
| `hull_type` | 舰种 | 31 | 97 |
| `naval_term` | 航海／军事术语 | 72 | 198 |
| `navy_prefix` | 阵营与舰名前缀 | 24 | 59 |
| `rank` | 军衔 | 24 | 44 |
| `game_term` | 游戏术语 | 24 | 61 |
| **合计** | — | **175** | **459** |

`tools/terms_data.py` 中人工维护的原始词条共 **478 条**（英文 175、日文 127、韩文 176），
生成时按 `(source, target, src_lng)` 去重；其中 `META`（归类 `navy_prefix`）因源串与目标串同为 `META` 而被剔除，
故生成表中实际只有 175 个概念带对照行。

### 舰船角色术语表

| 文件 | zh-CN | en-US | ja-JP | ko-KR |
| --- | --- | --- | --- | --- |
| `azur_lane_glossary.csv`（标准简中名为源） | 3514 | 2795 | 3516 | 3481 |
| `azur_lane_ship_character_glossary.csv`（和谐简中名为源） | 3804 | 3084 | 3805 | 3769 |

- 覆盖 **891 艘舰船 / 884 名舰船角色**，含 META、μ兵装、II 型、联动舰船。
- `azur_lane_ship_character_glossary` 的 `target` 一律为**简中服实际显示名称**：
  有和谐名的用和谐名（**295 名**），没有的用标准中文名；其余语言版本则以对应语种舰名为 `target`。
- 源语言包含：简中标准名、简中和谐名、英文名、英文全称（如 `IJN Fubuki`）、日文名、繁体名、韩文名。
- 示例（`azur_lane_glossary.csv`，每个语言目录内的实际条目）：

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| Enterprise                | 企业               | zh-CN   |
| エンタープライズ                 | 企业               | zh-CN   |
| Sheffield META            | 谢菲尔德·META        | zh-CN   |
| シェフィールド(META)             | 谢菲尔德·META        | zh-CN   |
| Illustrious μ             | 光辉(μ兵装)          | zh-CN   |
| イラストリアス(μ兵装)              | 光辉(μ兵装)          | zh-CN   |
```

- 示例（`azur_lane_ship_character_glossary.csv`，和谐简中名为源；`柚` 是 `绫波` 的简中和谐名）：

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| 柚                         | Ayanami           | en-US   |
| 柚                         | 綾波                | ja-JP   |
| 柚                         | 아야나미               | ko-KR   |
| 绫波                        | Ayanami           | en-US   |
```

- 每个源词条在主表只保留一条译文；同名多解取**舰船 id 最小者**，全部可能写法记入 detailed 表的
  `same_source_alternatives`。例：`ja-JP/azur_lane_glossary_detailed.csv` 中 `HMS Belfast` 同时对应
  `ベルファスト`（id 202121）与 `ベルちゃん`（id 202181），主表保留 id 较小的 `ベルファスト`，
  两个读法都写在 `same_source_alternatives` 里；`zh-CN` 侧对应 `贝尔法斯特` / `小贝法`。
- 只有 **亚尔薇特（Alvitr，铁血战巡，ship_id 404061）** 一名铁血角色无和谐名 —— 游戏配置与社区对照表均无该条目。

### 航海 / 军事 / 游戏术语表

`azur_lane_terms.csv`：人工维护 **176 个概念**（生成表中 175 个带对照行），原始源语言词条 478 条
（英文 175、日文 127、韩文 176）。

| 目标语言 | 条目数 |
| --- | --- |
| `zh-CN/azur_lane_terms.csv` | 449 |
| `en-US/azur_lane_terms.csv` | 404 |
| `ja-JP/azur_lane_terms.csv` | 356 |
| `ko-KR/azur_lane_terms.csv` | 459 |

- 五大类：`hull_type` 舰种 31、`naval_term` 航海／军事术语 72、`navy_prefix` 阵营与舰名前缀 24、
  `rank` 军衔 24、`game_term` 游戏术语 24（detailed 表带 `category` / `category_zh` 列）。
- 同一源词有多个概念时（如韩文 `대령` 既指「海军上校」也指「大佐」），主表取首个概念，
  其余写法记入 detailed 表的 `same_source_alternatives`。
- 示例（`ko-KR/azur_lane_terms.csv`）：

```
| source         | target   | tgt_lng |
| -------------- | -------- | ------- |
| 驱逐舰            | 구축함      | ko-KR   |
| Destroyer      | 구축함      | ko-KR   |
| 駆逐艦            | 구축함      | ko-KR   |
| 铁血             | 메탈 블러드   | ko-KR   |
| Iron Blood     | 메탈 블러드   | ko-KR   |
| 海军上将           | 대장       | ko-KR   |
```

- **韩文来源**：舰种、阵营名、游戏内用语取自 KR 服自身配置
  （`ship_data_by_type` → `구축/경순/중순/…`、`fleet_tech_group` → `이글 유니온`/`메탈 블러드`、
  `world_port_data`、`medal_template`、`emoji_template` → `한계돌파`、`enemy_data_statistics` → `특장형 부린` 等），
  其余航海与军衔用语为通用韩文标准译名。游戏内舰种显示为缩写（구축 / 경순 / …），
  术语表统一使用完整形式（구축함 / 경순양함 / …）。

### 字段与数据清洗

- `source` 源词条，`target` 目标语言词条，`tgt_lng` 目标语言，`src_lng` 源语言（detailed 表）。
- 抽取过程已处理：英文名串位（CN/JP/KR/TW 的 `english_name` 不可信，一律取 EN 服）、
  节日皮肤代号（`qipao`/`shengdan`/`xinnian` 等）混入、本体与皮肤/活动副本重复、
  敌方与 NPC 副本（用 `ship_data_template` 过滤）、`？？？？？` 占位名。
- 舰船唯一性以 `ship_skin_template.json` 的 `ship_group` 为准。
- **未翻译回退**：某服配置直接沿用简中字符串时视为未翻译，仅对**不使用汉字**的服
  （EN、KR）剔除；JP / TW 服的汉字名与简中相同属正常情况
  （如 `吹雪`、`雷`、`杜威`、`Z1`），一律保留。
- EN 服个别舰船完全没有英文名（如 `企业·META`），以该服的 `english_name`
  （去掉 `USS`/`HMS` 等舷号前缀）补位。
- detailed 表的列名在 `zh-CN` 与其他三语之间略有差异：`zh-CN` 用 `ship_type` / `nation`，
  另外三语用 `ship_type_zh` / `ship_type_en` / `nation_zh` / `nation_en`，
  并额外带 `zh_CN_form` / `zh_CN_standard` / `zh_CN_harmonised` 三列。

### 已知数据瑕疵

- EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），
  与本服 `english_name` 的 `Ark Royal.META` 不符 —— 为游戏原始数据问题，未作人工改写。

## 使用的相关内容

| 来源 | 用途 |
| --- | --- |
| [AzurLaneTools/AzurLaneData](https://github.com/AzurLaneTools/AzurLaneData) | CN / EN / JP / KR / TW 五服客户端配置：`sharecfgdata/ship_data_statistics.json`（各服舰船名）、`sharecfgdata/ship_data_template.json`（舰船唯一性过滤）、`ShareCfg/ship_skin_template.json`（`ship_group` 归一）、`ShareCfg/ship_data_by_type.json`（舰种名）、`ShareCfg/name_code.json`（和谐名与单字代称） |
| 萌娘百科《[碧蓝航线/名称对照表](https://zh.moegirl.org.cn/碧蓝航线/名称对照表)》 | 和谐名交叉校验；抓取结果保存在 `sources/moegirl_name_table.json`，不一致的条目在 `azur_lane_harmonized_names_detailed.csv` 的 `wiki_note` 列注明 |

## 生成与复现

脚本位于 `tools/`，一律以 `tools/` 为前缀调用（在游戏目录下执行）：

```bash
# 1) 舰船词库（简中标准名）+ 五语总表 + by_language + 歧义表 + IJN 单字代称
python tools/build_glossary.py

# 2) 和谐名对照表（依赖 1) 产出的五语总表）
python tools/build_harmonized.py

# 3) 舰船角色术语表（简中和谐名）
python tools/build_ship_character_glossary.py

# 4) 舰船的 en-US / ja-JP / ko-KR 版本（依赖 1) 产出的五语总表）
python tools/build_multilang_glossaries.py

# 5) 术语表的 zh-CN / en-US / ja-JP / ko-KR 版本（数据在 tools/terms_data.py）
python tools/build_terms_glossaries.py
```

游戏数据更新后按上表顺序重跑即可（`build_harmonized.py` 与 `build_multilang_glossaries.py` 依赖
`build_glossary.py` 产出的 `azur_lane_ship_names_multilingual.csv`）。
术语词条在 `tools/terms_data.py` 中维护，四个语言版本由 `build_terms_glossaries.py` 自动生成；
生成统计写入 `build_stats.json`（本仓库内的副本为 `tools/build_stats.json`）。
注意：脚本内的 `BASE` / `OUT` 路径常量指向**仓库外**的上游配置目录与生成工作目录，
重跑前需按本机情况修改（详见各脚本首部的常量定义）；本仓库保存的是生成结果的发布快照。

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
