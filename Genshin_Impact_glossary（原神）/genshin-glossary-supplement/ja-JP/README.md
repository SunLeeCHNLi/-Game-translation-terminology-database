# 原神 用語集（補完辞書） — 日本語（`ja-JP`）

[← ゲーム全体の説明に戻る](../../README.md) · [简体中文](README_zh-CN.md)

このディレクトリは、*原神* の用語集のうち**日本語（`ja-JP`）を対象言語とする補完辞書**です。本体の `genshin-glossary/` には 27 カテゴリ合計で **8,186 語**が収録されており、本補完辞書はそこに**含まれない語だけ**を追加します。日本語は**13,308 行の対照行**、さらに別名 `_variants.csv` が **283 行**です。`tgt_lng` 列は常に `ja-JP` で、各行の `source` は同じ語の**残り 3 言語（`zh-CN`、`zh-TW`、`en-US`）のいずれか**での表記、`target` は日本語の訳語です。

## 本体辞書との関係

- 本体辞書に**存在しない** `source/target/tgt_lng` の組み合わせだけを収録しているため、`genshin-glossary/ja-JP/` とそのまま**重ねて使用**でき、重複項目は生じません。
- 上流データが本体辞書と異なるため（「注記」参照）、同じ語でも用語や句読点などの細かな表記が本体辞書と異なる場合があります。
- 本補完辞書が対象とする言語は `zh-CN`、`zh-TW`、`en-US`、`ja-JP` の 4 言語、本体辞書は 14 言語です。

## ファイル

- 主要カテゴリ（本体辞書と同名の 9 ファイル）: `characters.csv`、`materials.csv`、`geographies.csv`、`enemies.csv`、`foods.csv`、`animals.csv`、`domains.csv`、`artifacts.csv`、`weapons.csv`
- 別名ファイル: `_variants.csv` — 別名・通称・よくある誤記を追加の `source` として収録
- 追加カテゴリ（`extra/` 内の 10 ファイル）: `extra/quests.csv`、`extra/events.csv`、`extra/objects.csv`、`extra/system.csv`、`extra/archives.csv`、`extra/story.csv`、`extra/facilities.csv`、`extra/organizations.csv`、`extra/dialogue.csv`、`extra/sereniteapot.csv`

合計 **20 個の CSV ファイル**（主要 9 + 別名 1 + 追加 10）。形式はすべて同じ 3 列です。

| source | target | tgt_lng |
| --- | --- | --- |
| Astral Vulture's Crimson Plumage | 星鷹の紅き羽 | ja-JP |
| Blackmarrow Lantern | 鳥髄の狐灯 | ja-JP |

ディレクトリ構成:

```text
ja-JP/
├── characters.csv
├── materials.csv
├── geographies.csv
├── enemies.csv
├── foods.csv
├── animals.csv
├── domains.csv
├── artifacts.csv
├── weapons.csv
├── _variants.csv
└── extra/
    ├── quests.csv
    ├── events.csv
    ├── objects.csv
    ├── system.csv
    ├── archives.csv
    ├── story.csv
    ├── facilities.csv
    ├── organizations.csv
    ├── dialogue.csv
    └── sereniteapot.csv
```

## カテゴリと件数

各カテゴリは上流データの**1 つの元テーブル**に対応するため、「テーマ」列にそのファイルの語がどこ由来かを示します。数値はすべてこのディレクトリのファイルの実データ行数です。

### 主要カテゴリ（本体辞書の同名カテゴリに対応）

| カテゴリ | ファイル | テーマ（上流ソース） | 行数 |
| --- | --- | --- | ---: |
| characters | `characters.csv` | characters-*（モンド／璃月／稲妻／スメール／フォンテーヌ／ナタ／ナド・クライ／スネージナヤ／カーンルイア／ファデュイなど） | 4,221 |
| materials | `materials.csv` | items / drops / drops-boss / gemstones / specialties / talent-materials / weapon-materials | 789 |
| geographies | `geographies.csv` | locations | 1,163 |
| enemies | `enemies.csv` | enemies | 697 |
| foods | `foods.csv` | foods | 246 |
| animals | `animals.csv` | living-beings | 175 |
| domains | `domains.csv` | domains | 226 |
| artifacts | `artifacts.csv` | artifacts | 32 |
| weapons | `weapons.csv` | weapons | 69 |
| **小計** | 9 ファイル | — | **7,618** |

