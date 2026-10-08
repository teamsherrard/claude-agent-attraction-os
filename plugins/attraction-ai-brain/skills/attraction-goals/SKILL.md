---
name: attraction-goals
description: >
  Phase 5 of the Agent Attraction Brain and the standalone deep dive: turns the member's
  organization goal into 12-month milestones and 30-60-90 targets for agents, conversations, calls,
  joins, and rev share, then reverse-engineers them into the weekly activity they control. Proposes
  the 90-day join target and the ratios; the member confirms. Calls the Rev Share Calculator for the
  money math (three illustrative scenarios, no earnings promise). Writes identity/goals.md, seeds
  memory/scorecard.md, renders the 90-Day Attraction Scorecard. Weekly check-in and quarterly
  refresh modes. Trigger on: "set my attraction goals", "my 90-day attraction target", "how many
  agents do I need", "how many conversations per week", "my attraction scorecard", "attraction
  weekly check-in", "am I on pace to my join target", "refresh my attraction plan", "plan my next
  attraction quarter", "set my agent targets", "update my money math", or right after Attraction
  Brain setup.
---

# Attraction Goals — the destination, reverse-engineered into this week (Brain Phase 5)

Every other skill helps the member *do* the work. This one tells them **which work, and how much**:
*you want **N agents** in 12 months, so your 90-day number is **n joins**, which at your ratios is
**this many conversations a week** — and here is the scorecard that tracks it.* The numbers serve the
why; the why is what re-anchors them in week six when joins lag activity.

**Where this runs.** First capture is INSIDE Attraction Brain Setup as **Phase 5, Stops 10–11**
(the eight questions below, the money math through the calculator, `goals.md` + the scorecard seed,
the Scorecard doc). This standalone skill is the same procedure on demand, plus **the rhythm**: the
weekly check-in, the monthly audit, and the quarterly refresh. When the Brain already holds locked
goals, READ them and refresh — never re-ask what setup captured.

**~10 minutes for the goals; ~3 minutes for a weekly check-in.**

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`
and obey them: plain language, no machinery in front of the member, 2–4 related questions per stop,
every stop ends with "your turn", propose-and-react when they are unsure, honour "skip" and "use
defaults". **Defaults are full-quality:** a member who is unsure on every number still leaves with a
real, specific, math-checked plan built from their Brain, labelled as assumptions they can adjust.

## Step 1 — Load the Brain (never ask what it knows)
Read `~/attraction-brain/brain.md`, then only what this needs:
- `identity/profile.md` — years in, brokerage, team or solo, agents in the organization today.
- `identity/journey.md` + `identity/strategy.md` — the why and the vision, if Phase 1 captured them.
- `identity/avatars.md` — who they are attracting (drives the "average production per attracted agent" estimate).
- `identity/brokerage-model.md` — plan mechanics, if the Brokerage Model Expert has run (often not yet in Week 1; fine).
- `identity/leadership.md`, `identity/operations.md` — capacity and hours, if built (Week 1 optional; empty is normal).
- `identity/goals.md` + `memory/scorecard.md` — if present, this is a refresh, not a first run.
- `memory/organization.md` — agents in the org today, if any rows exist.

If `~/attraction-brain/` does not exist locally, pull it via `attraction-brain-sync` first. A tool error
is never "no Brain" — say which connector failed and retry once; never suggest re-running setup. If no
Brain exists anywhere, tell them to say "set up my attraction brain" and stop.

## The doctrine this skill enforces (from Mike's Week 1 lessons)
- **Realistic beats heroic.** Unrealistic expectations are what guarantee failure; the people who want
  300 agents in year one are usually the ones who are not consistent (`01-foundation-mindset/8`). Three
  hard years, then the compounding does the work. Never let a member anchor on a number that makes
  month two feel like failure.
- **Set the outcome, commit to the actions.** The agent target has uncontrollable variables; the actions
  (conversations, calls, content shipped) are controllable with certainty (`01-foundation-mindset/8`).
  Every outcome in this plan is paired with the activity that produces it, and the scorecard tracks the
  activity first.
- **Singles win the game.** Do not build the plan around one whale — the big team, the influencer — who
  may never join. Enough singles, consistently, and the home run finds you (`01-foundation-mindset/9`).
  Q38 names the first agent; the plan still runs on volume.
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

## Stop 10 · Targets (plan questions 37–40 — one card, "your turn")
Orient first: *"Next up: your numbers. Four quick questions, then I'll do the math for you."*
1. **Agents in your organization in 12 months?** (Q37) If they are unsure, consult: propose a band from
   their situation (hours, years in, whether conversations already happen) and say why. Mike's worked
   example in the lesson is 30 frontline agents in 12 months for a consistent, full-effort attractor
   (`01-foundation-mindset/8`); a member giving attraction a few hours a week on top of production
   should hear a smaller, honest number. Their choice is final.
2. **Who's the first agent you'd want to join, and why them?** (Q38) Their words verbatim — this seeds
   `memory/top-50.md` (the Top-50 skill writes the row; hand it the name) and often reveals the avatar.
3. **Hours per week you can give to attraction, honestly.** (Q39) This is the capacity ceiling the
   weekly activity must fit inside.
4. **Your 90-day join target.** (Q40) **Propose it, never ask it cold.** Ramp, never flat: a member
   starting attraction from a standing start gets roughly **15% of the 12-month number in the first
   quarter** (quarters ramp about 15 / 20 / 30 / 35%, a planning assumption, labelled); a member who
   already has conversations flowing gets about 25%. Minimum 1. Show the working in one line and ask
   them to confirm or move it.
If the Brain holds no why (nothing usable in `journey.md` or `strategy.md`), add one skippable line to
this card — *"And who are you doing this for?"* — and keep the answer verbatim. It is the question
members thank you for; it is never homework.

## Stop 11 · The money, honestly (plan questions 41–44)
Orient: *"Now the money, honestly. Three short questions, then I show you three scenarios — every
number illustrative, nothing promised."*
1. **Your plan's mechanics** (Q41) — rev share tiers, caps, stock — or say **"explain mine to me"** and
   the **Brokerage Model Expert** (`attraction-brokerage-model`) walks them through it first. If
   `identity/brokerage-model.md` already holds the mechanics, show them and skip the question.
2. **Average production of the agent you're attracting** (Q42) — their estimate, from their avatar.
   Labelled "member's estimate" everywhere it appears.
3. **Your ratios, or take the defaults and adjust** (Q43): conversations → calls, calls held → joins.
   The calculator proposes the defaults and says which are benchmarks and which are assumptions.

Then **call `attraction-rev-share-calculator`** with: mechanics · organization size today · 12-month
target · average production estimate · ratios. It returns three scenarios (conservative / target /
stretch), the weekly activity each implies, and its compliance stamp. Show the table and ask the one
question:
4. **Does this weekly activity feel realistic?** (Q44) *Adjust the target or the hours, not the math.*
   If the weekly activity does not fit Q39's hours, say so plainly and offer the two honest moves:
   lower the 90-day target, or find the hours. Re-run the calculator on the adjusted input, once.

**This whole block is private material.** It goes in the Brain and the Book; it never goes into
content, DMs, ads, or a lead magnet (`identity/compliance.md` gate; the calculator's stamp says so).

## Build `identity/goals.md` (the locked shape — every section, no brackets left behind)
```
# [Name] — Attraction Goals
*identity · the destination and the weekly activity · owner: attraction-goals · Status: locked [YYYY-MM-DD] (quarter [start] → [end])*

