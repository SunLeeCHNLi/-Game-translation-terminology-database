# Glossaire Minecraft（我的世界）— Français（`fr-FR`）

[← Retour à la présentation du jeu](../../README.md) · [zh-CN](README_zh-CN.md)

Ce dossier est le glossaire terminologique Minecraft dont **la langue cible est le français (`fr-FR`)** : **7 823** termes dédoublonnés sur `target` et **101 569** lignes de correspondance répartis dans **34** fichiers CSV. La colonne `tgt_lng` vaut toujours `fr-FR` ; `source` contient le même terme tel qu'écrit dans **l'une des 13 autres langues** et `target` la forme française. Les fichiers sont séparés par **catégorie**, un CSV par catégorie, les catégories système et texte étant regroupées dans le sous-dossier `extra/`.

## Fichiers

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 19 fichiers de catégories principales
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — 15 fichiers de catégories système et texte dans `extra/`

Au total, **34 fichiers CSV**. Tous utilisent les trois mêmes colonnes :

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | Une alimentation équilibrée | fr-FR |
| A cidade no fim do jogo | Les mystérieuses cités de l'End | fr-FR |

Arborescence :

```text
fr-FR/
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
└── extra/  # catégories système et texte
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

## Catégories et décompte

La colonne « Termes » indique le nombre d'**objets nommés des fichiers de langue officiels** (clés des fichiers de langue, y compris les entrées non traduites dans cette langue) rattachés à une catégorie ; elle est donc identique dans chaque dossier de langue, provient de `tools/glossary_counts.json` et les 34 catégories totalisent 8 559 `entries`. La colonne « Lignes » est le nombre de lignes que **ce dossier** contient réellement dans ce fichier. Ces deux chiffres relèvent de définitions différentes et ne doivent pas être confondus.

### Catégories principales (contenu du jeu)

| Catégorie | Thème | Termes | Lignes |
| --- | --- | ---: | ---: |
| `blocks.csv` | Blocs | 1 975 | 25 426 |
| `items.csv` | Objets | 803 | 9 092 |
| `entities.csv` | Entités | 219 | 2 582 |
| `biomes.csv` | Biomes | 67 | 835 |
| `enchantments.csv` | Enchantements | 54 | 553 |
| `effects.csv` | Effets de statut | 42 | 514 |
| `instruments.csv` | Instruments | 8 | 98 |
| `materials.csv` | Matériaux de décoration | 11 | 143 |
| `paintings.csv` | Tableaux | 104 | 315 |
| `attributes.csv` | Attributs | 83 | 555 |
| `item-groups.csv` | Groupes d'objets | 16 | 198 |
| `jukebox-songs.csv` | Musiques de jukebox | 22 | 42 |
| `trim-patterns.csv` | Motifs de décoration | 18 | 234 |
| `colors.csv` | Couleurs | 16 | 184 |
| `statistics.csv` | Statistiques | 88 | 1 143 |
| `maps.csv` | Cartes | 33 | 414 |
| `music.csv` | Pistes musicales | 70 | 192 |
| `sound-categories.csv` | Catégories de son | 11 | 133 |
| `game-modes.csv` | Modes de jeu | 6 | 77 |
| **Sous-total** | 19 fichiers | **3 646** | **42 730** |

### Catégories de `extra/` (système et texte)

| Catégorie | Thème | Termes | Lignes |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | Sous-titres | 1 023 | 12 504 |
| `extra/death-messages.csv` | Messages de mort | 106 | 1 371 |
| `extra/advancement-titles.csv` | Titres de progrès | 127 | 1 603 |
| `extra/advancement-descriptions.csv` | Descriptions de progrès | 127 | 1 641 |
| `extra/gamerules.csv` | Règles de jeu | 117 | 1 490 |
| `extra/commands.csv` | Commandes et arguments | 856 | 10 747 |
| `extra/gui.csv` | Textes d'interface | 581 | 6 650 |
| `extra/options.csv` | Options et touches | 754 | 8 184 |
| `extra/multiplayer.csv` | Multijoueur | 173 | 2 029 |
| `extra/realms.csv` | Realms | 426 | 5 050 |
| `extra/world-management.csv` | Gestion des mondes | 294 | 3 577 |
| `extra/resource-packs.csv` | Packs de ressources et de données | 62 | 761 |
| `extra/telemetry.csv` | Télémétrie | 70 | 897 |
| `extra/dev-tools.csv` | Outils de développement et de test | 144 | 1 811 |
| `extra/misc.csv` | Divers | 53 | 524 |
| **Sous-total** | 15 fichiers | **4 913** | **58 839** |

**Total : 34 fichiers, 7 823 termes distincts (dédoublonnés sur `target`), 101 569 lignes de correspondance.**

## Remarques

- **Origine des traductions et alignement.** Tous les textes proviennent des **fichiers de langue officiels de Minecraft : Java Edition** (miroir [misode/mcmeta](https://github.com/misode/mcmeta), branche `assets`, chemin `assets/minecraft/lang/<locale>.json` ; pour cette langue, `fr_fr.json`). Il s'agit donc de **localisations officielles**, et non de retraductions ni de traduction automatique. L'alignement se fait par la clé du fichier de langue : chaque terme est émis une fois par *autre* langue, ce qui explique un nombre de lignes bien supérieur au nombre de termes.
- **Étiquettes de langue.** Dans ce dossier, `tgt_lng` vaut toujours `fr-FR` et désigne la langue cible ; `source` peut être n'importe laquelle des 13 autres langues : `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `de-DE`, `es-ES`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`.
- **Encodage.** Tous les CSV sont en **UTF-8 avec BOM**, avec des fins de ligne **CRLF** et une ligne d'en-tête ; les champs contenant des virgules ou des guillemets sont échappés selon la RFC 4180. Excel les ouvre directement, sans réglage d'encodage ; ce README est lui-même en UTF-8 sans BOM.
- **Limites connues.** Le nombre de lignes varie légèrement d'une langue à l'autre, car un terme est ignoré lorsqu'une langue n'a pas de traduction pour lui ou lorsque sa formulation est identique à celle de la langue cible. Les lignes de comparaison et les termes ne sont pas la même chose : les 34 catégories totalisent 8 559 `entries`, soit le nombre d'objets nommés des fichiers de langue officiels rattachés à ces catégories, y compris les entrées non traduites dans cette langue. Le décompte de ce dossier, dédoublonné sur `target`, est de 7 823 et relève d'une autre définition. La définition complète se trouve dans la section « Data Overview » de `../../README.md`, à la racine du jeu. Une même formulation peut apparaître dans plusieurs catégories ; la terminologie suit la localisation officielle, y compris lorsque les noms restent non traduits.
- **Glossaire complémentaire.** Le dossier voisin `../../minecraft-glossary-supplement/` ajoute les noms standard du wiki Minecraft, uniquement pour le chinois simplifié et traditionnel ; il peut être utilisé avec ce glossaire.
- **Reproduction.** Depuis la racine du jeu, `python tools/build_glossary.py` régénère ce glossaire à partir des fichiers de langue officiels (le script lit un dossier externe de ressources contenant `mcmeta_lang/<locale>.json` et écrit dans `minecraft-glossary/`) ; `python tools/verify_output.py` revérifie chaque décompte de lignes par rapport à `tools/glossary_counts.json`, et `python tools/make_readme.py` régénère les README des bibliothèques.

## Avertissement

Ce dossier est une base terminologique de traduction **non officielle**, tenue par une personne à titre privé pour l'étude personnelle, la recherche et la correspondance terminologique dans les outils de traduction assistée par IA (y compris, sans s'y limiter, Immersive Translate). Il n'existe aucun lien de subordination, de licence, de coopération, de mandat ni de représentation officielle avec les développeurs, éditeurs, distributeurs, exploitants ou titulaires des droits de Minecraft ; les noms contenus ici ne représentent aucune position officielle, ne sont pas garantis exacts, complets ou conformes à la version actuelle du jeu, et **ne doivent pas être considérés comme le glossaire officiel ni comme des fichiers de localisation officiels d'un jeu quelconque**.

Les noms de jeux, de personnages, les noms propres et les marques restent la propriété de leurs titulaires respectifs, et ce projet ne revendique aucun droit sur eux. La responsabilité découlant de l'utilisation de ce projet et des traductions qui en sont issues incombe à l'utilisateur. Tout titulaire de droits qui jugerait un contenu inapproprié peut nous écrire via GitHub Issues / Pull Request ; le mainteneur vérifiera puis modifiera ou supprimera ce contenu.

Les conditions complètes figurent dans `README.md` / `README_EN.md` / `README_JP.md` à la racine du dépôt.

---

**Game-translation-terminology-database est un projet personnel indépendant, sans lien d'appartenance, d'autorisation, de coopération ou de représentation avec ce jeu, ses développeurs, éditeurs, distributeurs ou titulaires de droits.**
