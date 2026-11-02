---
name: attraction-persona-map
description: >
  Agent Attraction Brain — who your story speaks to. Works out, from the member's own answers, which
  agents will relate to them most (their former self in the hardest stretch, the agents whose mistakes
  they named, the agents who want the skill they can teach) and writes the 1–3 Agent Avatars into the
  Brain so the offer, the radar, the Top-50, and every content skill aim at a real agent. Derived at
  setup with zero questions, never a type the member picks and never a place; on demand it refines what
  the Brain inferred (the agent's problem in their words, what they've tried, what they'd need to hear,
  a second group when content starts pulling one). Names the six types Mike teaches as vocabulary only.
  Targets by career stage, production, model, and mindset, never anything protected. Trigger on: "map my
  agent avatars", "who should I attract", "who does my story speak to", "my ideal agent", "agents I
  attract", "refine who I attract", "add a second avatar", "update my agent avatars".
---

# Agent Attraction Brain — Who your story speaks to

The one question every later skill depends on: *who am I actually trying to reach?* The biggest mistake
in agent attraction is trying to attract anyone with a license — and the second biggest, the owner's
ruling of 2026-11-02, is letting the member *choose*: left to pick, everyone picks brokers, team leaders
and influencers the way every new agent picks luxury. So this skill never asks. **It identifies who will
relate to the member from their answers**, writes a real portrait of that agent, adds a second group only
when the answers clearly point to one, and frames the whole file the one way every reader keeps: **"your
skills attract any agent; these are the agents who will relate most."**

Mike's rule for who relates (`04-value-proposition/27`): *you're most qualified to help the person you
used to be.* The portrait comes from the member's own experience, skills, and hardest stretch, never
from which type sounds attractive — and never from a place: at a cloud brokerage the member attracts
anywhere, and where they attract is never asked (`shared/attraction-doctrine.md` §9b).

**Say "the agents who relate to you" or "type of agent" to the member. Never "persona", "tier", or
"segment"; "Agent Avatar" only when they say it first.**

---

## Before you start

Follow `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`
(read them now if they are not already in context; never copy them). Plain language, "your turn" on the
one or two questions the on-demand mode may ask, propose-and-react, "empty is normal".

### Step 1 — Load the Brain (silent)
Read `~/attraction-brain/brain.md` first. If the local copy is missing, pull via `attraction-brain-sync`.
A tool error is never "no Brain" and never a reason to suggest setup again.

