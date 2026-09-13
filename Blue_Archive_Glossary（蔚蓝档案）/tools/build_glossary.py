#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《蔚蓝档案》Blue Archive 多语术语库生成脚本。

数据来源（默认从 BA_INPUT_DIR 指向的目录读取克隆好的仓库）：

  RedBeanN-BlueArchive                 官方客户端多语言数据表（6 语言按 Id/键对齐）
  ba-archive-blue-archive              剧情阅览器索引 + 剧情编辑器 Excel 表
  ba-storybook                         社区整理的 JP→CN 剧情对照表

用法（脚本位于 <游戏目录>/tools/ 下，输出默认写回游戏目录）：

  python tools/build_glossary.py
  BA_INPUT_DIR="D:\\src" BA_OUTPUT_DIR="D:\\out" python tools/build_glossary.py

输出：按目标语言拆分的 6 套术语库，每套内部再按分类归档。
"""

from __future__ import annotations

import csv
import io
import json
import os
import re
import subprocess
import sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.dirname(HERE)
INPUT = os.path.abspath(os.environ.get("BA_INPUT_DIR", r"E:\Download\BT\Codex_input"))
# 脚本已移入 <游戏目录>/tools/，术语库数据在游戏目录下，故默认输出到上一级
OUT = os.path.abspath(os.environ.get("BA_OUTPUT_DIR", GAME))

REDBEAN = os.path.join(INPUT, "RedBeanN-BlueArchive", "assets", "data")
ARCHIVE = os.path.join(INPUT, "ba-archive-blue-archive")
VIEWER = os.path.join(ARCHIVE, "apps", "blue-archive-story-viewer")
EDITOR = os.path.join(ARCHIVE, "apps", "blue-archive-story-editor", "src", "assets")
STORYBOOK = os.path.join(INPUT, "ba-storybook")

LANGS = ["zh-CN", "ja-JP", "zh-TW", "en-US", "ko-KR", "th-TH"]
REGION = {
    "zh-CN": "cn",
    "ja-JP": "jp",
    "zh-TW": "tw",
    "en-US": "en",
    "ko-KR": "kr",
    "th-TH": "th",
}
TEXT_FIELD = {
    "zh-CN": "TextCn",
    "ja-JP": "TextJp",
    "zh-TW": "TextTw",
    "en-US": "TextEn",
    "ko-KR": "TextKr",
    "th-TH": "TextTh",
}
LABELS = {}


# --------------------------------------------------------------------------- #
# 基础工具
# --------------------------------------------------------------------------- #
def norm(value):
    """折叠空白、去掉注音标记，得到干净的词条文本。"""
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\[ruby=[^\]]*\]|\[/ruby\]|\[\-?\]", "", text)
    text = text.replace("\u200b", "").replace("\ufeff", "")
    return re.sub(r"\s+", " ", text).strip()


def entry(eid, src_table, values):
    """构造一个词条；过滤空值，少于 2 种语言时视为无效。"""
    vals = {}
    for lang in LANGS:
        text = norm(values.get(lang))
        if text:
            vals[lang] = text
    if len(vals) < 2:
        return None
    return {"id": eid, "src_table": src_table, "values": vals}


def _load(path):
    with io.open(path, encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=None)
def rb_min(region, name):
    return _load(os.path.join(REDBEAN, region, name + ".min.json"))


@lru_cache(maxsize=None)
def rb_full(region, name):
    return _load(os.path.join(REDBEAN, region, name + ".json"))


@lru_cache(maxsize=None)
def rb_table(region, name):
    """返回 {str(Id): row}。"""
    rows = rb_min(region, name)
    if isinstance(rows, dict):
        return {str(k): v for k, v in rows.items()}
    return {str(row["Id"]): row for row in rows}


@lru_cache(maxsize=None)
def localization(region):
    """localization.json 的完整键集合（完整版与精简版互补）。"""
    merged = dict(rb_full(region, "localization"))
    for key, value in rb_min(region, "localization").items():
        merged.setdefault(key, value)
    return merged


@lru_cache(maxsize=1)
def storybook():
    return _load(os.path.join(STORYBOOK, "utils", "translation_table.json"))


@lru_cache(maxsize=1)
def stages():
    return _load(os.path.join(REDBEAN, "stages.json"))


@lru_cache(maxsize=1)
def load_ts_titles():
    """剧情阅览器索引里的多语标题（优先现取现用，失败则回落到缓存）。"""
    script = os.path.join(HERE, "extract_ts_titles.mjs")
    if os.path.exists(script):
        try:
            subprocess.run(
                ["node", script],
                cwd=HERE,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except (OSError, subprocess.CalledProcessError):
            pass
    return _load(os.path.join(HERE, "ts_titles.json"))


MOMOTALK_DIR = os.path.join(VIEWER, "public", "config", "yaml", "momotalk")


def iter_momotalk_titles():
    """产出 MomoTalk 会话标题（六语齐全）。"""
    if not os.path.isdir(MOMOTALK_DIR):
        return
    for fname in sorted(os.listdir(MOMOTALK_DIR)):
        if not fname.endswith(".yml"):
            continue
        char_id = fname[:-4]
        with io.open(os.path.join(MOMOTALK_DIR, fname), encoding="utf-8") as handle:
            lines = handle.read().split("\n")
        block = False
        current = None
        for raw in lines:
            if raw.startswith("title:"):
                block = True
                continue
            if block and raw and not raw.startswith(" "):
                block = False
            if not block:
                continue
            stripped = raw.strip()
            if stripped.startswith("- "):
                if current:
                    yield char_id, current
                current = {}
                stripped = stripped[2:]
            if current is None:
                continue
            match = re.match(r"^(Text(?:Cn|Tw|En|Jp|Kr|Th)):\s*(.*)$", stripped)
            if match:
                current[match.group(1)] = norm(match.group(2).strip("\"'"))
                continue
            cont = re.match(r"^\s{2,}([A-Za-z][^\t:]*?)\s*$", raw)
            if cont and current:
                last = list(current)[-1]
                if last.startswith("Text"):
                    current[last] = norm(current[last] + " " + cont.group(1))
        if current:
            yield char_id, current


@lru_cache(maxsize=1)
def scenario_names():
    """剧情角色名表（JP / KR / CN 三语 + 昵称）。"""
    path = os.path.join(EDITOR, "excel", "ScenarioCharacterNameExcelTable.json")
    payload = _load(path)
    rows = payload.get("DataList", payload) if isinstance(payload, dict) else payload
    seen = set()
    out = []
    for row in rows:
        jp = norm(row.get("NameJp") or row.get("NameJP"))
        if not jp or jp in seen:
            continue
        seen.add(jp)
        out.append(
            {
                "id": "ScenarioCharacter.%s" % row.get("CharacterName", len(out)),
                "jp": jp,
                "kr": norm(row.get("NameKr") or row.get("NameKR")),
                "cn": norm(row.get("NameCn") or row.get("NameCN")),
                "src_table": "ScenarioCharacterNameExcelTable.json",
            }
        )
    return out


# --------------------------------------------------------------------------- #
# 分类构建（官方多语言表）
# --------------------------------------------------------------------------- #
def full_name(family, personal, name):
    """拼接角色全名。

    变体角色（如「マシロ（水着）」）的 Name 带后缀而 PersonalName 不带，
    联动角色（如「初音ミク」）的 Name 本身就已包含姓氏，需要分别处理。
    """
    family = norm(family)
    personal = norm(personal)
    name = norm(name)
    if not name or name == personal:
        return family + personal
    if family and name.startswith(family):
        return name
    return family + name


def build_character():
    tables = {lang: rb_full(REGION[lang], "students") for lang in LANGS}
    ids = sorted(tables["ja-JP"], key=lambda value: int(value))
    out = []
    for sid in ids:
        out.append(
            entry(
                "Student.%s" % sid,
                "students.json",
                {lang: tables[lang].get(sid, {}).get("Name") for lang in LANGS},
            )
        )
    # 全名（中日韩的姓名顺序为「姓+名」，英文与泰文相反，官方数据无法直接拼接，故只生成中日韩三种语言）
    for sid in ids:
        out.append(
            entry(
                "Student.%s.full" % sid,
                "students.json",
                {
                    lang: full_name(
                        tables[lang].get(sid, {}).get("FamilyName"),
                        tables[lang].get(sid, {}).get("PersonalName"),
                        tables[lang].get(sid, {}).get("Name"),
                    )
                    for lang in ("zh-CN", "ja-JP", "zh-TW", "ko-KR")
                },
            )
        )
    return out


def build_school():
    loc = {lang: localization(REGION[lang]) for lang in LANGS}
    out = []
    for code in loc["ja-JP"]["School"]:
        out.append(
            entry(
                "School.%s" % code,
                "localization.json:School",
                {lang: loc[lang]["School"].get(code) for lang in LANGS},
            )
        )
    for code in loc["ja-JP"]["SchoolLong"]:
        long_vals = {lang: loc[lang]["SchoolLong"].get(code) for lang in LANGS}
        short_vals = {lang: loc[lang]["School"].get(code) for lang in LANGS}
        if {k: norm(v) for k, v in long_vals.items()} == {
            k: norm(v) for k, v in short_vals.items()
        }:
            continue
        out.append(
            entry("SchoolLong.%s" % code, "localization.json:SchoolLong", long_vals)
        )
    return out


def build_club():
    loc = {lang: localization(REGION[lang]) for lang in LANGS}
    return [
        entry(
            "Club.%s" % code,
            "localization.json:Club",
            {lang: loc[lang]["Club"].get(code) for lang in LANGS},
        )
        for code in loc["ja-JP"]["Club"]
    ]


def build_event():
    loc = {lang: localization(REGION[lang]) for lang in LANGS}
    out = [
        entry(
            "EventName.%s" % code,
            "localization.json:EventName",
            {lang: loc[lang]["EventName"].get(code) for lang in LANGS},
        )
        for code in loc["ja-JP"]["EventName"]
    ]
    for index, (key, row) in enumerate(sorted(storybook()["events"].items())):
        out.append(
            entry(
                "StoryEvent.%s" % key,
                "translation_table.json:events",
                {"ja-JP": row.get("jp"), "zh-CN": row.get("cn")},
            )
        )
    return out


def build_favor_item():
    tables = {lang: rb_table(REGION[lang], "items") for lang in LANGS}
    ids = [i for i, row in tables["ja-JP"].items() if row.get("Category") == "Favor"]
    ids.sort(key=int)
    return [
        entry(
            "Item.%s" % i,
            "items.json",
            {lang: tables[lang].get(i, {}).get("Name") for lang in LANGS},
        )
        for i in ids
    ]


def build_item():
    tables = {lang: rb_table(REGION[lang], "items") for lang in LANGS}
    ids = [i for i, row in tables["ja-JP"].items() if row.get("Category") != "Favor"]
    ids.sort(key=int)
    return [
        entry(
            "Item.%s" % i,
            "items.json",
            {lang: tables[lang].get(i, {}).get("Name") for lang in LANGS},
        )
        for i in ids
    ]


def build_equipment():
    tables = {lang: rb_table(REGION[lang], "equipment") for lang in LANGS}
    ids = sorted(tables["ja-JP"], key=int)
    return [
        entry(
            "Equipment.%s" % i,
            "equipment.json",
            {lang: tables[lang].get(i, {}).get("Name") for lang in LANGS},
        )
        for i in ids
    ]


def build_furniture():
    tables = {lang: rb_table(REGION[lang], "furniture") for lang in LANGS}
    ids = sorted(tables["ja-JP"], key=int)
    return [
        entry(
            "Furniture.%s" % i,
            "furniture.json",
            {lang: tables[lang].get(i, {}).get("Name") for lang in LANGS},
        )
        for i in ids
    ]


def build_enemy():
    tables = {lang: rb_table(REGION[lang], "enemies") for lang in LANGS}
    ids = sorted(tables["ja-JP"], key=int)
    return [
        entry(
            "Enemy.%s" % i,
            "enemies.json",
            {lang: tables[lang].get(i, {}).get("Name") for lang in LANGS},
        )
        for i in ids
    ]


def build_skill():
    tables = {lang: rb_full(REGION[lang], "students") for lang in LANGS}
    out = []
    for sid in sorted(tables["ja-JP"], key=lambda value: int(value)):
        skills = tables["ja-JP"][sid].get("Skills") or {}
        for kind in skills:
            values = {}
            for lang in LANGS:
                slot = (tables[lang].get(sid, {}).get("Skills") or {}).get(kind) or {}
                values[lang] = slot.get("Name")
            out.append(entry("Skill.%s.%s" % (sid, kind), "students.json:Skills", values))
    return out


def build_stage():
    out = []
    for group in ("Campaign", "Event", "Conquest"):
        for row in stages().get(group, []):
            out.append(
                entry(
                    "Stage.%s.%s" % (group, row.get("Id")),
                    "stages.json:%s" % group,
                    {
                        "zh-CN": row.get("NameCn"),
                        "ja-JP": row.get("NameJp"),
                        "zh-TW": row.get("NameTw"),
                        "en-US": row.get("NameEn"),
                        "ko-KR": row.get("NameKr"),
                        "th-TH": row.get("NameTh"),
                    },
                )
            )
    return out


TERM_KEYS = [
    "SquadType",
    "BulletType",
    "ArmorType",
    "ArmorTypeLong",
    "TacticRole",
    "AdaptationType",
    "SkillType",
    "SkillTypeShort",
    "Stat",
    "StatTooltip",
    "EnemyRank",
    "BossFaction",
    "ItemCategory",
    "ShopCategory",
    "StageType",
    "RaidDifficulty",
    "TimeAttackStage",
    "GroggyCondition",
    "BuffType",
    "BuffName",
    "BuffNameLong",
    "BuffTooltip",
    "CharacterSize",
    "FurnitureSet",
    "VoiceClipGroup",
    "VoiceClip",
    "Shortcut",
    "UI",
    "ui",
    "EnemyTags",
]


def build_terminology():
    loc = {lang: localization(REGION[lang]) for lang in LANGS}
    out = []
    for key in TERM_KEYS:
        table = loc["ja-JP"].get(key) or {}
        for code in table:
            out.append(
                entry(
                    "%s.%s" % (key, code),
                    "localization.json:%s" % key,
                    {lang: (loc[lang].get(key) or {}).get(code) for lang in LANGS},
                )
            )
    for key, row in sorted(storybook()["terms"].items()):
        out.append(
            entry(
                "StoryTerm.%d" % len(out),
                "translation_table.json:terms",
                {"ja-JP": key, "zh-CN": row.get("cn")},
            )
        )
    return out


# --------------------------------------------------------------------------- #
# 分类构建（社区对照表 / 剧情数据，需借官方表补齐语种）
# --------------------------------------------------------------------------- #
def build_story_title(indices):
    out = []
    titles = load_ts_titles()
    for group in ("main", "other", "event"):
        for index, item in enumerate(titles.get(group) or []):
            title = item.get("title") or {}
            out.append(
                entry(
                    "StoryIndex.%s.%d" % (group, index),
                    "story-viewer:%sStoryIndex.ts" % group,
                    {lang: title.get(TEXT_FIELD[lang]) for lang in LANGS},
                )
            )
            for section in item.get("sections") or []:
                sec = section.get("title") or {}
                sid = section.get("story_id")
                out.append(
                    entry(
                        "StoryIndex.%s.%s" % (group, sid if sid is not None else index),
                        "story-viewer:%sStoryIndex.ts" % group,
                        {lang: sec.get(TEXT_FIELD[lang]) for lang in LANGS},
                    )
                )
    for char_id, row in iter_momotalk_titles():
        group_id = row.get("GroupId") or len(out)
        out.append(
            entry(
                "MomoTalk.%s.%s" % (char_id, group_id),
                "momotalk/%s.yml" % char_id,
                {lang: row.get(TEXT_FIELD[lang]) for lang in LANGS},
            )
        )
    for index, (key, row) in enumerate(sorted(storybook()["story_titles"].items())):
        out.append(
            entry(
                "StoryTitle.%d" % index,
                "translation_table.json:story_titles",
                {"ja-JP": key, "zh-CN": row.get("cn")},
            )
        )
    return enrich(out, indices)


def build_location(indices):
    out = []
    for index, (key, row) in enumerate(sorted(storybook()["locations"].items())):
        out.append(
            entry(
                "Location.%d" % index,
                "translation_table.json:locations",
                {"ja-JP": key, "zh-CN": row.get("cn")},
            )
        )
    for item in load_ts_titles().get("eventPlaces") or []:
        out.append(
            entry(
                "EventPlace.%s" % item.get("code"),
                "story-viewer:eventStoryIndex.ts",
                {lang: item.get(TEXT_FIELD[lang]) for lang in LANGS},
            )
        )
    loc = {lang: localization(REGION[lang]) for lang in LANGS}
    for code in loc["ja-JP"].get("ConquestMap") or {}:
        out.append(
            entry(
                "ConquestMap.%s" % code,
                "localization.json:ConquestMap",
                {lang: (loc[lang].get("ConquestMap") or {}).get(code) for lang in LANGS},
            )
        )
    return enrich(out, indices)


def build_scenario_character(indices):
    """剧情角色名。

    先把官方数据表里的六语名称补齐（与学生名表保持一致），
    官方表覆盖不到的 NPC 再回落到客户端剧情名表的简中 / 韩文写法。
    """
    out = []
    for row in scenario_names():
        values = enrich_values({"ja-JP": row["jp"]}, indices)
        values.setdefault("zh-CN", row["cn"])
        values.setdefault("ko-KR", row["kr"])
        out.append(entry(row["id"], row["src_table"], values))
    return out


def enrich(entries, indices):
    for item in entries:
        if item is None:
            continue
        item["values"] = enrich_values(item["values"], indices)
    return entries


def enrich_values(values, indices):
    """用官方多语言表按完全相同的写法补齐缺失语种。"""
    index_jp, index_cn = indices
    merged = dict(values)
    for index, key in ((index_jp, "ja-JP"), (index_cn, "zh-CN")):
        probe = merged.get(key)
        if not probe:
            continue
        found = index.get(probe)
        if not found:
            continue
        for lang, text in found.items():
            merged.setdefault(lang, text)
    return merged


def build_indices(entries):
    index_jp, index_cn = {}, {}
    for item in entries:
        if item is None:
            continue
        if "ja-JP" in item["values"]:
            index_jp.setdefault(item["values"]["ja-JP"], item["values"])
        if "zh-CN" in item["values"]:
            index_cn.setdefault(item["values"]["zh-CN"], item["values"])
    return index_jp, index_cn


# --------------------------------------------------------------------------- #
# 输出


def dedupe_values(entries):
    """折叠六语写法完全相同的重复词条。"""
    seen = set()
    out = []
    for item in entries:
        if item is None:
            continue
        key = tuple(item["values"].get(lang, "") for lang in LANGS)
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


# code, label, builder, 分类性质（core 参与补齐索引 / supp 借用索引）, 是否按六语写法去重
CATEGORY_SPECS = (
    ("01_character", "角色名称", build_character, "core", True),
    ("02_school", "学校", build_school, "core", True),
    ("03_club", "社团", build_club, "core", True),
    ("04_story_title", "剧情标题", build_story_title, "supp", True),
    ("05_favor_item", "爱用品", build_favor_item, "core", True),
    ("06_location", "地名", build_location, "supp", True),
    ("07_terminology", "术语", build_terminology, "core", True),
    ("08_event", "活动", build_event, "core", True),
    ("09_scenario_character", "剧情角色", build_scenario_character, "supp", True),
    ("10_enemy", "敌人", build_enemy, "core", True),
    ("11_skill", "技能", build_skill, "core", False),
    ("12_item", "道具", build_item, "core", True),
    ("13_equipment", "装备", build_equipment, "core", True),
    ("14_furniture", "家具", build_furniture, "core", True),
    ("15_stage", "关卡", build_stage, "core", True),
)


def collect():
    """按固定顺序收集 15 个分类，先建索引再补齐社区来源的词条。"""
    collected = {}
    core_entries = []
    for code, label, builder, kind, dedupe in CATEGORY_SPECS:
        if kind != "core":
            continue
        items = [item for item in builder() if item is not None]
        if dedupe:
            items = dedupe_values(items)
        collected[code] = (label, items)
        core_entries.extend(items)
    indices = build_indices(core_entries)
    for code, label, builder, kind, dedupe in CATEGORY_SPECS:
        if kind != "supp":
            continue
        items = [item for item in builder(indices) if item is not None]
        if dedupe:
            items = dedupe_values(items)
        collected[code] = (label, items)
    return [(code, collected[code][0], collected[code][1]) for code, *_ in CATEGORY_SPECS]


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def language_rows(entries, lang):
    """返回该语言的 (对照行, 词条行)。对照行 = 其他语言写法 → 本语言写法。"""
    gloss = []
    terms = []
    seen = set()
    for item in entries:
        target = item["values"].get(lang)
        if not target:
            continue
        terms.append((item["id"], target, item["src_table"]))
        for src_lang in LANGS:
            if src_lang == lang:
                continue
            source = item["values"].get(src_lang)
            if not source:
                continue
            if source == target:
                # 与目标语言写法相同，属于无需翻译的自我映射
                continue
            pair = (source, target)
            if pair in seen:
                continue
            seen.add(pair)
            gloss.append((source, target, lang))
    return gloss, terms


def build_language(categories, lang):
    base = os.path.join(OUT, lang)
    index_rows = []
    master_gloss = []
    master_terms = []
    stats = {}
    for code, label, entries in categories:
        gloss, terms = language_rows(entries, lang)
        write_csv(
            os.path.join(base, code, "%s_glossary.csv" % code),
            ["source", "target", "tgt_lng"],
            gloss,
        )
        write_csv(
            os.path.join(base, code, "%s_terms.csv" % code),
            ["id", "term", "src_table"],
            terms,
        )
        index_rows.append(
            (
                code,
                label,
                len(terms),
                "%s/%s_glossary.csv" % (code, code),
                "%s/%s_terms.csv" % (code, code),
                lang,
            )
        )
        master_gloss.extend((code,) + row for row in gloss)
        master_terms.extend((code, label) + row for row in terms)
        stats[code] = (label, len(terms), len(gloss))
    total_terms = sum(row[2] for row in index_rows)
    total_rows = len(master_gloss)
    index_rows.append(("TOTAL", "", total_terms, "", "", lang))
    write_csv(
        os.path.join(base, "00_master", "all_glossary.csv"),
        ["category", "source", "target", "tgt_lng"],
        master_gloss,
    )
    write_csv(
        os.path.join(base, "00_master", "all_terms.csv"),
        ["category", "category_label", "id", "term", "src_table"],
        master_terms,
    )
    write_csv(
        os.path.join(base, "00_master", "index.csv"),
        ["category", "label", "term_count", "glossary_file", "terms_file", "target_language"],
        index_rows,
    )
    write_language_readme(lang, stats, total_terms, total_rows)
    return total_terms, total_rows


LANG_NAME = {
    "zh-CN": "简体中文",
    "zh-TW": "繁体中文",
    "en-US": "English",
    "ja-JP": "日本語",
    "ko-KR": "한국어",
    "th-TH": "ภาษาไทย",
}


def write_language_readme(lang, stats, total_terms, total_rows):
    lines = [
        "# 《蔚蓝档案》Blue Archive 术语库 — %s（`%s`）" % (LANG_NAME[lang], lang),
        "",
        "本文件夹是**以 `%s` 为目标语言**的术语库：每一条都是「其他语言词条 → %s」的对照，"
        % (lang, LANG_NAME[lang]),
        "共 **%d** 条词条、%d 行对照（`tgt_lng` 列固定为 `%s`）。" % (total_terms, total_rows, lang),
        "",
        "## 文件",
        "",
        "- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 格式，可直接导入 CAT / 术语管理工具",
        "- `NN_xxx/NN_xxx_terms.csv` — 本语言词条清单（`id, term, src_table`），适合校对与回查",
        "- `00_master/all_glossary.csv` — 全部 %d 个分类的合并术语表" % len(stats),
        "- `00_master/all_terms.csv` — 本语言全部词条清单",
        "- `00_master/index.csv` — 分类索引与条数",
        "",
        "## 分类与条数",
        "",
        "| 分类 | 主题 | 条数 | 对照行 |",
        "| --- | --- | ---: | ---: |",
    ]
    for code, (label, terms, rows) in stats.items():
        lines.append("| `%s` | %s | %d | %d |" % (code, label, terms, rows))
    lines.append("| **合计** | | **%d** | **%d** |" % (total_terms, total_rows))
    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- 译文全部取自官方客户端多语言文本（国服 / 国际服 / 日服 / 韩服 / 泰服）与社区剧情对照表，按同一文本键对齐，非二次翻译；",
            "- 每条词条会把其他语言的写法全部展开为对照行，因此也可反向当作「%s → 其他语言」查询；" % lang,
            "- 六种语言的标签：`zh-CN` 简体中文、`zh-TW` 繁体中文、`en-US` 英文、`ja-JP` 日文、`ko-KR` 韩文、`th-TH` 泰文；",
            "- 极少数词条会出现一条 `source` 对应多个 `target` 的情况（多为同名不同物的短词，或简繁两套客户端写法并存）；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `_terms.csv` 里的 `id` 与 `src_table` 回查上下文；",
            "- 文件编码为 UTF-8 with BOM，Excel 双击即可正确显示中日韩泰文字。",
            "",
        ]
    )
    path = os.path.join(OUT, lang, "00_master", "README.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CRLF.join(lines))


CRLF = "\r\n"


def category_tree(categories):
    width = 1 + max(len(code) for code, _, _ in categories)
    width = max(width, len("00_master/")) + 1
    lines = [
        "Blue_Archive_Glossary（蔚蓝档案）/",
        "  <目标语言>/                6 套独立术语库：zh-CN / ja-JP / zh-TW / en-US / ko-KR / th-TH",
        "    ├─ %-*s %s" % (width, "00_master/", "索引 + 合并总表 + 说明"),
    ]
    for index, (code, label, _) in enumerate(categories):
        branch = "└─" if index == len(categories) - 1 else "├─"
        lines.append("    %s %-*s %s" % (branch, width, code + "/", label))
    lines.extend(
        [
            "  multilingual/            六语并排总表",
            "  tools/                   生成脚本与生成元数据",
            "    build_glossary.py      生成脚本",
            "    extract_ts_titles.mjs  剧情标题提取脚本（需要 Node.js）",
            "    ts_titles.json         剧情标题提取结果（脚本的缓存）",
            "  README.md                本说明（简体中文）",
            "  README_EN.md             英文说明",
            "  README_JP.md             日文说明",
        ]
    )
    return CRLF.join(lines)


def build_multilingual(categories):
    base = os.path.join(OUT, "multilingual")
    header = ["category", "category_label", "id"] + LANGS + ["src_table"]
    master = []
    for code, label, entries in categories:
        rows = []
        for item in entries:
            rows.append(
                [code, label, item["id"]]
                + [item["values"].get(lang, "") for lang in LANGS]
                + [item["src_table"]]
            )
        write_csv(os.path.join(base, code, "%s_multilingual.csv" % code), header, rows)
        master.extend(rows)
    write_csv(os.path.join(base, "00_master", "all_terms_multilingual.csv"), header, master)
    write_multilingual_readme(len(master))
    return len(master)


def write_multilingual_readme(total):
    lines = [
        "# 六语并排总表",
        "",
        "把 15 个分类的全部 **%d** 条词条按「一条一行」摊开展示，方便横向比对与二次加工。" % total,
        "",
        "## 文件",
        "",
        "- `00_master/all_terms_multilingual.csv` — 全部词条",
        "- `NN_xxx/NN_xxx_multilingual.csv` — 单个分类的词条",
        "",
        "## 列",
        "",
        "| 列 | 说明 |",
        "| --- | --- |",
        "| `category` | 分类编号，例如 `01_character` |",
        "| `category_label` | 分类中文名 |",
        "| `id` | 词条 ID（对应官方数据的 Id / 键名） |",
        "| `zh-CN` | 简体中文 |",
        "| `ja-JP` | 日文 |",
        "| `zh-TW` | 繁体中文 |",
        "| `en-US` | 英文 |",
        "| `ko-KR` | 韩文 |",
        "| `th-TH` | 泰文 |",
        "| `src_table` | 该词条来自哪张表 |",
        "",
        "空白表示该词条在这一语言下没有找到对应写法。若想按目标语言拆开使用，",
        "请直接取上一层目录里对应的语言文件夹。",
        "",
    ]
    path = os.path.join(OUT, "multilingual", "00_master", "README.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CRLF.join(lines))


def write_root_readme(categories, per_language, total_entries):
    lines = [
        "# 《蔚蓝档案》Blue Archive 多语术语库 / ブルーアーカイブ 用語集",
        "",
        "共 **%d** 条词条，按目标语言拆分为 6 套独立术语库，每套内部再按 %d 个分类归档。"
        % (total_entries, len(categories)),
        "",
        "## 目录结构",
        "",
        "```",
        category_tree(categories),
        "```",
        "",
        "## 语言文件夹",
        "",
        "| 文件夹 | 语言 | 词条数 | 对照行数 |",
        "| --- | --- | ---: | ---: |",
    ]
    for lang in LANGS:
        terms, rows = per_language[lang]
        lines.append("| `%s/` | %s | %d | %d |" % (lang, LANG_NAME[lang], terms, rows))
    lines.extend(["", "## 分类与条数", ""])
    lines.append("| 分类 | 主题 | " + " | ".join("`%s`" % lang for lang in LANGS) + " |")
    lines.append("| --- | --- |" + " ---: |" * len(LANGS))
    for code, label, entries in categories:
        cells = [
            str(sum(1 for item in entries if item["values"].get(lang))) for lang in LANGS
        ]
        lines.append("| `%s` | %s | %s |" % (code, label, " | ".join(cells)))
    totals = [
        str(
            sum(
                1
                for _, _, entries in categories
                for item in entries
                if item["values"].get(lang)
            )
        )
        for lang in LANGS
    ]
    lines.append("| **合计** | | " + " | ".join("**%s**" % value for value in totals) + " |")
    lines.extend(
        [
            "",
            "## 每个分类里的两个文件",
            "",
            "**`NN_xxx_glossary.csv` —— 术语表（source / target / tgt_lng）**",
            "",
            "该语言的 `tgt_lng` 固定，`source` 是其余语言的写法，可直接导入术语工具：",
            "",
            "| source | target | tgt_lng |",
            "| --- | --- | --- |",
            "| Aru | 爱露 | zh-CN |",
            "| アル | 爱露 | zh-CN |",
            "| 아루 | 爱露 | zh-CN |",
            "",
            "**`NN_xxx_terms.csv` —— 本语言词条清单（id / term / src_table）**",
            "",
            "| id | term | src_table |",
            "| --- | --- | --- |",
            "| Student.10000 | 爱露 | students.json |",
            "",
            "## 数据来源",
            "",
            "| 来源 | 用途 |",
            "| --- | --- |",
            "| [RedBeanN/BlueArchive](https://github.com/RedBeanN/BlueArchive) | 官方客户端多语言数据表（`students` / `items` / `equipment` / `enemies` / `furniture` / `localization` / `stages`），六种语言按 Id 与文本键对齐，是本库的主体 |",
            "| [ba-archive/blue-archive](https://github.com/ba-archive/blue-archive) | 剧情阅览器索引（主线 / 其他 / 地域活动标题、MomoTalk 会话标题）与剧情编辑器名表（剧情角色） |",
            "| [HePudding/ba-storybook](https://github.com/HePudding/ba-storybook) | 社区整理的日→中剧情对照表（剧情标题 / 地名 / 活动 / 剧情角色），用于补齐官方数据表未覆盖的条目 |",
            "",
            "## 说明",
            "",
            "- 六种语言的标签：`zh-CN` 简体中文（国服）、`zh-TW` 繁体中文（国际服）、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어、`th-TH` ภาษาไทย；",
            "- 译文取自官方客户端多语言文本，按同一文本键对齐，属于官方本地化而非二次翻译；",
            "- `zh-CN` 与 `zh-TW` 是两套不同的官方本地化，译名并非总是只差繁简，同一个词在学校短名与全名之间也可能不同（例如 `Gehenna`：简中短名「格黑娜」、全名「歌赫娜」，繁中全名「格黑娜學園」）；",
            "- 同一个名称在不同来源间偶有写法差异，本库以官方数据表为准，社区对照表只用于补齐官方表没有的条目；",
            "- 角色分类另附「全名」条目（姓＋名），仅中日韩三种语言：英文与泰文的姓名顺序与中日韩相反，官方数据没有给出可直接拼接的写法；",
            "- `04_story_title`、`06_location`、`09_scenario_character` 以剧情与社区资料为底，会用官方表按完全相同的写法自动补齐语种，因此并非每条都六语齐全；`09_scenario_character` 里的中日韩学生名同样取自官方表，只有官方表没有的 NPC 才使用客户端名表；",
            "- 同一名称存在多条数据时（例如不同等级的同名敌人）会合并为一条；与目标语言写法完全相同的条目不会写入术语表；",
            "- 极少数词条（约 1%–3%）会在**同一个目标语言文件内**出现一条 `source` 对应多个 `target` 的情况，多来自同名不同物的短词（例如 `Normal` 既是装甲类型也是道具稀有度），或简繁两套客户端写法并存；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `_terms.csv` 里的 `id` 与 `src_table` 回查上下文；",
            "- 重新生成：`python tools/build_glossary.py`（默认读取 `E:\\Download\\BT\\Codex_input`，可用环境变量 `BA_INPUT_DIR` / `BA_OUTPUT_DIR` 覆盖；脚本位于 `tools/`，因此命令行必须带 `tools/` 前缀）。",
            "",
        ]
    )
    with io.open(os.path.join(OUT, "README.md"), "w", encoding="utf-8", newline="") as handle:
        handle.write(CRLF.join(lines))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    categories = collect()
    total_entries = sum(len(entries) for _, _, entries in categories)
    per_language = {}
    for lang in LANGS:
        per_language[lang] = build_language(categories, lang)
    build_multilingual(categories)
    write_root_readme(categories, per_language, total_entries)
    print("categories: %d, entries: %d" % (len(categories), total_entries))
    for code, label, entries in categories:
        present = {lang: sum(1 for item in entries if item["values"].get(lang)) for lang in LANGS}
        print("  %s %s: %d  %s" % (code, label, len(entries), present))
    for lang in LANGS:
        terms, rows = per_language[lang]
        print("  %s: %d terms, %d rows" % (lang, terms, rows))


if __name__ == "__main__":
    main()
