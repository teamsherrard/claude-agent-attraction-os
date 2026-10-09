# Agent Attraction Brain Book — the canonical chapter contract

*Supersedes the pointer rules in `shared/brain-doc.md`. When any skill (Setup Phase 8, "show me my Brain",
the post-offer refresh in Week 2, the post-kit refresh, a Prospect Radar run, brain-health) builds or
regenerates the master Brain document, THIS file is the contract. The invariants, grounding laws, demo-brain
rules, pipeline, verification gate, and regeneration rules are carried whole from the realtor Book spec; the
chapter contract is the plan's four parts (§6), reading the `aa-1.0` schema files.*

The **📕 Agent Attraction Brain Book** is the flagship deliverable of the whole system — the one document that
proves, in the member's hands, what they paid for. It is a **premium render of the Brain's identity files plus a
researched analysis of their market's agent landscape**: part leader dossier, part prospect-intelligence
report, part consultant's plan. It is also **"the AI Brain file"** every Design Studio (`ds-*`) skill and the
Lead Magnet skills ask the member to upload — one doc, everywhere.

Two identities it must never lose:
1. **It is a RENDER, never a source.** The markdown files in `identity/` and `memory/` stay the source of truth.
   Everything in the Book must exist in a brain file first — including the research, which is **written back to
   `identity/prospect-intel.md` before rendering**. The Book is always rebuildable from the Brain; it never
   drifts, and it never holds facts the Brain doesn't.
2. **It is the product.** Members pay a premium; the Book must read like a strategist built it for them
   personally — long, specific, researched, and impossible to mistake for anyone else's book.

---

## Non-negotiable invariants (carried forward — never weaken any)

- **Build ONLY via `shared/render_doc.py`** per `shared/doc-formatting.md`. Use `--eyebrow "Agent Attraction
  Brain"`, `--title`, `--subtitle "[Name] · [Market]"`, and `--accent HEX` with the member's primary brand
  colour when `identity/brand-visual.md` records one (pipeline step 6). Never hand-write document XML. **If the renderer prints
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
  in one book."*
- **Render the FULL content of every identity file — never summarize, never compress.** Rich brain + thin
  render = FAILED render. 15+ pages is normal; a complete Brain runs 30–45 pages, and that is welcome.
- **Restructure, don't append** (Part II): the avatars become per-avatar sub-sections; the brokerage footprint
  becomes a table plus prose; a one-bullet-per-item list surviving anywhere is a FAILED render.
- **Research-on-render backfill:** if `prospect-intel.md` is thin or stale for Chapters 7–8, run the Prospect
  Radar research mandate NOW — **write it back to `prospect-intel.md` first**, then render. The Book's research
  pass IS a `attraction-prospect-radar` run: same mandate, same budget, same file, same row shapes.
- **Tables via pipe rows** for anything tabular (the snapshot card, the avatar-at-a-glance, the story bank, the
  brokerage footprint, where-they-gather, the five pains vs the stack, the money scenarios, the plan, the weekly
  KPIs, the colour table). Prose where prose persuades; structure where structure clarifies.
- **Byline once** (title block) — never repeat the full credential line in the Snapshot or elsewhere.
- **No raw markup:** any `<w:` in the extracted text = corrupt build = rebuild.
- **Never fabricate** — no invented stories, quotes, testimonials, production numbers, rev-share figures, or
  agent-landscape numbers. Expanded into the **GROUNDING LAWS** below — all seven bind every build. **Every
  researched number carries its source + as-of date.** These numbers flow into published content and on-camera
  scripts — **an unsourced stat in published content is a compliance incident, not a shortcut.**
- **Compensation stays private.** Chapters 9 and 11 are private-call material: the Book is the member's, but
  nothing in it is written as if it could be pasted into a post. Every money figure is "(illustrative)".
- **The cardinal rules bind the Book** (`03-model-positioning/13`): no sentence characterizes another brokerage,
  sponsor, or person negatively — not in the landscape, not in the positioning, not in a story. Former
  brokerages in stories are "a franchise", "an independent".
- **Written FOR the member** — second person, warm, clear headings, genuinely useful as a reference (identity
  files are third-person for Claude; the Book converts the voice). The member is "you"; the people they attract
  are "agents".
- **Never narrate a failed render or the retry to the member** — they only ever see the finished Book.
- **Placeholder behavior for unbuilt sections is designed, not orphaned** (see Placeholders below), and the
  **open-items page** (Chapter 18) is where every gap lives with the week that fills it.

---

## GROUNDING LAWS — zero fabrication, true to THIS member

These laws bind every build and every regenerate, and they outrank style, length, and word targets: a Book
that misses a word range is thin; a Book that breaks a grounding law is wrong.

1. **Market lock.** The member's market and the states/provinces where they may attract (`profile.md`,
   `compliance.md`) are the only geography the Book treats as theirs. Research may describe adjacent markets
   ONLY in Chapter 7, capped at 2–3, each labeled "adjacent" / expansion candidate, and only inside their
   recruiting scope. **Same-name guard:** every research query carries city + state/province; a result whose
   geography doesn't match is discarded, never adapted.
2. **Brokerage and sponsor rule.** Name a brokerage in the landscape ONLY as a sourced, dated footprint fact
   (agent count, office count, a public move). Name a competing sponsor, team, or team leader ONLY when research
   verified them with source + as-of date, and ONLY as observable facts — never a verdict, never a weakness.
   **A missing name beats a wrong name**; and a negative sentence about any named party is a FAIL (cardinal rules).
3. **Voice & identity fidelity.** Every claim about the member — years, brokerage, journey beats, leader moment,
   why, what worked, proof, organization size — traces to their interview answers or Brain files. Reuse their
   own phrasing wherever it exists. NEVER invent quotes, agent anecdotes, testimonials, or stats about them.
   Where the Book paraphrases, it must still sound like `voice.md` / `voice-print.md`.
