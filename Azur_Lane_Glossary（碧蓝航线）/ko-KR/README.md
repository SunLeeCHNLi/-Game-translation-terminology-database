# 아주르 레인 용어집 — 한국어(`ko-KR`)

[← 게임 전체 설명으로 돌아가기](../README.md)

이 디렉터리는 **한국어(`ko-KR`)를 대상 언어로 하는** 《아주르 레인》(Azur Lane) 용어집입니다.
`target` 열은 항상 한국어 표기이고, `source` 열에는 중국어 간체·영어·번체 중국어·일본어 표기가 들어갑니다.
**CSV 6개, 대조 행 15 511행**을 수록했으며, 그중 3개 주 표는 **7 709행 / 중복 제거 기준 850 + 850 + 165개 표제어**입니다.
한국어 함선 이름은 KR 서버 클라이언트 설정에서 직접 추출한 **공식 현지화 문구**이며,
**기계 번역이 아닙니다**.

## 파일

- `azur_lane_glossary.csv` — `source,target,tgt_lng` 3열, 3481행. 함선 이름(표준명 표)이며 CAT·용어 관리 도구에 바로 가져올 수 있습니다
- `azur_lane_glossary_detailed.csv` — 3525행. `src_lng,ship_id,ship_type_zh,ship_type_en,nation_zh,nation_en,variant,zh_CN_form,zh_CN_standard,zh_CN_harmonised,same_source_alternatives` 추가
- `azur_lane_ship_character_glossary.csv` — `source,target,tgt_lng` 3열, 3769행. `target`은 한국어 함선 이름이고 `source`에는 중국어 간체판의 실제 표시명(조화명 포함)이 들어갑니다
- `azur_lane_ship_character_glossary_detailed.csv` — 3818행. 추가 열은 위와 같습니다
- `azur_lane_terms.csv` — `source,target,tgt_lng` 3열, 459행. 항해·군사·게임 용어
- `azur_lane_terms_detailed.csv` — 459행. `src_lng,category,category_zh,same_source_alternatives` 추가

같은 위치의 `by_language/`에는 출처 언어별로 나눈 함선 하위 표(`target`은 항상 중국어 간체)가,
`sources/`에는 조화명 대조에 사용하는 모에걸백과 『아주르 레인/명칭 대조표』 수집 결과가 있습니다.

## 분류와 개수

| 파일 | 대조 행 | 표제어 수(`target` 중복 제거) |
| --- | --- | --- |
| `azur_lane_glossary.csv` | 3481 | 850 |
| `azur_lane_glossary_detailed.csv` | 3525 | 850 |
| `azur_lane_ship_character_glossary.csv` | 3769 | 850 |
| `azur_lane_ship_character_glossary_detailed.csv` | 3818 | 850 |
| `azur_lane_terms.csv` | 459 | 165 |
| `azur_lane_terms_detailed.csv` | 459 | 165 |

함선 파생형(`azur_lane_ship_character_glossary_detailed.csv`의 `variant` 열 기준):

| 파생형 | 함선 수(`ship_id` 중복 제거) | 대조 행 |
| --- | --- | --- |
| 일반 함선(파생 태그 없음) | 770 | 3398 |
| META | 58 | 276 |
| μ장비 | 19 | 101 |
| II형 | 10 | 43 |
| **합계** | **857** | **3818** |

(같은 표의 `target`을 중복 제거하면 **850**개입니다. 일부 함선이 서로 다른 id에서 같은 한국어 표시명을 공유하기 때문입니다.)

용어 5개 분류(`azur_lane_terms_detailed.csv`의 `category` 열 기준):

| `category` | 주제 | 표제어 수 | 대조 행 |
| --- | --- | --- | --- |
| `hull_type` | 함종 | 31 | 97 |
| `naval_term` | 항해·군사 용어 | 72 | 198 |
| `navy_prefix` | 진영·함선 접두어 | 24 | 59 |
| `rank` | 계급 | 14 | 44 |
| `game_term` | 게임 용어 | 24 | 61 |
| **합계** | — | **165** | **459** |

