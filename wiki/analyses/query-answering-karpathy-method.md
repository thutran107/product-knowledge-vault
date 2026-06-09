---
type: analysis
title: "Query Answering Showcase — The Karpathy Method"
date: 2026-06-09
tags: [reference, query-method, llm-judge, onboarding]
---

# Query Answering Showcase — The Karpathy Method

A reference walkthrough of how the Anduin product knowledge vault answers
realistic CS/Sales/RM questions, and how the *best* answer is selected using a
generate-and-compare ("Karpathy method") tournament.

- **Generated:** 2026-06-09
- **Model:** Claude Haiku 4.5 (generation + judging)
- **Orchestration:** 9 agents — 5 generators, 4 comparative judges
- **Source of truth:** the `wiki/` layer of this vault, entered via `index.md`

---

## What "the Karpathy method" means here

The principle: **LLMs (and people) are far more reliable at *comparing* two
things than at *scoring* one thing in isolation.** An absolute score ("this
answer is a 7/10") is noisy and drifts; a pairwise verdict ("A is better than B,
because…") is stable and reproducible. So instead of grading each answer on a
rubric, we **generate several diverse candidates and let them fight pairwise**,
winners advancing until one remains.

This showcase applies that principle in three stages:

1. **Diverse generation** — five answers, each forced down a *distinct angle*
   so they don't collapse onto the same popular topic.
2. **Grounded retrieval** — every answer is built by reading the vault, not from
   model memory (the index-first pattern below).
3. **Comparative judging** — a single-elimination tournament where each match is
   a head-to-head "which is better, and why," never an absolute score.

---

## How each answer is produced (the index-first pattern)

Every generator follows the vault's canonical query workflow (`CLAUDE.md` §6):

```
1. Read index.md           ← the catalog: find which slugs are relevant
2. Read 2–4 wiki/ pages    ← the actual source material for the angle
3. Write the query         ← framed AFTER seeing the sources, so it's specific
4. Write the response       ← grounded, cites [[wiki/...]] slugs, hedges on gaps
```

The query is written *after* the source pages are read — which is why the
questions below carry real figures and customer names rather than generic
phrasing. If the vault lacks something, the answer says so instead of inventing.

| Angle | Pages actually read (verified from transcripts) |
|-------|--------------------------------------------------|
| A — Product capability | `index.md` → `products/ocr-data-extraction` → `sources/ocr-implementation-journey` → `ocr-table-view-how-it-works` → `ocr-fundsub-process-client-training` |
| B — Pricing | `index.md` → `sources/ocr-pricing-guide` → `investor-portal-pricing-faqs-boston` → `products/investor-portal` |
| C — Competitive | `index.md` → `competitors/investorflow` → `competitors/atominvest` |
| D — Implementation | `index.md` → `esignature-schwab-implementation-guide` → `esignature-schwab-cerity-training` |
| E — Customer case study | `index.md` → `customers/cerity-partners` → `esignature-schwab-cerity-training` → `products/aaa` → `esignature-schwab-implementation-guide` |

---

## The five queries & responses

### A — Product capability *(OCR Data Extraction)*

> **Q:** I'm new to CS and just got assigned to an OCR Data Extraction
> implementation. What does the product actually do, and how does the extraction
> process work end to end?

OCR Data Extraction is Anduin's service for digitizing structured data out of
investor documents — subscription forms, KYC packets, and fund documents — and
feeding it downstream into the FundSub processing pipeline (see
[[wiki/products/ocr-data-extraction]]).

How it works, end to end:

1. **Automated ingestion:** documents are run through Amazon Textract, the
   underlying AI/OCR engine that pulls raw structured data off the page.
2. **Human-augmented review:** Textract output isn't shipped as-is. A human
   review layer of Data Extraction Analysts (DEAs) validates and corrects the
   extracted values, which is the accuracy backstop for the AI
   ([[wiki/products/ocr-data-extraction]]).
3. **Table View:** reviewers see the extracted data in a table format before it
   flows downstream — this is the review/QA interface and is the most current
   "how it works" reference, as-of 2025-09-16
   ([[wiki/sources/ocr-table-view-how-it-works]]).
4. **FundSub handoff:** validated data flows into FundSub document processing;
   the OCR-FundSub intersection is what you'll deliver to clients
   ([[wiki/sources/ocr-fundsub-process-client-training]]).

For your implementation specifically, the canonical SOP is the CS-DEA-Client
Implementation Journey, which frames it as a three-party process between the CS
team, the DEAs, and the client — this is an onboarding-required read
([[wiki/sources/ocr-implementation-journey]]).

Two caveats from the vault: a new OCR UX launched in May 2025, so confirm any
pre-May training reflects the current interface; and the implementation/GTM
materials are undated, so verify currency. The vault catalogs these sources but
the full Notion/Slides bodies haven't been ingested, so for exact click-by-click
steps open the linked Implementation Journey directly.

---

### B — Pricing & packaging *(Investor Portal)*

> **Q:** A prospect with ~$1.7B AUM wants Investor Portal for 1 fund. They're
> already on FundSub + IDM. How do I price this, what's the beta discount, and
> what won't they get unless they add Landing Pages?

Per the Boston Popup pricing deck (as of May 2025), Investor Portal is priced as
an annual fee per fund/SPV, tiered by AUM, plus a one-time data migration fee.
See [[wiki/sources/investor-portal-pricing-faqs-boston]] and
[[wiki/products/investor-portal]].

At $1.7B AUM the prospect falls in the Enterprise tier ($1B–15B): $15K
annual/fund and a $7.5K one-time migration/fund. For one fund that's $15K ARR
list + $7.5K migration. (Note: BlueArc, a comparable $1.7B Enterprise beta
prospect in the same deck, was actually quoted $10–20K/fund/yr tiered by LP
count — so LP count can move the number within tier.)

Beta discount for early Y1/Y2 customers: 50% off list in Y1, 25% off in Y2, no
discount Y3+. With the beta discount, Y1 would be ~$7.5K, Y2 ~$11.25K.

Because they're already on FundSub + IDM, the guidance is explicit: keep their
existing FundSub/IDM pricing as-is and add Portal fees on top — don't repackage.

What they won't get on a Portal-only basis: Portal includes Standard IDM
Profile, Custom Contact Matrix, and API, plus a custom home page per Portal
instance. It does NOT include Custom IDM profile or KYC/AML management (needs IDM
add-on), and crucially does NOT include Branded Landing Pages for marketing new
funds unless they add the Landing Pages product. The recommended full bundle is
Portal + IDM + Landing Pages + Integration Hub.

Caveat: pricing is as-of May 2025; confirm current rates before quoting.

---

### C — Competitive differentiation *(vs. AtomInvest)*

> **Q:** A prospect with about $5B AUM told me AtomInvest quoted them $10K/fund/yr
> for their investor portal, but our list is $15K/fund/yr at the Enterprise tier.
> How do I respond to "AtomInvest is cheaper"? Where do we actually win against
> them?

You're right on the numbers — per the vault's pricing intel (as of May 2025,
sourced from an ex-employee), AtomInvest prices per-fund, tiered by AUM:
~$10K/fund/yr for $1B+ AUM GPs and ~$6K/fund/yr below $1B. Anduin's Investor
Portal Enterprise tier ($1B–15B) lists at $15K/fund/yr, so yes, we are higher at
this tier. (See [[wiki/competitors/atominvest]].)

The recommended response is to reframe from price to total cost of ownership and
product scope:

1. **Bundle/TCO argument** — Anduin's premium is justified because the full
   bundle (FundSub onboarding + IDM + Landing Pages + Portal + Integration Hub)
   replaces multiple point solutions: a fund-admin portal, a separate onboarding
   tool, and a data room. When you count every tool being replaced, TCO favors
   Anduin.
2. **Native integration** — Anduin's end-to-end flow (FundSub → IDM → Data Room
   → Portal) is native, not bolted on; AtomInvest's integrations are described
   as more fragmented. We also win on UX and branding customization per the
   product overview.
