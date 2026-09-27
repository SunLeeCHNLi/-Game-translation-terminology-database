# 《星布谷地》Petit Planet 多语言翻译术语库 / Petit Planet Terminology Database

收录 HoYoverse 生活模拟游戏《星布谷地》（Petit Planet / プチプラネット）的**官方多语言术语对照表**，
覆盖 **15 种目标语言**，共 **21,884** 条对照记录。
译文全部取自官方本地化数据（同一本地化 Key）与官方 HoYoLAB 公告，**不是机器翻译、不是二次翻译**。

| 名称 | 文本 |
| --- | --- |
| 简体中文 | 星布谷地 |
| 繁体中文 | 星布谷地 |
| English | Petit Planet |
| 日本語 | プチプラネット |
| 한국어 | 쁘띠플래닛 |
| Français | P'tite Planète |

**当前阶段**：Final Beta Test（官方中文：连接测试）　**公测**：2026 年冬季
**当前版本参考**：`PetitPlanet_FinalBetaTest_OSCBAndroid0.95.2`（取自官方网站下载链接）

## 数据来源与可信度

| 级别 | 来源 | 说明 | 记录数 |
| --- | --- | --- | ---: |
| 最高 | `planet.hoyoverse.com` 官方本地化文件 | 15 种语言使用**同一本地化 Key**，可一一对齐 | — |
| 最高 | HoYoLAB 官方公告（`gids=10`） | Coziness / Stardrift / Final Beta Test 官方文本，15 种语言 | — |
| 三级 | [petitplanet.life](https://petitplanet.life/) | 社区数据库，**仅英文名称**，无官方多语言文本 | 2,188 |
| 工具 | [c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) | 仅用于定位官方新闻源；**其语言字段不是游戏本地化数据** | — |
| 索引 | [petitplanet-life/petitplanet-resources](https://github.com/petitplanet-life/petitplanet-resources) | 仅为 petitplanet.life 页面索引，非官方数据仓库 | — |

- **官方已确认条目：19,696**
- 社区数据库（英文，未本地化）：2,188
- 存在多译名的 source：2,597

> 本项目为**非官方**个人整理项目，与《星布谷地》及其开发、发行、运营方无任何隶属、授权、合作或代理关系。
> 若与官方当前版本冲突，**以官方正式发布内容为准**。官方网站文案属于 **Web Only** 层级；游戏内文本以客户端为准。

## 目录结构

```text
Petit-Planet_Glossary（星布谷地）/
  terms/
    zh-CN/  ...  每个语言目录含 18 个分类文件 + 00_master.tsv
    zh-TW/  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
    pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
  Sources/sources.tsv          来源记录
  Metadata/petit-planet.json   版本信息与统计
  community-database/          petitplanet.life 英文名称清单（社区数据，未本地化）
  README.md
```

## 文件格式

所有术语文件严格为三列制表符分隔，UTF-8 (BOM) + CRLF：

```text
source	target	tgt_lng
Petit Planet	星布谷地	zh-CN
プチプラネット	星布谷地	zh-CN
Petit Planet	星布谷地	zh-TW
星海	Starsea	en-US
```

`source` 为实际本地化字符串（**不是**内部 ID）；`target` 为目标语言正式译名；`tgt_lng` 为目标语言代码。

## 语言与统计

`zh-CN` `zh-TW` `en-US` `ja-JP` `ko-KR` `fr-FR` `de-DE` `es-ES` `ru-RU` `pt-PT` `it-IT` `tr-TR` `th-TH` `vi-VN` `id-ID`

> `Português` 官方使用 **`pt-PT`**；`Bahasa Indonesia` 使用 **`id-ID`**（不是 `in-ID`）。
> 官方网站另有 `pl-pl`、`hi-in`，不在重点语言范围，未纳入。

| 目标语言 | 记录数 |
| --- | ---: |
| `zh-CN` | 1,363 |
| `zh-TW` | 1,358 |
| `en-US` | 3,545 |
| `ja-JP` | 1,303 |
| `ko-KR` | 1,304 |
| `fr-FR` | 1,298 |
| `de-DE` | 1,311 |
| `es-ES` | 1,298 |
| `ru-RU` | 1,296 |
| `pt-PT` | 1,308 |
| `it-IT` | 1,296 |
| `tr-TR` | 1,298 |
| `th-TH` | 1,304 |
| `vi-VN` | 1,304 |
| `id-ID` | 1,298 |
| **合计** | **21,884** |

| 分类 | 内容 | 记录数 |
| --- | --- | ---: |
| `00_game_title` | 游戏与测试名称 Game & Test Names | 147 |
| `01_neighbor` | 邻居与角色 Neighbors & Characters | 5,877 |
| `02_location` | 星球与地区 Planets & Locations | 315 |
| `03_item` | 道具 Items | 214 |
| `04_material` | 材料 Materials | 50 |
| `05_furniture` | 家具 Furniture | 762 |
| `06_test_version` | 测试版本 Test Versions | 615 |
| `07_cooking` | 烹饪 Cooking | 93 |
| `08_fish` | 鱼类 Fish | 92 |
| `09_bugs` | 昆虫 Bugs | 68 |
| `10_plants` | 植物与农作物 Plants & Crops | 76 |
| `11_shore` | 海岸生物 Shore-Dwellers | 47 |
| `12_shop` | 商店与经济 Shops & Economy | 510 |
| `13_neighbor_interaction` | 邻居互动 Neighbor Interaction | 14 |
| `15_event` | 活动 Events | 9 |
| `18_ui` | 系统与 UI System & UI | 6,786 |
| `21_world_term` | 世界观术语 Terminology | 3,870 |
| `22_title_tag` | 称号与标签 Titles & Tags | 2,100 |

## 社区数据库清单（未本地化）

以下英文名称来自 petitplanet.life，**只有英文，没有官方多语言文本**，因此在术语表中以
`source = target`（均为英文）记录并标记为 `community_database`，同时在此列出便于后续补充校对：

| 分类 | 英文名称数 |
| --- | ---: |
| `01_neighbor` | 14 |
| `03_item` | 214 |
| `04_material` | 50 |
| `05_furniture` | 762 |
| `06_crafting` | 239 |
| `07_cooking` | 93 |
| `08_fish` | 92 |
| `09_bugs` | 68 |
| `10_plants` | 76 |
| `11_shore` | 47 |
| `12_shop` | 510 |
| `13_neighbor_interaction` | 14 |
| `15_event` | 9 |
| **合计** | **2,188** |

## 测试阶段

| 阶段 | 官方中文 | 日期（依据官方公告） |
| --- | --- | --- |
| Final Beta Test | 连接测试 | 2026-09-22 起 |
| Stardrift Test | 星旅测试 | 2026-04-21 起 |
| Coziness Test | 居心地测试 | 2025-11 起 |
| Official Release | — | 未上线（2026 年冬季） |
| Historical / Unknown | — | 名称变更保留双记录；版本无法确认时记 `Version: Unknown`，不做猜测 |

## 已知限制

1. **游戏客户端多语言字符串未公开**：官方译文来自官方网站本地化文件与 HoYoLAB 公告；官方网页文案属 **Web Only**。
2. **道具 / 家具 / 鱼类 / 昆虫 / 食谱 / 商店**等条目目前只有 petitplanet.life 的英文名称，缺少官方多语言对照，
   因此以 `source = target`（英文）记录并标注 `community_database`，未编造任何译名。
3. 官方网站本地化文件共 443 个 Key，其中图片链接与空值已过滤；少数 Key（如 `miracle-suffix`）在多数语言中保留英文，已按实际情况记录。
4. `join-testing` 等极少数 Key 在部分语言中无文本，未强行补全。

## 质量检查

- **第一轮（结构）**：空 source / 空 target、错误语言代码、重复记录、HTML 标签、JSON 残留、内部 ID、
  转义残留、无意义字符串 —— 全部通过。
- **第二轮（语言方向）**：逐语言校验 target 列书写系统与 `tgt_lng` 一致 —— 全部通过。
- **第三轮（交叉核对）**：游戏名称、邻居名、UI 用语、世界观术语、测试名称
  与官方本地化 JSON 及官方 HoYoLAB 公告逐项核对 —— 全部通过。

## 复现

抓取与生成脚本位于 `E:\Download\BT\Codex_input\scripts\`：

`fetch_hoyolab.py`、`pp_extract.py`、`pp_clean.py`、`build_terms.py`、`build_final.py`、`emit_final.py`、`emit_docs2.py`、`qc1.py`、`qc4.py`

---

**Disclaimer**：本库为个人整理的**非官方**术语资料，仅供学习、研究与 AI 翻译辅助使用。
游戏名称、角色、地名、道具及相关素材的知识产权归各自权利人所有。如与官方内容冲突，以官方为准。
