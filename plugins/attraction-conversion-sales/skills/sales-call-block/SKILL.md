---
name: sales-call-block
description: >
  Sales OPS: the daily call block and the capacity math. Takes the weekly calls and conversations
  target from the Brain's goals and the hours from operations, and returns how many partner-call slots a
  day, when, how long, with the prep slot before the block and the debrief slot after each call, the
  conversation block kept separate, and the honest check that the target fits the hours. Show rate from
  the sales scorecard once it has data, a labelled planning assumption until then. Writes the block to
  the Brain's sales system and renders the Daily Call Block Planner. Member sets availability in the
  tool. Trigger on: "plan my call block", "how many calls a day", "my daily call block", "call capacity",
  "when should I take partner calls", "call block planner", "do my calls fit my hours", "slots per week
  for agent calls", "partner call schedule".
---

# Call Block — the slots that make the weekly number real

Mike took calls 10 to 2, thirty minutes each, eight a day at scale — and in year one, one-hour calls across
a much wider window, "as flexible as humanly possible… convenient for them, not you" (bonus: Calendly;
`10-presentation-delivery/42`). The member's number comes from their own goals: this skill turns "N calls a
week" into a block they can keep, inside the hours they actually have, with the prep and the debrief built
in — because a call without prep and without a debrief is a call that doesn't convert.

**Write-and-prepare.** The block is written to the Brain and a planner doc; the member sets their
availability in Calendly or GoHighLevel. Nothing is booked, moved, or blocked on a calendar from here.

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`, `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`. One stop, 2–3 questions, ~5 minutes.

## Step 1 — Load the Brain (never ask what it knows)
`~/attraction-brain/brain.md`, then `identity/goals.md` (**weekly activity**: conversations, calls,
follow-ups; **hours** per week for attraction; the daily slice), `identity/operations.md` (working hours,
the existing call block line, call length, where, the timezone lives in `config.md`), `identity/
sales-system.md` (tool, event length), `memory/scorecard.md` + `memory/sales-funnel.md` (booked vs held
— the real show rate, when four or more weeks exist), `memory/pipeline.md` (how many at Call booked now).
No locked goals (`Status: seeds`) → say the block needs the weekly number first: "say 'set my attraction
goals' — ten minutes — then I'll size the block." Missing locally → `attraction-brain-sync`. A tool error
is never "no Brain".

## The math (shown to the member in plain lines — every assumption labelled)
- **Calls per week** = `goals.md` weekly calls (the controllable).
- **Slots per week** = calls per week ÷ show rate. **Show rate** = held ÷ booked from the sales funnel
  when four or more weeks exist; until then a **planning assumption** the member confirms (propose "plan
  one spare slot for every four calls" and label it "assumption until your scorecard has a month of data"
  — never a quoted industry number).
- **Slot length** = call length (`sales-system.md`: 60 to start, 30 once mastered) + **15 minutes** (the
  10-minute debrief with `cv-debrief` and a breath). Mike ran back-to-back at scale; a member in year one
  does not.
- **Prep** = one block before the day's calls, not per call: the Call Block Prep agent (`cv-call-prep`,
  daily) has the briefs ready; the member reads them in 15 minutes for the day.
- **Conversations block** = separate from calls, sized from `goals.md` conversations per week ÷ working
  days, at the member's best DM hours — "you do not open conversations between calls."
- **Fit check** = slots × slot length + prep + conversations block + follow-up time (`goals.md` follow-
  ups per week × 5 minutes) must sit inside `goals.md` hours. If it doesn't, say so in one line and offer
  the two honest moves: fewer calls this quarter (and re-run the goals), or more hours. Never squeeze the
  math.

## Stop 1 · Shape the block (2–3 questions, proposed from the Brain)
Orient: *"Here's the math from your goals: [N] calls a week at [length] minutes means [n] slots. Three
quick questions to shape the block."*
1. **Which days and window?** Propose from `operations.md` hours: the days with the most open hours, a
   window agents can actually hit (late morning to mid-afternoon in their time zone; evenings only if the
   member said evenings are fine — never assume). Mike's 10–2 is the example, not the rule.
2. **Back-to-back or spaced?** Propose spaced (the 15-minute buffer) until the held→join rate holds.
3. **Where does the conversations block go?** Propose first thing or right after lunch — whichever
   `operations.md` leaves open.
**Your turn.** "You decide" → the proposed block, confirmed in one word.

## Write it (this plugin's file) and the planner
Update `identity/sales-system.md → ## Calendar → Window:` with the block in one line (days · window · slot
length · spacing · the prep slot · the conversations block) and add a `## Call block` section:
```
## Call block (set [YYYY-MM-DD] by sales-call-block)
Calls/week target: [N] (goals.md) · Show-rate used: [x%, real from n weeks | planning assumption] · Slots/week: [n]
Days · window: [Tue/Wed/Thu · 10:00–13:00] · Slot: [30+15] min · Max/day: [k]
Prep: [15 min at 9:30 — Call Block Prep briefs] · Debrief: [10 min after each call — cv-debrief]
Conversations block: [daily 8:30–9:15 — [x] conversations/day] · Follow-ups: [Fri 13:00–13:45]
Fit: [fits inside goals.md hours | over by [h] — member chose: fewer calls | more hours]
```
If `operations.md` carries a different call block line, say in one line that the operations skill mirrors
this ("say 'update my operations' to copy it over"); this skill never writes `operations.md`.
Render the Daily Call Block Planner per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md`: the math in a
table, the weekly grid, the per-call rhythm (prep brief → call → 10-minute debrief → recap email draft),
the availability settings to enter in their tool, via
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/call-block.txt "Daily Call Block Planner — [Name] — [YYYY-MM-DD].docx" --title "Daily Call Block Planner" --subtitle "[Name] · [Organization]"`
(read back; `RENDERER-UNAVAILABLE` → install nothing, upload the `.md`), upload to the workspace's `05 · Offer`
folder. Then `attraction-brain-sync` PUSH, verify, one step.

## Confirm (and the hand-offs)
*"Your call block: [days], [window], [k] calls a day at [length] minutes with a buffer — that's [n] slots a
week for your [N]-call target, and it fits inside your [h] hours. Set those hours as your availability in
[tool]. Your Call Block Prep briefs land each morning [if the agent is on; else: 'say "prep my calls" each
morning']. Your turn."* Re-run on "re-plan my call block" after the scorecard has a month of real show rate,
or whenever the goals change.

## Demo mode
Fictional member, every figure "(illustrative — demo)", DEMO in the filename, nothing written to a real Brain.

## Quality bar
Every number traces to `goals.md`, `operations.md`, or a labelled assumption; the fit check is honest; the
block respects the member's stated life (no invented evenings); the so-what test (each number ends in a
slot on a day); no "optimize your calendar" filler.
