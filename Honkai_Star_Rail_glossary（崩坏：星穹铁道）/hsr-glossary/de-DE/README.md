# Honkai: Star Rail Terminologiedatenbank — Deutsch (`de-DE`)

[← Zurück zur Spielübersicht](../../README.md) ｜ [← hsr-glossary Unterbibliothek](../README.md) ｜ [简体中文](README_zh-CN.md)

Dieses Verzeichnis enthält die Honkai-Star-Rail-Terminologiedatenbank mit **`de-DE` (Deutsch) als Zielsprache**: **26** Kategorie-CSVs und **307,905** Vergleichszeilen. Die Spalte `tgt_lng` ist immer `de-DE`, die Spalte `source` enthält die offizielle Lokalisierung jeder anderen Sprache.

## Dateien

Das Verzeichnis ist **flach aufgebaut**: die 26 Kategorie-CSVs liegen direkt hier.

| Datei | Kategorie | Zeilen in dieser Sprache |
| --- | --- | ---: |
| `01_character（Charaktere & NPCs）.csv` | Characters & NPCs | 2,910 |
| `02_path（Pfade）.csv` | Paths | 206 |
| `03_element（Elemente）.csv` | Elements | 149 |
| `04_skill（Fähigkeiten）.csv` | Skills | 5,136 |
| `05_trace（Spuren）.csv` | Traces | 3,073 |
| `06_eidolon（Eidolons）.csv` | Eidolons | 5,463 |
| `07_light_cone（Lichtkegel）.csv` | Light Cones | 3,217 |
| `08_relic（Relikte）.csv` | Relics | 2,712 |
| `09_item（Gegenstände）.csv` | Items | 19,739 |
| `10_material（Materialien）.csv` | Materials | 6,071 |
| `11_enemy（Gegner）.csv` | Enemies | 9,100 |
| `12_location（Orte）.csv` | Locations | 11,728 |
| `13_faction（Fraktionen & Organisationen）.csv` | Factions | 361 |
| `14_quest（Aufträge）.csv` | Quests | 61,758 |
| `15_stage（Ebenen & Domänen）.csv` | Stages | 1,987 |
| `16_event（Events）.csv` | Events | 14,772 |
| `17_achievement（Erfolge）.csv` | Achievements | 21,785 |
| `18_simulated_universe（Simulierte Universum）.csv` | Simulated Universe | 20,307 |
| `19_forgotten_hall（Vergessene Halle）.csv` | Forgotten Hall | 9,738 |
| `20_story（Handlung）.csv` | Story | 214 |
| `21_world_lore（Weltwissen）.csv` | World Lore | 1,196 |
| `22_book（Bücher）.csv` | Books | 11,305 |
| `23_dialogue（Dialoge）.csv` | Dialogue | 60,353 |
| `24_system（System）.csv` | System | 20,847 |
| `25_ui（Oberfläche）.csv` | UI | 11,567 |
| `26_other（Sonstiges）.csv` | Other | 2,211 |

## Hinweise

- Die Zieltexte stammen aus der Client-Lokalisierung (TextMap / ExcelOutput) und sind über denselben Textschlüssel ausgerichtet — keine Zweitübersetzung.
- Fehlt der Zielsprache ein Text, wird kein Eintrag erzeugt und nichts maschinell übersetzt.
- Derselbe Textschlüssel kann je nach Kontext mehrere offizielle Formulierungen haben; alle bleiben erhalten.
- Generiert mit `../../tools/build_hsr_glossary.py`, vollständig reproduzierbar.
