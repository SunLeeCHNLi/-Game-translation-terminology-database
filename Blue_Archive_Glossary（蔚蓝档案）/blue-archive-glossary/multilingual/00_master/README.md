# 六语并排总表

把 15 个分类的全部 **7535** 条词条按「一条一行」摊开展示，方便横向比对与二次加工。

## 文件

- `00_master/all_terms_multilingual.csv` — 全部词条
- `NN_xxx/NN_xxx_multilingual.csv` — 单个分类的词条

## 列

| 列 | 说明 |
| --- | --- |
| `category` | 分类编号，例如 `01_character` |
| `category_label` | 分类中文名 |
| `id` | 词条 ID（对应官方数据的 Id / 键名） |
| `zh-CN` | 简体中文 |
| `ja-JP` | 日文 |
| `zh-TW` | 繁体中文 |
| `en-US` | 英文 |
| `ko-KR` | 韩文 |
| `th-TH` | 泰文 |
| `src_table` | 该词条来自哪张表 |

空白表示该词条在这一语言下没有找到对应写法。若想按目标语言拆开使用，
请直接取上一层目录里对应的语言文件夹。
