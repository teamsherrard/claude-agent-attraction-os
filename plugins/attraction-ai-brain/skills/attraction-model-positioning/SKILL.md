---
name: attraction-model-positioning
description: >
  Agent Attraction Brain — Model Positioning. How the member positions their model, team, or
  brokerage without pitching: the one-line "why I'm here" they can say out loud, the two-minute
  model script for a private call, the Model Positioning Sheet (what to lead with per type of agent,
  what they'll ask, what stays for the private call, what to say when they name another brokerage or
  sponsor), and the agents-follow-people framing that makes the member the reason, not the logo.
  Enforces Mike's two cardinal rules hard: never a negative word about another brokerage or another
  person. Compensation never appears; it is answered on a call. Writes identity/positioning.md and
  renders the sheet. Week 2. Trigger on: "position my model", "position my brokerage", "my why I'm
  here line", "the two-minute model script", "model positioning sheet", "how do I talk about my
  brokerage without pitching", "what do I say when they mention another brokerage", "bridge the
  gap", "update my positioning".
---

# Agent Attraction Brain — Model Positioning

`03-model-positioning/17`: *agents follow people, not companies.* Mike's research line is that 87% of
agents who switch prioritize leadership, mentorship, and support (his figure, from that lesson). They
are asking three things: **Will you guide me? Will you help me succeed? Do you have a clear path I can
follow?** The brokerage is the vehicle; the member is the reason. Positioning is how the member says
that out loud, in their own words, so an agent hears a leader and not a recruiter.

This skill produces four things and writes one file:
1. The **one-line "why I'm here"** — said out loud, in bios, on camera.
2. The **two-minute model script** — for the private call, after discovery, never sent.
3. The **Model Positioning Sheet** — per type of agent: lead with, they'll ask, stays private, the bridge.
4. **What stays for the private call** — the explicit list.

---

## Before you start

Follow `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`
by reference.

### Step 1 — Load the Brain (silent)
Read `~/attraction-brain/brain.md` first; pull via `attraction-brain-sync` if the local copy is missing. A
tool error is never "no Brain".

Then only what this skill uses:
- `identity/profile.md` — brokerage, what they're building, how long there
- `identity/journey.md` — the three beats; **Stop 2's "why I actually joined"** (the real reason, not the
  brochure) and **the one line they'd say if asked "why are you there?"** (setup Q7 / Q36)
