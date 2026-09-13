# Genshin Impact 用語集 / Genshin Impact Terminology Database / 《原神》翻译术语库

## [中文](README.md) [English](README_EN.md)

本ディレクトリは『原神』（Genshin Impact）の多言語対照用語集です。**メイン用語集**と**補完用語集**の二部構成で、メイン用語集は **14 言語**（zh-CN / zh-TW / en-US / ja-JP / ko-KR / fr-FR / de-DE / es-ES / ru-RU / pt-BR / it-IT / tr-TR / th-TH / vi-VN）を対象言語とし、各言語 27 個のカテゴリ CSV でゲーム内の名称データを収録しています。補完用語集は 4 言語（zh-CN / zh-TW / en-US / ja-JP）を対象に、NPC・地名・任務・イベントなどメイン用語集に未収録の語句を補います。

メイン用語集は **8,186** 個の一意な見出し語（27 カテゴリの合計）、**1,252,692** 行の対照、**1,069,738** 個の全体一意な `source/target/tgt_lng` の組み合わせを収録し、補完用語集はさらに **51,581** 行の対照と **1,343** 行の別名を追加します。補完用語集はメイン用語集に存在しない組み合わせだけを含むため、そのまま重ねて使用できます。

訳語はすべてゲーム本体の公式ローカライズ済みテキスト（genshin-db / genshin-langdata が収録するゲームデータファイル）に由来し、**二次翻訳や機械翻訳ではありません**。

## 使用方法

1. 単一ファイルのダウンロード：`genshin-glossary/<言語コード>/` を開き、必要なカテゴリの CSV をダウンロードしてください（TCG カテゴリは `TCG/` サブディレクトリ内）。没入型翻訳などの用語ツールにそのまま取り込めます。補完語句は `genshin-glossary-supplement/<言語コード>/` にあります。
2. 言語ディレクトリごとの一括ダウンロード：GitHub で `genshin-glossary/<言語コード>/` を開き、ディレクトリのダウンロード機能でその対象言語の全カテゴリファイルを取得してください。補完用語集も同様です。
3. リポジトリ全体をクローンし、`tools/` 以下のスクリプトと、あらかじめダウンロードした参照元リポジトリ（genshin-db、genshin-langdata）のソースを用いて、すべての CSV を自力で再現できます。

## ディレクトリ構成

```text
Genshin_Impact_glossary（原神）/
├── README.md                     # 簡体字中国語
├── README_EN.md                  # English
├── README_JP.md                  # 本ファイル（日本語）
├── genshin-glossary/             # メイン用語集（genshin-db、14 対象言語、各言語 27 CSV）
│   ├── README.md                 # メイン用語集の説明（生成物）
│   ├── zh-CN/                    # 対象言語 = 簡体字中国語
│   │   ├── characters.csv
│   │   ├── talents.csv
│   │   ├── ...                   # 上位カテゴリ CSV は計 17 個
│   │   └── TCG/                  # TCG カテゴリ。サブタイプ別に 10 CSV へ分割
│   │       ├── action-cards.csv
│   │       └── ...
│   ├── zh-TW/
│   ├── en-US/  ja-JP/  ko-KR/  fr-FR/  de-DE/  es-ES/  ru-RU/
│   ├── pt-BR/  it-IT/  tr-TR/  th-TH/  vi-VN/     # 言語ディレクトリは計 14 個
├── genshin-glossary-supplement/  # 補完用語集（genshin-langdata、4 対象言語）
│   ├── README.md                 # 補完用語集の説明（生成物）
│   ├── zh-CN/
│   │   ├── characters.csv        # メイン用語集と同名の上位カテゴリ 9 個
│   │   ├── _variants.csv         # 別名・通称・よくある誤記。追加の source として補完
│   │   └── extra/                # 追加カテゴリ 10 個
│   │       ├── quests.csv
│   │       └── ...
│   ├── zh-TW/  en-US/  ja-JP/    # 言語ディレクトリは計 4 個、各 20 CSV
└── tools/
    ├── build_main_glossary.js    # genshin-db からメイン用語集を生成
    ├── build_supplement.mjs      # genshin-langdata から補完用語集を生成（メイン用語集の出力に依存）
    ├── readme_main.js            # genshin-glossary/README.md を生成
    ├── readme_sup.js             # genshin-glossary-supplement/README.md を生成
    ├── glossary_counts.json      # メイン用語集のビルドメタデータ（言語・カテゴリ別の語数と行数）
    └── supplement_counts.json    # 補完用語集のビルドメタデータ
```

