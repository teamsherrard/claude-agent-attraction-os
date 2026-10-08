---
name: sales-scorecard
description: >
  Sales OPS: the weekly sales scorecard for agent attraction. Calls booked, show rate, presentations
  held, 3-way calls, closes (joins), and conversion by source, read from the Brain's pipeline and Top-50
  with the member's corrections; the held-to-join rate against Mike's 50% line; and the diagnosis map
  from his performance-metrics lesson (which number is the constraint, and which skill fixes it). Keeps
  the funnel ledger and feeds the Brain's scorecard in its locked row shape; hands the weekly row to the
  AI Admin when it is installed. Renders the monthly Sales Scorecard. Trigger on: "sales scorecard",
  "attraction sales scorecard", "my show rate", "my conversion by source", "how many calls did I book
  this week", "what's my constraint", "where am I leaking calls", "calls booked vs held", "my
  held-to-join rate", "score my sales week".
---

# Sales Scorecard — "you can't argue ego and emotion with math"

"What gets measured gets managed. Without tracking you're guessing… metrics reveal where your growth is
coming from and, most importantly, where you're leaking opportunity" (`16-implementation-scaling/78`). This
is the sales-funnel half of that lesson: booked → held → presented → 3-way → joined, by source, every week,
with the one diagnosis Mike makes — is it a lead-flow problem, a conversion problem, or a retention
problem — and the skill that fixes it.

**Write-and-prepare.** It reads ledgers and writes numbers; it never moves a stage or sends anything.

