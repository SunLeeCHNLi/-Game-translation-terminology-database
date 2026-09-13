# ブルーアーカイブ 用語集 / Blue Archive Terminology Database / 《蔚蓝档案》翻译术语库

## [中文](README.md) [English](README_EN.md)

本ディレクトリは、モバイルゲーム『ブルーアーカイブ』（Blue Archive / 《蔚蓝档案》）の固有名詞対訳データベースです。キャラクター名、学園、部活、ストーリータイトル、愛用品、地名、用語、イベント、ストーリー登場キャラクター、敵、スキル、アイテム、装備、家具、ステージの計 15 分類を収録しています。15 分類の合計は **7535** 項目で、対象言語ごとに **6** 套の独立した用語集（`zh-CN` / `zh-TW` / `en-US` / `ja-JP` / `ko-KR` / `th-TH`）に分割され、それぞれに 15 の分類ファイルと統合マスター表があります。訳語は公式クライアントの多言語テキストから取得し、同一のテキストキーで対応付けているため、**公式ローカライズ**であり二次翻訳ではありません。公式データが網羅していない少数の項目は、コミュニティのストーリー対訳表で補っています。

## 使用方法

1. **単一ファイルのダウンロード**：必要な言語ディレクトリ（例：`zh-CN/`）を開き、`01_character/01_character_glossary.csv` などの分類用語集をダウンロードします。変換は不要で、そのまま没入型翻訳などの用語ツールにインポートできます。
2. **言語ディレクトリごとの一括ダウンロード**：15 分類すべてが必要な場合は、その言語ディレクトリ内の全分類ファイルをダウンロードするか、`00_master/all_glossary.csv`（その言語の全対訳行を統合したマスター表）をそのまま利用します。
3. **リポジトリ全体をクローンして再生成**：`git clone` の後、`tools/` に収録されている生成スクリプトと、そのスクリプトの docstring に記載された 3 つの上流リポジトリのソースを使えば、元データから全 CSV を再生成できます。

## ディレクトリ構成

```text
Blue_Archive_Glossary（蔚蓝档案）/
  zh-CN/                   対象言語を簡体字中国語とする用語集
    00_master/             索引 + 統合マスター表 + 説明
      all_glossary.csv     15 分類すべての対訳行を統合したマスター表
      all_terms.csv        この言語の全項目リスト
      index.csv            分類索引と件数（分類別件数の正本）
      README.md            この言語の用語集の詳細説明
    01_character/          キャラクター名
    02_school/             学園
    03_club/               部活
    04_story_title/        ストーリータイトル
    05_favor_item/         愛用品
    06_location/           地名
    07_terminology/        用語
    08_event/              イベント
    09_scenario_character/ ストーリー登場キャラクター
    10_enemy/              敵
    11_skill/              スキル
    12_item/               アイテム
    13_equipment/          装備
    14_furniture/          家具
    15_stage/              ステージ
  zh-TW/                    同じ構成（対象言語：繁体字中国語）
  en-US/                    同じ構成（対象言語：英語）
  ja-JP/                    同じ構成（対象言語：日本語）
  ko-KR/                    同じ構成（対象言語：韓国語）
  th-TH/                    同じ構成（対象言語：タイ語）
  multilingual/             6 言語並列表
    00_master/
      all_terms_multilingual.csv   全項目を 1 行 1 項目で 6 言語並列にした表
      README.md                    表の説明と列定義
    01_character/           01_character_multilingual.csv
    02_school/              02_school_multilingual.csv
    03_club/                03_club_multilingual.csv
    04_story_title/         04_story_title_multilingual.csv
    05_favor_item/          05_favor_item_multilingual.csv
    06_location/            06_location_multilingual.csv
    07_terminology/         07_terminology_multilingual.csv
    08_event/               08_event_multilingual.csv
    09_scenario_character/  09_scenario_character_multilingual.csv
    10_enemy/               10_enemy_multilingual.csv
    11_skill/               11_skill_multilingual.csv
    12_item/                12_item_multilingual.csv
    13_equipment/           13_equipment_multilingual.csv
    14_furniture/           14_furniture_multilingual.csv
    15_stage/               15_stage_multilingual.csv
  tools/                    生成スクリプトと生成メタデータ
    build_glossary.py       用語集生成スクリプト（Python）
    extract_ts_titles.mjs   ストーリータイトル抽出スクリプト（Node.js が必要）
    ts_titles.json          抽出結果（`extract_ts_titles.mjs` のキャッシュ。`build_glossary.py` が直接読み込む）
  README.md                 本説明（簡体字中国語）
  README_EN.md              英語の説明
  README_JP.md              日本語の説明
```

