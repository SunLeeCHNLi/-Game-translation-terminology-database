# NTE 数据来源记录 / Sources

生成日期：`2026-09-27`

## 本次术语生成使用的来源

| 来源 | URL | 类型 | 版本 / Commit | 用途 | 可信度 |
| --- | --- | --- | --- | --- | --- |
| NTE_Assets Localization | https://github.com/Waifus-Grace/NTE_Assets | Game Data / Localization | `ae1f348c35378184a9e14b56593f43854b7ce575` / `1.4.7 (CN extraction)` | 主数据源；按同一文本键提取多语言正式游戏文本 | High |
| NTE 官方国际服网站 | https://nte.perfectworld.com/en/index.html | Official | 2026-09-27 visited | 核对游戏标题、基础术语、地区名称与语言支持 | High |
| Steam 官方商店 | https://store.steampowered.com/app/4508340/ | Official | 2026-09-27 visited | 核对九种文字语言及语音语言范围 | High |

## 已检查但未作为术语主源的资料

| 来源 | 判定类型 | 处理结论 |
| --- | --- | --- |
| https://github.com/SolicenTEAM/UEExtractor | Unreal Engine extraction tool | 工具仓库，不是术语数据；未直接提取本地 .pak/.locres |
| https://github.com/NTE-ASIA/NTE-Internal | Teleport/coordinate data | 仅含 TP 坐标文件，分类为地图辅助数据，不进入术语库 |
| https://github.com/indrasundanese/Neverness-to-Everness-Localization | Community localization corpus | 仅含旧版 `en_US.json`，可作为英文键结构参考，未用于多语言术语生成 |
| https://interactivemap.app/neverness-to-everness/database/en/ | Third-party database | 用于分类与抽样复核；不覆盖客户端优先数据 |
| https://thegameswiki.com/nte/wiki/localization | AI-assisted Community Wiki | 用于核对语言支持范围；不作为逐词译名来源 |
| https://github.com/topics/neverness-to-everness | GitHub topic index | 已盘点；多数仓库为自动化、Mod、作弊、抽卡工具或地图工具 |

## 语言代码映射

| 本库代码 | 上游目录 | 备注 |
| --- | --- | --- |
| `zh-CN` | `Localization/zh-CN/game.json` | 简体中文文本 |
| `zh-TW` | `Localization/zh-Hant/game.json` | 繁体中文文本，统一映射为 `zh-TW` |
| `en-US` | `Localization/en/game.json` | English |
| `ja-JP` | `Localization/ja/game.json` | 日本語 |
| `ko-KR` | `Localization/ko/game.json` | 한국어 |
| `de-DE` | `Localization/de/game.json` | Deutsch |
| `fr-FR` | `Localization/fr/game.json` | Français |
| `es-ES` | `Localization/es/game.json` | Español |
| `ru-RU` | `Localization/ru/game.json` | Русский |

## 对齐规则

每条记录来自上游 `namespace + key` 下的同一文本键。生成器不使用字符串相似度猜测对应关系，也不会对缺失语言进行机器翻译。相同 `source + tgt_lng` 若存在多个 `target`，全部保留，并在 `tools/_validation.json` 中统计冲突。
