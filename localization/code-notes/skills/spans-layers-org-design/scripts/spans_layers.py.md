# skills/spans-layers-org-design/scripts/spans_layers.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/spans-layers-org-design/scripts/spans_layers.py)

### skills/spans-layers-org-design/scripts/spans_layers.py:2

原文：

```text

Spans & Layers calculator: measures average span of control by management
layer, flags layers with an inefficiently narrow span against a benchmark,
and prices the annual cost of carrying more layers than the benchmark
organization design would need.

Usage:
    python3 spans_layers.py --config org.json

org.json shape:
{
  "benchmark_span_by_layer_type": {"executive": 5, "middle_management": 6, "frontline_management": 8},
  "avg_fully_loaded_manager_cost": 145000,
  "layers": [
    {"layer_number": 1, "title": "C-suite", "layer_type": "executive", "manager_count": 1, "direct_reports": 6},
    {"layer_number": 2, "title": "VPs", "layer_type": "executive", "manager_count": 6, "direct_reports": 22},
    {"layer_number": 3, "title": "Directors", "layer_type": "middle_management", "manager_count": 22, "direct_reports": 68},
    {"layer_number": 4, "title": "Managers", "layer_type": "middle_management", "manager_count": 68, "direct_reports": 210},
    {"layer_number": 5, "title": "Team leads", "layer_type": "frontline_management", "manager_count": 90, "direct_reports": 340}
  ]
}

```

日本語：

スパンと階層の計算ツール。管理階層ごとに管理者1人当たりの平均直属部下数（管理スパン）を測定し、基準と比べて非効率に狭い階層を検出する。基準となる組織設計で必要な数を超える階層を維持する年間コストも見積もる。

使用例：

```sh
python3 spans_layers.py --config org.json
```

設定JSONの構造（キーと値は原文表記を保持）：

```json
{
  "benchmark_span_by_layer_type": {"executive": 5, "middle_management": 6, "frontline_management": 8},
  "avg_fully_loaded_manager_cost": 145000,
  "layers": [
    {"layer_number": 1, "title": "C-suite", "layer_type": "executive", "manager_count": 1, "direct_reports": 6},
    {"layer_number": 2, "title": "VPs", "layer_type": "executive", "manager_count": 6, "direct_reports": 22},
    {"layer_number": 3, "title": "Directors", "layer_type": "middle_management", "manager_count": 22, "direct_reports": 68},
    {"layer_number": 4, "title": "Managers", "layer_type": "middle_management", "manager_count": 68, "direct_reports": 210},
    {"layer_number": 5, "title": "Team leads", "layer_type": "frontline_management", "manager_count": 90, "direct_reports": 340}
  ]
}
```

benchmark_span_by_layer_typeは階層種別ごとの基準スパン、avg_fully_loaded_manager_costは諸経費込みの管理者1人当たりコスト、layersは各階層の人数・部下数などを指定する。


### skills/spans-layers-org-design/scripts/spans_layers.py:46

原文：

```text
=== Spans & Layers Analysis ===

```

日本語：

=== スパンとレイヤーの分析 ===


### skills/spans-layers-org-design/scripts/spans_layers.py:47

原文：

```text
Avg Span
```

日本語：

平均スパン


### skills/spans-layers-org-design/scripts/spans_layers.py:58

原文：

```text
managers needed at benchmark span vs actual managers = excess
```

日本語：

実際の管理者数と、基準スパンで必要な管理者数との差が過剰人数となる。


### skills/spans-layers-org-design/scripts/spans_layers.py:64

原文：

```text

Total managers across all layers: 
```

日本語：


すべての層にわたる合計マネージャー:


### skills/spans-layers-org-design/scripts/spans_layers.py:65

原文：

```text
Total layers: 
```

日本語：

合計レイヤー:


### skills/spans-layers-org-design/scripts/spans_layers.py:66

原文：

```text
Total individual contributors (below lowest layer): 
```

日本語：

一般担当者の総数（最下層の管理者より下にいる非管理職）：


### skills/spans-layers-org-design/scripts/spans_layers.py:69

原文：

```text

Estimated excess management positions (actual vs. benchmark span): 
```

日本語：


推定過剰管理ポジション（実績対ベンチマーク・スパン）:


### skills/spans-layers-org-design/scripts/spans_layers.py:70

原文：

```text
Estimated annual cost of excess layers: 
```

日本語：

余分なレイヤーの推定年間コスト:


### skills/spans-layers-org-design/scripts/spans_layers.py:74

原文：

```text

>>> FLAG: 
```

日本語：


>>> フラグ:


### skills/spans-layers-org-design/scripts/spans_layers.py:74

原文：

```text
 layer(s) have spans meaningfully narrower than
```

日本語：

階層で、管理スパンが基準より明らかに狭い。


### skills/spans-layers-org-design/scripts/spans_layers.py:75

原文：

```text
    benchmark. This usually means either genuine complexity that justifies
```

日本語：

通常は、より細かな監督が必要になるほど業務が実際に複雑であるか、


### skills/spans-layers-org-design/scripts/spans_layers.py:76

原文：

```text
    closer supervision, or organizational layering added for reasons other
```

日本語：

実際に必要な管理スパンとは別の理由で組織階層が


### skills/spans-layers-org-design/scripts/spans_layers.py:77

原文：

```text
    than actual span requirements (legacy structure, title inflation, avoiding
```

日本語：

追加されたことを意味する（過去から残る組織構造、役職の増加、難しい


### skills/spans-layers-org-design/scripts/spans_layers.py:78

原文：

```text
    a difficult consolidation conversation). Confirm which before acting.
```

日本語：

組織統合の議論を避けることなど）。対処する前にどちらなのかを確認する。


### skills/spans-layers-org-design/scripts/spans_layers.py:80

原文：

```text

No layers flagged as meaningfully narrow versus benchmark.
```

日本語：


ベンチマークに対して有意に狭いとフラグが立てられたレイヤーはありません。
