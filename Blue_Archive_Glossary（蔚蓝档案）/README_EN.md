## Usage

1. **Single-file download** — open `blue-archive-glossary/<target-language>/` (for example `blue-archive-glossary/zh-CN/`) and download a flat category glossary such as `character.csv`. It can be imported directly into terminology tools such as Immersive Translate, with no conversion needed.
2. **Whole-language download** — if you need all 15 categories, download every category CSV under that language, or simply take `blue-archive-glossary/_master/<target-language>__all_glossary.csv`, the merged table of every aligned row for that language.
3. **Clone the whole repository and regenerate** — after `git clone`, use the generation scripts kept in `tools/` together with the three upstream repositories named in the script's docstring to rebuild every CSV from the original data.

## Directory Structure

```text
Blue_Archive_Glossary（蔚蓝档案）/
  blue-archive-glossary/    data product container
    README.md               data product documentation
    _master/                former per-language 00_master/ contents, language-prefixed
      zh-CN__all_glossary.csv   merged aligned rows of all 15 categories for zh-CN
      zh-CN__all_terms.csv      complete term list for zh-CN
      zh-CN__index.csv          category index and counts
      zh-CN__README.md          existing detailed notes for this language
      ...
    zh-CN/                  termbase targeting Simplified Chinese
      README.md             detailed notes for this language termbase
      character.csv         character names (source,target,tgt_lng)
      character__terms.csv  character-name term list (id,term,src_table)
      school.csv            schools
      school__terms.csv
      club.csv              clubs
      club__terms.csv
      story_title.csv       story titles
      story_title__terms.csv
      favor_item.csv        favor items (gifts)
      favor_item__terms.csv
      location.csv          locations
      location__terms.csv
      terminology.csv       terminology
      terminology__terms.csv
      event.csv             events
      event__terms.csv
      scenario_character.csv  scenario characters
      scenario_character__terms.csv
      enemy.csv             enemies
      enemy__terms.csv
      skill.csv             skills
      skill__terms.csv
      item.csv              items
      item__terms.csv
      equipment.csv         equipment
      equipment__terms.csv
      furniture.csv         furniture
      furniture__terms.csv
      stage.csv             stages
      stage__terms.csv
    zh-TW/                  same layout (target language: Traditional Chinese)
    en-US/                  same layout (target language: English)
    ja-JP/                  same layout (target language: Japanese)
    ko-KR/                  same layout (target language: Korean)
    th-TH/                  same layout (target language: Thai)
    multilingual/           six-language side-by-side master table
      00_master/
        all_terms_multilingual.csv   every entry, one row, six languages side by side
        README.md                    notes and column definitions
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
  tools/                    generation scripts and generation metadata
    build_glossary.py       termbase generator (Python)
    extract_ts_titles.mjs   story-title extractor (requires Node.js)
    ts_titles.json          extracted story titles (cache for `extract_ts_titles.mjs`, read directly by `build_glossary.py`)
  README.md                 this file set: Simplified Chinese
  README_EN.md              English
  README_JP.md              Japanese
```

Every target-language directory stores 15 pairs of flat CSVs directly: `<category>.csv` and `<category>__terms.csv`, with no category subdirectories; `multilingual/` keeps its original six-language side-by-side subdirectory layout.