各言語ディレクトリの `NN_xxx/` には `NN_xxx_glossary.csv` と `NN_xxx_terms.csv` の 2 ファイルだけがあり、`multilingual/` の下には `NN_xxx_multilingual.csv` が 1 つだけあります。

## データ概要

言語ごとの項目数と対訳行数（`00_master/index.csv` の値。CSV の実データ行数と一致することを確認済み）：

| フォルダ | 言語 | 項目数 | 対訳行数 |
| --- | --- | ---: | ---: |
| `zh-CN/` | 簡体字中国語 | 7477 | 29463 |
| `zh-TW/` | 繁体字中国語 | 6036 | 27453 |
| `en-US/` | 英語 | 5909 | 26623 |
| `ja-JP/` | 日本語 | 7534 | 29216 |
| `ko-KR/` | 韓国語 | 7310 | 29009 |
| `th-TH/` | タイ語 | 5908 | 26478 |

分類 × 対象言語（セルはその言語に実際に存在する項目数。各言語の `00_master/index.csv` より）：

| 分類 | テーマ | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | `ko-KR` | `th-TH` |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `01_character` | キャラクター名 | 408 | 408 | 204 | 408 | 408 | 204 |
| `02_school` | 学園 | 26 | 26 | 26 | 26 | 26 | 26 |
| `03_club` | 部活 | 43 | 43 | 43 | 43 | 43 | 43 |
| `04_story_title` | ストーリータイトル | 1086 | 680 | 665 | 1144 | 1051 | 664 |
| `05_favor_item` | 愛用品 | 51 | 51 | 51 | 51 | 51 | 51 |
| `06_location` | 地名 | 90 | 8 | 8 | 90 | 8 | 8 |
| `07_terminology` | 用語 | 1402 | 1379 | 1379 | 1401 | 1379 | 1379 |
| `08_event` | イベント | 72 | 45 | 45 | 72 | 45 | 45 |
| `09_scenario_character` | ストーリー登場キャラクター | 945 | 134 | 134 | 945 | 945 | 134 |
| `10_enemy` | 敵 | 351 | 349 | 351 | 351 | 351 | 351 |
| `11_skill` | スキル | 1069 | 1069 | 1069 | 1069 | 1069 | 1069 |
| `12_item` | アイテム | 649 | 649 | 649 | 649 | 649 | 649 |
| `13_equipment` | 装備 | 155 | 155 | 155 | 155 | 155 | 155 |
| `14_furniture` | 家具 | 472 | 472 | 472 | 472 | 472 | 472 |
| `15_stage` | ステージ | 658 | 568 | 658 | 658 | 658 | 658 |
| **合計** | | **7477** | **6036** | **5909** | **7534** | **7310** | **5908** |

> `multilingual/00_master/all_terms_multilingual.csv` は**重複を排除した全項目の集合**で、全 **7535** 行、1 行 1 項目を 6 言語並列で示します。単一言語ディレクトリの項目数より大きいのは、その言語にしか存在しない項目も含まれるためです。

## 使用した関連コンテンツ