3. **Low-friction upgrade** — if they're already an Anduin FundSub/IDM customer,
   the Portal upgrade path is low-friction.

Where AtomInvest is genuinely strong: lower Enterprise pricing and extended
accounting capabilities. If accounting comes up, position Anduin as the
investor-relationship layer and note that accounting tools (e.g., Allvue/FIS)
can integrate via Integration Hub.

Confidence caveat: the pricing figures rest on a single ex-employee source from
May 2025, so treat them as directional. (Sources: [[wiki/competitors/atominvest]],
[[wiki/products/investor-portal]], [[wiki/sources/investor-portal-pricing-faqs-boston]].)

---

### D — Implementation / troubleshooting *(Schwab signature workflow)* 🏆 *tournament winner*

> **Q:** We're onboarding a new RIA to the Schwab signature workflow on FundSub,
> and the Schwab form isn't appearing for the right investors during testing.
> What's the full setup process I need to validate, and what are the most common
> configuration points that break the Schwab flow?

The Schwab signing workflow has 5 setup components (non-sequential) — walk
through each to find the gap (see
[[wiki/sources/esignature-schwab-implementation-guide]]):

1. **RIA + Anduin setup (per RIA):** Anduin creates a unique DocuSign sender
   email per RIA entity (`{ria-name}-docusign-sender@anduintransact.com`); the
   RIA must add it as an authorized user in their Schwab Advisor Center (SAC)
   account.
2. **Schwab + RIA addendum (per RIA):** RIA approves Anduin as a third-party
   DocuSign provider via signed addendum through SAC → Account Management →
   Advisor-Owned DocuSign → "Anduin Transaction."
3. **Technical validation (per RIA):** Anduin sends a test envelope; Schwab
   test-signs and approves. Failures go to engineer + product team.
4. **Digitization setup (per FundSub engagement):** the Schwab form PDF must
   contain `[Schwab form]` in its filename to trigger the Schwab template, AND a
   logic-gating question ("Is this investment associated with Schwab?") must be
   configured to show the form only to relevant investors.
5. **Anduin app setup (per fund):** DocuSign must be enabled as the signature
   type on each fund using the integration. POC is Form QA.

