---
name: sf-setup
description: >
  One-time onboarding for the Agent Attraction Short-Form System, the Week 4 layer on the member's
  Brain: one sitting, one step at a time — each step is shown, then it waits for the member's Yes or
  their changes. (1) Profiles and the two keywords confirmed (the Week 2 bios shown, refreshed only if
  something changed; GUIDE and the offer's word; platforms stated); (2) the Short-Form Game Plan with
  the ManyChat build sheet; (3) the Notion board with the next 30 days mapped; (4) four scheduled
  workflows switched on with a Yes (Monday Week Plan, Batch Prep, Wednesday News Watch, Monthly
  Calendar Refill; five extras stated), then the one question, Metricool or GoHighLevel; (5) the first
  Reel, then the Brain Board and Brain Book handed over. Never re-asks the Brain; a second call
  resumes one part. Trigger on: "set up my attraction short-form", "launch my attraction short-form",
  "confirm my attraction profiles", "audit my attraction profiles", "my attraction keywords", "set my
  keyword", "turn on my profile audit".
---

# Short-Form Attraction Engine — Setup (the five-step journey, Week 4)

A warm onboarding that switches on the member's short-form engine as a **layer on their Agent Attraction
Brain** — in an order that makes sense to them. Short-form is **Week 4**: when it opens the member already holds
the Brain (Week 1), the three Week 2 files — the Partner Offer, the guide, the kit (`exports/week3-kit-*.txt`,
whose chapter 6 is the bios and chapter 7 the six designed social posts and the CALLS TO ACTION table) — and the
brand from Week 3. By the end they hold five things in this sequence: **their profiles and their two keywords
confirmed → their Short-Form Game Plan (and their ManyChat build sheet) → their content board with the next 30 days
on it → their four scheduled workflows → their first Reel.** One sitting, about twenty-five minutes of work; **one
step at a time — every step ends by waiting for the member** (the owner, 2026-11-15).

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — above all #1: plain and warm, never
technical, **told, not asked** (every step a statement of what is being built; a question only for a fact the Brain
cannot hold) and **one step, then wait** (the stop at the end of every step), breadcrumbs. This is the member's first impression of the plugin. The
Brain Contract is `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## ⭐ THE RULES THAT SHAPE THIS SKILL
- **One Brain, never two.** Who they attract, their story, their positioning, their proof, their voice, their
  offer, their guide, their bios and their kit already live in the Brain. This skill reads them and never re-asks.
  If you catch yourself about to ask — stop and read.
- **Told, not asked (the owner, 2026-11-14).** Members follow the program. No "all, some, or not yet", no "want me
  to email you?", no platform question, no ManyChat question, no open-ended menu. Every step is a
  statement of what will be built; the consent card ends in ONE line the member answers with "Yes" — the one explicit
  yes the scheduled-task rule needs. Extras are stated, never offered as a menu. The only questions left are facts
  the Brain cannot hold.
- **ONE STEP, THEN WAIT (the owner, 2026-11-15 — this rule wins over every older "no stop" line).** The owner ran
  the sitting, walked away, and came back to find everything built: *"it ends up doing the entire work for me rather
  than waiting for me to give direction or feedback or answers… it should WAIT for me."* So:
  - **One step per reply.** Each reply does ONE step, shows what it built or what it proposes, and ends with **the
    stop line**. Nothing of the next step is read, built, saved or said until the member answers. A member who walks
    away comes back to exactly that line — nothing more has happened.
  - **The stop line is always the last line, always this shape:** *"Say **Yes** and I'll [the next step, in plain
    words] — or tell me what you'd change. **Your turn.**"* Each step below prints its own.
  - **Direction comes before a big build.** What shapes a document is shown first and waits: the five pillars and
    the week are proposed, the member says Yes or changes them, and only then is the Game Plan built.
  - **A change instead of a Yes** → make it, show only what changed, save it, and end with the same stop line
    again. **A question** → one plain answer, then the stop line again. **Anything unclear** → ask what they mean,
    once, and wait. Never read silence, a "hmm" or a question as a Yes.
  - **Still told, not asked.** The stop is never a menu and never one of the old questions (no "all, some or not
    yet", no "want me to email you?", no platform or ManyChat question): the step states what was built, and the
    only word the member ever has to say is **Yes**.
  - **"Do it all" / "don't stop" / "finish it without me"** — only when the member says so — → run the remaining
    steps without the stops, pausing only for the consent card's Yes and the posting-tool question. Never offered.
  - Each step still saves and stamps the moment it is built, so a member who leaves loses nothing and the next call
    opens on that step's stop line.
- **The journey is the product.** Confirm profiles and keyword → Game Plan → board and 30 days → workflows and the
  posting tool → the first Reel. Each step is announced in one breath (*"Okay, cool — now I'm going to…"*) and runs
  without a menu. Nothing is "an optional afterthought".
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
- **Platforms are never asked.** Instagram and Facebook, both, every Reel and every graphic (Facebook Reels is the
  same video reposted); TikTok and YouTube Shorts only as optional reposts of the same video — nothing new to make;
  LinkedIn for the carousels and story posts only when `identity/avatars.md` includes team leaders or broker-owners,
  otherwise off; the link in bio is the guide's funnel URL (one link) or the link-in-bio tool the Brain's bios already
  name. All stated, in one line each.
- **ManyChat is required, told, and never connected to Claude.** The Game Plan's section 5 tells the member to set it
  up this week in their own account from the build sheet `sf-comment-to-dm` writes; nothing here needs its connector
  or a paid plan for it; until it is live they reply by hand from the DM bank. Never "optional", never "connected".
- **Email is part of the process.** When the member's mail is connected (Gmail or Outlook tools present), every
  workflow emails them ONE short note at their own address when something is ready — never asked. No mail connected →
  one plain line, and their notes stay in Cowork.
- **The posting tool is not optional (the owner, 2026-11-14).** The posting step asks the one straight question —
  Metricool or GoHighLevel — and connects it (the Connect card in the chat for Metricool; the exact steps for
  GoHighLevel). Copy-paste is only the fallback line when the connect fails or the member walks away — never "for
  now", never a third option, never `declined`.
- **Public needs compliance.** A refreshed bio and the ManyChat messages are public → the three-state gate before
  they are written. The Game Plan is private and builds in every state; posting waits.
- **All the member ever has to say is "Yes" — at the end of each step — and ONE fact question (the owner,
  2026-11-14: "all that the student has to say is 'Yes'"; 2026-11-15: "it should WAIT for me").** Every step ends on
  its stop line; the consent card's Yes (Step 5) is also the consent every scheduled workflow needs; the one question
  is the posting tool, Metricool or GoHighLevel (Step 5's last item — a fact the Brain cannot hold). The pillars, the
  cadence and a refreshed bio are proposed and wait for the Yes — a member who wants one changed says so at the stop.
  Nothing else is asked in this journey.
- **The CTA law and the scalable offer bind every line.** Every call ask is the person · their help · free · to run
  the method (join register: *"If you want my help running this — the lessons, the templates, the community —
  partner with me and it's free."*; open register, `Join-gated package allowed: no`: *"I'll walk you through it,
  free, no strings."*) — never the brokerage as the reason, never compensation. Nothing promises the member's
  time per partner: no "stand next to me on a Saturday", no group-chat or one-to-one promise; the deliverables are
  the recorded lessons, the templates, the community, the weekly group call only when they already run one.
- **Week 4, in the member's words.** Never "Week 3" for short-form work (the brand and Claude Design are Week 3);
  YouTube is "a later week"; the editing step is stated, never hedged — *"when it's filmed: open a new chat and say
  'edit my reel' — your AI Editing Studio (Plugin 5)"*, installed in Week 4 with this plugin; never a skill id or a
  file path in a sentence to the member; a missing input gets one warm line with the phrase that creates it.
- **The close hands over the Brain Board and the Brain Book (the owner, 2026-11-14).** The sitting's last push is
  marked as the closing push; the sync returns the two links; the close says "here they are" with both, shows the
  Board file when it can, and never claims an update that did not happen.
- **Ask once, default if unsure** (`ask-once-default.md`, read by reference): propose from the Brain and state it;
  a genuine question — a fact the Brain cannot hold — is a handoff, "your turn".

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
   - **`profiles done`** → *"Welcome back — your profiles and your two words are confirmed. Say **Yes** and I'll lay
     out your five pillars and your week. **Your turn.**"* → wait; on the Yes, Step 3.
   - **`game plan done`** → *"Welcome back — your Game Plan is saved. Say **Yes** and I'll put your next thirty
     days on your content board. **Your turn.**"* → wait; on the Yes, Step 4.
   - **`board done`** → *"Welcome back — your board is mapped. Say **Yes** and I'll show you the four workflows that
     keep it filled. **Your turn.**"* → wait; on the Yes, Step 5.
   - **`workflows done`** → first read `publishing.md → Posting tool:`: while it still reads `manual` or `chosen: …
     — connect pending`, finish Step 5's last item (the one posting-tool question, or the chosen tool's connect).
     Then *"Welcome back — everything's switched on. Say **Yes** and I'll script your first Reel, '[title]'. **Your
     turn.**"* → wait; on the Yes, Step 6.
   - **a legacy value** (`pillars done` · `bios done` · `keyword done` from an earlier version) → resume at
     Step 2, keeping whatever exists: a `Keyword:` line already holding the two words is never re-asked (an older
     single word — a retired default or a resource word — is replaced by the two, said in one line); pillars
     already in `content-pillars.md` are read by the Game Plan, never rewritten here.
   - **`complete`** → the **READY BRIEF** (one line that it's loaded, naming 3–4 things you know about them — who
     they attract, their two words, this week's posts from `memory/content-calendar.md`, which workflows are on; at
     most ONE upgrade suggestion; then a statement of what is next and its phrase — *"Next on your calendar: [title], [day]. 'Script my attraction reels' writes it."* — never an open question). Then route a named part — "confirm my attraction
     profiles" / "check my attraction profiles" → Step 2 only · "audit my attraction profiles" → **Profile mode**
     (below) · "set / change my keyword" / "my attraction keywords" → Step 2's keyword part only (write `Keyword:` ·
     `What it opens:` for the two words, mirror into `content-pillars.md`, push) · "update my pillars" →
     `sf-gameplan` (UPDATE mode, section 2) · "my ManyChat build sheet" → `sf-comment-to-dm` Job E · "connect my
     posting tool" / "connected" → Step 5's last item only (the chosen tool's connect, or the question if none is
     chosen yet) · "turn on my [workflow]" → that one workflow's provisioning line in
     Step 5, nothing else · "email me my notes" / "stop emailing me" → Step 5's `Email me:` line only (`yes
     YYYY-MM-DD` when mail is connected; `no` when they say stop) — or hand to `sf-talkinghead` / `sf-stories`.
     **Never the interview again.**
   - **"start over" / "run the whole setup again" / "redo my short-form setup"** (said with or after the setup
     phrase — a member who wants a clean second pass, or a demo being shown again) → say one line (*"Running your
     whole short-form setup again, from the top — I'll update what you already have, never duplicate it."*), set
     `Short-form setup: not started`, push, and run the full journey (Steps 1–6). Everything is updated in place:
     the Game Plan is rebuilt under today's date, the board is upgraded and re-mapped by System ID (never a second
     board), a scheduled task that already exists is adopted (never a twin), the consent card is said again and its
     Yes is asked again, every step stops and waits as on a first run, and the posting-tool line is kept when a tool
     is already connected.
3. Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`)
   once now; it decides whether a refreshed bio and the ManyChat messages are written today.
