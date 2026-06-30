---
type: feature
title: "IDM Contacts & Communication Matrix"
parent_product: "IDM"
status: GA
source_count: 1
last_updated: 2026-06-30
tags: [idm, implementation, data-management, pricing]
---

## What it does
The contact model lets a firm store each person **once** and link them, many-to-many, to any number of clients and investment entities. The **communication matrix** then controls — per investment, per communication type — exactly what each contact receives. It replaces the scattered spreadsheets and institutional memory most firms use to manage who-gets-what.

## How it works
- **Single source of truth:** one contact record, keyed by **email** (the immutable unique identifier — no two contacts share one; changing it requires a new record). Updating a detail propagates everywhere the contact is linked.
- **Communication matrix:** a per-investment, per-communication-type permission grid (capital calls, K-1s, distribution notices, etc.). Communication types are customizable at firm level.
- **Three views, one record:** firm-wide All Contacts dashboard, client-level view, IE contact tab.
- **Four ingestion methods:** manual, bulk spreadsheet import, automatic FundSub sync (**requires digitization-team involvement**), and public API (e.g., Salesforce).
- **Matrix setup auto-creates an investment** only if none exists between an IE and a fund; once one exists you can only select existing investments — new ones must be created in the Fund tab first.
- **Client-level preferences** (e.g., Profile Access, **Auto Assign**) propagate and **lock** all current and future child entities unless switched to **Custom**. Auto Assign makes new entities inherit contacts by default.
- **Bulk management from parent views:** client-view *Access Controls* and IE-view *Edit Communication Matrix*.
- **Contact lists:** reusable mailing groups (a contact can belong to many); target a list instead of selecting recipients individually.
- **Removal is non-destructive** — affects future access only.
- **Engagements / Pages tabs are read-only** (edits happen upstream in the owning apps).

## Use cases
- Maintain one investor-relations contact graph across all funds, eliminating redundant per-fund lists.
- Targeted distribution of documents/communications via lists and communication-type filtering.
- Auto-assign contacts to new entities to prevent "added to an entity but never received the reports" errors.

## Pricing & availability
Everything in the contact model is available at the **base IDM tier — except** the **Financial Data permission** column. That column sits inside the communication matrix but governs a contact's access to **dynamic reports on the Investor Portal**, and is **exclusively available in the Investor Portal package**. Treat any lower-tier client asking about it as an **upgrade conversation**, not a configuration question. See [[concepts/product-packaging-bundling]].

## Known limitations
- **Email immutability** — a corrected email means a new contact record, a constraint to surface before bulk onboarding.
- The matrix-edit flow **cannot create a new investment** once any investment exists for the IE×fund pair (must detour to the Fund tab).

## Sources
- [[sources/idm-contacts-training-video]] — Contacts concepts + demo (cs-training, trust 6)

## Related
- [[products/investor-data-management|IDM]] — parent product
- [[products/investor-portal]] — Financial Data permission gates Portal report access
- [[features/idm-clients-tab]] — contacts link to clients and IEs
- [[sources/investor-portal-contact-management]] — Portal-side contact-management deep dive
- [[concepts/product-packaging-bundling]] — the Portal-exclusive permission as an upsell gate
