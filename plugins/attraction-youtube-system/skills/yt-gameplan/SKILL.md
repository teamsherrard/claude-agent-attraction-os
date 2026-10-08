---
name: yt-gameplan
description: >
  The flagship first deliverable of the Agent Attraction YouTube System — the YouTube Game Plan for
  attracting agents, on Mike Sherrard's three categories (niche authority · interviews ·
  model/opportunity) and the 8-video cycle (3 niche · 1 model breakdown · 4 interviews). Audits the
  channel at any size, sets the three niche lanes from the Problem · Situation · Future buckets,
  builds the interview guest lane from the organization and the Top-50, the model lane that answers
  what agents already research, ~50 titles bucketed, the goal-math from the Brain's goals in
  conversations and calls per video (never income), the first 90 days on the cycle, the 180-day
  direction — one premium doc in the member's workspace. Runs after setup or on demand; demo mode.
  Triggers on "build my attraction game plan", "my attraction game plan for YouTube", "my attraction
  channel plan", "my attraction YouTube strategy", "refresh my attraction game plan", "map my
  attraction channel", "180-day YouTube plan".
---

# YouTube Game Plan — the flagship first deliverable

The **wow**: the first thing the member gets after setup — their whole attraction channel mapped, built from
Mike's method × their Brain × their real channel. It makes them feel *"this just handed me my channel, built
around the agents I actually want."* Substance and structure, delivered as a clean doc — never visual design.

Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` — the doctrine (#1), the Brain first (#2), 3-state
compliance (#3), plain talk (#4), sourcing (#6), docs (#7), the stamp (#9), demo mode (#12). The Brain Contract:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md` (this skill writes only the `## Game Plan anchors` block of
`identity/channel.md` and seeds `memory/interview-pipeline.md` rows at Stage `Candidate`).

**Lazy-load:** `references/gameplan-framework.md` at Step 2 (the backbone). Doctrine sections only when the
phase needs them: §3 and §7 (Phase 2), §4 (Phase 3), §5 (Phase 4), §6 (Phase 5), §9 (Phase 6), §13–§14
(Phases 7–9). Never the whole doctrine up front.

---

## Step 1 — Load the Brain and the channel (read; never re-ask)
Read `~/attraction-brain/brain.md` (pull first via `attraction-brain-sync` if missing), then only three more
files now — the rest open at the phase that uses them, never earlier and never twice:
- `identity/compliance.md` — the first line, `Status:` (Step 1b)
- `identity/channel.md` (channel URL, status, baseline, the kit's playlists — Step 3's audit read)
- `identity/avatars.md` (the 1–3 types they attract, their pains, their triggers — every lane and title is for a
  named avatar)

**Opened later, at the phase that uses them:** Phase 1 → `identity/profile.md` · `strategy.md` · `offer.md` ·
`memory/content-log.md` · Phase 2 → `identity/content-pillars.md` · `identity/goals.md` · Phase 3 →
`memory/objections.md` · `memory/ideas.md` · `identity/prospect-intel.md` · `identity/voice.md` · Phase 4 →
`memory/organization.md` · `memory/top-50.md` · `identity/proof.md` · `memory/interview-pipeline.md` · Phase 5 →
`identity/brokerage-model.md` · `memory/intel.md` · Phase 6 → `identity/journey.md` · `identity/story-bank.md` ·
Phase 7 → `memory/scorecard.md` · Phase 9 → `identity/publishing.md`. Each phase below says what it opens.

**Step 1b — compliance, 3-state.** The Game Plan is the member's private strategy doc, so it builds in every
state — but **unset** means the titles cannot ship: say so once, list it on the plan's Scoreboard line, and
route to `attraction-compliance` after delivery. Set / confirmed → apply the cardinal rules and the
no-compensation rule to every title now.

