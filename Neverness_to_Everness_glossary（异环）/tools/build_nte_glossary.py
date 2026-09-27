#!/usr/bin/env python3
"""Build the NTE terminology database from extracted game localization JSON."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Iterable


DEFAULT_ASSETS = Path(r"E:\Download\BT\Codex_input\nte_upstream\NTE_Assets")
SOURCE_URL = "https://github.com/Waifus-Grace/NTE_Assets"
DEFAULT_COMMIT = "ae1f348c35378184a9e14b56593f43854b7ce575"
GAME_VERSION = "1.4.7 (CN extraction)"

LANGS = {
    "en-US": "Localization/en/game.json",
    "zh-CN": "Localization/zh-CN/game.json",
    "zh-TW": "Localization/zh-Hant/game.json",
    "ja-JP": "Localization/ja/game.json",
    "ko-KR": "Localization/ko/game.json",
    "de-DE": "Localization/de/game.json",
    "fr-FR": "Localization/fr/game.json",
    "es-ES": "Localization/es/game.json",
    "ru-RU": "Localization/ru/game.json",
}
LANGUAGE_LABELS = {
    "en-US": "English",
    "zh-CN": "\u7b80\u4f53\u4e2d\u6587",
    "zh-TW": "\u7e41\u9ad4\u4e2d\u6587",
    "ja-JP": "\u65e5\u672c\u8a9e",
    "ko-KR": "\ud55c\uad6d\uc5b4",
    "de-DE": "Deutsch",
    "fr-FR": "Fran\u00e7ais",
    "es-ES": "Espa\u00f1ol",
    "ru-RU": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
}

CATEGORIES = (
    "characters",
    "skills",
    "weapons",
    "equipment",
    "combat",
    "buffs",
    "specials",
    "quests",
    "dungeons",
    "regions",
    "factions",
    "enemies",
    "npcs",
    "items",
    "vehicles",
    "furniture",
    "achievements",
    "terms",
    "story",
    "ui",
    "system",
)

MAX_LEN = {
    "quests": 180,
    "dungeons": 140,
    "story": 160,
    "ui": 100,
    "system": 120,
}
DEFAULT_MAX_LEN = 160

QUEST_NAMESPACES = {
    "ST_Quest",
    "ST_MainQuest",
    "ST_LegendQuest",
    "ST_QuestEveryDay",
    "ST_ReviewQuest",
    "ST_ReturningQuest",
    "ST_NoteBookQuest",
    "ST_SurvivalQuest",
    "ST_Interact_Quest",
}
UI_NAMESPACES = {
    "ST_Ui",
    "ST_UI_C",
    "ST_Ui_D",
    "ST_UI_GYJ",
    "ST_UI_hpy",
    "ST_UI_J",
    "ST_UI_lsh",
    "ST_UI_N",
    "ST_UI_Volleyball",
    "ST_UI_Wy",
    "ST_UI_XZC",
    "ST_UITIPS",
    "ST_UITips",
    "ST_Gamepad",
}
SYSTEM_NAMESPACES = {
    "ST_Common",
    "ST_GameplayDec",
    "ST_Tycoon",
    "ST_TycoonRank",
    "ST_FinalTower",
    "ST_FinalTowerSuitDes",
}
CORE_TERM_KEYS = {
    ("ST_Manual", "NounManual_1_1_name"),
    ("ST_Manual", "NounManual_1_13_name"),
    ("ST_Manual", "NounManual_1_17_name"),
    ("ST_Manual", "NounManual_2_1_name"),
    ("ST_Manual", "NounManual_2_2_name"),
    ("ST_ActorName", "NPC_09601_Title"),
    ("Female_SkillDes", "GA_Female_Passive_1_name"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--assets-root", type=Path, default=DEFAULT_ASSETS)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-commit", default=DEFAULT_COMMIT)
    parser.add_argument("--game-version", default=GAME_VERSION)
    return parser.parse_args()


def clean_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    text = html.unescape(value)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def valid_term(value: str, category: str) -> bool:
    if not value or len(value) > MAX_LEN.get(category, DEFAULT_MAX_LEN):
        return False
    lower = value.casefold()
    if lower in {"none", "null", "undefined", "$undefined", "/", "-", "n/a"}:
        return False
    if value.startswith("<!>") or "{" in value or "}" in value:
        return False
    if "http://" in lower or "https://" in lower:
        return False
    if not re.search(r"[^\W_]", value, flags=re.UNICODE):
        return False
    if value.isdigit() or re.fullmatch(r"[IVXLCDM]+", value):
        return False
    return True


def classify(namespace: str, key: str, value: str) -> set[str]:
    categories: set[str] = set()
    low_key = key.casefold()

    if namespace == "ST_Player" and re.fullmatch(r"Role_Name_\d+", key):
        categories.add("characters")

    if namespace.endswith("_SkillDes") and low_key.endswith("_name"):
        categories.add("skills")
    if namespace in {"ST_CityCharacterAbility", "ST_SurvivalSkill", "ST_SurvivalSkillEffect"} and low_key.endswith("_name"):
        categories.add("skills")

    if namespace == "ST_Fork" and key.startswith("fork_") and low_key.endswith("_name"):
        categories.add("weapons")
    if namespace == "ST_Fork" and key.startswith("buff_fork_") and low_key.endswith("_name"):
        categories.add("specials")

    if namespace == "ST_Equipment" and (
        key.startswith(("Suit_", "own_grid_", "specification_grid_", "category_"))
        or key in {"Equipment_Suit", "Equipment_Attribute", "Equipment_Detail", "EquipmentList_1"}
    ):
        categories.add("equipment")
    if namespace == "ST_FinalTowerSuitDes" and low_key.endswith("_name"):
        categories.add("equipment")

    if namespace == "ST_CharacterTag":
        categories.add("combat")
    if namespace == "ST_Buffdes" and low_key.endswith("_name"):
        categories.add("buffs")
    if namespace == "ST_ReactionDes" and not low_key.endswith("_des"):
        categories.add("combat")
    if namespace == "ST_SurvivalAttribute" and not low_key.endswith("_des"):
        categories.add("combat")

    if namespace.startswith(("ST_MainQuest", "ST_Mainquest_", "ST_SideQuest", "ST_Sidequest_")):
        if "questname" in low_key and "obj" not in low_key and "panel" not in low_key:
            categories.add("quests")
    if namespace in QUEST_NAMESPACES and "questname" in low_key:
        categories.add("quests")

    if namespace == "ST_Chapter" and not low_key.endswith("_des") and key != "NotOpenQuest":
        categories.update({"dungeons", "story"})
    if namespace == "ST_Loading_Quest" and (low_key.endswith("_title_01") or low_key.endswith("_title")):
        categories.add("story")

    if namespace in {"ST_MapAreaDetails", "ST_SceneAreaName", "ST_QuestDisplayMapNameDetail"}:
        categories.add("regions")
    if namespace == "ST_Manual" and key.startswith("NounManual_") and low_key.endswith("_name"):
        categories.add("terms")
        if key == "NounManual_1_17_name":
            categories.add("regions")

    if namespace == "ST_Likeability" and key.startswith("RoleSort_") and value != "/":
        categories.add("factions")

    if namespace == "ST_ActorName":
        if key.startswith(("mon_", "boss_", "Anomaly_")) and (
            low_key.endswith("_name") or key.endswith("_BP")
        ):
            categories.add("enemies")
        if key.startswith(("NPC_", "CNPC_")) and (
            low_key.endswith("_name") or low_key.endswith("_title") or "title_name" in low_key
        ):
            categories.add("npcs")

    if namespace == "ST_Item" and low_key.endswith("_name"):
        if key.startswith("Furniture_"):
            categories.add("furniture")
        else:
            categories.add("items")

    if namespace == "NewStringTable" and re.match(r"^(V\d{3}|Vehicle).+_name$", key, flags=re.I):
        categories.add("vehicles")
    if namespace == "ST_Item" and "vehicle" in low_key and low_key.endswith("_name"):
        categories.add("vehicles")

    if namespace == "ST_Achievement" and low_key.endswith(("_title", "_title_en")):
        categories.add("achievements")

    if namespace in UI_NAMESPACES and low_key.endswith(("_name", "_title")):
        categories.add("ui")
    if namespace == "ST_Interact_Quest":
        categories.add("ui")
    if namespace == "ST_ErrCode":
        categories.add("system")

    if namespace in SYSTEM_NAMESPACES and (
        low_key.endswith(("_name", "_title"))
        or any(token in low_key for token in ("system", "gameplay", "function", "menu"))
    ):
        categories.add("system")

    if (namespace, key) in CORE_TERM_KEYS:
        categories.add("terms")
    if (namespace, key) in {("ST_Manual", "NounManual_2_1_name"), ("ST_Manual", "NounManual_2_2_name")}:
        categories.add("factions")

    return categories


def load_localization(assets_root: Path) -> dict[str, dict[str, dict[str, Any]]]:
    loaded: dict[str, dict[str, dict[str, Any]]] = {}
    for lang, relpath in LANGS.items():
        path = assets_root / relpath
        loaded[lang] = json.loads(path.read_text(encoding="utf-8"))
    return loaded


def build_catalog(loaded: dict[str, dict[str, dict[str, Any]]]) -> dict[str, dict[str, dict[str, str]]]:
    catalog: dict[str, dict[str, dict[str, str]]] = {category: {} for category in CATEGORIES}
    for lang, data in loaded.items():
        for namespace, table in data.items():
            if not isinstance(table, dict):
                continue
            for key, raw_value in table.items():
                value = clean_text(raw_value)
                if not value:
                    continue
                categories = classify(namespace, key, value)
                if not categories:
                    continue
                concept_id = f"{namespace}::{key}"
                for category in categories:
                    if valid_term(value, category):
                        catalog[category].setdefault(concept_id, {})[lang] = value

    catalog["terms"]["manual::game-title"] = {
        "en-US": "Neverness to Everness",
        "zh-CN": "\u5f02\u73af",
        "zh-TW": "\u7570\u74b0",
        "ja-JP": "\u7570\u74b0",
        "ko-KR": "\uc774\ud658",
        "de-DE": "Neverness to Everness",
        "fr-FR": "Neverness to Everness",
        "es-ES": "Neverness to Everness",
        "ru-RU": "Neverness to Everness",
    }
    return catalog


def write_csv(path: Path, rows: Iterable[tuple[str, str, str]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    seen: set[tuple[str, str, str]] = set()
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\r\n")
        writer.writerow(["source", "target", "tgt_lng"])
        for row in rows:
            if row in seen:
                continue
            seen.add(row)
            writer.writerow(row)
    return len(seen)


def build_rows(catalog: dict[str, dict[str, dict[str, str]]]) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for target_lang in LANGS:
        counts[target_lang] = {}
        for category in CATEGORIES:
            rows = []
            for values in catalog[category].values():
                target = values.get(target_lang)
                if not target or not valid_term(target, category):
                    continue
                for source_lang, source in values.items():
                    if source_lang == target_lang or source == target:
                        continue
                    if valid_term(source, category):
                        rows.append((source, target, target_lang))
            counts[target_lang][category] = len(set(rows))
    return counts


def write_docs(game_dir: Path, out_root: Path, stats: dict[str, Any]) -> None:
    counts = stats["counts"]
    concept_counts = stats["concept_counts"]
    total = stats["grand_total"]

    def language_table() -> str:
        return "".join(
            f"| `{lang}` | {sum(counts[lang].values()):,} |\n" for lang in LANGS
        )

    def category_table() -> str:
        return "".join(
            f"| `{category}` | {concept_counts[category]:,} | "
            f"{sum(counts[lang][category] for lang in LANGS):,} |\n"
            for category in CATEGORIES
        )

    zh_readme = f"""# 《异环》Neverness to Everness 翻译术语库

