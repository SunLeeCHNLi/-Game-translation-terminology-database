# Glossaire de Genshin Impact（原神）— Français（`fr-FR`）

[← Retour à la présentation du jeu](../../README.md) · [简体中文](README_zh-CN.md)

Ce répertoire constitue la partie principale du glossaire de Genshin Impact **avec `fr-FR` comme langue cible** : au total **8,186** termes dédoublonnés et **89,613** lignes parallèles — **63,156** lignes dans les 17 catégories principales et **26,457** lignes dans les 10 sous-catégories TCG. Dans les 27 fichiers CSV, la colonne `tgt_lng` est fixée à `fr-FR`, `source` contient la forme utilisée dans l’une des 13 autres langues et `target` le nom dans cette langue cible.

## Fichiers

Ce répertoire de langue contient **27 fichiers CSV** sur deux niveaux :

- **17 catégories principales** (directement dans ce répertoire) :
  `characters（Personnages）.csv`, `talents（Talents）.csv`, `constellations（Constellations）.csv`, `weapons（Armes）.csv`, `materials（Matériaux）.csv`, `foods（Nourriture）.csv`, `crafts（Matériaux de fabrication）.csv`, `artifacts（Artefacts）.csv`, `domains（Domaines）.csv`, `enemies（Ennemis）.csv`, `animals（Animaux）.csv`, `outfits（Tenues）.csv`, `windgliders（Planeurs）.csv`, `namecards（Cartes de visite）.csv`, `geographies（Noms de lieux）.csv`, `achievements（Succès）.csv`, `adventureranks（Textes de rang d’aventurier）.csv`
- **10 sous-catégories TCG** (dans le sous-dossier `tcg-`) :
  `tcg-action-cards（Cartes d’action）.csv`, `tcg-character-cards（Cartes de personnage）.csv`, `tcg-enemy-cards（Cartes d’ennemi）.csv`, `tcg-summons（Invocations）.csv`, `tcg-status-effects（Effets de statut）.csv`, `tcg-keywords（Mots-clés）.csv`, `tcg-card-backs（Dos de carte）.csv`, `tcg-card-boxes（Boîtes de cartes）.csv`, `tcg-detailed-rules（Règles détaillées）.csv`, `tcg-level-rewards（Récompenses de niveau）.csv`

Chaque fichier comporte exactement trois colonnes :

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Alhacén | Alhaitham | fr-FR |

`source` = le nom du même objet de jeu dans l’une des 13 autres langues, `target` = le nom dans la langue cible de ce répertoire, `tgt_lng` = l’étiquette de langue du fichier cible (ici toujours `fr-FR`). Les fichiers s’importent directement comme base terminologique dans les outils CAT (Trados, memoQ, Phrase, …) ou dans les extensions de correspondance terminologique telles qu’Immersive Translate.

## Catégories et décomptes

| Catégorie | Thème | Termes | Lignes |
| --- | --- | ---: | ---: |
| `characters（Personnages）.csv` | Personnages | 122 | 577 |
| `talents（Talents）.csv` | Talents | 125 | 632 |
| `constellations（Constellations）.csv` | Constellations | 125 | 632 |
| `weapons（Armes）.csv` | Armes | 249 | 2,823 |
| `materials（Matériaux）.csv` | Matériaux | 919 | 10,636 |
| `foods（Nourriture）.csv` | Nourriture | 398 | 4,541 |
| `crafts（Matériaux de fabrication）.csv` | Matériaux de fabrication | 295 | 3,522 |
| `artifacts（Artefacts）.csv` | Artefacts | 63 | 727 |
| `domains（Domaines）.csv` | Domaines | 284 | 3,636 |
| `enemies（Ennemis）.csv` | Ennemis | 346 | 4,103 |
| `animals（Animaux）.csv` | Animaux | 223 | 2,647 |
| `outfits（Tenues）.csv` | Tenues | 150 | 1,869 |
| `windgliders（Planeurs）.csv` | Planeurs | 18 | 211 |
| `namecards（Cartes de visite）.csv` | Cartes de visite | 289 | 3,606 |
| `geographies（Noms de lieux）.csv` | Noms de lieux | 268 | 3,389 |
| `achievements（Succès）.csv` | Succès | 1,548 | 19,461 |
| `adventureranks（Textes de rang d’aventurier）.csv` | Textes de rang d’aventurier | 21 | 144 |
| `tcg-action-cards（Cartes d’action）.csv` | Cartes d’action | 927 | 9,529 |
| `tcg-character-cards（Cartes de personnage）.csv` | Cartes de personnage | 149 | 929 |
| `tcg-enemy-cards（Cartes d’ennemi）.csv` | Cartes d’ennemi | 134 | 1,114 |
| `tcg-summons（Invocations）.csv` | Invocations | 152 | 1,159 |
| `tcg-status-effects（Effets de statut）.csv` | Effets de statut | 1,159 | 11,465 |
| `tcg-keywords（Mots-clés）.csv` | Mots-clés | 139 | 1,511 |
| `tcg-card-backs（Dos de carte）.csv` | Dos de carte | 39 | 407 |
| `tcg-card-boxes（Boîtes de cartes）.csv` | Boîtes de cartes | 7 | 32 |
| `tcg-detailed-rules（Règles détaillées）.csv` | Règles détaillées | 11 | 142 |
| `tcg-level-rewards（Récompenses de niveau）.csv` | Récompenses de niveau | 26 | 169 |
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
