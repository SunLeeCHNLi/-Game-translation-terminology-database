const fs=require('fs'),path=require('path');
// External generation pipeline (do not relocate): SUP is the working output directory
// written by build_supplement.mjs (which also reads ../genshin-glossary from there).
const SUP='E:/Download/BT/Codex_input/genshin-glossary-supplement';
// Build metadata produced by build_supplement.mjs. The copy kept in this repository
// lives at tools/supplement_counts.json (moved out of genshin-glossary-supplement/
// during the repository tools/ consolidation); keep the two in sync.
const counts=JSON.parse(fs.readFileSync(path.join(SUP,'_counts.json'),'utf8'));
const byCode={}; for(const l of counts.languages) byCode[l.code]=l;
const langNames={ 'zh-CN':'简体中文','zh-TW':'繁體中文','en-US':'English','ja-JP':'日本語' };
const cats=Object.keys(byCode['zh-CN'].categories);
const mainCats=cats.filter(c=>!c.startsWith('extra/'));
const extraCats=cats.filter(c=>c.startsWith('extra/'));
const md=[];
md.push('# 原神（Genshin Impact）多语言术语库 - 补充词库');
md.push('');
md.push('本目录是 `genshin-glossary/` 的**补充集**，用于补齐主词库未收录的词条（尤其是 NPC、地名、敌人、任务等）。');
md.push('');
md.push('## 数据来源');
md.push('');
md.push('- [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata)（覆盖 en / ja / zh-CN / zh-TW 四种语言）');
md.push('');
md.push('## 与主词库的关系');
md.push('');
md.push('- 只包含**主词库中没有的** `source/target/tgt_lng` 组合，因此可与主词库直接**叠合使用**，不会产生重复条目。');
md.push('- 仅覆盖 4 种目标语言：`zh-CN`、`zh-TW`、`en-US`、`ja-JP`。');
md.push('- 由于来源不同，同一词条的英/日/中写法可能与主词库存在细微差异（例如用词、标点）。');
md.push('');
md.push('## 目录结构');
md.push('');
md.push('```');
md.push('genshin-glossary-supplement/');
md.push('├── zh-CN/');
md.push('│   ├── characters.csv        # 与主词库同名的主类目');
md.push('│   ├── _variants.csv         # 别名/俗称/常见误写，作为额外 source 补充');
md.push('│   └── extra/                # 主类目之外、原神翻译常用的额外类目');
md.push('│       ├── quests.csv');
md.push('│       └── ...');
md.push('├── zh-TW/  en-US/  ja-JP/');
md.push('└── （生成元数据已移至同级 ../tools/supplement_counts.json）');
md.push('```');
md.push('');
md.push('> 本目录由同级 `tools/build_supplement.mjs` 生成，构建元数据（各语言、各类目的行数统计）');
md.push('> 存放于同级 `tools/supplement_counts.json`，不在本目录内。');
md.push('');
md.push('## 文件格式');
md.push('');
md.push('与主词库完全一致（UTF-8 含 BOM、CRLF、RFC 4180 转义）：');
md.push('');
md.push('| source | target | tgt_lng |');
md.push('| --- | --- | --- |');
md.push('| Blackmarrow Lantern | 鸟髄孑灯 | zh-CN |');
md.push('| 鳥髄の狐灯 | 鸟髄孑灯 | zh-CN |');
md.push('');
md.push('## 类目');
md.push('');
md.push('### 对应主词库的主类目');
md.push('');
md.push('| 类目 | 词条来源 |');
md.push('| --- | --- |');
const srcOf={
 'artifacts':'artifacts','characters':'characters-*（蒙德/璃月/稻妻/须弥/枫丹/纳塔/挪德卡莱/至冬/坎瑞亚/愚人众等）',
 'domains':'domains','enemies':'enemies','foods':'foods','geographies':'locations',
 'materials':'items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials',
 'weapons':'weapons','animals':'living-beings'};
for(const c of mainCats) md.push(`| ${c} | ${srcOf[c]||c} |`);
md.push('');
md.push('### 额外类目（`extra/`）');
md.push('');
md.push('| 类目 | 说明 |');
md.push('| --- | --- |');
const extraZh={'extra/quests':'任务名称（魔神/世界/传说/每日/部族等）','extra/organizations':'组织与势力','extra/facilities':'设施与建筑','extra/objects':'场景物件','extra/story':'剧情与章节','extra/events':'活动名称','extra/sereniteapot':'尘歌壶','extra/system':'系统与玩法术语','extra/dialogue':'对白用语','extra/archives':'档案资料'};
for(const c of extraCats) md.push(`| ${c} | ${extraZh[c]||''} |`);
md.push('');
md.push('## 行数统计');
md.push('');
md.push('| 语言 | 主类目文件 | 数据行数 | 别名行数 |');
md.push('| --- | --- | --- | --- |');
for(const c of Object.keys(langNames)){ const l=byCode[c]; md.push(`| \`${c}\` | ${Object.keys(l.categories).length} | ${l.rows.toLocaleString()} | ${l.variantRows} |`); }
md.push('');
md.push('> 行数指叠加前的新增行数；实际使用时与主词库合并即可。');
md.push('> 「主类目文件」= 9 个与主词库同名的主类目 + `extra/` 下的 10 个额外类目，合计 19 个 CSV，另有 1 个 `_variants.csv`。');
md.push('');
md.push('## 生成说明');
md.push('');
md.push('本目录由同级 `tools/build_supplement.mjs` 生成，它读取两个输入：`xicri/genshin-langdata` 的数据集，');
md.push('以及**主词库 `genshin-glossary/` 已生成的全部 CSV**（用于剔除重复行）：');
md.push('');
md.push('```bash');
md.push('node tools/build_main_glossary.js   # 先生成主词库');
md.push('node tools/build_supplement.mjs     # 再生成补充词库（依赖上一步的产物）');
md.push('```');
md.push('');
md.push('该脚本会在输出目录写出 4 个语言文件夹及统计元数据 `supplement_counts.json`；');
md.push('仓库内保存的那一份统计元数据位于 `tools/supplement_counts.json`。本 README 的表格由 `tools/readme_sup.js` 生成。');
md.push('');
fs.writeFileSync(path.join(SUP,'README.md'), md.join('\n'), 'utf8');
console.log('supplement README written,', md.length, 'lines');
