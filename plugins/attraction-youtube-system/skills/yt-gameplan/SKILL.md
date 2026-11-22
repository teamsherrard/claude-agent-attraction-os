---
name: yt-gameplan
description: >
  The flagship of the Agent Attraction YouTube System (Week 5): the YouTube Game Plan for
  attracting agents on Mike's three categories (niche authority · interviews · model) and the
  8-video cycle (3 niche · 1 model · 4 interviews). Reads the kit's calls to action and the offer's
  content branches first, audits the channel at any size, sets the three topics, the interview lane,
  the model lane, ~50 titles by lane, the goal in conversations and calls (never income), the
  cadence (one video a week for the first month, two the step-up), the first 90 days as a dated
  calendar in the Brain, the 180-day direction — one member-readable doc. Runs inline inside setup
  (no question stops) or on demand; demo mode. Triggers on "build my attraction game plan", "my
  attraction game plan for YouTube", "my attraction channel plan", "my attraction YouTube
  strategy", "refresh my attraction game plan", "map my attraction channel", "180-day plan for my
  attraction channel", "change my YouTube cadence".
---

# YouTube Game Plan — the flagship document of Week 5

The **wow**: the first thing the member gets after their channel is optimized — their whole attraction channel
mapped, built from Mike's method × their Brain × their kit × their real channel. It makes them feel *"this just
handed me my channel, built around the agents I actually want — at a pace I can keep."* Substance and structure,
delivered as a clean doc — never visual design.

Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` — the doctrine (#1), the Brain first (#2), 3-state
compliance (#3), plain talk (#4), sourcing (#6), docs (#7), the stamp (#9), demo mode (#13). The Brain Contract
(`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`): this skill writes only the `## Game Plan anchors` block of
`identity/channel.md` (plus two lines of its `## Channel` block, each only in the case named under "Run from setup":
`First full video:` and `Filming day:`), seeds `memory/interview-pipeline.md` rows at Stage `Candidate`, writes the
`## Long-form (YouTube)` section of `memory/content-calendar.md`, and keeps the plan's text at
`~/attraction-brain/exports/youtube-game-plan-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`; the Brain Board's
YouTube page reads it) — nothing else in the Brain. Every write is pushed through `attraction-brain-sync` at once
(write → push → verify); every push re-renders the member's Brain Board.

**The rules that bind every line it writes (the brief of 2026-11-14 §3):**
- **The CTA law.** Every call ask is angled at partnering with the PERSON to get their help, free, to run the
  method — never the brokerage. Join register (`offer.md` header `Join-gated package allowed: yes` or `unknown`):
  *"If you want my help running this — the lessons, the templates, the community — partner with me and it's free.
  Grab [the call]."* Open register (`no`): *"I'll walk you through it, free, no strings."* The method is named every
  time; the brokerage is never the reason; compensation never. Every title, description line, pinned-comment line
  and script CTA in the plan reads the register.
