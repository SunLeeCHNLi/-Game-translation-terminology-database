# Glossário de Genshin Impact — Português (`pt-BR`)

[← Voltar à descrição geral do jogo](../../README.md) · [简体中文](README_zh-CN.md)

Este diretório é o glossário de terminologia de *Genshin Impact* com o **português (`pt-BR`) como idioma de destino**: **8.186 termos** somando as 27 categorias do catálogo global, das quais **89.444 linhas de correspondência** pertencem a este idioma. A coluna `tgt_lng` é sempre `pt-BR`; cada linha traz em `source` a grafia do mesmo termo em **um dos outros 13 idiomas**, e em `target` a tradução em português. Os arquivos são separados por **categoria**, um CSV por categoria.

## Arquivos

- `characters（Personagens）.csv`, `talents（Talentos）.csv`, `constellations（Constelações）.csv`, `weapons（Armas）.csv`, `materials（Materiais）.csv`, `foods（Comidas）.csv`, `crafts（Materiais de fabricação）.csv`, `artifacts（Artefatos）.csv`, `domains（Domínios）.csv`, `enemies（Inimigos）.csv`, `animals（Animais）.csv`, `outfits（Trajes）.csv`, `windgliders（Asas Planadoras）.csv`, `namecards（Cartões de visita）.csv`, `geographies（Nomes de lugares）.csv`, `achievements（Conquistas）.csv`, `adventureranks（Textos de nível de aventureiro）.csv` — 17 arquivos de categoria principal
- `tcg-action-cards（Cartas de ação）.csv`, `tcg-character-cards（Cartas de personagem）.csv`, `tcg-enemy-cards（Cartas de inimigo）.csv`, `tcg-summons（Invocações）.csv`, `tcg-status-effects（Efeitos de estado）.csv`, `tcg-keywords（Palavras-chave）.csv`, `tcg-card-backs（Versos de carta）.csv`, `tcg-card-boxes（Caixas de cartas）.csv`, `tcg-detailed-rules（Regras detalhadas）.csv`, `tcg-level-rewards（Recompensas de nível）.csv` — 10 arquivos da subcategoria TCG (Jogo de Invocação das Sete)

Total: **27 arquivos CSV**. Todos têm o mesmo formato de três colunas:

| source | target | tgt_lng |
| --- | --- | --- |
| Alhacén | Alhaitham | pt-BR |
| Аль-Хайтам | Alhaitham | pt-BR |

Estrutura de diretórios:

```text
pt-BR/
├── characters（Personagens）.csv
├── talents（Talentos）.csv
├── constellations（Constelações）.csv
├── weapons（Armas）.csv
├── materials（Materiais）.csv
├── foods（Comidas）.csv
├── crafts（Materiais de fabricação）.csv
├── artifacts（Artefatos）.csv
├── domains（Domínios）.csv
├── enemies（Inimigos）.csv
├── animals（Animais）.csv
├── outfits（Trajes）.csv
├── windgliders（Asas Planadoras）.csv
├── namecards（Cartões de visita）.csv
├── geographies（Nomes de lugares）.csv
├── achievements（Conquistas）.csv
├── adventureranks（Textos de nível de aventureiro）.csv
└── tcg-<分类>.csv
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
| characters | `characters（Personagens）.csv` | 122 | 577 |
| talents | `talents（Talentos）.csv` | 125 | 632 |
| constellations | `constellations（Constelações）.csv` | 125 | 632 |
| weapons | `weapons（Armas）.csv` | 249 | 2.823 |
| materials | `materials（Materiais）.csv` | 919 | 10.636 |
| foods | `foods（Comidas）.csv` | 398 | 4.541 |
| crafts | `crafts（Materiais de fabricação）.csv` | 295 | 3.522 |
| artifacts | `artifacts（Artefatos）.csv` | 63 | 727 |
| domains | `domains（Domínios）.csv` | 284 | 3.636 |
| enemies | `enemies（Inimigos）.csv` | 346 | 4.103 |
| animals | `animals（Animais）.csv` | 223 | 2.647 |
| outfits | `outfits（Trajes）.csv` | 150 | 1.869 |
| windgliders | `windgliders（Asas Planadoras）.csv` | 18 | 211 |
| namecards | `namecards（Cartões de visita）.csv` | 289 | 3.606 |
| geographies | `geographies（Nomes de lugares）.csv` | 268 | 3.389 |
| achievements | `achievements（Conquistas）.csv` | 1.548 | 19.461 |
| adventureranks | `adventureranks（Textos de nível de aventureiro）.csv` | 21 | 169 |
| **Subtotal** | 17 arquivos | — | **63.181** |

### Subcategorias de TCG (`tcg-`)

| Subcategoria | Arquivo | Termos | Linhas |
| --- | --- | ---: | ---: |
| action-cards | `tcg-action-cards（Cartas de ação）.csv` | 927 | 9.605 |
| character-cards | `tcg-character-cards（Cartas de personagem）.csv` | 149 | 929 |
| enemy-cards | `tcg-enemy-cards（Cartas de inimigo）.csv` | 134 | 1.114 |
| summons | `tcg-summons（Invocações）.csv` | 152 | 1.139 |
| status-effects | `tcg-status-effects（Efeitos de estado）.csv` | 1.159 | 11.215 |
| keywords | `tcg-keywords（Palavras-chave）.csv` | 139 | 1.511 |
| card-backs | `tcg-card-backs（Versos de carta）.csv` | 39 | 407 |
| card-boxes | `tcg-card-boxes（Caixas de cartas）.csv` | 7 | 32 |
| detailed-rules | `tcg-detailed-rules（Regras detalhadas）.csv` | 11 | 142 |
| level-rewards | `tcg-level-rewards（Recompensas de nível）.csv` | 26 | 169 |
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