4. Read `config.md` for the `## Short-Form (Week 4)` block — an older `## Short-Form (Week 3)` heading is the same
   block (read it as such; rename the heading to `(Week 4)` on the next write, keeping every line that still exists
   in the contract and deleting the three retired ones the contract names).
5. Check once whether the member's mail is connected (Gmail or Outlook tools present in the session) — it decides
   the `Email me:` line at Step 5 and the email sentence on the consent card.

## Step 1 — Welcome (name the five steps, play the member back, then WAIT)
> "Let's switch on your short-form engine. You already hold more than you think — your offer, your guide, your
> six designed posts and your bios — and I know you from your Brain, so this is quick. We'll go one step at a
> time, and I'll wait for you after each one: first your profiles and the two words your Reels will use; then
> your Short-Form Game Plan; then your content board with your next thirty days on it; then the workflows that
> draft your week for you and the tool that schedules your posts; and we finish by scripting your first Reel."

Then open only the files the reflection needs: `identity/profile.md` (name, what they're building, brokerage,
market, handles) · `identity/avatars.md` (the primary type they attract; whether team leaders or broker-owners are
among them — it decides LinkedIn) · `identity/strategy.md` (the known-for) · `identity/voice.md` (their voice in one
line) · the newest `exports/week3-kit-*.txt` once (chapter 6 — BIOS — for the bios' identity line; chapter 7 — SOCIAL
GRAPHIC POSTS and the CALLS TO ACTION table — for the Game Plan at Step 3; absent → the kit is built at the end of the
offer sitting: note it, say nothing yet). Everything else opens at the step that uses it; a file already open stays
open — never re-read one. Reflect back in one breath so it's clear nothing will be re-asked:
> "Here's what I've got: you're [name], building [what] at [brokerage] in [market]; you attract [the primary
> type, one line]; you're known for [known-for]; your voice is [one line]; your guide is [its title]. I won't ask
> you any of that again."

