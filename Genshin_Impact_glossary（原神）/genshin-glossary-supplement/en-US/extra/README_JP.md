# 原神 用語集（補完辞書）—— 追加カテゴリ（`en-US/extra`）

## [English](README.md) [简体中文](README_zh-CN.md)

本ディレクトリは、英語を対象言語とする補完辞書の**追加カテゴリ**です。本体辞書と補完辞書の主カテゴリ以外にあたる 10 カテゴリを収録し、いずれも「他言語の語 → 英語」の対照で、`tgt_lng` 列は常に `en-US` です。本ディレクトリは **CSV 10 ファイル、対照 5,973 行**です。

## ディレクトリ構造

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

## ファイル形式

すべてのファイルは **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、3 列固定です：

| source | target | tgt_lng |
| --- | --- | --- |
| フィナーレの時計 | Concert's Final Hour | en-US |
| 不動 | Unyielding | en-US |

## カテゴリと件数

| カテゴリ | ファイル | 説明 | 行数 |
| --- | --- | --- | ---: |
| quests（任务） | `quests.csv` | 任務名（魔神 / 世界 / 伝説 / デイリー / 部族 など） | 1,769 |
| events（活动） | `events.csv` | イベント名 | 1,842 |
| objects（物件） | `objects.csv` | フィールドオブジェクト | 508 |
| system（系统） | `system.csv` | システムとプレイ用語 | 447 |
| archives（档案） | `archives.csv` | アーカイブ資料 | 386 |
| story（剧情） | `story.csv` | ストーリーとチャプター | 348 |
| facilities（设施） | `facilities.csv` | 施設と建築物 | 270 |
| organizations（组织） | `organizations.csv` | 組織と勢力 | 243 |
| dialogue（对话） | `dialogue.csv` | 会話表現 | 123 |
| sereniteapot（尘歌壶） | `sereniteapot.csv` | 塵歌壺 | 37 |
| **合計** | 10 ファイル | — | **5,973** |

## 説明

- 各行の `source` は同じ語の**残り 3 言語（`zh-CN`、`zh-TW`、`ja-JP`）のいずれか**での表記、`target` は英語名です。
- データは [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) に由来し、コミュニティが整理した**ゲーム公式のローカライズテキスト**です。再翻訳や機械生成ではありません。
- 本ディレクトリは `../` にある 9 つの主カテゴリ CSV と別名ファイルに重ねて使用できます。言語レベルの詳細は `../README.md` を参照してください。
- ゲーム全体の説明は `../../README.md` / `../../README_EN.md` / `../../README_JP.md` を参照してください。
