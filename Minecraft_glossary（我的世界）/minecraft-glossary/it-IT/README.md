# Glossario di Minecraft（我的世界）— Italiano（`it-IT`）

[← Torna alla panoramica del gioco](../../README.md) · [zh-CN](README_zh-CN.md)

Questa cartella è il glossario terminologico di Minecraft con **l'italiano (`it-IT`) come lingua di destinazione**: **7.777** voci deduplicate su `target` e **101.580** righe di confronto in **34** file CSV. La colonna `tgt_lng` è sempre `it-IT`; `source` contiene la stessa voce **in una delle altre 13 lingue** e `target` la forma italiana. I file sono divisi per **categoria**, un CSV per categoria, mentre le categorie di sistema e di testo sono raccolte nella sottocartella `extra/`.

## File

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 19 file delle categorie principali
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — 15 file delle categorie di sistema e testo in `extra/`

In totale **34 file CSV**. Tutti usano le stesse tre colonne:

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | Una dieta equilibrata | it-IT |
| A cidade no fim do jogo | Città al termine del gioco | it-IT |

Struttura delle cartelle:

```text
it-IT/
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
└── extra/  # categorie di sistema e testo
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

## Categorie e conteggi

La colonna «Voci» indica quante **entità denominate dei file di lingua ufficiali** (chiavi dei file di lingua, comprese le voci non tradotte in questa lingua) sono assegnate a una categoria; è quindi identica in ogni cartella di lingua, proviene da `tools/glossary_counts.json` e le 34 categorie totalizzano 8.559 `entries`. La colonna «Righe» è il numero di righe che **questa cartella** contiene davvero in quel file. Sono due cifre con definizioni diverse e non vanno confuse.

### Categorie principali (contenuti di gioco)

| Categoria | Tema | Voci | Righe |
| --- | --- | ---: | ---: |
| `blocks.csv` | Blocchi | 1.975 | 25.426 |
| `items.csv` | Oggetti | 803 | 9.065 |
| `entities.csv` | Entità | 219 | 2.582 |
| `biomes.csv` | Biomi | 67 | 835 |
| `enchantments.csv` | Incantesimi | 54 | 553 |
| `effects.csv` | Effetti di stato | 42 | 514 |
| `instruments.csv` | Strumenti | 8 | 98 |
| `materials.csv` | Materiali per fregi | 11 | 143 |
| `paintings.csv` | Quadri | 104 | 315 |
| `attributes.csv` | Attributi | 83 | 566 |
| `item-groups.csv` | Gruppi di oggetti | 16 | 198 |
| `jukebox-songs.csv` | Brani del giradischi | 22 | 42 |
| `trim-patterns.csv` | Motivi per fregi | 18 | 234 |
| `colors.csv` | Colori | 16 | 184 |
| `statistics.csv` | Statistiche | 88 | 1.143 |
| `maps.csv` | Mappe | 33 | 413 |
| `music.csv` | Brani musicali | 70 | 192 |
| `sound-categories.csv` | Categorie audio | 11 | 133 |
| `game-modes.csv` | Modalità di gioco | 6 | 77 |
| **Subtotale** | 19 file | **3.646** | **42.713** |

### Categorie in `extra/` (sistema e testo)

| Categoria | Tema | Voci | Righe |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | Sottotitoli | 1.023 | 12.602 |
| `extra/death-messages.csv` | Messaggi di morte | 106 | 1.340 |
| `extra/advancement-titles.csv` | Titoli dei progressi | 127 | 1.603 |
| `extra/advancement-descriptions.csv` | Descrizioni dei progressi | 127 | 1.641 |
| `extra/gamerules.csv` | Regole di gioco | 117 | 1.490 |
| `extra/commands.csv` | Comandi e argomenti | 856 | 10.779 |
| `extra/gui.csv` | Testi dell'interfaccia | 581 | 6.614 |
| `extra/options.csv` | Opzioni e tasti | 754 | 8.211 |
| `extra/multiplayer.csv` | Multigiocatore | 173 | 2.025 |
| `extra/realms.csv` | Realms | 426 | 5.022 |
| `extra/world-management.csv` | Gestione dei mondi | 294 | 3.563 |
| `extra/resource-packs.csv` | Pacchetti di risorse e dati | 62 | 761 |
| `extra/telemetry.csv` | Telemetria | 70 | 897 |
| `extra/dev-tools.csv` | Strumenti di sviluppo e test | 144 | 1.803 |
| `extra/misc.csv` | Varie | 53 | 516 |
| **Subtotale** | 15 file | **4.913** | **58.867** |

**Totale di questa cartella: 34 file, 7.777 voci distinte (deduplicate su `target`), 101.580 righe di confronto.**

## Note

- **Origine delle traduzioni e allineamento.** Tutti i testi provengono dai **file di lingua ufficiali di Minecraft: Java Edition** (mirror [misode/mcmeta](https://github.com/misode/mcmeta), ramo `assets`, percorso `assets/minecraft/lang/<locale>.json`; per questa lingua `it_it.json`). Si tratta quindi di **localizzazioni ufficiali**, non di ritraduzioni né di traduzioni automatiche. L'allineamento avviene tramite la chiave del file di lingua: ogni voce viene emessa una volta per ciascuna *altra* lingua, per cui il numero di righe è molto maggiore di quello delle voci.
- **Etichette di lingua.** In questa cartella `tgt_lng` è sempre `it-IT` e indica la lingua di destinazione; `source` può essere una qualsiasi delle altre 13 lingue: `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `tr-TR`, `th-TH`, `vi-VN`.
- **Codifica.** Tutti i CSV sono in **UTF-8 con BOM**, con fine riga **CRLF** e una riga di intestazione; i campi che contengono virgole o virgolette sono protetti secondo la RFC 4180. Excel li apre direttamente senza modificare la codifica; questo README è a sua volta in UTF-8 senza BOM.
- **Limiti noti.** Il numero di righe varia leggermente da lingua a lingua, perché una voce viene saltata quando una lingua non ne ha la traduzione oppure quando la sua forma coincide con quella della lingua di destinazione. Righe di confronto e voci non sono la stessa cosa: le 34 categorie totalizzano 8.559 `entries`, cioè il numero di oggetti denominati dei file di lingua ufficiali assegnati a quelle categorie, comprese le voci non tradotte in questa lingua. Il conteggio di questa cartella, deduplicato su `target`, è 7.777 e segue una definizione diversa. La definizione completa è nella sezione «Data Overview» di `../../README.md`, nella radice del gioco. La stessa denominazione può comparire in più categorie; la terminologia segue la localizzazione ufficiale, anche quando i nomi restano non tradotti.
- **Glossario supplementare.** La cartella gemella `../../minecraft-glossary-supplement/` aggiunge i nomi standard del wiki di Minecraft, solo per il cinese semplificato e tradizionale; può essere usata insieme a questo glossario.
- **Rigenerazione.** Dalla radice del gioco, `python tools/build_glossary.py` ricostruisce questo glossario dai file di lingua ufficiali (lo script legge una cartella esterna di materiali con `mcmeta_lang/<locale>.json` e scrive in `minecraft-glossary/`); `python tools/verify_output.py` ricontrolla ogni conteggio di righe rispetto a `tools/glossary_counts.json`, e `python tools/make_readme.py` rigenera i README delle biblioteche.

