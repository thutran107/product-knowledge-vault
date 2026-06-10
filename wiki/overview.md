---
type: overview
last_updated: 2026-06-10
source_count: 75
---

# Anduin Product Knowledge Library — Overview

## What This Knowledge Base Covers
The authoritative internal reference for CS, Sales, and RM on **Anduin's full product suite** — what each product does, how it works, how it's priced, and how to implement, sell, and support it. The base spans **75 sources across 13 products**, from the LP onboarding/subscription stack (FundSub, E-signature, OCR Data Extraction, AAA) through the investor-data layer (IDM), the investor-engagement layer (Engagement Hub, Investor Portal, Data Room), and the connectivity layer (Integration Hub).

> *This overview was last re-synthesized 2026-06-10. Earlier versions described the base as Integration-Hub-only; that scope has long since broadened to the whole suite.*

---

## The Anduin Product Suite

Anduin's products form an end-to-end fund-administration platform — **market → onboard → sign → extract → manage data → engage investors**, all stitched together by the Integration Hub.

### Onboarding & subscription stack
| Product | Role | Sources |
|---------|------|---------|
| [[wiki/products/fundsub\|FundSub]] | Core fund-subscription platform: LPs complete sub forms & sign; GPs review/approve. The central Anduin Object most integrations read from or write to. Multi-structure, multi-jurisdiction, one-envelope signing. | 15 |
| [[wiki/products/e-signature\|E-signature]] | Three eIDAS tiers (SES/AES/QES). Native SES, GlobalSign AES, DocuSign+IDnow QES, and the Schwab custodian signing workflow. A fund picks Anduin-native **or** DocuSign — not both. | 7 |
| [[wiki/products/ocr-data-extraction\|OCR Data Extraction]] | Amazon Textract + human-augmented review to digitize sub forms, KYC packets, and fund docs; feeds the FundSub pipeline. Proposal-based pricing. | 11 |
| [[wiki/products/aaa\|AAA (Advisor Advantage)]] | GP-side interface for RIAs/advisor entities; assign/unassign subscriptions. Used by Cerity Partners in the Schwab flow. *(Thin — Batch 8 sources pending.)* | 1 |

### Investor data layer
| Product | Role | Sources |
|---------|------|---------|
| [[wiki/products/investor-data-management\|IDM]] | Firm-level repository of investment entities, contacts, documents, and reusable investor profiles — the "golden source of truth." The **data foundation** for both Engagement Hub and Investor Portal (all three share one IDM Firm space). | 12 |

### Investor engagement layer
| Product | Role | Sources |
|---------|------|---------|
| [[wiki/products/engagement-hub\|Engagement Hub]] | IDM-based engagement layer: Branded Landing Pages, document distribution, centralized inbox, profile sharing. **= Investor Portal minus the per-fund instance & reporting.** Metered by published landing pages. | 3 |
| [[wiki/products/investor-portal\|Investor Portal]] | GP-branded LP destination spanning pre-marketing → post-close: branded home + vehicle pages, document distribution, inbox, tasks, **financial reporting**, contact management. **= Engagement Hub + per-fund instance + Reporting.** | 9 |
| [[wiki/products/data-room\|Data Room]] | Secure document sharing with engagement tracking, granular/multi-group permissions, branding, and a Public API; embedded within Portal/EH landing pages. | 10 |
| [[wiki/products/investor-access\|Investor Access]] | LP-side access product; referenced in the Neuberger Berman deployment. *(Placeholder — no dedicated source yet.)* | 0/1 |

### Connectivity & platform
| Product | Role | Sources |
|---------|------|---------|
| [[wiki/products/integration-hub\|Integration Hub]] | Self-service platform to discover, install, and monitor integrations between Anduin products and third-party systems (DealCloud, Affinity, Salesforce, Box). Built on Integration Cards; powered by Prismatic. "20+ app integrations." | 14 |
| [[wiki/products/platform\|Platform]] | Cross-product base (object model, config-vs-permission, user roles). *(No dedicated source page.)* | 0 |
| [[wiki/products/side-letter\|Side Letter]] | In the product taxonomy; not yet documented. *(Placeholder.)* | 0 |
| [[wiki/products/landing-page\|Landing Page]] | **Deprecated / folded into Engagement Hub** as the [[wiki/features/engagement-hub-branded-landing-pages\|Branded Landing Pages]] feature. Page retained only as a redirect. | 0 |

