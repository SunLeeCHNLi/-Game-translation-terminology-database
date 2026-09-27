# Honkai: Star Rail Terminologiedatenbank — Deutsch (`de-DE`)

[← Zurück zur Spielübersicht](../../README.md) ｜ [← hsr-glossary Unterbibliothek](../README.md)

Dieses Verzeichnis enthält die Honkai-Star-Rail-Terminologiedatenbank mit **`de-DE` (Deutsch) als Zielsprache**: **26** Kategorie-CSVs und **307,905** Vergleichszeilen. Die Spalte `tgt_lng` ist immer `de-DE`, die Spalte `source` enthält die offizielle Lokalisierung jeder anderen Sprache.

## Dateien

Das Verzeichnis ist **flach aufgebaut**: die 26 Kategorie-CSVs liegen direkt hier.

| Datei | Kategorie | Zeilen in dieser Sprache |
| --- | --- | ---: |
| `01_character.csv` | Characters & NPCs | 2,910 |
| `02_path.csv` | Paths | 206 |
| `03_element.csv` | Elements | 149 |
| `04_skill.csv` | Skills | 5,136 |
| `05_trace.csv` | Traces | 3,073 |
| `06_eidolon.csv` | Eidolons | 5,463 |
| `07_light_cone.csv` | Light Cones | 3,217 |
| `08_relic.csv` | Relics | 2,712 |
| `09_item.csv` | Items | 19,739 |
| `10_material.csv` | Materials | 6,071 |
| `11_enemy.csv` | Enemies | 9,100 |
| `12_location.csv` | Locations | 11,728 |
| `13_faction.csv` | Factions | 361 |
| `14_quest.csv` | Quests | 61,758 |
| `15_stage.csv` | Stages | 1,987 |
| `16_event.csv` | Events | 14,772 |
| `17_achievement.csv` | Achievements | 21,785 |
| `18_simulated_universe.csv` | Simulated Universe | 20,307 |
| `19_forgotten_hall.csv` | Forgotten Hall | 9,738 |
| `20_story.csv` | Story | 214 |
| `21_world_lore.csv` | World Lore | 1,196 |
| `22_book.csv` | Books | 11,305 |
| `23_dialogue.csv` | Dialogue | 60,353 |
| `24_system.csv` | System | 20,847 |
| `25_ui.csv` | UI | 11,567 |
| `26_other.csv` | Other | 2,211 |

## Hinweise

- Die Zieltexte stammen aus der Client-Lokalisierung (TextMap / ExcelOutput) und sind über denselben Textschlüssel ausgerichtet — keine Zweitübersetzung.
- Fehlt der Zielsprache ein Text, wird kein Eintrag erzeugt und nichts maschinell übersetzt.
- Derselbe Textschlüssel kann je nach Kontext mehrere offizielle Formulierungen haben; alle bleiben erhalten.
- Generiert mit `../../tools/build_hsr_glossary.py`, vollständig reproduzierbar.
