---
name: cv-question-funnel
description: >
  Mike's question funnel for agent conversations and partner calls: the discovery questions (where they are
  now), the vision questions (where they want to be), and the commitment questions (bridging the gap),
  adapted to the type of agent the member is talking to — new agent, experienced low-production, top
  producer, agent with a brand, team leader, broker-owner — and to what the member already knows about this
  person. Carries the rule that questions control conversations and the 30% talk-time rule, with what to do
  when the member catches themselves presenting. Trigger on: "what questions do I ask", "discovery questions",
  "question funnel", "questions for a team leader", "how do I get them talking", "vision questions",
  "commitment questions", "I talk too much on calls", "questions for my call with [name]".
---

# Question Funnel — questions control conversations

"Questions are where the game is won. Statements push. Questions pull." (`10-presentation-delivery/44`).
Questions shift the focus onto them, uncover pains, desires, and objections, and open loops only the member
can close. The three categories, in order, are the funnel. Doctrine: `${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md`
§4. House rules: `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`.

## Before writing (silent)
`brain.md` first (pull if missing) · `identity/avatars.md` (the type and its pains) · `identity/offer.md`
(what the member can actually solve — questions should open loops the member can close; seeds stage → open
loops around what they have to give so far) · `identity/journey.md` (the beat that lets the member say "I was
there") · for a named agent: `memory/intel-reports/` newest, `memory/conversations.md` rows, the Top-50 row ·
`identity/voice.md` (the questions are written as they'd ask them). Fast lane: a type or a name is enough;
no questions asked. Nothing known → ask ONE: *"Who's it for — a new agent, an experienced agent who's stuck,
a top producer, someone with a big following, a team leader, or a broker-owner? Or a name."* **Your turn.**

## The funnel (Mike's three categories, `/44`)
**1. Discovery — current state.** Pinpoint where they are and what frustrates them.
Mike's three: *What do you love about your current brokerage?* · *What's frustrating you most right now?* ·
*What do you feel is missing?* Plus the opener set from `bonus/perfect-presentation`: *What piqued your
interest and made you open to this conversation?* · *What are your biggest challenges right now?* · *What's
holding you back from hitting your goals?* · *Are you on track to hit your target this year?*

**2. Vision — future state.** Open the loop the model and the offer will close.
*If nothing changes at your current brokerage, where do you see yourself 12 months from now?* · *What would
doubling your business mean for you and your family?* · *What would make you feel confident in achieving your
potential?* · *What's your five-to-ten-year vision?* (`bonus/bridging-the-gap`).

**3. Commitment — bridging the gap.** Only after 1 and 2; built from their own words.
*If I could show you a way to [their vision] without any extra time away from your family, would you be open
to it?* · *What's more important — repeating another year in the same spot, or [their outcome]?* · *If we can
solve [the problem they named], would you be ready to go all in?*

## Adapted per type (the shape stays; the examples change — `persona-doctrine.md` §9)
| Type | Discovery leans on | Vision leans on | Commitment leans on |
|---|---|---|---|
| New agent | what they were told success would look like; what the first months have actually been; who answers their questions | a first full year with a plan and a person | "if you had a 30-60-90 plan and someone in your corner every week…" |
| Experienced, low production | what they've tried; what a good month looks like; where the leads come from and what they cost | consistent closings without the chase | "if the inconsistency were solved, would you go all in?" |
| Top producer | what happens if they stop; what builds past this year; who pulls them up | an exit, wealth beyond active income, respect | "if the next five years could build something that pays you when you're not closing…" |
| Agent with a brand | what their audience asks for; what the attention is turning into | monetizing the audience without running a team | "if the reach you already have could become income without adult daycare…" |
| Team leader | what their agents struggle with; what retention costs them; what the overhead is | partners instead of competitors; an exit that isn't selling the team | "if your agents could stay yours and the company carried the overhead…" |
| Broker-owner | what the business is worth today; what the risk and liability feel like; what they'd keep | keeping the brand, dropping the cons; a willable asset | "if you could keep the name and lose the liability, what would stop you?" |

## The talk-time rule and the catch
- The member talks about **30%** of the call; the agent talks 70% (the workshop's and the plan's rule — the
  transcript's words are "ask questions, be curious, and listen" and "stop word-vomiting," doctrine §4).
- **The catch:** when the member notices they've been talking for more than a minute, they stop with a question:
  *"— but tell me, how does that land for you?"* · *"what's your version of that?"* · *"does that match what
  you're seeing?"* The funnel includes three of these "hand-it-back" lines in the member's voice.
- Never talk over the agent; let every answer finish (`/41`). Silence after a question is theirs to fill.

## Output
```
DISCOVERY (current state) — 4–6 questions, ordered, in their voice, chosen for [type / name]
VISION (future state) — 3 questions
COMMITMENT (bridging the gap) — 2–3 questions written from the pains above, with [their words] slots if no name
HAND-IT-BACK LINES — 3
WHAT YOU'RE LISTENING FOR — one line per discovery question: the pain or signal it surfaces and which part of your offer answers it
```
For a named agent: the questions use what they wrote in the booking form and the intel report; the "listening
for" column names the objection each answer may surface (archetypes, `11-objection-handling/46`).
Offer the funnel as a one-page document (render per `shared/doc-formatting.md` → `04 · Agents/Prospects` for a
named agent, `05 · Offer` for the type-level set) only after delivering in chat.

## Rules
- Questions never contain the pitch ("have you considered a brokerage with rev share?" is a statement wearing a
  question mark). No compensation, no model, no "join" inside a question.
- Cardinal rules: no question invites them to run down their broker; "what's frustrating you" is about them.
- No income claims hidden in a vision question ("what would an extra $100k mean" — never a number the member
  can't ground; use their own words or "doubling").
- The any-agent test: a set that fits every type is not finished.
- Banned words and the recruiter register per `how-we-speak.md` §7.

## Close
*"Ask these in order and let the silence do the work. Want me to fold them into a full call prep for [name]?"*
