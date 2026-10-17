# skills/war-gaming/scripts/decision_tree_ev.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/war-gaming/scripts/decision_tree_ev.py)

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

シナリオ分析・ウォーゲーム分析用の決定木による期待値計算ツール。意思決定ノードに続く確率ノード（競合・市場の反応シナリオ）を、その確率と損益で評価し、最初の選択肢ごとに期待値（EV）を計算する。また、最悪の場合の損益が最もよい選択肢（マキシミン）が期待値最大の選択肢と異なる場合に、その違いを示す。

使用法:
```text
python3 decision_tree_ev.py --config scenarios.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

各選択肢に属するシナリオの確率は、合計 1.0（許容誤差 +/- 0.01）とする。例のシナリオは、競合が値下げに追随する、価格を据え置く、当該セグメントから撤退する、の 3 つ。


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

最悪時の損益が最良となる選択肢（マキシミン。リスク回避を重視する場合や、下振れに耐えられない場合に最も妥当）: 


### skills/war-gaming/scripts/decision_tree_ev.py:65

原文：

```text

>>> FLAG: the EV-maximizing option and the maximin (safest-downside)
```

日本語：

>>> 注意: 期待値を最大にする選択肢と、マキシミン（下振れが最も小さい）


### skills/war-gaming/scripts/decision_tree_ev.py:66

原文：

```text
    option are different choices. If the worst case of '
```

日本語：

の選択肢が異なる。次の選択肢の最悪時の損益が、


### skills/war-gaming/scripts/decision_tree_ev.py:67

原文：

```text
) is something the business could not actually
```

日本語：

) という事業として実際には


### skills/war-gaming/scripts/decision_tree_ev.py:68

原文：

```text
    survive, expected value alone is the wrong decision criterion here —
```

日本語：

耐えられない水準なら、期待値だけで判断するのは適切ではない。


### skills/war-gaming/scripts/decision_tree_ev.py:69

原文：

```text
    this needs an explicit risk-tolerance conversation, not a silent
```

日本語：

黙って期待値の最も高い行を選ぶのではなく、


### skills/war-gaming/scripts/decision_tree_ev.py:70

原文：

```text
    default to the highest-EV row.
```

日本語：

許容できるリスクの範囲を明示的に話し合う必要がある。


### skills/war-gaming/scripts/decision_tree_ev.py:72

原文：

```text

=== Scenario Detail ===
```

日本語：


=== シナリオ詳細 ===


