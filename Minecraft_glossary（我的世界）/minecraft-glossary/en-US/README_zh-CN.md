# 《我的世界》术语库 — 英文（`en-US`）

[← 返回游戏总说明](../../README.md) · [English](README.md)

本目录是**以 `en-US`（英文）为目标语言**的术语库：`target` 列去重后共 **7,854** 条英文词条、**101,550** 行对照，分布在 **34** 个分类 CSV 文件中。`tgt_lng` 列固定为 `en-US`；每行的 `source` 是同一词条在**其余 13 种语言中的某一种**的写法，`target` 是该词条的英文译文。文件按**类目**分列，一个类目一个 CSV；系统与文本类目统一放在 `extra/` 子文件夹内。

## 文件

- `blocks.csv`、`items.csv`、`entities.csv`、`biomes.csv`、`enchantments.csv`、`effects.csv`、`instruments.csv`、`materials.csv`、`paintings.csv`、`attributes.csv`、`item-groups.csv`、`jukebox-songs.csv`、`trim-patterns.csv`、`colors.csv`、`statistics.csv`、`maps.csv`、`music.csv`、`sound-categories.csv`、`game-modes.csv` —— 19 个主类目文件
- `extra/subtitles.csv`、`extra/death-messages.csv`、`extra/advancement-titles.csv`、`extra/advancement-descriptions.csv`、`extra/gamerules.csv`、`extra/commands.csv`、`extra/gui.csv`、`extra/options.csv`、`extra/multiplayer.csv`、`extra/realms.csv`、`extra/world-management.csv`、`extra/resource-packs.csv`、`extra/telemetry.csv`、`extra/dev-tools.csv`、`extra/misc.csv` —— 15 个 `extra/` 系统与文本类目文件

合计 **34 个 CSV 文件**，格式统一为三列：

| source | target | tgt_lng |
| --- | --- | --- |
| 2匹ずつ | Two by Two | en-US |
| A cidade no fim do jogo | The City at the End of the Game | en-US |

目录结构：

```text
en-US/
├── blocks.csv
├── items.csv
├── entities.csv
├── biomes.csv
├── enchantments.csv
├── effects.csv
├── instruments.csv
├── materials.csv
├── paintings.csv
├── attributes.csv
├── item-groups.csv
├── jukebox-songs.csv
├── trim-patterns.csv
├── colors.csv
├── statistics.csv
├── maps.csv
├── music.csv
├── sound-categories.csv
├── game-modes.csv
└── extra/  # 系统与文本类目
    ├── subtitles.csv
    ├── death-messages.csv
    ├── advancement-titles.csv
    ├── advancement-descriptions.csv
    ├── gamerules.csv
    ├── commands.csv
    ├── gui.csv
    ├── options.csv
    ├── multiplayer.csv
    ├── realms.csv
    ├── world-management.csv
    ├── resource-packs.csv
    ├── telemetry.csv
    ├── dev-tools.csv
    └── misc.csv
```

## 分类与条数

「词条数」为该类目在官方语言文件中对应的**游戏名称对象数**（即语言文件里的名称键数量，含在该语言中未翻译的条目），同一类目在各语言目录中完全相同，数据取自 `tools/glossary_counts.json`，34 个分类合计 8,559；「对照行」为**本目录**该文件的实际数据行数。两者口径不同，请勿混用。

### 主类目（游戏内容）

| 分类 | 主题 | 词条数 | 对照行 |
| --- | --- | ---: | ---: |
| `blocks.csv` | 方块 | 1,975 | 25,426 |
| `items.csv` | 物品 | 803 | 9,304 |
| `entities.csv` | 实体 | 219 | 2,582 |
| `biomes.csv` | 生物群系 | 67 | 835 |
| `enchantments.csv` | 魔咒 | 54 | 553 |
| `effects.csv` | 状态效果 | 42 | 514 |
| `instruments.csv` | 乐器 | 8 | 98 |
| `materials.csv` | 盔甲纹饰材料 | 11 | 143 |
| `paintings.csv` | 画 | 104 | 315 |
| `attributes.csv` | 属性 | 83 | 555 |
| `item-groups.csv` | 物品栏分类 | 16 | 198 |
| `jukebox-songs.csv` | 唱片曲目 | 22 | 42 |
| `trim-patterns.csv` | 盔甲纹饰图案 | 18 | 234 |
| `colors.csv` | 颜色 | 16 | 184 |
| `statistics.csv` | 统计 | 88 | 1,143 |
| `maps.csv` | 地图 | 33 | 422 |
| `music.csv` | 音乐曲目 | 70 | 192 |
| `sound-categories.csv` | 声音分类 | 11 | 133 |
| `game-modes.csv` | 游戏模式 | 6 | 77 |
| **小计** | 19 个文件 | **3,646** | **42,950** |

