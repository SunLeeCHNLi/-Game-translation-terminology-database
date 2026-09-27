# 原神 用語集（補完辞書）—— 追加カテゴリ（`zh-TW/extra`）

## [繁體中文](README.md) [English](README_EN.md)

本ディレクトリは、繁体字中国語を対象言語とする補完辞書の**追加カテゴリ**です。本体辞書と補完辞書の主カテゴリ以外にあたる 10 カテゴリを収録し、いずれも「他言語の語 → 繁体字中国語」の対照で、`tgt_lng` 列は常に `zh-TW` です。本ディレクトリは **CSV 10 ファイル、対照 5,354 行**です。

## ディレクトリ構造

```text
zh-TW/extra/
├── archives（檔案）.csv          347 行
├── dialogue（對話）.csv          115 行
├── events（活動）.csv           1705 行
├── facilities（設施）.csv        226 行
├── objects（物件）.csv           447 行
├── organizations（組織）.csv     205 行
├── quests（任務）.csv           1652 行
├── sereniteapot（塵歌壺）.csv      32 行
├── story（劇情）.csv             282 行
└── system（系統）.csv            343 行
```

## ファイル形式

すべてのファイルは **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行がヘッダーで、3 列固定です：

| source | target | tgt_lng |
| --- | --- | --- |
| Bard's Arrow Feather | 琴師的箭羽 | zh-TW |
| Berserker's Battle Mask | 戰狂的鬼面 | zh-TW |

## カテゴリと件数

| カテゴリ | ファイル | 説明 | 行数 |
| --- | --- | --- | ---: |
| quests（任務） | `quests（任務）.csv` | 任務名（魔神 / 世界 / 伝説 / デイリー / 部族 など） | 1,652 |
| events（活動） | `events（活動）.csv` | イベント名 | 1,705 |
| objects（物件） | `objects（物件）.csv` | フィールドオブジェクト | 447 |
| system（系統） | `system（系統）.csv` | システムとプレイ用語 | 343 |
| archives（檔案） | `archives（檔案）.csv` | アーカイブ資料 | 347 |
| story（劇情） | `story（劇情）.csv` | ストーリーとチャプター | 282 |
| facilities（設施） | `facilities（設施）.csv` | 施設と建築物 | 226 |
| organizations（組織） | `organizations（組織）.csv` | 組織と勢力 | 205 |
| dialogue（對話） | `dialogue（對話）.csv` | 会話表現 | 115 |
| sereniteapot（塵歌壺） | `sereniteapot（塵歌壺）.csv` | 塵歌壺 | 32 |
| **合計** | 10 ファイル | — | **5,354** |

## 説明

- 各行の `source` は同じ語の**残り 3 言語（`zh-CN`、`en-US`、`ja-JP`）のいずれか**での表記、`target` は繁体字中国語の訳語です。
- データは [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) に由来し、コミュニティが整理した**ゲーム公式のローカライズテキスト**です。再翻訳や機械生成ではありません。
- 本ディレクトリは `../` にある 9 つの主カテゴリ CSV と別名ファイルに重ねて使用できます。言語レベルの詳細は `../README.md` を参照してください。
- ゲーム全体の説明は `../../README.md` / `../../README_EN.md` / `../../README_JP.md` を参照してください。
