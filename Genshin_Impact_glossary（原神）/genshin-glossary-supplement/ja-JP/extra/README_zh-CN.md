# 原神术语库（补充词库）—— 额外类目（`ja-JP/extra`）

## [日本語](README.md) [English](README_EN.md)

本目录是以日文为目标语言的**额外类目**词库：收录主词库与补充词库主类目之外的 10 个类目，均为「其他语言词条 → 日文」的对照，`tgt_lng` 列固定为 `ja-JP`。本目录共 **10 个 CSV 文件、5,690 行对照**。

## 目录结构

```text
ja-JP/extra/
├── archives（書庫）.csv          382 行
├── dialogue（会話）.csv          121 行
├── events（イベント）.csv        1796 行
├── facilities（施設）.csv        236 行
├── objects（オブジェクト）.csv   472 行
├── organizations（組織）.csv     209 行
├── quests（任務）.csv           1753 行
├── sereniteapot（塵歌壺）.csv      32 行
├── story（ストーリー）.csv        302 行
└── system（システム）.csv         387 行
```

## 文件格式

所有文件均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，固定三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師の矢羽 | ja-JP |
| Berserker's Battle Mask | 狂戦士の仮面 | ja-JP |

## 类目与条数

| 分类 | 文件 | 说明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `quests（任務）.csv` | 任务名称（魔神/世界/传说/每日/部族等） | 1,753 |
| events（活动） | `events（イベント）.csv` | 活动名称 | 1,796 |
| objects（物件） | `objects（オブジェクト）.csv` | 场景物件 | 472 |
| system（系统） | `system（システム）.csv` | 系统与玩法术语 | 387 |
| archives（档案） | `archives（書庫）.csv` | 档案资料 | 382 |
| story（剧情） | `story（ストーリー）.csv` | 剧情与章节 | 302 |
| facilities（设施） | `facilities（施設）.csv` | 设施与建筑 | 236 |
| organizations（组织） | `organizations（組織）.csv` | 组织与势力 | 209 |
| dialogue（对话） | `dialogue（会話）.csv` | 对白用语 | 121 |
| sereniteapot（尘歌壶） | `sereniteapot（塵歌壺）.csv` | 尘歌壶 | 32 |
| **合计** | 10 个文件 | — | **5,690** |

## 说明

- 每行的 `source` 是同一词条在**其余 3 种语言（`zh-CN`、`zh-TW`、`en-US`）中的某一种**的写法，`target` 是日文译名。
- 数据来自 [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)，为社区整理的**游戏官方本地化文本**，不是二次翻译或机器生成。
- 本目录可与 `../` 下的 9 个主类目 CSV 与别名文件叠加使用；完整语言级说明请见 `../README.md`。
- 游戏级总说明见 `../../README.md` / `../../README_EN.md` / `../../README_JP.md`。
