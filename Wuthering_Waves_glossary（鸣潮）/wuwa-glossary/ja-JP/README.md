# 鳴潮（Wuthering Waves）用語集 — 日本語（`ja-JP`）

[← ゲーム全体の説明に戻る](../../README.md) ｜ [← wuwa-glossary サブライブラリの説明](../README.md)

本ディレクトリは**`ja-JP`（日本語）を対象言語とする**鳴潮（Wuthering Waves）の用語集です。**123,230** 件の用語と **648,414** 行の対訳（本ディレクトリの 23 個の CSV のデータ行の合計、約 **63.4 MiB**）を収録しています。すべての CSV で `tgt_lng` 列は `ja-JP` に固定され、`source` 列には他の 9 言語（`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ko-KR` (한국어), `fr-FR` (Français), `de-DE` (Deutsch), `es-ES` (Español), `pt-BR` (Português), `th-TH` (ภาษาไทย)）での表記が入るため、同じゲームテキストをどの言語からでも本言語の訳語に照合できます。

## ファイル

本ディレクトリは**フラット構成**で、23 個のカテゴリ CSV が本ディレクトリ直下にあり、追加のサブディレクトリはありません：

- `characters.csv` — キャラクター名
- `weapons.csv` — 武器名
- `echoes.csv` — 音骸
- `skills.csv` — スキル
- `resonant-chains.csv` — 共鳴チェーン
- `quests.csv` — クエスト
- `dungeons.csv` — ステージ・挑戦
- `regions.csv` — 地域・マップ
- `factions.csv` — 勢力・陣営
- `items.csv` — アイテム・素材
- `monsters.csv` — モンスター・生物
- `npcs.csv` — NPC・話者
- `achievements.csv` — 実績
- `activities.csv` — イベント・ゲームモード
- `buffs.csv` — バフ・効果
- `voice-lines.csv` — キャラクターボイス
- `archives.csv` — 書物・記録
- `terms.csv` — 用語・図鑑
- `system.csv` — システムテキスト
- `ui.csv` — UI テキスト
- `tutorials.csv` — チュートリアル
- `story.csv` — ストーリー
- `other.csv` — その他

各ファイルは `source,target,tgt_lng` の 3 列（先頭行は見出し行）です。`tgt_lng` が示す対象言語にとって `target` が訳文、`source` が**他のいずれかの言語**の原文です。したがって 1 件の項目は残り 9 言語それぞれを `source` として 1 行ずつ現れます（重複行と同形行は統合済みのため、実際の行数は用語数の 9 倍にはなりません）。ファイルは CAT ツールや Immersive Translate などの用語マッチングソフトにそのまま読み込めます。

## カテゴリと件数

| カテゴリ | テーマ | 件数 | 対訳行 |
| --- | --- | --- | --- |
| `characters.csv` | キャラクター名 | 1,230 | 5,204 |
| `weapons.csv` | 武器名 | 820 | 3,105 |
| `echoes.csv` | 音骸 | 1,000 | 6,099 |
| `skills.csv` | スキル | 5,344 | 30,475 |
| `resonant-chains.csv` | 共鳴チェーン | 784 | 6,131 |
| `quests.csv` | クエスト | 2,807 | 14,501 |
| `dungeons.csv` | ステージ・挑戦 | 1,910 | 12,127 |
| `regions.csv` | 地域・マップ | 2,229 | 16,177 |
| `factions.csv` | 勢力・陣営 | 8 | 49 |
| `items.csv` | アイテム・素材 | 8,384 | 54,386 |
| `monsters.csv` | モンスター・生物 | 685 | 4,522 |
| `npcs.csv` | NPC・話者 | 14,172 | 64,960 |
| `achievements.csv` | 実績 | 2,563 | 22,173 |
| `activities.csv` | イベント・ゲームモード | 9,531 | 63,557 |
| `buffs.csv` | バフ・効果 | 270 | 2,072 |
| `voice-lines.csv` | キャラクターボイス | 7,374 | 32,105 |
| `archives.csv` | 書物・記録 | 839 | 6,593 |
| `terms.csv` | 用語・図鑑 | 1,672 | 12,435 |
| `system.csv` | システムテキスト | 9,756 | 65,916 |
| `ui.csv` | UI テキスト | 13,866 | 79,262 |
| `tutorials.csv` | チュートリアル | 6,253 | 32,459 |
| `story.csv` | ストーリー | 29,841 | 100,775 |
| `other.csv` | その他 | 1,892 | 13,331 |
| **合計** | **23 カテゴリ** | **123,230** | **648,414** |

「件数」は重複を除いた用語数（1 用語 = ゲーム内の 1 テキストキー）で、`tools/_counts.json` の `concepts` フィールドの値です。**データベース全体で共通であり、対象言語には依存しません**。「対訳行」は本ディレクトリの該当カテゴリ CSV の実際のデータ行数です。同じテキストが複数のカテゴリに属することがあるため、カテゴリ別行数の合計は重複除去後の用語数より多くなります。

## 説明

- **訳文の出典**：`target` 列はゲーム本体のローカライズテキストをそのまま収録したものです（[Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data) の `Textmaps/<lang>/multi_text/MultiText.json`、ゲーム 3.6.0。一部のキーは [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData) の `TextMap/<lang>/MultiText.json`、ゲーム 3.1.0 で補完）。公式のゲーム内表記であり、二次翻訳ではありません。
- **対訳の作り方**：ゲームのテキストキー（例 `RoleInfo_1402_Name`）で対応付けています。同じキーの他言語表記が、本ディレクトリの `target` に対する `source` 行になります。
- **言語タグ**：`tgt_lng` は本ディレクトリの言語コードに固定され、ディレクトリ名と一致します。
- **文字コード**：すべての CSV は **UTF-8（BOM 付き）**・**CRLF** 改行・先頭行が見出し行です。カンマや引用符を含むフィールドは RFC 4180 に従ってエスケープしてあり、Excel でそのまま開けます。
- **既知の制限**：逐次のストーリー台詞（1 言語あたり約 17 万行）は既定では収録していません。必要なら `--with-dialogue` オプションで追加生成できます。方法は `../README.md` を参照してください。長すぎるテキストは `tools/wuwa_config.py` の `MAX_LEN` によりカテゴリ別に切り詰めています。`ru-RU`・`id-ID`・`vi-VN` は上流リポジトリで空のプレースホルダのため未収録、`it-IT`・`tr-TR` はゲームが対応するテキスト言語ではありません。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語集であり、個人の学習・研究および AI 翻訳ソフト（Immersive Translate 等を含みますがこれに限りません）の用語マッチングにのみ使用するものです。本用語集は、関連ゲームの開発元・発行元・販売元・運営元・権利者と、従属・許諾・提携・代理・公式代表のいずれの関係もありません。掲載される訳語は公式の見解ではなく、常に正確・完全であること、またゲームの現行バージョンと一致することは保証されず、**いかなるゲームの公式用語集や公式ローカライズファイルと見なすことはできません**。ゲーム名・キャラクター名・固有名詞・商標などの知的財産権はそれぞれの権利者に帰属し、本プロジェクトはそれらの権利を主張しません。権利者による申し立てがある場合は GitHub Issues / Pull Request でご連絡ください。内容を確認のうえ修正または削除します。完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。
