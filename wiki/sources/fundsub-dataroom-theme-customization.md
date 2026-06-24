---
type: source
title: "Theme Customization for FundSub and Data Room — Internal Guide"
date_ingested: 2026-05-11
as_of_date: 2025-09-08
source_type: implementation-guide
trust_level: 2
original_file: notion://2653f653-b1df-80e0-a0f9-d96aa43747cc
products: [Fundsub, Data Room]
target_audience: CS
onboarding_required: No
tags: [fundsub, data-room, branding, white-labeling, #implementation]
---

## Summary
Internal CS guide for configuring environment-level theme (brand color) customization for FundSub and Data Room. CS sets custom brand colors in iTools via the White Label > Theme Editor; changes apply platform-wide to all funds and data rooms in the environment. Includes setup workflow, accessibility validation requirements, and FAQs.

## Key Takeaways
- **Scope**: applies to FundSub and/or Data Room per environment. IDM and Investor Portal are not yet supported.
- **What's customizable**: primary brand color set (5 colors: Primary1–Primary5). Drives buttons, links, and key UI highlights. Not applicable to Badge, Callout, Stepper, Tag, Toast, or Well components (retain semantic colors).
- **Setup workflow in iTools**: Environment > White label > Theme editor → input 5 HEX colors or use auto-generator with a single accent color → choose Default or Neutral gray set → preview/validate → publish.
- **Gray sets**: Default (has blue tint, Anduin default), Neutral (more versatile; recommended for most customers, especially warm-toned brands).
- **Accessibility validation required**: Primary4/5 must pass WCAG AA contrast (≥4.5:1 white on color); Primary1/2 must pass AA (≥4.5:1 black on color).
- **Environment-level only**: all funds and data rooms in the same environment share one theme. No per-fund customization.
- **Customer self-service**: not available. All theme changes must go through CS via iTools.
- **Dark mode**: not supported. Light theme only.
- **Rollback**: reset to defaults in iTools and republish (reverts to Anduin blue).
- **Font/layout changes**: not part of theme customization — escalate to Product.
- **KKR example**: Primary5 `#46124A`, Primary4 `#49004B`, Primary3 `#9F5A9F`, Primary2 `#C7B1C8`, Primary1 `#F2EDF2`.

## Connections
- [[products/fundsub|FundSub]]
- [[products/data-room|Data Room]]

## Conflicts & Supersessions
No conflicts. First theme/white-labeling configuration guide ingested.

## Raw Notes
- As-of date derived from screenshot timestamps (2025-09-08) in the guide.
- Parent Notion context: originated from product feedback workspace > 2025 > "Customize color on all pages at platform level".
- References a Theme Editor overview deck: https://presentations.anduin.design/theme-editor
