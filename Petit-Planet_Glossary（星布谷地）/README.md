# 《星布谷地》Petit Planet 翻译术语库 / Petit Planet Terminology Database / プチプラネット 用語集

## [English](README_EN.md) [日本語](README_JP.md)

本库收录 HoYoverse 生活模拟游戏《星布谷地》（Petit Planet / プチプラネット）的专有名词对照表，
覆盖 **15 种目标语言**：简体中文、繁體中文、English、日本語、한국어、Français、Deutsch、Español、
Русский、Português、Italiano、Türkçe、ภาษาไทย、Tiếng Việt、Bahasa Indonesia。

| 名称 | 文本 |
| --- | --- |
| 简体中文 | 星布谷地 |
| 繁體中文 | 星布谷地 |
| English | Petit Planet |
| 日本語 | プチプラネット |
| 한국어 | 쁘띠플래닛 |
| Français | P'tite Planète |

译文取自**官方多语言本地化文本**（官方网站本地化文件，15 种语言使用**同一本地化 Key**）与
**官方 HoYoLAB 公告**（`gids=10`，同样覆盖 15 种语言），按同一文本键或同一官方名称对齐，
属于**官方本地化**而非二次翻译；不含机器翻译。

## 使用方法

1. **单文件下载**：进入对应语言目录（例如 `zh-CN/`），下载 `01_neighbor/01_neighbor_glossary.csv`
   之类的分类术语表，直接导入沉浸式翻译等术语工具即可，无需转换。
2. **整个语言目录打包下载**：若需要全部 18 个分类，下载该语言目录下的全部分类文件。
3. **十五语并排总表**：`multilingual/all_languages_master.csv`，每种语言一列。

## 目录结构

```text
Petit-Planet_Glossary（星布谷地）/
  zh-CN/                    以简体中文为目标语言的术语库
    README.md               本语言库说明
    00_master/              索引与说明
      index.csv             分类索引与条数
      README.md             本语言库说明
    00_game_title/          游戏与测试名称
    01_neighbor/            邻居与角色
    02_location/            星球与地区
    03_item/                道具
    04_material/            材料
    05_furniture/           家具
    06_test_version/        测试版本
    07_cooking/             烹饪
    08_fish/                鱼类
    09_bugs/                昆虫
    10_plants/              植物与农作物
    11_shore/               海岸生物
    12_shop/                商店与经济
    13_neighbor_interaction/ 邻居互动
    15_event/               活动
    18_ui/                  系统与UI
    21_world_term/          游戏机制术语
    22_title_tag/           称号与标签
  zh-TW/                    同上结构（繁体中文字为目标语言）
  en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
  pt-PT/  it-IT/  tr-TR/  th-TH/  vi-VN/  id-ID/
  multilingual/
    all_languages_master.csv  十五语并排总表
  README.md  README_EN.md  README_JP.md
```

## 文件格式

`*_glossary.csv` 严格为三列：

```text
source,target,tgt_lng
Petit Planet,星布谷地,zh-CN
プチプラネット,星布谷地,zh-CN
Petit Planet,星布谷地,zh-TW
星海,Starsea,en-US
```

- `source`：原始本地化字符串（**不是**内部 ID）
- `target`：目标语言正式译名
- `tgt_lng`：目标语言代码

`*_terms.csv` 为本语言词条清单（`id,term,src_table`），便于校对与回查。

## 语言与统计

| 目标语言 | 语言 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `zh-CN` | 简体中文 | 125 | 1,363 |
| `zh-TW` | 繁體中文 | 123 | 1,358 |
| `en-US` | English | 2,073 | 3,306 |
| `ja-JP` | 日本語 | 114 | 1,303 |
| `ko-KR` | 한국어 | 114 | 1,304 |
| `fr-FR` | Français | 113 | 1,298 |
| `de-DE` | Deutsch | 114 | 1,311 |
| `es-ES` | Español | 113 | 1,298 |
| `ru-RU` | Русский | 112 | 1,296 |
| `pt-PT` | Português | 114 | 1,308 |
| `it-IT` | Italiano | 112 | 1,296 |
| `tr-TR` | Türkçe | 113 | 1,298 |
| `th-TH` | ภาษาไทย | 114 | 1,304 |
| `vi-VN` | Tiếng Việt | 114 | 1,304 |
| `id-ID` | Bahasa Indonesia | 113 | 1,298 |
| **合计** | | **3,681** | **21,645** |

