# マインクラフト（Minecraft）Wiki 訳名標準化 補助用語集

## [简体中文](README.md) [English](README_EN.md)

本ディレクトリは `minecraft-glossary/` の**補助用語集**であり、[Minecraft Wiki 訳名標準化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) ページにある標準訳名を収録し、公式言語ファイルが網羅していない、あるいは Wiki 標準と一致しない訳名を補完するために使用します。

## データ出典

- [Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)（簡体字中国語 / 繁体字中国語の 2 変種をそれぞれ取得して統合）
- このページは Wiki の訳名規範の出典でもあり、その訳名は Crowdin 上で確定済みの公式ローカライズ方針と一致させ、未確定の場合はゲーム内の原文を暫定的に使用しています。

## 対象範囲

- 本補助用語集は**`zh-CN`（簡体字中国語）と `zh-TW`（繁体字中国語）の 2 つの対象言語のみ**を収録します。その他の言語は主用語集 `minecraft-glossary/` をご使用ください。
- 各言語フォルダ内では、同一項目が `en-US` と、もう一方の中国語変種をそれぞれ `source` として 1 行ずつ現れます。

## ディレクトリ構成

```
minecraft-glossary-supplement/
├── zh-CN/                    # 対象言語 = 簡体字中国語、13 個のカテゴリファイル
│   ├── blocks.csv
│   ├── items.csv
│   └── ...
├── zh-TW/                    # 対象言語 = 繁體中文、同じ 13 カテゴリ
└── README.md                 # 本ファイル

（各言語の項目数統計は親ディレクトリの `tools/supplement_counts.json` を参照）
```

## ファイル形式

主用語集と同一です：**UTF-8（BOM 付き）**、**CRLF**、先頭行が見出し。

| source | target | tgt_lng |
| --- | --- | --- |
| Chest | 箱子 | zh-CN |
| 儲物箱 | 箱子 | zh-CN |

## カテゴリと項目数

下表の数字は `tools/supplement_counts.json` から取得しています。

### 言語別の項目数

| 言語 | 言語（名称） | ファイル数 | データ行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 13 | 5,157 |
| `zh-TW` | 繁體中文 | 13 | 5,157 |

### 分類別の明細

「項目数」＝ その分類において英語名で重複排除した後の標準中国語名の件数；
「行数」＝ その言語フォルダ内の当該カテゴリ CSV のデータ行数（各項目は最大で `en-US` と、もう一方の中国語変種という 2 種類の `source` から
それぞれ 1 行ずつ生成されるため、行数は項目数の約 2 倍になります。2 種類の中国語表記が同一の場合、または英語名自体が訳名の場合は、その source 行は生成されません）。

| カテゴリ | ファイル | 項目数 | zh-CN 行数 | zh-TW 行数 |
| --- | --- | --- | --- | --- |
| advancements | `advancements.csv` | 126 | 242 | 242 |
| biomes | `biomes.csv` | 67 | 117 | 117 |
| blocks | `blocks.csv` | 1345 | 2561 | 2561 |
| effects | `effects.csv` | 40 | 73 | 73 |
| enchantments | `enchantments.csv` | 43 | 82 | 82 |
| entities | `entities.csv` | 161 | 289 | 289 |
| environment | `environment.csv` | 119 | 205 | 205 |
| game-content | `game-content.csv` | 67 | 113 | 113 |
| game-modes | `game-modes.csv` | 18 | 31 | 31 |
| game-versions | `game-versions.csv` | 64 | 101 | 101 |
| items | `items.csv` | 626 | 1178 | 1178 |
| other | `other.csv` | 38 | 64 | 64 |
| technical | `technical.csv` | 58 | 101 | 101 |

## 主用語集との相違点

- 分類体系が異なります：本補助用語集は Wiki ページの**章節**によって 13 カテゴリ（`advancements`、`biomes`、`blocks`、`effects`、`enchantments`、`entities`、`environment`、`game-content`、`game-modes`、`game-versions`、`items`、`other`、`technical`）に分かれており、主用語集 `minecraft-glossary/` の 34 カテゴリ（主カテゴリ 19 個 + `extra/` カテゴリ 15 個）とは**名称も基準も異なる**ため、両者はカテゴリ名で直接統合することはできません。
- 中国語のみを収録：`zh-CN` の行は `en-US` と `zh-TW` を `source` とし、`zh-TW` の行は `en-US` と `zh-CN` を `source` とします。その他の言語の表記は含まれません。
- Wiki は「台灣正體」の用語を採用しているため（例：`Chest` = 儲物箱、`Slab` = 半磚、`Stairs` = 階梯）、ゲーム内の繁体字中国語言語ファイルと差異が生じる場合があり、2 つの資料は**必要に応じて使い分けること**を推奨します。
- 「翻訳しない」と指定された項目（`Mojang`、`Minecraft` など）は本用語集に収録しません。
- 同一の英語名が複数の中国語表記に対応する場合は、Wiki の表記を使用し、` / ` で連結します（例：`Boolean` = 布林值 / 布林型）。

## 使用上のヒント

- 再生成：まずこのページの `zh-cn` / `zh-tw` の 2 変種（`action=parse&prop=text&variant=...`）を取得し、次に `tools/build_wiki_supplement.py` を実行します。
- 本 README は `tools/make_readme.py` によって生成され、本ページの数字は `tools/supplement_counts.json` から取得しています。数字を手動で変更しないでください。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習、研究、および AI 翻訳ソフトウェア（没入型翻訳を含むがこれに限らない）の用語マッチングを補助する目的にのみ使用されます。本データベースは『マインクラフト』（Minecraft）の開発元、販売元、代理店、運営元、著作権者との間にいかなる従属、許諾、提携、代理、公式代表の関係も有しません。データベース内の訳名は公式の立場を代表するものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なされるべきではありません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はすべてそれぞれの権利者に帰属します。本データベースは上記の第三者の知的財産権について一切の権利を主張しません。本プロジェクトおよびそれに基づいて生成された翻訳結果の使用によって生じる一切の責任は使用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。メンテナーが確認のうえ修正または削除します。完全な条項はリポジトリルートの `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元、販売元、代理店、著作権者との間にいかなる隷属、許諾、提携、代理の関係もありません。**