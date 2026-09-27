# 原神术语库（补充词库）—— 额外类目（`en-US/extra`）

## [English](README.md) [日本語](README_JP.md)

本目录是以英文为目标语言的**额外类目**词库：收录主词库与补充词库主类目之外的 10 个类目，均为「其他语言词条 → 英文」的对照，`tgt_lng` 列固定为 `en-US`。本目录共 **10 个 CSV 文件、5,973 行对照**。

## 目录结构

```text
en-US/extra/
├── archives.csv          386 行
├── dialogue.csv          123 行
├── events.csv           1842 行
├── facilities.csv        270 行
├── objects.csv           508 行
├── organizations.csv     243 行
├── quests.csv           1769 行
├── sereniteapot.csv       37 行
├── story.csv             348 行
└── system.csv            447 行
```

## 文件格式

所有文件均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，固定三列：

| source | target | tgt_lng |
| --- | --- | --- |
| フィナーレの時計 | Concert's Final Hour | en-US |
| 不動 | Unyielding | en-US |

## 类目与条数

| 分类 | 文件 | 说明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `quests.csv` | 任务名称（魔神/世界/传说/每日/部族等） | 1,769 |
| events（活动） | `events.csv` | 活动名称 | 1,842 |
| objects（物件） | `objects.csv` | 场景物件 | 508 |
| system（系统） | `system.csv` | 系统与玩法术语 | 447 |
| archives（档案） | `archives.csv` | 档案资料 | 386 |
| story（剧情） | `story.csv` | 剧情与章节 | 348 |
| facilities（设施） | `facilities.csv` | 设施与建筑 | 270 |
| organizations（组织） | `organizations.csv` | 组织与势力 | 243 |
| dialogue（对话） | `dialogue.csv` | 对白用语 | 123 |
| sereniteapot（尘歌壶） | `sereniteapot.csv` | 尘歌壶 | 37 |
| **合计** | 10 个文件 | — | **5,973** |

## 说明

- 每行的 `source` 是同一词条在**其余 3 种语言（`zh-CN`、`zh-TW`、`ja-JP`）中的某一种**的写法，`target` 是英文译名。
- 数据来自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，为社区整理的**游戏官方本地化文本**，不是二次翻译或机器生成。
- 本目录可与 `../` 下的 9 个主类目 CSV 与别名文件叠加使用；完整语言级说明请见 `../README.md`。
- 游戏级总说明见 `../../README.md` / `../../README_EN.md` / `../../README_JP.md`。
