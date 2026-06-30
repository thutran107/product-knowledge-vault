---
type: feature
title: "Reporting Dashboards (Datasets → Widgets → Pages)"
parent_product: "Investor Portal"
status: beta
source_count: 3
last_updated: 2026-06-30
tags: [investor-portal, implementation, integration]
---

## What it does
A flexible, manager-defined performance-reporting system that lets a GP structure their own data (IRR, MOIC, capital accounts, transactions) and present it to investors with automated, permission-aware access. It is **Investor Portal–only** — explicitly *not* part of [[products/engagement-hub|Engagement Hub]] — and is built on the IDM data layer.

## How it works
A three-layer architecture — **integrate once, present everywhere:**

| Layer | Role |
|-------|------|
| **Datasets** | Structured tables anchored to a **core object** (investment or transaction today; investment entities / fund vehicles roadmapped). Flexible user-defined schema; **master** (latest snapshot) vs. **time-series** (composite key core object + date, preserves history). |
| **Widgets** | Visualizations of a dataset. **Table widget is live; charts/line/pie/metrics are "near future."** One dataset feeds many widgets. |
| **Pages** | Landing-page compositions embedding widgets; inherit branded-landing-page flexibility; page-level access control serves different cohorts (LP tiers, co-investors, RPs). |

- **Auto-access permissioning:** a record is visible only if the contact has access to the underlying **investment object** *and* holds the **Financial Data permission** in their contact matrix — no manual row-level ACLs ("keep the contact matrix updated and permissioning happens automatically"). Record access and page access are decoupled; internal (admin) vs. external (investor) tracks are separate.
- **Versioning:** **draft / published / backup** — publishing promotes draft to live and preserves the prior state as a revertable backup.
- **Ingestion:** manual entry + **API live; spreadsheet import in progress.** Datasets refresh at any frequency → fresher-than-quarterly data; **RPs** can pull via API instead of parsing quarterly Excel/PDFs.
- **Table widget controls:** column show/hide/reorder/group/resize, permission-scoped **total row**, default + multi-column sort, conditional row styling, row-click navigation (context travels via column→filter mapping), **URL-parameter deep-linking**, custom disclaimer, custom no-access state.
- **Investor experience** is manager-configured: consolidated vs. segmented pages, selective data exposure, entity/capital-account filtering, always-available data download.

## Use cases
Live portfolio-holdings view with performance metrics; transaction drilldowns; cohort-specific reporting pages; API/deep-linked data feeds for placement agents.

## Pricing & availability
Investor Portal package only. The gating **Financial Data permission** is itself Portal-exclusive — see [[concepts/product-packaging-bundling]]. First iteration (tables) framed as a **March** release; charts/metrics and metric *computation* later (year inferred 2026).

## Known limitations
- **Tables only at launch**; charts/line/pie/metric widgets roadmapped.
- **Performance metrics must be imported, not computed** (computation "later").
- **Spreadsheet import in progress** — manual entry or API only at launch (API needs technical lift many firms lack).

## Sources
- [[sources/investor-portal-reporting-overview-training-video]] — architecture + investor experience (cs-training, trust 6)
- [[sources/investor-portal-reporting-datasets-training-video]] — datasets overview + details (cs-training, trust 6)
- [[sources/investor-portal-reporting-pages-widgets-training-video]] — pages & table widgets (cs-training, trust 6)

## Related
- [[products/investor-portal]] — parent product
- [[products/engagement-hub]] — reporting is the key Portal-only capability *not* in EH
- [[features/idm-contacts]] — the contact matrix + Financial Data permission that drives reporting access
- [[features/idm-funds-tab]] — core objects (investment/transaction) the datasets anchor to
- [[concepts/product-packaging-bundling]] — Portal-exclusive gating
- [[concepts/integration-patterns]] — "integrate once, present everywhere"
