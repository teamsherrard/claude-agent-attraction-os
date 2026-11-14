---
name: sf-setup
description: >
  One-time onboarding for the Agent Attraction Short-Form System, the Week 4 layer on the member's
  Brain, one journey of five steps: (1) confirm the profiles and the two keywords (the Week 2 bios
  shown, refreshed only if offer, proof or funnel link changed; GUIDE and the offer's word); (2) the
  Short-Form Game Plan; (3) the Notion board with the next 30 days mapped; (4) the scheduled
  workflows on one consent card (Monday Week Plan, Sunday Batch Prep, Daily Engagement List, News
  Watch, Friday Performance Note, Monthly Calendar Refill, the extras, one email when something is
  ready); (5) the first Reel. Never re-asks the Brain; a second call resumes one part; the quarterly
  profile audit lives here. Trigger on: "set up my attraction short-form", "set up short-form for
  agent attraction", "launch my attraction short-form", "open my attraction short-form", "confirm my
  attraction profiles", "audit my attraction profiles", "my attraction keywords", "set my keyword",
  "connect my posting tool".
---

# Short-Form Attraction Engine — Setup (the five-step journey, Week 4)

A warm onboarding that switches on the member's short-form engine as a **layer on their Agent Attraction
Brain** — in an order that makes sense to them. Short-form is **Week 4**: when it opens the member already holds
the Brain (Week 1), the three Week 2 files — the Partner Offer, the guide, the kit (`exports/week3-kit-*.txt`,
whose chapter 6 is the bios and chapter 7 the six designed social posts and the CALLS TO ACTION table) — and the
brand from Week 3. By the end they hold five things in this sequence: **their profiles and their two keywords
confirmed → their Short-Form Game Plan → their content board with the next 30 days on it → their scheduled
workflows → their first Reel.** One sitting, about twenty-five minutes; each step is announced before it starts.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — above all #1: plain and warm, never
technical, 2–4 related questions per stop, "your turn" on every stop, breadcrumbs. This is the member's first
impression of the plugin. The Brain Contract is `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## ⭐ THE RULES THAT SHAPE THIS SKILL
- **One Brain, never two.** Who they attract, their story, their positioning, their proof, their voice, their
  offer, their guide, their bios and their kit already live in the Brain. This skill reads them and never re-asks.
  If you catch yourself about to ask — stop and read.
- **The journey is the product.** Confirm profiles and keyword → Game Plan → board and 30 days → workflows → the
  first Reel. Each step is announced in one breath (*"Okay, cool — now I'm going to…"*) and runs without a menu.
  Nothing is "an optional afterthought"; the only optional item is the posting-tool connect, last.
- **Never hand off before saving.** Every step is written and pushed the moment it's confirmed (write → push →
  verify through `attraction-brain-sync`; every push re-renders the member's Brain Board). A member who leaves
  mid-way loses nothing.
- **Not re-run on a second call.** Step 0 routes: resume the unfinished step, or update the one part they named.
- **Confirm, never rewrite.** The bios were written in Week 2 and live in `identity/profiles.md` and chapter 6 of
  the kit; this step shows them and refreshes a bio only when the offer, the proof or the funnel URL changed since.
  No Profile Optimization Pack document any more (2026-11-14) — a refreshed bio is a copy block in chat, written
  back to the Brain.
- **Two keywords, never more.** `GUIDE` delivers the guide; the offer's `Comment keyword:` is the invitation word.
  PARTNER, SCALE, GROWTH and every other default are retired (2026-11-14); nothing here proposes a third word.
- **Public needs compliance.** A refreshed bio is public → the three-state gate before it is written back. The Game
  Plan is private and builds in every state; posting waits.
- **The CTA law and the scalable offer bind every line.** Every call ask is the person · their help · free · to run
  the method (join register: *"If you want my help running this — the lessons, the templates, the community —
  partner with me and it's free."*; open register, `Join-gated package allowed: no`: *"I'll walk you through it,
  free, no strings."*) — never the brokerage as the reason, never compensation. Nothing promises the member's
  time per partner: no "stand next to me on a Saturday", no group-chat or one-to-one promise; the deliverables are
  the recorded lessons, the templates, the community, the weekly group call only when they already run one.
- **Week 4, in the member's words.** Never "Week 3" for short-form work (the brand and Claude Design are Week 3);
  YouTube is "a later week"; the Riverside editor "when you have the editor installed"; never a skill id or a
  file path in a sentence to the member; a missing input gets one warm line with the phrase that creates it.
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
   - **`profiles pending compliance`** → a refreshed bio was held because compliance was `unset`: read it again
     now; `set` or `confirmed` → write the held bio back (Step 2.5), then continue where the journey left off;
     still `unset` → one plain line, then the next unfinished step (the Game Plan is private).
   - **`profiles done`** → *"Welcome back — your profiles and your two words are confirmed. Next: your Short-Form
     Game Plan."* → Step 3.
   - **`game plan done`** → *"Welcome back — your Game Plan is saved. Next: your content board and your next 30
     days."* → Step 4.
   - **`board done`** → *"Welcome back — your board is mapped. Next: your scheduled workflows."* → Step 5.
   - **`workflows done`** → *"Welcome back — everything's switched on. Let's make your first Reel."* → Step 6.
   - **a legacy value** (`pillars done` · `bios done` · `keyword done` from an earlier version) → resume at
     Step 2, keeping whatever exists: a `Keyword:` line already holding the two words is never re-asked (an older
     single word — a retired default or a resource word — is replaced by the two, said in one line); pillars
     already in `content-pillars.md` are read by the Game Plan, never rewritten here.
   - **`complete`** → the **READY BRIEF** (one line that it's loaded, naming 3–4 things you know about them — who
     they attract, their two words, this week's posts from `memory/content-calendar.md`, which workflows are on; at
     most ONE upgrade suggestion; *"What do you want to make?"*). Then route a named part — "confirm my attraction
     profiles" / "check my attraction profiles" → Step 2 only · "audit my attraction profiles" → **Profile mode**
     (below) · "set / change my keyword" / "my attraction keywords" → Step 2's keyword part only (write `Keyword:` ·
     `What it opens:` for the two words, mirror into `content-pillars.md`, push) · "update my pillars" →
     `sf-gameplan` (UPDATE mode, section 2) · "connect my posting tool" → Step 5's last item only · "turn on my
     [workflow]" → that one workflow's provisioning line in Step 5, nothing else · "email me my notes" / "stop
     emailing me" → Step 5's `Email me:` line only — or hand to `sf-talkinghead` / `sf-stories`. **Never the
     interview again.**
3. Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`)
   once now; it decides whether a refreshed bio is written back today.
