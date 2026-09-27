# 『崩壊：スターレイル』多言語翻訳用語集

## [简体中文](README.md) ｜ [English](README_EN.md)

『崩壊：スターレイル』（Honkai: Star Rail）のクライアント日本語版・他言語版テキストから、
キャラクター、運命、属性、スキル、痕跡、星魂、光円錐、遺物、アイテム、素材、敵、地名、勢力、
任務、ステージ、イベント、実績、模擬宇宙、忘却の庭、世界観用語、書籍、会話話者名、システム、
UI などの固有名詞を対訳化した用語集です。

- 総レコード数：**4,085,059**（`source,target,tgt_lng` の3列）
- 用語キー数：**42,126**
- 対象言語：**13**（zh-CN、zh-TW、en-US、ja-JP、ko-KR、fr-FR、de-DE、es-ES、ru-RU、pt-PT、id-ID、th-TH、vi-VN）
- 分類：**26**
- クライアントデータ：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`
- **機械翻訳は一切使用していません**（すべてクライアント公式テキスト）

## ファイル形式

```text
source,target,tgt_lng
Honkai: Star Rail,崩坏：星穹铁道,zh-CN
崩壊：スターレイル,崩坏：星穹铁道,zh-CN
```

`source` は同じテキストキーの他言語テキスト、`target` は対象言語のテキストです。
対応付けは **TextMap ハッシュ / エンティティID** で行い、文字列の類似度では推測しません。

## データ出典

- 主データ：`DimbreathBot/TurnBasedGameData` 4.5.0（commit `4ce30f69b`）— TextMap ×13 + ExcelOutput
- 構造化クロスチェック：`Mar-7th/StarRailRes` 4.5.0（commit `d226bef`）
- 旧版比較：`VizualAbstract/StarRailStaticAPI` 2.3.0、`nathacks/HSR-Mapping-DATA` 4.0

詳細は [`Sources/README.md`](Sources/README.md) を参照してください。

## 検証

全 338 ファイル・4,085,059 行を対象に、空値、言語コード、
重複、HTML タグ、開発用変数、ハッシュ、内部ID、N/A、および原文がクライアントテキストに存在するかを検査しています。

| 検査項目 | 結果 |
| --- | ---: |
| 空の source / target | 0 / 0 |
| 言語コードの誤り | 0 |
| 重複レコード | 0 |
| HTML タグ | 0 |
| 開発用変数 | 0 |
| ハッシュ / 内部ID | 0 / 0 |
| N/A 等 | 0 |
| クライアントテキストに存在しない訳文 | 0 |
| 機械翻訳 | 0 |

## 統計

[`Metadata/statistics.md`](Metadata/statistics.md) を参照（総数、言語別、分類別、確認済み/未確認、
旧版用語数、複数訳語数）。旧版の訳語変更は `hsr-glossary/historical/` に、手動確認した項目は
`hsr-glossary/curated/` に保存しています。

## 再生成

```bash
python tools/build_hsr_glossary.py
python tools/build_hsr_history.py
python tools/build_hsr_curated.py
python tools/validate_hsr_glossary.py
python tools/make_hsr_docs.py
```

## 免責

本プロジェクトは個人による非公式の用語資料であり、miHoYo / HoYoverse とは一切関係ありません。
ゲーム内の名称・キャラクター・関連アセットの権利は各権利者に帰属します。
