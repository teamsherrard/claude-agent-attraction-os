# The 30-day mapping — how the Game Plan calendar becomes dated cards (and stays 30 days ahead)

The rule this plugin adds on top of the shared board spec (`${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`,
byte-identical with the Short-Form System's copy and never edited here): **the 🎬 YouTube tab carries
the next 30 days of planned long-form videos, dated, at the member's cadence — never more, never less, never an
undated card.** The 90-day backlog lives in the Game Plan doc and the Brain's calendar rows; the Brain holds the
anchors (cadence, cycle position) and the content log. Read by `yt-board` (Step 3), the Monday Kickoff
(`yt-briefing`, the top-up), and `yt-make-video` (the top-up at publish).

## 1. The source, in order
1. **The Game Plan's dated calendar in the Brain** — `memory/content-calendar.md → ## Long-form (YouTube)`
   (written by `yt-gameplan` at anchor time; the section this plugin owns inside the Short-Form-owned file): one
   row per video with a real recording date, a publish date, the bucket, the lane, the guest, Status, a System
   ID; the `Window:` line says what is mapped. **The section absent** (a Brain that predates it) → the Game
   Plan doc's first-90-days calendar (`🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` in `03 · Content/Long-Form/`,
   newest is current; its table: Week of · Video · Kind · Guest). Nothing is said to the member about the missing
   file — `yt-gameplan` creates it with its next write.
2. **The anchors** in `identity/channel.md` → `## Game Plan anchors`: `Cadence:` (`1/week` — the default for the
   first month — or `2/week`, with its `since` date) and `Cycle position:` (where the member is on the 3-1-4 cycle —
   the first row to card is the row at that position); `## The CTA line` — the kit's two spoken lines for the
   Resource Assets cell.
3. **`memory/content-log.md`** — a title already `Scripted` / `Recorded` / `Published` is past the window's start:
   never re-card it; the window begins at the first calendar row with no row in the log (or an `Idea` row only).
4. **`memory/interview-pipeline.md`** — the guest for each interview slot (Stage `Candidate` / `Invited` / `Booked`
   / `Recorded`), their working title, their Recording date when booked.
