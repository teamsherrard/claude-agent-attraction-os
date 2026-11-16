---
name: sf-gameplan
description: >
  The Short-Form Game Plan for attracting agents, Week 4's flagship. Reads the member's kit (the six
  designed posts, the calls to action) and the offer's content branches first, then writes positioning
  for short-form (who they attract, the one line, the two keywords), five pillars with three angles
  each, the mix and cadence, a 30-hook bank, the comment-to-DM flow (ManyChat told, never asked), a
  dated 30-day calendar that opens with the six kit posts ("post, don't make") then the Reels, what we
  measure, the scheduled workflows, next steps. Saved to the workspace; pillars, publishing lines and
  calendar written to the Brain. Runs inside setup or on demand; re-runs update, never rebuild; the
  Monthly Calendar Refill (the last Friday) is its scheduled mode. Trigger on: "build my short-form
  game plan", "my attraction short-form game plan", "plan my next 30 days of reels", "update my
  short-form game plan", "update my pillars", "change my cadence", "refill my attraction calendar",
  "turn on my calendar refill".
---

# Short-Form Game Plan — the flagship document of Week 4

The **wow** of the short-form engine: one document that hands the member their whole short-form world — who
they are to the agents they attract, five pillars with real angles, the week they can actually sustain, thirty
hooks, the two words that turn a comment into a conversation, and the next thirty days with a date on every post —
opening with the six posts they already have designed. Built from Mike's method × their Brain × their kit. The
member should feel *"this just handed me my next month."* Substance and structure, delivered as a clean doc —
never visual design.

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
  replies, AFTER setup's interview (the owner, 2026-11-15: "it should WAIT for me" · it has to "feel almost like an
  interview"):** `sf-setup` Step 3a has asked the member its four questions and saved the answers under
  `identity/content-pillars.md → ## In your words`; first Phases 1 to 3 — the pillars and the week are PROPOSED
  from those answers in one short message, saved, and the reply stops on setup's stop line (the document is NOT
  built yet);
  then, on the member's Yes (or after their changes), Phases 4 to 9 — the plan is built, saved and anchored, and
  the skill hands back to setup, which says its own stop line. ManyChat is told, never asked (Phase 5); the
  interview's questions are setup's, never repeated here. No menu, no "come back later".
