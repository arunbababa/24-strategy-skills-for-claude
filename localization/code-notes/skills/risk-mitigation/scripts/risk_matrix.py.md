# skills/risk-mitigation/scripts/risk_matrix.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/risk-mitigation/scripts/risk_matrix.py)

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

リスク登録簿のスコア計算ツール。発生可能性 × 影響度に、リスクが現実化する速さを加味する。これは単純な 2 要素のヒートマップでは見落とされる点であり、発生可能性 × 影響度のスコアが同じでも、徐々に進行する壊滅的リスクと急速に顕在化するリスクでは、必要な監視頻度が大きく異なる。

使用法:
```text
python3 risk_matrix.py --config risks.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
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
```

`velocity_1to5`: 1 は現実化まで数年、5 は数週間以内に発生し得る。例の対策は「代替サプライヤー 1 社を特定したが、まだ未契約」。


### skills/risk-mitigation/scripts/risk_matrix.py:31

原文：

```text
CRITICAL - active mitigation now
```

日本語：

CRITICAL: 重大。今すぐ具体的な軽減策を実施する


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

 件の重大リスクで、


### skills/risk-mitigation/scripts/risk_matrix.py:65

原文：

```text
    documented current mitigation. These need an owner and a plan
```

日本語：

現在の軽減策が文書化されていない。これらのリスクについては、


### skills/risk-mitigation/scripts/risk_matrix.py:66

原文：

```text
    before anything else on this register.
```

日本語：

この登録簿の他の項目に先立ち、担当者と計画を決める必要がある。


### skills/risk-mitigation/scripts/risk_matrix.py:72

原文：

```text

>>> NOTE: risk(s) with moderate score but high velocity — a static
```

日本語：

>>> 注: スコアは中程度でも、顕在化が速いリスクがある。静的な


### skills/risk-mitigation/scripts/risk_matrix.py:73

原文：

```text
    heat map would rank these lower than they deserve, since they can
```

日本語：

ヒートマップでは優先度を過小評価されるが、


### skills/risk-mitigation/scripts/risk_matrix.py:74

原文：

```text
    materialize fast even if their expected impact score looks middling:
```

日本語：

想定影響度が中程度に見えても、素早く現実化し得るためである:


### skills/risk-mitigation/scripts/risk_matrix.py:76

原文：

```text
, velocity 
```

日本語：

、速度


