# 数据来源记录 / Source Records

《崩坏：星穹铁道》术语库的生成、交叉验证与历史比对所使用的数据源。
`Retrieved Date` 为 2026-09-27（本地克隆到 `E:\Download\BT\Codex_input`）。

## 1. 实际参与生成的来源

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DimbreathBot/TurnBasedGameData | https://github.com/DimbreathBot/TurnBasedGameData | Game Data / TextMap | CHS CHT EN JP KR DE ES FR ID PT RU TH VI（13） | 4.5.0（OSPRODWin4.5.0_D16545211_A16445860_L16502768） | `4ce30f69b`（2026-09-16） | 主数据：`ExcelOutput`（2185 个配置）+ `TextMap`（13 语言） | 所有 `target` 都来自该数据源同一 TextMap Key 的本地化文本；名称字段的字符串键按 xxHash64 计算 Hash |
| Mar-7th/StarRailRes | https://github.com/Mar-7th/StarRailRes | Structured Data | cn cht en jp kr fr de es ru pt id th vi（13） | 4.5.0（info.json timestamp 1787993304） | `d226bef`（2026-08-29） | 结构化补充 + 交叉验证：命途、属性、遗器词条、遗器/套装、模拟宇宙祝福/奇物/事件 | `index_min`（精简版）用于补充 TextMap 无法直接定位的按 ID 命名条目；所有写入的词条都回查客户端 TextMap，未命中的字符串不写入 |
| VizualAbstract/StarRailStaticAPI | https://github.com/VizualAbstract/StarRailStaticAPI | Historical / Structured Data | cn cht en jp kr fr de es ru pt id th vi（13） | 2.3.0（timestamp 1718980131） | `e039e51`（2024-07-05） | 历史译名比对基线（旧版本） | 与 4.5.0 同名实体逐 ID 比对，仅把**名称发生变化**的条目写入 `hsr-glossary/historical/` |
| nathacks/HSR-Mapping-DATA | https://github.com/nathacks/HSR-Mapping-DATA | Historical / Structured Data | chs cht en jp kr fr de es ru pt id th vi（13） | 4.0（README: Last Update 4.0） | `245f286`（2026-07-17） | 历史译名比对基线（上一版本） | 同上；仅写入差异，不覆盖当前译名 |
| mrzjy/StarrailDialog | https://github.com/mrzjy/StarrailDialog | Community / Story | CHS EN | 2024-07（仅 CHS/EN） | `149dd8e`（2024-07-12） | 剧情/对话文本结构的辅助核对 | 只覆盖中英双语且版本较旧，未用于生成正式术语；用于确认剧情类文本的组织方式 |
| M1k0t0/StarRail_Dialogue_Browser | https://github.com/M1k0t0/StarRail_Dialogue_Browser | Tool / Community | 取决于上游 submodule | 2026-04 | `99f27a6`（2026-04-11） | 剧情/对话浏览工具与结构参考 | 其数据来自 `TurnBasedGameData` 子模块，本库直接从主数据源取数 |

## 2. 检查过但未参与生成的来源

| Source | URL | Type | Language | Version | Commit | Retrieved Date | Usage | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| iuyangyuc/homdgcat | https://github.com/iuyangyuc/homdgcat | Wiki / Tool | 站点提供 CH EN JP KR RU | 2026-02 | `7d418f5`（2026-02-13） | 参考资料（未写入） | 仓库本体是 homdgcat.wiki 的镜像/下载脚本（含 15357 个文件清单），需要另行抓取站点数据；本轮未作为术语来源 |
| kel-z/HSR-Data | https://github.com/kel-z/HSR-Data | Structured Data | EN | 2.7 | `bbffd99`（2024-12-03） | 参考资料（未写入） | 仅英文且版本较旧（2.7），仅用于人工对照角色/光锥/遗器结构 |
| simon300000/starrail-voice | https://github.com/simon300000/starrail-voice | Voice / Tool | 多语言音频 | 2026-07 | `9478716`（2026-07-17） | 参考资料（未写入） | 语音提取工具与音频索引，用于确认角色名/说话者命名习惯；不含可对齐的文本术语键 |
| 米哈游《崩坏：星穹铁道》官网 | https://sr.mihoyo.com/ | Official | zh-CN | 4.5.0 周期 | — | 2026-09-27 | 官方写法核对（简体中文） | 用于确认简体中文官方译名与活动名称写法 |
| HoYoverse HSR 全球站 | https://hsr.hoyoverse.com/ | Official | en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-PT / id-ID / th-TH / vi-VN | 4.5.0 周期 | — | 2026-09-27 | 官方写法核对（多语言） | 用于确认各语言官方译名与语言支持范围；不作为批量数据源 |

## 3. 语言代码映射

| 本库 `tgt_lng` | 客户端 / TextMap 标识 | StarRailRes 目录 | 官方语言 |
| --- | --- | --- | --- |
| `zh-CN` | CHS | cn | 简体中文 |
| `zh-TW` | CHT | cht | 繁體中文 |
| `en-US` | EN | en | English |
| `ja-JP` | JP | jp | 日本語 |
| `ko-KR` | KR（`TextMapKR_0/1`） | kr | 한국어 |
| `fr-FR` | FR | fr | Français |
| `de-DE` | DE | de | Deutsch |
| `es-ES` | ES | es | Español |
| `ru-RU` | RU（`TextMapRU_0/1`） | ru | Русский |
| `pt-PT` | PT | pt | Português |
| `id-ID` | ID | id | Bahasa Indonesia |
| `th-TH` | TH（`TextMapTH_0/1`） | th | ไทย |
| `vi-VN` | VI | vi | Tiếng Việt |

> 说明：本库只收录《崩坏：星穹铁道》当前客户端实际支持的语言。
> 其它 HoYoverse 游戏支持的语言（例如 `it-IT`、`tr-TR`）不会被套用到本作。

## 4. 上游数据未随仓库分发

上游仓库体积较大（原始 TextMap、ExcelOutput、剧情、音频等），全部保留在本地
`E:\Download\BT\Codex_input` 下，不复制进本仓库。重新生成时按上表 URL 克隆对应版本即可。