4. Read `config.md` for the `## Short-Form (Week 4)` block — an older `## Short-Form (Week 3)` heading is the same
   block (read it as such; rename the heading to `(Week 4)` on the next write, keeping every line).

## Step 1 — Welcome (name the five steps and the first win)
> "Let's switch on your short-form engine. You already hold more than you think — your offer, your guide, your
> six designed posts and your bios — and I know you from your Brain, so this is quick. We'll go in order: first
> I'll confirm your profiles and the two words your Reels will use; then I'll build your Short-Form Game Plan;
> then your content board with your next thirty days mapped onto it; then I'll switch on the workflows that
> draft your week for you. And we finish by scripting your first Reel. About twenty-five minutes. Your turn —
> ready?"

Then open only the files the reflection needs: `identity/profile.md` (name, what they're building, brokerage,
market, handles) · `identity/avatars.md` (the primary type they attract) · `identity/strategy.md` (the known-for)
· `identity/voice.md` (their voice in one line) · the newest `exports/week3-kit-*.txt` once (chapter 6 — BIOS —
for the bios' identity line; chapter 7 — SOCIAL GRAPHIC POSTS and the CALLS TO ACTION table — for the Game Plan at
Step 3; absent → the kit is built at the end of the offer sitting: note it, say nothing yet). Everything else
opens at the step that uses it; a file already open stays open — never re-read one. Reflect back in one breath so
it's clear nothing will be re-asked:
> "Here's what I've got: you're [name], building [what] at [brokerage] in [market]; you attract [the primary
> type, one line]; you're known for [known-for]; your voice is [one line]; your guide is [its title]. I won't ask
> you any of that again."

