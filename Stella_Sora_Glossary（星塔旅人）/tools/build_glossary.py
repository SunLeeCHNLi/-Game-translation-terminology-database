# -*- coding: utf-8 -*-
"""Build the Stella Sora (星塔旅人) multilingual terminology base."""
import json, os, re, csv, collections

SRC   = r"E:\Download\BT\Codex_input\StellaSoraData-main\StellaSoraData-main"
OUT   = r"E:\Download\BT\Codex_input\StellaSora_Glossary"
FILES = os.path.join(SRC, "CN", "language", "zh_CN")
BIN   = os.path.join(SRC, "CN", "bin")

REGION = [("zh-CN", "CN", "zh_CN"), ("en-US", "EN", "en_US"), ("ja-JP", "JP", "ja_JP"),
          ("ko-KR", "KR", "ko_KR"), ("zh-TW", "TW", "zh_TW")]
LANGS = [r[0] for r in REGION]
LANGS4 = ["zh-CN", "en-US", "ja-JP", "ko-KR"]

CATS = [
    ("01_character",   "角色名称"),
    ("02_skill",       "技能名称"),
    ("03_potential",   "潜能名称"),
    ("04_disc",        "唱片 / Disc"),
    ("05_item",        "道具"),
    ("06_equipment",   "装备"),
    ("07_enemy",       "敌人"),
    ("08_stage",       "关卡"),
    ("09_event",       "活动"),
    ("10_system",      "系统术语"),
    ("11_ui",          "UI术语"),
    ("12_story",       "剧情专有名词"),
    ("13_faction",     "阵营"),
    ("14_location",    "地点"),
    ("15_terminology", "游戏机制术语"),
]
CATMAP = dict(CATS)

