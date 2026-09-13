# Glosario de Minecraft（我的世界）— Español（`es-ES`）

[← Volver a la descripción general del juego](../../README.md) · [zh-CN](README_zh-CN.md)

Este directorio es el glosario terminológico de Minecraft cuyo **idioma de destino es el español (`es-ES`)**: **7.833** términos sin duplicados según `target` y **101.647** filas de correspondencia en **34** archivos CSV. La columna `tgt_lng` es siempre `es-ES`; `source` contiene el mismo término tal como se escribe en **uno de los otros 13 idiomas** y `target` la forma en español. Los archivos están separados por **categoría**, un CSV por categoría, y las categorías de sistema y de texto se guardan en la subcarpeta `extra/`.

## Archivos

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 19 archivos de categorías principales
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — 15 archivos de categorías de sistema y texto en `extra/`

En total, **34 archivos CSV**. Todos usan las mismas tres columnas:

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | Una dieta equilibrada | es-ES |
| A cidade no fim do jogo | La ciudad al final del juego | es-ES |

Estructura de directorios:

```text
es-ES/
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
└── extra/  # categorías de sistema y texto
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

## Categorías y recuento

La columna «Términos» indica cuántos **objetos con nombre de los archivos de idioma oficiales** (claves de los archivos de idioma, incluidas las entradas sin traducir en este idioma) se asignan a una categoría; por eso es idéntica en todas las carpetas de idioma, procede de `tools/glossary_counts.json` y las 34 categorías suman 8.559 `entries`. La columna «Filas» es el número de filas que **esta carpeta** contiene realmente en ese archivo. Son dos cifras con definiciones distintas y no deben mezclarse.

### Categorías principales (contenido del juego)

| Categoría | Tema | Términos | Filas |
| --- | --- | ---: | ---: |
| `blocks.csv` | Bloques | 1.975 | 25.426 |
| `items.csv` | Objetos | 803 | 9.077 |
| `entities.csv` | Entidades | 219 | 2.582 |
| `biomes.csv` | Biomas | 67 | 835 |
| `enchantments.csv` | Encantamientos | 54 | 553 |
| `effects.csv` | Efectos de estado | 42 | 514 |
| `instruments.csv` | Instrumentos | 8 | 98 |
| `materials.csv` | Materiales de adornos | 11 | 143 |
| `paintings.csv` | Cuadros | 104 | 315 |
| `attributes.csv` | Atributos | 83 | 567 |
| `item-groups.csv` | Grupos de objetos | 16 | 198 |
| `jukebox-songs.csv` | Canciones del tocadiscos | 22 | 42 |
| `trim-patterns.csv` | Diseños de adornos | 18 | 234 |
| `colors.csv` | Colores | 16 | 184 |
| `statistics.csv` | Estadísticas | 88 | 1.143 |
| `maps.csv` | Mapas | 33 | 421 |
| `music.csv` | Pistas musicales | 70 | 192 |
| `sound-categories.csv` | Categorías de sonido | 11 | 133 |
| `game-modes.csv` | Modos de juego | 6 | 77 |
| **Subtotal** | 19 archivos | **3.646** | **42.734** |

### Categorías de `extra/` (sistema y texto)

| Categoría | Tema | Términos | Filas |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | Subtítulos | 1.023 | 12.520 |
| `extra/death-messages.csv` | Mensajes de muerte | 106 | 1.338 |
| `extra/advancement-titles.csv` | Títulos de progresos | 127 | 1.603 |
| `extra/advancement-descriptions.csv` | Descripciones de progresos | 127 | 1.650 |
| `extra/gamerules.csv` | Reglas de juego | 117 | 1.490 |
| `extra/commands.csv` | Comandos y argumentos | 856 | 10.770 |
| `extra/gui.csv` | Textos de interfaz | 581 | 6.658 |
| `extra/options.csv` | Opciones y teclas | 754 | 8.218 |
| `extra/multiplayer.csv` | Multijugador | 173 | 2.057 |
| `extra/realms.csv` | Realms | 426 | 5.055 |
| `extra/world-management.csv` | Gestión de mundos | 294 | 3.569 |
| `extra/resource-packs.csv` | Paquetes de recursos y datos | 62 | 761 |
| `extra/telemetry.csv` | Telemetría | 70 | 897 |
| `extra/dev-tools.csv` | Herramientas de desarrollo y prueba | 144 | 1.811 |
| `extra/misc.csv` | Varios | 53 | 516 |
| **Subtotal** | 15 archivos | **4.913** | **58.913** |

**Total: 34 archivos, 7.833 términos distintos (sin duplicados según `target`), 101.647 filas de correspondencia.**

## Notas

- **Origen de las traducciones y alineación.** Todo el texto procede de los **archivos de idioma oficiales de Minecraft: Java Edition** (replicados por [misode/mcmeta](https://github.com/misode/mcmeta), rama `assets`, ruta `assets/minecraft/lang/<locale>.json`; para este idioma, `es_es.json`). Son, por tanto, **localizaciones oficiales** y no traducciones secundarias ni generadas por máquina. La alineación se hace por la clave del archivo de idioma: cada término se emite una vez por cada *otro* idioma, de modo que el número de filas es mucho mayor que el de términos.
- **Etiquetas de idioma.** En esta carpeta `tgt_lng` es siempre `es-ES` e indica el idioma de destino; `source` puede ser cualquiera de los otros 13 idiomas: `zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `ru-RU`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`.
- **Codificación.** Todos los CSV están en **UTF-8 con BOM**, con saltos de línea **CRLF** y una fila de encabezado; los campos que contienen comas o comillas se escapan según la RFC 4180. Excel los abre directamente sin cambiar la codificación; este README es UTF-8 sin BOM.
- **Limitaciones conocidas.** El número de filas varía ligeramente entre idiomas, porque un término se omite cuando un idioma no tiene traducción para él o cuando su forma coincide con la del idioma de destino. Las filas de comparación y los términos no son lo mismo: las 34 categorías suman 8.559 `entries`, el número de objetos con nombre de los archivos de idioma oficiales asignados a esas categorías, incluidas las entradas sin traducir en este idioma. El recuento de esta carpeta sin duplicados según `target` es 7.833 y responde a otra definición. La definición completa está en la sección «Data Overview» de `../../README.md`, en la raíz del juego. Una misma denominación puede aparecer en varias categorías, y la terminología sigue la localización oficial, incluso cuando los nombres quedan sin traducir.
- **Glosario complementario.** La carpeta hermana `../../minecraft-glossary-supplement/` añade los nombres estándar de la wiki de Minecraft, solo para chino simplificado y tradicional; puede usarse junto con este glosario.
- **Reproducción.** Desde la raíz del juego, `python tools/build_glossary.py` reconstruye este glosario a partir de los archivos de idioma oficiales (el script lee un directorio externo de materiales con `mcmeta_lang/<locale>.json` y escribe en `minecraft-glossary/`); `python tools/verify_output.py` vuelve a comprobar cada recuento de filas contra `tools/glossary_counts.json`, y `python tools/make_readme.py` regenera los README de las bibliotecas.

## Aviso legal

Este directorio es una base de terminología de traducción **no oficial**, mantenida por una persona para estudio personal, investigación y coincidencia de terminología en herramientas de traducción asistida por IA (incluida, entre otras, Immersive Translate). No existe ninguna relación de dependencia, licencia, cooperación, representación o representación oficial con los desarrolladores, editores, distribuidores, operadores o titulares de derechos de Minecraft; los nombres aquí incluidos no representan ninguna postura oficial, no se garantiza que sean siempre exactos, completos o coherentes con la versión actual del juego y **no deben considerarse el glosario oficial ni archivos de localización oficiales de ningún juego**.

Los nombres de juegos, personajes, nombres propios y marcas pertenecen a sus respectivos titulares, y este proyecto no reclama derecho alguno sobre ellos. Toda responsabilidad derivada del uso de este proyecto y de las traducciones generadas a partir de él recae en el usuario. Si algún titular considera que un contenido es inadecuado, puede escribirnos mediante GitHub Issues / Pull Request; el responsable lo verificará y lo modificará o eliminará.

Las condiciones completas están en `README.md` / `README_EN.md` / `README_JP.md` de la raíz del repositorio.

---

**Game-translation-terminology-database es un proyecto personal independiente y no mantiene ninguna relación de pertenencia, autorización, cooperación ni representación con este juego, sus desarrolladores, editores, distribuidores o titulares de derechos.**
