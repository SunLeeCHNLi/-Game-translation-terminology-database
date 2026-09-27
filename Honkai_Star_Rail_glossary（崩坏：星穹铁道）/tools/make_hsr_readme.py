#!/usr/bin/env python3
"""Write the game-level README files and the source record documents."""

from __future__ import annotations

import json
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_hsr_glossary import CATEGORIES, CATEGORY_LABELS, LANG_ORDER  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
GLOSSARY = ROOT / "hsr-glossary"


def load(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def main() -> int:
    stats = load(TOOLS / "_counts.json", {})
    validation = load(TOOLS / "_validation.json", {})
    history = load(GLOSSARY / "historical" / "_history_counts.json", {})
    curated = load(GLOSSARY / "curated" / "_curated_counts.json", {})

    grand = stats.get("grand_total", 0)
    concepts = stats.get("unique_concepts", 0)
    lang_lines = "".join(f"- `{lang}`\n" for lang in LANG_ORDER)
    cat_lines = "".join(
        f"- `{cat}.csv` — {CATEGORY_LABELS[cat][0]} / {CATEGORY_LABELS[cat][1]}\n" for cat in CATEGORIES
    )
    category_table = "".join(
        f"| `{cat}` | {CATEGORY_LABELS[cat][0]} | {CATEGORY_LABELS[cat][1]} | "
        f"{stats['concept_counts'][cat]:,} | {sum(stats['counts'][cat][lang] for lang in LANG_ORDER):,} |\n"
        for cat in CATEGORIES
    )

    zh = f"""# 《崩坏：星穹铁道》Honkai: Star Rail 翻译术语库 / Honkai: Star Rail Terminology Database / 崩壊：スターレイル 用語集

## [English](README_EN.md) ｜ [日本語](README_JP.md)

本目录收录《崩坏：星穹铁道》（Honkai: Star Rail，HSR）游戏客户端本地化文本中的角色、命途、属性、
技能、行迹、星魂、光锥、遗器、道具、材料、敌人、地点、阵营、任务、关卡、活动、成就、模拟宇宙、
忘却之庭、剧情专有名词、世界观术语、书籍、对话说话者、系统、UI 等专有名词与固定文本。

- 总记录数：**{grand:,}**（`source,target,tgt_lng` 三列）
- 去重术语键：**{concepts:,}**
- 目标语言：**{len(LANG_ORDER)}**（zh-CN、zh-TW、en-US、ja-JP、ko-KR、fr-FR、de-DE、es-ES、ru-RU、pt-PT、id-ID、th-TH、vi-VN）
- 分类：**{len(CATEGORIES)}**
- 数据版本：`{stats.get('game_version', '')}`
- 全部译名均来自游戏客户端本地化文本，**没有机器翻译，也没有人工猜译**

## 目录结构

```text
Honkai_Star_Rail_glossary（崩坏：星穹铁道）/
├─ README.md / README_EN.md / README_JP.md   本说明（三语）
├─ hsr-glossary/                             正式术语库
│  ├─ README.md                             子库说明
│  ├─ zh-CN/ zh-TW/ en-US/ ja-JP/ ko-KR/     13 个目标语言目录
│  ├─ fr-FR/ de-DE/ es-ES/ ru-RU/ pt-PT/
│  ├─ id-ID/ th-TH/ vi-VN/
│  │  └─ 01_character.csv … 26_other.csv     每语言 {len(CATEGORIES)} 个分类文件 + README
│  ├─ historical/                            旧版本（2.3.0 / 4.0）译名变化
│  └─ curated/                               少量人工核对条目（开拓者/主角等）
├─ Sources/                                  数据来源记录
├─ Metadata/                                 统计与校验结果
└─ tools/                                    生成与校验脚本
```

每个语言目录都是**扁平结构**：{len(CATEGORIES)} 个分类 CSV 直接放在语言目录下。

## 文件格式

所有正式术语文件严格只有三列，UTF-8（含 BOM）、CRLF 换行、RFC 4180 转义：

```text
source	target	tgt_lng
Honkai: Star Rail	崩坏：星穹铁道	zh-CN
崩壊：スターレイル	崩坏：星穹铁道	zh-CN
```

- `source`：同一文本键在**其它语言**的官方本地化文本（可匹配原文）
- `target`：当前目录语言的官方本地化文本（译名）
- `tgt_lng`：当前目录语言代码，与目录名一致

- 分隔符与仓库其它游戏保持一致（逗号分隔的 `.csv`）；如需制表符版本，可运行
  `python tools/build_hsr_glossary.py --format tsv` 生成列结构完全相同的 `.tsv` 文件。

`source` 与 `target` 通过**同一 TextMap Hash / 实体 ID** 对齐，不使用字符串相似度猜测。
因此同一个 `target` 会以多行出现（每种可用原文各一行），可以直接用于沉浸式翻译、CAT 工具、
LLM  translators 的术语表导入。

## 分类

| 文件 | 中文名 | English | 独立术语键 | 全语言记录数 |
| --- | --- | --- | ---: | ---: |
{category_table}
## 数据来源与优先级

按官方优先、可验证优先的原则，本轮使用的数据源如下（完整记录见 [`Sources/README.md`](Sources/README.md)）：

- 主数据：`DimbreathBot/TurnBasedGameData` — 客户端 TextMap × 13 语言 + ExcelOutput，版本 4.5.0（commit `4ce30f69b`）
- 结构化交叉验证：`Mar-7th/StarRailRes` — 4.5.0（commit `d226bef`），命途/属性/遗器词条/模拟宇宙等按实体 ID 交叉核对
- 历史译名比对：`VizualAbstract/StarRailStaticAPI`（2.3.0）、`nathacks/HSR-Mapping-DATA`（4.0）
- 剧情与对话辅助核对：`mrzjy/StarrailDialog`、`M1k0t0/StarRail_Dialogue_Browser`
- 其它参考（未直接生成条目）：`iuyangyuc/homdgcat`、`kel-z/HSR-Data`、`simon300000/starrail-voice`

官方站点（<https://sr.mihoyo.com/>、<https://hsr.hoyoverse.com/>）用于核对语言支持范围与官方写法。

优先级：**当前客户端本地化 > 官方网站/公告 > 原始 TextMap > StarRailRes / HSR-Mapping-DATA >
结构化数据库 > Wiki > 其它社区资料**。

## TextMap 处理方式

1. 从 `ExcelOutput` 读取实体（角色、技能、行迹、星魂、光锥、遗器、道具、敌人、地点、任务、关卡、成就……）；
   名称字段是 `{{"Hash": …}}` 或字符串键（如 `SkillPointName_1001101`），后者按 **xxHash64** 计算 Hash。
2. 用同一 Hash 到 13 份 TextMap 中取值，形成「同一键 × 13 语言」的对齐表。
3. 过滤 `{{NICKNAME}}`、`{{RUBY_B#…}}`、`#1[i]` 等开发变量、HTML 标签、`N/A`、纯数字、占位符。
4. 同一语言内按 `(source,target,tgt_lng)` 去重，并保留同一 source 的多种译法（多译名）而不是强行合并。
5. 目标语言缺失文本时**不生成记录**，绝不用其它语言或机器翻译补全。

## 质量检查（两轮）

第一轮（结构，`tools/validate_hsr_glossary.py`，覆盖全部 {validation.get('files', 0):,} 个 CSV、{validation.get('rows', grand):,} 行）：

| 检查项 | 结果 |
| --- | ---: |
| 空 source / 空 target | {validation.get('issues', {}).get('empty_source', 0)} / {validation.get('issues', {}).get('empty_target', 0)} |
| 语言代码错误 | {validation.get('issues', {}).get('bad_language', 0)} |
| 重复记录 | {validation.get('issues', {}).get('duplicate_row', 0)} |
| HTML 标签 | {validation.get('issues', {}).get('html_tag', 0)} |
| 开发变量 | {validation.get('issues', {}).get('dev_variable', 0)} |
| Hash / 内部 ID | {validation.get('issues', {}).get('hash_like', 0)} / {validation.get('issues', {}).get('internal_id', 0)} |
| N/A 等占位符 | {validation.get('issues', {}).get('na_value', 0)} |
| 目标文本未出现在客户端文本中 | {validation.get('issues', {}).get('not_in_client_data', 0)} |
| 机器翻译记录 | {validation.get('issues', {}).get('machine_translation', 0)} |

第二轮（抽样核对，`tools/spotcheck_hsr_glossary.py`）：对角色、命途、属性、技能、行迹、星魂、光锥、
遗器、敌人、地点、阵营、任务、活动、模拟宇宙、忘却之庭、世界观、系统、UI、剧情等分类逐类抽样，
并用 StarRailRes 独立索引交叉比对（命中情况见 [`Metadata/statistics.md`](Metadata/statistics.md)）。

## 统计

完整统计（总术语数量、各语言数量、各分类数量、已确认/未确认数量、历史词条数量、多译名词条数量）见
[`Metadata/statistics.md`](Metadata/statistics.md)。

- 历史词条：{history.get('rows', 0):,}（`hsr-glossary/historical/`）
- 人工核对条目：{curated.get('rows', 0):,}（`hsr-glossary/curated/`）
- 多译名冲突组：{stats.get('conflicts', 0):,}（全部保留，不自动择优）

## 重新生成

```bash
python tools/build_hsr_glossary.py     # 生成 13 语言 × {len(CATEGORIES)} 分类 CSV
python tools/build_hsr_history.py      # 生成历史译名变化
python tools/build_hsr_curated.py      # 生成人工核对条目
python tools/validate_hsr_glossary.py  # 第一轮 + 第二轮校验
python tools/make_hsr_docs.py          # 生成本说明与统计文档
python tools/spotcheck_hsr_glossary.py # 人工抽样核对
```

脚本默认读取 `E:\\Download\\BT\\Codex_input` 下的上游仓库（不随本仓库分发）。

## 使用建议

- 沉浸式翻译 / 术语表工具：直接导入目标语言目录下的 CSV（`source,target,tgt_lng`）。
- 只需要专有名词时，可按分类挑选，例如 `01_character.csv`、`02_path.csv`、`07_light_cone.csv`。
- 需要完整剧情/对话文本时，请使用上游 `TurnBasedGameData` 原始数据，本仓库不复制原始游戏数据。

## 限制与免责声明

- 上游为社区提取的客户端数据，**不等同于发行商官方发布的术语表**；本项目与米哈游/HoYoverse 无任何隶属关系。
- 游戏文本随版本更新可能变化；本库以 4.5.0 客户端为准，旧版本差异单独保存在 `historical/`。
- `pt-PT` 使用游戏客户端「Português」文本，语言标签按本项目统一规范书写。
- 繁体中文上游标识为 `CHT`，本库统一写作 `zh-TW`；葡萄牙语上游标识为 `PT`，本库统一写作 `pt-PT`。
- 缺少某语言文本时不会生成记录，也不会用机器翻译补全；无法确认的内容一律不写入。
- 游戏名称、角色名、专有名词及相关资产权利归原权利人所有，本项目为个人学习与研究用途。
"""

    en = f"""# Honkai: Star Rail Multilingual Terminology Database

## [简体中文](README.md) ｜ [日本語](README_JP.md)

Client-localized terminology for *Honkai: Star Rail* (HSR): characters, Paths, elements, skills,
traces, Eidolons, Light Cones, Relics, items, materials, enemies, locations, factions, quests,
stages, events, achievements, Simulated Universe, Forgotten Hall, story proper nouns, world lore,
books, dialogue speakers, system and UI text.

- Total rows: **{grand:,}** (`source,target,tgt_lng`)
- Unique concept keys: **{concepts:,}**
- Target languages: **{len(LANG_ORDER)}** — zh-CN, zh-TW, en-US, ja-JP, ko-KR, fr-FR, de-DE, es-ES, ru-RU, pt-PT, id-ID, th-TH, vi-VN
- Categories: **{len(CATEGORIES)}**
- Client data version: `{stats.get('game_version', '')}`
- Every target string comes from the official client localization — **no machine translation**

## Layout

```text
Honkai_Star_Rail_glossary（崩坏：星穹铁道）/
├─ README.md / README_EN.md / README_JP.md
├─ hsr-glossary/
│  ├─ zh-CN/ … vi-VN/      one folder per target language, {len(CATEGORIES)} category CSVs each
│  ├─ historical/          names that changed between client versions (2.3.0 / 4.0 vs 4.5.0)
│  └─ curated/             small manually reviewed block (Trailblazer and similar)
├─ Sources/                source records
├─ Metadata/               statistics and validation results
└─ tools/                  build and validation scripts
```

## File format

Three columns only, UTF-8 with BOM, CRLF, RFC 4180 escaping:

```text
source,target,tgt_lng
Honkai: Star Rail,崩坏：星穹铁道,zh-CN
崩壊：スターレイル,崩坏：星穹铁道,zh-CN
```

`source` is the same localization key in another language, `target` is the target language string.
Rows are aligned by **shared TextMap hash / entity id**, never by fuzzy string matching.

## Data sources

- Primary: `DimbreathBot/TurnBasedGameData` 4.5.0 (commit `4ce30f69b`) — client TextMap ×13 + ExcelOutput
- Structured cross-check: `Mar-7th/StarRailRes` 4.5.0 (commit `d226bef`)
- Historical comparison: `VizualAbstract/StarRailStaticAPI` 2.3.0, `nathacks/HSR-Mapping-DATA` 4.0
- Story/dialogue support: `mrzjy/StarrailDialog`, `M1k0t0/StarRail_Dialogue_Browser`
- Reviewed but not used for generation: `iuyangyuc/homdgcat`, `kel-z/HSR-Data`, `simon300000/starrail-voice`

See [`Sources/README.md`](Sources/README.md) for the full record.

## Validation

Round 1 (structure) covers all {validation.get('files', 0):,} CSV files and {validation.get('rows', grand):,} rows:
empty values, wrong language codes, duplicates, HTML tags, dev variables, hashes, internal ids, N/A,
and whether each target string exists in the client TextMap.

| Check | Result |
| --- | ---: |
| Empty source / target | {validation.get('issues', {}).get('empty_source', 0)} / {validation.get('issues', {}).get('empty_target', 0)} |
| Wrong language code | {validation.get('issues', {}).get('bad_language', 0)} |
| Duplicate rows | {validation.get('issues', {}).get('duplicate_row', 0)} |
| HTML tags | {validation.get('issues', {}).get('html_tag', 0)} |
| Dev variables | {validation.get('issues', {}).get('dev_variable', 0)} |
| Hash / internal id leak | {validation.get('issues', {}).get('hash_like', 0)} / {validation.get('issues', {}).get('internal_id', 0)} |
| N/A placeholders | {validation.get('issues', {}).get('na_value', 0)} |
| Target not found in client data | {validation.get('issues', {}).get('not_in_client_data', 0)} |
| Machine-translated rows | {validation.get('issues', {}).get('machine_translation', 0)} |

Round 2 samples every category and cross-checks against the independent StarRailRes index.

## Statistics

See [`Metadata/statistics.md`](Metadata/statistics.md): totals, per-language, per-category,
confirmed/unconfirmed, historical and multi-translation counts.

- Historical entries: {history.get('rows', 0):,}
- Curated entries: {curated.get('rows', 0):,}
- Multi-translation groups: {stats.get('conflicts', 0):,}

## Rebuild

```bash
python tools/build_hsr_glossary.py
python tools/build_hsr_history.py
python tools/build_hsr_curated.py
python tools/validate_hsr_glossary.py
python tools/make_hsr_docs.py
```

## Disclaimer

Unofficial personal project for study, research and translation assistance. It is not affiliated with,
endorsed by, or connected to miHoYo / HoYoverse. Game names, characters and related assets belong to
their respective rights holders.
"""

    jp = f"""# 『崩壊：スターレイル』多言語翻訳用語集

## [简体中文](README.md) ｜ [English](README_EN.md)

『崩壊：スターレイル』（Honkai: Star Rail）のクライアント日本語版・他言語版テキストから、
キャラクター、運命、属性、スキル、痕跡、星魂、光円錐、遺物、アイテム、素材、敵、地名、勢力、
任務、ステージ、イベント、実績、模擬宇宙、忘却の庭、世界観用語、書籍、会話話者名、システム、
UI などの固有名詞を対訳化した用語集です。

- 総レコード数：**{grand:,}**（`source,target,tgt_lng` の3列）
- 用語キー数：**{concepts:,}**
- 対象言語：**{len(LANG_ORDER)}**（zh-CN、zh-TW、en-US、ja-JP、ko-KR、fr-FR、de-DE、es-ES、ru-RU、pt-PT、id-ID、th-TH、vi-VN）
- 分類：**{len(CATEGORIES)}**
- クライアントデータ：`{stats.get('game_version', '')}`
- **機械翻訳は一切使用していません**（すべてクライアント公式テキスト）

## ファイル形式

```text
source,target,tgt_lng
Honkai: Star Rail,崩坏：星穹铁道,zh-CN
崩壊：スターレイル,崩坏：星穹铁道,zh-CN
```

`source` は同じテキストキーの他言語テキスト、`target` は対象言語のテキストです。
対応付けは **TextMap ハッシュ / エンティティID** で行い、文字列の類似度では推測しません。

## データ出典

- 主データ：`DimbreathBot/TurnBasedGameData` 4.5.0（commit `4ce30f69b`）— TextMap ×13 + ExcelOutput
- 構造化クロスチェック：`Mar-7th/StarRailRes` 4.5.0（commit `d226bef`）
- 旧版比較：`VizualAbstract/StarRailStaticAPI` 2.3.0、`nathacks/HSR-Mapping-DATA` 4.0

詳細は [`Sources/README.md`](Sources/README.md) を参照してください。

## 検証

全 {validation.get('files', 0):,} ファイル・{validation.get('rows', grand):,} 行を対象に、空値、言語コード、
重複、HTML タグ、開発用変数、ハッシュ、内部ID、N/A、および原文がクライアントテキストに存在するかを検査しています。

| 検査項目 | 結果 |
| --- | ---: |
| 空の source / target | {validation.get('issues', {}).get('empty_source', 0)} / {validation.get('issues', {}).get('empty_target', 0)} |
| 言語コードの誤り | {validation.get('issues', {}).get('bad_language', 0)} |
| 重複レコード | {validation.get('issues', {}).get('duplicate_row', 0)} |
| HTML タグ | {validation.get('issues', {}).get('html_tag', 0)} |
| 開発用変数 | {validation.get('issues', {}).get('dev_variable', 0)} |
| ハッシュ / 内部ID | {validation.get('issues', {}).get('hash_like', 0)} / {validation.get('issues', {}).get('internal_id', 0)} |
| N/A 等 | {validation.get('issues', {}).get('na_value', 0)} |
| クライアントテキストに存在しない訳文 | {validation.get('issues', {}).get('not_in_client_data', 0)} |
| 機械翻訳 | {validation.get('issues', {}).get('machine_translation', 0)} |

## 統計

[`Metadata/statistics.md`](Metadata/statistics.md) を参照（総数、言語別、分類別、確認済み/未確認、
旧版用語数、複数訳語数）。旧版の訳語変更は `hsr-glossary/historical/` に、手動確認した項目は
`hsr-glossary/curated/` に保存しています。

## 再生成

```bash
python tools/build_hsr_glossary.py
python tools/build_hsr_history.py
python tools/build_hsr_curated.py
python tools/validate_hsr_glossary.py
python tools/make_hsr_docs.py
```

## 免責

本プロジェクトは個人による非公式の用語資料であり、miHoYo / HoYoverse とは一切関係ありません。
ゲーム内の名称・キャラクター・関連アセットの権利は各権利者に帰属します。
"""

    (ROOT / "README.md").write_text(zh, encoding="utf-8")
    (ROOT / "README_EN.md").write_text(en, encoding="utf-8")
    (ROOT / "README_JP.md").write_text(jp, encoding="utf-8")
    print("wrote game README trio")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