**The reply ends here, on the stop line — nothing of Step 2 is started:**
> "Is that still right? Say **Yes** and I'll start with your profiles — or tell me what's changed. **Your turn.**"
A correction (a new brokerage, a different agent they attract, a renamed guide) → say one line that it goes in
their Brain (*"say 'update my attraction brain' and I change it there"* — this skill never rewrites identity
files), carry the corrected fact through this sitting, and stop again.

## Step 2 — Confirm your profiles and keyword (never rewrite, never ask)
> "Okay, cool — first your profiles. Your bios are already written and pointed at your guide, so I'm checking them
> against what's changed since, confirming the two words your Reels will use, and setting your platforms — nothing
> for you to answer unless something changed."

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
chat** — a statement, never a Yes line: *"Your [platform] bio, refreshed because [what changed] — it's saved to your Brain; paste this into [platform]."* (the save follows the gate in point 4) **No file**
(they skipped the Week 2 lead magnet sitting) → one warm line — *"Your bios get written in your lead magnet sitting —
say 'launch my lead magnet plugin' and they're done in one go. Your Game Plan doesn't wait for them."* — and
continue; never write a bio from scratch here, never fill `## YouTube` (a later week).

**2. The two keywords — shown in one line, never asked, never more than two.** **GUIDE** (the magnet's keyword, set
in Week 2 — delivers the guide) and the offer's **`Comment keyword:`** (the invitation word — opens the one-pager and
the call). *"Your two words: GUIDE sends your guide; [WORD] opens the conversation about partnering with you."*
Never a third word, never a retired default, never a brokerage name. `Comment keyword:` missing (an offer at
`Status: seeds`) → GUIDE alone for now, one line that the second word arrives with "build my partner offer". No live
magnet → the offer's word alone, one line that "launch my lead magnet plugin" writes GUIDE. (ManyChat, the DM bank
and the keyword sheet are the Game Plan's section 5 and `sf-comment-to-dm`'s — one of the two words each time.)

**3. The platforms — stated, never asked (the owner, 2026-11-14).** One breath, from the Brain: *"Your platforms:
Instagram and Facebook, both — every Reel and every graphic; Facebook Reels is the same video reposted. TikTok and
YouTube Shorts take the same video any time you want more reach — nothing new to make. [LinkedIn carries your
carousels and story posts, because you attract team leaders. | LinkedIn stays off — you're attracting agents, not team
leaders.] Your link in bio is [the guide's funnel link | the link-in-bio tool your bios already name], one link."*
LinkedIn is on only when `identity/avatars.md` includes team leaders or broker-owners; the link in bio is the guide's
funnel URL (`memory/magnets.md → ## Current magnet`) — the booking link until the page is live — or the link-in-bio
tool the bios in `identity/profiles.md` already name. No question, no menu. A YouTube channel belongs to a later week
— never built or described here.

**4. The three-state gate — only when a bio is being refreshed** (a refreshed bio is public; confirming unchanged
bios, the two words and the platforms needs no gate): `confirmed` → go · `set` → go, remind once at the end to
confirm with the brokerage · `unset` → hold the refreshed bio: *"Your two words and your Game Plan are private, so
we keep moving — a refreshed bio is public, so before I write it back I need your compliance basics. Say 'set up my
attraction compliance' (three minutes) and I'll finish it."* Write the keyword and platform lines (Step 2.5) now, set
`Short-form setup: profiles pending compliance`, push, and end the step on its stop line (below) like any other. The held bio is written back on the next
call once the gate opens.

**5. Write, save, push:** `identity/publishing.md` — create it now in the contract's full shape if absent (every
line label present from day one, `Posting tool: manual`, `Best times:` empty) and fill `Keyword: GUIDE · [the
offer's word]` · `What it opens: GUIDE → [the guide's title] · [WORD] → the one-pager and the call` · `Link in bio:`
(the one link — the funnel URL, or the booking link until the page is live — or the tool the bios name with its links
in order and their action text: the guide, book a call, the community if they run one; a channel link only once a
channel exists, never a placeholder) · `Story highlights:` (the contract's names, unless the bios already name them)
· `Platforms (priority order): Instagram Reels · Facebook Reels (always, both) · LinkedIn (carousels, when
attracting team leaders) · TikTok / YouTube Shorts (optional reposts)` (the locked value; LinkedIn's clause reads
`LinkedIn off` when the avatars hold no team leaders) · `Short-form setup: profiles done`. `identity/profiles.md`
**only when a bio was refreshed** (and the gate in point 4 is open — no Yes is asked): replace the text inside that one `## [Platform]` heading, end
the section with `*Updated by the Short-Form System on YYYY-MM-DD — [what changed]*`, keep every other section,
heading and earlier update line byte-for-byte; never rename, reorder or drop a heading; `## YouTube` untouched.
**Push, verify** (the push re-renders their Brain Board). Say: *"Your profiles stand [or: your [platform] bio is
refreshed and saved], your two words are set, your platforms are set."* No document is saved — the bios live in the
kit and the Brain.

