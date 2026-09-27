# Stella Sora 用語集 / Stella Sora Terminology Database / 《星塔旅人》翻译术语库

## [中文](README.md) [English](README_EN.md)

本データベースは、モバイルゲーム『ステラソラ』（Stella Sora / 《星塔旅人》）の固有名詞対照表を収録したものです。キャラクター名、スキル、潜在能力、ディスク、アイテム、装備、敵、ステージ、イベント、システム用語、UI 文言、ストーリー固有名詞、勢力、地名、ゲームシステムという 15 分類を網羅し、5 言語並列表では合計 **12,292** 件の用語を収録しています。用語は対象言語ごとに **5** つの独立した用語集（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR`）に分割され、各々が 15 の分類ファイルと 1 つの統合表を持ちます。訳文はゲーム公式の多言語テキスト（CN / EN / JP / KR / TW の各リージョンのクライアントテキスト）に由来し、各言語は同一のテキストキーで対応付けられているため、**公式ローカライズ**であり二次翻訳ではありません。

## 使用方法

1. **単一ファイルのダウンロード**：`stella-sora-glossary/` 以下の対象言語ディレクトリ（例：`stella-sora-glossary/zh-CN/`）を開き、`character.csv` のような分類用語表をダウンロードしてください。変換なしで「没入型翻訳（Immersive Translation）」などの用語ツールに直接インポートできます。
2. **言語ディレクトリごとまとめてダウンロード**：15 分類すべてが必要な場合は、その言語ディレクトリ内の全分類ファイルをダウンロードしてください。各言語の統合表は `stella-sora-glossary/_master/<lang>__all_glossary.csv` にあります。
3. **リポジトリ全体をクローンして自力で再生成**：`git clone` の後、`tools/` に収録された生成スクリプトと、スクリプトの docstring が参照している上流リポジトリのソースコードを併用すれば、元データから全 CSV を再生成できます。ただし 2 つのスクリプトは**外部の絶対パス**を使用します。詳細は下記「再生成」を参照してください。

## ディレクトリ構成

```text
Stella_Sora_Glossary（星塔旅人）/
  stella-sora-glossary/     単一言語用語集のデータコンテナ
    README.md               サブライブラリの説明、分類一覧、件数
    zh-CN/                  簡体字中国語を対象言語とする用語集
      README.md             言語別の説明（簡体字中国語）
      character.csv         キャラクター名用語表（source,target,tgt_lng）
      character__terms.csv  本言語の用語一覧（id,term,src_table）
      skill.csv / skill__terms.csv
      ...                   計 15 組のフラットな分類 CSV
    zh-TW/                  同構造（対象言語は繁體中文）
    en-US/                  同構造（対象言語は English）
    ja-JP/                  同構造（対象言語は日本語）
    ko-KR/                  同構造（対象言語は한국어）
    _master/                各言語の統合表、索引、既存の言語説明
      zh-CN__all_glossary.csv
      zh-CN__all_terms.csv
      zh-CN__index.csv
      zh-CN__README.md
      ...                   他言語は <lang>__<元ファイル名>
    multilingual/           5 言語並列表（内部構成は変更なし）
      00_master/
        index.csv
        README.md
        source_mapping.csv
        StellaSora_all_terms.csv
      01_character/ … 15_terminology/
      StellaSora_Glossary.xlsx
  tools/                    生成スクリプト
    build_glossary.py       5 言語並列表の生成スクリプト（Python、外部データディレクトリを読み込む）
    split_by_language.py    対象言語ごとの分割スクリプト（Python、外部の並列表ディレクトリを読み込む）
  README.md                 本説明（簡体字中国語）
  README_EN.md              英語説明
  README_JP.md              日本語説明
