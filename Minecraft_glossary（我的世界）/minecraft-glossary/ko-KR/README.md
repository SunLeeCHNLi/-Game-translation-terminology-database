# Minecraft 용어집（我的世界）— 한국어（`ko-KR`）

[← 게임 전체 안내로 돌아가기](../../README.md) · [zh-CN](README_zh-CN.md)

이 디렉터리는 **한국어(`ko-KR`)를 대상 언어**로 하는 Minecraft 용어집입니다. **34**개의 분류별 CSV에 **7,784**개의 표제어(`target` 열 기준 중복 제거)와 **101,279**행의 대조가 담겨 있습니다. `tgt_lng` 열은 항상 `ko-KR`이고, `source`는 같은 표제어를 쓴 **나머지 13개 언어 가운데 하나**, `target`은 한국어 표기입니다. 파일은 **분류**별로 나뉘어 있고(분류당 CSV 하나), 시스템·텍스트 분류는 `extra-` 하위 폴더에 모아 두었습니다.

## 파일

- `blocks（블록）.csv`, `items（아이템）.csv`, `entities（개체）.csv`, `biomes（생물 군계）.csv`, `enchantments（마법 부여）.csv`, `effects（상태 효과）.csv`, `instruments（악기）.csv`, `materials（갑옷 장식 재료）.csv`, `paintings（그림）.csv`, `attributes（속성）.csv`, `item-groups（아이템 그룹）.csv`, `jukebox-songs（주크박스 곡）.csv`, `trim-patterns（갑옷 장식 문양）.csv`, `colors（색상）.csv`, `statistics（통계）.csv`, `maps（지도）.csv`, `music（음악）.csv`, `sound-categories（사운드 분류）.csv`, `game-modes（게임 모드）.csv` — 주요 분류 파일 19개
- `extra-subtitles（자막）.csv`, `extra-death-messages（사망 메시지）.csv`, `extra-advancement-titles（발전 과제 제목）.csv`, `extra-advancement-descriptions（발전 과제 설명）.csv`, `extra-gamerules（게임 규칙）.csv`, `extra-commands（명령어와 인수）.csv`, `extra-gui（인터페이스 텍스트）.csv`, `extra-options（설정과 키）.csv`, `extra-multiplayer（멀티플레이）.csv`, `extra-realms（Realms）.csv`, `extra-world-management（세계 관리）.csv`, `extra-resource-packs（리소스 팩과 데이터 팩）.csv`, `extra-telemetry（텔레메트리）.csv`, `extra-dev-tools（개발·테스트 도구）.csv`, `extra-misc（기타）.csv` — `extra-` 시스템·텍스트 분류 파일 15개

모두 **34개의 CSV 파일**이며, 형식은 동일한 3열입니다:

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | 균형 잡힌 식단 | ko-KR |
| A cidade no fim do jogo | 게임의 끝에서 만난 도시 | ko-KR |

디렉터리 구조:

```text
ko-KR/
├── blocks（블록）.csv
├── items（아이템）.csv
├── entities（개체）.csv
├── biomes（생물 군계）.csv
├── enchantments（마법 부여）.csv
├── effects（상태 효과）.csv
├── instruments（악기）.csv
├── materials（갑옷 장식 재료）.csv
├── paintings（그림）.csv
├── attributes（속성）.csv
├── item-groups（아이템 그룹）.csv
├── jukebox-songs（주크박스 곡）.csv
├── trim-patterns（갑옷 장식 문양）.csv
├── colors（색상）.csv
├── statistics（통계）.csv
├── maps（지도）.csv
├── music（음악）.csv
├── sound-categories（사운드 분류）.csv
├── game-modes（게임 모드）.csv
└── extra-  # 시스템·텍스트 분류
    ├── subtitles.csv
    ├── death-messages.csv
    ├── advancement-titles.csv
    ├── advancement-descriptions.csv
    ├── gamerules.csv
    ├── commands.csv
    ├── gui.csv
    ├── options.csv
    ├── multiplayer.csv
    ├── realms.csv
    ├── world-management.csv
    ├── resource-packs.csv
    ├── telemetry.csv
    ├── dev-tools.csv
    └── misc.csv
```

## 분류 및 개수

