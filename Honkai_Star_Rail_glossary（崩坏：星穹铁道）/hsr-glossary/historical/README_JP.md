# 過去の訳名 / Historical names

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、**旧バージョンのクライアント**と現行バージョン（4.5.0）の間で生じた訳名の
変更を保存するもので、バージョンの追溯と旧テキストの照合に用います。現行バージョンの訳名は、
常に `hsr-glossary/<lang>/` 配下の正式な項目です。

## ファイル

- `historical_names.csv` — 3列 `source,target,tgt_lng`
  - `source`：旧バージョンのクライアントでの表記（2.3.0 または 4.0）
  - `target`：現行 4.5.0 クライアントでの表記
  - `tgt_lng`：その表記の言語
- `_history_counts.json` — 由来別・言語別に検出した差異の件数

## 比較の基準

| 基準 | バージョン | Commit |
| --- | --- | --- |
| VizualAbstract/StarRailStaticAPI | 2.3.0 | `e039e51` |
| nathacks/HSR-Mapping-DATA | 4.0 | `245f286` |
| 現行バージョン | Mar-7th/StarRailRes 4.5.0 | `d226bef` |

比較対象（エンティティ ID で対応付け）：`characters`、`light_cones`、`relic_sets`、`relics`、
`simulated_curios`、`simulated_blessings`、`simulated_events`、`paths`、`elements`、`achievements`。

## 処理規則

1. **同一エンティティ ID** の名称のみを比較し、文字列の類似度による照合は行いません。
2. 比較前に `<i>` などの HTML タグ、`{RUBY_B#…}` などのルビ注釈、前後の引用符を除去するため、
   「マークアップだけの変更」が訳名変更として誤検出されることはありません。
3. 大文字小文字、空白、句読点などの実質的な差異は保持します（例：`Deja Vu` → `Déjà Vu`）。
4. 差異はすべてそのまま保存し、どちらがより「正しい」かは自動判定しません。正式な項目は常に
   現行バージョンに従います。

再生成：

```bash
python ../tools/build_hsr_history.py
```