## Step 2 — Confirm your profiles and keyword (never rewrite)
> "Okay, cool — first your profiles. Your bios are already written and pointed at your guide, so I'm going to
> check them against what's changed since, confirm the two words your Reels will use, and ask only what I can't
> read off your Brain."

**Lazy-load `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §8–§9a** (the ladder and the keyword; the profile is
the recruiting landing page — `07-instagram/87`). **Open now:** `identity/profiles.md` **if it exists** (normally it
does — the Lead Magnet plugin's `lm-profiles` wrote it in Week 2: the five sections `## Instagram` · `## Facebook` ·
`## TikTok` · `## LinkedIn` · `## YouTube`, then its own extra sections — `## X` · `## Threads` · `## Google Business
Profile` · `## Brokerage site` · `## Email signature`; each section ends with an italic update line and its date) ·
`identity/offer.md` (the header — `Status:` · `Offer name:` · `Comment keyword:` · `Join-gated package allowed:`;
`## UVP → Bio-safe line:`; `## How to talk about it → Booking line:`; at `Status: seeds` the Partner Offer is Week 2
— never call the seeds "the offer") · `memory/magnets.md → ## Current magnet` (the live guide by title, its keyword
GUIDE, the funnel URL once the page is live) · `identity/proof.md` (the dated rows — anything newer than a bio's
update line) · `identity/operations.md` (the booking link — the one link until the page is live) ·
`identity/compliance.md` (the disclosure fields; the stamp) · `identity/publishing.md` if it exists (`Platforms` ·
`Link in bio:` · `Keyword:`).

**1. Show, don't rewrite.** The bios open with one identity line — *"[First Last] — helps [type of agent] [outcome]
· [Brokerage as compliance requires] · [City]"* — and point at one link (the funnel URL; the booking link until the
page is live). Show both in one breath: *"Your bios all open with '[identity line]' and point at [the link] — they're
chapter 6 of your kit; paste each into its platform if you haven't yet."* Then run **the change test**, silently,
per bio: has the offer (its name, its `Comment keyword:`, its `Bio-safe line:`), the proof (a newer dated row) or
the funnel URL changed since that section's update line? **Nothing changed → the bios stand; say so in one line and
move on.** Something changed → refresh only the lines it touches in that bio (the identity line tightened to the
offer · the credibility fact · the ask and the link — the ask in the CTA law's shape: *"Want my help running [the
method], free? Grab the guide ↓"*, or *"I'll walk you through it, free"* at the open register; never the brokerage
as the reason), inside the platform's hard limit with the count shown (Instagram 150 · Facebook intro 101 · TikTok
80 · LinkedIn headline 220), every other word kept, the compliance line never cut; show it as a **copy block in
chat** (*"paste this into [platform]"*) and ask in a word. **No file** (they skipped the Week 2 lead magnet
sitting) → one warm line — *"Your bios get written in your lead magnet sitting — say 'launch my lead magnet plugin'
and they're done in one go. Your Game Plan doesn't wait for them."* — and continue; never write a bio from scratch
here, never fill `## YouTube` (a later week).

**2. The two keywords — confirmed in one line, never more than two.** **GUIDE** (the magnet's keyword, set in Week 2
— delivers the guide) and the offer's **`Comment keyword:`** (the invitation word — opens the one-pager and the
call). *"Your two words: GUIDE sends your guide; [WORD] opens the conversation about partnering with you. Good?"*
Never a third word, never a retired default, never a brokerage name. `Comment keyword:` missing (an offer at
`Status: seeds`) → GUIDE alone for now, one line that the second word arrives with "build my partner offer". No live
magnet → the offer's word alone, one line that "launch my lead magnet plugin" writes GUIDE. (ManyChat, the DM bank
and the keyword sheet are the Game Plan's section 5 and `sf-comment-to-dm`'s — one of the two words each time.)