> `Português` 官方使用 **`pt-PT`**；`Bahasa Indonesia` 使用 **`id-ID`**（不是 `in-ID`）。
> 官方网站另有 `pl-pl`、`hi-in`，不在本库重点语言范围。

## 数据来源与可信度

| 级别 | 来源 | 说明 |
| --- | --- | --- |
| 最高 | `planet.hoyoverse.com` 官方本地化文件 | 15 种语言使用**同一本地化 Key**（443 个 Key），可直接一一对齐 |
| 最高 | HoYoLAB 官方公告（`gids=10`） | Coziness / Stardrift / Final Beta Test 官方文本，15 种语言，共 81 篇 |
| 三级 | [petitplanet.life](https://petitplanet.life/) | 社区数据库，**仅英文名称**，无官方多语言文本 |
| 工具 | [c3kay/hoyolab-rss-feeds](https://github.com/c3kay/hoyolab-rss-feeds) | 仅用于定位官方新闻源（`Game.PLANET = 10`，section `planet`）；其语言字段不是游戏本地化数据 |
| 索引 | [petitplanet-life/petitplanet-resources](https://github.com/petitplanet-life/petitplanet-resources) | 仅为 petitplanet.life 页面索引，非官方数据仓库 |

- **官方已确认条目：18,558**
- 社区数据库（英文，未本地化）：2,188

## 测试阶段

| 阶段 | 官方中文 | 日期（依据官方公告） |
| --- | --- | --- |
| Final Beta Test | 连接测试 | 2026-09-22 起 |
| Stardrift Test | 星旅测试 | 2026-04-21 起 |
| Coziness Test | 居心地测试 | 2025-11 起 |
| Official Release | — | 未上线（2026 年冬季） |
| Unknown | — | 版本无法确认时记录 `Version: Unknown`，不做猜测 |

## 已知限制

- **游戏客户端多语言字符串尚未公开**：官方译文来自官方网站本地化文件与官方公告；
  官方网站文案可能属于 **Web Only** 层级，游戏内文本以客户端为准。
- **道具、家具、鱼类、昆虫、食谱、商店**等条目目前仅有 petitplanet.life 的**英文名称**，
  缺少官方多语言对照，因此以 `source = target`（均为英文）记录并标注 `community_database`，**未编造任何译名**。
- 官方网站本地化文件中的图片链接与空值已过滤。
- 本库是**纯数据产品**，游戏目录下没有 `tools/` 目录，也没有可执行脚本。

## 质量检查

- **第一轮（结构）**：空 source / 空 target、错误语言代码、重复记录、HTML 标签、JSON 残留、内部 ID、转义残留 —— 全部通过。
- **第二轮（语言方向）**：逐语言校验 target 列书写系统与 `tgt_lng` 一致 —— 全部通过。
- **第三轮（交叉核对）**：游戏名称、邻居名、UI 用语、世界观术语、测试名称与官方本地化文件及官方公告逐项核对 —— 全部通过。

## 免责声明

本项目（**Game-translation-terminology-database / 游戏翻译术语库**）为个人整理与维护的**非官方**翻译术语资料库，
主要用于个人学习、研究以及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语翻译。本项目及维护者与
《星布谷地》的开发商、发行商、代理商、运营商、版权方或其他相关企业、组织**不存在任何从属、授权、合作、代理或官方代表关系**。
库中译名**不代表官方立场、官方术语或官方翻译**，不保证始终准确、完整或与游戏当前版本一致，
**不应被视为官方术语表或官方本地化文件**。游戏名称、角色名称、人名、地名、专有名词、商标、Logo
及其他相关内容的知识产权均归各自权利人所有。使用本项目及其相关内容所产生的一切责任由使用者自行承担。
完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。
