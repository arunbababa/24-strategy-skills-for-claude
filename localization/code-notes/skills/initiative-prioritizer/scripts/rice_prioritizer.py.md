# skills/initiative-prioritizer/scripts/rice_prioritizer.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/initiative-prioritizer/scripts/rice_prioritizer.py)

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

RICE（Reach × Impact × Confidence / Effort）による優先順位づけに、遅延コストの評価を加える。RICE だけでは緊急性や実施順序を考慮できないため。

使用法:
```text
python3 rice_prioritizer.py --config initiatives.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

impact の標準スケール: 3=非常に大きい、2=大きい、1=中程度、0.5=小さい、0.25=ごく小さい。


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:39

原文：

```text
cost of a 3-month delay, a common sequencing lens
```

日本語：

3 か月遅延した場合のコスト。実施順序を判断する一般的な視点。


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

RICE は工数当たりの期待効果で順位を付けるが、


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:51

原文：

```text
for urgency. Cross-check: an initiative with a lower RICE score but a high
```

日本語：

緊急性は考慮しない。RICE スコアが低くても、


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:52

原文：

```text
cost of delay (e.g., a closing market window, a compliance deadline) may
```

日本語：

市場機会の期限や遵守期限などによる遅延コストが高い施策は、


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:53

原文：

```text
still need to be sequenced earlier. Don't apply the RICE rank mechanically
```

日本語：

先に実施する必要がある。CoD 列と実際の予定を照合せずに、


### skills/initiative-prioritizer/scripts/rice_prioritizer.py:54

原文：

```text
without checking the CoD column against the calendar.
```

日本語：

RICE の順位を機械的に適用しない。


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

RICE 順を既定のものとして採用せず、実施順序の判断を明示的に確認する。


