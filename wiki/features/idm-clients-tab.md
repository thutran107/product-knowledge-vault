---
type: feature
title: "IDM Clients Tab (Investor Profiles & Records)"
parent_product: "IDM"
status: GA
source_count: 1
last_updated: 2026-06-30
tags: [idm, implementation, data-management, compliance]
---

## What it does
The Clients tab is IDM's single source of truth for every investor relationship — clients, investment entities, profiles, documents, and risk assessments. It is the foundation everything else in IDM depends on: "this is the most important tab… where we store everything investor related."

## How it works
- **Mandatory creation hierarchy:** client → investment entity (IE) → profile → documents. No single template collapses the steps.
- **IDM profiles** are custom forms scoped per client; the proven scoping technique is to **anchor to the client's existing subscription agreement** as a baseline, then layer on CRM/risk fields (clients can't answer "what data do you want to track?" in the abstract).
- **Master profile** consolidates overlapping + unique fields across multiple funds into one profile; build timeline is **variable** and shouldn't be committed to upfront.
- **DG (data governance) mapping:** the back-end team completes **form-to-form field mapping** for each *historical* fund before data imports correctly; **all future funds map automatically** once IDM is live (pain front-loaded by design).
- **Bulk import is strictly sequential** (clients → IEs → profiles → documents → risk assessments), each from a separate template.
- **Auto-sync status limits:** after initial manual import, IDM auto-syncs back only for **submitted / countersigned / distributed** investors; pending/in-progress are manual.
- **Documents tab:** AI scanning activates only for **pre-configured document types**; a **document-name exact-match rule** means slight name differences create duplicate records. New **batch expiration-date alignment** feature.
- **Investor-chosen profile at subscription:** investors self-select their IE via a profile-selection banner (funds often don't know which entity a returning LP will use).
- **Risk assessments:** batch-create across multiple IEs with proof docs + audit trail.
- **Custom exports:** fully configurable extracts (e.g., per-investor tax reports); custom IDs at client and IE levels.

## Use cases
- Establish a firm-wide "golden source of truth" for investor data (cf. Neuberger Berman).
- Cross-fund commitment overview per IE — "something only IDM can provide at the moment."
- Compliance/document tracking with expiration management and renewal visibility.
- Clean up duplicate profiles via the client-merging feature without losing history.

## Pricing & availability
Core IDM capability. Custom IDM profiles and KYC/AML management are not included in Portal-only (no-IDM-add-on) packages — see [[products/investor-portal]] packaging.

## Known limitations
- **No automated anniversary reminders** for risk assessments yet — the next-cycle prompt is a manual responsibility ("not yet").
- Historical-fund data only populates correctly **after** DG mapping; unmapped past funds won't pull through.
- The **All Contacts** tab here is largely a Portal feature, not core IDM — don't conflate.

## Sources
- [[sources/idm-clients-tab-training-video]] — Clients tab profiles/mapping/import (cs-training, trust 6)

## Related
- [[products/investor-data-management|IDM]] — parent product
- [[features/idm-funds-tab]] — the fund side; investments bridge clients ↔ FLEs
- [[features/idm-contacts]] — contacts link to clients and IEs
- [[concepts/data-mapping]] — DG form-to-form mapping & document exact-match
- [[concepts/investor-onboarding-workflow]]
