# Glossario di Genshin Impact（原神）— Italiano（`it-IT`）

[← Torna alla panoramica del gioco](../../README.md)

Questa cartella è la parte principale del glossario di Genshin Impact **con `it-IT` come lingua di destinazione**: in totale **8,186** termini deduplicati e **89,437** righe parallele — **63,173** righe nelle 17 categorie principali e **26,264** righe nelle 10 sottocategorie TCG. In tutti i 27 file CSV la colonna `tgt_lng` è fissata a `it-IT`, `source` contiene la forma usata in una delle altre 13 lingue e `target` il nome in questa lingua di destinazione.

## File

Questa cartella di lingua contiene **27 file CSV** su due livelli:

- **17 categorie principali** (direttamente in questa cartella):
  `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv`
- **10 sottocategorie TCG** (nella sottocartella `TCG/`):
  `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv`

Ogni file ha esattamente tre colonne:

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Alhacén | Alhaitham | it-IT |

`source` = il nome dello stesso oggetto di gioco in una delle altre 13 lingue, `target` = il nome nella lingua di destinazione di questa cartella, `tgt_lng` = l’etichetta di lingua del file di destinazione (qui sempre `it-IT`). I file si importano direttamente come banca dati terminologica in strumenti CAT (Trados, memoQ, Phrase, …) o in estensioni di corrispondenza terminologica come Immersive Translate.

## Categorie e conteggi

| Categoria | Tema | Termini | Righe |
| --- | --- | ---: | ---: |
| `characters.csv` | Personaggi | 122 | 577 |
| `talents.csv` | Talenti | 125 | 632 |
| `constellations.csv` | Costellazioni | 125 | 632 |
| `weapons.csv` | Armi | 249 | 2,823 |
| `materials.csv` | Materiali | 919 | 10,636 |
| `foods.csv` | Cibo | 398 | 4,541 |
| `crafts.csv` | Materiali di fabbricazione | 295 | 3,522 |
| `artifacts.csv` | Manufatti | 63 | 727 |
| `domains.csv` | Domini | 284 | 3,636 |
| `enemies.csv` | Nemici | 346 | 4,104 |
| `animals.csv` | Animali | 223 | 2,647 |
| `outfits.csv` | Costumi | 150 | 1,869 |
| `windgliders.csv` | Alianti | 18 | 211 |
| `namecards.csv` | Biglietti da visita | 289 | 3,606 |
| `geographies.csv` | Toponimi | 268 | 3,389 |
| `achievements.csv` | Obiettivi | 1,548 | 19,464 |
| `adventureranks.csv` | Testi del grado di avventura | 21 | 157 |
| `TCG/action-cards.csv` | Carte azione | 927 | 9,618 |
| `TCG/character-cards.csv` | Carte personaggio | 149 | 929 |
| `TCG/enemy-cards.csv` | Carte nemico | 134 | 1,114 |
| `TCG/summons.csv` | Evocazioni | 152 | 1,139 |
| `TCG/status-effects.csv` | Effetti di stato | 1,159 | 11,203 |
| `TCG/keywords.csv` | Parole chiave | 139 | 1,511 |
| `TCG/card-backs.csv` | Dorsi delle carte | 39 | 407 |
| `TCG/card-boxes.csv` | Scatole delle carte | 7 | 32 |
| `TCG/detailed-rules.csv` | Regole dettagliate | 11 | 142 |
| `TCG/level-rewards.csv` | Ricompense di livello | 26 | 169 |
| **Categorie principali (17 file)** | — | **5,443** | **63,173** |
| **TCG (10 file)** | — | **2,743** | **26,264** |
| **Totale (27 file)** | — | **8,186** | **89,437** |

## Note

- **Origine e allineamento**: la colonna `target` contiene i nomi **ufficiali localizzati** del gioco presenti in [genshin-db](https://github.com/theBowja/genshin-db) 7.0: non si tratta di traduzione automatica né di traduzione di seconda mano. `source` contiene lo stesso oggetto di gioco in una delle altre 13 lingue; l’allineamento avviene per nome dell’oggetto e le righe con lo stesso nome e la stessa traduzione sono state unite.
- **Etichetta di lingua**: la colonna `tgt_lng` è fissata a `it-IT` in tutti i file di questa cartella (nome interno in genshin-db: `Italian`).
- **Codifica**: tutti i CSV sono **UTF-8 con BOM** e **CRLF**; i campi con virgole o virgolette sono protetti secondo la RFC 4180. Excel li apre con un doppio clic senza caratteri errati.
- **Termini ≠ righe**: «Termini» è il **numero deduplicato di oggetti-nome** per categoria (identico in tutta la raccolta); «Righe» è il numero effettivo di righe di dati del file CSV in questa cartella. Lo stesso termine compare inoltre una volta per ciascuna delle altre 13 lingue come `source`, quindi il numero di righe è un multiplo di quello dei termini; uno stesso nome può comparire in più categorie.
- **Limiti noti**: lo snapshot dei dati corrisponde a genshin-db 7.0 (14 lingue) e può essere indietro rispetto alla versione attuale del gioco; alcune categorie differiscono di poche righe tra le lingue (per es. `adventureranks`, `achievements`, `enemies`). Questa cartella contiene solo il glossario principale; il glossario supplementare si trova in `../../genshin-glossary-supplement/` e la panoramica di questo sottoinsieme in `../README.md`.

## Disclaimer

Questa cartella è una raccolta terminologica **non ufficiale** mantenuta a livello personale, destinata esclusivamente allo studio personale, alla ricerca e al supporto della corrispondenza terminologica negli strumenti di traduzione con IA (incluso, ma non solo, Immersive Translate). Non sussiste alcun rapporto di affiliazione, autorizzazione, collaborazione, agenzia o rappresentanza ufficiale con sviluppatori, editori, distributori, gestori o titolari dei diritti dei giochi interessati; le traduzioni qui contenute non rappresentano alcuna posizione ufficiale e non sono garantite come sempre accurate, complete o coerenti con la versione attuale del gioco, e **non devono essere considerate il glossario ufficiale o un file di localizzazione ufficiale di alcun gioco**. Tutti i diritti su nomi di giochi, nomi di personaggi, nomi propri e marchi appartengono ai rispettivi titolari, e questo progetto non rivendica alcun diritto su tale proprietà intellettuale di terzi. Ogni responsabilità derivante dall’uso di questo progetto e delle traduzioni da esso prodotte ricade sull’utente. Condizioni complete: `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) nella radice del repository.

---

**Game-translation-terminology-database è un progetto personale indipendente e non ha alcun legame con i giochi citati né con le aziende e organizzazioni correlate.**
