# The Partner Offer doc — the program definition that renders to `05 · Offer`

A clean, member-facing document in the one neutral house style (`shared/doc-formatting.md`), rendered through
`shared/render_doc.py`. It is **the member's partner program, defined like a product**: what the thing IS,
what it is called, who it is for, how it is built, what an agent actually receives, what Day 1 and the first
30 days look like, who is in the room, and how to talk about it. The member reads it, says it on calls,
hands it to an agent — and every downstream system builds from it: the Lead Magnet plugin's three
recommendations and the magnet itself (`lm-magnet-ideas`, `lm-magnet`), the funnel's product image and
WHY PARTNER section (`lm-funnel`, `aa-funnel-design`), the offer stack and the product mockup
(`aa-offer-kit-design`), the call presentation (`cv-presentation`). **If this document does not say what the
program is, everything after it breaks.** That was the live-run verdict of 2026-10-10: a 1,000-word offer
with no type, no name as a program, no framework, no structure, no onboarding sequence, no list of what an
agent receives, and several sections rendered as a heading over one stray line. Never again.

Written in the member's first-person voice (`identity/voice.md`), fifth-grade reading level, outcomes not
features (`04-value-proposition/32`). It reads like a program prospectus the member would be proud to send —
book-like (long, sectioned, tables where structure clarifies, prose where prose persuades) — but it is **not
the Brain Book**: a legacy render (no `[[TOC]]`, no `PART`/`CHAPTER` bands, no `>> ` lines — in a one-off
document `>> ` is a script cue, not an insight box). Its last line is always the compliance line, verbatim.

**Length: 2,500 to 4,000 words.** Every section has a floor. Floors are minimums, never a reason to compress
a rich Brain; a member with three recorded modules and five partners renders longer, and that is correct.
Under 2,500 words, or any section under its floor, or a section that is a heading with one line under it,
is a FAILED render — the verification gate in `SKILL.md` runs on every build before delivery.

**It is a render, never a source.** Everything in it exists in `identity/offer.md` first (the program block,
the framework table, the structure, the deliverables, the onboarding, the support lines, the four ways to
say it); proof only from `identity/proof.md`; the cadence from `identity/operations.md`; the type of agent
from `identity/avatars.md`. The doc never holds a fact the Brain doesn't.

---

## The render command

```
python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/partner-offer.txt \
  "Partner Offer · [Member] · [YYYY-MM-DD].docx" \
  --title "[Program name]" --subtitle "[the UVP one-liner]" --eyebrow "Partner Offer" [--accent HEX]
```
- `--title` is the PROGRAM NAME (the cover's headline); `--subtitle` is the UVP one-liner (the cover's second
  line and the footer's member line); `--eyebrow "Partner Offer"` (demo: `"Partner Offer · Demo"`).
- `--accent HEX`: the member's primary brand colour when `identity/brand-visual.md` records one (the Final
  kit `Colors:` line first, else the Direction block's primary); none recorded → omit the flag. Never the
  brokerage's colour.
- Saved to `05 · Offer` (newest date is current), then pushed. Demo filename:
  `💼 [Name]'s Partner Offer — DEMO — [YYYY-MM-DD].docx`, never into a real workspace.
- Renderer stderr must show ZERO warnings. `RENDERER-UNAVAILABLE` → install nothing; save the structured
  text as a `.md` file, upload that, say in one line that the styled version needs the renderer. Once.

## The grammar this doc uses (from `shared/doc-formatting.md` — nothing else)

- **Cover block** = the first lines before the first band: the program name on line 1 (the renderer takes
  `--title` over it), the UVP one-liner on line 2 (`--subtitle` dedupes it), then the meta line
  `[Member] · [brokerage — generic if compliance requires] · [Month D, YYYY]`, then (demo only) the demo line.
- **Section bands**: `────…────` rule, the band text in CAPS (`1 · THE PROMISE`), `────…────` rule, blank
  line. Fourteen bands, numbered, in the order below; the number and the middle dot are part of the band.
- **Sub-headings** inside a section: `──── Label ────` (label ≤ 80 characters).
- **`Label:` lines** for the program block (`Type: mentorship program — …`), signature lines, the keyword,
  the booking line. A `Label:` line directly above a table stays on the table's page.
- **Pipe tables** (`| a | b |` one row per line) for the four-ways table, the framework, the problems, the
  structure, the deliverables, the first 30 days, the layers. Never a table as a wall of prose.
- **`•` bullets** for lists; **numbered steps** `1.  …` for the Day 1 sequence — open each step with a plain
  word (`1.  The welcome call — 45 minutes …`), never a capital run that the renderer would read as a bold
  lead (`1. A 45-minute call` splits as "A 45-"). The sanctioned bold lead is ALL CAPS ending in a dash
  (`1.  WELCOME CALL — …`).
- Plain text in the body: no Markdown `#`, `**`, backticks; no `>> ` lines; no line beginning with `[`.
- **No bracket placeholders anywhere** — real or demo. "None yet — building it with my first partners" is
  written in words.

---

## The structure — the cover and fourteen sections, in this order

### Cover
- Line 1 — **the program name** as the title (`--title`).
- Line 2 — **the UVP one-liner** as the subtitle, in its locked shape: "I help [agent] achieve [outcome]
  through [unique mechanism]."
- Line 3 — `[Member] · [brokerage, generic if compliance.md's name rule requires] · [Month D, YYYY]`.
- Demo only — the Book spec's cover line, verbatim: `Demo document — illustrative data, not researched.`

### 1 · THE PROMISE — 200+ words
Source: `## UVP`, `avatars.md`'s portrait, `journey.md`'s hardest stretch.
- The UVP one-liner as the opening sentence, then two or three paragraphs that put the primary type of agent
  on a Tuesday: what their year looks like, what they have tried, what they are quietly worried about, and
  the one sentence of the member's own story that is the mirror (the "Say it like this" line from
  `avatars.md`). This is the article's opening, not a heading-and-bullets block.
