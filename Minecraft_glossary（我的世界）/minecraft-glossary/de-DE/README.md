# Minecraft-Glossar（我的世界）— Deutsch（`de-DE`）

[← Zurück zur Spielübersicht](../../README.md) · [zh-CN](README_zh-CN.md)

Dieses Verzeichnis ist das Minecraft-Terminologieglossar mit **Deutsch (`de-DE`) als Zielsprache**: **7.789** nach `target` entdoppelte Begriffe und **101.431** Vergleichszeilen in **34** CSV-Dateien. Die Spalte `tgt_lng` enthält immer `de-DE`; `source` enthält denselben Begriff in **einer der übrigen 13 Sprachen**, `target` die deutsche Fassung. Die Dateien sind nach **Kategorie** getrennt – eine CSV pro Kategorie –, wobei System- und Textkategorien im Unterordner `extra/` liegen.

## Dateien

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 19 Dateien der Hauptkategorien
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — 15 Dateien der Kategorien in `extra/`

Zusammen **34 CSV-Dateien**. Alle haben dieselben drei Spalten:

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | Ausgewogene Ernährung | de-DE |
| A cidade no fim do jogo | Die Stadt am Ende des Spiels | de-DE |

Verzeichnisstruktur:

```text
de-DE/
├── blocks.csv
├── items.csv
├── entities.csv
├── biomes.csv
├── enchantments.csv
├── effects.csv
├── instruments.csv
├── materials.csv
├── paintings.csv
├── attributes.csv
├── item-groups.csv
├── jukebox-songs.csv
├── trim-patterns.csv
├── colors.csv
├── statistics.csv
├── maps.csv
├── music.csv
├── sound-categories.csv
├── game-modes.csv
└── extra/  # System- und Textkategorien
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

## Kategorien und Anzahl

Die Spalte „Begriffe“ nennt die Anzahl der **Namensobjekte der offiziellen Sprachdateien** (Schlüssel der Sprachdateien, einschließlich der in dieser Sprache nicht übersetzten Einträge), die einer Kategorie zugeordnet sind; sie ist in jedem Sprachordner gleich, stammt aus `tools/glossary_counts.json` und die 34 Kategorien kommen zusammen auf 8.559 `entries`. Die Spalte „Zeilen“ ist die Zeilenzahl, die **dieser Ordner** in der jeweiligen Datei tatsächlich enthält. Beide Zahlen folgen unterschiedlichen Definitionen und dürfen nicht verwechselt werden.

### Hauptkategorien (Spielinhalte)

| Kategorie | Thema | Begriffe | Zeilen |
| --- | --- | ---: | ---: |
| `blocks.csv` | Blöcke | 1.975 | 25.426 |
| `items.csv` | Gegenstände | 803 | 9.066 |
| `entities.csv` | Entitäten | 219 | 2.582 |
| `biomes.csv` | Biome | 67 | 835 |
| `enchantments.csv` | Verzauberungen | 54 | 553 |
| `effects.csv` | Statuseffekte | 42 | 514 |
| `instruments.csv` | Instrumente | 8 | 98 |
| `materials.csv` | Rüstungsbesatz-Materialien | 11 | 143 |
| `paintings.csv` | Gemälde | 104 | 315 |
| `attributes.csv` | Attribute | 83 | 567 |
| `item-groups.csv` | Item-Gruppen | 16 | 197 |
| `jukebox-songs.csv` | Schallplatten-Titel | 22 | 42 |
| `trim-patterns.csv` | Rüstungsbesatz-Muster | 18 | 234 |
| `colors.csv` | Farben | 16 | 184 |
| `statistics.csv` | Statistiken | 88 | 1.143 |
| `maps.csv` | Karten | 33 | 422 |
| `music.csv` | Musikstücke | 70 | 192 |
| `sound-categories.csv` | Sound-Kategorien | 11 | 133 |
| `game-modes.csv` | Spielmodi | 6 | 77 |
| **Zwischensumme** | 19 Dateien | **3.646** | **42.723** |

### Kategorien in `extra/` (System und Text)

| Kategorie | Thema | Begriffe | Zeilen |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | Untertitel | 1.023 | 12.491 |
| `extra/death-messages.csv` | Todesmeldungen | 106 | 1.348 |
| `extra/advancement-titles.csv` | Fortschrittstitel | 127 | 1.603 |
| `extra/advancement-descriptions.csv` | Fortschrittsbeschreibungen | 127 | 1.641 |
| `extra/gamerules.csv` | Spielregeln | 117 | 1.490 |
| `extra/commands.csv` | Befehle und Argumente | 856 | 10.793 |
| `extra/gui.csv` | GUI-Texte | 581 | 6.606 |
| `extra/options.csv` | Optionen und Tastenbelegung | 754 | 8.152 |
| `extra/multiplayer.csv` | Mehrspieler | 173 | 2.019 |
| `extra/realms.csv` | Realms | 426 | 5.010 |
| `extra/world-management.csv` | Weltverwaltung | 294 | 3.570 |
| `extra/resource-packs.csv` | Ressourcen- und Datenpakete | 62 | 761 |
| `extra/telemetry.csv` | Telemetrie | 70 | 897 |
| `extra/dev-tools.csv` | Entwickler- und Testwerkzeuge | 144 | 1.803 |
| `extra/misc.csv` | Sonstiges | 53 | 524 |
| **Zwischensumme** | 15 Dateien | **4.913** | **58.708** |

**Gesamt: 34 Dateien, 7.789 eindeutige Begriffe (nach `target` entdoppelt), 101.431 Vergleichszeilen.**

## Hinweise

- **Herkunft der Übersetzungen und Ausrichtung.** Alle Texte stammen aus den **offiziellen Sprachdateien von Minecraft: Java Edition** (gespiegelt von [misode/mcmeta](https://github.com/misode/mcmeta), Zweig `assets`, Pfad `assets/minecraft/lang/<locale>.json`; für diese Sprache `de_de.json`). Es handelt sich also um **offizielle Lokalisierungen**, nicht um Nach- oder Maschinenübersetzungen. Die Ausrichtung erfolgt über den Schlüssel der Sprachdatei: Jeder Begriff wird einmal pro *anderer* Sprache als Zeile ausgegeben, deshalb ist die Zeilenzahl viel größer als die Begriffsanzahl.
- **Sprachkennungen.** `tgt_lng` ist in diesem Ordner immer `de-DE` und bezeichnet die Zielsprache; `source` kann jede der übrigen 13 Sprachen sein: `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`.
- **Kodierung.** Alle CSV-Dateien sind **UTF-8 mit BOM**, verwenden **CRLF**-Zeilenenden und eine Kopfzeile; Felder mit Kommas oder Anführungszeichen werden nach RFC 4180 maskiert. Excel öffnet sie direkt, ohne die Kodierung umzustellen; diese README selbst ist UTF-8 ohne BOM.
- **Bekannte Einschränkungen.** Die Zeilenzahlen unterscheiden sich leicht zwischen den Sprachen, weil ein Begriff übersprungen wird, wenn eine Sprache keine Übersetzung dafür hat oder wenn die Schreibweise mit der Zielsprache übereinstimmt. „Vergleichszeilen“ und „Begriffe“ sind nicht dasselbe: Die 34 Kategorien kommen zusammen auf 8.559 `entries`; das ist die Anzahl der Namensobjekte der offiziellen Sprachdateien, die diesen Kategorien zugeordnet sind, einschließlich der in dieser Sprache nicht übersetzten Einträge. Die nach `target` entdoppelte Zahl dieses Ordners beträgt 7.789 und folgt einer anderen Definition. Die vollständige Definition steht im Abschnitt «Data Overview» der Datei `../../README.md` im Wurzelverzeichnis des Spiels. Gleichlautende Begriffe können in mehreren Kategorien vorkommen; die Terminologie folgt der offiziellen Lokalisierung, auch dort, wo Namen unübersetzt bleiben.
- **Ergänzendes Glossar.** Der Nachbarordner `../../minecraft-glossary-supplement/` enthält die Standardbezeichnungen des Minecraft-Wikis, allerdings nur für vereinfachtes und traditionelles Chinesisch; er lässt sich mit diesem Glossar zusammen verwenden.
- **Reproduktion.** Im Wurzelverzeichnis des Spiels erzeugt `python tools/build_glossary.py` dieses Glossar aus den offiziellen Sprachdateien neu (das Skript liest ein externes Materialverzeichnis mit `mcmeta_lang/<locale>.json` und schreibt nach `minecraft-glossary/`); `python tools/verify_output.py` prüft jede Zeilenzahl gegen `tools/glossary_counts.json`, und `python tools/make_readme.py` erzeugt die READMEs der Bibliotheken neu.

## Haftungsausschluss

Dieses Verzeichnis ist eine **nicht offizielle**, privat gepflegte Terminologiedatenbank für Übersetzungen. Sie dient ausschließlich dem persönlichen Lernen, der Forschung und dem Terminologieabgleich in KI-Übersetzungswerkzeugen (einschließlich, aber nicht beschränkt auf Immersive Translate). Es besteht keinerlei Unterstellungs-, Lizenz-, Kooperations-, Vermittlungs- oder offizielles Vertretungsverhältnis zu den Entwicklern, Publishern, Vertrieben, Betreibern oder Rechteinhabern von Minecraft; die enthaltenen Bezeichnungen geben keine offizielle Position wieder, es wird nicht zugesichert, dass sie stets korrekt, vollständig oder mit der aktuellen Spielversion übereinstimmend sind, und **sie dürfen nicht als offizielles Glossar oder offizielle Lokalisierungsdatei irgendeines Spiels angesehen werden**.

Spielnamen, Figurennamen, Eigennamen und Marken bleiben Eigentum der jeweiligen Rechteinhaber; dieses Projekt erhebt darauf keine Ansprüche. Die Verantwortung für die Nutzung dieses Projekts und der daraus abgeleiteten Übersetzungen liegt allein beim Nutzer. Rechteinhaber, die Inhalte beanstanden, können sich über GitHub Issues / Pull Request melden; der Maintainer prüft und ändert oder entfernt sie anschließend.

Die vollständigen Bedingungen stehen in `README.md` / `README_EN.md` / `README_JP.md` im Wurzelverzeichnis des Repositories.

---

**Game-translation-terminology-database ist ein unabhängiges Privatprojekt und steht in keiner Zugehörigkeits-, Autorisierungs-, Kooperations- oder Vertretungsbeziehung zu diesem Spiel, seinen Entwicklern, Publishern, Vertrieben oder Rechteinhabern.**
