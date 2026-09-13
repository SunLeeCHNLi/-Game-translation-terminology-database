# 《蔚蓝档案》Blue Archive 翻译术语库 / Blue Archive Terminology Database / ブルーアーカイブ 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库收录手游《蔚蓝档案》（Blue Archive / ブルーアーカイブ）的专有名词对照表，覆盖角色名称、学校、社团、剧情标题、爱用品、地名、术语、活动、剧情角色、敌人、技能、道具、装备、家具、关卡共 15 个分类。全部 15 个分类合计 **7535** 条词条，按目标语言拆分为 **6** 套独立术语库（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `th-TH`），每套分别另有 15 个分类文件与一份合并总表。译文取自官方客户端多语言文本，按同一文本键对齐，属于**官方本地化**而非二次翻译；官方数据未覆盖的少量条目由社区剧情对照表补齐。

## 使用方法

1. **单文件下载**：进入对应语言目录（例如 `zh-CN/`），下载 `01_character/01_character_glossary.csv` 之类的分类术语表，直接导入沉浸式翻译等术语工具即可，无需任何转换。
2. **整个语言目录打包下载**：若需要全部 15 个分类，下载该语言目录下的全部分类文件，或直接取 `00_master/all_glossary.csv`（该语言全部对照行的合并总表）。
3. **克隆整个仓库自行复现**：`git clone` 本仓库后，配合已收录在 `tools/` 下的生成脚本，以及脚本文档字符串里引用的三个上游仓库源码，即可从原始数据重新生成全部 CSV。

## 目录结构

```text
Blue_Archive_Glossary（蔚蓝档案）/
  zh-CN/                    以简体中文为目标语言的术语库
    00_master/              索引 + 合并总表 + 说明
      all_glossary.csv      全部 15 个分类的对照行合并总表
      all_terms.csv         本语言全部词条清单
      index.csv             分类索引与条数（分类条数的权威来源）
      README.md             本语言库的详细说明
    01_character/           角色名称
    02_school/              学校
    03_club/                社团
    04_story_title/         剧情标题
    05_favor_item/          爱用品
    06_location/            地名
    07_terminology/         术语
    08_event/               活动
    09_scenario_character/  剧情角色
    10_enemy/               敌人
    11_skill/               技能
    12_item/                道具
    13_equipment/           装备
    14_furniture/           家具
    15_stage/               关卡
  zh-TW/                    同上结构（以繁体中文为目标语言）
  en-US/                    同上结构（以 English 为目标语言）
  ja-JP/                    同上结构（以日本語为目标语言）
  ko-KR/                    同上结构（以한국어为目标语言）
  th-TH/                    同上结构（以ภาษาไทย为目标语言）
  multilingual/             六语并排总表
    00_master/
      all_terms_multilingual.csv   全部词条，一条一行、六语并排
      README.md                    总表说明与列定义
    01_character/           01_character_multilingual.csv
    02_school/              02_school_multilingual.csv
    03_club/                03_club_multilingual.csv
    04_story_title/         04_story_title_multilingual.csv
    05_favor_item/          05_favor_item_multilingual.csv
    06_location/            06_location_multilingual.csv
    07_terminology/         07_terminology_multilingual.csv
    08_event/               08_event_multilingual.csv
    09_scenario_character/  09_scenario_character_multilingual.csv
    10_enemy/               10_enemy_multilingual.csv
    11_skill/               11_skill_multilingual.csv
    12_item/                12_item_multilingual.csv
    13_equipment/           13_equipment_multilingual.csv
    14_furniture/           14_furniture_multilingual.csv
    15_stage/               15_stage_multilingual.csv
  tools/                    生成脚本与生成元数据
    build_glossary.py       术语库生成脚本（Python）
    extract_ts_titles.mjs   剧情标题提取脚本（需要 Node.js）
    ts_titles.json          剧情标题提取结果（`extract_ts_titles.mjs` 的缓存，`build_glossary.py` 直接读取）
  README.md                 本说明（简体中文）
  README_EN.md              英文说明
  README_JP.md              日文说明
```

每个语言目录下的 `NN_xxx/` 都只有两个文件：`NN_xxx_glossary.csv` 与 `NN_xxx_terms.csv`（`multilingual/` 下则是单个 `NN_xxx_multilingual.csv`）。

## 数据概览

各语言词条数与对照行数（`00_master/index.csv` 与 CSV 数据行实测一致）：

| 文件夹 | 语言 | 词条数 | 对照行数 |
| --- | --- | ---: | ---: |
| `zh-CN/` | 简体中文 | 7477 | 29463 |
| `zh-TW/` | 繁体中文 | 6036 | 27453 |
| `en-US/` | English | 5909 | 26623 |
| `ja-JP/` | 日本語 | 7534 | 29216 |
| `ko-KR/` | 한국어 | 7310 | 29009 |
| `th-TH/` | ภาษาไทย | 5908 | 26478 |

分类 × 目标语言（单元格为**该语言下实际存在的词条数**，取自各语言 `00_master/index.csv`）：

