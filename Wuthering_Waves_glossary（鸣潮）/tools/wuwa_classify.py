"""Map every MultiText key to exactly one glossary category."""
from __future__ import annotations

import re

# Ordered rules over the data-table name. First match wins, so entity families
# that own their text come before the catch-all gameplay/UI tables.
CFG_RULES: list[tuple[str, str]] = [
    # ---- 角色 ----
    (r"^(RoleInfo|RoleDescription|RoleQualityInfo|RoleTag|RoleBirthday|RoleSkin|RoleSkinTrialInfo|RoleTrialRoleConfig|RoleTrialRoleInfo|RoleGift|RoleDevelopCurve|RoleDevProsProject|RoleDevTypeManage|RoleDevWeaponItem|RoleDevWeaponJumpGroup|Character|OccupationConfig|NewOccupationConfig|FavorRoleInfo|PersonalTitle|HeadIcon\w*|PlayerHead\w*)$", "characters"),
    # ---- 阵营 / 势力 ----
    (r"^(Country|Influence|RoleInfluence)$", "factions"),
    # ---- 武器 ----
    (r"^(WeaponConf|WeaponReson|WeaponQualityInfo|WeaponQuality|WeaponSkin|WeaponHandBook|WeaponBreach|WeaponLevel|WeaponPropertyGrowth|WeaponHideConfig|WeaponSceneInteract|WeaponVisibleConfig|WeaponModelTransform|TrialWeaponInfo)$", "weapons"),
    # ---- 声骸 ----
    (r"^(PhantomItem|PhantomHandBook|PhantomFetter|PhantomFetterGroup|PhantomSkill|PhantomSkillType|PhantomProp\w*|Phantommanageplan\w*|PhantomManagePlan\w*|TowerDefencePhantom\w*|TowerDefensePhantom\w*)$", "echoes"),
    # ---- 技能 ----
    (r"^(Skill|SkillDescription|SkillType|SkillTree|SkillBranch|SkillCondition|SkillInput|SkillTag|SkillIcon|SkillButtonCustom|SkillButtonText|SkillGameplayButton|SkillAudioEvent|RoleSkillInput|RoleSkillFightTrick|RoleSkillTreeInfo|RoleSkillTreeDesc|ComboTeaching|PassiveSkill\w*)$", "skills"),
    # ---- 共鸣链 ----
    (r"^(ResonantChain|RoleResonance|RoleResonanceGrouth|RoleTrainingDegree)$", "resonant-chains"),
    # ---- 任务 ----
    (r"^(Quest|QuestChapter|QuestStep|QuestType|QuestTag|QuestTreeNode|QuestNodeData|QuestReviewNode|QuestTree|QuestData|QuestRecall|QuestMultiLine|AdventureTask|AdventureTaskChapter|ActivityQuestConfig|TravelTask|TravelPhantomQuest|RoleQuest|QuestTrackingConfig|DailyAdventureTask)$", "quests"),
    # ---- 关卡 / 挑战 ----
    (r"^(InstanceDungeon|InstanceDungeonTitle|DungeonDetection|TowerConfig|TowerTarget|TowerQuickPass|TowerSeason\w*|TowerDifficulty|TowerGuide|NewTower\w*|TowerDefense\w*|TowerDefence\w*|SlashAndTower\w*|SlashTower\w*|Abyss\w*|BabelTowerLevel|BabelTowerDifficulty|BlackSword\w*|CorniceChallenge|LifePointChallenge|SoarChallenge|MotorcycleChallenge|LineCrossChallenge|ParkourChallenge|MowTower\w*|RogueResInstGrid|HardnessMode\w*|WeeklyChallenge\w*)$", "dungeons"),
    # ---- 地区 / 地图 ----
    (r"^(Area|AreaReport|AreaTerminal|AreaTerminalGroup|AreaQuestArea|AreaQuestScreen|AreaMapGroup|AreaAtmosphereInfo|MapMark|DynamicMapMark|MapNote|Mapping|GeographyHandBook|GeographyType|SoundBoxMark|TreasureBoxMark|TreasureBoxDetectorMark|TemporaryTeleportMark|AkiMap|AkiMapSource|Teleporter\w*|Region\w*)$", "regions"),
    # ---- 道具 / 材料 ----
    (r"^(ItemInfo|ItemHandBook|ItemHandBookType|ItemMainType|ItemShowType|ItemAttributeReward|SynthesisFormula|SynthesisLevel|CookFormula|CookLevel|CookProcessed|CookProcessMsg|CookFixTool|SpecialCook|ForgeFormula|Furniture|FavorGoods|PreviewItem|ShopFixed|ShopInfo|ShopBankInfo|BookItem|ChipHandBook|ChipType|Building|AbyssItem|HonamiStoryItem|HonamiStoryWeaponSuit|SurvivorsItem|SurvivorsWeapon\w*|TrapDefenseItem|RougeMiraclecreation|BackgroundCard|CalabashSkin|DrinksDrinkBase|DrinksDrinkMix|DrinksFlavorRange|DrinksOrnament|DrinksRequireList|DrinksRoleLikeDrink|DrinksBatching)$", "items"),
    # ---- 怪物 / 生物 ----
    (r"^(MonsterInfo|MonsterHandBook|MonsterHandBookType|MonsterDisplay|MonsterDetection|MonsterPerch|MonsterRarity|AnimalHandBook|AdvertisingTabEnemy|TrapDefenseMonster\w*|SurvivorsMonsterBody|SilentAreaDetection|MonsterEcology\w*)$", "monsters"),
    # ---- NPC / 说话人 ----
    (r"^(Speaker|NpcHeadInfo|ChatPartner|NpcGroupPerformConfig)$", "npcs"),
    # ---- 成就 ----
    (r"^(Achievement|AchievementCategory|AchievementGroup|AchievementStarLevel)$", "achievements"),
    # ---- 角色语音与档案 ----
    (r"^(FavorWord|FavorStory|FavorBehavior)$", "voice-lines"),
    (r"^(InfoDisplay|InteractData)$", "archives"),
    # ---- 术语 / 百科 ----
    (r"^(BabelTowerDeTerm|Term\w*|PropertyIndex|ElementInfo|ElementalReaction|PhysicsProperty\w*|AttributeShow\w*)$", "terms"),
    # ---- 教程 / 引导 ----
    (r"^(GuideTips|GuideTutorial|GuideTutorialPage|GuideFocusNew|GuideData|SecondaryGuideData|Tutorial\w*|Advice\w*)$", "tutorials"),
    # ---- 系统文本 ----
    (r"^(Text|ErrorCode|ConfirmBox|GenericPrompt|GenericPromptTypes|GeneralTipsTypes|MenuConfig|FunctionMenu|FunctionCondition|HelpText|LoadingTipsText|PersonalTips|PackageCapacity|PackageSort|AccessPath|Condition|ConditionGroup|ConditionType|DetectionText|DetectionTabType|DetectionTitlePanel|DetectionDropDownType|DropPackage|MailFilter|BanInfo|ReportPlayerInfo|CommonParam|SortRule|DaySelectPreset|DeviceInfo|DownLoad\w*|TransitionPopup|Revive|Chat|ChatExpression|ChatBg|QuickChat|ServerLimit|ServerTips|SettleFlag|ScoreReward|ActionType|ActionMapping|CompositeRewardDisplay|CommonRewardViewDisplay|BattlePassUnlockPop|BattlePassTask|BirthDayText|WorldLevel)$", "system"),
    # ---- UI 文本 ----
    (r"^(PrefabTextItem|PrefabRichTextData|HotKeyText|HotKeyMap|UiDynamicTab|UiResource|MainType|DigitalScreenText|UiShow|UiNormalConfig|UiFloatConfig|UiPlayItem|UiCameraMapping|UiWeaponVisibleConfig|SkillButtonText)$", "ui"),
    # ---- 活动 / 玩法 ----
    (r"^(Activity|Activity\w*|Advertising\w*|BattlePass\w*|Rogue\w*|RogueRes\w*|Dango\w*|TrapDefense\w*|Spring\w*|BabelTower\w*|BossRush\w*|Survivors\w*|Turntable\w*|Ciaccona\w*|BlackCoast\w*|DarkCoast\w*|TrackMoon\w*|Calabash\w*|Fishing\w*|Drinks\w*|Motor\w*|Newbie\w*|MoonChasing\w*|Circum\w*|PhotoFight\w*|DreamLink\w*|Consumptive\w*|TimePointReward\w*|WeeklyRogue\w*|PermanentRogue\w*|GiftPackage\w*|DirectTrain\w*|Dice\w*|RacingBets\w*|ScratchCard\w*|Tetris\w*|Pinball\w*|LongShan\w*|WuWu\w*|Kurotato\w*|MoonSignIn|WorldNewJourney|PhantomBattle\w*|MoraleKeepLevel|Cornice\w*|RiskHarvest\w*|Farm\w*|VillageInfr\w*|ShippingHiddenMultiText|BossPiling\w*|Wind\w*)$", "activities"),
    # ---- 增益 / 效果 ----
    (r"^(Buff\w*|TDBuff|BabelDebuff|TowerBuff|CycleTowerBuff|BossRushBuff|HonamiStoryBuffTemp|BuffEquipItem|MonsterBuff\w*|AbnormalDamage\w*|ToughModifier\w*|State\w*|Effect\w*)$", "buffs"),
    # ---- 语音 / 字幕（对白）----
    (r"^(PlotAudio|SubtitleText|VideoCaption|VideoSound|MusicSubTitle|Audio\w*)$", "dialogue"),
    # ---- 剧情 ----
    (r"^(LevelPlay\w*|Flow|Flow\w*|FlowText|RogueResEventStep|EntrustFinishDialog|SpecialDialog\w*|PlotDialog\w*|HonamiStory\w*|Avignon\w*|SceneStep\w*|SceneGameplay\w*|RandomPlot|ActivityGamePlayPlot|VideoData|VideoQte|PlotType|Costume\w*|ArtemisChat|ChatDialog|TrainRoleDialog|SpringChat|DangoBroadcast)$", "story"),
]