- **The four ways to say it** — a table `| How | The line |` with four rows: the UVP (locked shape) ·
  outcome-led · story-led · mechanism-led. The four lines the member picked at Stop 2.

### 2 · WHAT THIS IS — 250+ words — THE CORE
Source: `## The program` in `offer.md`. One block that defines the program, every line present, as `Label:`
lines (one per line, in this order), each followed by its plain-words sentence:
- `Name:` the program name.
- `Type:` exactly ONE of: partnership program · mentorship program · coaching program · accelerator ·
  course plus community · team system — then a dash and the one-line reason, chosen from what the member
  actually does (the type rule in `SKILL.md` §5).
- `Who it is for:` the primary type of agent in plain words (stage, production, model, mindset — never a
  protected characteristic), one sentence on the secondary type if there is one.
- `The 90-day outcome:` what the partner can SHOW by day 90 — the routine running, the first result from
  it — never what they will earn; one honest sentence that no result is promised, the method is.
- `Format:` the mix — 1:1 · group · recorded · in person — each named with what it is ("live group call",
  "one recorded lesson, more recorded with my first partners", "1:1 on Zoom").
- `Cadence:` the weekly call with its day, time and length · office hours if any · the group chat · the 1:1
  rhythm (Day 1, the first week, day 30, after that).
- `Duration:` the 90-day on-ramp (phases 1–3), then the ongoing partnership and what continues in it.
- `What it costs you:` "nothing today — everything here comes with the partnership"; any discounted item
  named by `## Value stack` once free-vs-paid has run (said plainly, price up front); the brokerage's own
  charges are "part of the model conversation, on a call, with the documents". NEVER compensation — no
  split, cap, stock, rev share, income, or the word "fees".
