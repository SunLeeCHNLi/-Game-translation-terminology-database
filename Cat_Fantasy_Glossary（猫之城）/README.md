# 《猫之城》Cat Fantasy 多语术语库

从官方多语言文本库抽取整理，共 **102,213** 条唯一词条，按目标语言拆分为 **7** 套独立术语库（合计 619,095 条对照），每套内部再按 16 个分类归档。

## 目录结构

```
Cat_Fantasy_Glossary（猫之城）/
  zh-CN  简体中文
         ├─ 00_master/              索引 + 说明
         ├─ 01_character/           角色与卡牌
         ├─ 02_skill/               技能与战斗效果
         ├─ 03_talent/              天赋与觉醒
         ├─ 04_equipment/           装备与专属武器
         ├─ 05_item/                道具与材料
         ├─ 06_enemy/               敌人与BOSS
         ├─ 07_stage/               关卡与章节
         ├─ 08_event/               活动玩法
         ├─ 09_gacha/               抽卡与兑换
         ├─ 10_shop/                商店与礼包
         ├─ 11_homeland/            家园与猫咖
         ├─ 12_system/              系统与任务
         ├─ 13_ui/                  UI与界面文本
         ├─ 14_story/               剧情专有名词
         ├─ 15_location/            地点与区域
         └─ 16_terminology/         游戏机制术语
  zh-TW 繁體中文 / en-US English / ja-JP 日本語 / ko-KR 한국어 / th-TH ภาษาไทย / id-ID Bahasa Indonesia
         （结构与 zh-CN 完全一致）
  multilingual/                       七语并排总表
  README.md                           本说明
```

## 各语言条数

| 语言代码 | 语言 | 词条数 | 对照行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 102,213 | 196,870 |
| `zh-TW` | 繁體中文 | 101,915 | 196,972 |
| `en-US` | English | 101,692 | 197,404 |
| `ja-JP` | 日本語 | 101,621 | 196,919 |
| `ko-KR` | 한국어 | 101,760 | 197,663 |
| `th-TH` | ภาษาไทย | 99,978 | 191,726 |
| `id-ID` | Bahasa Indonesia | 9,916 | 28,827 |

> `id-ID` 仅有官方 UI 文本（I18N 表）为印尼语，游戏数据表未提供印尼语实体名称，
> 因此该套术语库只包含 `13_ui` 一个分类，条数明显少于其他语言。

## 官方语言支持说明

本库整理的目标语言**以游戏官方已经实装的文本为准**，不做二次机翻：

| 语言 | 状态 |
| --- | --- |
| `zh-CN` 简体中文 | ✅ 官方实装（原始语言） |
| `zh-TW` 繁體中文 | ✅ 官方实装 |
| `en-US` English | ✅ 官方实装（见下方说明） |
| `ja-JP` 日本語 | ✅ 官方实装 |
| `ko-KR` 한국어 | ✅ 官方实装 |
| `th-TH` ภาษาไทย | ✅ 官方实装 |
| `id-ID` Bahasa Indonesia | ✅ 官方实装（仅界面文本） |
| `fr-FR` / `de-DE` / `es-ES` / `ru-RU` / `pt-BR` / `it-IT` / `tr-TR` / `vi-VN` | ❌ 官方未实装，本库不提供 |

**关于英文**：游戏文本表中英文只有一列 `en_UK`，而 I18N 文本表同时存在 `en_UK` 与 `en_US` 两套英文
（两者约 4,500 条内容不同）。本库的 `en-US` 目录中，实体名称取自 `en_UK` 列，界面文本优先取 `en_US`、
缺失时回退 `en_UK`；两套英文的原始文本都保留在 `multilingual/all_languages_master.csv` 的对应列中。

## 分类与条数（以 `zh-CN` 为例）

| 分类 | 主题 | 条数 | 内容 |
| --- | --- | --- | --- |
| `01_character` | 角色与卡牌 | 19,983 | 可战斗猫娘（卡牌）名称、猫形、职业、种族、皮肤、专属台词与角色档案 |
| `02_skill` | 技能与战斗效果 | 9,228 | 技能名称、技能关键词、被动/觉醒技能与效果说明 |
| `03_talent` | 天赋与觉醒 | 2,536 | 角色天赋名称与天赋效果 |
| `04_equipment` | 装备与专属武器 | 6,388 | 装备、专属武器、装备部位与筛选分类 |
| `05_item` | 道具与材料 | 4,650 | 消耗品、礼物、素材、货币等道具名称与说明 |
| `06_enemy` | 敌人与BOSS | 27 | 敌方目标及相关说明文本 |
| `07_stage` | 关卡与章节 | 7,278 | 主线章节、日常副本、迷宫、爬塔、挑战关卡 |
| `08_event` | 活动玩法 | 17,339 | 限时活动、节日活动、排行榜、世界BOSS等玩法 |
| `09_gacha` | 抽卡与兑换 | 53 | 卡池说明、召唤任务与兑换规则 |
| `10_shop` | 商店与礼包 | 4,589 | 商店、通行证、时装合约与各类礼包 |
| `11_homeland` | 家园与猫咖 | 8,913 | 猫咖/餐厅、钓鱼、俱乐部、家园天赋等休闲玩法 |
| `12_system` | 系统与任务 | 6,041 | 功能开关、新手引导、任务、图鉴、地区玩法、签到等 |
| `13_ui` | UI与界面文本 | 9,923 | 客户端界面文本（取自 I18N 文本表） |
| `14_story` | 剧情专有名词 | 3,180 | 剧情登场角色名、场景名、字幕与小剧场 |
| `15_location` | 地点与区域 | 449 | 地图、区域、战斗场景、电话区号等 |
| `16_terminology` | 游戏机制术语 | 1,636 | 属性、元素、克制关系、增益/减益等机制用语 |