**3. The platform questions — only where the Brain is silent** (together, 2–4, with the keyword confirm in the same
breath): *"Quick ones: (1) Which platforms do you actually post on, in order — Instagram, Facebook, TikTok,
LinkedIn? (2) Do you use a link-in-bio tool, and which? (3) Does LinkedIn matter for you?"* (yes by default when
they attract team leaders or broker-owners). Skip any the Brain already answers (`publishing.md → Platforms` ·
`Link in bio:`; the handles in `profile.md`). **Your turn.** Hesitation → propose from the Brain, confirm in a word.
A YouTube channel belongs to a later week — never built or described here.

**4. The three-state gate — only when a bio is being refreshed** (a refreshed bio is public; confirming unchanged
bios and the two words needs no gate): `confirmed` → go · `set` → go, remind once at the end to confirm with the
brokerage · `unset` → hold the refreshed bio: *"Your two words and your Game Plan are private, so we keep moving —
a refreshed bio is public, so before I write it back I need your compliance basics. Say 'set up my attraction
compliance' (three minutes) and I'll finish it."* Write the keyword lines (Step 2.5) now, set `Short-form setup:
profiles pending compliance`, push, and go to Step 3. The held bio is written back on the next call once the gate
opens.

**5. Write, save, push:** `identity/publishing.md` — create it now in the contract's full shape if absent (every
line label present from day one, `Posting tool: manual`, `Best times:` empty) and fill `Keyword: GUIDE · [the
offer's word]` · `What it opens: GUIDE → [the guide's title] · [WORD] → the one-pager and the call` · `Link in bio:`
(the tool · the one link the bios carry · the page's links in order with their action text — the guide, book a
call, the community if they run one; a channel link only once a channel exists, never a placeholder) · `Story
highlights:` (the contract's names, unless the bios already name them) · `Platforms (priority order):` (what they
said) · `Short-form setup: profiles done`. `identity/profiles.md` **only when a bio was refreshed and they said
yes**: replace the text inside that one `## [Platform]` heading, end the section with `*Updated by the Short-Form
System on YYYY-MM-DD — [what changed]*`, keep every other section, heading and earlier update line byte-for-byte;
never rename, reorder or drop a heading; `## YouTube` untouched. **Push, verify** (the push re-renders their Brain
Board). Say: *"Your profiles stand [or: your [platform] bio is refreshed and saved] and your two words are set."*
No document is saved — the bios live in the kit and the Brain.

## Step 3 — Now your Short-Form Game Plan (same session, no stop)
> "Okay, cool — now I'm going to build your Short-Form Game Plan: who you're talking to, your five pillars with
> real angles, the week you can actually keep, thirty hooks, the two words that turn a comment into a
> conversation, and your next thirty days with a date on every post — starting with the six posts you already
> have designed, so your first two weeks are post, don't make."

Run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/SKILL.md`** now, inside this session — it reads the kit first
(chapter 7's six posts and the CALLS TO ACTION table; `offer.md → ## Content branches` and `## The framework`), then
the two keywords and the profiles you just confirmed, and never re-asks them; it holds at most two short stops (the
five pillars as one block; the cadence in one word) and the ManyChat question; it writes `identity/content-pillars.md`,
the strategy lines of `publishing.md` and `memory/content-calendar.md` (the six kit posts as rows 1–6, then the Reels),
saves `[Name]'s Short-Form Game Plan — YYYY-MM-DD` to `03 · Content/Short-Form/`, keeps the text at
`exports/short-form-game-plan-YYYY-MM-DD.txt` (the Brain Board reads it), and sets `Short-form setup: game plan
done`. When it hands back, say one line — *"Your Game Plan is in your workspace under Content → Short-Form."* — and
go straight to Step 4. Never "come back later"; never a pasting session in between.

## Step 4 — Now your content board and your next 30 days
> "Okay, cool — now your content board: I'll put your next thirty days on a board in your own Notion, one card
> per post with its date, so you always know what's next."

