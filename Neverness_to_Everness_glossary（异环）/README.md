# 《异环》Neverness to Everness 翻译术语库

## [English](README_EN.md) [日本語](README_JP.md)

本库收录开放世界动作游戏《异环》（Neverness to Everness / NTE）的专有名词对照表，覆盖角色名称、武器、技能、战斗机制、任务、地区、阵营、道具、车辆、家具、UI 文本、剧情专有名词等共 **21 个类目**。按目标语言拆分为 **9** 套独立术语库。

> **当前状态**：本库处于初始搞建阶段，已确认的官方术语较少。需要从游戏客户端提取 `.locres` / TextMap 数据后方可大规模填充。详见 [`tools/SOURCES.md`](tools/SOURCES.md)。

## 使用方法

1. **单文件下载**：进入 `nte-glossary/` 下对应语言目录（例如 `zh-CN/`），按需要下载 `characters.csv`、`items.csv` 等类目文件。
2. **重新生成**：提取游戏 `.locres` 数据后，运行 `python tools/build_nte_glossary.py` 即可全量更新。

## 语言覆盖

| 语言代码 | 名称 | 类目数 | 已确认词条数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 21 | 6 |
| `zh-TW` | 繁體中文（待确认） | 21 | 0 |
| `en-US` | English | 21 | 5 |
| `ja-JP` | 日本語（待确认） | 21 | 0 |
| `ko-KR` | 한국어（待确认） | 21 | 0 |
| `de-DE` | Deutsch（待确认） | 21 | 0 |
| `fr-FR` | Français（待确认） | 21 | 0 |
| `es-ES` | Español（待确认） | 21 | 0 |
| `ru-RU` | Русский（待确认） | 21 | 0 |
| **合计** | | **189** | **11** |

## 类目说明

| 类目 | 文件名 | zh-CN 词条数 |
| --- | --- | --- |
| 角色名称 | `characters.csv` | 1 |
| 角色技能 | `skills.csv` | 0 |
| 武器与装备 | `weapons.csv` | 0 |
| 战斗机制 | `combat.csv` | 0 |
| 特殊生物/系统 | `specials.csv` | 0 |
| 任务 | `quests.csv` | 0 |
| 关卡与副本 | `dungeons.csv` | 0 |
| 地区与地点 | `regions.csv` | 1 |
| 阵营与组织 | `factions.csv` | 0 |
| 敌人与Boss | `enemies.csv` | 0 |
| 道具与材料 | `items.csv` | 0 |
| 车辆与载具 | `vehicles.csv` | 0 |
| 房屋与家具 | `furniture.csv` | 0 |
| 成就 | `achievements.csv` | 0 |
| 剧情专有名词 | `terms.csv` | 2 |
| UI文本 | `ui.csv` | 0 |
| 系统文本 | `system.csv` | 0 |
| 剧情文本 | `story.csv` | 0 |
| 增益与效果 | `buffs.csv` | 0 |
| NPC与说话人 | `npcs.csv` | 0 |
| 其他 | `other.csv` | 2 |

## 数据状态说明

- 全部词条均取自官方游戏客户端或官方公告，不包含机器翻译结果
- 标记为“待确认”的语言表示该语言支持情况尚未通过官方渠道独立验证
- 相同 source 存在多个 target 时保留全部记录并标注来源差异

## 免责声明

本目录为个人整理与维护的**非官方**翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件的术语匹配。本库与《异环》的开发商、发行商、代理商、运营商、版权方不存在任何从属、授权、合作或代理关系。

---

**Game-translation-terminology-database 是一个独立的个人项目，与《异环》及其开发商、发行商、代理商、版权方不存在任何隐属、授权、合作或代理关系。**
