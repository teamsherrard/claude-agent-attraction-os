---
name: sf-gameplan
description: >
  The Short-Form Game Plan for attracting agents, Week 4's flagship. Reads the member's kit (the designed
  posts, the calls to action) and the offer's content branches first, then writes positioning for
  short-form (who they attract, the one line, the two keywords), five pillars with three angles each, the
  week — two Reels filmed and one carousel posted, every week — a 30-hook bank, the asks on the 90/10
  rule (about one post in ten carries a keyword ask; the rest build trust), a dated four-week calendar,
  what we measure, the one Monday workflow, next steps. Saved to the workspace; pillars, publishing lines
  and calendar written to the Brain. Runs inside setup or on demand; re-runs update, never rebuild; the
  Monday Week Plan keeps the calendar mapped. Trigger on: "build my short-form game plan", "my attraction
  short-form game plan", "plan my next 30 days of reels", "update my short-form game plan", "update my
  pillars", "change my cadence", "refill my attraction calendar", "turn on my calendar refill".
---

# Short-Form Game Plan — the flagship document of Week 4

The **wow** of the short-form engine: one document that hands the member their whole short-form world — who
they are to the agents they attract, five pillars with real angles, the week they can actually sustain, thirty
hooks, the two words that turn a comment into a conversation, and the next four weeks with a date on every post —
two Reels they film and one carousel they post, every week. Built from Mike's method × their Brain × their kit. The
member should feel *"this just handed me my next month."* Substance and structure, delivered as a clean doc —
never visual design.

**Mike's simplicity rulings bind every line (2026-11-22, a recorded review of this plan's output — they win over any
older line here):** the week is **two Reels and one carousel, from week one** — never a run of designed posts before
the first Reel ("they should be getting straight to camera, like, now"); **the 90/10 rule** — about one post in ten
carries a keyword ask, every other post builds trust and asks only for a follow, a save, a share or a comment on the
topic ("90% of your content not having a sales-driven, conversion-focused call-to-action… it needs to be flipped");
**one scheduled workflow**, the Monday Week Plan; **the filming block is three hours**; **less is more** in every
sentence the member reads; the document carries the teleprompter app's name (Instagram's free Edits app).

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — plain and warm, never technical, the
Brain first, three-state compliance, the quality bar. **The doctrine** is
`${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` — lazy-load the sections each phase names, never the whole file
up front. **The Brain Contract** (`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`): this skill writes
`identity/content-pillars.md` (owner), the strategy lines of `identity/publishing.md` (`Platforms` · `Cadence` ·
`Weekly mix` · `Batch day(s)` · `Keyword` · `What it opens` · `ManyChat`), `memory/content-calendar.md` (owner) and
the plan's text at `~/attraction-brain/exports/short-form-game-plan-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`;
the Brain Board's Short-Form page reads it) — nothing else in the Brain. Every write is pushed through
`attraction-brain-sync` at once (write → push → verify); every push re-renders the member's Brain Board.