CFG_RULE_RE = [(re.compile(p, re.IGNORECASE), c) for p, c in CFG_RULES]
PREFIX_RULE_RE = []  # filled below

# Tables that name a real game entity. A key referenced by one of these keeps
# its entity category even when the key itself looks like a dialogue line.
STRONG_STEMS = {
    "RoleInfo", "RoleDescription", "RoleQualityInfo", "WeaponConf", "WeaponReson",
    "WeaponQualityInfo", "PhantomItem", "PhantomHandBook", "PhantomFetter",
    "PhantomFetterGroup", "PhantomSkill", "Skill", "SkillDescription", "SkillType",
    "SkillTree", "ResonantChain", "RoleResonance", "RoleTrainingDegree", "ItemInfo",
    "ItemHandBook", "ItemMainType", "ItemShowType", "SynthesisFormula", "CookFormula",
    "ForgeFormula", "MonsterInfo", "MonsterHandBook", "AnimalHandBook", "Area",
    "GeographyHandBook", "Country", "Influence", "RoleInfluence", "Achievement",
    "AchievementCategory", "AchievementGroup", "QuestChapter", "QuestType",
    "AdventureTask", "AdventureTaskChapter", "InstanceDungeon", "InstanceDungeonTitle",
    "Speaker", "NpcHeadInfo", "FavorRoleInfo", "FavorWord", "FavorStory", "PropertyIndex",
    "ElementInfo", "ElementalReaction", "BabelTowerDeTerm", "OccupationConfig",
    "NewOccupationConfig", "RoleSkin", "WeaponSkin", "PersonalTitle", "BackgroundCard",
    "PhonographMusic", "BookItem", "Furniture", "FavorGoods", "Building", "ChatPartner",
    "NpcGroupPerformConfig", "PhantomBattleCardRole", "PhantomBattleCard",
    "PhantomBattleChallenge", "PhantomBattleFactor", "PhantomBattleCardGroupInfo",
    "PhantomBattleBadge", "RogueBuffPool", "RogueResBuffPool", "RogueCharacterBuff",
    "RogueResCharacterBuff", "RogueWeeklyBuffPool", "HonamiStoryBuffTemp",
    "TowerTarget", "TowerConfig", "TowerSeason", "MapMark", "DynamicMapMark",
    "ItemHandBookType", "GuideTips", "GuideTutorial", "GuideTutorialPage",
    "GuideFocusNew", "MapNote", "I18nResources",
}
STRONG_STEMS_LOWER = {s.lower() for s in STRONG_STEMS}

