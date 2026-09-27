# Wuthering Waves（鸣潮）Terminologiedatenbank — Deutsch（`de-DE`）

[← Zurück zur Spielübersicht](../../README.md) ｜ [← Beschreibung der Unterbibliothek wuwa-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Dieses Verzeichnis ist die Wuthering-Waves-Terminologiedatenbank mit **`de-DE` (Deutsch) als Zielsprache**. Es enthält **123,230** Einträge und **652,349** Vergleichszeilen (die Datenzeilen der 23 CSV-Dateien in diesem Verzeichnis, etwa **63.0 MiB**). Die Spalte `tgt_lng` ist immer `de-DE`, und die Spalte `source` enthält die Schreibweise in jeder der anderen 9 Sprachen (`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ja-JP` (日本語), `ko-KR` (한국어), `fr-FR` (Français), `es-ES` (Español), `pt-BR` (Português), `th-TH` (ภาษาไทย)), sodass sich derselbe Spieltextschlüssel aus jeder dieser Sprachen zuordnen lässt.

## Dateien

Dieses Verzeichnis ist **flach aufgebaut**: die 23 Kategorie-CSVs liegen direkt hier, weitere Unterverzeichnisse gibt es nicht:

- `characters（Charakternamen）.csv` — Charakternamen
- `weapons（Waffennamen）.csv` — Waffennamen
- `echoes（Echoes）.csv` — Echoes
- `skills（Fähigkeiten）.csv` — Fähigkeiten
- `resonant-chains（Resonanzketten）.csv` — Resonanzketten
- `quests（Quests）.csv` — Quests
- `dungeons（Dungeons und Herausforderungen）.csv` — Dungeons und Herausforderungen
- `regions（Regionen und Karte）.csv` — Regionen und Karte
- `factions（Fraktionen und Mächte）.csv` — Fraktionen und Mächte
- `items（Items und Materialien）.csv` — Items und Materialien
- `monsters（Monster und Kreaturen）.csv` — Monster und Kreaturen
- `npcs（NPCs und Sprecher）.csv` — NPCs und Sprecher
- `achievements（Erfolge）.csv` — Erfolge
- `activities（Events und Spielmodi）.csv` — Events und Spielmodi
- `buffs（Buffs und Effekte）.csv` — Buffs und Effekte
- `voice-lines（Charakterstimmen）.csv` — Charakterstimmen
- `archives（Archive und Lesetexte）.csv` — Archive und Lesetexte
- `terms（Begriffe und Lexikon）.csv` — Begriffe und Lexikon
- `system（Systemtexte）.csv` — Systemtexte
- `ui（UI-Texte）.csv` — UI-Texte
- `tutorials（Tutorials）.csv` — Tutorials
- `story（Story-Texte）.csv` — Story-Texte
- `other（Sonstiges）.csv` — Sonstiges

Jede Datei hat genau drei Spalten, `source,target,tgt_lng`, mit einer Kopfzeile: Für die in `tgt_lng` angegebene Zielsprache ist `target` die Übersetzung und `source` die Formulierung in **einer der anderen Sprachen**. Ein Eintrag erscheint daher pro übriger Sprache einmal als `source`-Zeile (doppelte und gleichlautende Zeilen wurden zusammengeführt, die Zeilenzahl ist also nicht das Neunfache der Eintragszahl). Die Dateien lassen sich direkt in CAT-Tools oder Terminologie-Matching-Software wie Immersive Translate importieren.

## Kategorien und Anzahl

| Kategorie | Thema | Einträge | Vergleichszeilen |
| --- | --- | --- | --- |
| `characters（Charakternamen）.csv` | Charakternamen | 1,230 | 5,262 |
| `weapons（Waffennamen）.csv` | Waffennamen | 820 | 3,072 |
| `echoes（Echoes）.csv` | Echoes | 1,000 | 6,215 |
| `skills（Fähigkeiten）.csv` | Fähigkeiten | 5,344 | 31,062 |
| `resonant-chains（Resonanzketten）.csv` | Resonanzketten | 784 | 6,119 |
| `quests（Quests）.csv` | Quests | 2,807 | 14,709 |
| `dungeons（Dungeons und Herausforderungen）.csv` | Dungeons und Herausforderungen | 1,910 | 12,235 |
| `regions（Regionen und Karte）.csv` | Regionen und Karte | 2,229 | 16,216 |
| `factions（Fraktionen und Mächte）.csv` | Fraktionen und Mächte | 8 | 44 |
| `items（Items und Materialien）.csv` | Items und Materialien | 8,384 | 56,133 |
| `monsters（Monster und Kreaturen）.csv` | Monster und Kreaturen | 685 | 4,616 |
| `npcs（NPCs und Sprecher）.csv` | NPCs und Sprecher | 14,172 | 63,159 |
| `achievements（Erfolge）.csv` | Erfolge | 2,563 | 22,187 |
| `activities（Events und Spielmodi）.csv` | Events und Spielmodi | 9,531 | 64,261 |
| `buffs（Buffs und Effekte）.csv` | Buffs und Effekte | 270 | 2,084 |
| `voice-lines（Charakterstimmen）.csv` | Charakterstimmen | 7,374 | 31,807 |
| `archives（Archive und Lesetexte）.csv` | Archive und Lesetexte | 839 | 6,719 |
| `terms（Begriffe und Lexikon）.csv` | Begriffe und Lexikon | 1,672 | 12,501 |
| `system（Systemtexte）.csv` | Systemtexte | 9,756 | 66,344 |
| `ui（UI-Texte）.csv` | UI-Texte | 13,866 | 78,242 |
| `tutorials（Tutorials）.csv` | Tutorials | 6,253 | 32,039 |
| `story（Story-Texte）.csv` | Story-Texte | 29,841 | 104,033 |
| `other（Sonstiges）.csv` | Sonstiges | 1,892 | 13,290 |
| **Gesamt** | **23 Kategorien** | **123,230** | **652,349** |

„Einträge“ ist die Anzahl der deduplizierten Einträge (ein Eintrag = ein Spiel-Textschlüssel); der Wert stammt aus dem Feld `concepts` in `tools/_counts.json` und ist **für die gesamte Datenbank identisch und unabhängig von der Zielsprache**. „Vergleichszeilen“ ist die tatsächliche Anzahl der Datenzeilen in der CSV dieser Kategorie in diesem Verzeichnis. Derselbe Text kann zu mehreren Kategorien gehören, daher ergibt die Summe der Kategoriezeilen mehr als die deduplizierte Eintragszahl.

## Hinweise

- **Herkunft der Übersetzungen**: Die Spalte `target` stammt unverändert aus den Lokalisierungsdateien des Spiels selbst ([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data), `Textmaps/<lang>/multi_text/MultiText.json`, Spiel 3.6.0; einzelne Schlüssel wurden aus [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData), `TextMap/<lang>/MultiText.json`, Spiel 3.1.0 ergänzt). Es sind die offiziellen Begriffe aus dem Spiel, keine Zweitübersetzung.
- **Zuordnung**: Die Zeilen werden über den Spiel-Textschlüssel (z. B. `RoleInfo_1402_Name`) einander zugeordnet – derselbe Schlüssel in einer anderen Sprache wird zur `source`-Zeile des `target` in diesem Verzeichnis.
- **Sprachkennung**: `tgt_lng` ist auf den Sprachcode dieses Verzeichnisses festgelegt und stimmt mit dem Verzeichnisnamen überein.
- **Kodierung**: Alle CSV-Dateien sind **UTF-8 mit BOM**, verwenden **CRLF**-Zeilenenden und eine Kopfzeile; Felder mit Kommas oder Anführungszeichen sind nach RFC 4180 maskiert, sodass die Dateien direkt in Excel geöffnet werden können.
- **Bekannte Einschränkungen**: Satzweise Story-Dialoge (etwa 170.000 Zeilen pro Sprache) sind standardmäßig nicht enthalten – wie sie mit der Option `--with-dialogue` ergänzt werden, steht in `../README.md`. Zu lange Texte werden je Kategorie über `MAX_LEN` in `tools/wuwa_config.py` gekürzt. `ru-RU`, `id-ID` und `vi-VN` sind upstream leere Platzhalter und fehlen daher; `it-IT` und `tr-TR` sind keine vom Spiel unterstützten Textsprachen.

## Haftungsausschluss

Dieses Verzeichnis ist eine privat zusammengestellte und gepflegte **inoffizielle** Terminologiesammlung und dient ausschließlich dem persönlichen Lernen, der Forschung und dem Terminabgleich in KI-Übersetzungsprogrammen (einschließlich, aber nicht beschränkt auf Immersive Translate). Es besteht keine Unterstellungs-, Lizenz-, Kooperations-, Vertretungs- oder offizielle Repräsentationsbeziehung zu Entwicklern, Publishern, Vertrieben, Betreibern oder Rechteinhabern der betreffenden Spiele; die enthaltenen Übersetzungen geben keine offizielle Position wieder, sind nicht garantiert richtig, vollständig oder mit der aktuellen Spielversion identisch und **dürfen nicht als offizielles Glossar oder offizielle Lokalisierungsdatei eines Spiels angesehen werden**. Spielnamen, Charakternamen, Eigennamen und Marken gehören ihren jeweiligen Rechteinhabern, und dieses Projekt erhebt keine Ansprüche darauf. Sind Rechteinhaber mit Inhalten nicht einverstanden, genügt ein Hinweis über GitHub Issues / Pull Requests; die Inhalte werden geprüft und geändert oder entfernt. Vollständige Bedingungen stehen in `README.md` / `README_EN.md` / `README_JP.md` im Repository-Stammverzeichnis.
