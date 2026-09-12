# -*- coding: utf-8 -*-
"""
Build the Minecraft multilingual glossary from the official in-game language files.

Source : misode/mcmeta (branch `assets`) -> assets/minecraft/lang/<locale>.json
         (mirrors the official Minecraft language files shipped with the game)
Input  : SRC_DIR/mcmeta_lang/<locale>.json
Output : OUT_DIR/<lang>/<category>.csv  and  OUT_DIR/<lang>/extra/<category>.csv

CSV format (same as the rest of this repository):
    source,target,tgt_lng
UTF-8 with BOM, CRLF line endings, RFC 4180 quoting.
For a folder whose target language is T, every entry is emitted once per
*other* language as `source`, with the target language text as `target`.
Identical rows (source == target) and duplicate rows are merged away.
"""
import json, os, csv, collections

SRC_DIR = r"E:\Download\BT\Codex_input"
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "minecraft-glossary")

LANG_FILES = [
    ("zh-CN", "zh_cn"), ("zh-TW", "zh_tw"), ("en-US", "en_us"), ("ja-JP", "ja_jp"),
    ("ko-KR", "ko_kr"), ("fr-FR", "fr_fr"), ("de-DE", "de_de"), ("es-ES", "es_es"),
    ("ru-RU", "ru_ru"), ("pt-BR", "pt_br"), ("it-IT", "it_it"), ("tr-TR", "tr_tr"),
    ("th-TH", "th_th"), ("vi-VN", "vi_vn"),
]

# (file stem, subfolder, prefixes, required suffix) -- first match wins
CATEGORIES = [
    # ---- game content -------------------------------------------------
    ("blocks",                    None,    ["block.minecraft."],                                  None),
    ("items",                     None,    ["item.minecraft."],                                   None),
    ("entities",                  None,    ["entity."],                                           None),
    ("biomes",                    None,    ["biome.minecraft."],                                  None),
    ("enchantments",              None,    ["enchantment.minecraft.", "enchantment.level."],      None),
    ("effects",                   None,    ["effect."],                                           None),
    ("instruments",               None,    ["instrument.minecraft."],                             None),
    ("materials",                 None,    ["trim_material.minecraft."],                          None),
    ("paintings",                 None,    ["painting."],                                         None),
    ("attributes",                None,    ["attribute."],                                        None),
    ("item-groups",               None,    ["itemGroup."],                                        None),
    ("jukebox-songs",             None,    ["jukebox_song.minecraft."],                           None),
    ("trim-patterns",             None,    ["trim_pattern.minecraft."],                           None),
    ("colors",                    None,    ["color.minecraft."],                                  None),
    ("statistics",                None,    ["stat.minecraft.", "stat_type.minecraft."],           None),
    ("maps",                      None,    ["filled_map."],                                       None),
    ("music",                     None,    ["music."],                                            None),
    ("sound-categories",          None,    ["soundCategory."],                                    None),
    ("game-modes",                None,    ["gameMode."],                                         None),
    # ---- text / system ------------------------------------------------
    ("subtitles",                 "extra", ["subtitles."],                                        None),
    ("death-messages",            "extra", ["death."],                                            None),
    ("advancement-titles",        "extra", ["advancements."],                                     ".title"),
    ("advancement-descriptions",  "extra", ["advancements."],                                     ".description"),
    ("gamerules",                 "extra", ["gamerule.", "editGamerule."],                        None),
    ("commands",                  "extra", ["commands.", "command.", "argument.", "arguments.",
                                            "parsing.", "snbt.", "advMode.", "team.", "clear.",
                                            "particle.", "predicate.", "item_modifier.",
                                            "advancement."],                                      None),
    ("gui",                       "extra", ["gui.", "menu.", "container.", "inventory.", "title.",
                                            "spectator.", "spectatorMenu.", "chat.", "chat_screen.",
                                            "book.", "sign.", "hanging_sign.", "lectern.", "recipe.",
                                            "record.", "debug.", "deathScreen.", "merchant.",
                                            "sleep.", "mount.", "chunk.", "advancements."],        None),
    ("options",                   "extra", ["options.", "key.", "controls.", "accessibility.",
                                            "narrator.", "narration.", "language.", "slot.",
                                            "permissions.", "compliance.", "restrictions_screen.",
                                            "chat_restriction."],                                 None),
    ("multiplayer",               "extra", ["multiplayer.", "multiplayerWarning.", "addServer.",
                                            "selectServer.", "connect.", "disconnect.", "lanServer.",
                                            "manageServer.", "known_server_link."],               None),
    ("realms",                    "extra", ["mco.", "realms."],                                   None),
    ("world-management",          "extra", ["selectWorld.", "selecteWorld.", "createWorld.",
                                            "upgradeWorld.", "recover_world.", "optimizeWorld.",
                                            "flat_world_preset.", "generator.", "build.",
                                            "difficulty.", "demo.", "tutorial.", "quickplay.",
                                            "loading.", "download.", "upgrade.", "symlink_warning.",
                                            "outOfMemory.", "screenshot.",
                                            "credits_and_attribution."],                          None),
    ("resource-packs",            "extra", ["pack.", "resourcePack.", "resourcepack.", "dataPack.",
                                            "datapackFailure."],                                  None),
    ("telemetry",                 "extra", ["telemetry.", "telemetry_info."],                     None),
    ("dev-tools",                 "extra", ["structure_block.", "jigsaw_block.", "test.",
                                            "test_block.", "test_instance.", "test_instance_block.",
                                            "mirror."],                                           None),
]
MISC = ("misc", "extra")


