---
name: attraction-execution-framework
description: >
  Builds the member's 12-month Agent Attraction execution framework: four quarters from the goals in
  their Brain, the weekly KPIs they control (conversations, calls, follow-ups, content) beside the
  outcomes they do not (joins, organization size, rev share), the monthly metrics that reveal the
  constraint (conversations, conversion, retention, engagement, duplication, rev share trend), and
  the CEO rhythm: daily debrief, weekly CEO review, monthly KPI review. Writes
  identity/execution-framework.md; the AI Admin's reviews read it. Grounded in Mike's
  performance-metrics and duplication lessons. Trigger on: "my execution
  framework", "build my 12-month attraction plan", "my CEO rhythm", "my weekly attraction KPIs",
  "what should I review monthly", "install my daily weekly monthly reviews", "my attraction
  operating rhythm", "what is my constraint", "where am I leaking agents", "12-month organization
  plan".
---

# Execution Framework — the 12-month plan, the weekly KPIs, and the CEO rhythm

`attraction-goals` sets the destination and this week's activity. This skill is the year around it:
four quarters, the numbers reviewed every week and every month, the diagnosis map that says *which*
number is the constraint, and the operating rhythm — daily, weekly, monthly — that turns attraction
from a project into how the member runs their organization. "What gets measured gets managed; without
tracking you're guessing" (`16-implementation-scaling/78`).

**Where this runs.** By the cohort calendar it is a Week 6 skill (the CEO rhythm lands with the Team
& Retention and Admin plugins). It runs any time `identity/goals.md` is locked. **Never demands
later-week deliverables:** content pillars (Week 3), the pipeline (Week 5), onboarding (Week 6) are
referenced as "when built" and the framework says which week builds each.

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`.
Mostly this skill *shows* and asks the member to react; it has at most two short stops.

## Step 1 — Load the Brain
`~/attraction-brain/brain.md`, then: `identity/goals.md` (required — if it is absent or `seeds`,
say in one line that the targets come first and run `attraction-goals`, then return),
`memory/scorecard.md`, `identity/leadership.md` and `identity/operations.md` (if built — capacity,
hours, call cadence), `identity/content-pillars.md` or `identity/content-pillars.md` (if built — the
content KPI), `memory/organization.md`, `memory/pipeline.md`, `memory/content-log.md` (what has
actually happened), `identity/execution-framework.md` (if present, this is a refresh). Pull via
`attraction-brain-sync` if the local copy is missing; a tool error is never "no Brain".

## The doctrine (cite it when a rule comes from a lesson)
- **Track monthly, audit quarterly** (`16-implementation-scaling/78`): new agent conversations ·
  conversion from conversation to onboarding · agent retention · agent engagement (call attendance,
  community activity) · duplication rate (how many agents in the group are attracting) · rev share
  growth and trend line.
- **The monthly review's one question** (`16-implementation-scaling/78`): where is momentum slowing —
  is it a **lead-flow** issue, a **conversion** issue, or a **retention** issue? Then adjust.
- **The diagnosis map** (`16-implementation-scaling/78`), the heart of this skill:

| What the numbers show | What it usually means | What to fix, and where |
|---|---|---|
| Low conversations | not enough attraction activity, not enough valuable content | activity target + the content engine (Short-Form Week 3, YouTube Week 4) |
| High conversations, low conversions | messaging, model explanation, objection handling | Brokerage Model Expert now; Conversion plugin (objection coach, call audits) Week 5 |
| Good recruiting, poor retention | onboarding, no tight community | operations' onboarding steps now; Team & Retention plugin Week 6 |
| Low duplication | the member is the only one attracting; agents are not being taught to attract | Team plugin's teach-to-attract Week 6 (`13-team-building-duplication/63`) |
| Rev share flatlining | no new leadership development; the group scales to the leader's capacity | leadership audit + invest in yourself (`16-implementation-scaling/80`) |

- **Linear vs exponential** (`13-team-building-duplication/63`): the member adding agents is linear;
  their agents adding agents is exponential. The framework tracks duplication from day one even when
  the number is zero, so the moment it starts is visible.
- **Quarters, not years** (`01-foundation-mindset/8`): long enough to do something substantial, short
  enough to measure. Four quarters, each with its own 90-day target from `attraction-goals`.
- **Growth first, then duplication** (`16-implementation-scaling/80`): the leader is the ceiling. The
  framework's monthly review includes one line on what the member is learning or investing in.
- **Make it easy for producers to invite** (`13-team-building-duplication/63`): Mike ran one call
  every Tuesday evening for four years so production-focused agents could just invite people. The
  rhythm has a slot for "the standing call / three-way path" once the organization has agents.

## Stop A · Confirm the year's shape (one card, 2–3 questions — most answers come from the Brain)
Orient: *"Next: your year. I've built four quarters from your targets — two quick questions, then the
rhythm."*
1. **The three weekly non-negotiables.** Propose them from `goals.md` (conversations · calls ·
   content, with the numbers) and ask them to confirm or swap one. Three, not ten — the 20% that
   produces the result. Content is always one of the three once the content system exists (Week 3);
   before that, the third is follow-up touches.
2. **Which quarter are we in, and what is already true?** Confirm from the scorecard (joins to date,
   agents in the org) in one line; ask only if the Brain is silent.
3. *(Only if the org has agents)* **Do you run a standing call or three-way path today?** Yes / not
   yet / "what's that" — the last routes to Week 6; the first goes into the rhythm.

## Stop B · The rhythm (one card, 2–3 questions)
1. **Weekly CEO review — when?** Propose a day and time from `operations.md` hours (default Friday
   4 pm or Sunday evening); the member moves it.
2. **Monthly KPI review — the 1st, or a day you'll actually keep?**
3. **Who holds you to it?** Themselves, an accountability partner, their upline — one name or "me".
   (Nothing is shared by this skill; it is recorded so the reviews can name it.)

## Build the framework (then show it, then write it)
**1. The 12-month table** — four quarters, each: focus · joins target (ramped 15 / 20 / 30 / 35% of the
12-month number unless `goals.md` says otherwise — a planning assumption, labelled) · agents in the
organization at quarter end · the controllable weekly KPIs for that quarter (conversations, calls,
follow-ups, content) · what gets installed that quarter (from the member's cohort week, if they are in
one; otherwise from what is built). The focus line is theirs, not generic: Q1 for a member with no
content yet reads differently from Q1 for a member with a channel.

**2. The weekly KPI card** — two columns, locked vocabulary: **Controllables** (conversations · calls
booked · calls held · follow-ups sent · content shipped) and **Outcomes** (joins · agents in org ·
duplication · rev share, illustrative). Each controllable carries its number from `goals.md`; each
outcome carries the quarter target. The Debrief scores the controllables daily; the weekly review
reads both.

**3. The monthly metrics table** — the six metrics from `16-implementation-scaling/78`, each with: how
it is measured here (which Brain ledger or CRM export), this month's number (blank until data), the
diagnosis-map row it belongs to. Retention, engagement, and duplication read "no agents yet" until
`memory/organization.md` has rows — that is normal, say so once.

**4. The constraint of the quarter** — one line. Apply the diagnosis map to the real numbers in the
scorecard and pipeline; before data exists, the constraint is always "activity" and the line says so.

**5. The CEO rhythm table** — what, when, who runs it, and which skill or agent does it **now** versus
**once the later plugins install**:

| Rhythm | When | Runs it now (Week 1+) | Extends it later |
|---|---|---|---|
| Daily debrief | [debrief time] | `attraction-debrief` (the Daily Agent Attraction Debrief) | AI Admin's `admin-daily` (Week 5) |
| Weekly CEO review | [Stop B day/time] | `attraction-goals` weekly check-in | AI Admin's `admin-scorecard` CEO mode = the Weekly Recruiting CEO Review (Week 6) |
| Monthly KPI review | [Stop B date] | `attraction-goals` monthly audit | AI Admin's `admin-monthly-review` = the Monthly KPI Review (Week 6) |
| Quarterly audit + refresh | end of quarter | `attraction-goals` quarterly refresh + this skill's refresh | Team plugin's organization analysis (Week 6) |

The weekly review's four questions, fixed: what happened in recruiting this week (activity vs target),
what happened in the organization (joins, needs, wins), what is the constraint, what is next week's
one thing. The monthly review adds Mike's three audit questions and the intangibles
(`01-foundation-mindset/8`) plus "what did I invest in myself this month".

## Write `identity/execution-framework.md` (locked shape)
```
# [Name] — Execution Framework
*identity · the 12-month plan, weekly KPIs, monthly metrics, and the CEO rhythm · owner: attraction-execution-framework · built [date] · from goals.md locked [date]*