## Esclusione di responsabilità

Questa cartella è un database terminologico di traduzione **non ufficiale**, mantenuto da una persona per studio personale, ricerca e corrispondenza terminologica in strumenti di traduzione assistita dall'IA (incluso, ma non solo, Immersive Translate). Non esiste alcun rapporto di dipendenza, licenza, collaborazione, agenzia o rappresentanza ufficiale con gli sviluppatori, gli editori, i distributori, i gestori o i titolari dei diritti di Minecraft; i nomi qui contenuti non rappresentano alcuna posizione ufficiale, non sono garantiti come sempre accurati, completi o coerenti con la versione attuale del gioco e **non devono essere considerati il glossario ufficiale né file di localizzazione ufficiali di alcun gioco**.

I nomi di giochi, personaggi, i nomi propri e i marchi appartengono ai rispettivi titolari e questo progetto non rivendica alcun diritto su di essi. Ogni responsabilità derivante dall'uso di questo progetto e delle traduzioni da esso prodotte ricade sull'utente. I titolari dei diritti che ritengano inappropriato un contenuto possono scriverci tramite GitHub Issues / Pull Request: il curatore verificherà e provvederà a modificare o rimuovere il contenuto.

Le condizioni complete sono in `README.md` / `README_EN.md` / `README_JP.md` nella radice del repository.

---

**Game-translation-terminology-database è un progetto personale indipendente e non ha alcun rapporto di appartenenza, autorizzazione, collaborazione o rappresentanza con questo gioco, i suoi sviluppatori, editori, distributori o titolari dei diritti.**
