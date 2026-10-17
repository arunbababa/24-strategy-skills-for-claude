# skills/pricing-strategy/scripts/pricing_calculator.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/pricing-strategy/scripts/pricing_calculator.py)

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

価格計算ツール: Van Westendorp 法による価格感度分析と、価格弾力性を使った簡易的な売上・利益の最適化。

使用法:
```text
python3 pricing_calculator.py --config pricing.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

`elasticity_coefficient` は「販売数量の変化率 ÷ 価格の変化率」。値は負で、通常はカテゴリーにより -0.5 から -3。推定係数がない場合は、この結果に依存する前に実際の価格テストを行う。


### skills/pricing-strategy/scripts/pricing_calculator.py:36

原文：

```text

    Approximate the four VW curves using the median of each response set as
    a simple proxy for the crossing points (a lightweight version of the
    full cumulative-distribution method used in a dedicated survey tool).
    
```

日本語：

各回答群の中央値を交点の簡易的な代用値として使い、Van Westendorp 法の 4 本の曲線を近似する。専用調査ツールが用いる完全な累積分布法の簡易版。


### skills/pricing-strategy/scripts/pricing_calculator.py:46

原文：

```text
Point of Marginal Cheapness ~ where too_cheap crosses expensive
```

日本語：

下限価格（Point of Marginal Cheapness）: too_cheap と expensive の交点付近


### skills/pricing-strategy/scripts/pricing_calculator.py:48

原文：

```text
Point of Marginal Expensiveness ~ where cheap crosses too_expensive
```

日本語：

上限価格（Point of Marginal Expensiveness）: cheap と too_expensive の交点付近


### skills/pricing-strategy/scripts/pricing_calculator.py:50

原文：

```text
Optimal Price Point ~ where too_cheap crosses too_expensive
```

日本語：

最適価格（Optimal Price Point）: too_cheap と too_expensive の交点付近


### skills/pricing-strategy/scripts/pricing_calculator.py:52

原文：

```text
Indifference Price Point ~ where cheap crosses expensive
```

日本語：

無差別価格（Indifference Price Point）: cheap と expensive の交点付近


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

下限価格（これより安いと品質を疑われる）: $


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

無差別価格（中立となる中央値）: $


### skills/pricing-strategy/scripts/pricing_calculator.py:89

原文：

```text
Point of Marginal Expensiveness (ceiling, above = too costly): $
```

日本語：

上限価格（これより高いと高すぎると判断される）: $


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

注: 完全な累積分布ではなく、中央値による交点の近似を使用している。


### skills/pricing-strategy/scripts/pricing_calculator.py:92

原文：

```text
distributions. For a launch-critical decision, validate with the full
```

日本語：

発売に重大な影響を及ぼす判断では、最終決定の前に、正式な


### skills/pricing-strategy/scripts/pricing_calculator.py:93

原文：

```text
survey method (n=100+) before finalizing.

```

日本語：

調査手法（n=100 以上）で検証する。


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

使用した価格弾力性係数: 