**The reply ends here, on the stop line — nothing of Step 3 is started:**
> "Say **Yes** and I'll lay out your five pillars and your week — or tell me what you'd change here. **Your
> turn.**"
A change (*"add LinkedIn"*, *"that bio isn't right"*, *"my link is different"*) → make it inside this step's own
rules (two keywords only; a bio change is a refresh, inside its limit, through the gate), show only what changed,
save, push, and stop again with the same line.

## Step 3 — Now your Short-Form Game Plan (same session — TWO replies: your direction first, then the build)
**3a — the pillars and the week: proposed, then WAIT (the member's direction comes before the document).**
> "Okay, cool — now your Short-Form Game Plan. Before I build it, here's what it stands on — your five pillars and
> the week you can actually keep."

Run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/SKILL.md`** now, inside this session, **up to the end of its Phase 3
only** — it reads the kit first (chapter 7's six posts and the CALLS TO ACTION table; `offer.md → ## Content
branches` and `## The framework`), then the two keywords, the platforms and the profiles you just confirmed, and
never re-asks them. It shows the five pillars (one line each) and the week (how many posts, the mix, the filming
day), saves both to the Brain as it does today, and **the reply ends on the stop line — the plan document is NOT
built yet:**
> "Say **Yes** and I'll build your Game Plan on these — or tell me what to change: a pillar, how many posts a
> week, or your filming day. **Your turn.**"
A change → `sf-gameplan` applies it by its own rules (still five pillars from the OS's five; the cadence the
member names; the filming day they name), shows only what changed, saves, and stops again with the same line.

**3b — on the Yes: the plan is built, handed over, then WAIT.**
> "Building your Game Plan now: who you're talking to, your pillars with real angles, thirty hooks, the two words
> that turn a comment into a conversation, and your next thirty days with a date on every post — starting with
> the six posts you already have designed, so your first two weeks are post, don't make."

`sf-gameplan` runs its remaining phases; ManyChat is told, never asked; it
writes `identity/content-pillars.md`, the strategy lines of `publishing.md` and `memory/content-calendar.md` (the six
kit posts as rows 1–6 at `Ready to Post`, then the Reels), saves `[Name]'s Short-Form Game Plan — YYYY-MM-DD` to
`03 · Content/Short-Form/`, keeps the text at `exports/short-form-game-plan-YYYY-MM-DD.txt` (the Brain Board reads
it), and sets `Short-form setup: game plan done`.

**Then the ManyChat build sheet, handed over here (the owner, 2026-11-14).** Run `sf-comment-to-dm` Job E in this
session: it writes `YYYY-MM-DD · ManyChat Build Sheet` beside the Game Plan's month folder (its text in
`exports/manychat-build-sheet-YYYY-MM-DD.txt`) and sets `publishing.md → ManyChat: not yet — set it up this week
(build sheet YYYY-MM-DD)`, pushed. Compliance `unset` → the sheet's messages are public, so the sheet waits for the
gate — the Game Plan still stands; say so in the line below. When it hands back, the hand-over lines — never "come back later", never a pasting session in between:
> *"Your Game Plan is in your workspace under Content → Short-Form: [the link]. ManyChat is how your two keywords
> answer themselves — set it up this week from your build sheet, saved right beside the plan (say 'my ManyChat build
> sheet' any time and I'll print it). You don't connect ManyChat to Claude. Until it's live, reply by hand from your
> DM bank."*

**The reply ends here, on the stop line — nothing of Step 4 is started:**
> "Open your Game Plan and have a look. Say **Yes** and I'll put your next thirty days on your content board — or
> tell me what to change in the plan. **Your turn.**"
A change → `sf-gameplan` in its UPDATE mode for that one part (a new dated copy; the calendar's un-started rows
only), one line of what changed, and the same stop line again.

## Step 4 — Now your content board and your next 30 days
> "Okay, cool — now your content board: I'll put your next thirty days on a board in your own Notion — the tabs at
> the top are Graphics, your six designed posts; Reels; and a Calendar, where this week lives — one card per post
> with its date, so you always know what's next."

