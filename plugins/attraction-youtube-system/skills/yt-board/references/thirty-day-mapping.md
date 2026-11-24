# The 30-day mapping — how the Game Plan calendar becomes dated cards (and stays 30 days ahead)

The rule this plugin adds on top of the shared board spec (`${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`,
byte-identical with the Short-Form System's copy and never edited here): **the 🎬 YouTube tab carries
the next 30 days of planned long-form videos, dated, at the member's cadence — never more, never less, never an
undated card.** The 90-day backlog lives in the Game Plan doc and the Brain's calendar rows; the Brain holds the
anchors (cadence, cycle position) and the content log. Read by `yt-board` (Step 3), the Monday Kickoff
(`yt-briefing`, the top-up), and `yt-make-video` (the top-up at publish).

**A card is the member's own video and nothing else (Mike, 2026-11-23):** no reference video, no "watch first" link,
no competitor video or summary, no trailer card — the member watches nobody before planning theirs. One video a week,
drafted in full onto its card when its Monday comes (§3a).

## 1. The source, in order
1. **The Game Plan's dated calendar in the Brain** — `memory/content-calendar.md → ## Long-form (YouTube)`
   (written by `yt-gameplan` at anchor time; the section this plugin owns inside the Short-Form-owned file): one
   row per video with a real recording date, a publish date, the bucket, the lane, the guest, Status, a System
   ID; the `Window:` line says what is mapped. **The section absent** (a Brain that predates it) → the Game
   Plan doc's first-90-days calendar (`🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` in `03 · Content/Long-Form/`,
   newest is current; its table: Week of · Video · Kind · Guest). Nothing is said to the member about the missing
   file — `yt-gameplan` creates it with its next write. A row written before 2026-11-23 may carry a trailing
   `Reference video` cell — it is ignored, never read, never written.
2. **The anchors** in `identity/channel.md` → `## Game Plan anchors`: `Cadence:` (`1/week` — the default for the
   first month — or `2/week`, with its `since` date) and `Cycle position:` (where the member is on the eight-video
   cycle — the first row to card is the row at that position); `## The CTA line` — the kit's two spoken lines for the
   Resource Assets cell.
3. **`memory/content-log.md`** — a title already `Scripted` / `Recorded` / `Published` is past the window's start:
   never re-card it; the window begins at the first calendar row with no row in the log (or an `Idea` row only).
4. **`memory/interview-pipeline.md`** — the guest for each interview slot (Stage `Candidate` / `Invited` / `Booked`
   / `Recorded`), their working title, their Recording date when booked. A guest is anyone successful in the
   member's upline, downline or brokerage (Mike, 2026-11-23) — not only an agent who succeeded with the member's own
   method.
5. **The filming day** — `identity/channel.md → ## Channel → Filming day:` first (the day the member gave at
   setup), then `identity/operations.md → Filming window:` (the Short-Form Game Plan writes it when the batch day is
   set; `not set yet` is a real answer — the plan then dated its rows on Saturdays). Read only to explain a date: a
   card's dates are its row's own (§2) and are never recomputed here.
   `identity/publishing.md → Keyword:` — the two words (GUIDE · the offer's word); `memory/magnets.md → ## Current
   magnet` — the guide's title and funnel URL.
6. **The board's link** — `identity/publishing.md → Content board:` first; that file absent (the member skipped
   Week 4) → the `Board:` line of `identity/channel.md`'s `## Channel` block. Every reader looks in that order.
The member's own board edits win on dates and forward status moves (the spec's conflict rule) — read the board
before writing to it.

## 2. Which rows fall inside 30 days
- **The dates are the rows' own.** `yt-gameplan` dated every row by its first-date rule — video 1 recorded on the
  member's next filming day **at least three days after the plan was built** (no filming day on file → the Saturday
  after next), published two days later, every later row following from it (seven days apart at one a week). The
  card copies the row's Recording date and Publish date; nothing here recomputes them, and **no card is ever dated
  the day of the sitting** — a card never says "record today". Week 1 on the plan is the week of video 1's
  Recording date. The window = today through today + 30 days; a row is in the window when its Recording date falls
  inside it.
- **The first three rows of every plan, in this order — exactly these, never another set (Mike, 2026-11-23):**
  1. **The member's blueprint** — the most-searched topic that can be tied to their value proposition; its Pillar by
     the row's bucket (`Niche: Problem` · `Niche: Situation` · `Niche: Future`, as the plan's row says), `• Pillar: Authority`.
  2. **Why they joined their brokerage** — their own move, told the way they tell it (the Why I Switched format); a
     Situation row — Pillar `Niche: Situation`, `• Pillar: Authority · Story angle`.
  3. **An interview** — anyone successful in their upline, downline or brokerage; Pillar `Interview`, `• Pillar:
     Proof`; no guest named → the plan's own title, "A conversation with an agent — guest to be named", and the
     no-guest rule below when its week arrives.
  The cards follow the rows in the rows' order and never reorder them; the rest of the eight-video cycle (3 niche ·
  1 model · 4 interviews) follows as the plan wrote it. **There is no trailer row and no trailer card** — a plan that
  still carries one ("My channel trailer", written before 2026-11-23) is a `yt-gameplan` refresh away; this skill
  never cards it and says nothing about it (a trailer card already on the board is left to the member — never
  deleted, never topped up).
