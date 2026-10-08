---
name: sf-stories
description: >
  Daily Instagram stories for agent attraction — the four-category rotation (behind the scenes of leading ·
  agent wins · personal · opportunity), one to five stories a day, never a day without. Writes today's story
  set from the member's Brain: each story's text overlay, the sticker (poll, question box, quiz, link), and a
  story-reply CTA that hands to the ManyChat story-reply flow or a by-hand reply. Keeps a Story Prompt Deck for
  days with nothing to say; personal stories on passions and hobbies connect with agents who share them; agent
  wins are tagged so they reshare. Text only; never posts. Trigger on: "today's stories", "my story rotation",
  "stories for agents", "attraction stories", "story prompts", "what should I post on my stories",
  "behind-the-scenes story", "story ideas for this week", "write my stories", "a story about my agent's win".
---

# Daily Stories — the connection layer

Reels are width; stories are depth (`07-instagram/89`). This is where an agent decides they'd have a coffee with
the member. One to five stories a day, a mix of leading, wins, the person, and the opportunity — unpolished, in
the moment, with at least one thing to tap. "Do not go a day without posting stories."

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`). **Doctrine:**
`${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §9c (stories), §9d (daily), §8 (the ladder), §11 — lazy-load
at Phase 2. Stories are the lowest-friction win in the whole plugin: when a member says "I don't know what to
post," this is the answer.

**Text only.** The member films or photographs the moment on their phone; this skill writes the overlay text,
names the sticker, and writes the reply CTA. Never an image.

---

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first, then:
- `identity/content-pillars.md` — the Proof and Personality sections (the recurring behind-the-scenes, the
  passions and routines they're willing to share, what's off-limits); missing → `sf-setup` in one warm line
- `identity/publishing.md` — the keyword, ManyChat state (`connected` → story-reply flow; otherwise by hand),
  the highlights list
- `identity/avatars.md` — who's watching; what a quick win looks like for them
- `identity/proof.md` — agent wins with consent (a win without consent is told as "one of my agents", never named)
- `identity/story-bank.md` — a short story beat for a "food for thought" story; stamp Used-where if used
- `identity/voice.md` · `identity/voice-samples.md` — stories are typed, short: their written phrasing
- `identity/offer.md` — what they give today (the opportunity category); `seeds` → "what I'm building" sneak
  peeks and "book a call", never a demanded guide
- `identity/journey.md` — the WHY line (an end-of-day reflection story)
- `identity/compliance.md` — three-state (stories are public)
- `memory/content-log.md` — which categories ran this week (rows with Format `story`)
- `memory/ideas.md` (tag `story`) — the member's own moments, first; `memory/debriefs.md` is the Debrief's
  file — don't read it here; the member's "what happened today" comes from them in one line
- `memory/intel.md` — a verified item for an "opportunity" take (facts only)
- `memory/content-performance.md` — which stories got replies (from `sf-analytics`); skip if it doesn't exist yet

**Read the Brain; never re-ask.** `~/attraction-brain/` missing → pull with `attraction-brain-sync`.

## Step 2 — Read the reference file
`references/story-prompt-deck.md` — the four categories, the prompts, the stickers, the reply CTAs.

---

## Phase 1 — What happened today? (one question, optional)
Stories are about the day. One light question, only if they didn't already say:
> "What's on today — a call, a win, a workout, an appointment, nothing special? One line and I'll build your
> stories around it. Or say 'just pick' and I'll use the deck. Your turn."
"Just pick" / no answer → build from the deck and the Brain (house rules #8). Never more than this one question.

## Phase 2 — Build today's set (3 by default; 1–5)
**Read `references/story-prompt-deck.md`.** Rotate the four categories — fill the ones that didn't run this
week first (from the log):
1. **Behind the scenes of leading** — the weekly call (a screenshot with the one takeaway), what they're learning
   or investing in, the routine, a meeting with an agent, planning an event, the content they're recording.
2. **Agent wins** — a milestone, a first deal, a cap, a shout-out — tagged so the agent reshares; a testimonial
   line (consent); the call with "[N] agents on" (never an invented number).
3. **Personal** — family, fitness, travel, the dog, a hobby, a down day and how they're handling it, food for
   thought. "Relatable leaders are attractive leaders." Passions and hobbies pull in agents who share them.
4. **Opportunity** — a quick win agents can use today (a tip, a script line, a screenshot of a tool or template
   they're building), a poll or quiz on the agent's business, an AMA box, a sneak peek of what's coming, the
   YouTube thumbnail with the link (Week 4).
For EACH story, use these exact labels:
- **STORY [n] — [category]** · **What to capture** (one line: the photo/clip to take) · **Text overlay** (≤15
  words, in their voice) · **Sticker** (poll with the two options · question box prompt · quiz · link · mention
  @agent) · **Reply CTA** (one line — the story-reply flow or a by-hand reply, see below) · **Add to highlight**
  (About · Agent wins · Culture · Free value · Partner with me · [passion]) — or "no".
Rules: at least one interactive sticker per day; no production polish; the wins tag the agent; personal means
real, not flaunted (`05-big-picture/36`); the opportunity story is value, never a pitch; a model, a split, or a
number never appears in a story.

### Story-reply CTAs (how a story becomes a conversation)
The story-reply flow is the DM rung of the ladder. The CTA is a question the viewer answers by replying:
- *"Reply 'CALL' if you want the recording"* · *"Reply with the number of deals you're at — I'll tell you the one
  thing I'd change"* · *"Reply 'YES' and I'll send the template"* · *"Vote, then reply and tell me why."*
If `publishing.md` says `ManyChat: connected` → the reply word triggers the **story-reply** sequence (Mike's
bonus asset, imported into the member's account); write the CTA around that word. Otherwise → the member replies
by hand within the day (say so once), and from Week 5 the Daily Follow-Up Queue surfaces replies. A reply that
turns into a real conversation is handed to `sf-comment-to-dm` — the one short-form skill that logs a conversation
row (through `attraction-capture` when present) until the Conversion and Admin plugins exist; this skill never
logs one.

## Phase 3 — Compliance pass (third law, three-state)
`identity/compliance.md`: `unset` → the set stays in chat as a private draft with the plain line; `set` → apply +
remind once; `confirmed` → apply. Apply to stories: a named agent only with consent (`proof.md`); no screenshot of
a call that shows names without consent — say "blur or crop names"; no compensation, no earnings, no negative
word about any brokerage or person; brokerage name/license where the file says it must appear; any real-estate
example fair-housing safe.

## Phase 4 — Deliver
A clean copy-paste set, in order, with a one-line plan: *"Morning: the call screenshot. Lunch: the poll. Evening:
the dog. Thirty seconds each."* If the member has the content board (house rules #10), one card for the day's set
(Format `Graphic`, Context `• Pillar: Proof / Personality`). Never schedule stories through a tool — they're
posted live from the phone; say so if asked.

## Phase 5 — Save + log + push
1. **Save** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` only when the member asks for a week of sets
   or a deck doc — a daily set lives in chat. A saved set: rendered `.docx` to
   `03 · Content/Short-Form/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Stories · [Day / theme]`.
2. **Log it:** one row per day in `~/attraction-brain/memory/content-log.md`, locked shape:
   `| [date] | Instagram | story | Proof · Personality (the categories run) | [story set] [the day's theme] | [avatar] | [story hook or —] | [reply word · story reply] | Scripted | |`
3. **Stamp** a story-bank Used-where if a bank story was used; flip an `ideas.md` row to `used`.
4. **Push** (write → push → verify). Then: *"Logged today's stories — tomorrow I'll rotate to the categories you
   haven't hit this week."*

---

## Quality checklist
- [ ] Brain read; one optional question at most; nothing re-asked
- [ ] 1–5 stories, categories rotated from the log; at least one interactive sticker
- [ ] Each: what to capture · overlay ≤15 words in their voice · sticker · reply CTA · highlight
- [ ] Wins tag the agent, consent respected; personal is real, never flaunted; opportunity is value, never a pitch
- [ ] Reply CTA matches the ManyChat state; a real conversation hands to `sf-comment-to-dm`
- [ ] No compensation, no earnings, no negative word about any brokerage or person; compliance three-state applied
- [ ] Logged in the locked shape, pushed; text only