**The rules that bind every line it writes (the brief of 2026-11-14 §3):** **the CTA law** — every call ask is
angled at partnering with the PERSON to get their help, free, to run the method, never the brokerage: at the join
register (`Join-gated package allowed: yes` or `unknown`) *"If you want my help running this — the lessons, the
templates, the community — partner with me and it's free. [the booking line]"*; at the open register (`no`) *"I'll
walk you through it, free, no strings."*; the method named, the brokerage never the reason, compensation never —
captions and end cards take their call line from the kit's CALLS TO ACTION table verbatim. **Scalable by design**
(doctrine §10e) — no pillar, angle, hook, caption or calendar row promises the member's time per partner: no "stand
next to me on a Saturday", no group-chat or one-to-one promise, no "I answer my phone"; the deliverables are the
recorded lessons, the templates, the community, the weekly group call only when the member already runs one (the
member's OWN batch-filming day — a Saturday, a Sunday — is their routine and is fine). **The whole method, not one
tactic** — Reels and carousels that teach draw from `## The framework`'s steps and the guide's pages; the guide is
the resource every ask points at. **Two keywords, never more** — GUIDE and the offer's `Comment keyword:`.

**Lazy-load `references/gameplan-framework.md` at Step 2** — the backbone (the nine sections, their floors, the
method per section, the calendar's date rules, the gate). The starter hook bank
(`${CLAUDE_PLUGIN_ROOT}/skills/sf-ideas/references/starter-hook-bank.md`) opens at Phase 4 and Phase 6 only,
and only where the member's own material leaves a pillar short — the rank there is law.

## Three ways it runs
- **Inside setup** (`sf-setup` Step 3 — the normal Week 4 path): the member just heard *"now I'm going to build
  your Short-Form Game Plan"*; the two keywords, the platforms and the profiles are already confirmed. **It runs in TWO
  replies, AFTER setup's one blanket question (the owner, 2026-11-15: "it should WAIT for me"; 2026-11-16: the
  questions are "blanket… the same across the board", and "we don't really need more questions because they've
  already gone through a lot of this when they were building their AI brain"; 2026-11-17, on the "off the clock"
  question: "makes no sense remove it"):** `sf-setup` Step 3a has asked the member its one question — the day and
  place they film — and saved the answer under `identity/content-pillars.md → ## In your words`; first Phases 1 to
  3 — the pillars and the week are PROPOSED from the member's Brain and that answer in one short message, saved, and the reply stops on setup's stop line (the document is NOT
  built yet);
  then, on the member's Yes (or after their changes), Phases 4 to 9 — the plan is built, saved and anchored, and
  the skill hands back to setup, which says its own stop line. ManyChat is told, never asked (Phase 5); the
  one question is setup's, never repeated here, and no other question is ever added. No menu, no "come back later".
- **On demand** — **BUILD** when no `## Game Plan anchors` block exists in `content-pillars.md`; **UPDATE** when
  one does ("update my short-form game plan", "plan my next 30 days of reels"): refresh only what changed (a new
  30-day calendar from the day after the last mapped date; new research; a pillar the member asked to change),
  keep every section they confirmed, save a new dated copy — **update, never rebuild.** "Plan my next 30 days of
  reels" is UPDATE mode scoped to section 6 (and the board, if they have one). **"Update my pillars"** is UPDATE
  scoped to section 2: the pillar the member names is rebuilt from the Brain and read back for a Yes or a change. **No
  new question is ever asked here** (the owner, 2026-11-16 and 2026-11-17) — the only question that exists is
  setup's one printed question, the filming day; the member's own wording is welcome, never asked for.
  **"Change my cadence"** is UPDATE scoped to sections 3 and 6 — stated, never asked: three becomes five only as
  the step-up the Monthly Calendar Refill or the Monthly Deep Dive proposed (five goes back to three any time);
  `Cadence:` and `Weekly mix:` are rewritten (1 · 1 · 1 at three, 2 · 2 · 1 at five) and the rows from the next
  unscripted date are remapped, said in one line.
- **Scheduled — the Monthly Calendar Refill** (task id `attraction-sf-calendar-refill`; the last Friday of the
  month, 5:00 pm; the prompt
  `${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/references/calendar-refill-task-prompt.md`, verbatim): UPDATE scoped to
  section 6, run unattended — the next thirty days from the pillars, the branches and what performed, the board
  refilled, draft-only, nothing posted; **the cadence step-up lives here** (the owner, 2026-11-14): when the log shows
  a month at three Reels a week has held (three posted each of the last four weeks), the refill proposes five in one
  line — the member's phrase ("change my cadence") flips `Cadence:` through an UPDATE run, never the refill itself; **every run
  ends with a push** so the Brain Board shows it. Switched on by the consent card's Yes (the consent card), or by phrase
  ("turn on my calendar refill" / "refill my attraction calendar" — a statement, never an offer): `list_scheduled_tasks`
  first (adopt, never a twin), else `create_scheduled_task` with the prompt verbatim, verify (present, enabled, a
  `nextRunAt`), (RETIRED as a task 2026-11-22 — never create it; the Monday Week Plan keeps the four weeks mapped; on demand only) (an
  older `(Week 3)` heading is the same block), push. "Stop my calendar refill" → the task deleted or disabled, the line
  → `paused`, push, one line; still available by its phrase. Never claim a schedule that did not save; a demo Brain
  never gets a task.

## Step 1 — Load the Brain (read; never re-ask)
Read `~/attraction-brain/brain.md` first (pull with `attraction-brain-sync` if the local copy is missing — a tool
error is never "no Brain"; only if the cloud genuinely has none: *"let's build your Attraction Brain first — say
'set up my attraction brain'"*). Then **the kit first**, and three more files; the rest open at the phase that uses
them, never earlier and never twice:
- **the newest `exports/week3-kit-*.txt`** — the kit's text (the one file the member designed in Claude Design in
  Week 3): **chapter 7, SOCIAL GRAPHIC POSTS** — the six posts (Post 1 — The guide · Post 2 — Five problems, five
  fixes · Post 3 — My story · Post 4 — What you get · Post 5 — Proof · Post 6 — Book the call), each with its
  slides, its caption and its ask — and the **CALLS TO ACTION** table (the caption's last line · the comment keywords
  · the video pop-up · the spoken line · the end card · the story · the bio link · the DM reply — the ask for the
  guide and the ask for the call, verbatim). Read once; Phase 1 takes the two CTAs from the table, Phase 5 the ask
  lines, Phase 6 the posts as each week's carousel. **None** → one warm line in the Read-this-first — the kit is built at the
  end of the offer sitting ("build my partner offer"; an offer already built → "rebuild my kit") — and the calendar
  starts with the Reels (the "Your first two weeks" line is left out); never invent a post the kit does not hold.
- `identity/compliance.md` — the first line, `Status:` (Step 1b)
- `identity/avatars.md` — the one to three types they attract, their pains in their words, what they'd need to
  hear (every angle, hook, and calendar row is for a named avatar; never "avatar" out loud — "the agents you
  attract")
- `identity/publishing.md` — the `Short-form setup:` line, `Keyword:` (the two words — `GUIDE · [the offer's
  word]`), `What it opens:`, `ManyChat:`, `Platforms`, `Cadence`, `Content board:` (what setup already decided;
  empty lines are decided here)

**Opened later, at the phase that uses them:** Phase 1 → `identity/profile.md` · `strategy.md` · `positioning.md`
· `offer.md` · `journey.md` · `memory/magnets.md` · `identity/operations.md` · Phase 2 → `identity/story-bank.md`
· `proof.md` · `brand-visual.md` · `brokerage-model.md` · `memory/ideas.md` · `memory/objections.md` ·
`memory/content-log.md` · Phase 3 → `identity/goals.md` · Phase 4 → `memory/conversations.md` (read-only) ·
Phase 5 → `identity/voice.md` · Phase 6 → `memory/intel.md` · `memory/content-performance.md` ·
`memory/content-calendar.md` · Phase 8 → `config.md`.

**Step 1b — compliance, three-state.** The Game Plan is the member's private strategy document, so it builds in
every state — but `unset` means the hooks and the calendar's posts cannot ship: put it on the plan's section 7
line (*"compliance: not set — nothing posts until it is"*) and, on demand, say so once in plain words and route to
`attraction-compliance` after delivery. **Inside setup this skill says no compliance line in chat** — the section 7
line carries it and `sf-setup`'s close says the one compliance line of the whole sitting. `set` → apply the
cardinal rules and the no-compensation rule to every line now and remind once at the end (inside setup: setup's
close does); `confirmed` → apply. "If empty, proceed" is banned.

**Demo mode** (a fictional member, for training videos): no research, no live data, every figure tagged
"(illustrative — demo)", fictional agents and wins, filename `… — DEMO — YYYY-MM-DD`, the demo workspace only.
Same structure, same gate.

## Step 2 — Read the framework and set the budget
`references/gameplan-framework.md` is the backbone. Two rules stated once:
- **Research budget: ≤ 8 searches for the whole plan**, run as ONE pass at the top of Phase 6 (what agents are
  asking and searching right now — `sf-ideas`' Step 2 method, graded HIGH / MEDIUM / EMERGING, every query
  logged with its date for the plan's Sources band). **Never the live data connection during setup** — the
  setup-time Game Plan makes zero calls to it (`shared/composio-data-engine.md`, "never during setup"); web
  search only. Research unavailable or empty → build from the Brain, label the affected rows `unresearched`,
  say so once in the Read-this-first, and put the re-run on next steps. Never invent a demand signal.
- **The Brain first, the member's one answer with it, then one stop before the document (the owner, 2026-11-15:
  "it should WAIT for me… to give direction or feedback or answers"; 2026-11-16: blanket questions only, and no
  more of them — the Brain already holds the rest).** Read `identity/content-pillars.md → ## In your words`: the
  member's answer about their week (and an `Off the clock` line, where an earlier version saved one). The pillars
  and the week are PROPOSED in one short message,
  in the shape `sf-setup` Step 3a prints — each pillar one line with where in the member's own Brain it came from
  ("from your method", "from the story you told in Week 1"), then the
  week with their filming day — and the reply ENDS on setup's stop line: *"**If that sounds like you, say Yes** and I'll build your Game Plan on it — your next thirty days of posts — or tell me what to change: a pillar, how many posts a week, or your filming day. **Your turn.**"* (a statement, not a second question — the
  sitting promised one) **No question is ever asked that assumes the member has attracted an
  agent** — what agents say to them, who they have helped, calls they have had — and none about what the Brain
  already holds. Nothing of Phase 4 onward runs until the member answers. **A change** → apply it inside the
  rules (the five OS pillars stay five; the cadence and the filming day are the member's to set), show only what
  changed, save, and stop again with the same line. ManyChat is told, never asked (Phase 5); the platforms are
  stated (Phase 3); nothing else is a question. On demand the same applies to a first BUILD: when `## In your
  words` holds no `Your week` entry the one blanket question is asked first, exactly as `sf-setup` Step 3a prints
  it and in plain chat — never on a question card, never with options (this skill then saves the answer itself);
  then the proposal, then the Yes. An UPDATE changes the one part the member named and says so.

---

## Phase 1 — Positioning for short-form (section 1 · 150+ words)
**Read now:** `identity/profile.md` (name, what they're building, brokerage, market) · `strategy.md` (the known-for)
· `positioning.md` (the one-line "why I'm here"; what stays for the private call — never in a Reel) · `offer.md`
(the UVP one-liner and the `Comment keyword:` line; **`## Content branches`** — the UVP's 5 to 7 segments with
three topics each, the foundation of Phase 2's angles and Phase 4's hooks; the header's `Join-gated package
allowed:` line — `no` keeps every CTA and caption in the open register (`yes` or `unknown` reads as the join register — the header rule above; unknown is never no): what the member teaches,
their story, their mentorship, never "join me and get X"; at `Status: seeds` the Partner Offer is Week 2 — build the
one line from `strategy.md` + `avatars.md` and label it "(draft until your offer is built)"; never demand it) ·
`journey.md` (`## Why join me` if written — the one breath that says why them) · `memory/magnets.md →
## Current magnet` (the live guide, built in Week 2; empty only when the member skipped that session) ·
`operations.md` (the booking link).
Write, in their voice: **who they attract** (the primary type, the pain in the agent's words, the mirror moment
from the journey — `02-prospect-targeting/18`: agents leave problems, not companies) · **the one line** ("[Name]
helps [agent] [outcome] through [mechanism]") · **the short-form job** in one sentence (Awareness → Recognition →
Familiarity → Trust → Curiosity → Conversation; Reels are width, stories are depth — `07-instagram/89`) ·
**the two keywords** (the `Keyword:` line setup confirmed at the profile step — `GUIDE · [the offer's word]`:
GUIDE delivers the guide, the offer's `Comment keyword:` opens the one-pager and the call — `07-instagram/87`; the
line empty → write those two from `memory/magnets.md` and `offer.md`; one of them missing → the other alone and one
line naming the sitting that writes it; never a third word, never a retired default) · **the two CTAs** — taken
verbatim from the kit's CALLS TO ACTION table: **the guide** (*"Comment GUIDE and I'll send you [the guide, in three
words]"*) and **the call** (the booking line in the CTA law's shape — join register: *"Want my help running this,
free? [the booking line]"*; open register: *"I'll walk you through it, free, no strings — [the booking line]"*; the
brokerage never the reason). No kit → the same two built from `magnets.md` and `operations.md` in the law's shape,
labeled "(from your Brain — your kit's wording replaces it)". **Why I'm building this** — the why-line from
`journey.md`, verbatim or drafted and labeled (`01-foundation-mindset/10`). Never a question box.

## Phase 2 — The five pillars, three angles each (section 2 · 400+ words) — proposed here; the stop comes after Phase 3
**Lazy-load doctrine §5–§6.** **Read now:** `identity/story-bank.md` · `proof.md` (consent column) · `brand-visual.md`
(the "leader brand vs selling brand" line) · `brokerage-model.md` (facts only; never a figure) · `memory/ideas.md`
(tags `shortform` · `story`; the `## Past content (imported)` section's `pillars:` note — how they post today —
and what they already published, so the angles never repeat it) · `memory/objections.md` · `memory/content-log.md`
(empty is normal).
**Personality comes from the Brain — it is never asked for (the owner, 2026-11-17: the "off the clock" question
is removed).** `## In your words` is read first: where an earlier version saved an `Off the clock` line, that
answer is still ANGLE ONE of Personality — its hook the member's own sentence (tidied only to be sayable in one
breath, never a claim added, a named person and any income figure left out) — and it carries `your words
YYYY-MM-DD` (printed in the document as *built on what you told me*). No such line — every member from now on —
→ the pillar is built from the sources below. Every pillar is built from the Brain by the locked order — the
member was already asked about their agents, their method, their story and their wins in Weeks 1 and 2, and is
never asked again.
**Order of sources, locked (Mike, 2026-11-02 — the UVP is the foundation of the content; all content is a branch
of it):** `offer.md → ## Content branches` FIRST — each segment's three topics become angles under the pillar
they belong to (a framework step or a tactical segment → Authority; what agents pay for versus what works →
Perspective; the story's turning point → Story; a partner's result — or, with none yet, the member's own result — → Proof; the teaching method and the routines
the member keeps → Personality) — the Brain's other signals SECOND (the story bank, proof, objections, the
captured ideas, the conversations), the starter hook bank LAST (Phase 4, only where a pillar is still short).
No `## Content branches` yet (an offer file from before 2026-11-02, or still at seeds) → the Brain's signals as
before, and one line in the Read-this-first, in plain words (*"your pillars get sharper when your offer is refined"* —
the document never says "branches"). Never invent a
pillar angle the offer does not carry. **Every summary and angle passes the scalability test** (doctrine §10e): none
promises the member's time per partner — no "stand next to me on a Saturday", no group-chat or one-to-one line, no
"I answer my phone"; the Authority angles that teach draw from `## The framework`'s steps and the guide's pages — the
whole method, not one tactic.
Build the five from the Brain — **develop, never transcribe** — each pillar: the name (exactly `Authority` ·
`Perspective` · `Story` · `Proof` · `Personality`), a two-line summary of what it is *for this member*, and
**three angles** — each a working hook (one breath), the agent it is for, the pain it answers, and what it carries
(a content-branch topic, a story-bank hook, a win with consent, a routine they keep, a teach from the known-for — printed
in the document as "built on …", never the word "carries"): Authority = the niche
dissected into tactical pieces, the tip of the iceberg (`06-content-framework/37`, `07-instagram/88`) ·
Perspective = the takes they hold, the myths to bust, the questions agents ask — never about a named brokerage or
person (`07-instagram/88`, `03-model-positioning/13`) · Story = the journey's turning points with "who relates to this", the
former brokerage never named (`06-content-framework/39`, `/40`) · Proof = agents already helped (consent on file;
otherwise first name or initials), the weekly call, the training, the events — "it's not us saying our culture is
incredible, you're seeing it" (`06-content-framework/38`); **no agent wins on file — the normal state of a member attracting for the first time (the owner, 2026-11-16)** →
Proof is built from what IS theirs: their own results in `proof.md` (their production, their awards, their years),
the method working in their own business, and what they are building in the open (the first lesson recorded, the
first open house run their way) — three real angles, printed *your own results for now — agent wins join as they
come*; never "you have no proof", never an invented agent or win, never a gap sentence in the document; the
upline's proof may be added only labeled as the upline's · Personality = passions, routines, family lines they are willing to share (`07-instagram/88`,
`/89` — the patio-beer test). **Personality is never asked for** (the owner, 2026-11-17): it is built from
`identity/profile.md → Outside real estate:` when that line is filled, then the profile's "before real estate" line,
the journey, the story bank and the WHY. **The Brain holds little for Personality** → never a question: draft the
three angles from what it does hold and label them *"(a first draft — tell me what to change)"*; on demand ("update
my pillars") the pillar is rebuilt from the Brain and read back; nothing is asked.
**State the five in one short message** — setup's proposal shape, each pillar with where in the member's Brain it
came from (*"• **Story** — [one line] · from the story you told in Week 1"*; Personality: *"from what you
told me about your life outside real estate"*) — it runs
straight into Phase 3's line (the week), and after that line the reply STOPS and waits for the member (the rule
above); a member who names a change gets it applied before anything is built. Then **write `identity/content-pillars.md` now** in the contract's shape
(the template's header lines kept and filled · the one-line anchors · the five sections headed exactly by the
pillar names, three angles each · **`## In your words`, kept exactly as it was written** · `## Game Plan
anchors` · `## Weekly mix` · `## Hooks bank`), **push, verify.**
*"Saved — your pillars are in your Brain."* — **on demand only; inside setup this line is not said** (setup's
proposal is the only thing the member reads here, and it ends on the stop line). (Inside setup the header lines `Cadence` and `The two CTAs` line 2
fill at Phases 3 and 5 of this same run.)

## Phase 3 — The week (section 3 · 150+ words) — proposed; then the STOP
**Lazy-load doctrine §7, §9b, §9d.** **Read now:** `identity/goals.md` (the hours per week committed in Week 1 —
never ask for hours the Brain holds) · `strategy.md` (`Constraints / capacity`, already open) · `operations.md`
(`Filming window:`, already open).
**The week is fixed by Mike (2026-11-22): two Reels the member films and one carousel they post — three posts,
every week, from week one.** Not "three to five", not "five the step-up", not a run of designed posts first: *"get
them posting three times a week with two reels and one carousel, just to get into momentum."* A member who names
another number gets it — Reels fill it, the one carousel a week stays — said in one line; nothing proposes more.
**The two Reels** rotate the pillars: each week one that teaches or takes a stand (Authority or Perspective) and
one that shows who they are (Story, Proof or Personality); across four weeks every pillar at least once, no pillar
twice in a week. **The carousel** is a kit post while the kit's six last (one a week, in the kit's order — the
guide, five problems, my story, what you get, proof, book the call), then a carousel this plan outlines from the
guide's pages and the member's method. No kit → every week's carousel is outlined here and written by the Monday
Week Plan; one warm line names "rebuild my kit" in the Read-this-first, nowhere else.
**The formats, one line each in the document:** the talking-head Reel (30–60 s, hook → value → one ask, raw is
better than polished — `07-instagram/90`; filmed on their phone in Instagram's free Edits app, teleprompter built
in) · the carousel (the no-filming post; a LinkedIn document post when the member attracts team leaders or
broker-owners) · the green screen is **not a format of the week** — at most one industry story a week, inside the
Monday package, only when there is a good one (industry news, lead generation, new agents struggling — never a
brokerage headline; Mike, 2026-11-22) · stories are **one optional line**, never a routine in the chat: *"Stories
are the bonus — one a day when you feel like it; ideas are in section 5."*
**The platforms — stated, never asked** (the owner, 2026-11-14): the doc's line reads *"Platforms: Instagram and
Facebook, both — every Reel and every carousel; LinkedIn for the carousels when team leaders are among the agents
you want to attract; TikTok and YouTube Shorts take the same video any time you want more reach"* (LinkedIn on only
when `identity/avatars.md` includes team leaders or broker-owners, otherwise one line that it stays off).
**The filming day — the member's own answer in `## In your words`** (the day and the place they named); only when
that answer was skipped, fitted from the filming window, else Saturdays — said in one line. **The honest block is
three hours** for the two Reels (Mike: a beginner takes longer than an hour); the document says three hours wherever
it names the time, never one or two. **The 15-minute routine** (same time every day: reply to every comment with a
question, answer every DM the same day, five real comments on agents' posts in the lane, never a negative one) is
one line in the document.
Proposed, in one line: *"Your week: two Reels you film and one carousel you post — three posts, every week,
starting this week. Filming on [day]s."* **Then the stop line, and the reply ends** (inside setup, `sf-setup` Step
3a's line; on demand the same words): *"**If that sounds like you, say Yes** and I'll build your Game Plan on it —
your next four weeks, with a date on every post — or tell me what to change: a pillar, or your filming day. **Your
turn.**"* The lines below are written now (they are the proposal on file); a change at the stop rewrites them
before Phase 4 starts. Then write `Platforms (priority order): Instagram Reels · Facebook Reels (always, both) ·
LinkedIn (carousels, when attracting team leaders) · TikTok / YouTube Shorts (optional reposts)` (the locked value —
`LinkedIn off` in its clause when the avatars hold no team leaders; setup normally wrote it already — never rewrite
a filled line) · `Cadence: 3/week (2 Reels + 1 carousel)` · `Weekly mix: two Reels — one that teaches or takes a
stand, one that shows who you are — and one carousel` · `Batch day(s):` to `publishing.md` (the source), mirror
`Cadence` and `Platforms` into `content-pillars.md`'s header lines and `## Weekly mix`, and write the filming day
and time to the single `Filming window:` line of `identity/operations.md` (this plugin's one write there, by the
Brain contract's permission; the YouTube plugin reads it by name) → push.

## Phase 4 — The hook bank (section 4 · 250+ words · exactly 30)
**Lazy-load doctrine §7 (the hook) and §9b.** **Read now:** `memory/conversations.md` (read-only — the questions
agents actually asked; the richest source there is).
Thirty hooks, **six per pillar**, each under 12 words, sayable in one breath, the first word doing the work; no two
share a shape (question · contrarian · number/stakes · mistake · callout · curiosity-gap); never "stop scrolling",
never "hey guys", never credentials first. **Order of sources, locked:** the member's own angles from Phase 2
(built on the UVP's content branches, the framework's steps and the guide's pages — the whole method, not one
tactic) and their captured ideas first → the Brain's signals (conversations,
objections, the avatar's "biggest problem in their words") → **then** the starter hook bank (`sf-ideas/references/starter-hook-bank.md`, opened only now, only where a
pillar is still short; every seeded line marked `starter`, placeholders swapped per the bank's rules, never
presented as something agents are asking). Label each hook with its pillar, the agent it is for, and the rung it
would end on. Append the thirty as one dated block under `## Hooks bank` in `content-pillars.md` (the section
`sf-ideas` also appends to; newest block last) — push at Phase 10 with the rest. **In the document the bank is shown
in two parts** (assembled at Phase 10, once the calendar is dated): first **THE HOOKS FOR YOUR DATED POSTS** — one line
per dated post in date order (the date written "Tue, Nov 17" · the hook · who it is for); then, under the plain heading
**More hooks when you need them**, the rest of the thirty, grouped by pillar, each with who it is for and its ask in
words ("Comment GUIDE" · "Comment [WORD]" · "Follow"). The word "rung" never appears in the document.

## Phase 5 — CTAs and the comment-to-DM flow (section 5 · 150+ words)
**Lazy-load doctrine §8.** **Read now:** `identity/voice.md` (the asks sound like them).
State the ladder once — Follow / save / share → Comment → DM → Resource → Conversation → Call — and the rule of
one: one post, one ask, said on camera at the end, written as the caption's last line, pinned as the first
comment. **The two CTAs of this section are the guide and the call** (the brief's §3–§4), both
verbatim from the kit's CALLS TO ACTION table: **GUIDE** → the guide, instant (the Comment and Resource rungs); the
offer's **`Comment keyword:`** → the one-pager and the invitation to talk (the DM and Conversation rungs); **the
call line** in the CTA law's shape — *"If you want my help running this — the lessons, the templates, the
community — partner with me and it's free. [the booking line]"* at the join register, *"I'll walk you through it,
free, no strings."* at the open register. **The 90/10 rule — one rule everywhere (Mike, 2026-11-22; house rules #13):** *"90% of your content not having a
sales-driven, conversion-focused call-to-action."* **About one post in ten carries a keyword ask** — `Comment · GUIDE`
for the guide, or the offer's word with the call line in the law's shape; in a four-week plan of twelve posts that
is ONE post: the kit's guide carousel in week one (no kit → the Reel that teaches the guide's first page, in week
two), and when the kit's "book the call" post comes round it is the next one. **Every other post builds trust and
asks only for a follow, a save, a share or a comment on the topic** — Mike's example: *"follow if you want to learn
how to scale your business without having to pay for leads."* Never two asks on one post. The model itself is
explained on a call, never in a caption or a DM (doctrine §8, `02-prospect-targeting/19`: say as little as you have
to in text). **The ask map by pillar:** every pillar → a follow, a save, a share or a comment on the topic, in the
member's voice (Authority → *"save this for your next open house"* · Perspective → *"follow for the next one"* ·
Story → *"comment if you've been there"* · Proof → *"share this with an agent who needs it"* · Personality →
*"follow for the next one"*); the one keyword post of the month carries `Comment · GUIDE` (or the call line). Five
spoken ask lines in the member's voice, one per pillar, on that map; never a third word. **ManyChat — told, never asked (the owner, 2026-11-14); the section's ManyChat line reads, in
this shape:** *"ManyChat is how your keyword[s] answer[s] [itself | themselves]. Set it up this week: install ManyChat (the free
plan starts you — upgrade only if ManyChat itself asks you to for Instagram automations), import Mike's templates
from your Materials folder, put GUIDE [and [WORD]] in with your links. Say 'set up my ManyChat' and I'll write out the
steps. You don't connect ManyChat to Claude: nothing here needs its connector or a paid plan for it. Until it's live,
reply by hand from your DM bank."* Never a question, never an opt-out, never "connected". Write
`Keyword:` (if this run set it) · `What it opens:` (GUIDE → the guide's title · [WORD] → the one-pager and the call)
to `publishing.md`; the `ManyChat:` line — this plan writes it only when it is still empty, as `not yet — set it up
this week`; from there it is `sf-comment-to-dm`'s (Job E, which runs only when the member asks — "set up my ManyChat" —
and never inside setup: the owner, 2026-11-17; `set up YYYY-MM-DD` on the member's word that it is live); mirror the two words and what each opens into
`content-pillars.md`'s `The two CTAs` line 2. The full CTA bank, the DM copy bank and the ManyChat steps stay
`sf-comment-to-dm`'s — one line at the end of the section: *"the ask lines and your DM replies: say 'my keyword
sheet'; the ManyChat steps: 'set up my ManyChat'."*

## Phase 6 — The four-week calendar (section 6 · 300+ words · twelve dated rows: four weeks × one carousel + two Reels)
**Lazy-load `${CLAUDE_PLUGIN_ROOT}/skills/sf-talkinghead/references/calendar-guide.md`** (the calendar's rules —
no story twice; no pillar twice in a week; one ask on every post by the 90/10 rule; no Reel dated before the day
after the filming day that films it). **Read now:** `memory/content-performance.md` (what worked — skip if empty) ·
`memory/content-calendar.md` (UPDATE mode: the rows already mapped — the new window starts the day after the last
mapped date; rows at `Scripted` or later are never rewritten).
**The shape of every week — Mike, 2026-11-22: "Record these two videos this week, and post this carousel. That's
it."** Three rows a week, four weeks, twelve rows:
- **The carousel** — the week's first posting day (Monday unless the member's week says otherwise): a kit post while
  the six last, one a week in the kit's order (`format` `carousel` for posts 1–3, `graphic` for posts 4–6 — a
  single designed image; `pillar` the guide and the five problems → Authority · my story → Story · what you get and
  proof → Proof · book the call → Proof; `working title` the post's name; `hook` the post's slide 1 or headline,
  verbatim; `carries` `kit post n`; Status **`Ready to Post`** — designed in Week 3, nothing to draft or film, posting
  flips it to `Published`); after the six, or with no kit, a carousel this plan outlines (`format` `carousel`,
  Status `Idea`; the Monday Week Plan writes its slides).