## データ概要

### メイン用語集：言語別の対照行数

「対照行数」＝その言語ディレクトリ内の全 27 CSV のデータ行数（ヘッダーを除く）。「CSV ファイル数」はその言語ディレクトリ内の CSV の個数です。

| 言語 | 言語名 | CSV ファイル数 | 対照行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 27 | 89,790 |
| `zh-TW` | 繁體中文 | 27 | 89,434 |
| `en-US` | English | 27 | 89,412 |
| `ja-JP` | 日本語 | 27 | 89,490 |
| `ko-KR` | 한국어 | 27 | 89,460 |
| `fr-FR` | Français | 27 | 89,613 |
| `de-DE` | Deutsch | 27 | 89,362 |
| `es-ES` | Español | 27 | 89,411 |
| `ru-RU` | Русский | 27 | 89,418 |
| `pt-BR` | Português | 27 | 89,444 |
| `it-IT` | Italiano | 27 | 89,437 |
| `tr-TR` | Türkçe | 27 | 89,423 |
| `th-TH` | ภาษาไทย | 27 | 89,468 |
| `vi-VN` | Tiếng Việt | 27 | 89,530 |
| **合計** | **14 言語** | **378** | **1,252,692** |

> 14 の言語ディレクトリ全体で、**1,069,738** 個の全体一意な `source/target/tgt_lng` の組み合わせがあります（言語間の重複排除後）。
> 1 つの言語ディレクトリ内では、同じ項目が残り 13 言語それぞれを `source` として 1 行ずつ出現します（重複行および同形行は統合済み）。

### メイン用語集：上位カテゴリと語数

「語数」はそのカテゴリの**一意な見出し語数**です（1 語 = ゲーム内の 1 つの名称オブジェクト。集計は簡体字中国語側）。
「言語あたり行数」は、そのカテゴリ CSV のデータ行数の 14 言語にわたる平均値（四捨五入）です。

| カテゴリ | ファイル | 語数 | 言語あたり行数 |
| --- | --- | --- | --- |
| characters | `characters.csv` | 122 | 577 |
| talents | `talents.csv` | 125 | 632 |
| constellations | `constellations.csv` | 125 | 632 |
| weapons | `weapons.csv` | 249 | 2,823 |
| materials | `materials.csv` | 919 | 10,637 |
| foods | `foods.csv` | 398 | 4,541 |
| crafts | `crafts.csv` | 295 | 3,522 |
| artifacts | `artifacts.csv` | 63 | 727 |
| domains | `domains.csv` | 284 | 3,636 |
| enemies | `enemies.csv` | 346 | 4,104 |
| animals | `animals.csv` | 223 | 2,647 |
| outfits | `outfits.csv` | 150 | 1,869 |
| windgliders | `windgliders.csv` | 18 | 211 |
| namecards | `namecards.csv` | 289 | 3,606 |
| geographies | `geographies.csv` | 268 | 3,389 |
| achievements | `achievements.csv` | 1,548 | 19,463 |
| adventureranks | `adventureranks.csv` | 21 | 158 |
| **TCG（10 サブカテゴリの合計）** | `TCG/*.csv` | **2,743** | **26,304** |

### メイン用語集：TCG サブカテゴリ

