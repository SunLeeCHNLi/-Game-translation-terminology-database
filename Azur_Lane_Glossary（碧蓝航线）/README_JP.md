# Azur Lane 用語集 / Azur Lane Terminology Database / 《碧蓝航线》翻译术语库

## [中文](README.md) [English](README_EN.md)

本リポジトリは、スマートフォンゲーム『アズールレーン』（《碧蓝航线》／Azur Lane）の艦船名と
航海・軍事・ゲーム用語を **4 つの対象言語**（簡体中文 `zh-CN`、English `en-US`、日本語 `ja-JP`、
한국어 `ko-KR`）で収録した用語集です。
**891 隻の艦船**（通常艦のほか META・μ兵装・II 型・コラボ艦を含み、生成表では **884 名の艦船キャラ**）と
**176 件の用語概念**（うち 175 件は他言語に対照表記あり）を収録しています。
艦船名は公式の多言語クライアントデータ（CN / EN / JP / KR / TW の `sharecfgdata` / `ShareCfg`、
抽出時の簡体中文版データは 9.6.667）から直接抽出した**公式ローカライズ文言**であり、
機械翻訳でも英語からの二次翻訳でもありません。用語表は手作業で整理し各サーバーの設定と
1 件ずつ照合したもの、調和名（和谐名）はコミュニティの対照表でも突き合わせています。

## 使用方法

1. **単一ファイルのダウンロード**：目的の言語ディレクトリ（例：`en-US/`）で
   `azur_lane_glossary.csv`、`azur_lane_ship_character_glossary.csv`、`azur_lane_terms.csv` を
   ダウンロードすれば、Immersive Translate などの用語ツールにそのまま取り込めます。
2. **言語ディレクトリごとの一括ダウンロード**：その言語の艦船名と用語をまとめて取得できます
   （`*_detailed.csv` の詳細表を含む）。
3. **リポジトリ全体をクローンして再現**：`tools/` 以下のスクリプトと上流の `AzurLaneData`
   クライアントデータ（「使用した関連コンテンツ」参照）を使って生成処理を再実行できます。

## ディレクトリ構成

```text
Azur_Lane_Glossary（碧蓝航线）/
├─ zh-CN/                                  簡体中文の用語集（target = zh-CN）
│     azur_lane_glossary.csv                   艦船名（簡体中文の標準名をソースに）
│     azur_lane_glossary_detailed.csv          同上 + ship_id / 艦種 / 陣営 / 派生
│     azur_lane_ship_character_glossary.csv    艦船名（簡体中文の調和名をソースに）
│     azur_lane_ship_character_glossary_detailed.csv
│     azur_lane_terms.csv                      航海・軍事・ゲーム用語
│     azur_lane_terms_detailed.csv             同上 + category / same_source_alternatives
│     azur_lane_ambiguous.csv                  一語多義のソース語（zh-CN のみ）
│     azur_lane_combined_ships_and_terms.csv   艦船 + 用語の統合版（zh-CN のみ）
│     README.md                                このディレクトリの説明（簡体中文）
├─ en-US/                                  同じ 6 CSV + README.md / README_zh-CN.md
├─ ja-JP/                                  同じ 6 CSV + README.md / README_zh-CN.md
├─ ko-KR/                                  同じ 6 CSV + README.md / README_zh-CN.md
├─ by_language/                            ソース言語別に分割した艦船サブ表（target は常に簡体中文）
│     azur_lane_glossary_en-zh-CN.csv
│     azur_lane_glossary_ja-zh-CN.csv
│     azur_lane_glossary_ko-zh-CN.csv
│     azur_lane_glossary_zh-TW-zh-CN.csv
├─ sources/
│     moegirl_name_table.json              萌娘百科『アズールレーン/名称対照表』の取得結果（突き合わせ用）
├─ tools/                                  生成スクリプトと統計メタデータ
│     build_glossary.py                        艦船用語集（簡体中文の標準名）+ 5 言語総表 + by_language + 多義表 + 単字コード名
│     build_harmonized.py                      調和名（和谐名）対照表
│     build_ship_character_glossary.py         艦船キャラ用語集（簡体中文の調和名）
│     build_multilang_glossaries.py            艦船表の en-US / ja-JP / ko-KR 版
│     build_terms_glossaries.py                用語表の 4 言語版
│     terms_data.py                            用語データのソース（手作業で維持）
│     build_stats.json                         生成統計（前回ビルドの出力）
├─ azur_lane_ship_names_multilingual.csv   891 隻の中文／英／日／繁／韓 5 言語総表（ソースデータ）
├─ azur_lane_harmonized_ship_names.csv     調和名対照（原名 → 調和名、1187 行）
├─ azur_lane_harmonized_names_detailed.csv 調和名の明細（1259 行、萌娘百科による検証メモ付き）
├─ azur_lane_harmonized_equipment.csv      艦載機など装備の調和名 8 件
├─ azur_lane_ijn_codename_aliases.csv      旧日本海軍の単字コード名対照（柚 → 绫波、1082 行）
└─ README.md / README_EN.md / README_JP.md 中文 / English / 日本語の説明
```

