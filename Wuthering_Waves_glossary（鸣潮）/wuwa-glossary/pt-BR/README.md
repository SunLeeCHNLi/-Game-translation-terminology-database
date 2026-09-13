# Wuthering Waves（鸣潮）Base de terminologia — Português（`pt-BR`）

[← Voltar à visão geral do jogo](../../README.md) ｜ [← Descrição da sub-biblioteca wuwa-glossary](../README.md)

Este diretório é a base de terminologia de Wuthering Waves com **`pt-BR` (português) como idioma de destino**. Contém **123,230** verbetes e **648,957** linhas de correspondência (as linhas de dados dos 23 arquivos CSV deste diretório, cerca de **62.0 MiB**). A coluna `tgt_lng` é sempre `pt-BR` e a coluna `source` traz a forma em cada um dos outros 9 idiomas (`zh-CN` (简体中文), `zh-TW` (繁體中文), `en-US` (English), `ja-JP` (日本語), `ko-KR` (한국어), `fr-FR` (Français), `de-DE` (Deutsch), `es-ES` (Español), `th-TH` (ภาษาไทย)), de modo que o mesmo texto do jogo pode ser localizado a partir de qualquer um deles.

## Arquivos

Este diretório tem **estrutura plana**: os 23 CSVs de categoria ficam diretamente aqui e não há subdiretório adicional:

- `characters.csv` — Nomes de personagens
- `weapons.csv` — Nomes de armas
- `echoes.csv` — Ecos
- `skills.csv` — Habilidades
- `resonant-chains.csv` — Correntes de ressonância
- `quests.csv` — Missões
- `dungeons.csv` — Masmorras e desafios
- `regions.csv` — Regiões e mapa
- `factions.csv` — Facções e potências
- `items.csv` — Itens e materiais
- `monsters.csv` — Monstros e criaturas
- `npcs.csv` — NPCs e falantes
- `achievements.csv` — Conquistas
- `activities.csv` — Eventos e modos de jogo
- `buffs.csv` — Buffs e efeitos
- `voice-lines.csv` — Vozes de personagens
- `archives.csv` — Arquivos e leituras
- `terms.csv` — Termos e enciclopédia
- `system.csv` — Textos do sistema
- `ui.csv` — Textos de interface
- `tutorials.csv` — Tutoriais
- `story.csv` — Textos de história
- `other.csv` — Outros

Todos os arquivos têm três colunas, `source,target,tgt_lng`, com uma linha de cabeçalho: para o idioma de destino indicado em `tgt_lng`, `target` é a tradução e `source` é o texto em **um dos outros idiomas**. Assim, cada verbete aparece uma vez por idioma restante como linha `source` (linhas duplicadas e idênticas foram mescladas, portanto o número de linhas não é nove vezes o de verbetes). Os arquivos podem ser importados diretamente em ferramentas CAT ou em softwares de correspondência terminológica como o Immersive Translate.

## Categorias e contagem

| Categoria | Tema | Verbetes | Linhas de correspondência |
| --- | --- | --- | --- |
| `characters.csv` | Nomes de personagens | 1,230 | 5,258 |
| `weapons.csv` | Nomes de armas | 820 | 2,972 |
| `echoes.csv` | Ecos | 1,000 | 6,114 |
| `skills.csv` | Habilidades | 5,344 | 30,804 |
| `resonant-chains.csv` | Correntes de ressonância | 784 | 6,119 |
| `quests.csv` | Missões | 2,807 | 14,517 |
| `dungeons.csv` | Masmorras e desafios | 1,910 | 10,514 |
| `regions.csv` | Regiões e mapa | 2,229 | 16,092 |
| `factions.csv` | Facções e potências | 8 | 44 |
| `items.csv` | Itens e materiais | 8,384 | 55,588 |
| `monsters.csv` | Monstros e criaturas | 685 | 4,590 |
| `npcs.csv` | NPCs e falantes | 14,172 | 63,310 |
| `achievements.csv` | Conquistas | 2,563 | 22,179 |
| `activities.csv` | Eventos e modos de jogo | 9,531 | 64,429 |
| `buffs.csv` | Buffs e efeitos | 270 | 2,090 |
| `voice-lines.csv` | Vozes de personagens | 7,374 | 32,440 |
| `archives.csv` | Arquivos e leituras | 839 | 6,582 |
| `terms.csv` | Termos e enciclopédia | 1,672 | 11,875 |
| `system.csv` | Textos do sistema | 9,756 | 65,832 |
| `ui.csv` | Textos de interface | 13,866 | 78,457 |
| `tutorials.csv` | Tutoriais | 6,253 | 32,247 |
| `story.csv` | Textos de história | 29,841 | 103,562 |
| `other.csv` | Outros | 1,892 | 13,342 |
| **Total** | **23 categorias** | **123,230** | **648,957** |

