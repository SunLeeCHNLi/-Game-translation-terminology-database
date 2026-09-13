# 原神 用語集 — 日本語（`ja-JP`）

[← ゲーム総説に戻る](../../README.md)

本ディレクトリは、Genshin Impact（原神）用語集のうち **`ja-JP` を目標言語とする**主用語集です。重複を排除した **8,186** 件の語句と **89,490** 行の対訳行（主分類 17 ファイルで **63,173** 行、TCG 10 ファイルで **26,317** 行）を収録しています。27 個の CSV はすべて `tgt_lng` 列が `ja-JP` に固定され、`source` に他の 13 言語のいずれかの表記、`target` にこの目標言語での名称が入ります。

## ファイル

本言語ディレクトリには、2 つの階層に分けて **27 個の CSV ファイル**があります。

- **主分類 17 件**（このディレクトリ直下）:
  `characters.csv`、`talents.csv`、`constellations.csv`、`weapons.csv`、`materials.csv`、`foods.csv`、`crafts.csv`、`artifacts.csv`、`domains.csv`、`enemies.csv`、`animals.csv`、`outfits.csv`、`windgliders.csv`、`namecards.csv`、`geographies.csv`、`achievements.csv`、`adventureranks.csv`
- **TCG サブ分類 10 件**（`TCG/` サブフォルダ内）:
  `TCG/action-cards.csv`、`TCG/character-cards.csv`、`TCG/enemy-cards.csv`、`TCG/summons.csv`、`TCG/status-effects.csv`、`TCG/keywords.csv`、`TCG/card-backs.csv`、`TCG/card-boxes.csv`、`TCG/detailed-rules.csv`、`TCG/level-rewards.csv`

各ファイルは次の 3 列のみで構成されています。

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Aether | 空 | ja-JP |

`source` = 同じゲームオブジェクトを他の 13 言語のいずれかで表記したもの、`target` = 本ディレクトリの目標言語での名称、`tgt_lng` = 対象ファイルの言語タグ（本ディレクトリでは常に `ja-JP`）。CAT ツール（Trados、memoQ、Phrase など）や Immersive Translate などの用語一致機能にそのまま用語集として読み込めます。

## 分類と件数

| 分類 | テーマ | 語句数 | 対訳行 |
| --- | --- | ---: | ---: |
| `characters.csv` | キャラクター | 122 | 577 |
| `talents.csv` | 天賦 | 125 | 632 |
| `constellations.csv` | 命ノ星座 | 125 | 632 |
| `weapons.csv` | 武器 | 249 | 2,823 |
| `materials.csv` | 素材 | 919 | 10,636 |
| `foods.csv` | 食べ物 | 398 | 4,541 |
| `crafts.csv` | 合成素材 | 295 | 3,522 |
| `artifacts.csv` | 聖遺物 | 63 | 727 |
| `domains.csv` | 秘境 | 284 | 3,636 |
| `enemies.csv` | 敵 | 346 | 4,104 |
| `animals.csv` | 生物 | 223 | 2,647 |
| `outfits.csv` | 衣装 | 150 | 1,869 |
| `windgliders.csv` | 風の翼 | 18 | 211 |
| `namecards.csv` | 名刺 | 289 | 3,606 |
| `geographies.csv` | 地名 | 268 | 3,389 |
| `achievements.csv` | 実績 | 1,548 | 19,464 |
| `adventureranks.csv` | 冒険ランクの説明 | 21 | 157 |
| `TCG/action-cards.csv` | アクションカード | 927 | 9,534 |
| `TCG/character-cards.csv` | キャラカード | 149 | 929 |
| `TCG/enemy-cards.csv` | 敵カード | 134 | 1,125 |
| `TCG/summons.csv` | 召喚物 | 152 | 1,197 |
| `TCG/status-effects.csv` | 状態効果 | 1,159 | 11,271 |
| `TCG/keywords.csv` | キーワード | 139 | 1,511 |
| `TCG/card-backs.csv` | カードの裏面 | 39 | 407 |
| `TCG/card-boxes.csv` | カードボックス | 7 | 32 |
| `TCG/detailed-rules.csv` | 詳細ルール | 11 | 142 |
| `TCG/level-rewards.csv` | レベル報酬 | 26 | 169 |
| **主分類（17 ファイル）** | — | **5,443** | **63,173** |
| **TCG（10 ファイル）** | — | **2,743** | **26,317** |
| **合計（27 ファイル）** | — | **8,186** | **89,490** |

## 説明

- **訳語の出典と対応付け**：`target` 列は [genshin-db](https://github.com/theBowja/genshin-db) 7.0 に収録されたゲーム内の**公式ローカライズ**名称であり、機械翻訳や二次翻訳ではありません。`source` 列は同じゲームオブジェクトを他の 13 言語のいずれかで表記したもので、対応付けの単位は「ゲーム内の 1 つの名称オブジェクト」です。名称と訳語が同一の重複行は統合済みです。
- **言語タグ**：本ディレクトリの全ファイルで `tgt_lng` 列は `ja-JP` に固定されています（genshin-db の内部名は `Japanese`）。
- **文字コード**：すべての CSV は **UTF-8（BOM 付き）＋ CRLF** で、カンマや引用符を含むフィールドは RFC 4180 に従ってエスケープされています。Excel でダブルクリックしても文字化けしません。
- **語句数と対訳行数の違い**：「語句数」はカテゴリごとの**重複を排除した名称オブジェクト数**（コレクション全体で共通）で、「対訳行」はこのディレクトリにあるその CSV の実際のデータ行数です。同じ語句は他の 13 言語それぞれを `source` として 1 行ずつ持つため、行数は語句数の数倍になります。同名の語句が複数のカテゴリに現れることもあります。
- **既知の制限**：データは genshin-db 7.0（14 言語）時点のもので、ゲームの現行バージョンより古い可能性があります。一部のカテゴリは言語によって数行の差があります（例：`adventureranks`、`achievements`、`enemies`）。本ディレクトリは主用語集のみを収録しており、補足用語集は `../../genshin-glossary-supplement/`、この部分集合の概要は `../README.md` にあります。

## 免責事項

本ディレクトリは個人が整理・管理する**非公式**の翻訳用語集であり、個人の学習・研究および AI 翻訳ソフト（Immersive Translate 等を含みますがこれらに限りません）の用語マッチングの補助のみを目的としています。本用語集は、関連ゲームの開発元・販売元・配信元・運営元・著作権者といかなる所属・許諾・提携・代理・公式代表の関係もありません。収録されている訳語は公式の見解を示すものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なすこともできません**。ゲーム名・キャラクター名・固有名詞・商標などの知的財産権は各権利者に帰属し、本プロジェクトはこれらの第三者の知的財産権について一切の権利を主張しません。本プロジェクトおよびそれに基づく翻訳結果の利用によって生じたいかなる責任も利用者自身が負うものとします。完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) をご覧ください。

---

**Game-translation-terminology-database は個人による独立したプロジェクトであり、上記のいずれのゲームおよび関連企業・団体とも関係ありません。**
