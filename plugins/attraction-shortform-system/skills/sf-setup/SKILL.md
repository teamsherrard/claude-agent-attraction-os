---
name: sf-setup
description: >
  One-time onboarding for the Agent Attraction Short-Form System, the Week 3 layer on the member's
  Agent Attraction Brain, run as one journey: (1) profile optimization on every platform they use
  (Instagram name field, bio with the keyword line, link in bio, highlights, pinned post; Facebook,
  TikTok, LinkedIn) as a copy-paste Profile Optimization Pack; (2) the Short-Form Game Plan; (3) the
  Notion board with the next 30 days mapped; (4) the scheduled workflows (Monday Week Plan, Friday
  note, optional daily stories) on one consent card; then the first Reel scripted. Reads the Brain,
  never re-asks it. A second call resumes or updates one part. Trigger on: "set up my attraction
  short-form", "set up short-form for agent attraction", "launch my attraction short-form", "open my
  attraction short-form", "build my content pillars", "write my attraction bios", "my recruiter bio",
  "set my keyword", "update my pillars", "update my bios", "connect my posting tool", "optimize my
  profiles for agents".
---

# Short-Form Attraction Engine — Setup (the four-step journey)

A warm onboarding that switches on the member's short-form engine as a **layer on their Agent Attraction
Brain** — in an order that makes sense to them. By the end they hold four things that didn't exist before, in
this sequence: **every profile optimized for the agents they attract → their Short-Form Game Plan → their
content board with the next 30 days on it → their scheduled workflows** — and they finish by scripting their
first Reel. One sitting, about twenty-five minutes; each step is announced before it starts.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — above all #1: plain and warm, never
technical, 2–4 related questions per stop, "your turn" on every stop, breadcrumbs. This is the member's first
impression of the plugin. The Brain Contract is `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## ⭐ THE RULES THAT SHAPE THIS SKILL
- **One Brain, never two.** Who they attract, their story, their positioning, their proof, their voice, their
  offer and their lead magnet already live in the Brain. This skill reads them and never re-asks. If you catch
  yourself about to ask — stop and read.
- **The journey is the product.** Profiles → Game Plan → board and 30 days → workflows → the first Reel. Each
  step is announced in one breath (*"Okay, cool — now I'm going to…"*) and runs without a menu. Nothing is "an
  optional afterthought"; the only optional item is the posting-tool connect, last.
- **Never hand off before saving.** Every step is written and pushed the moment it's confirmed (write → push →
  verify). A member who leaves mid-way loses nothing.
- **Not re-run on a second call.** Step 0 routes: resume the unfinished step, or update the one part they named.
- **Public needs compliance.** The profiles are public → the three-state gate before Step 2's pack. The Game
  Plan is private and builds in every state; posting waits.
- **Ask once, default if unsure** (`ask-once-default.md`, read by reference): propose from the Brain, let them
  react in a word; a question is a handoff — "your turn".

---

## Step 0 — Route (silent — the member never sees step numbers)
1. If `~/attraction-brain/` is missing, **pull it first** with `attraction-brain-sync` (a fresh session starts
   empty; the Brain lives in their workspace; located by ID, never by name). A tool error is never "no Brain".
   Only if the cloud genuinely has none: one warm line — *"Let's build your Attraction Brain first — say 'set up
   my attraction brain'. The more it knows you, the more your Reels sound like you and not like everyone else."*
2. Read `~/attraction-brain/brain.md`. Then read `identity/publishing.md` **if it exists** and its
   `Short-form setup:` line:
   - **missing / `not started`** → the full journey (Steps 1–6).
   - **`profiles pending compliance`** → compliance was `unset` last time: read it again now; `set` or `confirmed`
     → write the pack (Step 2's public half), then continue where the journey left off; still `unset` → one plain
     line, then the next unfinished step (the Game Plan is private).
   - **`profiles done`** → *"Welcome back — your profiles are optimized. Next: your Short-Form Game Plan."* → Step 3.
   - **`game plan done`** → *"Welcome back — your Game Plan is saved. Next: your content board and your next 30
     days."* → Step 4.
   - **`board done`** → *"Welcome back — your board is mapped. Next: your scheduled workflows."* → Step 5.
   - **`workflows done`** → *"Welcome back — everything's switched on. Let's make your first Reel."* → Step 6.
   - **a legacy value** (`pillars done` · `bios done` · `keyword done` from an earlier version) → resume at
     Step 2, keeping whatever exists: a `Keyword:` already set is never re-asked; pillars already in
     `content-pillars.md` are read by the Game Plan, never rewritten here.
   - **`complete`** → the **READY BRIEF** (one line that it's loaded, naming 3–4 things you know about them — who
     they attract, their keyword, this week's posts from `memory/content-calendar.md`, which workflows are on; at
     most ONE upgrade suggestion; *"What do you want to make?"*). Then route a named part — "update my bios" /
     "optimize my profiles for agents" → Step 2 only · "set / change my keyword" → Step 2's keyword part only
     (write `Keyword:` · `What it opens:`, mirror into `content-pillars.md`, push) · "build my content pillars" /
     "update my pillars" → `sf-gameplan` (UPDATE mode, section 2) · "connect my posting tool" → Step 5's last
     item only — or hand to `sf-talkinghead` / `sf-stories`. **Never the interview again.**
3. Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`)
   once now; it decides whether Step 2 writes the pack today.

