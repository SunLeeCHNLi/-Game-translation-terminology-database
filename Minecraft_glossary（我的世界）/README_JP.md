# Minecraft 用語集 / Minecraft Terminology Database / 《我的世界》翻译术语库

## [中文](README.md) [English](README_EN.md)

本ディレクトリは『Minecraft（マインクラフト）』の多言語翻訳用語集です。**Minecraft Java 版の公式言語ファイル**を出典とし、ブロック・アイテム・エンティティ・バイオーム・エンチャント・ステータス効果・進捗・字幕・GUI・設定など 34 分類を **14 の対象言語**、**1,420,443** 行の対照データとして収録しています。さらに Minecraft Wiki の訳名標準化に基づく補助用語集（中国語 2 言語、**10,314** 行）を併設しています。本編の訳文はゲーム内の公式ローカライズそのものであり、**二次翻訳ではなく公式ローカライズ資料**です。補助用語集は Minecraft Wiki の訳名標準化ページ（Crowdin で確定した公式方針と整合）に基づくもので、併用して参照できます。すべて `source,target,tgt_lng` の 3 列 CSV で、Immersive Translate などの用語ツールにそのまま取り込めます。

## 使用方法

1. **単一ファイルのダウンロード**：該当する言語ディレクトリ（例：`minecraft-glossary/zh-CN/`。システム系・テキスト系の分類はその言語ディレクトリ内の `extra/` サブフォルダにあります）を開き、必要な分類ファイル（`blocks.csv` / `items.csv` / `extra/subtitles.csv` など）だけをダウンロードします。Immersive Translate など用語リストに対応したツールへそのまま取り込めます。
2. **言語ディレクトリごとダウンロード**：ひとつの言語ディレクトリ（例：`minecraft-glossary/ja-JP/`）をまとめてダウンロードし、必要な分類ファイルを選んで使います。補助用語集は `minecraft-glossary-supplement/zh-CN/` と `minecraft-glossary-supplement/zh-TW/` にあります。
3. **リポジトリ全体をクローンして再現**：`tools/` のスクリプトと「使用した関連コンテンツ」に挙げた上流リポジトリを用意すれば、すべての CSV とメタデータを自分で再生成できます（「再生成」を参照）。

## ディレクトリ構成

```text
Minecraft_glossary（我的世界）/
├── README.md                     # 簡体字中国語
├── README_EN.md                  # English
├── README_JP.md                  # 本ファイル
├── minecraft-glossary/           # 本編：14 の対象言語 × 34 分類
│   ├── README.md                 # 本編の中国語説明（tools/make_readme.py が生成）
│   ├── zh-CN/                    # 対象言語 = 簡体字中国語
│   │   ├── blocks.csv            # ゲーム内容の分類、19 ファイル
│   │   ├── items.csv
│   │   ├── ...
│   │   └── extra/                # システム系・テキスト系の分類、15 ファイル
│   │       ├── subtitles.csv
│   │       └── ...
│   ├── zh-TW/                    # 対象言語 = 繁体字中国語
│   ├── en-US/                    # English
│   ├── ja-JP/                    # 日本語
│   ├── ko-KR/                    # 한국어
│   ├── fr-FR/                    # Français
│   ├── de-DE/                    # Deutsch
│   ├── es-ES/                    # Español
│   ├── ru-RU/                    # Русский
│   ├── pt-BR/                    # Português
│   ├── it-IT/                    # Italiano
│   ├── tr-TR/                    # Türkçe
│   ├── th-TH/                    # ภาษาไทย
│   └── vi-VN/                    # Tiếng Việt
├── minecraft-glossary-supplement/   # 補助用語集（Wiki 訳名標準化）：2 の対象言語 × 13 分類
│   ├── README.md                 # 補助用語集の中国語説明（tools/make_readme.py が生成）
│   ├── zh-CN/                    # 対象言語 = 簡体字中国語
│   └── zh-TW/                    # 対象言語 = 繁体字中国語
└── tools/                        # 生成スクリプトと生成メタデータ
    ├── build_glossary.py         # 公式言語ファイルから本編を生成
    ├── build_wiki_supplement.py  # Wiki 訳名標準化ページから補助用語集を生成
    ├── make_readme.py            # 2 つの子用語集の README.md を生成
    ├── verify_output.py          # CSV のヘッダー・重複行・行数統計を検証
    ├── glossary_counts.json      # 本編の言語別・分類別の項目数統計
    └── supplement_counts.json    # 補助用語集の言語別・分類別の項目数統計
```

各言語ディレクトリにはゲーム内容の 19 分類 CSV に加えて、システム系・テキスト系 15 分類の CSV を入れた `extra/` サブフォルダがあります（1 言語あたり 34 CSV）。CSV のファイル名がそのまま分類名です。

## データ概要

### 規模