### `extra/` 类目（系统与文本）

| 分类 | 主题 | 词条数 | 对照行 |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | 字幕 | 1,023 | 12,415 |
| `extra/death-messages.csv` | 死亡消息 | 106 | 1,354 |
| `extra/advancement-titles.csv` | 进度标题 | 127 | 1,603 |
| `extra/advancement-descriptions.csv` | 进度描述 | 127 | 1,641 |
| `extra/gamerules.csv` | 游戏规则 | 117 | 1,490 |
| `extra/commands.csv` | 命令与参数 | 856 | 10,733 |
| `extra/gui.csv` | 界面文本 | 581 | 6,607 |
| `extra/options.csv` | 设置与按键 | 754 | 8,169 |
| `extra/multiplayer.csv` | 多人游戏 | 173 | 2,015 |
| `extra/realms.csv` | Realms | 426 | 5,016 |
| `extra/world-management.csv` | 世界管理 | 294 | 3,572 |
| `extra/resource-packs.csv` | 资源包与数据包 | 62 | 761 |
| `extra/telemetry.csv` | 遥测 | 70 | 897 |
| `extra/dev-tools.csv` | 开发与测试工具 | 144 | 1,811 |
| `extra/misc.csv` | 其他 | 53 | 516 |
| **小计** | 15 个文件 | **4,913** | **58,600** |

**本目录合计：34 个文件，`target` 列去重后 7,854 条词条、101,550 行对照。**

## 说明

- **译文来源与对齐方式**：全部文本取自 **Minecraft Java 版官方语言文件**（镜像自 [misode/mcmeta](https://github.com/misode/mcmeta) 的 `assets` 分支，路径 `assets/minecraft/lang/<locale>.json`，本语言为 `en_us.json`），属于**官方本地化**，不是二次翻译或机器生成。对齐以语言文件的键为单位：同一条目会以其余每一种语言作为 `source` 各出一行，因此行数远大于词条数。
- **语言标签**：本目录 `tgt_lng` 固定为 `en-US`（目标语言）；`source` 可能是其余 13 种语言（`zh-CN`, `zh-TW`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`）中的任意一种。
- **编码**：全部 CSV 为 **UTF-8 with BOM** 编码、**CRLF** 换行，首行为表头，含逗号或引号的字段按 RFC 4180 转义；Excel 可直接双击打开，无需调整编码。本 README 本身为 UTF-8（无 BOM）。
- **已知限制**：各类目行数在不同语言间略有差异，原因是某语言缺少该词条的译文、或译文与目标语言写法完全相同时整行不会生成；「对照行数」不等于「词条数」——34 个分类的 `entries` 合计为 8,559，指官方语言文件中归入各分类的词条对象数（含在该语言中未翻译的条目）；本目录 `target` 列去重后为 7,854 条，两者口径不同。完整定义见游戏根目录 `../../README.md` 的「数据概览」。同一条目名可能出现在多个类目（例如某方块名与物品名相同），各文件行数相加即本目录总行数。译名一律遵循官方本地化，官方未翻译的名称保留原文形态。
- **补充词库**：同级目录 `../../minecraft-glossary-supplement/` 收录 Minecraft Wiki 标准译名（仅简体中文 / 繁体中文），可与本库叠加使用。
- **复现**：在游戏根目录运行 `python tools/build_glossary.py` 可由官方语言文件重建本词库（脚本读取含 `mcmeta_lang/<locale>.json` 的外部素材目录，输出到 `minecraft-glossary/`）；`python tools/verify_output.py` 会把每一类目的行数与 `tools/glossary_counts.json` 逐条核对；`python tools/make_readme.py` 重新生成各库的 README。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与 Minecraft 及其开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。

游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有，本库不主张对上述第三方知识产权的任何权利。使用本库及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。

完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