## Step 1 — Welcome (name the four steps and the first win)
> "Let's switch on your short-form engine. I already know you from your Brain, so this is quick, and we'll go
> in order: first I'll make sure every platform you're on is optimized for the agents you attract; then I'll
> build your Short-Form Game Plan; then your content board with your next thirty days mapped onto it; then
> I'll switch on the workflows that draft your week for you. And we finish by scripting your first Reel.
> About twenty-five minutes. Your turn — ready?"

Then open only the four files the reflection needs: `identity/profile.md` (name, what they're building,
brokerage, market, handles) · `identity/avatars.md` (the primary type they attract) · `identity/strategy.md`
(the known-for) · `identity/voice.md` (their voice in one line). Everything else opens at the step that uses it;
a file already open stays open — never re-read one. Reflect back in one breath so it's clear nothing will be
re-asked:
> "Here's what I've got: you're [name], building [what] at [brokerage] in [market]; you attract [the primary
> type, one line]; you're known for [known-for]; your voice is [one line]. I won't ask you any of that again."

## Step 2 — Profile optimization (every platform they use)
> "Okay, cool — now I'm going to make sure every platform you're on is optimized for the agents you attract:
> your bios, your name fields, your link in bio, your highlights, and what to pin. You'll get it as one
> copy-paste pack."

**Lazy-load `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §8–§9a** (the keyword; the profile is the
recruiting landing page — `07-instagram/87`). **Open now:** `identity/journey.md` (the `## Why join me` breath if
written; otherwise the turning point) · `identity/positioning.md` · `identity/offer.md` (its `Comment keyword:`
line — the invitation word `attraction-offer` coined; the program's name goes into a bio only where the offer's
own bio line under `## How to talk about it` carries it, never its type or cadence; at `Status: seeds` the Partner
Offer is Week 2 — never call the seeds "the offer") · `memory/magnets.md → ## Current magnet` (the live guide and
funnel URL, built in Week 2) · `identity/proof.md` (credibility exactly as stated; none public → lead with who you
help; **never invent an award or a number**) · `identity/voice-samples.md` (their real phrasing) ·
`identity/operations.md` (the booking link if `profile.md` has none) · `identity/brand-visual.md` (the kit status
— the visuals line) · `identity/profiles.md` **if it exists** (normally it does — `lm-profiles` wrote it in Week 2,
aligned to the funnel; this step refreshes the text inside its five sections, never restarts, keeps every extra
section it added) · the Week 2 Platform Profiles pack in `02 · Brand`, if present (data — refresh it, never start
over) · `identity/compliance.md` (the disclosure fields; the stamp).

**1. The keyword first** (the bios carry it): propose ONE word — the offer's `Comment keyword:` first; **GUIDE**
when the live magnet rides on it (the primary route from Week 3 — the Resource rung delivers the guide by
keyword); a resource word like **SCRIPTS** or **PLAN** when there is a real free thing; **PARTNER** when the ask is
"get everything free — partner with me". One word, easy to say on camera and type in a comment, never a brokerage
name, never a word their followers already comment by habit. One line of why. (Per-Reel variants and ManyChat come
in the Game Plan and the keyword sheet.)

**2. The one stop of questions — only what the Brain doesn't answer** (2–4, together): *"Quick ones: (1) Which
platforms do you actually post on, in order — Instagram, Facebook, TikTok, LinkedIn? (2) Do you use a link-in-bio
tool, and which? (3) Does LinkedIn matter for you?"* (yes by default when they attract team leaders or
broker-owners) — and the keyword confirm in the same breath: *"and your keyword: [WORD] — good?"* **Your turn.**
Hesitation → propose from the Brain, confirm in a word. YouTube is Week 4's (`yt-setup` builds the channel) — only
if they ask for it now, write the channel's 2–3 sentence description into the pack and say the rest arrives in
Week 4; never fill `profiles.md → ## YouTube` here.