- **The two Reels** — the two posting days after the filming day that films them (the filming day is the member's own
  answer; a Reel's publishing date is never earlier than the day after it): `format` `talking head`; one that
  teaches or takes a stand (Authority or Perspective), one that shows who they are (Story, Proof or Personality);
  across the four weeks every pillar at least once, the member's own method and story first.
**The asks — the 90/10 rule (Phase 5):** the kit's guide carousel (week one) carries `Comment · GUIDE`; **every other
row's CTA cell is a soft ask** — `Follow` · `Save` · `Share` · `Comment · [the topic]` — in the member's words; a
kit post whose printed ask is a keyword or the call keeps it only when it is the month's one keyword post; otherwise
its caption's last line is the soft ask (the kit's slides are never redesigned). Never two asks in one cell.
**Say this once, then run the pass:** *"Give me a few minutes — I'm checking what agents in your lane are asking
right now; about [N] searches, then your calendar."* ([N] = the real number inside the ≤ 8.) Demo mode: no line,
no searches. Fill the Reels with `sf-ideas`' method and order: **the UVP's content branches, the framework's steps
and the Brain's own stories and systems first** (the branches' topics, the guide's pages, the story bank, the proof
with consent, the member's captured ideas and this month's objections), **fresh research second** (the graded
findings, each cited by number in the Sources band), **the starter bank last** (`starter`, only to fill a short
pillar). **The Personality Reel is built from the Brain, never from a question** (where an earlier version saved an
`Off the clock` line under `## In your words` its hook is that sentence and its `Carries` cell `your words
YYYY-MM-DD`). Every row: `#` · **date** (real calendar dates, never "Day 1") · day · format · pillar · working
title · hook (one breath) · CTA (one ask) · what it carries · **System ID** (`sf-YYYY-MM-DD-NN`, the publish date
and the row number — the board finds the card by it). No row promises the member's time per partner (doctrine
§10e). **Say the count plainly:** *"twelve posts this month: eight Reels to film, four carousels to post"* (no kit →
*"…four carousels, written for you each Monday"*).
Then **THE FILMING PLAN** — one line per week: the day, the two Reels that film together (same outfit, same spot),
*about three hours*; the app: *"Film on your phone in Instagram's free Edits app — it has a teleprompter built in:
paste the script, press record, read."* — and **THE TWO TO FILM FIRST** (week one's Reels, one line each on why).
**Stories** are one optional line here, never rows (*"Stories are the bonus — one a day when you feel like it."*).
**In the document the calendar is a five-column table the member reads at a glance**, one band per week —
**WEEK 1 (the week of [Mon, Nov 17])** and so on: `Date` (written "Tue, Nov 17", never 2026-11-17) · `What` (the
format and the working title — "Carousel — The guide", "Reel — The year I almost quit") · `The hook` · `The ask`
(in words: "Follow" · "Save this" · "Share this" · "Comment [the topic]" · "Comment GUIDE" on the one post) ·
`Status`. The row number, the weekday column, the pillar, what a row is built on and the System ID stay in the
Brain file and never appear in the document — with one exception the member should see: **a row built on their
own answer shows "(your words)" after its working title** in the `What` column.
Write **`memory/content-calendar.md`** in the contract's locked shape — the eleven columns `# | Date | Day | Format |
Pillar | Working title | Hook | CTA | Carries | Status | System ID`, untouched; only the document's table is the five
member-facing columns — (BUILD: create it from the header — and when the file is already there because the YouTube
System created it for a member who ran Week 5 first, keep its three `(YouTube)` sections exactly as they are and
write only the window line and the short-form table above them; UPDATE: append the new window below the old, never
rewriting a row at `Scripted` or later), push at Phase 10. Calendar rows are not logged to `content-log.md` — a row
enters the log when a piece is scripted (the Monday Week Plan or a content skill writes it); a kit post's row enters
the log when it goes out.

## Phase 7 — What we measure (section 7 · 100+ words)
The section opens *"Any time you ask 'how's my content doing', and each month in your deep dive, five numbers: …"*
(the owner, 2026-11-14 — no weekly note): people who saw you · Reels posted of the cadence · story days of seven ·
keyword comments · conversations started (from the log) — plus calls booked from content once the funnel ledger
exists; the member's own median is the benchmark, never a borrowed one; growth is today minus the last baseline. One
line on where the numbers come from (live data once connected after setup, the posting tool, or "add my numbers"
screenshots — never estimated, "not available" is a real value). The compliance line from Step 1b. Views are not
the score; conversations are.

## Phase 8 — Your Monday Week Plan (section 8 · 60+ words)
**Read now:** `config.md` (the `## Short-Form (Week 4)` block — an older `## Short-Form (Week 3)` heading is the
same block — its `Week Plan task:` line and `Email me:`; a missing block = the workflow is switched on at the end of
setup). **ONE workflow (Mike, 2026-11-22: "one scheduled task a week… here's your weekly package")**, in plain
words: *"Your Monday Week Plan — every Monday, 7:00 am: your week in one package — the scripts for your two Reels,
the cards you read from while you film, your carousel's caption, and one industry story to react to when there's a
good one[, all on your board]. It only drafts; nothing posts on its own."* Then the email line as a statement —
*"I'll email you a short note when it's ready"* (`Email me: yes`), or *"your note waits in Cowork"* (`no (no mail
connected)`). State its status honestly from `config.md`: *on since [date]* · *switched on at the end of setup* (no
block yet) · *stopped* (`paused`) · *say the word any time* (`later`). **Nothing else is listed** — not the five
by-phrase workflows, not the tasks retired on 2026-11-14 and 2026-11-22 (Batch Prep, the Wednesday news watch, the
monthly refill — their work rides inside the Monday package). Nothing posts, sends, schedules, or moves a stage on
its own.