def classify(key):
    for name, sub, prefixes, suffix in CATEGORIES:
        if not any(key.startswith(p) for p in prefixes):
            continue
        if suffix and not key.endswith(suffix):
            continue
        return name, sub
    return MISC


def load():
    data = {}
    for code, loc in LANG_FILES:
        with open(os.path.join(SRC_DIR, "mcmeta_lang", loc + ".json"), encoding="utf-8") as fh:
            data[code] = json.load(fh)
    return data


def main():
    data = load()
    codes = [c for c, _ in LANG_FILES]

    # bucket every key that exists in any language file
    all_keys = set()
    for c in codes:
        all_keys |= set(data[c])
    buckets = collections.defaultdict(lambda: collections.defaultdict(list))
    for key in sorted(all_keys):
        name, sub = classify(key)
        buckets[sub][name].append(key)

    SUB = {n: s for n, s, _, _ in CATEGORIES}
    SUB[MISC[0]] = MISC[1]
    names = sorted(SUB)
    counts = collections.defaultdict(dict)
    total_rows = 0

    for code in codes:
        for name in names:
            sub = SUB[name]
            keys = buckets[sub].get(name) or []
            rows = set()
            for key in keys:
                tgt = data[code].get(key, "")
                if not tgt:
                    continue
                for other in codes:
                    if other == code:
                        continue
                    src = data[other].get(key, "")
                    if not src or src == tgt:
                        continue
                    rows.add((src, tgt, code))
            out = sorted(rows, key=lambda r: (r[0].lower(), r[0], r[1]))
            d = os.path.join(OUT_DIR, code, sub) if sub else os.path.join(OUT_DIR, code)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, name + ".csv"), "w", encoding="utf-8-sig", newline="") as fh:
                w = csv.writer(fh, lineterminator="\r\n")
                w.writerow(["source", "target", "tgt_lng"])
                w.writerows(out)
            counts[code][name] = len(out)
            total_rows += len(out)
        print(f"{code}: " + ", ".join(f"{k}={v}" for k, v in sorted(counts[code].items())))

    payload = {
        "note": "entry count per category = number of CSV data rows in that language folder",
        "languages": [{"code": c, "language": cn} for c, cn in
                      [("zh-CN", "简体中文"), ("zh-TW", "繁體中文"), ("en-US", "English"), ("ja-JP", "日本語"),
                       ("ko-KR", "한국어"), ("fr-FR", "Français"), ("de-DE", "Deutsch"), ("es-ES", "Español"),
                       ("ru-RU", "Русский"), ("pt-BR", "Português"), ("it-IT", "Italiano"), ("tr-TR", "Türkçe"),
                       ("th-TH", "ภาษาไทย"), ("vi-VN", "Tiếng Việt")]],
        "categories": {name: {"entries": len(buckets[sub].get(name) or [])} for name, sub in
                       [(n, s) for n, s, _, _ in CATEGORIES] + [("misc", "extra")]},
        "rows": counts,
    }
    with open(os.path.join(OUT_DIR, "_counts.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    print(f"\nTOTAL data rows = {total_rows}")


if __name__ == "__main__":
    main()


