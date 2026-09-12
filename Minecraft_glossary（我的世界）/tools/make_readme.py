# -*- coding: utf-8 -*-
"""Generate the README files of the Minecraft glossary from _counts.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANG_NAMES = [("zh-CN", "简体中文"), ("zh-TW", "繁體中文"), ("en-US", "English"), ("ja-JP", "日本語"),
              ("ko-KR", "한국어"), ("fr-FR", "Français"), ("de-DE", "Deutsch"), ("es-ES", "Español"),
              ("ru-RU", "Русский"), ("pt-BR", "Português"), ("it-IT", "Italiano"), ("tr-TR", "Türkçe"),
              ("th-TH", "ภาษาไทย"), ("vi-VN", "Tiếng Việt")]
LOCALES = {"zh-CN": "zh_cn", "zh-TW": "zh_tw", "en-US": "en_us", "ja-JP": "ja_jp", "ko-KR": "ko_kr",
           "fr-FR": "fr_fr", "de-DE": "de_de", "es-ES": "es_es", "ru-RU": "ru_ru", "pt-BR": "pt_br",
           "it-IT": "it_it", "tr-TR": "tr_tr", "th-TH": "th_th", "vi-VN": "vi_vn"}

MAIN_CATS = ["blocks", "items", "entities", "biomes", "enchantments", "effects", "instruments",
             "materials", "paintings", "attributes", "item-groups", "jukebox-songs", "trim-patterns",
             "colors", "statistics", "maps", "music", "sound-categories", "game-modes"]
EXTRA_CATS = ["subtitles", "death-messages", "advancement-titles", "advancement-descriptions",
              "gamerules", "commands", "gui", "options", "multiplayer", "realms", "world-management",
              "resource-packs", "telemetry", "dev-tools", "misc"]
CAT_CN = {
    "blocks": "方块", "items": "物品", "entities": "实体", "biomes": "生物群系", "enchantments": "魔咒",
    "effects": "状态效果", "instruments": "乐器", "materials": "盔甲纹饰材料", "paintings": "画",
    "attributes": "属性", "item-groups": "物品栏分类", "jukebox-songs": "唱片曲目",
    "trim-patterns": "盔甲纹饰图案", "colors": "颜色", "statistics": "统计", "maps": "地图",
    "music": "音乐曲目", "sound-categories": "声音分类", "game-modes": "游戏模式",
    "subtitles": "字幕", "death-messages": "死亡消息", "advancement-titles": "进度标题",
    "advancement-descriptions": "进度描述", "gamerules": "游戏规则", "commands": "命令与参数",
    "gui": "界面文本", "options": "设置与按键", "multiplayer": "多人游戏", "realms": "Realms",
    "world-management": "世界管理", "resource-packs": "资源包与数据包", "telemetry": "遥测",
    "dev-tools": "开发与测试工具", "misc": "其他",
}


def table(rows, header):
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def main():
    g = json.load(open(os.path.join(ROOT, "minecraft-glossary", "_counts.json"), encoding="utf-8"))
    s = json.load(open(os.path.join(ROOT, "minecraft-glossary-supplement", "_counts.json"), encoding="utf-8"))
    rows = g["rows"]
    entries = g["categories"]

    main_rows = [[c, "`%s.csv`" % c, CAT_CN[c], entries[c]["entries"], rows["zh-CN"][c]] for c in MAIN_CATS]
    extra_rows = [[c, "`extra/%s.csv`" % c, CAT_CN[c], entries[c]["entries"], rows["zh-CN"][c]] for c in EXTRA_CATS]
    lang_rows = [[f"`{c}`", n, len(MAIN_CATS) + len(EXTRA_CATS), f"{sum(rows[c].values()):,}"]
                 for c, n in LANG_NAMES]
    total = sum(sum(rows[c].values()) for c, _ in LANG_NAMES)
    lang_rows.append(["**合计**", "", "**%d**" % ((len(MAIN_CATS) + len(EXTRA_CATS)) * len(LANG_NAMES)),
                      "**%s**" % f"{total:,}"])
    loc_rows = [[f"`{c}`", n, f"`{LOCALES[c]}`"] for c, n in LANG_NAMES]

    readme = f"""# 我的世界（Minecraft）多语言术语库

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放；系统与文本类目统一放在各语言的 `extra/` 子文件夹内。

## 数据来源