---

## How Engagement Hub & Investor Portal Relate (the key packaging story)
All three engagement-tier products sit on the **same IDM Firm space** and expose progressively more:

| Package | Adds (on IDM Firm space) |
|---------|--------------------------|
| **IDM only** | Investor data (Client, Fund, Contact); custom profile & AML/KYC; CSA |
| **Engagement Hub** | Branded Landing Pages, Communication (inbox), Profile Sharing, Document Distribution |
| **Investor Portal** | Everything in EH **plus** the per-fund Portal instance & **Reporting dashboards** |

> Reporting dashboards are **Portal-only** — explicitly not part of Engagement Hub. EH is bundled into Portal by default (the top/"Ultimate" tier).

---

## The Three Integration Patterns
Every Integration Hub workflow follows one of three patterns (see [[wiki/concepts/integration-patterns|Integration Patterns]]):

| Pattern | Direction | Example |
|---------|-----------|---------|
| Order Creation | CRM → FundSub | DealCloud/Affinity → invite investor + prefill form |
| Data Retrieval | Anduin → CRM | FundSub/Data Room → sync subscription & engagement data back |
| Document Retrieval | FundSub → Storage | FundSub → Box/SFTP folder |

Documented integrations: **DealCloud** (order creation, data retrieval, Data Room alerts), **Affinity** (order creation), **Box** (document retrieval), **Salesforce** (→ Data Room onboarding, IDM sync). Data fidelity depends on [[wiki/concepts/import-export-templates|Import/Export Templates]] and [[wiki/concepts/data-mapping|Data Mapping]].

---

## Cross-Cutting Concepts (10)
- [[wiki/concepts/anduin-object-model|Anduin Object Model]] — integrations bind to objects (funds, firms, data rooms), not orgs broadly.
- [[wiki/concepts/configuration-vs-permission|Configuration vs Permission]] — the Hub manages configuration; individual apps enforce permissions.
- [[wiki/concepts/user-roles|User Roles]] — Admins (GP users sharing an email domain) vs. Members (external).
- [[wiki/concepts/integration-patterns|Integration Patterns]] · [[wiki/concepts/crm-integration-playbook|CRM Integration Playbook]] · [[wiki/concepts/data-mapping|Data Mapping]] · [[wiki/concepts/import-export-templates|Import/Export Templates]]
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]] — the central CRM → FundSub → CRM → storage flow.
- [[wiki/concepts/product-packaging-bundling|Product Packaging & Bundling]] — lead-with-bundles motion (Portal + IDM + Landing Pages + IH).
- [[wiki/concepts/qes-aes-compliance|QES/AES/SES Compliance]] — eIDAS signature-tier framework.

---

## Pricing Models (by product)
- **FundSub** — *Anduin Essentials* (Starter / Advanced tiers) for emerging managers; *Enterprise* unlocks multi-fund/flow + other modules. No public figures.
- **Investor Portal** — annual fee per fund/SPV, tiered by AUM ($6K–$30K/fund) + one-time migration fee; beta discount 50% Y1 / 25% Y2.
- **Engagement Hub** — annual, three tiers metered by *published* landing pages (Starter ≤5 / Growth ≤10 / Unlimited); 30% beta discount. **Exact dollar figures are a data gap.**
- **OCR Data Extraction** — proposal-based (Sales/RM build the proposal).
- **E-signature** — DocuSign SES/QES charged per signature credits (tracked in Salesforce).
- **Data Room** — sold within bundles; Salesforce→Data Room is a paid IH integration.

---

