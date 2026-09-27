# データ出典記録 / Source Records

## [简体中文](README.md) [English](README_EN.md)

『崩壊：スターレイル』用語集の生成・相互検証・履歴比較に使用したデータソースです。
`Retrieved Date` は 2026-09-27 です（ローカルに `E:\Download\BT\Codex_input` へクローン済み）。

## 1. 生成に実際に使用した出典

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DimbreathBot/TurnBasedGameData | https://github.com/DimbreathBot/TurnBasedGameData | Game Data / TextMap | CHS CHT EN JP KR DE ES FR ID PT RU TH VI（13） | 4.5.0（OSPRODWin4.5.0_D16545211_A16445860_L16502768） | `4ce30f69b`（2026-09-16） | 主データ：`ExcelOutput`（設定 2185 個）+ `TextMap`（13 言語） | すべての `target` は、このデータソースの同一 TextMap Key のローカライズテキストに由来します。名称フィールドの文字列キーは xxHash64 で Hash を計算します |
| Mar-7th/StarRailRes | https://github.com/Mar-7th/StarRailRes | Structured Data | cn cht en jp kr fr de es ru pt id th vi（13） | 4.5.0（info.json timestamp 1787993304） | `d226bef`（2026-08-29） | 構造化補完 + 相互検証：命途、属性、遺物項目、遺物/セット、模擬宇宙の祝福/珍品/イベント | `index_min`（簡易版）は、TextMap で直接特定できない ID 命名項目の補完に使用します。書き込まれたすべての項目はクライアント TextMap で再確認し、一致しない文字列は書き込みません |
| VizualAbstract/StarRailStaticAPI | https://github.com/VizualAbstract/StarRailStaticAPI | Historical / Structured Data | cn cht en jp kr fr de es ru pt id th vi（13） | 2.3.0（timestamp 1718980131） | `e039e51`（2024-07-05） | 歴史的な訳名比較のベースライン（旧バージョン） | 4.5.0 と同名のエンティティを ID ごとに照合し、**名称が変化した**項目のみを `hsr-glossary/historical/` に書き込みます |
| nathacks/HSR-Mapping-DATA | https://github.com/nathacks/HSR-Mapping-DATA | Historical / Structured Data | chs cht en jp kr fr de es ru pt id th vi（13） | 4.0（README: Last Update 4.0） | `245f286`（2026-07-17） | 歴史的な訳名比較のベースライン（前バージョン） | 上記と同じ。差分のみを書き込み、現在の訳名を上書きしません |
| mrzjy/StarrailDialog | https://github.com/mrzjy/StarrailDialog | Community / Story | CHS EN | 2024-07（CHS/EN のみ） | `149dd8e`（2024-07-12） | ストーリー/セリフテキスト構造の補助的な照合 | 中国語と英語のみを収録しバージョンも古いため、正式な用語の生成には使用していません。ストーリー系テキストの構成方法の確認に使用 |
| M1k0t0/StarRail_Dialogue_Browser | https://github.com/M1k0t0/StarRail_Dialogue_Browser | Tool / Community | 上流の submodule に依存 | 2026-04 | `99f27a6`（2026-04-11） | ストーリー/セリフ閲覧ツールおよび構造の参考 | そのデータは `TurnBasedGameData` の子モジュールに由来し、本データベースは主データソースから直接データを取得します |

## 2. 確認したが生成には使用しなかった出典

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| iuyangyuc/homdgcat | https://github.com/iuyangyuc/homdgcat | Wiki / Tool | サイトは CH EN JP KR RU を提供 | 2026-02 | `7d418f5`（2026-02-13） | 参考資料（未書き込み） | リポジトリ本体は homdgcat.wiki のミラー/ダウンロードスクリプト（15357 個のファイル一覧を含む）で、サイトデータを別途取得する必要があります。今回は用語の出典として使用していません |
| kel-z/HSR-Data | https://github.com/kel-z/HSR-Data | Structured Data | EN | 2.7 | `bbffd99`（2024-12-03） | 参考資料（未書き込み） | 英語のみでバージョンも古く（2.7）、キャラクター/光円錐/遺物の構造の人力照合にのみ使用 |
| simon300000/starrail-voice | https://github.com/simon300000/starrail-voice | Voice / Tool | 多言語音声 | 2026-07 | `9478716`（2026-07-17） | 参考資料（未書き込み） | 音声抽出ツールと音声インデックスで、キャラクター名/話者の命名習慣の確認に使用。照合可能なテキスト用語キーは含まれていません |
| miHoYo『崩壊：スターレイル』公式サイト | https://sr.mihoyo.com/ | Official | zh-CN | 4.5.0 サイクル | — | 2026-09-27 | 公式表記の確認（簡体字中国語） | 簡体字中国語の公式訳名とイベント名の表記の確認に使用 |
| HoYoverse HSR グローバルサイト | https://hsr.hoyoverse.com/ | Official | en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-PT / id-ID / th-TH / vi-VN | 4.5.0 サイクル | — | 2026-09-27 | 公式表記の確認（多言語） | 各言語の公式訳名と言語サポート範囲の確認に使用。一括データソースとしては使用していません |

## 3. 言語コードの対応表

| 本データベースの `tgt_lng` | クライアント / TextMap 識別子 | StarRailRes ディレクトリ | 公式言語 |
| --- | --- | --- | --- |
| `zh-CN` | CHS | cn | 简体中文 |
| `zh-TW` | CHT | cht | 繁體中文 |
| `en-US` | EN | en | English |
| `ja-JP` | JP | jp | 日本語 |
| `ko-KR` | KR（`TextMapKR_0/1`） | kr | 한국어 |
| `fr-FR` | FR | fr | Français |
| `de-DE` | DE | de | Deutsch |
| `es-ES` | ES | es | Español |
| `ru-RU` | RU（`TextMapRU_0/1`） | ru | Русский |
| `pt-PT` | PT | pt | Português |
| `id-ID` | ID | id | Bahasa Indonesia |
| `th-TH` | TH（`TextMapTH_0/1`） | th | ไทย |
| `vi-VN` | VI | vi | Tiếng Việt |

> 説明：本データベースは『崩壊：スターレイル』の現行クライアントが実際に対応している言語のみを収録しています。
> 他の HoYoverse ゲームが対応している言語（例：`it-IT`、`tr-TR`）は本作には適用しません。

## 4. 上流データはリポジトリに同梱していません

上流リポジトリは容量が大きいため（生の TextMap、ExcelOutput、ストーリー、音声など）、すべてローカルの
`E:\Download\BT\Codex_input` 以下に保管しており、本リポジトリにはコピーしていません。再生成時は上表の URL に従って該当バージョンをクローンしてください。