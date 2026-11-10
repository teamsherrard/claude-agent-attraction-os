---
name: attraction-week3-kit
description: >
  Builds the member's WEEK 3 KIT: the ONE file they upload to Claude Design in Week 3, beside their Brain
  Book. Part A, the offer: the offer to join me in Mike's anatomy (why join
  me, the one line, why me, the five problems it solves, the value stack with the free line and the
  up-front cost line, the proof plan, why now, what their partners can offer), the digital product kept
  small, the copy for every asset that promotes the offer (one-pager, offer stack, product mockup, call
  deck, welcome pack, six social post outlines, the video pop-ups, every call to action) and the offer-kit design brief. Part B, the
  lead magnet: the guide's outline and brief, the page word for word with its build notes and the bios,
  written by the Lead Magnet plugin and included verbatim. Assembled, never rewritten; newest wins. Trigger on: "build my Week 3 kit", "my Week 3 kit", "rebuild my
  kit", "what do I upload to Claude Design", "what do I upload for my offer kit", "my offer kit is designed".
---

# The Week 3 Kit — the one file for Claude Design

A member finishing Week 2 should hold **three things**: their offer (the document they walk an agent through),
their guide (the PDF agents download) and **one kit** they upload to Claude Design in Week 3. Everything else —
the why-join-me story, what is free and what costs, the digital product, the page copy, the asset copy, the design
briefs — lives inside the kit or inside the Brain, never as another document in the member's chat
(`04-value-proposition/33`, `/34`, `/31`, `/28`). **This skill assembles the kit from the Brain and never rewrites a
word; it renders no graphic.** Chapters 4 to 6 (the lead magnet, the page, the bios) are written by the Lead Magnet plugin and included verbatim.

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
  join-gated package`, `## Content branches` (chapter 8), `## Week 3 Kit` (the last build).
- `identity/journey.md` → `## Why join me`. **Not written** → run **attraction-why-join-me** in silent mode now,
  then continue. The statement is the heartbeat of the offer; the kit never ships without it.
- `## Value stack` and `## Digital product` **empty** → run **attraction-free-vs-paid** in silent mode now, then
  continue.
- `identity/proof.md` (the only source of proof; consent per row) · `identity/operations.md` and `brain.md` quick
  reference (the booking link) · `identity/profile.md` (name, brokerage as required, handles, email, headshot
  location) · `identity/compliance.md` (the first line `Status:`; the stamp; the license display) ·
  `identity/brand-visual.md` (the Final kit, the Direction, the `## Design Package brief` block — normally empty
  before Week 3, which is fine) · `memory/magnets.md` → `## Current magnet` (the live guide; "none yet" is fine).
