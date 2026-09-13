# Glossário de Genshin Impact — Português (`pt-BR`)

[← Voltar à descrição geral do jogo](../../README.md) · [简体中文](README_zh-CN.md)

Este diretório é o glossário de terminologia de *Genshin Impact* com o **português (`pt-BR`) como idioma de destino**: **8.186 termos** somando as 27 categorias do catálogo global, das quais **89.444 linhas de correspondência** pertencem a este idioma. A coluna `tgt_lng` é sempre `pt-BR`; cada linha traz em `source` a grafia do mesmo termo em **um dos outros 13 idiomas**, e em `target` a tradução em português. Os arquivos são separados por **categoria**, um CSV por categoria.

## Arquivos

- `characters.csv`, `talents.csv`, `constellations.csv`, `weapons.csv`, `materials.csv`, `foods.csv`, `crafts.csv`, `artifacts.csv`, `domains.csv`, `enemies.csv`, `animals.csv`, `outfits.csv`, `windgliders.csv`, `namecards.csv`, `geographies.csv`, `achievements.csv`, `adventureranks.csv` — 17 arquivos de categoria principal
- `TCG/action-cards.csv`, `TCG/character-cards.csv`, `TCG/enemy-cards.csv`, `TCG/summons.csv`, `TCG/status-effects.csv`, `TCG/keywords.csv`, `TCG/card-backs.csv`, `TCG/card-boxes.csv`, `TCG/detailed-rules.csv`, `TCG/level-rewards.csv` — 10 arquivos da subcategoria TCG (Jogo de Invocação das Sete)

Total: **27 arquivos CSV**. Todos têm o mesmo formato de três colunas:

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | Alhaitham | pt-BR |
| Аль-Хайтам | Alhaitham | pt-BR |

Estrutura de diretórios:

```text
pt-BR/
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

## Categorias e contagens

**Termos** é o número de termos únicos daquela categoria em todo o banco (o mesmo valor para os 14 idiomas); **linhas** é o número de linhas de dados deste arquivo em `pt-BR`.

### Categorias principais

| Categoria | Arquivo | Termos | Linhas |
| --- | --- | ---: | ---: |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2.823 |
| materials | `materials.csv` | 919 | 10.636 |
| foods | `foods.csv` | 398 | 4.541 |
| crafts | `crafts.csv` | 295 | 3.522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3.636 |
| enemies | `enemies.csv` | 346 | 4.103 |
| animals | `animals.csv` | 223 | 2.647 |
| outfits | `outfits.csv` | 150 | 1.869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3.606 |
| geographies | `geographies.csv` | 268 | 3.389 |
| achievements | `achievements.csv` | 1.548 | 19.461 |
| adventureranks | `adventureranks.csv` | 21 | 169 |
| **Subtotal** | 17 arquivos | — | **63.181** |

### Subcategorias de TCG (`TCG/`)

| Subcategoria | Arquivo | Termos | Linhas |
| --- | --- | ---: | ---: |
| action-cards | `TCG/action-cards.csv` | 927 | 9.605 |
| character-cards | `TCG/character-cards.csv` | 149 | 929 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 | 1.114 |
| summons | `TCG/summons.csv` | 152 | 1.139 |
| status-effects | `TCG/status-effects.csv` | 1.159 | 11.215 |
| keywords | `TCG/keywords.csv` | 139 | 1.511 |
| card-backs | `TCG/card-backs.csv` | 39 | 407 |
| card-boxes | `TCG/card-boxes.csv` | 7 | 32 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 | 142 |
| level-rewards | `TCG/level-rewards.csv` | 26 | 169 |
| **Subtotal** | 10 arquivos | — | **26.263** |

**Total deste diretório: 27 arquivos, 89.444 linhas.**

## Notas

- **Origem das traduções e alinhamento.** Os dados vêm de [theBowja/genshin-db](https://github.com/theBowja/genshin-db) (versão de dados 7.0, cobrindo os 14 idiomas). São as **grafias de localização do próprio jogo**, não retraduções nem textos gerados automaticamente. O alinhamento é feito por termo: um mesmo objeto do jogo gera uma linha para cada idioma de origem, o que faz as contagens de linhas serem muito maiores que as de termos.
- **Etiquetas de idioma.** `tgt_lng` é sempre `pt-BR` neste diretório e indica o idioma de destino; `source` pode ser qualquer um dos outros 13 idiomas (`zh-CN`, `zh-TW`, `en-US`, `ja-JP`, `ko-KR`, `fr-FR`, `de-DE`, `es-ES`, `ru-RU`, `it-IT`, `tr-TR`, `th-TH`, `vi-VN`).
- **Codificação.** Todos os CSV estão em **UTF-8 com BOM** e quebras de linha **CRLF**, com cabeçalho na primeira linha; campos que contêm vírgulas ou aspas são escapados segundo a RFC 4180. Assim o Excel abre os arquivos diretamente, sem ajustes de codificação.
- **Limitações conhecidas.** As contagens por categoria variam um pouco entre idiomas (por exemplo, algumas entradas de `achievements` ou `adventureranks` não existem em todas as línguas). Termos homônimos podem aparecer em mais de uma categoria (por exemplo, um nome de arma também presente em `TCG`), de modo que a soma das linhas por arquivo é maior que o número de termos únicos. Nomes que não foram traduzidos pela localização oficial permanecem iguais ao original.
- **Glossário complementar.** O diretório irmão `genshin-glossary-supplement/` reúne termos ausentes deste banco principal e pode ser usado em conjunto com ele. Detalhes no `README.md` de cada biblioteca.

## Aviso legal

Este diretório é um banco de terminologia de tradução **não oficial**, mantido por uma pessoa física, destinado apenas a estudo, pesquisa e apoio a softwares de tradução assistida por IA (incluindo, mas não se limitando a, o Immersive Translate). Não há qualquer vínculo de subordinação, licença, cooperação, representação ou representação oficial com os desenvolvedores, publicadores, distribuidores, operadores ou detentores de direitos dos jogos relacionados; as traduções aqui contidas não representam posição oficial e não se garante que sejam sempre exatas, completas ou condizentes com a versão atual do jogo — **este material não deve ser considerado o glossário oficial nem um arquivo de localização oficial de nenhum jogo**. Marcas registradas, nomes de personagens e demais propriedade intelectual pertencem aos seus respectivos titulares. Todo o uso é de responsabilidade do usuário.

Os termos completos estão no `README.md` / `README_EN.md` / `README_JP.md` da raiz do repositório.

---

**Game-translation-terminology-database é um projeto pessoal independente, sem qualquer vínculo, autorização, cooperação ou representação com este jogo, seus desenvolvedores, publicadores, distribuidores ou detentores de direitos.**
