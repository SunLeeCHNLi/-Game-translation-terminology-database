# Глоссарий Genshin Impact — Русский (`ru-RU`)

[← Вернуться к общему описанию игры](../../README.md) · [简体中文](README_zh-CN.md)

Этот каталог — глоссарий терминологии *Genshin Impact* с **русским языком (`ru-RU`) в качестве целевого**: всего в глобальном каталоге **8 186 терминов** в сумме по 27 категориям, из них к этому языку относятся **89 418 строк соответствий**. Столбец `tgt_lng` всегда равен `ru-RU`; в каждой строке `source` содержит написание того же термина на **одном из остальных 13 языков**, а `target` — перевод на русский. Файлы разделены по **категориям**: одна категория — один CSV.

## Файлы

- `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv` — 17 файлов основных категорий
- `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv` — 10 файлов подкатегории TCG («Священное призывание семи»)

Всего **27 CSV-файлов**. Формат у всех одинаковый — три столбца:

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | Итэр | ru-RU |
| Leer | Итэр | ru-RU |

Структура каталога:

```text
ru-RU/
├── characters.csv
├── talents.csv
├── constellations.csv
├── weapons.csv
├── materials.csv
├── foods.csv
├── crafts.csv
├── artifacts.csv
├── domains.csv
├── enemies.csv
├── animals.csv
├── outfits.csv
├── windgliders.csv
├── namecards.csv
├── geographies.csv
├── achievements.csv
├── adventureranks.csv
└── TCG/
    ├── action-cards.csv
    ├── character-cards.csv
    ├── enemy-cards.csv
    ├── summons.csv
    ├── status-effects.csv
    ├── keywords.csv
    ├── card-backs.csv
    ├── card-boxes.csv
    ├── detailed-rules.csv
    └── level-rewards.csv
```

## Категории и количество

**Термины** — число уникальных терминов категории во всей базе (одинаково для всех 14 языков); **строки** — число строк данных в этом файле для `ru-RU`.

### Основные категории

| Категория | Файл | Термины | Строки |
| --- | --- | ---: | ---: |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2 823 |
| materials | `materials.csv` | 919 | 10 636 |
| foods | `foods.csv` | 398 | 4 541 |
| crafts | `crafts.csv` | 295 | 3 522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3 636 |
| enemies | `enemies.csv` | 346 | 4 104 |
| animals | `animals.csv` | 223 | 2 647 |
| outfits | `outfits.csv` | 150 | 1 869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3 606 |
| geographies | `geographies.csv` | 268 | 3 389 |
| achievements | `achievements.csv` | 1 548 | 19 461 |
| adventureranks | `adventureranks.csv` | 21 | 157 |
| **Итого** | 17 файлов | — | **63 170** |

### Подкатегории TCG (`TCG/`)

| Подкатегория | Файл | Термины | Строки |
| --- | --- | ---: | ---: |
| action-cards | `TCG/action-cards.csv` | 927 | 9 521 |
| character-cards | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 | 1 114 |
| summons | `TCG/summons.csv` | 152 | 1 139 |
| status-effects | `TCG/status-effects.csv` | 1 159 | 11 224 |
| keywords | `TCG/keywords.csv` | 139 | 1 571 |
| card-backs | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards | `TCG/level-rewards.csv` | 26 | 169 |
| **Итого** | 10 файлов | — | **26 248** |

**Всего в этом каталоге: 27 файлов, 89 418 строк.**

## Примечания

- **Источник переводов и выравнивание.** Данные взяты из [theBowja/genshin-db](https://github.com/theBowja/genshin-db) (версия данных 7.0, все 14 языков). Это **официальные локализационные написания самой игры**, а не повторный перевод и не машинно-сгенерированный текст. Выравнивание выполнено по терминам: один игровой объект даёт по одной строке на каждый исходный язык, поэтому число строк намного больше числа терминов.
- **Языковые метки.** В этом каталоге `tgt_lng` всегда `ru-RU` и обозначает целевой язык; `source` может быть любым из остальных 13 языков (`zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `pt-BR`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`).
- **Кодировка.** Все CSV — **UTF-8 с BOM**, переводы строк **CRLF**, первая строка — заголовок; поля с запятыми или кавычками экранированы по RFC 4180. Excel открывает файлы напрямую, без настройки кодировки.
- **Известные ограничения.** Количество строк по категориям немного различается между языками (например, часть записей `achievements` и `adventureranks` есть не во всех языках). Одинаковые термины могут встречаться в нескольких категориях (например, название оружия также в `TCG`), поэтому сумма строк по файлам превышает число уникальных терминов. Названия, не переведённые официальной локализацией, остаются в исходном виде.
- **Дополнительный глоссарий.** Соседний каталог `genshin-glossary-supplement/` содержит термины, отсутствующие в этой основной базе, и может использоваться вместе с ней; подробности — в его `README.md`.

## Отказ от ответственности

Этот каталог — **неофициальная** база терминологии перевода, поддерживаемая частным лицом и предназначенная только для личного изучения, исследований и поддержки систем машинного перевода с ИИ (включая, помимо прочего, Immersive Translate). База не состоит в отношениях подчинения, лицензирования, сотрудничества, представительства или официального представительства с разработчиками, издателями, распространителями, операторами или правообладателями соответствующих игр; приведённые переводы не выражают официальную позицию и не гарантируется их постоянная точность, полнота или соответствие текущей версии игры — **этот материал не следует считать официальным глоссарием или официальным файлом локализации какой-либо игры**. Права на названия игр, имена персонажей, термины и товарные знаки принадлежат их владельцам. Ответственность за использование несёт пользователь.

Полные условия — в `README.md` / `README_EN.md` / `README_JP.md` в корне репозитория.

---

**Game-translation-terminology-database — независимый личный проект, не связанный с этой игрой, её разработчиками, издателями, распространителями или правообладателями какими-либо отношениями подчинения, авторизации, сотрудничества или представительства.**
