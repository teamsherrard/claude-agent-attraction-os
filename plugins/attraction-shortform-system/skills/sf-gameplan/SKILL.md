---
name: sf-gameplan
description: >
  The Short-Form Game Plan for attracting agents, Week 4's flagship document. Reads the member's kit
  (the six designed posts, the calls to action) and the offer's content branches first, then writes
  positioning for short-form (who they attract, the one line, the two keywords and CTAs), five
  pillars with three angles each, the mix and cadence, a 30-hook bank, the comment-to-DM flow, a
  dated 30-day calendar that opens with the six kit posts ("post, don't make") then the Reels, the
  Friday numbers, the scheduled workflows, next steps. Gated; saved to the workspace; the pillars,
  publishing lines and calendar written into the Brain. Runs inside setup or on demand; re-runs
  update, never rebuild; the Monthly Calendar Refill is its scheduled mode. Trigger on: "build my
  short-form game plan", "my attraction short-form game plan", "short-form game plan for agents",
  "plan my next 30 days of reels", "update my short-form game plan", "refill my attraction calendar",
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
  your Short-Form Game Plan"*; the two keywords and the profiles are already confirmed. Build the plan with at most
  **two short stops** (the pillars block, the cadence word), deliver, save, anchor, then hand straight back to
  setup (the board is next). No menu, no "come back later".
- **On demand** — **BUILD** when no `## Game Plan anchors` block exists in `content-pillars.md`; **UPDATE** when
  one does ("update my short-form game plan", "plan my next 30 days of reels"): refresh only what changed (a new
  30-day calendar from the day after the last mapped date; new research; a pillar the member asked to change),
  keep every section they confirmed, save a new dated copy — **update, never rebuild.** "Plan my next 30 days of
  reels" is UPDATE mode scoped to section 6 (and the board, if they have one).
- **Scheduled — the Monthly Calendar Refill** (task id `attraction-sf-calendar-refill`; the last Friday of the
  month; the prompt `${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/references/calendar-refill-task-prompt.md`, verbatim):
  UPDATE scoped to section 6, run unattended — the next thirty days from the pillars, the branches and what
  performed, the board refilled, draft-only, nothing posted; **every run ends with a push** so the Brain Board shows
  it. Created only on the member's yes (setup's consent card, where it is recommended on, or "turn on my calendar
  refill" / "refill my attraction calendar" said in chat): `list_scheduled_tasks` first (adopt, never a twin), else
  `create_scheduled_task` with the prompt verbatim, verify (present, enabled, a `nextRunAt`), write `Calendar Refill
  task: attraction-sf-calendar-refill` to `config.md → ## Short-Form (Week 4)` (an older `(Week 3)` heading is the
  same block), push. "Not now" → `Calendar Refill task: declined`, never re-offered, available on demand. Stoppable
  in one sentence ("stop my calendar refill" → the task deleted or disabled, the line → `declined`, push). Never claim
  a schedule that did not save; a demo Brain never gets a task.

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
  starts with the Reels; never invent a post the kit does not hold.
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
every state — but `unset` means the hooks and the calendar's posts cannot ship: say so once in plain words, put
it on the plan's section 7 line (*"compliance: not set — nothing posts until it is"*), and route to
`attraction-compliance` after delivery. `set` → apply the cardinal rules and the no-compensation rule to every
line now and remind once at the end; `confirmed` → apply. "If empty, proceed" is banned.

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
- **The stops: at most two in setup** (the pillars block · the cadence word), plus the ManyChat question only
  when `publishing.md` has no answer yet. Everything else is proposed from the Brain and stated, never asked.

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

