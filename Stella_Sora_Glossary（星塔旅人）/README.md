# 《星塔旅人》Stella Sora 多语术语库

共 **12,292** 条词条，按目标语言拆分为 5 套独立术语库，每套内部再按 15 个分类归档。

## 目录结构

```
StellaSora_Glossary/
  zh-CN  简体中文
         ├─ 00_master/                索引 + 合并总表 + 说明
         ├─ 01_character/             角色名称
         ├─ 02_skill/                 技能名称
         ├─ 03_potential/             潜能名称
         ├─ 04_disc/                  唱片 / Disc
         ├─ 05_item/                  道具
         ├─ 06_equipment/             装备
         ├─ 07_enemy/                 敌人
         ├─ 08_stage/                 关卡
         ├─ 09_event/                 活动
         ├─ 10_system/                系统术语
         ├─ 11_ui/                    UI术语
         ├─ 12_story/                 剧情专有名词
         ├─ 13_faction/               阵营
         ├─ 14_location/              地点
         └─ 15_terminology/           游戏机制术语
  en-US  English（英文）
         ├─ 00_master/                索引 + 合并总表 + 说明
         ├─ 01_character/             角色名称
         ├─ 02_skill/                 技能名称
         ├─ 03_potential/             潜能名称
         ├─ 04_disc/                  唱片 / Disc
         ├─ 05_item/                  道具
         ├─ 06_equipment/             装备
         ├─ 07_enemy/                 敌人
         ├─ 08_stage/                 关卡
         ├─ 09_event/                 活动
         ├─ 10_system/                系统术语
         ├─ 11_ui/                    UI术语
         ├─ 12_story/                 剧情专有名词
         ├─ 13_faction/               阵营
         ├─ 14_location/              地点
         └─ 15_terminology/           游戏机制术语
  ja-JP  日本語（日文）
         ├─ 00_master/                索引 + 合并总表 + 说明
         ├─ 01_character/             角色名称
         ├─ 02_skill/                 技能名称
         ├─ 03_potential/             潜能名称
         ├─ 04_disc/                  唱片 / Disc
         ├─ 05_item/                  道具
         ├─ 06_equipment/             装备
         ├─ 07_enemy/                 敌人
         ├─ 08_stage/                 关卡
         ├─ 09_event/                 活动
         ├─ 10_system/                系统术语
         ├─ 11_ui/                    UI术语
         ├─ 12_story/                 剧情专有名词
         ├─ 13_faction/               阵营
         ├─ 14_location/              地点
         └─ 15_terminology/           游戏机制术语
  ko-KR  한국어（韩文）
         ├─ 00_master/                索引 + 合并总表 + 说明
         ├─ 01_character/             角色名称
         ├─ 02_skill/                 技能名称
         ├─ 03_potential/             潜能名称
         ├─ 04_disc/                  唱片 / Disc
         ├─ 05_item/                  道具
         ├─ 06_equipment/             装备
         ├─ 07_enemy/                 敌人
         ├─ 08_stage/                 关卡
         ├─ 09_event/                 活动
         ├─ 10_system/                系统术语
         ├─ 11_ui/                    UI术语
         ├─ 12_story/                 剧情专有名词
         ├─ 13_faction/               阵营
         ├─ 14_location/              地点
         └─ 15_terminology/           游戏机制术语
  zh-TW  繁體中文（繁中）
         ├─ 00_master/                索引 + 合并总表 + 说明
         ├─ 01_character/             角色名称
         ├─ 02_skill/                 技能名称
         ├─ 03_potential/             潜能名称
         ├─ 04_disc/                  唱片 / Disc
         ├─ 05_item/                  道具
         ├─ 06_equipment/             装备
         ├─ 07_enemy/                 敌人
         ├─ 08_stage/                 关卡
         ├─ 09_event/                 活动
         ├─ 10_system/                系统术语
         ├─ 11_ui/                    UI术语
         ├─ 12_story/                 剧情专有名词
         ├─ 13_faction/               阵营
         ├─ 14_location/              地点
         └─ 15_terminology/           游戏机制术语
  multilingual/        原来的五语并排总表（含 Excel 工作簿）
  README.md            本说明
```

## 每套术语库内的两个文件

**`NN_xxx_glossary.csv` —— 术语表（source / target / tgt_lng）**

该语言的 `tgt_lng` 固定，`source` 是其余四种语言的写法，可直接导入术语工具：

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| コハク | 琥珀 | zh-CN |
| 코하쿠 | 琥珀 | zh-CN |

**`NN_xxx_terms.csv` —— 本语言词条清单（id / term / src_table）**

| id | term | src_table |
| --- | --- | --- |
| Character.103.1 | 琥珀 | Character.json |

## 各语言条数

| 语言 | 词条数 | 对照行数 |
| --- | --- | --- |
| `zh-CN` | 12292 | 46279 |
| `en-US` | 12288 | 46032 |
| `ja-JP` | 12289 | 46426 |
| `ko-KR` | 12292 | 45950 |
| `zh-TW` | 12292 | 46052 |

## 说明

- 译文来自游戏官方多语言文本库，各语言按同一文本键对齐，非二次翻译；
- `multilingual/` 保留了五语并排的原始总表，以及同一份数据的 `StellaSora_Glossary.xlsx`；
- 词条提取规则、来源表映射见 `multilingual/00_master/README.md` 与 `multilingual/00_master/source_mapping.csv`。
