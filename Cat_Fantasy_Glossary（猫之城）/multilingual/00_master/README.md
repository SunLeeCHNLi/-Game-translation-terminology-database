# 七语并排总表

`all_languages_master.csv` 把全部 **102,213** 条词条按「一条一行」并排列出七种语言，便于整体检索与二次加工。

| 列 | 说明 |
| --- | --- |
| `id` | 词条编号，格式为 `源表名.主键.字段名`，可与各语言 `*_terms.csv` 的 `id` 对应 |
| `category` | 所属分类（见 `source_mapping.csv`） |
| `src_table` | 官方数据包中的来源表相对路径 |
| `zh-CN` ~ `id-ID` | 该词条在各语言下的官方文本，缺失则为空 |

## 目录

- `all_languages_master.csv` — 七语并排总表
- `00_master/source_mapping.csv` — 来源表 → 分类 的映射与词条数，共 379 张表

## 说明

- 本表是各语言分库的**上游总表**，各语言目录下的 `*_glossary.csv` 由它展开生成；
- `en_UK` 与 `en_US` 两套英文中，总表采用 `en_US` 优先、缺失回退 `en_UK` 的取值，与 `en-US` 目录一致；
- 若需按分类拆分，请直接使用各语言目录下的分类文件。
