---
name: attraction-goals
description: >
  The Brain's goals skill, on demand after setup: reads the four numbers Brain setup captured
  (agents today, the 12-month number, the long-term goal, hours a week), proposes the 90-day join
  target and the weekly activity the member controls (conversations, calls, follow-ups), confirms
  them, and locks the plan: 12-month milestones and 30-60-90 targets in identity/goals.md, the
  Targets block in memory/scorecard.md, and the 90-Day Attraction Scorecard. The money math (the Rev
  Share Calculator's scenarios) runs only when asked and never reaches the Brain Book. Weekly
  check-in, monthly audit and quarterly refresh modes. Trigger on: "set my attraction goals", "my
  90-day attraction target", "how many agents do I need", "how many conversations per week", "my
  attraction scorecard", "attraction weekly check-in", "am I on pace to my join target", "refresh my
  attraction plan", "plan my next attraction quarter", "set my agent targets", "update my money
  math", "lock my attraction plan".
---

# Attraction Goals — the destination, reverse-engineered into this week (on demand, after setup)

Every other skill helps the member *do* the work. This one tells them **which work, and how much**:
*you want **N agents** in 12 months, so your 90-day number is **n joins**, which at your ratios is
**this many conversations a week** — and here is the scorecard that tracks it.* The numbers serve the
why; the why is what re-anchors them in week six when joins lag activity.

**Where this runs.** Brain setup captures only the four numbers (Conversation 4 — agents in your revenue
share organization today · how many you realistically want to attract in the next 12 months · your
long-term goal · hours a week you can fully commit) and writes a proposed weekly rhythm labelled
"proposed". This skill is the on-demand step that **locks** the plan — the member comes to it when they
want the real target and the scorecard — plus **the rhythm**: the weekly check-in, the monthly audit, and
the quarterly refresh. When the Brain already holds locked goals, READ them and refresh — never re-ask what
setup captured. **Never asked:** the first agent (the Top-50 names them), the money (the calculator, only
when asked).

**~5 minutes to lock; ~3 minutes for a weekly check-in.**

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`
and obey them: plain language, no machinery in front of the member, one or two short questions at most,
"your turn", propose-and-react when they are unsure, honour "skip" and "use defaults". **Defaults are
full-quality:** a member who is unsure still leaves with a real, specific, math-checked plan built from their
Brain, labelled as assumptions they can adjust.

## Step 1 — Load the Brain (never ask what it knows)
Read `~/attraction-brain/brain.md`, then only what this needs:
- `identity/goals.md` — the four numbers from setup under "Your numbers", the why, the proposed weekly rhythm; if `Status: locked`, this is a refresh, not a first run.
- `identity/profile.md` — years in, brokerage, team or solo.
- `identity/journey.md` + `identity/strategy.md` — the why and the vision.
- `identity/avatars.md` — who their story speaks to (the shape of a realistic join).
- `identity/brokerage-model.md` — plan mechanics, only if the money is asked for (often not built; fine).
- `identity/leadership.md`, `identity/operations.md` — capacity and hours, if built (empty is normal).
- `memory/scorecard.md` — if the Targets block exists, this is a refresh.
- `memory/organization.md` — agents in the org today, if any rows exist.

If `~/attraction-brain/` does not exist locally, pull it via `attraction-brain-sync` first. A tool error
is never "no Brain" — say which connector failed and retry once; never suggest re-running setup. If no
Brain exists anywhere, tell them to say "set up my attraction brain" and stop. If `goals.md` holds no
numbers at all (setup was skipped there), ask the four in one short card — the only time this skill asks them.

## The doctrine this skill enforces (from Mike's Week 1 lessons)
- **Realistic over heroic.** Unrealistic expectations are what guarantee failure; the people who want
  300 agents in year one are usually the ones who are not consistent (`01-foundation-mindset/8`). Three
  hard years, then the compounding does the work. Never let a member anchor on a number that makes
  month two feel like failure.
- **Set the outcome, commit to the actions.** The agent target has uncontrollable variables; the actions
  (conversations, calls, content shipped) are controllable with certainty (`01-foundation-mindset/8`).
  Every outcome in this plan is paired with the activity that produces it, and the scorecard tracks the
  activity first.
- **Singles win the game.** Do not build the plan around one whale — the big team, the influencer — who
  may never join. Enough singles, consistently, and the home run finds you (`01-foundation-mindset/9`).
- **Compare only to yourself.** Last week, last month — never another member's numbers
  (`01-foundation-mindset/8`). The check-in never cites anyone else's results.
- **Audit monthly, tangible and intangible** (`01-foundation-mindset/8`): did you attract the agents you
  wanted — if not, why; did you convert the majority you spoke with — if not, why; did you stay
  consistent with content — if not, why. Plus the intangibles: confidence on camera, confidence explaining
  the model, confidence on calls. The monthly audit asks exactly these.
- **The why carries the hard days** (`01-foundation-mindset/10`). Who are they doing this for? Written
  down, in their words, read back at every check-in — never as guilt.
- **Residual income compounds** (`01-foundation-mindset/7`). January 1 starts where December 31 left
  off. That is the reason the plan is a 12-month plan with quarters, not a 30-day sprint. Mike's own
  figures in that lesson are Mike's story — quote them as his if asked, never as an expectation.

## LOCK mode ("set my attraction goals" · "lock my attraction plan" · the first run after setup)
Orient: *"Your numbers are already in your Brain — [N] agents today, [N] in 12 months, [N] long term, [N]
hours a week. I'll turn that into this quarter's target and your weekly activity; you confirm."*

1. **Propose the 90-day join target — never ask it cold.** Ramp, never flat: a member starting attraction
   from a standing start gets roughly **15% of the 12-month number in the first quarter** (quarters ramp
   about 15 / 20 / 30 / 35%, a planning assumption, labelled); a member who already has conversations
   flowing gets about 25%. Minimum 1. Show the working in one line.
2. **Propose the ratios** — conversations → calls held **25%** (a starting assumption from no lesson; say
   so; thirty days of scorecard rows replace it) · calls held → joins **50%** (Mike's floor,
   `16-implementation-scaling/78` — below it the model explanation, the value proposition, or the
   objection handling needs work; a benchmark to grow into, not a promise).
3. **Derive the weekly activity** — `weekly conversations = (90-day joins ÷ calls→joins ÷
   conversations→calls) ÷ 13`, the calls it implies, follow-ups at about the same count as conversations —
   and check it fits inside the hours from setup.
4. **One question:** *"Does this weekly activity feel realistic inside your [N] hours? Adjust the target or
   the hours, not the math."* **Your turn.** If it does not fit, say so plainly and offer the two honest
   moves: lower the 90-day target, or find the hours. Re-derive once.
If the 12-month number sounds like a hundred-agent first year, one gentle line from the lesson and their
number stands — the ramp does the rest.

## The money, honestly — ONLY when asked ("run my rev share scenarios" · "update my money math")
Never part of locking the plan, never part of setup, never in the Brain Book. When the member asks, call
`attraction-rev-share-calculator` with: mechanics (from `brokerage-model.md`, or "explain mine to me") ·
organization size today · the 12-month target · the member's own production estimate for the agents they
attract (asked once, labelled "member's estimate") · the ratios. It returns three scenarios (conservative /
target / stretch), every number "(illustrative)", with its compliance stamp; the block lands in `goals.md`
→ "The money, honestly" verbatim. **This whole block is private material.** It goes in the Brain only;
never into content, DMs, ads, a lead magnet, or the Book (`identity/compliance.md` gate; the calculator's
stamp says so).

## Build `identity/goals.md` (the locked shape — every section, no brackets left behind)
Keep the template's headings exactly (the setup "Your numbers" table stays as written). Fill:
```
## The why                       [verbatim, their words]
## Your numbers                  [the setup table, untouched]
## 12-month milestones (set [date])   | Measure | Today | 12 months | — agents (frontline) · conversations (weekly × 52) · calls held · joins (N minus today) · rev share row: "private-call material — the calculator, on request"
## 30-60-90 (quarter [start] → [end])  | | Day 30 | Day 60 | Day 90 | — conversations · calls held · joins (Day 90 = the target) · content shipped · agents in organization — ramped, never flat
## Weekly activity               the proposed line replaced by the locked numbers: conversations · calls · follow-ups · content ("set with the Short-Form system in Week 3" until then) · daily slice (weekly ÷ working days, default 5) · "Does this feel realistic?" — their answer
## Ratios                        conversations → calls [..] ([member / default]) · calls held → joins [..] ([member / Mike's benchmark floor])
## The money, honestly           untouched unless the calculator ran
## The 12-month plan             "build my execution framework" once locked
## First agent                   untouched — named on demand (the Top-50)
## Hours                         the hours from setup; the split (conversations / calls / content / follow-up)
## Intangibles to track          confidence on camera · explain the model without notes · objections handled calmly · the consistency streak
```
Status rules: `seeds` until the member has confirmed the 90-day target and the weekly activity; then
`locked [date] (quarter [start] → [end])`. A locked file is what the Debrief and the Admin read as the target.

## Seed `memory/scorecard.md` (the ONE block shape — the Debrief and the Admin append to it)
```
# [Name] — 90-Day Attraction Scorecard
*memory · the numbers against the 90-day targets · targets by attraction-goals · daily rows by attraction-debrief · weekly rows by the weekly check-in (the AI Admin's scorecard once installed)*

## Targets (locked [date] · quarter [start] → [end])
| Measure | 12-month | 90-day | Weekly activity |
|---|---|---|---|
| Agents in organization | | | — |
| Conversations | | | |
| Calls held | | | |
| Joins | | | |
| Content shipped | | | |
| Rev share (illustrative) | | | — |
Ratios: conversations → calls [..] · calls held → joins [..] · Daily slice: [..] conversations / [..] calls

## Weekly rows
| Week of | New prospects | Conversations | Meaningful conversations | Calls booked | Calls held | 3-ways | Joins | Content shipped | Score | Note |
|---|---|---|---|---|---|---|---|---|---|---|

## Daily rows
| Date | Conversations | Calls booked | Calls held | Joins | Content shipped | Score | Note |
|---|---|---|---|---|---|---|---|
```
The "Rev share (illustrative)" row stays empty unless the calculator ran, and even then reads "private-call
material". Score vocabulary, locked: **Ahead** (≥ 150% of the slice), **On pace**, **Behind**. Never a grade,
never a percentage the member has to interpret. If `scorecard.md` already exists, replace ONLY the Targets
block and leave every row untouched. **The weekly row's columns are the AI Admin's seven KPIs in its
order** (new prospects · conversations · meaningful conversations · calls booked · calls held · 3-ways ·
joins), then content shipped · score · note — the same header in the Brain template and
`admin-recruiting-scorecard`; never a new column. The daily rows keep their shorter shape (the Debrief's).

## Render the 90-Day Attraction Scorecard (the deliverable they hold — on lock, never at setup)
Assemble the structured text per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` (read it now, not
earlier): title, meta line, CAPS bands, pipe-row tables for the targets, the 30-60-90, the weekly
activity, and a one-page "how to use this weekly" band. No money table unless the calculator ran and the
member asked for it in the document (then with the stamp line under it). Then:
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/scorecard.txt "🎯 [Name]'s 90-Day Attraction Scorecard — [YYYY-MM-DD].docx" --title "90-Day Attraction Scorecard" --subtitle "[Name] · [Market]" --eyebrow "Agent Attraction Brain"`
Read the `.docx` text back (no `<w:` markup, every table present), upload it to the workspace's
`01 · AI Brain/` per `${CLAUDE_PLUGIN_ROOT}/shared/drive-map.md`, and hand them the direct link.
Dated filename; the newest is current. **If the renderer prints `RENDERER-UNAVAILABLE`, do exactly
what it says: install nothing, save the structured text as a `.md`, upload that, and say in one line
that the styled version needs the renderer.** One corrective re-render at most; never a loop.

## Write → push → verify, then confirm
Write `goals.md` and `scorecard.md`, then run `attraction-brain-sync` (PUSH) immediately and verify —
one atomic step; an unsynced write is a lost write. Refresh `brain.md`'s "This week's activity target"
line from the locked numbers (the one quick-reference line this skill owns). Confirm in their words:
*"Your targets are set — [N] agents in 12 months, [n] joins this quarter, which means about [x]
conversations and [y] calls a week. Your scorecard is in your home base, and 'run my debrief' scores each
day against it (or 'turn on my daily debrief' to make it automatic)."* Only if the AI Admin is installed
add: *"— and your morning brief carries your weekly activity."*

## WEEKLY CHECK-IN mode ("attraction weekly check-in" · "am I on pace" · Mondays via the Debrief)
~3 minutes, never a re-interview:
0. **Open with the why** — one line, theirs: *"Week [n] of the plan you're running for [why]. Here's
   the score."* When they are behind, the why is the re-anchor, never the stick.
1. Read `goals.md`, `scorecard.md` (last week's daily rows), `memory/conversations.md`,
   `memory/pipeline.md` (the Stage moves log), `memory/top-50.md` (rows added this week),
   `memory/content-log.md`, `memory/deadlines.md`; and, when they exist, `memory/sales-funnel.md`
   (show rate, held→join — or a `WEEKLY ROW:` line `sales-scorecard` handed over this session) and
   `memory/list-growth.md` → the newest row's **"Calls booked from the funnel"** (the Lead Magnet plugin's
   ledger, kept from Week 2; skip silently if absent). If `goals.md` is still `seeds`, run LOCK mode first
   (two minutes) — a check-in needs a target.
2. **Roll last week's daily rows into one weekly row** (sum the activity, carry the joins, score the
   week Ahead / On pace / Behind against the weekly activity target) and append it in the locked
   eleven-column shape. The three columns the daily rows lack are counted from the ledgers, never
   estimated (the Admin's locked definitions): **New prospects** = rows added to the Top-50 or to the
   pipeline Board at Identified this week · **Meaningful conversations** = conversation rows with a pain
   named or a next step agreed · **3-ways** = moves into 3-way or conversation rows with channel 3-way.
   Note carries show % and held→join % when the funnel ledger exists, and `funnel calls n` when
   `list-growth.md` has a row for the week. Compare to the 30-60-90 pace.
   **Who appends it:** read `config.md` first. If it holds a block whose heading starts with `## AI Admin`
   (first line `AI Admin: set up [date]`), the Admin owns the weekly rows from that moment — whether or not
   the member has run its CEO review yet — so this skill does NOT append: it hands the counted row to `admin-recruiting-scorecard`
   as a `WEEKLY ROW:` line (*"say 'my attraction scorecard' and it goes on"*) and reads the week from
   whatever row the Admin already wrote. No Admin block → this skill appends. **Never a duplicate:** before
   appending, check the `## Weekly rows` header is the locked eleven-column one and that no row already
   carries this `Week of` date — if one does, the week is scored: show it, append nothing.
3. **Name what moved, then the ONE thing for next week** — coach, not scold. If they are behind on
   activity, the fix is activity; if activity is on pace and joins lag, say that is normal for the
   first quarter and point at the conversion skills when they install (Week 5), not at the target.
4. Push. When the Admin is installed, say in one line that its scorecard carries the weekly row from here
   (and "run my CEO review" names the bottleneck).

## MONTHLY AUDIT (first check-in of each month, or "audit my month")
Ask Mike's three questions and the intangibles (`01-foundation-mindset/8`), answer them from the
scorecard before asking the member anything, and write the answers as a dated note at the bottom of
`goals.md`: agents attracted vs wanted (why not); conversations converted vs held (why not — model
explanation, objections, value proposition: point at the Brokerage Model Expert and, from Week 5, the
Objection Coach); content consistency (why not); and what got better that no number shows. When the
AI Admin's monthly review is installed, it owns this — say so and stop.

## QUARTERLY REFRESH ("plan my next attraction quarter")
After ~90 days: archive the finished quarter's scorecard as a dated doc in `01 · AI Brain/` (pushed,
never only local), celebrate the quarter against the target in two lines, then re-run LOCK mode with the
real ratios from the scorecard replacing the assumptions. Growth compounds when the plan does. Offer
`attraction-execution-framework` for the 12-month view and `attraction-leadership-audit` if the join
target now outruns their support capacity.

## Demo mode
When the session is explicitly a demo (the words "demo", "mock", "fictional"): use the demo member,
no live research, every number tagged "(illustrative — demo)", the Scorecard filename and cover
watermarked DEMO, same structure as real. Never push a demo over a real Brain.

## Quality bar before anything is shown
The delete test (every sentence earns its place), the any-agent test (nothing a member at any
brokerage in any city could have written — their why, their hours), the so-what test (every number is
followed by the activity it means), no hedging, no filler headings. Numbers come only from the member or
the labelled assumptions — never invented, never a projection.