Notion is the working board — the dated cards the member moves (the owner, 2026-11-14: "Notion is important");
their Brain Board is the read-only map of the same month, re-rendered on every push — never a second place to edit.
**Open now:** `identity/publishing.md → Content board:` (already open). Then:
- **A URL** → run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-board/SKILL.md`** in **mapping mode** ("map my next 30
  days"): it finds the board, ensures the Short-Form view, seeds the calendar's rows as dated cards by System ID —
  the six kit posts first, then the Reels — count-checks, and says so plainly.
- **Empty and Notion connected** → the same mapping mode: find-or-create the one shared Content Dashboard per the
  spec, add the This Week, Short-Form and Calendar tabs (This Week opens first), seed the thirty days, write the board's URL to `Content board:`, push.
- **Empty and Notion not connected** → the spec's plain-words connect path (one line on what it gives them, the
  click path, one reassurance — never a block): *"Your calendar is safe in your Game Plan and your Brain either
  way; once Notion is connected, say 'map my next 30 days' and I'll build the board."* Leave `Content board:`
  empty. If they say they don't want a board: `Content board: declined YYYY-MM-DD`, push, one line — *"no problem
  — your calendar lives in your Game Plan; your Monday plan drafts from it."*
- **`declined`** → one line that the calendar lives in the Game Plan and the Brain, and move on (they can change
  their mind any time by asking).
Set `Short-form setup: board done`, push, verify. The YouTube system shares the same board in a later week — say so
in one line only if they ask.

## Step 5 — Now your scheduled workflows (one consent card, then the optional plumbing)
> "Okay, cool — now your scheduled workflows. Six of them can run for you, and every one only drafts —
> nothing posts, sends, or schedules on its own."

**Open now:** `config.md` (timezone; the existing `## Short-Form (Week 4)` block, or the older `(Week 3)` heading
read as the same block) · `identity/operations.md` (`Friday note time:` · `Working hours:` — the Friday slot; both still "set in Week …" placeholders → Fri 4:00 pm; the Friday time the member picks on the card is written to `identity/operations.md → Friday note time:` — the one line this plugin writes there, by the Brain contract's grant) · `publishing.md → Batch day(s):` (set by the Game Plan at Step 3 — the day the
Sunday Batch Prep precedes). Check once whether the member's mail is connected (Gmail or Outlook tools present) —
it decides the card's last yes. **ONE consent card, in plain words, before creating anything:**
> *"Here's what I'd switch on — all six draft, none of them post: the **Monday Week Plan** — every Monday your
> week's scripts, captions and stories are drafted onto your board with a week brief, and any welcome or win post
> the week earned (7:00 am); **Sunday Batch Prep** — the evening before you film, your teleprompter doc: this
> week's scripts grouped by outfit and location, hooks three ways, the keyword on each; the **Daily Engagement
> List** — every weekday morning, ten agents to engage with today and one comment starter each; the **Wednesday
> News Watch** — three to six real brokerage headlines with a 30-second green-screen take each, on your board;
> the **Friday Performance Note** — what started agent conversations, the one change, next week's rows (three at the default cadence, five at five), the post
> to repurpose ([the Friday slot]); and the **Monthly Calendar Refill** — your next thirty days from your pillars
> and what performed, your board refilled, the last Friday of the month. There are extras too — a keyword
> follow-up queue, a mid-week nudge, a monthly deep dive, a daily stories prompt, a quarterly profile check — say
> the word any time. All six, some, or not yet? Different times are fine. And shall I email you when something's
> ready — the Monday plan, Wednesday's headlines, the Friday note? One short email to you, nothing to anyone else."*
**Your turn.**
**Provision only on the yes, never silently; the yes given here is each workflow's consent — their skills do not
ask again.** Every task: `list_scheduled_tasks` first (adopt an existing task with that id, never a twin), else
`create_scheduled_task` with the owning skill's prompt file **verbatim** (the one task-prompt reference in that
skill's `references/` — the paths below; the owning skill's SKILL.md is the authority on its name; never write a
prompt that belongs to another skill), at the member's time in `config.md → Timezone`; verify (present, enabled, a
`nextRunAt`); write the line. The exact ids and owners (the brief of 2026-11-14 §5):

