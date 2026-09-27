# 人工核对条目 / Curated entries

本目录保存少量**无法通过 TextMap Key 自动导出、但已在客户端文本中逐字验证**的条目。
这些条目单独存放，以保证 `hsr-glossary/<lang>/` 下的正式术语全部可由 TextMap Key 复现。

## 文件

- `curated_terms.csv` — 三列 `source,target,tgt_lng`
- `_curated_counts.json` — 每个语言取值的验证结果

## 当前内容

### 开拓者 / Trailblazer（主角）

客户端把主角名称存放为 `{NICKNAME}` 变量（玩家自定义名字），因此在 13 份 TextMap 中
**没有可直接导出的主角名称 Key**，`AvatarConfig` 中 `8001`–`8008`（星/穹 × 各命途形态）
的 `AvatarName` 全部解析为 `{NICKNAME}`，按规则被过滤，不会进入正式术语库。

为了保留主角这一专有概念，本目录收录主角在各语言的正式称呼：

| `tgt_lng` | 客户端写法 |
| --- | --- |
| zh-CN | 开拓者 |
| zh-TW | 開拓者 |
| en-US | Trailblazer |
| ja-JP | 開拓者 |
| ko-KR | 개척자 |
| fr-FR | Pionnier |
| de-DE | Trailblazer |
| es-ES | Trazacaminos |
| ru-RU | Первооткрыватель |
| pt-PT | Desbravador |
| id-ID | Trailblazer |
| th-TH | ผู้บุกเบิก |
| vi-VN | Nhà Khai Phá |

其中每一种写法都已在对应语言的客户端 TextMap 中检索到
（`build_hsr_curated.py` 会逐个验证，验证失败会在生成时给出警告）。

## 关于 Stelle / Caelus

`Stelle`（星）与 `Caelus`（穹）是**同一名主角**（开拓者）的两个默认名字/性别形象，
不是两个不同角色，也不是独立命途形态：

- 客户端内主角名称使用 `{NICKNAME}` 变量，`Stelle`/`Caelus` 不作为 TextMap 文本键存在，
  因此**没有写入正式术语库**，避免把非客户端文本伪装成官方术语。
- 主角的不同命途（毁灭、存护、同谐、记忆等）在客户端中以 `8001`–`8008` 的独立 Avatar ID
  区分，属于「同一角色的不同战斗形态」，本库按其 ID 分开处理，不合并为无关人物。

重新生成：

```bash
python ../tools/build_hsr_curated.py
```