- **The lead magnet chapters' text:** the newest `~/attraction-brain/exports/kit-magnet-*.txt` (written by the Lead
  Magnet plugin's `lm-package` — chapters 4 to 6: the idea and the outline with the picture ideas and the guide's design
  brief, the page word for word with the words for the guide and the build notes, the bios). None → one honest
  chapter 4 (below). Never write those chapters' copy here.

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
numbers. **The kit is a book** (the renderer's book grammar): a cover page, a linked CONTENTS page from the `[[TOC]]
CHAPTER 1 — SUMMARY :: the whole week on two pages
CHAPTER 2 — YOUR OFFER :: the program, what you get, what's free, proof, why now
CHAPTER 3 — WHY JOIN ME :: the statement, and the words to use
CHAPTER 4 — LEAD MAGNET :: the idea, the outline, the design brief
CHAPTER 5 — SALES FUNNEL :: the page, word for word, and how to build it
CHAPTER 6 — BIOS :: every platform, ready to paste
CHAPTER 7 — DESIGN ASSETS :: one-pager, stack, deck, posts, pop-ups, calls to action
CHAPTER 8 — YOUR NOTES :: assumptions, how to create it, hosting, content branches
[[/TOC]]

────────────────────────────────────────────
CHAPTER 1 — SUMMARY
────────────────────────────────────────────
Your offer, your guide and your page, on two pages. Everything else in this file is the same words again, laid out for you and for the designer.
| What | [Program name] |
| Program | [name — type, in plain words] |
| For | [the type of agent] |
| The promise | [the outcome-led line] |
| The method | [the framework's one line] |
| What's free from day one | [the free line] |
| What it costs | [the up-front cost line] |
| Why me | [the Differentiator line] |
| Next step | [the booking line · the comment keyword] |
──── YOUR LEAD MAGNET ────
[copied from chapter 4's idea and outline blocks — the title, the promise, who it is for, one line per page — or the one honest line that the lead magnet joins this file at the end of the lead magnet session]
──── YOUR SALES FUNNEL OUTLINE ────
[built from chapter 5 — the eleven section bands, one line each with their Headline, then the pop-up and the thank-you page — or the same honest line]
──── WHERE EVERYTHING LIVES ────
•  Your offer — the Partner Offer document, in your Offer folder: the pages you walk an agent through.
•  Your guide — in your Guides folder: open it in Word or Google Docs and download it as a PDF to hand out this week.
•  Your bios — chapter 6 of this file: paste each one into its platform this week.
•  This kit — in your home base folder beside your Brain Book: with your guide, the two files you upload to Claude Design in Week 3.
──── HOW TO USE THIS IN WEEK 3 ────
•  Open Claude Design, start one project, and upload three things: this file, your guide, and your Design Package brief (your brand, from the Week 3 brand chat; without it the briefs below use the clean neutral look).
•  Ask for the pieces one at a time, in this order: the Join My Team one-pager, the offer stack, the product mockup, the guide PDF with its cover, the opt-in page, the thank-you page, the six social posts, the video pop-up set, then the call deck and the welcome pack. Say "copy verbatim".
•  Save every file into your drive — the offer pieces, the posts and the pop-ups in your Offer folder, the guide PDF and its cover in your Guides folder — and tell me "my offer kit is designed" and "the PDF is done".

────────────────────────────────────────────
CHAPTER 2 — YOUR OFFER
────────────────────────────────────────────
──── THE PROGRAM ────
Program:  [name · type · for · the 90-day outcome · cadence]
The method:  [the framework's one line]
The promise:  [the UVP one-liner]
──── THE FIVE PROBLEMS IT SOLVES ────
[one line per pain, Mike's order: the pain in the agent's words → what you get → the outcome · the honest rows: "my brokerage covers this — I walk you through it on a call" or "not my lane"]
──── WHAT YOU GET, AND WHAT'S FREE ────
[the value stack rows in order: free · included · discounted — the upline's rows first when `## Start with your upline` says to lead with them; every row scalable (doctrine §10e) — "what you get · what it does for you · free / included / discounted ([the real price] for my partners)"]
The free line:  [the one sentence the member says on a call about what is free from day one]
The up-front cost line:  [what costs money, said plainly — or "nothing I offer costs anything beyond what the brokerage charges"]
Honest value line:  [only when a real price exists — never inflated; omit the label otherwise]
──── PROOF, AND THE PROOF PLAN ────
Proof:
   •  [each consented result as proof.md states it; upline proof labelled as the upline's — or one honest line that there is none yet]
Proof plan:  [the Proof plan line — the founding-partner exchange: who, what they get, the written OK and the 60-second video at day 90]
──── WHY NOW, AND WHAT MY PARTNERS CAN OFFER ────
Why now:  [the offer's Why now, verbatim]
What my partners can offer:  [the line]
The register:  [yes: "The program is what an agent receives when they partner with me." · unknown: the same line + the one check · no: "Every public line is what I teach, my story and how I mentor — offered to any agent who wants to learn it; nothing is gated on joining."]
──── YOUR DIGITAL PRODUCT ────
Product:  [name — outcome-led] · Format:  [course · playbook · guide · ebook] · For:  [the primary type of agent]
Promise:  after this, you can [outcome in 30 days] without [the pain]
Outline:
   •  [part 1 — after this you can…]      (3 to 7 parts)
Cover line:  [title] · Subtitle:  [under 10 words] · Three promises:  [ ] · [ ] · [ ]
Version one, this month:  [the template or sheet the member already uses, plus ONE short recording — a 10-to-15-minute screen recording of the first lesson — nothing more]
The full version:  [grown in Week 6 with the Value Vault only if the first partners ask, or "exists — in 05 · Offer"] · Status:  [mapped YYYY-MM-DD · version one by [date] · built YYYY-MM-DD]

────────────────────────────────────────────
CHAPTER 3 — WHY JOIN ME
────────────────────────────────────────────
──── WHY JOIN ME ────
[the one-breath version, verbatim from journey.md → ## Why join me]
[the 60-second version, verbatim]
──── THE ONE LINE, FOUR WAYS ────
The promise:  [the UVP one-liner] · Outcome-led:  [ ] · Story-led:  [ ] · Mechanism-led:  [ ]
Why me:  [the Differentiator line]
──── THE WORDS TO USE ────
The 30-second explanation:  [60 to 90 words, from ## How to talk about it]
DM:  [ ] · Caption:  [ ] · Bio:  [ ] · Video intro:  [ ]
Comment keyword:  [KEYWORD] — "Comment [KEYWORD] and I'll send it." · The free guide is cut from:  [the Lead-magnet seed line]

[the Lead Magnet plugin's kit text, verbatim and whole — its own CHAPTER 4, CHAPTER 5 and CHAPTER 6 bands and sub-bands — inserted HERE, between chapter 3 and chapter 7]
   — or, when no kit text exists yet, this one chapter and nothing else in its place:
────────────────────────────────────────────
CHAPTER 4 — LEAD MAGNET
────────────────────────────────────────────
Your lead magnet, your page and your bios join this file at the end of your lead magnet session this week — say "launch my lead magnet plugin".

────────────────────────────────────────────
CHAPTER 7 — DESIGN ASSETS
────────────────────────────────────────────
──── THE JOIN MY TEAM ONE-PAGER ────
Headline:  [the outcome-led line]
Subhead:  [who it is for, by stage and situation]
The promise:  [the UVP one-liner]
What you get:
   •  [5 outcome bullets from the stack — free items first; the brokerage as the last line]
How it works:
   •  [three steps: grab the guide or book the call → the call → Day 1]
Proof:
   •  [consented lines, or the one honest line]
Why me:  [the differentiator line]
Call to action:  [the booking line — or "email me at …" / "message me on Instagram @…" exactly as the Brain holds it]
Compliance:  [the stamp]
──── THE OFFER STACK ────
Stack title:  [the program name] · the product on top
Items:
   •  [each row of chapter 2's WHAT YOU GET, AND WHAT'S FREE, in that order — free first, then included, then discounted — shortened to "[what you get] — [the outcome] · [tag]"]
The free line:  [as chapter 2] · The up-front cost line:  [as chapter 2]
──── THE PRODUCT MOCKUP ────
Product:  [name] · Format:  [ ] · Cover line, subtitle and three promises:  as chapter 2
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
   •  Slide 9 — The model: "We talk through the model on the call, with the documents." (never a figure)
   •  Slide 10 — Your next step: [why now in a clause; the booking line; Day 1 in one line]
──── THE WELCOME PACK (DAY 1) ────
Welcome letter:  [120 words in the member's voice — what happens today, this week, by day 30]
Day 1 checklist:
   •  [the five Onboarding: Day 1 lines]
First lesson:  [the first lesson's name and what it hands over] · Calendar:  [the weekly group call if any · the day-30 self-check date]
──── SOCIAL GRAPHIC POSTS ────
Six posts for the two weeks after your page goes live, one every two or three days, then monthly with new proof. Carousels and single graphics are 1080 by 1350; stories 1080 by 1920, text clear of the top and bottom 250 pixels. One ask per post, from the calls to action below; the stamp on the last slide or in the caption.
Post 1 — The guide:  a carousel, 5 slides.
   •  Slide 1:  [the hero's pre-headline — chapter 5, SECTION 1]
   •  Slides 2 to 4:  [the opt-in's three bullets, one per slide — SECTION 11]
   •  Slide 5:  Comment [GUIDE keyword] and I'll send it.
   •  Caption:  [the hero's subhead] + the guide ask
Post 2 — Five problems, five fixes:  a carousel, 7 slides.
   •  Slide 1:  [a hook in the agent's words, cut from the first problem's pain line — chapter 2]
   •  Slides 2 to 6:  [one problem per slide — the pain in the agent's words with the fix under it, chapter 2's five rows in order]
   •  Slide 7:  the guide ask
   •  Caption:  [SECTION 2's headline] + the guide ask
Post 3 — My story:  a carousel, 5 slides, one line per part of the why-join-me statement.
   •  Slide 1:  [where I was — chapter 3's story-led line]
   •  Slides 2 to 4:  [what I tried · what changed · where I am now — one line each, figures as proof.md states them]
   •  Slide 5:  [why I do this, one line] + "If any of this sounds like your year, message me."
   •  Caption:  [the one-breath statement] + the call ask
Post 4 — What you get:  a single graphic, the offer stack.
   •  Title:  [the program name] · Rows:  the stack items above, free first, then included · Footer:  the free line
   •  Caption:  the up-front cost line + the call ask
Post 5 — Proof:  a single quote card.
   •  Quote:  [the member's own result, as proof.md states it] · Under it:  [one more consented line, or the proof plan's one honest line] · the headshot
   •  Caption:  [the method in one line] + the guide ask      (no result on file yet → the card carries the framework's one line as its steps instead)
Post 6 — Book the call:  a story and a single graphic.
   •  Headline:  [SECTION 10's headline] · Three lines:  [SECTION 10's three questions]
   •  Call to action:  [the booking line] · Story sticker:  "Reply and I'll send you the link."
   •  Caption:  [SECTION 10's "what the call is" and "what it isn't", in one line] + the booking line
──── CALLS TO ACTION ────
Two asks, everywhere. The guide: comment [GUIDE keyword] and the DM sends it. The call: [the booking line]. One ask per piece — the guide in most posts and videos, the call in about one of four and on every proof piece. The same words every time; a keyword never changes once content has used it.
| Where it goes | Ask for the guide | Ask for the call |
| Caption, last line | Comment [GUIDE] and I'll send you [the guide, in three words]. | [the booking line, as a sentence] |
| Comment keywords | [GUIDE] → the DM with the download link | [the offer's keyword] → the one-pager and the invitation to talk |
| Video pop-up, mid-video | Comment [GUIDE] · free guide | [the call in six words or fewer, from the booking line — "30 minutes · message me", "30-minute call · link in bio"] |
| Spoken, in the video | "[what the guide holds, one clause]. Comment [GUIDE] and I'll send it." | "If you want to talk through [the thing they bring], [the booking line]." |
| End card, last 5 seconds | [the guide's title] · Comment [GUIDE] · the stamp | [SECTION 10's headline] · [the booking line] · the stamp |
| Story | Reply [GUIDE] and I'll send it. | Reply and I'll send you the link. |
| Bio, the one link | Free guide: [the guide's title] ↓ | [the booking line] |
| DM, when someone comments | [the Delivery Kit's comment reply — or "not written yet — say 'deliver my guide'"] | "Happy to. Bring [the thing they bring] and [the booking line]." |
Pop-up rules:  six words or fewer, two lines at most, on screen for three seconds · never over the face, never in the lower quarter of a vertical video where captions sit · the name card, [First Last · Brokerage · City], in the first three seconds of every video · the stamp on every end card · [at the open register: no public line says "join me"] · no public line says what the model pays, ever.
──── DESIGN BRIEF — [PROGRAM NAME] OFFER KIT ────
What to build:  the Join My Team one-pager (letter or A4, portrait, phone-readable) · the offer stack graphic (every item in the order above, every label verbatim, the product on top) · the product mockup (the cover line, the subtitle, the three promises; a flat cover first, a 3D mockup if the tool exports pictures) · the six social posts (every slide and caption verbatim, 1080 by 1350; the story at 1080 by 1920) · the video pop-up set as PNGs with transparent backgrounds, at 1080 by 1920 and 1920 by 1080: the name card, the guide pop-up, the call pop-up and the two end cards, text verbatim from the calls to action · the call deck, one slide per line, slide 9 with no figure · the welcome pack as one PDF · square and 9:16 crops of the one-pager's headline and the stack.
Who sees each:  the one-pager, the stack and the posts, an agent weighing a move, on a phone · the pop-ups, inside the member's Reels and videos · the deck, a 30-minute call · the welcome pack, a new partner on Day 1.
The brand:  from your Design Package brief (logo · colours · fonts · headshot · tagline) — or, before the Week 3 brand chat, a clean neutral look: the member's headshot, one dark text colour, no accent unless named, the brokerage logo only where compliance requires it. Brokerage mark: [where it must appear — from the compliance file]; the brokerage's own colours are not the palette.
The rules:  copy verbatim from chapters 2, 3 and 7; no compensation, splits, revenue share, stock or income anywhere; no other brokerage's name or logo; no ranking, no "best"; proof lines only as written; real photos only; the compliance stamp on every public piece: [the stamp].
When it's done:  save every file into your Offer folder · tell me "my offer kit is designed".

────────────────────────────────────────────
CHAPTER 8 — YOUR NOTES
────────────────────────────────────────────
These pages are yours — never handed to an agent.
──── WHAT I ASSUMED (CHANGE ANY OF THESE) ────
   •  [each default the offer card decided, one line each — from ## What I assumed]
──── HOW TO CREATE IT ────
[the four groups from ## How to create it — Record · Write · The first 30 days · The weekly touchpoint — as short bullets; a thing that exists today reads "done — reuse it"]
──── START WITH YOUR UPLINE ────
[from ## Start with your upline: the upline's package · your own skill added to it · the offer you can run this week · the three signs, each "true today" or "not yet" · the verdict — as bullets]
──── THE BROKERAGE RULE, AND WHERE TO HOST IT ────
[from ## If your brokerage does not allow a join-gated package: the rule in force · what it means for the words · the check, at unknown — three lines] · [from ## Where to host it: the host, the community's name, the 20-minute set-up in four bullets]
──── YOUR CONTENT BRANCHES ────
[from ## Content branches: the 5 to 7 segment names on one line, "segment · segment · segment" — the topics live in your Brain; the Week 3 Short-Form plan and the Week 4 YouTube plan build from them]

════════════════════════════════════════════
▸ COMPLIANCE
[the stamp — set or confirmed only; never a bracket token. Unset: "Compliance rules not set yet — say 'paste my compliance link' before anything here goes public."]
```

## The page budget (25 pages is the hard cap — the owner's ruling, 2026-11-09)
Measured on a real build (2026-11-09, a full demo kit rendered through Pages): **pages ≈ words ÷ 370, plus 2** for the
cover and the contents page — the chapter breaks are already inside that average. So the kit holds **at most 8,500
words**. The guide is **not** copied into the kit (it is its own file and is uploaded beside the kit); the page copy is,
once — chapter 1 carries the one-line outlines, chapter 5 never repeats them. Word targets per chapter: 1 ≤ 650 ·
2 ≤ 900 · 3 ≤ 550 · 4 ≤ 700 · 5 the page copy as written (≤ 2,400; 1,900 is typical) plus ≤ 250 of words and build
notes · 6 ≤ 750 · 7 ≤ 1,900 · 8 ≤ 700. A typical build lands near 8,200 words, 24 pages.
**Measure after assembling**, with the standard library only:
`python3 -c "import re;t=open('/tmp/kit.txt').read();p=re.split(r'\n─+\n(CHAPTER \d+ — [^\n]+)\n─+\n',t);w=lambda s:len(re.findall(r\"[A-Za-z0-9'’]+\",s));print(w(t),'words total — about',w(t)//370+2,'pages');[print(p[i][:48],w(p[i+1])) for i in range(1,len(p)-1,2)]"`
Over 8,500 words in total, or a chapter over its target → trim **in this order, once, then re-measure**: every post's
caption to one line · the call deck to 8 slides · the welcome letter to 100 words · chapter 8's upline block to the
three signs and the verdict · chapter 7's one-pager "What you get" to 4 bullets · chapter 6's LinkedIn About to 120
words · chapter 3's 60-second version dropped (the one-breath stays). **Never trim** the summary, the page copy, the
bios' short forms, the calls to action, the briefs' rules or anything an agent reads. Still over after the pass →
deliver, and say in one plain line which chapter is long and why ("your page copy runs long because your offer has
eight deliverables").

Write the real values in — never a `[` bracket token in the member's file. A line whose source is honestly empty
(no consented proof, no priced item) carries its one honest line; it is never invented and never padded. The
`DESIGN BRIEF —` sub-band lines are written exactly, in capitals (the design skills key on them). The social posts and
the calls to action are assembled from lines that already exist — the hero, the opt-in bullets, the five problems, the
statement, the stack, the keyword and the booking line — never a new claim; the only new words are the ask itself.

## Step 2 — Save, deliver, log
1. **Render** with the shared renderer (`shared/doc-formatting.md`):
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/kit.txt "Week 3 Kit — [First Last] — YYYY-MM-DD.docx" --book --title "Week 3 Kit — [First Last]" --subtitle "[Name · Brokerage · City]" --eyebrow "Agent Attraction · the one file for Claude Design"`
   (the `[[TOC]]` block turns book mode on; `--book` makes it explicit)
   and upload the `.docx` to **`01 · AI Brain`** (the home base folder, beside the Brain Book) through the storage
   connector (`shared/connectors.md`; the workspace located by ID). `RENDERER-UNAVAILABLE` or no sandbox → the
   plain-document upload and its one line, never a retry loop. Read the finished document back once: a cover page,
   a CONTENTS page whose every entry is a link (zero `WARNING: TOC entry` lines on stderr), chapter 1 first, every
   chapter on its own page, every sub-band a subheading, full depth, and **under 25 pages** (the budget above). **Newest wins:** after the new copy is verified, trash the
   superseded `Week 3 Kit — …` copy so the folder holds one kit. A demo build carries ` — DEMO`.
2. **Keep the text** at `~/attraction-brain/exports/week3-kit-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`).
3. **Deliver in chat — one line and the link, never a tour:** *"Your Week 3 Kit is in your home base folder beside
   your Brain Book — with your guide, it's what you upload to Claude Design in Week 3, with your brand brief. Chapter 1
   is your two-page summary; chapter 6 is your bios. [lead magnet present: "Your page, your bios and your offer are all in it." · absent: "Your
   lead magnet, your page and your bios join it at the end of your lead magnet session."] Say 'rebuild my kit' any time
   something changes."* Never the full text in chat; never a path spoken as a
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
- Save the why-join-me story, the value stack, the page copy or the bios as documents of their own — they live here.
- Copy the guide into the kit, or let the kit pass 25 pages. The guide is its own file; the budget is the budget.

## Quality checklist
- [ ] Offer finalized or built; why join me written; stack and product present (run their skills silently if not)
- [ ] Chapter 1 (the summary) first, chapters 2–3 the offer and the statement, chapters 4–6 verbatim from the Lead Magnet plugin's text or the one honest chapter 4, chapter 7 the designer's, chapter 8 the private pages; the CONTENTS page links to every chapter; every inner heading a sub-band; the register applied everywhere; no `[` token
- [ ] Measured: under 7,400 words and 25 pages; the guide's full copy NOT in the kit; a trim pass done in the fixed order if needed and said plainly
- [ ] Proof only from the proof file; the proof plan, the free line and the up-front cost line present; the product small
- [ ] Rendered, uploaded to 01 · AI Brain with the dated name, read back; the older kit trashed; the text kept in exports/
- [ ] Chat = one line + the link; `## Week 3 Kit` stamped; pushed

## "my offer kit is designed" (Week 3, record only)
The member says it in Cowork after the Week 3 design session. Stamp `identity/offer.md → ## Week 3 Kit` with
`Designed: YYYY-MM-DD` (never backwards), **attraction-brain-sync PUSH**, and say one line: *"Recorded — your offer kit is
designed. Drop every file into your Offer folder and your Brand folder so everything that makes a graphic for you reads
from there."* No rebuild, no questions.