```

各言語ディレクトリの 15 分類 CSV は**言語ディレクトリ直下にフラット配置**されます。`<cat>.csv` が用語表、`<cat>__terms.csv` がその言語の用語一覧です。言語ディレクトリ内に `NN_xxx/` サブディレクトリはありません。`stella-sora-glossary/multilingual/` 配下の `NN_xxx/` は 5 言語並列の元表の構成を維持します。
## データ概要

各言語の用語数と対照行数（各言語の `stella-sora-glossary/_master/<lang>__index.csv` の `TOTAL` 行から取得し、15 分類すべての CSV の実データ行数、および `stella-sora-glossary/_master/<lang>__all_terms.csv` / `<lang>__all_glossary.csv` の行数と突き合わせて一致を確認済み）：

| フォルダ | 言語 | 用語数 | 対照行数 |
| --- | --- | ---: | ---: |
| `stella-sora-glossary/zh-CN/` | 簡体字中国語 | 12292 | 46279 |
| `stella-sora-glossary/zh-TW/` | 繁體中文 | 12292 | 46052 |
| `stella-sora-glossary/en-US/` | English | 12288 | 46032 |
| `stella-sora-glossary/ja-JP/` | 日本語 | 12289 | 46426 |
| `stella-sora-glossary/ko-KR/` | 한국어 | 12292 | 45950 |
| **合計（5 ディレクトリの単純合算）** | | **61453** | **230739** |

分類 × 対象言語の**用語数**マトリクス（各セルはその言語ディレクトリに実際に存在する用語数。各言語の `stella-sora-glossary/_master/<lang>__index.csv` より）：

| 分類 | テーマ | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | キャラクター名 | 287 | 287 | 287 | 287 | 287 |
| `skill.csv` | スキル名 | 628 | 628 | 628 | 628 | 628 |
| `potential.csv` | 潜在能力名 | 1457 | 1457 | 1457 | 1457 | 1457 |
| `disc.csv` | ディスク | 234 | 234 | 234 | 234 | 234 |
| `item.csv` | アイテム | 558 | 558 | 558 | 558 | 558 |
| `equipment.csv` | 装備 | 15 | 15 | 15 | 15 | 15 |
| `enemy.csv` | 敵 | 399 | 399 | 399 | 399 | 399 |
| `stage.csv` | ステージ | 1019 | 1019 | 1019 | 1019 | 1019 |
| `event.csv` | イベント | 581 | 581 | 581 | 581 | 581 |
| `system.csv` | システム用語 | 1055 | 1055 | 1055 | 1055 | 1055 |
| `ui.csv` | UI 文言 | 4248 | 4248 | 4244 | 4245 | 4248 |
| `story.csv` | ストーリー固有名詞 | 527 | 527 | 527 | 527 | 527 |
| `faction.csv` | 勢力 | 21 | 21 | 21 | 21 | 21 |
| `location.csv` | 地名 | 27 | 27 | 27 | 27 | 27 |
| `terminology.csv` | ゲームシステム用語 | 1236 | 1236 | 1236 | 1236 | 1236 |
| **合計** | | **12292** | **12292** | **12288** | **12289** | **12292** |

分類 × 対象言語の**対照行数**マトリクス（`<cat>.csv` のデータ行数）：

| 分類 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `character.csv` | 979 | 977 | 973 | 1021 | 968 |
| `skill.csv` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `potential.csv` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `disc.csv` | 893 | 896 | 896 | 893 | 893 |
| `item.csv` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `equipment.csv` | 58 | 58 | 58 | 58 | 58 |
| `enemy.csv` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `stage.csv` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `event.csv` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `system.csv` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `ui.csv` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `story.csv` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `faction.csv` | 81 | 78 | 78 | 78 | 78 |
| `location.csv` | 98 | 98 | 98 | 96 | 96 |
| `terminology.csv` | 4660 | 4637 | 4630 | 4661 | 4649 |
| **合計** | **46279** | **46052** | **46032** | **46426** | **45950** |

5 言語並列表 `stella-sora-glossary/multilingual/`（1 行 1 用語、5 言語並列）：

| ファイル | 行数 |
| --- | ---: |
| `stella-sora-glossary/multilingual/00_master/StellaSora_all_terms.csv` | 12292 |
| `stella-sora-glossary/multilingual/00_master/source_mapping.csv` | 219 |
| `stella-sora-glossary/multilingual/NN_xxx/<cat>__terms.csv` 15 件の合計 | 12292 |
| `stella-sora-glossary/multilingual/NN_xxx/<cat>.csv` 15 件の合計 | 147462 |

> 15 分類の**用語数は `ui.csv` を除いて完全に同一**です。差異は `ui.csv` のみに現れます：公式 UI テキストの一部の項目は一部リージョンに独立した訳文がないため、`en-US` は `zh-CN` より 4 件少なく、`ja-JP` は 3 件少なくなっています。また、対照行数は重複除去のため「用語数 × 4」より少なくなります。

## 使用した関連コンテンツ

| 出典 | 用途 |
| --- | --- |
| [Hiro420/StellaSoraData](https://github.com/Hiro420/StellaSoraData) | ゲーム公式の多言語テキストライブラリ（CN / EN / JP / KR / TW の各リージョンの `language/*` テキスト表と `bin/` 設定表）。`tools/build_glossary.py` はこのデータのみを読み込む、本データベースの主たる出典 |
| [JforPlay/sstoy](https://github.com/JforPlay/sstoy) | ステラソラ関連のデータ展開・ツールの参考（リポジトリ直下の README にも併記されている上流プロジェクト。本データベースの生成スクリプトの入力ではありません） |

分類ごとの個別の出典表との対応は `stella-sora-glossary/multilingual/00_master/source_mapping.csv` と `stella-sora-glossary/multilingual/00_master/README.md` に記載しています。

## 再生成

```bash
# 1) 上流の多言語テキストライブラリから 5 言語並列表を生成
python tools/build_glossary.py

# 2) 対象言語ごとに分割し、5 つの単一言語用語集を生成
#    （同一分類内で重複する source→target 対照行は除去されます）
python tools/split_by_language.py

# 構文チェック
python -m py_compile tools/build_glossary.py tools/split_by_language.py
```

> **重要：この 2 つのスクリプトは固定の外部絶対パスを使用しており、本リポジトリの読み書きは行いません。** スクリプトの移動（旧 `multilingual/00_master/tools/` からゲーム直下の `tools/` へ）は**実行には影響しません**。どちらのスクリプトも自身の所在ディレクトリに依存していないためです：
>
> - `tools/build_glossary.py`：入力 `E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main`（上流テキストライブラリ）、出力 `E:\Download\BT\Codex_input\StellaSora_Glossary`；
> - `tools/split_by_language.py`：入出力ルートは `E:\Download\BT\Codex_input\StellaSora_Glossary`。その中の `multilingual/` を読み、同階層の `zh-CN/`、`zh-TW/`、`en-US/`、`ja-JP/`、`ko-KR/` を書き出し、`_summary.json` をその外部ルートに書き出します（**本リポジトリではありません**）。
>
> つまり、本リポジトリの CSV は外部の生成パイプラインを実行した後に**コピーしてきたスナップショット**であり、現在のスクリプトをそのまま実行しても本リポジトリは更新されません。再現するには、まず上流リポジトリを上記の外部パスに配置し（またはスクリプト内の 2 つのパス定数を書き換え）、実行後に結果を本リポジトリへコピーし直してください。直近の確認時点で `E:\Download\BT\Codex_input\` は空のディレクトリであり、上流の 2 ディレクトリは存在しません。
>
> また、`stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx` と `stella-sora-glossary/multilingual/00_master/source_mapping.csv` はパイプライン外の一回限りの手順で作られたもので、**`tools/` の 2 スクリプトはいずれもこれらを生成しません。**

## 説明

- 訳文はゲーム公式の多言語テキストライブラリ `StellaSoraData-main`（公式の CN / EN / JP / KR / TW テキスト）に由来し、各言語は同一のテキストキーで対応付けられています。公式ローカライズであり、人手による二次翻訳ではありません。
- 5 つの言語タグ：`zh-CN` 簡体字中国語、`zh-TW` 繁體中文、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어。同一の用語は 5 言語すべてで元のテキストキー（`id`）が完全に一致します。
- 各用語集内の 2 ファイルの形式は次のとおりです。

  **`<cat>.csv` — 用語表（`source` / `target` / `tgt_lng`）**

  その言語の `tgt_lng` は固定で、`source` は残り 4 言語の表記です。用語ツールにそのままインポートできます：

  | source | target | tgt_lng |
  | --- | --- | --- |
  | Amber | 琥珀 | zh-CN |
  | コハク | 琥珀 | zh-CN |
  | 코하쿠 | 琥珀 | zh-CN |

  **`<cat>__terms.csv` — 本言語の用語一覧（`id` / `term` / `src_table`）**

  | id | term | src_table |
  | --- | --- | --- |
  | Character.103.1 | 琥珀 | Character.json |

  `stella-sora-glossary/_master/<lang>__all_glossary.csv` は `source,target,tgt_lng` の前に `category` 列が 1 つ増えます。`stella-sora-glossary/_master/<lang>__all_terms.csv` は `category,category_label,id,term,src_table`、`stella-sora-glossary/_master/<lang>__index.csv` は `category,label,term_count,glossary_file,terms_file,target_language` です。
- `stella-sora-glossary/multilingual/` には 5 言語並列の元表を保持しています：`<cat>__terms.csv` は `id,zh-CN,en-US,ja-JP,ko-KR,zh-TW,src_table` で 1 行 1 用語、`<cat>.csv` は zh-CN / en-US / ja-JP / ko-KR の 4 言語を総当たりで対にし、1 用語あたり最大 12 行（4×3 の順序付き言語ペア）に展開するため、どの言語を源言語にしても直接検索できます。同一データの Excel ブック `stella-sora-glossary/multilingual/StellaSora_Glossary.xlsx`（目次 + 15 分類、全 16 シート、存在を確認済み）も同梱しています。
- **抽出と絞り込みのルール**（詳細は `stella-sora-glossary/multilingual/00_master/README.md`）：
  - 「名称 / ラベル」フィールドのみを抽出します（通常は `.1`、ディスク表は `.1/.2/.3`）。説明文、数値、セリフ本文などの長文は**収録しません**；
  - `Item.json` は設定表の `Type`/`Stype` によってアイテム、潜在能力、ディスク、紋章、アバターなどへ正確に振り分けます；
  - 界面テキスト（`UIText` など）は短い用語のみを残します（簡体字で 24 文字以下、かつ文末約物を含まない）。文章全体のヒントは除外します；
  - 同一分類内で 5 言語の内容が完全に一致する重複用語は 1 件に統合します（最初に出現した出典表の ID を保持）；
  - `【不要翻译】`、`【废弃】`、`[no trans]` などのプレースホルダーや廃止項目は除去済みです；
  - `<color=…>`、`<sprite …>` などのリッチテキストマークは除去済みです；
  - 単一言語ディレクトリへ分割する際、対象言語の表記と完全に同じ `source`、および同一分類内で既に出現した `source`→`target` 対照行は削除されます。そのため対照行数は「用語数 × 4」より少なくなります。
- **既知の制限**：
  - セリフ、ストーリー本文、アイテム説明などの長文は本データベースの対象外です。必要な場合は翻訳メモリ（TMX / 対訳）として別途書き出してください；
  - `location.csv` のうち `DatingLandmark` と `StarTower` 以外の地名は、ゲームデータに専用の表が存在しないため、キャラクター資料の住所、実績、ストーリータイトルなど公式に対応付けられたテキストから人手で校訂して補い、出典を `curated (aligned in-game text)` と表記しています；
  - `equipment.csv` は 15 件のみです。本作には従来型の武器 / 防具表がなく、装備枠は「秘紋（Disc）」が担っています；
  - どの言語ディレクトリにも、1 つの `source` が複数の `target` に対応する例が存在します（`zh-CN` で 1133 件、`zh-TW` で 962 件、`en-US` で 826 件、`ja-JP` で 1269 件、`ko-KR` で 700 件の `source` が該当）。多くは同名異物の短い語に由来します（例：英語 `Amber` は `zh-CN` では「琥珀」と「暖黄」の両方に対応）。`source` で重複除去するツールは 1 件しか残しません。区別が必要な場合は `__terms.csv` の `id` と `src_table` で文脈を確認してください。
- すべての CSV は UTF-8 with BOM、CRLF 改行です。Excel でダブルクリックすれば中日韓文字が正しく表示されます。`.md` 説明ファイルは UTF-8（BOM なし）です。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習、研究、および AI 翻訳ソフトウェア（没入型翻訳を含みますがこれに限りません）の用語マッチングの補助のみを目的としています。本データベースは『ステラソラ』の開発元、発行元、販売代理店、運営会社、著作権者との間に、いかなる従属、許諾、提携、代理または公式代表の関係も有しません。収録された訳語は公式の立場を代表するものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なされるべきではありません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はそれぞれの権利者に帰属します。本データベースはこれらの第三者の知的財産権について一切の権利を主張しません。本プロジェクトおよびそれに基づいて生成された翻訳結果の利用に起因する一切の責任は利用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。維持者が確認のうえ修正または削除します。完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご参照ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元、発行元、販売代理店、著作権者といかなる隷属、許諾、提携、代理の関係もありません。**
