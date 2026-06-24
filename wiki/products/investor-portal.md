---
type: product
title: "Investor Portal"
status: GA
source_count: 9
last_updated: 2026-06-10
tags: [investor-portal, investor-access, sales-motion]
---

## What it does
Anduin Investor Portal is a unified, GP-branded investor communication platform that spans from pre-marketing through post-close. It gives LPs a single destination for documents, communications, reporting, and profile management, while giving fund managers self-service tools to distribute documents, manage contacts, and run financial reporting — all tied into the Anduin platform's IDM, Data Room, FundSub, and Integration Hub.

## Key capabilities
- **Customizable branded home page** — drag-and-drop section templates (hero banner, about us, teams, fund widgets); Anduin widgets surface pending tasks and recent documents; mobile-friendly; changes publish instantly.
- **Vehicle landing pages** — per-fund customizable pages; promote upcoming vehicles to existing LPs; integrated Data Room per vehicle with granular permissions and analytics.
- **Advanced white-label email** — firm-branded email design presets by type; customizable headers/footers; test email previews.
- **Document distribution** — three methods: Group Share (same docs to a group), Private Share (AI maps files to correct IEs by filename/content), Split & Share (one merged PDF → split → AI maps to IEs). All methods support comm type filtering, email templates, placeholders, watermarks, and scheduled delivery.
- **Centralized document library** — all LP documents in one place; new/unseen files highlighted; search and filter by vehicle, doc type; batch download.
- **Inbox** — all GP communications captured with document context; LP-accessible; read/unread tracking.
- **Tasks** — auto-created on capital calls and events; deadlines with automated reminders; multi-party completion tracking.
- **Financial reporting** — 3-layer modular framework: (1) fund-defined datasets (GP controls structure and columns; row permissions inherit from contact matrix), (2) flexible display widgets (tables, charts, numbers), (3) audience-specific reporting pages (control who sees what). Data available via direct dashboard download or optional investor-side API access.
- **Contact management** — granular contact matrices per (Investment Entity × Fund × Communication Type); batch updates across entities/funds; self-service investor profile view for contacts and wire info.
- **Integration Hub connectivity** — no-code integrations connect Portal with CRM, data room, FundSub, and other systems.

## Pricing & packaging
Pricing as of May 2025. Annual fee per fund/SPV, tiered by AUM; plus one-time data migration fee.

| AUM Tier | Annual / Fund | Annual / SPV | Migration / Fund | Migration / SPV |
|----------|--------------|-------------|-----------------|----------------|
| Emerging ($0–250M) | $6K | $2K | $5K | $1K |
| Established ($250M–1B) | $8K | $2K | $5K | $1K |
| Enterprise ($1B–15B) | $15K | $3K | $7.5K | $1.5K |
| Baby Whale ($15–50B) | $20K | $4K | $7.5K | $1.5K |
| Adult Whale ($50–100B) | $20K | $4K | $7.5K | $1.5K |
| Super Whale ($100B+) | $30K | $6K | $10K | $2K |

**Beta discount (Y1/Y2 early customers):** 50% off list price in Y1, 25% off in Y2, no discount Y3+.

**Fund and SPV defined** the same as FundSub — Fund = fund family (single or multiple vehicles); SPV = small standalone vehicle (single investment, co-invest, SMA).

**Bundle recommendation:** Sell Portal + IDM + Landing Pages + Integration Hub together. Portal-only customers get Standard IDM Profile + Custom Contact Matrix + API but not Custom IDM, KYC/AML management, or Branded Landing Pages for marketing.

If customer already has FundSub + IDM: keep existing pricing, add Portal fees on top.

See [[sources/investor-portal-pricing-faqs-boston]] for full pricing detail and beta prospect proposals.

> ⚠️ **Pricing structure conflict (flagged, unresolved).** The Engagement Hub decks ([[sources/engagement-hub-pricing]], pricing/trust 3, as-of 2025-09-18; and [[sources/engagement-hub-product-overview]], as-of 2026-02-02) state Portal pricing is being **restructured** to **"annual Engagement Hub platform fee + a *lower* annual per-fund Portal fee."** Those sources are newer than the Boston pricing deck above (as-of 2025-05-14), so per §10 the *structure* is superseded. Per user decision, the AUM table above is **retained as-is** and the conflict flagged here rather than overwritten — the EH decks did **not** include the actual new per-fund figures (data gap). Treat the table above as the legacy structure; confirm current numbers with the EH/Portal pricing slides before quoting to a client. EH is bundled into Portal by default (top/"Ultimate" tier). See [[concepts/product-packaging-bundling]].

