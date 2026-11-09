---
name: attraction-offer-package
description: >
  Builds the member's OFFER PACKAGE: the one file for the offer an agent joins. Part I, the offer to join
  me in Mike's anatomy (why join me, the one line, why me, the five problems it solves, the value stack
  sorted free · included · discounted with the free line and the up-front cost line, the proof plan, the
  honest why now, what their partners can offer). Part II, the digital product (name, promise, outline,
  cover line, three promises, the version-one path). Part III, the copy for every asset that promotes the
  offer: the Join My Team one-pager, the offer stack, the product mockup, the call deck, the welcome pack,
  bio line, captions, DM, the 60-second video script. Part IV, the design brief for the offer kit.
  Assembled from the Brain, never rewritten; saved to 05 · Offer, dated, newest wins; runs on its own
  after the offer session and whenever the story or the stack changes. Trigger on: "build my offer
  package", "my offer package", "rebuild my offer package", "what do I upload for my offer kit".
---

# The Offer Package — the one file for the offer an agent joins

A lead magnet starts a conversation. The **offer** is what an agent joins: the program, the stack, the product,
the mentorship — "when you join me you don't just get the brokerage, you also get…" (`04-value-proposition/33`,
`/34`, `/31`, `/28`). Mike promotes the offer everywhere (his Academy, his Accelerator, his community), and the
lead magnet is one door into it. This skill packs the member's offer into **one file**: the offer to join them,
the digital product, the copy for every asset that promotes the offer, and the design brief that turns the copy
into the offer kit in Claude Design in Week 3. **It assembles from the Brain and never rewrites a word; it renders
no graphic.**

Follow `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md` by
reference. Doctrine: `${CLAUDE_PLUGIN_ROOT}/shared/attraction-doctrine.md` §10–§11. Documents:
`${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` and `shared/render_doc.py`. The contract:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## When it runs
- **At the end of the offer session**, after `attraction-offer` has built the Partner Offer, the why join me
  story and the value stack exist (the offer skill runs `attraction-why-join-me` and `attraction-free-vs-paid`
  in silent mode first), with no welcome and no question.
- **Whenever the inputs change**: "update my why join me", a free-vs-paid rerun, "my digital product is built",
  "refine my partner offer" — each of those skills calls this one silently after it saves, so the package is
  never stale.
- **On demand**: "build my offer package" · "rebuild my offer package" · "my offer package" · "what do I upload
  for my offer kit" · "my offer assets" → hand them the newest package (build it first if none exists).

## Step 0 — Load the Brain (silent)
Read `~/attraction-brain/brain.md` first; pull with **attraction-brain-sync** if the local copy is missing (a tool
error is never "no Brain"). Then:
- `identity/offer.md` — `Status:` first. **`seeds`** → one line and the way back: *"Your offer isn't built yet —
  say 'build my partner offer' and the package comes at the end of that sitting."* Stop. Otherwise read every
  section: the header's `Join-gated package allowed:` line, `## UVP`, `## The program`, `## The framework`,
  `## Structure`, `## Support & community`, `## The problems this offer solves` (the five pains table), `## The
  seven parts`, `## The Partner Offer` (the deliverables table, Teach first, Onboarding Day 1, the first 30 days,
  `Differentiator:`, `Proof plan:`, `What my partners can offer:`), `## How to talk about it`, `## Value stack`,
  `## Digital product`, `## Where to host it`.
- `identity/journey.md` → `## Why join me` (the 60-second, long and one-breath versions). **Not written** → run
  **attraction-why-join-me** in silent mode now (it reads the Brain and asks nothing), then continue. The
  statement is the heartbeat of the offer; the package never ships without it.
- `## Value stack` and `## Digital product` **empty** → run **attraction-free-vs-paid** in silent mode now, then
  continue.
- `identity/proof.md` (the only source of proof; consent per row) · `identity/operations.md` and `brain.md`
  quick reference (the booking link) · `identity/profile.md` (name, brokerage as required, handles, email,
  headshot location) · `identity/compliance.md` (the first line `Status:`; the stamp; the license display) ·
  `identity/brand-visual.md` (the Final kit, the Direction, the `## Design Package brief` block — normally empty
  before Week 3, which is fine) · `memory/magnets.md` → `## Current magnet` (the live guide, for the one-pager's
  free-guide line; "none yet" is fine).

