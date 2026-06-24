---
type: product
title: "Engagement Hub"
status: GA
source_count: 4
last_updated: 2026-06-16
tags: [engagement-hub, investor-engagement, sales-motion]
---

## What it does
Anduin Engagement Hub is an IDM-based investor engagement layer that gives a fund manager's LPs a single, branded, invite-only destination — one URL and one login — spanning fund marketing, document distribution, communications, and investor-profile management. It is positioned to "own the investor experience, from first touchpoint to post-close," replacing fragmented apps, logins, and insecure email threads with one secure hub. It sits between IDM (data) and the full [[products/investor-portal|Investor Portal]] (which adds a per-fund portal instance and reporting on top of EH).

> **Naming & history:** Engagement Hub launched publicly on **Aug 27, 2025** as a repackaging of the **Branded Landing Page** product (originally called *"IDM Branding"* internally, Oct 2024). Rather than renaming Branded Landing Page outright, Anduin made it **one of four features** within the Engagement Hub solution — alongside Inbox/Communication, Document Sharing, and Profile Sharing. So "landing page" / "branded landing page" refers to that one feature, while "Engagement Hub" is the full bundle. See [[sources/engagement-hub-naming-history-slack]].

## Key capabilities
- **Branded Landing Pages** — self-service web builder; per-purpose pages with granular access controls; deep white-labeling and custom/white-label URLs; invitation emails and permissioned invite links per investor group. (See [[features/engagement-hub-branded-landing-pages]].)
- **Document Distribution** — GPs distribute announcements, newsletters, and fund-level reports to selected investors with watermarking, permissions, and audit trails; LPs get a centralized, searchable document repository. *Document activity tracking* (views/downloads, engagement, reminders) was roadmapped for Q2.
- **Communication (centralized inbox)** — all GP communications sent from IDM captured in one inbox with context-rich linkage to funds/entities/documents; fully customizable newsletter email templates. *In-app Q&A center* (2-way) roadmapped for Q4 2026.
- **Profile Sharing** — LPs view the data and documents the GP shares (view live since Dec 2025); LPs can request profile updates that apply only after GP review/approval (roadmapped Q3 2026); supports reusing GP-owned investor profiles for new subscriptions.

## Landing-page use cases
Market funds early (collect IOIs to gauge demand/pre-filter); fund marketing & onboarding (opportunities + resources + subscription workflow); high-level portfolio reporting; co-branded pages with advisors/wealth managers; polished co-investment sharing with hand-picked investors; advisory committee engagement via member-only permissioned spaces.

## Pricing & packaging
Pricing as of **2025-09-18** (see [[sources/engagement-hub-pricing]]). Annual subscription, **three tiers metered by number of *published* landing pages**:

| Tier | Published landing pages |
|------|------------------------|
| Starter | up to 5 |
| Growth | up to 10 |
| Unlimited | unlimited |

- **30% beta discount** at launch; full pricing expected late 2026 / early 2027 as more engagement functionality ships. (Exact dollar figures per tier are a known data gap — on a slide table not yet captured.)
- **Published vs. draft:** only published pages (visible to LPs) count; drafts are free; pages can be unpublished/retired to drop back under the limit; usage is visible in Anduin.
- **Exceeding the limit:** publishing continues; an automated alert prompts RM/CS to upgrade to the next tier; no single add-on pages are sold.
- **Standalone landing pages:** sellable as a standalone SKU but **not recommended** — offer a first-year discount, with a year-2 increase once value is proven.
- **Relationship to Portal pricing:** Portal buyers get EH bundled by default (referred to as the "Ultimate"/top tier); new Portal pricing = annual EH fee + a (lower) annual per-fund Portal fee. See the flagged conflict on [[products/investor-portal]].

## Implementation notes
- Built on the **IDM Firm space** — IDM is the data foundation for EH.
- **Enablement (internal):** Production via **iTools > IDM > Portal Package**; a demo sandbox path also exists.
- The EH / Portal / IDM packages all share the same IDM Firm space but expose different feature sets (see matrix below).

## Feature matrix (EH / Portal / IDM)

| Package | What it adds (all on IDM Firm space) |
|---------|--------------------------------------|
| **IDM only** | Investor data (Client, Fund, Contact); custom profile & AML/KYC management & CSA |
| **Engagement Hub** | Branded Landing Pages, Communication (inbox), Profile Sharing, Document Distribution |
| **Investor Portal** | Everything in EH **plus** the per-fund Portal instance & Reporting dashboards |

> **Reporting Dashboards are Portal-only** — explicitly *not* part of Engagement Hub.

## Known limitations
- **No reporting/analytics dashboards** — those are an Investor Portal capability.
- **Document activity tracking** was roadmapped (Q2) — confirm GA status.
- **Profile update requests** (LP-initiated, GP-approved) roadmapped Q3 2026; **in-app Q&A** Q4 2026; **news feed & engagement analytics** TBD.
- **Tier naming inconsistency** across source decks ("Ultimate tier" vs. published Starter/Growth/Unlimited) — clarify the canonical bundled tier with product.
- **Exact tier pricing** not yet captured from the pricing deck.

## Features & sub-modules
- [[features/engagement-hub-branded-landing-pages]] — Branded Landing Pages (the metered, self-service web-builder feature; folded in from the former Landing Page product).

## Related customers
None documented yet.

## Sources
- [[sources/engagement-hub-product-overview]] — capability authority (spec, trust 1) ⭐
- [[sources/engagement-hub-pricing]] — pricing authority (pricing, trust 3) ⭐
- [[sources/engagement-hub-one-pager]] — marketing positioning (one-pager, trust 10)

## Related
- [[products/investor-portal]] — Portal = EH + per-fund instance + Reporting; EH bundled into Portal by default
- [[products/investor-data-management]] — IDM Firm space is EH's data foundation
- [[products/data-room]] — embedded in landing pages; EH is distinguished from the Data Room homepage in objection handling
- [[products/fundsub]] — subscription workflows surfaced through EH landing pages
- [[concepts/product-packaging-bundling]] — lead-with-bundles sales motion
- [[concepts/investor-onboarding-workflow]]
