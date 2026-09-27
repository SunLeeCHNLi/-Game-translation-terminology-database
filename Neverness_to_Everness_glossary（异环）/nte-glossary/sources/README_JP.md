# NTE データ出典記録 / NTE 数据来源记录

## [简体中文](README.md) [English](README_EN.md)

生成日：`2026-09-27`

## 本回の用語生成に使用した出典

| 出典 | URL | 種別 | バージョン / Commit | 用途 | 信頼度 |
| --- | --- | --- | --- | --- | --- |
| NTE_Assets Localization | https://github.com/Waifus-Grace/NTE_Assets | Game Data / Localization | `ae1f348c35378184a9e14b56593f43854b7ce575` / `1.4.7 (CN extraction)` | 主データ源。同一テキストキーから多言語の公式ゲームテキストを抽出 | High |
| NTE 公式国際版サイト | https://nte.perfectworld.com/en/index.html | Official | 2026-09-27 閲覧 | ゲームタイトル、基本用語、地域名、対応言語の確認 | High |
| Steam 公式ストア | https://store.steampowered.com/app/4508340/ | Official | 2026-09-27 閲覧 | 9 種類のテキスト言語と音声言語の範囲を確認 | High |

## 確認したが用語の主出典としなかった資料

| 出典 | 判定種別 | 処理結論 |
| --- | --- | --- |
| https://github.com/SolicenTEAM/UEExtractor | Unreal Engine 抽出ツール | ツールリポジトリであり用語データではない。ローカルの .pak/.locres は直接抽出していない |
| https://github.com/NTE-ASIA/NTE-Internal | Teleport/coordinate data | TP 座標ファイルのみを含む。地図補助データとして分類し、用語集には入れない |
| https://github.com/indrasundanese/Neverness-to-Everness-Localization | Community localization corpus | 旧版の `en_US.json` のみを含む。英語キー構造の参考には使えるが、多言語用語の生成には使用していない |
| https://interactivemap.app/neverness-to-everness/database/en/ | Third-party database | 分類とサンプル確認に使用。クライアント優先データを上書きしない |
| https://thegameswiki.com/nte/wiki/localization | AI-assisted Community Wiki | 対応言語の範囲確認に使用。逐語的な訳名の出典にはしない |
| https://github.com/topics/neverness-to-everness | GitHub topic index | 一覧確認済み。多くは自動化、Mod、チート、ガチャ、地図ツールのリポジトリ |

## 言語コード対応

| 本リポジトリのコード | 上流ディレクトリ | 備考 |
| --- | --- | --- |
| `zh-CN` | `Localization/zh-CN/game.json` | 簡体字中国語テキスト |
| `zh-TW` | `Localization/zh-Hant/game.json` | 繁体字中国語テキスト。`zh-TW` に統一して対応付け |
| `en-US` | `Localization/en/game.json` | English |
| `ja-JP` | `Localization/ja/game.json` | 日本語 |
| `ko-KR` | `Localization/ko/game.json` | 한국어 |
| `de-DE` | `Localization/de/game.json` | Deutsch |
| `fr-FR` | `Localization/fr/game.json` | Français |
| `es-ES` | `Localization/es/game.json` | Español |
| `ru-RU` | `Localization/ru/game.json` | Русский |

## 対応付けの規則

各レコードは、上流の `namespace + key` 配下にある同一のテキストキーに由来します。生成器は文字列の
類似度による対応推測を行わず、欠落言語に対して機械翻訳も行いません。同一の `source + tgt_lng` に
複数の `target` が存在する場合はすべて保持し、その衝突は `tools/_validation.json` に集計します。