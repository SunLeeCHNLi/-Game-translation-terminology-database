# マインクラフト（Minecraft）多言語用語集

## [简体中文](README.md) [English](README_EN.md)

**対象言語**ごとに独立したフォルダに分割し、各フォルダ内では**カテゴリ**ごとにファイルを分けて格納しています。システムおよびテキスト系のカテゴリは、各言語の `extra/` サブフォルダにまとめています。

## データ出典

- 主用語集：**Minecraft Java 版公式言語ファイル**。[misode/mcmeta](https://github.com/misode/mcmeta) の `assets` ブランチ（`assets/minecraft/lang/<locale>.json`）から取得し、14 言語すべてを対象としています。
- カテゴリ構造は [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data) の `blocks` / `items` / `entities` / `biomes` / `effects` / `enchantments` / `instruments` / `materials` などの分類方法を参考に分けています。なお、同ライブラリの `particles`、`sounds` は公式言語ファイルでは内部 ID のみでローカライズ名が存在しないため、独立したカテゴリにはしていません。
- 補助用語集：同階層の `minecraft-glossary-supplement/`（出典：[Minecraft Wiki 訳名標準化](https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化)）を参照。Wiki 標準の訳名を追加で提供し、簡体字中国語 / 繁体字中国語を対象としています。
- 画像リソースライブラリ [InventivetalentDev/minecraft-assets](https://github.com/InventivetalentDev/minecraft-assets) はバージョン別ブランチでテクスチャを保管しており、本用語集はその言語ファイル構造を校正の参考としています。

## ディレクトリ構成

```
minecraft-glossary（我的世界）/
├── minecraft-glossary/       # 主用語集：14 言語 × 34 カテゴリ
│   ├── zh-CN/                # 対象言語 = 簡体字中国語
│   │   ├── blocks.csv        # 主カテゴリ（ゲーム内容）、19 ファイル
│   │   ├── items.csv
│   │   ├── ...
│   │   └── extra/            # システムおよびテキスト系カテゴリ、15 ファイル
│   │       ├── subtitles.csv
│   │       └── ...
│   ├── zh-TW/
│   ├── en-US/ ... vi-VN/     # 合計 14 個の言語フォルダ
│   └── README.md             # 本ファイル
├── minecraft-glossary-supplement/   # 補助用語集（Wiki 訳名標準化）、2 言語 × 13 カテゴリ
└── tools/                    # 生成スクリプトとメタデータ
    ├── build_glossary.py
    ├── build_wiki_supplement.py
    ├── make_readme.py
    ├── verify_output.py
    ├── glossary_counts.json      # 主用語集の各言語・各カテゴリの項目数統計
    └── supplement_counts.json    # 補助用語集の各言語・各カテゴリの項目数統計
```

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行が見出しです。フィールドにカンマや引用符が含まれる場合は RFC 4180 に従って引用符でエスケープしています。

| source | target | tgt_lng |
| --- | --- | --- |
| Abbaueffizienz | 挖掘效率 | zh-CN |
| 採掘効率 | 挖掘效率 | zh-CN |

意味：`tgt_lng` で指定された対象言語について、`target` が訳文、`source` が**その他のいずれかの言語**の原文です。
つまり各言語フォルダ内では、同一項目が残り 13 言語それぞれを `source` として 1 行ずつ現れます（重複行と同形行は統合済み）。

## 言語コード

| 言語フォルダ | 言語 | Minecraft 言語ファイル locale |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `zh_cn` |
| `zh-TW` | 繁體中文 | `zh_tw` |
| `en-US` | English | `en_us` |
| `ja-JP` | 日本語 | `ja_jp` |
| `ko-KR` | 한국어 | `ko_kr` |
| `fr-FR` | Français | `fr_fr` |
| `de-DE` | Deutsch | `de_de` |
| `es-ES` | Español | `es_es` |
| `ru-RU` | Русский | `ru_ru` |
| `pt-BR` | Português | `pt_br` |
| `it-IT` | Italiano | `it_it` |
| `tr-TR` | Türkçe | `tr_tr` |
| `th-TH` | ภาษาไทย | `th_th` |
| `vi-VN` | Tiếng Việt | `vi_vn` |

## カテゴリと項目数

「項目数」とは、その分類が公式言語ファイル内で対応する**ゲーム名称オブジェクト数**（その分類キーの件数。公式に未翻訳の少数のキーを含む）を指し、
すなわちこの分類がこの対象言語で照合に参加する項目の総量です。「行数」はその言語フォルダ内の当該カテゴリ CSV のデータ行数です。
2 つの数字は異なります：1 つの項目は残り 13 言語それぞれを `source` として 1 行ずつ生成されます。

### 主カテゴリ（ゲーム内容）

| カテゴリ | ファイル | 説明 | 項目数 | 言語あたり行数（zh-CN） |
| --- | --- | --- | --- | --- |
| blocks | `blocks.csv` | ブロック | 1975 | 25426 |
| items | `items.csv` | アイテム | 803 | 9061 |
| entities | `entities.csv` | エンティティ | 219 | 2582 |
| biomes | `biomes.csv` | バイオーム | 67 | 835 |
| enchantments | `enchantments.csv` | エンチャント | 54 | 553 |
| effects | `effects.csv` | ステータス効果 | 42 | 514 |
| instruments | `instruments.csv` | 楽器 | 8 | 98 |
| materials | `materials.csv` | 装飾用防具素材 | 11 | 143 |
| paintings | `paintings.csv` | 絵画 | 104 | 315 |
| attributes | `attributes.csv` | 属性 | 83 | 555 |
| item-groups | `item-groups.csv` | インベントリ分類 | 16 | 198 |
| jukebox-songs | `jukebox-songs.csv` | レコード曲 | 22 | 42 |
| trim-patterns | `trim-patterns.csv` | 装飾用防具模様 | 18 | 234 |
| colors | `colors.csv` | 色 | 16 | 184 |
| statistics | `statistics.csv` | 統計 | 88 | 1143 |
| maps | `maps.csv` | 地図 | 33 | 422 |
| music | `music.csv` | 音楽曲 | 70 | 192 |
| sound-categories | `sound-categories.csv` | サウンド分類 | 11 | 133 |
| game-modes | `game-modes.csv` | ゲームモード | 6 | 77 |

### `extra/` カテゴリ（システムおよびテキスト）

| カテゴリ | ファイル | 説明 | 項目数 | 言語あたり行数（zh-CN） |
| --- | --- | --- | --- | --- |
| subtitles | `extra/subtitles.csv` | 字幕 | 1023 | 12407 |
| death-messages | `extra/death-messages.csv` | 死亡メッセージ | 106 | 1334 |
| advancement-titles | `extra/advancement-titles.csv` | 進捗タイトル | 127 | 1603 |
| advancement-descriptions | `extra/advancement-descriptions.csv` | 進捗説明 | 127 | 1641 |
| gamerules | `extra/gamerules.csv` | ゲームルール | 117 | 1490 |
| commands | `extra/commands.csv` | コマンドと引数 | 856 | 10758 |
| gui | `extra/gui.csv` | インターフェーステキスト | 581 | 6604 |
| options | `extra/options.csv` | 設定とキー割り当て | 754 | 8165 |
| multiplayer | `extra/multiplayer.csv` | マルチプレイ | 173 | 2013 |
| realms | `extra/realms.csv` | Realms | 426 | 4962 |
| world-management | `extra/world-management.csv` | ワールド管理 | 294 | 3578 |
| resource-packs | `extra/resource-packs.csv` | リソースパックとデータパック | 62 | 761 |
| telemetry | `extra/telemetry.csv` | テレメトリ | 70 | 897 |
| dev-tools | `extra/dev-tools.csv` | 開発・テストツール | 144 | 1811 |
| misc | `extra/misc.csv` | その他 | 53 | 516 |

## 言語別総行数

| 言語 | 言語（名称） | ファイル数 | データ行数 |
| --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 34 | 101,247 |
| `zh-TW` | 繁體中文 | 34 | 101,215 |
| `en-US` | English | 34 | 101,550 |
| `ja-JP` | 日本語 | 34 | 101,553 |
| `ko-KR` | 한국어 | 34 | 101,279 |
| `fr-FR` | Français | 34 | 101,569 |
| `de-DE` | Deutsch | 34 | 101,431 |
| `es-ES` | Español | 34 | 101,647 |
| `ru-RU` | Русский | 34 | 101,629 |
| `pt-BR` | Português | 34 | 101,489 |
| `it-IT` | Italiano | 34 | 101,580 |
| `tr-TR` | Türkçe | 34 | 101,665 |
| `th-TH` | ภาษาไทย | 34 | 101,264 |
| `vi-VN` | Tiếng Việt | 34 | 101,325 |
| **合計** |  | **476** | **1,420,443** |

## データクリーニングについて

| 処理項目 | 処理方式 |
| --- | --- |
| 対象言語と完全に同形の行 | 削除（例：各言語で未翻訳の曲名、固有名詞） |
| 同一項目から生じた重複行 | 統合 |
| 空値 / 翻訳欠落 | その言語をスキップし、空行を生成しない |
| 書式用プレースホルダー（`%s`、`%1$s`、`%%`） | そのまま保持 |
| 同一キーの言語間で重複する訳文 | `source`+`target` で重複排除 |

## 使用上のヒント

- CAT ツール（Trados、memoQ、Phrase など）にインポートする際は、対応する対象言語の CSV を選び、そのまま用語集としてインポートしてください。
- ファイル名がそのままカテゴリ名で、必要に応じて統合できます。「全カテゴリを 1 つのファイルに統合」したい場合や `src_lng`（ソース言語）列を追加したい場合も、いつでも生成できます。
- 用語集の再生成：まず公式言語ファイル（`lang/<locale>.json`）を用意し、次に `tools/build_glossary.py` を実行します。プレフィックスからカテゴリへの完全なマッピングは、このスクリプトの `CATEGORIES` テーブルにあります。
- 公式言語ファイルには合計 144 種類の言語バリアントがあり、本用語集はそのうち 14 種類を必要に応じて選んでいます。他の言語が必要な場合は、`tools/build_glossary.py` の `LANG_FILES` に追加して再生成してください。
- 本 README は `tools/make_readme.py` によって生成され、本ページの数字は `tools/glossary_counts.json` から取得しています。数字を手動で変更しないでください。

## 免責事項

本ディレクトリは個人が整理・維持する**非公式**の翻訳用語資料集であり、個人の学習、研究、および AI 翻訳ソフトウェア（没入型翻訳を含むがこれに限らない）の用語マッチングを補助する目的にのみ使用されます。本データベースは『マインクラフト』（Minecraft）の開発元、販売元、代理店、運営元、著作権者との間にいかなる従属、許諾、提携、代理、公式代表の関係も有しません。データベース内の訳名は公式の立場を代表するものではなく、常に正確・完全であること、またはゲームの現行バージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なされるべきではありません**。ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はすべてそれぞれの権利者に帰属します。本データベースは上記の第三者の知的財産権について一切の権利を主張しません。本プロジェクトおよびそれに基づいて生成された翻訳結果の使用によって生じる一切の責任は使用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request にてご連絡ください。メンテナーが確認のうえ修正または削除します。完全な条項はリポジトリルートの `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元、販売元、代理店、著作権者との間にいかなる隷属、許諾、提携、代理の関係もありません。**