Notion is the working board — the dated cards the member moves (the owner, 2026-11-14: "Notion is important");
their Brain Board is the read-only map of the same month, re-rendered on every push — never a second place to edit.
**Open now:** `identity/publishing.md → Content board:` (already open). Then:
- **A URL** → run **`${CLAUDE_PLUGIN_ROOT}/skills/sf-board/SKILL.md`** in **mapping mode** ("map my next 30
  days"): it finds the board, ensures the Graphics, Reels and Calendar tabs, seeds the calendar's rows as dated cards
  by System ID — the six kit posts first, on the Graphics tab at `Ready to Post`, then the Reels — count-checks, and
  says so plainly.
- **Empty and Notion connected** → the same mapping mode: find-or-create the one shared Content Dashboard per the
  spec, add the Graphics (opens first), Reels and Calendar tabs, seed the thirty days, write the board's URL to
  `Content board:`, push.
- **Empty and Notion not connected** → stated, never a block and never a question. When the connector-directory
  tools are in the session, put the **Notion Connect card in the chat** (`search_mcp_registry` with keywords
  `["notion"]`, then `suggest_connectors` with the directory id `69f3a300-cc60-48c4-b237-dfac56530dbf` and keywords
  `["content board"]`) and say: *"Click Connect, sign in to Notion, come back and say 'connected' — then I'll build
  your board. I only create and update your content board, nothing else in your Notion."* Those tools absent → the
  click path only: *"In the left sidebar click Customize → Connectors → Notion → Connect, sign in and approve, then say 'connected'."*
  Either way: *"Your calendar is safe in your Game Plan and your Brain meanwhile."* Leave `Content board:` empty (never
  write `declined` — an empty line is how the next run knows to build the board). If the member connects during the
  sitting — they say "connected", or the Notion tools are simply there when the close is reached — run mapping mode
  then, before the close.
- **An older `declined` value** (never written any more) → honoured: one line that the calendar lives in the Game Plan and the Brain, and move on (they can change
  their mind any time by asking).
Set `Short-form setup: board done`, push, verify. The YouTube system adds its own tab to the same board in a later
week — say so in one line only if they ask.

**The reply ends here, on the stop line — nothing of Step 5 is started:**
> "Open your board and have a look: [the link]. Say **Yes** and I'll show you the four workflows that keep it
> filled — or tell me what to change. **Your turn.**"
(No board yet — the Connect card is in the chat — → *"Your board is waiting on Notion. Say **Yes** and we go on to
your workflows — or say 'connected' once you've connected Notion and I'll build it first. **Your turn.**"*) A
change (a date, a post swapped, a card removed) → make it on the board and in the calendar row, one line, and the
same stop line again.

## Step 5 — Now your scheduled workflows (one consent card and its Yes; then the posting tool; then WAIT)
> "Okay, cool — now your scheduled workflows. Four run for you, and every one only drafts — nothing posts, sends,
> or schedules on its own."

**Open now:** `config.md` (timezone; the existing `## Short-Form (Week 4)` block, or the older `(Week 3)` heading
read as the same block) · `publishing.md → Batch day(s):` (set by the Game Plan at Step 3 — the day the Batch
Prep precedes). The mail check from Step 0.5 decides the card's email sentence. **ONE consent card, in plain words,
before creating anything — a statement, ending in its Yes:**
> *"Here's what I'm switching on for you: the **Monday Week Plan** — Mondays, 7:00 am: your week's scripts,
> captions and stories drafted onto your board with a week brief, and any welcome or win post the week earned;
> **Batch Prep** — [the evening before your batch day], 6:00 pm: your teleprompter doc, this week's scripts
> grouped by outfit and location, hooks three ways, the keyword on each; the **Wednesday Brokerage News Watch** —
> Wednesdays, 8:00 am: three to six real brokerage headlines with a 30-second green-screen take each, on your board;
> and the **Monthly Calendar Refill** — the last Friday of the month, 5:00 pm: your next thirty days from your
> pillars and what performed, your board refilled. Every one only drafts; nothing posts, sends or schedules on its
> own. I'll also email you a short note at your own address when something's ready. Say Yes and I'll set them up."*
No mail connected → the email sentence reads *"No mail is connected yet, so your notes stay in Cowork."* The times
are the program's defaults in the member's timezone; a member who names a different time gets it, never asked.
**On the Yes, provision all four — never silently, never one by one; the Yes given here is each workflow's consent
and their skills do not ask again.** Every task: `list_scheduled_tasks` first (adopt an existing task with that id,
never a twin), else `create_scheduled_task` with the owning skill's prompt file **verbatim** (the one task-prompt
reference in that skill's `references/` — the paths below; the owning skill's SKILL.md is the authority on its name;
never write a prompt that belongs to another skill), at the member's time in `config.md → Timezone`; verify (present,
enabled, a `nextRunAt`); write the line. Then state the extras in one sentence — never a menu: *"There are five more
— a keyword follow-up queue, a mid-week nudge, a monthly deep dive, a daily stories prompt and a quarterly profile
check — they're there if you want them; say the word any time."* The nine, their ids and owners:

