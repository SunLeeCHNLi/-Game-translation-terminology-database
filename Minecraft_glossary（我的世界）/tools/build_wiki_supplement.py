# -*- coding: utf-8 -*-
"""
Build the Minecraft Wiki 译名标准化 supplement glossary.

Source : https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化  (rendered tables,
         fetched with action=parse&variant=zh-cn and &variant=zh-tw)
Input  : SRC_DIR/wiki_std_cn.json, SRC_DIR/wiki_std_tw.json
Output : OUT_DIR/zh-CN/<category>.csv, OUT_DIR/zh-TW/<category>.csv

The wiki lists standardised (Crowdin-aligned) names per category; the two fetches
give the 大陆简体 and 台灣正體 column of every row.  Only Chinese is covered by
this source, so the supplement only contains zh-CN / zh-TW folders.
"""
import json, os, re, csv, html, collections

SRC_DIR = r"E:\Download\BT\Codex_input"
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "minecraft-glossary-supplement")

# section headings appear in a fixed order; the traditional-Chinese variant uses
# different wording (生態域 / 附魔 / 遊戲難易度和模式 ...) so map by position
SECTION_ORDER = [
    "toc", "overview", "blocks", "items", "entities", "environment", "biomes",
    "effects", "enchantments", "advancements", "game-modes", "game-content",
    "game-versions", "technical", "other",
]

TAG = re.compile(r"<[^>]+>")
FOOTNOTE = re.compile(r"\[\s*(?:\d+|注\s*\d*|n\s*\d+)\s*\]")


UNTRANSLATED = {"-", "\u2212", "\u2014", "\u2013", "\u4e0d\u7ffb\u8bd1", "\u4e0d\u7ffb\u8b6f", ""}


def clean(cell, br=" / "):
    cell = re.sub(r"<sup.*?</sup>", "", cell, flags=re.S)     # footnote markers
    cell = re.sub(r"<style.*?</style>", "", cell, flags=re.S)
    cell = re.sub(r"<br\s*/?>", br, cell, flags=re.I)
    cell = TAG.sub("", cell)
    cell = html.unescape(cell)
    cell = FOOTNOTE.sub("", cell)
    return " ".join(cell.split()).strip()


def parse(path):
    """return [(section, english, translation), ...]"""
    text = json.load(open(path, encoding="utf-8"))["parse"]["text"]
    out, idx = [], -1
    for m in re.finditer(r"<h2[^>]*>(.*?)</h2>|<table.*?</table>", text, re.S):
        chunk = m.group(0)
        if chunk.startswith("<h2"):
            idx += 1
            continue
        section = SECTION_ORDER[idx] if 0 <= idx < len(SECTION_ORDER) else "other"
        rows = re.findall(r"<tr.*?</tr>", chunk, re.S)
        if not rows:
            continue
        # column layout differs per table (some tables have an icon column,
        # some have a trailing 备注 column) -> read it off the header row
        hcells = [clean(x, " ") for x in re.findall(r"<th[^>]*>(.*?)</th>", rows[0], re.S)]
        try:   # headers are 英文名稱/中文譯名 in the traditional variant
            i_en = next(i for i, h in enumerate(hcells) if h.startswith("英文"))
            i_tr = next(i for i, h in enumerate(hcells) if h.startswith("中文"))
        except StopIteration:
            i_en, i_tr = (1, 2) if len(hcells) >= 3 else (0, 1)
        for row in rows[1:]:
            cells = [clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
            if len(cells) <= max(i_en, i_tr):
                continue
            en = cells[i_en].split(" / ")[0].strip()   # "Disambig / Disambiguation"
            tr = cells[i_tr]
            if en and tr not in UNTRANSLATED:
                out.append((section, en, tr))
    return out


def write(folder, name, rows):
    d = os.path.join(OUT_DIR, folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name + ".csv"), "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, lineterminator="\r\n")
        w.writerow(["source", "target", "tgt_lng"])
        w.writerows(rows)


def main():
    cn = parse(os.path.join(SRC_DIR, "wiki_std_cn.json"))
    tw = parse(os.path.join(SRC_DIR, "wiki_std_tw.json"))
    pairs = collections.defaultdict(dict)          # section -> english -> {cn, tw}
    for section, en, tr in cn:
        pairs[section].setdefault(en, {})["zh-CN"] = tr
    for section, en, tr in tw:
        pairs[section].setdefault(en, {})["zh-TW"] = tr
    # merge duplicates listing the same English name twice (e.g. per variant tables)
    for section in pairs:
        for en in list(pairs[section]):
            e = en.strip()
            if e != en and e not in pairs[section]:
                pairs[section][e] = pairs[section].pop(en)

    counts = {}
    for target in ("zh-CN", "zh-TW"):
        counts[target] = {}
        for section, table in sorted(pairs.items()):
            rows = set()
            for en, tr in table.items():
                tgt = tr.get(target)
                if not tgt:
                    continue
                for other in ("en-US", "zh-CN", "zh-TW"):
                    if other == target:
                        continue
                    if other == "en-US":
                        src = en
                    else:
                        src = tr.get(other)
                    if not src or src == tgt:
                        continue
                    rows.add((src, tgt, target))
            rows = sorted(rows, key=lambda r: (r[0].lower(), r[0], r[1]))
            write(target, section, rows)
            counts[target][section] = len(rows)
        print(target, counts[target])

    payload = {
        "source": "https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化",
        "note": "此补充词库仅覆盖简体中文与繁体中文；行数 = 该语言文件夹内 CSV 数据行数",
        "categories": {s: {"entries": len(t)} for s, t in sorted(pairs.items())},
        "rows": counts,
    }
    with open(os.path.join(OUT_DIR, "_counts.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()