「표제어 수」는 해당 분류에 배정된 **공식 언어 파일의 이름 객체 수**(언어 파일의 키, 이 언어에서 번역되지 않은 항목 포함)입니다. 모든 언어 폴더에서 같은 값이며 `tools/glossary_counts.json`에서 가져오고, 34개 분류 합계는 8,559 `entries`입니다. 「대조 행 수」는 **이 폴더**의 해당 파일에 실제로 들어 있는 데이터 행 수입니다. 두 값은 정의가 다르므로 혼동하지 마십시오.

### 주요 분류(게임 콘텐츠)

| 분류 | 주제 | 표제어 수 | 대조 행 수 |
| --- | --- | ---: | ---: |
| `blocks（블록）.csv` | 블록 | 1,975 | 25,426 |
| `items（아이템）.csv` | 아이템 | 803 | 9,061 |
| `entities（개체）.csv` | 엔티티 | 219 | 2,582 |
| `biomes（생물 군계）.csv` | 생물 군계 | 67 | 835 |
| `enchantments（마법 부여）.csv` | 마법 부여 | 54 | 553 |
| `effects（상태 효과）.csv` | 상태 효과 | 42 | 514 |
| `instruments（악기）.csv` | 악기 | 8 | 98 |
| `materials（갑옷 장식 재료）.csv` | 갑옷 장식 재료 | 11 | 143 |
| `paintings（그림）.csv` | 그림 | 104 | 315 |
| `attributes（속성）.csv` | 속성 | 83 | 565 |
| `item-groups（아이템 그룹）.csv` | 아이템 그룹 | 16 | 198 |
| `jukebox-songs（주크박스 곡）.csv` | 주크박스 곡 | 22 | 42 |
| `trim-patterns（갑옷 장식 문양）.csv` | 갑옷 장식 무늬 | 18 | 234 |
| `colors（색상）.csv` | 색상 | 16 | 184 |
| `statistics（통계）.csv` | 통계 | 88 | 1,143 |
| `maps（지도）.csv` | 지도 | 33 | 422 |
| `music（음악）.csv` | 음악 | 70 | 192 |
| `sound-categories（사운드 분류）.csv` | 소리 분류 | 11 | 133 |
| `game-modes（게임 모드）.csv` | 게임 모드 | 6 | 77 |
| **소계** | 19개 파일 | **3,646** | **42,717** |

### `extra-` 분류(시스템·텍스트)

| 분류 | 주제 | 표제어 수 | 대조 행 수 |
| --- | --- | ---: | ---: |
| `extra-subtitles（자막）.csv` | 자막 | 1,023 | 12,412 |
| `extra-death-messages（사망 메시지）.csv` | 사망 메시지 | 106 | 1,352 |
| `extra-advancement-titles（발전 과제 제목）.csv` | 발전 과제 제목 | 127 | 1,603 |
| `extra-advancement-descriptions（발전 과제 설명）.csv` | 발전 과제 설명 | 127 | 1,641 |
| `extra-gamerules（게임 규칙）.csv` | 게임 규칙 | 117 | 1,490 |
| `extra-commands（명령어와 인수）.csv` | 명령어와 인수 | 856 | 10,733 |
| `extra-gui（인터페이스 텍스트）.csv` | 인터페이스 텍스트 | 581 | 6,637 |
| `extra-options（설정과 키）.csv` | 설정 및 키 | 754 | 8,163 |
| `extra-multiplayer（멀티플레이）.csv` | 멀티플레이 | 173 | 2,015 |
| `extra-realms（Realms）.csv` | Realms | 426 | 4,970 |
| `extra-world-management（세계 관리）.csv` | 월드 관리 | 294 | 3,569 |
| `extra-resource-packs（리소스 팩과 데이터 팩）.csv` | 리소스 팩과 데이터 팩 | 62 | 761 |
| `extra-telemetry（텔레메트리）.csv` | 원격 측정 | 70 | 897 |
| `extra-dev-tools（개발·테스트 도구）.csv` | 개발 및 테스트 도구 | 144 | 1,803 |
| `extra-misc（기타）.csv` | 기타 | 53 | 516 |
| **소계** | 15개 파일 | **4,913** | **58,562** |

**이 디렉터리 합계: 34개 파일, `target` 열 기준 중복 제거 표제어 7,784개, 대조 101,279행.**

## 설명

