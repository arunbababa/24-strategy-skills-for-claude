---
name: value-realization
description: Closes the loop that every other financial-case skill in this pack opens — checks realized results against the original business case, full-potential diagnostic, or synergy case line by line, and attributes the gap to assumption error, execution, or external shock. Use whenever the user wants a post-implementation review, wants to check if an initiative or deal actually delivered its promised value, or has a past business case, full-potential diagnostic, or synergy case that's never been checked against what actually happened.
---

# 価値の実現確認

> [英語原文](../../../skills/value-realization/SKILL.md)

> **description 日本語訳:** このパックの他の財務計画スキルが始めた検証を完結させる。実現結果を元の事業計画・最大改善余地診断・シナジー計画と項目別に比べ、差分を前提の誤り・実行・外的ショックへ帰属する。実施後レビュー、施策・取引が約束した価値を生んだかの確認、実際の結果と照合されていない過去の計画があるときに使う。

## 使用する場面
事業計画・最大改善余地診断・シナジー計画の承認から6〜18か月後、実際に成果を出したか確認するために使う。予測を作る `business-case-builder`・`full-potential-diagnostic`・`synergy-case-builder` は、この工程なしでは結果に責任を持つ循環がない。最終的な実現確認がない事業計画は、誤っても誰も責任を負わず、次第に楽観的になりやすい。

## 実行すること
元の予測の要因別の数値を、同じ粒度の実績と比較する。重要な差異を、前提の誤り・実行の不足・外的ショックへ具体的に帰属する。施策が方向は順調で遅れているだけか、本当に軌道を外れているかを明確に述べ、その発見を組織の今後の計画作成へ反映する。

## 方法
1. **見出しの総額でなく、元の予測を要因別で取得する。** `business-case-builder`・`full-potential-diagnostic`・`synergy-case-builder` が作ったのと同じ粒度にする。
2. **同じ要因別粒度・同じ期間の実績を集める。** 同条件で比較できるようにする。
3. **最終収支だけでなく、要因ごとの差異を求める。** 基礎要因がそれぞれ別方向に外れていても、誤りの相殺で総額は良好に見えることがある。
4. **重要な差異ごとに原因を1つ付ける。** 前提の誤り（入力が最初から間違っていた。既存の `assumption-audit` と照合）、実行の不足（前提は合理的だが実現が不足）、外的ショック（合理的に予測できる範囲外）に分ける。
5. **判定を明確に述べる。** 方向は順調だが予定より遅い（新たな判断でなく日程修正が必要）のか、本当に軌道を外れている（継続・調整・中止の実質的な判断が必要）のかを示す。
6. **繰り返す原因を実務へ戻す。** 過去のレビューで前提の誤りが繰り返し出るなら、上流の `assumption-audit` が省略されているか軽すぎる兆候である。業務改善事項として明示する。

## 入力
- 要因別の詳細を含む元の予測（事業計画・最大改善余地診断・シナジー計画）
- 同じ粒度・同じ期間の実績
- あれば、元の計画の `assumption-audit` の発見

## 出力形式
要因別の予測対実績と差異。重要差異ごとの原因帰属。順調だが遅延か、軌道逸脱かの明示的判定。将来の計画作成へ戻す、プロセス上の学び1つ。

## 例
18か月以内に NPV 300万ドルを見込んだ施策を12か月目にレビューする。売上は計画比15%未達で、楽観的すぎる転換率という前提の誤りが原因である。一方、費用は計画より10%少なく、実行上の成功である。合計 NPV は概ね順調に見えるが、最終収支がたまたま良好だから計画が検証されたと宣言せず、売上要因の未達を再検討すべき本当の兆候として挙げる。

## よくある落とし穴
- 最終収支だけを確認し、要因別の誤りの相殺で偶然健全な総額が生まれることを見逃す。
- 元の前提が現実的だったか確かめず、あらゆる未達を実行の失敗とする。
- 資金承認を得る役目を果たしたらレビューを省き、将来のすべての計画の結果責任の循環を断つ。
