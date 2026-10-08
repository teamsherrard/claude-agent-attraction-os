---
name: attraction-leadership-audit
description: >
  From Agent to Leader: audits whether the member is ready to serve the agents they want to attract.
  Scores five readiness areas (time available for agents, systems they can hand over, onboarding they
  can offer, support capacity for the number of agents they are targeting, their own consistency),
  explains each score from their own facts, and produces a fix-first list so they never attract
  agents they cannot serve. Writes identity/leadership.md. Grounded in Mike's From Agent to Leader,
  Leadership Evolution, and Supporting Without Babysitting lessons. Trigger on: "leadership audit",
  "am I ready to lead agents", "from agent to leader", "can I support more agents", "my readiness
  score", "what should I fix before attracting agents", "audit my leadership", "how many agents can
  I serve", "am I ready for my first agent", "attraction readiness".
---

# Leadership Audit — From Agent to Leader (readiness score + the fix-first list)

"The size of your business is the size of your leadership" (`01-foundation-mindset/6`). Production
is about the member; attraction is about the people who will look up to them. This skill asks the
honest question before the first agent joins: *can you serve the agents you are about to attract?*
It scores five areas, says why in the member's own facts, and hands back a short fix-first list. The
Retention pillar starts here — an agent attracted into nothing leaves, and tells people why.

**Tone law:** honest, never harsh, never disqualifying. A member in year three with no onboarding
and no systems scores low and that is *normal* — the audit exists to turn low scores into the first
three things to build, not to tell anyone they are not ready to begin. "Done is better than perfect"
(`16-implementation-scaling/80`).

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`.
Two stops, 3–4 questions each, "your turn" at the end of each; propose-and-react when they are unsure.

## Step 1 — Load the Brain (score from facts before asking anything)
`~/attraction-brain/brain.md`, then: `identity/profile.md` (years, team or solo), `identity/journey.md`
(what they built, the hardest stretch), `identity/goals.md` (the 90-day join target = **N**, the hours
from Q39), `identity/operations.md` (hours, onboarding steps, call cadence — if built),
`identity/offer.md` (what they give — Week 2; seeds are fine), `identity/proof.md` and
`memory/organization.md` (agents today, how long they stayed), `memory/content-log.md` and
`memory/scorecard.md` (consistency, in rows not claims), `identity/strategy.md` (vision),
`identity/leadership.md` (if present: a re-audit — show last time's scores and ask what changed).
Pull via `attraction-brain-sync` if missing; a tool error is never "no Brain".

## The doctrine (what "ready" means, from the lessons)
- **Vision, certainty, congruence, standards** (`01-foundation-mindset/6`): a compelling vision big
  enough that every agent's goals fit inside it; certainty in uncertain markets (never doom and gloom);
  walking the walk — never telling agents to do what the member does not do; high standards that
  raise theirs. Maxwell's laws as Mike applies them: magnetism (you attract who you are), solid ground
  (trust through execution), addition (value by serving), influence.
- **Growth first, then duplication** (`16-implementation-scaling/80`): the leader is the ceiling of
  the group; invest in yourself continuously; model the work ethic; share wins and struggles honestly.
- **Support without babysitting** (`14-retention-culture/71`): empower, do not enable. What support
  means in practice: a clear 30-60-90 onboarding action plan · access to systems, scripts, and
  resources on day one · regular touch points (the mastermind or team call) · recognition when they
  act · an open door, with the responsibility staying theirs. The trap: answering the same question
  over and over — document it once (a quick video, an FAQ, a training library) so answers scale.
  "Save the people swimming toward the boat." Time is earned by plugging in.
- **Duplication is the business** (`13-team-building-duplication/63`): if it does not duplicate, it
  does not matter. Readiness includes whether what the member does can be handed over.

## Stop A · Time and what you can hand over (one card, 3–4 questions)
Orient: *"Next: a quick, honest readiness check — two short rounds. Low scores are normal; they
become your first three fixes."*
1. **Hours a week for your agents** (not for attraction — for the people who have already joined).
   If `goals.md` Q39 exists, ask for the split: *"Of your [Q39] attraction hours, how many would go to
   supporting agents once they join?"*
2. **What would you hand a new agent on day one?** Scripts, a lead system, a routine, trainings, a
   call they can join, your brokerage's or upline's resources — list what exists, in their words.
   (The upline's assets count — the Week 2 audit packages them; here we only need to know they exist.)
3. **What happens to a new agent in their first 30 days today?** Steps, or "nothing yet". Never a
   demand for the full onboarding experience — that is built in Week 6 with the Retention &
   Duplication playbook; say which week.
4. *(Only if the org has agents)* **How many have stayed, and who left — why?** One line.

## Stop B · Support, consistency, vision (one card, 3–4 questions)
1. **How do your agents' questions reach you, and what is written down?** Text / calls / a group /
   nothing yet · an FAQ, a training library, recorded answers, or nothing yet.
2. **How many agents could you answer every week before it costs you your own production?** Their
   honest number.
3. **Consistency — the real streak.** Read `content-log.md` and the scorecard first and state what
   the rows show; then one question: *"What have you done every week for the last 8 weeks without
   missing?"* (content, calls, a routine — anything).
4. **The vision in one line.** Where the organization is going, big enough for an agent's goals to
   fit inside it (`01-foundation-mindset/6`). From `strategy.md` if it exists — confirm, do not re-ask.

## Scoring (0–3 per area, total out of 15 — the rubric is fixed so re-audits compare)
| Area | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Time for agents** | none set aside | ad hoc, when asked | a weekly block exists | a weekly block + a standing call or touch point |
| **Systems to hand over** | nothing written | one thing, in their head | 2+ things written and shareable | a kit an agent can use alone on day one |
| **Onboarding** | nothing | a welcome message | day 1 → week 1 steps written | a 30-day path with check-ins |
| **Support capacity** | every question comes to them live | some answers written | FAQ / library covers most repeats; a group exists | answers scale (library + community + leaders); their time is earned |
| **Consistency** | no streak | a streak under 4 weeks | 8+ weeks on one activity | 6+ months on the activities agents are asked to copy |

**Bands:** 0–5 **Build first** — attract one or two agents and build with them; 6–10 **Ready for the
90-day target, with fixes**; 11–15 **Ready to scale** — the constraint is activity, not readiness.

**Capacity line (a labelled assumption):** `agents you can serve ≈ hours for agents per month ÷
hours per agent per month` — use ~3 hours per agent per month with no systems, ~1 with a written kit
and a group, and say so. Compare it with **N** (the 90-day join target) and with the 12-month target.
If N outruns capacity, that is the headline of the fix-first list, not a reason to lower N.

## The fix-first list (three items, ranked, each with its first action and where it is built)
Rank by: blocks the 90-day join target → lowest score → fastest to fix. Each item: the area, the
score, **the first concrete action this week**, and the skill or plugin that builds the full thing:
- onboarding steps → `attraction-operations` now; the 30-day experience → the Week 6 Retention & Duplication playbook
- systems to hand over → the Week 2 offer audit (`attraction-offer`, what the brokerage + upline +
  member already provide); the Value Vault (Week 6)
- support capacity → start the FAQ today: the next question asked twice gets a recorded answer and a
  place to live (`14-retention-culture/71`); `attraction-capture` logs the questions
- consistency → the content engine (Weeks 3–4) and the Debrief's daily score
- explaining the model with confidence (the intangible Mike names first in `01-foundation-mindset/8`)
  → the Brokerage Model Expert
Never more than three. The member corrects the order; their call is final.

## Write `identity/leadership.md` (locked shape)
```
# [Name] — Leadership Readiness
*identity · From Agent to Leader · owner: attraction-leadership-audit · audited [date] · re-audit each quarter*

