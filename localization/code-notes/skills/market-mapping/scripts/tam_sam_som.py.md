# skills/market-mapping/scripts/tam_sam_som.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/market-mapping/scripts/tam_sam_som.py)

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

複数の方法で突き合わせる市場規模推計（TAM/SAM/SOM）。トップダウンとボトムアップを照合する。

使用例：

```sh
python3 tam_sam_som.py --config market.json
```

market.jsonの構造：

```json
{
  "top_down": {"total_population": 5000000, "target_share_pct": 12, "avg_annual_spend": 4800},
  "bottom_up": {"units_or_customers": 45000, "avg_annual_revenue_per_customer": 6200},
  "serviceable_filters": {"pct_geography": 70, "pct_segment_fit": 55, "pct_regulatory_eligible": 90},
  "obtainable": {"realistic_share_of_sam_pct": 8, "years_to_reach": 3}
}
```

TAM（独立した2つの推計とその差異）、SAM、SOMを出力する。トップダウンとボトムアップのTAMの推計差が30%を超える場合は警告する。これは、資料に数値を掲載する前に入力を見直すべき合図。


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

>>> 警告：トップダウンとボトムアップの推計差が30%を超えている。


### skills/market-mapping/scripts/tam_sam_som.py:60

原文：

```text
      Do not present a single TAM number yet — the two methods are
```

日本語：

まだTAMを単一の数値として提示しない。2つの手法が、


### skills/market-mapping/scripts/tam_sam_som.py:61

原文：

```text
      built on inconsistent assumptions about population, spend, or
```

日本語：

母集団、支出、適合性に関して整合しない前提に


### skills/market-mapping/scripts/tam_sam_som.py:62

原文：

```text
      fit. Reconcile the inputs before this goes in a deck.
```

日本語：

基づいている。資料に掲載する前に入力の整合を取る。


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

SAM（サービス提供可能性の条件で絞り込んだ後 


### skills/market-mapping/scripts/tam_sam_som.py:68

原文：

```text
% share of SAM over 
```

日本語：

年間で獲得するSAMに対するシェア（%）：


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

SOM到達に必要な年当たりの金額（計算上）：