- **Scalable deliverables** (doctrine §10e). No lane, title, interview angle, CTA or calendar row promises the
  member's time per partner — no weekend-beside-me line, no chat-group line, no private-call promise, no response
  time; the help is the recorded lessons, the templates, the community, the weekly group call only when the member
  already runs one. Mike's "all of my training, coaching, mentorship and mastermind calls for free" becomes the
  program's scalable assets in the member's words. (The member's own filming day is their routine and is fine.)
- **Two CTAs, two keywords.** The resource = the Week 2 guide (`memory/magnets.md → ## Current magnet`; its funnel
  URL on description line 2 and in the pinned comment; the spoken line may say "comment GUIDE"); the call = the
  booking link on description line 1, in the law's shape. The two words are `identity/publishing.md → Keyword:
  GUIDE · [the offer's word]`; every other default is retired; never a third.
- **The kit first.** The spoken lines, pop-ups and end cards come from the Week 3 Kit's chapter 7 CALLS TO ACTION
  table verbatim (`exports/week3-kit-*.txt`); the program's words from `offer.md → ## The program` and
  `journey.md → ## Why join me`. Never a new join line of the plugin's own.
- **The cadence.** One video a week is the default for the first month; two a week is Mike's recommendation, named
  as the step-up (Phase 2). The short-form cadence line is never read as the YouTube cadence.
- **Week 5, in the member's words.** Never "Week 4" for YouTube work (short-form is Week 4, the brand Week 3);
  later plugins are "a later week"; the editing next step stated, never hedged (Plugin 5 — "when it's filmed:
  'edit my YouTube video'"); other plugins by condition ("when your sales system arrives"); the Short-Form system by
  phrase ("script my attraction reels"); never a skill id or a
  file path in a line the member reads.

- **The document is for the member; the codes are for the Brain** (the owner, 2026-11-14 — the Short-Form Game
  Plan's treatment). Only the DOCUMENT changed: the Brain's files keep their locked shapes (`identity/channel.md →
  ## Game Plan anchors`, the rows of `memory/content-calendar.md → ## Long-form (YouTube)`). In the document: one
  member word for a content lane — "lane" (five lanes: the three topics, the interview lane, the model lane) — and
  none of the system's words ("bucket", "SIGNAL", "FOR · PAIN · SIGNAL", "cycle position", "anchors",
  "unresearched", "starter", "rung", "avatar"); dates in words ("Mon, Dec 7"); **YOUR NEXT 7 DAYS** as its own
  block right after Read this first, three numbered lines; the 90-day calendar as one plain table (Week of ·
  Video · Kind · Guest); the goal as four plain lines with every assumed number labelled "(an assumption — change it
  any time)"; the title list LAST, under **MORE TITLES WHEN YOU NEED THEM**, by lane, plain titles. Each title's
  working notes live only in the Brain's copy — the TITLE NOTES block of the export
  (`${CLAUDE_PLUGIN_ROOT}/shared/doc-format.md` has both shapes).
- **In every sentence the member hears:** "your eight-video plan" (never "the 3-1-4 cycle"), "your three topics"
  (never "niche lanes"), "your title and description" (never "SEO"), "your Channel Page" (never a kit).
- **The first-date rule** (the owner's review, 2026-11-14 — a card never says "record today"). Video 1's Recording
  date is the member's next filming day that is **at least three days after the day the plan is built**
  (**`identity/channel.md → ## Channel → Filming day:` first — the day the member gave at setup**; then
  `identity/operations.md → Filming window:` or the batch day recorded there; none on file → **the Saturday after
  next** — the second Saturday after the sitting, 8 to 14 days out); its Publish date is two days after that; and
  **every later row follows from it** — one a week: seven days after the row before; two a week: two rows a week
  on that filming day (or the window's two days when it names two), out two and five days later. A `Booked`
  guest's own recording date wins for that row. Week 1 on the plan is the week of video 1's Recording date — never
  the week of the sitting unless the filming day allows it. A refresh or a cadence change re-dates the un-started
  rows by the same rule, counted from the day it runs.

**Lazy-load:** `references/gameplan-framework.md` at Step 2 (the backbone). Doctrine sections only when the
phase needs them: §3 and §7 (Phase 2), §4 (Phase 3), §5 (Phase 4), §6 (Phase 5), §9 (Phase 6), §10 (Phase 1's two
CTAs), §13–§14 (Phases 7–9). `references/starter-title-bank.md` at Phase 6 only, and only when the member has no
titles of their own (the rule is stated there). Never the whole doctrine up front.

**Run from setup (`yt-setup` Step 6b — after the member's Yes).** Setup's Step 6a has already asked the member its
ONE blanket question — the filming day, the same for every member (the owner, 2026-11-16: "blanket questions… the
same across the board", and "we don't really need more questions because they've already gone through a lot of
this when they were building their AI brain"; and 2026-11-21, of the second question setup used to ask — which
topic they could talk about with no notes: "Why is this needed?") — saved the answer under `identity/channel.md →
## In your words`, PROPOSED what the plan stands on — the three topics, the first videos, the pace, the filming day
— and waited ("it should WAIT for me"); this skill starts only on the member's Yes and builds on what they approved
or changed there.
**What setup hands over:** the topic of the first niche video (video 1; on a new channel, the one right after the
trailer) — `channel.md → ## Channel → First full video:`, written by setup on the Yes — and the day every date is
counted from (`Filming day:`).
**The first-video rule — which of the three topics video 1 is on (the same rule setup's proposal used; never a
question).** In this order, the first that applies: **(1)** the topic the member named — at setup's proposal, later
("start with [topic] instead"), or in an answer an earlier version saved (`## In your words → Twenty minutes, no
notes` — kept, never asked again; this skill fills its `→` part with the title of the video it became) · **(2)** the
topic their guide is about (`memory/magnets.md → ## Current magnet` — the one of the three its title and pages
answer most directly: the video is half written already and its call to action is the guide) · **(3)** the topic
the first step of their method teaches (`identity/offer.md → ## The framework`) · **(4)** the first of the three as
the Channel Page lists them. Video 1 takes that topic's strongest title; the bank's order fills the rest (Phase 8).
**A plan built with no `First full video:` line on file** (an older Brain, or the plan built on demand) applies the
rule itself, writes the line (`[the topic] · [from your guide | from your method | the first of your three | your
choice] YYYY-MM-DD`), and says the choice and why in one line of its summary — a statement, never a question. **"Start
with [topic] instead"** → the line is rewritten as `your choice` and video 1 is rebuilt when it has not been
started; nothing else moves.
**Everything else comes from the Brain by this
skill's own phases, never from a question:** the first guest slot (Phase 4 — an agent the Brain holds, or the
honest line that the first conversation starts when the member names someone), the early story slot (Phase 8 —
the story `journey.md` marks as the "why join me" story, else the first of the member's own in the story bank),
the model video. `identity/content-pillars.md → ## In your words` (the Week 4 answers, read-only) is a source for
the trailer and the story video. A skipped filming day leaves the dates to the first-date rule's fallback. **No
question is ever asked that assumes the member has attracted an agent** — who they have helped, who they would sit
down with — **or asks who they are, what they like or what they are good at.**
**On demand, a refresh ("refresh my attraction game plan") with the filming day `skipped` on file** asks that one
question first, exactly as `yt-setup` Step 6a prints it; the answer replaces the entry and is written to
`Filming day:` (this skill writes both), and the videos not yet started are re-dated from it — said in one line.
From the member's Yes at setup's proposal the plan runs through with **no further stops**: the cadence is the one approved at 6a (Phase 2 — one video a
week unless the member chose two), never asked again; goals at `seeds` are used
and labeled, never asked for (Phase 7); the board step is skipped (Phase 9 step 6 — setup's next step adds the
YouTube tab and maps the next 30 days); **no chat summary of its own** (Phase 9 step 3 — setup hands the plan over
in two lines pointing at the document: no topic list, no title list, no calendar, no goal numbers in the chat);
the closing hand-off is replaced by handing back to setup (Phase 9 step 7); compliance `unset` is not mentioned
here (setup's close says the one line). The research line (Phase 3) is still said once — setup says it with its
announce line; it is a progress line, not a question. **Also not done from setup:** the public channel page is not
read a second time (the baseline `yt-setup` Step 3 wrote in `channel.md` is the audit's read); the Studio-screenshot
line and the "'change my YouTube cadence' is one phrase away" line are not said (both live in the document); and
**the three topic names and their playlist names already in `identity/channel.md → ## Lanes and playlists` are kept
word for word** — the member pasted them on their channel minutes ago; research fills the titles, never renames a
topic (on demand, a renamed topic is written back to that table and said in one line). On demand, every stop below
behaves as written.

**"Change my YouTube cadence" (on demand — the one phrase that changes the pace; never the whole plan again).**
The member's own words set the pace (one a week ↔ two a week — nothing is asked). No audit, no research, no new
titles: the lanes and the bank stand. Rewrite the cadence line and re-date the un-started rows of the 90-day
calendar at the new pace (the first-date rule, counted from today), then run Phase 9 as a refresh — the plan re-saved dated with its text in `exports/`,
the `Cadence:` anchor with today's date and the `Step-up:` line (step 5), the Brain's calendar (step 5b —
`Scripted` and later rows never move), the board by the rolling rule (step 6), the push — and say in one line
what moved.

---

## Step 1 — Load the Brain and the channel (read; never re-ask)
Read `~/attraction-brain/brain.md` (pull first via `attraction-brain-sync` if missing — a PULL is the whole Brain),
then only three more files now — the rest open at the phase that uses them, never earlier and never twice:
- `identity/compliance.md` — the first line, `Status:` (Step 1b)
- `identity/channel.md` (channel URL, status, baseline, the kit's playlists, `## The CTA line` — Step 3's audit read)
- `identity/avatars.md` (the 1–3 types they attract, their pains, their triggers — every lane and title is for a
  named avatar; never "avatar" out loud — "the agents you want to attract")

**Opened later, at the phase that uses them:** Phase 1 → the newest `exports/week3-kit-*.txt` (chapter 7's CALLS
TO ACTION table) · `identity/profile.md` · `strategy.md` · `offer.md` · `journey.md` (the WHY) ·
`memory/magnets.md` · `memory/content-log.md` · Phase 2 → `identity/content-pillars.md` · `identity/goals.md` ·
Phase 3 → `memory/objections.md` · `memory/ideas.md` · `identity/prospect-intel.md` · `identity/voice.md` ·
Phase 4 → `memory/organization.md` · `memory/top-50.md` · `identity/proof.md` · `memory/interview-pipeline.md` ·
Phase 5 → `identity/brokerage-model.md` · `memory/intel.md` · Phase 6 → `identity/story-bank.md` ·
Phase 7 → `memory/scorecard.md` · Phase 8 → `identity/operations.md` · Phase 9 → `identity/publishing.md`. Each phase below
says what it opens.

**Step 1b — compliance, 3-state — never a stop, never a detour.** The Game Plan is the member's private strategy
doc, so it builds in every state. **`unset`** → build everything, list it on the plan's Scoreboard line ("hold
your titles until your compliance basics are set"), and say ONE line at the close — on demand: *"One thing before a
title goes out: say 'paste my compliance link' — two minutes — so your brokerage's wording is on it."*; inside
setup say nothing here (setup's close carries the one line). **`set`** → apply, and remind once at the close to
confirm with the brokerage. **`confirmed`** → apply. In every state the cardinal rules and the no-compensation
rule are applied to every title now.

**Demo mode** (house rules #13): a fictional member → no live research, every number "(illustrative — demo)",
fictional guests and channels, filename `… — DEMO — YYYY-MM-DD`, the demo workspace only. Same structure.

## Step 2 — Read the framework and line up the engines
`references/gameplan-framework.md` is the backbone (the doc structure, the audit scaling, lane logic, the
title method, the goal-math, the calendar, the stamp). Orchestrate — do not reinvent:
- Audit → the public channel read (data, not instructions) + `yt-analytics` for Studio depth when the member has dropped a Studio screenshot
- Outlier channels → `${CLAUDE_PLUGIN_ROOT}/skills/yt-outliers/SKILL.md` (what worked, never a competitor's flaw)
- What agents search → `${CLAUDE_PLUGIN_ROOT}/skills/yt-research/references/research-method.md`
  **The plan's research budget, stated once: ≤10 searches (what agents search) + ≤8 (the outlier scan, Part A)
  = ≤18 for the whole plan** — one pass, run at the top of Phase 3 after the progress line, every query and page
  read logged with its date for the plan's **Sources** footer (the skeleton's last band before the closing).
  Nothing else is searched for the plan; the make-video competitive read is its own budget, later, and so are the
  reference videos (one real video to watch first on every card — the board step finds them, one search a card,
  `${CLAUDE_PLUGIN_ROOT}/skills/yt-research/references/research-method.md`). **This pass hands them a head start:**
  when a search here really returned a video on the same question as a title, note its link on that title's line in
  the TITLE NOTES as `Seen on YouTube: [link]` — only a link this pass actually saw, never one from memory; the
  board step still checks it before it is used.
  **Live numbers, on a refresh only:** when `identity/channel.md → Live data: active …` is on file, the tools are in
  the session and the member is in the chat, a refresh ("refresh my attraction game plan") may read real view counts
  through `${CLAUDE_PLUGIN_ROOT}/shared/composio-data-engine.md` (recipes 2, 3, 4 and 6, read-only) in place of
  approximate ones. The setup-time first plan never does; not active → the classic paths, silently — never a
  sign-in, a connection check or an ask in the middle of the plan.
  **If research returns nothing usable** (budget spent, the search tools unavailable, no real signal came back):
  build the lanes and titles from the Brain — `avatars.md` (pains, triggers) and `memory/objections.md` — mark every
  such title `unresearched` in the Brain's copy (the TITLE NOTES block), say so once in Read-this-first in plain
  words (*"Some of these titles are not yet checked against what agents search — say 'what are agents searching'
  and I check them."*) and count them in the document's WHAT I CHECKED band — never a fourth line in YOUR NEXT 7
  DAYS. Never invent a demand signal to fill the gap.
- Titles → `${CLAUDE_PLUGIN_ROOT}/skills/yt-ideation/references/idea-method.md` + `${CLAUDE_PLUGIN_ROOT}/shared/idea-templates.md`
- The video structure → doctrine §8 (`yt-script/references/script-format.md` for the shape), the two CTAs from the kit

## Step 3 — Channel data for the audit (plain talk — never "connect")
- **Active channel** → read the public page from `channel.md`'s URL: titles, views, lengths, cadence, playlists,
  about text, whether a CTA exists. Say once, as a statement: *"drop a screenshot of your Studio analytics any time and I'll add click-through and
  watch time."* Never required, never a question.
- **Empty / none** → skip the numbers; this is a launch plan, not a turnaround.
- Any public channel link works (a coach testing on a member's channel) — same read, no login.

---

## Phase 1 — The audit and the positioning read (scaled; honest, never flattery)
**Read now — the kit first:** the newest `exports/week3-kit-*.txt` — chapter 7's **CALLS TO ACTION** table (the
caption's last line · the comment keywords · the video pop-up · the spoken line · the end card · the story · the bio
link · the DM reply — the ask for the guide and the ask for the call, verbatim; Phase 1 takes the two CTAs from it,
Phase 9's video-structure band the spoken lines; none → the two CTAs are built from `magnets.md` and the booking
line in the law's shape, labeled "(from your Brain — your kit's wording replaces it)", and one line in
Read-this-first says the kit is built at the end of the offer sitting). Then `identity/profile.md` · `strategy.md`
(known for, priorities) · `offer.md` (the offer — once built, `## The framework`'s one-line version is hook and
title material (the steps as a chain) and `## The program`'s 90-day outcome is the promise a lane points at; the
program's name appears in a title, a description or the channel bio only where the offer's own `How to talk about
it` lines carry it — never its type or cadence; an older offer file without those blocks → the UVP line; the live
resource is `memory/magnets.md → ## Current magnet` first when it exists, `offer.md` second; **`## Content
branches`** — the UVP's 5 to 7 segments with three topics each — is the FIRST source of the niche lanes (Phase 3)
and the title bank (Phase 6), the Brain's other signals second, research third, the starter bank last (Mike,
2026-11-02: the UVP is the foundation of the content; an offer file without the section → as before, and one line
in Read-this-first that the branches arrive with the offer's next refine); **the header's `Join-gated package
allowed:` line sets the register** — `yes` or `unknown` → the join register, only `no` → the open register — for
every CTA, description and call line in the plan; `Status: seeds` → "Week 2 builds the offer"; never demand it) ·
`identity/journey.md` (`## The WHY`, `## The leader moment`, and `## Why join me` when Week 2 wrote it — the WHY
below) · `memory/content-log.md` (what already exists). Per the framework: 100 videos → full read (which of the
three categories are present, which absent; CTA present; playlists; packaging); 10 → the 2–3 highest-impact fixes;
1–2 → "too early to read"; 0 → skip. Always name the insight in attraction terms: *"your best videos have always
been the ones where you teach [niche] — there's an audience of agents, they just don't know you'll help them."*
The positioning read: can a first-time visitor tell who this channel is for and why to reach out?

**The two CTAs, stated in the positioning band:** **the guide** — the kit's spoken resource line (*"[what the guide
holds, one clause]. Comment GUIDE and I'll send it."*; its funnel URL on description line 2 and in the pinned
comment) and **the call** — the kit's spoken call line in the law's shape for the register (join: *"If you want my
help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*;
open: *"I'll walk you through it, free, no strings."*; the booking link on description line 1). The brokerage is
never the reason; nothing promises the member's time per partner.

**The WHY — three statements in their voice, never a question box.** Under the one line, the positioning band
carries: *why I'm building this* (`journey.md → ## The WHY` — the why-line verbatim, who it is for — and `## The
leader moment`) · *what's missing for the agents I attract — and how I bridge it* (`positioning.md`'s bridge-the-gap
line and `offer.md`; always the agents' problem, never a word against another team or brokerage —
`03-model-positioning/13`) · *why me, for a new agent and for a seasoned one* (`## Why join me` when Week 2 wrote
it; otherwise `leadership.md` and `strategy.md`'s known-for). A line the Brain has not written yet is drafted from
`strategy.md` + `avatars.md` + the journey's turning points and labeled "(draft — your Brain's WHY is written in Setup and
Week 2)"; the doc never asks for it and never shows a blank (`01-foundation-mindset/10`: write it down, replay it on
the hard days). Enthusiasm carries it — write it the way they would say it out loud.

## Phase 2 — The three categories, the cycle and the cadence (doctrine §3, §7)
**Read now:** `identity/content-pillars.md` (the Brain's five pillars — Authority · Perspective · Story · Proof ·
Personality — written by the Short-Form System in Week 4; empty only when the member skipped Week 4, say so; its
cadence line is the short-form cadence, never the YouTube one) · `identity/goals.md` (the hours and the content
line now; its 90-day targets carry into Phase 7 — never re-read).
State the funnel in the member's terms: niche content creates authority → interviews create proof → model
content captures intent → the two CTAs create conversations → the call. Lock the ratio: **3 niche · 1 model ·
4 interviews per 8 videos**. **Set the YouTube cadence here, once — the default is ONE video a week for the first
month** (the owner, 2026-11-14: too much at once overwhelms a working leader). **Two a week stays Mike's
recommendation** (`/94`: roughly four times the growth of one), named in the plan as **the step-up** the Monthly
Channel Review proposes after a month at one has held — or sooner when `identity/goals.md`'s hours clearly carry
it or the member asks. The 8-video cycle holds at either pace (one cycle in eight weeks at one a week, in four at
two); **the first four videos at one a week run niche · interview · niche · model** (Why I Switched allowed early,
Mike's own exception). On demand: state the pick and why in one line and build on it — a
statement, never a "does that work?". **Inside setup: no question and no chat line — the cadence approved at 6a goes into the document** (the phrase
"change my YouTube cadence" lives in the document, not in the chat). It becomes the `Cadence:` anchor every other skill
reads (Phase 9 — `1/week · since YYYY-MM-DD`, the step-up noted) and the pace the board's 30-day window is mapped
at: **four or five cards at one a week, eight or nine at two.** Say why not every video is brokerage content.

## Phase 3 — The three niche lanes: the Problem · Situation · Future buckets (doctrine §4)
**Read now:** `memory/objections.md` (the Situation and Model titles answer these) · `memory/ideas.md` (tags `youtube`,
`interview` — the member's own ideas first) · `identity/prospect-intel.md` (where agents gather, movement — if
researched) · `identity/voice.md` (the plan is written in their voice from here on).
**Before the first search — say this once, member-facing, then run the pass:** *"Give me a few minutes — I'm
checking what agents in your market search for and which channels work; about [N] searches, then your plan."*
([N] = the searches you will actually run, inside the ≤18 from Step 2 — the real number, never "a few".) Then
the one pass: the research method's queries scoped to the avatars, the niche, and the model (≤10) and the
outlier scan (`yt-outliers` Part A, ≤8) — feeding Phases 3–6; log each query and page read with its date.
Demo mode: no line, no searches; the Sources footer says so.
From the UVP's content branches first (`offer.md → ## Content branches` — each segment is a candidate lane or a
run of titles inside one), then the Brain (avatars, pains, known-for, objections) + what agents search (research)
+ what won elsewhere (outliers), set **one named lane per bucket**, each for a named avatar, each tied to one of Mike's five pains,
each with a playlist name and a one-line *"why this builds authority."* The lanes that teach draw from `## The
framework`'s steps and the guide's pages — the whole method, not one tactic. Future-lane content speaks to leverage
and the next stage **without numbers**. Say in the plan that all three carry the **Authority** pillar (Story and
Personality angles where the video is the member's own story), interviews carry **Proof**, model content
**Perspective** — the member's content pillars from the Short-Form setup (Week 4) are the same five, so they see
one strategy, not two.

## Phase 4 — The interview lane (doctrine §5)
**Read now:** `memory/organization.md` · `memory/top-50.md` (the interview guest lane) · `identity/proof.md` (real wins
only, consent column) · `memory/interview-pipeline.md` (existing rows — never touched).
From `organization.md` and `top-50.md` (plus the member's `ideas.md` tag `interview`): 6–10 candidate guests
with the **hook-and-transformation title** each ("How [guest] built … while …"), sequenced for relatability
across types (new agent · experienced · top producer · team leader · broker-owner · switched). **Zero
organization and no agent helped yet — the normal state of a member attracting for the first time (the owner,
2026-11-16)** → no guest table and no invented names: the lane block is the one paragraph `doc-format.md` prints
("You have not recorded a conversation yet — every member starts here…": the next agent they help, a winner from
their upline's team named as the upline's, a peer with a method worth sharing), the playlist is called
"Conversations with agents", every Interview row on the calendar is titled *"A conversation with an agent — guest
to be named"* with Guest "—", and no `interview-pipeline` row is seeded. The invitation
and the guest's outro CTA follow the law (the person · their help · free · to run the method) and never promise
the member's time per partner. Seed `memory/interview-pipeline.md` rows at Stage `Candidate` in `yt-interview`'s
shape (repeated in `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`; create the file with its header if it does
not exist, never touch existing rows). Never invent a guest or a result. **A guest with no result on file** (the member named
someone the Brain knows nothing about) → the row and the card are titled *"A conversation with [first name]"* until
the invitation chat learns their story — never a transformation nobody told you.

## Phase 5 — The model lane (doctrine §6)
**Read now:** `identity/brokerage-model.md` (the model lane; empty = "say 'explain my model to me' and the model lane
deepens") · `memory/intel.md` (dated brokerage news for the model lane).
The "answer what they're already researching" list for *their* model: explained · should you join · how
[component] actually works · before choosing a sponsor ask these questions · do NOT join if · myths · fit by
avatar. Mechanics and fit in public, compensation on the call. Include Mike's comparison warning in one line;
comparisons only on the member's explicit choice via `yt-model-breakdown`. An empty `brokerage-model.md` →
titles still build; the content deepens after "explain my model to me."

## Phase 6 — The title bank: ~50 exact titles, bucketed (doctrine §9)
**Read now:** `identity/story-bank.md` (Story and Personality angles); `journey.md` is already open from Phase 1 (the
Why I Switched material — the former brokerage never named; reused in Phase 8).
Problem 12–15 · Situation 12–15 · Future 6–8 · Interview 8–10 · Model 6–8 (the bucket decides the pillar a
future content-log row carries: Authority · Proof · Perspective). Every title: one promise, ≤70
characters, a formula number where one applies, the avatar and pain named in its note, a real signal cited
(demand · a dated news item · a captured question or objection · a proven outlier · a gap in their own
channel — or `unresearched`, Step 2's fallback). **The note is the Brain's copy only** — one line per title in the
TITLE NOTES block of the export; **the document prints the plain title and nothing beside it**: the thirteen or so
on the 90-day calendar in the calendar's table, the rest at the end under MORE TITLES WHEN YOU NEED THEM, grouped
by lane. **Hard gates:** no compensation figures or earnings implied · no
negative word about a brokerage or person · no protected-characteristic targeting · the old brokerage never named
in Why I Switched · model titles dated with the year · no title or note promises the member's time per partner ·
every CTA a title's note carries in the law's shape. Thumbnail text given with a title is 3–5 words and differs
from the title.

**No titles of their own?** When `offer.md` carries no `## Content branches`, `memory/ideas.md` holds no open
`youtube` / `interview` rows, the channel is empty or thin, and research came back thin — seed the bank from
`references/starter-title-bank.md` (open it now, not before): the agency's four-month arc, every title already
compliance-cleaned and tagged with its lane, pillar, arc month, agent type, and pain, plus eight interview angles.
The order never changes — the UVP's content branches and the member's own ideas, then the Brain's signals, then
fresh research, then the starter bank — and the branches and the member's captured ideas always lead the bank
even when the arc fills the rest. Swap `[my brokerage]` (the name only where `compliance.md` allows it in
public titles, otherwise "my brokerage"), `[year]`, and `[guest]` for real values; keep the lead-gen and CMA titles
only where that skill sits inside the member's known-for; mark every seeded title `starter` in the TITLE NOTES (the
research pass upgrades it to `demand` when a search confirms it — a starter title is never presented as a demand
signal). The arc's month tags are positions, not calendar months: the 3-1-4 ratio still rules every cycle (the
bank's header carries the fit math at one a week and two). Say it once in Read-this-first, in plain words: *"Your
title list starts from the starting list; your own ideas and your comments replace it as they come in."*

## Phase 7 — Your goal → the plan (conversations and calls, never income)
**Read now:** `memory/scorecard.md` Targets block (the ratios), with `goals.md` from Phase 2 (the 90-day conversations
and calls-held targets). **The goal is read from the Brain, never asked — on demand and inside setup alike.**
Locked → the Brain's numbers. `seeds` → the seed numbers, labeled. Neither file holds a target → the framework's
labeled default (`references/gameplan-framework.md`, the goal-math), stated plainly as a default. Seeds or
default: say once, in the plan and in chat, that it can be changed — *"these are starting numbers — say 'set my
attraction goals' to lock your own."* A statement, never a question.
Per the framework's math: the 90-day calls-held target from `goals.md` → calls booked needed (÷ show rate) →
conversations needed (÷ the Brain's conversations→calls ratio) → YouTube's share this quarter (the member's
split; default labeled) → per-video conversations at their cadence (≈ 13 videos in 90 days at one a week; ≈ 26 at
two). State every assumption; frame it as a credible path with the leading indicators they control (videos
published, interviews recorded, both CTAs placed, comments answered, DMs started); the step-up to two a week is
the first lever if the per-video number looks ambitious. **Never a dollar figure, never rev share, never "you'll
make."** Subscribers are tracked, not targeted.
**In the document the math is four plain lines** (the skeleton's YOUR GOAL, IN FOUR LINES): the 90-day goal in
calls held · the calls to book · the conversations to start · YouTube's part and what that means a video — each
with the member's own number, and **every number the member did not state labelled "(an assumption — change it any
time)"**; then the weekly things they control, the honest read, and "set my attraction goals". No formula, no
arrows, no ratio names.

## Phase 8 — The first 90 days on the cycle (doctrine §7, §13)
**Read now:** `identity/channel.md` (`Filming day:` — the member's own answer, the first-date rule's first source)
· `identity/operations.md` (`Filming window:` — the fallback).
A week-by-week calendar at their cadence, **one video per row**, **sized to the cadence** — about thirteen rows
at one a week (once round the eight in eight weeks, then the start of the second), about twenty-six at two.
- **The dates — the first-date rule (above):** video 1 is recorded on the member's next filming day at least three
  days after today (the day the member gave at setup, `channel.md → Filming day:`, comes first; none on file → the Saturday after next), published two days later; every later row follows
  from it. Never a row dated the day the plan is built.
- **The locked order at one a week — every file agrees on it:** **niche · interview · niche · model · interview ·
  niche · interview · interview** (opening with niche so a new viewer meets the member before the guests; the two
  interviews that close the eight may be recorded in one sitting). At two a week the same order runs two rows a
  week, niche first within the week. Why I Switched takes an early niche slot when their story is ready
  (`journey.md`); a bank seeded from the starter arc fills the slots in the bank's order (Month 1 niche titles
  open the first eight, M3-01 takes the model slot, M1-I1 the first interview) — the ratio never bends to the arc.
  **Video 1's topic is the one the first-video rule gives** (`channel.md → First full video:` — "Run from setup",
  above): the first niche slot takes that topic's strongest title, and the order above fills the rest.
- **A new channel's trailer** (status `none` or `empty`): the channel trailer is **week one's first row** — a row
  and a card like any other, 60 to 90 seconds, not one of the eight. At one a week it is week one's row and the
  eight start the week after; at two a week it takes week one's first slot and the first niche video the second.
  Setup's first-video line names it.
- **In the document, one plain table** — `Week of` (the Monday of the week, in words: "Mon, Dec 7") · `Video` (the
  exact title) · `Kind` (Niche / Interview / Model; the trailer's row says Trailer) · `Guest` — in two parts:
  YOUR FIRST 30 DAYS (the rows the board cards) and THE WEEKS AFTER; one line for the order of the eight; **the
  step-up checkpoint at the end of month one** in one line (*"A month in, your monthly review asks whether two
  videos a week fits. Any time: say 'change my YouTube cadence'."*). The real dates and the codes go to the Brain's
  rows (Phase 9 step 5b), never into the table.
Then **days 91–180 as the direction** (double down · compounding assets · the machine). The scoreboard from
`goals.md` (what they do · what follows), click-through rate 6–10% after month one, compliance status.

## Phase 9 — Assemble, deliver, save, anchor, hand off
1. Assemble on the **Game Plan skeleton** in `${CLAUDE_PLUGIN_ROOT}/shared/doc-format.md`, in its order —
   Read this first (with the cadence line) · **YOUR NEXT 7 DAYS** (its own block: the first video by exact title ·
   the first agent to invite for an interview (nobody on file → the first-conversation line `doc-format.md` prints,
   never "the first agent you have helped") · the one channel fix — three numbered lines, never a fourth) · the
   audit · positioning (the two calls to action, the WHY) · the three topics · the interview lane · the model lane
   · the goal in four lines · the video structure (the kit's spoken lines in their places — the guide inside
   minute one, the call a third in) · the cadence · the first 90 days (the plain table) · the direction · the
   scoreboard · WHAT I CHECKED, AND WHEN (every search and page read, dated in words; the channels read; searches
   run of 18; the titles not yet checked against search, counted; demo → "nothing searched") · **MORE TITLES WHEN
   YOU NEED THEM** (last — by lane, plain titles) · the closing, the stamp. **Read the document's rules at the top
   of that skeleton and check the text against them before it renders:** none of the system's words, one word for
   a lane, dates in words, no code beside a title.
2. **Compliance pass** (#3) on every title and line — plus the law's shape on every call ask and no line promising
   the member's time per partner.
3. **Deliver in chat** — inside setup: nothing here (setup's two lines point at the document). On demand — a warm
   summary in three lines, never the doc: *"Here's your Game Plan — your three topics, your first interviews, about
   fifty titles, one video a week to start, and your first 90 days on your eight-video plan. It opens with your
   next 7 days. It's in your workspace under Content → Long-Form."*
4. **Save** as `🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` to `03 · Content/Long-Form/` (per
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-setup/references/drive-structure.md`); a refresh saves a new dated copy —
   newest is current. **Keep the Brain's copy** at `~/attraction-brain/exports/youtube-game-plan-YYYY-MM-DD.txt`:
   the document's text, then the **TITLE NOTES** block — one line per title (lane · the exact title · who it is for
   · the pain · why it is on the list: demand / news (dated) / asked / proven / gap / unresearched / starter · and,
   when this pass really saw one, `Seen on YouTube: [link]`) —
   which the `.docx` never carries; ideation and the Monday Kickoff read each title's why from it. A save that
   fails: say it is NOT saved, keep the plan visible in chat, retry once, stop.
5. **Anchor it:** write the `## Game Plan anchors` block in `identity/channel.md` (plan date · doc link ·
   `Cadence: 1/week · since YYYY-MM-DD` (or `2/week`) · `Step-up:` · cycle position · the three lane names · the
   90-day target) and the interview seeds → push via `attraction-brain-sync` → verify (the push re-renders the
   Brain Board). Save fails → say so, keep the plan visible, retry once, stop.
5b. **The calendar in the Brain:** write the first-90-days calendar as dated rows into
   `memory/content-calendar.md → ## Long-form (YouTube)` — the one section this plugin owns inside that
   Short-Form-owned file (its locked shape in `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`): one row per
   video — `#` · Recording date and Publish date (the first-date rule: video 1 on the next filming day at least
   three days out — the day the member gave at setup, `channel.md → Filming day:`, comes first; none on file → the Saturday after next — published two days later, every later row following
   from it; never today) · Week · Bucket · Lane · Title · Guest · Status `Idea` · System ID
   (`yt-YYYY-MM-w[n][a/b]`) · `Reference video` — **left empty here**: the board step (or the Monday Kickoff, when
   there is no board) finds one real video for the row and writes the cell; the `Window:` line under the heading (`YYYY-MM-DD → YYYY-MM-DD · written by
   yt-gameplan · cadence [n]/week · 3 niche · 1 model · 4 interviews`). A refresh replaces un-started `Idea` rows
   whose titles changed (a replaced row starts with an empty `Reference video` cell; a row whose title did not
   change keeps its cell) and never touches a `Scripted` or later row; a cadence change re-dates the un-started rows
   only. **The file absent (a Brain that predates it) → create it now, silently, with this write** — in the
   creation shape `brain-contract.md` prints (the title line, the Short-Form System's empty table and `## Week
   briefs` left for their owner, then this plugin's two `(YouTube)` sections) — and write the rows. Nothing is said
   to the member about it: no "upgrade my attraction brain" line here, at setup's close, or anywhere. Never fill
   the file's short-form table or its `## Week briefs`.
6. **The board** (house rules #11): **inside setup → skip this step entirely** (setup's next step adds the YouTube
   tab and maps the next 30 days). On demand: read the board line now (`identity/publishing.md → Content board:`;
   that file absent → `identity/channel.md → Board:`) — a URL → on a
   refresh, update the board to the new plan (`yt-board`'s rolling rule: un-started cards inside the 30-day
   window are swapped for the new titles, `Scripted` and later cards untouched, one line about what moved);
   an older `declined` → silent; anything else → `yt-board` builds the board (or, with Notion not connected, puts
   the Connect button in the chat once and says how).
7. **Hand off:** inside setup → hand back to `yt-setup` (its Step 7 announces the board next); no closing line
   here. On demand: *"Your Brain Board is updated. Your first video is '[title]' — say 'make my attraction video:
   [title]'. Or say 'set up an agent interview' to invite your first guest."*

## Quality checklist
- [ ] Brain read; goals and ratios from `goals.md`/`scorecard.md`; nothing re-asked; demo mode honored if asked
- [ ] Four Brain files at Step 1, the kit's CALLS TO ACTION table first at Phase 1, the rest opened at their phase, nothing read twice; research that came back empty → the titles marked `unresearched` in the TITLE NOTES, one plain line in Read-this-first, the count in WHAT I CHECKED — never a fourth line in YOUR NEXT 7 DAYS
- [ ] Audit scaled; the positioning read present; the two CTAs stated verbatim from the kit (the guide; the call in the CTA law's shape for the register — `yes` or `unknown` join, `no` open)
- [ ] Three niche lanes (the Problem · Situation · Future buckets), each for a named avatar and pain, each with a playlist; the pillar mapping stated; the lanes that teach drawn from the method's steps and the guide's pages
- [ ] Interview lane with hook-and-transformation titles; pipeline rows seeded at `Candidate` in yt-interview's shape; no invented guests; no promise of the member's time
- [ ] Model lane answers what agents research; mechanics public, compensation private; comparison warning stated
- [ ] ~50 titles by lane; every title passes the hard gates and cites a signal in its note (the Brain's copy only); the UVP's content branches lead the lanes and the bank when the offer carries them
- [ ] The WHY in the positioning band — three statements in the member's voice from the Brain, drafted and labeled where the Brain is empty, never a question box
- [ ] Starter bank opened only when the member had no titles of their own; their captured ideas led; every seeded title marked `starter`, placeholders swapped, lead-gen/CMA titles kept only inside the known-for
- [ ] The goal in conversations and calls — four plain lines in the document, every assumed number labelled "(an assumption — change it any time)", no income
- [ ] The cadence stated once — one a week for the first month, two the step-up — never asked inside setup; the locked order niche · interview · niche · model · interview · niche · interview · interview; ~13 rows at one a week (~26 at two); a new channel's trailer as week one's first row; the first 30 days marked; the step-up checkpoint; 91–180 direction; scoreboard
- [ ] Video 1 (after the trailer on a new channel) is on the topic `channel.md → First full video:` names — the first-video rule, never a question; a plan built with no line on file applied the rule, wrote the line and said the choice and why in one line
- [ ] The first-date rule kept: video 1 recorded on the next filming day at least three days out (the day the member gave at setup, `channel.md → Filming day:`, comes first; none on file → the Saturday after next), published two days later, every later row following from it — no row and no card dated the day the plan was built
- [ ] The document is member-readable: YOUR NEXT 7 DAYS its own block of three numbered lines right after Read this first; one word for a lane; none of "bucket", "SIGNAL", "FOR · PAIN · SIGNAL", "cycle position", "anchors", "unresearched", "starter", "rung", "avatar"; dates in words; the calendar one plain table (Week of · Video · Kind · Guest); MORE TITLES WHEN YOU NEED THEM last, by lane, plain titles; the TITLE NOTES in the export only
- [ ] The progress line said once before the first search; the combined budget (≤10 + ≤8 = ≤18) stated once and kept; the Sources footer lists what was searched and when
- [ ] Stamp present; saved dated to `03 · Content/Long-Form`; the text and the TITLE NOTES kept in `exports/`; anchors (`Cadence:` with its date, `Step-up:`) and the calendar rows written and pushed (the calendar file created silently when a Brain predates it — never a line to the member); the Brain Board re-rendered; handed off; inside setup no chat summary; compliance never a stop or a detour
- [ ] Week 5 wherever the week is named (Week 4 only for short-form); every call ask in the law's shape; nothing promises the member's time per partner; never a skill id or a file path in a line the member reads