### 別名（`_variants.csv`）

| ファイル | 説明 | 行数 |
| --- | --- | ---: |
| `_variants.csv` | 別名・通称・よくある誤記を追加の `source` として収録 | 283 |

### 追加カテゴリ（`extra/`）

| カテゴリ | ファイル | 説明 | 行数 |
| --- | --- | --- | ---: |
| quests | `extra/quests.csv` | 任務名（魔神／世界／伝説／デイリー／部族など） | 1,753 |
| events | `extra/events.csv` | イベント名 | 1,796 |
| objects | `extra/objects.csv` | 場景オブジェクト | 472 |
| system | `extra/system.csv` | システム・遊び方の用語 | 387 |
| archives | `extra/archives.csv` | 書庫・資料 | 382 |
| story | `extra/story.csv` | ストーリーと章 | 302 |
| facilities | `extra/facilities.csv` | 施設と建物 | 236 |
| organizations | `extra/organizations.csv` | 組織と勢力 | 209 |
| dialogue | `extra/dialogue.csv` | 会話表現 | 121 |
| sereniteapot | `extra/sereniteapot.csv` | 塵歌壺 | 32 |
| **小計** | 10 ファイル | — | **5,690** |

**このディレクトリの合計: 20 ファイル、13,308 行（別名 283 行を含む）。**

## 注記

- **訳語の出典と対応付け** データは [xicri/genshin-langdata](https://github.com/xicri/genshin-langdata) に由来し、**ゲーム公式のローカライズ文本**をコミュニティがまとめたものです。再翻訳や機械生成ではありません。対応付けは語単位で、`target` が対象言語の訳語、`source` が他言語での表記です。生成時に本体辞書に存在する組み合わせは除外しているため、本体辞書と重ねて使えます。
- **言語タグ** 本ディレクトリの `tgt_lng` は常に `ja-JP` で対象言語を示します。`source` は `zh-CN`、`zh-TW`、`en-US` のいずれかです。
- **文字コード** すべての CSV は **UTF-8 with BOM**、改行は **CRLF**、1 行目はヘッダーです。カンマや引用符を含むフィールドは RFC 4180 に従ってエスケープされています（例: `"""Big Sis"""`）。Excel でそのまま開けます。
- **既知の制限** ファイルは上流の元テーブル単位で分割されているため、カテゴリの範囲は本体辞書と一対一には対応しません。`characters.csv` が最も大きいのは、NPC や登場人物を含むためです。英語・日本語・中国語の表記が本体辞書とわずかに異なる場合がありますが、これは想定内です。
- **語数と行数について** 本ライブラリは行数とは別の「重複除去後の語数」を公開していないため、本ページには実データ行数のみを記載し、推計値は載せていません。

## 免責事項

このディレクトリは個人が作成・保守する**非公式**の翻訳用語データベースであり、個人の学習・研究、および AI 翻訳ソフト（Immersive Translate を含みますがこれに限りません）の用語マッチングを補助する目的にのみ使用されます。関連するゲームの開発元、発行元、販売元、運営元、権利者との間に、従属・許諾・提携・代理・公式代表のいかなる関係もありません。ここに収録された訳語は公式の見解ではなく、常に正確・完全であること、またゲームの現行版本と一致することは保証されません。**いかなるゲームの公式用語集や公式ローカライズファイルとして扱うべきものではありません。** ゲーム名、キャラクター名、固有名詞、商標などの知的財産権はそれぞれの権利者に帰属します。利用によって生じたいかなる責任も利用者が負うものとします。

完全な条項はリポジトリ直下の `README.md` / `README_EN.md` / `README_JP.md` をご覧ください。

---

**Game-translation-terminology-database は独立した個人プロジェクトであり、本ゲームおよびその開発元・発行元・販売元・権利者との間に、従属・許諾・提携・代理のいかなる関係もありません。**