## Phase 9 — Next steps (section 9 · 40+ words)
Three short numbered lines, the same inside setup and on demand (Mike, 2026-11-22: "we should just stop here"):
1. *Film your two Reels on [day] — about three hours. On your phone, in Instagram's free Edits app: it has a
   teleprompter built in — paste the script, press record, read.*
2. *Post your carousel on [the day, in words].* (no kit → *"…its slides come in your Monday package; say 'rebuild
   my kit' for designed ones"*)
3. *When a Reel is filmed, open a new chat and say "edit my reel" — your AI Editing Studio edits it.*
Then, one line and only where it applies: compliance `unset` → *"Before anything is posted, say 'set up my
attraction compliance'."* Nothing else is listed here — no ManyChat (section 5 has its one line), no phrases, no
board or keyword-sheet lines.

## Phase 10 — Gate, assemble, deliver, save, anchor, hand off
1. **The gate (hard — fix, never ship past it):** every section present at its floor (1 · 150 · 2 · 400 · 3 · 200 ·
   4 · 250 · 5 · 150 · 6 · 400 · 7 · 100 · 8 · 100 · 9 · 50 words) · twelve dated calendar rows — four weeks, each one carousel (a kit post at `Ready to Post` while the six last) and two Reels, no run of designed posts before the first Reel · five pillars with three angles each · thirty hooks, six per pillar · **only the two keywords** anywhere
   (GUIDE and the offer's word) — present in section 1 and section 5; every row's CTA is one ask · **the 90/10 rule kept** (ONE keyword ask in the
   twelve — Comment GUIDE on the kit's guide carousel, or the call line on the kit's call post when its week comes;
   every other row a follow, a save, a share or a comment on the topic; never two asks on one row) · **every call
   ask in the CTA law's shape** (the person · their help · free · to run the method; the brokerage never the reason)
   · **no line promising the member's time per partner** (no "stand next to me on a Saturday", no group-chat or
   one-to-one line) · no compensation, split, cap, stock, rev-share, or income figure anywhere · no brokerage named
   other than the member's own, and that one only as `compliance.md` allows · no `[bracket]` placeholder · no
   negative word about any brokerage or person · every named agent consented · every number sourced or tagged
   "(illustrative — demo)" · "Week 4" wherever the week is named, never "Week 3" for short-form work · section 3's
   platform line, section 5's ManyChat line, section 6's two bands, section 7's opening and section 8's ONE
   workflow (Mike, 2026-11-22) — no weekly note, no engagement list, no list of extras, ManyChat told once · **dates that
   make sense** — no Reel dated earlier than the day after the filming day that films it; every week holds two Reels
   and one carousel · **the document in member-facing words** —
   READ THIS FIRST carries "Every week: film two Reels on [day] — about three hours — and post one carousel. That's
   it." right after its opening sentence; the filming plan names Instagram's Edits app and its teleprompter; the
   time is three hours wherever it is named; the calendar is the five columns Date · What · The hook · The ask
   · Status, its dates written "Tue, Nov 17"; the hook bank shows the dated posts' hooks first and the rest under
   "More hooks when you need them"; NEXT STEPS is the three lines in order; and none of "rung", "carries", "branch",
   "the OS default", "the kit's CALLS TO ACTION table, verbatim", a System ID or a date written 2026-11-17 appears
   anywhere in it. Count before delivering.
2. **Assemble** on the Short-Form Game Plan skeleton in `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` §5a —
   the title and meta line, READ THIS FIRST (its opening sentence — the verdict; then the one plain line *"Every week: film two
   Reels on [day] — about three hours — and post one carousel. That's it."*; then the first Reel to film and the
   filming day), the nine sections — section 4 in its two parts, section 6 in the five member-facing columns by
   week, section 9 as the three lines in order —, the SOURCES band (every search and page read, dated; `starter` and `unresearched`
   rows counted; demo → "nothing searched"), the closing paragraph (consistency before cleverness — "be consistent,
   not complicated", `07-instagram/89`), the stamp per house rules #4 (byline and footer only).
3. **Deliver in chat — on demand only; inside setup nothing is said here** (`sf-setup` Step 3b's own hand-over
   lines are the only ones the member reads — never the inventory twice, never the location twice) — a warm
   summary, not the doc: *"Here's your Short-Form Game Plan — two Reels and one carousel a week, filming on
   [day], with a date on every post for the next four weeks. It's in your workspace under Content → Short-Form."*
4. **Save** per the output standard: render through `shared/render_doc.py` and upload as
   **`[Name]'s Short-Form Game Plan — YYYY-MM-DD`** to `03 · Content/Short-Form/` (the bucket root, not the month
   folder; dated — newest is current; demo: `… — DEMO — YYYY-MM-DD`). **Keep the text** at
   `~/attraction-brain/exports/short-form-game-plan-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`; the Brain
   Board's Short-Form page reads the two keywords, the five pillars and this week's rows from it). A save that fails:
   say it is NOT saved, keep the plan visible in chat, retry once, stop.
5. **Anchor and push (write → push → verify, one step):** `content-pillars.md` — the `## Game Plan anchors` block
   (plan date · doc link · cadence `3/week (2 Reels + 1 carousel)` · mix · the two keywords · calendar window
   `YYYY-MM-DD → YYYY-MM-DD` · research budget used) and the hooks block; `publishing.md` — the strategy lines from Phases 3 and 5 and, inside setup,
   `Short-form setup: game plan done`; `memory/content-calendar.md` — the window; the exports text. Push via
   `attraction-brain-sync`, verify — **the push re-renders the Brain Board**.
6. **Hand off.** Inside setup → return to `sf-setup` Step 3b, which hands the plan over and says its stop line (the
   board is NOT started in this reply; setup's close names the Brain Board). On demand → *"Your Brain Board is updated. Say 'map my next 30 days' and these thirty days go onto your
   content board; 'script my first attraction reel' scripts your first Reel."*

## Quality checklist
- [ ] Brain read — the kit first (chapter 7's six posts and the CALLS TO ACTION table), three files at Step 1, the
      rest at their phase, nothing read twice, nothing re-asked; demo mode honored if asked; the live data connection
      never touched during a setup-time run
- [ ] Compliance three-state read first; `unset` named once on section 7 and routed after delivery, never blocking
      the private plan
- [ ] In setup: the pillars and the week PROPOSED in one short message and the reply stopped on the stop line; the
      plan built only on the member's Yes (or after their changes); ManyChat told in the owner's shape, never
      asked; the platforms stated, never asked
- [ ] Section 1: who they attract, the one line, the two keywords, the two CTAs verbatim from the kit's table (the
      guide; the call in the CTA law's shape), the why — drafted and labeled where the Brain is empty, never a
      question box
- [ ] `## In your words` read first: the filming day is the one they gave; Personality built from the Brain and
      never asked for (an `Off the clock` line from an earlier version still leads it, marked `your words`); no
      question beyond setup's one was asked, and none that assumes they have attracted an agent; the
      section kept exactly through every rewrite
- [ ] Five pillars, exact names, three angles each, developed from the UVP's content branches and the framework's
      steps first, then the Brain — stories from the bank, proof with consent, the former brokerage unnamed; no
      angle promising the member's time per partner; the branches' absence said once when the offer predates them;
      `content-pillars.md` written and pushed at once (no Yes line)
- [ ] The week stated as Mike fixed it — two Reels and one carousel, every week, from week one (Mike, 2026-11-22);
      the filming day the member's own answer; three hours wherever the time is named; the Edits app and its
      teleprompter named in the filming plan; the 15-minute routine one line (never a task); stories one optional line;
      the platform line in the owner's shape (Instagram and Facebook both; LinkedIn only for team leaders; TikTok and
      Shorts as optional reposts)
- [ ] Thirty hooks, six per pillar, under 12 words, shapes varied, the member's own first, `starter` marked
- [ ] The ladder, the ask map (every pillar a soft ask), the five ask lines in the member's voice, the call line in
      the law's shape, the 90/10 rule (ONE keyword ask in the month's twelve posts; never two asks on one post), what
      each word opens; the ManyChat line in the owner's
      shape ("you don't connect ManyChat to Claude"; set it up this week; no opt-out)
- [ ] Twelve dated rows — four weeks, each a carousel (a kit post at `Ready to Post` while the six last) and two
      Reels, one band per week; the calendar-guide rules kept; System IDs written; the filming plan (three hours, the
      app), the two to film first;
      research ≤ 8, cited, dated, or `unresearched` labeled with the re-run on next steps; no Reel dated before the
      day after the filming day that films it;
      the document's table in the five member-facing columns (the Brain file's eleven untouched)
- [ ] Sections 7–9 present; section 7 opens on "how's my content doing" and the deep dive (no Friday); section 8
      names the four switched-on workflows, the five extras in one sentence and the email note as statements, the
      statuses read from `config.md`, never assumed; section 9 is the four steps in order (post the six designed posts
      on their dates · film on the batch day · "edit my reel" in a new chat · ManyChat this week, "set up my ManyChat")
- [ ] READ THIS FIRST carries "Your first two weeks: post the six you already have designed — nothing to film yet."
      right after its opening sentence; the hook bank shows the dated posts' hooks first, the rest under "More hooks
      when you need them"; no internal word in the document ("rung", "carries", "branch", "the OS default", "the kit's
      CALLS TO ACTION table, verbatim")
- [ ] The gate passed and counted; saved dated to `03 · Content/Short-Form`; the text kept in `exports/`; anchors,
      hooks, publishing lines, and the calendar pushed and verified (the Brain Board re-rendered); handed back to
      setup or to the first Reel
- [ ] Week 4 everywhere; never a skill id or a file path in a line the member reads