| Workflow | Task id | Owner · the prompt | Default · when | `config.md` line |
|---|---|---|---|---|
| Monday Week Plan (the week's welcome and win posts inside it) | `attraction-sf-week-plan` | `sf-week-plan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-week-plan/references/week-plan-task-prompt.md` | on · Mondays, the member's hour (7:00 am) | `Week Plan task:` · `Week Plan slot: Mondays [time]` |
| Sunday Batch Prep | `attraction-sf-batch-prep` | `sf-batch-publish` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-batch-publish/references/batch-prep-task-prompt.md` | on · the evening before the batch day | `Batch Prep task:` · `Batch Prep slot: [the evening before the batch day, time]` |
| Daily Engagement List | `attraction-sf-engagement` | `sf-comment-to-dm` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-comment-to-dm/references/engagement-task-prompt.md` | on · each weekday morning | `Engagement task:` · `Engagement time: [time]` |
| Brokerage News Watch (the Wednesday one) | `attraction-sf-news-watch` | `sf-greenscreen` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-greenscreen/references/news-watch-task-prompt.md` | on · Wednesdays | `News Watch task:` · `News Watch slot: Wednesdays [time]` |
| Friday Performance Note | `attraction-sf-weekly-performance` | `sf-analytics` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-analytics/references/weekly-performance-task-prompt.md` | on · Fridays, the Friday slot | `Weekly Content Performance task:` |
| Monthly Calendar Refill | `attraction-sf-calendar-refill` | `sf-gameplan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/references/calendar-refill-task-prompt.md` | on · the last Friday of the month | `Calendar Refill task:` |
| Keyword Follow-up Queue | `attraction-sf-keyword-queue` | `sf-comment-to-dm` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-comment-to-dm/references/keyword-queue-task-prompt.md` | optional · Tuesdays and Thursdays | `Keyword Queue task:` |
| Mid-week Nudge | `attraction-sf-midweek-nudge` | `sf-week-plan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-week-plan/references/midweek-nudge-task-prompt.md` | optional · Wednesdays | `Midweek Nudge task:` |
| Monthly Deep Dive | `attraction-sf-deep-dive` | `sf-analytics` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-analytics/references/deep-dive-task-prompt.md` | optional · the 1st of the month | `Deep Dive task:` |
| Daily Stories Prompt | `attraction-sf-daily-stories` | `sf-stories` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-stories/references/daily-stories-task-prompt.md` | optional · each morning | `Daily Stories task:` · `Daily Stories time: [time]` |
| Quarterly Profile Audit | `attraction-sf-profile-audit` | this skill (Profile mode) · `${CLAUDE_PLUGIN_ROOT}/skills/sf-setup/references/profile-audit-task-prompt.md` | optional · quarterly | `Profile Audit task:` |

Win and milestone posts are **not** a task of their own (the owner, 2026-11-14): the Monday Week Plan scans the
Brain for a new partner or a consented win and drafts the recognition words inside the week's drafts; "write a win
post for [Name]" works on demand (`sf-stories`).
- **"Not yet" to any** → `declined` on that line, never re-offered, still available on demand ("turn on my Monday
  week plan", "turn on my batch prep", "turn on my news watch", "set up my Friday performance note", "turn on my
  calendar refill"). The five optional lines read `later` after the card (named in one sentence, not offered one by
  one) unless the member asked for one now — then provision it the same way ("turn on my daily stories", "turn on my
  keyword queue", "turn on my mid-week nudge", "turn on my deep dive", "turn on my profile audit").
- **The email yes** → `Email me: yes YYYY-MM-DD` (needs the member's connected mail — Gmail or Outlook; each
  workflow then sends ONE short email to the member's own address when it leaves something ready — the subject says
  what is ready, the body the doc link and the two or three lines that matter; never to anyone else, never a
  campaign) · a no → `Email me: no` · no mail connected → say so in one line (*"no mail is connected yet, so your
  notes wait for you in Cowork and on your Brain Board — connect Gmail or Outlook any time and say 'email me my
  notes'"*) and record `Email me: no (no mail connected)`. Nothing is sent during setup.
- Never claim a schedule that did not save — verify each with `list_scheduled_tasks` (present, enabled, a
  `nextRunAt`); a task that failed to save is named and its line reads `later`. A demo Brain never gets a task.
**Register the plugin in `config.md`** — the `## Short-Form (Week 4)` block (an older `## Short-Form (Week 3)`
heading is the same block: rename it on this write and keep its lines), exactly these lines and nothing else, in
this order, locked spelling: `Installed:` today's date · `Plugin version:` · `Layer:` → `identity/publishing.md` ·
`Week Plan task:` · `Week Plan slot:` · `Batch Prep task:` · `Batch Prep slot:` · `Engagement task:` ·
`Engagement time:` · `News Watch task:` · `News Watch slot:` · `Weekly Content Performance task:` · `Calendar Refill task:` ·
`Keyword Queue task:` · `Midweek Nudge task:` · `Deep Dive task:` · `Daily Stories task:` · `Daily Stories time:`
· `Profile Audit task:` · `Email me:` — eleven task lines, each a task id · `declined` · `later` · `not offered yet`,
plus the slot and time lines and the email line (`yes YYYY-MM-DD` · `no` · `no (no mail connected)` · `not offered
yet`). Set `Short-form setup: workflows done`. Push, verify. Confirm in one line: *"Switched on: [the ones they
chose][, and I'll email you when something's ready]. Say 'my attraction workflows' any time to see or stop them."*

