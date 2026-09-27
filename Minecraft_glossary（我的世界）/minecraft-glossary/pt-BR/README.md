# Base de terminologia de 我的世界（Minecraft） — Português (`pt-BR`)

[← Voltar à visão geral do jogo](../../README.md) · [简体中文](README_zh-CN.md)

Este diretório é a base de terminologia cujo **idioma de destino é o português (`pt-BR`)**.
Contém **101,489 linhas de correspondência** em **34 arquivos CSV** (34 categorias: 19 na raiz
do diretório e 15 em `extra-`), todas com `tgt_lng` fixado em `pt-BR`; a coluna `source` reúne as
grafias dos outros 13 idiomas. As traduções-alvo vêm dos **arquivos de idioma oficiais do Minecraft
Java Edition**, não de uma retradução.

## Ficheiros

- `<categoria>.csv` (19 arquivos) — três colunas `source,target,tgt_lng`; podem ser importados diretamente em ferramentas CAT ou de gestão de terminologia
- `extra-<categoria>.csv` (15 arquivos) — mesmas três colunas, para as categorias de sistema e texto

## Categorias e contagens

| Categoria | Tema | Arquivo | Linhas |
| --- | --- | --- | --- |
| `blocks` | Blocos | `blocks（Blocos）.csv` | 25,426 |
| `items` | Itens | `items（Itens）.csv` | 9,061 |
| `entities` | Entidades | `entities（Entidades）.csv` | 2,582 |
| `biomes` | Biomas | `biomes（Biomas）.csv` | 835 |
| `enchantments` | Encantamentos | `enchantments（Encantamentos）.csv` | 553 |
| `effects` | Efeitos de status | `effects（Efeitos de status）.csv` | 514 |
| `instruments` | Instrumentos | `instruments（Instrumentos）.csv` | 98 |
| `materials` | Materiais de ornamento | `materials（Materiais de ornamentos de armadura）.csv` | 143 |
| `paintings` | Quadros | `paintings（Quadros）.csv` | 315 |
| `attributes` | Atributos | `attributes（Atributos）.csv` | 555 |
| `item-groups` | Grupos de itens | `item-groups（Grupos de itens）.csv` | 198 |
| `jukebox-songs` | Faixas de jukebox | `jukebox-songs（Músicas da jukebox）.csv` | 42 |
| `trim-patterns` | Padrões de ornamento | `trim-patterns（Padrões de ornamentos de armadura）.csv` | 234 |
| `colors` | Cores | `colors（Cores）.csv` | 184 |
| `statistics` | Estatísticas | `statistics（Estatísticas）.csv` | 1,143 |
| `maps` | Mapas | `maps（Mapas）.csv` | 422 |
| `music` | Faixas musicais | `music（Música）.csv` | 192 |
| `sound-categories` | Categorias de som | `sound-categories（Categorias de som）.csv` | 133 |
| `game-modes` | Modos de jogo | `game-modes（Modos de jogo）.csv` | 77 |

### `extra-` (sistema e texto)

| Categoria | Tema | Arquivo | Linhas |
| --- | --- | --- | --- |
| `subtitles` | Legendas | `extra-subtitles（Legendas）.csv` | 12,504 |
| `death-messages` | Mensagens de morte | `extra-death-messages（Mensagens de morte）.csv` | 1,338 |
| `advancement-titles` | Títulos de progresso | `extra-advancement-titles（Títulos de progresso）.csv` | 1,603 |
| `advancement-descriptions` | Descrições de progresso | `extra-advancement-descriptions（Descrições de progresso）.csv` | 1,641 |
| `gamerules` | Regras de jogo | `extra-gamerules（Regras de jogo）.csv` | 1,490 |
| `commands` | Comandos e argumentos | `extra-commands（Comandos e argumentos）.csv` | 10,751 |
| `gui` | Textos de interface | `extra-gui（Textos de interface）.csv` | 6,655 |
| `options` | Opções e teclas | `extra-options（Configurações e teclas）.csv` | 8,223 |
| `multiplayer` | Multijogador | `extra-multiplayer（Multijogador）.csv` | 2,019 |
| `realms` | Realms | `extra-realms（Realms）.csv` | 5,005 |
| `world-management` | Gestão de mundos | `extra-world-management（Gestão do mundo）.csv` | 3,568 |
| `resource-packs` | Pacotes de recursos e de dados | `extra-resource-packs（Pacotes de recursos e dados）.csv` | 761 |
| `telemetry` | Telemetria | `extra-telemetry（Telemetria）.csv` | 897 |
| `dev-tools` | Ferramentas de desenvolvimento e teste | `extra-dev-tools（Ferramentas de desenvolvimento e teste）.csv` | 1,811 |
| `misc` | Outros | `extra-misc（Outros）.csv` | 516 |

