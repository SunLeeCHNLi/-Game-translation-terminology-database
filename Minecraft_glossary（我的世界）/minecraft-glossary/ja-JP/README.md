# Minecraft 用語集（我的世界）— 日本語（`ja-JP`）

[← ゲーム総合説明に戻る](../../README.md) · [zh-CN](README_zh-CN.md)

本ディレクトリは、**日本語（`ja-JP`）を対象言語**とする Minecraft 用語集です。**34** 個のカテゴリ別 CSV に、**7,826** 語の用語（`target` 列で重複除去）と **101,553** 行の対照が収録されています。`tgt_lng` 列は常に `ja-JP` で、`source` は同じ用語を書いた**他の 13 言語のいずれか**、`target` は日本語表記です。ファイルは**カテゴリ**単位に分割し（1 カテゴリ 1 CSV）、システム系・テキスト系のカテゴリは `extra/` サブフォルダにまとめています。

## ファイル

- `blocks.csv`, `items.csv`, `entities.csv`, `biomes.csv`, `enchantments.csv`, `effects.csv`, `instruments.csv`, `materials.csv`, `paintings.csv`, `attributes.csv`, `item-groups.csv`, `jukebox-songs.csv`, `trim-patterns.csv`, `colors.csv`, `statistics.csv`, `maps.csv`, `music.csv`, `sound-categories.csv`, `game-modes.csv` — 主要カテゴリのファイル 19 件
- `extra/subtitles.csv`, `extra/death-messages.csv`, `extra/advancement-titles.csv`, `extra/advancement-descriptions.csv`, `extra/gamerules.csv`, `extra/commands.csv`, `extra/gui.csv`, `extra/options.csv`, `extra/multiplayer.csv`, `extra/realms.csv`, `extra/world-management.csv`, `extra/resource-packs.csv`, `extra/telemetry.csv`, `extra/dev-tools.csv`, `extra/misc.csv` — `extra/` のシステム・テキスト系カテゴリのファイル 15 件

合計 **34 個の CSV ファイル**で、いずれも同じ 3 列の形式です。

| source | target | tgt_lng |
| --- | --- | --- |
| A Balanced Diet | バランスの取れた食事 | ja-JP |
| A cidade no fim do jogo | ゲームの果ての都市 | ja-JP |

ディレクトリ構成：

```text
ja-JP/
├── blocks.csv
├── items.csv
├── entities.csv
├── biomes.csv
├── enchantments.csv
├── effects.csv
├── instruments.csv
├── materials.csv
├── paintings.csv
├── attributes.csv
├── item-groups.csv
├── jukebox-songs.csv
├── trim-patterns.csv
├── colors.csv
├── statistics.csv
├── maps.csv
├── music.csv
├── sound-categories.csv
├── game-modes.csv
└── extra/  # システム系・テキスト系カテゴリ
    ├── subtitles.csv
    ├── death-messages.csv
    ├── advancement-titles.csv
    ├── advancement-descriptions.csv
    ├── gamerules.csv
    ├── commands.csv
    ├── gui.csv
    ├── options.csv
    ├── multiplayer.csv
    ├── realms.csv
    ├── world-management.csv
    ├── resource-packs.csv
    ├── telemetry.csv
    ├── dev-tools.csv
    └── misc.csv
```

## カテゴリと件数

「語数」は、そのカテゴリに分類された**公式言語ファイルの名称オブジェクト数**（言語ファイルのキー、本言語で未訳の項目を含む）です。どの言語ディレクトリでも同じ値になり、`tools/glossary_counts.json` から取得しており、34 カテゴリの合計は 8,559 `entries` です。「対照行数」は**このディレクトリ**のそのファイルに実際に入っているデータ行数です。両者は定義が異なるため混同しないでください。

### 主なカテゴリ（ゲーム内容）

| カテゴリ | テーマ | 語数 | 対照行数 |
| --- | --- | ---: | ---: |
| `blocks.csv` | ブロック | 1,975 | 25,426 |
| `items.csv` | アイテム | 803 | 9,092 |
| `entities.csv` | エンティティ | 219 | 2,582 |
| `biomes.csv` | バイオーム | 67 | 835 |
| `enchantments.csv` | エンチャント | 54 | 553 |
| `effects.csv` | ステータス効果 | 42 | 514 |
| `instruments.csv` | 楽器 | 8 | 98 |
| `materials.csv` | 装飾素材 | 11 | 143 |
| `paintings.csv` | 絵画 | 104 | 315 |
| `attributes.csv` | 属性 | 83 | 588 |
| `item-groups.csv` | アイテムグループ | 16 | 198 |
| `jukebox-songs.csv` | ジュークボックスの曲 | 22 | 42 |
| `trim-patterns.csv` | 装飾模様 | 18 | 234 |
| `colors.csv` | 色 | 16 | 184 |
| `statistics.csv` | 統計 | 88 | 1,143 |
| `maps.csv` | 地図 | 33 | 422 |
| `music.csv` | 音楽 | 70 | 192 |
| `sound-categories.csv` | サウンドカテゴリ | 11 | 133 |
| `game-modes.csv` | ゲームモード | 6 | 77 |
| **小計** | 19 ファイル | **3,646** | **42,771** |

### `extra/` のカテゴリ（システム・テキスト）

