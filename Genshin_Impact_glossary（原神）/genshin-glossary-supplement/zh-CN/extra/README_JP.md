# 原神 用語集（補完辞書）—— 追加カテゴリ（`zh-CN/extra`）

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、簡体字中国語を対象言語とする補完辞書の**追加カテゴリ**です。本体辞書と補完辞書の主カテゴリ以外にあたる 10 カテゴリを収録し、いずれも「他言語の語 → 簡体字中国語」の対照で、`tgt_lng` 列は常に `zh-CN` です。本ディレクトリは **CSV 10 ファイル、対照 5,423 行**です。

## ディレクトリ構造

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

## ファイル形式

すべてのファイルは **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、3 列固定です：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴师的箭羽 | zh-CN |
| Berserker's Battle Mask | 战狂的鬼面 | zh-CN |

## カテゴリと件数

| カテゴリ | ファイル | 説明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `quests（任务）.csv` | 任務名（魔神 / 世界 / 伝説 / デイリー / 部族 など） | 1,664 |
| events（活动） | `events（活动）.csv` | イベント名 | 1,715 |
| objects（物件） | `objects（物件）.csv` | フィールドオブジェクト | 459 |
| system（系统） | `system（系统）.csv` | システムとプレイ用語 | 357 |
| archives（档案） | `archives（档案）.csv` | アーカイブ資料 | 345 |
| story（剧情） | `story（剧情）.csv` | ストーリーとチャプター | 286 |
| facilities（设施） | `facilities（设施）.csv` | 施設と建築物 | 234 |
| organizations（组织） | `organizations（组织）.csv` | 組織と勢力 | 213 |
| dialogue（对话） | `dialogue（对话）.csv` | 会話表現 | 117 |
| sereniteapot（尘歌壶） | `sereniteapot（尘歌壶）.csv` | 塵歌壺 | 33 |
| **合計** | 10 ファイル | — | **5,423** |

## 説明

- 各行の `source` は同じ語の**残り 3 言語（`zh-TW`、`en-US`、`ja-JP`）のいずれか**での表記、`target` は簡体字中国語の訳語です。
- データは [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) に由来し、コミュニティが整理した**ゲーム公式のローカライズテキスト**です。再翻訳や機械生成ではありません。
- 本ディレクトリは `../` にある 9 つの主カテゴリ CSV と別名ファイルに重ねて使用できます。言語レベルの詳細は `../README.md` を参照してください。
- ゲーム全体の説明は `../../README.md` / `../../README_EN.md` / `../../README_JP.md` を参照してください。
