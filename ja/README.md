> [英語原文](../README.md)

<div align="center">

# Claude のための24の戦略スキル

**一般的なプロンプトのひな型ではなく、実際のマッキンゼーの実務構造に基づいて作られた、Claude 向けコンサルティングの仕事の仕組み。**

<!-- 原文の画像参照：<img src="../assets/overview.png" alt="24 Strategy Skills for Claude — overview" width="720"> -->

画像の参照先 `assets/overview.png` は、対象 commit の原文リポジトリに含まれていないため表示できない。参照情報は上の HTML コメントへ保持した。

</div>

Claude 向けの24の [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)。各スキルを1フォルダーに収め、それぞれに `SKILL.md`、定量的なスキルには付属の Python 計算ツールを置く。一般的な「診断 → 伝達」のひな型ではなく、マッキンゼーが実際に文書化した問題解決手法（問題の定義、MECE な論点ツリー、仮説の形成、優先順位付け、作業計画、分析、統合、伝達）と、実際の実務領域名を軸に構成されている。

**24スキル中13には、テスト済みの Python 計算ツールが付属する。** NPV／IRR、LTV:CAC、TAM／SAM／SOM、Van Westendorp の価格設定、管理範囲と階層、GE-McKinsey 9ボックス、意思決定ツリーの期待値、リスク採点、BATNA／ZOPA、RICE、シナジー NPV を扱う。数値中心のスキルは、方法を説明して計算を利用者に任せるのでなく、実際の答えを計算する。

