# NTE Glossary - 简体中文 (`zh-CN`)

This folder contains **55,559** aligned terminology rows in **21** CSV files.

Every file has exactly three columns: `source`, `target`, `tgt_lng`. The `tgt_lng` value is always `zh-CN`. Rows are generated only when the target game localization text exists for the same upstream text key.

Rebuild from the game directory with `python tools/build_nte_glossary.py`.
