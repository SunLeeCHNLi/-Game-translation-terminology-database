# Base terminologique Honkai: Star Rail — Français (`fr-FR`)

[← Retour à la présentation du jeu](../../README.md) ｜ [← sous-bibliothèque hsr-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Ce répertoire contient la base terminologique Honkai: Star Rail avec **`fr-FR` (Français) comme langue cible** : **26** fichiers CSV catégoriels et **306,045** lignes d’appariement. La colonne `tgt_lng` vaut toujours `fr-FR` et la colonne `source` contient la localisation officielle de chaque autre langue.

## Fichiers

Le répertoire est **plat** : les 26 CSV catégoriels sont directement ici.

| Fichier | Catégorie | Lignes dans cette langue |
| --- | --- | ---: |
| `01_character（Personnages et PNJ）.csv` | Characters & NPCs | 2,894 |
| `02_path（Voies）.csv` | Paths | 206 |
| `03_element（Éléments）.csv` | Elements | 149 |
| `04_skill（Compétences）.csv` | Skills | 5,139 |
| `05_trace（Traces）.csv` | Traces | 3,126 |
| `06_eidolon（Eidolons）.csv` | Eidolons | 5,517 |
| `07_light_cone（Cônes de lumière）.csv` | Light Cones | 3,219 |
| `08_relic（Reliques）.csv` | Relics | 2,712 |
| `09_item（Objets）.csv` | Items | 19,645 |
| `10_material（Matériaux）.csv` | Materials | 6,036 |
| `11_enemy（Ennemis）.csv` | Enemies | 9,157 |
| `12_location（Lieux）.csv` | Locations | 11,713 |
| `13_faction（Factions et organisations）.csv` | Factions | 361 |
| `14_quest（Quêtes）.csv` | Quests | 61,136 |
| `15_stage（Niveaux et domaines）.csv` | Stages | 1,987 |
| `16_event（Événements）.csv` | Events | 14,624 |
| `17_achievement（Succès）.csv` | Achievements | 21,176 |
| `18_simulated_universe（Univers simulé）.csv` | Simulated Universe | 20,352 |
| `19_forgotten_hall（Salle de l’oubli）.csv` | Forgotten Hall | 9,838 |
| `20_story（Histoire）.csv` | Story | 214 |
| `21_world_lore（Univers）.csv` | World Lore | 1,206 |
| `22_book（Livres）.csv` | Books | 11,223 |
| `23_dialogue（Dialogues）.csv` | Dialogue | 60,349 |
| `24_system（Système）.csv` | System | 20,371 |
| `25_ui（Interface）.csv` | UI | 11,491 |
| `26_other（Autres）.csv` | Other | 2,204 |

## Remarques

- Les textes proviennent de la localisation du client (TextMap / ExcelOutput), alignés par la même clé de texte — aucune traduction de seconde main.
- Si la langue cible n’a pas de texte pour une clé, aucune ligne n’est créée et rien n’est traduit automatiquement.
- Une même clé peut avoir plusieurs formulations officielles selon le contexte ; toutes sont conservées.
- Généré par `../../tools/build_hsr_glossary.py`, entièrement reproductible.