**The optional last item — the posting tool (offer once, never push):** *"One optional thing: want me to schedule
your posts for you? I can connect Metricool (free to start) or GoHighLevel if you already use it. Or keep it
copy-paste for now."* On yes → the connect flow in `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` (the four
checks, plain words) and record it all on the one `Posting tool:` line (`metricool · connected YYYY-MM-DD · brand
[name]` — never a secret) plus `Best times:` (per network, from the tool). On no → `Posting tool: manual` stays. On
"don't ask again" → `declined YYYY-MM-DD`. Both lines always exist — `sf-publish` updates only those two. Push.
No live-data connection is ever touched during setup.

## Step 6 — The first win: script the first Reel RIGHT NOW
> "Okay, cool — now let's make your first one. Your first two weeks open with the six posts you already have
> designed — post, don't make — and your first Reel is [title]: say **'script my first attraction reel'** and I'll
> write it from your story, hook three ways, keyword and all — or **'today's stories'** for three stories you can
> post in five minutes."

Hand to **`sf-talkinghead`** (Phase 2, with the calendar's first Reel row — the first talking-head row after the six
kit posts, the first of THE THREE TO FILM FIRST — as the topic: one Reel, no question stop) or **`sf-stories`**.
"Go" / "you pick" → the Reel. They finish holding a real, ready-to-film piece — not a checklist. When it's delivered:
set `Short-form setup: complete YYYY-MM-DD`, push, verify — **this last push re-renders the Brain Board** (the sync
does it on every push; a partial local Brain is completed first) — and close with the board line, then the
breadcrumb: *"You're set — and your Brain Board is updated: the Short-Form dot is green. Mondays your week is
drafted for you; the evening before you film, your teleprompter doc is waiting; every weekday morning, ten agents
to talk to; Wednesdays, your green-screen headlines; Fridays you get the note; the last Friday of the month, your
next thirty days. Reels: 'script my attraction reels'. Stories: 'today's stories'. No filming: 'attraction
carousel'. News: 'green screen on brokerage news'. Your rhythm: 'plan my attraction week'."* Name only the
workflows they switched on. If the board could not rebuild, the sync's own line replaces the first sentence:
*"your Brain Board couldn't rebuild this time — it will on the next save."*

> ⚡ **Keep onboarding light on the workspace.** The Brain pull at session start is the ONE heavy step; after it,
> local reads and small single-file pushes only. Never re-pull the whole Brain, never pre-create month folders
> (the content folder is made on first save), never run per-file verifies in a loop. The live data connection is
> never called during setup — not for the Game Plan, not for the board, not for the workflows.

