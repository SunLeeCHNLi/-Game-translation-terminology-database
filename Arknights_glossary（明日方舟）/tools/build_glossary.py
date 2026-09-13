# -*- coding: utf-8 -*-
"""Arknights multilingual glossary builder (zh-CN / zh-TW / en-US / ja-JP / ko-KR)."""
import io, os, re, gc, csv, json, collections

ROOT = os.path.dirname(os.path.abspath(__file__))       # <game>/tools
REPO = os.path.dirname(ROOT)                            # <game>
DATA = os.path.join(REPO, "_data", "gamedata")          # 外部数据目录（未随仓库分发）
OUT = os.path.join(REPO, "glossary")                    # <game>/glossary

LANGS = [("zh-CN", "cn"), ("zh-TW", "tw"), ("en-US", "en"), ("ja-JP", "jp"), ("ko-KR", "kr")]
CODES = [c for _, c in LANGS]
KEY = "zh-CN"
CLASSES = ["PIONEER", "WARRIOR", "SNIPER", "TANK", "MEDIC", "SUPPORT", "CASTER", "SPECIAL"]

_C = {}
def load(code, name):
    k = (code, name)
    if k not in _C:
        p = os.path.join(DATA, code, "gamedata", "excel", name + ".json")
        _C[k] = json.load(io.open(p, encoding="utf-8"))
    return _C[k]

def drop():
    _C.clear(); gc.collect()

SEG_MAXLEN = 14
MARK = re.compile(r"<[^<>]{0,60}>|\{[^{}]{0,60}\}")
QUOTE_PAIRS = [("'", "'"), ('"', '"'), ("\u201c", "\u201d"), ("\u300c", "\u300d"),
               ("\u300e", "\u300f"), ("\u300a", "\u300b"), ("\u3010", "\u3011"), ("[", "]")]

def strip_wrap(s):
    changed = True
    while changed and len(s) >= 2:
        changed = False
        for a, b in QUOTE_PAIRS:
            if s.startswith(a) and s.endswith(b) and len(s) > len(a) + len(b) - 1:
                s = s[len(a):len(s) - len(b)].strip()
                changed = True
    return s

def has_word(s):
    return bool(re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7afA-Za-z]", s))

