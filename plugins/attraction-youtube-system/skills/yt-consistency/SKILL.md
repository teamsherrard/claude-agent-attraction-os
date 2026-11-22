---
name: yt-consistency
description: >
  The Consistency Engine for the Agent Attraction YouTube System (Week 5) — solves the reason
  attraction channels die: the leader stops. Holds the attraction cadence (one long-form a week for the
  first month, two as the step-up once one has held; interviews counted inside the 8-video cycle of 3
  niche · 1 model · 4 interviews), runs batch-day planning (which scripted videos to film together, the
  run-of-show, the interview bookings to line up), gentle check-ins against what actually shipped, the
  month plan on the cycle, and the first-cycle ramp for a new channel. Calendar blocks only on the
  member's own phrase. Reads the content-log and the interview pipeline; never nags. Trigger on: "plan
  my attraction batch day", "keep me consistent on YouTube for agents", "am I on track with my
  attraction videos", "plan my attraction month", "my attraction YouTube cadence", "what's my first
  8-video cycle for agents", "film day for my agent videos", "block my attraction filming day", "I fell
  off my attraction YouTube cadence".
---

# Consistency Engine — the leader who keeps going wins

Channels do not fail on content; they fail because the leader stops. Trust is built through repetition
(`08-youtube/99`). Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §7 (the 8-video cycle and cadence) and
§13 (the 180-day plan) of `${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

**Week 5 rules that bind every check-in** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **Cadence.** The YouTube cadence is the `Cadence:` line of `identity/channel.md → ## Game Plan anchors`. The
  default is **one video a week for the first month** (the owner, 2026-11-14: twenty things at once overwhelms a
  working leader); Mike's **two a week** is the recommendation the plan names as the **step-up** — proposed by the
  Monthly Channel Review once a month at one has held, or sooner when `identity/goals.md`'s hours clearly carry it
  or the member asks ("change my YouTube pace"). The 8-video cycle holds at either pace (one cycle in eight weeks at one
  a week, four at two). `identity/content-pillars.md`'s cadence line is the short-form (Week 4) cadence — never
  read as the YouTube one.
- **The two CTAs recorded together** are the kit's lines (the Week 3 Kit's chapter 7 CALLS TO ACTION table) — the
  guide ask ("comment GUIDE") and the call ask in the law's shape; nothing filmed on batch day promises the
  member's time per partner.
- **Member-facing words:** Week 5; "your Game Plan", "your next video", "your content board", "your pace", "your
  filming day", "your three topics" / "a topic video"; never lane, niche, bucket, pillar, cadence or B-roll ("extra
  footage") in a line the member reads; the editing next step stated, never hedged, word for word — *"When it's
  filmed, open a new chat and say 'edit my YouTube video' (or 'edit my interview') — your AI Editing Studio edits
  it."*; never a file name, a skill id or a task id in a sentence to the member.
- **Nobody to interview is the normal first-time member.** A conversation week with no guest named takes the next
  video from the member's three topics, and the interview moves to the first open week after a guest is named; no
  week is ever empty, nothing is drafted to nobody, and it is said once, in these words: *"No guest named yet, so
  this week's video is '[title]', from your topics. Your first interview goes on your plan the day you name someone —
  say 'set up an agent interview'."* Never "your team", "your guests" or "the agents you've helped" unless the Brain
  holds such a person.
- **The Monday Kickoff is named only when it is on.** Read `config.md → ## YouTube (Week 5) → Monday Kickoff task:`
  before any sentence that says the Kickoff drafts or keeps anything: a task id → it may be said; anything else →
  the sentence is left out.

## The cadence (the Game Plan anchor wins; otherwise the default)
Read the `Cadence:` anchor. No anchor yet → the default: **one long-form a week**, with interviews inside the
count on the **8-video cycle: 3 niche · 1 model breakdown · 4 interviews** (eight weeks per cycle at one a week,
four at two). One strong video a week is a win, never a shortfall. Two a week is named only as the step-up, with
its condition — never pushed.

## Inputs
`brain.md`, then only three more files now — the rest at the mode that uses them: `identity/channel.md` (the
`## Game Plan anchors`: cadence, cycle position, lane names), `memory/content-log.md` (what shipped, by bucket and
status), `memory/content-calendar.md` → `## Long-form (YouTube)` (the Game Plan's dated 90-day calendar in the
Brain; the section absent → the Game Plan doc from `yt-gameplan`). `memory/interview-pipeline.md` (who is booked)
opens at batch day and at a check-in that counts interviews.
**Opened later:** batch day and "plan my month" → the filming day (`identity/channel.md → Filming day:` first; empty →
`identity/operations.md → Filming window:`), `identity/operations.md` (hours) and the board
if the board line has a link (`identity/publishing.md → Content board:`; that file absent → `identity/channel.md →
Board:`) — **the board already carries the next 30 days at the cadence** (mapped at
setup, and kept full by the Monday Kickoff when it is on): read it as the month, never re-seed it here — a board
that holds less than the month is filled out from the Game Plan's calendar in the chat plan only · check-ins → `memory/scorecard.md` (its word only) · a step-up question →
`identity/goals.md` (the hours).

