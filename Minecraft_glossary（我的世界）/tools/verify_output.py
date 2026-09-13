import csv, os, json, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
# game root = parent of this tools/ folder; no absolute path baked in
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LANGS={"zh-CN","zh-TW","en-US","ja-JP","ko-KR","fr-FR","de-DE","es-ES","ru-RU","pt-BR","it-IT","tr-TR","th-TH","vi-VN"}
# per-glossary metadata now lives in tools/, next to this script
COUNTS={ "minecraft-glossary": os.path.join(HERE, "glossary_counts.json"),
         "minecraft-glossary-supplement": os.path.join(HERE, "supplement_counts.json") }
problems=[]; total=0; counts=collections.defaultdict(collections.Counter)
for base in ("minecraft-glossary","minecraft-glossary-supplement"):
    for dirpath,_,fs in os.walk(os.path.join(ROOT,base)):
        for f in fs:
            if not f.endswith(".csv"): continue
            p=os.path.join(dirpath,f)
            lang=next(x for x in os.path.relpath(p,ROOT).split(os.sep) if x in LANGS)
            cat=f[:-4]
            with open(p,encoding="utf-8-sig",newline="") as fh:
                r=csv.reader(fh)
                if next(r)!=["source","target","tgt_lng"]: problems.append((base,lang,cat,"header"))
                n=0; seen=set()
                for row in r:
                    if len(row)!=3 or row[2]!=lang or row[0]==row[1] or not row[0] or not row[1]:
                        problems.append((base,lang,cat,row)); continue
                    if (row[0],row[1]) in seen: problems.append((base,lang,cat,"dup",row))
                    seen.add((row[0],row[1])); n+=1
                counts[(base,lang)][cat]=n; total+=n
    d=json.load(open(COUNTS[base],encoding="utf-8"))
    for lang,cats in d["rows"].items():
        for c,v in cats.items():
            if counts[(base,lang)][c]!=v:
                problems.append((base,lang,c,"count",v,counts[(base,lang)][c]))
print(f"total data rows = {total:,}   problems = {len(problems)}")
for p in problems[:10]: print("   ",p)
print("\nsupplement per-language rows:", {l:sum(v.values()) for (b,l),v in counts.items() if b.endswith("supplement")})
