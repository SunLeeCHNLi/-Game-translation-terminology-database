# Base de terminología de Honkai: Star Rail — Español (`es-ES`)

[← Volver a la descripción del juego](../../README.md) ｜ [← subbiblioteca hsr-glossary](../README.md)

Este directorio contiene la base de terminología de Honkai: Star Rail con **`es-ES` (Español) como idioma de destino**: **26** CSV de categorías y **307,652** filas de correspondencia. La columna `tgt_lng` es siempre `es-ES` y la columna `source` incluye la localización oficial de los demás idiomas.

## Archivos

El directorio es **plano**: los 26 CSV de categorías están directamente aquí.

| Archivo | Categoría | Filas en este idioma |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,883 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,147 |
| `05_trace.csv` | Traces | 3,073 |
| `06_eidolon.csv` | Eidolons | 5,442 |
| `07_light_cone.csv` | Light Cones | 3,217 |
| `08_relic.csv` | Relics | 2,712 |
| `09_item.csv` | Items | 19,704 |
| `10_material.csv` | Materials | 6,090 |
| `11_enemy.csv` | Enemies | 9,118 |
| `12_location.csv` | Locations | 11,729 |
| `13_faction.csv` | Factions | 365 |
| `14_quest.csv` | Quests | 62,709 |
| `15_stage.csv` | Stages | 1,991 |
| `16_event.csv` | Events | 14,651 |
| `17_achievement.csv` | Achievements | 21,011 |
| `18_simulated_universe.csv` | Simulated Universe | 20,076 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,748 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,196 |
| `22_book.csv` | Books | 11,239 |
| `23_dialogue.csv` | Dialogue | 60,320 |
| `24_system.csv` | System | 20,801 |
| `25_ui.csv` | UI | 11,646 |
| `26_other.csv` | Other | 2,215 |

## Notas

- Los textos provienen de la localización del cliente (TextMap / ExcelOutput), alineados por la misma clave de texto; no son traducciones de segunda mano.
- Si el idioma de destino no tiene texto para una clave, no se genera ninguna fila ni se rellena con traducción automática.
- Una misma clave puede tener varias formas oficiales según el contexto; se conservan todas.
- Generado con `../../tools/build_hsr_glossary.py`, totalmente reproducible.
