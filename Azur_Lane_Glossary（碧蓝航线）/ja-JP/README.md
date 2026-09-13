# アズールレーン 用語集 — 日本語（`ja-JP`）

[← ゲーム全体の説明に戻る](../README.md)

本ディレクトリは **日本語（`ja-JP`）を対象言語**とする『アズールレーン』の用語集です。`target` 列は
日本語表記に固定され、`source` 列には簡体中文・英語・繁体字中文・韓国語の表記が入ります。
**CSV 6 ファイル、対照行 15 519 行**を収録し、うち 3 つの主表は **7 677 行 / 去重後 877 + 877 + 125 語**です。
日本語の艦船名は公式 JP サーバーのクライアント設定から直接抽出した**公式ローカライズ文言**であり、
**機械翻訳ではありません**。

## ファイル

- `azur_lane_glossary.csv` — 列は `source,target,tgt_lng`、3516 行。艦船名（標準名表）。CAT・用語管理ツールにそのまま取り込めます
- `azur_lane_glossary_detailed.csv` — 3596 行。`src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` を追加
- `azur_lane_ship_character_glossary.csv` — 列は `source,target,tgt_lng`、3805 行。`target` は日本語艦名、`source` に簡体中文版の実際の表示名（調和名を含む）を収録
- `azur_lane_ship_character_glossary_detailed.csv` — 3890 行。追加列は上記と同じ
- `azur_lane_terms.csv` — 列は `source,target,tgt_lng`、356 行。航海・軍事・ゲーム用語
- `azur_lane_terms_detailed.csv` — 356 行。`src_lng,category,category_zh,same_source_alternatives` を追加

同階層の `by_language/` にはソース言語別に分割した艦船サブ表（`target` は常に簡体中文）、
`sources/` には調和名の突き合わせに使う萌娘百科『アズールレーン/名称対照表』の取得結果があります。

## 分類と件数

| ファイル | 対照行 | 語数（`target` の重複排除） |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 3516 | 877 |
| `azur_lane_glossary_detailed.csv` | 3596 | 879 |
| `azur_lane_ship_character_glossary.csv` | 3805 | 877 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3890 | 879 |
| `azur_lane_terms.csv` | 356 | 125 |
| `azur_lane_terms_detailed.csv` | 356 | 125 |

艦船の派生（`azur_lane_ship_character_glossary_detailed.csv` の `variant` 列で集計）：

| 派生 | 隻数（`ship_id` の重複排除） | 対照行 |
| --- | --- | --- |
| 通常艦（派生タグなし） | 795 | 3466 |
| META | 60 | 280 |
| μ兵装 | 19 | 101 |
| II 型 | 10 | 43 |
| **合計** | **884** | **3890** |

（同じ表の `target` を重複排除すると **879** 件です。複数の id が同一の日本語表示名を共有しているためです。）

用語の 5 分類（`azur_lane_terms_detailed.csv` の `category` 列で集計）：

| `category` | 主題 | 語数 | 対照行 |
| --- | --- | --- | --- |
| `hull_type` | 艦種 | 22 | 77 |
| `naval_term` | 航海・軍事用語 | 62 | 178 |
| `navy_prefix` | 陣営・艦名前綴り | 11 | 32 |
| `rank` | 階級 | 12 | 20 |
| `game_term` | ゲーム用語 | 18 | 49 |
| **合計** | — | **125** | **356** |

## 説明

- **訳文の出典と対応付け**：艦船名は公式の CN / EN / JP / KR / TW サーバーのクライアント設定から取得しています。
  艦船の同一性は `ship_skin_template.json` の `ship_group` で正規化し、敵・NPC の複製は
  `ship_data_template.json` で除外しています。用語表は手作業で整理し各サーバーの設定と 1 件ずつ照合したものです。
  本ディレクトリの主表では 1 つのソース語に対して訳を 1 件だけ残し、同名多義の場合は**艦船 id が最小のもの**を
  採用して、可能な読みをすべて明細表の `same_source_alternatives` 列に記録しています。
  例：`HMS Belfast` は `ベルファスト`（id 202121）と `ベルちゃん`（id 202181）の両方に対応し、
  主表は `ベルファスト` を残します。
- **言語タグ**：本ディレクトリの全 CSV で `tgt_lng` は `ja-JP` に固定されています。明細表の `src_lng` は
  `zh-CN` / `en-US` / `zh-TW` / `ko-KR`（用語表は `zh-CN` / `en-US` / `ko-KR`）です。
  なお `zh-CN` ディレクトリの艦船明細表は `en` / `ja` / `ko` / `zh-TW` という短いタグを使っており、
  タグの流儀はディレクトリ間で統一されていません（訳文の内容には影響しません）。
  同階層の `by_language/azur_lane_glossary_ja-zh-CN.csv` は、同じ日本語ソース文字列を簡体中文側から
  見たビューです。
- **文字コード**：すべての CSV は **UTF-8 with BOM + CRLF**（Excel でそのまま開けます）。`.md` は UTF-8（BOM なし）です。
- **既知の制限**：
  - 日本語名が簡体中文名と同じ漢字になる艦船（`吹雪`、`雷`、`杜威`、`Z1` など）は正常なケースとして
    そのまま収録しています。未翻訳と判定して除外するのは漢字を使わないサーバー（EN、KR）のみです。
  - EN サーバーの設定では `皇家方舟·META` の艦名が `Royal.META`（`Ark` が欠落）となっており、
    ゲーム元データの問題として人手による書き換えは行っていません。
  - 鉄血で簡体中文の調和名を持たない艦船キャラは亚尔薇特（Alvitr、巡洋戦艦、ship_id 404061）の 1 名だけです。
  - `azur_lane_ambiguous.csv` と `azur_lane_combined_ships_and_terms.csv` は `zh-CN` ディレクトリにのみ
    存在し、本ディレクトリには含まれません。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習・研究および
AI 翻訳ソフト（Immersive Translate を含みますがこれに限りません）の用語マッチング補助にのみ
使用するものです。**『アズールレーン』の公式用語集や公式ローカライズファイルと見なしてはなりません。**
収録された訳語は公式の立場を代表するものではなく、常に正確・完全であること、またはゲームの
現行バージョンと一致することを保証するものではありません。ゲーム名・キャラクター名・固有名詞・
商標などの知的財産権はすべてそれぞれの権利者に帰属し、本リポジトリはそれらについて何ら権利を
主張しません。本プロジェクトの利用によって生じたいかなる責任も利用者自身が負うものとします。

完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。
