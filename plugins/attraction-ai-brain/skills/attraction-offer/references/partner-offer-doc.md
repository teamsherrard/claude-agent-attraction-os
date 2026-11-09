# The Partner Offer doc — the program, written to be read (renders to `05 · Offer`)

A clean, member-facing document in the one neutral house style (`shared/doc-formatting.md`), rendered through
`shared/render_doc.py`. It is **the member's partner program, defined like a product and written like a letter
to the agent who will read it**: what it is called, who it is for, the promise, the method (once, in full), how
the first 90 days run, what an agent receives, Day 1 and the first 30 days, how the two of them work together,
the proof, why now, and the next step. The member reads it in ten minutes, says it on calls, hands it to an
agent — and every downstream system builds from it: the Lead Magnet plugin's one recommendation and the magnet
itself (`lm-magnet-ideas`, `lm-magnet`), the funnel's product image and WHY PARTNER section (`lm-funnel`,
`aa-funnel-design`), the offer stack and the product mockup (`aa-offer-kit-design`), the call presentation
(`cv-presentation`), the content engines' pillars and titles (`sf-gameplan`, `yt-gameplan` — from the content
branches). The **At a glance** page is the one-page summary those systems can build from.

**The member's own pages (Mike, 2026-11-02).** After the agent-facing document closes on the compliance line,
the document carries the pages only the member reads — the intangible half of Week 2's outcome: the marketing
language (in the appendix), how to create the program, how to start with the upline's package, what changes
when the brokerage does not allow a join-gated package, where to host it, and the content branches. Each is
one short section, written from `offer.md`, never a lecture.

**The 2026-10-18 ruling (after a live run):** the old render had the right content and read like a spec —
numbered caps labels ("1 · THE PROMISE", "2 · WHAT THIS IS"), a taxonomy lecture on what the program is not,
"if you only read one section, read this one", the method explained five times, the four one-liners
concatenated into one paragraph, chatty filler about why a section exists, and a demo tag stamped on every
number. The content stays. The shape and the voice change: selling headings written for the agent, the method
in full exactly once, paragraphs of at most three sentences, bold lead-ins, nothing that explains itself.

Written in the member's first-person voice (`identity/voice.md`), fifth-grade reading level, outcomes not
features (`04-value-proposition/32`). It is **not the Brain Book**: a legacy render (no `[[TOC]]`, no
`PART`/`CHAPTER` bands, no `>> ` lines — in a one-off document `>> ` is a script cue, not an insight box).

**Length: the agent-facing document 2,000 to 3,200 words (the cover through YOUR NEXT STEP); the member's own
pages 900 to 1,800 (the appendix through YOUR CONTENT BRANCHES).** Every section has a floor (below). Under a
floor, under a range, or a section that is a heading over one line is a FAILED render; over a ceiling is also a
fail — the document is meant to be read, so prose is cut (never the tables, never a checklist line) and it is
re-rendered once. The verification gate in `SKILL.md` runs on every build before delivery.

**It is a render, never a source.** Everything in it exists in `identity/offer.md` first (the program block,
the framework table, the structure, the deliverables, the onboarding, the support lines, the four ways to say
it); proof only from `identity/proof.md`; the cadence from `identity/operations.md`; the type of agent from
`identity/avatars.md`. The doc never holds a fact the Brain doesn't.

---

## The render command

```
python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" ~/attraction-brain/exports/partner-offer-YYYY-MM-DD.txt \
  "Partner Offer · [Member] · [YYYY-MM-DD].docx" \
  --title "[Program name]" --subtitle "[the UVP one-liner]" --eyebrow "Partner Offer" [--accent HEX]
```
- The input text lives at `~/attraction-brain/exports/partner-offer-YYYY-MM-DD.txt` (demo: `partner-offer-DEMO-…`), never
  in `/tmp`: the Brain Board's offer page re-reads it on every rebuild, and the sync skill carries `exports/*.txt` to
  `01 · AI Brain/_engine/exports/`.
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

- **Cover block** = the first lines before the first band, in this order: the program name (the renderer
  takes `--title` over it) · the UVP one-liner (`--subtitle` dedupes it) · the outcome-led tagline · `by
  [First Last]` · `for [the type of agent, plain words]` · `[Member] · [brokerage — generic if compliance
  requires] · [Month D, YYYY]` · demo only: `Demo: every figure is illustrative`. Seven lines at most.