4 つの言語ディレクトリのファイル構成はまったく同じです（`zh-CN` のみ
`azur_lane_ambiguous.csv` と `azur_lane_combined_ships_and_terms.csv` を追加で持ちます）。
`target` はその言語の名称、`tgt_lng` はそれぞれ `zh-CN` / `en-US` / `ja-JP` / `ko-KR` に固定され、
`source` には他のすべての言語の表記が入ります。
`by_language/` は同じ艦船群の**ソース言語側ビュー**です（英語 1544 行、日本語 696 行、韓国語 814 行、
繁体字 538 行、合計 3592 行 = `zh-CN/azur_lane_glossary_detailed.csv` の行数）。

## データ概要

### 語数と対照行数

| 言語 | 艦船名・簡体中文標準名がソース<br>語数 / 対照行 | 艦船名・簡体中文調和名がソース<br>語数 / 対照行 | 用語<br>語数 / 対照行 |
| --- | --- | --- | --- |
| `zh-CN` | 877 / 3514 | 875 / 3804 | 170 / 449 |
| `en-US` | 821 / 2795 | 855 / 3084 | 154 / 404 |
| `ja-JP` | 877 / 3516 | 877 / 3805 | 125 / 356 |
| `ko-KR` | 850 / 3481 | 850 / 3769 | 165 / 459 |

- **語数** = その言語ディレクトリの `azur_lane_*.csv` における `target` 列の重複排除後の件数
  （その言語で訳名を持つ艦船・用語の数）。**対照行** = ヘッダーを除く CSV のデータ行数
  （UTF-8 with BOM + CRLF なので Excel でそのまま開けます）。
- 明細表の行数：`azur_lane_glossary_detailed.csv` は 3592（zh-CN）/ 2809（en-US）/ 3596（ja-JP）/
  3525（ko-KR）、`azur_lane_ship_character_glossary_detailed.csv` は 3890 / 3104 / 3890 / 3818。
- `zh-CN` のみが持つ 2 表：`azur_lane_ambiguous.csv` は 162 行（一語多義のソース語 77 件）、
  `azur_lane_combined_ships_and_terms.csv` は 3985 行（艦船 3592 行と用語 475 行を統合・重複排除）。

### 分類と件数

艦船の派生（`zh-CN/azur_lane_ship_character_glossary_detailed.csv` で集計、**884 名の艦船キャラ**）：

| 派生 | 隻数 | 対照行 |
| --- | --- | --- |
| 通常艦（派生タグなし） | 795 | 3466 |
| META | 60 | 280 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合計** | **884** | **3890** |

用語の 5 分類（`zh-CN/azur_lane_terms_detailed.csv` で集計）：

| `category` | 主題 | 概念数 | 対照行 |
| --- | --- | --- | --- |
| `hull_type` | 艦種 | 31 | 97 |
| `naval_term` | 航海・軍事用語 | 72 | 198 |
| `navy_prefix` | 陣営・艦名前綴り | 24 | 59 |
| `rank` | 階級 | 24 | 44 |
| `game_term` | ゲーム用語 | 24 | 61 |
| **合計** | — | **175** | **459** |

`tools/terms_data.py` に手作業で維持している元データは **478 件**（英語 175、日本語 127、韓国語 176）で、
書き出し時に `(source, target, src_lng)` で重複排除されます。`META`（`navy_prefix` 分類）は
ソース文字列と中国語の target 文字列が同一のため除外され、生成表で対照行を持つ概念は 175 件になります。

### 艦船キャラ用語集

| ファイル | zh-CN | en-US | ja-JP | ko-KR |
| --- | --- | --- | --- | --- |
| `azur_lane_glossary.csv`（簡体中文の標準名がソース） | 3514 | 2795 | 3516 | 3481 |
| `azur_lane_ship_character_glossary.csv`（簡体中文の調和名がソース） | 3804 | 3084 | 3805 | 3769 |

- **891 隻の艦船 / 884 名の艦船キャラ**を収録（META・μ兵装・II 型・コラボ艦を含む）。
- `azur_lane_ship_character_glossary` の `target` は常に**簡体中文版クライアントの実際の表示名**です。
  調和名がある場合は調和名（**295 名**）、なければ標準中国語名を用います。他の言語版では
  それぞれの言語の艦船名が `target` になります。
- ソース言語には簡体中文の標準名・簡体中文の調和名・英語名・英語の正式艦名（例：`IJN Fubuki`）・
  日本語名・繁体字名・韓国語名が含まれます。
