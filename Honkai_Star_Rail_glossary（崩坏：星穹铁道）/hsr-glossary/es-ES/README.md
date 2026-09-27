# Base de terminología de Honkai: Star Rail — Español (`es-ES`)

[← Volver a la descripción del juego](../../README.md) ｜ [← subbiblioteca hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Este directorio contiene la base de terminología de Honkai: Star Rail con **`es-ES` (Español) como idioma de destino**: **26** CSV de categorías y **307,652** filas de correspondencia. La columna `tgt_lng` es siempre `es-ES` y la columna `source` incluye la localización oficial de los demás idiomas.

## Archivos

El directorio es **plano**: los 26 CSV de categorías están directamente aquí.

| Archivo | Categoría | Filas en este idioma |
| --- | --- | ---: |
| `01_character（Personajes y PNJ）.csv` | Characters & NPCs | 2,883 |
| `02_path（Caminos）.csv` | Paths | 206 |
| `03_element（Elementos）.csv` | Elements | 149 |
| `04_skill（Habilidades）.csv` | Skills | 5,147 |
| `05_trace（Rastros）.csv` | Traces | 3,073 |
| `06_eidolon（Eidolones）.csv` | Eidolons | 5,442 |
| `07_light_cone（Conos de luz）.csv` | Light Cones | 3,217 |
| `08_relic（Reliquias）.csv` | Relics | 2,712 |
| `09_item（Objetos）.csv` | Items | 19,704 |
| `10_material（Materiales）.csv` | Materials | 6,090 |
| `11_enemy（Enemigos）.csv` | Enemies | 9,118 |
| `12_location（Lugares）.csv` | Locations | 11,729 |
| `13_faction（Facciones y organizaciones）.csv` | Factions | 365 |
| `14_quest（Misiones）.csv` | Quests | 62,709 |
| `15_stage（Etapas y dominios）.csv` | Stages | 1,991 |
| `16_event（Eventos）.csv` | Events | 14,651 |
| `17_achievement（Logros）.csv` | Achievements | 21,011 |
| `18_simulated_universe（Universo simulado）.csv` | Simulated Universe | 20,076 |
| `19_forgotten_hall（Salón del olvido）.csv` | Forgotten Hall | 9,748 |
| `20_story（Historia）.csv` | Story | 214 |
| `21_world_lore（Trasfondo）.csv` | World Lore | 1,196 |
| `22_book（Libros）.csv` | Books | 11,239 |
| `23_dialogue（Diálogos）.csv` | Dialogue | 60,320 |
| `24_system（Sistema）.csv` | System | 20,801 |
| `25_ui（Interfaz）.csv` | UI | 11,646 |
| `26_other（Otros）.csv` | Other | 2,215 |

## Notas

- Los textos provienen de la localización del cliente (TextMap / ExcelOutput), alineados por la misma clave de texto; no son traducciones de segunda mano.
- Si el idioma de destino no tiene texto para una clave, no se genera ninguna fila ni se rellena con traducción automática.
- Una misma clave puede tener varias formas oficiales según el contexto; se conservan todas.
- Generado con `../../tools/build_hsr_glossary.py`, totalmente reproducible.