## Batch-day mode
(Read `identity/channel.md → Filming day:` first; open `identity/operations.md` and `identity/publishing.md` now.) Batch day ORGANIZES; it never mass-produces (one
chat = one video — scripts are written in each video's own chat by `yt-make-video`). Given the next N videos on the
plan (default 3–4 — a month at one a week):
- Check each has a Script in its folder (content-log Status ≥ Scripted — a row the Monday Kickoff set to
  `Scripted` holds only the script start; the full script still needs the video chat). Missing → *"[title] isn't
  scripted yet — open a new chat and say 'make my attraction video: [title]'."* Never script here. **The one
  exception is the first batch:** when three solo videos are still unscripted, say the one phrase instead —
  *"Say 'script my first three videos' and all three scripts are written in one sitting, ready for your filming
  day."* (`yt-script` owns it; interviews are never part of it.)
- **Interviews are booked, not batched:** list the pipeline rows at Invited/Booked with dates. A conversation week
  with no guest named is not on the filming day: it takes the next topic video (the rule above), said once in its
  fixed words — never a list of empty slots.
- Produce the filming order — to the member, "the order of your filming day": same setup groupings, the intros and
  the two calls to action (the kit's lines) recorded together, an interview's intro recorded AFTER the interview
  (`95`), a shot checklist per video, the expression each thumbnail sheet asked for.
- Close with the filming day and the phrase that puts it on their calendar — stated, never offered: *"Your
  filming day is [day]. Say 'block my attraction filming day' and it goes on your calendar."* The "Filming Day"
  block is created only when the member says that phrase (their explicit yes), with the storage provider's
  calendar connector; never silently. **No calendar tool in this session** → the line reads *"Your filming day is
  [day] — put it in your own calendar."* and the phrase is not named.

## Check-ins ("am I on track")
**Nothing published yet** (no YouTube row at `Published`) → no count, no mix, nothing about what is missing — three
short lines: what they have built (only what the Brain shows), their first video by title with its recording day, and
*"say 'make my attraction video: [title]'"*. Otherwise: compare what went out (content-log, Published rows) against
the member's pace and the mix — how many of the last eight were topic videos, the model video, interviews (interviews
counted only when a guest is named). Hold the line: consistency outranks volume. Back after a gap → one warm line, no
guilt: *"Good to see you — your next video is '[title]'. Say 'make my attraction video: [title]' to pick it up."*
Open `memory/scorecard.md` now and read its word (Ahead · On pace · Behind) if present; never recompute it here, and
never say "Behind" to the member — name the next video instead.
One a week held for a month and the member asks about more → read `identity/goals.md`'s hours and say in one
line whether two a week fits their week ("your pace" to the member); the change itself is "change my YouTube pace" (the Game Plan writes the anchor).

## Plan my month
Spread the next videos on the Game Plan across the member's weeks at their pace (four at one a week: which of their
three topics each week, an interview only where a guest is named — a conversation week with no guest takes the next
topic video — and the model video if it falls in the month) — from the board's next 30 days
when there is one (the dated cards ARE the month; read them, never re-seed), else from the Game Plan's calendar;
name one filming day and, where a guest is named, the interview recording days; close with the two next steps — stated, never offered:
*"Say 'block my attraction filming day' and those days go on your calendar. Say 'make my attraction video:
[title]' to start the first one."* (the calendar blocks only on that phrase — the member's explicit yes; no calendar tool in this session → the first
sentence reads *"Put those days in your own calendar."*; the
video is `yt-make-video`'s). A simple plan in chat — never a spreadsheet.

## The first cycle (new channels)
At one a week the first month is **niche · interview · niche · model** — to the member: a topic video, a
conversation with an agent, a topic video, your model video — authority first, proof inside the first month, the
model Explained video by week 4 (Why I Switched may go early in cycle one when the journey holds the story); the cycle
completes in eight weeks, the second cycle on the same mix, batching and repurposing in rhythm. **Nobody to interview
yet** → the conversation weeks take the next topic video and the interviews go on the plan the day a guest is named
(the rule above) — said once, never as a gap. At two a week the same order runs in four weeks. Once videos are out,
the deep dive (`yt-analytics`) is there on demand — lean into what produced conversations. The 180-day plan lives in the doctrine; deliver only the stage the member is in.

## Rules
- Never nag, never guilt; momentum over pressure.
- Nothing is scheduled, posted, or sent here. Calendar blocks only when the member says the phrase ("block my
  attraction filming day") — named once as a statement, never offered, never silent.
- Plain language: "your Game Plan", "your next video", "your pace" — never file names or skill names.