- **번역 출처와 정렬 방식.** 모든 텍스트는 **Minecraft: Java Edition 공식 언어 파일**(미러 [misode/mcmeta](https://github.com/misode/mcmeta), `assets` 브랜치, 경로 `assets/minecraft/lang/<locale>.json`, 이 언어는 `ko_kr.json`)에서 가져왔습니다. 즉 **공식 현지화**이며 2차 번역이나 기계 번역이 아닙니다. 정렬은 언어 파일의 키 단위로 이루어지며, 같은 표제어를 *다른* 언어마다 한 행씩 출력하므로 행 수가 표제어 수보다 훨씬 많습니다.
- **언어 태그.** 이 폴더의 `tgt_lng`는 항상 `ko-KR`이며 대상 언어를 뜻합니다. `source`는 나머지 13개 언어 가운데 어느 것이든 될 수 있습니다: `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`.
- **인코딩.** 모든 CSV는 **UTF-8(BOM 포함)**, 줄 바꿈은 **CRLF**, 첫 줄은 머리글입니다. 쉼표나 따옴표가 들어 있는 필드는 RFC 4180에 따라 이스케이프했습니다. Excel에서 바로 열 수 있으며, 이 README 자체는 UTF-8(BOM 없음)입니다.
- **알려진 제한.** 언어마다 행 수가 조금씩 다른 이유는, 어떤 언어에 번역이 없거나 표기가 대상 언어와 같을 때 그 표제어를 출력하지 않기 때문입니다. 대조 행 수와 표제어 수는 같은 것이 아닙니다. 34개 분류의 `entries` 합계는 8,559이며, 이는 공식 언어 파일에서 각 분류에 배정된 이름 객체 수(이 언어에서 번역되지 않은 항목 포함)입니다. 이 폴더의 `target` 열 기준 중복 제거 값은 7,784로 정의가 다릅니다. 전체 정의는 게임 루트의 `../../README.md` “Data Overview” 섹션에 있습니다. 같은 표기가 여러 분류에 나타날 수 있고, 용어는 공식 현지화를 따릅니다(번역되지 않은 이름은 그대로 유지).
- **보조 용어집.** 옆 폴더 `../../minecraft-glossary-supplement/`에는 Minecraft 위키 표준 번역명(중국어 간체·번체만)이 들어 있으며, 이 용어집과 함께 사용할 수 있습니다.
- **재생성.** 게임 루트에서 `python tools/build_glossary.py`를 실행하면 공식 언어 파일로 이 용어집을 다시 만들 수 있습니다(스크립트는 `mcmeta_lang/<locale>.json`이 있는 외부 자료 폴더를 읽고 `minecraft-glossary/`에 출력합니다). `python tools/verify_output.py`는 모든 행 수를 `tools/glossary_counts.json`과 대조하고, `python tools/make_readme.py`는 각 라이브러리의 README를 다시 생성합니다.

## 면책 조항

이 폴더는 개인이 정리·유지하는 **비공식** 번역 용어 데이터베이스이며, 개인 학습·연구와 AI 번역 소프트웨어(Immersive Translate를 포함하되 이에 한정하지 않음)의 용어 일치 보조에만 사용하기 위한 것입니다. Minecraft의 개발사, 배급사, 유통사, 운영사, 권리자와 어떠한 종속·허락·협력·대리·공식 대표 관계도 없습니다. 수록된 번역명은 공식 입장을 나타내지 않으며, 항상 정확하거나 완전하거나 현재 게임 버전과 일치한다고 보증하지 않고, **어떤 게임의 공식 용어집이나 공식 현지화 파일로 간주되어서는 안 됩니다**.

게임 이름, 캐릭터 이름, 고유 명사, 상표 등 지식 재산권은 각 권리자에게 있으며, 이 프로젝트는 이에 대한 어떠한 권리도 주장하지 않습니다. 이 프로젝트와 그로부터 만들어진 번역을 사용하면서 발생하는 모든 책임은 사용자에게 있습니다. 권리자가 내용이 부적절하다고 판단하면 GitHub Issues / Pull Request로 알려 주시기 바랍니다. 확인 후 수정하거나 삭제하겠습니다.

전체 조항은 저장소 루트의 `README.md` / `README_EN.md` / `README_JP.md`에 있습니다.

---

**Game-translation-terminology-database는 독립적인 개인 프로젝트이며, 이 게임과 그 개발사·배급사·유통사·권리자와 어떠한 소속·허락·협력·대리 관계도 없습니다.**