“Verbetes” é o número de verbetes sem duplicatas (um verbete = uma chave de texto do jogo); o valor vem do campo `concepts` de `tools/_counts.json` e é **comum a toda a base e independente do idioma de destino**. “Linhas de correspondência” é o número real de linhas de dados do CSV dessa categoria neste diretório. Um mesmo texto pode pertencer a várias categorias, por isso a soma das linhas por categoria é maior que o número de verbetes sem duplicatas.

## Observações

- **Origem das traduções**: a coluna `target` é copiada tal como está dos arquivos de localização do próprio jogo ([Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data), `Textmaps/<lang>/multi_text/MultiText.json`, jogo 3.6.0; algumas chaves são completadas por [Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData), `TextMap/<lang>/MultiText.json`, jogo 3.1.0). São os termos oficiais do jogo, não uma tradução de segunda mão.
- **Alinhamento**: as linhas são alinhadas pela chave de texto do jogo (por exemplo `RoleInfo_1402_Name`); a mesma chave escrita em outro idioma torna-se a linha `source` do `target` deste diretório.
- **Etiqueta de idioma**: `tgt_lng` é fixada no código de idioma deste diretório e coincide com o nome do diretório.
- **Codificação**: todos os CSVs são **UTF-8 com BOM**, com quebras de linha **CRLF** e linha de cabeçalho; campos com vírgulas ou aspas são escapados conforme a RFC 4180, de modo que abrem diretamente no Excel.
- **Limitações conhecidas**: os diálogos da história frase por frase (cerca de 170.000 linhas por idioma) não são incluídos por padrão; se desejado, podem ser gerados com a opção `--with-dialogue`, descrita em `../README.md`. Textos muito longos são truncados por categoria por `MAX_LEN` em `tools/wuwa_config.py`. `ru-RU`, `id-ID` e `vi-VN` são arquivos vazios na origem e por isso não constam, enquanto `it-IT` e `tr-TR` não são idiomas de texto suportados pelo jogo.

## Aviso legal

Este diretório é uma base de terminologia **não oficial**, organizada e mantida pessoalmente, destinada apenas ao estudo pessoal, à pesquisa e à correspondência de termos em softwares de tradução com IA (incluindo, mas não se limitando ao Immersive Translate). Não há qualquer relação de subordinação, licenciamento, cooperação, representação ou representação oficial com desenvolvedores, publicadoras, distribuidoras, operadoras ou titulares de direitos dos jogos envolvidos; as traduções aqui presentes não representam posição oficial, não há garantia de que sejam exatas, completas ou coerentes com a versão atual do jogo e **não devem ser consideradas o glossário oficial nem um arquivo de localização oficial de qualquer jogo**. Nomes de jogos, nomes de personagens, nomes próprios e marcas pertencem aos respectivos titulares, e este projeto não reivindica qualquer direito sobre eles. Se algum titular considerar algum conteúdo inadequado, entre em contato por GitHub Issues / Pull Requests; o conteúdo será verificado e alterado ou removido. Os termos completos estão em `README.md` / `README_EN.md` / `README_JP.md` na raiz do repositório.