## The why
[verbatim, their words — or "not captured yet" with the open-item note]

## 12-month milestones (set [date])
| Measure | Today | 12 months |
|---|---|---|
| Agents in organization (frontline) | [n] | [N] |
| Conversations (running total) | — | [from weekly activity × 52] |
| Calls held | — | [...] |
| Joins | — | [N minus today] |
| Rev share (illustrative, member's assumptions) | [today, if any] | [target scenario] |

## 30-60-90 (quarter [start] → [end])
| | Day 30 | Day 60 | Day 90 |
|---|---|---|---|
| Conversations | | | |
| Calls held | | | |
| Joins | | | [the 90-day target] |
| Content shipped | | | |
| Agents in organization | | | |
(Ramped: month 1 builds, month 2 compounds, month 3 converts — never flat.)

## Weekly activity (the controllables, inside [Q39] hours/week)
- Conversations: [x]/week   - Calls: [y]/week   - Follow-ups: [z]/week
- Content: [from identity/content-pillars.md when built; until Week 3: "set with the Short-Form system in Week 3"]
- Daily slice (for the Debrief): [weekly ÷ working days from operations.md, default 5]

## Ratios (assumptions until 30 days of real data replace them)
conversations → calls [..] ([member / default]) · calls held → joins [..] ([member / Mike's benchmark floor, 16-implementation-scaling/78])

## The money, honestly
[the calculator's block, verbatim, including its stamp line and the date]

## First agent
[Q38 verbatim — name, why them] → handed to the Top-50.

## Hours
[Q39] per week for attraction; [split into conversations / calls / content / follow-up].
```
Status rules: `seeds` while any of Q37/Q39/Q40 is a placeholder; `locked [date]` once the member has
confirmed Q40 and Q44. A locked file is what the Debrief and the Admin read as the target.

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
Score vocabulary, locked: **Ahead** (≥ 150% of the slice), **On pace**, **Behind**. Never a grade, never
a percentage the member has to interpret. If `scorecard.md` already exists, replace ONLY the Targets
block and leave every row untouched. **The weekly row's columns are the AI Admin's seven KPIs in its
order** (new prospects · conversations · meaningful conversations · calls booked · calls held · 3-ways ·
joins), then content shipped · score · note — the same header in the Brain template and `admin-recruiting-scorecard`;
never a new column. The daily rows keep their shorter shape (the Debrief's).

## Render the 90-Day Attraction Scorecard (the deliverable they hold)
Assemble the structured text per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` (read it now, not
earlier): title, meta line, CAPS bands, pipe-row tables for the targets, the 30-60-90, the weekly
activity, the money scenarios (with the stamp line under the table), and a one-page "how to use this
weekly" band. Then:
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/scorecard.txt "🎯 [Name]'s 90-Day Attraction Scorecard — [YYYY-MM-DD].docx" --title "90-Day Attraction Scorecard" --subtitle "[Name] · [Market]" --eyebrow "Agent Attraction Brain"`
Read the `.docx` text back (no `<w:` markup, every table present), upload it to the workspace's
`01 · AI Brain/` per `${CLAUDE_PLUGIN_ROOT}/shared/drive-map.md`, and hand them the direct link.
Dated filename; the newest is current. **If the renderer prints `RENDERER-UNAVAILABLE`, do exactly
what it says: install nothing, save the structured text as a `.md`, upload that, and say in one line
that the styled version needs the renderer.** One corrective re-render at most; never a loop.

## Write → push → verify, then confirm
Write `goals.md` and `scorecard.md`, then run `attraction-brain-sync` (PUSH) immediately and verify —
one atomic step; an unsynced write is a lost write. Hand Q38's name to the Top-50 (`attraction-top-50`
adds the row; this skill never writes `top-50.md`). Confirm in their words: *"Your targets are set —
[N] agents in 12 months, [n] joins this quarter, which means about [x] conversations and [y] calls a
week. Your scorecard is in your home base, and your Daily Debrief scores each day against it."*
Only if the AI Admin is installed add: *"— and your morning brief carries your weekly activity."*

## WEEKLY CHECK-IN mode ("attraction weekly check-in" · "am I on pace" · Mondays via the Debrief)
~3 minutes, never a re-interview:
0. **Open with the why** — one line, theirs: *"Week [n] of the plan you're running for [why]. Here's
   the score."* When they are behind, the why is the re-anchor, never the stick.
1. Read `goals.md`, `scorecard.md` (last week's daily rows), `memory/conversations.md`,
   `memory/pipeline.md` (the Stage moves log), `memory/top-50.md` (rows added this week),
   `memory/content-log.md`, `memory/deadlines.md`; and, when they exist, `memory/sales-funnel.md`
   (show rate, held→join — or a `WEEKLY ROW:` line `sales-scorecard` handed over this session) and
   `memory/list-growth.md` → the newest row's **"Calls booked from the funnel"** (the Lead Magnet plugin's
   ledger, Week 6; skip silently if absent).
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
   its CEO Review task is on — so this skill does NOT append: it hands the counted row to `admin-recruiting-scorecard`
   as a `WEEKLY ROW:` line (*"say 'my attraction scorecard' and it goes on"*) and reads the week from
   whatever row the Admin already wrote. No Admin block → this skill appends. **Never a duplicate:** before
   appending, check the `## Weekly rows` header is the locked eleven-column one and that no row already
   carries this `Week of` date — if one does, the week is scored: show it, append nothing.
3. **Name what moved, then the ONE thing for next week** — coach, not scold. If they are behind on
   activity, the fix is activity; if activity is on pace and joins lag, say that is normal for the
   first quarter and point at the conversion skills when they install (Week 5), not at the target.
4. Push. When the Admin is installed, say in one line that its scorecard carries the weekly row from here
   (and the Weekly Recruiting CEO Review, once they turn it on, names the bottleneck).

## MONTHLY AUDIT (first check-in of each month, or "audit my month")
Ask Mike's three questions and the intangibles (`01-foundation-mindset/8`), answer them from the
scorecard before asking the member anything, and write the answers as a dated note at the bottom of
`goals.md`: agents attracted vs wanted (why not); conversations converted vs held (why not — model
explanation, objections, value proposition: point at the Brokerage Model Expert and, from Week 5, the
Objection Coach); content consistency (why not); and what got better that no number shows. When the
AI Admin's monthly review is installed, it owns this — say so and stop.

## QUARTERLY REFRESH ("plan my next attraction quarter")
After ~90 days: archive the finished quarter's scorecard as a dated doc in `01 · AI Brain/` (pushed,
never only local), celebrate the quarter against the target in two lines, then re-run Stops 10–11
with the real ratios from the scorecard replacing the assumptions. Growth compounds when the plan does.
Offer `attraction-execution-framework` for the 12-month view and `attraction-leadership-audit` if
the join target now outruns their support capacity.

## Demo mode
When the session is explicitly a demo (the words "demo", "mock", "fictional"): use the demo member,
no live research, every number tagged "(illustrative — demo)", the Scorecard filename and cover
watermarked DEMO, same structure as real. Never push a demo over a real Brain.

## Quality bar before anything is shown
The delete test (every sentence earns its place), the any-agent test (nothing a member at any
brokerage in any city could have written — their why, their first agent, their hours), the so-what test
(every number is followed by the activity it means), no hedging, no filler headings. Numbers come
only from the member or the calculator's labelled assumptions — never invented, never a projection.
