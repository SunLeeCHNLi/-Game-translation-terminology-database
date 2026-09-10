# -*- coding: utf-8 -*-
import io, json, os

S = json.load(io.open("glossary/_summary.json", encoding="utf-8"))
cats = S["categories"]
LANGS = ["zh-CN", "zh-TW", "en-US", "ja-JP", "ko-KR"]

SRC = {
 "01_干员名称": "character_table.json — 全部可获取干员（八大职业）",
 "02_干员异格": "character_table.json — 异格干员（char_1xxx 编号）",
 "03_职业与分支": "i18n/string_map.txt（八大职业）+ uniequip_table.subProfDict（职业分支）",
 "04_技能名称": "skill_table.json — 全部技能（含通用技能与干员技能）",
 "05_技能描述关键术语": "skill_table / character_table 天赋描述，按占位符对齐后全语料投票提取术语",
 "06_天赋": "character_table.talents[].name — 天赋名",
 "07_潜能": "character_table.potentialRanks[].description + 潜能提升信物名称",
 "08_模组": "uniequip_table.equipDict.uniEquipName + equipTypeInfos（模组类型）",
 "09_敌人": "enemy_handbook_table.enemyData — NORMAL / ELITE 级敌人",
 "10_BOSS": "enemy_handbook_table.enemyData — BOSS 级敌人",
 "11_关卡": "stage_table.stages[].name — 关卡名",
 "12_地区": "zone_table.zones（章节/地区）+ activity_table 活动区域名",
 "13_阵营": "handbook_team_table — 势力/阵营名",
 "14_活动": "activity_table.basicInfo + crisis_v2 赛季 + climb_tower 赛季 + 集成战略主题",
 "15_道具": "item_table.items — 非材料类道具（凭证、票券、补给、纪念品等）",
 "16_装备": "climb_tower_table 战术装备 + sandbox_table 生息演算装备 + 集成战略收藏品",
 "17_材料": "item_table.items — MATERIAL 类材料（已剔除信物）",
 "18_剧情专有名词": "story_review_table 剧情名 + handbook_info_table NPC 名与档案名",
 "19_UI与系统术语": "i18n/string_map.txt — 客户端全部界面文本",
 "20_游戏机制": "tip_table 战斗提示 + GUIDE 任务 + 基建房间 + 特性/模组描述术语",
}

def fmt(n):
    return "{:,}".format(n)

tot_terms = sum(v["records"] for v in cats.values())
tot_rows = sum(x["rows"] for v in cats.values() for x in v["by_lang"].values())

L = []
w = L.append
w("# 明日方舟 (Arknights) 多语言术语库")
w("")
w("按**目标语言**分文件夹、按**20 个分类**分文件的翻译术语库，覆盖简体中文、繁体中文、英文、日文、韩文。")
w("")
w("## 目录结构")
w("")
w("```")
w("glossary/")
w("├── zh-CN/                    # 目标语言 = 简体中文")
w("│   ├── 01_干员名称.csv")
w("│   ├── 02_干员异格.csv")
w("│   ├── ...")
w("│   ├── 20_游戏机制.csv")
w("│   └── _all.json             # 上述 20 个文件的合并版（JSON）")
w("├── zh-TW/   (同结构)")
w("├── en-US/   (同结构)")
w("├── ja-JP/   (同结构)")
w("├── ko-KR/   (同结构)")
w("└── _summary.json             # 各分类词条数与覆盖率统计")
w("```")
w("")
w("## 文件格式")
w("")
w("每个 CSV 均为三列，UTF-8 BOM 编码（Excel 可直接打开）：")
w("")
w("| source | target | tgt_lng |")
w("| ------ | ------ | ------- |")
w("| Enterprise | 企业 | zh-CN |")
w("| エンタープライズ | 企业 | zh-CN |")
w("")
w("- `target`：该文件所属目标语言的官方译名。")
w("- `tgt_lng`：目标语言标签，等于所在文件夹名。")
w("- `source`：同一词条在**其他 4 种语言**中的写法（因此同一词条会出现在多行中）。")
w("  例如 `zh-CN/01_干员名称.csv` 中「阿米娅」会分别以 `Amiya`(en-US)、`アーミヤ`(ja-JP)、")
w("  `阿米婭`(zh-TW)、`아미야`(ko-KR) 作为 source 出现 4 行。")
w("")
w("> 只想保留「英→中」这类单向词表时，按 `source` 所在语言筛选即可，例如只保留 source 为拉丁字母的行。")
w("")
w("## 分类与数据来源")
w("")
w("| 分类 | 词条数 | 五语齐全 | 数据来源 |")
w("| ---- | -----: | -------: | -------- |")
for c, v in cats.items():
    w("| {} | {} | {} | {} |".format(c, fmt(v["records"]), fmt(v["records_all5"]), SRC.get(c, "")))
