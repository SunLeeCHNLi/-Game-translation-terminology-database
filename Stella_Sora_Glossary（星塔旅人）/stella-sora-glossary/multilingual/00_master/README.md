# 《星塔旅人》Stella Sora 五语并排总表（`multilingual/`）

由本地游戏多语言文本库 `StellaSoraData-main`（官方 CN / EN / JP / KR / TW 五区文本）逐键对齐生成。
每个词条在五种语言中的 ID 完全一致，因此互为官方译文，未经人工二次翻译。

本目录（`Stella_Sora_Glossary（星塔旅人）/multilingual/`）是**五语并排的原始总表**，不是单目标语言的术语库，
因此没有语言级 `README.md` / `README_zh-CN.md`；以某一语言为目标语言的拆分结果在游戏根目录下的
`zh-CN/`、`zh-TW/`、`en-US/`、`ja-JP/`、`ko-KR/` 五个目录中。游戏级总说明见游戏根目录的
`README.md` / `README_EN.md` / `README_JP.md`。

## 总量

- 词条总数：**12292** 条（五种语言的词条数一致，差异只出现在单语言目录的 `11_ui` 分类）
- 语言：`zh-CN`（简中）、`en-US`（英文）、`ja-JP`（日文）、`ko-KR`（韩文）、`zh-TW`（繁中）——五种语言全部收录
- 分类：15 个专属词库
- 对照行数：15 个分类的 `NN_xxx_glossary.csv` 合计 **147462** 行（每条词条最多 12 行）
- 生成日期：2026-09-11

## 目录结构

```text
multilingual/                     五语并排总表（游戏根目录下）
  01_character/      角色名称           287 条
  02_skill/          技能名称           628 条
  03_potential/      潜能名称          1457 条
  04_disc/           唱片 / Disc      234 条
  05_item/           道具             558 条
  06_equipment/      装备              15 条
  07_enemy/          敌人             399 条
  08_stage/          关卡            1019 条
  09_event/          活动             581 条
  10_system/         系统术语          1055 条
  11_ui/             UI术语          4248 条
  12_story/          剧情专有名词         527 条
  13_faction/        阵营              21 条
  14_location/       地点              27 条
  15_terminology/    游戏机制术语        1236 条
  00_master/
    index.csv                  分类索引与词条数
    source_mapping.csv         来源表 → 分类 的映射明细（219 行）
    StellaSora_all_terms.csv   全部分类的合并总表（12292 行）
    README.md                  本说明
  StellaSora_Glossary.xlsx     同一份数据的 Excel 工作簿（目录 + 15 个分类，共 16 个工作表）
```

- 每个分类文件夹内含 `NN_xxx_terms.csv` 与 `NN_xxx_glossary.csv` 两个文件；
- 生成脚本已移到游戏根目录的 `tools/`（`build_glossary.py`、`split_by_language.py`），本目录下不再有 `tools/`；
- `source_mapping.csv` 与 `StellaSora_Glossary.xlsx` 由生成管线之外的一次性步骤产出，`tools/` 下的两个脚本都不会生成它们。

## 文件格式

每个分类文件夹内含两个文件：

**1. `NN_xxx_terms.csv` —— 多语对照总表**

| id | zh-CN | en-US | ja-JP | ko-KR | zh-TW | src_table |
| --- | --- | --- | --- | --- | --- | --- |
| Character.103.1 | 琥珀 | Amber | コハク | 코하쿠 | 琥珀 | Character.json |

- `id`：游戏内原始文本键，可用于回查、比对与自动化更新
- `src_table`：该词条取自哪张数据表
- 一条词条一行，五种语言并排；`terms.csv` 的行数即该分类的词条数（15 个分类合计 12292 行，与 `StellaSora_all_terms.csv` 的 12292 行一致）

**2. `NN_xxx_glossary.csv` —— 术语表（source / target / tgt_lng）**

按需求的表格格式导出，四种语言两两成对，可直接导入 CAT / 术语管理工具：

| source | target | tgt_lng |
| --- | --- | --- |
| Amber | 琥珀 | zh-CN |
| 琥珀 | Amber | en-US |
| Amber | コハク | ja-JP |
| 코하쿠 | 琥珀 | zh-CN |

每条词条会展开成最多 12 行（zh-CN / en-US / ja-JP / ko-KR 四语的 4×3 有序语言对），
因此无论以哪种语言作为源语言，都能直接检索。文件均为 UTF-8 with BOM、CRLF 换行，
Excel 双击即可正确显示中日韩文字。

> 并非每条都是满 12 行：某一侧缺译文的语言对会被跳过，15 个分类合计 147462 行
> （满值应为 12292 × 12 = 147504，差额 42 行全部来自 `11_ui`，该分类有少量 UI 文本在个别语区没有独立译文）。

## 各分类来源与统计

