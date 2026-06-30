---
type: feature
title: "Branded Landing Pages"
parent_product: "Engagement Hub"
status: GA
source_count: 6
last_updated: 2026-06-30
tags: [engagement-hub, landing-page, investor-engagement, branding]
---

## What it does
Branded Landing Pages are the self-service, fully white-labeled investor-facing pages at the core of [[products/engagement-hub|Engagement Hub]]. GPs build private, permissioned pages to showcase fund opportunities, share resources and data rooms, surface subscription workflows, and present high-level reporting — all under the firm's own branding and (optionally) its own custom domain. The number of *published* landing pages is the metering unit for Engagement Hub pricing.

> **Note:** This page consolidates what was previously the standalone "Landing Page" product. Per the Engagement Hub sources, Branded Landing Pages are a feature *of* Engagement Hub, not a separate product. The [[products/landing-page]] entry now redirects here.

## Also known as / naming history
- **"Landing page" = "Branded Landing Page" = the same thing.** "Landing page" is just shorthand; the full name is Branded Landing Page. (Watch context: people sometimes say "landing page" when they mean the whole Engagement Hub bundle — but the feature itself is the Branded Landing Page.)
- **Originally "IDM Branding"** — the internal working name when the feature was first introduced (Oct 2024) before "Branded Landing Page" was adopted.
- **Repackaged under Engagement Hub (Aug 2025).** Marketing initially proposed renaming Branded Landing Page → "Engagement Hub" outright; the final outcome was that Branded Landing Page became **one of four features** within the Engagement Hub solution (alongside Inbox, Document Sharing, and Profile Sharing) rather than a straight rename.
- Source: [[sources/engagement-hub-naming-history-slack]] (internal Slack, low trust — naming/history only).

## How it works
- **Self-serve web builder** — full control over page content; ready-to-use templates; intuitive DIY UX, no technical skills needed.
- **Deep white-labeling** — customize every brand element, not just a logo (website and landing-page styling).
- **Custom / white-label URLs** — apply your own domain and meaningful per-page paths (e.g. `invest.ada-capital.com/#/Fintech-Fund-III`).
- **Invitation & permission** — send invitation emails to selected contacts; generate invite links with pre-defined permissions per investor group; fine-tune which contacts can access which pages.
- **Granular access controls** — ensure the right audience sees the right page; tailor experiences per audience group while maintaining security.
- **Publish lifecycle** — draft pages are unlimited and free; a page only "counts" once published (visible to LPs); pages can be unpublished or retired to drop back under tier limits. **Publish before navigating away in the builder — unsaved changes are silently discarded.**

### Custom vs. System pages
- **Custom pages** (firm homepage, fund pages) — fully editable, access-gated; built for differentiated storytelling per fund/opportunity.
- **System pages** (Resources, Documents, Inbox, Profile) — auto-populated from each investor's permissions, always-on, zero upkeep; color-themeable (separate System Pages theming modal that auto-generates complements — review for contrast) and can be **unpublished** if unused.

### Two-level access control + three mechanisms
- **Two levels:** (1) which **pages** a contact can reach; (2) which **dynamic content/widgets** (subscriptions, data rooms, opportunities, reporting) render inside — filtered in real time by that investor's permissions. "Same login screen, completely different experience."
- **Three ways to grant page access:** **direct** (manual per-contact), **invitation link** (shareable; optional password + expiry), and **auto access** (syncs with investment relationships via the contact matrix — the only one that scales; used for reporting pages).

### Demo-prep mechanics
- **Set global brand colors first** (three Primary slots in Site Settings) — every linked widget across all pages updates automatically (no per-page recoloring). Replace logo / set max-height / hide irrelevant nav items; swap unavailable imagery for solid brand-color sections.

## Use cases
- Market funds early — showcase funds in advance and collect IOIs to gauge demand / pre-filter.
- Fund marketing & onboarding — opportunities plus resources and the subscription workflow.
- High-level fund/portfolio reporting pages.
- Co-branded pages with advisors and wealth managers.
- Polished co-investment opportunities for hand-picked investors.
- Advisory committee engagement via member-only permissioned spaces.

## Pricing & availability
- Part of [[products/engagement-hub|Engagement Hub]]; the **published-page count** drives EH's tier (Starter ≤5 / Growth ≤10 / Unlimited). See [[sources/engagement-hub-pricing]].
- Bundled into [[products/investor-portal|Investor Portal]] by default.
- Sellable as a standalone SKU but not recommended (first-year discount, year-2 increase).

## Known limitations
- Exceeding the tier limit doesn't block publishing but triggers an RM/CS upgrade alert; no single add-on pages are sold.
- Reporting *dashboards* surfaced via pages are an Investor Portal capability, not EH.

## Sources
- [[sources/engagement-hub-product-overview]] — capability detail (spec, trust 1)
- [[sources/engagement-hub-pricing]] — published-page metering (pricing, trust 3)
- [[sources/engagement-hub-one-pager]] — positioning (one-pager, trust 10)
- [[sources/engagement-hub-naming-history-slack]] — naming & repackaging history (internal Slack, note, trust 10)
- [[sources/landing-page-concepts-training-video]] — concepts & positioning (cs-training, trust 6)
- [[sources/landing-page-customize-demo-training-video]] — demo customization walkthrough (cs-training, trust 6)

## Related
- [[products/engagement-hub]] — parent product
- [[products/investor-portal]] — bundles this feature
- [[products/data-room]] — embedded within landing pages
- [[features/investor-portal-reporting-dashboards]] — the "dynamic reporting" referenced in landing-page packaging (Portal-only)
- [[features/idm-contacts]] — contact matrix that powers auto access
- [[concepts/product-packaging-bundling]] — Portal/EH/standalone tiers & page-cap upsell
- [[concepts/investor-onboarding-workflow]]
