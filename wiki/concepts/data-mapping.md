---
type: concept
title: "Data Mapping"
source_count: 5
last_updated: 2026-06-30
tags: [data-mapping, integration, templates, configuration, idm]
---

## Definition
The process of specifying which fields in an external system (CRM, storage) correspond to which fields in Anduin (FundSub subscription, export template). Data mapping is a prerequisite for all integrations and is configured during the integration setup wizard.

## Key Dynamics

### Mapping UI in Integration Wizard
- Two-column interface: left = source system fields, right = Anduin template fields (or vice versa for export).
- Currently supports **1-to-1 mapping only** in the UI.
- Complex transformations (e.g., concatenating fields, conditional logic) require a Custom Template built with Anduin.

### Import Mapping (CRM → FundSub)
- Left: CRM fields (e.g., DealCloud object fields or Affinity list columns).
- Right: Anduin Import Template fields (ASA or Custom).
- Customer identifies which CRM data maps to which FundSub prefill fields.
- Contact fields (First Name, Last Name, Email) must be explicitly mapped for invitation sending.

### Export Mapping (FundSub → CRM)
- Left: Anduin Export Template fields.
- Right: CRM object fields.
- Customer specifies which subscription data points map to which CRM object fields.
- All CRM target fields must be text type — numeric/picklist types break the integration.

### IDM historical-fund mapping (DG form-to-form)
- Importing past subscription data into IDM requires the back-end **DG (data governance) team** to complete **form-to-form field mapping** for each *historical* fund before profiles populate correctly.
- **Front-loaded by design:** once IDM is live, **all future funds map automatically** — no further mapping configuration.
- An IDM setup request must therefore also **name which existing funds to map**; this is the most common onboarding miscommunication ("not just 'I want an IDM' — you also need to tell them which existing funds to map to").
- **Document-name exact-match rule:** the documents tab matches by exact name; the same KYC requirement appearing under two funds with even a slight name difference is stored as **two separate documents**, polluting the record. AI scanning only activates for pre-configured document types. See [[features/idm-clients-tab]].

### Data Mapping Prerequisites
- CRM object/list must be prepared with the correct fields before mapping (customer does this with Anduin guidance).
- Import/Export template must exist before mapping configuration.
- Unique ID field must be designated for deduplication.

## Evidence & Examples
- DealCloud Data Room integration requires ~20 specific fields — among the most complex mapping setups.
- DealCloud and Affinity Order Creation both use the same two-column mapping interface.
- Neuberger Berman's IDM integration with Salesforce required a "data standard" — essentially a documented mapping agreed upon across all fund types.

## Tensions & Open Questions
- UI is 1-to-1 only. Any transformation → Custom Template → Anduin dependency.
- No self-service Import Template yet — all import mapping requires Anduin involvement upfront.

## Related
- [[concepts/import-export-templates|Import/Export Templates]]
- [[concepts/integration-patterns|Integration Patterns]]
- [[entities/dealcloud|DealCloud]], [[entities/affinity|Affinity]]
- [[features/idm-clients-tab]] — IDM profile/import scoping & DG mapping
- [[sources/idm-clients-tab-training-video]]
