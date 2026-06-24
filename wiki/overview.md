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
| [[products/fundsub\|FundSub]] | Core fund-subscription platform: LPs complete sub forms & sign; GPs review/approve. The central Anduin Object most integrations read from or write to. Multi-structure, multi-jurisdiction, one-envelope signing. | 15 |
| [[products/e-signature\|E-signature]] | Three eIDAS tiers (SES/AES/QES). Native SES, GlobalSign AES, DocuSign+IDnow QES, and the Schwab custodian signing workflow. A fund picks Anduin-native **or** DocuSign — not both. | 7 |
| [[products/ocr-data-extraction\|OCR Data Extraction]] | Amazon Textract + human-augmented review to digitize sub forms, KYC packets, and fund docs; feeds the FundSub pipeline. Proposal-based pricing. | 11 |
| [[products/aaa\|AAA (Advisor Advantage)]] | GP-side interface for RIAs/advisor entities; assign/unassign subscriptions. Used by Cerity Partners in the Schwab flow. *(Thin — Batch 8 sources pending.)* | 1 |

### Investor data layer
| Product | Role | Sources |
|---------|------|---------|
| [[products/investor-data-management\|IDM]] | Firm-level repository of investment entities, contacts, documents, and reusable investor profiles — the "golden source of truth." The **data foundation** for both Engagement Hub and Investor Portal (all three share one IDM Firm space). | 12 |

### Investor engagement layer
| Product | Role | Sources |
|---------|------|---------|
| [[products/engagement-hub\|Engagement Hub]] | IDM-based engagement layer: Branded Landing Pages, document distribution, centralized inbox, profile sharing. **= Investor Portal minus the per-fund instance & reporting.** Metered by published landing pages. | 3 |
| [[products/investor-portal\|Investor Portal]] | GP-branded LP destination spanning pre-marketing → post-close: branded home + vehicle pages, document distribution, inbox, tasks, **financial reporting**, contact management. **= Engagement Hub + per-fund instance + Reporting.** | 9 |
| [[products/data-room\|Data Room]] | Secure document sharing with engagement tracking, granular/multi-group permissions, branding, and a Public API; embedded within Portal/EH landing pages. | 10 |
| [[products/investor-access\|Investor Access]] | LP-side access product; referenced in the Neuberger Berman deployment. *(Placeholder — no dedicated source yet.)* | 0/1 |

### Connectivity & platform
| Product | Role | Sources |
|---------|------|---------|
| [[products/integration-hub\|Integration Hub]] | Self-service platform to discover, install, and monitor integrations between Anduin products and third-party systems (DealCloud, Affinity, Salesforce, Box). Built on Integration Cards; powered by Prismatic. "20+ app integrations." | 14 |
| [[products/platform\|Platform]] | Cross-product base (object model, config-vs-permission, user roles). *(No dedicated source page.)* | 0 |
| [[products/side-letter\|Side Letter]] | In the product taxonomy; not yet documented. *(Placeholder.)* | 0 |
| [[products/landing-page\|Landing Page]] | **Deprecated / folded into Engagement Hub** as the [[features/engagement-hub-branded-landing-pages\|Branded Landing Pages]] feature. Page retained only as a redirect. | 0 |

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
Every Integration Hub workflow follows one of three patterns (see [[concepts/integration-patterns|Integration Patterns]]):

| Pattern | Direction | Example |
|---------|-----------|---------|
| Order Creation | CRM → FundSub | DealCloud/Affinity → invite investor + prefill form |
| Data Retrieval | Anduin → CRM | FundSub/Data Room → sync subscription & engagement data back |
| Document Retrieval | FundSub → Storage | FundSub → Box/SFTP folder |

Documented integrations: **DealCloud** (order creation, data retrieval, Data Room alerts), **Affinity** (order creation), **Box** (document retrieval), **Salesforce** (→ Data Room onboarding, IDM sync). Data fidelity depends on [[concepts/import-export-templates|Import/Export Templates]] and [[concepts/data-mapping|Data Mapping]].

---

## Cross-Cutting Concepts (10)
- [[concepts/anduin-object-model|Anduin Object Model]] — integrations bind to objects (funds, firms, data rooms), not orgs broadly.
- [[concepts/configuration-vs-permission|Configuration vs Permission]] — the Hub manages configuration; individual apps enforce permissions.
- [[concepts/user-roles|User Roles]] — Admins (GP users sharing an email domain) vs. Members (external).
- [[concepts/integration-patterns|Integration Patterns]] · [[concepts/crm-integration-playbook|CRM Integration Playbook]] · [[concepts/data-mapping|Data Mapping]] · [[concepts/import-export-templates|Import/Export Templates]]
- [[concepts/investor-onboarding-workflow|Investor Onboarding Workflow]] — the central CRM → FundSub → CRM → storage flow.
- [[concepts/product-packaging-bundling|Product Packaging & Bundling]] — lead-with-bundles motion (Portal + IDM + Landing Pages + IH).
- [[concepts/qes-aes-compliance|QES/AES/SES Compliance]] — eIDAS signature-tier framework.

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
- **Portal vs. Engagement Hub pricing structure (unresolved).** Newer EH decks (as-of 2026-02-02 / 2025-09-18) say Portal pricing is being restructured to *"annual EH platform fee + a lower per-fund Portal fee,"* superseding the legacy AUM table on [[products/investor-portal]] — but the new per-fund figures were never captured. Per user decision the AUM table is retained and the conflict flagged. **Confirm current numbers before quoting.**
- **"Ultimate tier" vs. Starter/Growth/Unlimited** naming inconsistency across EH decks — clarify the canonical bundled tier with product.
- **OCR sales decks** — two entries point at the same Google Slides deck; rationalize.

