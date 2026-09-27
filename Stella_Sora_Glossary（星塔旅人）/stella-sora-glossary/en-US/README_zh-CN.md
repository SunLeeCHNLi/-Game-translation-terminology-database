# 《星塔旅人》术语库 — English（`en-US`）

[← 返回游戏总说明](../README.md)

本目录是**以 `en-US`（English）为目标语言**的术语库：每一条都是「其他语言写法 → English」的对照，共 **12288** 条词条、**46032** 行对照，`tgt_lng` 列固定为 `en-US`，`source` 列收录 `zh-CN` / `zh-TW` / `ja-JP` / `ko-KR` 四种语言里同一词条的写法。需要每一条目五语并排的完整视图，请见 `00_master/README.md` 与 `../multilingual/00_master/`。

## 文件

- `NN_xxx/NN_xxx_glossary.csv` — `source,target,tgt_lng` 三列，可直接导入 CAT / 术语管理工具
- `NN_xxx/NN_xxx_terms.csv` — 本语言词条清单（`id,term,src_table`），适合校对与回查
- `00_master/all_glossary.csv` — 全部 15 个分类的对照行合并总表（`category,source,target,tgt_lng`）
- `00_master/all_terms.csv` — 本语言全部词条清单（`category,category_label,id,term,src_table`）
- `00_master/index.csv` — 分类索引与条数（`category,label,term_count,glossary_file,terms_file,target_language`）
- `00_master/README.md` — 本语言库的既有详细说明

`NN_xxx/` 是 15 个分类目录，每个目录下只有上面两个文件。`terms.csv` 的一条数据行对应一条词条，`glossary.csv` 的每一行是一条 `source → target` 对照。

## 分类与条数

数字取自 `00_master/index.csv`，并与 15 个分类 CSV、`00_master/all_terms.csv`、`00_master/all_glossary.csv` 的实际数据行数逐项核对一致。

| 分类 | 主题 | 条数 | 对照行 |
| --- | --- | ---: | ---: |
| `01_character` | 角色名称 | 287 | 973 |
| `02_skill` | 技能名称 | 628 | 2279 |
| `03_potential` | 潜能名称 | 1457 | 5553 |
| `04_disc` | 唱片 / Disc | 234 | 896 |
| `05_item` | 道具 | 558 | 2172 |
| `06_equipment` | 装备 | 15 | 58 |
| `07_enemy` | 敌人 | 399 | 1547 |
| `08_stage` | 关卡 | 1019 | 3856 |
| `09_event` | 活动 | 581 | 2231 |
| `10_system` | 系统术语 | 1055 | 4108 |
| `11_ui` | UI术语 | 4244 | 15529 |
| `12_story` | 剧情专有名词 | 527 | 2024 |
| `13_faction` | 阵营 | 21 | 78 |
| `14_location` | 地点 | 27 | 98 |
| `15_terminology` | 游戏机制术语 | 1236 | 4630 |
| **合计** | | **12288** | **46032** |

## 说明

- **译文来源与对齐方式**：译文全部取自游戏官方多语言文本库 `StellaSoraData-main`（官方 CN / EN / JP / KR / TW 五区客户端文本），各语言按同一文本键对齐，属于**官方本地化**而非二次翻译；每条词条会把其余四种语言的写法展开为对照行，因此本目录也可反向当作「English → 其他语言」查询。
- **语言标签**：本库出现的五种标签为 `zh-CN` 简体中文、`zh-TW` 繁體中文、`en-US` English、`ja-JP` 日本語、`ko-KR` 한국어；本目录的 `tgt_lng` 一律为 `en-US`。
- **编码**：所有 CSV 为 UTF-8 with BOM、CRLF 换行，Excel 双击即可正确显示中日韩文字；本说明文件为 UTF-8（无 BOM）。
- **对照行为何少于「条数 × 4」**：拆分脚本会去掉与目标语言写法完全相同的 `source`，以及同一分类内已经出现过的 `source` → `target` 对照行（`06_equipment` 只有 15 条词条、58 行对照即由此而来）。
- **已知限制**：
  - 台词、剧情正文、道具描述等长篇内容不在术语库范围内；
  - `14_location` 中除 `DatingLandmark` 与 `StarTower` 外，其余地名由人工校订补入（来源标注为 `curated (aligned in-game text)`）；
  - `06_equipment` 仅 15 条：本作没有传统武器 / 防具表，装备位由「秘纹（Disc）」承担；
  - 本目录内有 826 个 `source` 对应多个 `target`，多来自同名不同物的短词（例如简中 `薇洛` 同时对应 `Suntide Willow` 与 `Willow`）；按 `source` 去重的工具只会保留其中一条，需要区分时请用 `terms.csv` 里的 `id` 与 `src_table` 回查上下文；
  - 本目录共 12288 条词条，比 `zh-CN` 少 4 条，差异全部落在 `11_ui`：官方 UI 文本里有个别条目在英文语区没有独立译文。
- **重新生成**：本目录由 `tools/split_by_language.py` 从 `multilingual/` 拆分得到，脚本使用写死的外部绝对路径（`E:\Download\BT\Codex_input\StellaSora_Glossary`），**不会读写本仓库**；详见游戏根目录 `README.md` 的「生成与复现」。

## 免责声明

本目录为个人整理与维护的**非官方**英文翻译术语资料库，仅用于个人学习、研究及辅助 AI 翻译软件（包括但不限于沉浸式翻译）的术语匹配。本库与《星塔旅人》及其开发商、发行商、代理商、版权方不存在任何从属、授权、合作、代理或官方代表关系；库中译名不代表官方立场，不保证始终准确、完整或与游戏当前版本一致，**不应被视为任何游戏的官方术语表或官方本地化文件**。游戏名称、角色名称、专有名词、商标等知识产权均归各自权利人所有。本库不主张对上述第三方知识产权的任何权利。使用本库及基于其产生的翻译结果所引发的一切责任由使用者自行承担。如权利人认为内容不当，欢迎通过 GitHub Issues / Pull Request 联系，维护者将核实后修改或删除。完整条款见仓库根目录 `README.md` / `README_EN.md` / `README_JP.md`。

---

**Game-translation-terminology-database 是一个独立的个人项目，与本游戏及其开发商、发行商、代理商、版权方不存在任何隶属、授权、合作或代理关系。**
