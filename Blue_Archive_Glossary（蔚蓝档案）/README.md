# 《蔚蓝档案》Blue Archive 多语术语库 / ブルーアーカイブ 用語集

共 **7535** 条词条，按目标语言拆分为 6 套独立术语库，每套内部再按 15 个分类归档。

## 目录结构

```
Blue_Archive_Glossary（蔚蓝档案）/
  <目标语言>/                6 套独立术语库：zh-CN / ja-JP / zh-TW / en-US / ko-KR / th-TH
    ├─ 00_master/              索引 + 合并总表 + 说明
    ├─ 01_character/           角色名称
    ├─ 02_school/              学校
    ├─ 03_club/                社团
    ├─ 04_story_title/         剧情标题
    ├─ 05_favor_item/          爱用品
    ├─ 06_location/            地名
    ├─ 07_terminology/         术语
    ├─ 08_event/               活动
    ├─ 09_scenario_character/  剧情角色
    ├─ 10_enemy/               敌人
    ├─ 11_skill/               技能
    ├─ 12_item/                道具
    ├─ 13_equipment/           装备
    ├─ 14_furniture/           家具
    └─ 15_stage/               关卡
  multilingual/            六语并排总表
  README.md                本说明
  build_glossary.py        生成脚本
  extract_ts_titles.mjs    剧情标题提取脚本（需要 Node.js）
  ts_titles.json           剧情标题提取结果（脚本的缓存）
```

## 语言文件夹

| 文件夹 | 语言 | 词条数 | 对照行数 |
| --- | --- | ---: | ---: |
| `zh-CN/` | 简体中文 | 7477 | 29463 |
| `ja-JP/` | 日本語 | 7534 | 29216 |
| `zh-TW/` | 繁体中文 | 6036 | 27453 |
| `en-US/` | English | 5909 | 26623 |
| `ko-KR/` | 한국어 | 7310 | 29009 |
| `th-TH/` | ภาษาไทย | 5908 | 26478 |

## 分类与条数

| 分类 | 主题 | `zh-CN` | `ja-JP` | `zh-TW` | `en-US` | `ko-KR` | `th-TH` |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `01_character` | 角色名称 | 408 | 408 | 408 | 204 | 408 | 204 |
| `02_school` | 学校 | 26 | 26 | 26 | 26 | 26 | 26 |
| `03_club` | 社团 | 43 | 43 | 43 | 43 | 43 | 43 |
| `04_story_title` | 剧情标题 | 1086 | 1144 | 680 | 665 | 1051 | 664 |
| `05_favor_item` | 爱用品 | 51 | 51 | 51 | 51 | 51 | 51 |
| `06_location` | 地名 | 90 | 90 | 8 | 8 | 8 | 8 |
| `07_terminology` | 术语 | 1402 | 1401 | 1379 | 1379 | 1379 | 1379 |
| `08_event` | 活动 | 72 | 72 | 45 | 45 | 45 | 45 |
| `09_scenario_character` | 剧情角色 | 945 | 945 | 134 | 134 | 945 | 134 |
| `10_enemy` | 敌人 | 351 | 351 | 349 | 351 | 351 | 351 |
| `11_skill` | 技能 | 1069 | 1069 | 1069 | 1069 | 1069 | 1069 |
| `12_item` | 道具 | 649 | 649 | 649 | 649 | 649 | 649 |
| `13_equipment` | 装备 | 155 | 155 | 155 | 155 | 155 | 155 |
| `14_furniture` | 家具 | 472 | 472 | 472 | 472 | 472 | 472 |
| `15_stage` | 关卡 | 658 | 658 | 568 | 658 | 658 | 658 |
| **合计** | | **7477** | **7534** | **6036** | **5909** | **7310** | **5908** |

## 每个分类里的两个文件

**`NN_xxx_glossary.csv` —— 术语表（source / target / tgt_lng）**

该语言的 `tgt_lng` 固定，`source` 是其余语言的写法，可直接导入术语工具：

| source | target | tgt_lng |
| --- | --- | --- |
| Aru | 爱露 | zh-CN |
| アル | 爱露 | zh-CN |
| 아루 | 爱露 | zh-CN |

**`NN_xxx_terms.csv` —— 本语言词条清单（id / term / src_table）**

| id | term | src_table |
| --- | --- | --- |
| Student.10000 | 爱露 | students.json |

## 数据来源

| 来源 | 用途 |
| --- | --- |
| [RedBeanN/BlueArchive](https://github.com/RedBeanN/BlueArchive) | 官方客户端多语言数据表（`students` / `items` / `equipment` / `enemies` / `furniture` / `localization` / `stages`），六种语言按 Id 与文本键对齐，是本库的主体 |
| [ba-archive/blue-archive](https://github.com/ba-archive/blue-archive) | 剧情阅览器索引（主线 / 其他 / 地域活动标题、MomoTalk 会话标题）与剧情编辑器名表（剧情角色） |
| [HePudding/ba-storybook](https://github.com/HePudding/ba-storybook) | 社区整理的日→中剧情对照表（剧情标题 / 地名 / 活动 / 剧情角色），用于补齐官方数据表未覆盖的条目 |

## 说明

- 六种语言的标签：`zh-CN` 简体中文（国服）、`zh-TW` 繁体中文（国际服）、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어、`th-TH` ภาษาไทย；
- 译文取自官方客户端多语言文本，按同一文本键对齐，属于官方本地化而非二次翻译；
- `zh-CN` 与 `zh-TW` 是两套不同的官方本地化，译名并非总是只差繁简，同一个词在学校短名与全名之间也可能不同（例如 `Gehenna`：简中短名「格黑娜」、全名「歌赫娜」，繁中全名「格黑娜學園」）；
- 同一个名称在不同来源间偶有写法差异，本库以官方数据表为准，社区对照表只用于补齐官方表没有的条目；
- 角色分类另附「全名」条目（姓＋名），仅中日韩三种语言：英文与泰文的姓名顺序与中日韩相反，官方数据没有给出可直接拼接的写法；
- `04_story_title`、`06_location`、`09_scenario_character` 以剧情与社区资料为底，会用官方表按完全相同的写法自动补齐语种，因此并非每条都六语齐全；`09_scenario_character` 里的中日韩学生名同样取自官方表，只有官方表没有的 NPC 才使用客户端名表；
- 同一名称存在多条数据时（例如不同等级的同名敌人）会合并为一条；与目标语言写法完全相同的条目不会写入术语表；
- 极少数词条（约 1%–3%）会在**同一个目标语言文件内**出现一条 `source` 对应多个 `target` 的情况，多来自同名不同物的短词（例如 `Normal` 既是装甲类型也是道具稀有度），或简繁两套客户端写法并存；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `_terms.csv` 里的 `id` 与 `src_table` 回查上下文；
- 重新生成：`python build_glossary.py`（默认读取 `E:\Download\BT\Codex_input`，可用环境变量 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` 覆盖）。
