---
name: attraction-week3-kit
description: >
  Builds the member's WEEK 3 KIT: the ONE file they upload to Claude Design in Week 3, saved in their home
  base folder beside the Brain Book. Part A, the offer: the offer to join me in Mike's anatomy (why join
  me, the one line, why me, the five problems it solves, the value stack with the free line and the
  up-front cost line, the proof plan, why now, what their partners can offer), the digital product kept
  small, the copy for every asset that promotes the offer (one-pager, offer stack, product mockup, call
  deck, welcome pack, bio line, captions, DM, video script) and the offer-kit design brief. Part B, the
  lead magnet: the guide and the page word for word with their build notes, written by the Lead Magnet
  plugin and included verbatim. Assembled, never rewritten; newest wins; runs on its own after the offer
  session and whenever a part changes. Trigger on: "build my Week 3 kit", "my Week 3 kit", "rebuild my
  kit", "what do I upload to Claude Design", "what do I upload for my offer kit".
---

# The Week 3 Kit — the one file for Claude Design

A member finishing Week 2 should hold **three things**: their offer (the document they walk an agent through),
their guide (the PDF agents download) and **one kit** they upload to Claude Design in Week 3. Everything else —
the why-join-me story, what is free and what costs, the digital product, the page copy, the asset copy, the design
briefs — lives inside the kit or inside the Brain, never as another document in the member's chat
(`04-value-proposition/33`, `/34`, `/31`, `/28`). **This skill assembles the kit from the Brain and never rewrites a
word; it renders no graphic.** Part II (the lead magnet, chapters 7–10) is written by the Lead Magnet plugin and included verbatim.

Follow `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md` by
reference. Doctrine: `${CLAUDE_PLUGIN_ROOT}/shared/attraction-doctrine.md` §10–§11. Documents:
`${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` and `shared/render_doc.py`. The contract:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## When it runs
- **At the end of a standalone offer session** ("build my partner offer"), after `attraction-offer` has run
  `attraction-why-join-me` and `attraction-free-vs-paid` in silent mode: the kit is built with Part A and a one-line
  Part B ("your lead magnet joins this file at the end of your lead magnet session"). **When the Lead Magnet plugin
  started the session**, the offer step skips the kit; the Lead Magnet plugin builds it once, at the end of the
  sitting, with both parts.
- **Whenever a part changes**: the Lead Magnet plugin's `lm-package` (after the guide and the page, the bios or the
  delivery kit), `attraction-why-join-me`, `attraction-free-vs-paid`, "refine my partner offer" — each calls this
  skill silently after it saves. The kit is never stale and never duplicated: a rebuild is a new dated copy and the
  superseded copy is trashed after the new one is verified.
- **On demand**: "build my Week 3 kit" · "my Week 3 kit" · "rebuild my kit" · "what do I upload to Claude Design" ·
  "what do I upload for my offer kit" (and the older "build my offer package") → hand them the newest kit (build it
  first if none exists).

## Step 0 — Load the Brain (silent)
Read `~/attraction-brain/brain.md` first; pull with **attraction-brain-sync** if the local copy is missing (a tool
error is never "no Brain"). Then:
- `identity/offer.md` — `Status:` first. **`seeds`** → one line and the way back: *"Your offer isn't built yet —
  say 'build my partner offer' and your Week 3 Kit comes at the end of that sitting."* Stop. Otherwise read every
  section: the header's `Join-gated package allowed:` line, `## UVP`, `## The program`, `## The framework`,
  `## Structure`, `## Support & community`, `## The problems this offer solves`, `## The seven parts`, `## The Partner
  Offer` (the deliverables, Teach first, Onboarding Day 1, the first 30 days, `Differentiator:`, `Proof plan:`,
  `What my partners can offer:`), `## How to talk about it`, `## Value stack`, `## Digital product`, `## Where to
  host it`, `## What I assumed`, `## How to create it`, `## Start with your upline`, `## If your brokerage does not allow a
  join-gated package`, `## Content branches` (chapter 6), `## Week 3 Kit` (the last build).
- `identity/journey.md` → `## Why join me`. **Not written** → run **attraction-why-join-me** in silent mode now,
  then continue. The statement is the heartbeat of the offer; the kit never ships without it.