| 出典 | 用途 |
| --- | --- |
| [RedBeanN/BlueArchive](https://github.com/RedBeanN/BlueArchive) | 公式クライアントの多言語データテーブル（`students` / `items` / `equipment` / `enemies` / `furniture` / `localization` / `stages`）。6 言語を Id とテキストキーで対応付け。本データベースの主体 |
| [ba-archive/blue-archive](https://github.com/ba-archive/blue-archive) | ストーリービューアの索引（メインストーリー / その他 / 地域イベントのタイトル、MomoTalk 会話タイトル）と、ストーリーエディタの名前表（ストーリー登場キャラクター） |
| [HePudding/ba-storybook](https://github.com/HePudding/ba-storybook) | コミュニティが整理した日→中のストーリー対訳表（ストーリータイトル / 地名 / イベント / ストーリー登場キャラクター）。公式テーブルが網羅しない項目の補完に使用 |

## 再生成

```bash
# 既定では E:\Download\BT\Codex_input 配下の 3 つの上流リポジトリを読み込み、
# このゲームディレクトリへ出力する
python tools/build_glossary.py

# 入力 / 出力ディレクトリを上書きする
# PowerShell（Windows）：
$env:BA_INPUT_DIR="D:\src"; $env:BA_OUTPUT_DIR="D:\out"; python tools/build_glossary.py
# bash（Linux / macOS）：
BA_INPUT_DIR="/data/src" BA_OUTPUT_DIR="/data/out" python tools/build_glossary.py

# ストーリータイトルのキャッシュ：Node.js が必要。tools/ts_titles.json を出力する
node tools/extract_ts_titles.mjs
```

## 説明

- 6 言語のタグ：`zh-CN` 簡体字中国語（中国版）、`zh-TW` 繁体字中国語（グローバル版）、`en-US` 英語、`ja-JP` 日本語、`ko-KR` 韓国語、`th-TH` タイ語。
- 訳語は公式クライアントの多言語テキストから取得し、同一のテキストキーで対応付けています。公式ローカライズであり、二次翻訳ではありません。
- `zh-CN` と `zh-TW` は別々の公式ローカライズであるため、訳名が簡繁の違いだけにとどまらないことがあり、同じ語でも学園の略称と正式名称で異なる場合があります（例：`Gehenna` は簡体字の略称が「格黑娜」、正式名称が「歌赫娜」、繁体字の正式名称が「格黑娜學園」）。
- 同じ名称でも出典によって表記が揺れることがあります。本データベースは公式データテーブルを優先し、コミュニティの対訳表は公式表にない項目の補完にのみ使用します。
- キャラクター分類には「氏名（姓＋名）」の項目を別途収録していますが、日中韓の 3 言語のみです。英語とタイ語は姓名の順序が日中韓と逆で、公式データにそのまま連結できる表記がないためです。
- `04_story_title`、`06_location`、`09_scenario_character` はストーリーとコミュニティ資料を土台にしており、公式表と完全に同一の表記がある場合のみ他言語を自動補完するため、全項目が 6 言語そろっているわけではありません。`09_scenario_character` 内の日中韓の生徒名も公式表から取得し、公式表にない NPC のみクライアントの名前表を使います。
- 同じ名称に複数のデータがある場合（例：レベル違いの同名の敵）は 1 項目に統合します。対象言語と表記が完全に同じ項目は用語集に書き込みません。
- ごく少数の項目（約 1%–3%）では、**同一の対象言語ファイル内**で 1 つの `source` が複数の `target` に対応します。同名異物の短い語（例：`Normal` は装甲タイプでもありアイテムのレアリティでもある）や、簡体字版と繁体字版のクライアント表記が併存する場合によるものです。`source` で重複排除するツールは 1 件しか残しませんので、区別が必要な場合は `_terms.csv` の `id` と `src_table` で文脈を確認してください。
- 分類ファイル `NN_xxx_glossary.csv` は `source,target,tgt_lng` の 3 列、`00_master/all_glossary.csv` は先頭に `category` 列が付いた 4 列、`all_terms.csv` は `category,category_label,id,term,src_table`、`index.csv` は `category,label,term_count,glossary_file,terms_file,target_language` です。
- すべての CSV は UTF-8 with BOM、改行は CRLF で、Excel でダブルクリックすれば日中韓・タイ文字も正しく表示されます。`.md` の説明ファイルは UTF-8（BOM なし）です。
- 再生成：`python tools/build_glossary.py`（既定では `E:\Download\BT\Codex_input` を読み込み、環境変数 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` で上書きできます。スクリプトは `tools/` にあるため、コマンドラインには `tools/` の接頭辞が必要です）。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語データベースであり、個人の学習・研究、および AI 翻訳ソフト（没入型翻訳を含みますがこれに限りません）の用語マッチングを補助する目的にのみ使用されます。本データベースは『ブルーアーカイブ』の開発元、販売元、代理店、運営、権利者といかなる従属・許諾・提携・代理・公式代表の関係もありません。収録された訳名は公式の見解ではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なしてはなりません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はそれぞれの権利者に帰属します。本データベースはこれらの第三者の知的財産権について何らの権利も主張しません。本プロジェクトおよびそれに基づいて生成された翻訳結果の利用に起因する一切の責任は利用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。維持者が確認のうえ修正または削除します。完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元、販売元、代理店、権利者といかなる隷属・許諾・提携・代理関係もありません。**