5. **`identity/operations.md` → `Filming window:`** — the member's filming day and time (the Short-Form Game Plan
   writes it when the batch day is set; `not set yet` is a real answer — the plan then dated its rows on Saturdays).
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
- **At one a week (the default for the first month):** 4–5 rows in a full window — the eight run niche · interview
  · niche · model · interview · niche · interview · interview, so the first month is niche · interview · niche ·
  model and the fifth row, when the window holds it, is an interview. **Right after setup the count is often three
  or four**, because the first video is at least three days out (up to two weeks when no filming day is on file) —
  say the count that was read back, never a fixed number. **At two a week (the step-up):**
  8–9 rows (two per week, in the calendar's order within the week — niche first, as the plan wrote it). When the
  cadence anchor changes, the next top-up re-counts the window at the new pace; un-started cards are re-dated from
  the calendar's re-dated rows.
- **Interview slots count** — the 3-1-4 ratio is inside the cadence, never on top of it. A slot whose guest is
  `Booked` with a Recording date → that date wins (even if it sits outside the week's filming day). A slot at
  `Candidate` / `Invited` → card it as the plan wrote it, Guest = the named candidate, the Context's second line
  `• Invite: [guest] — not yet confirmed`. A slot with no candidate at all → Topic **"Book your next agent
  interview"** (a plain sentence — never a bracket tag in a title), Guest empty, so the week is never a blank; the
  Monday Kickoff turns it into the invite draft and renames the card to the hook-and-transformation title once a
  guest is named.
- **The channel trailer** (a new channel only): it is **week one's first row** — the plan writes it there — and a
  card like any other: Topic "My channel trailer", Format `Long-Form`, the Pillar cell left empty (the spec's
  options are never extended) with `• Pillar: Authority` as the Context's first line, its own Recording and
  Publishing dates. It is not one of the eight; setup's first-video line names it when it is first.
- **Batching** (two interviews recorded in one sitting, published on the plan): the Recording Dates share the
  sitting; the Publishing Dates keep the plan's weeks.
- When the plan runs short (fewer rows left than the window needs), card what exists and say so: *"your plan has
  [n] videos left — say 'refresh my attraction game plan' when you want the next 90 mapped."*

## 3. The card (the spec's vocabulary, exactly)
| Field | What goes in |
|---|---|
| **Topic** | the exact title from the plan as a plain sentence a person would say — sentence case, under twelve words; never a System ID, a bracket tag, a file name, a date or ALL CAPS (the member can refine it later — the System ID column keeps the card findable) |
| **Format** | `Long-Form` |
| **Status** | `Idea` (the Monday Kickoff moves this week's to `Scripted` when it drafts it; filmed → `Recorded`; edited and waiting to go out → `Ready to Post`; live → `Published`) |
| **Pillar** | the lane name — `Niche: Problem` · `Niche: Situation` · `Niche: Future` · `Interview` · `Model` — never an OS pillar name here |
| **Guest** | interviews only — the guest's name from the pipeline (or the candidate to invite) |
| **Context** | `• Pillar: Authority` (niche lanes; `· Story angle` noted for a Why I Switched) / `• Pillar: Proof` (Interview) / `• Pillar: Perspective` (Model) first; then `• What: …` and `• Outcome: …` from this title's line in the plan's TITLE NOTES (the Brain's copy of the plan), ≤12 words a bullet |
| **Recording Date** | the calendar row's own Recording date (the plan's first-date rule: never the day the plan was built — the first video is at least three days out); a `Booked` interview → its Recording date |
| **Publishing Date** | the calendar row's own Publish date — two days after recording by the plan's rule; never earlier than recording |
| **Resource Assets** | the two CTAs, copied from the Week 3 Kit's chapter 7 CALLS TO ACTION table as `channel.md → ## The CTA line` holds them: the guide ask (*"… Comment GUIDE and I'll send it."* · the guide's title · its funnel URL — description line 2 and the pinned comment) · the call line in the CTA law's shape for the register (join: *"If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*; open: *"I'll walk you through it, free, no strings."* · the booking link — description line 1) · the two words from `publishing.md → Keyword:`; always copied from `channel.md → ## The CTA line` (with no kit, setup built the two lines there, labeled "(from your Brain — your kit's wording replaces it)"); `identity/content-pillars.md`'s two CTAs line only when that block is empty. Never the brokerage as the reason; nothing that promises the member's time per partner |
| **System ID** | the calendar row's own (`yt-YYYY-MM-w[n][a/b]` — the plan's week and slot, `yt-2026-11-w2a`); a fresh one only when the row has none, written back to the row; never changed after; never in the title |
| **Reference Video** | the clean watch link of ONE real YouTube video close to this card's idea — the row's `Reference video` cell, or found now (§3a) — `https://www.youtube.com/watch?v=[id]`, nothing else in the cell; empty only when two searches found nothing that passed the check |
| **References** | the one-line note for that video: `[its real title] — [channel] · [closest match / close, not exact / for the format]` (`yt-make-video` later writes the three here) |
| **Script · SEO** | empty at seed — the Monday Kickoff and `yt-make-video` fill them (real links only) |
Card icon 🎬. **The card page at seed holds 🎯 THE HOOK, 📚 REFERENCE VIDEO — WATCH THIS FIRST and 📋 ASSETS & NOTES only** (the spec's locked long-form
layout — 🎯 THE HOOK · 🎬 SCRIPT · 🖼 THUMBNAIL BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE · 📚 REFERENCE VIDEO — WATCH THIS
FIRST · 🎙 GUEST · 📋 ASSETS & NOTES · ✅ PUBLISH IT · 📊 AFTER IT'S OUT; the same order on every card, a section replaced in place,
never stacked): 🎯 the working hook from the plan's title promise, one line, labeled *"working — your Monday Kickoff
writes it three ways"*; 📚 the reference video exactly as the spec lays it out — the titled link (`▶ [the video's
real title](link) — [channel]`), the video playable on the card (`<video source="[link]">Watch this before you plan
yours.</video>`; a player the connection refuses is skipped silently), **Why this one** (the honest label, in a
sentence) and **Watch for** (how it opens · where it asks for something · what it leaves out that you would say) —
or, when nothing was found, the one plain line with YouTube's own search for the topic; 📋 the brief, in plain words — the lane · who it is for · the pain · why it is on your plan ·
the filming date · your two calls to action · the compliance line to say. The Monday Kickoff fills the rest; the Monthly Channel Review and the on-demand
video reads write 📊 AFTER IT'S OUT; `yt-make-video` completes the card before filming.

### 3a. The reference video — found and checked before the card is created (the owner, 2026-11-15)
Every card carries one real YouTube video, as close as possible to its idea, so the member watches a realistic
example before planning their own. The steps are ONE place — `${CLAUDE_PLUGIN_ROOT}/skills/yt-research/references/research-method.md`
→ "The reference video — ONE real video for every card" — follow them exactly; this is only who runs them and when:
- **Before a card is created, read the row's `Reference video` cell** (the last cell of the row in
  `memory/content-calendar.md → ## Long-form (YouTube)`; a row written before 2026-11-15 has no such cell — read as
  empty). **Filled** → use it. **Empty** → run the steps now: a candidate the plan already saw (`Seen on YouTube:` on
  the title's line in the plan's TITLE NOTES) first; otherwise ONE search limited to youtube.com, a second, reworded,
  only when the first gave no candidate; at most three "is it real" checks a card. Write the cell on the row, then
  create the card with it.
