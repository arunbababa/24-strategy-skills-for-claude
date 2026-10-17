# コード・図・設定例の自然言語補訳

実行コード・設定値は原文どおりに保持しています。この付録はソースコード内のコメント・説明文字列・Markdown内の図やコード例にある自然言語の参考訳です。機械翻訳初稿であり、コードの動作を変更するものではありません。識別子、式、プレースホルダーは原文と照合してください。

## skills/business-case-builder/scripts/npv_case.py

[原文](../skills/business-case-builder/scripts/npv_case.py)


### skills/business-case-builder/scripts/npv_case.py:2

原文：

```text

Driver-based business case: NPV, IRR, payback, and a sensitivity table.

Usage:
    python3 npv_case.py --config case.json

case.json shape:
{
  "discount_rate_pct": 10,
  "initial_investment": 2000000,
  "years": [
    {"revenue": 800000, "cogs_pct": 40, "opex": 300000},
    {"revenue": 1800000, "cogs_pct": 38, "opex": 400000},
    {"revenue": 3200000, "cogs_pct": 35, "opex": 550000},
    {"revenue": 4500000, "cogs_pct": 33, "opex": 700000},
    {"revenue": 5600000, "cogs_pct": 32, "opex": 800000}
  ],
  "sensitivity": {
    "revenue_swing_pct": [-20, -10, 0, 10, 20],
    "discount_rate_swing_pts": [-2, -1, 0, 1, 2]
  }
}

Prints annual cash flows, NPV, IRR (bisection method, no numpy dependency),
payback period, and a revenue x discount-rate NPV sensitivity grid — the
part most hand-built "business cases" skip because it's tedious by hand.

```

日本語：


ドライバーベースのビジネス ケース: NPV、IRR、ペイバック、感度テーブル。

使用法:
python3 npv_case.py --config case.json

case.json の形状:
{
"discount_rate_pct": 10、
"initial_investment": 2000000,
「年」: [
{"収益": 800000, "cogs_pct": 40, "opex": 300000},
{"収益": 1800000、"cogs_pct": 38、"opex": 400000},
{"収益": 3200000、"cogs_pct": 35、"opex": 550000},
{"収益": 4500000、"cogs_pct": 33、"opex": 700000}、
{"収益": 5600000、"cogs_pct": 32、"opex": 800000}
  ],
「感度」: {
"revenue_swing_pct": [-20, -10, 0, 10, 20],
"discount_rate_swing_pts": [-2, -1, 0, 1, 2]
  }
}

年間キャッシュ フロー、NPV、IRR (二分法、numpy 依存関係なし) を出力します。
回収期間、および収益 x 割引率 NPV 感応度グリッド -
手作業で作成する「ビジネス ケース」のほとんどは、手作業では面倒なのでスキップします。


### skills/business-case-builder/scripts/npv_case.py:53

原文：

```text
no sign change in range -> no IRR found
```

日本語：

範囲内で符号の変化なし -> IRR が見つかりません


### skills/business-case-builder/scripts/npv_case.py:76

原文：

```text
never pays back within modeled years
```

日本語：

モデル年以内に返済できない


### skills/business-case-builder/scripts/npv_case.py:95

原文：

```text
=== Business Case: Base Case ===

```

日本語：

=== ビジネスケース: 基本ケース ===


### skills/business-case-builder/scripts/npv_case.py:96

原文：

```text
Year 0:
```

日本語：

0年目:


### skills/business-case-builder/scripts/npv_case.py:99

原文：

```text

Discount rate: 
```

日本語：


割引率:


### skills/business-case-builder/scripts/npv_case.py:101

原文：

```text
IRR: not found in range (check sign of cash flows)
```

日本語：

IRR: 範囲内に見つかりません (キャッシュ フローの兆候を確認してください)


### skills/business-case-builder/scripts/npv_case.py:102

原文：

```text
Payback: does not pay back within modeled years
```

日本語：

回収: モデル年内に回収されない


### skills/business-case-builder/scripts/npv_case.py:106

原文：

```text

=== NPV Sensitivity Grid ===
```

日本語：


=== NPV 感度グリッド ===


### skills/business-case-builder/scripts/npv_case.py:109

原文：

```text
Revenue \ Rate
```

日本語：

収益\レート


### skills/business-case-builder/scripts/npv_case.py:121

原文：

```text

Read: rows = revenue vs. plan, columns = discount rate vs. base.
```

日本語：


読み取り: 行 = 収益対計画、列 = 割引率対ベース。


### skills/business-case-builder/scripts/npv_case.py:122

原文：

```text
Use this to name the conditions under which the case still holds.
```

日本語：

これを使用して、ケースが依然として成立する条件に名前を付けます。

## skills/capital-reallocation-review/scripts/portfolio_matrix.py

[原文](../skills/capital-reallocation-review/scripts/portfolio_matrix.py)


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:2

原文：

```text

GE-McKinsey 9-box portfolio matrix (industry attractiveness x competitive
strength) — a strict upgrade on the old 2-factor BCG matrix, which collapses
"attractiveness" to growth rate alone and "strength" to relative share alone.

Usage:
    python3 portfolio_matrix.py --config portfolio.json

portfolio.json shape:
{
  "attractiveness_weights": {"market_growth": 0.3, "market_size": 0.2, "profitability": 0.3, "competitive_intensity_inverse": 0.2},
  "strength_weights": {"relative_share": 0.3, "margin_vs_peers": 0.3, "brand_strength": 0.2, "capability_fit": 0.2},
  "business_units": [
    {
      "name": "Core Product",
      "revenue": 40000000,
      "attractiveness_scores": {"market_growth": 6, "market_size": 8, "profitability": 7, "competitive_intensity_inverse": 5},
      "strength_scores": {"relative_share": 8, "margin_vs_peers": 7, "brand_strength": 8, "capability_fit": 9}
    }
  ]
}
Scores are 1-10 per factor. Weights within each axis should sum to 1.0.

```

日本語：


GE-マッキンゼーの9ボックスポートフォリオマトリックス（業界の魅力×競争力）
強度) — 崩壊した古い 2 要素 BCG マトリックスの厳密なアップグレード
「魅力」は成長率のみ、「強さ」は相対シェアのみ。

使用法:
python3 ポートフォリオ_マトリックス.py --config ポートフォリオ.json

ポートフォリオ.json の形状:
{
"attractiveness_weights": {"market_growth": 0.3, "market_size": 0.2, "収益性": 0.3, "competitive_intensity_inverse": 0.2},
"strength_weights": {"relative_share": 0.3, "margin_vs_peers": 0.3, "brand_strength": 0.2, "capability_fit": 0.2},
"business_units": [
    {
"名前": "コア製品",
「収益」: 40000000、
"attractiveness_scores": {"market_growth": 6, "market_size": 8, "収益性": 7, "competitive_intensity_inverse": 5},
"strength_scores": {"relative_share": 8、"margin_vs_peers": 7、"brand_strength": 8、"capability_fit": 9}
    }
  ]
}
スコアは要素ごとに 1 ～ 10 です。各軸内の重みの合計は 1.0 になる必要があります。


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:34

原文：

```text
scores are on a 1-10 scale
```

日本語：

スコアは 1 ～ 10 のスケールで表示されます


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:42

原文：

```text
SELECTIVE (build strength or exit)
```

日本語：

SELECTIVE (強化または終了)


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:43

原文：

```text
SELECTIVE (hold, fund selectively)
```

日本語：

SELECTIVE (ホールド、選択的に資金を供給)


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:44

原文：

```text
SELECTIVE (harvest strength, low growth)
```

日本語：

選択的 (収穫強さ、低成長)


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:63

原文：

```text
=== GE-McKinsey 9-Box Portfolio Review ===

```

日本語：

=== GE-マッキンゼー 9 ボックス ポートフォリオのレビュー ===


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:64

原文：

```text
Business Unit
```

日本語：

ビジネスユニット


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:64

原文：

```text
Rev Share
```

日本語：

売上シェア


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:75

原文：

```text

=== Portfolio-Level Read ===
```

日本語：


=== ポートフォリオレベルの読み取り ===


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:80

原文：

```text
Revenue in INVEST/GROW zone: 
```

日本語：

INVEST/GROWゾーンの収益:


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:81

原文：

```text
Revenue in HARVEST/DIVEST zone: 
```

日本語：

HARVEST/DIVEST ゾーンの収益:


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:83

原文：

```text
>>> FLAG: over 40% of revenue sits in harvest/divest zones.
```

日本語：