| 用語集 | 対象言語 | 分類 | CSV ファイル | データ行（項目 × 原文言語） |
| --- | --- | --- | --- | --- |
| 本編 `minecraft-glossary/` | 14 | 34 | 476 | 1,420,443 |
| 補助用語集 `minecraft-glossary-supplement/` | 2 | 13 | 26 | 10,314 |
| **合計** | **16 言語ディレクトリ** |  | **502** | **1,430,757** |

### 本編の言語別行数（各言語 34 ファイル）

| 言語 | 名称 | データ行 |
| --- | --- | --- |
| `zh-CN` | 简体中文 | 101,247 |
| `zh-TW` | 繁體中文 | 101,215 |
| `en-US` | English | 101,550 |
| `ja-JP` | 日本語 | 101,553 |
| `ko-KR` | 한국어 | 101,279 |
| `fr-FR` | Français | 101,569 |
| `de-DE` | Deutsch | 101,431 |
| `es-ES` | Español | 101,647 |
| `ru-RU` | Русский | 101,629 |
| `pt-BR` | Português | 101,489 |
| `it-IT` | Italiano | 101,580 |
| `tr-TR` | Türkçe | 101,665 |
| `th-TH` | ภาษาไทย | 101,264 |
| `vi-VN` | Tiếng Việt | 101,325 |
| **合計** |  | **1,420,443** |

### 本編のゲーム内容分類（19）

「項目数」は公式言語ファイルにおいてその分類が持つ**ゲーム名称オブジェクト数**、「行数」は簡体字中国語ディレクトリ内のその分類 CSV のデータ行数です。1 つの項目は他の 13 言語それぞれを `source` として 1 行を生成するため、両者は一致しません。

| 分類 | ファイル | 説明 | 項目数 | zh-CN 行数 |
| --- | --- | --- | --- | --- |
| blocks | `blocks.csv` | ブロック | 1975 | 25426 |
| items | `items.csv` | アイテム | 803 | 9061 |
| entities | `entities.csv` | エンティティ | 219 | 2582 |
| biomes | `biomes.csv` | バイオーム | 67 | 835 |
| enchantments | `enchantments.csv` | エンチャント | 54 | 553 |
| effects | `effects.csv` | ステータス効果 | 42 | 514 |
| instruments | `instruments.csv` | 楽器 | 8 | 98 |
| materials | `materials.csv` | 防具装飾の素材 | 11 | 143 |
| paintings | `paintings.csv` | 絵画 | 104 | 315 |
| attributes | `attributes.csv` | 属性 | 83 | 555 |
| item-groups | `item-groups.csv` | アイテムグループ | 16 | 198 |
| jukebox-songs | `jukebox-songs.csv` | ジュークボックスの曲 | 22 | 42 |
| trim-patterns | `trim-patterns.csv` | 防具装飾の模様 | 18 | 234 |
| colors | `colors.csv` | 色 | 16 | 184 |
| statistics | `statistics.csv` | 統計 | 88 | 1143 |
| maps | `maps.csv` | 地図 | 33 | 422 |
| music | `music.csv` | 音楽曲 | 70 | 192 |
| sound-categories | `sound-categories.csv` | サウンドカテゴリ | 11 | 133 |
| game-modes | `game-modes.csv` | ゲームモード | 6 | 77 |

### 本編の `extra/` 分類（システム系・テキスト系、15）

| 分類 | ファイル | 説明 | 項目数 | zh-CN 行数 |
| --- | --- | --- | --- | --- |
| subtitles | `extra/subtitles.csv` | 字幕 | 1023 | 12407 |
| death-messages | `extra/death-messages.csv` | 死亡メッセージ | 106 | 1334 |
| advancement-titles | `extra/advancement-titles.csv` | 進捗のタイトル | 127 | 1603 |
| advancement-descriptions | `extra/advancement-descriptions.csv` | 進捗の説明 | 127 | 1641 |
| gamerules | `extra/gamerules.csv` | ゲームルール | 117 | 1490 |
| commands | `extra/commands.csv` | コマンドと引数 | 856 | 10758 |
| gui | `extra/gui.csv` | 画面テキスト | 581 | 6604 |
| options | `extra/options.csv` | 設定とキー割り当て | 754 | 8165 |
| multiplayer | `extra/multiplayer.csv` | マルチプレイ | 173 | 2013 |
| realms | `extra/realms.csv` | Realms | 426 | 4962 |
| world-management | `extra/world-management.csv` | ワールド管理 | 294 | 3578 |
| resource-packs | `extra/resource-packs.csv` | リソースパックとデータパック | 62 | 761 |
| telemetry | `extra/telemetry.csv` | テレメトリ | 70 | 897 |
| dev-tools | `extra/dev-tools.csv` | 開発・テスト用ツール | 144 | 1811 |
| misc | `extra/misc.csv` | その他 | 53 | 516 |

### 補助用語集の分類（Wiki 訳名標準化、13）

数値は `tools/supplement_counts.json` によります。「項目数」は英語名で重複を除いた標準中国語名の数、「行数」は各言語ディレクトリ内のその分類 CSV のデータ行数です。