For your specific symptom — the form showing for the wrong investors — the cause
is almost always **Component 4**: a missing/misconfigured logic-gating question,
or the PDF filename lacking the `[Schwab form]` tag. Also confirm email-domain
enforcement: only advisors with the registered RIA email domain can initiate the
flow (Anduin hard-codes this). For Cerity Partners testing, the internal
backdoor alias is `+ceritypartners@anduin.fund`. Plan ~2–3 days of setup,
initiated 2–3 weeks before first live use.

The advisor-facing UX (custodian selection triggering the "Alternative
Investment Letter of Authorization," phone auth for both advisor and investor)
is documented in [[wiki/sources/esignature-schwab-cerity-training]].

---

### E — Customer case study *(Cerity Partners)*

> **Q:** A new RIA prospect wants the same Schwab custodian e-signing setup that
> Cerity Partners has. What products did Cerity actually deploy, and what are the
> key setup steps I need to flag to the implementation team?

Cerity Partners is an RIA running FundSub for subscription management, AAA
(Advisor Advantage) as the GP/advisor-side interface, and the Schwab DocuSign
custodian signing workflow under E-signature (see
[[wiki/customers/cerity-partners]]). Advisors access investor subscriptions from
the Advisor Advantage fund dashboard, select Schwab as custodian, and complete
signing in DocuSign (not Anduin's native e-signature) with phone-number
authentication for both advisor and investor; signed docs then auto-forward to
Schwab ([[wiki/sources/esignature-schwab-cerity-training]]).

For implementation, the internal CS guide
([[wiki/sources/esignature-schwab-implementation-guide]]) lays out 5
non-sequential components to flag:

1. **RIA + Anduin setup** — Anduin creates a unique DocuSign sender email per
   RIA (`{ria-name}-docusign-sender@anduintransact.com`); the RIA adds it as an
   authorized user in their Schwab Advisor Center (SAC).
2. **Schwab + RIA addendum** — RIA gets Schwab approval for Anduin as
   third-party DocuSign provider via signed addendum (SAC → Account Management →
   Advisor-Owned DocuSign → "Anduin Transaction").
3. **Technical validation** — Anduin sends a test envelope; Schwab test-signs
   and approves.
4. **Digitization** — the Schwab form PDF needs `[Schwab form]` in its filename
   to trigger the template, plus a logic-gating question so the form only shows
   to Schwab-custodied investors.
5. **App setup** — DocuSign must be enabled as a signature type on each fund.

Flag also: only advisors on the registered RIA email domain can initiate the
flow (hard-coded), setup runs ~2–3 days, and it should be initiated 2–3 weeks
before first live use.

Caveat: the vault confirms Cerity uses FundSub/AAA/E-signature but does not
document whether they use any other Anduin products, and AAA pricing/limitations
are still pending Batch 8 ingestion ([[wiki/products/aaa]]).

---

## The tournament — comparative judging in action

Five candidates, single elimination, one bye (E). Every match is a pairwise
"which is better, and why" — never an absolute score. Judges independently
re-read the cited vault pages to fact-check faithfulness before ruling.

```
QF1: A vs B  ──►  B          (E byes straight to the semifinal)
QF2: C vs D  ──►  D
SF:  B vs D  ──►  D
FIN: D vs E  ──►  D 🏆
```

| Match | Winner | Why it won (comparative) |
|-------|--------|--------------------------|
| QF1 A vs B | **B** | Both faithful; B answers a harder multi-constraint sales scenario with exact figures, correct discount math, and a real comparable-deal nuance (BlueArc). A is a more standard explainer that defers to external docs for the actual steps. |
| QF2 C vs D | **D** | Both faithful; D *diagnoses the symptom* (root-cause = Component 4) instead of restating process, and stratifies sources by trust level. C largely restates the "objections & responses" section. |
| SF B vs D | **D** | Tied on accuracy; D's query demanded troubleshooting depth and D delivered root-cause reasoning, while B's was a more mechanical pricing lookup. |
| FIN D vs E | **D** 🏆 | Same sources, both faithful. Decider = how well each answers its own query: D isolates the failure point for an active debugger; E stays descriptive (a recap) despite a good caveat. |

**Why D won overall:** across every match where accuracy tied — which was most
of them — the judges rewarded **diagnostic synthesis over descriptive listing**.
D demonstrated that quality three times running. That repeatable signal is
exactly what comparative judging surfaces and absolute scoring tends to blur.

---

## Takeaways for reusing this method

- **Force diversity up front.** Pre-assigning distinct angles stops five agents
  from converging on the same popular product. Distinctness is enforced, not
  hoped for.
- **Retrieve, then ask.** Reading the source pages *before* writing the query is
  what makes the questions concrete and the answers grounded.
- **Compare, don't score.** Pairwise verdicts are stable and explain themselves;
  the winning trait ("diagnostic depth") emerged because the same comparison ran
  repeatedly.
- **Make judges verify.** The strongest signal came when judges re-opened the
  cited pages to check faithfulness — bake that into the judge step rather than
  leaving it emergent.