# file -> (category, field numbers to take, mode)
# mode: "name"  = name/label rows, keep as-is
#       "short" = only keep term-like short strings
MAP = {
 "Character.json": ("01_character", ["1"], "name"),
 "CharacterDes.json": ("01_character", ["1"], "name"),
 "CharacterSkin.json": ("01_character", ["1"], "name"),
 "CharacterTag.json": ("01_character", ["1"], "name"),
 "CharacterArchiveBaseInfo.json": ("01_character", ["1"], "name"),
 "NPCAffinityGroup.json": ("01_character", ["1"], "name"),
 "NPCConfig.json": ("01_character", ["1"], "name"),
 "BoardNPC.json": ("01_character", ["1"], "name"),
 "StarTowerNPC.json": ("01_character", ["1"], "name"),
 "SoldierCharacter.json": ("01_character", ["1"], "name"),
 "SoldierPartner.json": ("01_character", ["1"], "name"),
 "SoldierPartnerGroup.json": ("01_character", ["1"], "name"),
 "SoldierSkin.json": ("01_character", ["1"], "name"),
 "TowerDefenseCharacter.json": ("01_character", ["1"], "name"),
 "BreakOutCharacter.json": ("01_character", ["1"], "name"),
 "TrialCharacter.json": ("01_character", ["1"], "name"),
 "AffinityLevel.json": ("01_character", ["1"], "name"),

 "Skill.json": ("02_skill", ["1", "13"], {"1": "name", "13": "short"}),
 "MainSkill.json": ("02_skill", ["1"], "name"),
 "SecondarySkill.json": ("02_skill", ["1"], "name"),
 "SubNoteSkill.json": ("02_skill", ["1"], "name"),
 "SkillInstance.json": ("02_skill", ["1"], "name"),
 "SkillInstanceType.json": ("02_skill", ["1"], "name"),

 "PotentialPreset.json": ("03_potential", ["1"], "name"),
 "SoldierPotential.json": ("03_potential", ["1"], "name"),
 "TowerDefensePotential.json": ("03_potential", ["1"], "name"),
 "VampireTalent.json": ("03_potential", ["1"], "name"),
 "Talent.json": ("03_potential", ["1"], "name"),
 "TalentGroup.json": ("03_potential", ["1"], "name"),

 "DiscIP.json": ("04_disc", ["1", "2", "3"], "name"),
 "DiscTag.json": ("04_disc", ["1"], "name"),

 "ActivityGoods.json": ("05_item", ["1"], "name"),
 "GoldenSpyItem.json": ("05_item", ["1"], "name"),
 "TowerDefenseItem.json": ("05_item", ["1"], "name"),
 "ThrowGiftItem.json": ("05_item", ["1"], "name"),
 "ResidentGoods.json": ("05_item", ["1"], "name"),
 "MiningTreasure.json": ("05_item", ["1"], "name"),
 "Production.json": ("05_item", ["1"], "name"),
 "MallShop.json": ("05_item", ["1"], "name"),
 "MallPackage.json": ("05_item", ["1"], "name"),
 "MallMonthlyCard.json": ("05_item", ["1"], "name"),
 "MallGem.json": ("05_item", ["1"], "name"),
 "ItemPackMark.json": ("05_item", ["1"], "name"),

 "CharGem.json": ("06_equipment", ["1"], "name"),
 "CharGemInstance.json": ("06_equipment", ["1"], "name"),
 "CharGemInstanceType.json": ("06_equipment", ["1"], "name"),

 "MonsterManual.json": ("07_enemy", ["1"], "name"),
 "TowerDefenseMonster.json": ("07_enemy", ["1"], "name"),
 "RegionBoss.json": ("07_enemy", ["1"], "name"),
 "WeekBossType.json": ("07_enemy", ["1"], "name"),
 "TravelerDuelBoss.json": ("07_enemy", ["1"], "name"),
 "ScoreBossAbility.json": ("07_enemy", ["1"], "name"),
 "ScoreBossGetControl.json": ("07_enemy", ["1"], "name"),

 "Chapter.json": ("08_stage", ["1"], "name"),
 "StoryChapter.json": ("08_stage", ["1"], "name"),
 "StorySetChapter.json": ("08_stage", ["1"], "name"),
 "StorySetSection.json": ("08_stage", ["1"], "name"),
 "DailyInstance.json": ("08_stage", ["1"], "name"),
 "DailyInstanceType.json": ("08_stage", ["1"], "name"),
 "InfinityTower.json": ("08_stage", ["1"], "name"),
 "InfinityTowerAffix.json": ("08_stage", ["1"], "name"),
 "InfinityTowerDifficulty.json": ("08_stage", ["1"], "name"),
 "InfinityTowerLevel.json": ("08_stage", ["1"], "name"),
 "JointDrillAffix.json": ("08_stage", ["1"], "name"),
 "JointDrillLevel.json": ("08_stage", ["1"], "name"),
 "JointDrill_2_Level.json": ("08_stage", ["1"], "name"),
 "RegionBossAffix.json": ("08_stage", ["1"], "name"),
 "RegionBossLevel.json": ("08_stage", ["1"], "name"),
 "WeekBossAffix.json": ("08_stage", ["1"], "name"),
 "WeekBossLevel.json": ("08_stage", ["1"], "name"),
 "TravelerDuelBossLevel.json": ("08_stage", ["1"], "name"),
 "TravelerDuelChallengeAffix.json": ("08_stage", ["1"], "name"),
 "TravelerDuelTarget.json": ("08_stage", ["1"], "name"),
 "TowerDefenseLevel.json": ("08_stage", ["1"], "name"),
 "PenguinCardFloor.json": ("08_stage", ["1"], "name"),
 "PenguinCardEndlessLevel.json": ("08_stage", ["1"], "name"),
 "BreakOutLevel.json": ("08_stage", ["1"], "name"),
 "TutorialLevel.json": ("08_stage", ["1"], "name"),
 "CookieLevel.json": ("08_stage", ["1"], "name"),
 "GoldenSpyLevel.json": ("08_stage", ["1"], "name"),
 "GoldenSpyLevelGroup.json": ("08_stage", ["1"], "name"),
 "ActivityLevelsLevel.json": ("08_stage", ["1"], "name"),
 "ActivityIceCreamLevel.json": ("08_stage", ["1"], "name"),
 "ActivityPenguinCardLevel.json": ("08_stage", ["1"], "name"),
 "ActivityAvgLevel.json": ("08_stage", ["1"], "name"),
 "StarTowerGroup.json": ("08_stage", ["1"], "name"),
 "StarTowerGrowthGroup.json": ("08_stage", ["1"], "name"),
 "SoldierEventBattlePool.json": ("08_stage", ["1"], "name"),
 "VampireSurvivor.json": ("08_stage", ["1"], "name"),

 "ActivityGroup.json": ("09_event", ["1"], "short"),
 "ActivityTask.json": ("09_event", ["1"], "short"),
 "ActivityTaskGroup.json": ("09_event", ["1"], "name"),
 "ActivityStory.json": ("09_event", ["1"], "short"),
 "ActivityShop.json": ("09_event", ["1"], "name"),
 "ActivityDouble.json": ("09_event", ["1"], "name"),
 "ActivityDoubleQuest.json": ("09_event", ["1"], "short"),
 "ActivityPenguinCardQuest.json": ("09_event", ["1"], "short"),
 "ActivityPenguinCardQuestGroup.json": ("09_event", ["1"], "name"),
 "StarTowerEventAction.json": ("09_event", ["1"], "short"),
 "StarTowerEventOptionAction.json": ("09_event", ["1"], "short"),
 "StarTowerBookEntrance.json": ("09_event", ["1"], "short"),
 "StarTowerBookEventReward.json": ("09_event", ["1"], "short"),
 "EventOptions.json": ("09_event", ["1"], "short"),
 "EventReminder.json": ("09_event", ["1"], "short"),
 "MiningQuest.json": ("09_event", ["1"], "short"),
 "MiningQuestGroup.json": ("09_event", ["1"], "name"),
 "TowerDefenseQuest.json": ("09_event", ["1"], "short"),
 "TowerDefenseQuestGroup.json": ("09_event", ["1"], "name"),
 "BdConvertCondition.json": ("09_event", ["1"], "short"),
 "BdConvertContent.json": ("09_event", ["1"], "short"),
 "BdConvertControl.json": ("09_event", ["1"], "short"),
 "BdConvertRewardGroup.json": ("09_event", ["1"], "short"),

 "OpenFunc.json": ("10_system", ["1"], "name"),
 "ErrorCode.json": ("10_system", ["1"], "short"),
 "WorldClass.json": ("10_system", ["1"], "short"),
 "Gacha.json": ("10_system", ["1"], "short"),
 "GachaType.json": ("10_system", ["1"], "short"),
 "GachaStorage.json": ("10_system", ["1"], "name"),
 "EnergyBuy.json": ("10_system", ["1"], "name"),
 "NotificationConfig.json": ("10_system", ["1"], "short"),
 "Agent.json": ("10_system", ["2"], "name"),
 "AgentTab.json": ("10_system", ["1"], "name"),
 "AssistQuest.json": ("10_system", ["1"], "short"),
 "BattlePassQuest.json": ("10_system", ["1"], "short"),
 "DailyQuest.json": ("10_system", ["1"], "short"),
 "WeeklyQuest.json": ("10_system", ["1"], "short"),
 "PeriodicQuest.json": ("10_system", ["1"], "short"),
 "TourGuideQuest.json": ("10_system", ["1"], "short"),
 "LevelQuest.json": ("10_system", ["1"], "short"),
 "LevelQuestTarget.json": ("10_system", ["1"], "short"),
 "LoginRewardGroup.json": ("10_system", ["1"], "short"),
 "JointDrillQuest.json": ("10_system", ["1"], "short"),
 "SoldierQuest.json": ("10_system", ["1"], "short"),
 "SoldierQuestGroup.json": ("10_system", ["1"], "name"),
 "StarTowerQuest.json": ("10_system", ["1"], "short"),
 "StarTowerBookFateCardQuest.json": ("10_system", ["1"], "short"),
 "TravelerDuelChallengeQuest.json": ("10_system", ["1"], "short"),
 "VampireSurvivorQuest.json": ("10_system", ["1"], "short"),
 "MallPackagePage.json": ("10_system", ["1"], "name"),
 "MallShopPage.json": ("10_system", ["1"], "name"),
 "MallRecommendGroup.json": ("10_system", ["1"], "short"),
 "ResidentShop.json": ("10_system", ["1"], "name"),

 "UIText.json": ("11_ui", ["1"], "short"),
 "TopBar.json": ("11_ui", ["1"], "short"),
 "JumpTo.json": ("11_ui", ["1"], "short"),
 "Title.json": ("11_ui", ["1"], "name"),
 "Honor.json": ("11_ui", ["1"], "name"),
 "PlayerHead.json": ("11_ui", ["1"], "name"),
 "Achievement.json": ("11_ui", ["1"], "name"),
 "MailTemplate.json": ("11_ui", ["1"], "short"),
 "InteractiveAction.json": ("11_ui", ["1"], "short"),
 "MainScreenCG.json": ("11_ui", ["1"], "name"),
 "CharacterCG.json": ("11_ui", ["1"], "name"),
 "StorySetTab.json": ("11_ui", ["1"], "name"),

 "Story.json": ("12_story", ["1"], "name"),
 "Plot.json": ("12_story", ["1"], "name"),
 "StoryEvidence.json": ("12_story", ["1"], "short"),
 "StoryPreview.json": ("12_story", ["1"], "name"),
 "AffinityQuest.json": ("10_system", ["1"], "short"),
 "NPCAffinityPlot.json": ("12_story", ["1"], "name"),
 "CharacterArchiveContent.json": ("12_story", ["1"], "name"),
 "DatingBranch.json": ("12_story", ["1"], "short"),
 "DatingCharacterEvent.json": ("12_story", ["1"], "short"),
 "DatingLandmarkEvent.json": ("12_story", ["1"], "short"),
 "DatingStartEndEvent.json": ("12_story", ["1"], "short"),
 "StarTowerTalk.json": ("12_story", ["1"], "short"),
 "MangaLoading.json": ("12_story", ["1"], "name"),

 "Force.json": ("13_faction", ["1"], "name"),
 "ContentWord.json": ("13_faction", ["1"], "name"),

 "DatingLandmark.json": ("14_location", ["1"], "name"),
 "StarTower.json": ("14_location", ["1"], "name"),

 "Word.json": ("15_terminology", ["1"], "name"),
 "EffectDesc.json": ("15_terminology", ["1"], "name"),
 "DictionaryEntry.json": ("15_terminology", ["1"], "name"),
 "DictionaryDiagram.json": ("15_terminology", ["1"], "name"),
 "DictionaryTab.json": ("15_terminology", ["1"], "name"),
 "DictionaryTopBarEntry.json": ("15_terminology", ["1"], "name"),
 "StoryPersonality.json": ("15_terminology", ["1"], "name"),
 "StoryRolePersonality.json": ("15_terminology", ["1"], "name"),
 "AssistAttribute.json": ("15_terminology", ["1"], "short"),
 "ProductionType.json": ("15_terminology", ["1"], "name"),
 "SoldierChessType.json": ("15_terminology", ["1"], "name"),
 "SoldierKeyGrade.json": ("15_terminology", ["1"], "name"),
 "SoldierGradeChallenge.json": ("15_terminology", ["1"], "name"),
 "SoldierPositionEffect.json": ("15_terminology", ["1"], "name"),
 "SoldierRecommendBuilds.json": ("15_terminology", ["1"], "name"),
 "SoldierStarterCard.json": ("15_terminology", ["1"], "name"),
 "SoldierStrategyCard.json": ("15_terminology", ["1"], "name"),
 "FateCard.json": ("15_terminology", ["1"], "name"),
 "StarTowerBookFateCard.json": ("15_terminology", ["1"], "name"),
 "StarTowerBookFateCardBundle.json": ("15_terminology", ["1"], "name"),
 "StarTowerGrowthNode.json": ("15_terminology", ["1"], "name"),
 "GoldenSpyBuffCard.json": ("15_terminology", ["1"], "name"),
 "PenguinBaseCard.json": ("15_terminology", ["1"], "name"),
 "PenguinCard.json": ("15_terminology", ["1"], "name"),
 "PenguinCardAide.json": ("15_terminology", ["1"], "name"),
 "PenguinCardBuff.json": ("15_terminology", ["1"], "name"),
 "PenguinCardHandRank.json": ("15_terminology", ["1"], "name"),
 "IceCreamBuff.json": ("15_terminology", ["1"], "name"),
 "MiningSupport.json": ("15_terminology", ["1"], "name"),
 "VampireTalentDesc.json": ("15_terminology", ["1"], "short"),
 "ThrowGiftLevel.json": ("15_terminology", ["1"], "name"),
 "DemonAdvance.json": ("15_terminology", ["1"], "name"),
 "TrialBuild.json": ("15_terminology", ["1"], "name"),
}