**3. The three-state gate, before anything public is written:** `confirmed` → go · `set` → go, remind once at the
end to confirm with the brokerage · `unset` → *"Your keyword and your Game Plan are private, so we keep moving —
but profiles are public, so before I write your pack I need your compliance basics. Say 'set up my attraction
compliance' (three minutes) and I'll pick the pack right back up."* Write `Keyword:` · `What it opens:` to
`publishing.md` now (create the file in the contract's full shape — every line label present, `Posting tool:
manual`, `Best times:` empty), set `Short-form setup: profiles pending compliance`, push, and go to Step 3 (the
Game Plan is private). The pack is written on the next call once the gate opens.

**4. Write the pack, in their voice — every bio answers the five questions** (who you are · who you help · what
you help them do · why they should listen · what to do next — `07-instagram/87`), each block with where it goes:
- **Instagram** — the **name field** (the searchable line: `[Name] · [what you help agents do]`, inside the field's
  limit — not the handle) · the **bio** (≤ 150 characters: line 1 who + how you help · line 2 who it's for + one
  credibility point · line 3 the ask — *"comment [KEYWORD]"* or *"free [resource] ↓"* — the keyword line) · the
  **link in bio and the order of its links** (1. the lead magnet — the live guide by name, the funnel URL; 2. book
  a call; 3. the YouTube channel — the line is written with "added in Week 4" when no channel exists yet; 4. the
  community, if they run one; action text, never "website") · the **five highlight names** (About · Agent wins ·
  Culture · Free value · Partner with me — plus one passion) and what goes in each · the **pinned-post plan** (three
  pins: the why-join-me or story Reel, one Proof Reel, the best Authority Reel — named from the calendar once the
  Game Plan maps them; until those exist, pin the strongest three they already have, or leave the slots empty with
  "pin [row] when it's live").
- **Facebook** — the profile intro line and the page intro (the short field), the **About** text (the five
  questions in a paragraph), the keyword line.
- **TikTok** — the **name** (name + the searchable phrase) and the **bio** (≤ 80 characters: who + for whom + the
  keyword).
- **LinkedIn** — the **headline** (≤ 220 characters, written for team leaders and broker-owners), the **About**
  (4–5 short paragraphs: the problem they carry, what the member built, proof, the ask), the **Featured section**
  (what to feature, in order: the lead magnet, the booking link, the best post).
- **The link-in-bio page** — its contents in order, each link's action text: the lead magnet · book a call · the
  YouTube channel · the community.
- **One line on visuals:** *"Your profile pictures and banners are the ones from your brand kit (02 · Brand);
  if the kit isn't done yet, the Design Package in Claude Design builds them — nothing to redo here."*
Compliance stamp as the file says (brokerage name / license where required). No compensation, no "#1" without a
source, no brokerage as the hook, former brokerages never named. Deliver the **Profile Optimization Pack** as
copy-paste blocks: *"Paste these in — or tell me what to change. Your turn."*

**5. On their yes — write, save, push:** `identity/profiles.md` exactly as the contract says — **the file normally
exists** (`lm-profiles` wrote it in Week 2) → replace only the text inside `## Instagram` · `## Facebook` ·
`## TikTok` · `## LinkedIn` (the bio, then the name field / highlights / pinned-post / link-order lines under it as
plain lines inside the same section) — never rename, reorder, or drop a section; leave `## YouTube` as it is; keep
every extra section and italic update line `lm-profiles` added, byte-for-byte. **Absent** (they skipped the Week 2
lead magnet session — say which week builds it, never "missing") → create it in the contract's shape: the title, the
owner line, then `## Instagram` · `## Facebook` · `## TikTok` · `## LinkedIn` · `## YouTube` (a one-line placeholder
— "written by your YouTube system in Week 4"). Then `identity/publishing.md` — create it now in the contract's full
shape if Step 2.3 didn't (every line label present from day one, `Posting tool: manual`, `Best times:` empty) and
fill `Keyword:` · `What it opens:` · `Link in bio:` (tool · the links in order with their action text) · `Story
highlights:` · `Platforms (priority order):` (what they said) · `Short-form setup: profiles done`. **Push both,
verify.** Save `Profile Optimization Pack — YYYY-MM-DD` to `02 · Brand/` per
`${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`. Say: *"Saved — your profiles are in your Brain and the pack is
in your Brand folder."*

## Step 3 — Now your Short-Form Game Plan (same session, no stop)
> "Okay, cool — now I'm going to build your Short-Form Game Plan: who you're talking to, your five pillars with
> real angles, the week you can actually keep, thirty hooks, the word that turns a comment into a conversation,
> and your next thirty days with a date on every post."

Run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/SKILL.md`** now, inside this session — it reads the keyword and
the profiles you just saved and never re-asks them; it holds at most two short stops (the five pillars as one
block; the cadence in one word) and the ManyChat question; it writes `identity/content-pillars.md`, the strategy
lines of `publishing.md`, and `memory/content-calendar.md`, saves `[Name]'s Short-Form Game Plan — YYYY-MM-DD`
to `03 · Content/Short-Form/`, and sets `Short-form setup: game plan done`. When it hands back, say one line —
*"Your Game Plan is in your workspace under Content → Short-Form."* — and go straight to Step 4. Never "come back
later"; never a pasting session in between.

## Step 4 — Now your content board and your next 30 days
> "Okay, cool — now your content board: I'll put your next thirty days on a board in your own Notion, one card
> per post with its date, so you always know what's next."

**Open now:** `identity/publishing.md → Content board:` (already open). Then:
- **A URL** → run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-board/SKILL.md`** in **mapping mode** ("map my next 30
  days"): it finds the board, ensures the Short-Form view, seeds the calendar's rows as dated `Idea` cards by System
  ID, count-checks, and says so plainly.
- **Empty and Notion connected** → the same mapping mode: find-or-create the one shared Content Dashboard per the
  spec, add the Short-Form view, seed the thirty days, write the board's URL to `Content board:`, push.
- **Empty and Notion not connected** → the spec's plain-words connect path (one line on what it gives them, the
  click path, one reassurance — never a block): *"Your calendar is safe in your Game Plan and your Brain either
  way; once Notion is connected, say 'map my next 30 days' and I'll build the board."* Leave `Content board:`
  empty. If they say they don't want a board: `Content board: declined YYYY-MM-DD`, push, one line — *"no problem
  — your calendar lives in your Game Plan; your Monday plan drafts from it."*
- **`declined`** → one line that the calendar lives in the Game Plan and the Brain, and move on (they can change
  their mind any time by asking).
Set `Short-form setup: board done`, push, verify. The YouTube system shares the same board in Week 4 — say so in
one line only if they ask.

## Step 5 — Now your scheduled workflows (one consent card, then the optional plumbing)
> "Okay, cool — now your scheduled workflows. Three of them can run for you, and every one only drafts —
> nothing posts, sends, or schedules on its own."

**Open now:** `config.md` (timezone; an existing `## Short-Form (Week 3)` block) · `identity/operations.md`
(`Friday note time:` · `Working hours:` — the Friday slot). **ONE consent card, in plain words, before creating
anything:**
> *"Here's what I'd switch on: the **Monday Week Plan** — every Monday morning your week's posts are drafted from
> your calendar and waiting, scripts, captions and your stories for the week, on your board (recommended: on, at
> 7:00 am); the **Friday performance note** — which Reels and stories started agent conversations this week, the
> one change, and next week's five (recommended: on, [the Friday slot]); and a **daily stories prompt** — three
> story ideas each morning (off unless you want it). All three, the Monday and Friday ones, or not yet? Different
> times are fine."* **Your turn.**
**Provision only on the yes, never silently; the yes given here is each workflow's consent — their skills do not
ask again:**
- **Monday Week Plan** → `sf-week-plan` Job A's provisioning: `list_scheduled_tasks` (adopt `attraction-sf-week-plan`
  if it exists), else `create_scheduled_task` with the prompt from
  `${CLAUDE_PLUGIN_ROOT}/skills/sf-week-plan/references/week-plan-task-prompt.md` verbatim, Mondays at their hour
  in `config.md → Timezone`; verify; `Week Plan task: attraction-sf-week-plan` · `Week Plan slot: Mondays [time]`.