## Phase 2 — The five pillars, three angles each (section 2 · 400+ words) — ONE stop
**Lazy-load doctrine §5–§6.** **Read now:** `identity/story-bank.md` · `proof.md` (consent column) · `brand-visual.md`
(the "leader brand vs selling brand" line) · `brokerage-model.md` (facts only; never a figure) · `memory/ideas.md`
(tags `shortform` · `story`; the `## Past content (imported)` section's `pillars:` note — how they post today —
and what they already published, so the angles never repeat it) · `memory/objections.md` · `memory/content-log.md`
(empty is normal).
**Order of sources, locked (Mike, 2026-11-02 — the UVP is the foundation of the content; all content is a branch
of it):** `offer.md → ## Content branches` FIRST — each segment's three topics become angles under the pillar
they belong to (a framework step or a tactical segment → Authority; what agents pay for versus what works →
Perspective; the story's turning point → Story; a partner's result → Proof; the teaching method and the routines
the member keeps → Personality) — the Brain's other signals SECOND (the story bank, proof, objections, the
captured ideas, the conversations), the starter hook bank LAST (Phase 4, only where a pillar is still short).
No `## Content branches` yet (an offer file from before 2026-11-02, or still at seeds) → the Brain's signals as
before, and one line in the Read-this-first that the branches arrive with the offer's next refine. Never invent a
pillar angle the offer does not carry. **Every summary and angle passes the scalability test** (doctrine §10e): none
promises the member's time per partner — no "stand next to me on a Saturday", no group-chat or one-to-one line, no
"I answer my phone"; the Authority angles that teach draw from `## The framework`'s steps and the guide's pages — the
whole method, not one tactic.
Build the five from the Brain — **develop, never transcribe** — each pillar: the name (exactly `Authority` ·
`Perspective` · `Story` · `Proof` · `Personality`), a two-line summary of what it is *for this member*, and
**three angles** — each a working hook (one breath), the agent it is for, the pain it answers, and what it carries
(a content-branch topic, a story-bank hook, a win with consent, a routine they keep, a teach from the known-for): Authority = the niche
dissected into tactical pieces, the tip of the iceberg (`06-content-framework/37`, `07-instagram/88`) ·
Perspective = the takes they hold, the myths to bust, the questions agents ask — never about a named brokerage or
person (`07-instagram/88`, `03-model-positioning/13`) · Story = the journey's turning points with "who relates to this", the
former brokerage never named (`06-content-framework/39`, `/40`) · Proof = agents already helped (consent on file;
otherwise first name or initials), the weekly call, the training, the events — "it's not us saying our culture is
incredible, you're seeing it" (`06-content-framework/38`); zero proof → one honest line and the upline's proof
labeled as the upline's · Personality = passions, routines, family lines they are willing to share (`07-instagram/88`,
`/89` — the patio-beer test). **If the Brain holds nothing for Personality**, this is the one stop of questions in
the phase (2–4 together): *"Three quick ones so your personal side isn't a blank: (1) What do you do outside real
estate that other agents would relate to — sport, family, faith, a hobby? (2) One routine or discipline you keep?
(3) Anything that's off-limits to post? Your turn."* Hesitation → propose from the Brain, let them confirm in a word.
Present the five as **one block** (name · summary · the three hooks), then: *"That's your plan. Your turn — say
'good' or tell me what's off."* On the yes, **write `identity/content-pillars.md` now** in the contract's shape
(the template's header lines kept and filled · the one-line anchors · the five sections headed exactly by the
pillar names, three angles each · `## Game Plan anchors` · `## Weekly mix` · `## Hooks bank`), **push, verify.**
*"Saved — your pillars are in your Brain."* (Inside setup the header lines `Cadence` and `The two CTAs` line 2
fill at Phases 3 and 5 of this same run.)