>>> FLAG: 収益の 40% 以上が収穫/売却ゾーンにあります。


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:84

原文：

```text
    The portfolio is over-weighted toward declining positions —
```

日本語：

ポートフォリオはポジション減少に偏りすぎています —


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:85

原文：

```text
    capital reallocation toward the invest zone should be a priority.
```

日本語：

投資ゾーンへの資本の再配分が優先されるべきである。

## skills/full-potential-diagnostic/scripts/full_potential_calc.py

[原文](../skills/full-potential-diagnostic/scripts/full_potential_calc.py)


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:2

原文：

```text

Full-Potential Diagnostic calculator: sizes the $ value at stake between
current performance and a top-quartile/best-practice benchmark, metric by
metric, then rolls it into a single "value at stake" number — the core
tool behind McKinsey's "full potential" transformation framing.

Usage:
    python3 full_potential_calc.py --config metrics.json

metrics.json shape:
{
  "revenue_base": 120000000,
  "metrics": [
    {
      "name": "Gross margin %",
      "current_value": 38,
      "benchmark_value": 46,
      "unit": "pct_of_revenue",
      "direction": "higher_is_better"
    },
    {
      "name": "SG&A as % of revenue",
      "current_value": 22,
      "benchmark_value": 16,
      "unit": "pct_of_revenue",
      "direction": "lower_is_better"
    },
    {
      "name": "Inventory turns",
      "current_value": 4.2,
      "benchmark_value": 6.5,
      "unit": "turns",
      "working_capital_base": 18000000,
      "direction": "higher_is_better"
    }
  ]
}
For pct_of_revenue metrics, value at stake = |benchmark - current| % x revenue_base.
For "turns" metrics with a working_capital_base, value at stake is approximated as
the working capital freed by moving current turns to benchmark turns.

```

日本語：


全可能性診断計算機: 問題となる $ 値のサイズを以下の範囲に設定します。
現在のパフォーマンスと上位 4 分の 1/ベストプラクティスのベンチマーク、指標別
メトリクスを取得し、それを単一の「問題の価値」の数値、つまりコアにロールします。
マッキンゼーの「可能性を最大限に発揮する」変革の枠組みを支えるツール。

使用法:
python3 full_potential_calc.py --config metrics.json

metrics.json の形状:
{
"収益ベース": 120000000、
「メトリクス」: [
    {
"名前": "粗利益率 %",
"現在の値": 38、
「ベンチマーク値」: 46、
"単位": "収益の割合",
"方向": "高いほど良い"
    },
    {
"name": "収益に占める販管費の割合",
"現在の値": 22、
「ベンチマーク値」: 16、
"単位": "収益の割合",
"方向": "低い方が良い"
    },
    {
"name": "在庫回転数",
「現在の値」: 4.2、
「ベンチマーク値」: 6.5、
"単位": "ターン",
"working_capital_base": 18000000、
"方向": "高いほど良い"
    }
  ]
}
pct_of_revenue メトリクスの場合、賭けられる価値 = |benchmark - current| % x 収益ベース。
working_capital_base の「ターン」メトリクスの場合、問題となる価値は次のように近似されます。
現在のターンをベンチマークターンに移動することで解放された運転資本。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:61

原文：

```text
=== Full-Potential Diagnostic: Value at Stake ===

```

日本語：

=== 全可能性診断: 危機に瀕する価値 ===


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:62

原文：

```text
Revenue base: 
```

日本語：

収益ベース:


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:63

原文：

```text
Value at Stake
```

日本語：

危機に瀕する価値


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:75

原文：

```text
working capital roughly scales inversely with turns
```

日本語：

運転資本は回転数にほぼ反比例して増加します


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:86

原文：

```text
TOTAL VALUE AT STAKE
```

日本語：

賭けられる総額


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:87

原文：

```text

As % of revenue base: 
```

日本語：


収益ベースの割合として:


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:88

原文：

```text

Note: this is the theoretical gap to benchmark, not a capture plan.
```

日本語：


注: これはベンチマークに対する理論上のギャップであり、キャプチャ プランではありません。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:89

原文：

```text
Typical full-potential programs capture 40-70% of the identified gap
```

日本語：

典型的なフルポテンシャルプログラムは、特定されたギャップの 40 ～ 70% を捕らえます


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:90

原文：

```text
within the first 18-24 months — use this number to size ambition, not
```

日本語：

最初の 18 ～ 24 か月以内 — この数字は野心の大きさを決めるのに使用します。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:91

原文：

```text
as a guaranteed outcome. Pair with initiative-prioritizer to sequence
```

日本語：

保証された結果として。イニシアチブ優先順位付け機能と組み合わせて順序付けする


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:92

原文：

```text
which gaps to close first.
```

日本語：

どのギャップを最初に埋めるか。

## skills/initiative-prioritizer/scripts/rice_prioritizer.py

[原文](../skills/initiative-prioritizer/scripts/rice_prioritizer.py)


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:2

原文：

```text

RICE prioritization (Reach x Impact x Confidence / Effort) plus a
cost-of-delay overlay, since RICE alone ignores urgency/sequencing.

Usage:
    python3 rice_prioritizer.py --config initiatives.json

initiatives.json shape:
{
  "initiatives": [
    {
      "name": "Onboarding redesign",
      "reach": 8000,
      "impact": 2,
      "confidence_pct": 80,
      "effort_person_weeks": 6,
      "monthly_value_if_delayed": 15000
    }
  ]
}
impact scale: 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal (standard RICE scale)

```

日本語：


RICE の優先順位付け (リーチ x インパクト x 信頼性 / 労力) に加えて、
RICE だけでは緊急性/順序性が無視されるため、遅延コストのオーバーレイ。

使用法:
python3 Rice_prioritizer.py --config 取り組み.json

イニシアチブ.json の形状:
{
「イニシアチブ」: [
    {
"name": "オンボーディングの再設計",
「リーチ」: 8000、
「インパクト」：2、
"confidence_pct": 80、
"effort_person_weeks": 6、
「遅延の場合の月間値」: 15000
    }
  ]
}
影響スケール: 3=大規模、2=高、1=中、0.5=低、0.25=最小 (標準 RICE スケール)


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:39

原文：

```text
cost of a 3-month delay, a common sequencing lens
```

日本語：

一般的なシーケンス レンズの 3 か月の遅延のコスト


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:44

原文：

```text
=== RICE Prioritization ===

```

日本語：

=== RICEの優先順位付け ===


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:45

原文：

```text
CoD 3mo
```

日本語：

CoD 3mo


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:50

原文：

```text

RICE ranks by expected impact per unit of effort — it does NOT account
```

日本語：


RICE は、単位努力当たりの予想される影響によってランク付けされます。これは考慮されていません。


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:51

原文：

```text
for urgency. Cross-check: an initiative with a lower RICE score but a high
```

日本語：

緊急のため。クロスチェック: RICE スコアは低いが高い取り組み


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:52

原文：

```text
cost of delay (e.g., a closing market window, a compliance deadline) may
```

日本語：

遅延コスト（市場窓口の閉鎖、遵守期限など）が発生する可能性があります。


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:53

原文：

```text
still need to be sequenced earlier. Don't apply the RICE rank mechanically
```

日本語：

まだ早い段階で順序付けする必要があります。 RICEランクを機械的に適用しないでください


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:54

原文：

```text
without checking the CoD column against the calendar.
```

日本語：

CoD 列をカレンダーと照合せずに。


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:62

原文：

```text

>>> FLAG: '
```

日本語：


>>> フラグ: '


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:62

原文：

```text
' has the highest cost of delay but is not
```

日本語：

' は遅延コストが最も高くなりますが、そうではありません


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:63

原文：

```text
    the top RICE-ranked item ('
```

日本語：

