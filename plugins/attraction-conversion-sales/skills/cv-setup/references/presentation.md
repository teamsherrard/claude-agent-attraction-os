# The Partner Presentation — how Step 2 of the sitting builds the bridge-the-gap one-pager

*Read by `cv-setup` at Step 2 (and on "update my presentation"). Method: `${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md`
§1–§4 and §10 — Mike's bridge-the-gap (current state → desired state → the bridge: the member's leadership, the
model, the value) and the perfect-presentation flow (rapport → qualifying questions → bridge the gap → close with
confidence). "Do not pitch. The goal is that by the end of the call the agent willingly wants to join because they
clearly see you are the solution to their pain points." A presentation shows **the three things that matter most**
to this agent — never every feature. Grounding note: the vault's lesson 45 is not in the transcript export; this
build rests on the two bonus lessons and the workshop's Align step. Said here, never to the member.*

## What to read (silent)
`identity/offer.md` (the UVP line; `## The program` — name · type · cadence · the 90-day outcome; `## The framework`
— the one-line version; the deliverables table; `Onboarding: Day 1`; an older offer → what's included, the first 30
days; `Status: seeds` → "what you have to give so far", already said once at Step 1 — not again) ·
`identity/positioning.md` (the vehicle vs the reason; what stays private) · `identity/brokerage-model.md` (the model
per type from the member's materials; empty → one line, "and everything [brokerage] provides — walked through on the
call") · `identity/avatars.md` (the primary type; the secondary types for the table below) · `identity/journey.md →
## Why join me` · `identity/proof.md` (real, cleared) · `identity/story-bank.md` (one story; stamp `Used-where`) ·
`identity/operations.md` (the booking link, the Week 2 page — never re-done, never asked about) ·
`identity/offer.md → ## Week 3 Kit` (`Status: built YYYY-MM-DD` → the Kit exists: read its text, the newest
`~/attraction-brain/exports/week3-kit-YYYY-MM-DD.txt`, at CHAPTER 7 — THE JOIN MY TEAM ONE-PAGER and THE CALL DECK,
SLIDE BY SLIDE — the Kit rule below) · `identity/compliance.md` (the gate, below).

## The Week 3 Kit rule — one set of words for the program
When the Week 3 Kit exists, the one-pager uses the SAME program and stack words as the Kit's chapter 7: the program
strip reads as slide 5 of the call deck states it (name · type · cadence), the three outcome blocks and "What
partnering looks like" use the one-pager's "What you get" and "How it works" wording, the proof and "Why me" lines are
the Kit's. Read it first, never contradict it — the designed call deck and this one-pager are the same offer in the
same words. Where today's `offer.md` has moved on from the Kit (a renamed program, a changed cadence), the Kit is
behind: the one-pager follows the Kit's words all the same, and the skill says one plain line — *"Your Week 3 Kit is
behind your offer — say 'build my Week 3 kit' and then 'update my presentation'."* No Kit yet → the one-pager is built
from `offer.md` alone, and nothing about the Kit is said.

## The outline — what the member says, in order, inside Positioning (6–10 minutes)
1. **Mirror** — their current state in their words, from Discovery and Diagnosis: *"you said [pain], [pain], [goal]."*
2. **The three things that matter most** — chosen from what they said. Each: the pain → what the member gives that
   answers it → the outcome (never the feature) → one real proof line, or *"you'd be early."*
3. **The bridge, in three layers:** the member's support (the program by name — "[name] is a [type]: [cadence]" —
   the framework walked step by step; the 90-day outcome as what they'll be able to SHOW; the first 30 days) · the
   partner and the community, as they are today · the brokerage's model, only as far as their goals go, in plain
   English from `brokerage-model.md`.
4. **The story** — one, from the story bank, the one that mirrors them.
5. **Close with confidence** — assume the close; the transition-date question; what happens next (Day 1).
Each step with **Say it like this:** and the line. Production pain → no revenue share in the outline; exit or
time-freedom pain → residual income as the vehicle, numbers from the member's materials, labeled, never projected.

## The three things, by type of agent — the table the document carries
The one-pager is written for the primary type; the table gives the member the three things for every type they
may sit across from, so the same page bends to the person. Shape stays, examples change (doctrine §4):

| Type of agent | The three things that usually matter most | Never lead with |
|---|---|---|
| New agent | a plan for the first full year · a person who answers this week · training they can follow today | revenue share, stock, the org chart |
| Experienced, low production | a system that ends the chase · consistent closings without a lead bill · someone who has done it | compensation math |
| Top producer | an exit beyond active income · wealth that builds past this year · respect — being featured, not managed | production training |
| Agent with a brand | monetizing the audience they already have · brand freedom · no "adult daycare" | the brokerage's logo or look |
| Team leader | partners instead of competitors · the company carrying the overhead · an exit that isn't selling the team | splits |
| Broker-owner | keeping the brand, dropping the liability · a willable asset · what they'd keep | anything that sounds like "give it up" |

Each cell is rewritten in the member's voice with their own offer parts; a cell that would need a program the
Brain does not confirm reads "ask your brokerage" in the member's copy, never an assertion.

## The one-pager — copy, then (optionally) design
Title line (the UVP one-liner from `offer.md`) · the program strip (name · type · cadence) · the framework in one
line · **three outcome blocks** (the three things, for the primary type) · "What partnering looks like" (the first 30
days, four lines) · one proof line · the member's one-line story · **one next step** (the booking line from
`operations.md`, or "I'll send you a time"). **Never on the page:** splits, caps, stock, tiers, revenue share, income,
any other brokerage's name, "join my brokerage". The brokerage's name appears as `compliance.md`'s display rule
requires and the required disclaimer is appended verbatim.

**The one design line (in the document only, always the same words):** *"Your designed call deck lives in Week 3 —
say 'design my call deck' in Claude Design and it uses this one-pager's words."* No Kit yet → *"Your designed call
deck lives in Week 3 — once your Week 3 Kit is built, say 'design my call deck' in Claude Design and it uses this
one-pager's words."* Nothing more about design here; the Design Studio owns it. No new document is made for the deck.

## The document — `Partner Presentation — [Name]`
Structured text per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md`: the title and meta lines; CAPS bands — HOW TO
USE THIS (two lines: it's the bridge, not the brochure; pick the three live, from what they said) · THE OUTLINE (five
`──── Step ────` sub-bands with "Say it like this:") · THE ONE-PAGER (the copy, block by block, paste-ready) · THE
THREE THINGS BY TYPE OF AGENT (the table) · the one design line. Rendered through `render_doc.py` to `Partner
Presentation — [Name] · YYYY-MM-DD.docx` → `05 · Offer`; `RENDERER-UNAVAILABLE` → the `.md` upload, one plain line.
The same text goes, in full, under `## Presentation` in `identity/conversion.md`.

## Gates and rules
- The one-pager is something a prospect sees → the first line of `identity/compliance.md`, `Status:`. **`unset`** →
  built and saved all the same, stamped *"hold until your compliance basics are set"* under the title, the
  brokerage's wording kept as one bracket; the member is told how ONCE, at the close (the sitting's one compliance
  line). The outline is private and carries no stamp. **`set`** → apply; one reminder at the close. **`confirmed`** →
  apply. Never a detour to the compliance skill mid-sitting.
- Through their lens, always: a block that does not tie to something the type (or the prospect) says is cut.
- Cardinal rules; no competitor's name; no comparison sheet (that is model positioning's, gated). No income claims;
  every number from the member's materials and labeled. Zero fabrication of proof. The quality bar (delete ·
  any-agent · so-what · no hedging · no filler headings). Banned words per `how-we-speak.md` §7.
