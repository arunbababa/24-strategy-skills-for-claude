# skills/full-potential-diagnostic/scripts/full_potential_calc.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/full-potential-diagnostic/scripts/full_potential_calc.py)

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

潜在的な改善余地を診断する計算ツール。現在の業績と上位 25%・ベストプラクティスのベンチマークの差を指標ごとに金額換算し、改善可能な価値の合計に集約する。McKinsey の「full potential」という変革の考え方を支える中核ツール。

使用法:
```text
python3 full_potential_calc.py --config metrics.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

`pct_of_revenue` の指標では、改善余地の金額 = |benchmark - current| % × revenue_base。
`working_capital_base` を持つ `turns`（回転数）指標では、現在の回転数をベンチマークまで高めることで解放される運転資本を、改善余地の金額として概算する。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:61

原文：

```text
=== Full-Potential Diagnostic: Value at Stake ===

```

日本語：

=== 潜在的な改善余地の診断: 改善可能な価値 ===


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

改善余地の金額


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:75

原文：

```text
working capital roughly scales inversely with turns
```

日本語：

運転資本はおおむね回転数に反比例する


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:86

原文：

```text
TOTAL VALUE AT STAKE
```

日本語：

改善余地の金額の合計


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

注: これはベンチマークまでの理論的な差であり、実現計画ではない。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:89

原文：

```text
Typical full-potential programs capture 40-70% of the identified gap
```

日本語：

一般的な full-potential プログラムでは、最初の 18-24 か月で特定した差の 40-70% を実現する。


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:90

原文：

```text
within the first 18-24 months — use this number to size ambition, not
```

日本語：

この値は目指す規模を決めるために使い、


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:91

原文：

```text
as a guaranteed outcome. Pair with initiative-prioritizer to sequence
```

日本語：

成果の保証とはしない。initiative-prioritizer と組み合わせ、


### skills/full-potential-diagnostic/scripts/full_potential_calc.py:92

原文：

```text
which gaps to close first.
```

日本語：

どの差を先に埋めるか、順序を決める。


