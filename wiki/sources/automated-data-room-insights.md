---
type: source
title: "Automated Data Room Insights Retrievals (DealCloud)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Automated data room insights retrievals.md
products: [Integration Hub, Data Room]
target_audience: CS
onboarding_required: No
tags: [integration, dealcloud, data-room, crm-sync]
---

## Summary
Describes the DealCloud (Data Room alert) integration that automatically syncs investor engagement data from Anduin Data Rooms into the customer's DealCloud CRM, providing real-time visibility into investor activity.

## Key Takeaways
- Pattern: **Data Retrieval** — Data Room → DealCloud CRM.
- Tracks: investor invitations, joins, document views, and downloads.
- Historical backfill on first run based on a configurable "Initial Backfill Period (Days)."
- Subsequent runs are real-time event-driven (not batch).
- Configurable event filtering: customers choose which investor activities to track.
- Target persona: Data Room customers using DealCloud as their CRM.
- Prerequisites: DealCloud API key + pre-created DealCloud object with ~20 specific fields (all text type).
- DealCloud object must include fields: DataroomID, DataroomName, FirstName, LastName, Email, Domain, GroupName, LastAction, FileID, FileName, Viewed, Downloaded, etc.
- All mapped fields must use text type — numeric/picklist types break the integration.

## Connections
- [[concepts/integration-patterns|Integration Patterns]] — Data Retrieval pattern.
- [[entities/dealcloud|DealCloud]] — the target CRM.
- [[products/data-room|Data Room]] — the Anduin source.
- [[concepts/configuration-vs-permission|Configuration vs Permission]].

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- One of the most field-heavy integrations — requires ~20 specific fields on the DealCloud object.
- Event filter options: Invited, Joined, Viewed, Downloaded.