w("")
w("合计 **{}** 个词条，导出 **{}** 行**（5 个语言文件夹 × 20 个分类）".format(fmt(tot_terms), fmt(tot_rows)))
w("")
w("## 各语言分布")
w("")
w("| 分类 | " + " | ".join(LANGS) + " |")
w("| ---- |" + " ----: |" * len(LANGS))
for c, v in cats.items():
    w("| {} | ".format(c) + " | ".join(fmt(v["by_lang"].get(l, {}).get("rows", 0)) for l in LANGS) + " |")
w("")
w("（表内为 CSV 行数；同一词条会因多语言 source 产生多行）")
w("")
w("## 数据来源与版本")
w("")
w("- 主数据：[ArknightsAssets/ArknightsGamedata](https://github.com/ArknightsAssets/ArknightsGamedata)")
w("  —— 各区服官方客户端解包表格，`cn` / `tw` / `en` / `jp` / `kr` 五区并存且表结构一致，是本词库的基础。")
w("- 交叉校验：[ArchyCillp/ArknightsTranslationContrast](https://github.com/ArchyCillp/ArknightsTranslationContrast)")
w("  —— 用于抽样核对干员/技能译名。")
w("- 结构参考：[flandia/ArknightsGameDataComposite](https://github.com/flandia/ArknightsGameDataComposite)")
w("  —— 仅 4 语（无繁中）且条目少于主数据，未作为数据源，仅用于比对。")
w("")
w("各服版本（`data_version.txt`）：")
w("")
w("- 简中 `rel77.0`（2026/08/31）")
w("- 英文 `51.4.0`")
w("- 繁中 `50.8.0`")
w("")
w("> 由于各区服进度不同，最新内容在日/英/韩/繁中可能尚未实装，这些词条不会出现在词库中")
w("> （生成时要求至少两种语言同时存在）。")
w("")
w("## 生成方法")
w("")
w("1. **按 ID 对齐**：所有表格以条目 ID（如 `char_002_amiya`、`skchr_amiya_2`）为键，")
w("   把 5 个区服的同一 ID 值配成一组，保证是同一个概念的官方译名。")
w("2. **名称类分类**直接取官方字段（干员名、技能名、关卡名、敌人名等）。")
w("3. **描述类分类**（技能描述关键术语、部分游戏机制）采用**占位符分段 + 全语料投票**：")
w("   游戏文本中的 `<@ba.vup>`、`{atk:0%}` 等标记在各语言完全一致，以标记切分文本即可得到")
w("   结构对齐的片段；再对同一中文片段统计各语言出现最多的写法，消除语序差异带来的错配。")
w("4. **清洗**：去除富文本标签、换行、成对引号与书名号，过滤纯数字/纯符号片段。")
w("")
w("## 已知限制")
w("")
w("- 描述类术语（05、20）由文本自动挖掘，少数条目仍是短语片段而非严格术语，建议按需人工复核。")
w("- 关卡、活动等词条大量同名的（如「标准实战环境」）会各自成行，未做跨条目合并。")
w("- 干员异格仅收录异格形态本身；基础干员见 `01_干员名称`。")
w("")
w("## 复现")
w("")
w("```")
w("python build_glossary.py     # 读取 _data/gamedata，输出 glossary/")
w("```")
w("")

io.open("glossary/README.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("README written:", len(L), "lines")