## Readiness: [total]/15 — [band]
| Area | Score | Why (their facts) |
|---|---|---|
| Time for agents | | |
| Systems to hand over | | |
| Onboarding | | |
| Support capacity | | |
| Consistency | | |

## Capacity (assumption: ~[x] hrs per agent per month)
Can serve ≈ [n] agents today · 90-day join target: [N] · 12-month target: [T] → [fits / outruns capacity by ...]

## Fix first
1. [area · score] — this week: [action] → built in full by [skill / plugin, week]
2. ...
3. ...

## Vision (their line)
[verbatim]

## What they hand an agent on day one (today)
- ...

## First 30 days today
[steps, or "nothing yet — Week 6 builds it"]

## Re-audit log
| Date | Score | What changed |
|---|---|---|
```
Write it, then `attraction-brain-sync` (PUSH) immediately and verify. No separate document by
default (the Book carries this as part of *How You Operate* in Part IV); render one on request via
`${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md`.

## Confirm (their words, no scores recited as a verdict)
*"You're at [band]. The one thing to fix first is [item 1] — here's this week's move. Your agents
will get [the strongest area] from day one; the rest we build in Weeks [n]."* Then your turn: do they
want `attraction-operations` to write the onboarding steps now?

## Re-audit (quarterly, with the goals refresh, or "re-audit my leadership")
Show last time's row, ask only what changed, re-score, append the log row, push. Scores should move;
if they have not in a quarter, say so plainly and make the stuck area item 1.

## Demo mode
Fictional member, "(illustrative — demo)" on the capacity line, same structure.

## Quality bar
The any-agent test on every "why" cell (their facts, not adjectives), the so-what test (every low
score names the first action), the delete test, no hedging, no filler headings. Never invent a streak,
an agent, or a system they did not name.
