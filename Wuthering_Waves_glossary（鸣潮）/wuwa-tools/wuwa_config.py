"""Shared configuration and source-data helpers for the WuWa glossary build."""
from __future__ import annotations

import json
import os
import pickle
import re

SOURCE_ROOT = os.environ.get("WUWA_DATA_ROOT", r"E:\Download\BT\Codex_input")

# Arikatsu/WutheringWaves_Data (game 3.6.0) is the primary text source: its
# MultiText.json is keyed by the same ``Table_Id_Field`` strings as the older
# Dimbreath dump but ships newer content and ten localised languages.
ARIKATSU_ROOT = os.path.join(SOURCE_ROOT, "WutheringWaves_Data")
ARIKATSU_TEXTMAP = os.path.join(ARIKATSU_ROOT, "Textmaps")
ARIKATSU_BINDATA = os.path.join(ARIKATSU_ROOT, "BinData")

# Dimbreath/WutheringData (game 3.1.0) still ships ConfigDB tables whose field
# names are richer than BinData, and fills a handful of keys Arikatsu dropped.
DIMBREATH_ROOT = os.path.join(SOURCE_ROOT, "WutheringData")
DIMBREATH_TEXTMAP = os.path.join(DIMBREATH_ROOT, "TextMap")
DIMBREATH_CONFIGDB = os.path.join(DIMBREATH_ROOT, "ConfigDB")

# (game folder name, glossary language code, native name)
# Russian, Indonesian and Vietnamese ship as empty stubs upstream in both data
# repositories, so they are excluded (see README).
LANGS = [
    ("zh-Hans", "zh-CN", "简体中文"),
    ("zh-Hant", "zh-TW", "繁體中文"),
    ("en", "en-US", "English"),
    ("ja", "ja-JP", "日本語"),
    ("ko", "ko-KR", "한국어"),
    ("fr", "fr-FR", "Français"),
    ("de", "de-DE", "Deutsch"),
    ("es", "es-ES", "Español"),
    ("pt", "pt-BR", "Português"),
    ("th", "th-TH", "ภาษาไทย"),
]

LANG_CODES = [c for _, c, _ in LANGS]
NATIVE = {c: n for _, c, n in LANGS}
GAME_LANG = {c: g for g, c, _ in LANGS}

CATEGORIES = [
    ("characters", "角色名称"),
    ("weapons", "武器名称"),
    ("echoes", "声骸"),
    ("skills", "技能"),
    ("resonant-chains", "共鸣链"),
    ("quests", "任务"),
    ("dungeons", "关卡与挑战"),
    ("regions", "地区与地图"),
    ("factions", "阵营与势力"),
    ("items", "道具与材料"),
    ("monsters", "怪物与生物"),
    ("npcs", "NPC 与说话人"),
    ("achievements", "成就"),
    ("activities", "活动与玩法"),
    ("buffs", "增益与效果"),
    ("voice-lines", "角色语音"),
    ("archives", "档案与读物"),
    ("terms", "术语与百科"),
    ("system", "系统文本"),
    ("ui", "UI 文本"),
    ("tutorials", "教程与引导"),
    ("story", "剧情文本"),
    ("dialogue", "剧情对白"),
    ("other", "其他"),
]
CATEGORY_LABEL = dict(CATEGORIES)

MAX_LEN = {
    "dialogue": 400,
    "ui": 60,
    "other": 80,
    "npcs": 80,
    "system": 150,
    "tutorials": 150,
    "activities": 150,
    "story": 200,
    "items": 250,
    "archives": 400,
    "voice-lines": 250,
    "regions": 250,
    "quests": 250,
    "achievements": 250,
    "dungeons": 250,
    "skills": 250,
    "echoes": 250,
    "monsters": 250,
    "weapons": 250,
    "characters": 300,
    "terms": 250,
    "buffs": 300,
    "resonant-chains": 300,
    "factions": 300,
}
DEFAULT_MAX_LEN = 250