- 例（各言語ディレクトリの実際の行、`azur_lane_glossary.csv`）：

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| Enterprise                | 企业               | zh-CN   |
| エンタープライズ                 | 企业               | zh-CN   |
| Sheffield META            | 谢菲尔德·META        | zh-CN   |
| シェフィールド(META)             | 谢菲尔德·META        | zh-CN   |
| Illustrious μ             | 光辉(μ兵装)          | zh-CN   |
| イラストリアス(μ兵装)              | 光辉(μ兵装)          | zh-CN   |
```

- 例（`azur_lane_ship_character_glossary.csv`、簡体中文の調和名がソース。`柚` は `绫波` の調和名）：

```
| source                    | target            | tgt_lng |
| ------------------------- | ----------------- | ------- |
| 柚                         | Ayanami           | en-US   |
| 柚                         | 綾波                | ja-JP   |
| 柚                         | 아야나미               | ko-KR   |
| 绫波                        | Ayanami           | en-US   |
```

- 主表では 1 つのソース語に対して訳を 1 件だけ残します。同名多義の場合は**艦船 id が最小のもの**を
  採用し、可能な表記はすべて明細表の `same_source_alternatives` 列に記録します。例えば
  `ja-JP/azur_lane_glossary_detailed.csv` のソース `HMS Belfast` は `ベルファスト`（id 202121）と
  `ベルちゃん`（id 202181）の両方に対応し、主表は id の小さい `ベルファスト` を残し、
  両方の読みを `same_source_alternatives` に記載しています（`zh-CN` 側は `贝尔法斯特` / `小贝法`）。
- **亚尔薇特（Alvitr、鉄血の巡洋戦艦、ship_id 404061）** だけが鉄血で調和名を持たない艦船キャラです
  —— ゲーム内データにもコミュニティ対照表にも該当項目がありません。

### 航海・軍事・ゲーム用語集

`azur_lane_terms.csv`：手作業で維持する **176 件の概念**（生成表で対照行を持つのは 175 件）、
元となるソース言語別の語は 478 件（英語 175、日本語 127、韓国語 176）。

| 対象言語 | 件数 |
| --- | --- |
| `zh-CN/azur_lane_terms.csv` | 449 |
| `en-US/azur_lane_terms.csv` | 404 |
| `ja-JP/azur_lane_terms.csv` | 356 |
| `ko-KR/azur_lane_terms.csv` | 459 |

- 5 分類：`hull_type` 艦種 31、`naval_term` 航海・軍事用語 72、`navy_prefix` 陣営・艦名前綴り 24、
  `rank` 階級 24、`game_term` ゲーム用語 24（明細表には `category` / `category_zh` 列があります）。
- 同一のソース語が複数の概念に対応する場合（例：韓国語 `대령` は「海軍大佐」と「大佐」の両方）、
  主表は最初の概念を採用し、他の表記は明細表の `same_source_alternatives` 列に記録します。
- 例（`ko-KR/azur_lane_terms.csv`）：

```
| source         | target   | tgt_lng |
| -------------- | -------- | ------- |
| 驱逐舰            | 구축함      | ko-KR   |
| Destroyer      | 구축함      | ko-KR   |
| 駆逐艦            | 구축함      | ko-KR   |
| 铁血             | 메탈 블러드   | ko-KR   |
| Iron Blood     | 메탈 블러드   | ko-KR   |
| 海军上将           | 대장       | ko-KR   |
```

- **韓国語の出典**：艦種・陣営名・ゲーム内用語は KR サーバー自身の設定から取得しています
  （`ship_data_by_type` → `구축/경순/중순/…`、`fleet_tech_group` → `이글 유니온`/`메탈 블러드`、
  `world_port_data`、`medal_template`、`emoji_template` → `한계돌파`、`enemy_data_statistics` →
  `특장형 부린` など）。残りの航海用語と階級名は標準的な韓国語訳です。ゲーム内の艦種表示は
  略称（구축 / 경순 / …）ですが、用語表は常に完全形（구축함 / 경순양함 / …）を用います。

### フィールドとデータクリーニング

- `source` ソース語、`target` 対象言語の語、`tgt_lng` 対象言語、`src_lng` ソース言語（明細表のみ）。
- 抽出時に処理済みの事項：英語名のずれ（CN/JP/KR/TW の `english_name` は信頼できず、常に EN サーバーから取得）、
  期間限定スキンのコード（`qipao`/`shengdan`/`xinnian` など）の混入、本体とスキン／イベント複製の重複、
  敵・NPC の複製（`ship_data_template` で除外）、`？？？？？` のプレースホルダ名。
- 艦船の同一性は `ship_skin_template.json` の `ship_group` に従います。
- **未翻訳のフォールバック**：あるサーバーの設定が簡体中文の文字列をそのまま使っている場合は
  未翻訳と見なしますが、除外するのは**漢字を使わない**サーバー（EN、KR）だけです。
  JP / TW の漢字名が簡体中文と同じになるのは正常なケース
  （例：`吹雪`、`雷`、`杜威`、`Z1`）なので、そのまま残します。
- EN サーバーで英語名がまったく存在しない艦船（例：`企业·META`）は、同サーバーの `english_name`
  （`USS`/`HMS` などの艦籍前綴りを除去）で補います。
- 明細表の列名は `zh-CN` と他 3 言語で少し異なります。`zh-CN` は `ship_type` / `nation`、
  他の 3 言語は `ship_type_zh` / `ship_type_en` / `nation_zh` / `nation_en` を使い、
  さらに `zh_CN_form` / `zh_CN_standard` / `zh_CN_harmonised` の 3 列を持ちます。

### 既知のデータ不備

- EN サーバーの設定では `皇家方舟·META` の艦名が `Royal.META`（`Ark` が欠落）となっており、
  同サーバーの `english_name` である `Ark Royal.META` と一致しません。これはゲーム元データの
  問題であり、人手による書き換えは行っていません。

## 使用した関連コンテンツ

| 出典 | 用途 |
| --- | --- |
| [AzurLaneTools/AzurLaneData](https://github.com/AzurLaneTools/AzurLaneData) | CN / EN / JP / KR / TW のクライアント設定：`sharecfgdata/ship_data_statistics.json`（各サーバーの艦船名）、`sharecfgdata/ship_data_template.json`（艦船同一性の絞り込み）、`ShareCfg/ship_skin_template.json`（`ship_group` による正規化）、`ShareCfg/ship_data_by_type.json`（艦種名）、`ShareCfg/name_code.json`（調和名と単字コード名） |
| 萌娘百科『[碧蓝航线/名称对照表](https://zh.moegirl.org.cn/碧蓝航线/名称对照表)』 | 調和名の突き合わせ。取得結果は `sources/moegirl_name_table.json` に保存し、不一致は `azur_lane_harmonized_names_detailed.csv` の `wiki_note` 列に記載しています |

## 再生成

スクリプトは `tools/` にあり、常に `tools/` を前置して呼び出します（ゲームディレクトリで実行）：

```bash
# 1) 艦船用語集（簡体中文の標準名）+ 5 言語総表 + by_language + 多義表 + 旧日本海軍の単字コード名
python tools/build_glossary.py