- `identity/strategy.md` — what they want to be known for; what they can teach
- `identity/positioning.md` — the seed line from setup if present; real content = update, not rebuild
- `identity/avatars.md` — the primary type and its ranked pains (the sheet is written primary-first)
- `identity/brokerage-model.md` — the plain-English mechanics and the "never say" list (if built; if not,
  the sheet's mechanics lines read "[the Brokerage Model Expert fills this in — say 'learn my brokerage
  model']" and nothing is invented)
- `identity/offer.md` — `Status:` and the three layers (brokerage · upline · you). If Status is seeds,
  the script's "what I add" beat uses the raw material and says Week 2's offer skill sharpens it; it never
  demands an offer that isn't built.
- `identity/proof.md` — agents helped, organization size (the "prove what you say" beat, `/17`)
- `identity/compliance.md` — the **3-state gate** for anything public (below)

### Compliance gate — before the one-liner or script is handed over as public words
Read `identity/compliance.md`. **Set / confirmed** → proceed, apply its rules (brokerage name and
license display where their rules require it in bios; no compensation in public). **Unset** → still
write the Brain file and show the member their private-call material, but hand over the public-facing
one-liner and bio lines with this plain line and nothing else: *"Before this goes in a bio or on camera,
your compliance rules need setting — say 'set my compliance rules' and it's five minutes."* "If empty,
proceed" is banned.

---

## The two cardinal rules — enforced, not suggested (`03-model-positioning/13`)

1. **Never talk badly about any other brokerage.** If the member must tear another brokerage down to
   prop theirs up, they don't understand how to position their own value. Every model has pros and cons;
   the sheet positions pros, never someone else's cons.
2. **Never talk badly about any other person**, including other sponsors at their own brokerage. Agents
   sponsor-shop. Word gets back. Be the better person, every time.

**The posture when an agent names another brokerage or sponsor** (Mike's own, `/13`): give credit —
*"They're great, I've heard good things"* — then revert immediately to what you can do, the value you
provide, the people you've helped. If the member has heard negatives: say nothing about it, and come
back to the value. Never "I've heard they..." in a positioning line.

**Enforcement in this skill:** every line this skill writes is read back against both rules before it is
shown. A violation is rewritten, never softened. If the member asks for a comparison that names another
brokerage's or person's flaw: one line — *"I'll keep that off the page; here's how to say the same thing
on your strengths"* — then the strength version, in full. No lecture.

---

## Stop A · Your line (2–4 questions, one stop)

Orient: *"Next: how you talk about where you are, without it sounding like a pitch. Three quick ones."*

Fold in what the Brain holds (the setup one-liner is read back, not re-asked):
1. *"Here's the line you gave me for 'why are you there?' — [quote]. Still true, or has it sharpened?"*
   (no seed line → *"If an agent asked 'why are you there?', what's the honest thing you'd say right
   now? Not a pitch, the real thing."*)
2. *"When an agent tells you they're also talking to another brokerage or another sponsor, what do you
   say today?"* (this is where the cardinal-rule posture gets built from their actual habit)
3. *"Of the three things agents are really asking — will you guide me, will you help me succeed, do you
   have a clear path — which one are you strongest at today, honestly?"*
4. *(only if `offer.md` Status is finalized)* *"Anything in your offer that should be in the two-minute
   version, or does it stay for the call?"*

**Your turn.** Unsure on 1 → propose three one-liners built from Stop 2's "why I actually joined" and
the journey, say why each fits, recommend one. Their choice is final.

---

## Build

### 1. The one-line "why I'm here"
In the member's voice (`identity/voice.md` if built), first person, under 25 words, passes the swap test
(another agent could not say it word for word), names a person-reason not a logo-reason, contains no
compensation and no brokerage comparison. Three alternates: story-led · outcome-led · support-led.
Plus the bio-safe version (one sentence for Instagram / YouTube / LinkedIn; the Short-Form plugin's
profile audit reads it).

### 2. The two-minute model script (private call only, after discovery)
`02-prospect-targeting/19`: the model is presented on a private one-on-one call, tailored to what the agent
said they want and why they're not getting it — never by text, never by sending a video, never cold.
The script is a skeleton the member speaks, not a monologue they read. Beats:
1. **Mirror what they said** (one sentence from discovery: their goal, their frustration).
2. **The problem agents leave** (`/18`): *"Most agents leave problems, not companies — [their problem]
   is one of the big ones."*
3. **Why I'm here** — the one-liner, then the real reason from Stop 2.
4. **What the vehicle gives, in plain words** — three to five mechanics from `brokerage-model.md`, as
   benefits to THIS type of agent (`04-value-proposition/32`: feature → benefit → outcome), no numbers:
   support layers, training, how a brand can grow beyond a market, how someone's best agent can stay
   their partner — only the ones true for the member's model.
5. **What I personally add** — the "you" layer from `offer.md` (seeds → the one thing they'd teach first,
   stated as that; finalized → the UVP one-liner).
6. **Proof** (`/17`: prove what you say) — one agent helped, or "I'm doing this myself right now and
   here's what's happened", never fabricated; none yet → the upline's proof as "we / our group"
   (`02-prospect-targeting/21`), named generically.
7. **The money line** — *"The numbers are real and I'll walk you through every one of them — on a call
   with [my upline / our broker], because I want you to see them properly, not hear me wing them."*
8. **The ask** — one next step (a follow-up call, a 3-way with the upline, a look at the training).

Under the script: three lines the member says **when the agent names another brokerage or sponsor**,
written in the give-credit-then-revert posture.

### 3. The Model Positioning Sheet
```
| Type of agent | Lead with (the bridge) | They'll ask | Stays for the private call | One line I can say |
```
Primary avatar row first, full; the other five short. Content comes from the agent-type lessons:
- New agents (`/21`): mentorship and five-to-seven layers of support vs one busy broker; a 30/60/90 plan;
  "you'll never be a number"; local-office and "I love my broker" objections answered on strengths.
- Experienced, low production (`/22`): the turnaround plan; empathy without shame; proof of agents who
  switched before and it finally worked here (upline proof if none).
- Top producers (`/23`): respect first; "surround yourself with people doing more"; a proactive transition
  plan; the math is theirs to run with the upline.
- Influencers (`/24`): brand stays the focal point; "your audience can partner with you from anywhere";
  "I take the calls, you keep creating".
- Team leaders (`/25`): "your best agent can leave your team and still be your partner"; overhead and
  adult-daycare relief; corporate helps with the transition.
- Broker-owners (`/26`): keep the brand and ownership, drop the risk and liability; look period first.
Every "Lead with" is a strength of the member's model, never a weakness of someone else's. A row whose
mechanics don't exist in the member's model (a local team with no rev share) says what IS true for them.

### 4. What stays for the private call (the explicit list)
Splits, caps, fees, tiers, stock or cap-back details, any dollar figure, any comparison of two brokerages'
numbers, anything the member heard second-hand, the member's own rev share. Public content gets: story,
what they teach, support, proof, the one-liner, the ask.

---

## Write `identity/positioning.md`
```
# Positioning — [Member first name]
Updated: [YYYY-MM-DD] · Model: [from brokerage-model.md or profile.md] · Offer status: [from offer.md]

## Why I'm here (one line)            [the chosen line + the three alternates + the bio-safe version]
## The three questions                 [guide / succeed / path — one honest line each on how the member answers them today]
## The two-minute model script         [the eight beats, in the member's words]
## When they name another brokerage or sponsor   [three lines, give credit → revert to value]
## Model Positioning Sheet             [the table]
## Stays for the private call          [the list]
## Rules for every reader
Cardinal rules: never a negative word about another brokerage or person. Compensation never in public
content. Brokerage name and license display per compliance.md where required.
```
Write → push via `attraction-brain-sync` → verify, one step. If the push fails: say it is NOT saved, keep
the content visible, retry once, stop.

**Deliverable (default in Week 2, one doc):** the Model Positioning Sheet as structured text through
`${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py` per `shared/doc-formatting.md`, saved as
`Model Positioning Sheet · [Member] · [YYYY-MM-DD].docx` to `05 · Offer` (newest date is current), with
"Private-call material" in the meta line. If the renderer reports it is unavailable, do not install
anything: save the structured text as a `.md`, upload that, and say in one line that the styled version
needs the renderer.

---

## Stop B · Read-back (optional, one question)
Show the one-liner and the script's beats 3–5. *"Would you say this out loud, word for word? Change
anything that isn't you."* **Your turn.** Edits are verbatim; never overwrite a real answer with a guess.

---

## Close
*"You can now answer 'why are you there?' in one breath, and the model on a call in two minutes — without
a number and without a word about anyone else. The YouTube and Short-Form systems read your one-liner for
bios and intros; your call prep reads the sheet. Want the 60-second version of your story to go with it?
Say 'build my why join me story'."* (`attraction-why-join-me` owns that.)

---

## Rules

**Quality bar:** the delete test · the any-agent test (a line any sponsor at any brokerage could say isn't
finished) · the so-what test · no hedging · no filler headings · the swap test on every first-person line.

- **Attraction, not recruiting:** lead with story, skills, support; compensation on a private call, never
  in content, never in the one-liner, never in the sheet's "Lead with".
- **Cardinal rules** are enforced by read-back, not by reminder.
- **No income promises, no rev-share earnings claims, no stock potential** (`/14`).
- **Zero fabrication:** proof only from `proof.md`; mechanics only from `brokerage-model.md` or the
  member; "we / our group" proof is named generically and honestly.
- **Brokerage-agnostic:** eXp, REAL, LPT, Epique, any cloud brokerage, a local team, a local brokerage —
  the sheet positions what the member actually has.
- **Former brokerages are never named** in any beat ("a franchise", "an independent").
- **Later-week deliverables never demanded early:** offer seeds are used as seeds; the script says what
  the member teaches first and that Week 2's offer skill sharpens it.
- **Draft-only:** nothing here is sent or published; the member speaks it.
- **One owner per file:** writes `identity/positioning.md` only.
- Banned words: unlock, supercharge, game-changer, revolutionary, secret weapon, leverage (as a verb).
