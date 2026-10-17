# skills/stakeholder-alignment/scripts/power_interest_grid.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/stakeholder-alignment/scripts/power_interest_grid.py)

### skills/stakeholder-alignment/scripts/power_interest_grid.py:2

原文：

```text

Power-Interest stakeholder grid with a recommended engagement strategy per
quadrant, plus a coalition-math check: does the sum of "power" among
currently-supportive stakeholders actually exceed the power held by
opposed/skeptical stakeholders? A grid with lots of green dots but a
minority of the real power is a false-confidence trap.

Usage:
    python3 power_interest_grid.py --config stakeholders.json

stakeholders.json shape:
{
  "stakeholders": [
    {"name": "CFO", "power_1to5": 5, "interest_1to5": 4, "stance": "skeptical"}
  ]
}
stance: one of "champion", "supportive", "neutral", "skeptical", "opposed"

```

日本語：

影響力と関心度で関係者を 4 象限に分類し、各象限に推奨する関与方針を示す。さらに、現在の支持者の「影響力」の合計が、反対・懐疑派の影響力を実際に上回るかを確認する。支持を示す緑の点が多くても、実質的な影響力で少数派なら、根拠のない安心につながる。

使用法:
```text
python3 power_interest_grid.py --config stakeholders.json
```

設定 JSON の例（キー・値は原文どおり）:
```json
{
  "stakeholders": [
    {"name": "CFO", "power_1to5": 5, "interest_1to5": 4, "stance": "skeptical"}
  ]
}
```

`stance` は `champion`（積極的推進者）、`supportive`（支持）、`neutral`（中立）、`skeptical`（懐疑的）、`opposed`（反対）のいずれか。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:27

原文：

```text
MANAGE CLOSELY (high power, high interest)
```

日本語：

MANAGE CLOSELY: 密接に関与する（影響力が高く、関心度も高い）


### skills/stakeholder-alignment/scripts/power_interest_grid.py:29

原文：

```text
KEEP SATISFIED (high power, low interest)
```

日本語：

KEEP SATISFIED: 満足を保つ（影響力が高く、関心度は低い）


### skills/stakeholder-alignment/scripts/power_interest_grid.py:31

原文：

```text
KEEP INFORMED (low power, high interest)
```

日本語：

KEEP INFORMED: 情報を提供する（影響力が低く、関心度は高い）


### skills/stakeholder-alignment/scripts/power_interest_grid.py:32

原文：

```text
MONITOR (low power, low interest)
```

日本語：

MONITOR: 状況を見守る（影響力も関心度も低い）


### skills/stakeholder-alignment/scripts/power_interest_grid.py:45

原文：

```text
=== Power-Interest Stakeholder Grid ===

```

日本語：

=== 影響力・関心度による関係者マップ ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:59

原文：

```text

=== Coalition Math ===
```

日本語：

=== 支持連合の影響力を計算 ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:60

原文：

```text
Total power among supportive/champion stakeholders: 
```

日本語：

支持者/チャンピオン関係者間の総力:


### skills/stakeholder-alignment/scripts/power_interest_grid.py:61

原文：

```text
Total power among skeptical/opposed stakeholders:   
```

日本語：

懐疑的/反対する利害関係者の間の総力:


### skills/stakeholder-alignment/scripts/power_interest_grid.py:63

原文：

```text
>>> FLAG: opposed/skeptical power meets or exceeds supportive power.
```

日本語：

>>> 旗: 反対/懐疑的な勢力が支持的な勢力に匹敵するか、それを上回ります。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:64

原文：

```text
    Having more supportive NAMES doesn't matter if they don't carry
```

日本語：

支持者の人数が多くても、その人たちが持つ実質的な


### skills/stakeholder-alignment/scripts/power_interest_grid.py:65

原文：

```text
    more actual POWER. This needs a deliberate coalition-building plan
```

日本語：

影響力が大きくなければ意味がない。進める前に、


### skills/stakeholder-alignment/scripts/power_interest_grid.py:66

原文：

```text
    for the highest-power skeptical/opposed stakeholders before
```

日本語：

影響力が最も大きい懐疑・反対派を対象とする、意図的な支持連合づくりの計画が必要である。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:67

原文：

```text
    proceeding — not just broader 'stakeholder communication.'
```

日本語：

単に「関係者への情報発信」を広げるだけでは足りない。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:69

原文：

```text
Supportive coalition currently holds more power than opposition —
```

日本語：

現在は支持連合の影響力が反対派を上回っているが、


### skills/stakeholder-alignment/scripts/power_interest_grid.py:70

原文：

```text
still worth a specific plan for the highest-power skeptics individually.
```

日本語：

最も強力な懐疑論者向けに、個別に具体的な計画を立てる価値は依然としてある。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:72

原文：

```text

=== Engagement Strategy by Quadrant ===
```

日本語：


=== クアドラント別のエンゲージメント戦略 ===


### skills/stakeholder-alignment/scripts/power_interest_grid.py:73

原文：

```text
MANAGE CLOSELY : involve directly in decisions, address concerns personally.
```

日本語：

MANAGE CLOSELY: 意思決定に直接参加してもらい、懸念に個別に対応する。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:74

原文：

```text
KEEP SATISFIED : minimal detail, but don't surprise them — they can block
```

日本語：

KEEP SATISFIED: 詳細の説明は最小限にしつつ、不意打ちを避ける。反感を買えば、


### skills/stakeholder-alignment/scripts/power_interest_grid.py:75

原文：

```text
                 even with low day-to-day interest if provoked.
```

日本語：

日常的な関心度が低くても、この層は進行を阻止できる。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:76

原文：

```text
KEEP INFORMED  : regular updates; they can become advocates if engaged well.
```

日本語：

KEEP INFORMED: 定期的に情報を伝える。うまく関与してもらえば支援者になり得る。


### skills/stakeholder-alignment/scripts/power_interest_grid.py:77

原文：

```text
MONITOR        : light-touch, periodic check-in only.
```

日本語：

モニター : ライトタッチ、定期チェックインのみ。


