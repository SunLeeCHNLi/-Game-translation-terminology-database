# 崩壊：スターレイル（Honkai: Star Rail）多言語用語集

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは、『崩壊：スターレイル』（Honkai: Star Rail / HSR）の用語集を対象言語別に格納しています。
各 CSV ファイルは厳密に 3 列のみです：`source`、`target`、`tgt_lng`。

- 総レコード数：**4,085,059**
- 重複排除後の用語キー（concept）：**42,126**
- 対象言語：**13**
- 分類：**26**
- クライアントデータバージョン：`4.5.0 (TurnBasedGameData 4.5.0, commit 4ce30f69b)`

`source` は同一のゲームテキストキーにおける他言語の公式ローカライズテキスト、`target` は本ディレクトリの言語の公式ローカライズテキストであり、
両者は TextMap Hash / エンティティ ID によって対応付けられており、機械翻訳は使用していません。

ファイルはリポジトリ共通の CSV 形式（`source,target,tgt_lng` の 3 列、UTF-8（BOM 付き）、CRLF）を使用しています。
タブ区切りで同一内容のファイルが必要な場合は、`python ../tools/build_hsr_glossary.py --format tsv` を実行すると
同名の `.tsv` ファイルを生成できます（列構造は完全に同一で、区切り文字のみ異なります）。

再生成と検証：

```bash
python ../tools/build_hsr_glossary.py
python ../tools/build_hsr_history.py
python ../tools/build_hsr_curated.py
python ../tools/validate_hsr_glossary.py
python ../tools/make_hsr_docs.py
```

## 言語別規模

| 対象言語 | 言語 | レコード数 |
| --- | --- | ---: |
| `zh-CN` | 简体中文 | 319,693 |
| `zh-TW` | 繁體中文 | 320,157 |
| `en-US` | English | 313,831 |
| `ja-JP` | 日本語 | 317,716 |
| `ko-KR` | 한국어 | 319,228 |
| `fr-FR` | Français | 306,045 |
| `de-DE` | Deutsch | 307,905 |
| `es-ES` | Español | 307,652 |
| `ru-RU` | Русский | 313,470 |
| `pt-PT` | Português | 311,326 |
| `id-ID` | Bahasa Indonesia | 313,603 |
| `th-TH` | ไทย | 317,329 |
| `vi-VN` | Tiếng Việt | 317,104 |

## 分類別規模

| 分類 | 中国語名 | English | 独立用語キー | 全言語レコード数 |
| --- | --- | --- | ---: | ---: |
| `01_character` | 角色与 NPC | Characters & NPCs | 513 | 37,756 |
| `02_path` | 命途 | Paths | 18 | 2,678 |
| `03_element` | 属性 | Elements | 14 | 1,937 |
| `04_skill` | 技能 | Skills | 825 | 67,089 |
| `05_trace` | 行迹 | Traces | 1,380 | 39,786 |
| `06_eidolon` | 星魂 | Eidolons | 840 | 71,475 |
| `07_light_cone` | 光锥 | Light Cones | 338 | 41,840 |
| `08_relic` | 遗器 | Relics | 918 | 35,527 |
| `09_item` | 道具 | Items | 2,101 | 258,055 |
| `10_material` | 材料 | Materials | 604 | 79,033 |
| `11_enemy` | 敌人 | Enemies | 1,899 | 123,140 |
| `12_location` | 地点 | Locations | 2,315 | 152,554 |
| `13_faction` | 阵营与组织 | Factions | 61 | 4,618 |
| `14_quest` | 任务 | Quests | 10,378 | 866,645 |
| `15_stage` | 关卡与副本 | Stages | 211 | 25,915 |
| `16_event` | 活动 | Events | 2,145 | 192,044 |
| `17_achievement` | 成就 | Achievements | 1,928 | 281,679 |
| `18_simulated_universe` | 模拟宇宙 | Simulated Universe | 3,010 | 264,638 |
| `19_forgotten_hall` | 忘却之庭 | Forgotten Hall | 962 | 126,858 |
| `20_story` | 剧情 | Story | 24 | 2,826 |
| `21_world_lore` | 世界观 | World Lore | 175 | 15,998 |
| `22_book` | 书籍 | Books | 1,100 | 147,763 |
| `23_dialogue` | 对话 | Dialogue | 6,258 | 784,728 |
| `24_system` | 系统 | System | 2,373 | 281,948 |
| `25_ui` | 界面 | UI | 1,315 | 149,681 |
| `26_other` | 其他 | Other | 421 | 28,848 |

## その他のディレクトリ

- `historical/` — 旧バージョンのクライアント（2.3.0 / 4.0）と比較して得られた歴史的な訳名の変更。
- `curated/` — 少数の人力確認済み項目（開拓者/主人公など）。すべてクライアントテキスト内に存在することを検証済み。

## 品質検証

直近の検証結果（`../tools/_validation.json`）：

| 検査項目 | 結果 |
| --- | ---: |
| 空の source / 空の target | 0 / 0 |
| 言語コードの誤り | 0 |
| 重複レコード | 0 |
| HTML タグ | 0 |
| 開発用変数 | 0 |
| Hash / 内部 ID | 0 / 0 |
| N/A などのプレースホルダー | 0 |
| 対象テキストがクライアントテキストに存在しない | 0 |
| 機械翻訳レコード | 0 |