## Implementation notes
Onboarding sequence: Kickoff call (30 min) → IDM setup → Portal setup → Data migration → Live training (1 hr) → Customer testing → Go live.

**Pre-condition:** Customer must be familiar with IDM concepts (Fund Family, FLE, Client, IE, Contact Matrix, Communication Types) before Portal live training.

**Key setup steps:**
1. Create Fund Family and/or Fund Legal Entities in IDM
2. Add Clients, Investment Entities, and Contacts; establish communication matrices
3. Configure Communication Types at firm level; enable per fund
4. Set up Portal home page and vehicle landing pages (self-service editor)
5. Configure email templates and design presets
6. Test LP experience with a test Contact account
7. Invite actual investors via Landing Pages → Page Access → Notify contact

**Bulk import** available for large contact onboarding (spreadsheet import for clients, IEs, and contacts).

See [[sources/investor-portal-customer-training-guide]] for detailed CS training script.

## Known limitations
- **Reporting dashboards** were not in the initial MVP; available post-launch (live data as of Q1 2026 for capital account + transaction details).
- **Profile updates** (investor edits to contact matrix/wire info) are Q2 2026.
- **Document split markers** — AI-powered detection; manual override available.
- **Portal-only (no IDM add-on):** Limited to Standard IDM Profile, Custom Contact Matrix, API. No Custom IDM, KYC/AML.
- **Portal-only (no Landing Pages):** Portal home page is included but Branded Landing Pages for marketing new funds are not.

## 2026 Roadmap
- Q1: Advanced Email Customization, Public API
- Q2: Reporting — Transactions & capital movements; Portfolio & performance metrics
- Q3: Documents & Engagements analytics; Profiles sharing for contact & wire info updates
- Q4: Portal AI Agents

## Competitive positioning
Direct competitors are standalone investor portals: [[competitors/investorflow]] and [[competitors/atominvest]]. Anduin's differentiation:
- End-to-end platform (onboarding → portal → data room → IDM → Integration Hub) vs. point solutions
- Superior UX/branding customization
- Existing customer base on FundSub/IDM makes portal adoption lower friction
- Pricing is competitive vs. InvestorFlow for Enterprise/Whale; higher than AtomInvest at Enterprise but justified by full bundle

See [[sources/investor-portal-pricing-faqs-boston]] for competitive pricing benchmarks.

## Features & sub-modules
- [[sources/investor-portal-contact-management]] — Contact Management deep dive
- Financial Reporting (3-layer framework — see sources)
- Document Distribution (Group Share / Private Share / Split & Share)

## Related customers
- PFG (Principal Financial Group) — beta prospect, $30K/fund/yr × 12 funds = $360K/yr ARR target
- Sands Capital — beta prospect, Enterprise tier
- BlueArc, Nimble, NewVest, Dauntless — beta prospects (see pricing source for details)

## Sources
- [[sources/investor-portal-sales-deck]] — primary capabilities deck (sales-deck, trust 5)
- [[sources/investor-portal-pricing-faqs-boston]] — pricing authority (pricing, trust 3) ⭐
- [[sources/investor-portal-gtm-primer]] — market context & acquisition targets (gtm-training, trust 5)
- [[sources/investor-portal-product-overview]] — competitive category overview (note, trust 10)
- [[sources/investor-portal-rfp]] — RFP template (rfp, trust 11, metadata only)
- [[sources/investor-portal-prerelease-training-boston]] — Boston Popup GTM training (metadata only)
- [[sources/investor-portal-customer-training-guide]] — CS implementation training (client-training, trust 7)
- [[sources/investor-portal-contact-management]] — Contact Management spec (spec, trust 1) ⭐
- [[sources/investor-portal-training-materials]] — training materials bundle (metadata only)
- [[sources/anduin-investor-guide-may-2025]] — LP-facing guide (client-training, trust 7)

## Related
- [[products/engagement-hub]] — Portal = Engagement Hub + per-fund instance + Reporting; EH is bundled into Portal by default
- [[products/investor-data-management]] — IDM is prerequisite; contact matrix and data profiles shared
- [[products/data-room]] — embedded in vehicle landing pages
- [[products/fundsub]] — onboarding feeds into Portal; pricing kept separate
- [[features/engagement-hub-branded-landing-pages]] — branded landing pages (formerly the "Landing Page" product) used for fund marketing
- [[products/integration-hub]] — Portal connectivity layer
- [[concepts/product-packaging-bundling]] — EH/Portal/IDM packaging & pricing motion
- [[concepts/investor-onboarding-workflow]]
- [[competitors/investorflow]]
- [[competitors/atominvest]]