| 分类 | 主题 | 词条数 | 对照行 | 主要来源表 |
| --- | --- | --- | --- | --- |
| `01_character` | 角色名称 | 287 | 3444 | Character / CharacterSkin / CharacterDes / CharacterTag / NPCConfig / BoardNPC / SoldierCharacter / TrialCharacter / AffinityLevel + 角色头像形象（Item Type 3·10·18） |
| `02_skill` | 技能名称 | 628 | 7536 | Skill（技能名）/ MainSkill（主控技）/ SecondarySkill（援护技）/ SubNoteSkill / SkillInstance / SkillInstanceType |
| `03_potential` | 潜能名称 | 1457 | 17484 | 潜能（Item Type 6 Stype 41·42，共 1044 条）/ Talent 天赋 / TalentGroup / SoldierPotential / TowerDefensePotential / VampireTalent / PotentialPreset |
| `04_disc` | 唱片 / Disc | 234 | 2808 | DiscIP（唱片名与主题曲名）/ DiscTag（唱片标签）/ 唱片本体（Item Type 7）/ 曲调素材（Item Type 2 Stype 40）/ 秘纹素材（Stype 12） |
| `05_item` | 道具 | 558 | 6696 | Item 各类道具、素材、货币、礼盒 / ActivityGoods / ResidentGoods / MallShop / MallPackage / MiningTreasure / Production / ThrowGiftItem / TowerDefenseItem / GoldenSpyItem / MallGem |
| `06_equipment` | 装备 | 15 | 180 | CharGem 纹章 / CharGemInstance 纹章试炼 / CharGemInstanceType（游戏内装备位由“秘纹 Disc”承担，已归入 04_disc） |
| `07_enemy` | 敌人 | 399 | 4788 | MonsterManual 怪物图鉴 / TowerDefenseMonster / RegionBoss / WeekBossType / TravelerDuelBoss / ScoreBossAbility / ScoreBossGetControl |
| `08_stage` | 关卡 | 1019 | 12228 | 各玩法关卡与章节：Chapter / StoryChapter / StorySet* / DailyInstance / InfinityTower* / JointDrill* / RegionBossLevel / WeekBossLevel / TowerDefenseLevel / ActivityLevelsLevel / CookieLevel / BreakOutLevel / TutorialLevel / VampireSurvivor / 各类词条（Affix） |
| `09_event` | 活动 | 581 | 6972 | Activity* 活动组/活动任务/活动商店/活动剧情 / StarTowerEvent* 星塔事件 / EventOptions / MiningQuest / TowerDefenseQuest / BdConvert* |
| `10_system` | 系统术语 | 1055 | 12660 | OpenFunc 功能名 / ErrorCode / Gacha* 卡池 / Agent 委托 / 各类任务（Daily/Weekly/Periodic/Guide/Level/好感度 类）/ WorldClass / NotificationConfig |
| `11_ui` | UI术语 | 4248 | 50934 | UIText（界面用语）/ TopBar / JumpTo / Achievement 成就名 / Honor 荣誉称号 / Title 头衔 / PlayerHead 玩家头像 / MailTemplate / MainScreenCG / CharacterCG / StorySetTab |
| `12_story` | 剧情专有名词 | 527 | 6324 | Story 主线 / Plot 旅人剧情 / StoryEvidence / StoryPreview / NPCAffinityPlot / CharacterArchiveContent 角色档案 / Dating* 邀约剧情 / StarTowerTalk / MangaLoading |
| `13_faction` | 阵营 | 21 | 252 | Force 阵营 / ContentWord 专有名词（诺瓦帝国、恩惠意志等） |
| `14_location` | 地点 | 27 | 324 | DatingLandmark 邀约地点 / StarTower 星塔名 / 人工校订地名（菲莱、埃摩、贝林港、米拉什、苍梧城等，译文取自官方文本对齐） |
| `15_terminology` | 游戏机制术语 | 1236 | 14832 | Word 状态与机制词条 / EffectDesc 属性词条 / DictionaryDiagram·DictionaryEntry 游戏辞典 / FateCard 命运卡 / PenguinCard 系列 / SoldierStarterCard·SoldierStrategyCard / StarTowerGrowthNode / MiningSupport / VampireTalentDesc 等玩法机制名 |
| **合计** | | **12292** | **147462** | |

## 提取与筛选规则

- 仅提取“名称/标签”字段（通常为 `.1`，唱片表取 `.1/.2/.3`），**不收录**描述、数值、台词正文等长文本；
- `Item.json` 依据配置表的 `Type`/`Stype` 精确分流道具、潜能、唱片、纹章、头像等类别；
- 界面文本（UIText 等）只保留短术语（简中 ≤24 字且不含句末标点），过滤掉整句提示；
- 同一分类内如出现五语内容完全一致的重复词条，会合并为一条（保留首次出现的来源表 ID）；
- 已剔除 `【不要翻译】`、`【废弃】`、`[no trans]` 等占位与废弃条目；
- 已清除 `<color=…>`、`<sprite …>` 等富文本标记。

## 生成与复现

```bash
# 生成本目录（五语并排总表）。脚本使用写死的外部绝对路径：
#   输入 E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main
#   输出 E:\Download\BT\Codex_input\StellaSora_Glossary
python tools/build_glossary.py

# 由本目录拆分为单语言术语库。脚本同样使用外部绝对路径
# E:\Download\BT\Codex_input\StellaSora_Glossary，并把 _summary.json 写到该外部根目录
python tools/split_by_language.py
```

两个脚本都在游戏根目录的 `tools/` 下，且**都不读写本仓库**：本目录的内容是外部生成管线跑完后复制进来的快照。

## 已知限制

- 台词、剧情正文、道具描述等长篇内容不在术语库范围内，如需可另行导出为翻译记忆库（TMX/双语对照）；
- `14_location` 中除 `DatingLandmark` 与 `StarTower` 外，其余地名在游戏数据里没有独立表，
  已从角色档案地址、成就、故事标题等官方对齐文本中人工校订补入，并标注来源为 `curated (aligned in-game text)`；
- `06_equipment` 仅 15 条：本作没有传统武器/防具表，装备位由“秘纹（Disc）”承担。
