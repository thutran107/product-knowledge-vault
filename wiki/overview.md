---
type: overview
last_updated: 2026-05-04
source_count: 13
---

# Product Knowledge Library — Overview

## What This Knowledge Base Covers
Anduin's Integration Hub product — its architecture, integration patterns, implementation playbook, and how it connects the Anduin product suite (FundSub, Data Room, IDM, Investor Access) to third-party systems (DealCloud, Affinity, Box, Salesforce).

---

## The Core Product: Integration Hub

The [[wiki/products/integration-hub|Integration Hub]] is Anduin's self-service platform for configuring, managing, and monitoring integrations. Its goal is to reduce pre-sales friction and implementation time by enabling customers to discover and activate integrations without deep technical support.

**Key architectural ideas:**
- [[wiki/concepts/anduin-object-model|Anduin Object Model]]: integrations connect to specific objects (funds, firms, data rooms) — not to organizations broadly.
- [[wiki/concepts/configuration-vs-permission|Configuration vs Permission]]: the Hub manages configuration; individual Anduin apps enforce permissions.
- [[wiki/concepts/user-roles|User Roles]]: Admins (all GP users in the same email domain) and Members (external consultants).

---

## The Three Integration Patterns

All integrations in the Hub follow one of three patterns (see [[wiki/concepts/integration-patterns|Integration Patterns]]):

| Pattern | Direction | Example |
|---------|-----------|---------|
| Order Creation | CRM → FundSub | DealCloud/Affinity → invite investor + prefill form |
| Data Retrieval | Anduin → CRM | FundSub/Data Room → sync data back to CRM |
| Document Retrieval | FundSub → Storage | FundSub → Box folder |

---

## Integrations Available (as of current sources)

| Integration | Pattern | CRM/System |
|-------------|---------|-----------|
| DealCloud (Order creation) | Order Creation | DealCloud |
| DealCloud (Data retrieval) | Data Retrieval | DealCloud |
| DealCloud (Data Room alert) | Data Retrieval | DealCloud + Data Room |
| Affinity (Order creation) | Order Creation | Affinity |
| Box | Document Retrieval | Box |

---

## How Data Flows

The [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]] is the central use case:

```
CRM (DealCloud / Affinity)
  → [Order Creation] → FundSub (subscription created, form prefilled, investor invited)
  → [Data Retrieval] → CRM (completed subscription data synced back)
  → [Document Retrieval] → Box/SFTP (signed documents transferred)
```

Data fidelity depends on [[wiki/concepts/import-export-templates|Import/Export Templates]] and [[wiki/concepts/data-mapping|Data Mapping]] — both configured during integration setup.

---

## Anduin Products in This Knowledge Base

| Product | Role |
|---------|------|
| [[wiki/products/fundsub|FundSub]] | Core subscription platform; destination for Order Creation, source for Data/Document Retrieval |
| [[wiki/products/data-room|Data Room]] | Investor document access; source for engagement data integrations |
| [[wiki/products/investor-data-management|IDM]] | Centralized investor data repo; enables reusable investor profiles |
| [[wiki/products/investor-access|Investor Access]] | Referenced in Neuberger Berman deployment; minimal documentation |

---

## Key Customer: Neuberger Berman

[[wiki/customers/neuberger-berman|Neuberger Berman]] ($460B AUM) deployed the full Anduin stack: FundSub + Data Room + IDM + Investor Access + Integration Hub. Used IDM to create reusable investor profiles and Salesforce integration for subscription tracking. Result: ~3,000 LPs onboarded, $5.4B raised. See [[wiki/sources/neuberger-berman-case-study|case study]].

---

## Onboarding Essentials

Must-read documents for new CS and Sales hires. Sources tagged `onboarding_required: Yes`:

| Source | Type | Audience |
|--------|------|----------|
| [[wiki/sources/ih-implementation-guide\|IH Implementation Guide (Internal CS Playbook)]] | implementation-guide | CS |
| [[wiki/sources/ih-implementation-guide-pdf\|IH Implementation Guide (PDF)]] | implementation-guide | CS |

*This section is maintained automatically during ingest (Step 8 of ingest workflow).*

---

## What's Not Yet Covered

- Sales Deck (PDF not yet ingested)
- Integration Hub Implementation Guide PDF (not yet ingested)
- Salesforce integration details (only mentioned, not documented)
- SFTP Document Retrieval integration
- Investor Access product detail
- Data Room permission management in Integration Hub (listed as TBD in docs)
- Self-service Import Templates (not yet available)
