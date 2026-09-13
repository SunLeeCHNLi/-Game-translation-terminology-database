# Stella Sora 用語集 / Stella Sora Terminology Database / 《星塔旅人》翻译术语库

## [中文](README.md) [English](README_EN.md)

本データベースは、モバイルゲーム『ステラソラ』（Stella Sora / 《星塔旅人》）の固有名詞対照表を収録したものです。キャラクター名、スキル、潜在能力、ディスク、アイテム、装備、敵、ステージ、イベント、システム用語、UI 文言、ストーリー固有名詞、勢力、地名、ゲームシステムという 15 分類を網羅し、5 言語並列表では合計 **12,292** 件の用語を収録しています。用語は対象言語ごとに **5** つの独立した用語集（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR`）に分割され、各々が 15 の分類ファイルと 1 つの統合表を持ちます。訳文はゲーム公式の多言語テキスト（CN / EN / JP / KR / TW の各リージョンのクライアントテキスト）に由来し、各言語は同一のテキストキーで対応付けられているため、**公式ローカライズ**であり二次翻訳ではありません。

## 使用方法

1. **単一ファイルのダウンロード**：対象の言語ディレクトリ（例：`zh-CN/`）を開き、`01_character/01_character_glossary.csv` のような分類用語表をダウンロードしてください。変換なしで「没入型翻訳（Immersive Translation）」などの用語ツールに直接インポートできます。
2. **言語ディレクトリごとまとめてダウンロード**：15 分類すべてが必要な場合は、その言語ディレクトリ内の全分類ファイルをダウンロードするか、`00_master/all_glossary.csv`（その言語の全対照行を統合した表）をそのまま取得してください。
3. **リポジトリ全体をクローンして自力で再生成**：`git clone` の後、`tools/` に収録された生成スクリプトと、スクリプトの docstring が参照している上流リポジトリのソースコードを併用すれば、元データから全 CSV を再生成できます。ただし 2 つのスクリプトは**外部の絶対パス**を使用します。詳細は下記「再生成」を参照してください。

## ディレクトリ構成

```text
Stella_Sora_Glossary（星塔旅人）/
  zh-CN/                    簡体字中国語を対象言語とする用語集
    README.md               言語別の説明（簡体字中国語）
    00_master/              索引 + 統合表 + 説明
      all_glossary.csv      15 分類すべての対照行を統合した表
      all_terms.csv         本言語の全用語一覧
      index.csv             分類索引と件数（分類別件数の権威ある出典）
      README.md             本言語の既存の詳細説明
    01_character/           キャラクター名
    02_skill/               スキル名
    03_potential/           潜在能力名
    04_disc/                ディスク
    05_item/                アイテム
    06_equipment/           装備
    07_enemy/               敵
    08_stage/               ステージ
    09_event/               イベント
    10_system/              システム用語
    11_ui/                  UI 文言
    12_story/               ストーリー固有名詞
    13_faction/             勢力
    14_location/            地名
    15_terminology/         ゲームシステム用語
  zh-TW/                    同構造（対象言語は繁體中文）。README_zh-CN.md あり
  en-US/                    同構造（対象言語は English）。README_zh-CN.md あり
  ja-JP/                    同構造（対象言語は日本語）。README_zh-CN.md あり
  ko-KR/                    同構造（対象言語は한국어）。README_zh-CN.md あり
  multilingual/             5 言語並列表（単一言語ディレクトリではないため言語別 README なし）
    00_master/
      index.csv                       分類索引と件数
      README.md                       並列表の説明、列定義、分類別の出典表
      source_mapping.csv              出典表 → 分類 の対応明細（219 行）
      StellaSora_all_terms.csv        全用語を 1 行 1 件、5 言語並列で収録
    01_character/                     01_character_glossary.csv + 01_character_terms.csv
    02_skill/                         02_skill_glossary.csv + 02_skill_terms.csv
    03_potential/                     03_potential_glossary.csv + 03_potential_terms.csv
    04_disc/                          04_disc_glossary.csv + 04_disc_terms.csv
    05_item/                          05_item_glossary.csv + 05_item_terms.csv
    06_equipment/                     06_equipment_glossary.csv + 06_equipment_terms.csv
    07_enemy/                         07_enemy_glossary.csv + 07_enemy_terms.csv
    08_stage/                         08_stage_glossary.csv + 08_stage_terms.csv
    09_event/                         09_event_glossary.csv + 09_event_terms.csv
    10_system/                        10_system_glossary.csv + 10_system_terms.csv
    11_ui/                            11_ui_glossary.csv + 11_ui_terms.csv
    12_story/                         12_story_glossary.csv + 12_story_terms.csv
    13_faction/                       13_faction_glossary.csv + 13_faction_terms.csv
    14_location/                      14_location_glossary.csv + 14_location_terms.csv
    15_terminology/                   15_terminology_glossary.csv + 15_terminology_terms.csv
    StellaSora_Glossary.xlsx          同一データの Excel ブック（目次 + 15 分類、全 16 シート）
  tools/                    生成スクリプト
    build_glossary.py       5 言語並列表の生成スクリプト（Python、外部データディレクトリを読み込む）
    split_by_language.py    対象言語ごとの分割スクリプト（Python、外部の並列表ディレクトリを読み込む）
  README.md                 本説明（簡体字中国語）
  README_EN.md              英語説明
  README_JP.md              日本語説明
