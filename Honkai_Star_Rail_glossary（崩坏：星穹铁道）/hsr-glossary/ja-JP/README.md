# 『崩壊：スターレイル』用語集 — 日本語（`ja-JP`）

[← ゲーム全体の説明に戻る](../../README.md) ｜ [← hsr-glossary の説明](../README.md) ｜ [简体中文](README_zh-CN.md)

本ディレクトリは **`ja-JP`（日本語）を対象言語**とする『崩壊：スターレイル』用語集です。**26** 個のカテゴリ CSV、**317,716** 行の対訳を収録しています。`tgt_lng` 列は常に `ja-JP`、`source` 列には他言語の公式ローカライズ文が入るため、どの言語からでも本言語の訳語に一致させられます。

## ファイル

本ディレクトリは**フラット構造**で、26 個のカテゴリ CSV が直接置かれています：

| ファイル | カテゴリ | 本言語の行数 |
| --- | --- | ---: |
| `01_character（キャラクターとNPC）.csv` | Characters & NPCs | 2,910 |
| `02_path（運命）.csv` | Paths | 206 |
| `03_element（属性）.csv` | Elements | 149 |
| `04_skill（スキル）.csv` | Skills | 5,147 |
| `05_trace（痕跡）.csv` | Traces | 3,051 |
| `06_eidolon（星魂）.csv` | Eidolons | 5,486 |
| `07_light_cone（光円錐）.csv` | Light Cones | 3,219 |
| `08_relic（遺物）.csv` | Relics | 2,743 |
| `09_item（アイテム）.csv` | Items | 19,938 |
| `10_material（素材）.csv` | Materials | 6,082 |
| `11_enemy（敵）.csv` | Enemies | 9,759 |
| `12_location（場所）.csv` | Locations | 11,755 |
| `13_faction（陣営と組織）.csv` | Factions | 357 |
| `14_quest（クエスト）.csv` | Quests | 70,065 |
| `15_stage（ステージと秘境）.csv` | Stages | 1,991 |
| `16_event（イベント）.csv` | Events | 14,832 |
| `17_achievement（実績）.csv` | Achievements | 21,902 |
| `18_simulated_universe（模擬宇宙）.csv` | Simulated Universe | 20,421 |
| `19_forgotten_hall（忘卻の庭）.csv` | Forgotten Hall | 9,728 |
| `20_story（ストーリー）.csv` | Story | 214 |
| `21_world_lore（世界観）.csv` | World Lore | 1,288 |
| `22_book（書籍）.csv` | Books | 11,421 |
| `23_dialogue（会話）.csv` | Dialogue | 60,460 |
| `24_system（システム）.csv` | System | 22,379 |
| `25_ui（UI）.csv` | UI | 9,997 |
| `26_other（その他）.csv` | Other | 2,216 |

## 注意

- 訳文はゲームクライアントのローカライズテキスト（TextMap / ExcelOutput）を同一テキストキーで対応付けたもので、二次翻訳ではありません。
- 対象言語にテキストが無い場合はレコードを生成せず、機械翻訳での補完も行いません。
- 同じテキストキーでも文脈によって複数の訳語があり得るため、すべて保持します。
- `../../tools/build_hsr_glossary.py` で生成でき、再現可能です。