RICEランキング1位の商品('


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:63

原文：

```text
' is). Confirm the
```

日本語：

』です）。確認してください


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:64

原文：

```text
    sequencing call explicitly rather than defaulting to RICE order.
```

日本語：

デフォルトの RICE 順序ではなく、明示的に呼び出しをシーケンスします。

## skills/market-mapping/scripts/tam_sam_som.py

[原文](../skills/market-mapping/scripts/tam_sam_som.py)


### skills/market-mapping/scripts/tam_sam_som.py:2

原文：

```text

Triangulated market sizing (TAM/SAM/SOM) with top-down vs. bottom-up cross-check.

Usage:
    python3 tam_sam_som.py --config market.json

market.json shape:
{
  "top_down": {"total_population": 5000000, "target_share_pct": 12, "avg_annual_spend": 4800},
  "bottom_up": {"units_or_customers": 45000, "avg_annual_revenue_per_customer": 6200},
  "serviceable_filters": {"pct_geography": 70, "pct_segment_fit": 55, "pct_regulatory_eligible": 90},
  "obtainable": {"realistic_share_of_sam_pct": 8, "years_to_reach": 3}
}

Prints TAM (two independent estimates + variance), SAM, SOM, and flags if the
top-down and bottom-up TAM estimates disagree by more than 30% (a signal the
inputs need to be revisited before anyone puts the number in a deck).

```

日本語：


トップダウンとボトムアップのクロスチェックによる、三角形の市場サイジング (TAM/SAM/SOM)。

使用法:
python3 tam_sam_som.py --config マーケット.json

Market.json の形状:
{
"top_down": {"total_population": 5000000, "target_share_pct": 12, "avg_annual_spend": 4800},
"bottom_up": {"units_or_customers": 45000, "avg_annual_revenue_per_customer": 6200},
"serviceable_filters": {"pct_geography": 70, "pct_segment_fit": 55, "pct_regulatory_eligible": 90},
"取得可能": {"realistic_share_of_sam_pct": 8, "years_to_reach": 3}
}

TAM (2 つの独立した推定値 + 分散)、SAM、SOM、およびフラグがある場合はフラグを出力します。
トップダウンとボトムアップの TAM 推定値は 30% 以上不一致です (
誰かが数字をデッキに入れる前に、入力を再検討する必要があります)。


### skills/market-mapping/scripts/tam_sam_som.py:54

原文：

```text
=== Market Sizing: TAM / SAM / SOM ===

```

日本語：

=== 市場規模: TAM / SAM / SOM ===


### skills/market-mapping/scripts/tam_sam_som.py:55

原文：

```text
TAM (top-down):    
```

日本語：

TAM (トップダウン):


### skills/market-mapping/scripts/tam_sam_som.py:56

原文：

```text
TAM (bottom-up):   
```

日本語：

TAM (ボトムアップ):


### skills/market-mapping/scripts/tam_sam_som.py:59

原文：

```text
  >>> FLAG: top-down and bottom-up disagree by more than 30%.
```

日本語：

>>> フラグ: トップダウンとボトムアップの意見は 30% 以上一致しません。


### skills/market-mapping/scripts/tam_sam_som.py:60

原文：

```text
      Do not present a single TAM number yet — the two methods are
```

日本語：

まだ単一の TAM 番号を提示しないでください。次の 2 つの方法があります。


### skills/market-mapping/scripts/tam_sam_som.py:61

原文：

```text
      built on inconsistent assumptions about population, spend, or
```

日本語：

人口、支出、または支出に関する一貫性のない仮定に基づいて構築されている


### skills/market-mapping/scripts/tam_sam_som.py:62

原文：

```text
      fit. Reconcile the inputs before this goes in a deck.
```

日本語：

フィットします。これをデッキに組み込む前に入力を調整します。


### skills/market-mapping/scripts/tam_sam_som.py:63

原文：

```text
TAM (reconciled, avg): 
```

日本語：

TAM (調整済み、平均):


### skills/market-mapping/scripts/tam_sam_som.py:65

原文：

```text
SAM (after serviceability filters 
```

日本語：

SAM (保守性フィルタ後)


### skills/market-mapping/scripts/tam_sam_som.py:68

原文：

```text
% share of SAM over 
```

日本語：

SAM の割合 (%)


### skills/market-mapping/scripts/tam_sam_som.py:68

原文：

```text
SOM (realistic 
```

日本語：

SOM (現実的な


### skills/market-mapping/scripts/tam_sam_som.py:70

原文：

```text
  Implied annual run-rate to reach SOM: 
```

日本語：

SOM に達するための暗黙の年間実行率:

## skills/negotiation-prep/scripts/batna_zopa.py

[原文](../skills/negotiation-prep/scripts/batna_zopa.py)


### skills/negotiation-prep/scripts/batna_zopa.py:2

原文：

```text

BATNA / ZOPA calculator: computes the zone of possible agreement between
your reservation price and the counterparty's estimated reservation price,
recommends an anchor, and flags when no ZOPA exists (in which case the
right move is walking away or changing the deal structure, not negotiating
harder on price).

Usage:
    python3 batna_zopa.py --config negotiation.json

negotiation.json shape:
{
  "role": "buyer",
  "your_target_price": 400000,
  "your_batna_value": 480000,
  "counterparty_estimated_reservation_price": 460000,
  "counterparty_estimated_target_price": 420000
}
role: "buyer" or "seller". your_batna_value is what you get if this deal
falls through (your best alternative) — for a buyer, your reservation
price should never exceed your BATNA value; for a seller, it should never
go below it.

```

日本語：


BATNA / ZOPA 計算機: の間で一致する可能性のあるゾーンを計算します。
お客様の予約価格と相手方の推定予約価格、
アンカーを推奨し、ZOPA が存在しない場合にフラグを立てます (この場合、
正しい行動は、交渉ではなく、立ち去るか、取引構造を変更することです
価格的には厳しい）。

使用法:
python3 butna_zopa.py --config ネゴシエーション.json

ネゴシエーション.json の形状:
{
"役割": "購入者"、
「あなたの目標価格」: 400000、
"your_batna_value": 480000、
"counterparty_estimated_reservation_price": 460000、
「カウンターパーティの推定ターゲット価格」: 420000
}
役割: 「買い手」または「売り手」。 your_batna_value は、この取引の場合に得られるものです
失敗する (最良の代替案) — 購入者にとって、あなたの予約
価格は決してBATNA値を超えてはなりません。売り手にとって、それは決してあってはならないことです
その下に行きます。


### skills/negotiation-prep/scripts/batna_zopa.py:46

原文：

```text
=== BATNA / ZOPA Analysis ===

```

日本語：

=== BATNA / ZOPA 分析 ===


### skills/negotiation-prep/scripts/batna_zopa.py:47

原文：

```text
Your role: 
```

日本語：

あなたの役割:


### skills/negotiation-prep/scripts/batna_zopa.py:48

原文：

```text
Your target price: 
```

日本語：

あなたの目標価格:


### skills/negotiation-prep/scripts/batna_zopa.py:49

原文：

```text
Your BATNA value (walk-away point): 
```

日本語：

あなたのBATNA値（ウォークアウェイポイント）:


### skills/negotiation-prep/scripts/batna_zopa.py:50

原文：

```text
Counterparty's estimated reservation price: 
```

日本語：

カウンターパーティの推定予約価格:


### skills/negotiation-prep/scripts/batna_zopa.py:53

原文：

```text
never pay more than your BATNA
```

日本語：

BATNAを超える支払いは決してしないでください


### skills/negotiation-prep/scripts/batna_zopa.py:54

原文：

```text
seller won't go below their reservation
```

日本語：

売り手は予約を下回ることはありません


### skills/negotiation-prep/scripts/batna_zopa.py:55

原文：

```text
you won't go above yours
```

日本語：

あなたはあなたのものを超えることはありません


### skills/negotiation-prep/scripts/batna_zopa.py:57

原文：

```text

Your implied reservation price (should not exceed BATNA): 
```

日本語：


暗黙の予約価格 (BATNA を超えてはなりません):


### skills/negotiation-prep/scripts/batna_zopa.py:59

原文：

```text
never sell for less than your BATNA
```

日本語：

BATNA を下回って販売しないでください


### skills/negotiation-prep/scripts/batna_zopa.py:63

原文：

```text

Your implied reservation price (should not go below BATNA): 
```

日本語：


暗黙の予約価格 (BATNA を下回ってはなりません):


### skills/negotiation-prep/scripts/batna_zopa.py:66

原文：

```text

ZOPA (Zone of Possible Agreement): 
```

日本語：


ZOPA (可能な合意のゾーン):


### skills/negotiation-prep/scripts/batna_zopa.py:68

原文：

```text
ZOPA midpoint: 
```

日本語：

ZOPA中間点:


### skills/negotiation-prep/scripts/batna_zopa.py:72

原文：

```text

Recommended opening anchor: 
```

日本語：


推奨される開口アンカー:


### skills/negotiation-prep/scripts/batna_zopa.py:73

原文：

```text
As buyer, anchor near or slightly below your target, but inside the ZOPA
```

日本語：

買い手として、ターゲットの近くまたはわずかに下、ただし ZOPA の内側にアンカーします。


### skills/negotiation-prep/scripts/batna_zopa.py:74

原文：

```text
so the opening offer is taken seriously rather than dismissed as a bad-faith move.
```

日本語：

したがって、最初のオファーは悪意のある動きとして無視されるのではなく、真剣に受け止められます。


### skills/negotiation-prep/scripts/batna_zopa.py:77

原文：

```text

Recommended opening anchor: 
```

日本語：


推奨される開口アンカー:


### skills/negotiation-prep/scripts/batna_zopa.py:78

原文：

```text
As seller, anchor near or slightly above your target, but inside the ZOPA.
```

日本語：

売り手として、ターゲットの近くまたは少し上、ただし ZOPA の内側にアンカーします。


### skills/negotiation-prep/scripts/batna_zopa.py:80

原文：

```text

Your walk-away price: 
```

日本語：


ウォークアウェイ価格:


### skills/negotiation-prep/scripts/batna_zopa.py:80

原文：

```text
 (this is your BATNA, not a
```

日本語：

(これはあなたの BATNA であり、


### skills/negotiation-prep/scripts/batna_zopa.py:81

原文：

```text
negotiating tactic — going past it means the deal destroys value versus your
```

日本語：

交渉戦術 — それを通り過ぎることは、その取引があなたの価値に対して価値を破壊することを意味します


### skills/negotiation-prep/scripts/batna_zopa.py:82

原文：

```text
actual alternative, regardless of how the conversation feels in the room).
```

日本語：

部屋での会話がどのように感じられるかに関係なく、実際の代替手段です）。


### skills/negotiation-prep/scripts/batna_zopa.py:85

原文：

```text

>>> NO ZOPA EXISTS. Your reservation price and the counterparty's estimated
```

日本語：


>>> ZOPA は存在しません。お客様の予約価格と取引相手の見積額


### skills/negotiation-prep/scripts/batna_zopa.py:86

原文：

```text
    reservation price do not overlap by an estimated 
```

日本語：

予約価格が見積もりと重複しないこと


### skills/negotiation-prep/scripts/batna_zopa.py:87

原文：

```text
    Negotiating harder on price will not close a gap this size. Either:
```

日本語：

価格交渉を厳しくしても、これほどの差は埋まりません。次のいずれか:


### skills/negotiation-prep/scripts/batna_zopa.py:88

原文：

```text
    (a) the deal should not happen at current terms, walk away to your BATNA,
```

日本語：

(a) 現在の条件で取引を行うべきではありません。BATNA へ立ち去り、


### skills/negotiation-prep/scripts/batna_zopa.py:89

原文：

```text
    (b) change the deal structure (financing, timeline, scope) to create value
```

日本語：

(b) 価値を生み出すために取引構造 (資金調達、スケジュール、範囲) を変更する


### skills/negotiation-prep/scripts/batna_zopa.py:90

原文：

```text
        that shifts one side's reservation price, or
```

日本語：

一方の予約価格を変更する、または


### skills/negotiation-prep/scripts/batna_zopa.py:91

原文：

```text
    (c) your estimate of their reservation price may be wrong — verify before
```

日本語：

(c) 予約価格の見積もりが間違っている可能性があります - 事前に確認してください


### skills/negotiation-prep/scripts/batna_zopa.py:92

原文：

```text
        concluding no deal is possible.
```

日本語：

合意を結ばないことは不可能だ。


### skills/negotiation-prep/scripts/batna_zopa.py:95

原文：

```text

Counterparty's estimated target price: 
```

日本語：


カウンターパーティの推定目標価格:


### skills/negotiation-prep/scripts/batna_zopa.py:96

原文：

```text
Treat this as the number they'll open near, not what they'll actually accept.
```

日本語：

これは、実際に受け入れられる数ではなく、近くオープンする数として扱います。

## skills/pricing-strategy/scripts/pricing_calculator.py

[原文](../skills/pricing-strategy/scripts/pricing_calculator.py)


### skills/pricing-strategy/scripts/pricing_calculator.py:2

原文：

```text

Pricing calculator: Van Westendorp Price Sensitivity Meter analysis +
simple price elasticity revenue/margin optimizer.

Usage:
    python3 pricing_calculator.py --config pricing.json

pricing.json shape:
{
  "van_westendorp": {
    "too_cheap":   [10, 12, 15, 9, 11, 14, 13, 10, 12, 8],
    "cheap":       [20, 22, 25, 19, 21, 24, 23, 20, 22, 18],
    "expensive":   [35, 38, 40, 33, 36, 39, 37, 34, 38, 32],
    "too_expensive": [50, 55, 58, 48, 52, 56, 54, 49, 53, 47]
  },
  "elasticity": {
    "current_price": 29,
    "current_volume": 1000,
    "elasticity_coefficient": -1.8,
    "unit_cost": 9,
    "price_test_range": [19, 24, 29, 34, 39, 44]
  }
}

elasticity_coefficient is %change in volume / %change in price (negative,
typically -0.5 to -3 depending on category). If you don't have an estimated
coefficient, run a real price test before trusting this section.

```

日本語：


価格計算ツール: Van Westendorp 価格感応度メーター分析 +
シンプルな価格弾力性収益/利益率オプティマイザー。

使用法:
python3価格計算_calculator.py --config価格設定.json

価格設定.json の形状:
{
"ヴァン_ウェストエンドルプ": {
"安すぎる": [10, 12, 15, 9, 11, 14, 13, 10, 12, 8],
「安い」: [20, 22, 25, 19, 21, 24, 23, 20, 22, 18],
「高価」: [35, 38, 40, 33, 36, 39, 37, 34, 38, 32],
「高すぎる」: [50, 55, 58, 48, 52, 56, 54, 49, 53, 47]
  },
「弾性」: {
"現在の価格": 29、
「現在のボリューム」: 1000、
「弾性係数」: -1.8、
"単位コスト": 9、
「価格テスト範囲」: [19, 24, 29, 34, 39, 44]
  }
}

elastic_coefficient は体積の % 変化 / 価格の % 変化 (負、
通常はカテゴリに応じて -0.5 ～ -3)。お見積りがない場合
このセクションを信頼する前に、実際の価格テストを実行してください。


### skills/pricing-strategy/scripts/pricing_calculator.py:36

原文：

```text

    Approximate the four VW curves using the median of each response set as
    a simple proxy for the crossing points (a lightweight version of the
    full cumulative-distribution method used in a dedicated survey tool).
    
```

日本語：


次のように設定された各応答の中央値を使用して、4 つの VW 曲線を近似します。
交差点の単純なプロキシ (軽量バージョンの
専用調査ツールで使用される完全累積分布法）。
    


### skills/pricing-strategy/scripts/pricing_calculator.py:46

原文：

```text
Point of Marginal Cheapness ~ where too_cheap crosses expensive
```

日本語：

限界安さのポイント ~ 安すぎると高価が交差する場所


### skills/pricing-strategy/scripts/pricing_calculator.py:48

原文：

```text
Point of Marginal Expensiveness ~ where cheap crosses too_expensive
```

日本語：

限界費用のポイント ～ 安さが高すぎる点


### skills/pricing-strategy/scripts/pricing_calculator.py:50

原文：

```text
Optimal Price Point ~ where too_cheap crosses too_expensive
```

日本語：

最適価格点 ~ 安すぎる価格と高すぎる価格が交差する場所


### skills/pricing-strategy/scripts/pricing_calculator.py:52

原文：

```text
Indifference Price Point ~ where cheap crosses expensive
```

日本語：

無関心の価格点 ~ 安さと高さが交差する場所


### skills/pricing-strategy/scripts/pricing_calculator.py:85

原文：

```text
=== Van Westendorp Price Sensitivity (n={}) ===

```

日本語：

=== ヴァン・ヴェステンドルプの価格感応度 (n={}) ===


### skills/pricing-strategy/scripts/pricing_calculator.py:86

原文：

```text
Point of Marginal Cheapness (floor, below = quality doubt): $
```

日本語：

限界安さのポイント (フロア、以下 = 品質に疑問): $


### skills/pricing-strategy/scripts/pricing_calculator.py:87

原文：

```text
Optimal Price Point (most acceptable):                      $
```

日本語：

最適な価格点 (最も許容できる): $


### skills/pricing-strategy/scripts/pricing_calculator.py:88

原文：

```text
Indifference Price Point (neutral median):                  $
```

日本語：

無関心価格点 (中立中央値): $


### skills/pricing-strategy/scripts/pricing_calculator.py:89

原文：

```text
Point of Marginal Expensiveness (ceiling, above = too costly): $
```

日本語：

限界費用のポイント (天井、上 = 高すぎる): $


### skills/pricing-strategy/scripts/pricing_calculator.py:90

原文：

```text

Acceptable price range: $
```

日本語：


許容可能な価格帯: $


### skills/pricing-strategy/scripts/pricing_calculator.py:91

原文：

```text
Note: this uses median-crossing approximation, not full cumulative
```

日本語：

注: これは完全な累積ではなく、中央値交差近似を使用します。


### skills/pricing-strategy/scripts/pricing_calculator.py:92

原文：

```text
distributions. For a launch-critical decision, validate with the full
```

日本語：

配布物。起動に不可欠な決定については、完全な情報を使用して検証してください。


### skills/pricing-strategy/scripts/pricing_calculator.py:93

原文：

```text
survey method (n=100+) before finalizing.

```

日本語：

最終決定前の調査方法 (n=100+)。


### skills/pricing-strategy/scripts/pricing_calculator.py:98

原文：

```text
=== Price Elasticity: Revenue & Margin by Price Point ===

```

日本語：

=== 価格弾力性: 価格ポイント別の収益と利益 ===


### skills/pricing-strategy/scripts/pricing_calculator.py:105

原文：

```text
  <- max revenue
```

日本語：

<- 最大収益


### skills/pricing-strategy/scripts/pricing_calculator.py:107

原文：

```text
  <- max margin
```

日本語：

<- 最大マージン


### skills/pricing-strategy/scripts/pricing_calculator.py:109

原文：

```text

Elasticity coefficient used: 
```

日本語：


使用される弾性係数:

## skills/risk-mitigation/scripts/risk_matrix.py

[原文](../skills/risk-mitigation/scripts/risk_matrix.py)


### skills/risk-mitigation/scripts/risk_matrix.py:2

原文：

```text

Risk register scorer: likelihood x impact matrix with a velocity factor
(how fast the risk could materialize), which a plain 2-factor heat map
misses — a slow-brewing catastrophic risk and a fast-moving one with the
same likelihood x impact score need very different monitoring cadences.

Usage:
    python3 risk_matrix.py --config risks.json

risks.json shape:
{
  "risks": [
    {
      "name": "Key supplier concentration",
      "likelihood_1to5": 3,
      "impact_1to5": 5,
      "velocity_1to5": 2,
      "current_mitigation": "Single backup supplier identified, not yet contracted"
    }
  ]
}
velocity_1to5: 1 = years to materialize, 5 = could hit within weeks.

```

日本語：


リスク レジスタ スコアラー: 速度係数を含む可能性 x 影響マトリックス
(リスクがどのくらいの速さで現実化するか)、これは単純な 2 要素ヒート マップです
見逃す — ゆっくりと醸成される壊滅的なリスクと、急速に進行するリスク
同じ可能性 x 影響スコアには、非常に異なる監視頻度が必要です。

使用法:
python3risk_matrix.py --configrisks.json

risks.json の形状:
{
「リスク」: [
    {
"name": "主要サプライヤーの集中",
"尤度_1to5": 3、
"impact_1to5": 5、
"velocity_1to5": 2、
"current_mitigation": "単一のバックアップ サプライヤーが特定されましたが、まだ契約されていません"
    }
  ]
}
Velocity_1to5: 1 = 実現までに数年、5 = 数週間以内に実現する可能性があります。


### skills/risk-mitigation/scripts/risk_matrix.py:31

原文：

```text
CRITICAL - active mitigation now
```

日本語：

クリティカル - 現在軽減策が有効です


### skills/risk-mitigation/scripts/risk_matrix.py:33

原文：

```text
HIGH - mitigation plan required
```

日本語：

高 - 軽減計画が必要です


### skills/risk-mitigation/scripts/risk_matrix.py:35

原文：

```text
MODERATE - monitor, contingency plan
```

日本語：

中程度 - 監視、緊急時対応計画


### skills/risk-mitigation/scripts/risk_matrix.py:36

原文：

```text
LOW - accept, periodic review
```

日本語：

低 - 受け入れる、定期的なレビュー


### skills/risk-mitigation/scripts/risk_matrix.py:55

原文：

```text
=== Risk Register: Likelihood x Impact x Velocity ===

```

日本語：

=== リスクレジスタ: 可能性 x 影響 x 速度 ===


### skills/risk-mitigation/scripts/risk_matrix.py:64

原文：

```text

>>> FLAG: 
```

日本語：


>>> フラグ:


### skills/risk-mitigation/scripts/risk_matrix.py:64

原文：

```text
 CRITICAL risk(s) have no
```

日本語：

クリティカルなリスクはありません


### skills/risk-mitigation/scripts/risk_matrix.py:65

原文：

```text
    documented current mitigation. These need an owner and a plan
```

日本語：

現在の緩和策を文書化します。これらには所有者と計画が必要です


### skills/risk-mitigation/scripts/risk_matrix.py:66

原文：

```text
    before anything else on this register.
```

日本語：

この登録上の他のものよりも先に。


### skills/risk-mitigation/scripts/risk_matrix.py:72

原文：

```text

>>> NOTE: risk(s) with moderate score but high velocity — a static
```

日本語：


>>> 注: スコアは中程度だがベロシティが高いリスク - 静的


### skills/risk-mitigation/scripts/risk_matrix.py:73

原文：

```text
    heat map would rank these lower than they deserve, since they can
```

日本語：

ヒート マップでは、これらは本来よりも低くランク付けされる可能性があります。


### skills/risk-mitigation/scripts/risk_matrix.py:74

原文：

```text
    materialize fast even if their expected impact score looks middling:
```

日本語：

予想される影響スコアが中程度に見えても、すぐに具体化されます。


### skills/risk-mitigation/scripts/risk_matrix.py:76

原文：

```text
, velocity 
```

日本語：

、速度

## skills/spans-layers-org-design/scripts/spans_layers.py

[原文](../skills/spans-layers-org-design/scripts/spans_layers.py)


### skills/spans-layers-org-design/scripts/spans_layers.py:2

原文：

```text

Spans & Layers calculator: measures average span of control by management
layer, flags layers with an inefficiently narrow span against a benchmark,
and prices the annual cost of carrying more layers than the benchmark
organization design would need.

Usage:
    python3 spans_layers.py --config org.json

org.json shape:
{
  "benchmark_span_by_layer_type": {"executive": 5, "middle_management": 6, "frontline_management": 8},
  "avg_fully_loaded_manager_cost": 145000,
  "layers": [
    {"layer_number": 1, "title": "C-suite", "layer_type": "executive", "manager_count": 1, "direct_reports": 6},
    {"layer_number": 2, "title": "VPs", "layer_type": "executive", "manager_count": 6, "direct_reports": 22},
    {"layer_number": 3, "title": "Directors", "layer_type": "middle_management", "manager_count": 22, "direct_reports": 68},
    {"layer_number": 4, "title": "Managers", "layer_type": "middle_management", "manager_count": 68, "direct_reports": 210},
    {"layer_number": 5, "title": "Team leads", "layer_type": "frontline_management", "manager_count": 90, "direct_reports": 340}
  ]
}

```

日本語：


スパンとレイヤーの計算ツール: 管理者による管理の平均スパンを測定します
レイヤー、ベンチマークに対して非効率的に狭いスパンを持つレイヤーにフラグを立てます。
ベンチマークよりも多くのレイヤーを運ぶ場合の年間コストの価格を設定します
組織設計が必要になります。

使用法:
python3spans_layers.py --config org.json

org.json の形状:
{
"benchmark_span_by_layer_type": {"executive": 5, "middle_management": 6, "frontline_management": 8},
「avg_full_loaded_manager_cost」: 145000、
「レイヤー」: [
{"layer_number": 1, "title": "C-suite", "layer_type": "executive", "manager_count": 1, "direct_reports": 6},
{"layer_number": 2、"title": "VP"、"layer_type": "executive"、"manager_count": 6、"direct_reports": 22}、
{"layer_number": 3, "title": "ディレクター", "layer_type": "middle_management", "manager_count": 22, "direct_reports": 68},
{"layer_number": 4, "title": "Managers", "layer_type": "middle_management", "manager_count": 68, "direct_reports": 210},
{"layer_number": 5、"title": "チーム リード"、"layer_type": "frontline_management"、"manager_count": 90、"direct_reports": 340}
  ]
}


### skills/spans-layers-org-design/scripts/spans_layers.py:46

原文：

```text
=== Spans & Layers Analysis ===

```

日本語：

=== スパンとレイヤーの分析 ===


### skills/spans-layers-org-design/scripts/spans_layers.py:47

原文：

```text
Avg Span
```

日本語：

平均スパン


### skills/spans-layers-org-design/scripts/spans_layers.py:58

原文：

```text
managers needed at benchmark span vs actual managers = excess
```

日本語：

ベンチマーク スパンで必要なマネージャーと実際のマネージャー = 過剰


### skills/spans-layers-org-design/scripts/spans_layers.py:64

原文：

```text

Total managers across all layers: 
```

日本語：


すべての層にわたる合計マネージャー:


### skills/spans-layers-org-design/scripts/spans_layers.py:65

原文：

```text
Total layers: 
```

日本語：

合計レイヤー:


### skills/spans-layers-org-design/scripts/spans_layers.py:66

原文：

```text
Total individual contributors (below lowest layer): 
```

日本語：

個人貢献者の合計 (最下層以下):


### skills/spans-layers-org-design/scripts/spans_layers.py:69

原文：

```text

Estimated excess management positions (actual vs. benchmark span): 
```

日本語：


推定過剰管理ポジション（実績対ベンチマーク・スパン）:


### skills/spans-layers-org-design/scripts/spans_layers.py:70

原文：

```text
Estimated annual cost of excess layers: 
```

日本語：

余分なレイヤーの推定年間コスト:


### skills/spans-layers-org-design/scripts/spans_layers.py:74

原文：

```text

>>> FLAG: 
```

日本語：


>>> フラグ:


### skills/spans-layers-org-design/scripts/spans_layers.py:74

原文：

```text
 layer(s) have spans meaningfully narrower than
```

日本語：

レイヤーのスパンが大幅に狭い


### skills/spans-layers-org-design/scripts/spans_layers.py:75

原文：

```text
    benchmark. This usually means either genuine complexity that justifies
```

日本語：

ベンチマーク。これは通常、正当な理由がある真の複雑さを意味します。


### skills/spans-layers-org-design/scripts/spans_layers.py:76

原文：

```text
    closer supervision, or organizational layering added for reasons other
```

日本語：

より緊密な監督、またはその他の理由で追加された組織の階層化


### skills/spans-layers-org-design/scripts/spans_layers.py:77

原文：

```text
    than actual span requirements (legacy structure, title inflation, avoiding
```

日本語：

実際のスパン要件よりも（レガシー構造、タイトルのインフレ、回避


### skills/spans-layers-org-design/scripts/spans_layers.py:78

原文：

```text
    a difficult consolidation conversation). Confirm which before acting.
```

日本語：

統合するのは難しい会話です）。行動する前にどちらかを確認してください。


### skills/spans-layers-org-design/scripts/spans_layers.py:80

原文：

```text

No layers flagged as meaningfully narrow versus benchmark.
```

日本語：


ベンチマークに対して有意に狭いとフラグが立てられたレイヤーはありません。

## skills/stakeholder-alignment/scripts/power_interest_grid.py

[原文](../skills/stakeholder-alignment/scripts/power_interest_grid.py)


### skills/stakeholder-alignment/scripts/power_interest_grid.py:2

原文：

```text

Power-Interest stakeholder grid with a recommended engagement strategy per
quadrant, plus a coalition-math check: does the sum of "power" among
currently-supportive stakeholders actually exceed the power held by
opposed/skeptical stakeholders? A grid with lots of green dots but a
minority of the real power is a false-confidence trap.

Usage:
    python3 power_interest_grid.py --config stakeholders.json

stakeholders.json shape:
{
  "stakeholders": [
    {"name": "CFO", "power_1to5": 5, "interest_1to5": 4, "stance": "skeptical"}
  ]
}
stance: one of "champion", "supportive", "neutral", "skeptical", "opposed"

```

日本語：


推奨されるエンゲージメント戦略を含む権力と利益の関係者グリッド
象限、および連立数学チェック: 間の「力」の合計を計算します。
現在支援している利害関係者は、実際に利害関係者が保有する権限を超えています。
反対/懐疑的な利害関係者はいますか?緑の点がたくさんあるグリッドですが、
実権力の少数派は偽りの自信の罠だ。

使用法:
python3 power_interest_grid.py --config stakeholders.json

stakeholders.json の形状:
{
「利害関係者」: [
{"名前": "CFO"、"power_1to5": 5、"interest_1to5": 4、"スタンス": "懐疑的"}
  ]
}
スタンス：「支持者」、「支持者」、「中立」、「懐疑的」、「反対」のいずれか


### skills/stakeholder-alignment/scripts/power_interest_grid.py:27

原文：

```text
MANAGE CLOSELY (high power, high interest)
```

日本語：

綿密に管理 (大きな権限、高い関心)


### skills/stakeholder-alignment/scripts/power_interest_grid.py:29

原文：

```text
KEEP SATISFIED (high power, low interest)
```

日本語：

満足を維持 (高出力、低金利)


### skills/stakeholder-alignment/scripts/power_interest_grid.py:31

原文：

```text
KEEP INFORMED (low power, high interest)
```

日本語：

情報を入手 (低消費電力、高関心)


### skills/stakeholder-alignment/scripts/power_interest_grid.py:32

原文：

```text
MONITOR (low power, low interest)
```

日本語：

MONITOR (低電力、低金利)


### skills/stakeholder-alignment/scripts/power_interest_grid.py:45

原文：

```text
=== Power-Interest Stakeholder Grid ===

```

日本語：

=== 権力と利益の関係者グリッド ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:59

原文：

```text

=== Coalition Math ===
```

日本語：


=== 連合数学 ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:60

原文：

```text
Total power among supportive/champion stakeholders: 
```

日本語：

支持者/チャンピオン関係者間の総力:


### skills/stakeholder-alignment/scripts/power_interest_grid.py:61

原文：

```text
Total power among skeptical/opposed stakeholders:   
```

日本語：

懐疑的/反対する利害関係者の間の総力:


### skills/stakeholder-alignment/scripts/power_interest_grid.py:63

原文：

```text
>>> FLAG: opposed/skeptical power meets or exceeds supportive power.
```

日本語：

>>> 旗: 反対/懐疑的な勢力が支持的な勢力に匹敵するか、それを上回ります。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:64

原文：

```text
    Having more supportive NAMES doesn't matter if they don't carry
```

日本語：

より協力的なNAMESがいることは、彼らが持っていなくても問題ではありません


### skills/stakeholder-alignment/scripts/power_interest_grid.py:65

原文：

```text
    more actual POWER. This needs a deliberate coalition-building plan
```

日本語：

より実際のパワーを。これには意図的な連合構築計画が必要だ


### skills/stakeholder-alignment/scripts/power_interest_grid.py:66

原文：

```text
    for the highest-power skeptical/opposed stakeholders before
```

日本語：

以前は最高権力の懐疑的/反対派の利害関係者のために


### skills/stakeholder-alignment/scripts/power_interest_grid.py:67

原文：

```text
    proceeding — not just broader 'stakeholder communication.'
```

日本語：

単に広範な「ステークホルダーコミュニケーション」だけではありません。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:69

原文：

```text
Supportive coalition currently holds more power than opposition —
```

日本語：

現在、支持連合が野党よりも大きな力を持っている —


### skills/stakeholder-alignment/scripts/power_interest_grid.py:70

原文：

```text
still worth a specific plan for the highest-power skeptics individually.
```

日本語：

最も強力な懐疑論者向けに、個別に具体的な計画を立てる価値は依然としてある。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:72

原文：

```text

=== Engagement Strategy by Quadrant ===
```

日本語：


=== クアドラント別のエンゲージメント戦略 ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:73

原文：

```text
MANAGE CLOSELY : involve directly in decisions, address concerns personally.
```

日本語：

緊密に管理する : 意思決定に直接関与し、懸念事項に個人的に対処します。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:74

原文：

```text
KEEP SATISFIED : minimal detail, but don't surprise them — they can block
```

日本語：

満足を保つ : 詳細は最小限ですが、驚かないでください。ブロックされる可能性があります。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:75

原文：

```text
                 even with low day-to-day interest if provoked.
```

日本語：

たとえ刺激されれば、日々の関心が低くても。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:76

原文：

```text
KEEP INFORMED  : regular updates; they can become advocates if engaged well.
```

日本語：

最新情報を入手: 定期的な更新。うまく関与すれば、彼らは擁護者になることができます。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:77

原文：

```text
MONITOR        : light-touch, periodic check-in only.
```

日本語：

モニター : ライトタッチ、定期チェックインのみ。

## skills/synergy-case-builder/scripts/synergy_case.py

[原文](../skills/synergy-case-builder/scripts/synergy_case.py)


### skills/synergy-case-builder/scripts/synergy_case.py:2

原文：

```text

M&A synergy case calculator: models cost + revenue synergies against a
realistic ramp curve (synergies rarely arrive day 1), nets out one-time
integration costs, and computes NPV of the synergy case specifically —
separate from the standalone deal economics, which is where most synergy
cases get inflated.

Usage:
    python3 synergy_case.py --config synergies.json

synergies.json shape:
{
  "discount_rate_pct": 10,
  "years": 4,
  "cost_synergies": {
    "run_rate_annual_value": 15000000,
    "ramp_pct_by_year": [30, 70, 100, 100]
  },
  "revenue_synergies": {
    "run_rate_annual_value": 8000000,
    "ramp_pct_by_year": [10, 35, 70, 100],
    "confidence_haircut_pct": 50
  },
  "integration_costs": {
    "one_time_costs_by_year": [12000000, 4000000, 1000000, 0]
  }
}
confidence_haircut_pct on revenue synergies reflects that revenue synergies
are historically far less reliable than cost synergies (harder to control,
easier to attribute to something else) — cost synergies default to no
haircut since they're the more controllable, historically more reliable
category, but you can add one if there's specific reason to.

```

日本語：


M&A シナジー ケースの計算ツール: M&A に対するコスト + 収益のシナジーをモデル化します。
現実的なランプカーブ (初日に相乗効果が得られることはめったにありません)、ネットアウトは 1 回限り
統合コストを計算し、特にシナジーケースの NPV を計算します。
スタンドアロンの取引の経済性から分離されており、そこに最も相乗効果が発揮されます。
ケースが膨らみます。

使用法:
python3 synergy_case.py --config synergies.json

synergies.json の形状:
{
"discount_rate_pct": 10、
「年」: 4、
"コストシナジー": {
"run_rate_annual_value": 15000000、
"ramp_pct_by_year": [30, 70, 100, 100]
  },
"収益シナジー": {
"run_rate_annual_value": 8000000、
"ramp_pct_by_year": [10, 35, 70, 100],
「confidence_haircut_pct」: 50
  },
"統合コスト": {
"1 年ごとの費用": [12000000, 4000000, 1000000, 0]
  }
}
収益相乗効果に関するconfidence_haircut_pctは、収益相乗効果を反映しています。
歴史的に、コストシナジーよりも信頼性がはるかに低い（制御が難しく、
他のものに帰するのが簡単です) — コストシナジーのデフォルトは「なし」です
ヘアカットはより制御可能で、歴史的により信頼性が高いためです
カテゴリを追加できますが、特別な理由がある場合は追加できます。


### skills/synergy-case-builder/scripts/synergy_case.py:76

原文：

```text
=== M&A Synergy Case ===

```

日本語：

=== M&Aシナジー事例 ===


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Cost Syn.
```

日本語：

コスト同期


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Integ. Cost
```

日本語：

統合コスト


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Rev Syn (gross)
```

日本語：

Rev Syn (グロス)


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Rev Syn (haircut)
```

日本語：

Rev Syn (ヘアカット)


### skills/synergy-case-builder/scripts/synergy_case.py:89

原文：

```text

NPV of cost synergies:              
```

日本語：


コストシナジーのNPV:


### skills/synergy-case-builder/scripts/synergy_case.py:90

原文：

```text
NPV of revenue synergies (haircut 
```

日本語：

収益相乗効果の NPV (ヘアカット)


### skills/synergy-case-builder/scripts/synergy_case.py:91

原文：

```text
NPV of integration costs:           -
```

日本語：

統合コストの NPV: -


### skills/synergy-case-builder/scripts/synergy_case.py:92

原文：

```text
NET SYNERGY CASE NPV:                
```

日本語：

ネットシナジーケースNPV:


### skills/synergy-case-builder/scripts/synergy_case.py:95

原文：

```text

>>> NOTE: revenue synergy haircut is only 
```

日本語：


>>> 注: 収益相乗効果のヘアカットは


### skills/synergy-case-builder/scripts/synergy_case.py:95

原文：

```text
%. Historically,
```

日本語：

%。歴史的には、


### skills/synergy-case-builder/scripts/synergy_case.py:96

原文：

```text
    revenue synergies are realized far less reliably than cost synergies
```

日本語：

収益の相乗効果はコストの相乗効果よりも実現される信頼性がはるかに低い


### skills/synergy-case-builder/scripts/synergy_case.py:97

原文：

```text
    (harder to isolate from baseline growth, dependent on customer/market
```

日本語：

(顧客/市場に応じて、ベースラインの成長から切り離すのが困難


### skills/synergy-case-builder/scripts/synergy_case.py:98

原文：

```text
    behavior outside management's direct control). Confirm this haircut
```

日本語：

経営陣の直接の制御の範囲外の行動）。このヘアカットを確認してください


### skills/synergy-case-builder/scripts/synergy_case.py:99

原文：

```text
    is evidence-based, not just optimism carried over from deal advocacy.
```

日本語：

それは証拠に基づいており、合意支持から引き継がれた単なる楽観主義ではありません。


### skills/synergy-case-builder/scripts/synergy_case.py:103

原文：

```text

Cost synergies are 
```

日本語：


コストシナジーは、


### skills/synergy-case-builder/scripts/synergy_case.py:103

原文：

```text
% of total synergy NPV (post-haircut).
```

日本語：

総シナジー NPV の % (ヘアカット後)。


### skills/synergy-case-builder/scripts/synergy_case.py:104

原文：

```text
A deal case leaning heavily on revenue synergies carries materially more
```

日本語：

収益相乗効果に大きく依存した取引案件は、実質的により多くの利益をもたらします


### skills/synergy-case-builder/scripts/synergy_case.py:105

原文：

```text
execution risk than one anchored in cost synergies — size confidence accordingly.
```

日本語：

実行リスクはコストの相乗効果に基づくリスクよりも高く、それに応じて信頼度を決定します。

## skills/unit-economics-health-check/scripts/unit_economics.py

[原文](../skills/unit-economics-health-check/scripts/unit_economics.py)


### skills/unit-economics-health-check/scripts/unit_economics.py:2

原文：

```text

Unit economics health check: LTV, LTV:CAC ratio, CAC payback period, and a
cohort-decay-aware LTV calculation (not the naive "ARPU / churn" shortcut,
which overstates LTV whenever churn is front-loaded, as it usually is).

Usage:
    python3 unit_economics.py --config unit_econ.json

unit_econ.json shape:
{
  "cac": 450,
  "monthly_revenue_per_customer": 80,
  "gross_margin_pct": 75,
  "monthly_churn_pct_by_month": [8, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3],
  "discount_rate_annual_pct": 12
}
monthly_churn_pct_by_month lets churn decay realistically over the first
year (most businesses lose new customers faster than mature ones) instead
of assuming one flat churn rate forever, which is the most common way LTV
gets overstated.

```

日本語：


ユニットエコノミクスの健全性チェック: LTV、LTV:CAC 比率、CAC 回収期間、および
コホート減衰を考慮した LTV 計算 (単純な「ARPU / チャーン」ショートカットではなく、
通常のように、チャーンが前倒しされると常に LTV が誇張されます)。

使用法:
python3 ユニットエコノミクス.py --config ユニットエコノミクス.json

Unit_econ.json の形状:
{
「cac」: 450、
「顧客あたりの月間収益」: 80、
「総利益率」: 75、
"monthly_churn_pct_by_month": [8, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3],
「割引率_年間_pct」: 12
}
month_churn_pct_by_month を使用すると、最初の期間でチャーンが現実的に減少します。
（ほとんどの企業は成熟した顧客よりも早く新規顧客を失う）
LTV を測定する最も一般的な方法である、一定の解約率を永久に仮定する方法
誇張されてしまう。


### skills/unit-economics-health-check/scripts/unit_economics.py:50

原文：

```text
=== Unit Economics Health Check ===

```

日本語：

=== ユニットエコノミクス健康チェック ===


### skills/unit-economics-health-check/scripts/unit_economics.py:51

原文：

```text
Cum Margin $
```

日本語：

カムマージン$


### skills/unit-economics-health-check/scripts/unit_economics.py:51

原文：

```text
Margin $
```

日本語：

マージン$


### skills/unit-economics-health-check/scripts/unit_economics.py:51

原文：

```text
Survival %
```

日本語：

生存率


### skills/unit-economics-health-check/scripts/unit_economics.py:64

原文：

```text
extend LTV tail at final churn rate to a reasonable horizon (36 months total)
```

日本語：

最終的な解約率での LTV テールを妥当な期間まで延長する (合計 36 か月)


### skills/unit-economics-health-check/scripts/unit_economics.py:77

原文：

```text

=== Summary (36-month horizon, discounted) ===
```

日本語：


=== 概要 (36 か月期間、割引) ===


### skills/unit-economics-health-check/scripts/unit_economics.py:79

原文：

```text
LTV (discounted contribution margin): 
```

日本語：

LTV (割引貢献利益率):


### skills/unit-economics-health-check/scripts/unit_economics.py:80

原文：

```text
LTV:CAC ratio:                
```

日本語：

LTV:CAC比:


### skills/unit-economics-health-check/scripts/unit_economics.py:81

原文：

```text
CAC payback period:           
```

日本語：

CAC の回収期間:


### skills/unit-economics-health-check/scripts/unit_economics.py:83

原文：

```text

=== Health Read ===
```

日本語：


=== ヘルスリード ===


### skills/unit-economics-health-check/scripts/unit_economics.py:85

原文：

```text
 is in the healthy range (>=3 is the common benchmark).
```

日本語：

は健全な範囲内にあります (>=3 が一般的なベンチマークです)。


### skills/unit-economics-health-check/scripts/unit_economics.py:85

原文：

```text
LTV:CAC of 
```

日本語：

LTV:CACの


### skills/unit-economics-health-check/scripts/unit_economics.py:87

原文：

```text
 is marginal. Growth is likely destroying value per
```

日本語：

限界です。成長により、あたりの価値が破壊される可能性が高い


### skills/unit-economics-health-check/scripts/unit_economics.py:87

原文：

```text
LTV:CAC of 
```

日本語：

LTV:CACの


### skills/unit-economics-health-check/scripts/unit_economics.py:88

原文：

```text
customer acquired even though revenue is growing. Investigate CAC or retention.
```

日本語：

収益が伸びているにもかかわらず顧客を獲得した。 CAC または保持を調査します。


### skills/unit-economics-health-check/scripts/unit_economics.py:90

原文：

```text
 is below 1.5. Acquiring customers at this rate is
```

日本語：

1.5未満です。このペースで顧客を獲得するのは、


### skills/unit-economics-health-check/scripts/unit_economics.py:90

原文：

```text
LTV:CAC of 
```

日本語：

LTV:CACの


### skills/unit-economics-health-check/scripts/unit_economics.py:91

原文：

```text
likely destroying value. This is a stop-and-fix signal, not a scale signal.
```

日本語：

価値を破壊する可能性があります。これはストップアンドフィックス信号であり、スケール信号ではありません。


### skills/unit-economics-health-check/scripts/unit_economics.py:94

原文：

```text

>>> FLAG: 
```

日本語：


>>> フラグ:


### skills/unit-economics-health-check/scripts/unit_economics.py:94

原文：

```text
-month payback is long. Growth at this payback
```

日本語：

・月々の返済が長い。この投資回収による成長


### skills/unit-economics-health-check/scripts/unit_economics.py:95

原文：

```text
    period requires either a lot of cash runway or outside financing to fund
```

日本語：

この期間には多額の資金が必要となるか、外部からの資金調達が必要となります。


### skills/unit-economics-health-check/scripts/unit_economics.py:96

原文：

```text
    the gap between spending on CAC and recovering it.
```

日本語：

CAC への支出とそれを回収する間のギャップ。

## skills/war-gaming/scripts/decision_tree_ev.py

[原文](../skills/war-gaming/scripts/decision_tree_ev.py)


### skills/war-gaming/scripts/decision_tree_ev.py:2

原文：

```text

Decision-tree expected value calculator for scenario/war-gaming analysis.
Handles a decision node followed by chance nodes (competitor/market response
scenarios) with probabilities and payoffs, computing EV per initial choice
and flagging the choice with the best worst-case (maximin) if it differs
from the best-EV choice.

Usage:
    python3 decision_tree_ev.py --config scenarios.json

scenarios.json shape:
{
  "options": [
    {
      "name": "Aggressive price cut",
      "scenarios": [
        {"name": "Competitor matches", "probability": 0.5, "payoff": -200000},
        {"name": "Competitor holds", "probability": 0.3, "payoff": 900000},
        {"name": "Competitor exits segment", "probability": 0.2, "payoff": 1500000}
      ]
    }
  ]
}
Probabilities within an option's scenarios must sum to 1.0 (+/- 0.01).

```

日本語：


シナリオ/ウォーゲーム分析用のディシジョンツリー期待値計算ツール。
意思決定ノードとその後に続くチャンス ノード (競合他社/市場の反応) を処理します。
シナリオ) 確率と利得を使用して、最初の選択ごとに EV を計算
異なる場合は、最良の最悪のケース (最大値) を選択にフラグを立てます。
最適なEVの選択から。

使用法:
python3 Decision_tree_ev.py --config scenarios.json

scenarios.json の形状:
{
「オプション」: [
    {
"name": "積極的な値下げ",
「シナリオ」: [
{"名前": "競合他社の試合"、"確率": 0.5、"報酬": -200000},
{"名前": "競合他社が保有", "確率": 0.3, "ペイオフ": 900000},
{"名前": "競合他社がセグメントを撤退する"、"確率": 0.2、"利益": 1500000}
      ]
    }
  ]
}
オプションのシナリオ内の確率は、合計が 1.0 (+/- 0.01) になる必要があります。


### skills/war-gaming/scripts/decision_tree_ev.py:38

原文：

```text
=== Decision Tree: Expected Value by Option ===

```

日本語：

=== デシジョン ツリー: オプション別の期待値 ===


### skills/war-gaming/scripts/decision_tree_ev.py:44

原文：

```text
  >>> WARNING: '
```

日本語：

>>> 警告: '


### skills/war-gaming/scripts/decision_tree_ev.py:44

原文：

```text
' scenario probabilities sum to 
```

日本語：

' シナリオの確率の合計は


### skills/war-gaming/scripts/decision_tree_ev.py:44

原文：

```text
, not 1.0 — fix before trusting this EV.
```

日本語：

、1.0 ではありません — この EV を信頼する前に修正してください。


### skills/war-gaming/scripts/decision_tree_ev.py:51

原文：

```text
Best case
```

日本語：

ベストケース


### skills/war-gaming/scripts/decision_tree_ev.py:51

原文：

```text
Worst case
```

日本語：

最悪の場合


### skills/war-gaming/scripts/decision_tree_ev.py:59

原文：

```text

Highest expected value: 
```

日本語：


最も高い期待値:


### skills/war-gaming/scripts/decision_tree_ev.py:60

原文：

```text
 (worst case = 
```

日本語：

(最悪の場合 =


### skills/war-gaming/scripts/decision_tree_ev.py:60

原文：

```text
Best worst-case (maximin, most defensible if you're risk-averse or can't survive the downside): 
```

日本語：

最良の最悪のケース (リスクを回避する場合、またはマイナス面に耐えられない場合に最も防御可能な最大値):


### skills/war-gaming/scripts/decision_tree_ev.py:65

原文：

```text

>>> FLAG: the EV-maximizing option and the maximin (safest-downside)
```

日本語：


>>> FLAG: EV 最大化オプションと最大値 (最も安全なマイナス面)


### skills/war-gaming/scripts/decision_tree_ev.py:66

原文：

```text
    option are different choices. If the worst case of '
```

日本語：

オプションは異なる選択肢です。最悪の場合、


### skills/war-gaming/scripts/decision_tree_ev.py:67

原文：

```text
) is something the business could not actually
```

日本語：

）はビジネスでは実際には不可能なことです


### skills/war-gaming/scripts/decision_tree_ev.py:68

原文：

```text
    survive, expected value alone is the wrong decision criterion here —
```

日本語：

生き残れ、期待値だけがここでの間違った判断基準である —


### skills/war-gaming/scripts/decision_tree_ev.py:69

原文：

```text
    this needs an explicit risk-tolerance conversation, not a silent
```

日本語：

これには、沈黙ではなく、明確なリスク許容度の会話が必要です。


### skills/war-gaming/scripts/decision_tree_ev.py:70

原文：

```text
    default to the highest-EV row.
```

日本語：

デフォルトはEVの最も高い行です。


### skills/war-gaming/scripts/decision_tree_ev.py:72

原文：

```text

=== Scenario Detail ===
```

日本語：


=== シナリオ詳細 ===
