# 异环（Neverness to Everness）术语库 — Español（`es-ES`）

[← 返回游戏总说明](../../README.md) ｜ [← nte-glossary 子库说明](../README.md)

本目录是**以 `es-ES`（Español）为目标语言**的异环术语库。共 **21** 个类目 CSV、
**55,275** 行对照。所有 CSV 的 `tgt_lng` 列固定为 `es-ES`；`source` 列收录其余语言
（`zh-CN`（简体中文）、`zh-TW`（繁體中文）、`en-US`（English）、`ja-JP`（日本語）、`ko-KR`（한국어）、`fr-FR`（Français）、`de-DE`（Deutsch）、`ru-RU`（Русский））的写法，因此同一条游戏文本可以从任意一种语言匹配到本语言的译名。

## 文件

本目录为**扁平结构**，21 个类目 CSV 直接放在本目录下，没有额外的子目录：

- `achievements（Logros）.csv` — 成就
- `buffs（Mejoras y efectos）.csv` — 增益与效果
- `characters（Personajes）.csv` — 角色
- `combat（Combate）.csv` — 战斗
- `dungeons（Etapas y dominios）.csv` — 关卡与副本
- `enemies（Enemigos）.csv` — 敌人
- `equipment（Equipamiento）.csv` — 装备
- `factions（Facciones）.csv` — 阵营与势力
- `furniture（Muebles）.csv` — 家具
- `items（Objetos y materiales）.csv` — 道具与材料
- `npcs（PNJ）.csv` — NPC
- `quests（Misiones）.csv` — 任务
- `regions（Regiones）.csv` — 地区
- `skills（Habilidades）.csv` — 技能
- `specials（Sistemas especiales）.csv` — 特殊系统
- `story（Términos de la historia）.csv` — 剧情专有名词
- `system（Textos del sistema）.csv` — 系统文本
- `terms（Términos）.csv` — 术语
- `ui（Textos de interfaz）.csv` — UI 文本
- `vehicles（Vehículos）.csv` — 载具
- `weapons（Armas）.csv` — 武器

每个文件都是 `source,target,tgt_lng` 三列（首行为表头）：对 `tgt_lng` 指定的目标语言，
`target` 是译文，`source` 是**其它某一语言**的原文。文件可直接导入 CAT 工具或沉浸式翻译等术语匹配软件。

## 说明

- **译文来源**：官方多语言本地化文本，按同一文本键对齐，属于官方本地化而非二次翻译。
- **编码**：所有 CSV 均为 **UTF-8 with BOM + CRLF**，Excel 双击即可正确显示。
- **已知限制**：不同语言覆盖的文本键并不完全一致，故各语言的对照行数略有差异。
- **更新与复现**：在游戏目录下运行 `../tools/` 中的生成脚本即可重建本目录。
