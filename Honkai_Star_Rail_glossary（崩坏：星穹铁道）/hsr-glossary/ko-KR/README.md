# 붕괴: 스타레일(Honkai: Star Rail) 용어집 — 한국어(`ko-KR`)

[← 게임 전체 설명으로](../../README.md) ｜ [← hsr-glossary 안내](../README.md)

이 디렉터리는 **`ko-KR`(한국어)을 대상 언어로 하는** 붕괴: 스타레일 용어집입니다. **26**개 분류 CSV, **319,228**행의 대역을 수록했습니다. `tgt_lng` 열은 항상 `ko-KR`이며, `source` 열에는 다른 언어의 공식 현지화 텍스트가 들어가므로 어떤 언어에서도 이 언어의 표기를 찾을 수 있습니다.

## 파일

이 디렉터리는 **평면 구조**이며, 26개 분류 CSV가 바로 있습니다:

| 파일 | 분류 | 이 언어의 행 수 |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,910 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,142 |
| `05_trace.csv` | Traces | 3,051 |
| `06_eidolon.csv` | Eidolons | 5,491 |
| `07_light_cone.csv` | Light Cones | 3,218 |
| `08_relic.csv` | Relics | 2,746 |
| `09_item.csv` | Items | 19,935 |
| `10_material.csv` | Materials | 6,082 |
| `11_enemy.csv` | Enemies | 9,648 |
| `12_location.csv` | Locations | 11,751 |
| `13_faction.csv` | Factions | 347 |
| `14_quest.csv` | Quests | 69,904 |
| `15_stage.csv` | Stages | 1,991 |
| `16_event.csv` | Events | 14,833 |
| `17_achievement.csv` | Achievements | 21,928 |
| `18_simulated_universe.csv` | Simulated Universe | 20,318 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,728 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,264 |
| `22_book.csv` | Books | 11,304 |
| `23_dialogue.csv` | Dialogue | 60,351 |
| `24_system.csv` | System | 22,479 |
| `25_ui.csv` | UI | 12,020 |
| `26_other.csv` | Other | 2,218 |

## 참고

- 번역문은 게임 클라이언트 현지화 텍스트(TextMap / ExcelOutput)를 동일한 텍스트 키로 정렬한 것이며, 2차 번역이 아닙니다.
- 대상 언어에 해당 텍스트가 없으면 레코드를 만들지 않으며, 기계 번역으로 채우지 않습니다.
- 같은 텍스트 키라도 문맥에 따라 여러 표기가 있을 수 있고, 모두 유지합니다.
- `../../tools/build_hsr_glossary.py` 로 생성되며 재현 가능합니다.