## The year (four quarters)
| Quarter | Focus | Joins target | Agents in org at end | Weekly controllables | What installs |
|---|---|---|---|---|---|

## Weekly KPIs
| Controllables (scored daily) | Target | Outcomes (reviewed weekly) | Quarter target |
|---|---|---|---|

## Three weekly non-negotiables
1. ... 2. ... 3. ...

## Monthly metrics (16-implementation-scaling/78)
| Metric | Measured from | This month | Diagnosis row |
|---|---|---|---|

## Constraint of the quarter
[one line, dated]

## CEO rhythm
| Rhythm | When | Runs it now | Extends it later |
|---|---|---|---|
Accountability: [name]

## Standing call / three-way path
[what exists today, or "not yet — Week 6"]
```
Write it, then `attraction-brain-sync` (PUSH) immediately and verify. The Book renders this as *Your
12-Month and 90-Day Plan* and *Your Weekly Activity* in Part IV.

## Render the doc (optional, on request or at a quarterly refresh)
"📈 [Name]'s 12-Month Execution Framework — [YYYY-MM-DD]" per
`${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` (read it then):
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/framework.txt "📈 [Name]'s 12-Month Execution Framework — [date].docx" --title "12-Month Execution Framework" --subtitle "[Name] · [Market]" --eyebrow "Agent Attraction Brain"`
→ read back, upload to `01 · AI Brain/` per `shared/drive-map.md`, hand them the direct link. **If the
renderer prints `RENDERER-UNAVAILABLE`, do exactly what it says: install nothing, save the structured
text as a `.md`, upload that, and say in one line that the styled version needs the renderer.**

## "What is my constraint?" mode
Read `scorecard.md`, `pipeline.md`, `organization.md`, `content-log.md`; apply the diagnosis map;
answer in three lines: the number, what it means, the one fix and where it lives. Update the
*Constraint of the quarter* line and push. No interview.

## Hand-offs (one line each, only when relevant)
`attraction-goals` for targets and the weekly check-in · `attraction-leadership-audit` when the join
target outruns support capacity · `attraction-debrief` to switch the daily rhythm on · the AI Admin's
reviews once installed (they read this file; this skill does not write theirs).

## Demo mode
Fictional member, every number "(illustrative — demo)", DEMO watermark on any render, same structure.

## Quality bar
The delete test, the any-agent test (quarter focus lines that only this member could own), the
so-what test (every metric names its fix), no hedging, no filler headings. Never a wall of
paragraphs: tables for the year, the KPIs, the metrics, the rhythm.
