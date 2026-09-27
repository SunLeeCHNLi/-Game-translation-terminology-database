# Wuthering Waves（鸣潮）Base terminológica — Español（`es-ES`）

[← Volver a la descripción general del juego](../../README.md) ｜ [← Descripción de la subbiblioteca wuwa-glossary](../README.md) ｜ [简体中文](README_zh-CN.md)

Este directorio es la base terminológica de Wuthering Waves con **`es-ES` (español) como idioma de destino**. Contiene **123,230** entradas y **646,691** líneas de correspondencia (las filas de datos de los 23 archivos CSV de este directorio, unos **61.8 MiB**). La columna `tgt_lng` es siempre `es-ES` y la columna `source` recoge la forma en cada uno de los otros 9 idiomas (`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ja-JP` (日本語), `ko-KR` (한국어), `fr-FR` (Français), `de-DE` (Deutsch), `pt-BR` (Português), `th-TH` (ภาษาไทย)), de modo que un mismo texto del juego puede localizarse desde cualquiera de ellos.

## Archivos

Este directorio tiene una **estructura plana**: los 23 CSV de categoría están directamente aquí y no hay ningún subdirectorio adicional:

- `characters（Nombres de personajes）.csv` — Nombres de personajes
- `weapons（Nombres de armas）.csv` — Nombres de armas
- `echoes（Ecos）.csv` — Ecos
- `skills（Habilidades）.csv` — Habilidades
- `resonant-chains（Cadenas de resonancia）.csv` — Cadenas de resonancia
- `quests（Misiones）.csv` — Misiones
- `dungeons（Mazmorras y desafíos）.csv` — Mazmorras y desafíos
- `regions（Regiones y mapa）.csv` — Regiones y mapa
- `factions（Facciones y poderes）.csv` — Facciones y poderes
- `items（Objetos y materiales）.csv` — Objetos y materiales
- `monsters（Monstruos y criaturas）.csv` — Monstruos y criaturas
- `npcs（PNJ y hablantes）.csv` — PNJ y hablantes
- `achievements（Logros）.csv` — Logros
- `activities（Eventos y modos de juego）.csv` — Eventos y modos de juego
- `buffs（Mejoras y efectos）.csv` — Mejoras y efectos
- `voice-lines（Voces de personajes）.csv` — Voces de personajes
- `archives（Archivos y lecturas）.csv` — Archivos y lecturas
- `terms（Términos y enciclopedia）.csv` — Términos y enciclopedia
- `system（Textos del sistema）.csv` — Textos del sistema
- `ui（Textos de interfaz）.csv` — Textos de interfaz
- `tutorials（Tutoriales）.csv` — Tutoriales
- `story（Textos de historia）.csv` — Textos de historia
- `other（Otros）.csv` — Otros

Todos los archivos tienen tres columnas, `source,target,tgt_lng`, con una fila de encabezado: para el idioma de destino indicado en `tgt_lng`, `target` es la traducción y `source` es el texto en **uno de los otros idiomas**. Por eso cada entrada aparece una vez por cada idioma restante como fila `source` (las filas duplicadas e idénticas se han fusionado, así que el número de filas no es nueve veces el de entradas). Los archivos se pueden importar directamente en herramientas CAT o en programas de correspondencia terminológica como Immersive Translate.

## Categorías y recuento

