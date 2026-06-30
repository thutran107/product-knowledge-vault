---
type: feature
title: "IDM Public API & Integration"
parent_product: "IDM"
status: GA
source_count: 1
last_updated: 2026-06-30
confidence: medium
tags: [idm, integration, implementation]
---

## What it does
A bidirectional REST API (plus webhooks) that connects IDM to external systems — CRMs (Salesforce), data warehouses (Snowflake, GCP), and SFTP. It turns IDM from a central database into integration infrastructure by moving data **both inward** (CRM records pre-populate subscriptions) and **outward** (post-close investment data lands in the warehouse), eliminating manual export/re-entry/reconciliation.

## How it works
- **Two directions, one closed loop:** **invitation** (inbound — invite + pre-fill from CRM) and **retrieval** (outbound — push IDM data to downstream systems). Each delivers value alone; together they "close the loop."
- **Subscription pre-fill:** because IDM stores investor identity at the **entity level** (not transaction level), returning LPs get pre-populated subscription forms. Every fundraise enriches the profile that powers the next.
- **Webhooks** fire on meaningful state changes (signed doc, status update, closed investment) to keep Salesforce/warehouse records live without human intervention.
- **Data model = the API contract:** firm → client group → investment entity → fund legal entity → transaction, with **custom ID support** so external systems reference IDM records without migrating their own identifiers.
- **Setup:** a **service-account API key** issued by Anduin, **basic auth over HTTPS**, REST + webhook registration, and **production + sandbox** servers. **Trial keys expire after one month; production keys don't expire unless revoked.**

## Use cases
The four use cases that "cover ~90% of what GPs need": **CRM-driven invitations**, **centralized client reusability**, **continuous sync**, and **compliance monitoring**. Workflow benefit: the sales team never leaves Salesforce; the LP sees fewer fields to fill in.

## Pricing & availability
Presented as a standard IDM integration surface; no tier gating mentioned in the training video. Sits alongside the no-code [[products/integration-hub]] as the developer/API path.

## Known limitations
- **Trial key one-month expiry** will silently break a workflow if the team doesn't plan ahead for a production key.
- FundSub alone captures **transaction-level** data; investor-level structure (and thus reuse) requires IDM — the API is what exposes that structure to external systems.

## Sources
- [[sources/idm-public-api-training-video]] — Public API & Integration (cs-training, trust 6)

## Related
- [[products/investor-data-management|IDM]] — parent product
- [[products/integration-hub]] — no-code integration counterpart
- [[entities/salesforce]] — primary CRM target (invite + pre-fill, live sync)
- [[concepts/integration-patterns]]
- [[features/idm-contacts]] — API is one of the four contact-ingestion methods