- 主词库：**Minecraft Java 版官方语言文件**，取自 [misode/mcmeta](https://github.com/misode/mcmeta) 的 `assets` 分支（`assets/minecraft/lang/<locale>.json`），覆盖全部 14 种目标语言。
- 类目结构参照 [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) 中 `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` 等分类方式划分；该库中的 `particles`、`sounds` 在官方语言文件中只有内部 ID、没有本地化名称，故未单独成类。
- 补充词库：见同级目录 `minecraft-glossary-supplement/`（来源 [Minecraft Wiki 译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)），额外提供 Wiki 标准译名，覆盖简体中文 / 繁体中文。
- 图片资源库 [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) 按版本分支存放材质，本词库以其语言文件结构作为校对参考。

## 目录结构

```
minecraft-glossary/
├── zh-CN/                    # 目标语言 = 简体中文
│   ├── blocks.csv
│   ├── items.csv
│   ├── ...
│   └── extra/                # 系统与文本类目
│       ├── subtitles.csv
│       └── ...
├── zh-TW/
├── en-US/ ... vi-VN/         # 共 14 个语言文件夹
└── _counts.json              # 各语言、各类目的条目数统计
```

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、首行为表头，字段含逗号或引号时按 RFC 4180 加引号转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Enterprise | 企业 | zh-CN |
| エンタープライズ | 企业 | zh-CN |

含义：对于 `tgt_lng` 指定的目标语言，`target` 是译文，`source` 是**其它任一语言**的原文。
即每个语言文件夹内，同一条目会以其余 13 种语言分别作为 `source` 各出现一行（重复行与同形行已合并）。

## 语言代码

| 语言文件夹 | 语言 | Minecraft 语言文件 |
| --- | --- | --- |
{table(loc_rows, ["语言文件夹", "语言", "locale"])}

## 类目与条目数

「条目」指该分类下的**去重词条数**（一个词条 = 游戏中的一个名称对象）；「行数」为简体中文文件夹内该类目 CSV 的数据行数。

### 主类目（游戏内容）

{table(main_rows, ["类目", "文件", "说明", "词条数", "每语言行数（zh-CN）"])}

### `extra/` 类目（系统与文本）

{table(extra_rows, ["类目", "文件", "说明", "词条数", "每语言行数（zh-CN）"])}

## 各语言总行数

{table(lang_rows, ["语言", "语言（名称）", "文件数", "数据行数"])}

## 数据清洗说明

| 处理项 | 处理方式 |
| --- | --- |
| 与目标语言完全同形的行 | 删除（例如各语言均未翻译的曲名、专有名词） |
| 同一条目产生的重复行 | 合并 |
| 空值 / 缺失翻译 | 跳过该语言，不生成空行 |
| 格式化占位符（`%s`、`%1$s`、`%%`） | 原样保留 |
| 同一键在不同语言下的重复译文 | 按 `source`+`target` 去重 |

## 使用提示

- 导入 CAT 工具（Trados、memoQ、Phrase 等）时，选择对应目标语言的 CSV 直接作为术语库导入即可。
- 文件名即类目名，可按需合并；如需「全部类目合并为单一文件」或增加 `src_lng`（源语言）列，可随时生成。
- 重新生成词库：先准备官方语言文件（`lang/<locale>.json`），再运行 `tools/build_glossary.py`；前缀到类目的完整映射见该脚本中的 `CATEGORIES` 表。
- 官方语言文件共有 144 种语言变体，本词库按需选取其中 14 种；若需其它语言，在 `tools/build_glossary.py` 的 `LANG_FILES` 中补充后重新生成即可。
"""
    open(os.path.join(ROOT, "minecraft-glossary", "README.md"), "w", encoding="utf-8", newline="\n").write(readme)

    sup_rows = [[c, "`%s.csv`" % c, s["categories"][c]["entries"],
                 s["rows"]["zh-CN"].get(c, 0), s["rows"]["zh-TW"].get(c, 0)] for c in sorted(s["categories"])]
    supp = f"""# 我的世界（Minecraft）Wiki 译名标准化 补充词库

本目录是 `minecraft-glossary/` 的**补充词库**，收录 [Minecraft Wiki 译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) 页面中的标准译名，用于补充官方语言文件未覆盖或与 Wiki 标准不一致的译名。

## 数据来源

- [Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)（简体中文 / 繁体中文两种变体分别抓取后合并）
- 该页面同时是 Wiki 的译名规范来源，其译名与 Crowdin 上已确定的官方本地化方案保持一致，未确定时暂用游戏内原文。

## 覆盖范围

- 本补充词库**仅覆盖 `zh-CN`（简体中文）与 `zh-TW`（繁体中文）**两种目标语言，其余语言请使用主词库 `minecraft-glossary/`。
- 每个语言文件夹内，同一条目会以 `en-US` 与另一中文变体分别作为 `source` 各出现一行。

## 目录结构

```
minecraft-glossary-supplement/
├── zh-CN/
│   ├── blocks.csv
│   ├── items.csv
│   └── ...
├── zh-TW/
└── _counts.json
```

## 文件格式

与主词库一致：**UTF-8（含 BOM）**、**CRLF**、首行表头。

| source | target | tgt_lng |
| --- | --- | --- |
| Chest | 箱子 | zh-CN |
| 儲物箱 | 箱子 | zh-CN |

## 类目与条目数

{table(sup_rows, ["类目", "文件", "词条数", "zh-CN 行数", "zh-TW 行数"])}

## 与主词库的差异

- Wiki 采用「台灣正體」用词（例如 `Chest` = 儲物箱、`Slab` = 半磚、`Stairs` = 階梯），与游戏内繁体中文语言文件可能存在差异，两份资料**建议按需取用**。
- 标注为「不翻译」的条目（如 `Mojang`、`Minecraft`）不会收入本词库。
- 同一英文名对应多个中文写法时，使用 Wiki 的写法并以 ` / ` 连接（例如 `Boolean` = 布林值 / 布林型）。

## 使用提示

- 重新生成：先抓取该页面的 `zh-cn` / `zh-tw` 两种变体（`action=parse&prop=text&variant=...`），再运行 `tools/build_wiki_supplement.py`。
"""
    open(os.path.join(ROOT, "minecraft-glossary-supplement", "README.md"), "w", encoding="utf-8", newline="\n").write(supp)
    print("READMEs written")
    print(f"total rows = {total:,}")


if __name__ == "__main__":
    main()