## Phase 3 — The format mix and the weekly cadence (section 3 · 200+ words) — ONE word
**Lazy-load doctrine §7, §9b, §9d.** **Read now:** `identity/goals.md` (the hours per week committed in Week 1;
its `Content:` line defers to this plan — never ask for hours the Brain holds) · `strategy.md` (`Constraints /
capacity`, already open) · `operations.md` (`Filming window:`, already open).
Propose, from those: **the number — three Reels a week is the default for the first month** (the owner, 2026-11-14: twenty posts at once overwhelms; Mike's own path is three to five, working up to five — `07-instagram/88`); propose five only when `goals.md`'s hours carry it or the member asks, and let the Friday note propose the step to five once a month at three has held; honest capacity outranks ambition · **the mix** — *"one attraction · one authority · one story at three a week (2 · 2 · 1 at five), stories daily —
the OS default"* (label it exactly so; attraction = Proof + Personality, authority = Authority
+ Perspective, story = Story — doctrine §9d; Mike's sample week — Monday value · Tuesday recognition · Wednesday
leadership insight · Thursday culture or event recap · Friday personal or opinion — `07-instagram/90` — is the
fallback shape when their number is lower) · **the formats and what each is for**: the talking-head Reel (the
batchable core, 30–60 s, hook → value → one CTA, raw is better than polished — `07-instagram/90`), the green screen (a take
on brokerage or industry news, facts with a source, never a dig), the carousel (the no-filming format; a LinkedIn
document post when the member attracts team leaders or broker-owners), stories (one to five a day, never a day
without — `07-instagram/89`) · **the platforms in priority order** (Instagram Reels first; one video reposted to
TikTok, YouTube Shorts, Facebook Reels — `07-instagram/90`; LinkedIn for the carousel) · **the batch day** (Mike's
simple week: Monday plan · Tuesday record one to two hours · Wednesday edit · post or schedule from Thursday — or his
alternate Saturdays; fitted to the filming window) · **the 15-minute routine** (same time every day: reply to every
comment with a question, answer every DM the same day, tag the agents featured so they reshare, one interactive
story element, five real comments on agents' posts in the lane, never a negative one — an OS default built on
`07-instagram/89` and `05-big-picture/36`).
Confirm in one word: *"Default plan: three Reels a week — one attraction, one authority, one story — stories every day; batch day [day]. Keep it, or change the number?"* (at five a week the mix reads one attraction · one authority · one story at three a week (2 · 2 · 1 at five)) Then write `Platforms (priority order):` · `Cadence:` · `Weekly
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
`sf-ideas` also appends to; newest block last) — push at Phase 10 with the rest.

## Phase 5 — CTAs and the comment-to-DM flow (section 5 · 150+ words)
**Lazy-load doctrine §8.** **Read now:** `identity/voice.md` (the asks sound like them).
State the ladder once — Follow / save / share → Comment → DM → Resource → Conversation → Call — and the rule of
one: one Reel, one rung, one of the two words, said on camera at the end, written as the caption's last line,
pinned as the first comment. **The two CTAs of this section are the guide and the call** (the brief's §3–§4), both
verbatim from the kit's CALLS TO ACTION table: **GUIDE** → the guide, instant (the Comment and Resource rungs); the
offer's **`Comment keyword:`** → the one-pager and the invitation to talk (the DM and Conversation rungs); **the
call line** in the CTA law's shape — *"If you want my help running this — the lessons, the templates, the
community — partner with me and it's free. [the booking line]"* at the join register, *"I'll walk you through it,
free, no strings."* at the open register — the kit's call posts carry it as the kit wrote it, and a Reel carries it
at most once a month (an OS rule: the call comes after a conversation — doctrine §8, `02-prospect-targeting/19`:
say as little as you have to in text; the model is explained on a call, never in a DM). The ask map by pillar
(Authority → Comment / Resource · Perspective → Follow / save / share · Story → DM · Proof → DM · Personality →
Follow only), five spoken ask lines in the member's voice — one per pillar, each ending on GUIDE or the offer's
word, never a third. **The one question, only if `ManyChat:` is still empty:** *"Do you use ManyChat? Your two
words import into your own account — optional. Without it they still work: you reply by hand, and the keyword
follow-up queue, when you switch it on, surfaces the comments it can see — through a connected Instagram — or the ones you paste. Your turn."* Write `Keyword:` (if this run
set it) · `What it opens:` (GUIDE → the guide's title · [WORD] → the one-pager and the call) · `ManyChat:`
(`set up YYYY-MM-DD` / `not yet — replying by hand` / `declined`) to `publishing.md`; mirror the two words and
what each opens into `content-pillars.md`'s `The two CTAs` line 2. The full CTA bank, the DM copy bank and the
ManyChat paste sheet stay `sf-comment-to-dm`'s — one line at the end of the section: *"the ask lines and your DM
replies: say 'my keyword sheet'."*

## Phase 6 — The 30-day calendar (section 6 · 400+ words · twelve dated rows at the default three a week (twenty at five), the six kit posts among them)
**Lazy-load doctrine §9b–§9d and `${CLAUDE_PLUGIN_ROOT}/skills/sf-talkinghead/references/calendar-guide.md`
(the calendar's rules — Week 1 establishes who they are; no story twice; no pillar more than twice in a week; the
keyword on at least three posts a week; the call rung at most once in the month; brokerage content woven through,
never a week of it).** **Read now:** `memory/intel.md` (dated, sourced news for a Perspective green screen) ·
`memory/content-performance.md` (what worked — skip if empty) · `memory/content-calendar.md` (UPDATE mode: the
rows already mapped — the new window starts the day after the last mapped date; rows at `Scripted` or later are
never rewritten).
**The first rows are the six kit posts — "post, don't make."** They were designed in Claude Design in Week 3, so
nothing is written for them here: rows 1–6 carry the kit's posts in the kit's order (Post 1 — The guide · Post 2 —
Five problems, five fixes · Post 3 — My story · Post 4 — What you get · Post 5 — Proof · Post 6 — Book the call),
dated one every two or three days from the first posting day — the kit's own rhythm — across the first two weeks;
**format** `carousel` (posts 1–3) or `graphic` (posts 4–6 — a single designed image, post 6 with its story;
`graphic` is the kit posts' value and maps to the board's `Graphic`) · **pillar** (the guide and the five problems →
Authority · my story → Story · what you get and proof → Proof · book the call → Proof, the call rung) · **working
title** the post's name · **hook** the post's slide 1 or headline, verbatim · **CTA** the post's ask as the kit
wrote it (`Comment · GUIDE` for the guide ask; `Call · [the offer's word]` for the call ask — the kit's call posts
keep their ask; the once-a-month call rule counts the Reels) · **carries** `kit post n` · Status **`Recorded`** (the copy is final and the file exists — nothing to draft or film, only the caption to paste and the posting; the Monday Week Plan counts them as "post, don't make", the board seeds them as cards) · a System ID like every row. No kit → no kit rows, said once in the Read-this-first.
**Then the Reels. Say this once, then run the pass:** *"Give me a few minutes — I'm checking what agents in your lane
are asking right now; about [N] searches, then your calendar."* ([N] = the real number inside the ≤ 8.) Demo mode:
no line, no searches. Then fill the remaining posting days of the four weeks with `sf-ideas`' method and order so the month holds **twelve rows at the default three a week (twenty at five) — the six kit posts counted among them, so the first month asks for six Reels filmed**: **the UVP's content
branches, the framework's steps and the Brain's own stories and systems first** (the branches' topics, the guide's
pages, the story bank, the proof with consent, the weekly call, the training, the member's captured ideas and this
month's objections — Weeks 1–2), **fresh research second** (the graded findings, each cited by number in the Sources
band), **the starter bank last** (`starter`, only to fill a short pillar). Week 1 still establishes who they are: the
kit's story and proof posts cover Story and Proof, so the first Reels are Personality, Perspective and the Authority
teach. Every row: `#` · **date** (the first posting day on or after the batch day following today, then the
cadence's posting days — real calendar dates, never "Day 1") · day · **format** (talking head · green screen ·
carousel · the story rhythm is a standing line, not a row) · **pillar** (one OS name) · **working title** · **hook**
(one breath) · **CTA** (the rung + GUIDE or the offer's word; the call line in the law's shape, in at most one Reel)
· what it carries (story hook / win / teach) · **System ID** (`sf-YYYY-MM-DD-NN`, the publish date and the row number
— the board finds the card by it). No row promises the member's time per partner (doctrine §10e). Say the count plainly — *"twelve posts this month: six already designed, six to film"* — twenty only at five a week; the floor is the cadence × four. Then **STORIES, DAILY** (the
four-category rotation runs every day regardless — one line, plus the week's story rhythm: morning · midday ·
evening — `07-instagram/90`), **THE BATCH PLAN** (the sessions, what films together, the honest hours — the member's
own batch-filming day), and **THE THREE TO FILM FIRST** (Reels only — the kit posts need no filming).
Write **`memory/content-calendar.md`** in the contract's locked shape (BUILD: create it from the header; UPDATE:
append the new window below the old, never rewriting a row at `Scripted` or later), push at Phase 10. Calendar
rows are not logged to `content-log.md` — a row enters the log when a piece is scripted (the Monday Week Plan or a
content skill writes it); a kit post's row enters the log when it goes out.