ITEM_TYPE_TO_CAT = {
 (1, None): "05_item", (2, 2): "05_item", (2, 6): "05_item", (2, 12): "04_disc",
 (2, 13): "05_item", (2, 24): "05_item", (2, 25): "05_item", (2, 31): "05_item",
 (2, 32): "05_item", (2, 33): "05_item", (2, 34): "05_item", (2, 35): "05_item",
 (2, 40): "04_disc", (2, 44): "05_item", (2, 48): "05_item",
 (3, None): "01_character", (4, None): "05_item", (5, None): "05_item",
 (6, 1): "05_item", (6, 2): "05_item", (6, 19): "15_terminology",
 (6, 41): "03_potential", (6, 42): "03_potential",
 (7, None): "04_disc", (10, None): "01_character", (11, None): "05_item",
 (12, None): "11_ui", (13, None): "11_ui", (14, None): "11_ui",
 (15, None): "05_item", (16, None): "05_item", (17, None): "05_item",
 (18, 1): "05_item", (18, 49): "01_character",
}

TAG_RE = re.compile(r"<[^>]*>")
MARK_RE = re.compile(r"##.*?#\d+#")
BAD_MARKERS = ("\u3010\u4e0d\u8981\u7ffb\u8bd1\u3011", "\u3010\u5e9f\u5f03\u3011",
               "[no trans]", "[NO TRANS]", "TODO", "TBD")

