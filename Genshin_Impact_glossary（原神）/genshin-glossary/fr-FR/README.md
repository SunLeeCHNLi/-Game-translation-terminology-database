# Glossaire de Genshin Impact（原神）— Français（`fr-FR`）

[← Retour à la présentation du jeu](../../README.md)

Ce répertoire constitue la partie principale du glossaire de Genshin Impact **avec `fr-FR` comme langue cible** : au total **8,186** termes dédoublonnés et **89,613** lignes parallèles — **63,156** lignes dans les 17 catégories principales et **26,457** lignes dans les 10 sous-catégories TCG. Dans les 27 fichiers CSV, la colonne `tgt_lng` est fixée à `fr-FR`, `source` contient la forme utilisée dans l’une des 13 autres langues et `target` le nom dans cette langue cible.

## Fichiers

Ce répertoire de langue contient **27 fichiers CSV** sur deux niveaux :

- **17 catégories principales** (directement dans ce répertoire) :
  `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv`
- **10 sous-catégories TCG** (dans le sous-dossier `TCG/`) :
  `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv`

Chaque fichier comporte exactement trois colonnes :

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Alhacén | Alhaitham | fr-FR |

`source` = le nom du même objet de jeu dans l’une des 13 autres langues, `target` = le nom dans la langue cible de ce répertoire, `tgt_lng` = l’étiquette de langue du fichier cible (ici toujours `fr-FR`). Les fichiers s’importent directement comme base terminologique dans les outils CAT (Trados, memoQ, Phrase, …) ou dans les extensions de correspondance terminologique telles qu’Immersive Translate.

## Catégories et décomptes

| Catégorie | Thème | Termes | Lignes |
| --- | --- | ---: | ---: |
| `characters.csv` | Personnages | 122 | 577 |
| `talents.csv` | Talents | 125 | 632 |
| `constellations.csv` | Constellations | 125 | 632 |
| `weapons.csv` | Armes | 249 | 2,823 |
| `materials.csv` | Matériaux | 919 | 10,636 |
| `foods.csv` | Nourriture | 398 | 4,541 |
| `crafts.csv` | Matériaux de fabrication | 295 | 3,522 |
| `artifacts.csv` | Artefacts | 63 | 727 |
| `domains.csv` | Domaines | 284 | 3,636 |
| `enemies.csv` | Ennemis | 346 | 4,103 |
| `animals.csv` | Animaux | 223 | 2,647 |
| `outfits.csv` | Tenues | 150 | 1,869 |
| `windgliders.csv` | Planeurs | 18 | 211 |
| `namecards.csv` | Cartes de visite | 289 | 3,606 |
| `geographies.csv` | Noms de lieux | 268 | 3,389 |
| `achievements.csv` | Succès | 1,548 | 19,461 |
| `adventureranks.csv` | Textes de rang d’aventurier | 21 | 144 |
| `TCG/action-cards.csv` | Cartes d’action | 927 | 9,529 |
| `TCG/character-cards.csv` | Cartes de personnage | 149 | 929 |
| `TCG/enemy-cards.csv` | Cartes d’ennemi | 134 | 1,114 |
| `TCG/summons.csv` | Invocations | 152 | 1,159 |
| `TCG/status-effects.csv` | Effets de statut | 1,159 | 11,465 |
| `TCG/keywords.csv` | Mots-clés | 139 | 1,511 |
| `TCG/card-backs.csv` | Dos de carte | 39 | 407 |
| `TCG/card-boxes.csv` | Boîtes de cartes | 7 | 32 |
| `TCG/detailed-rules.csv` | Règles détaillées | 11 | 142 |
| `TCG/level-rewards.csv` | Récompenses de niveau | 26 | 169 |
| **Catégories principales (17 fichiers)** | — | **5,443** | **63,156** |
| **TCG (10 fichiers)** | — | **2,743** | **26,457** |
| **Total (27 fichiers)** | — | **8,186** | **89,613** |

## Remarques

- **Source et alignement** : la colonne `target` contient les noms **officiels localisés** du jeu présents dans [genshin-db](https://github.com/theBowja/genshin-db) 7.0 — il ne s’agit ni de traduction automatique ni de traduction de seconde main. `source` contient le même objet de jeu dans l’une des 13 autres langues ; l’alignement se fait par le nom de l’objet, et les lignes de même nom et de même traduction ont été fusionnées.
- **Étiquette de langue** : la colonne `tgt_lng` est fixée à `fr-FR` dans tous les fichiers de ce répertoire (nom interne dans genshin-db : `French`).
- **Encodage** : tous les CSV sont en **UTF-8 avec BOM** et en **CRLF** ; les champs contenant des virgules ou des guillemets sont échappés selon la RFC 4180. Excel les ouvre par double-clic sans caractères erronés.
- **Termes ≠ lignes** : « Termes » est le **nombre dédoublonné d’objets de nom** par catégorie (identique pour toute la collection) ; « Lignes » est le nombre réel de lignes de données du fichier CSV dans ce répertoire. Le même terme apparaît en outre une fois pour chacune des 13 autres langues en `source`, de sorte que le nombre de lignes est un multiple du nombre de termes ; un même nom peut aussi figurer dans plusieurs catégories.
- **Limites connues** : l’instantané de données correspond à genshin-db 7.0 (14 langues) et peut être en retard sur la version actuelle du jeu ; quelques catégories diffèrent de quelques lignes selon la langue (par ex. `adventureranks`, `achievements`, `enemies`). Ce répertoire ne contient que le glossaire principal ; le glossaire complémentaire se trouve dans `../../genshin-glossary-supplement/` et la vue d’ensemble de ce sous-ensemble dans `../README.md`.

## Avertissement

Ce répertoire est une collection terminologique **non officielle** tenue à titre personnel, destinée uniquement à l’étude personnelle, à la recherche et à l’aide à la correspondance terminologique des outils de traduction par IA (y compris, sans s’y limiter, Immersive Translate). Il n’existe aucun lien d’affiliation, d’autorisation, de coopération, de représentation ou de représentation officielle avec les développeurs, éditeurs, distributeurs, exploitants ou titulaires de droits des jeux concernés ; les traductions qu’il contient ne représentent aucune position officielle et ne sont pas garanties exactes, complètes ou conformes à la version actuelle du jeu, et **ne doivent pas être considérées comme le glossaire officiel ou un fichier de localisation officiel d’un jeu**. Tous les droits sur les noms de jeux, noms de personnages, noms propres et marques appartiennent à leurs titulaires respectifs, et ce projet ne revendique aucun droit sur cette propriété intellectuelle de tiers. Toute responsabilité découlant de l’utilisation de ce projet et des traductions produites à partir de celui-ci incombe à l’utilisateur. Conditions complètes : `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) à la racine du dépôt.

---

**Game-translation-terminology-database est un projet personnel indépendant et n’a aucun lien avec les jeux mentionnés ni avec les entreprises et organisations associées.**
