# 붕괴: 스타레일(Honkai: Star Rail) 용어집 — 한국어(`ko-KR`)

[← 게임 전체 설명으로](../../README.md) ｜ [← hsr-glossary 안내](../README.md) ｜ [简体中文](README_zh-CN.md)

이 디렉터리는 **`ko-KR`(한국어)을 대상 언어로 하는** 붕괴: 스타레일 용어집입니다. **26**개 분류 CSV, **319,228**행의 대역을 수록했습니다. `tgt_lng` 열은 항상 `ko-KR`이며, `source` 열에는 다른 언어의 공식 현지화 텍스트가 들어가므로 어떤 언어에서도 이 언어의 표기를 찾을 수 있습니다.

## 파일

이 디렉터리는 **평면 구조**이며, 26개 분류 CSV가 바로 있습니다:

| 파일 | 분류 | 이 언어의 행 수 |
| --- | --- | ---: |
| `01_character（캐릭터와 NPC）.csv` | Characters & NPCs | 2,910 |
| `02_path（운명의 길）.csv` | Paths | 206 |
| `03_element（속성）.csv` | Elements | 149 |
| `04_skill（스킬）.csv` | Skills | 5,142 |
| `05_trace（흔적）.csv` | Traces | 3,051 |
| `06_eidolon（성혼）.csv` | Eidolons | 5,491 |
| `07_light_cone（광추）.csv` | Light Cones | 3,218 |
| `08_relic（유물）.csv` | Relics | 2,746 |
| `09_item（아이템）.csv` | Items | 19,935 |
| `10_material（재료）.csv` | Materials | 6,082 |
| `11_enemy（적）.csv` | Enemies | 9,648 |
| `12_location（장소）.csv` | Locations | 11,751 |
| `13_faction（세력과 조직）.csv` | Factions | 347 |
| `14_quest（임무）.csv` | Quests | 69,904 |
| `15_stage（스테이지와 비경）.csv` | Stages | 1,991 |
| `16_event（이벤트）.csv` | Events | 14,833 |
| `17_achievement（업적）.csv` | Achievements | 21,928 |
| `18_simulated_universe（모의 우주）.csv` | Simulated Universe | 20,318 |
| `19_forgotten_hall（망각의 정원）.csv` | Forgotten Hall | 9,728 |
| `20_story（스토리）.csv` | Story | 214 |
| `21_world_lore（세계관）.csv` | World Lore | 1,264 |
| `22_book（서적）.csv` | Books | 11,304 |
| `23_dialogue（대사）.csv` | Dialogue | 60,351 |
| `24_system（시스템）.csv` | System | 22,479 |
| `25_ui（인터페이스）.csv` | UI | 12,020 |
| `26_other（기타）.csv` | Other | 2,218 |

## 참고

- 번역문은 게임 클라이언트 현지화 텍스트(TextMap / ExcelOutput)를 동일한 텍스트 키로 정렬한 것이며, 2차 번역이 아닙니다.
- 대상 언어에 해당 텍스트가 없으면 레코드를 만들지 않으며, 기계 번역으로 채우지 않습니다.
- 같은 텍스트 키라도 문맥에 따라 여러 표기가 있을 수 있고, 모두 유지합니다.
- `../../tools/build_hsr_glossary.py` 로 생성되며 재현 가능합니다.