---

## Customers
**Documented (with sources):** [[customers/neuberger-berman|Neuberger Berman]] ($460B AUM; full stack — FundSub + Data Room + IDM + Investor Access + IH; ~3,000 LPs, $5.4B raised), [[customers/cerity-partners|Cerity Partners]] (FundSub + AAA + E-signature Schwab flow), [[customers/accolade|Accolade Partners]] (Data Room + FundSub), [[customers/nxstep|NXSTEP]] (FundSub Essentials).

**Tracked but undocumented (0 sources):** [[customers/kkr|KKR]], [[customers/eqt|EQT]], [[customers/blackstone|Blackstone]], [[customers/hg-capital|Hg Capital]], [[customers/sequoia-heritage|Sequoia Heritage]], [[customers/clearlake|Clearlake]], [[customers/atalaya|Atalaya]], [[customers/audax|Audax]], [[customers/proskauer|Proskauer]], [[customers/stone-ridge|Stone Ridge]], [[customers/pag|PAG]], [[customers/oakley|Oakley]], [[customers/antler|Antler]].

---

## Competitors
The competitive picture is anchored by the **Competitive Intel Repository** ([[sources/competitive-intel-tracking-table|153 field-intel entries]], 2022–2026). 18 competitor pages plus three cross-cutting concept pages: [[concepts/competitor-pricing-benchmarks|pricing benchmarks]], [[concepts/competitive-win-loss|win/loss patterns]], and the [[concepts/private-markets-competitive-landscape|market landscape]].

- **Fundsub (primary battleground):** [[competitors/passthrough|Passthrough]] is the #1 competitor — wins on price (one-time non-recurring fee), LP UI, in-app AML/KYC, and the Goodwin law-firm channel; loses on maturity, CS, and SSO. [[competitors/atominvest|AtomInvest]] (broad all-in-one, weak data integrity + security gaps) and [[competitors/subscribe|Subscribe]] ($45K all-in + managed services + Altscape marketplace) round out the top three.
- **Side letter / MFN:** [[competitors/ontra|Ontra]] is the category leader (AI terms tracking, ~$75–80K/yr); also Carta, Pro-Vision, Robin AI, and [[competitors/kirkland-ellis|K&E]]'s SideTrack.
- **Portals & standalones:** [[competitors/investorflow|InvestorFlow]], [[competitors/juniper-square|Juniper Square]], [[competitors/bunch|bunch]], [[competitors/backstop|Backstop]], [[competitors/bitestream|BiteStream/Investor Pointe]].
- **Structural threats:** fund admins building in-house onboarding ([[competitors/nav|NAV]], [[competitors/flow|Flow→Apex]], Dynamo); AI-native LP-side entrants (JunieAI, Vantager, Daphne, BlueFlame.ai); wealth-channel platforms ([[competitors/icapital-cais|iCapital]], Privatize). See the [[competitors/competitor-landscape-watchlist|watchlist]] for 20 single-mention firms.

Anduin differentiates on the end-to-end platform (onboarding → portal → data room → IDM → IH), branding/UX, platform maturity, SSO, and lower-friction adoption for existing FundSub/IDM customers.

---

## Onboarding Essentials
Curated must-reads (`onboarding_required: Yes`) — see [[onboarding|full list]]:
- **All teams:** [[sources/ih-intro-overview|Intro for Integration Hub]], [[sources/ih-knowledge-hub|IH Knowledge Hub]], [[sources/ih-setup-guide|IH Setup Guide]]
- **CS:** [[sources/ocr-implementation-guide|OCR Implementation Guide]], [[sources/ocr-implementation-journey|OCR Implementation Journey]]
- **Sales + RM:** [[sources/ih-sales-deck-feb-2025|IH Sales Deck]], [[sources/ocr-managed-services-sales-deck|OCR Managed Services Deck]], [[sources/fundsub-essentials-sales-deck|FundSub Essentials Deck]], [[sources/investor-portal-sales-deck|Investor Portal Deck]]

---

## Data Gaps / Not Yet Covered
- **AAA** — only one release-note source; User Guide / Product Brief / GTM / CS training queued in Batch 8.
- **Side Letter, Platform, Investor Access** — in the taxonomy but no dedicated source pages.
- **Engagement Hub tier pricing** — exact dollar figures not yet captured.
- **AES (GlobalSign eSeal)** — no dedicated implementation guide.
- **Named enterprise accounts** (KKR, EQT, Blackstone, etc.) — tracked as entities but no case studies ingested.

---

## Filed Analyses
- [[analyses/investor-portal-vs-integration-hub|Investor Portal vs. Integration Hub]]
- [[analyses/query-answering-karpathy-method|Query Answering Showcase — The Karpathy Method]]
