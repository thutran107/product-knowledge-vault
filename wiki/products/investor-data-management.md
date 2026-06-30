---
type: product
title: "Investor Data Management (IDM)"
status: GA
source_count: 18
last_updated: 2026-06-30
tags: [idm, anduin, investor-data, crm]
---

## What it does
IDM is Anduin's centralized investor-data layer — a firm-level source of truth for investment entities, contacts, documents, profiles, and fund/capital records. It exists to collapse investor data scattered across multiple systems into one authoritative layer that every fund, product, and integration draws from. It is sold not as a standalone database but through **three workflows**: **onboarding** (collect data once, reuse it across every future fundraise), **compliance** (track and renew AML/KYC), and **integrations** (a single connection point out to a CRM or data warehouse).

> One-sentence definition (field-ready): *"IDM is the centralized investor data layer that powers reuse through onboarding, tracking through compliance, and provides a single integration point out to the client's CRM or warehouse."*

## Key capabilities
- **Clients tab** — single source of truth for investor relationships: clients → investment entities → IDM profiles → documents; master profiles across funds; risk assessments; custom exports; cross-fund commitment view. See [[features/idm-clients-tab]].
- **Funds tab** — fund/capital structure and cash-flow ledger: fund subscription → fund legal entity (FLE) → investment → transaction, with automatch sync and Awaiting Sync controls. See [[features/idm-funds-tab]].
- **Contacts & communication matrix** — one firm-wide contact record (keyed by email) linked many-to-many to clients/entities; per-investment, per-communication-type permission grid; contact lists. See [[features/idm-contacts]].
- **Public API & integration** — bidirectional REST API + webhooks (invite/pre-fill inbound, retrieval/sync outbound) to CRMs and warehouses; subscription pre-fill for returning LPs. See [[features/idm-public-api]].
- **Firm settings** — white-labeling (logos, header colors) and email sender configuration (Anduin server vs. custom SMTP). See [[features/idm-firm-settings]].
- **Reusable investor profiles** — eliminate re-entry of the same information for each new subscription.

## Pricing & packaging
Sold via workflow, typically bundled with FundSub / Portal / Integration Hub rather than standalone. Key packaging boundary: the **Financial Data permission** (which gates a contact's access to dynamic Investor Portal reports) is **Investor Portal–package exclusive** — base IDM exposes the full contact matrix *except* that column. Portal-only customers (no IDM add-on) get Standard IDM Profile + Custom Contact Matrix + API but **not** Custom IDM or KYC/AML management. See [[concepts/product-packaging-bundling]].

## Implementation notes
- **Scope before demo.** Four variables drive every implementation: client type, engagement scenario (existing fund client / new client with fundraise / combination case), CRM presence, and **sequencing priority** ("which must be ready first — the fundraise or IDM?"). Getting these wrong "leads to months of remapping and redesigning profiles."
- **Single vs. multiple IDM.** Because IDM does not yet support granular fund-level access controls within one environment, any client with separate teams that must not see each other's data requires **multiple IDM environments**.
- **DG mapping is front-loaded.** Historical funds need back-end form-to-form mapping before data imports correctly; all future funds map automatically once IDM is live. See [[concepts/data-mapping]].
- **Creation order is mandatory:** client → investment entity → profile → documents (no single-pass template).
- **Profile scoping technique:** anchor to the client's existing subscription agreement, then layer on CRM/risk fields — clients can't answer "what data do you want?" in the abstract.
- **Auto-sync status limits:** only submitted / countersigned / distributed investors sync back automatically; pending/in-progress are manual.
- Settings > Integrations exposes permission grants (same pattern as FundSub).

## Known limitations
- **No granular fund-level access control** within a single IDM environment (drives multi-IDM deals for clients with team-level data boundaries).
- **No automated risk-assessment anniversary reminders** yet (manual follow-up).
- **Email is an immutable contact identifier** — correcting it requires a new contact record.
- **Document-name exact-match** — slight name differences create duplicate document records.
- Master-profile build timelines are variable and shouldn't be committed to upfront.

## Features & sub-modules
- [[features/idm-clients-tab|Clients Tab (Investor Profiles & Records)]]
- [[features/idm-funds-tab|Funds Tab (Fund Structure & Capital Flow)]]
- [[features/idm-contacts|Contacts & Communication Matrix]]
- [[features/idm-public-api|Public API & Integration]]
- [[features/idm-firm-settings|Firm Settings — White-Labeling & Email/SMTP]]

## Related customers
- [[customers/neuberger-berman|Neuberger Berman]] — used IDM to establish a "golden source of truth" for investor data (CRM integration with Salesforce required a documented data standard).

## Sources
- [[sources/idm-feature-documentation|IDM Feature Guide Library]] *(spec, trust 1 — authoritative feature reference)*
- [[sources/idm-implementation-guide|IDM Internal Implementation Guide]] *(trust 2)*
- [[sources/idm-introduction-training-video|IDM — Introduction (training video)]] *(cs-training, trust 6)*
- [[sources/idm-clients-tab-training-video|IDM — Clients Tab (training video)]] *(cs-training, trust 6)*
- [[sources/idm-funds-tab-training-video|IDM — Funds Tab (training video)]] *(cs-training, trust 6)*
- [[sources/idm-contacts-training-video|IDM — Contacts (training video)]] *(cs-training, trust 6)*
- [[sources/idm-public-api-training-video|IDM — Public API & Integration (training video)]] *(cs-training, trust 6)*
- [[sources/idm-settings-training-video|IDM — Settings Part 1: White-Labeling & SMTP (training video)]] *(cs-training, trust 6)*
- [[sources/idm-gtm-training|IDM GTM Training]]
- [[sources/idm-client-training|IDM Client Training Deck]]
- [[sources/idm-sales-brochure|IDM Sales Brochure]] *(as-of 2024-08-01)*
- [[sources/idm-release-notes|IDM Release Notes]] *(running log)*
- [[sources/idm-release-notes-sprint-362|IDM Sprint 362 Release Notes]] *(2025-09-16)*
- [[sources/idm-fundsub-onboarding-deck-oct2025|IDM + FundSub Onboarding Deck]] *(Oct 2025 — preferred)*
- [[sources/idm-fundsub-investor-onboarding-may-2025|IDM + FundSub Onboarding Deck — May 2025]] *(superseded)*
- [[sources/neuberger-berman-case-study|Neuberger Berman Case Study]]
- [[sources/configuration-vs-permission|Configuration vs Permission]]
- [[sources/mission-and-core-components|Mission and Core Components]]

## Related
- [[products/fundsub|FundSub]] — onboarding intake; IDM stores investor-level data FundSub captures at transaction level
- [[products/investor-portal|Investor Portal]] — IDM is the data foundation; Financial Data permission gates Portal reports
- [[products/engagement-hub|Engagement Hub]] — built on the IDM Firm space
- [[products/integration-hub|Integration Hub]] — no-code counterpart to the IDM public API
- [[entities/salesforce|Salesforce]]
- [[concepts/anduin-object-model|Anduin Object Model]]
- [[concepts/data-mapping|Data Mapping]]
- [[concepts/investor-onboarding-workflow|Investor Onboarding Workflow]]
- [[concepts/product-packaging-bundling|Product Packaging & Bundling]]