| 分類 | ファイル | 項目数 | zh-CN 行数 | zh-TW 行数 |
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

補助用語集の 2 つの言語ディレクトリはそれぞれ 13 CSV、**5,157** 行です。分類は Wiki ページの節立てに従っており、本編の 34 分類とは名称も範囲も異なるため、分類名で直接統合することはできません。

## 使用した関連コンテンツ

| 出典リポジトリ / ページ | 用途 |
| --- | --- |
| [misode/mcmeta](https://github.com/misode/mcmeta) | 本編のデータ源：`assets` ブランチの `assets/minecraft/lang/<locale>.json`、すなわち Minecraft Java 版の公式言語ファイル。14 の対象言語はすべてここから取得 |
| [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) | `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` などの分類方法を分類分けの参考に使用。同ライブラリの `particles`・`sounds` は公式言語ファイルでは内部 ID のみでローカライズ名がないため、独立した分類にしていません |
| [Minecraft Wiki:译名标准化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化) | 補助用語集のデータ源：Wiki の標準訳名（簡体字・繁体字の 2 変種を別々に取得して統合）。Crowdin で確定した公式ローカライズ方針と整合し、未確定の場合はゲーム内表記を使用 |
| [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) | バージョン別ブランチでテクスチャを保管する素材リポジトリ。その言語ファイル構造を照合の参考にしています |

## 再生成

```bash
# 1) 本編：公式言語ファイルから 14 言語 × 34 分類の CSV を生成
python tools/build_glossary.py

# 2) 補助用語集：Wiki 訳名標準化ページの 2 変種から zh-CN / zh-TW の 13 分類を生成
python tools/build_wiki_supplement.py

# 3) 2 つのメタデータファイルから子用語集 2 冊の中国語 README を再生成
python tools/make_readme.py

# 4) 検証：ヘッダー・tgt_lng・空値・重複行を 1 行ずつ確認し、メタデータの行数と照合
python tools/verify_output.py
```

補足：

- 2 つの生成スクリプトはいずれも**スクリプト外のソースデータディレクトリを読みます**（既定は `SRC_DIR = E:\Download\BT\Codex_input`。テキストエディタで自分のパスに変更してください）：
  `build_glossary.py` は `mcmeta_lang/<locale>.json`（mcmeta の `assets` ブランチから取得）、
  `build_wiki_supplement.py` はソースディレクトリ内の wiki_std_cn.json / wiki_std_tw.json（同ページの `action=parse&prop=text&variant=zh-cn|zh-tw` のレンダリング結果。ファイル名は `tools/build_wiki_supplement.py` の `SRC_DIR` 定義を参照）が必要です。
  これらのソースデータは本リポジトリには含まれず、別途用意する必要があります。
- 生成メタデータは `tools/glossary_counts.json` と `tools/supplement_counts.json` に書き出されます。スクリプトが用語集のデータディレクトリへメタデータを書き込むことはもうありません。
- パイプライン全体は **Python 標準ライブラリのみ**（`json` / `os` / `csv` / `re` / `html` / `collections`）で動作し、Node.js もサードパーティパッケージも不要です（Python 3.8 以上）。
- スクリプトは自身の位置からゲームのルートを割り出すため、実行時は必ず `tools/` 接頭辞を付けます（例：ゲームディレクトリで `tools/verify_output.py` を実行）。
- CSV はすべて **UTF-8（BOM 付き）**、**CRLF** 改行、先頭行はヘッダー `source,target,tgt_lng` で、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従って引用符で囲みます。説明用の Markdown ファイルは UTF-8（BOM なし）です。
- データクリーニングの方針：対象言語と完全に同一の行は削除（各言語で未訳の曲名・固有名詞など）。同一項目から生じた重複行は統合。空値・訳抜けは行を生成しません。書式プレースホルダー（`%s`、`%1$s`、`%%`）はそのまま保持。同一キーの言語間で重複する訳文は `source`+`target` で重複排除。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習・研究および AI 翻訳ソフト（Immersive Translate を含みますがこれに限りません）の用語マッチング支援のみを目的としています。本用語集は、関連ゲームの開発元・発行元・販売代理店・運営・権利者といかなる所属・許諾・協力・代理・公式代表の関係も持ちません。収録された訳名は公式の立場を代表するものではなく、常に正確・完全であること、またゲームの現行バージョンと一致することを保証しません。**いかなるゲームの公式用語集や公式ローカライズファイルと見なすこともできません。** ゲーム名・キャラクター名・固有名詞・商標などの知的財産権はそれぞれの権利者に帰属し、本用語集はそれらの第三者的知的財産権について何ら権利を主張しません。本プロジェクトおよびそれに基づく翻訳結果の利用によって生じたいかなる責任も利用者自身が負うものとします。権利者が必要と判断された場合には GitHub Issues / Pull Request にてご連絡ください。確認のうえ修正または削除いたします。完全な条項はリポジトリのルートにある `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元・発行元・販売代理店・権利者といかなる隷属・許諾・協力・代理の関係もありません。**
