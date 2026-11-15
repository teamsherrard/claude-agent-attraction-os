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
   newest is current; `Week · Video · exact title · bucket (· guest)`) and one line that "upgrade my attraction
   brain" adds the calendar to the Brain.
2. **The anchors** in `identity/channel.md` → `## Game Plan anchors`: `Cadence:` (`1/week` — the default for the
   first month — or `2/week`, with its `since` date) and `Cycle position:` (where the member is on the 3-1-4 cycle —
   the first row to card is the row at that position); `## The CTA line` — the kit's two spoken lines for the
   Resource Assets cell.
3. **`memory/content-log.md`** — a title already `Scripted` / `Recorded` / `Published` is past the window's start:
   never re-card it; the window begins at the first calendar row with no row in the log (or an `Idea` row only).
4. **`memory/interview-pipeline.md`** — the guest for each interview slot (Stage `Candidate` / `Invited` / `Booked`
   / `Recorded`), their working title, their Recording date when booked.
5. **`identity/operations.md` → `Filming window:`** — the member's filming day and time (the Short-Form Game Plan
   writes it when the batch day is set; `not set yet` is a real answer). `identity/publishing.md → Keyword:` — the
   two words (GUIDE · the offer's word); `memory/magnets.md → ## Current magnet` — the guide's title and funnel URL.
The member's own board edits win on dates and forward status moves (the spec's conflict rule) — read the board
before writing to it.

## 2. Which rows fall inside 30 days
- **Week math:** the plan's `Week n` is relative to the plan date (the anchors' `Plan date:`) — Week 1 starts the
  Monday on or after it. The window = today through today + 30 days. A row is in the window when its planned
  week's filming day falls inside it.
- **At one a week (the default for the first month):** 4–5 rows (five when a fifth filming day lands inside the 30
  days) — in the first month, niche · interview · niche · model (· the next niche). **At two a week (the step-up):**
  8–9 rows (two per week, in the calendar's order within the week — niche first, as the plan wrote it). When the
  cadence anchor changes, the next top-up re-counts the window at the new pace; un-started cards are re-dated from
  the calendar's re-dated rows.
- **Interview slots count** — the 3-1-4 ratio is inside the cadence, never on top of it. A slot whose guest is
  `Booked` with a Recording date → that date wins (even if it sits outside the week's filming day). A slot at
  `Candidate` / `Invited` → card it as the plan wrote it, Guest = the named candidate, the Context's second line
  `• Invite: [guest] — not yet confirmed`. A slot with no candidate at all → Topic **"Book this cycle's agent
  interview"** (a plain sentence — never a bracket tag in a title), Guest empty, so the week is never a blank; the
  Monday Kickoff turns it into the invite draft and renames the card to the hook-and-transformation title once a
  guest is named.
- **The channel trailer** (a new channel, Week 1 of the plan) is a card like any other.
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
| **Context** | `• Pillar: Authority` (niche lanes; `· Story angle` noted for a Why I Switched) / `• Pillar: Proof` (Interview) / `• Pillar: Perspective` (Model) first; then `• What: …` and `• Outcome: …` from the plan's FOR · PAIN · SIGNAL note, ≤12 words a bullet |
| **Recording Date** | that week's filming day (`Filming window:`); `not set yet` → the week's Monday; a `Booked` interview → its Recording date |
| **Publishing Date** | the plan's publish day for that week; default Recording Date + 2 days; never earlier than recording |
| **Resource Assets** | the two CTAs, copied from the Week 3 Kit's chapter 7 CALLS TO ACTION table as `channel.md → ## The CTA line` holds them: the guide ask (*"… Comment GUIDE and I'll send it."* · the guide's title · its funnel URL — description line 2 and the pinned comment) · the call line in the CTA law's shape for the register (join: *"If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*; open: *"I'll walk you through it, free, no strings."* · the booking link — description line 1) · the two words from `publishing.md → Keyword:`; no kit → `identity/content-pillars.md`'s two CTAs line, labeled "(from your Brain — your kit's wording replaces it)". Never the brokerage as the reason; nothing that promises the member's time per partner |
| **System ID** | the calendar row's own (`yt-YYYY-MM-w[n][a/b]` — the plan's week and slot, `yt-2026-11-w2a`); a fresh one only when the row has none, written back to the row; never changed after; never in the title |
| **References · Script · SEO** | empty at seed — the Monday Kickoff and `yt-make-video` fill them (real links only) |
Card icon 🎬. **The card page at seed holds 🎯 THE HOOK and 📋 ASSETS & NOTES only** (the spec's locked long-form
layout — 🎯 THE HOOK · 🎬 SCRIPT · 🖼 THUMBNAIL BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE · 📚 REFERENCES — WATCH THESE 3
FIRST · 🎙 GUEST · 📋 ASSETS & NOTES · 📊 AFTER IT'S OUT; the same order on every card, a section replaced in place,
never stacked): 🎯 the working hook from the plan's title promise, one line, labeled *"working — your Monday Kickoff
writes it three ways"*; 📋 the brief — bucket · who it is for · the pain · the signal · the filming date · the two
CTAs · the compliance line to say. The Monday Kickoff fills the rest; the Monthly Channel Review and the on-demand
video reads write 📊 AFTER IT'S OUT; `yt-make-video` completes the card before filming.

## 4. Find-first, count-check, say so
- Before creating any card: System ID → exact title → near match (the spec's two-way sync). Found → update, never a
  twin. A card the member deleted stays deleted (note it once: *"skipping [title] — you took it off the board"*).
- After the batch: count the cards in the window and say it plainly — *"your next 30 days — [n] videos, [n] of them
  interviews — are on your board, under the YouTube tab at the top."* A failed write is named and retried once; never
  silent;
  never a count you did not read back.
- Never a card without a date; never the whole 90 days; never a loose idea; never a tag or an id in a title.

## 5. The rolling rule — who tops it up, when
- **The Monday Kickoff** (every run, scheduled or on demand): after drafting this week's video, re-count the window
  from today at the cadence anchor; pull the next calendar row(s) until 30 days are visible; one line in its note:
  `🗓 BOARD: next 30 days topped up ([n] cards)`.
- **`yt-make-video` at publish** and **"update my attraction video board"**: the same count and pull.
- **A plan refresh** (`yt-gameplan` on "refresh my attraction game plan") or **a cadence change** ("change my
  cadence" — the step-up to two a week, or back to one): the new calendar's rows replace un-started `Idea` rows and
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
