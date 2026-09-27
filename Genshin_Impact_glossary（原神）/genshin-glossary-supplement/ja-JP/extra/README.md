# 原神 用語集（補完辞書）—— 追加カテゴリ（`ja-JP/extra`）

## [简体中文](README_zh-CN.md) [English](README_EN.md)

本ディレクトリは、日本語を対象言語とする補完辞書の**追加カテゴリ**です。本体辞書と補完辞書の主カテゴリ以外にあたる 10 カテゴリを収録し、いずれも「他言語の語 → 日本語」の対照で、`tgt_lng` 列は常に `ja-JP` です。本ディレクトリは **CSV 10 ファイル、対照 5,690 行**です。

## ディレクトリ構造

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

## ファイル形式

すべてのファイルは **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、3 列固定です：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師の矢羽 | ja-JP |
| Berserker's Battle Mask | 狂戦士の仮面 | ja-JP |

## カテゴリと件数

| カテゴリ | ファイル | 説明 | 行数 |
| --- | --- | --- | ---: |
| quests（任務） | `quests（任務）.csv` | 任務名（魔神 / 世界 / 伝説 / デイリー / 部族 など） | 1,753 |
| events（イベント） | `events（イベント）.csv` | イベント名 | 1,796 |
| objects（オブジェクト） | `objects（オブジェクト）.csv` | フィールドオブジェクト | 472 |
| system（システム） | `system（システム）.csv` | システムとプレイ用語 | 387 |
| archives（書庫） | `archives（書庫）.csv` | アーカイブ資料 | 382 |
| story（ストーリー） | `story（ストーリー）.csv` | ストーリーとチャプター | 302 |
| facilities（施設） | `facilities（施設）.csv` | 施設と建築物 | 236 |
| organizations（組織） | `organizations（組織）.csv` | 組織と勢力 | 209 |
| dialogue（会話） | `dialogue（会話）.csv` | 会話表現 | 121 |
| sereniteapot（塵歌壺） | `sereniteapot（塵歌壺）.csv` | 塵歌壺 | 32 |
| **合計** | 10 ファイル | — | **5,690** |

## 説明

- 各行の `source` は同じ語の**残り 3 言語（`zh-CN`、`zh-TW`、`en-US`）のいずれか**での表記、`target` は日本語の訳語です。
- データは [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) に由来し、コミュニティが整理した**ゲーム公式のローカライズテキスト**です。再翻訳や機械生成ではありません。
- 本ディレクトリは `../` にある 9 つの主カテゴリ CSV と別名ファイルに重ねて使用できます。言語レベルの詳細は `../README.md` を参照してください。
- ゲーム全体の説明は `../../README.md` / `../../README_EN.md` / `../../README_JP.md` を参照してください。