- **On demand** — **BUILD** when no `## Game Plan anchors` block exists in `content-pillars.md`; **UPDATE** when
  one does ("update my short-form game plan", "plan my next 30 days of reels"): refresh only what changed (a new
  30-day calendar from the day after the last mapped date; new research; a pillar the member asked to change),
  keep every section they confirmed, save a new dated copy — **update, never rebuild.** "Plan my next 30 days of
  reels" is UPDATE mode scoped to section 6 (and the board, if they have one). **"Update my pillars"** — first looks at `## In your words`: an entry that reads `skipped` is asked now, ONE
  question, in `sf-setup` Step 3a's wording with its seed; the answer replaces the entry, becomes angle one of
  its pillar marked `your words`, and the reply says what it became. Then it is UPDATE
  scoped to section 2 (the pillar the member names; where the Brain is empty, one plain question at a time).
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
  `nextRunAt`), write `Calendar Refill task: attraction-sf-calendar-refill` to `config.md → ## Short-Form (Week 4)` (an
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
  lines, Phase 6 the six posts as rows 1–6. **None** → one warm line in the Read-this-first — the kit is built at the
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
- **The member's answers first, then one stop before the document (the owner, 2026-11-15: "it should WAIT for
  me… to give direction or feedback or answers" · the sitting has to "feel almost like an interview").** Read
  `identity/content-pillars.md → ## In your words` before anything else: the member's answers to setup's
  interview (the question agents ask them · the one step · off the clock · their week). The pillars and the week
  are PROPOSED from them in one short message, in the shape `sf-setup` Step 3a prints — each pillar one line, the
  member's own words shown inside the pillars they answered for, then the week with their filming day — and the
  reply ENDS on setup's stop line: *"**Does that sound like you?** Say **Yes** and I'll build your thirty-day plan
  on it — or tell me what to change: a pillar, how many posts a week, your filming day, or an answer you'd give
  differently. **Your turn.**"* Nothing of Phase 4 onward runs until the member answers. **A change** → apply it inside the
  rules (the five OS pillars stay five; the cadence and the filming day are the member's to set), show only what
  changed, save, and stop again with the same line. ManyChat is told, never asked (Phase 5); the platforms are
  stated (Phase 3); nothing else is a question. On demand the same applies to a first BUILD: when `## In your words` is absent the four questions are asked first,
  one per reply, by `sf-setup` Step 3a's table and rules (this skill then saves the answers itself); then the
  proposal, then the Yes. An UPDATE changes the one part the member named and says so.

---

## Phase 1 — Positioning for short-form (section 1 · 150+ words)
**Read now:** `identity/profile.md` (name, what they're building, brokerage, market) · `strategy.md` (the known-for)
· `positioning.md` (the one-line "why I'm here"; what stays for the private call — never in a Reel) · `offer.md`
(the UVP one-liner and the `Comment keyword:` line; **`## Content branches`** — the UVP's 5 to 7 segments with
three topics each, the foundation of Phase 2's angles and Phase 4's hooks; the header's `Join-gated package
allowed:` line — `no` or `unknown` keeps every CTA and caption in the open register: what the member teaches,
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
**The member's own answers lead (the owner, 2026-11-15).** `## In your words` is read first: each answer is ANGLE
ONE of its pillar — "the question agents ask you" under Perspective, "the one step" under Authority, "off the
clock" under Personality — its hook the member's own sentence (tidied only to be sayable in one breath, never a
claim added, a named brokerage or person and any income figure left out), and it carries `your words YYYY-MM-DD`
(printed in the document as *built on what you told me*). A skipped answer leaves its pillar to the sources below.
The other angles follow the locked order.
**Order of sources, locked (Mike, 2026-11-02 — the UVP is the foundation of the content; all content is a branch
of it):** `offer.md → ## Content branches` FIRST — each segment's three topics become angles under the pillar
they belong to (a framework step or a tactical segment → Authority; what agents pay for versus what works →
Perspective; the story's turning point → Story; a partner's result → Proof; the teaching method and the routines
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
incredible, you're seeing it" (`06-content-framework/38`); zero proof → one honest line and the upline's proof
labeled as the upline's · Personality = passions, routines, family lines they are willing to share (`07-instagram/88`,
`/89` — the patio-beer test). **Personality is the interview's third question** ("off the clock") — its answer is angle one. **Skipped, and the
Brain holds nothing for Personality** → never a second ask: draft the three angles from what the Brain does hold (the profile's "before real estate" line, the journey,
the WHY) and label them *"(draft — tell me what you do off the clock and I'll sharpen these)"*; on demand ("update my
pillars") one plain question at a time fills them.
**State the five in one short message** — setup's proposal shape, the member's own words shown inside the pillars
they answered for (*"• **Perspective** — [one line] · your words: "[the question]""*) — it runs
straight into Phase 3's line (the week), and after that line the reply STOPS and waits for the member (the rule
above); a member who names a change gets it applied before anything is built. Then **write `identity/content-pillars.md` now** in the contract's shape
(the template's header lines kept and filled · the one-line anchors · the five sections headed exactly by the
pillar names, three angles each · **`## In your words`, kept exactly as the interview wrote it** · `## Game Plan
anchors` · `## Weekly mix` · `## Hooks bank`), **push, verify.**
*"Saved — your pillars are in your Brain."* (Inside setup the header lines `Cadence` and `The two CTAs` line 2
fill at Phases 3 and 5 of this same run.)

## Phase 3 — The format mix and the weekly cadence (section 3 · 200+ words) — proposed; then the STOP
**Lazy-load doctrine §7, §9b, §9d.** **Read now:** `identity/goals.md` (the hours per week committed in Week 1;
its `Content:` line defers to this plan — never ask for hours the Brain holds) · `strategy.md` (`Constraints /
capacity`, already open) · `operations.md` (`Filming window:`, already open).
Propose, from those: **the number — three Reels a week is the default for the first month** (the owner, 2026-11-14: twenty posts at once overwhelms; Mike's own path is three to five, working up to five — `07-instagram/88`); five only when the member names it — the step to five is proposed by the Monthly Calendar Refill and the Monthly Deep Dive once a month at three has held, never here; honest capacity outranks ambition · **the mix** — *"one attraction · one authority · one story a week, stories every day"* at the default three
(2 · 2 · 1 only at five) — the cohort's standard, not a lesson of Mike's: never attributed to him, and printed in plain
words (the document never carries the label "the OS default"; attraction = Proof + Personality, authority = Authority
+ Perspective, story = Story — doctrine §9d; Mike's sample week — Monday value · Tuesday recognition · Wednesday
leadership insight · Thursday culture or event recap · Friday personal or opinion — `07-instagram/90` — is the
fallback shape when their number is lower) · **the formats and what each is for**: the talking-head Reel (the
batchable core, 30–60 s, hook → value → one CTA, raw is better than polished — `07-instagram/90`), the green screen (a take
on brokerage or industry news, facts with a source, never a dig), the carousel (the no-filming format; a LinkedIn
document post when the member attracts team leaders or broker-owners), stories (one to five a day, never a day
without — `07-instagram/89`) · **the platforms — stated, never asked** (the owner, 2026-11-14; the doc's line reads
*"Platforms: Instagram and Facebook, both — every Reel and every graphic; LinkedIn for the carousels when you attract
team leaders; TikTok and YouTube Shorts take the same video any time you want more reach"* — Facebook Reels is the
same video reposted; TikTok and Shorts are optional reposts, nothing new to make; LinkedIn on only when
`identity/avatars.md` includes team leaders or broker-owners, otherwise one line that it stays off; Mike's lesson that
one video covers every short-form platform — `07-instagram/90` — is the why) · **the batch day — the member's own answer to "your week" in `## In your words` (the day and the place they named);
only when that answer was skipped, fitted from the filming window by** (Mike's
simple week: Monday plan · Tuesday record one to two hours · Wednesday edit · post or schedule from Thursday — or his
alternate Saturdays; fitted to the filming window) · **the 15-minute routine** (same time every day: reply to every
comment with a question, answer every DM the same day, tag the agents featured so they reshare, one interactive
story element, five real comments on agents' posts in the lane, never a negative one — an OS default built on
`07-instagram/89` and `05-big-picture/36`).
Proposed, in one line: *"Your week: three posts a week — your first two weeks are the six posts you already have designed; then one attraction, one authority and one story Reel a week, stories every day; filming on [day]s."* **Then the stop line, and the reply ends** (inside setup, `sf-setup` Step 3a's line; on demand the same words): *"**Does that sound like you?** Say **Yes** and I'll build your thirty-day plan on it — or tell me what to change: a pillar, how many posts a week, your filming day, or an answer you'd give differently. **Your turn.**"* The lines below are written now (they are the proposal on file); a change at the stop rewrites them before Phase 4 starts. (at five a week the mix reads 2 · 2 · 1; "change my cadence" changes it later) Then write `Platforms (priority order): Instagram Reels · Facebook Reels (always, both) · LinkedIn (carousels, when attracting team leaders) · TikTok / YouTube Shorts (optional reposts)` (the locked value — `LinkedIn off` in its clause when the avatars hold no team leaders; setup normally wrote it already — never rewrite a filled line) · `Cadence:` · `Weekly
mix:` · `Batch day(s):` to `publishing.md` (the source), mirror `Cadence` and `Platforms` into `content-pillars.md`'s
header lines and `## Weekly mix`, and write the batch day and time to the single `Filming window:` line of
`identity/operations.md` (this plugin's one write there, by the Brain contract's permission — the mirror of
`Batch day(s):`; the YouTube plugin reads it by name) → push. (The routine that runs it week to week is `sf-weekly-routine`.)

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
free, no strings."* at the open register. **The call-ask rule — one rule everywhere** (house rules #13, the
optimizer's platform rules, the kit's own six posts): **GUIDE is the ask on most posts. The invitation (the offer's
own word, or the kit's call line) is the ask on about one post in four — most naturally a Proof piece or a "what you
get" piece. A Proof piece may carry the guide instead. Never two asks on one post. The six designed kit posts keep
exactly the asks the kit printed.** The model itself is explained on a call, never in a caption or a DM (doctrine
§8, `02-prospect-targeting/19`: say as little as you have to in text). **The ask map by pillar:** Authority → GUIDE ·
Perspective → follow, save or share (or GUIDE) · Story → GUIDE or the invitation · Proof → the invitation or GUIDE ·
Personality → follow — never a keyword, never the call. Five spoken ask lines in the member's voice, one per pillar,
on that map: Personality's is "follow for the next one" and nothing more (never "Comment GUIDE"); never a third
word. **ManyChat — told, never asked (the owner, 2026-11-14); the section's ManyChat line reads, in
this shape:** *"ManyChat is how your two keywords answer themselves. Set it up this week: install ManyChat (the free
plan starts you — upgrade only if ManyChat itself asks you to for Instagram automations), import Mike's templates
from your Materials folder, put GUIDE and [WORD] in with your links — your build sheet walks you through it step by
step. You don't connect ManyChat to Claude: nothing here needs its connector or a paid plan for it. Until it's live,
reply by hand from your DM bank."* Never a question, never an opt-out, never "connected". Write
`Keyword:` (if this run set it) · `What it opens:` (GUIDE → the guide's title · [WORD] → the one-pager and the call)
to `publishing.md`; the `ManyChat:` line is written by `sf-comment-to-dm` (Job E — `not yet — set it up this week
(build sheet YYYY-MM-DD)` when the sheet is written, `set up YYYY-MM-DD` on the member's word that it is live; inside
setup the build sheet is handed over right after this plan) — this plan writes the line only when it is still empty
and the sheet does not exist yet, as `not yet — set it up this week`; mirror the two words and what each opens into
`content-pillars.md`'s `The two CTAs` line 2. The full CTA bank, the DM copy bank and the ManyChat Build Sheet stay
`sf-comment-to-dm`'s — one line at the end of the section: *"the ask lines and your DM replies: say 'my keyword
sheet'; the ManyChat steps: 'my ManyChat build sheet'."*

## Phase 6 — The 30-day calendar (section 6 · 400+ words · twelve dated rows at the default three a week (twenty at five), the six kit posts among them)
**Lazy-load doctrine §9b–§9d and `${CLAUDE_PLUGIN_ROOT}/skills/sf-talkinghead/references/calendar-guide.md`
(the calendar's rules — Week 1 establishes who they are; no story twice; no pillar more than twice in a week; one ask
on every post by Phase 5's rule — GUIDE on most, the invitation on about one post in four (most naturally a Proof
piece or a "what you get" piece), "follow" only on a Personality post; no Reel dated before the day after the batch
day that films it;
brokerage content woven through, never a week of it).** **Read now:** `memory/intel.md` (dated, sourced news for a Perspective green screen) ·
`memory/content-performance.md` (what worked — skip if empty) · `memory/content-calendar.md` (UPDATE mode: the
rows already mapped — the new window starts the day after the last mapped date; rows at `Scripted` or later are
never rewritten).
**The first rows are the six kit posts — "post, don't make."** In the doc they sit under the band **GRAPHICS — THE
SIX POSTS YOU ALREADY HAVE (post, don't make — the Graphics tab on your board)**; the Reels follow under **REELS — [n]
rows at your cadence (the Reels tab)** (the owner, 2026-11-14). They were designed in Claude Design in Week 3, so
nothing is written for them here: rows 1–6 carry the kit's posts in the kit's order (Post 1 — The guide · Post 2 —
Five problems, five fixes · Post 3 — My story · Post 4 — What you get · Post 5 — Proof · Post 6 — Book the call),
dated one every two or three days from the first posting day — the kit's own rhythm — across the first two weeks;
**format** `carousel` (posts 1–3) or `graphic` (posts 4–6 — a single designed image, post 6 with its story;
`graphic` is the kit posts' value and maps to the board's `Graphic`) · **pillar** (the guide and the five problems →
Authority · my story → Story · what you get and proof → Proof · book the call → Proof, the call rung) · **working
title** the post's name · **hook** the post's slide 1 or headline, verbatim · **CTA** the post's ask as the kit
wrote it (`Comment · GUIDE` for the guide ask; `Call · [the offer's word]` for the call ask — a kit post keeps exactly
the ask the kit printed) · **carries** `kit post n` · Status **`Ready to Post`** (the owner, 2026-11-14: a designed post never gets the filmed status — nothing was recorded; the copy is final and the file exists — nothing to draft or film, only the caption to paste and the posting; the Monday Week Plan writes their captions and leaves the status; posting flips them to `Published`; the board seeds them as cards on the Graphics tab) · a System ID like every row. No kit → no kit rows, said once in the Read-this-first.
**Then the Reels. Say this once, then run the pass:** *"Give me a few minutes — I'm checking what agents in your lane
are asking right now; about [N] searches, then your calendar."* ([N] = the real number inside the ≤ 8.) Demo mode:
no line, no searches. Then fill the remaining posting days of the four weeks with `sf-ideas`' method and order so the month holds **twelve rows at the default three a week (twenty at five) — the six kit posts counted among them, so the first month asks for six Reels filmed**: **the UVP's content
branches, the framework's steps and the Brain's own stories and systems first** (the branches' topics, the guide's
pages, the story bank, the proof with consent, the weekly call, the training, the member's captured ideas and this
month's objections — Weeks 1–2), **fresh research second** (the graded findings, each cited by number in the Sources
band), **the starter bank last** (`starter`, only to fill a short pillar). Week 1 still establishes who they are: the
kit's story and proof posts cover Story and Proof, so the first Reels are Personality, Perspective and the Authority
teach. **Those three are the member's own answers** (`## In your words` — the owner, 2026-11-15): the FIRST Reel row
is the question agents ask them (Perspective), then the one step (Authority), then off the clock (Personality) —
each row's working title and hook from the member's own sentence, each `Carries` cell reading `your words
YYYY-MM-DD` (with whatever else the row carries after it), and the `→` part of each `## In your words` entry filled
with its row's working title. A skipped answer's slot is filled by the order above and carries no mark. THE THREE
TO FILM FIRST are these three. Every row: `#` · **date** (real calendar dates, never "Day 1", on the cadence's posting days — **a Reel's
publishing date is never earlier than the day after the batch day that films it**: the first Reel lands on the first
posting day AFTER the first batch day that follows today and that a kit post does not take, and every later Reel after
the batch day that films it) · day · **format** (talking head · green screen ·
carousel · the story rhythm is a standing line, not a row) · **pillar** (one OS name) · **working title** · **hook**
(one breath) · **CTA** (one ask per row, by Phase 5's rule: `Comment · GUIDE` on most rows; the invitation —
`Comment · [the offer's word]`, or `Call · [the offer's word]` when the ask is the kit's call line in the law's shape —
on about one row in four, most naturally a Proof row or a "what you get" row (a Proof row may carry `Comment · GUIDE`
instead); `Follow` on a Personality row, and on a Perspective row whose take does not lead to the guide; never two
asks in one cell)
· what it carries (story hook / win / teach) · **System ID** (`sf-YYYY-MM-DD-NN`, the publish date and the row number
— the board finds the card by it). No row promises the member's time per partner (doctrine §10e). Say the count plainly — *"twelve posts this month: six already designed, six to film"* — twenty only at five a week; the floor is the cadence × four. Then **STORIES, DAILY** (the
four-category rotation runs every day regardless — one line, plus the week's story rhythm: morning · midday ·
evening — `07-instagram/90`), **THE BATCH PLAN** (the sessions, what films together, the honest hours — the member's
own batch-filming day), and **THE THREE TO FILM FIRST** (Reels only — the kit posts need no filming).
**In the document the calendar is a five-column table the member reads at a glance**, under each band: `Date` (written
"Tue, Nov 17", never 2026-11-17) · `What` (the format and the working title — "Carousel — The guide", "Reel — The year
I almost quit") · `The hook` · `The ask` (in words: "Comment GUIDE" · "Comment [WORD]" · "Follow") · `Status`. The row
number, the weekday column, the pillar, what a row is built on and the System ID stay in the Brain file and never
appear in the document — with one exception the member should see: **a row built on their own answer shows
"(your words)" after its working title** in the `What` column. **A week made only of designed posts carries the one line** *"This week you only post —
nothing to film."* (the first two weeks of a first window).
Write **`memory/content-calendar.md`** in the contract's locked shape — the eleven columns `# | Date | Day | Format |
Pillar | Working title | Hook | CTA | Carries | Status | System ID`, untouched; only the document's table is the five
member-facing columns — (BUILD: create it from the header — and when the file
is already there because the YouTube System created it for a member who ran Week 5 first, keep its three `(YouTube)`
sections exactly as they are and write only the window line and the short-form table above them; UPDATE:
append the new window below the old, never rewriting a row at `Scripted` or later), push at Phase 10. Calendar
rows are not logged to `content-log.md` — a row enters the log when a piece is scripted (the Monday Week Plan or a
content skill writes it); a kit post's row enters the log when it goes out.

## Phase 7 — What we measure (section 7 · 100+ words)
The section opens *"Any time you ask 'how's my content doing', and each month in your deep dive, five numbers: …"*
(the owner, 2026-11-14 — no weekly note): people who saw you · Reels posted of the cadence · story days of seven ·
keyword comments · conversations started (from the log) — plus calls booked from content once the funnel ledger
exists; the member's own median is the benchmark, never a borrowed one; growth is today minus the last baseline. One
line on where the numbers come from (live data once connected after setup, the posting tool, or "add my numbers"
screenshots — never estimated, "not available" is a real value). The compliance line from Step 1b. Views are not
the score; conversations are.

## Phase 8 — Your scheduled workflows (section 8 · 100+ words)
**Read now:** `config.md` (the `## Short-Form (Week 4)` block — an older `## Short-Form (Week 3)` heading is the
same block — its task lines and `Email me:`; a missing block = the workflows are switched on at the end of setup).
Describe them in plain words, by the brief's names, each with when it runs, what it produces, and that it only
drafts — **the four switched on**: the **Monday Week Plan** (Mondays, 7:00 am — this week's scripts, captions and
stories drafted onto the board with a week brief, and any welcome or win post the week earned) · **Batch
Prep** (the evening before the batch day, 6:00 pm — the teleprompter doc: this week's scripts grouped by outfit and
location, hooks three ways, the keyword on each) · the **Wednesday Brokerage News Watch** (Wednesdays, 8:00 am — three
to six real headlines, each with a 30-second green-screen take, on the board) · the **Monthly Calendar Refill** (the
last Friday of the month, 5:00 pm — the next thirty days from the pillars, the branches and what performed, the board
refilled; this skill's scheduled mode) — then **the five extras in one sentence** (the Keyword Follow-up Queue, the
Mid-week Nudge, the Monthly Deep Dive, the Daily Stories Prompt, the Quarterly Profile Audit — "they're there if you
want them; say the word any time"), and the email line as a statement — *"I'll email you a short note at your own
address when something's ready"* (`Email me: yes`), or *"no mail is connected yet, so your notes stay in Cowork"*
(`no (no mail connected)`). State each one's status honestly from `config.md`: *on since [date]* · *switched on at
the end of setup* (no block yet) · *stopped* (`paused`) · *say the word any time* (`later`). Never "offered at the
end of setup", never the two workflows retired on 2026-11-14. Nothing posts, sends, schedules,
or moves a stage on its own.

## Phase 9 — Next steps (section 9 · 50+ words)
The section names four steps, in this order, as four short numbered lines — the same inside setup and on demand:
1. *Post your six designed posts on their dates* (the first date named, written "Tue, Nov 17"; no kit → this line is
   the phrase that builds it instead — "say 'rebuild my kit'").
2. *Film on your batch day, [day]* (the first Reel named by its working title).
3. *When it's filmed, open a new chat and say "edit my reel".*
4. *Set up ManyChat from your build sheet — say "my ManyChat build sheet" and I'll print it.*
Then, one line each and only where it applies: compliance `unset` → *"Before anything is posted, say 'set up my
attraction compliance'."* · rows built without research → *"Say 'what are agents asking right now' and I'll check
what agents are searching."* Nothing else is listed here — the board, the keyword sheet and the performance read keep
their own phrases and are said in chat, not in this section.

## Phase 10 — Gate, assemble, deliver, save, anchor, hand off
1. **The gate (hard — fix, never ship past it):** every section present at its floor (1 · 150 · 2 · 400 · 3 · 200 ·
   4 · 250 · 5 · 150 · 6 · 400 · 7 · 100 · 8 · 100 · 9 · 50 words) · twelve dated calendar rows at the default three a week (twenty at five, said plainly), the six kit posts as rows 1–6 when the kit exists, each with the kit's ask
   verbatim · five pillars with three angles each · thirty hooks, six per pillar · **only the two keywords** anywhere
   (GUIDE and the offer's word) — present in section 1 and section 5; every row's CTA is one ask — GUIDE, the
   invitation, or a follow (a Personality row's is always "follow") · **the call-ask rule kept** (GUIDE on most rows;
   the invitation on about one row in four, most naturally a Proof row or a "what you get" row; never two asks on one
   row; the kit rows carrying exactly the asks the kit printed) · **every call
   ask in the CTA law's shape** (the person · their help · free · to run the method; the brokerage never the reason)
   · **no line promising the member's time per partner** (no "stand next to me on a Saturday", no group-chat or
   one-to-one line) · no compensation, split, cap, stock, rev-share, or income figure anywhere · no brokerage named
   other than the member's own, and that one only as `compliance.md` allows · no `[bracket]` placeholder · no
   negative word about any brokerage or person · every named agent consented · every number sourced or tagged
   "(illustrative — demo)" · "Week 4" wherever the week is named, never "Week 3" for short-form work · section 3's
   platform line, section 5's ManyChat line, section 6's two bands, section 7's opening and section 8's four
   workflows in the owner's shapes (2026-11-14) — no weekly note, no engagement list, ManyChat told · **dates that
   make sense** — no Reel dated earlier than the day after the batch day that films it; every week made only of
   designed posts carries "This week you only post — nothing to film." · **the document in member-facing words** —
   READ THIS FIRST carries "Your first two weeks: post the six you already have designed — nothing to film yet." right
   after its opening sentence (when the kit exists); the calendar is the five columns Date · What · The hook · The ask
   · Status, its dates written "Tue, Nov 17"; the hook bank shows the dated posts' hooks first and the rest under
   "More hooks when you need them"; NEXT STEPS is the four lines in order; and none of "rung", "carries", "branch",
   "the OS default", "the kit's CALLS TO ACTION table, verbatim", a System ID or a date written 2026-11-17 appears
   anywhere in it. Count before delivering.
2. **Assemble** on the Short-Form Game Plan skeleton in `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` §5a —
   the title and meta line, READ THIS FIRST (its opening sentence — the verdict; then, when the kit exists, the one
   plain line *"Your first two weeks: post the six you already have designed — nothing to film yet."*; then the
   insight and the plan in one line · the first post to film · the batch day), the nine sections — section 4 in its
   two parts, section 6 in the five member-facing columns, section 9 as the four lines in order —, the SOURCES band (every search and page read, dated; `starter` and `unresearched`
   rows counted; demo → "nothing searched"), the closing paragraph (consistency before cleverness — "be consistent,
   not complicated", `07-instagram/89`), the stamp per house rules #4 (byline and footer only).
3. **Deliver in chat** — a warm summary, not the doc: *"Here's your Short-Form Game Plan — who you're talking to,
   your five pillars with real angles, [N] Reels a week on [batch day], thirty hooks, the two words that turn a
   comment into a conversation, and your next thirty days with a date on every post — your six designed posts
   first, so the first two weeks are post, don't make. It's in your workspace under Content → Short-Form."*
4. **Save** per the output standard: render through `shared/render_doc.py` and upload as
   **`[Name]'s Short-Form Game Plan — YYYY-MM-DD`** to `03 · Content/Short-Form/` (the bucket root, not the month
   folder; dated — newest is current; demo: `… — DEMO — YYYY-MM-DD`). **Keep the text** at
   `~/attraction-brain/exports/short-form-game-plan-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`; the Brain
   Board's Short-Form page reads the two keywords, the five pillars and this week's rows from it). A save that fails:
   say it is NOT saved, keep the plan visible in chat, retry once, stop.
5. **Anchor and push (write → push → verify, one step):** `content-pillars.md` — the `## Game Plan anchors` block
   (plan date · doc link · cadence · mix · the two keywords · calendar window `YYYY-MM-DD → YYYY-MM-DD` · research
   budget used) and the hooks block; `publishing.md` — the strategy lines from Phases 3 and 5 and, inside setup,
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
- [ ] `## In your words` read first: each answer the member gave is angle one of its pillar, in their own sentence,
      marked `your words`; the three Reels built on them lead the calendar (the question agents ask them first)
      and show "(your words)" in the document; the section kept exactly through every rewrite
- [ ] Five pillars, exact names, three angles each, developed from the UVP's content branches and the framework's
      steps first, then the Brain — stories from the bank, proof with consent, the former brokerage unnamed; no
      angle promising the member's time per partner; the branches' absence said once when the offer predates them;
      `content-pillars.md` written and pushed at once (no Yes line)
- [ ] The mix stated in plain words (the label "the OS default" never printed in the document); the number honest
      to the hours; the batch day fitted
      to the filming window; the 15-minute routine present (the engagement routine lives here as text — never a task);
      the platform line in the owner's shape (Instagram and Facebook both; LinkedIn only for team leaders; TikTok and
      Shorts as optional reposts)
- [ ] Thirty hooks, six per pillar, under 12 words, shapes varied, the member's own first, `starter` marked
- [ ] The ladder, the ask map, the five ask lines (Personality's is "follow" only — never "Comment GUIDE"), the call
      line in the law's shape, the call-ask rule (GUIDE on most posts; the invitation on about one post in four — most
      naturally a Proof piece or a "what you get" piece, a Proof piece may carry the guide instead; never two asks on
      one post; the kit posts keep exactly the asks the kit printed), what each word opens; the ManyChat line in the owner's
      shape ("you don't connect ManyChat to Claude"; set it up this week; no opt-out)
- [ ] Twelve dated rows at the default three a week (twenty at five, said plainly) — the six kit posts as rows 1–6 at `Ready to Post` under the
      GRAPHICS band with the kit's asks, then the Reels under the REELS band; Week 1 establishes who they are; the
      calendar-guide rules kept; System IDs written; the stories line, the batch plan, the three to film first;
      research ≤ 8, cited, dated, or `unresearched` labeled with the re-run on next steps; no Reel dated before the
      day after the batch day that films it; designed-only weeks carry "This week you only post — nothing to film.";
      the document's table in the five member-facing columns (the Brain file's eleven untouched)
- [ ] Sections 7–9 present; section 7 opens on "how's my content doing" and the deep dive (no Friday); section 8
      names the four switched-on workflows, the five extras in one sentence and the email note as statements, the
      statuses read from `config.md`, never assumed; section 9 is the four steps in order (post the six designed posts
      on their dates · film on the batch day · "edit my reel" in a new chat · ManyChat from the build sheet)
- [ ] READ THIS FIRST carries "Your first two weeks: post the six you already have designed — nothing to film yet."
      right after its opening sentence; the hook bank shows the dated posts' hooks first, the rest under "More hooks
      when you need them"; no internal word in the document ("rung", "carries", "branch", "the OS default", "the kit's
      CALLS TO ACTION table, verbatim")
- [ ] The gate passed and counted; saved dated to `03 · Content/Short-Form`; the text kept in `exports/`; anchors,
      hooks, publishing lines, and the calendar pushed and verified (the Brain Board re-rendered); handed back to
      setup or to the first Reel
- [ ] Week 4 everywhere; never a skill id or a file path in a line the member reads
