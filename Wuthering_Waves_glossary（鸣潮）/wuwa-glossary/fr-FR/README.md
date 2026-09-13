# Wuthering Waves（鸣潮）Base terminologique — Français（`fr-FR`）

[← Retour à la présentation du jeu](../../README.md) ｜ [← Description de la sous-bibliothèque wuwa-glossary](../README.md)

Ce répertoire est la base terminologique de Wuthering Waves avec le **`fr-FR` (français) comme langue cible**. Il contient **123,230** entrées et **654,776** lignes d’appariement (les lignes de données des 23 fichiers CSV de ce répertoire, environ **63.8 MiB**). La colonne `tgt_lng` vaut toujours `fr-FR` et la colonne `source` contient la formulation dans chacune des 9 autres langues (`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ja-JP` (日本語), `ko-KR` (한국어), `de-DE` (Deutsch), `es-ES` (Español), `pt-BR` (Português), `th-TH` (ภาษาไทย)), de sorte qu’un même texte du jeu peut être retrouvé depuis n’importe laquelle d’entre elles.

## Fichiers

Ce répertoire est de **structure plate** : les 23 CSV de catégorie se trouvent directement ici et il n’y a pas de sous-répertoire supplémentaire :

- `characters.csv` — Noms de personnages
- `weapons.csv` — Noms d’armes
- `echoes.csv` — Échos
- `skills.csv` — Compétences
- `resonant-chains.csv` — Chaînes de résonance
- `quests.csv` — Quêtes
- `dungeons.csv` — Donjons et défis
- `regions.csv` — Régions et carte
- `factions.csv` — Factions et puissances
- `items.csv` — Objets et matériaux
- `monsters.csv` — Monstres et créatures
- `npcs.csv` — PNJ et locuteurs
- `achievements.csv` — Succès
- `activities.csv` — Événements et modes de jeu
- `buffs.csv` — Bonus et effets
- `voice-lines.csv` — Voix des personnages
- `archives.csv` — Archives et lectures
- `terms.csv` — Termes et encyclopédie
- `system.csv` — Textes système
- `ui.csv` — Textes d’interface
- `tutorials.csv` — Tutoriels
- `story.csv` — Textes de scénario
- `other.csv` — Autres

Chaque fichier comporte exactement trois colonnes, `source,target,tgt_lng`, avec une ligne d’en-tête : pour la langue cible indiquée par `tgt_lng`, `target` est la traduction et `source` la formulation dans **l’une des autres langues**. Une entrée apparaît donc une fois par langue restante en ligne `source` (les lignes en double et identiques ont été fusionnées, le nombre de lignes n’est donc pas neuf fois celui des entrées). Les fichiers s’importent directement dans les outils CAT ou les logiciels d’appariement terminologique tels qu’Immersive Translate.

## Catégories et nombre d’entrées

| Catégorie | Thème | Entrées | Lignes d’appariement |
| --- | --- | --- | --- |
| `characters.csv` | Noms de personnages | 1,230 | 5,287 |
| `weapons.csv` | Noms d’armes | 820 | 3,122 |
| `echoes.csv` | Échos | 1,000 | 6,311 |
| `skills.csv` | Compétences | 5,344 | 31,438 |
| `resonant-chains.csv` | Chaînes de résonance | 784 | 6,119 |
| `quests.csv` | Quêtes | 2,807 | 14,598 |
| `dungeons.csv` | Donjons et défis | 1,910 | 12,255 |
| `regions.csv` | Régions et carte | 2,229 | 16,271 |
| `factions.csv` | Factions et puissances | 8 | 49 |
| `items.csv` | Objets et matériaux | 8,384 | 55,824 |
| `monsters.csv` | Monstres et créatures | 685 | 4,614 |
| `npcs.csv` | PNJ et locuteurs | 14,172 | 63,544 |
| `achievements.csv` | Succès | 2,563 | 22,171 |
| `activities.csv` | Événements et modes de jeu | 9,531 | 64,701 |
| `buffs.csv` | Bonus et effets | 270 | 2,043 |
| `voice-lines.csv` | Voix des personnages | 7,374 | 32,992 |
| `archives.csv` | Archives et lectures | 839 | 6,714 |
| `terms.csv` | Termes et encyclopédie | 1,672 | 12,618 |
| `system.csv` | Textes système | 9,756 | 66,208 |
| `ui.csv` | Textes d’interface | 13,866 | 79,475 |
| `tutorials.csv` | Tutoriels | 6,253 | 32,328 |
| `story.csv` | Textes de scénario | 29,841 | 102,760 |
| `other.csv` | Autres | 1,892 | 13,334 |
| **Total** | **23 catégories** | **123,230** | **654,776** |