## [English](README_EN.md) [日本語](README_JP.md)

本库收录《异环》（Neverness to Everness / NTE）客户端本地化文本中的角色、技能、武器、装备、战斗、任务、地点、阵营、敌人、NPC、道具、载具、家具、成就、世界观术语、UI 和系统名称。目前共 **{total:,}** 条 `source,target,tgt_lng` 对照记录，覆盖 **{len(LANGS)}** 种目标语言和 **{len(CATEGORIES)}** 个分类。

> 主数据来自 `NTE_Assets` 的 1.4.7 CN 提取文件。所有 `target` 都来自同一文本键下的游戏本地化值，不使用机器翻译补全。目标语言缺失文本时不生成记录，也不伪造译名。

## 目录结构

```text
Neverness_to_Everness_glossary/
  README.md
  README_EN.md
  README_JP.md
  nte-glossary/
    zh-CN/  zh-TW/  en-US/  ja-JP/  ko-KR/
    de-DE/  fr-FR/  es-ES/  ru-RU/
  tools/
    build_nte_glossary.py
    validate_nte_glossary.py
    scrape_interactivemap.py
    _counts.json
    _validation.json
  Sources/
    README.md
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
{language_table()}

## 分类规模

| 分类文件 | 独立实体数 | 全语言对照行数 |
| --- | ---: | ---: |
{category_table()}

## 当前版本

- 游戏数据版本：`{stats['game_version']}`
- 上游仓库：{stats['source_url']}
- 上游提交：`{stats['source_commit']}`
- 生成日期：`{stats['generated']}`
- 数据来源数：本次生成 `{stats['source_count']}`，累计检查 `{stats['checked_source_count']}`
- 去重文本键数：`{stats['unique_concepts']:,}`
- 分类内实体数（分类累计）：`{stats['concept_total_across_categories']:,}`
- 客户端本地化确认实体数：`{stats['confirmed_concepts']:,}`
- 未确认/机器翻译补全记录：`{stats['unconfirmed_concepts']:,}` / `{stats['machine_translation_rows']:,}`
- 多译名冲突组：`{stats['conflicts']:,}`。冲突记录全部保留，未自动选择“最佳译名”。

## 重新生成

```bash
python tools/build_nte_glossary.py
python tools/validate_nte_glossary.py
```

默认读取 `E:\\Download\\BT\\Codex_input\\nte_upstream\\NTE_Assets`。可通过 `--assets-root` 指定新的上游路径。

## 限制

- 上游为社区提取的客户端文本，不等同于发行商公开发布的官方术语表。
- 繁体中文在本库中统一写为 `zh-TW`，上游原始标识为 `zh-Hant`。
- 缺少某语言文本时不会生成虚假对照；空分类表示当前上游没有可确认的实体名称。
- 同一文本键在不同语境下可能有不同译名，详见 `tools/_validation.json` 的冲突统计。

## 免责声明

本目录为非官方个人术语资料库，仅用于学习、研究与翻译辅助。游戏名称、角色、专有名词及相关资产的权利归原权利人所有。
"""

    en_readme = f"""# Neverness to Everness Terminology Database

## [简体中文](README.md) [日本語](README_JP.md)

This repository contains **{total:,}** `source,target,tgt_lng` rows extracted from the NTE 1.4.7 localization files, covering **{len(LANGS)}** target languages and **{len(CATEGORIES)}** categories.

All targets come from aligned game localization keys. Missing values are omitted rather than filled with machine translation.

## Language Coverage

| Target language | Rows |
| --- | ---: |
{language_table()}

## Data Source

- Repository: {stats['source_url']}
- Commit: `{stats['source_commit']}`
- Game version: `{stats['game_version']}`
- Generated: `{stats['generated']}`
- Sources used / checked: `{stats['source_count']}` / `{stats['checked_source_count']}`
- Unique text keys: `{stats['unique_concepts']:,}`
- Concepts across categories: `{stats['concept_total_across_categories']:,}`
- Client-localization-confirmed concepts: `{stats['confirmed_concepts']:,}`
- Unconfirmed / machine-translated rows: `{stats['unconfirmed_concepts']:,}` / `{stats['machine_translation_rows']:,}`
- Multi-target conflict groups: `{stats['conflicts']:,}`

## Rebuild

```bash
python tools/build_nte_glossary.py
python tools/validate_nte_glossary.py
```

This is an unofficial personal project and is not affiliated with Hotta Studio, Perfect World Games, or NTE.
"""

    jp_readme = f"""# 『異環』Neverness to Everness 翻訳用語集

## [简体中文](README.md) [English](README_EN.md)

NTE 1.4.7 のローカライズデータから、{len(LANGS)} 言語・{len(CATEGORIES)} 分類・**{total:,}** 行の対訳を生成しています。原文と訳文は同一のゲームテキストキーで対応付けています。

## データ出典

- リポジトリ: {stats['source_url']}
- コミット: `{stats['source_commit']}`
- ゲーム版: `{stats['game_version']}`
- 生成日: `{stats['generated']}`

非公式の個人プロジェクトです。権利者は各社に帰属します。
"""

    sub_readme = f"""# NTE Terminology Data

This directory stores the generated glossary by target language. Each CSV has exactly three columns: `source`, `target`, `tgt_lng`.

- Generated rows: **{total:,}**
- Target languages: **{len(LANGS)}**
- Categories: **{len(CATEGORIES)}**
- Source commit: `{stats['source_commit']}`

Run the scripts in `../tools/` from the game directory to rebuild or verify the data.
"""

    sources = f"""# NTE 数据来源记录 / Sources

生成日期：`{stats['generated']}`

## 本次术语生成使用的来源

| 来源 | URL | 类型 | 版本 / Commit | 用途 | 可信度 |
| --- | --- | --- | --- | --- | --- |
| NTE_Assets Localization | {stats['source_url']} | Game Data / Localization | `{stats['source_commit']}` / `{stats['game_version']}` | 主数据源；按同一文本键提取多语言正式游戏文本 | High |
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
"""

    (game_dir / "README.md").write_text(zh_readme, encoding="utf-8")
    (game_dir / "README_EN.md").write_text(en_readme, encoding="utf-8")
    (game_dir / "README_JP.md").write_text(jp_readme, encoding="utf-8")
    (out_root / "README.md").write_text(sub_readme, encoding="utf-8")
    for lang in LANGS:
        lang_readme = f"""# NTE Glossary - {LANGUAGE_LABELS[lang]} (`{lang}`)

This folder contains **{sum(counts[lang].values()):,}** aligned terminology rows in **{len(CATEGORIES)}** CSV files.

Every file has exactly three columns: `source`, `target`, `tgt_lng`. The `tgt_lng` value is always `{lang}`. Rows are generated only when the target game localization text exists for the same upstream text key.

Rebuild from the game directory with `python tools/build_nte_glossary.py`.
"""
        (out_root / lang / "README.md").write_text(lang_readme, encoding="utf-8")
    sources_dir = game_dir / "Sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    (sources_dir / "README.md").write_text(sources, encoding="utf-8")


def main() -> None:
    args = parse_args()
    game_dir = Path(__file__).resolve().parents[1]
    out_root = args.out or (game_dir / "nte-glossary")
    loaded = load_localization(args.assets_root)
    catalog = build_catalog(loaded)
    counts = build_rows(catalog)
    total = sum(sum(values.values()) for values in counts.values())
    concept_counts = {category: len(entries) for category, entries in catalog.items()}
    unique_concepts = len(set().union(*(set(entries) for entries in catalog.values())))
    source_targets: dict[tuple[str, str], set[str]] = defaultdict(set)
    for target_lang in LANGS:
        for category in CATEGORIES:
            for values in catalog[category].values():
                target = values.get(target_lang)
                if not target:
                    continue
                for source_lang, source in values.items():
                    if source_lang != target_lang and source != target:
                        source_targets[(target_lang, source)].add(target)
    conflicts = sum(1 for targets in source_targets.values() if len(targets) > 1)

    print(f"game_version={args.game_version}")
    print(f"total_rows={total}")
    for target_lang in LANGS:
        print(f"{target_lang}\t{sum(counts[target_lang].values())}")
    for category in CATEGORIES:
        print(f"{category}\tconcepts={concept_counts[category]}\trows={sum(counts[x][category] for x in LANGS)}")
    if args.dry_run:
        return

    for target_lang in LANGS:
        for category in CATEGORIES:
            rows: list[tuple[str, str, str]] = []
            for values in catalog[category].values():
                target = values.get(target_lang)
                if not target or not valid_term(target, category):
                    continue
                for source_lang, source in values.items():
                    if source_lang == target_lang or source == target:
                        continue
                    if valid_term(source, category):
                        rows.append((source, target, target_lang))
            write_csv(out_root / target_lang / f"{category}.csv", rows)

    stats = {
        "generated": date.today().isoformat(),
        "game_version": args.game_version,
        "source_url": SOURCE_URL,
        "source_commit": args.source_commit,
        "source_count": 3,
        "checked_source_count": 9,
        "languages": list(LANGS),
        "categories": list(CATEGORIES),
        "counts": counts,
        "concept_counts": concept_counts,
        "totals": {lang: sum(counts[lang].values()) for lang in LANGS},
        "grand_total": total,
        "conflicts": conflicts,
        "unique_concepts": unique_concepts,
        "concept_total_across_categories": sum(concept_counts.values()),
        "confirmed_concepts": unique_concepts,
        "unconfirmed_concepts": 0,
        "machine_translation_rows": 0,
        "official_cross_checked_concepts": len(CORE_TERM_KEYS) + 1,
    }
    tools_dir = game_dir / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    (tools_dir / "_counts.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_docs(game_dir, out_root, stats)
    print(f"wrote {out_root}")
    print(f"wrote {tools_dir / '_counts.json'}")


if __name__ == "__main__":
    main()
