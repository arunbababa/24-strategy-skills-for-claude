# skills/negotiation-prep/scripts/batna_zopa.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../skills/negotiation-prep/scripts/batna_zopa.py)

### skills/negotiation-prep/scripts/batna_zopa.py:2

原文：

```text

BATNA / ZOPA calculator: computes the zone of possible agreement between
your reservation price and the counterparty's estimated reservation price,
recommends an anchor, and flags when no ZOPA exists (in which case the
right move is walking away or changing the deal structure, not negotiating
harder on price).

Usage:
    python3 batna_zopa.py --config negotiation.json

negotiation.json shape:
{
  "role": "buyer",
  "your_target_price": 400000,
  "your_batna_value": 480000,
  "counterparty_estimated_reservation_price": 460000,
  "counterparty_estimated_target_price": 420000
}
role: "buyer" or "seller". your_batna_value is what you get if this deal
falls through (your best alternative) — for a buyer, your reservation
price should never exceed your BATNA value; for a seller, it should never
go below it.

```

日本語：

BATNA / ZOPA計算ツール。自分の留保価格（取引を受け入れられる限界価格）と相手の推定留保価格の間にある合意可能領域を計算し、最初の提示額（アンカー）を提案する。ZOPAがない場合も検出する。その場合は価格交渉をさらに強めるのではなく、交渉を離脱するか取引の構造を変える。

使用例：

```sh
python3 batna_zopa.py --config negotiation.json
```

設定JSONの構造（キーと値は原文表記を保持）：

```json
{
  "role": "buyer",
  "your_target_price": 400000,
  "your_batna_value": 480000,
  "counterparty_estimated_reservation_price": 460000,
  "counterparty_estimated_target_price": 420000
}
```

roleは"buyer"（買い手）または"seller"（売り手）。your_batna_valueはこの取引が成立しない場合に得られる最良の代替案の価値。買い手の留保価格はBATNAの価値を超えてはならず、売り手の留保価格はBATNAの価値を下回ってはならない。


### skills/negotiation-prep/scripts/batna_zopa.py:46

原文：

```text
=== BATNA / ZOPA Analysis ===

```

日本語：

=== BATNA / ZOPA 分析 ===


### skills/negotiation-prep/scripts/batna_zopa.py:47

原文：

```text
Your role: 
```

日本語：

あなたの役割:


### skills/negotiation-prep/scripts/batna_zopa.py:48

原文：

```text
Your target price: 
```

日本語：

あなたの目標価格:


### skills/negotiation-prep/scripts/batna_zopa.py:49

原文：

```text
Your BATNA value (walk-away point): 
```

日本語：

あなたのBATNA値（ウォークアウェイポイント）:


### skills/negotiation-prep/scripts/batna_zopa.py:50

原文：

```text
Counterparty's estimated reservation price: 
```

日本語：

相手の推定留保価格：


### skills/negotiation-prep/scripts/batna_zopa.py:53

原文：

```text
never pay more than your BATNA
```

日本語：

BATNAを超える支払いは決してしないでください


### skills/negotiation-prep/scripts/batna_zopa.py:54

原文：

```text
seller won't go below their reservation
```

日本語：

売り手は自分の留保価格を下回る価格を受け入れない。


### skills/negotiation-prep/scripts/batna_zopa.py:55

原文：

```text
you won't go above yours
```

日本語：

買い手である自分は、自分の留保価格を超える価格を受け入れない。


### skills/negotiation-prep/scripts/batna_zopa.py:57

原文：

```text

Your implied reservation price (should not exceed BATNA): 
```

日本語：

算定される自分の留保価格（BATNAを超えてはならない）：


### skills/negotiation-prep/scripts/batna_zopa.py:59

原文：

```text
never sell for less than your BATNA
```

日本語：

BATNA を下回って販売しないでください


### skills/negotiation-prep/scripts/batna_zopa.py:63

原文：

```text

Your implied reservation price (should not go below BATNA): 
```

日本語：

算定される自分の留保価格（BATNAを下回ってはならない）：


### skills/negotiation-prep/scripts/batna_zopa.py:66

原文：

```text

ZOPA (Zone of Possible Agreement): 
```

日本語：

ZOPA（合意可能領域）：


### skills/negotiation-prep/scripts/batna_zopa.py:68

原文：

