# skills/business-case-builder/scripts/npv_case.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/business-case-builder/scripts/npv_case.py)

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

事業の主要な要因に基づくビジネスケース: NPV（正味現在価値）、IRR（内部収益率）、投資回収期間、感応度表を計算する。

使用法:
```text
python3 npv_case.py --config case.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

年間キャッシュフロー、NPV、IRR（二分法で計算し numpy に依存しない）、投資回収期間、および売上高 × 割引率の NPV 感応度表を出力する。最後の感応度表は、手計算が面倒なため、手作業のビジネスケースでは省略されがちな部分。


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

モデルの対象年数内に投資を回収できない


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

IRR: 指定範囲で見つからない（キャッシュフローの正負を確認）


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

これを使い、ビジネスケースが成立し続ける条件を明示する。


