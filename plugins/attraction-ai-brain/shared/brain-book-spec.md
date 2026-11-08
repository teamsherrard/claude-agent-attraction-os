# Agent Attraction Brain Book — the canonical contract (nine sections, at most 15 pages)

*Supersedes the pointer rules in `shared/brain-doc.md`. When any skill (Setup's close, "show me my Brain",
"regenerate my Brain Book", the post-offer refresh in Week 2, brain-health) builds or regenerates the member's
Brain Book, THIS file is the contract. Rewritten 2026-11-02 on the owner's verdict: the old eighteen-chapter
Book was "way too long, overwhelming, not structured — it gives overwhelm instead of clarity." The Book is now
SHORT, STRUCTURED and CLEAR: nine sections, at most fifteen pages, plain words, short paragraphs, tables where
they help. The Brain files behind it keep their full depth for the plugins; the Book is the member's clear,
simple read.*

The **📕 Agent Attraction Brain Book** is the one document the member holds at the end of Week 1: everything
the system knows about them, in the order they will use it, readable in ten minutes. It is also **"the AI Brain
file"** the Design Studio and the Lead Magnet skills ask the member to upload (`shared/brain-doc.md`) — it tells
those tools WHO the member is; their offer, brand, operations and compliance live in their own documents and
files (below), never in the Book.

Two identities it must never lose:
1. **It is a RENDER, never a source.** The markdown files in `identity/` and `memory/` stay the source of truth.
   Everything in the Book exists in a Brain file first; the Book is always rebuildable from the Brain, never
   drifts, and never holds a fact the Brain doesn't.
2. **It is clarity, not volume.** A member who reads it should feel *"this is me, and I know what's next"* — not
   "where do I start". Long is wrong. A Book that runs past fifteen pages has failed its job.

---

## Non-negotiable invariants

- **Build ONLY via `shared/render_doc.py`** per `shared/doc-formatting.md`. Use `--eyebrow "Agent Attraction
  Brain"`, `--title`, `--subtitle "[First name] · [Market]"`, and `--accent HEX` with the member's primary brand
  colour when `identity/brand-visual.md` records one (the brand chat writes it — omit the flag before that; the
  renderer's near-black default applies). Never hand-write document XML. **If the renderer prints
  `RENDERER-UNAVAILABLE`, do exactly what it says: install nothing, never run pip, never retry — save the
  structured text as a `.md` file, upload that to `01 · AI Brain`, and say in one line that the styled version
  needs the renderer.** That is the whole fallback chain.
- **Upload the rendered `.docx`, never the raw structured text as a Google Doc.** Literal `════`/`────` lines
  visible as text in a converted doc = the renderer's *input* was uploaded = FAILED delivery; re-render and
  re-upload (the `.md`-file fallback above is the one sanctioned exception and is uploaded as a plain file).
- **Name:** **"📕 [Name]'s Agent Attraction Brain Book — [YYYY-MM-DD]"** — emoji + the words "Agent Attraction
  Brain Book" + ISO date. Dated regenerations never collide; **newest = current**. Same name pattern on EVERY
  regeneration — refresh, don't fork. *(For this one document the name overrides `doc-formatting.md`'s generic
  `[Deliverable] · [Subject] · [Date]` scheme.)*
- **Save to the workspace's `01 · AI Brain`**, then push via `attraction-brain-sync`.
- **Hand the member the DIRECT LINK to the Book itself** — never just the folder: *"Your Agent Attraction Brain
  Book is in your home base → 01 · AI Brain — here's the direct link. Everything the system knows about you,
  on about a dozen pages."*
- **Nine sections, in the order below, and nothing else.** No money chapter, no compliance, no operations, no
  scorecard, no open-items wall, no content pillars, no landscape research, no brand kit, no Design Package
  brief. Those live where their owners put them (the Partner Offer doc in `05 · Offer`, the Design Package
  brief in `02 · Brand`, `identity/compliance.md`, `identity/operations.md`, the Scorecard doc) — the Book
  points at them in one line each in Section 9 and nowhere else.
- **At most 15 pages; every section has a TARGET and a MAXIMUM.** The section table below gives each section a
  target (below it the section is thin — fix it from the Brain file, never pad, and never fail the build for it)
  and a maximum (above it the build FAILS). The whole Book: target 1,500 words and up, maximum about 3,500
  words; the demo Book's target is 2,000–2,600 words. A rich Brain file is SUMMARISED into its section — the
  reverse of the old spec — and the depth stays in the Brain for the plugins. Over a maximum: cut prose, never
  a table, never a section.
- **Tables where they help:** the at-a-glance table (Section 1 — 8 to 12 rows, every value at most 15 words),
  the strategies table (Section 4), the agents-helped table (Section 5), the numbers table (Section 7). Prose
  everywhere else, in short paragraphs — **at most four sentences each** (the gate counts them).