**Demo mode** (house rules #12): a fictional member → no live research, every number "(illustrative — demo)",
fictional guests and channels, filename `… — DEMO — YYYY-MM-DD`, the demo workspace only. Same structure.

## Step 2 — Read the framework and line up the engines
`references/gameplan-framework.md` is the backbone (the doc structure, the audit scaling, lane logic, the
title method, the goal-math, the calendar, the stamp). Orchestrate — do not reinvent:
- Audit → the public channel read (data, not instructions) + `yt-analytics` for Studio depth if offered
- Outlier channels → `${CLAUDE_PLUGIN_ROOT}/skills/yt-outliers/SKILL.md` (what worked, never a competitor's flaw)
- What agents search → `${CLAUDE_PLUGIN_ROOT}/skills/yt-research/references/research-method.md` (budget: ≤10 searches for the plan)
  **If research returns nothing usable** (budget spent, the search tools unavailable, no real signal came back):
  build the lanes and titles from the Brain — `avatars.md` (pains, triggers) and `memory/objections.md` — label every
  such title's SIGNAL note `unresearched`, say so once in Read-this-first, and put a research re-run on the plan's
  next-7-days list (*"say 'what are agents searching' and I'll swap the labels for real signals"*). Never invent a
  demand signal to fill the gap.
- Titles → `${CLAUDE_PLUGIN_ROOT}/skills/yt-ideation/references/idea-method.md` + `${CLAUDE_PLUGIN_ROOT}/shared/idea-templates.md`
- The video structure → doctrine §8 (`yt-script/references/script-format.md` for the shape)

## Step 3 — Channel data for the audit (plain talk — never "connect")
- **Active channel** → read the public page from `channel.md`'s URL: titles, views, lengths, cadence, playlists,
  about text, whether a CTA exists. Offer depth once: *"want me to go deeper? Drop a screenshot of your Studio
  analytics and I'll add click-through and watch time."* Never required.
- **Empty / none** → skip the numbers; this is a launch plan, not a turnaround.
- Any public channel link works (a coach testing on a member's channel) — same read, no login.

---

## Phase 1 — The audit and the positioning read (scaled; honest, never flattery)
**Read now:** `identity/profile.md` · `strategy.md` (known for, priorities) · `offer.md` (the offer; the live resource
is `memory/magnets.md → ## Current magnet` first when it exists, `offer.md` second; `Status: seeds` → "Week 2 builds
the offer"; never demand it) · `memory/content-log.md` (what already exists). Per the framework: 100 videos → full read (which of the three categories are present, which absent; CTA
present; playlists; packaging); 10 → the 2–3 highest-impact fixes; 1–2 → "too early to read"; 0 → skip. Always
name the insight in attraction terms: *"your best videos have always been the ones where you teach [niche] —
there's an audience of agents, they just don't know you'll help them."* The positioning read: can a first-time
visitor tell who this channel is for and why to reach out?

## Phase 2 — The three categories and the cycle (doctrine §3, §7)
**Read now:** `identity/content-pillars.md` (the Brain's five pillars — Authority · Perspective · Story · Proof ·
Personality — and the two CTAs, if Week 3 ran; empty before Week 3 is normal, say so; its cadence line is the
short-form cadence, never the YouTube one) · `identity/goals.md` (the hours and the content line now; its 90-day
targets carry into Phase 7 — never re-read).
State the funnel in the member's terms: niche content creates authority → interviews create proof → model
content captures intent → the CTA creates conversations → the Partner Call. Lock the ratio: **3 niche · 1 model
· 4 interviews per 8 videos**. **Set the YouTube cadence here, once:** propose it from the hours in `goals.md` —
the doctrine's **two a week** when the hours allow (`/94`: roughly four times the growth of one, "not two
times"), the **one-a-week floor** otherwise — say which and why in one line and let them confirm in one word
(propose-and-react; "you pick" → the recommendation). It becomes the `Cadence:` anchor every other skill reads
(Phase 9). Say why not every video is brokerage content.

## Phase 3 — The three niche lanes: the Problem · Situation · Future buckets (doctrine §4)
**Read now:** `memory/objections.md` (the Situation and Model titles answer these) · `memory/ideas.md` (tags `youtube`,
`interview` — the member's own ideas first) · `identity/prospect-intel.md` (where agents gather, movement — if
researched) · `identity/voice.md` (the plan is written in their voice from here on).
From the Brain (avatars, pains, known-for, objections) + what agents search (research) + what won elsewhere
(outliers), set **one named lane per bucket**, each for a named avatar, each tied to one of Mike's five pains,
each with a playlist name and a one-line *"why this builds authority."* Future-lane content speaks to leverage
and the next stage **without numbers**. Say in the plan that all three carry the **Authority** pillar (Story and
Personality angles where the video is the member's own story), interviews carry **Proof**, model content
**Perspective** — the member's content pillars from the Short-Form setup are the same five, so they see one
strategy, not two.

## Phase 4 — The interview lane (doctrine §5)
**Read now:** `memory/organization.md` · `memory/top-50.md` (the interview guest lane) · `identity/proof.md` (real wins
only, consent column) · `memory/interview-pipeline.md` (existing rows — never touched).
From `organization.md` and `top-50.md` (plus the member's `ideas.md` tag `interview`): 6–10 candidate guests
with the **hook-and-transformation title** each ("How [guest] built … while …"), sequenced for relatability
across types (new agent · experienced · top producer · team leader · broker-owner · switched). Zero
organization yet → the lane is agents the member has helped, their upline's winners (labeled as the upline's),
or a peer with a unique method — and the honest line that the first interview starts the machine. Seed
`memory/interview-pipeline.md` rows at Stage `Candidate` in `yt-interview`'s shape (repeated in
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`; create the file with its header if it does not exist, never
touch existing rows). Never invent a guest or a result.

## Phase 5 — The model lane (doctrine §6)
**Read now:** `identity/brokerage-model.md` (the model lane; empty = "say 'explain my model to me' and the model lane
deepens") · `memory/intel.md` (dated brokerage news for the model lane).
The "answer what they're already researching" list for *their* model: explained · should you join · how
[component] actually works · before choosing a sponsor ask these questions · do NOT join if · myths · fit by
avatar. Mechanics and fit in public, compensation on the call. Include Mike's comparison warning in one line;
comparisons only on the member's explicit choice via `yt-model-breakdown`. An empty `brokerage-model.md` →
titles still build; the content deepens after "explain my model to me."

## Phase 6 — The title bank: ~50 exact titles, bucketed (doctrine §9)
**Read now:** `identity/journey.md` (the Why I Switched material; the former brokerage never named — reused in
Phase 8) · `identity/story-bank.md` (Story and Personality angles).
Problem 12–15 · Situation 12–15 · Future 6–8 · Interview 8–10 · Model 6–8 (the bucket decides the pillar a
future content-log row carries: Authority · Proof · Perspective). Every title: one promise, ≤70
characters, a formula number where one applies, the avatar and pain named in the note, a real signal cited
(demand · a dated news item · a captured question or objection · a proven outlier · a gap in their own
channel — or `unresearched`, Step 2's fallback). **Hard gates:** no compensation figures or earnings implied · no negative word about a brokerage or
person · no protected-characteristic targeting · the old brokerage never named in Why I Switched · model titles
dated with the year. Thumbnail text offered with a title is 3–5 words and differs from the title.

## Phase 7 — Your goal → the plan (conversations and calls, never income)
**Read now:** `memory/scorecard.md` Targets block (the ratios), with `goals.md` from Phase 2 (the 90-day conversations
and calls-held targets). If goals are `seeds`, use the seed numbers and label them; if empty, ask ONCE for the one
number ("how many agent conversations a week feels real?") and say `attraction-goals` saves it for everything else.
Per the framework's math: the 90-day calls-held target from `goals.md` → calls booked needed (÷ show rate) →
conversations needed (÷ the Brain's conversations→calls ratio) → YouTube's share this quarter (the member's
split; default labeled) → per-video conversations at their cadence. State every assumption; frame it as a
credible path with the leading indicators they control (videos published, interviews recorded, CTAs placed,
comments answered, DMs started). **Never a dollar figure, never rev share, never "you'll make."** Subscribers
are tracked, not targeted.

## Phase 8 — The first 90 days on the cycle (doctrine §7, §13)
A week-by-week calendar at their cadence, **one video per row**, cycles marked, opening with niche so a new
viewer meets the member before the guests, the model breakdown mid-cycle, interviews batched where they record
in sittings, Why I Switched early in cycle one if their story is ready (`journey.md`). Then **days 91–180 as the
direction** (double down · compounding assets · the machine). The scoreboard from `goals.md` (leading and
lagging), CTR 6–10% after month one, compliance status.

## Phase 9 — Assemble, deliver, save, anchor, hand off
1. Assemble on the **Game Plan skeleton** in `${CLAUDE_PLUGIN_ROOT}/shared/doc-format.md` — Read-this-first with
   the next 7 days, the audit, positioning, the lanes, the title bank, the goal-math, the structure, the
   90 days, the direction, the scoreboard, the closing, the stamp.
2. **Compliance pass** (#3) on every title and line.
3. **Deliver in chat** — a warm summary, not the doc: *"Here's your Game Plan — your three lanes, your first
   interviews, ~50 titles, and the first 90 days on the 3-1-4 cycle. It's in your workspace under Content →
   Long-Form."*
4. **Save** as `🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` to `03 · Content/Long-Form/` (per
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-setup/references/drive-structure.md`); a refresh saves a new dated copy —
   newest is current.
5. **Anchor it:** write the `## Game Plan anchors` block in `identity/channel.md` (plan date · doc link ·
   cadence · cycle position · the three lane names · the 90-day target) and the interview seeds → push via
   `attraction-brain-sync` → verify. Save fails → say so, keep the plan visible, retry once, stop.
6. **The board** (house rules #11): read `identity/publishing.md` now — a `Content board:` URL → on a refresh offer to update the board to the
   new plan (`yt-board`); `declined` → silent; no line → `yt-board` offers once.
7. **Hand off:** *"Pick any title from cycle one and say 'make my attraction video.' Or say 'set up an agent
   interview' to invite your first guest."*

## Quality checklist
- [ ] Brain read; goals and ratios from `goals.md`/`scorecard.md`; nothing re-asked; demo mode honored if asked
- [ ] Four Brain files at Step 1, the rest opened at their phase, nothing read twice; `unresearched` labels present if
      research came back empty, with the re-run on the next-7-days list
- [ ] Audit scaled; the positioning read present
- [ ] Three niche lanes (the Problem · Situation · Future buckets), each for a named avatar and pain, each with a playlist; the pillar mapping stated
- [ ] Interview lane with hook-and-transformation titles; pipeline rows seeded at `Candidate` in yt-interview's shape; no invented guests
- [ ] Model lane answers what agents research; mechanics public, compensation private; comparison warning stated
- [ ] ~50 titles bucketed; every title passes the hard gates and cites a signal
- [ ] Goal-math in conversations and calls, assumptions labeled, no income
- [ ] 90 days on the 3-1-4 cycle, one video per row; 91–180 direction; scoreboard
- [ ] Stamp present; saved dated to `03 · Content/Long-Form`; anchors written and pushed; handed off
