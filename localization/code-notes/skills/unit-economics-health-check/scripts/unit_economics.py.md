# skills/unit-economics-health-check/scripts/unit_economics.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/unit-economics-health-check/scripts/unit_economics.py)

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

ユニットエコノミクスの健全性を確認する。LTV、LTV:CAC比率、CAC回収期間に加え、コホートの経過に伴う解約率の低下を考慮してLTVを計算する。単純な「ARPU / churn」という近道は使わない。この近道は、通常よく見られるように解約が初期に集中する場合、LTVを過大評価する。

使用例：

```sh
python3 unit_economics.py --config unit_econ.json
```

設定JSONの構造（キーと値は原文表記を保持）：

```json
{
  "cac": 450,
  "monthly_revenue_per_customer": 80,
  "gross_margin_pct": 75,
  "monthly_churn_pct_by_month": [8, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3],
  "discount_rate_annual_pct": 12
}
```

monthly_churn_pct_by_monthにより、最初の1年間に解約率が現実的に低下する様子を表せる。多くの事業では、長期利用客より新規顧客の方が早期に離脱しやすい。永久に一定の解約率を仮定することは、LTVが過大評価される最も一般的な原因である。


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

累積限界利益額（$）


### skills/unit-economics-health-check/scripts/unit_economics.py:51

原文：

```text
Margin $
```

日本語：

限界利益額（$）


### skills/unit-economics-health-check/scripts/unit_economics.py:51

原文：

```text
Survival %
```

日本語：

顧客継続率（%）


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

LTV（割引後の限界利益額）：


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

=== 健全性の評価 ===


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

は境界的な水準。売上高が増えていても、成長によって、獲得顧客1人当たりの


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

価値を損なっている可能性が高い。CACまたは顧客継続率を調べる。


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

価値を損なう可能性が高い。拡大を進める合図ではなく、いったん止めて改善する合図。


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

か月という回収期間は長い。この回収期間のまま成長するには、


### skills/unit-economics-health-check/scripts/unit_economics.py:95

原文：

```text
    period requires either a lot of cash runway or outside financing to fund
```

日本語：

CACへの支出からその回収までの資金ギャップを埋めるために、十分な手元資金の余裕、または外部資金調達が


### skills/unit-economics-health-check/scripts/unit_economics.py:96

原文：

```text
    the gap between spending on CAC and recovering it.
```

日本語：

必要となる。
