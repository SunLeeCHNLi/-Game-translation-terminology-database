# Base de terminologia de Honkai: Star Rail — Português (`pt-PT`)

[← Voltar à descrição do jogo](../../README.md) ｜ [← sub-biblioteca hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Este diretório contém a base de terminologia de Honkai: Star Rail com **`pt-PT` (Português) como idioma de destino**: **26** CSV de categorias e **311,326** linhas de correspondência. A coluna `tgt_lng` é sempre `pt-PT` e a coluna `source` traz a localização oficial dos restantes idiomas.

## Ficheiros

O diretório é **plano**: os 26 CSV de categorias estão diretamente aqui.

| Ficheiro | Categoria | Linhas neste idioma |
| --- | --- | ---: |
| `01_character（Personagens e NPCs）.csv` | Characters & NPCs | 2,905 |
| `02_path（Caminhos）.csv` | Paths | 206 |
| `03_element（Elementos）.csv` | Elements | 149 |
| `04_skill（Habilidades）.csv` | Skills | 5,211 |
| `05_trace（Vestígios）.csv` | Traces | 3,030 |
| `06_eidolon（Eidolons）.csv` | Eidolons | 5,543 |
| `07_light_cone（Cones de Luz）.csv` | Light Cones | 3,219 |
| `08_relic（Relíquias）.csv` | Relics | 2,719 |
| `09_item（Itens）.csv` | Items | 19,851 |
| `10_material（Materiais）.csv` | Materials | 6,082 |
| `11_enemy（Inimigos）.csv` | Enemies | 9,573 |
| `12_location（Locais）.csv` | Locations | 11,744 |
| `13_faction（Facções e Organizações）.csv` | Factions | 353 |
| `14_quest（Missões）.csv` | Quests | 64,787 |
| `15_stage（Fases e Domínios）.csv` | Stages | 2,013 |
| `16_event（Eventos）.csv` | Events | 14,696 |
| `17_achievement（Conquistas）.csv` | Achievements | 20,993 |
| `18_simulated_universe（Universo Simulado）.csv` | Simulated Universe | 20,670 |
| `19_forgotten_hall（Salão do Esquecimento）.csv` | Forgotten Hall | 9,839 |
| `20_story（História）.csv` | Story | 214 |
| `21_world_lore（Lore do Mundo）.csv` | World Lore | 1,196 |
| `22_book（Livros）.csv` | Books | 11,360 |
| `23_dialogue（Diálogos）.csv` | Dialogue | 60,352 |
| `24_system（Sistema）.csv` | System | 20,891 |
| `25_ui（Interface）.csv` | UI | 11,498 |
| `26_other（Outros）.csv` | Other | 2,232 |

## Notas

- Os textos vêm da localização do cliente (TextMap / ExcelOutput), alinhados pela mesma chave de texto — não é tradução de segunda mão.
- Se o idioma de destino não tiver texto para uma chave, nenhuma linha é criada e nada é traduzido automaticamente.
- A mesma chave pode ter várias formas oficiais conforme o contexto; todas são mantidas.
- Gerado por `../../tools/build_hsr_glossary.py`, totalmente reproduzível.