- `## Value stack` and `## Digital product` **empty** → run **attraction-free-vs-paid** in silent mode now, then
  continue.
- `identity/proof.md` (the only source of proof; consent per row) · `identity/operations.md` and `brain.md` quick
  reference (the booking link) · `identity/profile.md` (name, brokerage as required, handles, email, headshot
  location) · `identity/compliance.md` (the first line `Status:`; the stamp; the license display) ·
  `identity/brand-visual.md` (the Final kit, the Direction, the `## Design Package brief` block — normally empty
  before Week 3, which is fine) · `memory/magnets.md` → `## Current magnet` (the live guide; "none yet" is fine).
- **Part II's text:** the newest `~/attraction-brain/exports/kit-magnet-*.txt` (written by the Lead Magnet plugin's
  `lm-package` — chapters 7 to 10: the outline and the guide word for word, the page, the messaging, the design brief
  for the guide and the page). None → Part II is one honest chapter (below). Never write Part II's copy here.

**Compliance:** `set` or `confirmed` → the stamp goes on every public asset. `unset` → build the kit (it is the
member's own file) and add one plain line in chat: *"Before any of this goes public, your compliance rules need
setting — say 'paste my compliance link', two minutes."*

## The register (read once, applied everywhere)
`Join-gated package allowed:` decides the words, never the structure:
- **`yes`, or `unknown`** → **the join register, Mike's model**: the program is what an agent receives when they
  partner with the member — "when you join me you don't just get [the brokerage], you also get…". At `unknown`
  Part A carries one line: *"One check is open: confirm with your brokerage's compliance desk that a package may be
  offered as a reason to join. If the answer is no, say 'my brokerage does not allow a join package' and I rewrite
  the lines."*
- **`no`** → **the open register**: the offer is what the member teaches, their story and their mentorship, offered
  to any agent who wants to learn it; nothing is gated on joining; no line reads "join me and get X"; the product's
  status line reads "free to any agent who asks".
Compensation is never in either register.

## Step 1 — Assemble the kit (structured text, `shared/doc-formatting.md`)
Every line is copied from the Brain (Part I) or from the Lead Magnet plugin's text (Part II) — the same words as
`offer.md`, `journey.md` and the Partner Offer document; nothing added, nothing "punched up", no new claims, no new
numbers. **The kit is a book** (the renderer's book grammar): a cover page, a linked CONTENTS page from the `[[TOC]]`
block, `CHAPTER n — TITLE` bands that each start on a new page with a small kicker, `PART I` / `PART II` opener
pages, and **every heading inside a chapter a sub-band `──── LIKE THIS ────`**; the guide's own `── PAGE N - TITLE ──`
lines stay as they are. Chapter 1 is the two-page summary the member actually reads; the TOC summaries are the
plain-words line under each entry. Never a line of copy in capitals; never a `[` bracket token; no skill ids
anywhere in the file. Chapter 1's two outline blocks are copied from Part II's own outline and structure sub-bands
(the Lead Magnet plugin writes them); chapter 6 is rendered from `offer.md`'s member sections (`## How to talk about
it`, `## What I assumed`, `## How to create it`, `## Start with your upline`, `## If your brokerage does not allow a
join-gated package`, `## Where to host it`, `## Content branches`) — the pages that used to sit at the back of the
Partner Offer document.

```
Week 3 Kit — [First Last]
[Name] · [Brokerage] · [City] · [Date]   ·   Built from: Partner Offer [date] · Why join me [date] · Value stack [date] · Lead magnet [date, or "not yet"] · Page copy [date, or "not yet"]
Upload this file to Claude Design in Week 3, with your Design Package brief. You do not have to read it cover to cover: chapter 1 is your two-page summary, and the contents page finds anything in one click. Everything after chapter 1 is reference, word for word, for the design session.

[[TOC]]
CHAPTER 1 — YOUR WEEK 2 AT A GLANCE :: your offer, your lead magnet outline and your page outline on two pages, and what to do in Week 3
PART I — YOUR OFFER
CHAPTER 2 — THE OFFER TO JOIN ME :: why join me, the one line, the five problems it solves, what you get and what's free, proof, why now
CHAPTER 3 — THE DIGITAL PRODUCT :: the one thing you give agents who join — small on purpose
CHAPTER 4 — THE ASSETS THAT PROMOTE THE OFFER :: the Join My Team one-pager, the offer stack, the product mockup, the call deck, the welcome pack, the social lines
CHAPTER 5 — THE DESIGN BRIEF FOR THE OFFER KIT :: what to build and the rules
CHAPTER 6 — YOUR OFFER, FOR YOUR EYES ONLY :: the words to use, what I assumed, how to create it, start with your upline, the brokerage rule, where to host it, your content branches
PART II — YOUR LEAD MAGNET
CHAPTER 7 — YOUR GUIDE, WORD FOR WORD :: the outline, then every page exactly as written
CHAPTER 8 — THE OPT-IN PAGE AND THE THANK-YOU PAGE :: the eleven sections, the pop-up, the thank-you page
CHAPTER 9 — THE MESSAGING :: headline, hook, button, keyword, call line; the bios and the DMs when written
CHAPTER 10 — THE DESIGN BRIEF FOR THE GUIDE AND THE PAGE :: what to build, the rules, and notes for whoever builds the page
[[/TOC]]

────────────────────────────────────────────
CHAPTER 1 — YOUR WEEK 2 AT A GLANCE
────────────────────────────────────────────
Your offer, your guide and your page, on two pages. Everything else in this file is the same words again, laid out for the designer.
| What | [Program name] |
| Program | [name — type, in plain words] |
| For | [the type of agent] |
| The promise | [the outcome-led line] |
| The method | [the framework's one line] |
| What's free from day one | [the free line] |
| What it costs | [the up-front cost line] |
| Why me | [the Differentiator line] |
| Next step | [the booking line · the comment keyword] |
──── YOUR LEAD MAGNET: THE OUTLINE ────
[copied from Part B's outline block — the title, the promise, one line per page — or the one honest line that the lead magnet joins this file at the end of the lead magnet session]
──── YOUR SALES FUNNEL OUTLINE ────
[copied from Part B's structure block — the eleven sections one line each with their headline, the pop-up, the thank-you page — or the same honest line]
──── WHERE EVERYTHING LIVES ────
•  Your offer — the Partner Offer document, in your Offer folder: the pages you walk an agent through.
•  Your guide — in your Guides folder: open it in Word or Google Docs and download it as a PDF to hand out this week.
•  This kit — in your home base folder beside your Brain Book: the one file you upload to Claude Design in Week 3.
──── HOW TO USE THIS IN WEEK 3 ────
•  Open Claude Design, start one project, and upload this file and your Design Package brief (your brand, from the Week 3 brand chat; without it the briefs below use the clean neutral look).
•  Ask for the pieces one at a time, in this order: the Join My Team one-pager, the offer stack, the product mockup, the guide PDF with its cover, the opt-in page, the thank-you page, then the call deck and the welcome pack. Say "copy verbatim from the kit".
•  Save every file into your drive — the offer pieces in your Offer folder, the guide PDF and its cover in your Guides folder — and tell me "my offer kit is designed" and "the PDF is done".

────────────────────────────────────────────
PART I — YOUR OFFER
────────────────────────────────────────────
The offer an agent joins, and everything that promotes it. Chapters 2 to 5 are for the designer; chapter 6 is for you.

────────────────────────────────────────────
CHAPTER 2 — THE OFFER TO JOIN ME
────────────────────────────────────────────
──── WHY JOIN ME ────
[the one-breath version, verbatim from journey.md → ## Why join me]
[the 60-second version, verbatim]
──── THE ONE LINE ────
The promise:  [the UVP one-liner]
Outcome-led:  [ ] · Story-led:  [ ] · Mechanism-led:  [ ]
Why me:  [the Differentiator line]
──── THE PROGRAM ────
Program:  [name · type · for · the 90-day outcome · format · cadence]
The method:  [the framework's one line]
Steps:
   •  [step — what you do · what you get · the tool or template]      (every step, in order)
──── THE FIVE PROBLEMS IT SOLVES ────
[one line per pain, Mike's order, from ## The problems this offer solves: the pain in the agent's words → what you get → the outcome · the honest rows: "my brokerage covers this — I walk you through it on a call" or "not my lane"]
──── WHAT YOU GET, AND WHAT'S FREE ────
[the value stack rows in order: free · included · discounted — "what you get · what it does for you · free / included / discounted ([the real price] for my partners)"]
The free line:  [the one sentence the member says on a call about what is free from day one]
The up-front cost line:  [what costs money, said plainly — or "nothing I offer costs anything beyond what the brokerage charges"]
Honest value line:  [only when a real price exists — never inflated; omit the label otherwise]
──── PROOF, AND THE PROOF PLAN ────
Proof:
   •  [each consented result as proof.md states it; upline proof labelled as the upline's — or one honest line that there is none yet]
Proof plan:  [the Proof plan line — the founding-partner exchange: who, what they get, the written OK and the 60-second video at day 90]
──── WHY NOW ────
[the offer's Why now, verbatim]
──── WHAT MY PARTNERS CAN OFFER ────
[the What my partners can offer line]
──── THE REGISTER ────
[yes: "The program is what an agent receives when they partner with me." · unknown: the same line + the one check · no: "Every public line is what I teach, my story and how I mentor — offered to any agent who wants to learn it; nothing is gated on joining."]

────────────────────────────────────────────
CHAPTER 3 — THE DIGITAL PRODUCT
────────────────────────────────────────────
Product:  [name — outcome-led, from ## Digital product] · Format:  [course · playbook · guide · ebook] · For:  [the primary type of agent]
Promise:  after this, you can [outcome in 30 days] without [the pain]
Built from:  [Teach first lesson 1 — the real sheet, the real setup, the real message]
Outline:
   •  [part 1 — after this you can…]      (3 to 7 parts)
Cover line:  [title] · Subtitle:  [under 10 words]
Three promises:
   •  [ ]
   •  [ ]
   •  [ ]
Version one, this month:  [the template or sheet the member already uses, plus ONE short recording — a 10-to-15-minute screen recording of the first lesson — nothing more; the weekly call and the templates are the product]
The full version:  [grown in Week 6 with the Value Vault only if the first partners ask, or "exists — in 05 · Offer"]
Status:  [mapped YYYY-MM-DD · version one by [date] · built YYYY-MM-DD]

────────────────────────────────────────────
CHAPTER 4 — THE ASSETS THAT PROMOTE THE OFFER
────────────────────────────────────────────
──── THE JOIN MY TEAM ONE-PAGER ────
Headline:  [the outcome-led line]
Subhead:  [who it is for, by stage and situation]
The promise:  [the UVP one-liner]
What you get:
   •  [5 to 7 outcome bullets from the stack — free items first; the brokerage as the last line]
How it works:
   •  [three steps: grab the guide or book the call → the call → Day 1]
Proof:
   •  [consented lines, or the one honest line]
Why me:  [the differentiator line]
Call to action:  [the booking line — or "email me at …" / "message me on Instagram @…" exactly as the Brain holds it]
Compliance:  [the stamp]
──── THE OFFER STACK ────
Stack title:  [the program name]
Items:
   •  [each stack row, in order — free first, then included, then discounted — "[what you get] — [the outcome]" with its tag]
The free line:  [as chapter 2] · The up-front cost line:  [as chapter 2]
──── THE PRODUCT MOCKUP ────
Product:  [name] · Format:  [ ] · Cover line:  [ ] · Subtitle:  [ ]
Three promises:
   •  [ ]
Status line:  ["Included when you partner with me" · "Coming this quarter" · at the open register: "Free to any agent who asks"]
──── THE CALL DECK, SLIDE BY SLIDE ────
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
Welcome letter:  [120 to 180 words in the member's voice — what happens today, this week, by day 30]
Day 1 checklist:
   •  [the five Onboarding: Day 1 lines]
First lesson:  [the first lesson's name and what it hands over]
Calendar:  [the weekly call · the first 1:1 · the first Saturday or session]
──── SOCIAL LINES ABOUT THE OFFER ────
Bio line:  [ ]
Caption 1:  [ ] · Caption 2:  [ ] · Caption 3:  [ ]      (each under 20 words, outcome first, in the register)
DM:  [the DM line] · Comment keyword:  [the offer's keyword]
Video script (60 seconds):  [the 60-second why join me, verbatim]

────────────────────────────────────────────
CHAPTER 5 — THE DESIGN BRIEF FOR THE OFFER KIT
────────────────────────────────────────────
──── DESIGN BRIEF — [PROGRAM NAME] OFFER KIT ────
What to build:  the Join My Team one-pager (letter or A4, portrait, phone-readable) · the offer stack graphic (every item in chapter 4's order, every label verbatim, the product on top) · the product mockup (the cover line, the subtitle, the three promises; a flat cover first, a 3D mockup if the tool exports pictures) · the call deck, one slide per line, slide 10 with no figure · the welcome pack as one PDF · square and 9:16 crops of the one-pager's headline and the stack.
Who sees each:  the one-pager and the stack, an agent weighing a move, on a phone · the deck, a 30-minute call · the welcome pack, a new partner on Day 1.
The brand:  from your Design Package brief (logo · colours · fonts · headshot · tagline) — or, before the Week 3 brand chat, a clean neutral look: the member's headshot, one dark text colour, no accent unless named, the brokerage logo only where compliance requires it. Brokerage mark: [where it must appear — from the compliance file]; the brokerage's own colours are not the palette.
The rules:  copy verbatim from chapters 2 to 4; no compensation, splits, revenue share, stock or income anywhere; no other brokerage's name or logo; no ranking, no "best"; proof lines only as written; real photos only; the compliance stamp on every public piece: [the stamp].
When it's done:  save every file into your Offer folder · tell me "my offer kit is designed".

────────────────────────────────────────────
CHAPTER 6 — YOUR OFFER, FOR YOUR EYES ONLY
────────────────────────────────────────────
These pages are yours — never handed to an agent. They used to sit at the back of your Partner Offer document.
──── THE WORDS TO USE ────
The promise:  [the UVP] · Outcome-led:  [ ] · Story-led:  [ ] · Mechanism-led:  [ ] · Why me:  [ ] · Why join me (one breath):  [ ]
The 30-second explanation:  [60 to 90 words, from ## How to talk about it]
DM:  [ ] · Caption:  [ ] · Bio:  [ ] · Video intro:  [ ]
Comment keyword:  [KEYWORD] — "Comment [KEYWORD] and I'll send it."
The free guide is cut from:  [the Lead-magnet seed line]
──── WHAT I ASSUMED (CHANGE ANY OF THESE) ────
   •  [each default the offer card decided, one line each — from ## What I assumed]
──── HOW TO CREATE IT ────
[the four groups from ## How to create it — Record · Write · The first 30 days · The weekly touchpoint — as bullets; a thing that exists today reads "done — reuse it"]
──── START WITH YOUR UPLINE ────
[from ## Start with your upline: the upline's package · your own skill added to it · the offer you can run this week · the three signs, each "true today" or "not yet" · the verdict]
──── THE BROKERAGE RULE ────
[from ## If your brokerage does not allow a join-gated package: the rule in force · what it means for the words · the lines that change · the check, at unknown]
──── WHERE TO HOST IT ────
[from ## Where to host it: Skool recommended · Circle the alternative · your community's name · the 20-minute set-up · keep it simple]
──── YOUR CONTENT BRANCHES ────
[from ## Content branches: 5 to 7 segments, each with its three topics]

────────────────────────────────────────────
PART II — YOUR LEAD MAGNET
────────────────────────────────────────────
The guide and the page that gives it away, exactly as written. Chapters 7 to 10 are written by your Lead Magnet system and included here word for word.

[the Lead Magnet plugin's kit text, verbatim and whole — its own CHAPTER 7 to CHAPTER 10 bands and sub-bands]
   — or, when no kit text exists yet, this one chapter and nothing else:
────────────────────────────────────────────
CHAPTER 7 — YOUR GUIDE, WORD FOR WORD
────────────────────────────────────────────
Your lead magnet joins this file at the end of your lead magnet session this week — say "launch my lead magnet plugin".

════════════════════════════════════════════
▸ COMPLIANCE
[the stamp — set or confirmed only; never a bracket token. Unset: "Compliance rules not set yet — say 'paste my compliance link' before anything here goes public."]
```

Write the real values in — never a `[` bracket token in the member's file. A line whose source is honestly empty
(no consented proof, no priced item) carries its one honest line; it is never invented and never padded. The
`DESIGN BRIEF —` sub-band lines are written exactly, in capitals (the design skills key on them).

## Step 2 — Save, deliver, log
1. **Render** with the shared renderer (`shared/doc-formatting.md`):
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/kit.txt "Week 3 Kit — [First Last] — YYYY-MM-DD.docx" --book --title "Week 3 Kit — [First Last]" --subtitle "[Name · Brokerage · City]" --eyebrow "Agent Attraction · the one file for Claude Design"`
   (the `[[TOC]]` block turns book mode on; `--book` makes it explicit)
   and upload the `.docx` to **`01 · AI Brain`** (the home base folder, beside the Brain Book) through the storage
   connector (`shared/connectors.md`; the workspace located by ID). `RENDERER-UNAVAILABLE` or no sandbox → the
   plain-document upload and its one line, never a retry loop. Read the finished document back once: a cover page,
   a CONTENTS page whose every entry is a link (zero `WARNING: TOC entry` lines on stderr), chapter 1 before Part I,
   every chapter on its own page, every sub-band a subheading, full depth. **Newest wins:** after the new copy is verified, trash the
   superseded `Week 3 Kit — …` copy so the folder holds one kit. A demo build carries ` — DEMO`.
2. **Keep the text** at `~/attraction-brain/exports/week3-kit-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`).
3. **Deliver in chat — one line and the link, never a tour:** *"Your Week 3 Kit is in your home base folder beside
   your Brain Book — the one file you upload to Claude Design in Week 3, with your brand brief. [Part B present: "It
   carries your offer and your lead magnet." · absent: "Your lead magnet joins it at the end of your lead magnet
   session."] Say 'rebuild my kit' any time something changes."* Never the full text in chat; never a path spoken as a
   path.
4. **Log it (silently):** `identity/offer.md` → `## Week 3 Kit` → `Status: built YYYY-MM-DD · Week 3 Kit — [First
   Last] — YYYY-MM-DD · parts: I [+ II]` (this skill owns that section and nothing else in the file).
   **attraction-brain-sync PUSH** (write → push → verify). Never narrate this or name the file.

## Step 3 — When another skill calls it (silent)
`attraction-offer` (end of a standalone offer session), the Lead Magnet plugin's `lm-package`,
`attraction-why-join-me`, `attraction-free-vs-paid` ("my digital product is built" included) run Steps 0–2 with no
welcome and no question; the caller adds one line to its own close (*"your Week 3 Kit is rebuilt"*). A gather that
fails (connector down) → the caller says so in one line and names "rebuild my kit" for later; never a stop, never a
retry loop.

## Never
- Rewrite, shorten or "improve" a line while assembling; write or edit Part B's copy (the Lead Magnet plugin owns it);
  invent proof, a price, a product or a number; add a compensation word; name another brokerage; render a graphic;
  put a skill id in front of the member.
- Build on `Status: seeds`; ship without the why join me statement; leave two kits in the folder.
- **Make the product big.** Realtors are not course creators: version one is a template plus one short recording,
  never a module list, never "record your course". The Value Vault grows it later, only if the first partners ask.
- Save the why-join-me story, the value stack or the page copy as documents of their own — they live here.

## Quality checklist
- [ ] Offer finalized or built; why join me written; stack and product present (run their skills silently if not)
- [ ] Chapter 1 (the summary) first, then Part I with chapters 2–6, then Part II verbatim from the Lead Magnet plugin's text (chapters 7–10) or its one honest chapter; the CONTENTS page links to every chapter; every inner heading a sub-band; the register applied everywhere; no `[` token
- [ ] Proof only from the proof file; the proof plan, the free line and the up-front cost line present; the product small
- [ ] Rendered, uploaded to 01 · AI Brain with the dated name, read back; the older kit trashed; the text kept in exports/
- [ ] Chat = one line + the link; `## Week 3 Kit` stamped; pushed