# Key shapes. "structure" keys name or summarise story content; "dialogue" keys
# are individual spoken lines (two or more trailing index segments).
STRUCTURE_QUEST_RE = re.compile(r"_Quest(Name|Desc|Detail|Title)")
STRUCTURE_STORY_RE = re.compile(
    r"(ChapterName|ChapterTitle|LevelPlayName|PlotName|PlotTitle|TaskName|StoryName|"
    r"QuestTip|QuestSchedule|InteractContent|DialogueTitle)"
)
DIALOGUE_RE = re.compile(r"_\d+_\d+$")

# Key names that identify a category regardless of the referring table.
KEY_RULES: list[tuple[str, str]] = [
    (r"^Term\d+_", "terms"),
    (r"^(OccupationConfig|NewOccupationConfig)_", "characters"),
    (r"^CharacterDisplayStyle_", "characters"),
    (r"^RoleInfo_", "characters"),
    (r"^WeaponConf_", "weapons"),
    (r"^PhantomItem_", "echoes"),
    (r"^MonsterInfo_", "monsters"),
    (r"^ItemInfo_", "items"),
    (r"^ResonantChain_", "resonant-chains"),
    (r"^SMC_Name_", "npcs"),
    (r"^Speaker_\d+_Name$", "npcs"),
    (r"^Entity_[0-9a-f]{16,}$", "npcs"),
]