- **Friday performance note** → `sf-analytics`' provisioning: adopt an existing Friday task, else create
  `attraction-sf-weekly-performance` with the prompt from
  `${CLAUDE_PLUGIN_ROOT}/skills/sf-analytics/references/weekly-performance-task-prompt.md` verbatim, Fridays at the
  `Friday note time:` line (else the last working hour); verify; `Weekly Content Performance task:
  attraction-sf-weekly-performance`.
- **Daily stories** → only if they asked for it: `sf-stories`' provisioning with
  `${CLAUDE_PLUGIN_ROOT}/skills/sf-stories/references/daily-stories-task-prompt.md` verbatim, every morning at their
  time; verify; `Daily Stories task: attraction-sf-daily-stories` · `Daily Stories time: [time]`. Not taken →
  `Daily Stories task: later` (they can say "turn on my daily stories" any time).
- **"Not yet" to any** → `declined` on that line, never re-offered, still available on demand ("turn on my Monday
  week plan", "set up my Friday performance note"). Never claim a schedule that did not save — verify each with
  `list_scheduled_tasks` (present, enabled, a `nextRunAt`). A demo Brain never gets a task.
**Register the plugin in `config.md`** — the `## Short-Form (Week 3)` block, exactly these lines and nothing else:
`Installed:` today's date · `Plugin version:` · `Layer:` → `identity/publishing.md` · `Week Plan task:` · `Week Plan
slot:` · `Weekly Content Performance task:` · `Daily Stories task:` · `Daily Stories time:` (each task line a task
id · `declined` · `later`; a line not yet offered reads `not offered yet`). Set `Short-form setup: workflows done`.
Push, verify. Confirm in one line: *"Switched on: [the ones they chose]. Say 'my attraction workflows' any time
to see or stop them."*

**The optional last item — the posting tool (offer once, never push):** *"One optional thing: want me to schedule
your posts for you? I can connect Metricool (free to start) or GoHighLevel if you already use it. Or keep it
copy-paste for now."* On yes → the connect flow in `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` (the four
checks, plain words) and record it all on the one `Posting tool:` line (`metricool · connected YYYY-MM-DD · brand
[name]` — never a secret) plus `Best times:` (per network, from the tool). On no → `Posting tool: manual` stays. On
"don't ask again" → `declined YYYY-MM-DD`. Both lines always exist — `sf-publish` updates only those two. Push.
No live-data connection is ever touched during setup.

## Step 6 — The first win: script the first Reel RIGHT NOW
> "Okay, cool — now let's make your first one. Row 1 of your calendar is [title]: say **'script my first
> attraction reel'** and I'll write it from your story, hook three ways, keyword and all — or **'today's
> stories'** for three stories you can post in five minutes."

Hand to **`sf-talkinghead`** (Phase 2, with the calendar's row 1 — the first of THE THREE TO FILM FIRST — as the
topic: one Reel, no question stop) or **`sf-stories`**. "Go" / "you pick" → the Reel. They finish holding a real,
ready-to-film piece — not a checklist. When it's delivered: set `Short-form setup: complete YYYY-MM-DD`, push,
verify, and close with the breadcrumb: *"You're set. Mondays your week is drafted for you; Fridays you get the
note. Reels: 'script my attraction reels'. Stories: 'today's stories'. No filming: 'attraction carousel'. News:
'green screen on brokerage news'. Your rhythm: 'plan my attraction week'."*

> ⚡ **Keep onboarding light on the workspace.** The Brain pull at session start is the ONE heavy step; after it,
> local reads and small single-file pushes only. Never re-pull the whole Brain, never pre-create month folders
> (the content folder is made on first save), never run per-file verifies in a loop. The live data connection is
> never called during setup — not for the Game Plan, not for the board, not for the workflows.

---

## Completion checklist
- [ ] Brain located (pulled first if empty); four files at Step 1, the rest at the step that used them; reflected back — **nothing re-asked**
- [ ] Second call routed: resume the unfinished step or one named part — **the journey never re-ran**
- [ ] Each step announced in one breath before it started; no menu, no "come back later" between steps
- [ ] The keyword proposed from the offer's word / the live magnet, confirmed in a word; `publishing.md` created in the full shape
- [ ] Compliance three-state applied before the pack; `unset` wrote the keyword privately, set `profiles pending compliance`, and continued to the Game Plan
- [ ] The Profile Optimization Pack: Instagram (name field · bio with the keyword line · link order · five highlights · pinned-post plan), Facebook, TikTok, LinkedIn (headline · About · Featured), the link-in-bio page in order, the visuals line; every bio answers the five questions; no invented credibility; no compensation; stamp applied — written into `identity/profiles.md`'s five sections (extra sections kept, headings never renamed; created with the `## YouTube` placeholder only if absent) + saved to `02 · Brand` — pushed
- [ ] The Game Plan built in the same session by `sf-gameplan` (pillars, publishing lines, the calendar written; the doc saved); `game plan done`
- [ ] The board mapped (or the connect path given, never blocking; `declined` honored); `board done`
- [ ] ONE consent card with the recommended defaults (Monday on · Friday on · daily stories off); tasks created only on the yes, adopted not twinned, verified; the `config.md` block with the five task keys — pushed; `workflows done`
- [ ] Posting tool offered once, last; answer recorded on the one line
- [ ] The first Reel scripted from row 1 (or today's stories); `Short-form setup: complete` — pushed, verified
- [ ] Whole thing felt fast, warm, value-first, non-technical — the member heard each step coming
