# 我的世界（Minecraft） 术语库 — 泰文（`th-TH`）

[← 返回游戏总说明](../../README.md)

本目录是**以泰文（`th-TH`）为目标语言**的术语库，共 **34 个 CSV 文件**（34 个分类：
19 个在目录根层、15 个在 `extra/` 子目录）、**101,264 行对照**；`tgt_lng` 列固定为 `th-TH`，
`source` 列收录其余 13 种语言的写法。译文取自 **Minecraft Java 版官方语言文件**（locale `th_th`），
属官方本地化文本，非二次翻译。

## 文件

- `<分类>.csv`（19 个）— `source,target,tgt_lng` 三列，可直接导入 CAT / 术语管理工具
- `extra/<分类>.csv`（15 个）— 同为三列，收录系统与文本类分类

## 分类与条数

| 分类 | 主题 | 文件 | 对照行 |
| --- | --- | --- | --- |
| `blocks` | 方块 | `blocks.csv` | 25,426 |
| `items` | 物品 | `items.csv` | 9,061 |
| `entities` | 实体 | `entities.csv` | 2,581 |
| `biomes` | 生物群系 | `biomes.csv` | 835 |
| `enchantments` | 魔咒 | `enchantments.csv` | 553 |
| `effects` | 状态效果 | `effects.csv` | 514 |
| `instruments` | 乐器 | `instruments.csv` | 98 |
| `materials` | 盔甲纹饰材料 | `materials.csv` | 143 |
| `paintings` | 画 | `paintings.csv` | 315 |
| `attributes` | 属性 | `attributes.csv` | 555 |
| `item-groups` | 物品栏分类 | `item-groups.csv` | 198 |
| `jukebox-songs` | 唱片曲目 | `jukebox-songs.csv` | 42 |
| `trim-patterns` | 盔甲纹饰图案 | `trim-patterns.csv` | 234 |
| `colors` | 颜色 | `colors.csv` | 184 |
| `statistics` | 统计 | `statistics.csv` | 1,143 |
| `maps` | 地图 | `maps.csv` | 422 |
| `music` | 音乐曲目 | `music.csv` | 192 |
| `sound-categories` | 声音分类 | `sound-categories.csv` | 133 |
| `game-modes` | 游戏模式 | `game-modes.csv` | 77 |

### `extra/`（系统与文本）

| 分类 | 主题 | 文件 | 对照行 |
| --- | --- | --- | --- |
| `subtitles` | 字幕 | `extra/subtitles.csv` | 12,402 |
| `death-messages` | 死亡消息 | `extra/death-messages.csv` | 1,336 |
| `advancement-titles` | 进度标题 | `extra/advancement-titles.csv` | 1,603 |
| `advancement-descriptions` | 进度描述 | `extra/advancement-descriptions.csv` | 1,641 |
| `gamerules` | 游戏规则 | `extra/gamerules.csv` | 1,490 |
| `commands` | 命令与参数 | `extra/commands.csv` | 10,750 |
| `gui` | 界面文本 | `extra/gui.csv` | 6,649 |
| `options` | 设置与按键 | `extra/options.csv` | 8,162 |
| `multiplayer` | 多人游戏 | `extra/multiplayer.csv` | 2,010 |
| `realms` | Realms | `extra/realms.csv` | 4,964 |
| `world-management` | 世界管理 | `extra/world-management.csv` | 3,574 |
| `resource-packs` | 资源包与数据包 | `extra/resource-packs.csv` | 761 |
| `telemetry` | 遥测 | `extra/telemetry.csv` | 897 |
| `dev-tools` | 开发与测试工具 | `extra/dev-tools.csv` | 1,803 |
| `misc` | 其他 | `extra/misc.csv` | 516 |

### 文件清单

```text
minecraft-glossary/
<lang>/                       # 14 个语言文件夹
|   blocks.csv
|   items.csv
|   entities.csv
|   biomes.csv
|   enchantments.csv
|   effects.csv
|   instruments.csv
|   materials.csv
|   paintings.csv
|   attributes.csv
|   item-groups.csv
|   jukebox-songs.csv
|   trim-patterns.csv
|   colors.csv
|   statistics.csv
|   maps.csv
|   music.csv
|   sound-categories.csv
|   game-modes.csv
|   +-- extra/               # 系统与文本类分类
|       |-- subtitles.csv
|       |-- death-messages.csv
|       |-- advancement-titles.csv
|       |-- advancement-descriptions.csv
|       |-- gamerules.csv
|       |-- commands.csv
|       |-- gui.csv
|       |-- options.csv
|       |-- multiplayer.csv
|       |-- realms.csv
|       |-- world-management.csv
|       |-- resource-packs.csv
|       |-- telemetry.csv
|       |-- dev-tools.csv
|       \-- misc.csv
+-- de-DE/ en-US/ ... vi-VN/
```

## 说明

- **译文来源与对齐方式。** 词条取自 Minecraft Java 版官方语言文件
  （`assets/minecraft/lang/th_th.json`，经 [misode/mcmeta](https://github.com/misode/mcmeta) 获取），
  即官方本地化文本。每个语言文件夹内，`target` 为该目标语言的译文，`source` 为**其余 13 种语言中
  任一语言**的原文；同一条目会以每种源语言各出现一行（完全同形的行与重复行已合并）。

- **语言标签。** `tgt_lng` 固定为 `th-TH`，对应官方 locale `th_th`。

- **编码说明。** 所有 CSV 均为 **UTF-8（含 BOM）**、**CRLF** 换行、首行为表头；含逗号、引号或换行
  的字段按 RFC 4180 加引号转义。带 BOM 与 CRLF 便于 Excel 双击直接打开。注意：部分长文本字段在引号
  内含换行符（每种语言约 2,000 处），统计行数时请使用符合 RFC 4180 的 CSV 解析器，不要直接数物理
  行数。

- **已知限制。** 「对照行数」不等于「词条数」——34 个分类的 `entries` 合计为 8,559，指官方语言
  文件中归入各分类的词条对象数（含在该语言中未翻译的条目）；完整定义见游戏根目录 `../../README.md`
  的「数据概览」。部分行只是界面文本（GUI、多人游戏、Realms 等），并非严格意义上的术语。官方语言
  文件中未翻译的条目不会生成行。14 个语言目录的行数略有差异，因为各语言的翻译覆盖率不同。

- **复现方式。** `python tools/build_glossary.py`（在游戏根目录下执行）；脚本读取外部数据目录，
  前缀到分类的完整映射见脚本中的 `CATEGORIES` 表。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件的
术语匹配。本库与游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或
官方代表关系；库中译名不代表官方立场，不应被视为任何游戏的官方术语表或官方本地化文件。游戏名称、
角色名称、专有名词、商标等知识产权均归各自权利人所有。使用本项目及基于其产生的翻译结果所引发的
一切责任由使用者自行承担。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
