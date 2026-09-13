# 鸣潮（Wuthering Waves）术语库 — 韩文（`ko-KR`）

[← 返回游戏总说明](../../README.md) ｜ [← wuwa-glossary 子库说明](../README.md)

本目录是**以 `ko-KR`（韩文）为目标语言**的鸣潮（Wuthering Waves）术语库。共 **123,230** 条词条、**646,888** 行对照（本目录 23 个 CSV 的数据行数合计），目录体积约 **63.4 MiB**。所有 CSV 的 `tgt_lng` 列固定为 `ko-KR`；`source` 列收录其余 9 种语言（`zh-CN`（简体中文）、`zh-TW`（繁體中文）、`en-US`（English）、`ja-JP`（日本語）、`fr-FR`（Français）、`de-DE`（Deutsch）、`es-ES`（Español）、`pt-BR`（Português）、`th-TH`（ภาษาไทย））的写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，23 个类目 CSV 直接放在本目录下，没有额外的子目录：

- `characters.csv` — 角色名称
- `weapons.csv` — 武器名称
- `echoes.csv` — 声骸
- `skills.csv` — 技能
- `resonant-chains.csv` — 共鸣链
- `quests.csv` — 任务
- `dungeons.csv` — 关卡与挑战
- `regions.csv` — 地区与地图
- `factions.csv` — 阵营与势力
- `items.csv` — 道具与材料
- `monsters.csv` — 怪物与生物
- `npcs.csv` — NPC 与说话人
- `achievements.csv` — 成就
- `activities.csv` — 活动与玩法
- `buffs.csv` — 增益与效果
- `voice-lines.csv` — 角色语音
- `archives.csv` — 档案与读物
- `terms.csv` — 术语与百科
- `system.csv` — 系统文本
- `ui.csv` — UI 文本
- `tutorials.csv` — 教程与引导
- `story.csv` — 剧情文本
- `other.csv` — 其他

每个文件都是 `source,target,tgt_lng` 三列（首行为表头）：对 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它某一语言**的原文。因此同一条目会以其余 9 种语言分别作为 `source` 各出现一行（重复行与同形行已合并，故实际行数并非词条数的 9 倍）。文件可直接导入 CAT 工具或沉浸式翻译等术语匹配软件。

## 分类与条数

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | --- | --- |
| `characters.csv` | 角色名称 | 1,230 | 5,209 |
| `weapons.csv` | 武器名称 | 820 | 3,112 |
| `echoes.csv` | 声骸 | 1,000 | 6,083 |
| `skills.csv` | 技能 | 5,344 | 30,562 |
| `resonant-chains.csv` | 共鸣链 | 784 | 6,124 |
| `quests.csv` | 任务 | 2,807 | 14,620 |
| `dungeons.csv` | 关卡与挑战 | 1,910 | 12,155 |
| `regions.csv` | 地区与地图 | 2,229 | 16,199 |
| `factions.csv` | 阵营与势力 | 8 | 44 |
| `items.csv` | 道具与材料 | 8,384 | 54,484 |
| `monsters.csv` | 怪物与生物 | 685 | 4,529 |
| `npcs.csv` | NPC 与说话人 | 14,172 | 63,418 |
| `achievements.csv` | 成就 | 2,563 | 22,169 |
| `activities.csv` | 活动与玩法 | 9,531 | 63,608 |
| `buffs.csv` | 增益与效果 | 270 | 2,034 |
| `voice-lines.csv` | 角色语音 | 7,374 | 31,923 |
| `archives.csv` | 档案与读物 | 839 | 6,563 |
| `terms.csv` | 术语与百科 | 1,672 | 12,423 |
| `system.csv` | 系统文本 | 9,756 | 65,835 |
| `ui.csv` | UI 文本 | 13,866 | 78,159 |
| `tutorials.csv` | 教程与引导 | 6,253 | 31,905 |
| `story.csv` | 剧情文本 | 29,841 | 102,395 |
| `other.csv` | 其他 | 1,892 | 13,335 |
| **合计** | **23 个类目** | **123,230** | **646,888** |

「条数」为去重后的词条数（一个词条 = 游戏中的一条文本键），取自 `tools/_counts.json` 的 `concepts` 字段，**全库共用同一套、与目标语言无关**；「对照行」为本目录该类目 CSV 的实际数据行数。同一文本可能同时属于多个类目，各类目行数相加会大于去重词条数，属正常现象。

## 说明

- **译文来源**：`target` 列直接取自游戏自身的本地化文本（[Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) 的 `Textmaps/<lang>/multi_text/MultiText.json`，游戏 3.6.0；少量键由 [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) 的 `TextMap/<lang>/MultiText.json`，游戏 3.1.0 补齐），是游戏内官方译名，不是二次翻译。
- **对齐方式**：以游戏文本键（如 `RoleInfo_1402_Name`）对齐——同一文本键在其它语言的写法，即成为本目录该 `target` 的 `source` 行。
- **语言标签**：`tgt_lng` 固定为本目录的语言代码，与目录名一致。
- **编码**：全部 CSV 为 **UTF-8（含 BOM）**、**CRLF** 换行、首行为表头；字段含逗号或引号时按 RFC 4180 转义，Excel 可直接打开。
- **已知限制**：默认不收录逐句剧情对白（约 17 万条/语言），需要时可用 `--with-dialogue` 选项额外生成，方法见 `../README.md`；超长文本按 `tools/wuwa_config.py` 的 `MAX_LEN` 按类目截断；上游数据仓库中 `ru-RU`、`id-ID`、`vi-VN` 为空占位文件故未收录，`it-IT`、`tr-TR` 并非游戏支持的文本语言。

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与相关游戏的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有，本库不主张对上述第三方知识产权的任何权利；如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