| Workflow | Task id | Owner · the prompt | Switched on · when | `config.md` line |
|---|---|---|---|---|
| Monday Week Plan (the week's welcome and win posts inside it) | `attraction-sf-week-plan` | `sf-week-plan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-week-plan/references/week-plan-task-prompt.md` | by the Yes · Mondays 7:00 am | `Week Plan task:` · `Week Plan slot: Mondays [time]` |
| Batch Prep | `attraction-sf-batch-prep` | `sf-batch-publish` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-batch-publish/references/batch-prep-task-prompt.md` | by the Yes · the evening before the batch day, 6:00 pm | `Batch Prep task:` · `Batch Prep slot: [the evening before the batch day, time]` |
| Wednesday Brokerage News Watch | `attraction-sf-news-watch` | `sf-greenscreen` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-greenscreen/references/news-watch-task-prompt.md` | by the Yes · Wednesdays 8:00 am | `News Watch task:` · `News Watch slot: Wednesdays [time]` |
| Monthly Calendar Refill | `attraction-sf-calendar-refill` | `sf-gameplan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/references/calendar-refill-task-prompt.md` | by the Yes · the last Friday of the month, 5:00 pm | `Calendar Refill task:` |
| Keyword Follow-up Queue | `attraction-sf-keyword-queue` | `sf-comment-to-dm` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-comment-to-dm/references/keyword-queue-task-prompt.md` | by phrase · Tuesdays and Thursdays | `Keyword Queue task:` |
| Mid-week Nudge | `attraction-sf-midweek-nudge` | `sf-week-plan` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-week-plan/references/midweek-nudge-task-prompt.md` | by phrase · Wednesdays | `Midweek Nudge task:` |
| Monthly Deep Dive | `attraction-sf-deep-dive` | `sf-analytics` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-analytics/references/deep-dive-task-prompt.md` | by phrase · the 1st of the month | `Deep Dive task:` |
| Daily Stories Prompt | `attraction-sf-daily-stories` | `sf-stories` · `${CLAUDE_PLUGIN_ROOT}/skills/sf-stories/references/daily-stories-task-prompt.md` | by phrase · each morning | `Daily Stories task:` · `Daily Stories time: [time]` |
| Quarterly Profile Audit | `attraction-sf-profile-audit` | this skill (Profile mode) · `${CLAUDE_PLUGIN_ROOT}/skills/sf-setup/references/profile-audit-task-prompt.md` | by phrase · quarterly | `Profile Audit task:` |

Win and milestone posts are **not** a task of their own (the owner, 2026-11-14): the Monday Week Plan scans the
Brain for a new partner or a consented win and drafts the recognition words inside the week's drafts; "write a win
post for [Name]" works on demand (`sf-stories`). The engagement routine is the Game Plan's 15-minute daily routine
(text, not a task); the performance read is on demand ("how's my content doing") and in the Monthly Deep Dive.
- **Anything but a Yes** → nothing is created; the four lines read `later`, and the four phrases bring any of them
  back ("turn on my Monday week plan", "turn on my batch prep", "turn on my news watch", "turn on my calendar
  refill"). A "stop" or "no" to a named one → `paused` on that line, never re-offered, still available by its
  phrase. The five by-phrase lines read `later` after the card unless the member asked for one now — then provision
  it the same way ("turn on my daily stories", "turn on my keyword queue", "turn on my mid-week nudge", "turn on my
  monthly deep dive", "turn on my profile audit").
- **The email line — never asked:** mail connected (Gmail or Outlook) → `Email me: yes YYYY-MM-DD` (each workflow
  then sends ONE short email to the member's own address when it leaves something ready — the subject says what is
  ready, the body the doc link and the two or three lines that matter; never to anyone else, never a campaign) ·
  no mail connected → `Email me: no (no mail connected)` and the one plain line (*"no mail is connected yet, so your
  notes stay in Cowork — connect Gmail or Outlook any time and say 'email me my notes'"*). Nothing is sent during
  setup. The value is the OS answer other plugins read.
- Never claim a schedule that did not save — verify each with `list_scheduled_tasks` (present, enabled, a
  `nextRunAt`); a task that failed to save is named and its line reads `later`. A demo Brain never gets a task.
**Register the plugin in `config.md`** — the `## Short-Form (Week 4)` block (an older `## Short-Form (Week 3)`
heading is the same block: rename it on this write and keep its lines; delete the three retired lines the contract
names if an older block carries them), exactly these lines and
nothing else, in this order, locked spelling: `Installed:` today's date · `Plugin version:` · `Layer:` →
`identity/publishing.md` · `Week Plan task:` · `Week Plan slot:` · `Batch Prep task:` · `Batch Prep slot:` · `News
Watch task:` · `News Watch slot:` · `Calendar Refill task:` · `Keyword Queue task:` · `Midweek Nudge task:` · `Deep
Dive task:` · `Daily Stories task:` · `Daily Stories time:` · `Profile Audit task:` · `Email me:` — nine task lines,
each a task id · `paused` · `later`, plus the slot and time lines and the email line (`yes YYYY-MM-DD` · `no (no
mail connected)` · `no` only when the member said "stop emailing me"). No brackets in the block. Set `Short-form
setup: workflows done`. Push, verify. Confirm in one line: *"Switched on: your Monday plan, your batch prep, your
Wednesday headlines and your monthly refill[, and I'll email you when something's ready]. Say 'my attraction
workflows' any time to see or stop them."*

**The last item — the posting tool (the owner, 2026-11-14: NOT optional; never copy-paste as the plan).** The one
straight question of this step — a fact the Brain cannot hold: *"Which one schedules your posts — Metricool or
GoHighLevel? Metricool is free to start and connects with one click; GoHighLevel only if you already run it. Your
turn."* One word back. No "optional", no third option in the question. Then, per `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md`
(the connect flow; the member never hears "API", "token" is said only as the thing they paste into the connector's
own settings):
- **Metricool** → write `Posting tool: chosen: metricool — connect pending`, push. When the connector-directory tools
  are in the session (`search_mcp_registry` → `suggest_connectors`), call them so the **Connect card appears in the
  chat** — `search_mcp_registry` with keywords `["metricool", "scheduling posts"]`, then `suggest_connectors` with
  the directory id `70ba6d62-7e98-4ef4-9073-d161d900a95f` and keywords `["posts"]` ("For your posts", a Connect
  button) — and say: *"Click Connect, sign in to Metricool, come back and say 'connected'."* Those tools absent →
  the click path only: *"Customize → Connectors → find Metricool → Connect, then come back and say 'connected'."* —
  never a URL to paste for Metricool. On "connected" (or any yes — never wait for the exact word): verify with `getBrandSettings` + `getScheduledPosts`, write
  `Posting tool: metricool · connected YYYY-MM-DD · brand [name]` (never a secret) and `Best times:` (per network,
  from the tool), push, one line.
- **GoHighLevel** → write `Posting tool: chosen: gohighlevel — connect pending`, push. The exact steps in plain words:
  *"In GoHighLevel: Settings → Integrations → Private Integrations → create a token with the social-planner scopes
  and copy it. In Cowork: Customize → Connectors → Add custom connector → name it GoHighLevel → URL
  `https://services.leadconnectorhq.com/mcp/` → paste the token and your location id into the connector's own fields
  (never into this chat) → Connect. Then come back and say 'connected'."* On "connected": verify (the connected social
  accounts read back), write `Posting tool: gohighlevel · connected YYYY-MM-DD · location [name]`, push, one line.