def clean(s):
    if not isinstance(s, str):
        return ""
    s = TAG_RE.sub("", s)
    s = MARK_RE.sub("", s)
    s = s.replace("\u000b", " ").replace("\r", " ").replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def is_bad(s):
    if not s:
        return True
    for m in BAD_MARKERS:
        if m in s:
            return True
    if set(s) <= set("-\u2014\u2026. "):
        return True
    return False

def is_term_like(s):
    if len(s) > 24:
        return False
    if s.endswith(("\u3002", "\uff01", "\uff1f", "\u2026", "\uff5e")):
        return False
    if "  " in s:
        return False
    return True

cache = {}

def load(lang):
    if lang in cache:
        return cache[lang]
    table = {}
    for code, region, folder in REGION:
        if code != lang:
            continue
        base = os.path.join(SRC, region, "language", folder)
        table = {}
        if os.path.isdir(base):
            for fn in os.listdir(base):
                if fn.endswith(".json"):
                    try:
                        table[fn] = json.load(open(os.path.join(base, fn), encoding="utf-8"))
                    except Exception:
                        table[fn] = {}
    cache[lang] = table
    return table

def get(lang, fname):
    return load(lang).get(fname, {})

data = collections.defaultdict(list)   # category -> list of dicts
seen = set()
stats = collections.Counter()