- **Section bands**: `────…────` rule, the band text in CAPS, `────…────` rule, blank line. Seventeen bands in
  the order below — eleven agent-facing, then the member's six. **Never a number, never a middle dot in a
  band** — the headings sell, they do not index. The band names never change with the brokerage register
  (downstream systems key on them); the words inside them do.
- **Sub-headings** inside a section: `──── Label ────` (label ≤ 80 characters), used for the two tables inside
  "What you get" and for Day 1 inside "Your first 30 days".
- **`Label:` lines** (`The Tuesday table: …`, `Comment keyword: …`, `DM: …`) — a bold lead-in; the renderer
  keeps a `Label:` line directly above a table on the table's page.
- **Pipe tables** (`| a | b |` one row per line) for At a glance, the method, the phases, the first three
  lessons, the deliverables, the weeks. Never a table as a wall of prose.
- **`•` bullets** for lists; **numbered lines** `1.  …` for Day 1 — open each with a plain word (`1.  The
  welcome call — 45 minutes …`), never a capital run the renderer reads as a bold lead (`1. A 45-minute call`
  splits as "A 45-").
- Plain text in the body: no Markdown `#`, `**`, backticks; no `>> ` lines; no line beginning with `[`; no
  ALL-CAPS line except the bands; no `...` (the renderer reads dotted leaders as a metric table).
- **No bracket placeholders anywhere** — real or demo. "None yet — building it with my first partners" is
  written in words.

---

## The structure — the cover, At a glance, twelve sections, then the member's own pages

### Cover
- **The program name** as the title (`--title`) — outcome-based, the naming rule in `SKILL.md` §5 (the
  outcome plus the mechanism in an agent's words; never a club, a portal or a place; an organization or
  community name in use is not the title).
- **The UVP one-liner** as the subtitle, in its locked shape: "I help [agent] achieve [outcome] through
  [unique mechanism]."
- **The outcome-led tagline** — the outcome-led line from `## UVP`'s alternates.
- `by [First Last]`.
- `for [the type of agent, plain words]` — the primary type by stage and situation, one line.
- `[Member] · [brokerage, generic if compliance.md's name rule requires] · [Month D, YYYY]`.
- Demo only — ONE line, exactly: `Demo: every figure is illustrative`. No other demo stamp anywhere on the
  cover.

### AT A GLANCE — 120+ words — the one-page summary
Source: `## The program`, `## The framework` (the one line), `## Support & community`, `## Structure`, the
deliverables table, `## How to talk about it`.
One or two plain sentences, then a **twelve-row label table** `| What | [Program name] |` with these rows in
this order, **each cell one line**:
1. `Program` — the name, then a dash and the type (exactly one of the six) in plain words: "a mentorship
   program: a weekly call, a 1:1 to start".
2. `For` — the primary type of agent by stage, production and situation (never a protected characteristic).
3. `The promise` — the outcome-led line.
4. `The method` — the framework's name and the step chain (the one-line version, under 20 words).
5. `Format` — the mix: live group call · 1:1 · recorded · in person, each named.
6. `Weekly rhythm` — the call (day, time, length, where) · the chat · the 1:1 rhythm.
7. `Your first 90 days` — the three phases by name with their days, and what day 90 looks like.
8. `What you get` — the deliverables as a comma list of outcomes-in-hand; ends "and everything my brokerage
   provides".
9. `What's free from day one` — the free line from `## Value stack` (free-vs-paid's silent run): the items
   that cost the agent nothing, as one sentence; Mike's honest value line when a real price exists ("[item],
   normally $[real price], free when you partner with me").
10. `What it costs you` — the up-front cost line: "nothing today — it comes with the partnership", or the
    discounted items named by `## Value stack` with their real price; the brokerage's own charges are "a call,
    with the documents". NEVER a compensation word. **At `Join-gated package allowed: no`** the row reads
    "nothing — I teach it to any agent who asks; partnering with me is a separate conversation" (the open
    register: the program is what the member teaches, never a package gated on joining).
11. `Why me` — the `Differentiator:` line, one sentence.
12. `Next step` — the booking line and "bring [the thing]", and the comment keyword.
The offer kit, the funnel and the call presentation build from this table; the rest of the document says the
same thing with the detail.

### WHO THIS IS FOR — 80+ words
Source: `avatars.md` one-line target, the secondary type, "what they've tried", "Not the right fit".
The primary type in two or three sentences (stage, production, model, situation, what they have tried), one
sentence on the secondary type if there is one. Then the **two "This is not…" lines**, and only these two,
each as its own sentence: "This is not a lead program — …" · "This is not a pitch about the brokerage — …".
No other sentence in the document says what the program is not.

### THE PROMISE — 150 to 250 words — the story, told once
Source: `## UVP`, `journey.md`'s hardest stretch and turning point, `avatars.md`'s mirror line.
The UVP one-liner as the opening sentence. Then the story in the member's voice: the agent on a Tuesday (the
invoice, the sheet in the drawer, what they tried) · the one sentence of the member's own story that is the
mirror · what changed · what this program is built around. Paragraphs of at most three sentences. The four
ways to say it do NOT appear here — they live in the appendix.

