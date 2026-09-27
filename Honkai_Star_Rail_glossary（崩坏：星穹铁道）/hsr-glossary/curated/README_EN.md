# Curated entries / 人工核对条目

## [简体中文](README.md) [日本語](README_JP.md)

This directory holds a small number of entries that **cannot be exported automatically from
TextMap keys but have been verified character by character in the client text**. They are kept
apart so that every regular entry under `hsr-glossary/<lang>/` can be reproduced from TextMap keys.

## Files

- `curated_terms.csv` — three columns `source,target,tgt_lng`
- `_curated_counts.json` — verification result for each language value

## Current contents

### Trailblazer / 开拓者 (protagonist)

The client stores the protagonist name in a `{NICKNAME}` variable (a player-chosen name), so across
the 13 TextMaps there is **no directly exportable key for the protagonist name**; in `AvatarConfig`
the `AvatarName` of `8001`–`8008` (Stelle/Caelus × each Path form) all resolve to `{NICKNAME}`,
which is filtered out by the rules and never enters the regular termbase.

To preserve the protagonist as a proper concept, this directory records the official wording for the
protagonist in every language:

| `tgt_lng` | Client wording |
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

Each wording has been located in the client TextMap for the corresponding language
(`build_hsr_curated.py` verifies them one by one and warns at build time if verification fails).

## About Stelle / Caelus

`Stelle` and `Caelus` are **two default names / gender presentations of the same protagonist**
(Trailblazer), not two different characters and not separate Path forms:

- The client uses the `{NICKNAME}` variable for the protagonist name, and `Stelle`/`Caelus` do not
  exist as TextMap text keys, so they are **not written into the regular termbase**, to avoid
  passing non-client text off as official terminology.
- The protagonist's different Paths (Destruction, Preservation, Harmony, Remembrance, ...) are
  distinguished in the client by the separate Avatar IDs `8001`–`8008`; they count as "different
  combat forms of the same character", and this database keeps them separate by ID rather than
  merging them into unrelated characters.

Regenerate:

```bash
python ../tools/build_hsr_curated.py
```