## 文件格式

每个分类文件夹内有两个文件，均使用 **UTF-8 with BOM + CRLF**（Excel 双击可直接打开）。

**`NN_xxx_glossary.csv` —— 术语对照表（source / target / tgt_lng）**

该语言的 `tgt_lng` 固定，`source` 是其余六种语言的写法，可直接导入沉浸式翻译等术语工具：

| source | target | tgt_lng |
| --- | --- | --- |
| Enterprise | 企业 | zh-CN |
| エンタープライズ | 企业 | zh-CN |

**`NN_xxx_terms.csv` —— 本语言词条清单（id / term / src_table）**

| id | term | src_table |
| --- | --- | --- |
| Card.101005.name | 涂鸦战争 | Card/Card.txt |

- `id` = `源表名.主键.字段名`，可据此回查游戏原始数据表；
- `src_table` = 该词条在官方数据包中的相对路径（`MasterData\Setting\Data\` 之下）。

**`00_master/index.csv`** 为该语言的分类索引与条数；合并全部 16 个分类即可得到该语言的完整术语表。

## 数据来源

| 来源 | 用途 |
| --- | --- |
| [PackageInstaller/DataTable · game/CatFantasy](https://github.com/PackageInstaller/DataTable/tree/game/CatFantasy) | 官方多语言数据表（`Setting/Data`）与 I18N 文本表（`Setting/I18N`），版本 2.14.0 |
| [Moli13337/CatFantasy-2.18.1](https://github.com/Moli13337/CatFantasy-2.18.1) | 交叉核对游戏数据结构（版本 2.18.1） |
| 简中官网 [cat.fantanggame.com](https://cat.fantanggame.com/) ／ 繁中 [tw.catfantasygame.com](https://tw.catfantasygame.com/) ／ 英文 [cat.elex.com](https://cat.elex.com/) ／ 日文 [jp.catfantasygame.com](https://jp.catfantasygame.com/) ／ 韩文 [kr.catfantasygame.com](https://kr.catfantasygame.com/) ／ 东南亚 [catfantasysea.bonfiregathering.com](https://catfantasysea.bonfiregathering.com/en/) | 语言支持情况核对 |

## 生成说明

1. 扫描 `Setting/Data` 下全部 2,590 个数据表，识别带 `_zh_TW / _en_UK / _ja_JP / _ko_KR / _th_TH` 后缀的多语言字段，
   基准列（无后缀）即 `zh-CN` 原文；
2. 按数据表所属玩法模块划分到 16 个分类（映射关系见 `multilingual/00_master/source_mapping.csv`）；
3. `13_ui` 分类取自 `Setting/I18N` 哈希文本表，按 `Id` 键对齐七种语言；
4. 对 `NewChapter`（剧情表）只提取登场角色名与场景名等专有名词，剧情正文对话不纳入术语库；
5. 同一分类内按 `(source, target)` 去重；源语言与目标语言写法完全相同时不生成对照行。

每套术语库都是**按同一文本键对齐**的官方文本，非二次翻译；同一条词条会把其余六种语言全部展开为对照行，
因此也可以反向当作「`zh-CN` → 其他语言」的查询表使用。

## 已知限制

- 分类为按数据表自动归类，个别词条（如跨玩法的通用文本）可能归入相邻分类；
- 游戏数据表中敌人类名称未提供多语言列，`06_enemy` 分类条数很少；
- 文本中的占位符（如 `_name_`、`_num_`、`#num_percent_0_1_1_`、`\n`）保留官方原样，未做替换；
- 不同地区版本、游戏版本之间可能存在译名差异，本库以所引用的数据包版本为准。

## 免责声明

本文件夹为个人整理的非官方术语资料，与《猫之城》及其开发商、发行商、代理商不存在任何隶属或授权关系。
游戏名称、角色名、专有名词等知识产权归各自权利人所有。详细条款见仓库根目录 `README.md`。