- `What this is not:` two lines — the two things an agent might wrongly expect (from `avatars.md`'s "what
  they've tried" and the "Not the right fit" line): "Not a lead program — …" · "Not a pitch about the
  brokerage — …".

### 3 · THE [FRAMEWORK NAME] — 300+ words
Source: `## The framework` in `offer.md` (built from the Teach-first lessons and `strategy.md`'s Teach-it rows).
Band: `3 · THE [NAME]` — add the word FRAMEWORK only when the name doesn't already say what it is.
- One paragraph on **how it works** — the member's method in their voice, with the one line of their own
  story that produced it (the turning point from `journey.md`).
- The table `| Step | What you do | What you get | The tool or template | Taught in |` — 3 to 7 named steps
  (a verb or a short name per step), every "Taught in" cell a phase or lesson from section 5.
- **The one-line version for graphics** as a `Label:` line (`One line:` …) — under 20 words, the steps as
  a chain ("Host → Ask → Text → Track → Table"); the offer stack and the funnel reuse it as-is.
- When the member had no name: the consultant move ran at Stop 1 — three options from their words, one
  recommended, the chosen one used here; the doc never shows the options.

### 4 · THE PROBLEMS I SOLVE — 200+ words
Source: `## The problems this offer solves` / the five-pains table in `offer.md`.
- A short narrative above the table (80+ words): the pains in the member's words, which they solve
  themselves, which the upline and brokerage carry, and the one that is "not my lane" if any.
- The table `| Their problem | Why it hurts right now | What I do about it | Proof |` — three to five rows,
  only from the overlap; a Proof cell with nothing yet reads "none yet — building it with my first
  partners" in words, never a bracket.

### 5 · HOW THE PROGRAM IS BUILT — 300+ words
Source: `## Structure` and the Teach-first table in `offer.md`.
- **The phases** (3 or more) — one sub-band or table row each: the phase name and days, what is LIVE and
  what is RECORDED in it, which framework steps live in it, what "done" looks like. A phase table
  `| Phase | Days | Live | Recorded | Framework steps | Done when |` is the default shape.
- **The first three lessons** — the Teach-first table `| Lesson | After this you can | What's on screen |
  Template handed over | Run time |`. Lesson 1 concrete enough to record tonight; a lesson not yet
  recorded is written exactly so ("taught live at the Tuesday call; recorded with my first partners").
- **The rest as an outline** — the remaining lessons or modules as a numbered list, one line each, each
  tagged live or recorded, each naming the phase it lives in.

### 6 · WHAT YOU GET — 250+ words
Source: the deliverables in `## The Partner Offer` (`What's included`) + `## The three value layers`.
- One paragraph on how to read the list (the member's own things first, then the organization's, then the
  brokerage's; everything real today or marked).
- The deliverables table `| What | What it is | Format | Free or discounted | Exists today? |` — SIX or more
  rows: the member's own items first, then the upline's (generic names, with the access line), then ONE
  generic row "everything my brokerage provides — walked through on a call". Every row is real today or
  reads "built with my first partners". `Free or discounted` follows `## Value stack` when free-vs-paid has
  run; before that every member item is "included".
- Close with the line: "And everything my brokerage provides — I walk you through that on a call."

### 7 · YOUR FIRST 30 DAYS — 250+ words
Source: `## The Partner Offer` → `Onboarding: Day 1` lines and the `First 30 days` table.
- **Day 1** as numbered steps (4 or more): the welcome call (length, where, what to bring) · the setup
  (what is handed over on the call) · the first lesson (sent or watched together) · the group introduction
  (the chat, the weekly call invite) · the first date put on the calendar.
- The week-by-week table `| Week | You | Me | Done when |` — all four weeks; week 1 is always the 1:1
  onboarding and lesson 1's setup together; week 4 ends with the partner's first result or an honest reset.
- A `Done when:` line for the month — the three things that are true at day 30.

### 8 · SUPPORT AND COMMUNITY — 150+ words
Source: `## Support & community` in `offer.md` (from `operations.md`).
- The weekly call (name, day, time, length, what happens on it) · the group chat (who is in it today, what
  it is for) · the 1:1 cadence · the response expectation in plain words ("I reply the same day on
  weekdays; Sunday evening for anything about a sign-in sheet") · who else is in the room (the upline, a
  mentor — first names only, labeled as the upline's) · the organization's rhythm (the recognition moment,
  the monthly check, what repeats).

### 9 · THE THREE LAYERS — 150+ words
Source: `## The three value layers`.
- The table `| Layer | What it gives you | How you reach it |` with three rows — brokerage · upline / my
  organization · me — generic names, outcome lines, the access line ("I walk you through all of it on a
  call", "I'll introduce you"). One paragraph on why the layers are listed this way (the newest partner is
  never asked to wait for the member to build everything: the upline's and the brokerage's assets are
  theirs on day one).

### 10 · THE [PLAYBOOK · COURSE · GUIDE] YOU WILL OWN — 150+ words
Source: `## Digital product` (owned by `attraction-free-vs-paid`; this doc carries its promise) and
`## The framework`. Band: `10 · THE [FORMAT] YOU WILL OWN` with the format word the product map chose
(playbook · course · guide · ebook); before free-vs-paid has run: `10 · THE PLAYBOOK YOU WILL OWN`.
- The digital product promise: name, format, who it is for, **the three things it does for them** (bullets).
- If it is still being built: "First version with my first partners — built this quarter." Never a promise
  of a product that will not exist.
- **The lead-magnet seed line**, as a `Label:` line (`The free cut:` …): which framework step (or steps) the
  free lead magnet is cut from, and why that step runs without the member — so `lm-magnet-ideas` has a
  seed. When a magnet is already live (`memory/magnets.md → ## Current magnet`, mirrored in `brain.md`),
  name it and its keyword here instead of re-seeding.

### 11 · PROOF — 100+ words
Source: `identity/proof.md` ONLY.
- The member's own result with the method (as written there, with its label) · agents already helped
  (first names or initials, the result, consent state in plain words — "said on calls; her written OK
  before it goes in print") · the organization today · upline proof labeled as the upline's.
- Zero proof → in words: "None yet — I'm building it with my first partners. Mike's own path: help agents
  for free and earn the first case study." Never manufactured credibility, never a bracket.

### 12 · WHY NOW — 100+ words
Source: the seven parts → `Why now`. The honest paragraph: the real reason to move this quarter (a first-partner
window, a cohort date, a season, the size of the table today) — and why waiting costs the agent something
in their own pain's terms. No countdown clocks, no fake scarcity.

### 13 · HOW TO TALK ABOUT IT — 150+ words
Source: `## UVP` + `## How to talk about it`.
- `The four lines:` the four ways to say it (section 1's table, repeated as four `Label:` lines so the member
  can copy them) — or a one-line pointer to the table plus the three lines below when the member asked for
  a shorter doc (the floor still binds).
- Three short lines under 20 words — DM · caption · bio — as `Label:` lines, first person, in their voice.
- `Comment keyword:` the ONE word in caps — "Comment [KEYWORD] and I'll send it."
- `The booking line:` from `operations.md` ("not set yet — add it in your operations" when missing, in words).
- `What the call is:` one sentence in the member's voice — "30 minutes, about your business, no pitch —
  bring your [the thing]."

### 14 · NEXT STEP — then the compliance line
- The ask, in the member's voice (book the call, bring the thing), the keyword line once more, and one
  sentence on what happens after the call (the Day 1 sequence, in one line).
- **Last line, verbatim:** *Compensation isn't on this page on purpose — it's a private, brokerage-approved
  conversation. Before this goes anywhere public, check your brokerage's advertising and rev-share marketing
  rules.*

---

## Demo mode (`config.md` → `Demo brain: yes`, or the member explicitly asked for a fictional demo)
- Every production, money, ratio, count and landscape figure carries "(illustrative — demo)" exactly as
  `shared/brain-book-spec.md` → DEMO BRAINS says (dates, clock times, durations, step and week numbers, and
  cells under a tagged header are exempt). No real competitor, sponsor, lead-vendor, CRM or coach names.
- The cover carries the demo line verbatim; the eyebrow is `Partner Offer · Demo`; the filename carries
  `— DEMO —`. Never saved into a real workspace; never handed to the Design Studio as "the" Partner Offer.
- **Every section COMPLETE at its floor** — a demo is never thinner than a real build; it is what the
  training video shows. A demo never renders a bracketed token.
- Real builds get the mirror tripwire: "(illustrative — demo)", a DEMO filename, or the demo cover line
  appearing anywhere = automatic FAIL; rebuild from the Brain files.

## What never appears
Splits, caps, fees, tiers, stock, rev share, income figures (the compliance last line is the one sanctioned
mention of compensation); another brokerage's name as a comparison; a former brokerage by name; a claim not
in `proof.md`; a lesson, module, call or product that does not exist and is not marked "built with my first
partners"; bracketed template text; a section that is a heading over one line; `>> ` lines; Markdown.
