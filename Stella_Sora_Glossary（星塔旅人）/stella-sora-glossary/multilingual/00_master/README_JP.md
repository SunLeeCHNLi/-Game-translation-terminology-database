# 『ステラソラ』Stella Sora 五言語並列総表（`multilingual/`）

## [简体中文](README.md) [English](README_EN.md)

ローカルのゲーム多言語テキストライブラリ `StellaSoraData-main`（公式 CN / EN / JP / KR / TW の 5 地域テキスト）をキー単位で対応付けて生成したものです。
各語彙は 5 言語で ID が完全に一致しているため、互いに公式訳であり、人手による再翻訳は行っていません。

本ディレクトリ（`Stella_Sora_Glossary（星塔旅人）/multilingual/`）は**五言語並列の元総表**であり、単一の目標言語向けの用語集ではありません。
そのため言語レベルの `README.md` / `README_zh-CN.md` はありません。単一の目標言語に分割した結果は、ゲームルートディレクトリの
`zh-CN/`、`zh-TW/`、`en-US/`、`ja-JP/`、`ko-KR/` の 5 ディレクトリにあります。ゲーム全体の説明はゲームルートの
`README.md` / `README_EN.md` / `README_JP.md` を参照してください。

## 総量

- 語彙総数：**12292** 語（5 言語の語彙数は一致しており、差異は単一言語ディレクトリの `11_ui` 分類にのみ現れます）
- 言語：`zh-CN`（簡体字中国語）、`en-US`（英語）、`ja-JP`（日本語）、`ko-KR`（韓国語）、`zh-TW`（繁体字中国語）——5 言語すべてを収録
- 分類：15 の専用用語集
- 対照行数：15 分類の `NN_xxx_glossary.csv` の合計 **147462** 行（1 語あたり最大 12 行）
- 生成日：2026-09-11

## ディレクトリ構造

```text
multilingual/                     五言語並列総表（ゲームルートディレクトリ下）
  01_character/      キャラクター名         287 語
  02_skill/          スキル名             628 語
  03_potential/      潜在能力名          1457 語
  04_disc/           ディスク / Disc      234 語
  05_item/           アイテム            558 語
  06_equipment/      装備                15 語
  07_enemy/          敵                 399 語
  08_stage/          ステージ           1019 語
  09_event/          イベント            581 語
  10_system/         システム用語       1055 語
  11_ui/             UI 用語           4248 語
  12_story/          ストーリー固有名詞   527 語
  13_faction/        陣営                21 語
  14_location/       地点                27 語
  15_terminology/    ゲーム機制用語     1236 語
  00_master/
    index.csv                  分類索引と語彙数
    source_mapping.csv         取得元テーブル → 分類 の対応明細（219 行）
    StellaSora_all_terms.csv   全分類の統合総表（12292 行）
    README.md                  本説明
  StellaSora_Glossary.xlsx     同じデータの Excel ブック（目次 + 15 分類、全 16 ワークシート）
```

- 各分類ディレクトリには `NN_xxx_terms.csv` と `NN_xxx_glossary.csv` の 2 ファイルが含まれます；
- 生成スクリプトはゲームルートの `tools/`（`build_glossary.py`、`split_by_language.py`）に移動済みで、本ディレクトリに `tools/` はありません；
- `source_mapping.csv` と `StellaSora_Glossary.xlsx` は生成パイプライン外の一度限りの手順で作成されたもので、`tools/` 下の 2 スクリプトはどちらもこれらを生成しません。

## ファイル形式

各分類ディレクトリには 2 ファイルが含まれます：

**1. `NN_xxx_terms.csv` —— 多言語対照総表**

| id | zh-CN | en-US | ja-JP | ko-KR | zh-TW | src_table |
| --- | --- | --- | --- | --- | --- | --- |
| Character.103.1 | 琥珀 | Amber | コハク | 코하쿠 | 琥珀 | Character.json |