| カテゴリ | テーマ | 語数 | 対照行数 |
| --- | --- | ---: | ---: |
| `extra/subtitles.csv` | 字幕 | 1,023 | 12,528 |
| `extra/death-messages.csv` | 死亡メッセージ | 106 | 1,354 |
| `extra/advancement-titles.csv` | 進捗のタイトル | 127 | 1,603 |
| `extra/advancement-descriptions.csv` | 進捗の説明 | 127 | 1,650 |
| `extra/gamerules.csv` | ゲームルール | 117 | 1,490 |
| `extra/commands.csv` | コマンドと引数 | 856 | 10,743 |
| `extra/gui.csv` | インターフェース | 581 | 6,655 |
| `extra/options.csv` | 設定とキー | 754 | 8,162 |
| `extra/multiplayer.csv` | マルチプレイ | 173 | 2,015 |
| `extra/realms.csv` | Realms | 426 | 4,988 |
| `extra/world-management.csv` | ワールド管理 | 294 | 3,609 |
| `extra/resource-packs.csv` | リソースパックとデータパック | 62 | 761 |
| `extra/telemetry.csv` | テレメトリ | 70 | 897 |
| `extra/dev-tools.csv` | 開発・テストツール | 144 | 1,811 |
| `extra/misc.csv` | その他 | 53 | 516 |
| **小計** | 15 ファイル | **4,913** | **58,782** |

**本ディレクトリ合計：34 ファイル、`target` 列で重複除去した用語 7,826 語、対照 101,553 行。**

## 説明

- **訳文の出典と対応付け。** すべてのテキストは **Minecraft: Java Edition の公式言語ファイル**（[misode/mcmeta](https://github.com/misode/mcmeta) の `assets` ブランチ、`assets/minecraft/lang/<locale>.json`、本言語は `ja_jp.json`）に由来します。つまり**公式ローカライズ**であり、二次翻訳や機械翻訳ではありません。対応付けは言語ファイルのキー単位で行い、同じ用語を*他の*言語ごとに 1 行ずつ出力するため、行数は語数よりはるかに多くなります。
- **言語タグ。** このディレクトリの `tgt_lng` は常に `ja-JP`（対象言語）です。`source` は残り 13 言語のいずれかです：`zh-CN`、`zh-TW`、`en-US`、`ko-KR`、`fr-FR`、`de-DE`、`es-ES`、`ru-RU`、`pt-BR`、`it-IT`、`tr-TR`、`th-TH`、`vi-VN`。
- **文字コード。** CSV はすべて **UTF-8（BOM 付き）**、改行は **CRLF**、1 行目はヘッダー行で、カンマや引用符を含むフィールドは RFC 4180 に従ってエスケープしています。Excel でそのまま開けます。この README 自体は UTF-8（BOM なし）です。
- **既知の制限。** 言語ごとに行数がわずかに異なるのは、ある言語に訳が存在しない場合や、対象言語と同じ表記の場合にその用語を出力しないためです。対照行数と語数は同じものではありません。34 カテゴリの `entries` の合計は 8,559 で、これは公式言語ファイルのうち各カテゴリに分類された名称オブジェクトの数（本言語で未訳の項目を含む）です。本ディレクトリの `target` 列で重複除去した数は 7,826 で、定義が異なります。完全な定義はゲームルートの `../../README.md` の「データ概要」にあります。同じ表記が複数のカテゴリに現れることもあり、用語は公式ローカライズに従います（未訳の名称はそのまま保持されます）。
- **補助用語集。** 隣接する `../../minecraft-glossary-supplement/` には Minecraft Wiki の標準訳名（簡体字・繁体字中国語のみ）が入っており、本用語集と併用できます。
- **再生成。** ゲームのルートで `python tools/build_glossary.py` を実行すると、公式言語ファイルから本用語集を作り直せます（スクリプトは `mcmeta_lang/<locale>.json` を含む外部素材ディレクトリを読み、`minecraft-glossary/` に出力します）。`python tools/verify_output.py` は各行数を `tools/glossary_counts.json` と照合し、`python tools/make_readme.py` は各ライブラリの README を再生成します。

## 免責事項

本ディレクトリは個人が整理・維持している**非公式**の翻訳用語データベースであり、個人の学習・研究および AI 翻訳ソフト（Immersive Translate を含みますがこれに限りません）の用語一致の補助にのみ使用するものです。Minecraft の開発元、発行元、販売元、運営元、権利者との間に、従属・許諾・提携・代理・公式代表のいずれの関係もありません。収録されている訳語は公式の見解を示すものではなく、常に正確・完全であること、また現在のゲームバージョンと一致することを保証するものではなく、**いかなるゲームの公式用語集や公式ローカライズファイルと見なしてはなりません**。

ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はそれぞれの権利者に帰属し、本プロジェクトはそれらについて何ら権利を主張しません。本プロジェクトおよびそこから生成された翻訳の利用に起因する責任は、すべて利用者が負うものとします。権利者の方が内容を不適切とお考えの場合は、GitHub Issues / Pull Request でご連絡ください。確認のうえ修正または削除します。

完全な条項はリポジトリのルートにある `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元・発行元・販売元・権利者との間に、所属・許諾・提携・代理のいかなる関係もありません。**
