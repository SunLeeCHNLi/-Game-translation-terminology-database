# 人工確認済み項目 / Curated entries

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、**TextMap キーから自動出力できず、クライアント本文中で一字ずつ確認した**
少数の項目を保存するものです。これらを別に保管することで、`hsr-glossary/<lang>/` 配下の
正式な用語はすべて TextMap キーから再現できる状態を保っています。

## ファイル

- `curated_terms.csv` — 3列 `source,target,tgt_lng`
- `_curated_counts.json` — 言語ごとの値の検証結果

## 現在の内容

### 開拓者 / Trailblazer（主人公）

クライアントは主人公名を `{NICKNAME}` 変数（プレイヤーが設定する名前）として保持しているため、
13 個の TextMap の中に**そのまま出力できる主人公名のキーは存在しません**。`AvatarConfig` の
`8001`–`8008`（星／穹 × 各運命形態）の `AvatarName` はすべて `{NICKNAME}` に解決され、
規則により除外されるため、正式な用語集には入りません。

主人公という固有名詞の概念を残すため、本ディレクトリには各言語での主人公の正式な呼称を収録しています。

| `tgt_lng` | クライアント表記 |
| --- | --- |
| zh-CN | 开拓者 |
| zh-TW | 開拓者 |
| en-US | Trailblazer |
| ja-JP | 開拓者 |
| ko-KR | 개척자 |
| fr-FR | Pionnier |
| de-DE | Trailblazer |
| es-ES | Trazacaminos |
| ru-RU | Первооткрыватель |
| pt-PT | Desbravador |
| id-ID | Trailblazer |
| th-TH | ผู้บุกเบิก |
| vi-VN | Nhà Khai Phá |

いずれの表記も、対応する言語のクライアント TextMap 内で確認済みです
（`build_hsr_curated.py` が 1 件ずつ検証し、検証に失敗した場合は生成時に警告を出します）。

## Stelle / Caelus について

`Stelle`（星）と `Caelus`（穹）は**同一の主人公（開拓者）の 2 つの既定名／性別表現**であり、
2 人の別キャラクターでも、独立した運命形態でもありません。

- クライアント内の主人公名は `{NICKNAME}` 変数で扱われ、`Stelle`／`Caelus` は TextMap の
  テキストキーとして存在しないため、**正式な用語集には書き込みません**。クライアント本文以外の
  文字列を公式用語と誤認させないためです。
- 主人公の各運命（壊滅、存護、調和、記憶など）は、クライアント内では `8001`–`8008` の個別の
  Avatar ID で区別されており、「同一キャラクターの異なる戦闘形態」に当たります。本データベースは
  ID ごとに分けて扱い、無関係な別人として統合することはありません。

再生成：

```bash
python ../tools/build_hsr_curated.py
```