- **Plain words — the jargon list.** These never appear in the Book's text: *downline* · *upline* unless it is
  explained where it first appears ("your upline — your sponsor and the leaders above them") · *the model*
  unless explained the same way ("how the brokerage works and pays") · *three-way call* · *unique value
  proposition* / *UVP* · *funnel* · *doctrine* · *Partner Offer* outside Section 9 · spec-speak ("labeled as
  such", "never here", "the files behind it"). "Revenue share organization" is explained once, in plain words,
  in Section 1. **Commands** — any *say "…"* / *type "…"* — appear only in Section 9, at most three distinct
  phrases; every other section describes, never instructs.
- **Byline once** (the cover) — never repeat the credential line inside a section.
- **No raw markup:** any `<w:` in the extracted text = corrupt build = rebuild.
- **Never fabricate** — no invented stories, quotes, testimonials, production numbers, agent counts or figures of
  any kind. The **GROUNDING LAWS** below bind every build.
- **Compensation never appears.** No rev-share, split, cap, stock, income or earnings figure anywhere in the
  Book — not as a scenario, not as a target, not as an illustration. The only numbers in the Book are the
  member's own agent counts, hours and years (Sections 1, 5 and 7) and the dates in their story.
- **The cardinal rules bind the Book** (`03-model-positioning/13`): no sentence characterizes another brokerage,
  sponsor or person negatively — not in the brokerage story, not in a story, not anywhere. Former brokerages are
  "a franchise", "an independent", "a team".
- **No location as a limit, no agent type as a choice.** The member's local market appears once, in Section 1,
  as a fact. Section 6 is DERIVED from their answers and framed "your skills attract any agent; these are the
  agents who will relate most" — never "the agents you chose" and never "the agents in [place]". (The owner's
  ruling, 2026-11-02: the whole point of a cloud brokerage is attracting anywhere, and nobody picks their agent
  type — the system identifies who will relate.)
- **Written FOR the member** — second person, warm, plain; the member is "you", the people they attract are
  "agents"; never "persona", "avatar", "tier", "beat", "schema" or any file name.
- **Never narrate a failed render or the retry to the member** — they only ever see the finished Book.

---

## GROUNDING LAWS — zero fabrication, true to THIS member

These laws outrank style, length and word targets: a Book that misses a target is thin; a Book that breaks a
grounding law is wrong.

1. **Voice & identity fidelity.** Every claim about the member — years, brokerage, the story's turning points,
   the almost-quit moment, achievements, agents helped, organization size, hours — traces to their interview
   answers or Brain files. Reuse their own phrasing wherever it exists; the three dictated answers are quoted
   verbatim in Section 8. NEVER invent a quote, an anecdote, a testimonial or a number about them. Where the Book
   paraphrases, it still sounds like `voice.md` / `voice-print.md`.
2. **Numbers.** Every figure is the member's own, as they stated it (agents today, the 12-month and long-term
   numbers, hours, years, achievements). No research, no scenarios, no defaults dressed as facts. Locale and
   units come from `config.md`.
3. **Brokerage and people.** The member's own brokerage and sponsor may be named (as the member names them and as
   compliance allows); nobody else is named, and nobody is characterized negatively. A missing name is better
   than a wrong one.
4. **Uncertainty protocol.** Cannot verify → omit it, or mark it `[confirm: …]` inline for the member. A wrong
   specific is worse than a gap. Markers go mid-sentence, never at line start; more than 3 in the whole draft
   means the Brain isn't ready — capture the answers with the member first, then render.
5. **Pre-render grounding audit** (pipeline step 4). Before rendering, enumerate every proper noun and every
   number in the draft; trace each to a Brain file; CUT anything untraceable. A former brokerage named in a story
   is cut and replaced with its type. Keep the tally — "N facts traced, M cut" — in the build log, never in the
   member's message.
6. **Read-back check** (pipeline step 3). After assembly, re-read `voice.md` + `voice-print.md` and confirm the
   Book's characterization of the member matches, and that no sentence carries a compensation figure or an
   earnings claim; fix mismatches before rendering — ONE fix pass per build. A mismatch surviving it is noted
   in the build log, never re-fixed in a loop and never narrated to the member.
7. **Derived, never chosen.** Section 6 names the agents who will relate from the member's own answers (their
   former self in the hardest stretch, the agents whose mistakes they named, the agents who want the skill they
   teach). It never reads as a selection the member made, never names a place, never uses a protected
   characteristic.

---

## DEMO BRAINS — explicitly fictional, for training and demos only

When the person in the session **explicitly asks for a fictional brain** — the words "demo", "mock", "fake",
"fictional", "test member", "sample agent" in THEIR OWN request (Mike demoing for the cohort, a test drive) —
the build runs in **demo mode**. Two conditions, both required:

- **The subject is fictional** — a named persona who is NOT the person in the session. The demo world for this
  OS is **Taylor Brooks · Real Broker · Austin, TX · 6th year · former teacher · open-house lead system + a
  Sunday follow-up routine · 2 agents in the organization · goal 25 agents in 12 months**; the demo success story
  is Priya Nair, 3 buyers under contract in her first 60 days. Demo keywords aimed at the member's OWN identity
  ("mock something up for MY market", "let's just do a test run on my brain") are a REAL build — the grounding
  laws bind.
