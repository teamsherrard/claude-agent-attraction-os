---
name: lm-magnet-ideas
description: >
  Recommends the member's lead magnet for attracting agents — every campaign, first and later. Reads
  the finished Partner Offer (the UVP one-liner, the unique mechanism, the Teach-first lessons, the
  five pains), the type of agent they attract, their proof, the questions agents keep asking, and
  what converted, then puts exactly three recommendations in one plain message, each built from the
  member's own offer: their system as a guide, checklist, or template; the result their agent wants,
  as a plan; the question agents ask most, answered honestly. Each names who it's for, the pain,
  what it's built from, and why Mike would recommend it, with the lesson. Recommends number one so
  "yes" works. No default magnet; no two lists alike. Trigger on: "lead magnet ideas", "which lead
  magnet should I make", "what's my next lead magnet for agents", "another guide for agents", "next
  attraction magnet", "switching checklist", "questions to ask a sponsor guide", "90-day plan
  template for new agents".
---

# Lead Magnet Recommender — three from the member's offer; the member picks

Every member's magnet is built from their own unique value proposition, so no two look alike. You read the
finished offer and Mike's training, put **exactly three** recommendations in front of the member, recommend
the first with conviction, and let them pick. This is the one place in the plugin a numbered list of three is
allowed (house rules #1) — still a normal chat message, never an option widget.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1 (plain, never "avatar" or "UVP"
out loud), #2 (the Brain first), #9 (advise with conviction), #11 (the magnet is chosen from the member's
offer; no default magnet; a comparison guide is one shape among many). The three laws:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Step 0 — The Brain and the offer (silent)
Pull the Brain (house rule 2). Read `identity/offer.md` → `Status:`. **Seeds, missing, or placeholders** →
the offer comes first, in this session: hand to `lm-navigator` Step 1 (it builds the offer with the member
and returns here). Never recommend a magnet from an unbuilt offer — there is nothing to build it from.
Read `memory/magnets.md`: a row `written` or `designed` with no funnel URL → finish that first (one line, then
`lm-funnel`); a `planned` row with no doc → the pick already happened; confirm it in one line and hand off.

