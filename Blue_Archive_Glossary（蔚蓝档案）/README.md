## 使用方法

1. **单文件下载**：进入 `blue-archive-glossary/<目标语言>/`（例如 `blue-archive-glossary/zh-CN/`），下载 `character.csv` 之类的扁平分类术语表，直接导入沉浸式翻译等术语工具即可，无需任何转换。
2. **整个语言目录打包下载**：若需要全部 15 个分类，下载该语言目录下的全部分类 CSV，或直接取 `blue-archive-glossary/_master/<目标语言>__all_glossary.csv`（该语言全部对照行的合并总表）。
3. **克隆整个仓库自行复现**：`git clone` 本仓库后，配合已收录在 `tools/` 下的生成脚本，以及脚本文档字符串里引用的三个上游仓库源码，即可从原始数据重新生成全部 CSV。

## 目录结构

```text
Blue_Archive_Glossary（蔚蓝档案）/
  blue-archive-glossary/          数据产品容器
    README.md                     数据产品说明（本页结构）
    _master/                      原各语言 00_master/ 内容，按语言前缀保留
      zh-CN__all_glossary.csv     简体中文全部对照行合并总表
      zh-CN__all_terms.csv        简体中文全部词条清单
      zh-CN__index.csv            分类索引与条数
      zh-CN__README.md            该语言库的既有详细说明
      ...
    zh-CN/                        以简体中文为目标语言的术语库
      README.md                   本语言库说明
      character.csv               角色名称（source,target,tgt_lng）
      character__terms.csv        角色名称词条清单（id,term,src_table）
      school.csv                  学校
      school__terms.csv
      club.csv                    社团
      club__terms.csv
      story_title.csv             剧情标题
      story_title__terms.csv
      favor_item.csv              爱用品
      favor_item__terms.csv
      location.csv                地名
      location__terms.csv
      terminology.csv             术语
      terminology__terms.csv
      event.csv                   活动
      event__terms.csv
      scenario_character.csv      剧情角色
      scenario_character__terms.csv
      enemy.csv                   敌人
      enemy__terms.csv
      skill.csv                   技能
      skill__terms.csv
      item.csv                    道具
      item__terms.csv
      equipment.csv               装备
      equipment__terms.csv
      furniture.csv               家具
      furniture__terms.csv
      stage.csv                   关卡
      stage__terms.csv
    zh-TW/                        同上结构（以繁体中文为目标语言）
    en-US/                        同上结构（以 English 为目标语言）
    ja-JP/                        同上结构（以日本語为目标语言）
    ko-KR/                        同上结构（以한국어为目标语言）
    th-TH/                        同上结构（以ภาษาไทย为目标语言）
    multilingual/                 六语并排总表
      00_master/
        all_terms_multilingual.csv   全部词条，一条一行、六语并排
        README.md                    总表说明与列定义
      01_character/           01_character_multilingual.csv
      02_school/              02_school_multilingual.csv
      03_club/                03_club_multilingual.csv
      04_story_title/         04_story_title_multilingual.csv
      05_favor_item/          05_favor_item_multilingual.csv
      06_location/            06_location_multilingual.csv
      07_terminology/         07_terminology_multilingual.csv
      08_event/               08_event_multilingual.csv
      09_scenario_character/  09_scenario_character_multilingual.csv
      10_enemy/               10_enemy_multilingual.csv
      11_skill/               11_skill_multilingual.csv
      12_item/                12_item_multilingual.csv
      13_equipment/           13_equipment_multilingual.csv
      14_furniture/           14_furniture_multilingual.csv
      15_stage/               15_stage_multilingual.csv
  tools/                          生成脚本与生成元数据
    build_glossary.py             术语库生成脚本（Python）
    extract_ts_titles.mjs         剧情标题提取脚本（需要 Node.js）
    ts_titles.json                剧情标题提取结果（`extract_ts_titles.mjs` 的缓存，`build_glossary.py` 直接读取）
  README.md                       本说明（简体中文）
  README_EN.md                    英文说明
  README_JP.md                    日文说明
```

每个目标语言目录下直接存放 15 组扁平 CSV：`<category>.csv` 与 `<category>__terms.csv`，没有分类子目录；`multilingual/` 保持原有的六语并排子目录结构。