- **The budget, stated once:** one search a card (two at most), three checks a card; setup's board step covers the
  cards it creates (three to five). Say one plain progress line while it runs — *"Finding one real video to watch
  first for each of them…"* — and nothing per card.
- **Honest numbers:** no view count and no date unless they were really seen (`Live data: active` on file, the
  tools in the session, and the member in the chat → the data engine's recipe 4; never in a scheduled run). Not
  connected → title and channel only, silently; never ask the member to connect here. **Inside the setup sitting:
  always the search path, even when live numbers are active** (setup never calls that connection).
- **Nothing found** → the `Reference Video` field stays empty, the card page carries the plain line and YouTube's
  own search link, the row's cell stays empty, and the next Monday Kickoff looks again. Never a made-up link.
- **A demo Brain** gets real reference videos too (one search a card, the same check); everything else in a demo
  stays illustrative.
- **An older board** (made before 2026-11-15) has no `Reference Video` column: the first time this skill touches it,
  add the column, add it to the 🎬 YouTube tab's shown columns and re-apply the page layout — the spec's build recipe
  holds the exact statements — once, silently; then fill the cards still at `Idea` or `Scripted`, at most five a run.

## 4. Find-first, count-check, say so
- Before creating any card: System ID → exact title → near match (the spec's two-way sync). Found → update, never a
  twin.
- **The carded test — how a run tells "never carded" from "the member took it off the board".** Every run that
  creates long-form cards records them in the Brain: one dated block appended under `memory/content-calendar.md →
  ## Kickoff briefs (YouTube)` holding the line `carded: [the System ID of each card created]` (the board step at
  setup, "update my attraction video board", and `yt-make-video` when it creates a card or tops up at publish write
  a short block of their own — `Board — YYYY-MM-DD · carded: …`; the Monday Kickoff adds the line to its own
  block, whose first line is `Kickoff — YYYY-MM-DD · [title]`). **A row with no card:** its System ID is in an earlier
  `carded:` line → the member removed that card — it stays off the board, nothing is re-created, and it is said
  once (*"skipping [title] — you took it off the board"*; in a Kickoff, inside the note's bracketed notice). Never
  listed → the card was never made: create it now, with the row's own System ID. A Brain with no `carded:` line at
  all (a board built before 2026-11-15) → treat a missing card inside the 30 days as never carded, once, and start
  the record with this run.
- After the batch: count the cards in the window and say it plainly — *"your next 30 days — [n] videos, [n] of them
  interviews — are on your board, under the YouTube tab at the top."* Then the one statement about the reference
  videos, by what is true: every card has one → *"Each video on your board has one real video to watch first — found on YouTube and checked."* · some have none → *"[n] of your [m] videos have one real video to
  watch first; for the others I put YouTube's own search on the card."* A failed write is named and retried once;
  never silent; never a count you did not read back.
- Never a card without a date; never the whole 90 days; never a loose idea; never a tag or an id in a title.

## 5. The rolling rule — who tops it up, when
- **The Monday Kickoff** (every run, scheduled or on demand): after drafting this week's video, re-count the window
  from today at the cadence anchor; pull the next calendar row(s) until 30 days are visible — each new card with its
  reference video (§3a; a scheduled run uses the web search and the check only, never the live data connection); one line in its note,
  in this wording — the same in every file: `🗓 BOARD: your next 30 days are on your board ({n} videos)`.
- **`yt-make-video` at publish** and **"update my attraction video board"**: the same count and pull.
- **A plan refresh** (`yt-gameplan` on "refresh my attraction game plan") or **a cadence change** ("change my
  YouTube cadence" — the step-up to two a week, or back to one): the new calendar's rows replace un-started `Idea` rows and
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
"your next 30 days", "your board", "the tabs at the top of your board", "the YouTube tab", "filming date", "your
interview slot" — never "window", "System ID", "properties", "views", "database", "the spec". If they ask what the
small tag in the side column is: *"that's how I find your card even if you rename it — just leave it be."*