## Step 0 — How we speak
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`. A
scorecard is a mirror, never a verdict; compare the member only to their own prior weeks
(`01-foundation-mindset/08`).

## Step 1 — Load the Brain
`~/attraction-brain/brain.md`, then `memory/pipeline.md` (the **Stage moves log** — the dated moves into
Call booked, Call held, 3-way, Joined this week), `memory/top-50.md` (the **Source** column per agent),
`memory/conversations.md` (channel, 3-way rows), `memory/scorecard.md` (the Targets block: the weekly calls
and joins target; existing rows), `memory/sales-funnel.md` (this skill's ledger, if it exists),
`identity/goals.md` (ratios), `memory/list-growth.md` only when it exists (Week 6 — its row's `Calls booked
from the funnel`, for the `funnel n` note), `config.md` (the AI Admin block → who appends the weekly row).
Missing locally → `attraction-brain-sync`. A tool error is never "no Brain". Empty ledgers → "no calls logged yet —
the scorecard starts the week you hold your first" and stop; never invent a number.

## Step 2 — Count the week (then one correction question)
From the stage-moves log and the ledgers, for the week being scored (default: last Monday to Sunday):
**Calls booked** (moves into Call booked) · **Calls held** = presentations (moves into Call held) · **Show
rate** = held ÷ booked-and-due-this-week · **3-ways** (moves into 3-way, or `conversations.md` channel
`3-way`) · **Closes** = joins (moves into Joined) · **Held → join** = joins ÷ held (rolling four weeks — a
single week is noise) · **By source** = each of the above split by the Top-50 Source value (youtube ·
instagram · referral · sphere · event · lead-magnet · other).
Show the counts and ask ONE question: *"Anything I can't see — a call that wasn't logged, a no-show, a
3-way? One line, or 'that's right'. Your turn."* Fold the answer in; log a missing call as a
`conversations.md` row (this plugin's ledger) so next week counts itself.

## Step 3 — The diagnosis (Mike's map, `/78`, in his order)
State the one constraint — "the biggest thing holding you back right now" — and the fix:
| What the numbers show | Mike's read | The fix (by name) |
|---|---|---|
| Few conversations, few bookings | "not enough attraction activity" — not enough valuable content, not enough conversations | the Short-Form and YouTube systems; `cv-conversation-starter`; the Prospect Radar |
| Conversations up, bookings low | the invite isn't landing (the build's extension of Mike's "lead flow" bucket) | `cv-dm-flow`, `cv-conversation-starter`, `sales-booking-page` |
| Booked up, held low (show rate) | booked is not held (the build's extension) | `sales-show-up` (the warm-intro video, reminders), `sales-setter` confirmation call |
| Held up, joins low — **held → join under 50%** | "you need to get better at explaining the model, the value proposition, handling objections" — tailoring, bridging the gap | `cv-objection-coach` (drills), `cv-enrollment-script`, `attraction-brokerage-model`, `cv-three-way` ("bring in the heavy artillery") |
| Joins up, retention down | onboarding and community | outside this plugin — Team & Retention is not in this build; the Brain's `attraction-operations` (onboarding steps) and `memory/organization.md` are what exists; say so plainly |
| Nobody else attracting | "you're still the only one putting in the effort" — teach agents to attract | outside this plugin (duplication was the removed Team & Retention plugin); point to `attraction-leadership-audit` and say so plainly |
| Rev share flat | leadership development — "your group scales to the capacity you are" | `attraction-leadership-audit` |
One constraint per week, named plainly, with the next action in one line. When held → join is above 50%
and bookings are below target, the constraint is activity — say so; it is the most common first-quarter
read and it is good news.

## Step 4 — Write it (one owner per file)
- **`memory/sales-funnel.md`** — this skill's ledger (created from this header on first run; proposed to the
  coordinator as a Conversion-plugin-owned memory file in the sync allowlist):
  ```
  # [Name] — Sales Funnel
  *memory · weekly funnel by source · owner: sales-scorecard (Conversion & Sales) · rows are never edited*
  | Week of | Booked | Held | Show % | 3-ways | Joins | Held→join % (4-wk) | By source (booked/held/joins) | Constraint | Note |
  |---|---|---|---|---|---|---|---|---|---|
  ```
- **`memory/scorecard.md`** — the Brain's one scorecard, and **this plugin never writes it**
  (`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`). It feeds it in the locked weekly-row shape — the header
  `| Week of | New prospects | Conversations | Meaningful conversations | Calls booked | Calls held | 3-ways | Joins | Content shipped | Score | Note |`,
  identical in the Brain template, `attraction-goals`, and `admin-scorecard` — by handing the row to its
  owner, every column in that order. End the output with
  *"WEEKLY ROW: [week of — the Monday] · new prospects [rows added to the Top-50 or to the Board at Identified
  this week] · conversations [conversations.md rows this week] · meaningful conversations [rows with a pain
  named or a next step agreed] · calls booked [n] · calls held [n] · 3-ways [n] · joins [n] · content shipped
  [— ; the appender counts it from the content-log] · score [Ahead | On pace | Behind against the Targets
  block's weekly calls] · note: show [x]% · held→join [y]% · funnel [n — only when `memory/list-growth.md`
  carries `Calls booked from the funnel`] · constraint [..]"*. **AI Admin installed** (its block in
  `config.md`) → `admin-scorecard` appends it on its next run, reconciling booked / held / 3-ways / joins
  against the same Stage-moves log and keeping show, held→join, funnel, and the constraint in Note; say so.
  **Not installed** → the Brain's weekly check-in appends it: *"say 'attraction weekly check-in' and this row
  goes on your scorecard."* Never the Targets block, never an existing row, never a new column.
- Then `attraction-brain-sync` PUSH and verify, one step. Unsaved → say so, keep the numbers visible,
  retry once, stop.

## Step 5 — The monthly Sales Scorecard doc (first run of each month, or "render my sales scorecard")
Per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md`: the month's four weeks as a table, the funnel by
source, the held → join trend, the constraint each week and what changed, the next month's one focus. Via
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/sales-scorecard.txt "Sales Scorecard — [Name] — [YYYY-MM].docx" --title "Sales Scorecard" --subtitle "[Name] · [Month YYYY]"`
(read back; `RENDERER-UNAVAILABLE` → install nothing, upload the `.md`), upload to the workspace's `01 · AI
Brain` folder next to the 90-Day Attraction Scorecard. Mike audits "in immense detail every quarter"; the
AI Admin's monthly review and the Weekly Recruiting CEO Review (Week 6) read this ledger — say so once.

## What the member sees (~15 lines)
THIS WEEK (booked · held · show rate · 3-ways · joins, each against last week's) · BY SOURCE (one line per
source with bookings and joins) · HELD → JOIN (four-week, against the 50% line, one sentence) · THE
CONSTRAINT and the fix, by name · one closing line with the next move. No percentages the member has to
interpret without the sentence that interprets them.

## Demo mode
Fictional member, every number "(illustrative — demo)", DEMO in the filename, nothing written to a real Brain.

## Quality bar
Every count traces to a dated ledger row or the member's own correction; one constraint, not three; the
so-what test (every number ends in a skill or an action); no comparison to Mike's or anyone else's results;
no income or rev-share figure anywhere on the card.
