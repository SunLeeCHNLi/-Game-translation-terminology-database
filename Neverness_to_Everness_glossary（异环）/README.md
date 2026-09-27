# 《异环》Neverness to Everness 翻译术语库

## [English](README_EN.md) [日本語](README_JP.md)

本库收录《异环》（Neverness to Everness / NTE）客户端本地化文本中的角色、技能、武器、装备、战斗、任务、地点、阵营、敌人、NPC、道具、载具、家具、成就、世界观术语、UI 和系统名称。目前共 **498,495** 条 `source,target,tgt_lng` 对照记录，覆盖 **9** 种目标语言和 **21** 个分类。

> 主数据来自 `NTE_Assets` 的 1.4.7 CN 提取文件。所有 `target` 都来自同一文本键下的游戏本地化值，不使用机器翻译补全。目标语言缺失文本时不生成记录，也不伪造译名。

## 目录结构

```text
Neverness_to_Everness_glossary/
  README.md
  README_EN.md
  README_JP.md
  nte-glossary/
    README.md
    zh-CN/  zh-TW/  en-US/  ja-JP/  ko-KR/
    de-DE/  fr-FR/  es-ES/  ru-RU/
    sources/                语料/来源说明
      README.md
  tools/
    build_nte_glossary.py
    validate_nte_glossary.py
    scrape_interactivemap.py
    _counts.json
    _validation.json
```

## 文件格式

所有 CSV 使用 UTF-8（含 BOM）、CRLF 换行、RFC 4180 转义，并严格保持三列：

| source | target | tgt_lng |
| --- | --- | --- |
| Hethereau | 海特洛 | zh-CN |
| Anomaly Hunter | 异象猎人 | zh-CN |

`source` 是同一文本键的其它语言本地化文本，`target` 是当前目录语言的游戏客户端本地化文本，`tgt_lng` 固定为目录语言代码。

## 各语言规模

| 目标语言 | 对照行数 |
| --- | ---: |
| `en-US` | 55,226 |
| `zh-CN` | 55,559 |
| `zh-TW` | 55,530 |
| `ja-JP` | 55,582 |
| `ko-KR` | 55,393 |
| `de-DE` | 55,259 |
| `fr-FR` | 55,391 |
| `es-ES` | 55,275 |
| `ru-RU` | 55,280 |


## 分类规模

| 分类文件 | 独立实体数 | 全语言对照行数 |
| --- | ---: | ---: |
| `characters` | 38 | 1,062 |
| `skills` | 974 | 42,226 |
| `weapons` | 51 | 3,456 |
| `equipment` | 66 | 4,563 |
| `combat` | 96 | 5,284 |
| `buffs` | 80 | 5,148 |
| `specials` | 51 | 3,042 |
| `quests` | 1,912 | 90,058 |
| `dungeons` | 179 | 11,466 |
| `regions` | 187 | 7,209 |
| `factions` | 10 | 450 |
| `enemies` | 176 | 9,743 |
| `npcs` | 2,118 | 98,377 |
| `items` | 1,314 | 79,137 |
| `vehicles` | 449 | 14,968 |
| `furniture` | 347 | 23,937 |
| `achievements` | 547 | 36,975 |
| `terms` | 55 | 3,332 |
| `story` | 187 | 11,799 |
| `ui` | 1,410 | 24,391 |
| `system` | 326 | 21,872 |


## 当前版本

- 游戏数据版本：`1.4.7 (CN extraction)`
- 上游仓库：https://github.com/Waifus-Grace/NTE_Assets
- 上游提交：`ae1f348c35378184a9e14b56593f43854b7ce575`
- 生成日期：`2026-09-27`
- 数据来源数：本次生成 `3`，累计检查 `9`
- 去重文本键数：`10,340`
- 分类内实体数（分类累计）：`10,573`
- 客户端本地化确认实体数：`10,340`
- 未确认/机器翻译补全记录：`0` / `0`
- 多译名冲突组：`6,169`。冲突记录全部保留，未自动选择“最佳译名”。

## 重新生成

```bash
python tools/build_nte_glossary.py
python tools/validate_nte_glossary.py
```

默认读取 `E:\Download\BT\Codex_input\nte_upstream\NTE_Assets`。可通过 `--assets-root` 指定新的上游路径。

## 限制

- 上游为社区提取的客户端文本，不等同于发行商公开发布的官方术语表。
- 繁体中文在本库中统一写为 `zh-TW`，上游原始标识为 `zh-Hant`。
- 缺少某语言文本时不会生成虚假对照；空分类表示当前上游没有可确认的实体名称。
- 同一文本键在不同语境下可能有不同译名，详见 `tools/_validation.json` 的冲突统计。

## 免责声明

本目录为非官方个人术语资料库，仅用于学习、研究与翻译辅助。游戏名称、角色、专有名词及相关资产的权利归原权利人所有。
