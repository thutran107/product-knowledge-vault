---
type: source
title: "GTM Enablement — Investor Portal Customer Training Guide (Oct 2025)"
date_ingested: 2026-06-08
as_of_date: 2025-10-01
source_type: client-training
trust_level: 7
original_file: raw/GTM enablement - Investor Portal Onboarding Guide.pptx
products: [Investor Portal, IDM]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation, onboarding]
---

## Summary
CS onboarding guide for Investor Portal (October 2025). Covers the full implementation process from kickoff through go-live: discovery, fund/client/contact setup, document distribution, email composition, LP experience testing, and investor onboarding. Detailed step-by-step training script with slide-by-slide instructions.

## Key Takeaways
- Onboarding sequence: Kickoff → IDM setup → Portal setup → Data migration → Live training (1 hr) → Customer testing → Go live.
- Pre-condition for live training: Customer must already be familiar with IDM concepts (fund structure, contact matrices).
- Three document distribution methods: Group Share, Private Share (AI maps files to IEs), Split & Share (one PDF → split → AI maps).
- Profile sharing with investors (view-only) was "coming Nov 2025" as of this deck.
- Additional training modules available on request: Landing Pages, Reporting, Profile updates (Q2 2026), Integration.

## Kickoff Call Agenda (30 min)
1. Background & objectives — fund structure, investor base, main goals (improve comms, streamline doc sharing, enhance investor experience), expected rollout timeline
2. Current workflows — how they manage investor communications today; doc types/frequency; teams involved; pain points
3. Permissions — introduce fund structure concepts (Fund Family, FLE, Client, IE, Contact, Contact Matrix, Communication Types)
4. Training needs — who will use the Portal and what tasks each role performs

## Live Training Agenda (1 hour)
Pre-condition: Client already familiar with IDM concepts
1. Setup — create funds, add investors, set up contact permissions
2. Document distribution & management — add doc/comm types; distribute docs; manage after sharing
3. Communication — track communications, send direct emails, set up email templates
4. Other features — share IDM Profiles with investors (view-only, Nov 2025)
5. LP experience — test investor view; invite/onboard investors to Portal

## GP Setup: Three Fund Onboarding Use Cases
- **Use case 1:** New investors to new funds — create Fund Family/FLE → create Client + IE → add contacts → set communication matrix
- **Use case 2:** New investors to existing funds — add clients/contacts; link to existing funds
- **Use case 3:** Existing investors to new funds — create new fund; link existing IEs

## Document Distribution
**Group Share** — same docs to a group: upload → assign doc types (AI auto-detects) → select fund → choose recipients (all contacts, specific contacts, specific IE, or specific FLE) → select comm types → compose email (templates/placeholders) → configure settings (immediate/scheduled, notifications, download permission, watermarks).

**Private Share** — investor-specific docs in batch: upload → AI maps each file to correct IE by filename/content → review mappings → select comm types → compose + send.

**Split & Share** — one merged PDF containing docs for multiple investors: upload → system splits by manual markers / page count / embedded markers → AI maps sub-files to IEs → rest follows Private Share flow.

**From inside a Portal instance:** Document sharing scoped to IEs within the linked FLEs of that Portal — reduces errors.

## Email Composition
- Default email templates auto-fill subject/body from firm's template library
- Dynamic placeholders supported (type `[` or `{{` to see list); auto-replaced with recipient name etc.
- Cc/Bcc support; attachments appear in Documents dashboard for both GP and LP
- Save as draft for team collaboration before sending

## Testing LP Experience
- Create test Client → IE → Contact using a firm test email
- Contact receives same email notifications as actual investors
- LP doc dashboard: view/preview/search/filter/download docs
- LP inbox: read/unread tracking; search by sender/subject; filter by attachment/time range

## Onboarding Actual Investors
- Go to "Page access" tab in Landing Pages → select contacts → Batch → Notify contact → customize email → send

## Additional Training Modules (on request)
- Landing Pages setup + contact permissions + investor invitation
- Reporting: datasets, permissions, displays
- Profile updates (Q2 2026): enable investor editing; review/approve investor-submitted changes
- Integration: data flows to/from other systems via Integration Hub

## Connections
- [[wiki/products/investor-portal]]
- [[wiki/products/investor-data-management]] — IDM setup is pre-condition
- [[wiki/sources/investor-portal-contact-management]] — contact matrix setup detail
- [[wiki/sources/investor-portal-sales-deck]] — capabilities overview

## Conflicts & Supersessions
None found.

## Raw Notes
- Watermarks configured at firm level; only visible from LP side, not GP view.
- Profile sharing with investors (view-only) was "coming Nov 2025" — likely live by now.
- Profile update (investor edits) feature is Q2 2026.