# 2) 調和名（和谐名）対照表（1) の 5 言語総表が必要）
python tools/build_harmonized.py

# 3) 艦船キャラ用語集（簡体中文の調和名）
python tools/build_ship_character_glossary.py

# 4) 艦船表の en-US / ja-JP / ko-KR 版（1) の 5 言語総表が必要）
python tools/build_multilang_glossaries.py

# 5) 用語表の zh-CN / en-US / ja-JP / ko-KR 版（データは tools/terms_data.py）
python tools/build_terms_glossaries.py
```

ゲームデータを更新したら、この順序で再実行するだけです（`build_harmonized.py` と
`build_multilang_glossaries.py` は `build_glossary.py` が出力する
`azur_lane_ship_names_multilingual.csv` に依存します）。
用語の項目は `tools/terms_data.py` で維持し、4 言語版は `build_terms_glossaries.py` が自動生成します。
生成統計は `build_stats.json` に書き出されます（本リポジトリ内のコピーは `tools/build_stats.json`）。
注意：スクリプト内の `BASE` / `OUT` パス定数は**リポジトリ外**の上流設定ディレクトリと生成作業
ディレクトリを指しています。再実行前に環境に合わせて変更してください（各スクリプト冒頭の定数を参照）。
本リポジトリが保持しているのは生成結果の公開スナップショットです。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習・研究および
AI 翻訳ソフト（Immersive Translate を含みますがこれに限りません）の用語マッチング補助にのみ
使用するものです。本リポジトリは、対象ゲームの開発元・発行元・販売元・運営元・著作権者と、
いかなる従属・許諾・提携・代理・公式代表の関係も持ちません。収録された訳語は公式の立場を
代表するものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを
保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なしては
なりません**。ゲーム名・キャラクター名・固有名詞・商標などの知的財産権はすべてそれぞれの
権利者に帰属します。本リポジトリはこれらの第三者の知的財産権について何ら権利を主張しません。
本プロジェクトおよびそれに基づく翻訳結果の利用によって生じたいかなる責任も利用者自身が負うものとします。
権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。
維持者が確認のうえ修正または削除します。

完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元・発行元・販売元・著作権者と、いかなる隷属・許諾・提携・代理関係もありません。**
