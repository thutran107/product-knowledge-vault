---
type: source
title: "AAA (Advisor Advantage) — Product x CS Demo + Training (Jan 2026)"
date_ingested: 2026-06-15
as_of_date: 2026-01-01
source_type: client-training
trust_level: 7
original_file: Google Slides — Product x CS Demo + Training: Advisor Advantage (1OlXLo4_FhAx4DtWzUF0Gisihyro2_tG-KByzgxe7hBY)
products: [AAA]
target_audience: CS
onboarding_required: No
tags: [aaa, advisor, ria, implementation, permissions, demo, troubleshooting]
---

## Summary
The most current (last updated Jan 2026) and most detailed internal CS enablement for Advisor Advantage. Beyond personas and value props, it adds the parts CS needs operationally: a demo outline for three personas, step-by-step setup guidelines, a full "technical concepts explained" glossary of the advisor data model, and customer FAQs. This is the authoritative CS-facing walkthrough of how AAA actually works.

## Key Takeaways
- **Setup prerequisite**: a feature switch in the **Admin Portal** must be enabled to expose the "Advisor Group" tab in each FundSub environment, allowing GPs to invite advisors and advisors to create entities.
- **CS setup flow**: (0) enable the feature switch; (1) join the fund as Anduin Support; (2) invite the advisor group and add yourself as an advisor; (3) open the email invitation and create the advisor entity per request — *always input the email domain* so other members of the advisor entity can be auto-added.
- **Core data model glossary** (key for CS troubleshooting):
  - *Temporary Advisor Group* — a placeholder group the GP creates in FundSub to invite advisors; transforms into an active group once accepted.
  - *Advisor Entity (RIA entity)* — created by the advisor on accepting an invitation; represents their advisor firm.
  - *(Active) Advisor Fund Group* — auto-generated when an advisor accepts a fund invitation; links the fund and the advisor entity.
  - *Advisor Fund Dashboard* — page listing all subscriptions associated with an advisor in a given fund.
  - *Advisor Home Dashboard* — page listing all opportunities (funds) an advisor can access.
  - *Advisor Subscriptions* — subscriptions tagged to a specific advisor entity.
- **Permission model** (matches the sales deck): three-level entity permission (Admin/Manager/Member) and fund-group permission (Entity Admin always has access / Fund Group Admin / Fund Group Member).
- **Email-domain FAQ**: whitelisting auto-adds advisors to the entity when invited by GPs, ensures immediate platform access, and removes manual additions.
- **Link-vs-placeholder FAQ**: a GP-created advisor group is a placeholder until the advisor entity explicitly accepts; the entity name the advisor inputs may differ from the GP's group name.
- **Demo flows** documented for three personas: Fund Manager, Advisor Admin, Advisor Member.
- Includes a **Knowledge Validation** self-assessment covering five areas (advisor ecosystem, features, support readiness).

## Connections
- Primary implementation/troubleshooting source for [[products/aaa|AAA (Advisor Advantage)]]; feeds the product page's "Implementation notes" and "Known limitations."
- The advisor data model (temporary group → entity → active fund group) connects to [[concepts/anduin-object-model|Anduin Object Model]] and [[concepts/user-roles|User Roles]].
- Setup via Admin Portal feature switch connects to [[concepts/configuration-vs-permission|Configuration vs Permission Model]].

## Conflicts & Supersessions
- Supersedes the [[sources/aaa-gtm-training|Nov 2024 GTM deck]] for feature/process specifics (that deck explicitly points here as the up-to-date enablement). No factual conflicts; this deck is more current and more detailed.

## Raw Notes
- Slide content extracted via Google Drive connector. Help-doc links and demo recordings referenced but not ingested.
- Document Type in Notion = "Client Training Deck" (mapped to `client-training`, trust 7) despite the "CS Training" name; target audience CS.
- onboarding_required field not set in Notion → No.