**Compliance:** `set` or `confirmed` → the stamp goes on every public asset. `unset` → build the package (it is
the member's own file) and add one plain line in chat: *"Before any of this goes public, your compliance rules
need setting — say 'paste my compliance link', two minutes."*

## The register (read once, applied everywhere)
`Join-gated package allowed:` decides the words, never the structure (the band names never change):
- **`yes`, or `unknown`** → **the join register, Mike's model**: the program is what an agent receives when they
  partner with the member — "when you join me you don't just get [the brokerage], you also get…". At `unknown`
  Part I carries one line: *"One check is open: confirm with your brokerage's compliance desk that a package may
  be offered as a reason to join. If the answer is no, say 'my brokerage does not allow a join package' and I
  rewrite the lines."*
- **`no`** → **the open register**: the offer is what the member teaches, their story and their mentorship,
  offered to any agent who wants to learn it; nothing is gated on joining; no line reads "join me and get X";
  the product's status line reads "free to any agent who asks".
Compensation is never in either register.

## Step 1 — Assemble the package (structured text, `shared/doc-formatting.md`)
Every line is copied from the Brain — the same words as `offer.md`, `journey.md` and the Partner Offer
document; nothing added, nothing "punched up", no new claims, no new numbers. Part bands are CAPS bands wrapped
by rules; **every heading inside a part is a sub-band `──── LIKE THIS ────`**. Never a line of copy in capitals;
never a `[` bracket token; no skill ids anywhere in the file; fifth-grade reading level is the Brain's already.

```
OFFER PACKAGE — [PROGRAM NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Built from: Partner Offer [date] · Why Join Me [date] · Value stack [date] · Digital product [status]
Your offer in one file: the offer to join you, your digital product, the copy for every asset that promotes the offer, and the build notes. Upload this file to Claude Design in Week 3 together with your Design Package brief; your Lead Magnet Package is the other file. The words are final; the design serves them.

────────────────────────────────────────────
HOW TO USE THIS IN WEEK 3
•  Open Claude Design, start one project for your offer, and upload this file and your Design Package brief (your brand, from the Week 3 brand chat; without it the brief in Part IV uses the clean neutral look).
•  Ask for the pieces in Part IV one at a time: the Join My Team one-pager, the offer stack, the product mockup, then the deck and the welcome pack. Say "copy verbatim from the package".
•  Save every file into your Offer folder and tell me "my offer kit is designed".

────────────────────────────────────────────
WHAT'S INSIDE
•  Part I — The offer to join me.
•  Part II — The digital product.
•  Part III — The assets that promote the offer: the copy.
•  Part IV — The design brief for the offer kit.

────────────────────────────────────────────
PART I — THE OFFER TO JOIN ME
──── WHY JOIN ME ────
[the one-breath version, verbatim from journey.md → ## Why join me]
[the 60-second version, verbatim]
──── THE ONE LINE ────
The promise: [the UVP one-liner]
Outcome-led: [ ] · Story-led: [ ] · Mechanism-led: [ ]
Why me: [the Differentiator line from ## How to talk about it — what makes the member different from every other leader at their brokerage, which pain they solve that others don't, how they are uniquely equipped]
──── THE PROGRAM ────
Program: [name · type · for · the 90-day outcome · format · cadence]
The method: [the framework's one line]
Steps:
   •  [step — what you do · what you get · the tool or template]      (every step, in order)
──── THE FIVE PROBLEMS IT SOLVES ────
[one line per pain, in this order, from ## The problems this offer solves: the pain in the agent's words → what you get → the outcome · the honest rows: "my brokerage covers this — I walk you through it on a call" or "not my lane"]
──── WHAT YOU GET, AND WHAT'S FREE ────
[the value stack rows, in this order: free · included · discounted — each "what you get · what it does for you · free / included / discounted ([the real price] for my partners)"]
The free line: [the one sentence the member says on a call about what is free from day one]
The up-front cost line: [what costs money, said plainly — or "nothing I offer costs anything beyond what the brokerage charges"]
Honest value line: [only when a real price exists: "[item], normally $[real price], free when you partner with me" — never an inflated figure; omit the label otherwise]
──── PROOF, AND THE PROOF PLAN ────
Proof:
   •  [each consented result as proof.md states it; upline proof labelled as the upline's — or one honest line that there is none yet]
Proof plan: [the Proof plan line from ## The Partner Offer — the founding-partner exchange: who, what they get, the written OK and the 60-second video at day 90]
──── WHY NOW ────
[the offer's Why now, verbatim — one honest reason; never a countdown]
──── WHAT MY PARTNERS CAN OFFER ────
[the What my partners can offer line — the same program, scripts and calls, offered by the member's partners to the agents they attract; co-sponsoring where the brokerage allows it]
──── THE REGISTER ────
[yes: "The program is what an agent receives when they partner with me." · unknown: the same line + the one check · no: "Every public line is what I teach, my story and how I mentor — offered to any agent who wants to learn it; nothing is gated on joining."]

────────────────────────────────────────────
PART II — THE DIGITAL PRODUCT
──── THE PRODUCT ────
Product: [name — outcome-led, from ## Digital product]
Format: [course · playbook · guide · ebook]
For: [the primary type of agent]
Promise: after this, you can [outcome in 30 days] without [the pain]
Built from: [Teach first lesson 1 (and 2–3) — the real sheet, the real setup, the real message]
Outline:
   •  [part 1 — after this you can…]      (3 to 7 parts)
Cover line: [title] · Subtitle: [under 10 words]
Three promises:
   •  [ ]
   •  [ ]
   •  [ ]
──── THE VERSION-ONE PATH ────
Version one, this month: [the template or sheet the member already uses, plus ONE short recording — a 10-to-15-minute screen recording of the first lesson, phone or Zoom — nothing more; the weekly call and the templates are the product; a real product the day that one recording exists]
The full version: [grown in Week 6 with the Value Vault from what the first partners asked for, or "exists — in 05 · Offer" when it does]
Status: [mapped YYYY-MM-DD · version one by [date] · built YYYY-MM-DD]
How it's said in the offer: "[the honest promise line — never a product that won't exist]"

────────────────────────────────────────────
PART III — THE ASSETS THAT PROMOTE THE OFFER
──── THE JOIN MY TEAM ONE-PAGER ────
Headline: [the outcome-led line]
Subhead: [who it is for, by stage and situation]
The promise: [the UVP one-liner]
What you get:
   •  [5 to 7 outcome bullets from the stack — free items first; the brokerage as the last line]
How it works:
   •  [three steps: grab the guide or book the call → the call → Day 1]
Proof:
   •  [consented lines, or the one honest line]
Why me: [the differentiator line]
Call to action: [the booking line — or "email me at …" / "message me on Instagram @…" exactly as the Brain holds it]
Compliance: [the stamp]
──── THE OFFER STACK ────
Stack title: [the program name]
Items:
   •  [each stack row, in order — free first, then included, then discounted — "[what you get] — [the outcome]" with its tag]
The free line: [as Part I]
The up-front cost line: [as Part I]
──── THE PRODUCT MOCKUP ────
Product: [name] · Format: [ ] · Cover line: [ ] · Subtitle: [ ]
Three promises:
   •  [ ]
Status line: ["Included when you partner with me" · "Coming this quarter" · at the open register: "Free to any agent who asks"]
──── THE OPPORTUNITY-CALL DECK, SLIDE BY SLIDE ────
   •  Slide 1 — Who I am: [one line from the story's past]
   •  Slide 2 — The problem: [the pains in the agent's words]
   •  Slide 3 — What changed for me: [the transformation]
   •  Slide 4 — The method: [the framework's one line]
   •  Slide 5 — The program: [name · type · cadence]
   •  Slide 6 — What you get: [the stack, as outcomes]
   •  Slide 7 — Proof: [consented lines]
   •  Slide 8 — Your first 30 days: [the four weeks in a line each]
   •  Slide 9 — How we work together: [the weekly rhythm]
   •  Slide 10 — The model: "We talk through the model on the call, with the documents." (never a figure)
   •  Slide 11 — Why now: [the honest reason]
   •  Slide 12 — Your next step: [the booking line; Day 1 in one line]
──── THE WELCOME PACK (DAY 1) ────
Welcome letter: [120 to 180 words in the member's voice — what happens today, this week, by day 30]
Day 1 checklist:
   •  [the five Onboarding: Day 1 lines]
First lesson: [the first lesson's name and what it hands over]
Calendar: [the weekly call · the first 1:1 · the first Saturday or session]
──── SOCIAL LINES ABOUT THE OFFER ────
Bio line: [ ]
Caption 1: [ ] · Caption 2: [ ] · Caption 3: [ ]      (each under 20 words, outcome first, in the register)
DM: [the DM line]
Comment keyword: [the offer's keyword]
Video script (60 seconds): [the 60-second why join me, verbatim]

────────────────────────────────────────────
PART IV — THE DESIGN BRIEF FOR THE OFFER KIT
DESIGN BRIEF — [PROGRAM NAME] OFFER KIT
[Name] · [Brokerage] · [Date]
──── WHAT TO BUILD ────
•  The Join My Team one-pager (letter or A4, portrait, phone-readable) from Part III.
•  The offer stack graphic: every item in Part III's order, every label verbatim, the product on top.
•  The product mockup: the cover line, the subtitle, the three promises; a flat cover first, a 3D mockup if the tool exports pictures.
•  The opportunity-call deck, one slide per line in Part III; slide 10 carries no figure.
•  The welcome pack: the letter, the checklist, the first lesson, the calendar — one PDF.
•  Square and 9:16 crops of the one-pager's headline and the stack for Instagram and stories.
──── WHO SEES EACH ────
The one-pager and the stack: an agent weighing a move, on a phone · the deck: a 30-minute call · the welcome pack: a new partner on Day 1.
──── THE BRAND ────
From your Design Package brief (do not improvise): Logo · Colours · Fonts · Headshot · Tagline — or, before the Week 3 brand chat: a clean neutral look (the member's headshot, one dark text colour, no accent unless named, the brokerage logo only where compliance requires it); the Week 3 kit restyles everything.
Brokerage mark: [where it must appear — from the compliance file]; the brokerage's own colours are not the palette.
──── THE RULES ────
•  Copy verbatim from Parts I–III. Nothing added, nothing cut.
•  No compensation, splits, revenue share, stock or income anywhere; no other brokerage's name or logo; no ranking, no "best".
•  Proof lines only as written; real photos only — the member's headshot, real agents with consent, never stock people.
•  The compliance stamp on every public piece: [the stamp].
──── WHEN IT'S DONE ────
Save every file into your Offer folder in your drive · tell me "my offer kit is designed" · the one-pager's link and the stack go into your bios, your DMs and your partner call.

════════════════════════════════════════════
▸ COMPLIANCE
[the stamp — set or confirmed only; never a bracket token. Unset: "Compliance rules not set yet — say 'paste my compliance link' before anything here goes public."]
```

Write the real values in — never a `[` bracket token in the member's file. A part whose source is honestly empty
(no consented proof, no priced item) carries its one honest line; it is never invented and never padded. The
lead magnet's name appears only in the one-pager's "How it works" (grab the guide) when a live magnet exists.

## Step 2 — Save, deliver, log
1. **Render** with the shared renderer (`shared/doc-formatting.md`):
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/offer-package.txt "Offer Package — [Program Name] — YYYY-MM-DD.docx" --title "Offer Package — [Program Name]" --subtitle "[Name · Brokerage · City]" --eyebrow "Agent Attraction Offer · the Week 3 upload"`
   and upload the `.docx` to **`05 · Offer`** through the storage connector (`shared/connectors.md`; the workspace
   located by ID). `RENDERER-UNAVAILABLE` or no sandbox → the plain-document upload and its one line, never a
   retry loop. Read the finished document back once: every part a heading, every sub-band a subheading, full
   depth. A rebuild is a new dated copy; **the newest date is current**; a demo build carries ` — DEMO`.
2. **Keep the text** at `~/attraction-brain/exports/offer-package-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`).
3. **Deliver in chat** — the link, the title and five plain lines: what is inside (the four parts in a breath),
   that this is the one file for your offer kit in Claude Design in Week 3 (beside the Lead Magnet Package), where
   it lives ("your Offer folder"), that "rebuild my offer package" refreshes it, and what is still thin (no
   consented proof yet; the product is version one). Never the full text in chat; never a path spoken as a path.
4. **Log it (silently):** `identity/offer.md` → `## Offer Package` → `Status: built YYYY-MM-DD · Offer Package —
   [Program Name] — YYYY-MM-DD` (this skill owns that section and nothing else in the file). **attraction-brain-sync
   PUSH** (write → push → verify). Never narrate this or name the file.

## Step 3 — When another skill calls it (silent)
`attraction-offer` (end of the session), `attraction-why-join-me`, `attraction-free-vs-paid` ("my digital
product is built" included) run Steps 0–2 with no welcome and no question; the caller adds one line to its own
close (*"your Offer Package is rebuilt"*). A gather that fails (connector down) → the caller says so in one line
and names "rebuild my offer package" for later; never a stop, never a retry loop.

## Never
- Rewrite, shorten or "improve" a line while assembling; invent proof, a price, a product or a number; add a
  compensation word; name another brokerage; render a graphic; put a skill id in front of the member.
- Build on `Status: seeds`; ship without the why join me statement; ship a product that will not exist as
  anything but version one without saying so.
- **Make the product big.** Realtors are not course creators: version one is a template plus one short recording,
  never a module list, never "record your course"; a product the member would not finish this month is not a
  product. The Value Vault grows it later, only if the first partners ask.

## Quality checklist
- [ ] Offer finalized or built; why join me written; stack and product present (run their skills silently if not)
- [ ] Parts I–IV present; every inner heading a sub-band; copy verbatim; the register applied everywhere; no `[` token
- [ ] Proof only from the proof file; the proof plan present; the free line and the up-front cost line present
- [ ] The product is small: a template plus one short recording for version one — no module list, no course to build
- [ ] Rendered, uploaded to 05 · Offer with the dated name, read back; the text kept in exports/
- [ ] Chat = link + title + five lines; `## Offer Package` stamped; pushed
