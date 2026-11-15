---
name: sf-stories
description: >
  Week 4 daily Instagram stories for agent attraction: the four-category rotation, one to five a day,
  never a day without. Writes today's set from the member's Brain: each story's overlay, sticker, and
  reply ask (Reply GUIDE for the guide, or a plain reply) for the ManyChat story-reply flow or a by-hand
  reply; keeps a Story Prompt Deck for empty days. On demand, writes the words for a welcome, agent-win
  or team-milestone post in the shape of the member's team templates, with the consent gate. Owns the
  optional Daily Stories workflow (off by default; only with the member's yes). Text only; never posts.
  Trigger on: "today's stories", "my story rotation", "stories for agents", "attraction stories", "story
  prompts", "what should I post on my stories", "story ideas for this week", "write my stories", "write
  a win post for [Name]", "welcome post for my new partner", "a story about my agent's win", "team
  milestone post", "turn on my daily stories", "stop my daily stories".
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

**Week 4 rules that bind every story** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **Two keywords, never more.** `GUIDE` delivers the guide (`memory/magnets.md → ## Current magnet`); the offer's
  `Comment keyword:` (`identity/offer.md`) is the invitation. Both sit on `publishing.md`'s `Keyword:` line. A story's
  reply ask is either *"Reply GUIDE and I'll send it."* (the guide) or a plain reply — *"Reply and I'll send you the
  link."* (the call), *"Reply with your answer."* — never a third word (CALL, LIST, YES, WIN, SCRIPT are retired).
- **The call ask follows the law:** the person · their help · free · to run the method — never the brokerage, never
  compensation. Join register (`offer.md → Join-gated package allowed: yes` or `unknown`): *"Want my help running this,
  free? Reply and I'll send you the link."* Open register (`no`): *"I'll walk you through it, free, no strings."* The
  story lines are the kit's CALLS TO ACTION table (chapter 7 of the newest `exports/week3-kit-*.txt`), verbatim.
- **Scalable by design.** No story promises the member's time per partner — no in-person days beside the member, no
  chat group, no one-to-one calls, no "call me any time". Behind the scenes of leading shows recorded lessons being
  made, templates, the community, and the weekly group call ONLY when `identity/operations.md` shows the member already
  runs one — never an invented call, never "three partner calls today". The member's OWN batch-filming day is fine.
- **The guide is the resource** every opportunity story points at; a teaching story gives one step of
  `offer.md → ## The framework`.
- **Member-facing words:** plain, one question at a time, never a skill id or a file path; the graphics for a win or
  welcome post are made in the member's Claude Design from their Week 3 masters — this skill writes the words.

---

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first, then:
- `identity/content-pillars.md` — the Proof and Personality sections (the recurring behind-the-scenes, the
  passions and routines they're willing to share, what's off-limits); written by the Game Plan inside setup —
  missing → "say 'set up my attraction short-form'" in one warm line
- `memory/content-calendar.md` — today's planned post, if any (a "recording day" story proposes itself)
- `identity/publishing.md` — the two keywords (`Keyword: GUIDE · [the offer's word]`), the ManyChat state (`set up
  YYYY-MM-DD` → the story-reply flow keys on GUIDE and the offer's word; `not yet — set it up this week` → by hand from
  the DM bank until it's live; never asked), the highlights list, `Content board:`
- `identity/avatars.md` — who's watching; what a quick win looks like for them
- `identity/proof.md` — agent wins with consent — the **Agents helped** rows (name · what you did · what happened ·
  dated) and their consent column (a win without consent is told as "one of my agents", never named); **Organization**
  (size, milestones — the only count a milestone post may carry)
- `memory/organization.md` (name · join date · status `Joined`) and `memory/pipeline.md` (stage `Joined` /
  `Onboarded`) — new partners, for the welcome post (the on-demand mode below)
- `identity/story-bank.md` — a short story moment for a "food for thought" story; stamp Used-where if used
- `identity/voice.md` · `identity/voice-samples.md` — stories are typed, short: their written phrasing
- `identity/offer.md` — `## The framework` (a teaching story = one step), the `Comment keyword:` line, `Join-gated
  package allowed:` (the register of the call line), `## The program` (the program name a win or welcome post carries)
- `memory/magnets.md → ## Current magnet` — the guide (GUIDE): the opportunity category's resource; no live guide yet →
  "what I'm building" sneak peeks and the call line, never a demanded guide
- the newest `exports/week3-kit-*.txt` — chapter 7's CALLS TO ACTION table (the two story lines) and the stamp
- `identity/journey.md` — the WHY line (an end-of-day reflection story)
- `identity/operations.md` — the `Weekly model call:` line: ONLY when it names a day does the behind-the-scenes story
  of that call propose itself on that day (the screenshot, names blurred); an empty line → no call story, ever
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
Stories are about the day. If `operations.md` puts the member's weekly group call on today, lead with that story
and skip the question. Otherwise one light question, only if they didn't already say:
> "What's on today — a call, a win, a workout, an appointment, nothing special? One line and I'll build your
> stories around it. Or say 'just pick' and I'll use the deck. Your turn."
"Just pick" / no answer → build from the deck and the Brain (house rules #8). Never more than this one question.

## Phase 2 — Build today's set (3 by default; 1–5)
**Read `references/story-prompt-deck.md`.** Rotate the four categories — fill the ones that didn't run this
week first (from the log):
1. **Behind the scenes of leading** — the weekly group call when the member runs one (a screenshot with the one
   takeaway), the lesson they're recording for partners, the template they're building, what they're learning or
   investing in, the routine, planning an event, the content they're recording on their batch day.
2. **Agent wins** — a milestone, a first deal, a shout-out — tagged so the agent reshares; a testimonial
   line (consent); the call with "[N] agents on" (never an invented number). "A cap" is named as the milestone only
   when the `Rev-share marketing and income-claim policy` in `identity/compliance.md` allows it; otherwise the
   milestone stands without it ("a big month", "first deal").
3. **Personal** — family, fitness, travel, the dog, a hobby, a down day and how they're handling it, food for
   thought. "Relatable leaders are attractive leaders." Passions and hobbies pull in agents who share them.
4. **Opportunity** — a quick win agents can use today (one step of the method, a script line, a screenshot of a
   template they're building), the guide (*"Reply GUIDE and I'll send it"*), a poll or quiz on the agent's business,
   an AMA box, a sneak peek of what's coming, the YouTube thumbnail with the link (a later week, when their YouTube
   system runs).
For EACH story, use these exact labels:
- **STORY [n] — [category]** · **What to capture** (one line: the photo/clip to take) · **Text overlay** (≤15
  words, in their voice) · **Sticker** (poll with the two options · question box prompt · quiz · link · mention
  @agent) · **Reply CTA** (one line — the story-reply flow or a by-hand reply, see below) · **Add to highlight**
  (About · Agent wins · Culture · Free value · Partner with me — at the open register "Free help" · [passion]) — or "no".
Rules: at least one interactive sticker per day; no production polish; the wins tag the agent; personal means
real, not flaunted (`05-big-picture/36`); the opportunity story is value, never a pitch; a model, a split, or a
number never appears in a story; nothing promises the member's time per partner.

### Story-reply CTAs (how a story becomes a conversation)
The story-reply flow is the DM rung of the ladder. Two words only: **GUIDE** when the story hands out the guide
(*"Reply GUIDE and I'll send it."*); a plain reply for everything else — the call (*"Want my help running this, free?
Reply and I'll send you the link."*), a question (*"Reply with the number of deals you're at — I'll tell you the one
thing I'd change"*), a vote (*"Vote, then reply and tell me why."*). Never a third word. The CTA is a question the
viewer answers by replying. If `publishing.md` says `ManyChat: set up` → GUIDE triggers the **story-reply**
sequence (Mike's bonus asset, imported into the member's own account — never connected to Claude) and the offer's
word opens the invitation; write the CTA around those. `not yet — set it up this week` → the member replies by hand
from the DM bank within the day (say so once, with *"your build sheet has the steps — 'my ManyChat build sheet'"*);
once the AI Admin is installed (a later week) its follow-up queue surfaces replies. A reply that turns into a real conversation is
handed to `sf-comment-to-dm` — the one short-form skill that logs a conversation row (through `attraction-capture`
when present) until the Conversion and Admin plugins exist; this skill never logs one.

## Phase 3 — Compliance pass (third law, three-state)
the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`): `unset`
→ the set stays in chat as a private draft with the plain line; `set` → apply + remind once; `confirmed` →
apply. Apply to stories: a named agent only with consent (`proof.md`); no screenshot of a call that shows names
without consent — say "blur or crop names"; no compensation, no earnings, no negative word about any brokerage
or person; brokerage name/license where the file says it must appear; any real-estate example fair-housing safe.

## Phase 4 — Deliver
A clean copy-paste set, in order, with a one-line plan: *"Morning: the call screenshot. Lunch: the poll.
Evening: the dog. Thirty seconds each."* If the member has the content board (house rules #10), one card for the
day's set (Format `Graphic`; Pillar = the set's lead pillar, one OS name, never two — the log carries one row per
pillar; Context per `sf-board`). Never schedule stories through a tool — they're posted live from the phone; say
so if asked.

## On demand — the win, welcome and team-milestone posts (the words; the Week 3 team templates' shape)
"Write a win post for [Name]" · "welcome post for my new partner" · "a story about my agent's win" · "team milestone
post" → this mode. **Not a scheduled task of its own** (the owner, 2026-11-14): the Monday Week Plan scans the Brain
each week for a new partner or a consented win since its last run and calls this mode for the words; the member asks
any day. This skill writes the words; the graphic is the member's, in Claude Design, from the Week 3 masters.
1. **Find the moment in the Brain** — never invent one: a new partner in `memory/organization.md` (status `Joined`,
   the join date) or `memory/pipeline.md` (stage `Joined` / `Onboarded`); a win in `identity/proof.md → Agents helped`
   (what happened, dated) with its consent column; a milestone count in `identity/proof.md → Organization` (the only
   figure a milestone post may carry — never a projection, never a ranking). Nothing on file → one warm line: *"tell me
   the win in one line and say whether [First] has said yes to being posted — say 'attraction win' and I'll remember
   it"* (the Brain's capture phrase); never write the post from memory.
2. **The consent gate.** An agent is named or pictured only with their written OK on file (the consent column in
   `proof.md`; the Testimonial consent line in `identity/compliance.md`). No OK → the draft is still written but marked
   **"needs [First]'s OK"** at the top, with the one-line ask the member sends first: *"Hey [First] — may I share your
   [win] on my page this week, with your photo? A yes here is all I need."* The draft holds until the member says
   "[First] said yes". A production figure only as the agent stated it and consent covers it; a "cap" only where the
   compliance file's rev-share marketing policy allows it; income, splits, revenue share — never.
3. **Write the three pieces, in the shape of the member's Week 3 team templates** (the fixed words come from the kit:
   the program name from chapter 1 / `offer.md → ## The program`; the stamp from the kit's closing line; the status
   word from the win — WELCOME · FIRST DEAL · MILESTONE · SHOWED UP · the count):
   - **Welcome a new partner** — the status word WELCOME · the first name · the member's one line about them (who they
     are and why the member is glad — never "joined [brokerage]" as the point; at the join register "joined [the program
     name]" is allowed, at the open register the first name and the line carry it) · the program name · the stamp.
   - **Agent win** — the status word · the first name · the result exactly as the agent stated it and consented to ·
     the program name · the stamp.
   - **Team milestone** — the true count from `proof.md → Organization` (`(demo)` kept on demo builds) · one sentence
     on what it took · the program name · the stamp. Never a ranking, never "best", never a figure the Brain does not
     hold.
   For each: **the slide copy** (the status word · the name · the one line — three lines, verbatim for the template's
   swaps; the headshot noted as "[First]'s photo — written OK on file" or "needs OK") · **the caption** (two to four
   lines in the member's voice, the agent tagged so they reshare, ending on the kit's call line — every proof piece
   carries the call: *"Want my help running this, free? [the booking line]"*, the law's shape, open register *"I'll
   walk you through it, free, no strings"*) · **the story line** (≤15 words, the mention sticker, *"Reply and I'll send
   you the link."*). No compensation, no negative word about any brokerage or person; the stamp on every public piece.
4. **The board card** (only when `publishing.md` carries a `Content board:` URL, per `${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`):
   Topic = the status word + the first name · Format `Graphic` · Pillar `Proof` · Status `Scripted` (`Ready to Film` is
   wrong for a graphic) · Context `• For: [the avatar]` · `• Rung: the call` · the full words in the page body · a fresh
   System ID. A held draft's Topic starts with "HELD —" until the OK arrives.
5. **Deliver + the one line about the graphic:** the three pieces in chat, then: *"The graphic is yours to make in your
   Claude Design: say 'my welcome post for [First]' (or 'win post for [First]', 'design my team posts') — your Week 3
   masters fill with these words; drop [First]'s photo in and tell it they've said yes."* Never render an image here.
6. **Log + push:** one row in `memory/content-log.md` (`| [date] | Instagram | graphic | Proof | [win post] [the status
   word · First] | [avatar] | — | the call · [the booking line] | Scripted | |`), the consent state in the Topic cell
   when held (`HELD — needs First's OK`); push via `attraction-brain-sync` at once (write → push → verify) — the Brain
   Board shows it. A win that is also proof for the member's own story: "say 'attraction win' so it's remembered".

## The scheduled workflow — Daily Stories (by phrase — one of the five extras; this skill owns it)
Three story ideas each morning as a draft — for the member who wants the day started for them. **Provisioned
only with the member's explicit yes, never silently.** Setup states it among the five extras in one sentence
("they're there if you want them — say the word any time") and never provisions it from that sentence alone. "Turn on
my daily stories" → read `config.md`'s `Daily Stories task:` line first (the `## Short-Form (Week 4)` block; an older
Brain's block may carry the previous week number in its heading — read it the same): a task id → it is on, say so;
`paused` → they stopped it, its phrase brings it back; `later` / no line / any other value → on the phrase, a statement, never an
offer or a question (the owner, 2026-11-14: told, not asked): *"Switching on your daily stories — every morning,
7:30 am; name another time any time."*
- **On the phrase** → `list_scheduled_tasks` first (adopt `attraction-sf-daily-stories` if it exists, never a twin), else
  `create_scheduled_task` with `taskId: attraction-sf-daily-stories`, every morning at their time (default
  7:30 am, in `config.md → Timezone`), the `prompt` set **verbatim** from `references/daily-stories-task-prompt.md`.
  Verify with `list_scheduled_tasks` (present, enabled, a `nextRunAt`) — never claim a schedule that did not save.
  Write `Daily Stories task: attraction-sf-daily-stories` and `Daily Stories time: [time]` to the `## Short-Form
  (Week 4)` block of `config.md`; push via `attraction-brain-sync`; confirm once: *"On. Say 'stop my daily stories'
  any time."*
- **Stop / pause** → `delete_scheduled_task` (or disable) on the saved id; write `paused`; push; one
  line. A demo Brain never gets a task.
- The scheduled run writes nothing to the Brain's files — it leaves the three ideas as its closing message; the
  member says "post these" in chat and this skill logs them (Phase 5). **Telling the member:** when the config block
  says `Email me: yes` the run sends ONE short email to the member's OWN address through their connected mail (never to
  anyone else) with the three overlays; otherwise the Cowork note alone. **Every run ends with a push** through
  `attraction-brain-sync`, so the Brain Board is current. Draft-only, always — nothing posts.

## Phase 5 — Save + log + push
1. **Save** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` only when the member asks for a week of sets
   or a deck doc — a daily set lives in chat. A saved set: rendered `.docx` to
   `03 · Content/Short-Form/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Stories · [Day / theme]`.
2. **Log it:** one row per pillar the set ran in `~/attraction-brain/memory/content-log.md` — the Pillar cell holds
   ONE value, never `Proof · Personality` in one cell (behind the scenes + agent wins → `Proof`; personal →
   `Personality`; opportunity → `Authority` for a tip, script, template, or poll on their business, `Proof` for a
   sneak peek of what's coming). Locked shape, one row each:
   `| [date] | Instagram | story | Proof | [story set] [the day's theme] | [avatar] | [story hook or —] | [reply word · story reply] | Scripted | |`
   `| [date] | Instagram | story | Personality | [story set] [the day's theme] | [avatar] | — | [reply word · story reply] | Scripted | |`
3. **Stamp** a story-bank Used-where if a bank story was used; flip an `ideas.md` row to `used`.
4. **Push** (write → push → verify) through `attraction-brain-sync` the moment the rows are written — every write
   pushes at once; the push re-renders the member's Brain Board. Then: *"Logged today's stories — tomorrow I'll rotate
   to the categories you haven't hit this week."*

---

## Quality checklist
- [ ] Brain read; one optional question at most; nothing re-asked
- [ ] 1–5 stories, categories rotated from the log; at least one interactive sticker
- [ ] Each: what to capture · overlay ≤15 words in their voice · sticker · reply CTA · highlight
- [ ] Wins tag the agent, consent respected; personal is real, never flaunted; opportunity is value, never a pitch
- [ ] Reply CTA is "Reply GUIDE" or a plain reply — never a third word; the call line in the law's shape; matches the
      ManyChat state; a real conversation hands to `sf-comment-to-dm`
- [ ] Scalable: no story promises the member's time per partner; the weekly call appears only when `operations.md`
      says the member runs one
- [ ] A win, welcome or milestone post: the moment found in the Brain (never invented), the consent gate applied (held
      drafts marked "needs [First]'s OK" with the ask), the team templates' shape, the program name and the stamp, the
      call line, the board card when the board exists, the one line to Claude Design, logged and pushed
- [ ] No compensation, no earnings, no negative word about any brokerage or person; compliance three-state applied;
      "a cap" as a milestone only where the rev-share marketing policy allows
- [ ] Logged one row per pillar in the locked shape (one value per Pillar cell), pushed; text only
- [ ] The Daily Stories workflow provisioned by the member's phrase (a statement, never an offer), adopted not
      twinned, verified; the two config lines written to `## Short-Form (Week 4)` and pushed; by phrase only;
      draft-only; the run emails the member only when `Email me: yes`, and ends with a push
