# 星塔旅人（Stella Sora）五语并排总表（`multilingual/`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录是《星塔旅人》术语库**五语并排的原始总表**，把全部 **12292** 条词条按「一条一行」摊开，五种语言并排展示，便于横向比对与二次加工。以单一语言为目标语言的拆分结果在上一层目录的 `../zh-CN/`、`../en-US/` 等语言文件夹中。

## 目录结构

```text
multilingual/
├── 00_master/
│   ├── index.csv                  分类索引与词条数（15 个分类 + 1 行 TOTAL）
│   ├── source_mapping.csv         来源表 → 分类 的映射明细（219 行）
│   ├── StellaSora_all_terms.csv   全部分类的合并总表（12292 行）
│   └── README.md                  本说明
├── 01_character/ … 15_terminology/   15 个分类目录，各含 terms 与 glossary 两个 CSV
└── StellaSora_Glossary.xlsx       同一份数据的 Excel 工作簿（16 个工作表）
```

每个分类目录内含两个文件：`NN_xxx_terms.csv`（多语并排）与 `NN_xxx_glossary.csv`（`source,target,tgt_lng` 对照表）。

## 文件格式

**1. `NN_xxx_terms.csv` —— 多语对照总表**

| id | zh-CN | en-US | ja-JP | ko-KR | zh-TW | src_table |
| --- | --- | --- | --- | --- | --- | --- |
| Character.103.1 | 琥珀 | Amber | コハク | 코하쿠 | 琥珀 | Character.json |

**2. `NN_xxx_glossary.csv` —— 术语表（`source,target,tgt_lng`）**

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| 琥珀 | Amber | en-US |

**3. `00_master/StellaSora_all_terms.csv` —— 合并总表**

| 列 | 说明 |
| --- | --- |
| `category` | 分类编号，例如 `01_character` |
| `category_label` | 分类中文名 |
| `id` | 词条 ID（游戏内原始文本键） |
| `zh-CN` | 简体中文 |
| `en-US` | 英文 |
| `ja-JP` | 日文 |
| `ko-KR` | 韩文 |
| `zh-TW` | 繁体中文 |
| `src_table` | 该词条取自哪张数据表 |

## 各分类条数

| 分类 | 主题 | 条数 | 对照行数 |
| --- | --- | ---: | ---: |
| `01_character` | 角色名称 | 287 | 3444 |
| `02_skill` | 技能名称 | 628 | 7536 |
| `03_potential` | 潜能名称 | 1457 | 17484 |
| `04_disc` | 唱片 / Disc | 234 | 2808 |
| `05_item` | 道具 | 558 | 6696 |
| `06_equipment` | 装备 | 15 | 180 |
| `07_enemy` | 敌人 | 399 | 4788 |
| `08_stage` | 关卡 | 1019 | 12228 |
| `09_event` | 活动 | 581 | 6972 |
| `10_system` | 系统术语 | 1055 | 12660 |
| `11_ui` | UI术语 | 4248 | 50934 |
| `12_story` | 剧情专有名词 | 527 | 6324 |
| `13_faction` | 阵营 | 21 | 252 |
| `14_location` | 地点 | 27 | 324 |
| `15_terminology` | 游戏机制术语 | 1236 | 14832 |
| **合计** | | **12292** | **147462** |

## 说明

- 所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头。
- 各语言词条 ID 完全一致，互为官方译文，未经人工二次翻译；`glossary` 表按 `source/target/tgt_lng` 展开，同一条目最多 12 行。
- `StellaSora_Glossary.xlsx` 与 `00_master/index.csv`、`00_master/source_mapping.csv` 由生成管线之外的一次性步骤产出。
- 游戏级总说明见 `../README.md` / `../README_EN.md` / `../README_JP.md`；语言级说明见 `../<lang>/README.md`。