def add(cat, key, row):
    values = tuple(row[l] for l in LANGS)
    sig = (cat, values)
    if values[0] == "" or sig in seen:
        return
    seen.add(sig)
    row["id"] = key
    data[cat].append(row)

def harvest(fname, cat, fields, mode):
    tables = {l: get(l, fname) for l in LANGS}
    base = tables["zh-CN"]
    if not base:
        return
    for key, zh in base.items():
        parts = key.split(".")
        if len(parts) < 3 or parts[-1] not in fields:
            continue
        zhc = clean(zh)
        if is_bad(zhc):
            continue
        fmode = mode.get(parts[-1], "name") if isinstance(mode, dict) else mode
        if fmode == "short" and not is_term_like(zhc):
            continue
        if fmode == "name" and len(zhc) > 20 and ("\u3002" in zhc or "\uff0c" in zhc):
            continue
        if len(zhc) > 60:
            continue
        row = {"src_table": fname}
        for l in LANGS:
            row[l] = clean(tables[l].get(key, ""))
        if not row["en-US"] and not row["ja-JP"] and not row["ko-KR"]:
            continue
        row["zh-CN"] = zhc
        add(cat, key, row)

for cat, label in CATS:
    os.makedirs(os.path.join(OUT, cat), exist_ok=True)

for fname, (cat, fields, mode) in MAP.items():
    harvest(fname, cat, fields, mode)

# ---- Item.json (classified by Type/Stype from the config table) ----
cfg = json.load(open(os.path.join(BIN, "Item.json"), encoding="utf-8"))
tables = {l: get(l, "Item.json") for l in LANGS}
for iid, v in cfg.items():
    t, s = v.get("Type"), v.get("Stype")
    cat = ITEM_TYPE_TO_CAT.get((t, s)) or ITEM_TYPE_TO_CAT.get((t, None))
    if not cat:
        continue
    key = v.get("Title")
    if not key:
        continue
    zhc = clean(tables["zh-CN"].get(key, ""))
    if is_bad(zhc) or len(zhc) > 60:
        continue
    row = {"src_table": "Item.json (Type %s/Stype %s)" % (t, s)}
    for l in LANGS:
        row[l] = clean(tables[l].get(key, ""))
    if not row["en-US"] and not row["ja-JP"] and not row["ko-KR"]:
        continue
    row["zh-CN"] = zhc
    add(cat, key, row)

