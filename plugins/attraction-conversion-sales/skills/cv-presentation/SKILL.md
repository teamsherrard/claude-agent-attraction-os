---
name: cv-presentation
description: >
  The opportunity presentation: a short outline for the partner call and a one-pager, customized to the
  member's brokerage model and told through the lens of the prospect's goals — "the three things that matter
  most," never every feature. Built from Mike's bridge-the-gap method (current state → desired state → the
  bridge: the member's leadership, the model, the value proposition) and the perfect-presentation flow
  (rapport → qualifying questions → bridge the gap → close with confidence). Produces the outline, the
  one-pager copy, and a paste-ready design brief for the Design Studio's ds-offer-assets. Trigger on: "my
  presentation", "opportunity presentation", "my opportunity one-pager", "the opportunity deck", "join my team one-pager",
  "presentation for a top producer", "what do I show on the call", "update my presentation".
---

# Opportunity Presentation — the bridge, not the brochure

"Do not pitch. The goal is that by the end of the call the agent willingly wants to join because they clearly
see you are the solution to their pain points" (`bonus/bridging-the-gap`). A presentation is the bridge from
their current state to their desired state, shown through their goals — "based on what you told me, these are
the three things that matter most," not "here's every feature at my brokerage" (the workshop's Align step).
Doctrine: `${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md` §2–§4, §10. House rules:
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`.

*Grounding note: the vault's lesson 45, "The Perfect Agent Opportunity Presentation," is not in the transcript
export. This skill is built from the two bonus lessons (Bridging the Gap · The Perfect Presentation), lesson 42,
and the workshop's Align / Show the Opportunity steps. It says so here and nowhere the member sees.*

## Before writing (silent)
`brain.md` first (pull if missing) · `identity/offer.md` (the Partner Offer — UVP line, what's included, first
30 days; seeds stage → "what you have to give so far," Week 2 named once) · `identity/positioning.md` (the
vehicle vs the reason; what stays private) · `identity/brokerage-model.md` (the model per type, from the
member's materials; empty → the model is one line, "and everything [brokerage] provides — walked through on the
call") · `identity/avatars.md` (the primary type; a per-type variant on request) · `identity/journey.md`
`## Why join me` · `identity/proof.md` (real, cleared) · `identity/story-bank.md` (one story; stamp
`Used-where`) · `identity/brand-visual.md` (for the design brief) · for a named prospect: the intel report, the
call prep, the conversation rows — the three things are THEIRS.
Compliance: the one-pager is something a prospect sees → `identity/compliance.md` **unset → the outline
renders, the one-pager and the brief are held** with one warm line; **set** → apply and remind once; **confirmed**
→ apply.

**Fast lane:** Brain loaded → one line and the output. The only question, if neither a type nor a name is
clear: *"Who's this for — your main type of agent, or a specific person?"* **Your turn.**

## The outline (for the call — what the member says, in order, 6–10 minutes inside Positioning)
1. **Mirror** — their current state in their words (from Discovery/Diagnosis): "you said [pain], [pain], [goal]."
2. **The three things that matter most** — chosen from what they said; each one: the pain → what the member
   gives that answers it → the outcome (not the feature) → one proof line or "you'd be early."
3. **The bridge, in three layers** (`04-value-proposition/28` via the Brain doctrine §10a): the member's support
   (the first 30 days, the recurring call, the thing they teach first) · the upline and community (as it is) ·
   the brokerage's model, only as far as their goals go, in plain English, from `brokerage-model.md`.
4. **The story** — one, from the story bank, the one that mirrors them.
5. **Close with confidence** — assume the close; the transition-date question; what happens next
   (`bonus/perfect-presentation` step 4).
Each beat with **Say it like this:** and the line. Production pain → no rev share in the outline; exit or
time-freedom pain → residual income as the vehicle, numbers from the member's materials, labeled, never projected.

## The one-pager (copy, then design)
Title line (the UVP one-liner from `offer.md`) · three outcome blocks (the three things, for the primary type)
· "What partnering looks like" (first 30 days, four lines) · one proof line · the member's one-line story ·
one next step (the booking line; `Booking page` from the Conversion block or "I'll send you a time").
**Never on the page:** splits, caps, stock, tiers, rev share, income, any other brokerage's name, "join my
brokerage." The brokerage's name appears as `compliance.md`'s display rule requires, and the required disclaimer
is appended verbatim.

Then the **design brief for `ds-offer-assets`** (paste-ready, by name):
```
FOR ds-offer-assets (the opportunity one-pager)
Member: [name] · [brokerage, as compliance.md displays it] · [market]
Headline: [UVP one-liner]
Three outcome blocks: 1. [pain → outcome] 2. … 3. …
What partnering looks like: four lines
Proof line: [one, real] · Story line: [one]
Next step: [booking line]
Brand: [from brand-visual.md — logo status, colours, type; or "Design Package first: ds-logo → ds-style-sheet → ds-brand"]
Required disclaimer (verbatim): [from compliance.md]
Never on the graphic: splits, caps, stock, rev share, income, another brokerage's name.
```
Deck request ("the opportunity deck") → the same content as 6–8 slide titles with one line each, same brief
header, `FOR ds-offer-assets (the opportunity deck)`; still never a feature dump.

## Render, save, push
Render per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` via `${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py` →
`Opportunity Presentation · [Member Name or Prospect] · [Date].docx` → `05 · Offer` (fallback: `.md` upload,
one line). The brief stays in chat for pasting into Claude Design. Stamp the story's `Used-where`; push.

## Rules
- Through their lens, always: a block that doesn't tie to something the prospect (or the type) said is cut.
- Cardinal rules; no competitor's name; no comparison sheet here (that is model-positioning's, compliance-gated).
- No income claims; no projections; every number from the member's materials and labeled.
- Zero fabrication of proof. The week rule for a seeds-stage offer.
- Quality bar: delete · any-agent · so-what · no hedging · no filler headings.
- Banned words and the recruiter register per `how-we-speak.md` §7.

## Close
*"Outline for the call, one-pager copy, and the design brief to paste into Claude Design. Want a version
aimed at a different type of agent?"*