| Categoría | Tema | Entradas | Líneas de correspondencia |
| --- | --- | --- | --- |
| `characters（Nombres de personajes）.csv` | Nombres de personajes | 1,230 | 5,264 |
| `weapons（Nombres de armas）.csv` | Nombres de armas | 820 | 3,106 |
| `echoes（Ecos）.csv` | Ecos | 1,000 | 6,113 |
| `skills（Habilidades）.csv` | Habilidades | 5,344 | 30,433 |
| `resonant-chains（Cadenas de resonancia）.csv` | Cadenas de resonancia | 784 | 6,169 |
| `quests（Misiones）.csv` | Misiones | 2,807 | 14,558 |
| `dungeons（Mazmorras y desafíos）.csv` | Mazmorras y desafíos | 1,910 | 12,177 |
| `regions（Regiones y mapa）.csv` | Regiones y mapa | 2,229 | 16,169 |
| `factions（Facciones y poderes）.csv` | Facciones y poderes | 8 | 49 |
| `items（Objetos y materiales）.csv` | Objetos y materiales | 8,384 | 54,692 |
| `monsters（Monstruos y criaturas）.csv` | Monstruos y criaturas | 685 | 4,533 |
| `npcs（PNJ y hablantes）.csv` | PNJ y hablantes | 14,172 | 62,976 |
| `achievements（Logros）.csv` | Logros | 2,563 | 22,168 |
| `activities（Eventos y modos de juego）.csv` | Eventos y modos de juego | 9,531 | 64,032 |
| `buffs（Mejoras y efectos）.csv` | Mejoras y efectos | 270 | 2,029 |
| `voice-lines（Voces de personajes）.csv` | Voces de personajes | 7,374 | 31,684 |
| `archives（Archivos y lecturas）.csv` | Archivos y lecturas | 839 | 6,709 |
| `terms（Términos y enciclopedia）.csv` | Términos y enciclopedia | 1,672 | 12,547 |
| `system（Textos del sistema）.csv` | Textos del sistema | 9,756 | 65,754 |
| `ui（Textos de interfaz）.csv` | Textos de interfaz | 13,866 | 77,772 |
| `tutorials（Tutoriales）.csv` | Tutoriales | 6,253 | 31,933 |
| `story（Textos de historia）.csv` | Textos de historia | 29,841 | 102,517 |
| `other（Otros）.csv` | Otros | 1,892 | 13,307 |
| **Total** | **23 categorías** | **123,230** | **646,691** |

«Entradas» es el número de entradas sin duplicados (una entrada = una clave de texto del juego); procede del campo `concepts` de `tools/_counts.json` y es **común a toda la base de datos e independiente del idioma de destino**. «Líneas de correspondencia» es el número real de filas de datos del CSV de esa categoría en este directorio. Un mismo texto puede pertenecer a varias categorías, por lo que la suma de las filas por categoría supera el número de entradas sin duplicados.

## Notas

- **Origen de las traducciones**: la columna `target` se toma tal cual de los archivos de localización del propio juego ([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data), `Textmaps/<lang>/multi_text/MultiText.json`, juego 3.6.0; algunas claves se completan desde [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData), `TextMap/<lang>/MultiText.json`, juego 3.1.0). Son los términos oficiales del juego, no una traducción de segunda mano.
- **Alineación**: las filas se alinean mediante la clave de texto del juego (p. ej. `RoleInfo_1402_Name`); la misma clave escrita en otro idioma se convierte en la fila `source` del `target` de este directorio.
- **Etiqueta de idioma**: `tgt_lng` está fijada al código de idioma de este directorio y coincide con su nombre.
- **Codificación**: todos los CSV son **UTF-8 con BOM**, con finales de línea **CRLF** y fila de encabezado; los campos con comas o comillas se escapan según RFC 4180, por lo que se abren directamente en Excel.
- **Limitaciones conocidas**: los diálogos de la historia frase por frase (unas 170.000 líneas por idioma) no se incluyen por defecto; si se desean, pueden generarse con la opción `--with-dialogue`, descrita en `../README.md`. Los textos demasiado largos se recortan por categoría mediante `MAX_LEN` en `tools/wuwa_config.py`. `ru-RU`, `id-ID` y `vi-VN` son marcadores vacíos en el origen y por eso faltan, mientras que `it-IT` y `tr-TR` no son idiomas de texto admitidos por el juego.

## Aviso legal

Este directorio es una base terminológica **no oficial**, recopilada y mantenida de forma personal, destinada únicamente al estudio personal, la investigación y la correspondencia de terminología en programas de traducción con IA (incluido, entre otros, Immersive Translate). No existe ninguna relación de dependencia, licencia, cooperación, representación ni representación oficial con los desarrolladores, editores, distribuidores, operadores o titulares de derechos de los juegos correspondientes; las traducciones aquí incluidas no representan una postura oficial, no se garantiza que sean exactas, completas ni coherentes con la versión actual del juego, y **no deben considerarse el glosario oficial ni un archivo de localización oficial de ningún juego**. Los nombres de juegos, personajes, nombres propios y marcas pertenecen a sus respectivos titulares, y este proyecto no reclama derecho alguno sobre ellos. Si algún titular considera que un contenido es inadecuado, puede contactar mediante GitHub Issues / Pull Requests; se revisará y se corregirá o eliminará. Las condiciones completas están en `README.md` / `README_EN.md` / `README_JP.md` en la raíz del repositorio.
