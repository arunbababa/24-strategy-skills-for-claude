# skills/synergy-case-builder/scripts/synergy_case.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/synergy-case-builder/scripts/synergy_case.py)

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

M&Aシナジーの計算ツール。コストと売上高のシナジーを、現実的な立ち上がり曲線に沿ってモデル化する（初日から全シナジーが得られることはまれ）。一時的な統合費用を控除し、シナジー部分だけのNPVを計算する。単独ベースの取引採算とは分けて扱う。これらを混同することが、多くのシナジー試算が水増しされる原因となる。

使用例：

```sh
python3 synergy_case.py --config synergies.json
```

設定JSONの構造（キーと値は原文表記を保持）：

```json
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
```

売上シナジーのconfidence_haircut_pctは、売上シナジーが過去の実績上、コストシナジーより大幅に実現しにくいことを反映する（制御しにくく、別の要因による成果と区別しにくい）。コストシナジーは制御しやすく、過去の実績上も確実性が高いため、既定では減額しない。具体的な理由があれば、コストシナジーにも減額を設定できる。


### skills/synergy-case-builder/scripts/synergy_case.py:76

原文：

```text
=== M&A Synergy Case ===

```

日本語：

=== M&Aシナジー試算 ===


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Cost Syn.
```

日本語：

コストシナジー


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

売上シナジー（減額前）


### skills/synergy-case-builder/scripts/synergy_case.py:77

原文：

```text
Rev Syn (haircut)
```

日本語：

売上シナジー（実現確度による減額後）


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

売上シナジーのNPV（減額率 


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

>>> 注：売上シナジーの減額率はわずか 


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

（基礎的な成長による効果と切り分けにくく、経営陣が直接制御できない顧客や市場の


### skills/synergy-case-builder/scripts/synergy_case.py:98

原文：

```text
    behavior outside management's direct control). Confirm this haircut
```

日本語：

動向に依存するため）。この減額率が


### skills/synergy-case-builder/scripts/synergy_case.py:99

原文：

```text
    is evidence-based, not just optimism carried over from deal advocacy.
```

日本語：

根拠に基づくものであり、取引を推進する側の楽観をそのまま引き継いだ値でないことを確認する。


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

売上シナジーに大きく依存する取引計画は、コストシナジーを軸にした計画よりも


### skills/synergy-case-builder/scripts/synergy_case.py:105

原文：

```text
execution risk than one anchored in cost synergies — size confidence accordingly.
```

日本語：

実行リスクが大幅に高い。その点に応じて確信度を調整する。
