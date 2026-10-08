---
name: sf-setup
description: >
  One-time onboarding for the Agent Attraction Short-Form System — the Week 3 layer on top of the member's
  Agent Attraction Brain. Reads the Brain (who they attract, their journey and stories, positioning, proof,
  voice) and never re-asks it. Writes their five content pillars (Authority · Perspective · Story · Proof ·
  Personality) mapped to the agents they attract; writes their bios for Instagram, Facebook, TikTok and
  LinkedIn with the recruiter CTA (the five questions every profile must answer); saves the one keyword that
  carries every Reel; then, last and optional, offers to connect a posting tool (Metricool / GoHighLevel /
  manual). A second call resumes or updates one part — it never re-runs. Trigger on: "set up my attraction
  short-form", "set up short-form for agent attraction", "launch my attraction short-form", "open my attraction
  short-form", "build my content pillars", "write my attraction bios", "my recruiter bio", "set my keyword",
  "update my pillars", "update my bios", "connect my posting tool", or any first run of the attraction
  short-form system.
---

# Short-Form Attraction Engine — Setup

A warm, short onboarding that turns on the member's short-form engine as a **layer on top of their Agent
Attraction Brain**. By the end they hold three things that didn't exist before: **their pillars, their bios,
their keyword** — and they've made their first real piece. One sitting, about fifteen minutes.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — above all #1: plain and warm, never
technical, 2–4 related questions per stop, "your turn" on every stop, breadcrumbs. This is the member's first
impression of the plugin.

## ⭐ THE RULES THAT SHAPE THIS SKILL
- **One Brain, never two.** Who they attract, their story, their positioning, their proof, their voice already
  live in the Brain. This skill reads them and never re-asks. If you catch yourself about to ask — stop and read.
- **Value first, plumbing last.** Pillars → bios → keyword → a first piece — before any tool is mentioned.
  Connecting a posting tool is a separate, optional, last step (Step 7). Manual is the default and always valid.
- **Never hand off before saving.** Every section is written and pushed the moment it's confirmed (write → push
  → verify). A member who leaves mid-way loses nothing.
- **Not re-run on a second call.** Step 0 routes: resume the unfinished part, or update the one part they named.
- **Public needs compliance.** Pillars and the keyword are private; bios are public → the three-state gate before
  Step 4. `unset` → do the private parts, stop before the bios with one plain line.

---

## Step 0 — Route (silent — the member never sees step numbers)
1. If `~/attraction-brain/` is missing, **pull it first** with `attraction-brain-sync` (a fresh session starts
   empty; the Brain lives in their workspace; located by ID, never by name). A tool error is never "no Brain".
   Only if the cloud genuinely has none: one warm line — *"Let's build your Attraction Brain first — say 'set up
   my attraction brain'. The more it knows you, the more your Reels sound like you and not like everyone else."*
2. Read `~/attraction-brain/brain.md`. Then read `identity/publishing.md` **if it exists** and its
   `Short-form setup:` line:
   - **missing / `not started`** → full run (Steps 1–7).
   - **`pillars done` / `bios done` / `keyword done`** → one line of where they left off, then resume at the next
     part. *"Welcome back — your pillars are saved. Next: your bios. Four quick questions."*
   - **`complete`** → the **READY BRIEF** (one line that it's loaded, naming 3–4 things you know about them —
     who they attract, their known-for, their keyword, this week's mix; at most ONE upgrade suggestion; the next
     thing on the calendar; *"What do you want to make?"*). Then route a named part — "update my pillars" →
     Step 3 only · "update my bios" → Step 4 only · "set / change my keyword" → Step 5 only · "connect my posting
     tool" → Step 7 only — or hand to `sf-talkinghead` / `sf-stories`. **Never the interview again.**
3. Read `identity/compliance.md` once now (its Status decides whether Step 4 runs today).

## Step 1 — Welcome (set the tone; what they'll leave with)
> "Let's switch on your short-form engine. I already know you from your Brain, so this is quick. You'll leave
> with three things: your five content pillars (so you always know what to post), your bios rewritten for the
> agents you attract, and the one keyword every Reel will carry. Then we'll make your first piece. About fifteen
> minutes. Your turn — ready?"

## Step 2 — Read the Brain and reflect it back (never re-ask)
Read `identity/profile.md`, `identity/journey.md` (including the `## Why join me` block, if written),
`identity/strategy.md`, `identity/avatars.md`, `identity/positioning.md`, `identity/offer.md` (respect its
Status — at `seeds` the Partner Offer is Week 2; never call the seeds "the offer"), `identity/proof.md`,
`identity/story-bank.md`, `identity/voice.md`, `identity/voice-samples.md`, `identity/brand-visual.md` (the
"leader brand vs selling brand" line), `memory/ideas.md` (tags `shortform`, `story`), `memory/content-log.md`
(empty is normal), `memory/objections.md`.
Reflect back in one breath so it's clear nothing will be re-asked:
> "Here's what I've got: you're [name], building [what they're building] at [brokerage] in [market]; you attract
> [primary avatar, one line]; you're known for [known-for]; your voice is [one line]. I won't ask you any of
> that again."