# ============ curated supplement (verified against aligned in-game text) ============
CURATED = [
    ("菲莱", "Philae", "フィーリエ", "필리에", "菲萊", "14_location"),
    ("菲莱城", "Philae City", "フィーリエ", "필리에", "菲萊城", "14_location"),
    ("埃摩", "Emor", "アモール", "아모르", "埃摩", "14_location"),
    ("埃摩城", "Emor City", "アモール", "아모르", "埃摩城", "14_location"),
    ("灰城区", "Ash District", "アッシュエリア", "애시 에리어", "灰城區", "14_location"),
    ("金城区", "Gold District", "ゴールドエリア", "골드 에리어", "金城區", "14_location"),
    ("银城区", "Silver District", "シルバーエリア", "실버 에리어", "銀城區", "14_location"),
    ("贝林港", "Port Bellin", "ベイリーン港", "베일린 항구", "貝林港", "14_location"),
    ("米拉什", "Mirage", "ミラーシュ", "미라슈", "米拉什", "14_location"),
    ("伊西村", "Eaze Village", "イッシ村", "잇시 마을", "伊西村", "14_location"),
    ("塞尔斯泰", "Sailstead", "セルスティ", "셀스티", "塞爾斯泰", "14_location"),
    ("弗拉维奥", "Flavio", "フラヴィオ", "플라비오", "弗拉維奧", "14_location"),
    ("苍梧城", "Cangwu City", "蒼梧城", "창오성", "蒼梧城", "14_location"),
    ("幸运绿洲号", "The Lucky Oasis", "オアシス号", "럭키 오아시스호", "幸運綠洲號", "14_location"),
    ("诺瓦大陆", "Nova", "ノヴァ大陸", "노바 대륙", "諾瓦大陸", "14_location"),
    ("诺瓦帝国", "Nova Empire", "ノヴァ帝国", "노바 제국", "諾瓦帝國", "14_location"),
    ("星塔", "Monolith", "星ノ塔", "별의 탑", "星塔", "14_location"),
]
for _zh, _en, _ja, _ko, _tw, _cat in CURATED:
    _row = {"id": "curated.%s" % _zh, "zh-CN": _zh, "en-US": _en, "ja-JP": _ja,
            "ko-KR": _ko, "zh-TW": _tw, "src_table": "curated (aligned in-game text)"}
    add(_cat, _row["id"], _row)

# ---- write ----
def write_cat(cat, label, rows):
    d = os.path.join(OUT, cat)
    rows = sorted(rows, key=lambda r: r["id"])
    with open(os.path.join(d, cat + "_terms.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id"] + LANGS + ["src_table"])
        for r in rows:
            w.writerow([r["id"]] + [r[l] for l in LANGS] + [r["src_table"]])
    with open(os.path.join(d, cat + "_glossary.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "target", "tgt_lng"])
        for r in rows:
            for s_lang in LANGS4:
                for t_lang in LANGS4:
                    if s_lang == t_lang:
                        continue
                    if r[s_lang] and r[t_lang]:
                        w.writerow([r[s_lang], r[t_lang], t_lang])
    return len(rows)

total = 0
counts = {}
for cat, label in CATS:
    n = write_cat(cat, label, data[cat])
    counts[cat] = n
    total += n

# ---- master outputs ----
master = os.path.join(OUT, "00_master")
os.makedirs(master, exist_ok=True)
all_rows = []
for cat, label in CATS:
    for r in sorted(data[cat], key=lambda x: x["id"]):
        all_rows.append([cat, label] + [r["id"]] + [r[l] for l in LANGS] + [r["src_table"]])
with open(os.path.join(master, "StellaSora_all_terms.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["category", "category_label", "id"] + LANGS + ["src_table"])
    w.writerows(all_rows)
with open(os.path.join(master, "index.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["category", "label", "term_count", "terms_file", "glossary_file", "languages"])
    for cat, label in CATS:
        w.writerow([cat, label, counts[cat], "%s/%s_terms.csv" % (cat, cat),
                    "%s/%s_glossary.csv" % (cat, cat), ", ".join(LANGS)])
    w.writerow(["TOTAL", "", total, "", "", ""])

print("TOTAL TERMS:", total)
for cat, label in CATS:
    print("%-18s %5d" % (cat, counts[cat]))
