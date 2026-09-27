# Base terminologique Honkai: Star Rail — Français (`fr-FR`)

[← Retour à la présentation du jeu](../../README.md) ｜ [← sous-bibliothèque hsr-glossary](../README.md)

Ce répertoire contient la base terminologique Honkai: Star Rail avec **`fr-FR` (Français) comme langue cible** : **26** fichiers CSV catégoriels et **306,045** lignes d’appariement. La colonne `tgt_lng` vaut toujours `fr-FR` et la colonne `source` contient la localisation officielle de chaque autre langue.

## Fichiers

Le répertoire est **plat** : les 26 CSV catégoriels sont directement ici.

| Fichier | Catégorie | Lignes dans cette langue |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,894 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,139 |
| `05_trace.csv` | Traces | 3,126 |
| `06_eidolon.csv` | Eidolons | 5,517 |
| `07_light_cone.csv` | Light Cones | 3,219 |
| `08_relic.csv` | Relics | 2,712 |
| `09_item.csv` | Items | 19,645 |
| `10_material.csv` | Materials | 6,036 |
| `11_enemy.csv` | Enemies | 9,157 |
| `12_location.csv` | Locations | 11,713 |
| `13_faction.csv` | Factions | 361 |
| `14_quest.csv` | Quests | 61,136 |
| `15_stage.csv` | Stages | 1,987 |
| `16_event.csv` | Events | 14,624 |
| `17_achievement.csv` | Achievements | 21,176 |
| `18_simulated_universe.csv` | Simulated Universe | 20,352 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,838 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,206 |
| `22_book.csv` | Books | 11,223 |
| `23_dialogue.csv` | Dialogue | 60,349 |
| `24_system.csv` | System | 20,371 |
| `25_ui.csv` | UI | 11,491 |
| `26_other.csv` | Other | 2,204 |

## Remarques

- Les textes proviennent de la localisation du client (TextMap / ExcelOutput), alignés par la même clé de texte — aucune traduction de seconde main.
- Si la langue cible n’a pas de texte pour une clé, aucune ligne n’est créée et rien n’est traduit automatiquement.
- Une même clé peut avoir plusieurs formulations officielles selon le contexte ; toutes sont conservées.
- Généré par `../../tools/build_hsr_glossary.py`, entièrement reproductible.