## Step 1 — Read what decides it (lazy — open only these)
- `identity/offer.md` — **the source of every candidate:** the UVP one-liner ("I help [agent] achieve
  [outcome] through [mechanism]" — the `## UVP` section's first line, or the `UVP one-liner:` line), the
  framework (`## The framework` — the named steps, each with what the partner does, what they get and the tool or
  template; the step the `Lead-magnet seed:` line under `## How to talk about it` names is the first candidate),
  the program (`## The program` — the name, the type and the 90-day outcome a magnet points toward), the
  unique mechanism, the Teach-first lessons (lesson 1 first — the thing the member can record tonight), the
  seven parts (core promise, proof, support), and the five-pains table — which pains the member genuinely
  solves and with what.
- `identity/avatars.md` — the primary type of agent (and secondary if one exists), their biggest problem in
  their words, what they've tried, the objections to expect, the ask that fits.
- `identity/strategy.md` — what worked in production and the "Teach it: yes / partly / not yet" flags.
- `identity/proof.md` — the results the magnet may cite (consent on file).
- `memory/objections.md` — the questions agents keep asking; **a question asked three times is a magnet.**
- `memory/ideas.md` (tag `leadmagnet`, status open) — **the member's own ideas come first.**
- `memory/magnets.md` — what exists, its status, opt-ins and calls booked so far (what converted).
- `identity/compliance.md` — the compensation policy line (whether a rev-share explainer is even
  available) and recruiting scope (whether a leader's guide can mention moving a team).
- `${CLAUDE_PLUGIN_ROOT}/skills/lm-magnet/references/magnet-guide.md` → "The shapes" — the shapes, each
  with its page structure and its default pairing of type and pain.

## Step 2 — Generate candidates along three lanes (silent)
Every candidate is something the member can teach from experience (`04-value-proposition/27`: you are most
qualified to help the person you used to be) and something an agent would trade an email for
(`15-advanced-scaling/73`: guides, checklists, scripts, prompts, mini-courses are the assets that build a
list). Three lanes, so the three differ in kind:

1. **The mechanism magnet** — the member's own system as a guide, a checklist, or a template: ONE step of the
   framework, cut out whole with its tool or template (`## The framework` — the step the offer's `Lead-magnet
   seed:` line names comes first) or, on an older offer without a framework, from
   Teach-first lesson 1 (the open-house routine · the Sunday follow-up · the sphere plan · the expired
   script · the listing-launch sheet). The thing only they can write, because they did it.
2. **The outcome magnet** — the result the primary type of agent wants (the UVP's outcome; `avatars.md` →
   Offer direction) as a plan or roadmap: "your first 90 days, mapped," "the 30-day plan to [outcome]."
3. **The question magnet** — the question agents ask the member most (`objections.md` ×3; `avatars.md`
   objections), answered honestly. A fair comparison guide, a questions-to-ask-a-sponsor guide, or a
   switching checklist are shapes here **ONLY when they fit the UVP** — the member's mechanism is about
   choosing or switching well, their type researches brokerages before talking to anyone
   (`02-prospect-targeting/21`, `/22`), and they can speak to it from their own move. Otherwise this lane
   answers the real question with a straight page (a prompt list, a script, an FAQ guide).

If a lane has no honest fit, fill it with a second mechanism or outcome candidate — still three, still
distinct in kind.

## Step 3 — Score silently, never out loud
1. **UVP fit** — must be teachable from the offer (a framework step, a Teach-first lesson, the mechanism, or a "Teach it: yes"
   strategy). A magnet the member can't back with real experience is a pitch — out.
2. **The primary type of agent's pain**, in Mike's five (financial uncertainty · lack of support, mentorship,
   training · technology gaps · limited growth · work-life balance and recognition) — the one that type
   lives, from `avatars.md`; a magnet speaks to one reader and one pain (`02-prospect-targeting/18`).
3. **What converted** — opt-ins and calls booked on earlier magnets (`magnets.md`); if calls are low
   relative to opt-ins, favor a shape that makes the call the obvious next step (a plan, a checklist).
4. **The member's own ideas** — an open `leadmagnet` idea that passes 1–2 outranks anything you'd invent.
5. **Compliance** — a rev-share explainer only if the policy line allows public rev-share content
   (structure only, no figures, the income disclaimer appended); a leader's switching guide only inside the
   recruiting scope, with the franchise look-period rule stated; nothing that names another brokerage.

Pick the top three (one per lane where possible); rank them; number one is the one you'd bet on.

## Step 4 — Say it: ONE message, plain words, exactly three

> *"Based on your offer and Mike's training, these are the three lead magnets Mike would recommend you
> create:*
>
> *1. **[The magnet, in plain words — e.g. The Five-Step Sunday Routine: the open-house follow-up system,
> step by step]** — for [the type of agent, plainly — e.g. agents two to five years in who are paying for
> leads that don't close]; it answers [the pain in their words — e.g. no reliable next client]; built from
> [the offer item — e.g. the Sunday routine you teach every new partner in week one]. Why Mike would pick it:
> [one line — e.g. you're most qualified to help the person you used to be, and this is the exact thing that
> got you out] (Mike's lesson: [module/lesson — Lesson title]).*
>
> *2. **[Magnet two]** — for […]; it answers […]; built from […]. Why Mike would pick it: […] (Mike's lesson:
> […]).*
>
> *3. **[Magnet three]** — for […]; it answers […]; built from […]. Why Mike would pick it: […] (Mike's
> lesson: […]).*
>
> *I'd go with the first — [one line on why it beats the other two for this member]. Say yes and I'll start
> it, or tell me which one resonates."*

**Lesson citations:** cite only lessons that resolve in the Support plugin's lesson index
(`plugins/maa-claude-support/shared/kb/kb-index.md`), as `module/lesson — title`. The lead-magnet lessons:
`15-advanced-scaling/73 — Building an email list` (trade a real asset for an email; give the information
away) and `12-simple-tech-stack/84 — Social Media to Nurture` (value content: free prompts, lead magnets,
courses). The grounding for WHICH magnet is the value-proposition module — `04-value-proposition/27 —
Identifying Your Niche` (the person you used to be), `/31 — Free vs. Paid` (evergreen information is free),
`/32 — Features vs. Benefits` (outcomes, not features), `/33 — Building Your Irresistible Offer` (the core
promise and the mechanism) — plus the type's lesson (`02-prospect-targeting/21`–`/26`) for the pain. When no
lead-magnet-specific lesson covers a card, ground it in the value-proposition lessons and say so in the card
("Mike's lesson on building the offer: …"). Never a lesson number you haven't seen in the index.

**The reply:** a **yes** (or silence, or "you pick") → number one. **A number** → that one. **A different
idea** → size it against Step 3 in one line; if it fits, take it (*"That works — it's something you've done
and it answers the pain. Let's build it."*); if it breaks compliance or isn't something they can teach, say
so kindly and hold your pick (house rules #9). Never more than one round of alternatives.

## Step 5 — Lock it and hand off (silent write)
Add a `planned` row to `memory/magnets.md` — `[YYYY-MM-DD] · [Magnet Name] · [type of agent] · [pain] ·
planned · — · — · GUIDE · — · — · [date]` — and, if the pick came from `memory/ideas.md`, mark that idea
**used** (status column only). **attraction-brain-sync PUSH** (write → push → verify). Then hand back the
**locked focus**: the shape · the type of agent · the one pain · the single core promise (the reference's
promise line adapted to the member) · "built from: [the framework step and its tool or template — or, on an older offer, the UVP mechanism or Teach-first lesson]."
- Came through `lm-navigator` → it runs the intake (its Step 4) and hands `lm-magnet` the focus plus the answers.
- Entered directly → run the navigator's intake yourself
  (`${CLAUDE_PLUGIN_ROOT}/skills/lm-navigator/references/intake-questions.md`: saved intake first, at most
  five questions, one at a time, pre-answered), then hand `lm-magnet` the focus plus the answers. It skips
  its Phase 1 either way.

## Never
- A default magnet, or the same three for two members. Every card names what in THEIR offer it's built from.
- A question box; more than three; a menu of shapes without the why.
- A magnet the member can't teach from experience.
- Compensation figures, rankings, a named brokerage, a protected characteristic in the target.
- A second magnet before the first one's page is live — finish, then start.
- A lesson citation that doesn't resolve in the index.
