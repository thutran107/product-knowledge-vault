---
type: source
title: "IDM — Public API & Integration (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/idm-public-api/"
products: [IDM, Integration Hub]
target_audience: CS | Sales + RM
onboarding_required: No
tags: [idm, integration, implementation]
---

## Summary
Positions IDM's **public API** as the connector that "closes the loop" between IDM and external systems (Salesforce, Snowflake, GCP, SFTP). Data flows **both directions** — inward (CRM records pre-populate subscriptions) and outward (post-close investment data lands in the data warehouse) — eliminating manual reconciliation. Covers the data-model-as-API-contract, four core use cases, two live demos (invite-and-pre-fill, data sync), and lightweight service-account setup.

## Key Takeaways
- **Bidirectional = the whole point.** "Each direction delivers value on its own. Together they close the loop entirely." One-way integration "leaves half the value on the table." The two directions are framed as **invitation** (inbound) and **retrieval** (outbound).
- **Subscription pre-fill for returning LPs.** Because IDM stores investor identity at the entity level (not the transaction level), returning LPs get pre-populated subscription forms — "no re-entry, no re-upload, no starting from scratch." Every fundraise enriches the profile that powers the next.
- **Webhook-driven real-time sync.** A meaningful state change (signed doc, status update, closed investment) fires a webhook that propagates to Salesforce / the warehouse "without exports, without copy paste, without manual reconciliation."
- **Data model is the API contract.** Hierarchy: **firm → client group → investment entity → fund legal entity → transaction**, with **custom ID support** so external systems can reference IDM records without migrating internal identifiers. (Note: FundSub captures *transaction-level* data; IDM exposes *investor-level* structure — that's the gap the API closes.)
- **Four use cases cover ~90%:** CRM-driven invitations, centralized client reusability, continuous sync, and compliance monitoring.
- **Low-ceremony setup:** a **service-account API key** delivered by the Anduin team, **basic auth over HTTPS**, REST + webhook registration, and **production + sandbox** servers. **Trial keys expire after one month**; production keys do not expire unless revoked — plan ahead so a trial key doesn't silently break a workflow.

## Connections
- Primary source for the new [[features/idm-public-api|IDM Public API & Integration]] feature page.
- Bidirectional/invite-retrieval model + Salesforce pre-fill connect to [[products/integration-hub]], [[entities/salesforce]], and [[concepts/integration-patterns]].
- Subscription pre-fill / profile reuse links to [[concepts/investor-onboarding-workflow]] and the IDM contact API ingestion path in [[sources/idm-contacts-training-video]].

## Conflicts & Supersessions
- No conflict. Complements the existing Salesforce integration material; adds the investor-level-vs-transaction-level framing and the service-account/key lifecycle detail.

## Raw Notes
- 6:16 / 10 sections. "Unknown" date.
- Named external systems: Salesforce (CRM), Snowflake / GCP (warehouse), SFTP.
- Design principle stated: "Manual reconciliation is a design smell."
