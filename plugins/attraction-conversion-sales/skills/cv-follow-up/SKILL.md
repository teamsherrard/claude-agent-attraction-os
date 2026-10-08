---
name: cv-follow-up
description: >
  Mike's Follow-Up Engine for agent attraction: an individualized 90-day nurture plan per prospect,
  never one drip for everyone. Built from the relationship, their intent, the objection left standing,
  their timeline, and what they said they care about: Sarah gets the case study, James gets nothing for
  30 days, Rebecca gets a call now. Every touch has a reason from Mike's trigger list (a model update, a
  notable join, new training, a resource, an event, a story, a milestone), never "just checking in". The
  week-one recap, weeks two to four value touches, the monthly story, the quarterly invite. Drafts only,
  in the member's voice, across text, email, DM, and video message. Feeds the AI Admin's Daily Follow-Up
  Queue. Trigger on: "follow-up plan for [agent]", "how should I follow up with", "nurture plan for",
  "what do I send [agent] next", "follow-up engine", "90-day plan for [agent]", "keep [agent] warm",
  "who do I need to follow up with", "my follow-up touches this week".
---

# Follow-Up Engine — the fortune is in the follow-up, and every touch has a reason

"Most agents will not join after the first conversation… regular, value-driven follow-up keeps the door
open. Follow-up should feel like leadership, not chasing" (`12-simple-tech-stack/85`). Mike does not run
a drip campaign: "I don't have a CRM where they're on some templated drip pushing everybody"
(`10-presentation-delivery/41`). The plan is per person — relationship, intent, objection, timeline, interests
(the launching doc's Follow-Up Engine spec) — and every touch leaves value.

**Write-and-prepare only.** Drafts land in chat or as email drafts; the member sends. The AI Admin's
Daily Follow-Up Queue (`admin-follow-up-queue`, Week 5) owns the daily "who is due" and its scheduled
agent; this skill builds the plan it draws from.

## Step 0 — How we speak
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`, `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`,
and `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`. Plain language, no machinery; "the agents you're
talking to", never "leads". Never the recruiter register.

## Step 1 — Load the Brain (never ask what it knows)
Read `~/attraction-brain/brain.md`, then:
- `memory/conversations.md` — what this agent said, the objection heard, the pain, the promised next step.
- `memory/top-50.md` and `memory/pipeline.md` — type, stage, last touch, next move, due.
- `memory/intel.md` — the follow-up triggers the Brain already holds (model changes, joins, industry shifts).
- `memory/organization.md` — recent joins and wins ("somebody just like you just joined").
- `identity/proof.md`, `identity/story-bank.md` — the case study, the interview, the story that answers
  their objection.
- `identity/offer.md`, `identity/positioning.md` — the resources to send; new additions to the value stack.
- `identity/operations.md` — the follow-up cadence, the weekly model call, events, the signature.
- `identity/voice.md` — so every draft sounds like them.
- `identity/compliance.md` — the gate: every touch is a prospect-facing message.
- `config.md` — whether the AI Admin block exists.
`${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md` at the trigger step if detail is needed. If
`~/attraction-brain/` is missing locally, pull via `attraction-brain-sync`. A tool error is never "no Brain".

**No conversation row for the named agent?** One question: *"I don't have notes on [name] yet — how did the
last conversation go, and what did they push back on? Two lines, or paste the thread. Your turn."* Then
`cv-debrief` logs it, and this skill continues.

## The five principles of follow-up (Mike's, `12-simple-tech-stack/85`)
1. **Always leave value** — never "just checking in" ("you're annoying, go away").
2. **Share updates that benefit or inspire them.**
3. **Personalize the touch to what matters most to them** — "it's not about you… it's what they care about."
4. **Use multiple channels** — text, email, DM, video message.
5. **Consistency matters more than frequency** — stay in touch at the pace their interest sets.
*(The cohort materials call this skill "the 5-Point Framework"; the five points are not defined anywhere
in the vault beyond these five principles in lesson 85 — `${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md`
§7 reads them the same way — so these five are what the engine enforces; flagged DECISION NEEDED for Mike.)*

## The reasons a touch is allowed to exist (Mike's trigger list — `/85`, `/42`)
A touch with none of these is not sent; it is replaced or the date is moved:
- **A positive change to the brokerage model** — compensation, stock, rev-share structure, co-sponsorship,
  going public (from `intel.md`; facts with a date, never an earnings claim).
- **New tools or technology rolled out** — a CRM choice, an AI platform.
- **New training or an update to the member's value proposition** — "we just rolled out X; it solves exactly
  what you mentioned" (`offer.md` changes, Value Vault additions).
- **A notable join** — a team, a broker-owner, an agent of the same type: "they just made the move, they're in
  a similar position — made me think of you."
- **A win or recognition in the member's organization** — "somebody just like you hit the milestone you told
  me you want."
- **An event coming up** — the brokerage's conference, the member's mastermind or weekly model call; the
  invitation IS the value.
- **An industry shift that makes the model more attractive** — regulation, lawsuits, rates: "a lot of agents
  are rethinking their brokerage — curious how you're approaching it."
- **A resource that answers their objection** — the interview with an agent who had the same objection, the
  case study, the training module.
- **Their life** (`/42`) — a milestone, a trip, a holiday, a new listing they posted: congratulate, thank,
  a personal video message. Nothing from a search; only what they shared or posted publicly.

## Step 2 — Place the agent (the decision that sets the pace)
From the ledgers, in one line each: **relationship** (cold · acquaintance · warm · post-call) · **intent**
(High / Medium / Low from the last debrief) · **objection standing** (bank entry, by name) · **timeline**
(what they said: "after my closings", "when my cap resets", "next year", none) · **interests** (what they
lit up about). Then the pace, Mike's rule: "if they're super interested, stay on top of them; if not,
whenever it feels right." Three honest patterns, named for the member:
- **Call now** — high intent, a date or a trigger just fired (the Rebecca case). The next touch is today,
  by phone or voice note; the plan is a week long.
- **Value cadence** — medium intent or an objection standing (the Sarah case): the next touch is the
  resource that answers the objection, then the 90-day cadence below.
- **Leave it alone for 30 days** — they asked for space, just switched (`11-objection-handling/61`), or
  are mid-transaction (the James case): one date in the diary, nothing before it unless a real trigger
  fires. Silence is a move when it is chosen.

## Step 3 — The 90-day plan (Mike's simple plan, `/85`, individualized)
Build the plan as dated touches, each with **reason · channel · what to send · the one personal line**:
- **Week 1 — the recap** (always, after any first conversation): the personal first paragraph plus all the
  resources, "thank them for the time… write something personal so they know you listened." If `cv-debrief`
  already drafted it, reference it; never draft twice.
- **Weeks 2–4 — value touches**: one or two, each tied to a trigger above or to the objection standing
  (the interview, the case study, the training clip). Multiple channels across the month.
- **Monthly** — a success story or an industry update, when there is a real one.
- **Quarterly** — an invitation: the event, the webinar, the mastermind, the weekly model call.
- **Any time a trigger fires** — a join, a model change, their milestone: move the next touch up.
Cap the plan at what the member can actually do (`goals.md` weekly follow-up activity; `operations.md`
hours). A plan of fifteen touches nobody sends is worse than four they do.

**Timeline-shaped plans:** "after my closings" → the proactive transition plan behind the scenes (`/58`):
touches become working sessions, and the launch interview is scheduled for the move week. "When my cap
resets" (`/60`) → the date is the anchor; the touches before it build the day-one strategy.

## Step 4 — Draft the touches (compliance gate first)
Read `identity/compliance.md`: `unset` → the plan is built and shown, but no message draft leaves the chat
— say in one line that drafts need their compliance basics ("set up my attraction compliance", three minutes). `set`
→ apply and remind once. `confirmed` → apply.
Then draft the **next two touches** in full (not all twelve — usage discipline), in the member's voice:
short, personal first line, the reason stated plainly, one link or one attachment, one soft open door;
no compensation figures, no earnings claims, nothing negative about anyone; "it made me think of you",
never "circling back". Email → create a **draft** in the email connector (draft-only on both providers;
say where it is). Text / DM → paste-ready in chat. Video message → a 20–30 second script for Loom or a
voice note. Later touches are one line each with their reason and date. Read every draft back against the NEVER list before it is shown (house rules #9: no immediate pitch, no wall of text, no corporate recruiting language, no compensation, nothing AI-sounding, no fake personalization, no forced Zoom); one failure = rewrite.

## Step 5 — Write, push, hand to the queue
- **The plan file:** `memory/intel-reports/YYYY-MM-DD-[agent]-follow-up.md` (this plugin owns the folder):
  placement, the dated touches with reasons, the drafts. Newest file is current.
- **Next move and due date:** the pipeline Board's **Next move · Due** for that agent — written directly
  only when the AI Admin is not installed (same vocabulary), otherwise **requested** in one line for
  `admin-pipeline`; the Top-50 row's Next move · Due follow the same rule (the capture skill's interim
  allowance).
- **A new trigger learned from the member** ("my brokerage just announced…") → hand it to `attraction-capture`
  (it owns that write — the Watcher's `memory/intel.md`); never written from here.
- **When the member says a touch went out:** append one `memory/conversations.md` row in the locked shape —
  Date · Agent · Type · Channel · "What they said" = their reply if there was one, else *(touch sent — [the
  reason])* · Objection = — · Pain · Next step = the next dated touch · `Stage after` = the current stage,
  unchanged — and update that agent's Last touch · Next move · Due per the rule above. A reply that changes the
  stage goes through `cv-debrief`. Never log a touch the member didn't say they sent.
- Then `attraction-brain-sync` PUSH, verify. Unsaved → say so, keep the plan visible, retry once, stop.
- **Hand-off:** *"Your Daily Follow-Up Queue picks these up each morning"* — only if the AI Admin is
  installed; otherwise: *"Say 'who do I need to follow up with' any Monday and I'll pull what's due."*

## "Who do I need to follow up with" (the weekly pull, when the Admin isn't installed)
Read `top-50.md` and `pipeline.md` for every agent whose **Due** is this week or overdue, plus anyone
at Call held or 3-way with no touch in 14 days. List: name · stage · reason to reach out (a trigger from
`intel.md` / `organization.md`, or the objection standing) · the draft in one line. Five at most, the
rest collapsed. Never a touch without a reason; if none exists for a name, say "no reason yet — leave it"
and move on. Quiet for 30+ days → hand to `cv-reactivation`.

## The Switching Transition Plan (an asset, behind a gate)
The one-pager that answers "I have closings to finish" — license transfer, listings and the ICA check,
MLS, email, signage, the launch interview, the week-by-week plan (`11-objection-handling/58`). Build it
only when `identity/compliance.md` shows **Inducement rules reviewed: yes**; otherwise say in one line that
it waits on that review (it is on the Brain Book's open-items page) and draft the transition conversation
instead. Rendered per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` via `render_doc.py` into the
workspace's `04 · Agents/Prospects` folder, dated; the renderer's `RENDERER-UNAVAILABLE` path installs
nothing and uploads the `.md`.

## Demo mode
Fictional member and agents, no ledger reads of a real Brain, every number "(illustrative — demo)".

## Quality bar
Every touch has a reason the member can say out loud; no two prospects get the same plan; drafts pass the
any-agent test (a line that fits every prospect is cut); no "just checking in", "circling back", "touching
base"; dates, not "soon"; nothing the agent didn't tell the member or post publicly; cardinal rules intact.
