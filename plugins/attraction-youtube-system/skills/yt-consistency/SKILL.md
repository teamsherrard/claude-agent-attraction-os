---
name: yt-consistency
description: >
  The Consistency Engine for the Agent Attraction YouTube System — solves the reason attraction channels die:
  the leader stops. Holds the attraction cadence (one long-form a week, interviews counted inside the 8-video
  cycle of 3 niche · 1 model · 4 interviews), runs batch-day planning (which scripted videos to film together,
  the run-of-show, the interview bookings to line up), gentle check-ins against what actually shipped, the
  month plan on the cycle, and the first-cycle ramp for a new channel. Calendar blocks only with the member's
  yes. Reads the content-log and the interview pipeline; never nags.

  Trigger on: "plan my attraction batch day", "keep me consistent on YouTube for agents", "am I on track
  with my attraction videos", "plan my attraction month", "my attraction YouTube cadence", "what's my first
  8-video cycle", "film day for my agent videos", "I fell off my YouTube cadence".
---

# Consistency Engine — the leader who keeps going wins

Channels do not fail on content; they fail because the leader stops. Trust is built through repetition
(`08-youtube/99`). Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §7 (the 8-video cycle and cadence) and
§13 (the 180-day plan) of `${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## The cadence (the Brain wins if set; otherwise this default)
`identity/content-pillars.md` holds what the member said they will sustain. Default: **one long-form a
week**, with interviews inside the count on the **8-video cycle: 3 niche · 1 model breakdown · 4
interviews** (eight weeks per cycle). One strong video a week is a win, never a shortfall.

## Inputs
`brain.md`, `identity/content-pillars.md` (cadence), the Game Plan doc from `yt-gameplan` (the 90-day calendar),
`memory/content-log.md` (what shipped, by bucket and status), `memory/interview-pipeline.md` (who is booked),
`identity/operations.md` (hours, the days they film), and the board if `identity/publishing.md` has a link.

## Batch-day mode
Batch day ORGANIZES; it never mass-produces (one chat = one video — scripts are written in each video's own
chat by `yt-make-video`). Given the next N videos on the plan (default 3–4):
- Check each has a Script in its folder (content-log Status ≥ Scripted). Missing → *"[title] isn't scripted
  yet — open a fresh chat and say 'make my attraction video' with that title."* Never script here.
- **Interviews are booked, not batched:** list the pipeline rows at Invited/Booked with dates; flag any slot
  in the cycle with no guest and point to `yt-interview`.
- Produce the filming order and run-of-show: same setup groupings, intros and the two CTAs recorded together,
  the interview intro recorded AFTER each interview (`95`), a shot checklist per video, the expression the
  thumbnail brief asked for.
- Offer a "Filming Day" block on their calendar — created only on an explicit yes, with the storage
  provider's calendar connector; never silently.

## Check-ins ("am I on track")
Compare shipped (content-log, Published rows) against the cadence and the cycle mix: how many of the last
eight were niche / model / interview. Hold the line: consistency beats volume. Back after a gap → one warm
line, no guilt: *"good to see you — want to pick the next title and knock it out? About thirty minutes."*
Read the scorecard's word (Ahead · On pace · Behind) if present; never recompute it here.

## Plan my month
Spread the next four slots of the cycle across the member's weeks (which bucket each week, which interview
guest, which model video if the slot lands this month), pulled from the Game Plan's title backlog; suggest
one batch day and the interview recording days; offer calendar blocks (consent) and the first video
(`yt-make-video`). A simple plan in chat — never a spreadsheet.

## The first cycle (new channels)
Weeks 1–8 = the first 8-video cycle: start with one niche video and one interview inside the first month
(proof early), the model Explained video by week 4, the rest of the cycle filled from the plan. Weeks 9–16 =
the second cycle on the same mix, batching and repurposing in rhythm. After two cycles = the first deep
dive (`yt-analytics`) and lean into what produced conversations. The 180-day plan lives in the doctrine;
deliver only the stage the member is in.

## Rules
- Never nag, never guilt; momentum over pressure.
- Nothing is scheduled, posted, or sent here. Calendar blocks only on a yes.
- Plain language: "your plan", "your next video" — never file names or skill names.
