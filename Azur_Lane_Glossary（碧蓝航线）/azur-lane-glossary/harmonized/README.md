# 《碧蓝航线》和谐名对照与五语总表（`harmonized`）

## [English](README_EN.md) [日本語](README_JP.md)

本目录保存《碧蓝航线》（Azur Lane）的**和谐名（CN 服替换名）对照关系**与**五语舰船名总表**。
所谓「和谐名」，指国服客户端把部分舰船原名替换为植物 / 动物类代称后所使用的名称，例如
`峰风` → `樱`、`吹雪` → `桐`；映射关系来自游戏文件 `ShareCfg/name_code.json`
（`name` = 原名，`code` = 和谐名），并与萌娘百科《碧蓝航线/名称对照表》交叉校验。

## 目录结构

```text
harmonized/
├── README.md                        本说明（简体中文）
├── README_EN.md                     英文说明
├── README_JP.md                     日文说明
├── ship-names-multilingual.csv      五语舰船名总表（唯一的多列表）
├── ship-names-harmonized.csv        原名 → 和谐名 对照（三列）
├── harmonized-names-detailed.csv    含元数据的详细对照（十二列）
├── equipment-harmonized.csv         装备和谐名对照（三列）
└── ijn-codename-aliases.csv         旧日本海军单字代称别称表（五列）
```

## 文件说明

| 文件 | 数据行数 | 用途 |
| --- | ---: | --- |
| `ship-names-multilingual.csv` | 891 | 五语总表，后续所有拆分表的基准数据 |
| `ship-names-harmonized.csv` | 1,187 | 舰船原名 → 和谐名 的扁平映射，用于批量替换 |
| `harmonized-names-detailed.csv` | 1,259 | 原名 → 和谐名 + 语言 / 舰种 / ID / 多语对照 |
| `equipment-harmonized.csv` | 8 | 装备名的和谐化对照 |
| `ijn-codename-aliases.csv` | 1,082 | 单字代称 / 别称 → 正式译名，用于指代消解 |

## 文件格式

全部 CSV 为 **UTF-8（含 BOM）**、**CRLF**、首行为表头。

| 文件 | 实际表头 |
| --- | --- |
| `ship-names-multilingual.csv` | `ship_id,zh_CN,en,ja,zh_TW,ko,english_name,ship_type_zh,ship_type_en,nation_zh,nation_en,variant` |
| `ship-names-harmonized.csv` | `source,target,tgt_lng` |
| `harmonized-names-detailed.csv` | `source,target,tgt_lng,src_lng,name_code_id,kind,ship_type,ship_id,en,ja,zh_TW,wiki_note` |
| `equipment-harmonized.csv` | `source,target,tgt_lng` |
| `ijn-codename-aliases.csv` | `source,target,tgt_lng,src_lng,name_code_id` |

### 三列表的读法

`source,target,tgt_lng` 家族（`ship-names-harmonized.csv`、`equipment-harmonized.csv`）中
`tgt_lng` 恒为 `zh-CN`，`source` 为客户端原名，`target` 为和谐名：

| `source` | `target` | `tgt_lng` |
| --- | --- | --- |
| 峰风 | 樱 | zh-CN |
| 吹雪 | 桐 | zh-CN |
| Fubuki | 桐 | zh-CN |

### `harmonized-names-detailed.csv` 的 `kind` 分布

| `kind` | 行数 | 含义 |
| --- | ---: | --- |
| `ship` | 1,251 | 舰船 |
| `equipment` | 8 | 装备 |

`src_lng` 分布：`zh-CN` 436、`en` 255、`ko` 253、`ja` 172、`zh-TW` 143。
同一和谐名对应多条原名，因此 1,259 行只对应 1,195 个不同的 `source` 与 424 个不同的 `target`。

### `ijn-codename-aliases.csv`

`src_lng` 分布：`zh-CN` 434、`en` 383、`ja` 265。`name_code_id` 指向
`ShareCfg/name_code.json` 中的条目 ID，用于把单字代称（如「貃」）与正式舰船名（如「阿武隈」）关联起来。

## 说明

- 和谐名是**国服客户端实际显示**的文本，不是译者改写，可直接作为简体中文的官方译名使用。
- 部分舰船在舰种 / 阵营 / 改造等维度上存在多态（META、μ兵装、II 型等），`variant` 列即用于标注。
- 繁体中文用 `zh_TW`（下划线），与三列表的 `zh-TW`（连字符）写法不同，转换时请勿混淆。
- 生成脚本为 `tools/build_harmonized.py`，依赖 `ship-names-multilingual.csv` 等上游产物。