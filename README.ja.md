# 24 Strategy Skills — 日本語版の入口

[日本語の全体説明](ja/README.md) · [英語の全体説明](README.md) · [翻訳上の注記](localization/TRANSLATION-NOTES.ja.md)

24個の戦略・コンサルティング用 Agent Skills と、13個の標準ライブラリ中心の Python 計算ツールからなる第三者製の公開リポジトリ。マッキンゼー公式のプラグインや、公認の社内手法集ではない。原文は、仮説思考、MECE、制約理論、財務評価、組織設計、合意形成、意思決定メモなどの公開手法をまとめたものとして説明している。

## 実体と読む順番

各スキルの主な実体は、使う場面・実行すること・方法・入力・出力形式・例・落とし穴を記した `SKILL.md`。定量的な13スキルには `scripts/` があり、入力 JSON を使って計算する。任意の業務データへ勝手に接続するアプリではない。

- 現状の理解：`situation-assessment` → `assumption-audit` → `growth-barriers`
- 何をするかの判断：`strategic-options` → `business-case-builder` → `initiative-prioritizer`
- 実行と説明：`operating-model-design` → `stakeholder-alignment` → `decision-memo`／`narrative-builder`
- 結果の振り返り：`value-realization`

これは用途を理解するための読み順で、原文の方法を3か月用へ改変したものではない。特に `100-day-plan` は新任リーダー・買収後統合の最初の100日を扱う。

## 翻訳範囲と保存方針

原文：`Natan-Mohart/24-strategy-skills-for-claude`、commit `f6825ba48543d52ce6a103af4109849e94d19a65`。

- README、CONTRIBUTING、24個の SKILL.md の計26文書を、原文と対応する `ja/` 以下へ全文翻訳。
- 原文ファイル・コードフェンス・YAML frontmatter・識別子を保持。各スキルの英語 description には全文の日本語補訳を併記。
- 13個の Python は原文とバイト一致のものを日本語側へ複製。プログラム内の英文は [コード・フェンスの日本語参考訳](localization/CODE-AND-FENCE-NOTES.ja.md) を参照。
- [MIT ライセンス原文](LICENSE)を保持し、[日本語参考訳](ja/LICENSE.md)を添付。権利表示の原文を変更していない。
- README のテキスト図は原文のまま保持し、日本語説明を追加。冒頭で参照される `assets/overview.png` は対象 commit に存在しないため、画像参照をコメントへ保持して欠落を明記。画像の捏造・描き直しはしていない。

日本語本文は機械翻訳初稿の後、AI が原文全文と照合して書き直した。否定・数値・条件・手順は照合したが、独立した専門家校閲、金融モデルの実務保証、外部一次資料の検証は含まない。原文の数値不整合などは勝手に修正せず、[翻訳上の注記](localization/TRANSLATION-NOTES.ja.md)に記した。コード内英文の参考訳は別資料として扱う。

インストール・コード実行・自動有効化は行っていない。`ja/README.md` 内のコマンドは原文の説明を保持しており、そのまま実行すると upstream の英語版を対象とする。

## 収録・確認の記録

[全ファイルの対応と確認範囲](localization/VALIDATION.ja.md) · [原本・訳文のハッシュ対応表](localization/source-manifest.json) · [コード内説明の全文照合](localization/CODE-REVIEW.ja.md)

原文のファイル構成と実行内容を保ち、補訳は読解用の別資料として保存しています。
