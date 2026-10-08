---
name: lm-magnet-ideas
description: >
  Picks the member's NEXT lead magnet for attracting agents — from campaign two onward, once the Honest
  Brokerage Comparison Guide is live. Reads the type of agent they attract, that agent's pains, what the
  member can genuinely teach (the Partner Offer), the questions agents keep asking, the ideas they captured
  on the go, and what converted so far (memory/magnets.md), then recommends ONE magnet in plain words with
  one line of why — the Switching Checklist, Questions to Ask a Sponsor, the Rev Share Explainer
  (model-generic, compliance-gated), the 90-Day Plan template, the member's own system guide — each tied
  to one type of agent and one of Mike's five pains. Writes a planned row and hands the locked focus to the
  magnet writer. Never a menu; never jumps the first-campaign lock.
  Trigger on: "what's my next lead magnet for agents", "next attraction magnet", "switching checklist",
  "questions to ask a sponsor guide", "rev share explainer", "90-day plan template for new agents",
  "another guide for agents", "which lead magnet should I build next for attraction".
---

# Next Magnet Picker (campaign two onward)

The member shipped the comparison guide. Now they've earned the options — and you make the pick for them,
with conviction, from their own data. **One recommendation, one line of why, one yes.** Never a pick-list.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1 (plain, never "avatar"), #2 (the
Brain first), #9 (advise with conviction), #11 (the comparison guide is always first). The three laws:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Step 0 — Guard the lock (silent)
Pull the Brain (house rule 2). Read `memory/magnets.md`. **If no comparison guide row exists** (no row with
Status `written` or beyond), this is a first campaign at the wrong door: say one line — *"First one's always
the Honest Brokerage Comparison Guide — it earns the trust every guide after it rides on. Let's build that,
then I'll pick your second."* — and hand to `lm-navigator`. (The navigator's one-pushback allowance applies
there, not here; if it sends the member back having declined twice, proceed below as campaign one.)
If a magnet row is `written` or `designed` with no funnel, finish that first (hand to `lm-funnel`).

## Step 1 — Read what decides it (lazy)
- `identity/avatars.md` — the primary type of agent (and secondary if one exists), their biggest problem in
  their words, what they've tried, the objections to expect, "the ask that fits."
- `identity/offer.md` — what the member can genuinely teach ("Teach first," "Module 1 / first lesson," the
  five-pains table: which pains they actually solve). A magnet the member can't back with real experience is
  a pitch.
- `memory/magnets.md` — what exists, its status, opt-ins and calls booked so far (what converted).
- `memory/objections.md` — the questions agents keep asking (a question asked three times is a magnet).
- `memory/ideas.md` (tag `leadmagnet`, status open) — **the member's own ideas come first.**
- `identity/compliance.md` — the compensation policy line (decides whether the Rev Share Explainer is even
  available) and recruiting scope (decides whether a Leader's Switching Guide can mention moving a team).
- `skills/lm-magnet/references/magnet-guide.md` → "Second campaign onward" — the shapes, each tied to a type
  and a pain.

## Step 2 — Pick ONE (the method)
Score silently, never out loud:
1. **The type of agent** — the primary type from `avatars.md`. A magnet speaks to one reader.
2. **The one pain** — the pain that type lives, in Mike's five (financial uncertainty · lack of support,
   mentorship, training · technology gaps · limited growth · work-life balance and recognition).
3. **What the member can teach it with** — only a shape the Partner Offer backs. "Teach first" in `offer.md`
   is usually the answer: the member's own system (open houses, YouTube, expireds, sphere) as a guide beats a
   generic checklist every time, because only they can write it.
4. **What converted** — if the comparison guide's opt-ins skew to a question (from `objections.md` or the
   member's DMs), the next magnet answers it. If calls booked are low relative to opt-ins, pick a shape that
   makes the call the obvious next step (the 90-Day Plan template, the Switching Checklist).
5. **The member's own idea** — an open `leadmagnet` idea that fits 1–3 wins over anything you'd invent.
6. **Compliance** — the Rev Share Explainer only if the policy line allows public rev-share content (structure
   only, no figures, the income disclaimer appended); a Leader's Switching Guide only inside the recruiting
   scope, with the franchise look-period rule stated.

The shapes and their default pairings (from the reference):
- **Switching Checklist** → experienced, low production · lack of support ("switching didn't work before").
- **Questions to Ask a Sponsor** → new agent · lack of support, mentorship, training.
- **Rev Share Explainer** (model-generic, gated) → experienced or top producer · limited growth.
- **90-Day Plan template** → new agent · financial uncertainty (no direction).
- **The [member's system] guide** → the type they attract · financial uncertainty — when `offer.md` says they
  teach it (the open house routine, the YouTube launch, the expireds script).
- **Leader's Switching Guide** → team leader / broker-owner · limited growth, work-life balance.
- **Mini-course / prompt list** → agent with a brand · technology gaps.

## Step 3 — Say it (one message, plain words, never the labels)
> *"Your comparison guide's live — nice. For the next one I'd do **[the magnet, in plain words]**: it's for
> [the type of agent, plainly], it answers [the pain in their words], and it's built from [what the member
> actually does — e.g. the open-house routine you teach every new partner]. [One line on what converted, if
> there's data.] Or we could go with [one alternative, one phrase]. I'd start with the first — want me to
> write it?"*

A yes (or silence) → Step 4. A different idea → size it against Steps 2.1–2.6 in one line; if it fits, take
it; if it breaks compliance or isn't something they can teach, say so kindly and hold your pick (house rules
#9). Never more than one alternative.

## Step 4 — Lock it and hand off (silent write)
Add a `planned` row to `memory/magnets.md` — `[YYYY-MM-DD] · [Magnet Name] · [type of agent] · [pain] ·
planned · — · — · GUIDE · — · — · [date]` — and, if the pick came from `memory/ideas.md`, mark that idea
**used** (status column only). **attraction-brain-sync PUSH** (write → push → verify). Then hand `lm-magnet`
the locked focus: the shape, the type of agent, the one pain, the single core promise (the reference's example
line adapted to the member), and "built from: [the offer item]." The magnet writer skips its Phase 1.

## Never
- A menu, a numbered list, or a question box of shapes.
- A magnet the member can't teach from experience.
- Compensation figures, rankings, a named brokerage, a protected characteristic in the target.
- A second magnet before the first one's page is live — finish, then start.
