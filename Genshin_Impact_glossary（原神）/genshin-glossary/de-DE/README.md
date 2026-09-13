# Genshin-Impact-Glossar（原神）— Deutsch（`de-DE`）

[← Zurück zur Spielübersicht](../../README.md)

Dieses Verzeichnis ist der Hauptglossar-Teil der Genshin-Impact-Terminologiesammlung **mit `de-DE` als Zielsprache**: insgesamt **8,186** deduplizierte Begriffe und **89,362** Parallelzeilen — davon **63,172** Zeilen in den 17 Hauptkategorien und **26,190** Zeilen in den 10 TCG-Unterkategorien. In allen 27 CSV-Dateien ist `tgt_lng` fest auf `de-DE` gesetzt, `source` enthält die Schreibweise einer der übrigen 13 Sprachen und `target` den Namen in dieser Zielsprache.

## Dateien

Dieses Sprachverzeichnis enthält **27 CSV-Dateien** auf zwei Ebenen:

- **17 Hauptkategorien** (direkt im Verzeichnis):
  `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv`
- **10 TCG-Unterkategorien** (im Unterordner `TCG/`):
  `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv`

Jede Datei hat genau drei Spalten:

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Aether | Leer | de-DE |

`source` = Bezeichnung desselben Spielobjekts in einer der übrigen 13 Sprachen, `target` = Name in der Zielsprache dieses Verzeichnisses, `tgt_lng` = Sprachkennung der Zieldatei (hier immer `de-DE`). Die Dateien lassen sich direkt als Terminologiedatenbank in CAT-Werkzeuge (Trados, memoQ, Phrase …) oder in Terminerweiterungen wie Immersive Translate importieren.

## Kategorien und Anzahl

| Kategorie | Thema | Begriffe | Zeilen |
| --- | --- | ---: | ---: |
| `characters.csv` | Charaktere | 122 | 577 |
| `talents.csv` | Talente | 125 | 632 |
| `constellations.csv` | Konstellationen | 125 | 632 |
| `weapons.csv` | Waffen | 249 | 2,823 |
| `materials.csv` | Materialien | 919 | 10,636 |
| `foods.csv` | Speisen | 398 | 4,541 |
| `crafts.csv` | Handwerksmaterialien | 295 | 3,522 |
| `artifacts.csv` | Artefakte | 63 | 727 |
| `domains.csv` | Domänen | 284 | 3,636 |
| `enemies.csv` | Gegner | 346 | 4,103 |
| `animals.csv` | Tiere | 223 | 2,647 |
| `outfits.csv` | Kostüme | 150 | 1,869 |
| `windgliders.csv` | Windgleiter | 18 | 211 |
| `namecards.csv` | Namenskarten | 289 | 3,606 |
| `geographies.csv` | Orts- und Gebietsnamen | 268 | 3,389 |
| `achievements.csv` | Erfolge | 1,548 | 19,464 |
| `adventureranks.csv` | Abenteurerstufen-Texte | 21 | 157 |
| `TCG/action-cards.csv` | Aktionskarten | 927 | 9,530 |
| `TCG/character-cards.csv` | Charakterkarten | 149 | 929 |
| `TCG/enemy-cards.csv` | Gegnerkarten | 134 | 1,114 |
| `TCG/summons.csv` | Beschwörungen | 152 | 1,139 |
| `TCG/status-effects.csv` | Statuseffekte | 1,159 | 11,217 |
| `TCG/keywords.csv` | Schlüsselwörter | 139 | 1,511 |
| `TCG/card-backs.csv` | Kartenrücken | 39 | 407 |
| `TCG/card-boxes.csv` | Kartenboxen | 7 | 32 |
| `TCG/detailed-rules.csv` | Ausführliche Regeln | 11 | 142 |
| `TCG/level-rewards.csv` | Stufenbelohnungen | 26 | 169 |
| **Hauptkategorien (17 Dateien)** | — | **5,443** | **63,172** |
| **TCG (10 Dateien)** | — | **2,743** | **26,190** |
| **Gesamt (27 Dateien)** | — | **8,186** | **89,362** |

## Hinweise

- **Quelle und Ausrichtung**: Die Spalte `target` enthält die in [genshin-db](https://github.com/theBowja/genshin-db) 7.0 hinterlegten **offiziellen lokalisierten** Namen aus dem Spiel — keine Maschinenübersetzung und keine Übersetzung aus zweiter Hand. `source` enthält denselben Spielgegenstand in einer der übrigen 13 Sprachen; ausgerichtet wird über den Namen des Spielobjekts, und Zeilen mit gleichem Namen und gleicher Übersetzung wurden zusammengeführt.
- **Sprachkennung**: Die Spalte `tgt_lng` ist in allen Dateien dieses Verzeichnisses fest auf `de-DE` gesetzt (interner Name in genshin-db: `German`).
- **Kodierung**: Alle CSV-Dateien sind **UTF-8 mit BOM** und **CRLF**; Felder mit Kommas oder Anführungszeichen sind nach RFC 4180 maskiert. Excel öffnet sie per Doppelklick ohne Zeichensalat.
- **Begriffe ≠ Zeilen**: „Begriffe“ ist die **deduplizierte Anzahl der Namenobjekte** je Kategorie (im gesamten Bestand gleich); „Zeilen“ ist die tatsächliche Anzahl der Datenzeilen der CSV-Datei in diesem Verzeichnis. Derselbe Begriff kommt zusätzlich mit jeder der übrigen 13 Sprachen als `source` vor, daher ist die Zeilenzahl ein Vielfaches der Begriffsanzahl; außerdem können Namen in mehreren Kategorien auftauchen.
- **Bekannte Einschränkungen**: Der Datenstand entspricht genshin-db 7.0 (14 Sprachen) und kann hinter der aktuellen Spielversion zurückliegen; einzelne Kategorien haben je Sprache leicht abweichende Zeilenzahlen (z. B. `adventureranks`, `achievements`, `enemies`). Dieses Verzeichnis enthält nur das Hauptglossar; das Zusatzglossar liegt in `../../genshin-glossary-supplement/`, die Übersicht dieses Teilbestands in `../README.md`.

## Haftungsausschluss

Dieses Verzeichnis ist eine **inoffizielle**, privat gepflegte Terminologiesammlung und dient ausschließlich dem persönlichen Lernen, der Recherche und der Unterstützung der Terminübereinstimmung von KI-Übersetzungswerkzeugen (einschließlich, aber nicht beschränkt auf Immersive Translate). Es besteht keine Zugehörigkeit, Genehmigung, Zusammenarbeit, Vertretung oder offizielle Verbindung zu den Entwicklern, Publishern, Vertreibern, Betreibern oder Rechteinhabern der betreffenden Spiele; die hier enthaltenen Übersetzungen geben keine offizielle Position wieder, sind nicht garantiert stets korrekt, vollständig oder mit der aktuellen Spielversion identisch, und **dürfen nicht als offizielles Glossar oder offizielle Lokalisierungsdatei eines Spiels angesehen werden**. Alle Rechte an Spielnamen, Charakternamen, Eigennamen und Marken liegen bei ihren jeweiligen Inhabern, und dieses Projekt erhebt keine Ansprüche auf solche Rechte Dritter. Die Verantwortung für die Nutzung dieses Projekts und der damit erzeugten Übersetzungen liegt ausschließlich beim Nutzer. Vollständige Bedingungen: `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) im Repository-Stammverzeichnis.

---

**Game-translation-terminology-database ist ein unabhängiges Privatprojekt und steht in keiner Verbindung zu den genannten Spielen oder den zugehörigen Unternehmen und Organisationen.**
