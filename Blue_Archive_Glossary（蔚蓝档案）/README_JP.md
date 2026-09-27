## 使用方法

1. **単一ファイルのダウンロード**：`blue-archive-glossary/<対象言語>/`（例：`blue-archive-glossary/zh-CN/`）を開き、`character.csv` などのフラットな分類用語集をダウンロードします。変換は不要で、そのまま没入型翻訳などの用語ツールにインポートできます。
2. **言語ディレクトリごとの一括ダウンロード**：15 分類すべてが必要な場合は、その言語ディレクトリ内の全分類 CSV をダウンロードするか、`blue-archive-glossary/_master/<対象言語>__all_glossary.csv`（その言語の全対訳行を統合したマスター表）をそのまま利用します。
3. **リポジトリ全体をクローンして再生成**：`git clone` の後、`tools/` に収録されている生成スクリプトと、そのスクリプトの docstring に記載された 3 つの上流リポジトリのソースを使えば、元データから全 CSV を再生成できます。

## ディレクトリ構成

```text
Blue_Archive_Glossary（蔚蓝档案）/
  blue-archive-glossary/   データ製品コンテナ
    README.md              データ製品の説明
    _master/               旧各言語 00_master/ の内容（言語接頭辞付き）
      zh-CN__all_glossary.csv  簡体字中国語の全 15 分類の対訳行を統合したマスター表
      zh-CN__all_terms.csv     簡体字中国語の全項目リスト
      zh-CN__index.csv         分類索引と件数
      zh-CN__README.md         この言語の既存の詳細説明
      ...
    zh-CN/                 対象言語を簡体字中国語とする用語集
      README.md            この言語の用語集の詳細説明
      character.csv        キャラクター名（source,target,tgt_lng）
      character__terms.csv キャラクター名の項目リスト（id,term,src_table）
      school.csv           学園
      school__terms.csv
      club.csv             部活
      club__terms.csv
      story_title.csv      ストーリータイトル
      story_title__terms.csv
      favor_item.csv       愛用品
      favor_item__terms.csv
      location.csv         地名
      location__terms.csv
      terminology.csv      用語
      terminology__terms.csv
      event.csv            イベント
      event__terms.csv
      scenario_character.csv  ストーリー登場キャラクター
      scenario_character__terms.csv
      enemy.csv            敵
      enemy__terms.csv
      skill.csv            スキル
      skill__terms.csv
      item.csv             アイテム
      item__terms.csv
      equipment.csv        装備
      equipment__terms.csv
      furniture.csv        家具
      furniture__terms.csv
      stage.csv            ステージ
      stage__terms.csv
    zh-TW/                 同じ構成（対象言語：繁体字中国語）
    en-US/                 同じ構成（対象言語：英語）
    ja-JP/                 同じ構成（対象言語：日本語）
    ko-KR/                 同じ構成（対象言語：韓国語）
    th-TH/                 同じ構成（対象言語：タイ語）
    multilingual/          6 言語並列表
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

各対象言語ディレクトリには、`<category>.csv` と `<category>__terms.csv` の 15 組のフラット CSV が直接置かれ、分類サブディレクトリはありません。`multilingual/` は元の 6 言語並列サブディレクトリ構成を維持します。