TAG_RE = re.compile(r"<[^<>]{1,160}>")
GENDER_ALT_RE = re.compile(r"\{Male=([^{};]*);Female=[^{}]*\}")
GENDER_TAG_RE = re.compile(r"\{M#([^{}]*)\}\{F#[^{}]*\}|\{F#[^{}]*\}\{M#([^{}]*)\}")
LITERAL_NL_RE = re.compile(r"\\n")
SPACE_RUN_RE = re.compile(r"[ \t\u00a0]{2,}")
NL_RUN_RE = re.compile(r"\n{3,}")


def normalize_text(value: str) -> str:
    """Strip rich-text markup and gender branches, returning display text."""
    s = LITERAL_NL_RE.sub("\n", value)
    s = TAG_RE.sub("", s)
    previous = None
    while previous != s:
        previous = s
        s = GENDER_ALT_RE.sub(lambda m: m.group(1), s)
    s = GENDER_TAG_RE.sub(lambda m: m.group(1) or m.group(2) or "", s)
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("{NON_BREAK_SPACE}", " ").replace("{SPACE}", " ")
    if s.startswith("dnt/"):
        s = s[7:]
    s = SPACE_RUN_RE.sub(" ", s)
    s = "\n".join(line.strip() for line in s.split("\n"))
    s = NL_RUN_RE.sub("\n\n", s)
    return s.strip()


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_arikatsu(lang: str) -> dict:
    path = os.path.join(ARIKATSU_TEXTMAP, lang, "multi_text", "MultiText.json")
    return {row["Id"]: row.get("Content") or "" for row in load_json(path)}


def _load_dimbreath(lang: str) -> dict:
    path = os.path.join(DIMBREATH_TEXTMAP, lang, "MultiText.json")
    return load_json(path)


def load_multitext(game_lang: str) -> dict:
    """Primary text map for one language, backfilled from the older dump."""
    texts = _load_arikatsu(game_lang)
    try:
        older = _load_dimbreath(game_lang)
    except OSError:
        return texts
    added = 0
    for key, value in older.items():
        if value and not texts.get(key):
            texts[key] = value
            added += 1
    if added:
        print(f"    ({game_lang}: backfilled {added} keys from Dimbreath 3.1.0)", flush=True)
    return texts


KEY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,80}$")


def _scan(root: str, keys: set, result: dict) -> int:
    """Record every ConfigDB/BinData field that points at a text key."""
    scanned = 0

    def walk(node, trail, sink):
        if isinstance(node, dict):
            for name, value in node.items():
                walk(value, trail + "/" + str(name), sink)
        elif isinstance(node, list):
            for value in node:
                walk(value, trail, sink)
        elif isinstance(node, str) and node in keys and KEY_RE.match(node):
            sink.append((trail.strip("/"), node))

    for dirpath, _, names in os.walk(root):
        for name in sorted(names):
            if not name.endswith(".json"):
                continue
            path = os.path.join(dirpath, name)
            try:
                data = load_json(path)
            except Exception:
                continue
            scanned += 1
            hits = []
            walk(data, "", hits)
            if not hits:
                continue
            rel = os.path.relpath(path, root).replace("\\", "/")
            stems = {rel.split("/")[-1][:-5]}
            if rel.startswith("Textmaps/") or rel.startswith("TextMap/"):
                parts = rel.split("/")
                if len(parts) > 2:
                    leaf = parts[-1][:-5]
                    if leaf.lower() == "multitext":
                        leaf = parts[-2]
                    stems = {leaf}
            for field, key in hits:
                for stem in stems:
                    result.setdefault(key, set()).add(stem + ":" + field.split("/")[-1])
    return scanned


def config_key_map(cache_path: str, rebuild: bool = False) -> dict:
    """key -> sorted list of ``Table:Field`` references from every data table."""
    if os.path.exists(cache_path) and not rebuild:
        with open(cache_path, "rb") as fh:
            return pickle.load(fh)
    keys = set(_load_arikatsu("en"))
    result: dict[str, set] = {}
    n_bin = _scan(ARIKATSU_BINDATA, keys, result)
    n_cfg = _scan(DIMBREATH_CONFIGDB, keys, result)
    print(f"    scanned {n_bin} BinData + {n_cfg} ConfigDB tables", flush=True)
    result = {k: sorted(v) for k, v in result.items()}
    with open(cache_path, "wb") as fh:
        pickle.dump(result, fh)
    return result