- **At one a week (the default for the first month):** 4–5 rows in a full window — the first month is the
  blueprint · why I joined my brokerage · an interview · the plan's next row, and the fifth row, when the window
  holds it, follows the plan. **Right after setup the count is often three
  or four**, because the first video is at least three days out (up to two weeks when no filming day is on file) —
  say the count that was read back, never a fixed number. **At two a week (the step-up):**
  8–9 rows (two per week, in the calendar's order within the week — niche first, as the plan wrote it). When the
  cadence anchor changes, the next top-up re-counts the window at the new pace; un-started cards are re-dated from
  the calendar's re-dated rows.
- **Interview slots count** — the interviews are inside the cadence, never on top of it. A slot whose guest is
  `Booked` with a Recording date → that date wins (even if it sits outside the week's filming day). A slot at
  `Candidate` / `Invited` → card it as the plan wrote it, Guest = the named candidate, with
  `• Invite: [guest] — not yet confirmed` in the Context right after the pillar line. **A slot with no guest → the
  card keeps the plan's own title, exactly: "A conversation with an agent — guest to be named"** (the row's title —
  never "Book your next agent interview", never a to-do or a bracket tag in a title), Guest empty; the card is
  renamed to the guest's title once a guest is named.
- **An interview week with no guest** (the owner's decision, 2026-11-21 — the normal first-time member). When that
  week arrives and no guest is named: the week's video is the next topic video from the member's four pillars, and the
  interview moves to the first open week after a guest is named. No week is ever empty; no invite, guide or note is
  drafted to nobody; nobody is ever contacted without the member's yes. On the board: this week's video is the next
  `Idea` topic row forward (Problem, Situation or Future) — by the plan's rule (`yt-gameplan` Phase 8, "An interview week
  with no guest", the same as the Monday Kickoff's) that row takes the Recording and Publishing dates the
  conversation row carried, and its card takes them too. The conversation row and its card stay exactly as they are
  until a guest is named (then `yt-interview` writes the guest and their date on the earliest card still titled
  "guest to be named"). Never a second card, never a card without a date. What the member reads, word for word: *"No guest named yet, so this week's video is
  '[title]', from your topics. Your first interview goes on your plan the day you name someone — say 'set up an
  agent interview'."*
- **Batching** (two interviews recorded in one sitting, published on the plan): the Recording Dates share the
  sitting; the Publishing Dates keep the plan's weeks.
- When the plan runs short (fewer rows left than the window needs), card what exists and say so: *"Your Game Plan has
  [n] videos left — say 'refresh my attraction game plan' when you want the next ninety days planned."*

## 3. The card (the spec's vocabulary, exactly)
| Field | What goes in |
|---|---|
| **Topic** | the exact title from the plan as a plain sentence a person would say — sentence case, under twelve words; never a System ID, a bracket tag, a file name, a date or ALL CAPS (the member can refine it later — the System ID column keeps the card findable; the Monday Kickoff confirms it as the video's final title when it drafts the video) |
| **Format** | `Long-Form` |
| **Status** | `Idea` (the Monday Kickoff moves this week's to `Scripted` when it drafts it in full; filmed → `Recorded`; edited and waiting to go out → `Ready to Post`; live → `Published`) |
| **Pillar** | by the row's bucket — Problem → `Niche: Problem` · Situation → `Niche: Situation` · Future → `Niche: Future` · Interview → `Interview` · Model → `Model`; never the playlist name (the calendar row's `Lane` cell carries that), never an OS pillar name here |
| **Guest** | interviews only — the guest's name from the pipeline (or the candidate to invite): anyone successful in the member's upline, downline or brokerage, and only a guest named under the plan's rule (`yt-gameplan` Phase 4: the member named them, or the Brain holds them — never a name the plan itself took from the Top 50); empty for a slot with no guest |
| **Context** | `• Pillar: Authority` (the three Niche options; the why-I-joined-my-brokerage video — `Niche: Situation` — adds `· Story angle`) / `• Pillar: Proof` (Interview) / `• Pillar: Perspective` (Model) first — the spec's rule; then, **only for a video the member gave their own WORDING for (an `identity/channel.md → ## In your words` entry that is a line of theirs for this video), `• Your words: "[their sentence]"`** — a topic pick, a filming day, a name alone or a `skipped` entry is never quoted on a card; then `• Invite: [guest] — not yet confirmed` for a guest not yet booked; then `• What: …` (the title's promise in a few words) and `• Outcome: …` (what the viewer can do after it), written from the title and the "for" and "pain" of its line in the plan's TITLE NOTES — that note holds no What or Outcome of its own, and its codes are never copied onto a card; ≤12 words a bullet |
| **Recording Date** | the calendar row's own Recording date (the plan's first-date rule: never the day the plan was built — the first video is at least three days out); a `Booked` interview → its Recording date |
| **Publishing Date** | the calendar row's own Publish date — two days after recording by the plan's rule; never earlier than recording |
| **Resource Assets** | the two CTAs, copied from the Week 3 Kit's chapter 7 CALLS TO ACTION table as `channel.md → ## The CTA line` holds them: the guide ask (*"… Comment GUIDE and I'll send it."* · the guide's title · its funnel URL — description line 2 and the pinned comment) · the call line in the CTA law's shape for the register (join: *"If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*; open: *"I'll walk you through it, free, no strings."* · the booking link — description line 1) · the two words from `publishing.md → Keyword:`; always copied from `channel.md → ## The CTA line` (with no kit, setup built the two lines there, labeled "(from your Brain — your kit's wording replaces it)"); `identity/content-pillars.md`'s two CTAs line only when that block is empty. Never the brokerage as the reason; nothing that promises the member's time per partner |
| **System ID** | the calendar row's own (`yt-YYYY-MM-w[n][a/b]` — the plan's week and slot, `yt-2026-11-w2a`); a fresh one only when the row has none, written back to the row; never changed after; never in the title |
| **Script · SEO** | empty at seed — the Monday Kickoff and `yt-make-video` fill them (real links to the member's own documents only) |
No `Reference Video`, no `References` — the columns are gone from the spec (Mike, 2026-11-23); a board that still has
them hides them (§3b).
Card icon 🎬. **The card page at seed holds 🎯 THE HOOK and 📋 ASSETS & NOTES only** (the spec's locked long-form
layout — 🎯 THE HOOK · 🎬 SCRIPT · 🖼 THUMBNAIL BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE · 🎙 GUEST · 📋 ASSETS &
NOTES · ✅ PUBLISH IT · 📊 AFTER IT'S OUT; the same order on every card, a section replaced in place,
never stacked): 🎯 one working opening line from the plan's title promise, labeled *"working line — the scripted hook
and the breakdown are written when this video is drafted"* (never a promise of the Monday Kickoff: a card is seeded
before the member has said Yes to any workflow); 📋 the brief, in plain words — which of your four pillars it belongs
to, by the pillar's own name (an interview or a model video says so) · who it is for · the problem it answers · why it
is on your plan, as a sentence (`yt-board` Step 3 holds the sentences — never the note's code, never "lane", "niche",
"bucket" or "pillar", never another channel's video) · the filming date · your two calls to action · the compliance
line to say. The Monday Kickoff drafts the video in full (§3a); the Monthly Channel Review and the on-demand video
reads write 📊 AFTER IT'S OUT; `yt-make-video` completes the card before filming.

### 3a. The card body when the Kickoff has drafted it — ONE video a week, in full (Mike, 2026-11-23)
When a card's Monday comes, the Monday Kickoff (`yt-briefing`) — or `yt-make-video`, for a video the member starts
early — writes the whole package onto the card, in the locked sections. **The shape, every time:**
- **The title** — the card's Topic, confirmed as the video's final title (renamed in place when the draft sharpened
  it; the System ID keeps the card findable).
- **🎯 THE HOOK** — the scripted hook, word for word, the one the member reads to camera; under it the
  bullet-point breakdown of the video — its sections in order, one line each, the guide ask inside minute one and
  the call ask about a third of the way in marked where they fall.
- **🎬 SCRIPT** — the full teleprompter script, eight to twelve minutes, word for word (the hook → the guide ask
  inside minute one → the sections → the call ask → the payoff → the next video), ready to paste into the
  teleprompter and read.
- **An interview card has NO 🎬 SCRIPT section** — its package is 🎙 GUEST: the guest, the transformation the
  title promises, the question list (the whole interview, in order), their three distribution sentences. An
  interview is never scripted.
- **✅ PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO** — laid down with its click paths as the spec writes them; the
  video's own values arrive when `yt-make-video` writes the SEO package.
- Status → `Scripted`. Nothing else: 🖼 THUMBNAIL BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE are `yt-make-video`'s;
  📊 AFTER IT'S OUT the review's.
Never a summary in place of the script, never a batch of several videos' summaries on one Monday, never a reference
video, never a competitor's video or title on the card.

### 3b. An older board (made between 2026-11-15 and 2026-11-23)
It carries a `Reference Video` and a `References` column and its cards may carry a `📚 REFERENCE VIDEO — WATCH THIS
FIRST` section. The first time this skill touches such a board: hide both columns from the 🎬 YouTube tab's shown
columns (update the view to the spec's six) and from the card's side panel (the spec's page layout) — once, silently;
never delete a column or clear a cell (the member's data). A card's 📚 section is dropped the next time that card is
written (the writer rewrites the page in the locked order without it); nothing is said about any of it. A trailer
card is left exactly as the member has it.

## 4. Find-first, count-check, say so
- Before creating any card: System ID → exact title → near match (the spec's two-way sync). Found → update, never a
  twin.
- **The carded test — how a run tells "never carded" from "the member took it off the board".** Every run that
  creates long-form cards records them in the Brain: one dated block appended under
  `memory/content-calendar.md → ## Kickoff briefs (YouTube)` holding the line `carded: [the System ID of each card created]` (the board step at
  setup, "update my attraction video board", and `yt-make-video` when it creates a card or tops up at publish write
  a short block of their own — `Board — YYYY-MM-DD · carded: …`; the Monday Kickoff adds the line to its own
  block, whose first line is `Kickoff — YYYY-MM-DD · [title]`). **A row with no card:** its System ID is in an earlier
  `carded:` line → the member removed that card — it stays off the board, nothing is re-created, and it is said
  once (*"skipping [title] — you took it off the board"*; in a Kickoff, inside the note's bracketed notice). Never
  listed → the card was never made: create it now, with the row's own System ID. A Brain with no `carded:` line at
  all (a board built before 2026-11-15) → treat a missing card inside the 30 days as never carded, once, and start
  the record with this run.
- After the batch: count the cards in the window and read the count back. A failed write is named and retried once;
  never silent; never a count you did not read back. **The count is said once, by the reply's owner** — inside setup
  `yt-setup` Step 7's own count line; on demand `yt-board` Step 4's one reply: *"✓ Your next 30 days are on your
  content board — [n] videos, under the YouTube tab at the top: [link]."* Nothing about reference videos — there are
  none. Never an interview count in the line, never "your interview guests" — a
  guest is mentioned only when a card's Guest cell holds a name.
- Never a card without a date; never the whole 90 days; never a loose idea; never a tag or an id in a title.

## 5. The rolling rule — who tops it up, when
- **The Monday Kickoff** (every run, scheduled or on demand): after drafting this week's ONE video in full (§3a),
  re-count the window from today at the cadence anchor; pull the next calendar row(s) until 30 days are visible —
  each new card a seed (§3), nothing searched for it; one line in its note,
  in this wording — the same in every file: `🗓 BOARD: your next 30 days are on your content board ({n} videos)`.
- **`yt-make-video` at publish** and **"update my attraction video board"**: the same count and pull.
- **A plan refresh** (`yt-gameplan` on "refresh my attraction game plan") or **a cadence change** ("change my
  YouTube pace" — the step-up to two a week, or back to one): the new calendar's rows replace un-started `Idea` rows and
  cards inside the window only when the titles or dates changed; `Scripted` and later rows and cards are never
  touched; the member hears one line about what moved.
- **Status, one truth:** a row's Status in the Brain's calendar and its card's Status on the board move together —
  the Monday Kickoff flips both to `Scripted`, `yt-make-video` to `Recorded`, `Ready to Post` and `Published`; a row is never
  deleted (a dropped video is `Status: dropped`, its card removed only by the member).
- Every write that touches the Brain (a System ID written back, a row's Status) ends with an `attraction-brain-sync`
  push; the push re-renders the Brain Board — the read-only map of the same month.
- Without a board (Notion not connected or declined): nothing here runs; the Game Plan calendar is the window
  and the Monday Kickoff drafts straight from it.

## 6. Plain words (what the member hears)
"your next 30 days", "your content board", "the tabs at the top of your board", "the YouTube tab", "its card",
"your filming day", "your Game Plan", "your four pillars" / "a topic video", "your blueprint", "this week's video, scripted in full" —
never "window", "System ID", "properties", "views",
"database", "the spec"; never "lane", "niche", "bucket", "pillar" or "cadence" (say "your pace"), never "the hook"
(say "how it opens"); never "your guests", "your interview guests" or "your agents" as a fact; never "reference
video", "watch first", "trailer" or a competitor's name. If they ask what the
small tag in the side column is: *"that's how I find your card even if you rename it — just leave it be."* If they
ask where the video to watch went: *"Your card is about your video now — nothing to watch first."*
