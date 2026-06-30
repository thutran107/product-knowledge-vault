---
type: source
title: "Investor Portal — Reporting: Pages & Widgets (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/reporting/5-pages-and-widgets/"
products: [Investor Portal]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation]
---

## Summary
Building reporting **pages** and **table widgets** — the presentation layers on top of datasets. Covers column management, the total row, default sorting, conditional formatting, row-click navigation, URL-parameter deep-linking, custom no-access messaging, and the composable widget model. Tables ship first; charts/metrics are roadmapped.

## Key Takeaways
- **Sequence dependency:** datasets → widgets → pages. "If no dataset has been created, you should create one first" — the most common first-time setup failure is building a widget with no backing dataset.
- **Tables now, charts later:** table widget is live; **charts, line charts, pie charts, metrics** are "near future." Every future widget follows the **same section-embed pattern** (learn once).
- **Column management:** show/hide, drag-reorder, group under merged headers, resize, remove; built-in search filtering.
- **Total row:** auto-aggregates (e.g., total commitment) **scoped to exactly what each investor is permitted to see** — no manual calc.
- **Default sort** (single + multi-column priority) so investors land on a table that already tells a story.
- **Conditional row styling:** rule-based, column-driven — encodes meaning visually without extra columns.
- **Row-click navigation:** clickable rows drill to a linked page; a column value binds to the destination page's filter so context travels with the click — turns a table into a workflow.
- **URL parameter handling:** encode a column value into the URL so external systems (email, CRM, third-party) deep-link an investor straight to a pre-filtered view — "a low-ceremony API for deep linking" configurable without engineering.
- **Custom disclaimer** (table footer) and **custom no-access state** (styled message + CTA) — the no-access screen is often a newly-onboarded investor's first impression.
- **Composable & embeddable:** reporting widgets behave like any landing-page widget — mix with non-reporting sections or embed externally. "Opinionated about architecture, unopinionated about layout."

## Connections
- Co-source for [[features/investor-portal-reporting-dashboards]].
- Widgets/pages sit atop datasets ([[sources/investor-portal-reporting-datasets-training-video]]) and inherit landing-page flexibility from [[features/engagement-hub-branded-landing-pages]].

## Conflicts & Supersessions
- No conflict. Configuration-level detail beneath the Portal reporting feature.

## Raw Notes
- 7:21 / 10 sections. "Unknown" date.
