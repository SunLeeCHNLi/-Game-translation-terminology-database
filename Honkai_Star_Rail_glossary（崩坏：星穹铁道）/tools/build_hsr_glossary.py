#!/usr/bin/env python3
"""Build the Honkai: Star Rail multilingual terminology database.

Primary data: DimbreathBot/TurnBasedGameData (client TextMap x13 languages + ExcelOutput).
Structured cross-check / supplementary data: Mar-7th/StarRailRes.

Every concept is keyed by the shared TextMap hash (or a stable entity id for the
sources that carry ids instead of hashes), so translations are aligned by key
instead of by string similarity. Nothing is machine translated.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hsr_common import clean_text, is_valid_term, text_key  # noqa: E402

DATA_ROOT = Path(r"E:\Download\BT\Codex_input")
TBD_ROOT = DATA_ROOT / "TurnBasedGameData"
EXCEL = TBD_ROOT / "ExcelOutput"
TEXTMAP = TBD_ROOT / "TextMap"
STARRAILRES = DATA_ROOT / "StarRailRes" / "index_min"
DEFAULT_OUT = Path(__file__).resolve().parents[1] / "hsr-glossary"

TBD_COMMIT = "4ce30f69b"
TBD_VERSION = "4.5.0"
GAME_VERSION = "4.5.0"
SRR_VERSION = "4.5.0"

LANG_ORDER = [
    "zh-CN", "zh-TW", "en-US", "ja-JP", "ko-KR",
    "fr-FR", "de-DE", "es-ES", "ru-RU", "pt-PT",
    "id-ID", "th-TH", "vi-VN",
]

TEXTMAP_FILES = {
    "zh-CN": ["TextMapCHS.json"],
    "zh-TW": ["TextMapCHT.json"],
    "en-US": ["TextMapEN.json"],
    "ja-JP": ["TextMapJP.json"],
    "ko-KR": ["TextMapKR_0.json", "TextMapKR_1.json"],
    "fr-FR": ["TextMapFR.json"],
    "de-DE": ["TextMapDE.json"],
    "es-ES": ["TextMapES.json"],
    "ru-RU": ["TextMapRU_0.json", "TextMapRU_1.json"],
    "pt-PT": ["TextMapPT.json"],
    "id-ID": ["TextMapID.json"],
    "th-TH": ["TextMapTH_0.json", "TextMapTH_1.json"],
    "vi-VN": ["TextMapVI.json"],
}

SRR_LANG_DIR = {
    "zh-CN": "cn", "zh-TW": "cht", "en-US": "en", "ja-JP": "jp", "ko-KR": "kr",
    "fr-FR": "fr", "de-DE": "de", "es-ES": "es", "ru-RU": "ru", "pt-PT": "pt",
    "id-ID": "id", "th-TH": "th", "vi-VN": "vi",
}

CATEGORIES = [
    "01_character", "02_path", "03_element", "04_skill", "05_trace", "06_eidolon",
    "07_light_cone", "08_relic", "09_item", "10_material", "11_enemy", "12_location",
    "13_faction", "14_quest", "15_stage", "16_event", "17_achievement",
    "18_simulated_universe", "19_forgotten_hall", "20_story", "21_world_lore",
    "22_book", "23_dialogue", "24_system", "25_ui", "26_other",
]

CATEGORY_LABELS = {
    "01_character": ("角色与 NPC", "Characters & NPCs"),
    "02_path": ("命途", "Paths"),
    "03_element": ("属性", "Elements"),
    "04_skill": ("技能", "Skills"),
    "05_trace": ("行迹", "Traces"),
    "06_eidolon": ("星魂", "Eidolons"),
    "07_light_cone": ("光锥", "Light Cones"),
    "08_relic": ("遗器", "Relics"),
    "09_item": ("道具", "Items"),
    "10_material": ("材料", "Materials"),
    "11_enemy": ("敌人", "Enemies"),
    "12_location": ("地点", "Locations"),
    "13_faction": ("阵营与组织", "Factions"),
    "14_quest": ("任务", "Quests"),
    "15_stage": ("关卡与副本", "Stages"),
    "16_event": ("活动", "Events"),
    "17_achievement": ("成就", "Achievements"),
    "18_simulated_universe": ("模拟宇宙", "Simulated Universe"),
    "19_forgotten_hall": ("忘却之庭", "Forgotten Hall"),
    "20_story": ("剧情", "Story"),
    "21_world_lore": ("世界观", "World Lore"),
    "22_book": ("书籍", "Books"),
    "23_dialogue": ("对话", "Dialogue"),
    "24_system": ("系统", "System"),
    "25_ui": ("界面", "UI"),
    "26_other": ("其他", "Other"),
}

NAME_MAX = 80
DESC_MAX = 400

# category -> list of (file, record filter, [(field, kind), ...])
SPECS: dict[str, list[dict]] = {
    "01_character": [
        {"file": "AvatarConfig.json", "fields": [("AvatarName", "name"), ("AvatarFullName", "name")]},
        {"file": "DialogueNPC.json",
         "key_filter": lambda k: k.startswith(("NPCName_", "NPCTitle_", "TalkSentenceName_")),
         "fields": [("InteractTitle", "name")]},
        {"file": "MessageContactsConfig.json", "fields": [("Name", "name")]},
    ],
    "04_skill": [
        {"file": "AvatarSkillConfig.json", "filter": lambda r: r.get("Level") == 1,
         "fields": [("SkillName", "name"), ("SkillDesc", "desc"), ("SkillTag", "name"), ("SkillTypeDesc", "name")]},
    ],
    "05_trace": [
        {"file": "AvatarSkillTreeConfig.json", "filter": lambda r: r.get("Level") == 1,
         "fields": [("PointName", "name"), ("PointDesc", "desc"), ("SimplePointDesc", "desc")]},
    ],
    "06_eidolon": [
        {"file": "AvatarRankConfig.json", "fields": [("Name", "name"), ("Desc", "desc")]},
    ],
    "07_light_cone": [
        {"file": "EquipmentConfig.json", "fields": [("EquipmentName", "name")]},
        {"file": "EquipmentSkillConfig.json", "filter": lambda r: r.get("Level") == 1,
         "fields": [("SkillName", "name"), ("SkillDesc", "desc")]},
    ],
    "08_relic": [
        {"file": "RelicSetConfig.json", "fields": [("SetName", "name")]},
    ],
    "09_item": [
        {"file": "ItemConfig.json", "filter": lambda r: r.get("ItemMainType") != "Material",
         "fields": [("ItemName", "name")]},
    ],
    "10_material": [
        {"file": "ItemConfig.json", "filter": lambda r: r.get("ItemMainType") == "Material",
         "fields": [("ItemName", "name")]},
    ],
    "11_enemy": [
        {"file": "MonsterConfig.json", "fields": [("MonsterName", "name"), ("MonsterIntroduction", "desc")]},
        {"file": "NPCMonsterData.json", "fields": [("NPCName", "name")]},
        {"file": "MonsterGuideSkill.json", "fields": [("SkillName", "name")]},
    ],
    "12_location": [
        {"file": "MazeFloor.json", "fields": [("FloorName", "name")]},
        {"file": "MazeFloorLD.json", "fields": [("FloorName", "name")]},
        {"file": "NavMapTab.json", "fields": [("Name", "name")]},
        {"file": "AreaMapConfig.json", "fields": [("Name", "name")]},
        {"file": "WorldDataConfig.json", "fields": [("WorldName", "name"), ("WorldLanguageName", "name")]},
        {"file": "MapEntranceGroup.json", "fields": [("GroupName", "name")]},
        {"file": "SubNavMapName.json", "fields": [("Name", "name")]},
        {"file": "MappingInfo.json", "fields": [("Name", "name")]},
    ],
    "13_faction": [
        {"file": "AvatarCamp.json", "fields": [("Name", "name")]},
        {"file": "MonsterCamp.json", "fields": [("Name", "name")]},
        {"file": "MessageContactsCamp.json", "fields": [("Name", "name")]},
    ],
    "14_quest": [
        {"file": "MainMission.json", "fields": [("Name", "name")]},
        {"file": "MissionChapterConfig.json",
         "fields": [("ChapterName", "name"), ("StageName", "name"), ("ChapterDesc", "desc")]},
        {"file": "SubMission.json", "filter": lambda r: bool(r.get("TargetText")),
         "name_max": 60, "fields": [("TargetText", "name")]},
    ],
    "15_stage": [
        {"file": "StageConfig.json", "fields": [("StageName", "name")]},
    ],
    "17_achievement": [
        {"file": "AchievementData.json", "fields": [("AchievementTitle", "name")]},
        {"file": "AchievementSeries.json", "fields": [("SeriesTitle", "name")]},
    ],
    "18_simulated_universe": [
        {"file": "RogueAeonDisplay.json", "fields": [("RogueAeonName", "name"), ("RogueAeonPathName", "name")]},
        {"file": "RogueBonus.json", "fields": [("BonusTitle", "name")]},
        {"file": "RogueHandBookEvent.json", "fields": [("EventTitle", "name")]},
        {"file": "RogueHandBookEventType.json", "fields": [("RogueEventTypeTitle", "name")]},
        {"file": "RogueDLCArea.json", "fields": [("AreaNameID", "name")]},
        {"file": "RogueDLCAeon.json", "fields": [("PlayShortDesc", "desc")]},
        {"file": "RogueDLCAeonCabinet.json", "fields": [("CabinetName", "name")]},
        {"file": "RogueDLCAeonDiceSurface.json", "fields": [("DiceSurfaceName", "name")]},
        {"file": "RogueDLCBlockIntro.json", "fields": [("BlockIntroName", "name")]},
        {"file": "RogueDLCChessBoardEvent.json", "fields": [("ChessBoardEventName", "name")]},
        {"file": "RogueDLCMainStory.json", "fields": [("MainStoryName", "name")]},
        {"file": "RogueDLCSubStory.json", "fields": [("SubStoryName", "name")]},
        {"file": "RogueDLCSubStoryGroup.json", "fields": [("SubStoryGroupName", "name")]},
        {"file": "RogueTournMiracleDisplay.json", "fields": [("MiracleName", "name")]},
        {"file": "RogueTournHexDisplay.json", "fields": [("Name", "name")]},
        {"file": "RogueTournTitanType.json", "fields": [("TitanTitle", "name")]},
        {"file": "RogueTournWeeklyChallenge.json", "fields": [("WeeklyName", "name")]},
        {"file": "RogueMagicArea.json", "fields": [("AreaNameID", "name")]},
        {"file": "RogueMagicStory.json", "fields": [("StoryName", "name")]},
        {"file": "RogueNousDiceSurface.json", "fields": [("SurfaceName", "name")]},
        {"file": "RogueDLCBlockType.json", "fields": [("BlockTypeNameID", "name")]},
        {"file": "RogueDLCLayer.json", "fields": [("LayerNameID", "name")]},
        {"file": "RogueAreaConfig.json", "fields": [("AreaNameID", "name")]},
    ],
    "19_forgotten_hall": [
        {"file": "ChallengeMazeConfig.json", "fields": [("Name", "name")]},
        {"file": "ChallengeBossMazeConfig.json", "fields": [("Name", "name")]},
        {"file": "ChallengeStoryMazeConfig.json", "fields": [("Name", "name")]},
        {"file": "ChallengePeakConfig.json", "fields": [("Title", "name")]},
        {"file": "ChallengePeakGroupConfig.json", "fields": [("Title", "name")]},
        {"file": "ChallengeGroupConfig.json", "fields": [("GroupName", "name")]},
        {"file": "ChallengeStoryGroupConfig.json", "fields": [("GroupName", "name")]},
        {"file": "ChallengeBossGroupConfig.json", "fields": [("GroupName", "name")]},
        {"file": "ChallengeTargetConfig.json", "fields": [("ChallengeTargetName", "name")]},
        {"file": "ChallengeStoryTargetConfig.json", "fields": [("ChallengeTargetName", "name")]},
        {"file": "ChallengeBossTargetConfig.json", "fields": [("ChallengeTargetName", "name")]},
        {"file": "ChallengeBadgeConfig.json", "fields": [("Name", "name")]},
    ],
    "20_story": [
        {"file": "StoryAtlasTextmap.json", "fields": [("StoryName", "name")]},
        {"file": "AtlasConfig.json", "fields": [("Name", "name")]},
    ],
    "21_world_lore": [
        {"file": "NounAtlas.json", "fields": [("NounTitle", "name"), ("NounDesc", "desc")]},
        {"file": "AtlasUnlockTextmap.json", "fields": [("UnlockDesc", "desc")]},
    ],
    "22_book": [
        {"file": "LocalbookConfig.json", "fields": [("BookInsideName", "name")]},
    ],
    "23_dialogue": [
        {"file": "TalkSentenceConfig.json", "fields": [("TextmapTalkSentenceName", "name")]},
        {"file": "MessageContactsConfig.json", "fields": [("Name", "name")]},
        {"file": "MessageContactsType.json", "fields": [("Name", "name")]},
    ],
    "24_system": [
        {"file": "TutorialGuideData.json", "desc_max": 240, "fields": [("DescText", "desc")]},
        {"file": "TutorialGuideGroup.json", "desc_max": 240, "fields": [("MessageText", "desc")]},
        {"file": "TutorialGuideGroupType.json", "fields": [("MessageTitle", "name")]},
    ],
    "25_ui": [
        {"file": "MenuItemName.json", "fields": [("TextID", "name")]},
        {"file": "MiniMapIcon.json", "fields": [("IconName", "name")]},
        {"file": "GuideChallengeTab.json", "fields": [("Name", "name")]},
        {"file": "GuideRogueTab.json", "fields": [("Name", "name")]},
        {"file": "GuideChallengeData.json", "fields": [("Name", "name")]},
        {"file": "GuideRogueData.json", "fields": [("Name", "name")]},
        {"file": "MapProgressConfig.json", "fields": [("ProgressName", "name")]},
    ],
    "26_other": [
        {"file": "CutSceneConfig.json", "fields": [("CutSceneName", "name")]},
        {"file": "DialogueProp.json", "fields": [("InteractTitle", "name")]},
        {"file": "ItemConfig.json", "filter": lambda r: r.get("ItemMainType") == "Display",
         "fields": [("ItemName", "name")]},
        {"file": "MonsterGuidePhase.json", "fields": [("PhaseName", "name")]},
        {"file": "MonsterGuideTag.json", "fields": [("TagName", "name")]},
    ],
}

# Extra activity/event systems: any ExcelOutput/Activity*.json field whose name ends
# with Name/Title is treated as an event term.
EVENT_GLOBS = [
    "Activity*.json", "Anniv*.json", "ClockPark*.json", "Fever*.json",
    "Heliobus*.json", "AetherDivide*.json",
]
EVENT_FIELD_RE = re.compile(r"(Name|Title)$")
EVENT_SKIP_FIELD_RE = re.compile(
    r"(ConstValueName|TagName|IconName|PrefabName|StateName|PathName|AbilityName"
    r"|Icon|Image|Audio|Voice|Json|Param|BGM|Path$|GroupName$)",
    re.I,
)

# Stable-id concepts taken from StarRailRes (13 languages, current 4.5.0).
SRR_SPECS = [
    ("02_path", "paths.json", "name", "name", ["name", "desc"]),
    ("03_element", "elements.json", "id", "name", ["name", "desc"]),
    ("08_relic", "properties.json", "type", "name", ["name"]),
    ("18_simulated_universe", "simulated_curios.json", "id", "name", ["name"]),
    ("18_simulated_universe", "simulated_blessings.json", "id", "name", ["name"]),
    ("18_simulated_universe", "simulated_events.json", "id", "name", ["name"]),
    ("08_relic", "relics.json", "id", "name", ["name"]),
    ("08_relic", "relic_sets.json", "id", "name", ["name"]),
]


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def iter_records(payload):
    if isinstance(payload, dict):
        return list(payload.values())
    if isinstance(payload, list):
        return payload
    return []


def build_plan() -> tuple[dict[str, dict[str, int]], dict]:
    """Pass 1: collect every TextMap hash used by the spec, per category."""
    plan: dict[str, dict[str, int]] = {cat: {} for cat in CATEGORIES}
    files: set[str] = set()
    missing: list[str] = []

    def add(category: str, field_value, kind: str, name_max: int = NAME_MAX,
            desc_max: int = DESC_MAX) -> None:
        hashed = text_key(field_value)
        if not hashed:
            return
        limit = name_max if kind == "name" else desc_max
        current = plan[category].get(hashed)
        if current is None or limit > current:
            plan[category][hashed] = limit

    for category, entries in SPECS.items():
        for entry in entries:
            name = entry["file"]
            path = EXCEL / name
            if not path.exists():
                if name not in missing:
                    missing.append(name)
                continue
            files.add(name)
            predicate = entry.get("filter")
            for record in iter_records(load_json(path)):
                if not isinstance(record, dict):
                    continue
                if predicate and not predicate(record):
                    continue
                key_filter = entry.get("key_filter")
                for field, kind in entry["fields"]:
                    raw = record.get(field)
                    if key_filter and isinstance(raw, str) and not key_filter(raw):
                        continue
                    add(category, raw, kind, entry.get("name_max", NAME_MAX),
                        entry.get("desc_max", DESC_MAX))

    for pattern in EVENT_GLOBS:
        for path in sorted(EXCEL.glob(pattern)):
            files.add(path.name)
            for record in iter_records(load_json(path)):
                if not isinstance(record, dict):
                    continue
                for field, value in record.items():
                    if not EVENT_FIELD_RE.search(field) or EVENT_SKIP_FIELD_RE.search(field):
                        continue
                    add("16_event", value, "name")

    meta = {"files": sorted(files), "missing": missing}
    return plan, meta


def load_textmaps(lang: str, wanted: set[str]) -> dict[str, str]:
    merged: dict[str, str] = {}
    for name in TEXTMAP_FILES[lang]:
        path = TEXTMAP / name
        if not path.exists():
            continue
        for hashed, raw in load_json(path).items():
            if hashed in wanted:
                merged[hashed] = raw
    return merged


def collect_catalog(plan: dict[str, dict[str, int]]) -> dict[str, dict[str, dict[str, str]]]:
    catalog: dict[str, dict[str, dict[str, str]]] = {cat: defaultdict(dict) for cat in CATEGORIES}
    for lang in LANG_ORDER:
        wanted_by_cat = plan
        all_wanted = set().union(*[set(v) for v in wanted_by_cat.values()]) if wanted_by_cat else set()
        textmap = load_textmaps(lang, all_wanted)
        print(f"  [{lang}] textmap entries kept: {len(textmap):,}")
        for category, wanted in plan.items():
            target = catalog[category]
            for hashed, limit in wanted.items():
                raw = textmap.get(hashed)
                if raw is None:
                    continue
                cleaned = clean_text(raw)
                if is_valid_term(cleaned, limit):
                    target[hashed][lang] = cleaned
    return catalog


RUBY_RE = re.compile(r"\{RUBY_[BE]#[^}]*\}")


def client_text_set(lang: str) -> set[str]:
    """All official localization strings of one language (markup stripped)."""
    values: set[str] = set()
    for name in TEXTMAP_FILES[lang]:
        path = TEXTMAP / name
        if not path.exists():
            continue
        for raw in load_json(path).values():
            if isinstance(raw, str):
                values.add(clean_text(RUBY_RE.sub("", raw)))
    return values


def add_starrailres(catalog: dict[str, dict[str, dict[str, str]]]) -> tuple[int, int]:
    """Add StarRailRes concepts, keeping only text that also exists in the client TextMap."""
    candidates: list[tuple[str, str, str, str]] = []
    for category, filename, _id_field, label, fields in SRR_SPECS:
        per_lang: dict[str, dict] = {}
        for lang, folder in SRR_LANG_DIR.items():
            path = STARRAILRES / folder / filename
            if path.exists():
                per_lang[lang] = load_json(path)
        if not per_lang:
            continue
        ids: set[str] = set()
        for payload in per_lang.values():
            ids.update(payload.keys())
        for entity_id in sorted(ids):
            for field in fields:
                concept = f"srr:{filename}:{entity_id}:{field}"
                limit = NAME_MAX if field == label else DESC_MAX
                for lang in LANG_ORDER:
                    record = per_lang.get(lang, {}).get(entity_id)
                    if not isinstance(record, dict):
                        continue
                    cleaned = clean_text(RUBY_RE.sub("", record.get(field) or ""))
                    if is_valid_term(cleaned, limit):
                        candidates.append((category, concept, lang, cleaned))

    kept = 0
    dropped = 0
    for lang in LANG_ORDER:
        pending = [c for c in candidates if c[2] == lang]
        if not pending:
            continue
        allowed = client_text_set(lang)
        for category, concept, _lang, text in pending:
            if text in allowed:
                catalog[category][concept][lang] = text
                kept += 1
            else:
                dropped += 1
    return kept, dropped


def build_rows(catalog: dict[str, dict[str, dict[str, str]]]):
    """Yield per-language, per-category deduplicated (source, target) rows."""
    rows: dict[str, dict[str, list[tuple[str, str, str]]]] = {}
    conflicts = 0
    for category, concepts in catalog.items():
        per_lang: dict[str, set[tuple[str, str, str]]] = {lang: set() for lang in LANG_ORDER}
        target_index: dict[str, dict[str, set[str]]] = {lang: defaultdict(set) for lang in LANG_ORDER}
        for values in concepts.values():
            for target_lang, target in values.items():
                if not target:
                    continue
                target_index[target_lang][target].add(target)
                bucket = per_lang[target_lang]
                for source_lang, source in values.items():
                    if source_lang == target_lang or source == target:
                        continue
                    bucket.add((source, target, target_lang))
        for lang in LANG_ORDER:
            group = defaultdict(set)
            for source, target, _ in per_lang[lang]:
                group[source].add(target)
            conflicts += sum(1 for targets in group.values() if len(targets) > 1)
        rows[category] = {lang: sorted(per_lang[lang]) for lang in LANG_ORDER}
    return rows, conflicts


def write_csv(path: Path, rows, delimiter: str = ",") -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, delimiter=delimiter, lineterminator="\r\n")
        writer.writerow(["source", "target", "tgt_lng"])
        count = 0
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--skip-starrailres", action="store_true")
    parser.add_argument("--format", choices=("csv", "tsv"), default="csv",
                        help="csv (comma, repository default) or tsv (tab, same three columns)")
    args = parser.parse_args()
    delimiter = "," if args.format == "csv" else "\t"
    extension = args.format

    print("Pass 1: collecting TextMap keys from ExcelOutput ...")
    plan, meta = build_plan()
    concepts_planned = sum(len(v) for v in plan.values())
    print(f"  planned concepts: {concepts_planned:,} across {len(plan)} categories")
    if meta["missing"]:
        print(f"  missing files: {', '.join(meta['missing'])}")

    print("Pass 2: resolving localization per language ...")
    catalog = collect_catalog(plan)

    if not args.skip_starrailres:
        print("Pass 3: adding StarRailRes concepts (paths, elements, affixes, relics) ...")
        kept, dropped = add_starrailres(catalog)
        print(f"  verified against client TextMap: kept {kept:,}, dropped {dropped:,} unverified strings")

    print("Writing CSV files ...")
    rows, conflicts = build_rows(catalog)
    counts: dict[str, dict[str, int]] = {}
    concept_counts: dict[str, int] = {}
    for category in CATEGORIES:
        counts[category] = {}
        concept_counts[category] = len(catalog[category])
        for lang in LANG_ORDER:
            counts[category][lang] = write_csv(
                args.out / lang / f"{category}.{extension}", rows[category][lang], delimiter
            )

    totals = {lang: sum(counts[cat][lang] for cat in CATEGORIES) for lang in LANG_ORDER}
    grand_total = sum(totals.values())
    stats = {
        "generated": date.today().isoformat(),
        "game_version": f"{GAME_VERSION} (TurnBasedGameData {TBD_VERSION}, commit {TBD_COMMIT})",
        "source_count": 2,
        "checked_source_count": 9,
        "languages": LANG_ORDER,
        "categories": CATEGORIES,
        "counts": counts,
        "concept_counts": concept_counts,
        "totals": totals,
        "grand_total": grand_total,
        "conflicts": conflicts,
        "unique_concepts": sum(concept_counts.values()),
        "machine_translation_rows": 0,
    }
    (args.out.parent / "tools").mkdir(parents=True, exist_ok=True)
    (args.out.parent / "tools" / "_counts.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Done. rows={grand_total:,} concepts={stats['unique_concepts']:,} conflicts={conflicts:,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
