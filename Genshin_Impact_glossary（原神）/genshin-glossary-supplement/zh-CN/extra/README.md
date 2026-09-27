# 原神术语库（补充词库）—— 额外类目（`zh-CN/extra`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录是以简体中文为目标语言的**额外类目**词库：收录主词库与补充词库主类目之外的 10 个类目，均为「其他语言词条 → 简体中文」的对照，`tgt_lng` 列固定为 `zh-CN`。本目录共 **10 个 CSV 文件、5,423 行对照**。

## 目录结构

```text
zh-CN/extra/
├── archives（档案）.csv          345 行
├── dialogue（对话）.csv          117 行
├── events（活动）.csv          1715 行
├── facilities（设施）.csv        234 行
├── objects（物件）.csv           459 行
├── organizations（组织）.csv     213 行
├── quests（任务）.csv          1664 行
├── sereniteapot（尘歌壶）.csv      33 行
├── story（剧情）.csv             286 行
└── system（系统）.csv            357 行
```

## 文件格式

所有文件均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，固定三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴师的箭羽 | zh-CN |
| Berserker's Battle Mask | 战狂的鬼面 | zh-CN |

## 类目与条数

| 分类 | 文件 | 说明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `quests（任务）.csv` | 任务名称（魔神/世界/传说/每日/部族等） | 1,664 |
| events（活动） | `events（活动）.csv` | 活动名称 | 1,715 |
| objects（物件） | `objects（物件）.csv` | 场景物件 | 459 |
| system（系统） | `system（系统）.csv` | 系统与玩法术语 | 357 |
| archives（档案） | `archives（档案）.csv` | 档案资料 | 345 |
| story（剧情） | `story（剧情）.csv` | 剧情与章节 | 286 |
| facilities（设施） | `facilities（设施）.csv` | 设施与建筑 | 234 |
| organizations（组织） | `organizations（组织）.csv` | 组织与势力 | 213 |
| dialogue（对话） | `dialogue（对话）.csv` | 对白用语 | 117 |
| sereniteapot（尘歌壶） | `sereniteapot（尘歌壶）.csv` | 尘歌壶 | 33 |
| **合计** | 10 个文件 | — | **5,423** |

## 说明

- 每行的 `source` 是同一词条在**其余 3 种语言（`zh-TW`、`en-US`、`ja-JP`）中的某一种**的写法，`target` 是简体中文译名。
- 数据来自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，为社区整理的**游戏官方本地化文本**，不是二次翻译或机器生成。
- 本目录可与 `../` 下的 9 个主类目 CSV 及别名文件叠加使用；如只需完整语言级说明，请见 `../README.md`。
- 游戏级总说明见 `../../README.md` / `../../README_EN.md` / `../../README_JP.md`。