PREFIX_RULES: list[tuple[str, str]] = [
    (r"^Speaker_\d+_Name$", "npcs"),
    (r"^Entity_[0-9a-f]{16,}$", "npcs"),
    (r"^(POI|TWTPOI)\w*", "regions"),
    (r"^(MapMark|AkiMap)\w*", "regions"),
    (r"^(Main|MAIN|Side|SIDE|Event|EVENT|Daily|Daliy|DAILY|NPC|GNNPC|FWNPC|STNPC|Character|CHARACTER|LevelPlay|Quest|Flow|Entity|Plot|Dialog|Story)\w*", "story"),
    (r"^Achievement\w*", "achievements"),
    (r"^(Guide|Tutorial)\w*", "tutorials"),
    (r"^(UI|Ui|Prefab)\w*", "ui"),
    (r"^(Text|ErrorCode|ConfirmBox|Menu|Function|Condition)\w*", "system"),
    (r"^(Item|Phantom|Weapon|Skill|Role|Monster)\w*", "items"),
]

PREFIX_RULE_RE = [(re.compile(p), c) for p, c in PREFIX_RULES]
KEY_RULE_RE = [(re.compile(p), c) for p, c in KEY_RULES]
FALLBACK_DIALOGUE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]{0,32}_\d")


def _stem_category(stem: str) -> str | None:
    for regex, cat in CFG_RULE_RE:
        if regex.match(stem):
            return cat
    return None


def stem_of(reference: str) -> str:
    stem = reference.split(":", 1)[0]
    return stem[:-5] if stem.endswith(".json") else stem


def classify(key: str, refs: list[str]) -> str:
    """Return the glossary category for ``key`` given its data-table references."""
    stems = []
    for ref in refs:
        stem = stem_of(ref)
        if stem not in stems:
            stems.append(stem)
    for stem in stems:
        if stem.lower() in STRONG_STEMS_LOWER:
            cat = _stem_category(stem)
            if cat:
                return cat
    for regex, cat in KEY_RULE_RE:
        if regex.match(key):
            return cat
    if STRUCTURE_QUEST_RE.search(key):
        return "quests"
    if STRUCTURE_STORY_RE.search(key):
        return "story"
    if DIALOGUE_RE.search(key):
        return "dialogue"
    for stem in stems:
        cat = _stem_category(stem)
        if cat:
            return cat
    for regex, cat in PREFIX_RULE_RE:
        if regex.match(key):
            return cat
    if FALLBACK_DIALOGUE_RE.match(key):
        return "other"
    return "other"
