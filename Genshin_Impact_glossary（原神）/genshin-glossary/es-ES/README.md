# Glosario de Genshin Impact（原神）— Español（`es-ES`）

[← Volver a la descripción general del juego](../../README.md) · [简体中文](README_zh-CN.md)

Este directorio es la parte principal del glosario de Genshin Impact **con `es-ES` como idioma de destino**: en total **8,186** términos deduplicados y **89,411** filas paralelas — **63,173** filas en las 17 categorías principales y **26,238** filas en las 10 subcategorías de TCG. En los 27 archivos CSV la columna `tgt_lng` está fijada a `es-ES`, `source` contiene la forma usada en uno de los otros 13 idiomas y `target` el nombre en este idioma de destino.

## Archivos

Este directorio de idioma contiene **27 archivos CSV** en dos niveles:

- **17 categorías principales** (directamente en este directorio):
  `characters（Personajes）.csv`, `talents（Talentos）.csv`, `constellations（Constelaciones）.csv`, `weapons（Armas）.csv`, `materials（Materiales）.csv`, `foods（Comida）.csv`, `crafts（Materiales de fabricación）.csv`, `artifacts（Artefactos）.csv`, `domains（Dominios）.csv`, `enemies（Enemigos）.csv`, `animals（Animales）.csv`, `outfits（Trajes）.csv`, `windgliders（Planeadores）.csv`, `namecards（Tarjetas de visita）.csv`, `geographies（Topónimos）.csv`, `achievements（Logros）.csv`, `adventureranks（Textos de rango de aventura）.csv`
- **10 subcategorías de TCG** (en la subcarpeta `tcg-`):
  `tcg-action-cards（Cartas de acción）.csv`, `tcg-character-cards（Cartas de personaje）.csv`, `tcg-enemy-cards（Cartas de enemigo）.csv`, `tcg-summons（Invocaciones）.csv`, `tcg-status-effects（Efectos de estado）.csv`, `tcg-keywords（Palabras clave）.csv`, `tcg-card-backs（Reversos de carta）.csv`, `tcg-card-boxes（Cajas de cartas）.csv`, `tcg-detailed-rules（Reglas detalladas）.csv`, `tcg-level-rewards（Recompensas de nivel）.csv`

Todos los archivos tienen exactamente tres columnas:

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| Aether | Éter | es-ES |

`source` = el nombre del mismo objeto del juego en uno de los otros 13 idiomas, `target` = el nombre en el idioma de destino de este directorio, `tgt_lng` = la etiqueta de idioma del archivo de destino (aquí siempre `es-ES`). Los archivos pueden importarse directamente como base de datos terminológica en herramientas TAO (Trados, memoQ, Phrase, …) o en extensiones de coincidencia de términos como Immersive Translate.

## Categorías y recuento

| Categoría | Tema | Términos | Filas |
| --- | --- | ---: | ---: |
| `characters（Personajes）.csv` | Personajes | 122 | 577 |
| `talents（Talentos）.csv` | Talentos | 125 | 632 |
| `constellations（Constelaciones）.csv` | Constelaciones | 125 | 632 |
| `weapons（Armas）.csv` | Armas | 249 | 2,823 |
| `materials（Materiales）.csv` | Materiales | 919 | 10,636 |
| `foods（Comida）.csv` | Comida | 398 | 4,541 |
| `crafts（Materiales de fabricación）.csv` | Materiales de fabricación | 295 | 3,522 |
| `artifacts（Artefactos）.csv` | Artefactos | 63 | 727 |
| `domains（Dominios）.csv` | Dominios | 284 | 3,636 |
| `enemies（Enemigos）.csv` | Enemigos | 346 | 4,104 |
| `animals（Animales）.csv` | Animales | 223 | 2,647 |
| `outfits（Trajes）.csv` | Trajes | 150 | 1,869 |
| `windgliders（Planeadores）.csv` | Planeadores | 18 | 211 |
| `namecards（Tarjetas de visita）.csv` | Tarjetas de visita | 289 | 3,606 |
| `geographies（Topónimos）.csv` | Topónimos | 268 | 3,389 |
| `achievements（Logros）.csv` | Logros | 1,548 | 19,464 |
| `adventureranks（Textos de rango de aventura）.csv` | Textos de rango de aventura | 21 | 157 |
| `tcg-action-cards（Cartas de acción）.csv` | Cartas de acción | 927 | 9,557 |
| `tcg-character-cards（Cartas de personaje）.csv` | Cartas de personaje | 149 | 929 |
| `tcg-enemy-cards（Cartas de enemigo）.csv` | Cartas de enemigo | 134 | 1,114 |
| `tcg-summons（Invocaciones）.csv` | Invocaciones | 152 | 1,139 |
| `tcg-status-effects（Efectos de estado）.csv` | Efectos de estado | 1,159 | 11,238 |
| `tcg-keywords（Palabras clave）.csv` | Palabras clave | 139 | 1,511 |
| `tcg-card-backs（Reversos de carta）.csv` | Reversos de carta | 39 | 407 |
| `tcg-card-boxes（Cajas de cartas）.csv` | Cajas de cartas | 7 | 32 |
| `tcg-detailed-rules（Reglas detalladas）.csv` | Reglas detalladas | 11 | 142 |
| `tcg-level-rewards（Recompensas de nivel）.csv` | Recompensas de nivel | 26 | 169 |
| **Categorías principales (17 archivos)** | — | **5,443** | **63,173** |
| **TCG (10 archivos)** | — | **2,743** | **26,238** |
| **Total (27 archivos)** | — | **8,186** | **89,411** |

