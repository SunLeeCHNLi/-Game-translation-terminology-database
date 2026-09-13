# 원신（原神）용어집 — 한국어（`ko-KR`）

[← 게임 전체 설명으로 돌아가기](../../README.md)

이 디렉터리는 Genshin Impact(원신) 용어집 가운데 **`ko-KR`를 대상 언어로 하는** 주 용어집입니다. 중복을 제거한 **8,186**개 용어와 **89,460**개 대역 행(주 분류 17개 파일 **63,180**행, TCG 10개 파일 **26,280**행)을 수록합니다. 27개 CSV 모두 `tgt_lng` 열이 `ko-KR`로 고정되어 있고, `source`에는 나머지 13개 언어 중 하나의 표기, `target`에는 이 대상 언어의 명칭이 들어 있습니다.

## 파일

이 언어 디렉터리에는 두 계층에 걸쳐 **CSV 파일 27개**가 있습니다.

- **주 분류 17개**(이 디렉터리 바로 아래):
  `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv`
- **TCG 하위 분류 10개**(`TCG/` 하위 폴더):
  `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv`

각 파일은 다음 세 개 열로만 구성됩니다.

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Aether | 아이테르 | ko-KR |

`source` = 동일한 게임 오브젝트를 나머지 13개 언어 중 하나로 표기한 것, `target` = 이 디렉터리의 대상 언어 명칭, `tgt_lng` = 대상 파일의 언어 태그(이 디렉터리에서는 항상 `ko-KR`). 이 파일들은 CAT 도구(Trados, memoQ, Phrase 등)나 Immersive Translate 같은 용어 매칭 확장 기능에 용어집으로 바로 가져올 수 있습니다.

## 분류와 개수

| 분류 | 주제 | 용어 수 | 대역 행 |
| --- | --- | ---: | ---: |
| `characters.csv` | 캐릭터 | 122 | 577 |
| `talents.csv` | 특성 | 125 | 632 |
| `constellations.csv` | 별자리 | 125 | 632 |
| `weapons.csv` | 무기 | 249 | 2,823 |
| `materials.csv` | 재료 | 919 | 10,636 |
| `foods.csv` | 음식 | 398 | 4,541 |
| `crafts.csv` | 제작 재료 | 295 | 3,522 |
| `artifacts.csv` | 성유물 | 63 | 727 |
| `domains.csv` | 비경 | 284 | 3,636 |
| `enemies.csv` | 적 | 346 | 4,104 |
| `animals.csv` | 동물 | 223 | 2,647 |
| `outfits.csv` | 의상 | 150 | 1,869 |
| `windgliders.csv` | 바람의 날개 | 18 | 211 |
| `namecards.csv` | 명함 | 289 | 3,606 |
| `geographies.csv` | 지명 | 268 | 3,389 |
| `achievements.csv` | 업적 | 1,548 | 19,461 |
| `adventureranks.csv` | 모험 등급 설명 | 21 | 167 |
| `TCG/action-cards.csv` | 행동 카드 | 927 | 9,636 |
| `TCG/character-cards.csv` | 캐릭터 카드 | 149 | 929 |
| `TCG/enemy-cards.csv` | 적 카드 | 134 | 1,114 |
| `TCG/summons.csv` | 소환물 | 152 | 1,139 |
| `TCG/status-effects.csv` | 상태 효과 | 1,159 | 11,201 |
| `TCG/keywords.csv` | 키워드 | 139 | 1,511 |
| `TCG/card-backs.csv` | 카드 뒷면 | 39 | 407 |
| `TCG/card-boxes.csv` | 카드 상자 | 7 | 32 |
| `TCG/detailed-rules.csv` | 상세 규칙 | 11 | 142 |
| `TCG/level-rewards.csv` | 레벨 보상 | 26 | 169 |
| **주 분류(17개 파일)** | — | **5,443** | **63,180** |
| **TCG(10개 파일)** | — | **2,743** | **26,280** |
| **합계(27개 파일)** | — | **8,186** | **89,460** |

## 설명

- **번역 출처와 정렬 방식**: `target` 열은 [genshin-db](https://github.com/theBowja/genshin-db) 7.0에 수록된 게임 내 **공식 현지화** 명칭이며, 기계 번역이나 재번역이 아닙니다. `source` 열은 동일한 게임 오브젝트를 나머지 13개 언어 중 하나로 표기한 것이고, 정렬 단위는 “게임 내 하나의 명칭 오브젝트”입니다. 이름과 번역이 동일한 중복 행은 병합했습니다.
- **언어 태그**: 이 디렉터리의 모든 파일에서 `tgt_lng` 열은 `ko-KR`로 고정되어 있습니다(genshin-db 내부 이름: `Korean`).
- **인코딩**: 모든 CSV는 **UTF-8(BOM 포함) + CRLF**이며, 쉼표나 따옴표가 포함된 필드는 RFC 4180에 따라 이스케이프했습니다. Excel에서 더블클릭으로 열어도 글자가 깨지지 않습니다.
- **용어 수와 대역 행 수의 차이**: “용어 수”는 분류별 **중복을 제거한 명칭 오브젝트 수**(전체 컬렉션에서 동일)이고, “대역 행”은 이 디렉터리에 있는 해당 CSV의 실제 데이터 행 수입니다. 같은 용어가 나머지 13개 언어 각각을 `source`로 한 행씩 추가로 가지므로 행 수는 용어 수의 몇 배가 됩니다. 같은 이름이 여러 분류에 나타날 수도 있습니다.
- **알려진 제한**: 데이터는 genshin-db 7.0(14개 언어) 기준이며 게임의 현재 버전보다 뒤처질 수 있습니다. 일부 분류는 언어별로 몇 행 차이가 있습니다(예: `adventureranks`, `achievements`, `enemies`). 이 디렉터리는 주 용어집만 담고 있으며, 보충 용어집은 `../../genshin-glossary-supplement/`, 이 부분집합의 개요는 `../README.md`에 있습니다.

## 면책 조항

이 디렉터리는 개인이 정리·관리하는 **비공식** 번역 용어집으로, 개인의 학습·연구 및 AI 번역 소프트웨어(Immersive Translate 등을 포함하되 이에 국한되지 않음)의 용어 매칭 보조만을 목적으로 합니다. 본 용어집은 관련 게임의 개발사·퍼블리셔·유통사·운영사·권리자와 어떠한 소속·허가·협력·대리·공식 대표 관계도 없습니다. 수록된 번역은 공식 입장을 나타내지 않으며 항상 정확하거나 완전하다거나 게임의 현재 버전과 일치한다고 보장하지 않고, **어떤 게임의 공식 용어집이나 공식 현지화 파일로 간주되어서도 안 됩니다**. 게임 이름, 캐릭터 이름, 고유명사, 상표 등 지식재산권은 각 권리자에게 있으며 본 프로젝트는 이러한 제3자 지식재산권에 대해 어떠한 권리도 주장하지 않습니다. 본 프로젝트와 그에 기반해 생성된 번역 결과의 사용으로 발생하는 모든 책임은 사용자 본인에게 있습니다. 전체 조항은 저장소 루트의 `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md))를 참조하세요.

---

**Game-translation-terminology-database는 개인이 운영하는 독립 프로젝트이며, 위에 언급된 어떤 게임 및 관련 기업·단체와도 관계가 없습니다.**
