# 原神（Genshin Impact）多语言术语库 - 补充词库

本目录是 `genshin-glossary/` 的**补充集**，用于补齐主词库未收录的词条（尤其是 NPC、地名、敌人、任务等）。

## 数据来源

- [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)（覆盖 en / ja / zh-CN / zh-TW 四种语言）

## 与主词库的关系

- 只包含**主词库中没有的** `source/target/tgt_lng` 组合，因此可与主词库直接**叠合使用**，不会产生重复条目。
- 仅覆盖 4 种目标语言：`zh-CN`、`zh-TW`、`en-US`、`ja-JP`。
- 由于来源不同，同一词条的英/日/中写法可能与主词库存在细微差异（例如用词、标点）。

## 目录结构

```
genshin-glossary-supplement/
├── zh-CN/
│   ├── characters.csv        # 与主词库同名的主类目
│   ├── _variants.csv         # 别名/俗称/常见误写，作为额外 source 补充
│   └── extra/                # 主类目之外、原神翻译常用的额外类目
│       ├── quests.csv
│       └── ...
├── zh-TW/  en-US/  ja-JP/
└── _counts.json
```

## 文件格式

与主词库完全一致（UTF-8 含 BOM、CRLF、RFC 4180 转义）：

| source | target | tgt_lng |
| --- | --- | --- |
| Harbinger of Dawn | 黎明神剑 | zh-CN |
| 黎明の神剣 | 黎明神剑 | zh-CN |

## 类目

### 对应主词库的主类目

| 类目 | 词条来源 |
| --- | --- |
| artifacts | artifacts |
| characters | characters-*（蒙德/璃月/稻妻/须弥/枫丹/纳塔/挪德卡莱/至冬/坎瑞亚/愚人众等） |
| domains | domains |
| materials | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials |
| enemies | enemies |
| foods | foods |
| animals | living-beings |
| geographies | locations |
| weapons | weapons |

### 额外类目（`extra/`）

| 类目 | 说明 |
| --- | --- |
| extra/dialogue | 对白用语 |
| extra/facilities | 设施与建筑 |
| extra/objects | 场景物件 |
| extra/organizations | 组织与势力 |
| extra/quests | 任务名称（魔神/世界/传说/每日/部族等） |
| extra/sereniteapot | 尘歌壶 |
| extra/story | 剧情与章节 |
| extra/system | 系统与玩法术语 |
| extra/events | 活动名称 |
| extra/archives | 档案资料 |

## 行数统计

| 语言 | 主类目文件 | 数据行数 | 别名行数 |
| --- | --- | --- | --- |
| `zh-CN` | 19 | 12,237 | 333 |
| `zh-TW` | 19 | 12,221 | 332 |
| `en-US` | 19 | 13,815 | 395 |
| `ja-JP` | 19 | 13,308 | 283 |

> 行数指叠加前的新增行数；实际使用时与主词库合并即可。