« Entrées » est le nombre d’entrées dédoublonnées (une entrée = une clé de texte du jeu) ; la valeur provient du champ `concepts` de `tools/_counts.json` et est **commune à toute la base et indépendante de la langue cible**. « Lignes d’appariement » est le nombre réel de lignes de données du CSV de cette catégorie dans ce répertoire. Un même texte peut appartenir à plusieurs catégories : la somme des lignes par catégorie dépasse donc le nombre d’entrées dédoublonnées.

## Remarques

- **Origine des traductions** : la colonne `target` est reprise telle quelle des fichiers de localisation du jeu lui-même ([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data), `Textmaps/<lang>/multi_text/MultiText.json`, jeu 3.6.0 ; quelques clés sont complétées depuis [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData), `TextMap/<lang>/MultiText.json`, jeu 3.1.0). Ce sont les termes officiels du jeu, et non une traduction de seconde main.
- **Appariement** : les lignes sont alignées par la clé de texte du jeu (par ex. `RoleInfo_1402_Name`) ; la même clé écrite dans une autre langue devient la ligne `source` du `target` de ce répertoire.
- **Étiquette de langue** : `tgt_lng` est fixée au code de langue de ce répertoire et correspond à son nom.
- **Encodage** : tous les CSV sont en **UTF-8 avec BOM**, avec des fins de ligne **CRLF** et une ligne d’en-tête ; les champs contenant des virgules ou des guillemets sont échappés selon la RFC 4180, ce qui permet de les ouvrir directement dans Excel.
- **Limites connues** : les dialogues scénarisés phrase par phrase (environ 170 000 lignes par langue) ne sont pas inclus par défaut ; si besoin, ils peuvent être générés avec l’option `--with-dialogue`, décrite dans `../README.md`. Les textes trop longs sont tronqués par catégorie via `MAX_LEN` dans `tools/wuwa_config.py`. `ru-RU`, `id-ID` et `vi-VN` sont des fichiers vides en amont et sont donc absents, tandis que `it-IT` et `tr-TR` ne sont pas des langues de texte prises en charge par le jeu.

## Avertissement

Ce répertoire est une base terminologique **non officielle**, constituée et maintenue à titre personnel, destinée uniquement à l’étude personnelle, à la recherche et à l’appariement terminologique dans les logiciels de traduction par IA (y compris, sans s’y limiter, Immersive Translate). Elle n’entretient aucune relation de subordination, de licence, de coopération, de mandat ou de représentation officielle avec les développeurs, éditeurs, distributeurs, exploitants ou titulaires de droits des jeux concernés ; les traductions qu’elle contient ne représentent pas une position officielle, ne sont pas garanties exactes, complètes ou conformes à la version actuelle du jeu et **ne doivent pas être considérées comme le glossaire officiel ni un fichier de localisation officiel d’un jeu**. Les noms de jeux, noms de personnages, noms propres et marques appartiennent à leurs titulaires respectifs, et ce projet ne revendique aucun droit sur ceux-ci. Si un titulaire de droits estime qu’un contenu est inapproprié, il peut nous contacter via GitHub Issues / Pull Requests ; le contenu sera vérifié puis modifié ou supprimé. Les conditions complètes figurent dans `README.md` / `README_EN.md` / `README_JP.md` à la racine du dépôt.
