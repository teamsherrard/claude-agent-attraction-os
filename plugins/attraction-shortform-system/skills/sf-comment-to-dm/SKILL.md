---
name: sf-comment-to-dm
description: >
  The comment-to-DM engine for attracting agents: the escalating ask ladder (Follow → Comment → DM →
  Resource → Conversation → Call), the keyword every Reel carries, and the DM copy bank the member pastes
  into their own ManyChat (PARTNER, GUIDE, SCALE, GROWTH, the story reply, the DM qualifier). Every message
  selfless and useful, never a pitch, never compensation. Hands a real conversation to the Conversion
  plugin's cv-dm-flow when installed; otherwise logs it to the Brain in the locked stage vocabulary and adds
  the agent to the Top-50. Trigger on: "keyword for this reel", "comment to DM for agents", "my DM bank", "ManyChat
  copy for my organization", "what's the ask on this reel", "CTA ladder", "keyword sheet", "an agent
  commented my keyword", "an agent DMed me from a reel", "write my DM replies", or any request to turn
  comments on attraction content into conversations.
---

# Comment to DM — the ask ladder and the DM bank

Short-form is not about views. The path is Awareness → Recognition → Familiarity → Trust → Curiosity →
Conversation, and the asks climb the same way: Follow → Comment → DM → Resource → Conversation → Call.
One keyword rides on every Reel so a comment becomes a message and a message becomes a human conversation.
Nothing on this ladder pitches. The brokerage, the model, and compensation are answered on a private call,
never in a DM (`02-prospect-targeting/19`: say as little as you have to in text; the model is explained on a private call).

**Apply** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md`.
Every DM template here is **public-facing** (an agent outside the organization reads it), so the compliance
gate applies before any of it is delivered.

## Three jobs (detect from the message)
- **A · THE KEYWORD FOR THIS REEL** — "what's the ask on this reel", "keyword for this reel": pick the rung and
  the keyword for one post (the member's primary keyword is set once in `sf-setup`; this picks the rung and any
  per-Reel variant).
- **B · THE KEYWORD SHEET + DM BANK** — "my DM bank", "ManyChat copy": build the whole set once; refresh it
  when the offer or the free resource changes.
- **C · A CONVERSATION STARTED** — "an agent commented PARTNER", "she DMed me from the reel": write the human
  reply, qualify, and hand off or log.

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first (pull via **attraction-brain-sync** if the local copy is empty).
Then only what the job needs:
- `identity/publishing.md` — the `Keyword:` line (the one word `sf-setup` chose; the default on every Reel),
  `What it opens:`, and `ManyChat:` (`connected` → the sequences run; otherwise the member replies by hand)
- `identity/avatars.md` — who the keyword is for and their pains (the qualifier questions mirror them)
- `memory/magnets.md` → `## Current magnet` (Week 6; skip if it doesn't exist) — the live guide the GUIDE keyword
  delivers, read before `offer.md`
- `identity/offer.md` — the free resource(s) the GUIDE keyword delivers; the one-line promise. `Status:
  seeds` → every ask points to the call and the sheet marks where the guide slots in when Week 2's offer is
  finished (never ask for it early).
- `identity/positioning.md` + `identity/journey.md` (the `## Why join me` block) — how the member talks
  about partnering, in their words
- `identity/voice.md` + `identity/voice-samples.md` — every DM sounds like them, not like software
- `identity/operations.md` — the booking link and the call cadence
- `identity/compliance.md` — its first line, `Status:` — the gate (Step 4)
- `memory/top-50.md` + `memory/conversations.md` — before replying to a named agent, check whether they are
  already in a conversation (never restart one that exists)
- `memory/objections.md` — the answers that worked, for a qualifier reply that hits a known objection

## Step 2 — The ladder (every Reel sits on exactly one rung)

| Rung | The ask, spoken and in the caption | What it earns | Sequence variant (once ManyChat runs) |
|---|---|---|---|
| **Follow** | "follow for more of this" | reach and recognition | none |
| **Comment** | "comment [KEYWORD] and I'll send it" | a signal, a DM opens | GUIDE · GROWTH · SCALE |
| **DM** | "DM me [KEYWORD]" | a private channel | PARTNER |
| **Resource** | the guide, the checklist, the training | trust, a reason to come back | GUIDE |
| **Conversation** | one human question about their situation | the real relationship | all |
| **Call** | "if it makes sense, let's talk; here's my calendar" | the partner call | PARTNER |

**The keyword rule, one sentence:** The member has ONE primary keyword, chosen once in `sf-setup` (the
`Keyword:` line in `identity/publishing.md`); GUIDE · GROWTH · SCALE · PARTNER are the four sequence names from
Mike's ManyChat templates — per-Reel variants that default to the primary keyword's flow until the member runs
those templates in their own ManyChat. (`mike-frameworks.md` §8.) If the member renames their primary keyword
here, update the `Keyword:` line in `publishing.md` (the one line this skill writes there) and push.

**The rule of one:** one Reel, one keyword, one rung. The keyword is said on camera at the end, written in
the caption's last line, and pinned as the first comment. Authority Reels carry the keyword on the Comment or
Resource rung (variant GUIDE, GROWTH, or SCALE); Story and Proof Reels carry it on the DM rung (variant PARTNER)
or a soft "DM me if this is you"; Personality Reels carry nothing but "follow." **The direct call-rung** ("book a
call" as a post's CTA) appears **at most once a month** in the calendar; every other post earns it (an OS rule,
not a Week 3 lesson — `mike-frameworks.md` §8: the call comes after a conversation).