```

各言語ディレクトリ内の `NN_xxx/` には `NN_xxx_glossary.csv` と `NN_xxx_terms.csv` の 2 ファイルだけがあります。`multilingual/` 配下の `NN_xxx/` もファイル名は同じですが、中身は 5 言語並列の元表です（下記「説明」を参照）。

## データ概要

各言語の用語数と対照行数（各言語の `00_master/index.csv` の `TOTAL` 行から取得し、15 分類すべての CSV の実データ行数、および `00_master/all_terms.csv` / `all_glossary.csv` の行数と突き合わせて一致を確認済み）：

| フォルダ | 言語 | 用語数 | 対照行数 |
| --- | --- | ---: | ---: |
| `zh-CN/` | 簡体字中国語 | 12292 | 46279 |
| `zh-TW/` | 繁體中文 | 12292 | 46052 |
| `en-US/` | English | 12288 | 46032 |
| `ja-JP/` | 日本語 | 12289 | 46426 |
| `ko-KR/` | 한국어 | 12292 | 45950 |
| **合計（5 ディレクトリの単純合算）** | | **61453** | **230739** |

分類 × 対象言語の**用語数**マトリクス（各セルはその言語ディレクトリに実際に存在する用語数。各言語の `00_master/index.csv` より）：

| 分類 | テーマ | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `01_character` | キャラクター名 | 287 | 287 | 287 | 287 | 287 |
| `02_skill` | スキル名 | 628 | 628 | 628 | 628 | 628 |
| `03_potential` | 潜在能力名 | 1457 | 1457 | 1457 | 1457 | 1457 |
| `04_disc` | ディスク | 234 | 234 | 234 | 234 | 234 |
| `05_item` | アイテム | 558 | 558 | 558 | 558 | 558 |
| `06_equipment` | 装備 | 15 | 15 | 15 | 15 | 15 |
| `07_enemy` | 敵 | 399 | 399 | 399 | 399 | 399 |
| `08_stage` | ステージ | 1019 | 1019 | 1019 | 1019 | 1019 |
| `09_event` | イベント | 581 | 581 | 581 | 581 | 581 |
| `10_system` | システム用語 | 1055 | 1055 | 1055 | 1055 | 1055 |
| `11_ui` | UI 文言 | 4248 | 4248 | 4244 | 4245 | 4248 |
| `12_story` | ストーリー固有名詞 | 527 | 527 | 527 | 527 | 527 |
| `13_faction` | 勢力 | 21 | 21 | 21 | 21 | 21 |
| `14_location` | 地名 | 27 | 27 | 27 | 27 | 27 |
| `15_terminology` | ゲームシステム用語 | 1236 | 1236 | 1236 | 1236 | 1236 |
| **合計** | | **12292** | **12292** | **12288** | **12289** | **12292** |

分類 × 対象言語の**対照行数**マトリクス（`NN_xxx_glossary.csv` のデータ行数）：

| 分類 | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `01_character` | 979 | 977 | 973 | 1021 | 968 |
| `02_skill` | 2322 | 2273 | 2279 | 2311 | 2289 |
| `03_potential` | 5545 | 5545 | 5553 | 5575 | 5545 |
| `04_disc` | 893 | 896 | 896 | 893 | 893 |
| `05_item` | 2176 | 2176 | 2172 | 2172 | 2172 |
| `06_equipment` | 58 | 58 | 58 | 58 | 58 |
| `07_enemy` | 1547 | 1547 | 1547 | 1547 | 1547 |
| `08_stage` | 3882 | 3856 | 3856 | 3861 | 3854 |
| `09_event` | 2245 | 2228 | 2231 | 2241 | 2234 |
| `10_system` | 4130 | 4121 | 4108 | 4137 | 4117 |
| `11_ui` | 15638 | 15540 | 15529 | 15742 | 15428 |
| `12_story` | 2025 | 2022 | 2024 | 2033 | 2022 |
| `13_faction` | 81 | 78 | 78 | 78 | 78 |
| `14_location` | 98 | 98 | 98 | 96 | 96 |
| `15_terminology` | 4660 | 4637 | 4630 | 4661 | 4649 |
| **合計** | **46279** | **46052** | **46032** | **46426** | **45950** |

5 言語並列表 `multilingual/`（1 行 1 用語、5 言語並列）：

| ファイル | 行数 |
| --- | ---: |
| `multilingual/00_master/StellaSora_all_terms.csv` | 12292 |
| `multilingual/00_master/source_mapping.csv` | 219 |
| `multilingual/NN_xxx/NN_xxx_terms.csv` 15 件の合計 | 12292 |
| `multilingual/NN_xxx/NN_xxx_glossary.csv` 15 件の合計 | 147462 |

> 15 分類の**用語数は `11_ui` を除いて完全に同一**です。差異は `11_ui` のみに現れます：公式 UI テキストの一部の項目は一部リージョンに独立した訳文がないため、`en-US` は `zh-CN` より 4 件少なく、`ja-JP` は 3 件少なくなっています。また、対照行数は重複除去のため「用語数 × 4」より少なくなります。

## 使用した関連コンテンツ

| 出典 | 用途 |
| --- | --- |
| [Hiro420/StellaSoraData](https://github.com/Hiro420/StellaSoraData) | ゲーム公式の多言語テキストライブラリ（CN / EN / JP / KR / TW の各リージョンの `language/*` テキスト表と `bin/` 設定表）。`tools/build_glossary.py` はこのデータのみを読み込む、本データベースの主たる出典 |
| [JforPlay/sstoy](https://github.com/JforPlay/sstoy) | ステラソラ関連のデータ展開・ツールの参考（リポジトリ直下の README にも併記されている上流プロジェクト。本データベースの生成スクリプトの入力ではありません） |

分類ごとの個別の出典表との対応は `multilingual/00_master/source_mapping.csv` と `multilingual/00_master/README.md` に記載しています。

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
> また、`multilingual/StellaSora_Glossary.xlsx` と `multilingual/00_master/source_mapping.csv` はパイプライン外の一回限りの手順で作られたもので、**`tools/` の 2 スクリプトはいずれもこれらを生成しません。**

## 説明

- 訳文はゲーム公式の多言語テキストライブラリ `StellaSoraData-main`（公式の CN / EN / JP / KR / TW テキスト）に由来し、各言語は同一のテキストキーで対応付けられています。公式ローカライズであり、人手による二次翻訳ではありません。
- 5 つの言語タグ：`zh-CN` 簡体字中国語、`zh-TW` 繁體中文、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어。同一の用語は 5 言語すべてで元のテキストキー（`id`）が完全に一致します。
- 各用語集内の 2 ファイルの形式は次のとおりです。

  **`NN_xxx_glossary.csv` — 用語表（`source` / `target` / `tgt_lng`）**

  その言語の `tgt_lng` は固定で、`source` は残り 4 言語の表記です。用語ツールにそのままインポートできます：

  | source | target | tgt_lng |
  | --- | --- | --- |
  | Amber | 琥珀 | zh-CN |
  | コハク | 琥珀 | zh-CN |
  | 코하쿠 | 琥珀 | zh-CN |

  **`NN_xxx_terms.csv` — 本言語の用語一覧（`id` / `term` / `src_table`）**

  | id | term | src_table |
  | --- | --- | --- |
  | Character.103.1 | 琥珀 | Character.json |

  `00_master/all_glossary.csv` は `source,target,tgt_lng` の前に `category` 列が 1 つ増えます。`00_master/all_terms.csv` は `category,category_label,id,term,src_table`、`00_master/index.csv` は `category,label,term_count,glossary_file,terms_file,target_language` です。
- `multilingual/` には 5 言語並列の元表を保持しています：`NN_xxx_terms.csv` は `id,zh-CN,en-US,ja-JP,ko-KR,zh-TW,src_table` で 1 行 1 用語、`NN_xxx_glossary.csv` は zh-CN / en-US / ja-JP / ko-KR の 4 言語を総当たりで対にし、1 用語あたり最大 12 行（4×3 の順序付き言語ペア）に展開するため、どの言語を源言語にしても直接検索できます。同一データの Excel ブック `multilingual/StellaSora_Glossary.xlsx`（目次 + 15 分類、全 16 シート、存在を確認済み）も同梱しています。
- **抽出と絞り込みのルール**（詳細は `multilingual/00_master/README.md`）：
  - 「名称 / ラベル」フィールドのみを抽出します（通常は `.1`、ディスク表は `.1/.2/.3`）。説明文、数値、セリフ本文などの長文は**収録しません**；
  - `Item.json` は設定表の `Type`/`Stype` によってアイテム、潜在能力、ディスク、紋章、アバターなどへ正確に振り分けます；
  - 界面テキスト（`UIText` など）は短い用語のみを残します（簡体字で 24 文字以下、かつ文末約物を含まない）。文章全体のヒントは除外します；
  - 同一分類内で 5 言語の内容が完全に一致する重複用語は 1 件に統合します（最初に出現した出典表の ID を保持）；
  - `【不要翻译】`、`【废弃】`、`[no trans]` などのプレースホルダーや廃止項目は除去済みです；
  - `<color=…>`、`<sprite …>` などのリッチテキストマークは除去済みです；
  - 単一言語ディレクトリへ分割する際、対象言語の表記と完全に同じ `source`、および同一分類内で既に出現した `source`→`target` 対照行は削除されます。そのため対照行数は「用語数 × 4」より少なくなります。
- **既知の制限**：
  - セリフ、ストーリー本文、アイテム説明などの長文は本データベースの対象外です。必要な場合は翻訳メモリ（TMX / 対訳）として別途書き出してください；
  - `14_location` のうち `DatingLandmark` と `StarTower` 以外の地名は、ゲームデータに専用の表が存在しないため、キャラクター資料の住所、実績、ストーリータイトルなど公式に対応付けられたテキストから人手で校訂して補い、出典を `curated (aligned in-game text)` と表記しています；
  - `06_equipment` は 15 件のみです。本作には従来型の武器 / 防具表がなく、装備枠は「秘紋（Disc）」が担っています；
  - どの言語ディレクトリにも、1 つの `source` が複数の `target` に対応する例が存在します（`zh-CN` で 1133 件、`zh-TW` で 962 件、`en-US` で 826 件、`ja-JP` で 1269 件、`ko-KR` で 700 件の `source` が該当）。多くは同名異物の短い語に由来します（例：英語 `Amber` は `zh-CN` では「琥珀」と「暖黄」の両方に対応）。`source` で重複除去するツールは 1 件しか残しません。区別が必要な場合は `_terms.csv` の `id` と `src_table` で文脈を確認してください。
- すべての CSV は UTF-8 with BOM、CRLF 改行です。Excel でダブルクリックすれば中日韓文字が正しく表示されます。`.md` 説明ファイルは UTF-8（BOM なし）です。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習、研究、および AI 翻訳ソフトウェア（没入型翻訳を含みますがこれに限りません）の用語マッチングの補助のみを目的としています。本データベースは『ステラソラ』の開発元、発行元、販売代理店、運営会社、著作権者との間に、いかなる従属、許諾、提携、代理または公式代表の関係も有しません。収録された訳語は公式の立場を代表するものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なされるべきではありません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はそれぞれの権利者に帰属します。本データベースはこれらの第三者の知的財産権について一切の権利を主張しません。本プロジェクトおよびそれに基づいて生成された翻訳結果の利用に起因する一切の責任は利用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。維持者が確認のうえ修正または削除します。完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご参照ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元、発行元、販売代理店、著作権者といかなる隷属、許諾、提携、代理の関係もありません。**