## Profile mode — the Quarterly Profile Audit (on demand, or the scheduled task)
"audit my attraction profiles" / "check my attraction profiles", or the scheduled task `attraction-sf-profile-audit`
(quarterly; the prompt `${CLAUDE_PLUGIN_ROOT}/skills/sf-setup/references/profile-audit-task-prompt.md`, verbatim;
created only on the member's yes — the consent card's "say the word any time" or "turn on my profile audit" — adopted
if it exists, verified with `list_scheduled_tasks`, recorded as `Profile Audit task:` in the config block, stoppable
in one sentence). **Read:** `identity/profiles.md` (every section; the update lines) · `identity/offer.md` (the
header; `Bio-safe line:`; `Booking line:`) · `identity/proof.md` · `memory/magnets.md → ## Current magnet` ·
`identity/compliance.md` (the gate; the license display never cut) · `identity/voice.md`. **The test, per bio — the
five questions** (who you are: the identity line, the same everywhere · who you help: the type of agent, by stage ·
the outcome: one, in the agent's words · why believe you: one credibility fact that is in `proof.md` today · what
next: one ask in the CTA law's shape and one link — the funnel URL if live, else the booking link) **and the change
test** (the offer, the proof or the funnel URL changed since the section's update line). A bio that passes:
*"stands"*, one line. A bio that fails or is stale: **propose the refresh as a copy block** — the whole bio inside its
hard limit, the count under it, what changed and why in one line; never rewrite silently, never a third keyword. On
the member's yes → write it back inside the same heading with the update line (Step 2.5's rules), **push** (the
Brain Board re-renders), one line. **The scheduled run is draft-only:** it writes nothing to `profiles.md`; it keeps
its proposals at `~/attraction-brain/exports/profile-audit-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`), **ends
with a push** so the Brain Board shows the audit, sends the one short email when `Email me:` is yes and leaves its
note in Cowork; the member applies a refresh by saying "audit my attraction profiles" in chat. A whole-stack rewrite
(a new offer, a new brokerage) is the Lead Magnet plugin's — one line: *"say 'update my attraction bios' and the
whole stack is redone"*.

---

## Completion checklist
- [ ] Brain located (pulled first if empty); the reflection files and the kit text at Step 1, the rest at the step that used them; reflected back — **nothing re-asked**
- [ ] Second call routed: resume the unfinished step or one named part — **the journey never re-ran**
- [ ] Each step announced in one breath before it started; no menu, no "come back later" between steps; Week 4 in every line, never "Week 3" for short-form work, never a skill id or a path in a line the member reads
- [ ] Profiles **confirmed, not rewritten**: the identity line and the one link shown; the change test run per bio; a refresh only where the offer, the proof or the funnel URL changed — shown as a copy block, written back inside its heading with the update line on the yes; no bio written from scratch; `## YouTube` untouched; no pack document saved
- [ ] **Two keywords exactly** — GUIDE and the offer's `Comment keyword:` — confirmed in one line; no third word proposed; `publishing.md` created in the full shape, `Keyword:` carrying both words, `What it opens:` for each
- [ ] The platform questions asked only where the Brain was silent; compliance three-state applied only to a refreshed bio; `unset` held it, set `profiles pending compliance`, and continued to the Game Plan
- [ ] The Game Plan built in the same session by `sf-gameplan` — the kit read first, the six kit posts as rows 1–6, then the Reels; pillars, publishing lines, the calendar written; the doc saved; the text in `exports/`; `game plan done`
- [ ] The board mapped in Notion — the working board, the kit posts seeded first; the Brain Board named as the read-only map; or the connect path given, never blocking; `declined` honored; `board done`
- [ ] ONE consent card: the six recommended workflows with their times (the Monday plan carrying the week's win posts), the five extras in one sentence, the email yes; tasks created only on the yes, adopted not twinned, verified, each from its owner's prompt file; the `config.md` `## Short-Form (Week 4)` block with the eleven task lines, the slot and time lines and `Email me:` — pushed; `workflows done`
- [ ] Posting tool offered once, last; answer recorded on the one line
- [ ] The first Reel scripted from the first talking-head row (or today's stories); `Short-form setup: complete` — pushed, verified; the close named the Brain Board ("the Short-Form dot is green") and only the workflows switched on
- [ ] Every call ask in the CTA law's shape; nothing promised the member's time per partner; every write followed by a push
- [ ] Whole thing felt fast, warm, value-first, non-technical — the member heard each step coming