| 分类 | 主题 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` | `th-TH` |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `01_character` | 角色名称 | 408 | 408 | 204 | 408 | 408 | 204 |
| `02_school` | 学校 | 26 | 26 | 26 | 26 | 26 | 26 |
| `03_club` | 社团 | 43 | 43 | 43 | 43 | 43 | 43 |
| `04_story_title` | 剧情标题 | 1086 | 680 | 665 | 1144 | 1051 | 664 |
| `05_favor_item` | 爱用品 | 51 | 51 | 51 | 51 | 51 | 51 |
| `06_location` | 地名 | 90 | 8 | 8 | 90 | 8 | 8 |
| `07_terminology` | 术语 | 1402 | 1379 | 1379 | 1401 | 1379 | 1379 |
| `08_event` | 活动 | 72 | 45 | 45 | 72 | 45 | 45 |
| `09_scenario_character` | 剧情角色 | 945 | 134 | 134 | 945 | 945 | 134 |
| `10_enemy` | 敌人 | 351 | 349 | 351 | 351 | 351 | 351 |
| `11_skill` | 技能 | 1069 | 1069 | 1069 | 1069 | 1069 | 1069 |
| `12_item` | 道具 | 649 | 649 | 649 | 649 | 649 | 649 |
| `13_equipment` | 装备 | 155 | 155 | 155 | 155 | 155 | 155 |
| `14_furniture` | 家具 | 472 | 472 | 472 | 472 | 472 | 472 |
| `15_stage` | 关卡 | 658 | 568 | 658 | 658 | 658 | 658 |
| **合计** | | **7477** | **6036** | **5909** | **7534** | **7310** | **5908** |

> `multilingual/00_master/all_terms_multilingual.csv` 是**去重后的词条全集**，共 **7535** 行，一条词条一行、六语并排；该数字比任何单一语言目录的词条数都大，因为它把各语言独有的条目也算进来了。

## 使用的相关内容

| 来源 | 用途 |
| --- | --- |
| [RedBeanN/BlueArchive](https://github.com/RedBeanN/BlueArchive) | 官方客户端多语言数据表（`students` / `items` / `equipment` / `enemies` / `furniture` / `localization` / `stages`），六种语言按 Id 与文本键对齐，是本库的主体 |
| [ba-archive/blue-archive](https://github.com/ba-archive/blue-archive) | 剧情阅览器索引（主线 / 其他 / 地域活动标题、MomoTalk 会话标题）与剧情编辑器名表（剧情角色） |
| [HePudding/ba-storybook](https://github.com/HePudding/ba-storybook) | 社区整理的日→中剧情对照表（剧情标题 / 地名 / 活动 / 剧情角色），用于补齐官方数据表未覆盖的条目 |

## 生成与复现

```bash
# 默认读取 E:\Download\BT\Codex_input 下的三个上游仓库，输出到本游戏目录
python tools/build_glossary.py

# 覆盖输入 / 输出目录
# PowerShell（Windows）：
$env:BA_INPUT_DIR="D:\src"; $env:BA_OUTPUT_DIR="D:\out"; python tools/build_glossary.py
# bash（Linux / macOS）：
BA_INPUT_DIR="/data/src" BA_OUTPUT_DIR="/data/out" python tools/build_glossary.py

# 剧情标题缓存：需要 Node.js，输出 tools/ts_titles.json
node tools/extract_ts_titles.mjs
```

## 说明

- 六种语言的标签：`zh-CN` 简体中文（国服）、`zh-TW` 繁体中文（国际服）、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어、`th-TH` ภาษาไทย；
- 译文取自官方客户端多语言文本，按同一文本键对齐，属于官方本地化而非二次翻译；
- `zh-CN` 与 `zh-TW` 是两套不同的官方本地化，译名并非总是只差繁简，同一个词在学校短名与全名之间也可能不同（例如 `Gehenna`：简中短名「格黑娜」、全名「歌赫娜」，繁中全名「格黑娜學園」）；
- 同一个名称在不同来源间偶有写法差异，本库以官方数据表为准，社区对照表只用于补齐官方表没有的条目；
- 角色分类另附「全名」条目（姓＋名），仅中日韩三种语言：英文与泰文的姓名顺序与中日韩相反，官方数据没有给出可直接拼接的写法；
- `04_story_title`、`06_location`、`09_scenario_character` 以剧情与社区资料为底，会用官方表按完全相同的写法自动补齐语种，因此并非每条都六语齐全；`09_scenario_character` 里的中日韩学生名同样取自官方表，只有官方表没有的 NPC 才使用客户端名表；
- 同一名称存在多条数据时（例如不同等级的同名敌人）会合并为一条；与目标语言写法完全相同的条目不会写入术语表；
- 极少数词条（约 1%–3%）会在**同一个目标语言文件内**出现一条 `source` 对应多个 `target` 的情况，多来自同名不同物的短词（例如 `Normal` 既是装甲类型也是道具稀有度），或简繁两套客户端写法并存；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `_terms.csv` 里的 `id` 与 `src_table` 回查上下文；
- 单个分类文件 `NN_xxx_glossary.csv` 为 `source,target,tgt_lng` 三列；`00_master/all_glossary.csv` 在前面多一列 `category`；`all_terms.csv` 为 `category,category_label,id,term,src_table`；`index.csv` 为 `category,label,term_count,glossary_file,terms_file,target_language`；
- 全部 CSV 为 UTF-8 with BOM、CRLF 换行，Excel 双击即可正确显示中日韩泰文字；`.md` 说明文件为 UTF-8（无 BOM）；
- 重新生成：`python tools/build_glossary.py`（默认读取 `E:\Download\BT\Codex_input`，可用环境变量 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` 覆盖；脚本位于 `tools/`，因此命令行必须带 `tools/` 前缀）。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《蔚蓝档案》的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本项目及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
