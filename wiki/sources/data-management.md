---
type: source
title: "Data Management"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Data management.md
products: [Integration Hub, FundSub]
target_audience: CS
onboarding_required: No
tags: [data-management, import, export, templates]
---

## Summary
Explains Anduin's two core data movement concepts — Import (external → Anduin for form prefill) and Export (Anduin → external for post-subscription data retrieval) — and how Templates define the data points involved in each.

## Key Takeaways
- **Import**: transfers external data into Anduin, converted to subscription/order information. Primary use: pre-populating subscription forms.
- **Export**: extracts subscription data from Anduin to external systems. Delivered as CSV or JSON.
- **Template**: a defined set of data points for a specific import or export. Either Import Template or Export Template.
- Import Templates enable data from external systems to be digested by Anduin for prefill.
- Export Templates format Anduin data into a standardized form for external systems.
- Templates are typically set up collaboratively between Anduin and the customer.
- Customers can now self-create Export Templates via FundSub dashboard (Import self-service not yet available).

## Connections
- [[concepts/import-export-templates|Import/Export Templates]] — concept page.
- [[concepts/data-mapping|Data Mapping]] — how fields are mapped between systems.
- [[products/fundsub|FundSub]] — where templates are managed.

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- "Integrations can require automated data flow between systems, which relies on Templates for successful execution."
- Self-service Export Template creation is available; Import templates still require Anduin collaboration.