| サブカテゴリ | ファイル | 語数 |
| --- | --- | --- |
| action-cards | `TCG/action-cards.csv` | 927 |
| character-cards | `TCG/character-cards.csv` | 149 |
| enemy-cards | `TCG/enemy-cards.csv` | 134 |
| summons | `TCG/summons.csv` | 152 |
| status-effects | `TCG/status-effects.csv` | 1,159 |
| keywords | `TCG/keywords.csv` | 139 |
| card-backs | `TCG/card-backs.csv` | 39 |
| card-boxes | `TCG/card-boxes.csv` | 7 |
| detailed-rules | `TCG/detailed-rules.csv` | 11 |
| level-rewards | `TCG/level-rewards.csv` | 26 |

### 補完用語集：言語別の追加行数

| 言語 | 言語名 | 上位カテゴリ CSV | 対照行数 | 別名行数（`_variants.csv`） |
| --- | --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 19 | 12,237 | 333 |
| `zh-TW` | 繁體中文 | 19 | 12,221 | 332 |
| `en-US` | English | 19 | 13,815 | 395 |
| `ja-JP` | 日本語 | 19 | 13,308 | 283 |
| **合計** | **4 言語** | **76** | **51,581** | **1,343** |

> 補完用語集の各言語ディレクトリには 20 個の CSV があります。メイン用語集と同名の上位カテゴリ 9 個、`extra/` 以下の追加カテゴリ 10 個、そして `_variants.csv` 1 個です。

### 補完用語集：カテゴリ別の追加行数

| カテゴリ | `zh-CN` | `zh-TW` | `en-US` | `ja-JP` | 合計 |
| --- | --- | --- | --- | --- | --- |
| artifacts | 28 | 29 | 31 | 32 | 120 |
| characters | 3,873 | 3,796 | 4,609 | 4,221 | 16,499 |
| domains | 216 | 212 | 240 | 226 | 894 |
| materials | 691 | 738 | 741 | 789 | 2,959 |
| enemies | 480 | 518 | 525 | 697 | 2,220 |
| foods | 209 | 259 | 233 | 246 | 947 |
| animals | 157 | 158 | 172 | 175 | 662 |
| geographies | 1,104 | 1,082 | 1,235 | 1,163 | 4,584 |
| weapons | 56 | 75 | 56 | 69 | 256 |
| extra/dialogue | 117 | 115 | 123 | 121 | 476 |
| extra/facilities | 234 | 226 | 270 | 236 | 966 |
| extra/objects | 459 | 447 | 508 | 472 | 1,886 |
| extra/organizations | 213 | 205 | 243 | 209 | 870 |
| extra/quests | 1,664 | 1,652 | 1,769 | 1,753 | 6,838 |
| extra/sereniteapot | 33 | 32 | 37 | 32 | 134 |
| extra/story | 286 | 282 | 348 | 302 | 1,218 |
| extra/system | 357 | 343 | 447 | 387 | 1,534 |
| extra/events | 1,715 | 1,705 | 1,842 | 1,796 | 7,058 |
| extra/archives | 345 | 347 | 386 | 382 | 1,460 |

### ファイル形式

メイン用語集と補完用語集の CSV は形式が完全に同一です。3 列 `source,target,tgt_lng`、**UTF-8（BOM 付き）**、**CRLF** 改行、先頭行はヘッダー、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従って引用符で囲みます。`target` は `tgt_lng` が示す言語の訳語、`source` は同じ項目を**他のいずれかの言語**で書いた表記です。

| source | target | tgt_lng |
| --- | --- | --- |
| Aether | 空 | zh-CN |
| Alhaitham | 艾尔海森 | zh-CN |
| Harbinger of Dawn | 黎明神剑 | zh-CN |

### データクリーニングについて

元データの以下のマーカーは生成時に処理済みです。