- **The connect fails or cannot be read back** → one line, the only place copy-paste is said: *"until it's
  connected your posts are copy-paste; say 'connect my posting tool' when you're back."* **The member walks away
  mid-connect** → nothing more happens; the sitting waits where it is. The line keeps `chosen: …
  — connect pending`; `declined` is gone. Both lines always exist — `Posting tool:` and `Best times:`; `sf-publish`
  updates only those two (`manual` is the placeholder from file creation at Step 2 until this step runs, the same
  sitting). No live-data connection is ever touched during setup; the connect itself is the member's click.

**The step ends on the stop line — the first Reel is NOT scripted yet** (said once the posting tool is connected,
or its one fallback line has been said):
> "Last step: your first Reel — '[the first talking-head title on your calendar]'. Say **Yes** and I'll script it
> now — or name a different one from your plan. **Your turn.**"
Another title named → that row becomes the first Reel (it must be a row on the calendar; an idea that is not on it
goes through "script my attraction reels" later — say so in one line), and the same stop line again.

## Step 6 — The first win: script the first Reel (on the member's Yes)
> "Okay, cool — here's your first one. Your first two weeks open with the six posts you already have
> designed — post, don't make; they're on your Graphics tab, ready to post. Your first Reel is [title] — I'm
> scripting it now, from your story, hook three ways, keyword and all."

