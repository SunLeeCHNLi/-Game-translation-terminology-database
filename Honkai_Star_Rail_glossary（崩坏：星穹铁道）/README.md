# 《崩坏：星穹铁道》Honkai: Star Rail 翻译术语库 / Honkai: Star Rail Terminology Database / 崩壊：スターレイル 用語集

## [English](README_EN.md) ｜ [日本語](README_JP.md)

本目录收录《崩坏：星穹铁道》（Honkai: Star Rail，HSR）游戏客户端本地化文本中的角色、命途、属性、
技能、行迹、星魂、光锥、遗器、道具、材料、敌人、地点、阵营、任务、关卡、活动、成就、模拟宇宙、
忘却之庭、剧情专有名词、世界观术语、书籍、对话说话者、系统、UI 等专有名词与固定文本。

- 总记录数：**4,085,059**（`source,target,tgt_lng` 三列）
- 去重术语键：**42,126**
- 目标语言：**13**（zh-CN、zh-TW、en-US、ja-JP、ko-KR、fr-FR、de-DE、es-ES、ru-RU、pt-PT、id-ID、th-TH、vi-VN）
- 分类：**26**
- 数据版本：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`
- 全部译名均来自游戏客户端本地化文本，**没有机器翻译，也没有人工猜译**

## 目录结构

```text
Honkai_Star_Rail_glossary（崩坏：星穹铁道）/
├─ README.md / README_EN.md / README_JP.md   本说明（三语）
├─ hsr-glossary/                             正式术语库
│  ├─ README.md                             子库说明
│  ├─ zh-CN/ zh-TW/ en-US/ ja-JP/ ko-KR/     13 个目标语言目录
│  ├─ fr-FR/ de-DE/ es-ES/ ru-RU/ pt-PT/
│  ├─ id-ID/ th-TH/ vi-VN/
│  │  └─ 01_character.csv … 26_other.csv     每语言 26 个分类文件 + README
│  ├─ historical/                            旧版本（2.3.0 / 4.0）译名变化
│  └─ curated/                               少量人工核对条目（开拓者/主角等）
├─ Sources/                                  数据来源记录
├─ Metadata/                                 统计与校验结果
└─ tools/                                    生成与校验脚本
```

每个语言目录都是**扁平结构**：26 个分类 CSV 直接放在语言目录下。

## 文件格式

所有正式术语文件严格只有三列，UTF-8（含 BOM）、CRLF 换行、RFC 4180 转义：

```text
source	target	tgt_lng
Honkai: Star Rail	崩坏：星穹铁道	zh-CN
崩壊：スターレイル	崩坏：星穹铁道	zh-CN
```

- `source`：同一文本键在**其它语言**的官方本地化文本（可匹配原文）
- `target`：当前目录语言的官方本地化文本（译名）
- `tgt_lng`：当前目录语言代码，与目录名一致

- 分隔符与仓库其它游戏保持一致（逗号分隔的 `.csv`）；如需制表符版本，可运行
  `python tools/build_hsr_glossary.py --format tsv` 生成列结构完全相同的 `.tsv` 文件。

`source` 与 `target` 通过**同一 TextMap Hash / 实体 ID** 对齐，不使用字符串相似度猜测。
因此同一个 `target` 会以多行出现（每种可用原文各一行），可以直接用于沉浸式翻译、CAT 工具、
LLM  translators 的术语表导入。

## 分类

| 文件 | 中文名 | English | 独立术语键 | 全语言记录数 |
| --- | --- | --- | ---: | ---: |
| `01_character` | 角色与 NPC | Characters & NPCs | 513 | 37,756 |
| `02_path` | 命途 | Paths | 18 | 2,678 |
| `03_element` | 属性 | Elements | 14 | 1,937 |
| `04_skill` | 技能 | Skills | 825 | 67,089 |
| `05_trace` | 行迹 | Traces | 1,380 | 39,786 |
| `06_eidolon` | 星魂 | Eidolons | 840 | 71,475 |
| `07_light_cone` | 光锥 | Light Cones | 338 | 41,840 |
| `08_relic` | 遗器 | Relics | 918 | 35,527 |
| `09_item` | 道具 | Items | 2,101 | 258,055 |
| `10_material` | 材料 | Materials | 604 | 79,033 |
| `11_enemy` | 敌人 | Enemies | 1,899 | 123,140 |
| `12_location` | 地点 | Locations | 2,315 | 152,554 |
| `13_faction` | 阵营与组织 | Factions | 61 | 4,618 |
| `14_quest` | 任务 | Quests | 10,378 | 866,645 |
| `15_stage` | 关卡与副本 | Stages | 211 | 25,915 |
| `16_event` | 活动 | Events | 2,145 | 192,044 |
| `17_achievement` | 成就 | Achievements | 1,928 | 281,679 |
| `18_simulated_universe` | 模拟宇宙 | Simulated Universe | 3,010 | 264,638 |
| `19_forgotten_hall` | 忘却之庭 | Forgotten Hall | 962 | 126,858 |
| `20_story` | 剧情 | Story | 24 | 2,826 |
| `21_world_lore` | 世界观 | World Lore | 175 | 15,998 |
| `22_book` | 书籍 | Books | 1,100 | 147,763 |
| `23_dialogue` | 对话 | Dialogue | 6,258 | 784,728 |
| `24_system` | 系统 | System | 2,373 | 281,948 |
| `25_ui` | 界面 | UI | 1,315 | 149,681 |
| `26_other` | 其他 | Other | 421 | 28,848 |

## 数据来源与优先级

按官方优先、可验证优先的原则，本轮使用的数据源如下（完整记录见 [`Sources/README.md`](Sources/README.md)）：

- 主数据：`DimbreathBot/TurnBasedGameData` — 客户端 TextMap × 13 语言 + ExcelOutput，版本 4.5.0（commit `4ce30f69b`）
- 结构化交叉验证：`Mar-7th/StarRailRes` — 4.5.0（commit `d226bef`），命途/属性/遗器词条/模拟宇宙等按实体 ID 交叉核对
- 历史译名比对：`VizualAbstract/StarRailStaticAPI`（2.3.0）、`nathacks/HSR-Mapping-DATA`（4.0）
- 剧情与对话辅助核对：`mrzjy/StarrailDialog`、`M1k0t0/StarRail_Dialogue_Browser`
- 其它参考（未直接生成条目）：`iuyangyuc/homdgcat`、`kel-z/HSR-Data`、`simon300000/starrail-voice`

官方站点（<https://sr.mihoyo.com/>、<https://hsr.hoyoverse.com/>）用于核对语言支持范围与官方写法。

优先级：**当前客户端本地化 > 官方网站/公告 > 原始 TextMap > StarRailRes / HSR-Mapping-DATA >
结构化数据库 > Wiki > 其它社区资料**。

## TextMap 处理方式

1. 从 `ExcelOutput` 读取实体（角色、技能、行迹、星魂、光锥、遗器、道具、敌人、地点、任务、关卡、成就……）；
   名称字段是 `{"Hash": …}` 或字符串键（如 `SkillPointName_1001101`），后者按 **xxHash64** 计算 Hash。
2. 用同一 Hash 到 13 份 TextMap 中取值，形成「同一键 × 13 语言」的对齐表。
3. 过滤 `{NICKNAME}`、`{RUBY_B#…}`、`#1[i]` 等开发变量、HTML 标签、`N/A`、纯数字、占位符。
4. 同一语言内按 `(source,target,tgt_lng)` 去重，并保留同一 source 的多种译法（多译名）而不是强行合并。
5. 目标语言缺失文本时**不生成记录**，绝不用其它语言或机器翻译补全。

## 质量检查（两轮）

第一轮（结构，`tools/validate_hsr_glossary.py`，覆盖全部 338 个 CSV、4,085,059 行）：

| 检查项 | 结果 |
| --- | ---: |
| 空 source / 空 target | 0 / 0 |
| 语言代码错误 | 0 |
| 重复记录 | 0 |
| HTML 标签 | 0 |
| 开发变量 | 0 |
| Hash / 内部 ID | 0 / 0 |
| N/A 等占位符 | 0 |
| 目标文本未出现在客户端文本中 | 0 |
| 机器翻译记录 | 0 |

第二轮（抽样核对，`tools/spotcheck_hsr_glossary.py`）：对角色、命途、属性、技能、行迹、星魂、光锥、
遗器、敌人、地点、阵营、任务、活动、模拟宇宙、忘却之庭、世界观、系统、UI、剧情等分类逐类抽样，
并用 StarRailRes 独立索引交叉比对（命中情况见 [`Metadata/statistics.md`](Metadata/statistics.md)）。

## 统计

完整统计（总术语数量、各语言数量、各分类数量、已确认/未确认数量、历史词条数量、多译名词条数量）见
[`Metadata/statistics.md`](Metadata/statistics.md)。

- 历史词条：166（`hsr-glossary/historical/`）
- 人工核对条目：117（`hsr-glossary/curated/`）
- 多译名冲突组：41,475（全部保留，不自动择优）

## 重新生成

```bash
python tools/build_hsr_glossary.py     # 生成 13 语言 × 26 分类 CSV
python tools/build_hsr_history.py      # 生成历史译名变化
python tools/build_hsr_curated.py      # 生成人工核对条目
python tools/validate_hsr_glossary.py  # 第一轮 + 第二轮校验
python tools/make_hsr_docs.py          # 生成本说明与统计文档
python tools/spotcheck_hsr_glossary.py # 人工抽样核对
```

脚本默认读取 `E:\Download\BT\Codex_input` 下的上游仓库（不随本仓库分发）。

## 使用建议

- 沉浸式翻译 / 术语表工具：直接导入目标语言目录下的 CSV（`source,target,tgt_lng`）。
- 只需要专有名词时，可按分类挑选，例如 `01_character.csv`、`02_path.csv`、`07_light_cone.csv`。
- 需要完整剧情/对话文本时，请使用上游 `TurnBasedGameData` 原始数据，本仓库不复制原始游戏数据。

## 限制与免责声明

- 上游为社区提取的客户端数据，**不等同于发行商官方发布的术语表**；本项目与米哈游/HoYoverse 无任何隶属关系。
- 游戏文本随版本更新可能变化；本库以 4.5.0 客户端为准，旧版本差异单独保存在 `historical/`。
- `pt-PT` 使用游戏客户端「Português」文本，语言标签按本项目统一规范书写。
- 繁体中文上游标识为 `CHT`，本库统一写作 `zh-TW`；葡萄牙语上游标识为 `PT`，本库统一写作 `pt-PT`。
- 缺少某语言文本时不会生成记录，也不会用机器翻译补全；无法确认的内容一律不写入。
- 游戏名称、角色名、专有名词及相关资产权利归原权利人所有，本项目为个人学习与研究用途。