### THE [METHOD NAME], IN [N] STEPS — 200+ words — the method, in full, once
Source: `## The framework`. Band: `THE [NAME], IN [N] STEPS` (the name as the member says it; the word
"framework" only when the name does not already say what it is).
- **One short paragraph on how it works** — the member's method in their voice, with the line of their own
  story that produced it. This is the only place the method is explained; everywhere else it is referenced
  by name or by the one-line chain.
- The table `| Step | What you do | What you get | The tool or template | Taught in |` — 3 to 7 named steps
  (a verb or a short name per step), every "Taught in" cell a phase or lesson from "Inside".
- **The one-line version** as a `Label:` line (`One line:` …) — under 20 words, the steps as a chain ("Host →
  Ask → Text → Track → Table"); the offer stack and the funnel reuse it as-is.
- Nothing else. No "why N steps" paragraph, no second explanation.

### INSIDE [PROGRAM NAME]: YOUR FIRST 90 DAYS — 250+ words
Source: `## Structure` and the Teach-first table.
- **The three phases** (or more), each with a name — a table `| Phase | Days | Live | Recorded | Steps | Ends
  with |` is the default shape: what is LIVE and what is RECORDED in each, which framework steps live in it,
  what it ends with. A fourth row for "then — the partnership" is the default.
- **The first three lessons** — the Teach-first table `| Lesson | After this you can | What's on screen |
  Template handed over | Run time |`. Lesson 1 concrete enough to record tonight; a lesson not yet recorded is
  written exactly so ("live at the Tuesday call; recorded with my first partners").
- **The rest** — the remaining lessons as `•` lines, one each, tagged live or recorded, naming the phase.

### WHAT YOU GET WHEN YOU PARTNER WITH ME — 200+ words
Source: the deliverables in `## The Partner Offer` (`What's included`) + `## The three value layers`.
- One or two sentences on how to read it (my own things first, then my organization's, then the brokerage as
  one line; everything real today or marked).
- `──── From me ────` then the table `| What | What it is | Format | Exists today? |` — the member's own
  items (the templates, the recorded lesson, the calls, the chat, the checks; the digital product with "built
  with my first partners" when that is the truth). **No prices, no values, no "free or discounted" column** —
  nothing on this page is priced.
- `──── From my organization ────` then the same table for the upline's items (generic names, the access line
  in the What-it-is cell: "I'll introduce you").
- **The brokerage as one line**, the last line of the section: "And everything my brokerage provides — I walk
  you through that on a call, with the real documents."
- Six or more rows across the two tables; every row real today or reads "built with my first partners".
- **What my partners can offer** — the last paragraph before the brokerage line: the `What my partners can
  offer:` line from `## The Partner Offer`, in the register (join: "the day you've run it, it's yours to offer the
  agents you attract"; open: "what I teach, you can teach").
- **The register:** at `Join-gated package allowed: no` the opening sentence says the program is taught to any
  agent who wants to learn it and that partnering is a separate conversation; at `yes` and `unknown` it says the
  program is what an agent receives when they partner with the member; the band name stays (downstream systems
  key on it).

### THE FIVE PROBLEMS THIS SOLVES — 120+ words
Band: `THE FIVE PROBLEMS THIS SOLVES`. Source: `## The problems this offer solves` (the five pains table) and the
deliverables. One sentence in (Mike's frame: agents leave problems, not companies — `02-prospect-targeting/18`),
then one `•` line per pain in Mike's order — financial uncertainty · lack of support, mentorship, training ·
technology gaps · limited growth · work-life balance and recognition — each "[the pain in the agent's words] →
[what you get] → [the outcome]"; a pain the member does not solve reads honestly: "my brokerage covers this — I
walk you through it on a call" or "not my lane". Outcomes, never features (`04-value-proposition/32`); no
compensation word; no brokerage named by brand as the solver (`04-value-proposition/28`).

### YOUR FIRST 30 DAYS — 200+ words
Source: `## The Partner Offer` → `Onboarding: Day 1` lines and the `First 30 days` table.
- One sentence in, then `──── Day 1 ────` and **five short numbered lines** (4+): the welcome call (length,
  where, what to bring) · the setup (what is handed over) · the first lesson (sent or watched together) · the
  group (the chat, the weekly-call invite) · the calendar (the first date put on it before the call ends).
- The week-by-week table `| Week | You | Me | Done when |` — all four weeks; week 1 is always the 1:1
  onboarding and lesson 1's setup together; week 4 ends with the partner's first result or an honest reset.
- A `Done when:` line for the month — the three things that are true at day 30.

### HOW WE WORK TOGETHER — 120 to 180 words
Source: `## Support & community` in `offer.md` (from `operations.md`).
`Label:` lines, one each: the weekly call (name, day, time, length, what happens on it) · the group chat (who
is in it today, what it is for) · the 1:1 rhythm (Day 1, the first week, day 30, after that) · the response
time in plain words ("I reply the same day on weekdays; Sunday evening for anything about a sign-in sheet";
never "24/7") · who else is in the room (the upline, a mentor — first names only, labeled as the upline's) ·
the organization's rhythm (the recognition moment, the monthly check, what repeats).

### PROOF — 60+ words
Source: `identity/proof.md` ONLY.
`•` lines: the member's own result with the method (as written there) · agents already helped (first names or
initials, the result; a result whose consent is not on file is written as the member says it on calls, never
as a printed quote) · the organization today · upline proof labeled as the upline's. Zero proof → in words:
"None yet — I'm building it with my first partners. Mike's own path: help agents for free and earn the first
case study." Never manufactured credibility, never a bracket.
- `Proof plan:` closes the section — the `Proof plan:` line from `## The Partner Offer`, one or two sentences:
  the founding-partner exchange (who, what they get, the written OK and the 60-second video at day 90). Present on
  every offer; at zero proof it is the section's second half.

### WHY NOW — 80 to 120 words
Source: the seven parts → `Why now`. The honest reason to move this quarter (a first-partner window, a
cohort date, a season, the size of the table today) and what waiting costs the agent in their own pain's
terms. No countdown clocks, no fake scarcity.

### YOUR NEXT STEP — 80+ words — then the compliance line
- The ask in the member's voice: the booking line and what to bring · what the call is and is not (one
  sentence each) · the comment keyword line · one sentence on what happens after the call (Day 1, in one
  line).
- **The compliance line closes the agent-facing document — the last line of this section, verbatim, nothing
  after it before the appendix band:** *Compensation isn't on this page on purpose — it's a private,
  brokerage-approved conversation. Before this goes anywhere public, check your brokerage's advertising and
  rev-share marketing rules.*

### APPENDIX — FOR MY CONTENT — 200+ words — the member's own page, never handed to an agent
Band: `APPENDIX — FOR MY CONTENT`. Source: `## UVP`, `## How to talk about it`, the card's silent decisions.
**This is the marketing language** — outcome-based, the member's voice, no hype words, every line in the
register the brokerage rule sets (at `no`: what the member teaches, their story, their mentorship — never
"join me and get X"; at `yes` and `unknown`: the join register).
- `──── The four ways to say it ────` — six `Label:` lines: `The promise:` (the UVP, locked shape) ·
  `Outcome-led:` · `Story-led:` · `Mechanism-led:` · `Why me:` (the `Differentiator:` line) · `Why join me (one
  breath):` (the one-breath statement from `journey.md → ## Why join me`, verbatim — written in the same session by
  `attraction-why-join-me`'s silent run). Never concatenated into a paragraph.
- `──── The 30-second explanation ────` — one paragraph, 60 to 90 words, what the member says when an agent
  asks "so what do you actually do?": who I help · what they get · how · what happens next.
- `──── The short lines ────` — `DM:` · `Caption:` · `Bio:` · `Video intro:` — under 20 words each, first
  person, in the member's voice; the video intro is the first sentence on camera.
- `Comment keyword:` the ONE word in caps — "Comment [KEYWORD] and I'll send it."
- `The free guide is cut from:` which framework step (or steps) the free lead magnet is cut from and why that
  step runs without the member — the seed `lm-magnet-ideas` reads. When a magnet is already live
  (`memory/magnets.md → ## Current magnet`), name it and its keyword here instead of re-seeding.
- `──── What I assumed (change any of these) ────` — `•` lines, one per default the offer card decided
  silently: the program type · the program name, with the two alternates that were offered and why this one ·
  the framework name · the weekly call's day and time · what is recorded vs live · the support rhythm and
  response time · the 90-day outcome · the first lesson · the "what it costs you" line · the comment keyword ·
  the brokerage answer (allowed · not allowed · being checked). One line each, the value and where it came
  from in plain words ("from what you do today", "from the outcome in your one-liner"). This is the only list
  of assumptions anywhere — never in chat.

### HOW TO CREATE IT — 150+ words — the member's build checklist
Band: `HOW TO CREATE IT`. Source: `## How to create it` (from `## Structure`, the Teach-first table, the
deliverables, `operations.md`). One sentence in, then four `Label:` lead-ins each followed by `•` lines:
`Record:` (lesson 1 tonight — what is on screen, the run time; lessons 2 and up live first, recorded with the
first partners) · `Write:` (the templates handed over, the welcome-call agenda, the Day 1 hand-over list, the
community's welcome post) · `The first 30 days:` (the member's side of the weeks table, one line per week) ·
`The weekly touchpoint:` (the call — day, time, length, format, what happens on it, who runs it when the
member cannot). Every line is something the member can do this week; a thing that exists today reads "done —
reuse it", never as a to-do. No numbered lines, no values, no compensation.

### START WITH YOUR UPLINE — 120+ words
Band: `START WITH YOUR UPLINE`. Source: `## Start with your upline` (the upline layer — Brain question 16 —
`proof.md`'s upline proof, `operations.md`'s 3-way partner, `avatars.md`, `strategy.md`). Mike's rule in one
sentence (use your upline's package and your own skill to get started; build your own over time). Then
`Label:` lines: `My upline's package:` (generic names, the access line) · `My own skill added to it:` (the one
lesson) · `The offer I can run this week:` (one line). Then **the three signs you are ready to build your
own**, as three `•` lines, each ending "— true today" or "— not yet" with the evidence in plain words: you have
attracted agents who ask for your way of doing something · your process has a result you can stand behind ·
the upline's package does not serve who your story speaks to. Close with the verdict line: all three true →
"this program is yours; my upline's package is a layer inside it"; fewer → which sign to watch for. The upline
by first name only, labeled as the upline's; never a word against the upline's package.

### IF YOUR BROKERAGE DOES NOT ALLOW A JOIN-GATED PACKAGE — 100+ words
Band: `IF YOUR BROKERAGE DOES NOT ALLOW A JOIN-GATED PACKAGE`. Source: the header's `Join-gated package
allowed:` line and `## If your brokerage does not allow a join-gated package`. Always present, written for the
state in force. `Rule in force:` allowed · not allowed · being checked. One short paragraph on what it means:
at `yes`, the program is what an agent receives when they partner with the member, and compensation still
stays off every page; at `unknown`, the same join register (Mike's model — the norm at eXp and REAL) with one open
check, and the member flips it with 'my brokerage does not allow a join package' if the desk says no; at `no`,
the offer is what the member teaches, their story and their mentorship, offered to any agent who wants to learn
it — nothing gated on joining, never "join me and get X". `The lines that change:` `•` lines naming each — the
for-line, the "What it costs you" row, the four ways to say it, the short lines, the funnel's Offer and Why Join
Me sections, the bios — one line each on how it reads in the register in force. At `unknown`, `The check:` one
line — confirm with the compliance desk whether a package may be offered as a reason to join. Never a brokerage
named as the example; never a word against the brokerage's rule.

### WHERE TO HOST IT — 100+ words — a guide, not a comparison
Band: `WHERE TO HOST IT`. Source: `## Where to host it`. `Label:` lines: `Recommended:` Skool — the easiest:
one community, the classroom for the recorded lessons and the templates, the calendar for the weekly call,
one welcome post · `The alternative:` Circle — the same four things, a little more to configure · `Your
community's name:` the organization or community name in use (else the program name) · `Set up in 20
minutes:` four `•` lines (create the community · add lesson 1 and the templates to the classroom · put the
weekly call on the calendar · write the welcome post) · `Keep it simple:` one community, one welcome post, one
weekly call · `The group chat:` stays the chat. **The Skool link line:** this reference carries the
placeholder `[Skool link — set by the cohort]`; when the cohort sets the affiliate link it replaces the
placeholder here and the line renders as `Skool:` + the link. Until then the rendered line reads, in words,
"Skool — the cohort's link is in your Week 2 materials" — **never a bracket in the document** (gate check 7).
No platform comparison, no pricing, no other platform named.

### YOUR CONTENT BRANCHES — 150+ words — the UVP as the foundation of the content
Band: `YOUR CONTENT BRANCHES`. Source: `## Content branches`, the same words. One sentence in (all content is
a branch of the UVP — tactical, valuable information from one segment of it at a time), then 5 to 7 `Label:`
lines, one per segment (the framework's steps, the pains in the overlap, the member's perspective on what
agents pay for versus what works, the story's turning point, the teaching method itself), each followed by
its three example topics as one line separated by middle dots — specific, tactical, a result or a number in
each, never compensation. One closing sentence: the Short-Form Game Plan (Week 3) and the YouTube Game Plan
(Week 4) build their pillars and titles from these branches first.

---

## Voice rules (the gate reads for these)
- First person, confident, no filler. No sentence explains why a section exists ("so neither of us has to
  guess", "I list them in this order on purpose") — cut it.
- **Say what it is; never what it is not** beyond the two "This is not…" lines in "Who this is for". No
  taxonomy ("it isn't an accelerator because there are no cohort dates; it isn't a course because…").
- **The method appears in full once** — the step table and its paragraph. Elsewhere, the name or the one-line
  chain only.
- Paragraphs of at most three sentences. Bold lead-ins (`Label:` lines) where a list reads better than prose.
- No "if you only read one section, read this one", no "one name, so you always know what I'm talking about",
  no "all four, said as one". The four lines are a labelled list in the appendix.
- Headings sell — `WHAT YOU GET WHEN YOU PARTNER WITH ME`, not `6 · WHAT YOU GET`.

## Demo mode (`config.md` → `Demo brain: yes`, or the member explicitly asked for a fictional demo)
The Partner Offer's demo marking is lighter than the Brain Book's (the 2026-10-18 ruling — the Book keeps
its own rules):
- **The cover carries ONE line**, exactly `Demo: every figure is illustrative`, and nothing else on the cover
  says demo.
- **Every money and production figure carries a short `(demo)`** after it — the lead bill, closings, buyers
  under contract, sign-in counts, organization counts, partner counts, the booking link. Dates, clock times,
  durations, step and week numbers, and cells under a header that already carries `(demo)` are exempt. The
  tag `(illustrative — demo)` never appears in a Partner Offer.
- No real competitor, sponsor, lead-vendor, CRM or coach names. The eyebrow is `Partner Offer · Demo`; the
  filename carries `— DEMO —`. Never saved into a real workspace; never handed to the Design Studio as "the"
  Partner Offer.
- **Every section COMPLETE at its floor** — a demo is never thinner than a real build; it is what the training
  video shows. A demo never renders a bracketed token.
- Real builds get the mirror tripwire: `(demo)`, `(illustrative — demo)`, the demo cover line or a DEMO
  filename anywhere = automatic FAIL; rebuild from the Brain files.

## What never appears
Splits, caps, fees, tiers, stock, rev share, income figures, commission (the compliance last line is the one
sanctioned mention of compensation); another brokerage's name as a comparison; a former brokerage by name; a
claim not in `proof.md`; a lesson, module, call or product that does not exist and is not marked "built with
my first partners"; bracketed template text (the Skool placeholder included); a numbered or middle-dotted band;
a section that is a heading over one line; `>> ` lines; Markdown; the method explained a second time; a list
of assumptions anywhere but the appendix; "join me and get" in any form at `Join-gated package allowed: no` or
`unknown`; a platform comparison or a price in Where to host it; a program name that is a club, a portal, a
place or a label.