## Notas

- **Origen y alineación**: la columna `target` contiene los nombres **oficiales localizados** del juego incluidos en [genshin-db](https://github.com/theBowja/genshin-db) 7.0: no es traducción automática ni traducción de segunda mano. `source` contiene el mismo objeto de juego en uno de los otros 13 idiomas; la alineación se hace por el nombre del objeto y las filas con el mismo nombre y la misma traducción se han fusionado.
- **Etiqueta de idioma**: la columna `tgt_lng` está fijada a `es-ES` en todos los archivos de este directorio (nombre interno en genshin-db: `Spanish`).
- **Codificación**: todos los CSV son **UTF-8 con BOM** y **CRLF**; los campos con comas o comillas se escapan según la RFC 4180. Excel los abre con doble clic sin caracteres corruptos.
- **Términos ≠ filas**: «Términos» es el **número deduplicado de objetos de nombre** por categoría (idéntico en toda la colección); «Filas» es el número real de filas de datos de ese CSV en este directorio. El mismo término aparece además una vez por cada uno de los otros 13 idiomas como `source`, por lo que el número de filas es un múltiplo del de términos; un mismo nombre puede aparecer en varias categorías.
- **Limitaciones conocidas**: la instantánea de datos corresponde a genshin-db 7.0 (14 idiomas) y puede ir por detrás de la versión actual del juego; algunas categorías difieren en unas pocas filas entre idiomas (p. ej. `adventureranks`, `achievements`, `enemies`). Este directorio solo contiene el glosario principal; el glosario complementario está en `../../genshin-glossary-supplement/` y la visión general de este subconjunto en `../README.md`.

## Aviso legal

Este directorio es una colección terminológica **no oficial** mantenida de forma personal, destinada únicamente al estudio personal, la investigación y la ayuda a la coincidencia de términos en herramientas de traducción con IA (incluida, entre otras, Immersive Translate). No existe ninguna relación de dependencia, autorización, cooperación, representación ni representación oficial con los desarrolladores, editores, distribuidores, operadores o titulares de derechos de los juegos correspondientes; las traducciones aquí incluidas no representan ninguna postura oficial y no se garantiza que sean siempre exactas, completas o coherentes con la versión actual del juego, y **no deben considerarse el glosario oficial ni un archivo de localización oficial de ningún juego**. Todos los derechos sobre nombres de juegos, nombres de personajes, nombres propios y marcas pertenecen a sus respectivos titulares, y este proyecto no reclama ningún derecho sobre dicha propiedad intelectual de terceros. Toda responsabilidad derivada del uso de este proyecto y de las traducciones generadas con él recae en el usuario. Condiciones completas: `README.md` / `README_EN.md` / `README_JP.md` ([简体中文](../../../README.md), [English](../../../README_EN.md), [日本語](../../../README_JP.md)) en la raíz del repositorio.

---

**Game-translation-terminology-database es un proyecto personal independiente y no tiene relación alguna con los juegos mencionados ni con sus empresas y organizaciones relacionadas.**