## ⚠️ Known Conflicts & Tensions
- **Portal vs. Engagement Hub pricing structure (unresolved).** Newer EH decks (as-of 2026-02-02 / 2025-09-18) say Portal pricing is being restructured to *"annual EH platform fee + a lower per-fund Portal fee,"* superseding the legacy AUM table on [[wiki/products/investor-portal]] — but the new per-fund figures were never captured. Per user decision the AUM table is retained and the conflict flagged. **Confirm current numbers before quoting.**
- **"Ultimate tier" vs. Starter/Growth/Unlimited** naming inconsistency across EH decks — clarify the canonical bundled tier with product.
- **OCR sales decks** — two entries point at the same Google Slides deck; rationalize.

---

## Customers
**Documented (with sources):** [[wiki/customers/neuberger-berman|Neuberger Berman]] ($460B AUM; full stack — FundSub + Data Room + IDM + Investor Access + IH; ~3,000 LPs, $5.4B raised), [[wiki/customers/cerity-partners|Cerity Partners]] (FundSub + AAA + E-signature Schwab flow), [[wiki/customers/accolade|Accolade Partners]] (Data Room + FundSub), [[wiki/customers/nxstep|NXSTEP]] (FundSub Essentials).

**Tracked but undocumented (0 sources):** [[wiki/customers/kkr|KKR]], [[wiki/customers/eqt|EQT]], [[wiki/customers/blackstone|Blackstone]], [[wiki/customers/hg-capital|Hg Capital]], [[wiki/customers/sequoia-heritage|Sequoia Heritage]], [[wiki/customers/clearlake|Clearlake]], [[wiki/customers/atalaya|Atalaya]], [[wiki/customers/audax|Audax]], [[wiki/customers/proskauer|Proskauer]], [[wiki/customers/stone-ridge|Stone Ridge]], [[wiki/customers/pag|PAG]], [[wiki/customers/oakley|Oakley]], [[wiki/customers/antler|Antler]].

---

## Competitors
- [[wiki/competitors/investorflow|InvestorFlow]] and [[wiki/competitors/atominvest|AtomInvest]] — standalone investor portals. Anduin differentiates on the end-to-end platform (onboarding → portal → data room → IDM → IH), branding/UX, and lower-friction adoption for existing FundSub/IDM customers.

---

## Onboarding Essentials
Curated must-reads (`onboarding_required: Yes`) — see [[wiki/onboarding|full list]]:
- **All teams:** [[wiki/sources/ih-intro-overview|Intro for Integration Hub]], [[wiki/sources/ih-knowledge-hub|IH Knowledge Hub]], [[wiki/sources/ih-setup-guide|IH Setup Guide]]
- **CS:** [[wiki/sources/ocr-implementation-guide|OCR Implementation Guide]], [[wiki/sources/ocr-implementation-journey|OCR Implementation Journey]]
- **Sales + RM:** [[wiki/sources/ih-sales-deck-feb-2025|IH Sales Deck]], [[wiki/sources/ocr-managed-services-sales-deck|OCR Managed Services Deck]], [[wiki/sources/fundsub-essentials-sales-deck|FundSub Essentials Deck]], [[wiki/sources/investor-portal-sales-deck|Investor Portal Deck]]

---

## Data Gaps / Not Yet Covered
- **AAA** — only one release-note source; User Guide / Product Brief / GTM / CS training queued in Batch 8.
- **Side Letter, Platform, Investor Access** — in the taxonomy but no dedicated source pages.
- **Engagement Hub tier pricing** — exact dollar figures not yet captured.
- **AES (GlobalSign eSeal)** — no dedicated implementation guide.
- **Named enterprise accounts** (KKR, EQT, Blackstone, etc.) — tracked as entities but no case studies ingested.

---

## Filed Analyses
- [[wiki/analyses/investor-portal-vs-integration-hub|Investor Portal vs. Integration Hub]]
- [[wiki/analyses/query-answering-karpathy-method|Query Answering Showcase — The Karpathy Method]]