```text
ZOPA midpoint: 
```

日本語：

ZOPA中間点:


### skills/negotiation-prep/scripts/batna_zopa.py:72

原文：

```text

Recommended opening anchor: 
```

日本語：

推奨する最初の提示額（アンカー）：


### skills/negotiation-prep/scripts/batna_zopa.py:73

原文：

```text
As buyer, anchor near or slightly below your target, but inside the ZOPA
```

日本語：

買い手として、ターゲットの近くまたはわずかに下、ただし ZOPA の内側にアンカーします。


### skills/negotiation-prep/scripts/batna_zopa.py:74

原文：

```text
so the opening offer is taken seriously rather than dismissed as a bad-faith move.
```

日本語：

したがって、最初のオファーは悪意のある動きとして無視されるのではなく、真剣に受け止められます。


### skills/negotiation-prep/scripts/batna_zopa.py:77

原文：

```text

Recommended opening anchor: 
```

日本語：

推奨する最初の提示額（アンカー）：


### skills/negotiation-prep/scripts/batna_zopa.py:78

原文：

```text
As seller, anchor near or slightly above your target, but inside the ZOPA.
```

日本語：

売り手として、ターゲットの近くまたは少し上、ただし ZOPA の内側にアンカーします。


### skills/negotiation-prep/scripts/batna_zopa.py:80

原文：

```text

Your walk-away price: 
```

日本語：

自分が交渉から離脱する価格：


### skills/negotiation-prep/scripts/batna_zopa.py:80

原文：

```text
 (this is your BATNA, not a
```

日本語：

（これは自分のBATNAであり、交渉上の


### skills/negotiation-prep/scripts/batna_zopa.py:81

原文：

```text
negotiating tactic — going past it means the deal destroys value versus your
```

日本語：

駆け引きではない。この限界を超える取引は、話し合いの場でどれほど好感触でも、


### skills/negotiation-prep/scripts/batna_zopa.py:82

原文：

```text
actual alternative, regardless of how the conversation feels in the room).
```

日本語：

実際の代替案と比べて価値を損なう。）


### skills/negotiation-prep/scripts/batna_zopa.py:85

原文：

```text

>>> NO ZOPA EXISTS. Your reservation price and the counterparty's estimated
```

日本語：

>>> ZOPAは存在しない。自分の留保価格と相手の推定


### skills/negotiation-prep/scripts/batna_zopa.py:86

原文：

```text
    reservation price do not overlap by an estimated 
```

日本語：

留保価格の間には、推定で次の金額の隔たりがある：


### skills/negotiation-prep/scripts/batna_zopa.py:87

原文：

```text
    Negotiating harder on price will not close a gap this size. Either:
```

日本語：

価格交渉を厳しくしても、これほどの差は埋まりません。次のいずれか:


### skills/negotiation-prep/scripts/batna_zopa.py:88

原文：

```text
    (a) the deal should not happen at current terms, walk away to your BATNA,
```

日本語：

(a) 現在の条件で取引を行うべきではありません。BATNA へ立ち去り、


### skills/negotiation-prep/scripts/batna_zopa.py:89

原文：

```text
    (b) change the deal structure (financing, timeline, scope) to create value
```

日本語：

(b) 価値を生み出すために取引構造 (資金調達、スケジュール、範囲) を変更する


### skills/negotiation-prep/scripts/batna_zopa.py:90

原文：

```text
        that shifts one side's reservation price, or
```

日本語：

一方の留保価格を変える、または


### skills/negotiation-prep/scripts/batna_zopa.py:91

原文：

```text
    (c) your estimate of their reservation price may be wrong — verify before
```

日本語：

(c) 相手の留保価格の推定が誤っているかもしれないため、


### skills/negotiation-prep/scripts/batna_zopa.py:92

原文：

```text
        concluding no deal is possible.
```

日本語：

合意不可能だと結論づける前に確認する。


### skills/negotiation-prep/scripts/batna_zopa.py:95

原文：

```text

Counterparty's estimated target price: 
```

日本語：

相手の推定目標価格：


### skills/negotiation-prep/scripts/batna_zopa.py:96

原文：

```text
Treat this as the number they'll open near, not what they'll actually accept.
```

日本語：

これは、相手が最初に提示しそうな額として扱う。実際に受け入れる限界額とは区別する。