## Step 3 — The keyword sheet and the DM bank (Job B; Job A picks one row)
**The four sequence variants (each defaults to the primary keyword's flow until the ManyChat templates run; rename
to the member's words if they prefer):**
- **GUIDE** — "send me the free [guide name]." Delivers the live guide from `memory/magnets.md → ## Current magnet`
  first (Week 6, the Lead Magnet plugin's file) and the resource in `identity/offer.md` second.
- **GROWTH** — for the avatar who is stuck or newer: delivers the training, tip, or template the Reel
  promised, then one question about where they are.
- **SCALE** — for the producer or team leader avatar: delivers the systems piece the Reel promised, then one
  question about what they are building.
- **PARTNER** — "how do I partner with you / get access to all of it." The only keyword that moves to the
  call, and only after one human exchange.
- **Story reply** — the reply to a story poll, question box, or "ask me anything" (`07-instagram/89`): thank,
  answer in one line, ask one back.
- **DM qualifier** — three questions, asked one at a time, never as a form: where are you now (production
  and brokerage type, in their words) · what are you working toward this year · what is in the way. These
  mirror the five pains; the answers are what gets logged.

**Write six messages for the primary keyword first, then six for each variant** (until the ManyChat templates
run, every variant answers with the primary keyword's six), in the member's voice, each under 60 words:
1. **Auto-reply** (the ManyChat one): acknowledge the comment, deliver the thing or the link, no questions.
2. **The human follow-up** (sent by the member, same day): one real observation about *their* content or
   comment, one question about their situation. No link, no pitch.
3. **The qualifier** (the three questions above, as three short messages).
4. **The bridge to the resource** (when the answer shows a pain the member solves): "I made something on
   exactly that; want it?" then the resource.
5. **The invite to a call** (only after they ask about partnering, or after the qualifier shows fit and
   readiness): "happy to walk you through how I help agents with that; grab fifteen minutes here: [link]."
   Never "let's hop on a Zoom" as the first message.
6. **The graceful no** (not a fit or not now): a real thank-you, one useful thing, the door left open.
   "Parked" is fit and timing, never disrespect.

**The NEVER list (every message):** no pitch · no compensation, rev share, splits, caps, or fees · no
brokerage-to-brokerage comparison and never a negative word about another brokerage or person
(`03-model-positioning/13`) · no walls of text · no corporate recruiting language ("opportunity," "join my
team") · no fake personalization (if you have not read their profile, do not pretend you have) · no forced
Zoom · no income promises; the model, the money, and the paperwork are "a call conversation."

**The ManyChat hand-over (bring-your-own account):** the member imports Mike's sequence templates from the
cohort's bonus asset into their own ManyChat and pastes this copy in. Deliver the sheet in the template's shape
so it pastes clean: keyword · trigger (comment / DM / story reply) · message 1 · button text · message 2 · the
tag to apply · the human follow-up (sent manually, never automated). This skill writes copy; it never connects
to, configures, or sends through ManyChat.

## Step 4 — Compliance (three-state, before anything is delivered)
Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`).
`unset` → **stop**: *"these DM templates go to agents outside your organization, so I need your compliance
basics first; say 'set up my attraction compliance' and it takes three minutes."* Deliver nothing public. `set`
→ apply every rule and remind once per session. `confirmed` → apply. Append the compliance stamp (house rules
#4 — built from `identity/compliance.md`) only where a template names the brokerage; the income disclaimer never
appears because no template mentions income. "If empty, proceed" is banned.

## Step 5 — A conversation started (Job C): reply, qualify, hand off or log
1. Check `memory/top-50.md` and `memory/conversations.md` for the agent's name first.
2. Write the human reply (message 2 above) in the member's voice; if they already answered a qualifier
   question, write the next one, not the first one again.
3. **When it is real** (they answered the qualifier, or asked how to partner, or asked for the call):
   - **If the Conversion plugin is installed** → hand to **`cv-dm-flow`** by name with: the agent's name and
     handle, which Reel and keyword started it, the resource promised, the thread so far, the pains they
     named, and the rung they are on. `cv-dm-flow` owns the conversation from here.
   - **If it is not installed yet** → log one row to `memory/conversations.md` in the locked shape (Date ·
     Agent · Type · Channel = DM · what they said, short, their words · objection heard · pain · next step ·
     Stage after = `Conversation`), through **`attraction-capture`** when it is present (it is the interim
     owner of that ledger), otherwise appended directly in that exact shape; and add or update the agent in
     the Top-50 through **`attraction-top-50`** (Source = `reel: [title]`, Stage = `Conversation`). Stage
     vocabulary is locked: Identified → Conversation → Call booked → Call held → 3-way → Joined → Onboarded →
     Active. Then push via **attraction-brain-sync**; if the push fails, say it is not saved, retry once, stop.
4. Never send anything. The member sends every DM themselves; this writes the words.

## Step 6 — Save
Deliver in chat. Offer to save the sheet and bank per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`:
render to `.docx` (`shared/render_doc.py`) → `03 · Content/Short-Form/[YYYY-MM · Month]/`, named
`[YYYY-MM-DD] · Keyword Sheet + DM Bank`. Close with the one next step: *"pick the keyword for this week's
Reels and say the word on camera; I'll write the human replies as they come in."*

## Quality checklist
- [ ] Brain loaded; avatars, offer, voice, booking link taken from it, nothing re-asked; offer seeds
      respected
- [ ] One keyword per Reel, matched to the rung and the pillar; the direct call-rung at most once a month
- [ ] Six messages for the primary keyword and for each variant, under 60 words, in the member's voice; the NEVER
      list kept on every one
- [ ] Compliance read first; `unset` blocked delivery; no compensation anywhere
- [ ] Conversation handed to `cv-dm-flow` by name, or logged in the locked shape and added to the Top-50,
      then pushed; nothing sent
