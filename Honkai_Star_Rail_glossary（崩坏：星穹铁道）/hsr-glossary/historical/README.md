# 历史译名 / Historical names

本目录保存**旧版本客户端**与当前版本（4.5.0）之间发生的译名变化，
用于版本回溯与老文本匹配。当前版本译名始终是 `hsr-glossary/<lang>/` 下的正式条目。

## 文件

- `historical_names.csv` — 三列 `source,target,tgt_lng`
  - `source`：旧版本客户端中的写法（2.3.0 或 4.0）
  - `target`：当前 4.5.0 客户端中的写法
  - `tgt_lng`：该写法的语言
- `_history_counts.json` — 各来源、各语言检出的差异数量

## 比对基线

| 基线 | 版本 | Commit |
| --- | --- | --- |
| VizualAbstract/StarRailStaticAPI | 2.3.0 | `e039e51` |
| nathacks/HSR-Mapping-DATA | 4.0 | `245f286` |
| 当前版本 | Mar-7th/StarRailRes 4.5.0 | `d226bef` |

比对对象（按实体 ID 对齐）：`characters`、`light_cones`、`relic_sets`、`relics`、
`simulated_curios`、`simulated_blessings`、`simulated_events`、`paths`、`elements`、`achievements`。

## 处理规则

1. 只比较**同一实体 ID** 的名称，不做字符串相似度匹配。
2. 比较前会去除 `<i>` 等 HTML 标签、`{RUBY_B#…}` 注音标记与首尾引号，
   因此「单纯标记变化」不会被误报为译名变化。
3. 大小写、空格、标点等真实差异会保留（例如 `Deja Vu` → `Déjà Vu`）。
4. 差异全部保留，不自动判断哪一个更「正确」；正式条目始终以当前版本为准。

重新生成：

```bash
python ../tools/build_hsr_history.py
```