### Lista de ficheiros

```text
minecraft-glossary/
<lang>/                       # 14 pastas de idioma
|   blocks（Blocos）.csv
|   items（Itens）.csv
|   entities（Entidades）.csv
|   biomes（Biomas）.csv
|   enchantments（Encantamentos）.csv
|   effects（Efeitos de status）.csv
|   instruments（Instrumentos）.csv
|   materials（Materiais de ornamentos de armadura）.csv
|   paintings（Quadros）.csv
|   attributes（Atributos）.csv
|   item-groups（Grupos de itens）.csv
|   jukebox-songs（Músicas da jukebox）.csv
|   trim-patterns（Padrões de ornamentos de armadura）.csv
|   colors（Cores）.csv
|   statistics（Estatísticas）.csv
|   maps（Mapas）.csv
|   music（Música）.csv
|   sound-categories（Categorias de som）.csv
|   game-modes（Modos de jogo）.csv
|   +-- extra-               # categorias de sistema e texto
|       |-- subtitles.csv
|       |-- death-messages.csv
|       |-- advancement-titles.csv
|       |-- advancement-descriptions.csv
|       |-- gamerules.csv
|       |-- commands.csv
|       |-- gui.csv
|       |-- options.csv
|       |-- multiplayer.csv
|       |-- realms.csv
|       |-- world-management.csv
|       |-- resource-packs.csv
|       |-- telemetry.csv
|       |-- dev-tools.csv
|       \-- misc.csv
+-- de-DE/ en-US/ ... vi-VN/
```

## Notas

- **Fonte e alinhamento.** Os termos-alvo são extraídos dos arquivos de idioma oficiais do Minecraft
  Java Edition (`assets/minecraft/lang/pt_br.json`, via [misode/mcmeta](https://github.com/misode/mcmeta)),
  ou seja, são a localização oficial. Em cada arquivo, `target` é o texto em português e `source` é o
  texto correspondente em **qualquer um dos outros 13 idiomas**; o mesmo termo aparece uma vez por
  idioma de origem (linhas iguais, incluindo `source` igual a `target`, foram mescladas).

- **Rótulo de idioma.** `tgt_lng` é sempre `pt-BR` e corresponde ao locale oficial `pt_br`.

- **Codificação.** Todos os CSV estão em **UTF-8 com BOM**, com quebras de linha **CRLF** e cabeçalho na
  primeira linha; campos que contêm vírgula, aspas ou quebra de linha são escapados segundo a RFC 4180.
  O BOM e o CRLF fazem com que o Excel abra os arquivos corretamente com um duplo clique. Atenção: alguns
  campos de texto longo contêm quebras de linha dentro de aspas (cerca de 2.000 campos por idioma);
  use um analisador CSV compatível com a RFC 4180 em vez de contar linhas brutas.

- **Limitações conhecidas.** O «número de linhas de correspondência» não é o «número de entradas» — as
  `entries` das 34 categorias somam 8,559, o número de objetos de nome do jogo atribuídos a cada categoria
  nos arquivos de idioma oficiais (incluindo entradas não traduzidas nesse idioma). Definição completa na
  secção «Data Overview» do `../../README.md` na raiz do jogo. Cerca de 2.000 das linhas são apenas textos
  de interface (GUI, multijogador, Realms etc.) e não termos propriamente ditos. Termos que a localização
  oficial deixou sem tradução não geram linha. As 14 pastas de idioma têm contagens ligeiramente diferentes
  porque cada idioma tem cobertura de tradução distinta.

- **Reprodução.** `python tools/build_glossary.py` (na raiz do jogo); o script lê um diretório de dados
  externo. O mapa completo de prefixos para categorias está na tabela `CATEGORIES` do script.

## Aviso legal

Este diretório é uma base de terminologia de tradução **não oficial**, mantida a título pessoal, destinada
apenas a estudo, pesquisa e apoio à correspondência de termos em software de tradução com IA. Não existe
qualquer vínculo de subordinação, autorização, cooperação ou representação oficial com os desenvolvedores,
publicadores, distribuidores, operadores ou detentores dos direitos do jogo; os termos aqui contidos não
representam posição oficial e não devem ser considerados a terminologia oficial de nenhum jogo. Os direitos
de propriedade intelectual sobre nomes de jogos, personagens e marcas pertencem aos respetivos titulares.
O uso deste projeto e de quaisquer traduções dele derivadas é da inteira responsabilidade do utilizador.
Os termos completos constam do `README.md` / `README_EN.md` / `README_JP.md` na raiz do repositório.
