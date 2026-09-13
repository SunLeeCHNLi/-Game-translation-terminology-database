# 명조（Wuthering Waves）용어집 — 한국어（`ko-KR`）

[← 게임 전체 설명으로 돌아가기](../../README.md) ｜ [← wuwa-glossary 하위 라이브러리 설명](../README.md)

이 디렉터리는 **`ko-KR`(한국어)을 대상 언어로 하는** 명조(Wuthering Waves) 용어집입니다. **123,230**개 용어와 **646,888**행의 대역(이 디렉터리에 있는 CSV 23개의 데이터 행 합계, 약 **63.4 MiB**)을 수록하고 있습니다. 모든 CSV의 `tgt_lng` 열은 `ko-KR`로 고정되어 있고, `source` 열에는 나머지 9개 언어(`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ja-JP` (日本語), `fr-FR` (Français), `de-DE` (Deutsch), `es-ES` (Español), `pt-BR` (Português), `th-TH` (ภาษาไทย))의 표기가 들어가므로 동일한 게임 텍스트를 어느 언어에서든 이 언어의 역어와 대조할 수 있습니다.

## 파일

이 디렉터리는 **평면 구조**로, 23개의 분류 CSV가 이 디렉터리에 바로 있으며 추가 하위 디렉터리가 없습니다:

- `characters.csv` — 캐릭터 이름
- `weapons.csv` — 무기 이름
- `echoes.csv` — 에코
- `skills.csv` — 스킬
- `resonant-chains.csv` — 공명 체인
- `quests.csv` — 퀘스트
- `dungeons.csv` — 스테이지·도전
- `regions.csv` — 지역·지도
- `factions.csv` — 세력·진영
- `items.csv` — 아이템·재료
- `monsters.csv` — 몬스터·생물
- `npcs.csv` — NPC·화자
- `achievements.csv` — 업적
- `activities.csv` — 이벤트·콘텐츠
- `buffs.csv` — 버프·효과
- `voice-lines.csv` — 캐릭터 음성
- `archives.csv` — 기록·서적
- `terms.csv` — 용어·도감
- `system.csv` — 시스템 텍스트
- `ui.csv` — UI 텍스트
- `tutorials.csv` — 튜토리얼
- `story.csv` — 스토리
- `other.csv` — 기타

각 파일은 `source,target,tgt_lng` 세 열(첫 행은 헤더)로 이루어집니다. `tgt_lng`가 지정하는 대상 언어에 대해 `target`은 번역문이고 `source`는 **다른 어느 한 언어**의 원문입니다. 따라서 하나의 항목은 나머지 9개 언어 각각을 `source`로 하여 한 행씩 나타납니다(중복 행과 동일 표기 행은 병합되었으므로 실제 행 수가 용어 수의 9배는 아닙니다). 파일은 CAT 도구나 Immersive Translate 등 용어 매칭 소프트웨어에 바로 가져올 수 있습니다.

## 분류와 개수

| 분류 | 주제 | 용어 수 | 대역 행 |
| --- | --- | --- | --- |
| `characters.csv` | 캐릭터 이름 | 1,230 | 5,209 |
| `weapons.csv` | 무기 이름 | 820 | 3,112 |
| `echoes.csv` | 에코 | 1,000 | 6,083 |
| `skills.csv` | 스킬 | 5,344 | 30,562 |
| `resonant-chains.csv` | 공명 체인 | 784 | 6,124 |
| `quests.csv` | 퀘스트 | 2,807 | 14,620 |
| `dungeons.csv` | 스테이지·도전 | 1,910 | 12,155 |
| `regions.csv` | 지역·지도 | 2,229 | 16,199 |
| `factions.csv` | 세력·진영 | 8 | 44 |
| `items.csv` | 아이템·재료 | 8,384 | 54,484 |
| `monsters.csv` | 몬스터·생물 | 685 | 4,529 |
| `npcs.csv` | NPC·화자 | 14,172 | 63,418 |
| `achievements.csv` | 업적 | 2,563 | 22,169 |
| `activities.csv` | 이벤트·콘텐츠 | 9,531 | 63,608 |
| `buffs.csv` | 버프·효과 | 270 | 2,034 |
| `voice-lines.csv` | 캐릭터 음성 | 7,374 | 31,923 |
| `archives.csv` | 기록·서적 | 839 | 6,563 |
| `terms.csv` | 용어·도감 | 1,672 | 12,423 |
| `system.csv` | 시스템 텍스트 | 9,756 | 65,835 |
| `ui.csv` | UI 텍스트 | 13,866 | 78,159 |
| `tutorials.csv` | 튜토리얼 | 6,253 | 31,905 |
| `story.csv` | 스토리 | 29,841 | 102,395 |
| `other.csv` | 기타 | 1,892 | 13,335 |
| **합계** | **23 개 분류** | **123,230** | **646,888** |