Hand to **`sf-talkinghead`** (Phase 2, with the calendar's first Reel row — the first talking-head row after the six
kit posts, the first of THE THREE TO FILM FIRST — as the topic (or the row the member named at Step 5's stop): one Reel, no further stop inside the script; **inside setup it skips its own editing paragraph, its own closing push
and its own Board-and-Book line — this step's close says each of them exactly once**). They finish holding a real, ready-to-film piece — not a checklist. When it's delivered: set
`Short-form setup: complete YYYY-MM-DD`, then **the sitting's closing push** (the owner, 2026-11-14) — push through
`attraction-brain-sync` **marked as the sitting's closing push**: the Brain plugin's sync rebuilds the Brain Board AND
refreshes the Brain Book's "What's next" page from the WHOLE local Brain (a partial local Brain is completed first)
and gives back two links — both files live in the member's `01 · AI Brain` folder. This skill only calls it and
relays what it returns.

**The close — a fixed, visible step, never a passing mention.** Before the breadcrumb, in this shape:
> *"Your Brain Board and your Brain Book are updated — here they are: [the Board link] · [the Book link]. Download the Board and open the file — it opens in your browser: your Short-Form dot is green, and its page shows your two keywords, this week's posts and
> your workflows."*
When the session can show a file in the chat, show the Board file itself as well as the link. If the Board or the
Book could not rebuild, say which, plainly, with the phrase that retries it (*"refresh my brain board"* / *"show me
my Brain"*) — never claim an update that did not happen. A demo Brain gets the same close (the files are tagged
DEMO). **Before the close, look once at what got connected during the sitting:** Notion connected now and no board
yet → build it (Step 4) first; a posting tool still at `chosen: … — connect pending` whose tools are now in the
session → verify it and write the connected line. **Then the breadcrumb — five short numbered lines, never a
paragraph** (a member reads a list, not a wall):
> 1. **Post** your six designed posts on their dates — they're on your Graphics tab, ready to post.
> 2. **Film** on your batch day, [day]. The evening before, your teleprompter doc is waiting.
> 3. **When it's filmed:** open a new chat and say "edit my reel" — that opens your AI Editing Studio.
> 4. **Set up ManyChat** this week from your build sheet — say "my ManyChat build sheet" to see it.
> 5. **"My attraction workflows"** shows or pauses your Monday plan, your batch prep, your Wednesday headlines and
>    your monthly refill.
Line 3 adds *"Install Plugin 5 from the same marketplace first, then say 'set up riverside' once"* only when the
editor is not installed. The other phrases ("script my attraction reels", "today's stories", "how's my content
doing") are on the Brain Board's Short-Form page — they are not said here.
Name only the workflows that saved. No board yet → "they're in your Game Plan's calendar" replaces "on your Graphics
tab" in both lines. Compliance `unset` → the compliance line is said ONCE in the whole sitting: when a held bio already said it at Step 2, it is not repeated; otherwise the breadcrumb opens with the one line *"Before anything is posted, say 'set up
my attraction compliance' — three minutes"*, said once. The editing step is part of the process (Plugin 5 is installed in Week 4 with
this plugin) — never hedged.

> ⚡ **Keep onboarding light on the workspace.** The Brain pull at session start is the ONE heavy step; after it,
> local reads and small single-file pushes only. Never re-pull the whole Brain, never pre-create month folders
> (the content folder is made on first save), never run per-file verifies in a loop. The live data connection is
> never called during setup — not for the Game Plan, not for the board, not for the workflows.

## Profile mode — the Quarterly Profile Audit (on demand, or the scheduled task)
"audit my attraction profiles" / "check my attraction profiles", or the scheduled task `attraction-sf-profile-audit`
(quarterly; the prompt `${CLAUDE_PLUGIN_ROOT}/skills/sf-setup/references/profile-audit-task-prompt.md`, verbatim;
created on the member's phrase — "turn on my profile audit" — adopted if it exists, verified with
`list_scheduled_tasks`, recorded as `Profile Audit task:` in the config block, stoppable in one sentence; the
provisioning is a statement: *"Switching on your quarterly profile check — the first of January, April, July and
October, 8:00 am."*). **Read:** `identity/profiles.md` (every section; the update lines) · `identity/offer.md` (the
header; `Bio-safe line:`; `Booking line:`) · `identity/proof.md` · `memory/magnets.md → ## Current magnet` ·
`identity/compliance.md` (the gate; the license display never cut) · `identity/voice.md`. **The test, per bio — the
five questions** (who you are: the identity line, the same everywhere · who you help: the type of agent, by stage ·
the outcome: one, in the agent's words · why believe you: one credibility fact that is in `proof.md` today · what
next: one ask in the CTA law's shape and one link — the funnel URL if live, else the booking link) **and the change
test** (the offer, the proof or the funnel URL changed since the section's update line). A bio that passes:
*"stands"*, one line. A bio that fails or is stale: **propose the refresh as a copy block** — the whole bio inside its
hard limit, the count under it, what changed and why in one line — a statement, never a Yes line (*"saved to your Brain — paste this
into [platform]"*); never silently, never a third keyword. In chat, write it back inside the same heading with the update line
(Step 2.5's rules), **push** (the Brain Board re-renders), one line. **The scheduled run is draft-only:** it writes
nothing to `profiles.md`; it keeps its proposals at `~/attraction-brain/exports/profile-audit-YYYY-MM-DD.txt` (the
Brain syncs `exports/*.txt`), **ends with a push** so the Brain Board shows the audit, sends the one short email when
`Email me:` is yes and leaves its note in Cowork; the member applies a refresh by saying "audit my attraction
profiles" in chat. A whole-stack rewrite (a new offer, a new brokerage) is the Lead Magnet plugin's — one line:
*"say 'update my attraction bios' and the whole stack is redone"*.

---

## Completion checklist
- [ ] Brain located (pulled first if empty); the reflection files and the kit text at Step 1, the rest at the step that used them; reflected back — **nothing re-asked**
- [ ] Second call routed: resume the unfinished step or one named part — **the journey never re-ran**
- [ ] **ONE STEP PER REPLY, AND EVERY STEP ENDED ON ITS STOP LINE** — after the welcome, the profiles, the pillars-and-week proposal, the built Game Plan, the board, the consent card and the posting tool; nothing of the next step was read, built, saved or said before the member answered; a change was made, shown and followed by the same stop line; silence or a question was never read as a Yes; "do it all" was honoured only when the member said it
- [ ] Each step announced in one breath before it started; **told, not asked** — no menu, no "all, some or not yet", no "want me to", no platform or ManyChat question; the only word the member had to say was Yes; the ONE fact question is the posting tool; Week 4 in every line, never "Week 3" for short-form work, never a skill id or a path in a line the member reads
- [ ] Profiles **confirmed, not rewritten**: the identity line and the one link shown; the change test run per bio; a refresh only where the offer, the proof or the funnel URL changed — shown as a copy block, written back inside its heading with the update line (stated, no Yes); no bio written from scratch; `## YouTube` untouched; no pack document saved
- [ ] **Two keywords exactly** — GUIDE and the offer's `Comment keyword:` — shown in one line; no third word proposed; `publishing.md` created in the full shape, `Keyword:` carrying both words, `What it opens:` for each
- [ ] **Platforms stated, never asked**: Instagram and Facebook both; TikTok and Shorts as optional reposts; LinkedIn only when the avatars hold team leaders or broker-owners; the one link in bio; `Platforms (priority order):` written in the locked value; compliance three-state applied only to a refreshed bio; `unset` held it, set `profiles pending compliance`, and continued to the Game Plan
- [ ] The pillars and the week PROPOSED first and the Game Plan built only on the member's Yes, in the same session, by `sf-gameplan` — the kit read first, the six kit posts as rows 1–6 at `Ready to Post`, then the Reels; pillars, publishing lines, the calendar written; the doc saved; the text in `exports/`; `game plan done`; **the ManyChat build sheet written and handed over in one line** (set it up this week; never connected to Claude; "my ManyChat build sheet" prints it)
- [ ] The board mapped in Notion — the Graphics, Reels and Calendar tabs; the kit posts seeded first on Graphics at `Ready to Post`; the Brain Board named as the read-only map; or the Notion Connect card put in the chat (the click path as the fallback), never blocking, never asked; an older `declined` honored, never written; `board done`
- [ ] ONE consent card in the owner's shape: the four with their days and times, "every one only drafts", the email sentence (or the no-mail line), **"Say Yes and I'll set them up"**; all four created on the Yes, adopted not twinned, verified, each from its owner's prompt file; the five extras stated in one sentence; `Email me:` set from the mail check, never asked; the `config.md` `## Short-Form (Week 4)` block with the nine task lines, the slot and time lines and `Email me:` in the locked order, the retired lines deleted — pushed; `workflows done`
- [ ] Posting tool asked as the one straight question (Metricool or GoHighLevel — never optional, never a third option) and connected: the Connect card in the chat for Metricool (the click path only as the fallback, never a URL), the exact steps for GoHighLevel (token and location into the connector's own fields, never into chat); verified on "connected"; the `Posting tool:` line one of the four values, pushed; copy-paste said only as the fallback line
- [ ] The first Reel scripted only after the member's Yes at Step 5's stop, from the first talking-head row (or the row they named); `Short-form setup: complete` — the sitting's closing push made through the sync, marked as such, verified
- [ ] **The close handed over the Brain Board and the Brain Book with their links — "here they are"** (the Board file shown too when the session can; a rebuild that failed named plainly with its retry phrase); then the breadcrumb in the owner's order — the six designed posts · the batch day · "edit my reel" in a new chat (Plugin 5, the AI Editing Studio; install it first if missing) · "my ManyChat build sheet" · "my attraction workflows" — naming only the workflows that saved
- [ ] Every call ask in the CTA law's shape; nothing promised the member's time per partner; every write followed by a push
- [ ] Whole thing felt fast, warm, value-first, non-technical — the member heard each step coming
