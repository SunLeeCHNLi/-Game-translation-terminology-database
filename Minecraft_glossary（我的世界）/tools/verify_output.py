import csv, os, json, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT=r"C:\Users\admin\Documents\GitHub\-Game-translation-terminology-database\Minecraft_glossary（我的世界）"
LANGS={"zh-CN","zh-TW","en-US","ja-JP","ko-KR","fr-FR","de-DE","es-ES","ru-RU","pt-BR","it-IT","tr-TR","th-TH","vi-VN"}
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
    d=json.load(open(os.path.join(ROOT,base,"_counts.json"),encoding="utf-8"))
    for lang,cats in d["rows"].items():
        for c,v in cats.items():
            if counts[(base,lang)][c]!=v:
                problems.append((base,lang,c,"count",v,counts[(base,lang)][c]))
print(f"total data rows = {total:,}   problems = {len(problems)}")
for p in problems[:10]: print("   ",p)
print("\nsupplement per-language rows:", {l:sum(v.values()) for (b,l),v in counts.items() if b.endswith("supplement")})