def clean(s):
    if not isinstance(s, str):
        return ""
    s = MARK.sub("", s)
    s = s.replace("\\n", " ").replace("\n", " ").replace("\r", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return strip_wrap(s)

def split_seg(s):
    return MARK.findall(s), MARK.split(s)

def collect(fn):
    """fn(code) -> {id: text}; returns {id: {lang: text}}"""
    res = {}
    for lang, code in LANGS:
        try:
            items = fn(code) or {}
        except Exception:
            items = {}
        for k, v in items.items():
            if isinstance(v, str) and v.strip():
                res.setdefault(k, {})[lang] = v
        drop()
    return res

CATS = collections.OrderedDict()
def add(cat, key, vals, wordy=False, maxlen=0):
    cv = {}
    for lang, v in vals.items():
        c = clean(v)
        if c:
            cv[lang] = c
    if len(cv) < 2:
        return
    if wordy:
        for c in cv.values():
            if len(c) < 2 or not has_word(c):
                return
        k = cv.get(KEY, "")
        if k and maxlen and len(k) > maxlen:
            return
    CATS.setdefault(cat, []).append((key, cv))

def add_map(cat, mapping):
    for k, vals in mapping.items():
        add(cat, k, vals)

def smap(code):
    k = ("sm", code)
    if k not in _C:
        d = {}
        p = os.path.join(DATA, code, "i18n", "string_map.txt")
        for line in io.open(p, encoding="utf-8", errors="replace"):
            line = line.strip()
            if not line.startswith("["):
                continue
            i = line.find("]")
            if i < 1:
                continue
            d.setdefault(line[1:i], line[i + 1:])
        _C[k] = d
    return _C[k]

def sm_collect(keyfilter):
    res = {}
    for lang, code in LANGS:
        d = smap(code)
        for k, v in d.items():
            if keyfilter(k) and v.strip():
                res.setdefault(k, {})[lang] = v
        _C.pop(("sm", code), None)
    return res

# ---------------------------------------------------------------- 01 / 02
def build_operators():
    def allc(code):
        ct = load(code, "character_table")
        return {k: v.get("name") for k, v in ct.items()
                if k.startswith("char_") and (v.get("profession") in CLASSES)}
    ops = collect(allc)
    alter = re.compile(r"^char_1\d{3}_")
    for k, v in ops.items():
        add("01_干员名称", k, v)
        if alter.match(k):
            add("02_干员异格", k, v)

# ---------------------------------------------------------------- 03
def build_profession():
    prof = sm_collect(lambda k: k.startswith("CHARACTER_PROFESSION_"))
    for k, v in prof.items():
        add("03_职业与分支", k, v)
    def subs(code):
        sp = load(code, "uniequip_table").get("subProfDict", {})
        return {k: v.get("subProfessionName") for k, v in sp.items()}
    for k, v in collect(subs).items():
        add("03_职业与分支", k, v)

# ---------------------------------------------------------------- 04 / 05
def skill_names(code):
    st = load(code, "skill_table")
    out = {}
    for sid, sk in st.items():
        lv = sk.get("levels") or []
        if not lv:
            continue
        nm = lv[-1].get("name") or lv[0].get("name")
        if nm:
            out[sid] = nm
    return out

def skill_descs(code):
    st = load(code, "skill_table")
    out = {}
    for sid, sk in st.items():
        lv = sk.get("levels") or []
        if lv:
            d = lv[-1].get("description")
            if d:
                out[sid] = d
    return out

# ---------------------------------------------------------------- 06
def talent_names(code):
    ct = load(code, "character_table")
    out = {}
    for cid, ent in ct.items():
        if not cid.startswith("char_"):
            continue
        for ti, tl in enumerate(ent.get("talents") or []):
            for cand in (tl.get("candidates") or []):
                nm = cand.get("name")
                if nm and nm not in ("Unknown", "???"):
                    out["%s_t%d" % (cid, ti)] = nm
    return out

def talent_descs(code):
    ct = load(code, "character_table")
    out = {}
    for cid, ent in ct.items():
        if not cid.startswith("char_"):
            continue
        for ti, tl in enumerate(ent.get("talents") or []):
            for cand in (tl.get("candidates") or []):
                d = cand.get("description")
                if d:
                    out["%s_t%d_p%s" % (cid, ti, cand.get("requiredPotentialRank"))] = d
    return out

# ---------------------------------------------------------------- 07
def potential_descs(code):
    ct = load(code, "character_table")
    out = {}
    for cid, ent in ct.items():
        if not cid.startswith("char_"):
            continue
        for i, pr in enumerate(ent.get("potentialRanks") or []):
            d = pr.get("description")
            if d:
                out["%s_p%d" % (cid, i)] = d
    return out

def trait_descs(code):
    ct = load(code, "character_table")
    out = {}
    for cid, ent in ct.items():
        if not cid.startswith("char_"):
            continue
        tr = ent.get("trait")
        for i, cand in enumerate((tr or {}).get("candidates") or []):
            d = cand.get("description")
            if d:
                out["%s_tr%d" % (cid, i)] = d
    return out

# ---------------------------------------------------------------- 08 / 16
def module_names(code):
    eq = load(code, "uniequip_table").get("equipDict", {})
    out = {}
    for k, v in eq.items():
        if v.get("uniEquipName"):
            out[k] = v["uniEquipName"]
    return out

def module_types(code):
    infos = load(code, "uniequip_table").get("equipTypeInfos") or []
    out = {}
    for i, v in enumerate(infos):
        nm = v.get("uniEquipTypeName")
        if nm:
            out["type_%s" % i] = nm
    return out

def module_descs(code):
    eq = load(code, "uniequip_table").get("equipDict", {})
    out = {}
    for k, v in eq.items():
        if v.get("uniEquipDesc"):
            out[k] = v["uniEquipDesc"]
    return out

def tower_cards(code):
    ct = load(code, "climb_tower_table")
    out = {}
    for grp in ("mainCards", "subCards"):
        for k, v in (ct.get(grp) or {}).items():
            if v.get("name"):
                out["%s_%s" % (grp, k)] = v["name"]
    return out

def sandbox_items(code):
    sb = load(code, "sandbox_table").get("itemDatas", {})
    return {k: v.get("itemName") for k, v in sb.items()}

# ---------------------------------------------------------------- 09 / 10
def enemies(code, level):
    ed = load(code, "enemy_handbook_table").get("enemyData", {})
    return {k: v.get("name") for k, v in ed.items() if v.get("enemyLevel") == level}

# ---------------------------------------------------------------- 11
def stage_names(code):
    st = load(code, "stage_table").get("stages", {})
    return {k: v.get("name") for k, v in st.items() if v.get("name")}

# ---------------------------------------------------------------- 12
def zone_names(code):
    z = load(code, "zone_table").get("zones", {})
    out = {}
    for k, v in z.items():
        for f in ("zoneNameFirst", "zoneNameSecond", "zoneNameThird"):
            if v.get(f):
                out["%s_%s" % (k, f)] = v[f]
    at = load(code, "activity_table").get("activity", {})
    for aid, av in (at or {}).items():
        for zi, zz in enumerate((av or {}).get("zoneList") or []):
            if zz.get("zoneName"):
                out["%s_z%d" % (aid, zi)] = zz["zoneName"]
    return out

# ---------------------------------------------------------------- 13
def teams(code):
    tb = load(code, "handbook_team_table")
    out = {}
    for k, v in tb.items():
        if isinstance(v, dict) and v.get("powerName"):
            out[k] = v["powerName"]
    return out

# ---------------------------------------------------------------- 14
def activity_names(code):
    at = load(code, "activity_table")
    out = {}
    for k, v in (at.get("basicInfo") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["act_" + k] = v["name"]
    ct = load(code, "climb_tower_table")
    for k, v in (ct.get("seasonInfos") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["tower_" + k] = v["name"]
    cv = load(code, "crisis_v2_table")
    for k, v in (cv.get("seasonInfoDataMap") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["crisis_" + k] = v["name"]
    rg = load(code, "roguelike_topic_table")
    for k, v in (rg.get("topics") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["rogue_" + k] = v["name"]
    return out

# ---------------------------------------------------------------- 15 / 17
def items(code, want_material):
    it = load(code, "item_table").get("items", {})
    pot = potential_ids()
    out = {}
    for k, v in it.items():
        t = v.get("itemType")
        if (t == "MATERIAL") != want_material:
            continue
        if want_material and k in pot:
            continue
        if v.get("name"):
            out[k] = v["name"]
    return out

_POT = None
def potential_ids():
    global _POT
    if _POT is None:
        s = set()
        for tier, m in (load("cn", "item_table").get("potentialItems") or {}).items():
            if isinstance(m, dict):
                for iid in m.values():
                    if isinstance(iid, str):
                        s.add(iid)
        _POT = s
    return _POT

def potential_items(code):
    it = load(code, "item_table")
    items = it.get("items", {})
    out = {}
    for iid in potential_ids():
        v = items.get(iid)
        if isinstance(v, dict) and v.get("name"):
            out["pot_" + iid] = v["name"]
    return out

def rogue_items(code):
    rg = load(code, "roguelike_topic_table").get("details", {})
    out = {}
    for topic, det in rg.items():
        for k, v in (det.get("items") or {}).items():
            if isinstance(v, dict) and v.get("name"):
                out["%s_%s" % (topic, k)] = v["name"]
    return out

# ---------------------------------------------------------------- 18
def story_names(code):
    sr = load(code, "story_review_table")
    out = {}
    for k, v in sr.items():
        if not isinstance(v, dict):
            continue
        for i, iu in enumerate(v.get("infoUnlockDatas") or []):
            if isinstance(iu, dict) and iu.get("storyName"):
                out["%s_s%d" % (k, i)] = iu["storyName"]
    hi = load(code, "handbook_info_table")
    for k, v in (hi.get("npcDict") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["npc_" + k] = v["name"]
    for k, v in (hi.get("handbookDict") or {}).items():
        if isinstance(v, dict) and v.get("infoName"):
            out["hb_" + k] = v["infoName"]
    return out

# ---------------------------------------------------------------- 19
def build_ui():
    ui = sm_collect(lambda k: True)
    for k, v in ui.items():
        if any(x.strip().startswith("#") for x in v.values()):
            continue
        add("19_UI与系统术语", k, v, wordy=True, maxlen=48)

# ---------------------------------------------------------------- 20
def tips(code):
    tp = load(code, "tip_table")
    out = {}
    for i, v in enumerate(tp.get("tips") or []):
        if isinstance(v, dict) and v.get("tip"):
            out["tip_%d" % i] = v["tip"]
    for i, v in enumerate(tp.get("worldViewTips") or []):
        if isinstance(v, dict) and v.get("tip"):
            out["wv_%d" % i] = v["tip"]
    return out

def missions(code):
    m = load(code, "mission_table").get("missions", {})
    return {k: v.get("description") for k, v in m.items()
            if isinstance(v, dict) and v.get("type") == "GUIDE" and v.get("description")}

def equip_descs(code):
    be = load(code, "battle_equip_table")
    out = {}
    for uid, v in be.items():
        for ph in v.get("phases") or []:
            for pi, part in enumerate(ph.get("parts") or []):
                for tb in ("overrideTraitDataBundle", "addOrOverrideTalentDataBundle"):
                    for ci, cand in enumerate((part.get(tb) or {}).get("candidates") or []):
                        d = cand.get("additionalDescription") or cand.get("overrideDescripton")
                        if d:
                            out["%s_%s_%s_%s_%s" % (uid, ph.get("equipLevel"), pi, tb, ci)] = d
    return out

def rooms(code):
    bd = load(code, "building_data")
    out = {}
    for k, v in (bd.get("rooms") or {}).items():
        if isinstance(v, dict) and v.get("name"):
            out["room_" + k] = v["name"]
    return out

# ---------------------------------------------------------------- segments
STOP = set("的 了 和 与 或 使 被 并 且 时 中 后 前 内 外 对 为 以 及 是 在 有 无 不 该 其 所 得 等 每个 所有".split())
BAD_ANY = set("\u7684\u4e86\u5e76\u4e14\u6216\u7b49\u4f7f\u7684\uff0c")
BAD_HEAD = set("\u540e\u524d\u4e2d\u4ee5\u548c\u4e0e\u53ca\u5176\u6240\u6bcf\u8be5\u5c06\u4f1a\u53ef\u80fd")

def _seg_ok(cn):
    if not (2 <= len(cn) <= SEG_MAXLEN):
        return False
    if cn in STOP or re.search(r"[0-9%\uff0b+]", cn):
        return False
    if re.search(r"[\uff0c\u3002\uff01\uff1f\uff1b\uff1a\u3001,.!?;:()\u3010\u3011\[\]\"\'\u201c\u201d]", cn):
        return False
    if any(ch in BAD_ANY for ch in cn) or cn[0] in BAD_HEAD or cn[-1] in BAD_HEAD:
        return False
    return bool(re.search(r"[\u4e00-\u9fff]", cn))

def seg_records(records, cat, min_count=2, max_len=14):
    """Align segments across languages by identical markup tokens, then resolve
    word order differences with corpus-wide majority voting."""
    global SEG_MAXLEN
    SEG_MAXLEN = max_len
    slot = collections.defaultdict(collections.Counter)
    for rid, vals in records:
        if len(vals) < 3:
            continue
        seqs = set(tuple(split_seg(v)[0]) for v in vals.values())
        if len(seqs) != 1:
            continue
        parts = {l: split_seg(v)[1] for l, v in vals.items()}
        if KEY not in parts:
            continue
        n = len(parts[KEY])
        for i in range(n):
            seg = {}
            for l in parts:
                s = re.sub(r"\s+", " ", parts[l][i] if i < len(parts[l]) else "").strip()
                s = strip_wrap(s)
                s = re.sub(r"^[\s,\u3001\u3002.!;:\uff0c\uff01\uff1f\uff1b\uff1a\-\u2013\u2014\u2018\u2019\u201c\u201d~\u301c()\uff08\uff09\u3010\u3011\[\]]+", "", s)
                s = re.sub(r"[\s,\u3001.!;:\uff0c\uff01\uff1f\uff1b\uff1a\-\u2013\u2014~\u301c()\uff08\uff09\u3010\u3011\[\]]+$", "", s)
                if not s or not has_word(s):
                    continue
                if l in ("en-US", "ko-KR") and re.match(r"^(and|or|the|with|to|of|for|in|on|a|an|is|are)\b", s):
                    continue
                seg[l] = s
            cn = seg.get(KEY, "")
            if not _seg_ok(cn):
                continue
            for l, v in seg.items():
                if l == KEY:
                    continue
                slot[(cn, l)][v] += 1
    emitted = 0
    for cn in sorted({k[0] for k in slot}):
        mapping = {KEY: cn}
        total = 0
        ok = True
        for lang, _code in LANGS:
            if lang == KEY:
                continue
            c = slot.get((cn, lang))
            if not c:
                continue
            val, cnt = c.most_common(1)[0]
            s = sum(c.values())
            total += s
            if s > 1 and cnt / float(s) < 0.6:
                ok = False
                break
            if not val or len(val) > 42 or re.search(r",\s|\band\b\s*$", val):
                ok = False
                break
            mapping[lang] = val
        if not ok or total < max(min_count, 3) or len(mapping) < 2:
            continue
        if len({v for v in mapping.values()}) < 2:
            continue
        add(cat, "seg_%s_%d" % (cat, len(CATS.get(cat, []))), mapping)
        emitted += 1
    return emitted

# ---------------------------------------------------------------- run
def main():
    build_operators()
    build_profession()

    add_map("04_技能名称", collect(skill_names))
    seg_records(collect(skill_descs).items(), "05_技能描述关键术语")
    seg_records(collect(talent_descs).items(), "05_技能描述关键术语")
    add_map("06_天赋", collect(talent_names))
    add_map("07_潜能", collect(potential_descs))
    add_map("07_潜能", collect(potential_items))
    add_map("08_模组", collect(module_names))
    add_map("08_模组", collect(module_types))
    add_map("09_敌人", collect(lambda c: enemies(c, "NORMAL")))
    add_map("09_敌人", collect(lambda c: enemies(c, "ELITE")))
    add_map("10_BOSS", collect(lambda c: enemies(c, "BOSS")))
    add_map("11_关卡", collect(stage_names))
    add_map("12_地区", collect(zone_names))
    add_map("13_阵营", collect(teams))
    add_map("14_活动", collect(activity_names))
    add_map("15_道具", collect(lambda c: items(c, False)))
    add_map("16_装备", collect(tower_cards))
    add_map("16_装备", collect(sandbox_items))
    add_map("16_装备", collect(rogue_items))
    add_map("17_材料", collect(lambda c: items(c, True)))
    add_map("18_剧情专有名词", collect(story_names))
    build_ui()
    add_map("20_游戏机制", collect(tips))
    add_map("20_游戏机制", collect(missions))
    add_map("20_游戏机制", collect(rooms))
    seg_records(collect(trait_descs).items(), "20_游戏机制", max_len=12)
    seg_records(collect(potential_descs).items(), "20_游戏机制", max_len=12)
    seg_records(collect(module_descs).items(), "20_游戏机制", max_len=12)
    seg_records(collect(equip_descs).items(), "20_游戏机制", max_len=12)

    os.makedirs(OUT, exist_ok=True)
    summary = {"generated": None, "categories": {}}
    for lang, rcode in LANGS:
        d = os.path.join(OUT, lang)
        os.makedirs(d, exist_ok=True)
        allj = {}
        for cat, recs in CATS.items():
            rows = set()
            for rid, vals in recs:
                tgt = vals.get(lang)
                if not tgt:
                    continue
                for sl, sv in vals.items():
                    if sl == lang or not sv or sv == tgt:
                        continue
                    rows.add((sv, tgt))
            rows = sorted(rows)
            with io.open(os.path.join(d, cat + ".csv"), "w", encoding="utf-8-sig", newline="") as f:
                w = csv.writer(f)
                w.writerow(["source", "target", "tgt_lng"])
                for s, t in rows:
                    w.writerow([s, t, lang])
            allj[cat] = [{"source": s, "target": t, "tgt_lng": lang} for s, t in rows]
            summary["categories"].setdefault(cat, {})
            summary["categories"][cat]["by_lang"] = summary["categories"][cat].get("by_lang", {})
            summary["categories"][cat]["by_lang"][lang] = {"rows": len(rows)}
        io.open(os.path.join(d, "_all.json"), "w", encoding="utf-8").write(
            json.dumps({"tgt_lng": lang, "categories": allj}, ensure_ascii=False))
    for cat, recs in CATS.items():
        s = summary["categories"].setdefault(cat, {})
        s["records"] = len(recs)
        s["records_all5"] = sum(1 for _, v in recs if len(v) == len(LANGS))
        s["present"] = {l: sum(1 for _, v in recs if l in v) for l, _ in LANGS}
    summary["generated"] = "Arknights gamedata (cn/tw/en/jp/kr)"
    io.open(os.path.join(ROOT, "_summary.json"), "w", encoding="utf-8").write(
        json.dumps(summary, ensure_ascii=False, indent=1))
    print(json.dumps({c: len(v) for c, v in CATS.items()}, ensure_ascii=False, indent=1))

main()

