# Base de terminologia de Honkai: Star Rail — Português (`pt-PT`)

[← Voltar à descrição do jogo](../../README.md) ｜ [← sub-biblioteca hsr-glossary](../README.md)

Este diretório contém a base de terminologia de Honkai: Star Rail com **`pt-PT` (Português) como idioma de destino**: **26** CSV de categorias e **311,326** linhas de correspondência. A coluna `tgt_lng` é sempre `pt-PT` e a coluna `source` traz a localização oficial dos restantes idiomas.

## Ficheiros

O diretório é **plano**: os 26 CSV de categorias estão diretamente aqui.

| Ficheiro | Categoria | Linhas neste idioma |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,905 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,211 |
| `05_trace.csv` | Traces | 3,030 |
| `06_eidolon.csv` | Eidolons | 5,543 |
| `07_light_cone.csv` | Light Cones | 3,219 |
| `08_relic.csv` | Relics | 2,719 |
| `09_item.csv` | Items | 19,851 |
| `10_material.csv` | Materials | 6,082 |
| `11_enemy.csv` | Enemies | 9,573 |
| `12_location.csv` | Locations | 11,744 |
| `13_faction.csv` | Factions | 353 |
| `14_quest.csv` | Quests | 64,787 |
| `15_stage.csv` | Stages | 2,013 |
| `16_event.csv` | Events | 14,696 |
| `17_achievement.csv` | Achievements | 20,993 |
| `18_simulated_universe.csv` | Simulated Universe | 20,670 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,839 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,196 |
| `22_book.csv` | Books | 11,360 |
| `23_dialogue.csv` | Dialogue | 60,352 |
| `24_system.csv` | System | 20,891 |
| `25_ui.csv` | UI | 11,498 |
| `26_other.csv` | Other | 2,232 |

## Notas

- Os textos vêm da localização do cliente (TextMap / ExcelOutput), alinhados pela mesma chave de texto — não é tradução de segunda mão.
- Se o idioma de destino não tiver texto para uma chave, nenhuma linha é criada e nada é traduzido automaticamente.
- A mesma chave pode ter várias formas oficiais conforme o contexto; todas são mantidas.
- Gerado por `../../tools/build_hsr_glossary.py`, totalmente reproduzível.