- `id`：ゲーム内の元テキストキー。照合、比較、自動更新に利用できます
- `src_table`：その語彙の取得元データテーブル
- 1 語 1 行で 5 言語を並べています。`terms.csv` の行数がその分類の語彙数です（15 分類の合計は 12292 行で、`StellaSora_all_terms.csv` の 12292 行と一致します）

**2. `NN_xxx_glossary.csv` —— 用語集（source / target / tgt_lng）**

要求された表形式でエクスポートしたもので、4 言語を総当たりで対にし、CAT / 用語管理ツールに直接インポートできます：

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| 琥珀 | Amber | en-US |
| Amber | コハク | ja-JP |
| 코하쿠 | 琥珀 | zh-CN |

各語彙は最大 12 行に展開されます（zh-CN / en-US / ja-JP / ko-KR の 4 言語による 4×3 の順序付き言語ペア）。
したがってどの言語を源言語にしても直接検索できます。ファイルはすべて UTF-8 with BOM、CRLF 改行で、
Excel でダブルクリックすれば中日韓の文字が正しく表示されます。

> すべてが 12 行に達するわけではありません。片側に訳文がない言語ペアはスキップされ、15 分類の合計は 147462 行です
> （満値は 12292 × 12 = 147504 で、差の 42 行はすべて `11_ui` によるものです。この分類では一部の UI テキストが一部地域に独立した訳文を持ちません）。

## 各分類の來源と統計

| 分類 | テーマ | 語彙数 | 対照行 | 主要な取得元テーブル |
| --- | --- | --- | --- | --- |
| `01_character` | キャラクター名 | 287 | 3444 | Character / CharacterSkin / CharacterDes / CharacterTag / NPCConfig / BoardNPC / SoldierCharacter / TrialCharacter / AffinityLevel + キャラクターアバター形象（Item Type 3·10·18） |
| `02_skill` | スキル名 | 628 | 7536 | Skill（スキル名）/ MainSkill（主力スキル）/ SecondarySkill（支援スキル）/ SubNoteSkill / SkillInstance / SkillInstanceType |
| `03_potential` | 潜在能力名 | 1457 | 17484 | 潜在能力（Item Type 6 Stype 41·42、計 1044 語）/ Talent 天賦 / TalentGroup / SoldierPotential / TowerDefensePotential / VampireTalent / PotentialPreset |
| `04_disc` | ディスク / Disc | 234 | 2808 | DiscIP（ディスク名と主題歌名）/ DiscTag（ディスクタグ）/ ディスク本体（Item Type 7）/ 曲調素材（Item Type 2 Stype 40）/ 秘紋素材（Stype 12） |
| `05_item` | アイテム | 558 | 6696 | Item 各種アイテム・素材・通貨・ギフトボックス / ActivityGoods / ResidentGoods / MallShop / MallPackage / MiningTreasure / Production / ThrowGiftItem / TowerDefenseItem / GoldenSpyItem / MallGem |
| `06_equipment` | 装備 | 15 | 180 | CharGem 紋章 / CharGemInstance 紋章試練 / CharGemInstanceType（ゲーム内の装備枠は「秘紋 Disc」が担っており、04_disc に分類済み） |
| `07_enemy` | 敵 | 399 | 4788 | MonsterManual モンスター図鑑 / TowerDefenseMonster / RegionBoss / WeekBossType / TravelerDuelBoss / ScoreBossAbility / ScoreBossGetControl |
| `08_stage` | ステージ | 1019 | 12228 | 各玩法のステージとチャプター：Chapter / StoryChapter / StorySet* / DailyInstance / InfinityTower* / JointDrill* / RegionBossLevel / WeekBossLevel / TowerDefenseLevel / ActivityLevelsLevel / CookieLevel / BreakOutLevel / TutorialLevel / VampireSurvivor / 各種詞条（Affix） |
| `09_event` | イベント | 581 | 6972 | Activity* イベントグループ / イベント任務 / イベントショップ / イベントストーリー / StarTowerEvent* 星塔イベント / EventOptions / MiningQuest / TowerDefenseQuest / BdConvert* |
| `10_system` | システム用語 | 1055 | 12660 | OpenFunc 機能名 / ErrorCode / Gacha* ガチャ / Agent 依頼 / 各種任務（Daily/Weekly/Periodic/Guide/Level/好感度 類）/ WorldClass / NotificationConfig |
| `11_ui` | UI 用語 | 4248 | 50934 | UIText（インターフェース用語）/ TopBar / JumpTo / Achievement 実績名 / Honor 称号 / Title 肩書き / PlayerHead プレイヤーアバター / MailTemplate / MainScreenCG / CharacterCG / StorySetTab |
| `12_story` | ストーリー固有名詞 | 527 | 6324 | Story メインストーリー / Plot 旅人ストーリー / StoryEvidence / StoryPreview / NPCAffinityPlot / CharacterArchiveContent キャラクターアーカイブ / Dating* デートストーリー / StarTowerTalk / MangaLoading |
| `13_faction` | 陣営 | 21 | 252 | Force 陣営 / ContentWord 固有名詞（ノヴァ帝国、恩恵意志など） |
| `14_location` | 地点 | 27 | 324 | DatingLandmark デート地点 / StarTower 星塔名 / 人手で校訂した地名（フィーリエ、アモール、ベイリーン港、ミラーシュ、蒼梧城など。訳文は公式テキストの対応付けから取得） |
| `15_terminology` | ゲーム機制用語 | 1236 | 14832 | Word 状態・機制語彙 / EffectDesc 属性語彙 / DictionaryDiagram·DictionaryEntry ゲーム辞典 / FateCard 運命カード / PenguinCard シリーズ / SoldierStarterCard·SoldierStrategyCard / StarTowerGrowthNode / MiningSupport / VampireTalentDesc など玩法機制名 |
| **合計** | | **12292** | **147462** | |