## 설명

- **번역 출처와 정렬 방식**: 함선 이름은 공식 CN / EN / JP / KR / TW 서버 클라이언트 설정에서 가져왔습니다.
  함선 동일성은 `ship_skin_template.json`의 `ship_group`으로 정규화하고, 적·NPC 복제본은
  `ship_data_template.json`으로 걸러냅니다. 용어 표는 사람이 정리해 각 서버 설정과 한 건씩 대조했습니다.
  이 디렉터리의 주 표는 하나의 소스 문자열에 번역을 하나만 남기며, 여러 뜻이 있는 경우
  **함선 id가 가장 작은 것**을 채택하고 가능한 모든 표기를 상세 표의 `same_source_alternatives` 열에 기록합니다.
  예를 들어 한국어 `대령`은 「해군 대령」과 「대좌」 두 개념에 대응하며, 첫 번째 개념이 주 표에 남습니다.
- **언어 태그**: 이 디렉터리의 모든 CSV에서 `tgt_lng`는 `ko-KR`로 고정됩니다. 상세 표의 `src_lng`는
  `zh-CN` / `en-US` / `zh-TW` / `ja-JP`(용어 표는 `zh-CN` / `en-US` / `ja-JP`)입니다.
  참고로 `zh-CN` 디렉터리의 함선 상세 표는 `en` / `ja` / `ko` / `zh-TW` 같은 짧은 태그를 사용하므로
  태그 표기가 디렉터리마다 통일되어 있지 않습니다(번역 내용에는 영향이 없습니다).
  같은 위치의 `by_language/azur_lane_glossary_ko-zh-CN.csv`는 동일한 한국어 소스 문자열을
  중국어 간체를 대상으로 본 뷰입니다.
- **인코딩**: 모든 CSV는 **UTF-8 with BOM + CRLF**이므로 Excel에서 바로 열 수 있습니다. `.md`는 UTF-8(BOM 없음)입니다.
- **알려진 한계**:
  - 함종·진영·게임 내 용어는 KR 서버 설정에서 가져왔고, 나머지 항해·계급 용어는 표준 한국어 대응어입니다.
    게임 내 함종 표시는 약어(구축 / 경순 / …)지만 용어 표는 항상 전체형(구축함 / 경순양함 / …)을 씁니다.
  - EN 서버 설정에서 `皇家方舟·META`의 함선 이름이 `Royal.META`(`Ark` 누락)로 저장되어 있어
    게임 원본 데이터의 문제로 보고 수정하지 않았습니다.
  - 철혈 진영에서 중국어 간체 조화명이 없는 함선 캐릭터는 亚尔薇特(Alvitr, 순양전함, ship_id 404061) 한 명뿐입니다.
  - `azur_lane_ambiguous.csv`와 `azur_lane_combined_ships_and_terms.csv`는 `zh-CN` 디렉터리에만 있으며
    이 디렉터리에는 없습니다.

## 면책 조항

이 디렉터리는 개인이 정리·유지하는 **비공식** 번역 용어 자료집으로, 개인의 학습·연구와 AI 번역
소프트웨어(Immersive Translate를 포함하되 이에 한정하지 않음)의 용어 매칭 보조에만 사용해야 합니다.
**《아주르 레인》의 공식 용어집이나 공식 현지화 파일로 간주해서는 안 됩니다.** 수록된 번역은 공식 입장을
대표하지 않으며 항상 정확·완전하다거나 게임의 현재 버전과 일치한다고 보장하지 않습니다. 게임 이름,
캐릭터 이름, 고유 명사, 상표 등 지식 재산권은 각 권리자에게 있으며 이 저장소는 이에 대해 어떠한
권리도 주장하지 않습니다. 이 프로젝트의 사용으로 발생하는 모든 책임은 사용자 본인에게 있습니다.

전체 조항은 저장소 최상위 `README.md` / `README_EN.md` / `README_JP.md`를 참고하십시오.