## Step 3 — The five pillars (propose, they react; writes `identity/content-pillars.md`)
**Lazy-load `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §5–§6 now.** Build the proposal from the Brain —
develop, never transcribe:
- **Authority — what I teach.** The known-for and the "what worked / teach first" lines dissected into **8–12
  topic seeds**, each tied to one of the avatar's pains in their words ("cast a wide net around your niche").
- **Perspective — what I believe.** 3–5 takes the member holds (the "one thing they wish struggling agents
  understood", the avatar's "what they'd need to hear", objections heard) and 3 myths to bust — never about a
  named brokerage or person.
- **Story — where I've been.** The three journey beats, each with "who relates to this", plus the story-bank hooks
  tagged for a story Reel. Former brokerages never named.
- **Proof — what's happening in my world.** Agents already helped (only rows marked OK to use publicly; others as
  first name or initials), the recurring behind-the-scenes (the weekly call, training they give, events), the
  upline's proof labeled as the upline's. Zero proof → one honest line and "earn it by helping agents free".
- **Personality — who I am off the clock.** From the profile's "before real estate" line and the journey. If the
  Brain has nothing here, this is the **one stop of questions in this step (2–4, together):**
  > "Three quick ones so your personal side isn't a blank: (1) What do you do outside real estate that other
  > agents would relate to — sport, family, faith, a hobby? (2) One routine or discipline you keep? (3) Anything
  > that's off-limits to post? Your turn."
  If they hesitate: propose from the Brain and let them confirm in one word (`ask-once → default-if-unsure`).
Present the five as **one block** — pillar name, two-line summary, the first three topics — then:
> "That's your plan. Your turn — say 'good' or tell me what's off."
Then write `~/attraction-brain/identity/content-pillars.md` in the shape in
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md` (status, the one-line anchors, the five sections, the weekly
mix, an empty hooks bank). Create `identity/publishing.md` now with `Short-form setup: pillars done` and whatever
platforms/handles the Brain already knows. **Push both, verify.** Say: *"Saved — your pillars are in your Brain."*

## Step 4 — The bios (public → the gate first)
**The three-state check:** `confirmed` → go · `set` → go, remind once at the end to confirm with the brokerage ·
`unset` → *"Your pillars and keyword are private, so we're fine so far — but bios are public, so before I write
them I need your compliance basics. Say 'set up my compliance' (three minutes) and I'll pick the bios right back
up."* Then skip to Step 5 and leave `bios done` unset.

**Lazy-load `mike-frameworks.md` §9a.** Every bio answers **the five questions**: who you are · who you help ·
what you help them do · why they should listen · what to do next. Inputs are all in the Brain: the why-join-me
one-breath line (or the journey's turning point if Week 2 hasn't written it), the known-for, the primary avatar,
credibility from `proof.md` exactly as stated (none public → lead with who you help; **never invent an award or a
number**), the resource (from `offer.md`; at seeds → the free thing they already give today, or "book a call"),
handles and booking link from `profile.md`, brokerage name and license display per `compliance.md`.
One stop of questions **only if the Brain doesn't answer them** (2–4, together): which platforms they actually
post on and in what order · the link-in-bio tool they use (if any) · whether LinkedIn matters (yes by default when
an avatar is a team leader or broker-owner).
Write, in their voice:
- **Instagram** (≤150 characters): line 1 who + how you help · line 2 who it's for + one credibility point · line
  3 the ask — "comment/DM **[KEYWORD]**" or "free [resource] ↓". Plus the **link-in-bio order** (free resource
  first, then book a call / apply to partner — action text, never "website") and the **highlights** list (About ·
  Agent wins · Culture · Free value · Partner with me · one passion).
- **Facebook** (intro line + About paragraph, same five questions).
- **TikTok** (≤80 characters: who + for whom + the keyword).
- **LinkedIn** (headline ≤220 characters + an About of 4–5 short paragraphs written for team leaders and
  broker-owners: the problem they carry, what the member built, proof, the ask).
Compliance stamp as the file says (brokerage name / license where required). No compensation, no "#1" without a
source, no brokerage as the hook. If a Week 2 bios document already exists in `02 · Brand`, read it as data and
refresh it rather than starting over.
Deliver copy-paste blocks: *"Paste these in — or tell me what to change. Your turn."* On their yes: write them into
`identity/publishing.md → ## Bios (current — date)` with the five questions ticked, set `bios done`, **push,
verify**; save `Profiles & Bios — YYYY-MM-DD.docx` to `02 · Brand/` per
`${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`.