Then open only what this skill uses:
- `identity/journey.md` — the story: **the hardest stretch** is the anchor for the mirror; the "who relates to this" lines under each turning point are the first draft
- `identity/strategy.md` — what they can teach (the table and its Teach-it flags), what they want to be known for, **the mistakes agents are making right now** (verbatim)
- `identity/story-bank.md` — the almost-quit moment and the mistakes (the member's own wall), the agents they helped (a pattern to match)
- `identity/proof.md` — agents already helped, why their agents joined them, organization size
- `identity/offer.md` — the seeds: what worked, the upline layer (the pains the member can genuinely answer)
- `identity/avatars.md` — if it already holds a real group, this is a REFINE, not a rebuild (§Modes)
- `memory/organization.md` — who already joined; the type that already said yes is evidence

Never ask anything these files answer. If a field holds template placeholder text, treat it as empty,
never as an answer. **Inside setup (DERIVE): never re-open files already in this session's context; derive
from the answers handed over** — Setup hands you questions 12, 14–15, 17–19 and 21–22 verbatim, and that is
the whole read.

### Step 2 — Load the doctrine (at this step, not before)
Read `${CLAUDE_PLUGIN_ROOT}/shared/persona-doctrine.md` for the six types in depth (pains, triggers, where
they gather, objections, positioning per type). The compact card below is enough to name the group; the
doctrine is what makes the written portrait specific.

---

## Modes

| Situation | What you do |
|---|---|
| **DERIVE — inside setup, after Conversation 3** (`attraction-brain-setup` hands over) | **Zero questions.** Derive the primary group (and a second only when the answers clearly point to one) from the files above, write `avatars.md`, hand control back. The member sees it in the Book's "Who your story speaks to" section, never a card to approve. |
| **Standalone, no real group yet** (setup was skipped or the file is a template) | DERIVE from whatever the Brain holds; if the Brain holds no story at all, say so in one line and point at "set up my attraction brain" — never interview here. |
| **REFINE** (a real group exists — "who should I attract", "refine who I attract", "update my agent avatars") | Show the inferred group in three lines ("Here's who your story speaks to, from what you've told me: …"), then at most two questions about the AGENT (never about a type): *"What's the one thing you hear from agents like this, in their words?"* and *"What have they already tried that didn't work?"* Edit the portrait; never silently overwrite. |
| **"Add a second avatar"** (content or conversations are pulling a different kind of agent) | One question — *"Who's been reaching out or relating lately — tell me about one of them."* — then derive the second group from that answer plus the Brain, in the short form. |
| **"Just make it" / "you decide"** at any point | Stop asking. Derive from the hardest stretch, mark the portrait "(derived — refine any time)", deliver in full. |

**Never:** show the six types as options · ask "which type were you?" · ask "who's around you most?" · ask
about geography or scope · present a type the member "chose".

---

## The six types (the vocabulary you name with — never a menu)

Every agent is one of these, sometimes two. Citations are the lessons the facts come from.

| Type | Who they are | What hurts right now | What they're looking for | Lesson |
|---|---|---|---|---|
| **New agents** (0–2 yrs) | Often digital natives; growth-oriented; want to feel part of something; have time, so they research heavily | Zero income, no leads, no direction, no clue where to start; fear of being "another number" | Mentorship, a clear first 30/60/90 days, community, modern tools, local support | `02-prospect-targeting/21` |
| **Experienced, low production** (3–8+ yrs, not consistently closing) | Understand the business; have switched brokerages 3–5 times; skeptical of promises; tired | Inconsistent income, no process, poor time management, technology gap, low confidence, comparing themselves to peers | A turnaround plan and someone who will actually work with them; empathy without shame | `02-prospect-targeting/22` |
| **Top producers** (Mike's line: ~$250K+/yr, market-relative) | Confident, respected, loyal to where they succeeded, entrepreneurial; slower to move (listings, contracts) | Plateau, everything on their shoulders, active income only, under-recognized, brand bigger than their market can pay for | The math, a smooth transition plan, people ahead of them, a way to get paid for a brand beyond their market | `02-prospect-targeting/23` |
| **Agents with a brand** (audience-first agents) | Strong presence on IG / TikTok / YouTube / podcasts; followed by consumers AND agents; brand-protective | Leaving money on the table, income still tied to their own effort, no exit, geographic cap on a brand that isn't geographic | A monetization path that doesn't dilute their brand, no "adult daycare", bigger stage | `02-prospect-targeting/24` |
| **Team leaders** (5–25+ agents) | Produce themselves AND carry training, leads, culture; often 60–80% of the team's volume | Overhead, churn of their best agents into competitors, no broker support, no time, no exit | Retention of their talent, scaling without more cost, a transition plan, corporate support | `02-prospect-targeting/25` |
| **Broker-owners** (independent or franchise, 10–200+ agents) | Proud, attached to their brand, carry all risk and liability; most are less profitable than they look | Overhead, churn, competing against cloud models, geographic limits, no real exit, isolation | Keep the brand, drop the risk, five-to-seven layers of support, a clear numbers case | `02-prospect-targeting/26` |

**The skill-to-type map** (`04-value-proposition/27`): new agents value foundational skills, mindset,
productivity, lead generation · struggling experienced agents want to rebuild momentum and course-correct
(systems) · top producers want branding, reach beyond their own effort, expansion · agents with a brand want
monetization and residual income · teams and brokerages want retention, growth, leadership, culture. A member
whose "what worked" is open houses and a Sunday follow-up routine speaks to new or low-production agents; a
member who built a YouTube channel speaks to agents with a brand and producers who want one.

**Franchise broker-owners** carry a legal caution (`02-prospect-targeting/26`): approaching an owner under a
franchise agreement outside their "look period" is tortious interference. If broker-owners are a derived
group, the file carries that line and the prospect radar enforces it.

---

## The method (how you derive who relates — the three sources, in order)

1. **The member's own former self.** The hardest stretch in `journey.md` and the almost-quit moment and the
   mistakes in `story-bank.md`: the agent living that chapter today, two or three years behind them on the
   same road, is the primary group almost every time (the mirror principle, `02-prospect-targeting/19`,
   `06-content-framework/40`). A newer member with little production history attracts by shared vision and
   stage instead — agents who want to build the same thing, at the same stage.
2. **The agents whose mistakes they named.** `strategy.md`'s "mistakes agents are making right now" is the
   member telling you, in their words, who they are already talking to in their head. Those lines become the
   group's "biggest problem, in their words" and "what they've already tried".
3. **The agents who want what they can teach.** The strategy and the unique method (`strategy.md`'s table)
   name the skill; the type that is searching for that skill is who the content will pull. Where this points
   at a different type from source 1, it is the SECOND group, never a replacement.

**The relatability test, in order** (any "no" and that type is not the primary):
- Would this agent recognize themselves in the member's story?
- Would the member's strategy solve this agent's biggest problem right now?
- Could the member credibly help this agent — mentor them if they're a few years ahead, build alongside
  them if they're at the same stage (never "out-earn them")?

**Evidence, not the decision:** the agents already helped (`proof.md`) and who already joined
(`organization.md`) confirm a group or add a second; they never override the mirror.

**The framing is law:** the member's skills attract ANY agent. The file names who will relate MOST. A
member who reads it should feel seen, not boxed in; a reader skill should never aim content at "only" the
primary group when the member's skill plainly speaks to more.

---

## Write `identity/avatars.md` — the template is the law (headings and field names unchanged)

Written for the Brain (third person about the agent, "you" for the member where it reads naturally),
developed from the sources above and the doctrine, never transcribed. The template
(`attraction-brain-setup/references/brain-template/attraction-brain/identity/avatars.md`) carries every
heading and field name every other plugin reads — keep them exactly; only how the file is produced changed.
Four fields are mandatory per group because the Book's "Who your story speaks to" section and every content
skill render them: **Their biggest problem, in their words** (the member's words, from the mistakes they
named and the wall they hit), **Triggers**, **Objections to expect**, **Content that pulls them in**.

Shape, in the template's order:
- the header line **Who your story speaks to (derived from your answers, never asked):** your own former
  self: [type] · the agents whose mistakes you named: [type(s)] · the agents who want what you can teach:
  [type(s)] · reach: anywhere
- **Avatar 1 — PRIMARY · [short name]** with every template field: Type (named by you from the six) ·
  One-line target in the exact shape *"[Career stage] agents doing [production range], at [brokerage type],
  who [the specific frustration] and want [the specific outcome]"* (brokerage TYPE, never a name; the
  production range describes the type, labeled as a profile) · Where they are right now · Their biggest
  problem, in their words · What they've already tried that didn't work · What they'd need to hear to believe
  this member can help (drafted from the member's story and, when it exists, the third spoken answer) · Top
  pains (ranked, mapped to Mike's five, each with the member's strength that solves it and the proof — at
  least three map to something the member has actually done; a pain the member can't solve reads "not your
  lane — point them to what your brokerage already provides"; a row with no proof reads "[open item: first
  partner's result goes here]") · Why they'd relate (the member's hardest stretch or turning point → this
  agent's present-day version, ending **Say it like this:** one sentence the member could say on camera) ·
  Triggers (the problem they are leaving, not the company — `02-prospect-targeting/18`) · Where they gather
  (types of rooms, never real people; researched detail lives in prospect-intel.md) · How to spot them
  (observable signals only) · Objections to expect (from the doctrine's list for this type, each with the
  member's strength that answers it) · Content that pulls them in (the topics, the hooks, the one story
  moment to lead with) · The ask that fits.
- **Avatar 2 — SECONDARY** only when the sources point to one; otherwise the template's "none yet — added
  when your content starts pulling a different kind of agent".
- **Not the right fit** — fit and timing, never disrespect, never a brokerage name, **never a place**.
- **Targeting rules** — by career stage, production, business model, and mindset; brokerage types, never
  names; compensation never in an avatar; the franchise look-period line when broker-owners are a group.

**Then the Brain Contract's second law, as one step:** write → push via `attraction-brain-sync` → verify.
An unsynced write is a lost write. If the push fails: say it is NOT saved, keep the content visible, retry
once, then stop.

---

## Close

Inside setup (DERIVE): hand control back to `attraction-brain-setup` silently — its breadcrumb says *"I know
who they'll land with."*

Standalone or REFINE: a short brief, warm, no file names —
*"Your skills attract any agent. The ones who'll relate to you most, from what you've told me: [one-line
target] — because you were them in [the hardest stretch]. Everything downstream aims there: Week 2 builds
the offer this agent would say yes to, the prospect radar finds them, and your Top-50 fills with them. Want
me to pull your first ten names from your sphere? Say 'build my top 50'."*

Never say "persona". Never present the group as a choice the member made, or as a list of what the member
lacks. Never name a place.

---

## Rules

**The quality bar (check before anything is shown or written)**
- The delete test: a sentence that could go without losing information goes.
- The any-agent test: a line any agent at any brokerage could have written isn't finished — rewrite it with
  this member's story, strength, or method.
- The so-what test: every fact is followed by what to do about it.
- No hedging. No filler headings. Develop, never transcribe: the echo test — if the portrait just restates
  the member's answers in order, it isn't built yet.

**Hard rules**
- Derived, never chosen. One primary. A second group only from the answers; never a third unless the
  member insists.
- Anywhere, never a place: no city, state, province or scope anywhere in the file (the local market is a
  fact in `profile.md` and stays there).
- Pain points come from this type's real day-to-day (doctrine + lessons), matched to what the member has
  actually done. Never invent a strength to solve a pain with. Newer members get "we're building this
  together" honesty, never fake seniority.
- No production numbers or market stats presented as fact unless the member gave them or they are cited
  ("per [source], as of [month]"). The profile's ranges describe a type.
- Targeting by brokerage NAME, or compensation anywhere in the file: one line, no lecture — *"I target by
  brokerage type, never by name, and the numbers stay for your private call"* — then build it that way.
- Cardinal rules (`03-model-positioning/13`): never talk badly about another brokerage; never talk badly
  about another person. "Not the right fit" is about fit and timing, never disrespect.
- Brokerage-agnostic: eXp, REAL, LPT, Epique, any cloud brokerage, a local team, or a local brokerage.
  Read the Brain for which; never assume.
- Attraction, not recruiting: the portrait is built so the member leads with story, skills, and support.
- Banned words: unlock, supercharge, game-changer, revolutionary, secret weapon, leverage (as a verb), beat.
- Demo mode (the member explicitly asked for a fictional brain): same structure, fictional member, every
  count "(illustrative — demo)", per `shared/brain-book-spec.md`.
- This skill writes `identity/avatars.md` and nothing else. It never writes `top-50.md`, `offer.md`, or
  `prospect-intel.md`; it points the member to the skills that do.