- **When there is ANY doubt who the subject is, ask the one question** — "Fictional demo member, or your real
  Brain?" — before proceeding.

In demo mode:
- **One sanctioned string — "(illustrative — demo)" — and in the Book it lives in ONE place per section:** a
  small line directly under each SECTION band, verbatim *"(illustrative — demo) Every count and figure in this
  section is fictional."* — nine lines in all, and NO inline tag anywhere else in the Book: not in story prose,
  not in table headers, not in cells, never on a date, and never a variant ("your own tracking, illustrative —
  demo", "dictated at setup — demo, fictional", "(a profile, illustrative — demo)" are all FAILS). The Brain
  files keep their per-figure tags — every count, production or achievement figure in a brain file carries the
  exact string; dates, clock times, durations and step numbers never do — and the Book carries the band line
  instead. No figure anywhere carries a fabricated source attribution.
- **No real competitor, sponsor, team, lead-vendor, CRM or coach names.** Fictional names only. Platforms used as
  tools (Instagram, YouTube, Zoom, Google Sheets, Claude Design) may be named, and so may the demo member's own
  brokerage (Real Broker); nothing is claimed about any real person.
- **Watermark it, unmissably:** filename **"📕 [Name]'s Agent Attraction Brain Book — DEMO — [YYYY-MM-DD]"**;
  eyebrow `Agent Attraction Brain · Demo`; one meta line on the cover, **verbatim — never suffixed, never
  reworded** (the gate checks the exact string): *"Demo document — illustrative data, not researched."*
- **Total isolation from real Brains.** A demo scaffolds locally at `~/attraction-brain-demo/` and creates/pushes
  to its OWN workspace folder named **"[Workspace name] — DEMO"** (own `_attraction-workspace.md` marker, also
  demo-stamped) — NEVER into an existing real workspace. The demo Book is excluded from "newest = current":
  Claude Design's "upload your AI Brain file" must never be handed a demo Book. Isolation cuts BOTH ways: a
  demo build never modifies, renames, retires or cleans up anything outside its own workspace. Demo pushes are
  LIGHT: create the files, one folder-listing verify at the end.
- **Every demo brain file opens with the banner line** `DEMO BRAIN — fictional member, illustrative data —
  never publish.` — so ANY skill that reads the file sees what it's holding before it quotes a number.
- **Demo-to-real never converts.** "Love it — now build mine" starts a REAL build from a fresh template with
  every gate re-armed.
- **No placeholder sections.** A demo Book renders all nine sections FILLED — a demo shows the finished product.
  The per-section targets and maxima bind in demo mode exactly as in a real build; a demo never renders a
  `[bracketed]` token.
- **The demo marker travels with the BRAIN.** A demo build writes `Demo brain: yes` into `config.md` and keeps
  the "(illustrative — demo)" tags inside the brain files themselves. Any skill that touches a brain whose
  `config.md` says `Demo brain: yes` STAYS in demo mode; a real member resuming on a demo brain is told plainly
  and offered a fresh real setup — never a silent conversion.
- **Demo mode is NEVER inferred.** Thin answers, a rushed member, "just fill it in" or "use defaults" do NOT
  trigger it — only the explicit fictional framing above does (and a `Demo brain: yes` already in `config.md`).

---

## THE STATE RULE — the Book shows the week the member is in

`config.md → Cohort week` decides what Sections 1, 4 and 9 say, regardless of what the later-week files hold (a
demo Brain, a bridged Brain or a member who ran ahead can hold a built offer while the cohort is in Week 1):

- **Cohort week 1 — or no week recorded and `offer.md` at `Status: seeds` — the WEEK-1 STATE.** Section 1 carries
  no offer row. Section 4 opens with the one forward-looking line (*"Next week turns this page into your offer
  …"*) and carries no one-liner and no program name. Section 9 is exactly three one-line bullets — the brand chat
  this week · the lead magnet next week · one any-time line — and its callout is the one phrase to type:
  **"my attraction brand direction"**. The `--accent` flag is omitted (the brand chat has not run in this state;
  the Book picks the colour up on its next regeneration after it has).
- **Cohort week 2 or later with the offer built — the POST-OFFER STATE.** Section 4's opener flips to the past
  tense (*"Next week turned this page into your offer: …"*, then the one-liner and the program's name, the same
  words as `offer.md`) — never both the forward line and "your offer is built". Section 9's first bullet reads
  "your brand direction is set" when `brand-visual.md` shows the brand chat has run, its second bullet points at
  the offer and the magnet, and its callout is the next phrase to type for THAT week.
- Everything else renders the same in both states. **The demo Book ships in the Week-1 state** — that is what a
  member holds at the end of Setup.

---

## The build pipeline (run in this order, every build and every regenerate)

1. **Pull + read.** Sync the Brain (`attraction-brain-sync` PULL), then read `brain.md`, `config.md`, and only
   these identity files: `profile.md` · `journey.md` · `strategy.md` · `story-bank.md` · `proof.md` · `offer.md`
   (the seeds and, once built, the `## UVP` first line and `## The program` name) · `positioning.md` (the seed
   line) · `avatars.md` · `goals.md` · `voice.md` · `voice-samples.md` · `voice-print.md` · `brand-visual.md`
   (only the `Final kit` / `Direction` colour for `--accent`, and whether the brand chat has run — for Section
   9). Nothing else is read: no research, no ledgers, no compliance text, no operations.
2. **Assemble the structured text** per the **Book structure** (below) — and ONLY that grammar: the cover title
   block; the `[[TOC]] … [[/TOC]]` contents block; nine `SECTION N — TITLE` CAPS bands wrapped in divider
   rules (in a demo build, the one demo line directly under each band); sub-bands (`──── Label ────`) inside a
   section only where the contract names them; `•` bullets; `Label:` lead-ins (the signature lines); `>> `
   lines for each section's one key line; pipe-row tables where the contract mandates them; generous blank-line
   spacing. No Markdown `#`/`**`/backticks in the body. **Write it to the input file — `~/attraction-brain/exports/brain-book-YYYY-MM-DD.txt` (a demo build:
   `brain-book-DEMO-YYYY-MM-DD.txt`; the Brain Board re-reads this file for the member's pages and the sync skill
   carries `exports/*.txt` to the cloud, so it is never a `/tmp` path) — section by section — one append per
   SECTION band, never one emission** (a cut-off emission renders as a clean two-page Book with no
   error). **Structural pre-check — run on the input file before step 5, every build:** (1) the `[[TOC]] …
   [[/TOC]]` block holds exactly nine `SECTION n — TITLE :: summary` rows, numbered 1–9 in order, each summary
   at most twelve words, and no PART rows; (2) the body holds exactly nine `SECTION` bands numbered 1–9 with no
   gap; (3) every contents row's text left of `::` equals a band character-for-character; (4) the last band is
   `SECTION 9 — WHAT'S NEXT`, with its body under it. The count that proves it: `grep -c '^SECTION [0-9] — '
   <input>` = **18** (9 rows + 9 bands) and `grep -c '^PART \|^CHAPTER ' <input>` = **0**. Any other number =
   the input is incomplete: append the missing sections, re-run the pre-check, and only then render — never
   render a short file. If the member is waiting while it trips, they see one progress line — *"your Book is
   still assembling, one more minute"* — a status, not a failure narration.
3. **Read-back check** (Grounding Law 6). One fix pass; survivors noted in the build log.
4. **Pre-render grounding audit** (Grounding Law 5). Keep the tally in the build log.
5. **Render** with `render_doc.py` to `.docx` — only an input that passed the step-2 pre-check. Pass `--accent
   HEX` with the member's primary brand colour when `identity/brand-visual.md` has one (the `Final kit`
   `Colors:` line first, else the Direction block's `Primary / brand: #hex`); no hex recorded (the brand chat
   has not run, a `[#hex]` placeholder, "none", or only a description) → omit the flag. Never pass the
   brokerage's colours. **Renderer stderr must show ZERO warnings.** An unresolved-TOC warning means a contents
   row and a band don't match character-for-character: fix the structured text, re-render (at most twice). A
   `sub-band label is N characters (cap 80)` warning means a `──── Label ────` line is too long: shorten it,
   re-render. `RENDERER-UNAVAILABLE` → the `.md` fallback, once, no loop.
6. **Verify** against the hard gate (below) — first the executable part: run **`shared/measure_book.py
   "<the rendered .docx>"`** (python-docx, the same dependency as the renderer; no install, no retry — if it
   prints `RENDERER-UNAVAILABLE`, the gate is run by hand). It extracts the text in document order and prints
   the per-section words against the targets and maxima, the **page estimate** (words and forced breaks against
   the renderer's layout — FAIL above 15 pages, WARN above 13), and every check it can run: bands and their
   order, the contents rows and their twelve-word summaries, the byline once, no raw markup, no bracketed token,
   no money figure, four-sentence paragraphs, the jargon list, commands only in Section 9, the demo-tag rule or
   the real-build tripwire, the table shapes. It exits non-zero on any FAIL. Then check by hand what it cannot:
   the grounding audit, the cardinal rules, voice fidelity, the swap test, the state rule. FAIL → rebuild the
   failing sections from the Brain files and re-verify. Never upload a failed render.
7. **Upload to `01 · AI Brain`, push, hand over the direct link** — the hand-off message is the link and the
   standing line, nothing else. The grounding-audit tally ("N facts traced, M cut"), the measure output, the
   read-back survivors and any `[confirm:]` list stay in the build log, never in the member's message. Never a
   list of what is "open".

---

## Book structure — cover, contents, nine sections (the render grammar)

**Page 1 — the cover.** Eyebrow `Agent Attraction Brain` (`--eyebrow`). Title `[First name]'s Agent Attraction
Brain Book` (`--title`; no 📕 on the cover — the emoji lives in the filename). Byline `--subtitle "[First name]
· [Market]"`, with the one credential line (brokerage · years licensed · what they are building, in plain
words — "building a group of agents who …", never "downline") as the meta line — its ONE appearance. Date
`[Month D, YYYY]` on its own meta line — the same date as the filename's ISO stamp. Demo: the verbatim demo
cover line under the date. Every page after the cover carries the title top-right and `[First name] · [Market]
· AGENT ATTRACTION BRAIN` + `Page X of Y` in the footer — automatic.

**Page 2 — CONTENTS.** Immediately after the title/meta lines, one `[[TOC]] … [[/TOC]]` block — the renderer
builds a linked contents page and page-breaks around it. Nine rows, no PART rows:

```
[[TOC]]
SECTION 1 — WHO YOU ARE :: [one line, at most twelve words, written for THIS member]
SECTION 2 — YOUR STORY :: …
SECTION 3 — YOUR BROKERAGE STORY :: …
SECTION 4 — YOUR UNIQUE APPROACH :: …
SECTION 5 — YOUR PROOF :: …
SECTION 6 — WHO YOUR STORY SPEAKS TO :: …
SECTION 7 — YOUR NUMBERS :: …
SECTION 8 — YOUR VOICE :: …
SECTION 9 — WHAT'S NEXT :: …
[[/TOC]]
```

Each `::` summary is one short line — **at most twelve words** — **written for that member**: their brokerage,
their method, their own phrase. *"The Sunday routine that replaced a lead bill — the thing you teach"* passes;
*"An overview of the member's approach"* is a FAILED contents page — the swap test applies to every row. Row
text left of `::` must match its band **character-for-character**. Nine rows fit on one contents page.

**The bands.** `SECTION N — TITLE` in CAPS, wrapped in divider rules, numbered 1–9 with no gaps, no PART and
no CHAPTER bands (the renderer page-breaks before each band — nine section pages plus the cover and the
contents is eleven pages before any section spills; the maxima keep the whole Book at fifteen or fewer). The
renderer prints the small "SECTION N" kicker above each title — the member reads sections, and that is the
word they see. **Demo builds:** the first line under every band is the one demo line (DEMO BRAINS), rendered
small; nothing else in the Book carries the tag.

**`>> ` callouts.** Each section surfaces ONE key line this way — the member's own sharpest sentence, or the
one thing to remember from the section. Never more than one per section; Section 1 has none (the table is the
page); the signature lines in Section 8 keep their `Label:` treatment and the three dictated answers sit under
their sub-bands, never in a callout.

**Tables** stay pipe rows, exactly where the section contract mandates them.

---

## The section contract — nine sections, in this order

Targets are what a good section reaches; maxima are hard limits. Every section renders filled — there are no
placeholder sections. A thin Brain file renders a short, honest section, never a padded one. In a demo build the
one demo line under the band counts toward the section's words.

| # | Section (CAPS band) | Source file(s) | Target – MAXIMUM (words) | Shape |
|---|---|---|---|---|
| 1 | WHO YOU ARE | `brain.md` quick reference · `profile.md` | the table (8–12 rows) + two short lines; 80 – 200 | table; one page |
| 2 | YOUR STORY | `journey.md` (the story, the turning points, the leader moment, the WHY) · `story-bank.md` (the almost-quit moment, the mistakes) | 250 – 400 | prose, four sub-bands |
| 3 | YOUR BROKERAGE STORY | `profile.md` (joined, the story behind choosing it, the sponsor) · `journey.md` (why revenue share) | 150 – 300 | prose |
| 4 | YOUR UNIQUE APPROACH | `strategy.md` (what they can teach, the method) · `offer.md` seeds (what worked, the upline layer, the mistakes agents make) · `offer.md → ## UVP` + `## The program` once built (post-offer state only) | 200 – 400 | the strategies table + prose |
| 5 | YOUR PROOF | `proof.md` (achievements, agents helped, why their agents joined them) · `story-bank.md` (the almost-quit moment, the lessons) | 150 – 300 | the agents-helped table + prose |
| 6 | WHO YOUR STORY SPEAKS TO | `avatars.md` (derived) | 150 – 300 | prose; one page |
| 7 | YOUR NUMBERS | `goals.md` (today, 12 months, long term, hours) | 60 – 150 | table + two lines |
| 8 | YOUR VOICE | `voice.md` (the one line, the signature lines) · `voice-samples.md` (the three dictated answers) | 150 – 320 | `Label:` lines + the three answers |
| 9 | WHAT'S NEXT | `config.md → Cohort week` · `brand-visual.md` (has the brand chat run?) · `offer.md` Status | 40 – 150 | three bullets |

**Totals.** Target **1,500 words** and up; maximum **about 3,500 words / 15 pages**; the demo Book targets
**2,000–2,600 words**. A real first-run Book lands around 2,000–2,800 words and 12–14 pages. Below a section's
target the section is thin — fix it from the Brain file, never pad, never fail. Above a maximum — cut prose,
starting with Sections 2 and 4, never a table.

### Section 1 — WHO YOU ARE
One page. The at-a-glance **table** (| Label | Value |), **8 to 12 rows, every value at most 15 words**: name ·
brokerage (and sponsor, first name) · local market (a fact — never followed by "attracts in") · category of
agent (solo · team leader · broker owner) · licensed since (years) · before real estate · why you got into real
estate (the big WHY, one line) · why a revenue share organization (one line) · organization today · where
you're going (the 12-month number · the long-term number · hours a week, in ONE row) · the one line you'd say
out loud (the seed from `positioning.md`, marked "(drafted — confirm)" until Week 2 confirms it). **Rows that
Sections 4, 6, 8 and 9 carry are never repeated here:** no "strategy you can teach", no "agents your story
speaks to", no "voice in one line", no offer row. Then two short lines of prose: first, what a revenue share
organization is, in plain words (*the agents you help bring to your brokerage, and the agents they bring; the
brokerage shares part of what it earns on their deals with you — the numbers are for a private conversation,
never for this Book*); second, how to use the Book (*it is the readable version of everything your Brain knows
about you; every tool reads the same facts, so you never explain yourself twice*). No command, no credential
line (byline rule), no callout.

### Section 2 — YOUR STORY
The journey, told once, from `journey.md` — never a list. Sub-bands, in order, each a short paragraph (at most
four sentences) in the member's own phrasing (the echo test: their answer, what it means for the agents who
will read it, nothing invented): **How it started** · **The hardest stretch** · **The turning point — when it
clicked** · **After — what the business looked like** (the strategy that did it, in one line). Then two short paragraphs
without sub-bands: the moment selling houses and chasing the next deal wasn't enough any more (the leader
moment), and the WHY — who they are doing this for, in their words (the why-line verbatim as the section's
`>> ` callout). Another person's words (an agent's text, a partner's message) are quoted only when `proof.md`
says they may be used publicly; otherwise the moment is told, not quoted. The "who relates to this" lines stay
in the Brain file; the Book keeps the story clean. Former brokerages never named. A newer member's story is
year one plus what they are building — short and true, never fabricated.