## Step 5 — The keyword (one word, chosen once)
**Lazy-load `mike-frameworks.md` §8.** Propose ONE word: tied to the resource or the invitation (e.g. **PARTNER**
when the ask is "get everything free — partner with me"; a resource word like **SCRIPTS** or **PLAN** when there
is a real free thing), one word, easy to say on camera and type in a comment, never a brokerage name, never a
word their followers already comment by habit. One line of why. Then the one question that matters:
> "Do you use ManyChat? Mike's sequences import into your own account — optional. Without it, the keyword still
> works: you reply by hand, and from Week 5 your follow-up queue surfaces every comment. Your turn."
Write `Keyword:` · `What it opens:` · `ManyChat:` (`connected YYYY-MM-DD` / `not yet — replying by hand` /
`declined`) to `identity/publishing.md`, set `keyword done`, **push, verify**. (Per-Reel keyword variants and the
DM copy bank come later from `sf-comment-to-dm` — say so in one line only if they ask.)

## Step 6 — First win: make their first piece RIGHT NOW
This is the moment that sells the whole system — before anything technical:
> "Let's make your first one now. Say **'script my first attraction reel'** and I'll write it from your story,
> hook three ways, keyword and all — or **'today's stories'** for three stories you can post in five minutes."
Hand to **`sf-talkinghead`** or **`sf-stories`**. They finish holding a real, ready-to-film piece — not a checklist.
Come back for Step 7 only after that piece is delivered (or if they say "set up the rest").

## Step 7 — Plumbing last (separate, optional, once each)
1. **Cadence and the weekly mix** — propose the defaults from the doctrine and confirm in one word: *"Default
   plan: 3–5 Reels a week — 2 attraction, 2 authority, 1 story — and stories every day; batch day Tuesday. Keep
   it, or change the number?"* (Honest capacity beats ambition; three is the floor.) Write `Cadence:` ·
   `Weekly mix:` · `Batch day(s):` → push. The routine itself is `sf-weekly-routine`.
2. **The posting tool — offer once, never push:** *"Want me to schedule your posts for you? I can connect
   Metricool (free to start) or GoHighLevel if you already use it. Or keep it copy-paste for now."* On yes → run
   the connect flow in `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` (the four checks, plain words) and
   record `Posting tool:` · `Connected on:` · `Brand / location:`. On no → `Posting tool: manual`. On "don't ask
   again" → `declined YYYY-MM-DD`. Push.
3. **The content board — offer once:** *"Want your posts on a visual board in your Notion? The YouTube plugin
   shares it."* Yes → `sf-board`; no → `Content board: declined YYYY-MM-DD`. Nothing → leave empty.
4. **The Friday performance note** — one line, never provisioned here: *"Once you're posting, say 'set up my
   Friday performance note' and every Friday you'll get which Reels and stories started agent conversations."*
   (`sf-analytics` owns it, with their explicit yes.)
5. Register the plugin in `config.md` — the one-line `## Short-Form (Week 3)` block (installed date, plugin
   version, "see identity/publishing.md") — **nothing else in config.md.** Set `Short-form setup: complete
   YYYY-MM-DD`. Push, verify. Close with the breadcrumb: *"You're set. Reels: 'script my attraction reels'.
   Stories: 'today's stories'. No filming: 'attraction carousel'. News: 'green screen on brokerage news'."*

> ⚡ **Keep onboarding light on the workspace.** The Brain pull at session start is the ONE heavy step; after it,
> local reads and small single-file pushes only. Never re-pull the whole Brain, never pre-create month folders
> (the content folder is made on first save), never run per-file verifies in a loop.

---

## Completion checklist
- [ ] Brain located (pulled first if empty), read, reflected back — **nothing re-asked**
- [ ] Second call routed: resume or one named part — **the interview never re-ran**
- [ ] `identity/content-pillars.md` written in the contract shape, five pillars mapped to the avatars, stories, positioning, proof — pushed
- [ ] Compliance three-state applied before the bios; `unset` stopped the bios with a plain line, nothing else
- [ ] Four bios, each answering the five questions, no invented credibility, no compensation, stamp applied — written to `publishing.md` + saved to `02 · Brand` — pushed
- [ ] Keyword chosen (one word), ManyChat state recorded — pushed
- [ ] Member handed to a first piece **before** any tool was mentioned
- [ ] Cadence/mix written; posting tool offered once with a real connect flow, answer recorded; board offered once; Friday note mentioned, not provisioned
- [ ] `config.md` Short-Form block only; `Short-form setup: complete` — pushed, verified
- [ ] Whole thing felt fast, warm, value-first, non-technical