## Phase 7 — What we measure and the Friday check (section 7 · 100+ words)
The five numbers `sf-analytics` reads every Friday — people who saw you · Reels posted of the cadence · story days
of seven · keyword comments · conversations started (from the log) — plus calls booked from content once the
funnel ledger exists; the member's own median is the benchmark, never a borrowed one; growth is today minus the
last baseline. One line on where the numbers come from (live data once connected after setup, the posting tool,
or "add my numbers" screenshots — never estimated, "not available" is a real value). The compliance line from
Step 1b. Views are not the score; conversations are.

## Phase 8 — Your scheduled workflows (section 8 · 100+ words)
**Read now:** `config.md` (the `## Short-Form (Week 4)` block — an older `## Short-Form (Week 3)` heading is the
same block — its task lines and `Email me:`; a missing block or `not offered yet` = "offered at the end of setup").
Describe them in plain words, by the brief's names, each with when it runs, what it produces, and that it only
drafts — **the six recommended**: the **Monday Week Plan** (Mondays, the member's hour — this week's scripts,
captions and stories drafted onto the board with a week brief, and any welcome or win post the week earned) ·
**Sunday Batch Prep** (the evening before the batch day — the teleprompter doc: this week's scripts grouped by
outfit and location, hooks three ways, the keyword on each) · the **Daily Engagement List** (each weekday morning —
ten agents to engage with today, one comment starter each) · the **Brokerage News Watch** (Wednesdays — three to six
real headlines, each with a 30-second green-screen take) · the **Friday Performance Note** (Fridays, the Friday slot
— what started agent conversations, the one change, next week's rows (three at the default cadence, five at five), the post to repurpose) · the **Monthly
Calendar Refill** (the last Friday of the month — the next thirty days from the pillars, the branches and what
performed, the board refilled; this skill's scheduled mode) — then **the extras in one sentence** (the Keyword
Follow-up Queue, the Mid-week Nudge, the Monthly Deep Dive, the Daily Stories Prompt, the Quarterly Profile Audit —
"say the word any time"), and whether the member asked to be emailed when something is ready (`Email me:`). State
each one's status honestly from `config.md`: *on since [date]* · *offered at the end of setup — recommended on* ·
*declined* · *say the word any time*. Nothing posts, sends, schedules, or moves a stage on its own.

## Phase 9 — Next steps (section 9 · 50+ words)
Inside setup: *"Next: your content board and these 30 days mapped onto it, then your workflows, then your first
Reel."* On demand: the six kit posts, posted as dated (*"your first two weeks are post, don't make"*), the first
Reel (*"script my first attraction reel"* — the first talking-head row after the kit posts), the board (`sf-board`
— map the calendar, or update it), the keyword sheet (`sf-comment-to-dm`), the film day (`sf-batch-publish`), and
the research re-run if any row is `unresearched` (*"what are agents asking right now"*). If compliance is `unset`:
the one line that sends them to the gate before anything posts.

## Phase 10 — Gate, assemble, deliver, save, anchor, hand off
1. **The gate (hard — fix, never ship past it):** every section present at its floor (1 · 150 · 2 · 400 · 3 · 200 ·
   4 · 250 · 5 · 150 · 6 · 400 · 7 · 100 · 8 · 100 · 9 · 50 words) · twelve dated calendar rows at the default three a week (twenty at five, said plainly), the six kit posts as rows 1–6 when the kit exists, each with the kit's ask
   verbatim · five pillars with three angles each · thirty hooks, six per pillar · **only the two keywords** anywhere
   (GUIDE and the offer's word) — present in section 1, section 5, and on at least three rows a week · **every call
   ask in the CTA law's shape** (the person · their help · free · to run the method; the brokerage never the reason)
   · **no line promising the member's time per partner** (no "stand next to me on a Saturday", no group-chat or
   one-to-one line) · no compensation, split, cap, stock, rev-share, or income figure anywhere · no brokerage named
   other than the member's own, and that one only as `compliance.md` allows · no `[bracket]` placeholder · no
   negative word about any brokerage or person · every named agent consented · every number sourced or tagged
   "(illustrative — demo)" · "Week 4" wherever the week is named, never "Week 3" for short-form work. Count before
   delivering.
2. **Assemble** on the Short-Form Game Plan skeleton in `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` §5a —
   the title and meta line, READ THIS FIRST (the verdict in three sentences · the first post to film · the
   batch day), the nine sections, the SOURCES band (every search and page read, dated; `starter` and `unresearched`
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
6. **Hand off.** Inside setup → return to `sf-setup` Step 4 without a question (setup's close names the Brain
   Board). On demand → *"Your Brain Board is updated. Want these thirty days on your content board? Say 'map my next
   30 days'. Or say 'script my first attraction reel' for your first Reel."*

## Quality checklist
- [ ] Brain read — the kit first (chapter 7's six posts and the CALLS TO ACTION table), three files at Step 1, the
      rest at their phase, nothing read twice, nothing re-asked; demo mode honored if asked; the live data connection
      never touched during a setup-time run
- [ ] Compliance three-state read first; `unset` named once on section 7 and routed after delivery, never blocking
      the private plan
- [ ] At most two stops in setup (the pillars block, the cadence word) + the ManyChat question only when unanswered
- [ ] Section 1: who they attract, the one line, the two keywords, the two CTAs verbatim from the kit's table (the
      guide; the call in the CTA law's shape), the why — drafted and labeled where the Brain is empty, never a
      question box
- [ ] Five pillars, exact names, three angles each, developed from the UVP's content branches and the framework's
      steps first, then the Brain — stories from the bank, proof with consent, the former brokerage unnamed; no
      angle promising the member's time per partner; the branches' absence said once when the offer predates them;
      `content-pillars.md` written and pushed on the yes
- [ ] The mix labeled "the OS default"; the number honest to the hours; the batch day fitted
      to the filming window; the 15-minute routine present
- [ ] Thirty hooks, six per pillar, under 12 words, shapes varied, the member's own first, `starter` marked
- [ ] The ladder, the ask map, the five ask lines ending on GUIDE or the offer's word, the call line in the law's
      shape (the kit's call posts; at most one Reel a month), what each word opens; ManyChat state recorded
- [ ] Twenty dated rows (or twelve, said plainly) — the six kit posts as rows 1–6 at `Recorded` with the kit's asks,
      then the Reels; Week 1 establishes who they are; the calendar-guide rules kept; System IDs written; the stories
      line, the batch plan, the three to film first; research ≤ 8, cited, dated, or `unresearched` labeled with the
      re-run on next steps
- [ ] Sections 7–9 present; section 8 names the six recommended workflows and the extras by the brief's names, the
      statuses read from `config.md`, never assumed
- [ ] The gate passed and counted; saved dated to `03 · Content/Short-Form`; the text kept in `exports/`; anchors,
      hooks, publishing lines, and the calendar pushed and verified (the Brain Board re-rendered); handed back to
      setup or to the first Reel
- [ ] Week 4 everywhere; never a skill id or a file path in a line the member reads