4. **Numbers.** Every figure is from their Brain (labeled as theirs), from research (source + as-of date), or an
   illustrative scenario built on their own stated assumptions (labeled "(illustrative)") — no fourth source,
   and no invented precision. Nothing in the Book states what a partner will earn. Locale, currency, and units
   come from `config.md`.
5. **Uncertainty protocol.** Cannot verify → omit it, or mark it `[confirm: …]` inline for the member. A wrong
   specific is worse than a gap. Markers go mid-sentence (never at line start), NEVER on researched numbers in
   Chapters 7–8 (omit those instead) — and more than 3 in the whole draft means the Brain isn't ready: capture
   the answers with the member first, then render.
6. **Pre-render grounding audit** (pipeline step 5). Before rendering, enumerate every proper noun (brokerage,
   sponsor, team, association, event, platform, employer, the member's former brokerage if it slipped in) and
   every number in the draft; trace each — as the pairing it's used in — to a Brain file or a sourced research
   result; CUT anything untraceable. A former brokerage named in a story is cut and replaced with its type. If
   cuts drop a chapter below its minimum, the owning brain file is thin: re-run that chapter's research mandate
   ONCE per chapter per build; if refreshed research still can't support the minimum, render the honest gap and
   what would fill it — never pad, never loop. Report the tally — "N facts traced, M cut" — in the hand-off.
7. **Read-back check** (pipeline step 4). After assembly, re-read `voice.md` + `voice-print.md` (if built) and
   `compliance.md`, and confirm the Book's characterization of the member matches, and that no public-style
   sentence carries a compensation number or an earnings claim; fix mismatches before rendering — ONE fix pass
   per build. A mismatch surviving it is flagged in the hand-off message, never re-fixed in a loop.

---

## DEMO BRAINS — explicitly fictional, for training + demos only

When the person in the session **explicitly asks for a fictional brain** — the words "demo", "mock", "fake",
"fictional", "test member", "sample agent" in THEIR OWN request (Mike demoing for the cohort, a test drive) —
the build runs in **demo mode**. Two conditions, both required:

- **The subject is fictional** — a named persona who is NOT the person in the session. The demo world for this
  OS is **Taylor Brooks · Real Broker · Austin, TX · 6th year · former teacher · open-house lead system + a
  Sunday follow-up routine · 2 agents in the organization · goal 25 agents in 12 months**; the demo avatar is a
  2–5 year agent paying for leads with no system; the demo success story is Priya Nair, 3 buyers under
  contract in her first 60 days. Demo keywords aimed at the member's OWN identity ("mock something up for MY
  market", "let's just do a test run on my brain") are a REAL build — the grounding laws bind.
- **When there is ANY doubt who the subject is, ask the one question** — "Fictional demo member, or your real
  Brain?" — before proceeding.

In demo mode:
- **No live research.** Skip the research pass, the staleness rules, and the grounding audit's tracing. Fill
  Chapters 7–8 with plausible, clearly-labeled illustrative content — minutes, not research cycles.
- **Every production, money, ratio, count and landscape figure is tagged "(illustrative — demo)"** — in prose,
  in table headers and in table cells — and NEVER carries a fabricated source attribution. Exempt from the tag:
  dates, clock times, durations, chapter and step numbers, and table cells under a header that already carries
  the tag (tag the header once, not every cell).
- **No real competitor, sponsor, team, lead-vendor, CRM, or coach names.** Fictional names only ("the Lakeline
  team"). Platforms used as tools (Instagram, YouTube, Zoom, Google Sheets, Claude Design) may be named, and so
  may the demo member's own brokerage (Real Broker) and the state regulator; nothing is claimed about any real
  person.
- **Watermark it, unmissably:** filename **"📕 [Name]'s Agent Attraction Brain Book — DEMO — [YYYY-MM-DD]"**;
  eyebrow `Agent Attraction Brain · Demo`; one meta line on the cover, **verbatim — never suffixed, never
  reworded** (the gate checks the exact string): *"Demo document — illustrative data, not researched."*
- **Total isolation from real Brains.** A demo scaffolds locally at `~/attraction-brain-demo/` and creates/pushes
  to its OWN workspace folder named **"[Workspace name] — DEMO"** (own `_attraction-workspace.md` marker, also
  demo-stamped) — NEVER into an existing real workspace. The demo Book is excluded from "newest = current":
  Claude Design's "upload your AI Brain file" must never be handed a demo Book. Isolation cuts BOTH ways: a
  demo build never modifies, renames, retires, or cleans up anything outside its own workspace. Demo pushes
  are LIGHT: create the files, one folder-listing verify at the end.
- **Every demo brain file opens with the banner line** `DEMO BRAIN — fictional member, illustrative data —
  never publish.` — so ANY skill that reads the file sees what it's holding before it quotes a number.
- **Demo-to-real never converts.** "Love it — now build mine" starts a REAL build from a fresh template with
  every gate re-armed.
- **No placeholder chapters.** A demo Book renders all eighteen chapters FILLED — the offer, the pillars, the
  framework, operations all get illustrative content (a demo shows the finished product).
- **Everything else holds at full strength:** the complete structure, the linked contents page, chapter bands,
  formatting gates, voice conversion. Word counts: **the per-chapter minimums bind in demo mode exactly as in a real
  build** (the demo is what the training video shows, so it must look like the finished product); the only exceptions are
  the two researched chapters (7 and 8), which render as honest demo landscapes at no less than half their minimum, and a
  demo never renders a `[bracketed]` token — every value is a fictional one (a demo booking link reads like a real link).
- **The demo marker travels with the BRAIN.** A demo build writes `Demo brain: yes` into `config.md` and keeps
  the "(illustrative — demo)" tags inside the brain files themselves. Any skill that touches a brain whose
  `config.md` says `Demo brain: yes` STAYS in demo mode; a real member resuming on a demo brain is told plainly
  and offered a fresh real setup — never a silent conversion.
- **Demo mode is NEVER inferred.** Thin answers, a rushed member, "just fill it in", or "use defaults" do NOT
  trigger it — only the explicit fictional framing above does (and a `Demo brain: yes` already in `config.md`).

---

## The build pipeline (run in this order, every build and every regenerate)

1. **Pull + read.** Sync the Brain (`attraction-brain-sync` PULL), then read `brain.md`, `config.md`, every
   identity file that exists, `memory/scorecard.md` (Targets block), `memory/top-50.md` (count only, never
   names into the Book), and `shared/brand-doctrine.md` + `shared/attraction-doctrine.md` §7b, §13 (for the
   labeled-doctrine lines).
2. **Research pass — backfill `prospect-intel.md` FIRST — inside a budget.** The whole build gets **~30 web
   searches/fetches, total**, spent by priority: brokerage footprint in the member's market (≤8) → recent agent
   movement and team formations (≤8) → where each avatar type gathers in that market (≤4 per avatar) → licensing
   and agent-count trends (≤4) → adjacents last (≤2 each, only with budget left). One search per fact-family,
   never one per fact; stop the moment a chapter's must-appear list is covered; a `prospect-intel.md` that is
   current (staleness windows) costs ZERO searches. Budget exhausted = render what's verified with honest gaps.
   This pass IS `attraction-prospect-radar`'s mandate: same shape, same research log row, same file. Write it
   into `identity/prospect-intel.md` with source + as-of date on every number, **push before rendering**
   (write → push → verify). **Skipped entirely in demo mode and on a Week 1 first build when the member said
   "skip the research for now"** — then Chapters 7–8 render the designed placeholder (below).
3. **Assemble the structured text** per the **Book structure** (below) — and ONLY that grammar: the cover title
   block; the `[[TOC]] … [[/TOC]]` contents block; every PART and CHAPTER as a CAPS band wrapped in divider rules;
   sub-bands (`──── Label ────`) inside chapters — one per avatar, per story, per scenario; `•` bullets; numbered
   steps as `1.  …` lines; `Label:` lead-ins (signature phrases, testimonials, the compliance disclaimer); `>> `
   lines for each chapter's 1–2 key-insight callouts; pipe-row tables; generous blank-line spacing. No Markdown
   `#`/`**`/backticks in the body.
   **Write it to the input file chapter by chapter — one append per PART or CHAPTER band, never one emission.**
   The full text runs 60–100 KB; emitted in one block, a cut-off output renders as a clean-looking 3-page Book
   with no error, because the renderer cannot tell a short file from a finished one. Append the cover and the
   contents block first, then each band with its body as it is assembled, and re-read the file's tail before
   the next append. **Structural pre-check — run on the input file before step 6, every build:** (1) the
   `[[TOC]] … [[/TOC]]` block holds exactly 22 rows — 4 `PART` rows and 18 `CHAPTER n — TITLE :: summary` rows
   numbered 1–18 in order; (2) the body holds exactly 4 `PART` bands and 18 `CHAPTER` bands numbered 1–18 with
   no gap, each inside its Part; (3) every contents row's text left of `::` equals a band
   character-for-character; (4) the last band is `CHAPTER 18 — YOUR OPEN ITEMS`, with its body under it. The
   two counts that prove it: `grep -c '^CHAPTER [0-9]* — ' <input>` = **36** (18 rows + 18 bands) and
   `grep -c '^PART [IVX]* — ' <input>` = **8** (4 + 4). Any other number = the input is incomplete: append the
   missing chapters, re-run the pre-check, and only then render — **never render a short file, never "render
   what's there".** If the member is waiting while it trips, they see one progress line — *"your Book is still
   assembling, one more minute"* — a status, not a failure narration (they never hear "truncated" or "retry").
4. **Read-back check** (Grounding Law 7). One fix pass; survivors flagged in the hand-off.
5. **Pre-render grounding audit** (Grounding Law 6). Keep the tally for the hand-off.
6. **Render** with `render_doc.py` to `.docx` — only an input that passed the step-3 structural pre-check.
   **Pass `--accent HEX` with the member's primary brand colour** when `identity/brand-visual.md` has one:
   the Final kit `Colors:` line first (the primary / brand hex), else the Direction block's
   `Primary / brand: #hex`; no hex recorded yet (a `[#hex]` placeholder, "none", or only a description like
   "a lot of green") → omit the flag and the renderer's near-black default applies. Never pass the
   brokerage's colours. The accent colours only the cover rule, the PART kickers, the `>> ` callout bar and
   the table-header tint — everything else stays the neutral house standard — and the renderer falls back
   to near-black for text by itself when the colour is too light to read on white.
   **Renderer stderr must show ZERO warnings.** An unresolved-TOC warning means a contents row and a chapter
   band don't match character-for-character: fix the structured text, re-emit, re-render (at most twice — a
   copy-paste alignment fix, never a rebuild). A `sub-band label is N characters (cap 80)` warning means a
   `──── Label ────` line is too long and has rendered as body text WITH its literal dashes: shorten the
   label, re-render. `RENDERER-UNAVAILABLE` → the `.md` fallback, once, no loop.
7. **Verify** against the hard gate (below). FAIL → rebuild the failing chapters from the full brain-file
   contents and re-verify. Never upload a failed render.
8. **Upload to `01 · AI Brain`, push, hand over the direct link** — with the grounding-audit tally ("N facts
   traced, M cut") and the open-items count in the hand-off message.

---

## Book structure — cover, contents, parts, chapters (the render grammar)

**Page 1 — the cover.** Eyebrow `Agent Attraction Brain` (`--eyebrow`). Title `[Name]'s Agent Attraction
Brain Book` (`--title`; no 📕 on the cover — the emoji lives in the filename). Byline `--subtitle "[Name] ·
[Market]"`, with the one credential line (brokerage · years · what they're building) as the meta line — its ONE
appearance. Date `[Month D, YYYY]` on its own meta line — the same date as the filename's ISO stamp. Every
page after the cover carries the title top-right and `[Name] · [Market] · AGENT ATTRACTION BRAIN` + `Page X
of Y` in the footer — automatic, nothing to write.

**Page 2 — CONTENTS.** Immediately after the title/meta lines, one `[[TOC]] … [[/TOC]]` block — the renderer
builds a linked contents page and page-breaks around it. One row per chapter — all eighteen, in order — with
the four PART rows grouping them:

```
[[TOC]]
PART I — WHO YOU ARE
CHAPTER 1 — SNAPSHOT :: [one line, written for THIS member]
CHAPTER 2 — THE LEADER :: …
…
PART IV — HOW YOU WIN
…
CHAPTER 18 — YOUR OPEN ITEMS :: …
[[/TOC]]
```

Each `::` summary is one line **written for that member** — it names their actual type of agent, their market,
their edge, their one-line why. *"Why 2–5 year agents paying for leads will hear Taylor before anyone else —
and the Sunday routine that proves it"* passes; *"An overview of the member's target audience"* is a FAILED
contents page — the swap test applies to every row. Row text left of `::` must match its chapter band
**character-for-character**.

**PART and CHAPTER bands.** `CHAPTER N — TITLE` and `PART I — WHO YOU ARE` / `PART II — WHO YOU ATTRACT` /
`PART III — WHAT YOU OFFER` / `PART IV — HOW YOU WIN` — CAPS bands wrapped in divider rules, chapter numbers
sequential 1–18 with no gaps. Sub-headings inside chapters stay sub-bands (`──── Label ────`, label ≤ 80
characters). Each PART page closes with an automatic **"IN THIS PART"** linked list of its chapters (number ·
title · the contents summary), built by the renderer from the contents rows — write the Part bridge as usual;
the list is appended after it, so a Part page is never near-empty.

**`>> ` callouts.** Each chapter surfaces its **1–2 key insights** this way (placeholder chapters exempt): the
most decision-relevant, member-specific line — a sourced fact plus what it means for them, or their own
sharpest line. Never more than two per chapter, never generic advice. Testimonials and signature phrases keep
their `Label:` treatment; `>> ` is reserved for insight. Chapter 13 opens with the why-line as its callout.

**Tables** stay pipe rows, exactly where the chapter contract mandates them.

---

## The chapter contract — four parts, eighteen chapters

The Book runs the plan's arc: **who you are → who you attract → what you offer → how you win.** Each PART
opens with its CAPS band and a 2–4 sentence consultant-voiced bridge. Chapter headings are exact — the verify
gate checks all eighteen. **Word counts are per-chapter MINIMUMS — floors, never ceilings.** A rich brain file
renders in full even when its chapter runs two or three times the floor (a 1,200-word voice file is a
1,200-word chapter; eleven chapters of a complete Brain land well above their floors), and a floor is never a
reason to compress — "render the FULL content, never summarize" outranks every number in this table. A
placeholder chapter is exempt from its floor but must still render its heading + designed placeholder text.

| # | Chapter (CAPS band) | Source file(s) | Words (minimum) | Researched? |
| --- | --- | --- | --- | --- |
| — | PART I — WHO YOU ARE | — | 40+ (a 2–4 sentence bridge) | no |
| 1 | SNAPSHOT | `brain.md` quick-ref | 100+ | no |
| 2 | THE LEADER | `profile.md` + `strategy.md` + `journey.md` (leader moment) | 250+ | no |
| 3 | YOUR JOURNEY | `journey.md` (three beats + "who relates to this" + the WHY) | 350+ | no |
| 4 | YOUR STORY BANK | `story-bank.md` | 400+ (the six developed Stop-6 seeds meet it on a first run) | no |
| 5 | YOUR VOICE & BRAND | `voice.md` + `voice-samples.md` + `voice-print.md` + `brand-visual.md` | 300+ | no |
| — | PART II — WHO YOU ATTRACT | — | 40+ (bridge) | — |
| 6 | YOUR AGENT AVATARS | `avatars.md` | 500+ | no |
| 7 | YOUR MARKET'S AGENT LANDSCAPE | `prospect-intel.md` | 500+ · placeholder until researched | yes |
| 8 | WHERE THEY GATHER | `prospect-intel.md` + `avatars.md` | 250+ · placeholder until researched | yes |
| — | PART III — WHAT YOU OFFER | — | 40+ (bridge) | — |
| 9 | YOUR MODEL, POSITIONED | `positioning.md` + `brokerage-model.md` + `journey.md` → `## Why join me` | 350+ at Week 2 · 1,200+ once the why-join-me long version and the model are built · designed placeholder while `positioning.md` is at seed | no |
| 10 | YOUR OFFER | `offer.md` | 300+ · "(so far)" mode when Status is seeds | no |
| 11 | THE MONEY, HONESTLY | `goals.md` → "The money, honestly" | 300+ · placeholder if the calculator was skipped | no |
| 12 | YOUR PROOF | `proof.md` | 200+ | no |
| — | PART IV — HOW YOU WIN | — | 40+ (bridge) | — |
| 13 | YOUR 12-MONTH AND 90-DAY PLAN | `goals.md` + `execution-framework.md` (if built) | 400+ (250+ before `execution-framework.md` is built) | no |
| 14 | YOUR WEEKLY ACTIVITY | `goals.md` (weekly activity, ratios) + `scorecard.md` Targets block + `execution-framework.md` KPIs (if built) | 150+ | no |
| 15 | YOUR CONTENT PILLARS | `content-pillars.md` | 200+ · placeholder until Week 3 | no |
| 16 | HOW YOU OPERATE | `operations.md` + `leadership.md` | 150+ · placeholder OK | no |
| 17 | COMPLIANCE | `compliance.md` | 150+ | no |
| 18 | YOUR OPEN ITEMS | every skipped question, unset field, and later-week file | 100+ | no |

**Totals (minimums).** **The 3,000-word absolute floor binds every real build.** A Week 1 first-run Book
(research done; Chapters 15 and 16 placeholders; Chapter 10 in "so far" mode; Chapter 9 at seed) lands
**≥ 4,400**; a first run with research skipped **≥ 3,600**; a complete Brain with the Week 2–3 files built
**≥ 5,000 — and typically 9,000–16,000 words / 30–45 pages. Long is correct.** Below its floor a rendered
chapter is thin — fix the chapter, never pad. Above it, never compress.

### Chapter 1 — SNAPSHOT
The one-page "who is this leader" card. **Table** (Label | Value): name · brokerage · what they're building ·
market and recruiting scope · primary type of agent (one line) · known for · the one-line why I'm here · offer
status (in plain words: "Partner Offer: Week 2") · voice in one line · this week's activity target ·
organization today / 12-month target · booking link · socials · brand colours (hex) · compliance status. One
prose line on how to use the Book. No credential line (byline rule).

### Chapter 2 — THE LEADER
`profile.md` in prose: the before-story, what they do outside real estate (when they shared it), the path in,
the brokerage and the human reason they joined (never the mechanics), what they are building and why that shape, the leader moment from `journey.md`, what they want
to be known for and the niche from `strategy.md`. Through the brand formula: name which of Authority ·
Relatability · Aspiration is strongest today (labeled as doctrine, per `brand-doctrine.md` §1).

### Chapter 3 — YOUR JOURNEY
The three beats as **sub-bands**, each developed (never transcribed — the echo test from the workshop skills:
their answer, what it means for attracting agents, how to use it), each ending with the `Label:` line
**Who relates to this:**. Then the WHY in full, the why-line as the chapter's `>> ` callout. Former
brokerages never named.

### Chapter 4 — YOUR STORY BANK
Open with the **table** | Story | The moment | The lesson | Lands with (type) | Pain | Use |. Then every story
written out in full under its own sub-band. On a first run every Stop-6 seed renders as its developed
60–120-word block (the scene · what it proves · where it gets used — written by Setup Stop 6 before the Book
is built) under its own sub-band; only seeds captured later (the capture rows) render as one-liners in a
closing **"Still to tell"** list, with the phrase that builds them ("build my attraction story bank"). A seed
pasted under a heading is not a story (the echo test). Never invent a story.

### Chapter 5 — YOUR VOICE & BRAND
Tone rules (**bullets**), sounds-like / never-sounds-like, signature phrases as `Label:` lines, the writing
samples, the spoken voice-print if built (else one friendly "say 'capture my speaking voice'" line inside the
chapter, not a placeholder chapter). Then brand: the **Inventory** as a **table** (| Item | State |), the
**Direction** in prose, the **colour table** (| Colour | Hex | Role |) when colours exist, the leader-vs-selling
decision, and the standing note: *the Design Package (aa-logo-design → aa-style-sheet-design → aa-brand-kit-design) builds the visuals
in Claude Design this week; drop the kit into 02 · Brand and this chapter shows it on the next regenerate.*
After the kit exists, render the kit's logo file name, palette, and type.

### Chapter 6 — YOUR AGENT AVATARS
Open with the **avatar-at-a-glance table**: | Avatar | Type | Where they are | Core pain | What they need to
hear |. Then **one sub-band per avatar**, each rendered IN FULL from `avatars.md`: the one-line target, where
they are right now, their biggest problem in their words, what they've tried, the top pains mapped to the
member's strengths (table: | Pain (Mike's wording) | Why it hurts now | Your strength | Proof |), the mirror
("why they'd relate" + the **Say it like this:** line), triggers, objections to expect, the ask that fits.
Every avatar in the file appears. Then the **"Not the right fit"** line (fit and timing, never a brokerage name).
Type of agent, never a location, never a protected characteristic.

### Chapter 7 — YOUR MARKET'S AGENT LANDSCAPE  *(researched)*
The heart of Part II. Open with the **brokerage footprint table**: | Brokerage type / name | Approx. agents in
market | 12-month trend | Source · as-of |. Then prose on the landscape: who is growing, who is shrinking,
recent movement and team formations (each sourced and dated), licensing and agent-count trends, and **2–3
adjacent markets** inside the member's recruiting scope, labeled "adjacent". Then **3–5 "what this means for
you" implications, each tied to a named avatar AND a sourced fact**. Honesty rules: observable facts only;
"no visible movement found as of [Month YYYY]" is a finding; never a negative characterization of any
brokerage or person (cardinal rules); "a missing name beats a wrong name". **Research mandate:** write back to
`prospect-intel.md` first, per `attraction-prospect-radar`'s mandate. Anti-fluff rule applies.

### Chapter 8 — WHERE THEY GATHER  *(researched)*
**Table** per avatar type: | Avatar | Online rooms (groups by type, channels, podcasts) | In person
(associations, events, trainings) | Signals they're ready | Source · as-of |. Then prose connecting the rooms
to the member's content and the Top-50 ("your first ten names are already in …"). Types of places, never lists
of real people; never scraped members. Where research found little, say so and point at the avatar's
sphere-first sources (the workshop's "first ten": the other side of their last deals, former colleagues, agents
who comment).

### Chapter 9 — YOUR MODEL, POSITIONED
From `positioning.md`: the one line said out loud, the vehicle-vs-reason framing, the bridge-the-gap line per
avatar, what stays for the private call, and the 2-minute model script (rendered, clearly marked "for your
call, not for posting"). From `brokerage-model.md` (if built): the model in plain English, each mechanic with
its source document — else one line: "say 'explain my model to me' in Week 2." Then the **`## Why join me`
block from `journey.md`** as its own sub-band: the 60-second version, the long version, the one-breath line —
if not written yet, one line naming Week 2. No competitor named negatively; no number without a source.
**When `positioning.md` holds only the Q36 seed line** (the model, the script and the why-join-me are Week 2),
the chapter renders the designed **"Your model, positioned (so far)"** placeholder (Placeholders, below) — the
seed line developed, Week 2 named — never four sentences under a bare heading.

### Chapter 10 — YOUR OFFER
**When `offer.md` Status is seeds:** the band reads `CHAPTER 10 — YOUR OFFER` and the first sub-band is
**"What you have to give (so far)"** with one line: *"Your Partner Offer is built in Week 2 — this is the raw
material it starts from."* Render the "what worked" **table** (| Strategy | What it involved | Result | Teach
it? |), the edge, teach-first, and the three layers (brokerage · upline · you) as captured. Nothing reads as a
gap. **When finalized or built:** the full offer — the UVP one-liner as the `>> ` callout, the five pains table
(| Pain (Mike's wording) | Solved? | What they give | The outcome | Proof |), the Partner Offer (core promise ·
mechanism · proof · support · why now), what's included (**bullets**), Module 1, the first 30 days (**table**),
the value stack (**table**) and the digital product. Outcomes, never features; what the member will SHOW, never
what a partner will EARN; no splits, caps, stock, or earnings.

### Chapter 11 — THE MONEY, HONESTLY
From `goals.md` → "The money, honestly": the plan mechanics used (with source), the member's own production
assumption, the ratios, and the **scenario table** (| Scenario | Agents at 12 months | Weekly conversations |
Illustrative annual rev share | Label |) — every number "(illustrative)", the stamp line under the table, the
chapter marked private-call material in one line. The `>> ` callout is the weekly activity it takes, not a
dollar figure. Placeholder (below) only if the member explicitly skipped Stop 11.

**When the member deferred the plan mechanics ("explain mine to me"):** the calculator still runs, on the strictest
generic default mechanics for their model type, every number labelled "default mechanics — replaced in Week 2 by the
Brokerage Model Expert"; the chapter always carries the three-scenario **table**, the weekly-activity derivation under
it, and a plain-words reading of what the member's own assumptions imply. A money chapter that is only stamps and
ratios is a FAIL (minimum 400).

### Chapter 12 — YOUR PROOF
`proof.md` in full: production wins as stated, agents already helped (**table**: | Agent | What you did | What
happened | When |), organization today, reviews from agents as `Label:` quotes (verbatim, consent noted),
upline proof labeled as the upline's. Zero proof = one honest line + "help agents for free and earn the first
case study" (`04-value-proposition/33`) — never manufactured credibility.

### Chapter 13 — YOUR 12-MONTH AND 90-DAY PLAN
**Opens with the why-line** (verbatim, the `>> ` callout). Then `goals.md` in full: the 12-month milestones
**table** — whose "Rev share (illustrative, member's assumptions)" row renders as *"see Chapter 11 —
private-call material"*, never the figure (the figure lives in Chapter 11 only) — the 30-60-90 **table**, the
three-year commitment stated once, the intangibles to track. When `execution-framework.md` is built: the
four-quarter **table**, the three weekly non-negotiables, the constraint of the quarter, the CEO rhythm
**table**; before it is built the chapter is goals-only and its floor is 250. Never summarize the math.

### Chapter 14 — YOUR WEEKLY ACTIVITY
The controllables: the weekly activity and daily slice from `goals.md`, the ratios with their labels (member /
default), the Targets block from `scorecard.md` as a **table** — its "Rev share (illustrative)" row renders as
*"see Chapter 11 — private-call material"*, never the figure — the weekly KPIs from the framework when built,
and one paragraph on how the Daily Debrief scores each day (Ahead · On pace · Behind) and the Monday check-in
rolls the week. "Adjust the target or the hours, never the math."

### Chapter 15 — YOUR CONTENT PILLARS
When built (Week 3): `content-pillars.md` in full — pillars (**bullets**, each with its why), platforms, the
cadence as a **table** (| Day/Slot | Platform | Format/Series |), the two CTAs, the signature series — plus one
bridging paragraph tying each pillar to an avatar's pain and to Mike's four content types (labeled as doctrine,
`attraction-doctrine.md` §13). When not built: the designed placeholder (below).

### Chapter 16 — HOW YOU OPERATE
When built: `operations.md` in full (hours, CRM and tagging, booking link, call block, 3-way partner, the
follow-up cadence as a **table**, onboarding steps as **numbered steps**) + `leadership.md`'s readiness
scorecard **table** and fix-first list when built. When only the Stop 16 basics exist: render them under a
sub-band and the placeholder line for the rest.

### Chapter 17 — COMPLIANCE
`compliance.md` in full: Status in plain words, the brokerage disclaimer **verbatim** under a `Label:` line, the
income disclaimer verbatim (labeled "default — replace with your brokerage's" when it is the default), license
and name display rules, the rev-share marketing policy as captured, recruiting scope, the AI-likeness line, the
claims-to-avoid list (**bullets**), the cardinal rules. Unset items render as flagged, never invented — this
chapter never guesses at legal text.

### Chapter 18 — YOUR OPEN ITEMS
A designed page, never a list of failures. One **table**: | Open item | What fills it | When |. Rows come from:
skipped questions (a placeholder in any file), `compliance.md` fields still unset, `offer.md` at seeds ("your
Partner Offer" → Week 2), `positioning.md` at seed ("position my model" → Week 2), `brokerage-model.md` empty
("explain my model to me" → Week 2), `prospect-intel.md`
thin ("run my prospect radar" → Week 2), the brand kit not yet in `02 · Brand` ("run the Design Package" →
this week), `content-pillars.md` (Week 3), `execution-framework.md` ("build my execution framework"),
`leadership.md` / `operations.md` (optional), `voice-print.md` ("capture my speaking voice"). Then the
**workshop map**: the next three things to type, in order. A Book with zero open items renders this chapter as
a short "Nothing open — here's what to do this week" page.

---

## The anti-fluff rule (Chapters 2, 6, 7, 8, 9 — and the Part bridges)

**Every claim must trace to exactly one of:** (a) something the member said — captured in the Brain, ideally in
their words; (b) a sourced, dated researched fact from `prospect-intel.md`; (c) explicitly-labeled doctrine —
"per Mike Sherrard's lesson …" / "per the OS's brand doctrine …" — named as doctrine, never dressed up as fact.

**The swap test:** if a sentence would be equally true for any agent at any brokerage in any market ("agents
follow people", "consistency is key", "relationships matter") without the member's specifics attached, it is
filler — delete it, or attach the specific. **A chapter an unrelated member could paste into their own book is
a FAILED chapter.** Better three specific, traceable insights than ten generalities. When the Brain is too thin
to support a claim, say what's missing and how to capture it — an honest gap beats confident fluff.

---

## Placeholders (real builds only — demo brains NEVER placeholder)

Every placeholder is a DESIGNED page, not an orphan line — it sells the next step and names the week. Each
placeholder line is ONE line of structured text (never split mid-sentence). Exact treatment:

- **Chapters 7–8 (research skipped or not yet run)** → lead line: *"Your market's agent landscape gets
  researched in Week 2."* Callout: `>> Say "run my prospect radar" — who is growing in [market], who is moving,
  and the rooms where [primary avatar] actually gather, every number sourced and dated.` Then a short "What
  will appear here" bullet list: the brokerage footprint table · recent moves and team formations · where each
  type of agent gathers · what it means for you.
- **Chapter 9 (`positioning.md` at seed — the Q36 line only)** → first sub-band **"Your model, positioned (so
  far)"**. The seed line is the chapter's first `>> ` callout, then one short paragraph developing it (what it
  means for the agents they attract, how to say it on a call — their words, the echo test), then the lead line:
  *"Your model gets positioned in Week 2."* Second callout: `>> Say "position my model", "explain my model to
  me", and "why join me" — the vehicle and the reason, the two-minute script for your call, your model in
  plain English, and your why-join-me story in three lengths.` Then the "What will appear here" bullet list:
  the one line said out loud · the bridge-the-gap line per avatar · the 2-minute model script · the model in
  plain English · the why-join-me in three lengths. Nothing reads as a gap. Mirrored in Chapter 18.
- **Chapter 10 at seeds** is NOT a placeholder — it renders in "(so far)" mode (above).
- **Chapter 11 (calculator skipped)** → lead line: *"This chapter is waiting on one 10-minute conversation."*
  Callout: `>> Say "run my rev share scenarios" — three illustrative scenarios built on your own assumptions,
  and the weekly activity each one takes. Nothing here is a promise.`
- **Chapter 15 (before Week 3)** → lead line: *"Your content pillars are built in Week 3 with the Short-Form
  system."* Callout: `>> Your pillars will come from your journey, what you teach, and your agents' wins —
  Mike's four content types, aimed at [primary avatar].`
- **Chapter 16 (basics only / not built)** → lead line: *"This chapter fills in as your systems do."* Callout:
  `>> Say "set up my attraction operations" and "audit my leadership" — your hours, follow-up rhythm, onboarding steps,
  and an honest readiness score, so you never attract agents you can't serve.`
- Voice-print and later-captured story seeds get their one-line "how to add" note inside Chapters 4–5, not a placeholder
  chapter. **No other chapter may placeholder on a complete brain.** If a first-run identity file is genuinely
  missing, render its heading + the honest one-line state + the phrase that fills it — never a fabricated
  section, never a silently skipped heading. Every placeholder also appears as a row in Chapter 18.

---

## The verification gate (hard PASS/FAIL — run on EVERY build before upload)

Extract the text back out of the rendered `.docx` and check ALL of:
1. **Count** — complete brain: 5,000+ words; Week 1 first run with research: 4,400+; research skipped:
   3,600+; **absolute floor in all cases: 3,000**. An honest-gap chapter rendered per Grounding Law 6 is exempt
   from its per-chapter range; the floor still binds. **Per chapter:** every chapter is at or above its minimum
   from the chapter table (designed placeholders and honest-gap chapters exempt; demo builds included). Any chapter
   under its minimum is a FAIL for that chapter: rebuild it from the full brain-file contents — develop (the three
   moves: their answer · what it means · how to use it), never pad — and re-verify. **No `[bracketed]` token anywhere**
   in the rendered text, real or demo.
2. **All EIGHTEEN chapter headings present** (Snapshot · The Leader · Your Journey · Your Story Bank · Your
   Voice & Brand · Your Agent Avatars · Your Market's Agent Landscape · Where They Gather · Your Model,
   Positioned · Your Offer · The Money, Honestly · Your Proof · Your 12-Month and 90-Day Plan · Your Weekly
   Activity · Your Content Pillars · How You Operate · Compliance · Your Open Items) + the four Part bands.
3. **Byline appears once** (title block only).
4. **No `<w:` markup** anywhere in the text.
5. **Avatar structure** — one sub-band per avatar in `avatars.md`, the at-a-glance table present, no avatar
   skipped; the "Not the right fit" line names no brokerage.
6. **Source discipline** — every number in Chapters 7–8 carries source + as-of date, verified within the
   staleness window (research RUN within 3 months for footprint and movement, 6 for where-they-gather — the
   researched-stamp, not the source's publication date; the newest available data older than the window is
   cited as the newest available and PASSES). At most ONE refresh per chapter per build.
7. **Money discipline** — every figure in Chapter 11 carries "(illustrative)"; the stamp line is present; no
   sentence anywhere states what a partner will earn; no compensation number appears outside Chapters 9 and 11
   — the rev-share rows of the 12-month table (Chapter 13) and the Targets table (Chapter 14) point at Chapter
   11 ("see Chapter 11 — private-call material"), so a complete real Brain passes this check on its first render.
8. **Cardinal rules** — no negative characterization of any named brokerage, sponsor, team, or person anywhere;
   no former brokerage named in a story.
9. **Tables rendered where the contract says table** — tabular data as wall-of-prose = FAIL.
10. **Anti-fluff spot check** — read Chapters 2, 6, 7, 8, 9: any paragraph failing the swap test = FAIL that
    chapter; rebuild it from the member's data (one rebuild cycle; the honest-gap render is the terminal state).
11. **Placeholders only where allowed**, each mirrored in Chapter 18; Chapter 10 at seeds is in "(so far)" mode
    with the Week 2 line, never a gap sentence.
12. **Contents page** — exactly one CONTENTS section, beginning on page 2, with all EIGHTEEN chapter rows, in
    order, each carrying its one-line summary written for THIS member; any summary failing the swap test =
    FAIL. (22 rows with summaries run onto page 3 at the renderer's spacing — that is one contents, not two.)
13. **Chapter labels** — `CHAPTER 1` through `CHAPTER 18`, sequential, each inside its correct `PART I–IV` band.
14. **TOC resolution** — ZERO unresolved-TOC warnings on the renderer's stderr.
15. **Grounding audit ran** and its "N facts traced, M cut" tally is in the hand-off message.
16. **Grounding laws hold** — no market outside the member's scope presented as theirs (adjacents labeled, ≤3,
    Chapter 7 only); no sponsor or team named without a sourced + dated verification; no quote, anecdote,
    testimonial, stat, or biographical claim about the member that isn't in their Brain.
17. **`[confirm:]` discipline** — every marker enumerated in the hand-off; none on researched numbers in
    Chapters 7–8; more than 3 total = FAIL.
18. **Open items** — Chapter 18's rows match the actual placeholders and unset fields (no phantom items, no
    missing ones).

**Demo builds** swap checks 6, 15, and 16 for the demo checks: every production, money, ratio, count and
landscape figure tagged "(illustrative — demo)" (the DEMO BRAINS exemptions apply — dates, times, durations,
chapter/step numbers, cells under a tagged header); ZERO real source attributions; ZERO real competitor,
sponsor, team, lead-vendor, CRM, or coach names (platforms used as tools, the member's own brokerage, and the
regulator may appear); the watermark present (filename + eyebrow + the cover line **verbatim**); all eighteen
chapters filled. Every other check binds unchanged. **Real builds
get the mirror tripwire:** the string "(illustrative — demo)", a DEMO watermark, or the demo cover line
appearing ANYWHERE in a non-demo render = automatic FAIL — rebuild from the brain files.

On any FAIL: rebuild the failing chapters from the full brain-file contents and re-verify. **Never upload a
failed render. Never narrate the retry** — the member only ever sees the finished Book.

**Bounded retries — a gate may fail a build, never trap one.** Research refresh: at most ONCE per chapter per
build. TOC re-render: at most TWICE. Rebuild cycles: at most TWO — a cycle is ANY post-gate rebuild +
re-verify pass, full-book or single-chapter. A build still failing after its bounded retries **STOPS and tells
the member plainly** what's blocking (the one gate, the one chapter, what would fill it) — a visible blocker
beats an invisible loop. "Never upload a failed render" holds absolutely; "never narrate the retry" applies to
retries that succeed, not to a build that has exhausted them. Edges: **wrong file in the workspace** (raw
`════` text visible in a converted doc) = ONE corrective re-upload of the already-rendered `.docx`; **push
verify-fails** = TWO attempts per file, then `attraction-brain-sync`'s recovery path; **renderer unavailable** =
the `.md` fallback once, then stop (never install, never loop).

---

## Regeneration rules

- **When:** end of Setup (Phase 8) · after the Partner Offer is built or finalized (Week 2) · after
  `brokerage-model.md` is built · after a Prospect Radar run · after the brand kit lands in `02 · Brand` ·
  after `content-pillars.md` is written (Week 3) · after `execution-framework.md` is built · "show me my Brain" /
  "regenerate my Brain Book" · whenever the Brain materially changes (new avatar, brand change, migration).
  **A build's OWN write-backs** (its research, its config stamps) **are never a material change and never
  trigger another regenerate** — one build per trigger, always.
- **Refresh, don't fork:** same name pattern, new date, saved beside the old — newest = current; the old dated
  copies are the version history (the superseded copy may be trashed after a verified push; snapshots never).
- **Research staleness on regenerate** (check the research-log stamps in `prospect-intel.md`; refresh only
  what's stale or missing — never re-run everything blindly): footprint + movement older than **3 months** →
  refresh; where-they-gather older than **6 months** → refresh; missing → run it now. Refreshed research
  writes back first, always. A refresh **REPLACES** the adjacent-market set (cap 3).
- **The open-items page is re-derived on every build** so it always reflects the current Brain.
- After upload: push, then hand the member the direct link with the standing line — this is their book;
  everything the system knows about them, in one place.