| 元データの表記 | 処理 | 例 |
| --- | --- | --- |
| 隣接する `{M#...}{F#...}` の性別バリアント | 男性形を採用 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| 単独の `{M#…}` / `{F#…}` | 中身を採用 | `#Искатель{F#ница}` → `Искательница` |
| 名称先頭の `#`（性別関連マーカー） | 削除 | `#Éclaireuse 100%` → `Éclaireuse 100%` |
| `{NON_BREAK_SPACE}`、`{SPACE}` | 通常の空白に置換 | `PB{NON_BREAK_SPACE}-{NON_BREAK_SPACE}Retorno` → `PB - Retorno` |
| その他のプレースホルダー（そのまま保持） | `{NICKNAME}`、`{REALNAME[…]}`、`{MATEAVATAR#SEXPRO[…]} ` | いずれも各 1 行 |

原文と訳文が同一の重複行（英語・フランス語・ドイツ語で同形の人名など）は統合済みです。

## 使用した関連コンテンツ

| 参照元リポジトリ | 用途 |
| --- | --- |
| [theBowja/genshin-db](https://github.com/theBowja/genshin-db) | メイン用語集 `genshin-glossary/` の唯一のデータ源。ゲーム内 14 言語の公式名称マッピングを提供（データバージョン 7.0） |
| [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) | 補完用語集 `genshin-glossary-supplement/` の唯一のデータ源。NPC・地名・敵・任務・イベント・システムなどの語句と別名を提供。en / ja / zh-CN / zh-TW を収録 |

## 再生成

スクリプトは**リポジトリ外の外部データディレクトリ**（genshin-db / genshin-langdata のソースのローカルコピー）を読み込み、CSV を外部の作業ディレクトリへ出力します。本リポジトリに保存されているのはその出力結果と、ビルドメタデータ `tools/glossary_counts.json`、`tools/supplement_counts.json` です。ゲームディレクトリで以下を順に実行してください。

```bash
# 1. メイン用語集を生成（データ源：genshin-db）。14 の言語ディレクトリ + glossary_counts.json を出力
node tools/build_main_glossary.js

# 2. 補完用語集を生成（データ源：genshin-langdata。手順 1 のメイン用語集 CSV を読んで重複を除去）
node tools/build_supplement.mjs

# 3. ビルドメタデータから 2 つの子用語集 README を再生成（上記の外部出力ディレクトリへ書き込み）
node tools/readme_main.js
node tools/readme_sup.js
```

依存関係：手順 2 は手順 1 の出力（`genshin-glossary/` 以下の全 CSV）を重複判定の基準として読み込むため、**必ず手順 1 を先に実行**してください。手順 3 の 2 つのスクリプトはそれぞれの用語集の `_counts.json` ビルドメタデータだけを読むため、互いに独立しています。
再現する前に [genshin-db](https://github.com/theBowja/genshin-db) と
[xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) のソースを取得し、スクリプト冒頭のパス定数をローカルコピーへ向けてください
（`build_main_glossary.js` / `build_supplement.mjs` の `SRC`/`LD`/`OUT`、および 2 つの readme スクリプトの `MAIN`/`SUP`）。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習・研究および AI 翻訳ソフト（没入型翻訳を含みますがこれに限りません）の用語マッチングを補助する目的にのみ使用されます。本集は『原神』の開発元、発行元、販売代理店、運営会社、権利者といかなる従属・許諾・協力・代理・公式代表の関係も持ちません。本集の訳語は公式の立場を表すものではなく、常に正確・完全であること、またゲームの現行バージョンと一致することを保証するものではなく、**本ゲームの公式用語集や公式ローカライズファイルと見なしてはなりません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はすべてそれぞれの権利者に帰属します。本集はこれらの第三者の知的財産権について何ら権利を主張しません。本プロジェクトおよびそれに基づく翻訳結果の利用によって生じたいかなる責任も利用者自身が負います。権利者の方が内容を不適切と判断された場合は、GitHub Issues / Pull Request にてご連絡ください。維持者が確認のうえ修正または削除します。

完全な条項はリポジトリルートの `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元・発行元・販売代理店・権利者と、いかなる隷属・許諾・協力・代理の関係もありません。**
