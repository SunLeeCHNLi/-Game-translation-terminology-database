# 『鳴潮』（Wuthering Waves）多言語用語集

## [简体中文](README.md) [English](README_EN.md)

**対象言語**ごとに独立したフォルダへ分割し、各フォルダ内では**カテゴリ**ごとにファイルを分けて格納しています。

## データ出典

- テキストの主ソース：[Arikatsu/WutheringWaves_Data](https://github.com/Arikatsu/WutheringWaves_Data)（ゲーム 3.6.0）
  - `Textmaps/<lang>/multi_text/MultiText.json`：テキストキー（例：`RoleInfo_1402_Name`）で索引付けされた全言語テキスト表
- テキストの補完：[Dimbreath/WutheringData](https://github.com/Dimbreath/WutheringData)（ゲーム 3.1.0）
  - `TextMap/<lang>/MultiText.json`：3.6 版で削除された少数のテキストキーを補完
- カテゴリ分類：Arikatsu `BinData/` + Dimbreath `ConfigDB/` のフィールド参照（テキストキー → エンティティ表 → カテゴリ）
- 参考実装：[My-Denia/wuwa-translate-bot](https://github.com/My-Denia/wuwa-translate-bot)（カテゴリフィールドとテキストクリーニング）、[CM-Edelweiss/WutheringWavesUID](https://github.com/CM-Edelweiss/WutheringWavesUID)（語句の照合）

## ディレクトリ構造

```
wuwa-glossary/
├── zh-CN/                    # 対象言語 = 簡体字中国語
│   ├── characters.csv
│   ├── items.csv
│   └── ...                   # 計 23 個のカテゴリファイル
├── zh-TW/
├── en-US/ ... th-TH/         # 計 10 個の言語フォルダ
└── _counts.json              # 各言語・各カテゴリの件数統計
```

## ファイル形式

すべての CSV は **UTF-8（BOM 付き）** エンコード、**CRLF** 改行、先頭行はヘッダーで、フィールドにカンマや引用符が含まれる場合は RFC 4180 に従って引用符でエスケープしています。

| source | target | tgt_lng |
| --- | --- | --- |
| Yangyang | 秧秧 | zh-CN |
| 秧秧（ヤンヤン） | 秧秧 | zh-CN |

意味：`tgt_lng` で指定された対象言語において、`target` は訳文、`source` は**他のいずれかの言語**の原文です。
つまり各言語フォルダ内では、同じ項目が残りの 9 言語それぞれを `source` として 1 行ずつ出現します（重複行と同形行は統合済み）。

## 言語コード

| 言語フォルダ | 言語 | ゲームテキストディレクトリ |
| --- | --- | --- |
| `zh-CN` | 简体中文 | `Textmaps/zh-Hans/` |
| `zh-TW` | 繁體中文 | `Textmaps/zh-Hant/` |
| `en-US` | English | `Textmaps/en/` |
| `ja-JP` | 日本語 | `Textmaps/ja/` |
| `ko-KR` | 한국어 | `Textmaps/ko/` |
| `fr-FR` | Français | `Textmaps/fr/` |
| `de-DE` | Deutsch | `Textmaps/de/` |
| `es-ES` | Español | `Textmaps/es/` |
| `pt-BR` | Português | `Textmaps/pt/` |
| `th-TH` | ภาษาไทย | `Textmaps/th/` |

> **未収録の言語**：`ru-RU`（Русский）、`id-ID`（Bahasa Indonesia）、`vi-VN`（Tiếng Việt）は、上流の 2 つのデータリポジトリにおいて**空のプレースホルダーファイル**です（3.6.0 版と 3.1.0 版のいずれも同様）。そのため本用語集では提供できません。`it-IT`、`tr-TR` は鳴潮が公式にサポートするテキスト言語ではありません。
> 今後上流で補完された場合は、下記の「再生成」コマンドを実行すれば自動的に取り込まれます。

## カテゴリと件数

「件数」とはその分類で重複を除いた後の語句数（1 語句 = ゲーム内の 1 テキストキー）を指し、「行数」は **zh-CN** フォルダ内のそのカテゴリ CSV のデータ行数です。

| カテゴリ | ファイル | 説明 | 件数 | zh-CN 行数 |
| --- | --- | --- | --- | --- |
| キャラクター名 | `characters.csv` | キャラクター、漂泊者の身分、キャラクター資料フィールド | 1,230 | 5,181 |
| 武器名 | `weapons.csv` | 武器名と武器図鑑テキスト | 820 | 3,072 |
| 音骸 | `echoes.csv` | 音骸（残象）の名称、図鑑、音骸対戦テキスト | 1,000 | 6,091 |
| スキル | `skills.csv` | 共鳴スキル、スキル説明、スキルツリー | 5,344 | 30,340 |
| 共鳴チェーン | `resonant-chains.csv` | 共鳴チェーンノードの名称と説明 | 784 | 6,116 |
| クエスト | `quests.csv` | クエスト／チャプター名、クエスト説明、デイリー依頼 | 2,807 | 14,529 |
| ステージと挑戦 | `dungeons.csv` | 副本、深塔、ホログラム、挑戦ステージの名称と説明 | 1,910 | 12,157 |
| 地域とマップ | `regions.csv` | 地域、マップマーカー、地理図鑑 | 2,229 | 16,143 |
| 陣営と勢力 | `factions.csv` | 国家と陣営の名称 | 8 | 44 |
| アイテムと素材 | `items.csv` | アイテム、素材、合成／調理／鍛造レシピ、ショップ | 8,384 | 54,388 |
| モンスターと生物 | `monsters.csv` | モンスターと生物の図鑑 | 685 | 4,542 |
| NPC と話者 | `npcs.csv` | NPC と話者の名称 | 14,172 | 64,138 |
| 実績 | `achievements.csv` | 実績の名称と説明 | 2,563 | 22,173 |
| イベントと遊び方 | `activities.csv` | イベント、ローグライク、釣り、トラップディフェンスなどのテキスト | 9,531 | 63,487 |
| バフと効果 | `buffs.csv` | バフ／デバフ効果の名称と説明 | 270 | 2,034 |
| キャラクターボイス | `voice-lines.csv` | キャラクターのボイス台詞と絆ストーリー | 7,374 | 31,692 |
| アーカイブと読み物 | `archives.csv` | アーカイブ、読み物、調査記録 | 839 | 6,574 |
| 用語と百科 | `terms.csv` | ゲーム内用語集、属性と元素反応 | 1,672 | 12,387 |
| システムテキスト | `system.csv` | システム通知、エラーコード、確認ダイアログ、機能メニュー | 9,756 | 65,502 |
| UI テキスト | `ui.csv` | 画面用プリセットテキスト、ショートカットキー、動的タブ | 13,866 | 78,131 |
| チュートリアルとガイド | `tutorials.csv` | チュートリアル、ガイド、戦闘ヒント | 6,253 | 31,741 |
| ストーリーテキスト | `story.csv` | ストーリータイトル、クエスト目標、場景の語りテキスト | 29,841 | 102,144 |
| その他 | `other.csv` | 未分類テキスト | 1,892 | 13,340 |

## 言語別の総行数

| 言語 | ファイル数 | データ行数 | サイズ |
| --- | --- | --- | --- |
| `zh-CN` | 23 | 645,946 | 55.6 MiB |
| `zh-TW` | 23 | 645,529 | 55.7 MiB |
| `en-US` | 23 | 645,837 | 58.6 MiB |
| `ja-JP` | 23 | 648,414 | 63.4 MiB |
| `ko-KR` | 23 | 646,888 | 63.4 MiB |
| `fr-FR` | 23 | 654,776 | 63.8 MiB |
| `de-DE` | 23 | 652,349 | 63.0 MiB |
| `es-ES` | 23 | 646,691 | 61.8 MiB |
| `pt-BR` | 23 | 648,957 | 62.0 MiB |
| `th-TH` | 23 | 644,759 | 91.4 MiB |
| **合計** | **230** | **6,480,146** | **638.6 MiB** |

> 同じテキストが複数のカテゴリに同時に属することがあるため（例えばある武器の説明が `weapons` と `items` の両方に出現する）、各カテゴリの行数を合計すると全体の重複除去後の件数より多くなりますが、これは正常な現象です。

## データクリーニングの説明

元データの以下の内容は生成時に処理済みです：

| 元データの表記 | 処理 | 例 |
| --- | --- | --- |
| `<color=...>`、`<size=...>`、`<te href=...>`、`<i>`、`<b>` などのリッチテキストタグ | タグを除去 | `<color=Highlight>共鸣解放</color>` → `共鸣解放` |
| `{Male=…;Female=…}` の性別分岐 | 男性形を採用 | `{Male=大哥哥;Female=大姐姐}` → `大哥哥` |
| `{M#…}{F#…}` の性別変異 | 男性形を採用 | `{M#du débutant}{F#de la débutante}` → `du débutant` |
| リテラルの `\n` | 改行に復元 | `第一行\n第二行` → 2 行 |
| `dnt/` 接頭辞（do not translate） | 接頭辞を除去 | `dnt/测试` → `测试` |
| 原文と訳文が完全に同一の行 | 出力しない | — |

## 収録範囲の説明

- **既定では逐句のストーリー台詞を収録しません**（話者台詞・字幕、言語あたり約 17 万件）。収録すると 1 言語あたりのサイズが約 60 MiB から約 230 MiB に増えます。
  台詞ライブラリが必要な場合は実行してください：`python tools/build_wuwa_glossary.py --out <目录> --with-dialogue`（追加で `dialogue.csv` を生成します）。
- 長すぎるテキストはカテゴリごとの閾値で切り詰めます。閾値は `tools/wuwa_config.py` の `MAX_LEN` で定義しています（例：`ui` 60 文字、`story` 200 文字、`items` 250 文字、`archives` 400 文字）。
- テキストキーからカテゴリへの割り当ては、ゲーム設定テーブルのフィールド参照に基づきます。どの設定テーブルからも参照されない少数のキーは、命名規則によるフォールバックで分類します。

## 再生成

先に 2 つのデータリポジトリ（`WutheringWaves_Data`、`WutheringData`）を `E:\Download\BT\Codex_input` に準備するか、環境変数 `WUWA_DATA_ROOT` で別の場所を指定する必要があります。

```bash
# 全量生成（既定）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary

# 一部のカテゴリのみ生成（サイズがより小さく、マッチングがより正確）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --only characters,weapons,echoes,skills,resonant-chains

# 長文の閾値を圧縮（例えば短い語句のみ残す場合、サイズは既定の約 1/3）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --len-scale 0.5

# 逐句のストーリー台詞 dialogue.csv を追加生成（非常に大きく、言語あたり約 +170 MiB）
python tools/build_wuwa_glossary.py --out ./wuwa-glossary --with-dialogue
```

その他の引数：`--dry-run`（集計のみでファイルを書き込まない）、`--rebuild-cache`（`BinData`/`ConfigDB` を再スキャン。既定では結果を `tools/_cfgmap_cache.pkl` にキャッシュ）。

## 使用のヒント

- CAT ツール（Trados、memoQ、Phrase など）や没入型翻訳系ソフトウェアにインポートする際は、対応する対象言語の CSV を選んでそのまま用語集としてインポートするだけで済みます。
- ファイル名がカテゴリ名なので、必要に応じて統合できます。領域ごとに分割する（例えば `characters.csv` + `weapons.csv` + `skills.csv` のみをインポートする）と、マッチング精度が大幅に向上します。
