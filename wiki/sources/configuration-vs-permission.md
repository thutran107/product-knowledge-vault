---
type: source
title: "Configuration vs Permission"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Configuration vs permission.md
products: [Integration Hub, FundSub, IDM, Data Room]
target_audience: CS
onboarding_required: No
tags: [integration-hub, permissions, architecture]
---

## Summary
Explains the architectural separation between Integration Hub (which manages configuration) and individual Anduin apps (which enforce permissions). A user can only automate data flows for objects they have permission to access in the underlying app.

## Key Takeaways
- Integration Hub = manages integration setup and configuration.
- Each Anduin app (FundSub, IDM, Data Room) = enforces its own permission rules independently.
- "Anduin Object" terminology: a fund in FundSub, a firm in IDM, a data room in Data Room.
- Permission is granted per-object: you must explicitly grant each integration access in the relevant app's Settings > Integrations.
- FundSub and IDM both expose a Settings > Integrations page for this purpose; Data Room support is TBD.
- Once permission is granted, the Integration Hub shows the object with a "Linked" tag.

## Connections
- [[concepts/configuration-vs-permission|Configuration vs Permission]] — concept page for this pattern.
- [[concepts/anduin-object-model|Anduin Object Model]] — defines the objects referenced.
- [[products/integration-hub|Integration Hub]], [[products/fundsub|FundSub]], [[products/investor-data-management|IDM]], [[products/data-room|Data Room]].

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- The Hub shows a list of Anduin objects the user has permission for; clicking "Open" takes them to the relevant app to grant permission.
- Data Room permission management listed as "TBD" in the source.