## 抽出とフィルタリングの規則

- 「名称 / ラベル」フィールドのみを抽出します（通常は `.1`、ディスク表は `.1/.2/.3`）。説明、数値、台詞本文などの長文は**収録しません**；
- `Item.json` は設定テーブルの `Type`/`Stype` に基づき、アイテム、潜在能力、ディスク、紋章、アバターなどの分類へ正確に振り分けます；
- インターフェーステキスト（UIText など）は短い用語のみを残し（簡体字中国語で 24 文字以下かつ文末記号なし）、一文まるごとの案内は除外します；
- 同一分類内で 5 言語の内容が完全に一致する重複語彙は 1 件に統合します（最初に出現した取得元テーブル ID を保持）；
- `【不要翻译】`、`【废弃】`、`[no trans]` などのプレースホルダーや廃止項目は除外済みです；
- `<color=…>`、`<sprite …>` などのリッチテキストマークアップは除去済みです。

## 生成と再現

```bash
# 本ディレクトリ（五言語並列総表）を生成します。スクリプトは固定の外部絶対パスを使用します：
#   入力 E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main
#   出力 E:\Download\BT\Codex_input\StellaSora_Glossary
python tools/build_glossary.py

# 本ディレクトリから単一言語用語集へ分割します。スクリプトは同様に外部絶対パス
# E:\Download\BT\Codex_input\StellaSora_Glossary を使用し、_summary.json をその外部ルートに書き出します
python tools/split_by_language.py
```

両スクリプトはゲームルートの `tools/` 下にあり、**どちらも本リポジトリを読み書きしません**：本ディレクトリの内容は、外部生成パイプラインの実行後にコピーされたスナップショットです。

## 既知の制限

- 台詞、ストーリー本文、アイテム説明などの長編コンテンツは本用語集の範囲外です。必要なら翻訳メモリ（TMX / 対訳）として別途エクスポートしてください；
- `14_location` では `DatingLandmark` と `StarTower` を除き、その他の地名はゲームデータに独立したテーブルがありません。
  キャラクターアーカイブの住所、実績、ストーリータイトルなどの公式対応テキストから人手で校訂・追加し、取得元を `curated (aligned in-game text)` と表記しています；
- `06_equipment` は 15 語のみです：本作には従来型の武器 / 防具表がなく、装備枠は「秘紋（Disc）」が担っています。