**貢献を歓迎する。** 不足、計算ツールのバグ、追加したいスキルがあれば、[貢献](#contributing)を参照。

## スキルとは

スキルは、特定の作業について専門知識と再現可能な方法を Claude に与える Markdown ファイルである。Claude がアクセスできる場合、会話がスキルの `description` と一致すると判断し、その方法を自動的に適用する。名前で呼ぶ必要はないが、「`market-mapping` スキルを使ってこの機会の規模を測って」のように明示してもよい。

## スキル同士のつながり

`situation-assessment` と `assumption-audit` は、実際の案件の出発点になる。`full-potential-diagnostic` と `business-case-builder` は、意思決定の価値をドルで測る。`value-realization` は、このパックで唯一過去を振り返るスキルであり、予測を作るスキルの見込みと実際の結果を照合して、検証の循環を閉じる。

```
                    ┌───────────────────────────────────────┐
                    │         situation-assessment           │
                    │   (hypothesis tree + fact base first)  │
                    └───────────────────┬─────────────────────┘
                                        │
   ┌─────────────┬──────────────┬───────┼────────┬──────────────┬──────────────┐
   ▼             ▼              ▼       ▼        ▼              ▼              ▼
┌─────────┐ ┌──────────┐ ┌────────────┐ ┌──────────────┐ ┌───────────┐ ┌──────────────┐
│Problem  │ │Market &  │ │Strategy &  │ │Performance   │ │Risk &     │ │Communication │
│Def.     │ │Competitive│ │Corp Finance│ │Transformation│ │Value Cap. │ │& Change      │
├─────────┤ ├──────────┤ ├────────────┤ ├──────────────┤ ├───────────┤ ├──────────────┤
│growth-  │ │market-   │ │strategic-  │ │operating-    │ │war-gaming │ │stakeholder-  │
│ barriers│ │ mapping  │ │ options    │ │ model-design │ │risk-      │ │ alignment    │
│full-    │ │competitiv│ │pricing-    │ │spans-layers  │ │ mitigation│ │narrative-    │
│ potential│ │e-intel   │ │ strategy   │ │initiative-   │ │synergy-   │ │ builder      │
│         │ │customer- │ │business-   │ │ prioritizer  │ │ case      │ │decision-memo │
│         │ │ segment  │ │ case       │ │100-day-plan  │ │value-     │ │negotiation-  │
│         │ │unit-econ │ │capital-    │ │              │ │ realization│ │ prep         │
│         │ │          │ │ realloc    │ │              │ │(checks →) │ │              │
└─────────┘ └──────────┘ └─────┬──────┘ └──────┬───────┘ └─────┬─────┘ └──────────────┘
                               │               │                │
                               └───────────────┴────────────────┘
                     value-realization checks these three against actuals
```

**図の日本語補訳：** 最初に `situation-assessment` で仮説ツリーと事実の基盤を作る。その下に「問題定義」「市場・競争」「戦略・コーポレートファイナンス」「業績変革」「リスク・価値実現」「伝達・変化」の6領域がある。各箱内の識別子は下表のスキルを指す。`value-realization` は図の下部でつながる3領域の見込みを実績と照合する。図中の英語と識別子は原文どおり保持している。

## 利用できるスキル

| スキル | 説明 |
|---|---|
| [`100-day-plan`](skills/100-day-plan/SKILL.md) | 買収成立後・新任リーダーの実際の順序。傾聴・決定・開始を組み立て、短期間の成果を組み込む |
| [`assumption-audit`](skills/assumption-audit/SKILL.md) | 計画の成立を左右する重要前提を洗い出し、証拠の質を採点し、反証テストを設計する |
| [`business-case-builder`](skills/business-case-builder/SKILL.md) 🧮 | 実際の事業要因に基づく NPV／IRR／回収期間と、具体的な感度分析表 |
| [`capital-reallocation-review`](skills/capital-reallocation-review/SKILL.md) 🧮 | GE-McKinsey 9ボックス採点と、実際の資本再配分の度合いの測定 |
| [`competitive-intel`](skills/competitive-intel/SKILL.md) | 能力・動機・制約による競合モデルと、事前に決める対応 |
| [`customer-segmentation`](skills/customer-segmentation/SKILL.md) | Jobs-to-be-Done による顧客区分、魅力度 × 勝てる根拠の採点 |
| [`decision-memo`](skills/decision-memo/SKILL.md) | 明確な可否を引き出すよう設計した、ベゾス流の1ページ意思決定メモ |
| [`full-potential-diagnostic`](skills/full-potential-diagnostic/SKILL.md) 🧮 | 指標ごとに上位25%の基準との差分を、ドル換算した改善余地として測る |
| [`growth-barriers`](skills/growth-barriers/SKILL.md) | 制約理論によるファネル診断。実際に成長を制約する1つの要因を絞り込む |
| [`initiative-prioritizer`](skills/initiative-prioritizer/SKILL.md) 🧮 | RICE 採点に遅延コストによる実行順の確認を重ねる |
| [`market-mapping`](skills/market-mapping/SKILL.md) 🧮 | 推計を突き合わせた TAM／SAM／SOM。トップダウンとボトムアップの不一致を警告 |
| [`narrative-builder`](skills/narrative-builder/SKILL.md) | ピラミッド原則と、状況・問題の発生・解決による再構成 |
| [`negotiation-prep`](skills/negotiation-prep/SKILL.md) 🧮 | 実際の合意可能領域を求め、存在しない場合は警告 |
| [`operating-model-design`](skills/operating-model-design/SKILL.md) | RAPID／DACI による判断権限、7S の整合性、能力不足の確認 |
| [`pricing-strategy`](skills/pricing-strategy/SKILL.md) 🧮 | Van Westendorp の価格感応度と、弾力性による売上・利益モデル |
| [`risk-mitigation`](skills/risk-mitigation/SKILL.md) 🧮 | 発生可能性・影響度・顕在化速度による評価、軽減策のない重大リスクの警告 |
| [`situation-assessment`](skills/situation-assessment/SKILL.md) | 初日の MECE な仮説ツリーと作業計画、その後の3つの観点による事実の照合 |
| [`spans-layers-org-design`](skills/spans-layers-org-design/SKILL.md) 🧮 | 階層別の管理範囲を測り、過剰な管理階層の費用を算出 |
| [`stakeholder-alignment`](skills/stakeholder-alignment/SKILL.md) 🧮 | 影響力・関心度の表と、人数でなく影響力を足した連合の力関係 |
| [`strategic-options`](skills/strategic-options/SKILL.md) | 実質的に異なる案を求め、加重採点し、リアルオプションで段階化する |
| [`synergy-case-builder`](skills/synergy-case-builder/SKILL.md) 🧮 | 現実的な立ち上がり曲線と、売上シナジーの確信度に応じた減額を備えた M&A シナジー NPV |
| [`unit-economics-health-check`](skills/unit-economics-health-check/SKILL.md) 🧮 | 現実的に低下する解約曲線による LTV:CAC と CAC 回収期間 |
| [`value-realization`](skills/value-realization/SKILL.md) | 他スキルの予測と実際の結果を照合して、検証の循環を閉じる |
| [`war-gaming`](skills/war-gaming/SKILL.md) 🧮 | 意思決定ツリーの期待値。期待値最良とマキシミン最良の食い違いを警告 |

🧮 = `scripts/` に Python 計算ツールが付属する。

## スキルの分類

### 01 · 問題定義
解決策へ手を付ける前に。
`situation-assessment` · `growth-barriers` · `assumption-audit` · `full-potential-diagnostic`

### 02 · 市場・競争分析
実際に価値がある場所を見極める。
`market-mapping` · `competitive-intel` · `customer-segmentation` · `unit-economics-health-check`

### 03 · 戦略・コーポレートファイナンス
勝負をかける先と資本配分を決める。マッキンゼー自身の実務領域名。
`strategic-options` · `pricing-strategy` · `business-case-builder` · `capital-reallocation-review`

### 04 · 業績変革
戦略を実際の成果に変える。こちらも実際のマッキンゼーの実務領域名。
`operating-model-design` · `spans-layers-org-design` · `initiative-prioritizer` · `100-day-plan`

### 05 · リスク・価値実現
開始前と、その後に。
`war-gaming` · `risk-mitigation` · `synergy-case-builder` · `value-realization`

### 06 · 伝達・変化
会議の後も検討成果が生きるようにする。
`stakeholder-alignment` · `narrative-builder` · `decision-memo` · `negotiation-prep`

## 計算ツール

このパックの作成中、全計算ツールは具体的なテスト事例で実行された。各スキルの**例**の数値は、創作した説明用の数字ではなく実際の出力である。文章だけのスキルでは捉えられないものの例は次のとおり。

- `market-mapping/scripts/tam_sam_som.py` は、トップダウン・ボトムアップの市場規模推計が30%を超えて違うと警告する。
- `business-case-builder/scripts/npv_case.py` は、単一点でなく、売上 × 割引率の NPV 感度分析表全体を返す。
- `war-gaming/scripts/decision_tree_ev.py` は、期待値最大の案と、最悪ケースが最も安全な案が違うと警告する。
- `stakeholder-alignment/scripts/power_interest_grid.py` は、人数でなく影響力で連合の力関係を計算し、反対が支持を上回ると警告する。
- `negotiation-prep/scripts/batna_zopa.py` は、埋められない差について交渉を続けさせず、合意可能領域がないと明確に示す。

## インストール

### 選択肢1：Claude.ai／Claude Desktop

Settings → Skills → Add → Upload a skill（設定 → スキル → 追加 → スキルをアップロード）から、各スキルの `SKILL.md`、対応環境ならフォルダーを選ぶ。スキルごとに繰り返すか、24個すべてをアップロードする。

### 選択肢2：Claude Code — CLI でインストール

```bash
npx skills add Natan-Mohart/24-strategy-skills-for-claude
```

CLI への回答に応じ、`.claude/skills/`（プロジェクト用）または `~/.claude/skills/`（個人用）へ入る。Claude Code は次のセッションで `SKILL.md` を自動検出する。

### 選択肢3：Claude Code — clone してコピー

```bash
git clone https://github.com/Natan-Mohart/24-strategy-skills-for-claude.git
cp -r 24-strategy-skills-for-claude/skills/* ~/.claude/skills/
```

### 選択肢4：Fork してカスタマイズ

このリポジトリを Fork し、`SKILL.md` や `scripts/*.py` を自分の事業に合わせて編集し、上記のいずれかの方法で自分の Fork からインストールする。

## スキルの形式

各 `SKILL.md` は、**使用する場面 → 実行すること → 方法 → 入力 → 出力形式 → 例 → よくある落とし穴**という共通の構造を持つ。一般的な「アイデアを出す」という指示でなく、MECE、RAPID／DACI、制約理論、Van Westendorp、GE-McKinsey、RICE、Jobs-to-be-Done、リアルオプション、BATNA／ZOPA、管理範囲と階層など、名前のある枠組みに基づく。

## 作成した理由

Claude 向けの「戦略スキル」の多くは、文章のみのプロンプト枠組みと同じ題目の一覧で、同じ6段階のコンサルティングの流れをなぞる。このパックは次の点を備える。

- マッキンゼーが実際に文書化した仮説思考の方法と、実際の実務領域名を使う。
- 状況評価と仮説ツリー構築を、重複する2スキルでなく1つで行う。初日に仮説を置き、次にそれを検証する事実を集める。
- 一般的なパックが省きがちな、最大改善余地診断、最初の100日計画、M&A シナジー評価、管理範囲と階層による組織設計、ユニットエコノミクスの健全性確認、交渉準備を含む。
- 計算ツールがゼロではなく、テスト済みの Python 計算ツールを13個付属する。
- `value-realization` が、`business-case-builder`・`full-potential-diagnostic`・`synergy-case-builder` の予測を実際の結果と照合し、検証の循環を閉じる。

<a id="contributing"></a>

## 貢献

不足、計算ツールのバグ、他スキルとの重複を見つけたら、[CONTRIBUTING.md](CONTRIBUTING.md) を参照。

## ライセンス

[MIT](../LICENSE) — 利用・Fork・改変が可能。

---

<div align="center">

作者：**Natan Mohart** · Claude と AI 戦略の情報をさらに得たい方はフォローを

</div>
