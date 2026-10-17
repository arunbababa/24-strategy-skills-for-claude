# skills/capital-reallocation-review/scripts/portfolio_matrix.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/capital-reallocation-review/scripts/portfolio_matrix.py)

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

GE-McKinsey の 9 マスポートフォリオマトリックス（業界の魅力度 × 競争力）。従来の 2 要素の BCG マトリックスを改善したもので、BCG が「魅力度」を成長率のみ、「競争力」を相対シェアのみで表すのに対し、複数要因で評価する。

使用法:
```text
python3 portfolio_matrix.py --config portfolio.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

各要因のスコアは 1-10。各軸のウェイト合計は 1.0 にする。


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

SELECTIVE: 選別的に対応（競争力を強化するか撤退）


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:43

原文：

```text
SELECTIVE (hold, fund selectively)
```

日本語：

SELECTIVE: 選別的に対応（維持し、選択的に資金投入）


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:44

原文：

```text
SELECTIVE (harvest strength, low growth)
```

日本語：

SELECTIVE: 選別的に対応（低成長下で競争力を活かして収益回収）


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

>>> 注意: 売上高の 40% 超が、収益回収・売却の領域にある。


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:84

原文：

```text
    The portfolio is over-weighted toward declining positions —
```

日本語：

ポートフォリオが衰退する事業に偏りすぎているため、


### skills/capital-reallocation-review/scripts/portfolio_matrix.py:85

原文：

```text
    capital reallocation toward the invest zone should be a priority.
```

日本語：

投資ゾーンへの資本の再配分が優先されるべきである。


