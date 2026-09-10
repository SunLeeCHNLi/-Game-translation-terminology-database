# 碧蓝航线（Azur Lane）翻译术语库

数据来源：`AzurLaneData-main` 官方多语言配置（CN / EN / JP / KR / TW 五服 `sharecfgdata` / `ShareCfg`，简中服版本 9.6.667）。
舰船名全部直接抽取自游戏配置；术语表为人工整理并逐条与各服配置校对，未做机器翻译。

---

## 目录结构

```
AzurLane_Glossary/
├─ zh-CN/   ├─ en-US/   ├─ ja-JP/   ├─ ko-KR/      四个目标语言的术语表
│     azur_lane_glossary.csv                舰船名（简中标准名为源）
│     azur_lane_glossary_detailed.csv
│     azur_lane_ship_character_glossary.csv 舰船名（简中和谐名为源）
│     azur_lane_ship_character_glossary_detailed.csv
│     azur_lane_terms.csv                   航海/军事/游戏术语
│     azur_lane_terms_detailed.csv
│     （zh-CN 另有 azur_lane_ambiguous.csv、azur_lane_combined_ships_and_terms.csv，
│       这两个文件本来就是「外语 → 简中」，没有其它语言版本）
├─ by_language/     按 en / ja / zh-TW / ko 拆分的舰船子表（target 均为简中）
├─ sources/         萌娘百科《碧蓝航线/名称对照表》抓取结果，用于交叉校验
├─ azur_lane_ship_names_multilingual.csv   891 艘舰船的中/英/日/繁/韩五语总表（源数据）
├─ azur_lane_harmonized_ship_names.csv     和谐名对照（中文原名 → 中文和谐名，1187 条）
├─ azur_lane_harmonized_names_detailed.csv
├─ azur_lane_harmonized_equipment.csv      舰载机等装备和谐名 8 条
├─ azur_lane_ijn_codename_aliases.csv      旧日本海军单字代称对照（柚 → 绫波）
└─ *.py / README.md / build_stats.json     生成脚本与说明
```

以上四个语言目录内的文件结构完全一致，`target` 为该语言的名称，`tgt_lng` 相应为
`zh-CN` / `en-US` / `ja-JP` / `ko-KR`；`source` 收录其余所有语言的写法。

---

## 一、舰船角色术语表

| 文件 | zh-CN | en-US | ja-JP | ko-KR |
| --- | --- | --- | --- | --- |
| `azur_lane_glossary.csv`（标准简中名为源） | 3514 | 2795 | 3516 | 3481 |
| `azur_lane_ship_character_glossary.csv`（和谐简中名为源） | 3804 | 3084 | 3805 | 3769 |

- 覆盖 **891 艘舰船 / 884 名舰船角色**，含 META、μ兵装、II 型、联动舰船。
- `azur_lane_ship_character_glossary` 的 `target` 一律为**简中服实际显示名称**：
  有和谐名的用和谐名（**295 名**），没有的用标准中文名；其余语言版本则以对应语种舰名为 `target`。
- 源语言包含：简中标准名、简中和谐名、英文名、英文全称（如 `IJN Fubuki`）、日文名、繁体名、韩文名。
- 示例（每个语言目录内的实际条目）：

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| Enterprise                | 企业               | zh-CN   |
| エンタープライズ                 | 企业               | zh-CN   |
| Sheffield META            | 谢菲尔德·META        | zh-CN   |
| シェフィールド(META)             | 谢菲尔德·META        | zh-CN   |
| Illustrious μ             | 光辉(μ兵装)          | zh-CN   |
| イラストリアス(μ兵装)              | 光辉(μ兵装)          | zh-CN   |
| 柚                         | Ayanami           | en-US   |
| 柚                         | 綾波                | ja-JP   |
| 柚                         | 아야나미               | ko-KR   |
```

- 每个源词条在主表只保留一条译文；同名多解（如 `HMS Belfast` → `ベルファスト` / `ベルちゃん`）
  取舰船 id 最小者，全部可能写法记入 detailed 表的 `same_source_alternatives`。
- 只有 **亚尔薇特（Alvitr，铁血战巡）** 一名铁血角色无和谐名 —— 游戏文件与社区对照表均无该条目。

---

## 二、航海 / 军事 / 游戏术语表

`azur_lane_terms.csv`：共 **176 个概念**，按源语言 479 条词条（英文 175、日文 127、韩文 176、中文概念名 176）整理。

| 目标语言 | 条目数 |
| --- | --- |
| `zh-CN/azur_lane_terms.csv` | 449 |
| `en-US/azur_lane_terms.csv` | 404 |
| `ja-JP/azur_lane_terms.csv` | 356 |
| `ko-KR/azur_lane_terms.csv` | 459 |

- 五大类：`hull_type` 舰种 31、`naval_term` 航海/军事术语 69、`navy_prefix` 阵营与舰名前缀 25、
  `rank` 军衔 25、`game_term` 游戏术语 26（detailed 表带 `category` / `category_zh` 列）。
- 同一源词有多个概念时（如韩文 `대령` 既指「海军上校」也指「大佐」），主表取首个概念，
  其余写法记入 detailed 表的 `same_source_alternatives`。
- 示例（`ko-KR`）：

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

---

## 字段与数据清洗

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

## 已知数据瑕疵

- EN 服配置中 `皇家方舟·META` 的舰名写作 `Royal.META`（缺少 `Ark`），
  与本服 `english_name` 的 `Ark Royal.META` 不符 —— 为游戏原始数据问题，未作人工改写。

## 重新生成

```bash
python build_glossary.py                    # 舰船词库（简中标准名）+ 五语总表 + by_language
python build_harmonized.py                  # 和谐名对照表
python build_ship_character_glossary.py     # 舰船角色术语表（简中和谐名）
python build_multilang_glossaries.py        # 舰船的 en-US / ja-JP / ko-KR 版本
python build_terms_glossaries.py            # 术语表的 zh-CN / en-US / ja-JP / ko-KR 版本
```

游戏数据更新后按上表顺序重跑即可（`build_multilang_glossaries.py` 依赖五语总表）。
术语词条在 `terms_data.py` 中维护，四个语言版本由 `build_terms_glossaries.py` 自动生成。