“용어 수”는 중복을 제거한 용어 개수(1개 용어 = 게임 내 텍스트 키 1개)이며 `tools/_counts.json`의 `concepts` 필드 값입니다. **전체 데이터베이스가 같은 값을 공유하며 대상 언어와 무관합니다.** “대역 행”은 이 디렉터리에 있는 해당 분류 CSV의 실제 데이터 행 수입니다. 같은 텍스트가 여러 분류에 속할 수 있으므로 분류별 행 수의 합계는 중복 제거된 용어 수보다 큽니다.

## 설명

- **번역 출처**: `target` 열은 게임 자체의 현지화 텍스트를 그대로 수록한 것입니다([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data)의 `Textmaps/<lang>/multi_text/MultiText.json`, 게임 3.6.0. 일부 키는 [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData)의 `TextMap/<lang>/MultiText.json`, 게임 3.1.0으로 보완). 공식 게임 내 표기이며 2차 번역이 아닙니다.
- **정렬 방식**: 게임 텍스트 키(예: `RoleInfo_1402_Name`)로 대응합니다. 같은 키의 다른 언어 표기가 이 디렉터리의 `target`에 대한 `source` 행이 됩니다.
- **언어 태그**: `tgt_lng`는 이 디렉터리의 언어 코드로 고정되며 디렉터리 이름과 일치합니다.
- **인코딩**: 모든 CSV는 **UTF-8(BOM 포함)**, **CRLF** 줄바꿈, 첫 행은 헤더입니다. 쉼표나 따옴표가 있는 필드는 RFC 4180에 따라 이스케이프되어 있어 Excel에서 바로 열 수 있습니다.
- **알려진 제한**: 문장 단위 스토리 대사(언어당 약 17만 행)는 기본적으로 수록하지 않습니다. 필요하면 `--with-dialogue` 옵션으로 추가 생성할 수 있으며, 방법은 `../README.md`를 참조하십시오. 지나치게 긴 텍스트는 `tools/wuwa_config.py`의 `MAX_LEN`에 따라 분류별로 잘립니다. `ru-RU`, `id-ID`, `vi-VN`은 상위 저장소에서 빈 자리표시자라 미수록이며, `it-IT`와 `tr-TR`은 게임이 지원하는 텍스트 언어가 아닙니다.

## 면책 조항

이 디렉터리는 개인이 정리·관리하는 **비공식** 번역 용어집으로, 개인 학습·연구 및 AI 번역 소프트웨어(Immersive Translate 등을 포함하되 이에 한정하지 않음)의 용어 매칭을 돕기 위한 용도로만 사용됩니다. 본 용어집은 관련 게임의 개발사·퍼블리셔·유통사·운영사·권리자와 어떠한 종속·허가·협력·대리·공식 대표 관계도 없습니다. 수록된 번역은 공식 입장을 대표하지 않으며 항상 정확하거나 완전하다거나 게임 최신 버전과 일치한다고 보장할 수 없고, **어떤 게임의 공식 용어집이나 공식 현지화 파일로도 간주되어서는 안 됩니다**. 게임 이름·캐릭터 이름·고유명사·상표 등 지식재산권은 각 권리자에게 있으며 본 프로젝트는 이에 대한 권리를 주장하지 않습니다. 권리자가 부적절하다고 판단하는 경우 GitHub Issues / Pull Request로 연락해 주시면 확인 후 수정 또는 삭제하겠습니다. 전체 조항은 저장소 루트의 `README.md` / `README_EN.md` / `README_JP.md`를 참조하십시오.