### Section 3 — YOUR BROKERAGE STORY
From `profile.md` and `journey.md`, in prose: when they joined · the story behind choosing this brokerage (why
over other cloud brokerages, whether they ignored it or had a bad taste about it first, what changed their
mind) · **what they now understand that most agents misunderstand** (this is the section's `>> ` callout — it
is the member's best content angle) · why they chose their sponsor specifically — said plainly, in the member's
words, as what the sponsor actually does (*"Jordan runs the Tuesday teaching call and joins your calls with
agents who want to see how the brokerage works"*), never "three-way" and never "the model" · why they believe
revenue share is the key to what they want, and why other agents should care. The brokerage is the vehicle, the
member is the reason; never a mechanic, a split or a figure — and no "the details stay for a private call"
sentence: the Book simply leaves the mechanics out. Nothing negative about any other brokerage or person.

### Section 4 — YOUR UNIQUE APPROACH
The seeds next week builds from — said plainly as seeds, never as "your offer". Open with ONE line, by the
state rule: Week-1 state *"Next week turns this page into your offer — the one line that says who you help and
how, and what an agent gets by partnering with you."*; post-offer state *"Next week turned this page into your
offer: [the one-liner, the same words as `offer.md`] — [the program's name]."* Then the **strategies table**
(| Strategy | What it actually involves (your method) | The result you can stand behind | You can teach it |)
from `strategy.md` / `offer.md` seeds — only what the member has actually used or is comfortable teaching.
Then prose: the unique part of the method (the scripts that convert, the routine, the sheet — the specific
thing); what the member's upline provides today — introduce the word once, plainly (*"your upline — your
sponsor and the leaders above them"*), then say what they provide in the member's words, and say whose it is
in plain words ("that is Jordan's, not yours — and an agent gets it on day one"); and the biggest mistakes
agents are making right now and why the member — or joining their brokerage — is the answer (the member's
words, nothing negative about any named party). The `>> ` callout is the one sentence that says what they can
teach that most agents can't. **Post-offer state only:** one closing line points at the full program in the
member's Offer folder (`05 · Offer`) — the Book never renders the program itself.

### Section 5 — YOUR PROOF
`proof.md` in plain words, real only: the biggest achievements as the member stated them (top producer, awards,
expensive homes, a doubled year — their own labels, never rounded up) · the **agents-helped table**
(| Agent | What you did | What happened | When |) — an agent's own words appear only when `proof.md` says they
may be used publicly, and the consent status itself is never printed · why the agents in their group joined
THEM specifically, in the member's recollection (trimmed of any sentence that would need "the model" explained)
· then the moment they almost quit and what kept them going, and the mistakes that taught them something — one
short paragraph each, in their words (`story-bank.md`). Lesson and module names from the member's program
("Module 1") are said plainly ("the first lesson"). The `>> ` callout is the member's own best line about what
kept them going. Zero proof is one honest line — *"no agents helped yet; the first partner's result goes here"*
— never manufactured credibility.

### Section 6 — WHO YOUR STORY SPEAKS TO
One page, DERIVED from `avatars.md` (which the Brain derives from the answers — never asked). Open with the
framing line, verbatim: *"Your skills attract any agent. These are the agents who will relate to you most,
because you were them."* Then prose: the member's own former self (the agent living the hardest stretch they
described, two or three years behind them) · the agents whose mistakes they named in Section 4 · the agents
who want the skill they can teach. For the primary group: who they are in plain words (career stage, situation
— never a place, never a protected characteristic), their biggest problem **in the member's words**, what
they have probably already tried, and what they would need to hear from the member to believe it. A second
group only when the Brain derived one. Close with one line, no command: *this changes as your content starts
pulling a different kind of agent, and it can be refined any time.* The `>> ` callout is the "Say it like
this" mirror line from `avatars.md`. Never "the type you chose"; never a brokerage name; never a profile tag.

### Section 7 — YOUR NUMBERS
The **table** (| Measure | Your number |): agents in your revenue share organization today · agents you want to
attract in the next 12 months · your long-term goal · hours a week you can fully commit to attraction. Then
two lines: what a first weekly rhythm looks like inside those hours — the proposed line from `goals.md`
(conversations a week, nothing else, computed by Setup's fixed arithmetic), labeled *proposed — locked when
you set your attraction goals* (no command in this section; never "the Sunday block" or any clause from a
later-week file); and the three-year frame in one sentence (Mike's lesson: commit for three years, measure in
twelve-week quarters — said as Mike's, never with the word "doctrine"). **No money math, no scenarios, no
ratios, no rev-share figure, no scorecard.** The `>> ` callout is the 12-month number said as a sentence in
the member's words.

### Section 8 — YOUR VOICE
How the member talks, so they can see the system heard them — short: the voice in one line (from `voice.md`) ·
the three signature lines as `Label:` lines (verbatim, from the dictated answers and how they typed) · then
the three dictated answers, each under its own sub-band — **Why I'm excited about agent attraction** · **My
why** · **Why someone should partner with me** — quoted verbatim (typos and filler kept) and **trimmed to the
60–80-word core of each**. The tone-rule bullets and the never-say list stay in `voice.md`; the Book does not
carry them. No source tag after an answer. If a dictated answer is missing (the member skipped it or typed
instead), the sub-band carries the typed answer's core and one plain line that the spoken layer can be added
later (no command). The `>> ` callout is the member's single best spoken line.

### Section 9 — WHAT'S NEXT
Exactly three one-line bullets, plain, in order — by the state rule. The Week-1 state:
- **This week, in a new chat:** *say "my attraction brand direction"* — your brand (logo, colours, fonts), built
  in its own chat from this Book and how you talk.
- **Next week:** your lead magnet plugin builds your offer first, from Section 4, then your lead magnet and its
  opt-in page.
- **Any time:** *"just talked to an agent"* from the car · *"show me my Brain"* to refresh this Book.
Post-offer state: the first bullet reads *your brand direction is set; your Design Package brief is in 02 ·
Brand* when `brand-visual.md` shows the brand chat has run; the second names the Partner Offer in `05 · Offer`
and the magnet's state; the third is unchanged. At most three distinct command phrases in the section. No
open-items list, no compliance note, no scheduled-task note, no booking-link / CRM / tools sentence. The `>> `
callout is the one next thing to type — in the Week-1 state, **"my attraction brand direction"**.

---

## The anti-fluff rule (every section)

**Every claim traces to** (a) something the member said — captured in the Brain, ideally in their words — or
(b) explicitly-labeled doctrine ("per Mike's lesson …"), named as doctrine, never dressed up as fact. **The
swap test:** a sentence equally true for any agent at any brokerage ("agents follow people", "consistency is
key") is filler — delete it, or attach the specific. **A section an unrelated member could paste into their
own Book is a FAILED section.** Three specific lines are better than ten generalities. When the Brain is too
thin to support a claim, say what's missing and the phrase that captures it — an honest gap, never
confident fluff.

---

## The verification gate (hard PASS/FAIL — run on EVERY build before upload)

`shared/measure_book.py` extracts the text back out of the rendered `.docx` and runs checks 1–8 and 11–13 (and
the demo checks) by machine; 9, 10, 14 and 15 are read by hand. Check ALL of:
1. **Length** — every section at or under its MAXIMUM (above = FAIL); below its target = thin, reported, never a
   fail; the whole Book about 3,500 words or fewer (a demo Book 2,000–2,600). **The page estimate** — the
   script's layout estimate (the renderer's type scale, the forced breaks, the tables) — **FAIL above 15 pages,
   WARN above 13.** **No `[bracketed]` token anywhere**, real or demo.
2. **All NINE section headings present, in order, and nothing else:** Who You Are · Your Story · Your Brokerage
   Story · Your Unique Approach · Your Proof · Who Your Story Speaks To · Your Numbers · Your Voice · What's
   Next. No PART bands, no CHAPTER bands, no tenth band.
3. **Byline once** — the `--subtitle` line appears in the body on the cover only (the running footer does not
   count); the credential line appears once.
4. **No `<w:` markup** anywhere in the text.
5. **The tables** — Section 1 (8 to 12 rows, every value at most 15 words), Section 4 (the strategies table, 1+
   real rows), Section 5 (the agents-helped table, or the one honest line), Section 7 (the four-row numbers
   table) — tabular data as a wall of prose = FAIL.
6. **No money** — no rev-share, split, cap, stock, income, earnings or dollar figure anywhere; no scenario, no
   ratio, no scorecard, no "illustrative" money line. A single one = FAIL.
7. **Plain words** — at most four sentences in any paragraph; none of the jargon list in the text (downline ·
   unexplained upline · unexplained "the model" · three-way call · unique value proposition / UVP · funnel ·
   doctrine · "Partner Offer" outside Section 9 · "labeled as such" · "never here" · "the files behind it" · the
   standing banned words); commands (*say "…"*, *type "…"*) in Section 9 only, at most three distinct phrases.
8. **Nothing that was cut** — no compliance text, no operations (hours of business, booking link, CRM, call
   block, follow-up rhythm), no content pillars, no landscape research, no brand kit, no Design Package brief,
   no open-items list, no consent line, no "private call" sentence. Section 9 may name a later-week item in one
   line and nowhere else.
9. **Cardinal rules** — no negative characterization of any named brokerage, sponsor, team or person anywhere;
   no former brokerage named in a story.
10. **Derived, never chosen; anywhere, never a place** — Section 6 opens with the framing line verbatim; no
    sentence reads as a type the member picked; the local market appears in Section 1 only and never as a limit
    on who or where they attract; no protected characteristic anywhere.
11. **Contents page** — exactly one CONTENTS section, on page 2, with nine rows, in order, each carrying its
    summary of at most twelve words written for THIS member; any summary failing the swap test = FAIL.
12. **Band labels** — `SECTION 1` through `SECTION 9`, sequential, nine contents links resolving, and ZERO
    unresolved-TOC warnings on the renderer's stderr.
13. **The state rule** — a Week-1 Brain shows no offer row in Section 1, the forward opener in Section 4 and
    three bullets with the brand-chat callout in Section 9; a post-offer Brain shows the past-tense opener and
    never the forward line.
14. **Voice fidelity** — Section 8 carries the three signature lines verbatim and the three dictated answers
    (or the typed stand-in with its one line), each trimmed to its 60–80-word core; the read-back check ran.
15. **Grounding audit ran** — its "N facts traced, M cut" tally is in the build log (never in the member's
    message); `[confirm:]` markers, if any survived to the draft, 3 or fewer and resolved before render.
    **Anti-fluff spot check** — read Sections 2, 4 and 6: any paragraph failing the swap test = FAIL that
    section; rebuild it from the member's data (one rebuild cycle; the honest short render is the terminal
    state).

**Demo builds** add: the sanctioned string "(illustrative — demo)" appears exactly nine times, once in the small
line directly under each band, and nowhere else — no inline tag, no tag on a date, no variant; ZERO real source
attributions; ZERO real competitor, sponsor, team, lead-vendor, CRM or coach names (platforms used as tools and
the member's own brokerage may appear); the watermark present (filename + eyebrow + the cover line **verbatim**);
all nine sections filled. Every other check binds unchanged. **Real builds get the mirror tripwire:** the string
"(illustrative — demo)", a DEMO watermark or the demo cover line appearing ANYWHERE in a non-demo render =
automatic FAIL — rebuild from the Brain files.

On any FAIL: rebuild the failing sections from the Brain files and re-verify. **Never upload a failed render.
Never narrate the retry** — the member only ever sees the finished Book.

**Bounded retries — a gate may fail a build, never trap one.** TOC re-render: at most TWICE. Rebuild cycles:
at most TWO — a cycle is ANY post-gate rebuild + re-verify pass, full-Book or single-section. A build still
failing after its bounded retries **STOPS and tells the member plainly** what's blocking (the one gate, the one
section, what would fill it) — a visible blocker is better than an invisible loop. "Never upload a failed
render" holds absolutely; "never narrate the retry" applies to retries that succeed, not to a build that has
exhausted them. Edges: **wrong file in the workspace** (raw `════` text visible in a converted doc) = ONE
corrective re-upload of the already-rendered `.docx`; **push verify-fails** = TWO attempts per file, then
`attraction-brain-sync`'s recovery path; **renderer unavailable** = the `.md` fallback once, then stop.

---

## Regeneration rules

- **When:** the end of Setup · after the Partner Offer is built in Week 2 (Section 4 gains the UVP line,
  Section 9 updates) · "show me my Brain" / "regenerate my Brain Book" · whenever the Brain materially changes
  (the story updated, a second group derived, the voice refreshed). The brand chat does NOT regenerate the
  Book on its own (the Book carries no brand) — it updates on the next trigger. **A build's OWN write-backs**
  are never a material change and never trigger another regenerate — one build per trigger, always.
- **Refresh, don't fork:** same name pattern, new date, saved beside the old — newest = current; the old dated
  copies are the version history (the superseded copy may be trashed after a verified push; snapshots never).
- **No research, ever.** The Book never triggers a Prospect Radar run; the landscape lives in
  `prospect-intel.md` for the skills that need it and is never rendered here.
- After upload: push, then hand the member the direct link with the standing line — this is their book;
  everything the system knows about them, on about a dozen pages.
