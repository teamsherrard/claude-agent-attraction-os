# The 30-day mapping — how the Game Plan calendar becomes dated cards (and stays 30 days ahead)

The rule this plugin adds on top of the shared board spec (`${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`,
byte-identical with the Short-Form System's copy and never edited here): **the board carries the next 30 days
of planned long-form videos, dated, at the member's cadence — never more, never less, never an undated card.**
The 90-day backlog lives in the Game Plan doc; the Brain holds the anchors (cycle position) and the content log.
Read by `yt-board` (Step 3), the Monday Kickoff (`yt-briefing`, the top-up), and `yt-make-video` (the top-up at
publish).

## 1. The source, in order
1. **The Game Plan's dated calendar in the Brain** — `memory/content-calendar.md → ## Long-form (YouTube)`
   (written by `yt-gameplan` at anchor time; the section this plugin owns inside the Short-Form-owned file): one
   row per video with a real recording date, a publish date, the bucket, the lane, the guest, Status, a System
   ID; the `Window:` line says what is mapped. **The section absent** (a Brain that predates it) → the Game
   Plan doc's first-90-days calendar (`🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` in `03 · Content/Long-Form/`,
   newest is current; `Week · Video · exact title · bucket (· guest)`) and one line that "upgrade my attraction
   brain" adds the calendar to the Brain.
2. **The anchors** in `identity/channel.md` → `## Game Plan anchors`: `Cadence:` (1 or 2 a week) and
   `Cycle position:` (where the member is on the 3-1-4 cycle — the first row to card is the row at that position).
3. **`memory/content-log.md`** — a title already `Scripted` / `Recorded` / `Published` is past the window's start:
   never re-card it; the window begins at the first calendar row with no row in the log (or an `Idea` row only).
4. **`memory/interview-pipeline.md`** — the guest for each interview slot (Stage `Candidate` / `Invited` / `Booked`
   / `Recorded`), their working title, their Recording date when booked.
5. **`identity/operations.md` → `Filming window:`** — the member's filming day and time (Stop 16 of the Brain's
   setup writes it; `not set yet` is a real answer).
The member's own board edits win on dates and forward status moves (the spec's conflict rule) — read the board
before writing to it.

## 2. Which rows fall inside 30 days
- **Week math:** the plan's `Week n` is relative to the plan date (the anchors' `Plan date:`) — Week 1 starts the
  Monday on or after it. The window = today through today + 30 days. A row is in the window when its planned
  week's filming day falls inside it.
- **At 1 a week:** 4–5 rows (five when a fifth filming day lands inside the 30 days). **At 2 a week:** 8–9 rows
  (two per week, in the calendar's order within the week — niche first, as the plan wrote it).
- **Interview slots count** — the 3-1-4 ratio is inside the cadence, never on top of it. A slot whose guest is
  `Booked` with a Recording date → that date wins (even if it sits outside the week's filming day). A slot at
  `Candidate` / `Invited` → card it as the plan wrote it, Guest = the named candidate, the Context's second line
  `• Invite: [guest] — not yet confirmed`. A slot with no candidate at all → `[Interview] invite [the next
  candidate from the pipeline or the plan's guest list]`, so the week is never a blank; the Monday Kickoff turns
  it into the invite draft.
- **The channel trailer** (a new channel, Week 1 of the plan) is a card like any other.
- **Batching** (two interviews recorded in one sitting, published on the plan): the Recording Dates share the
  sitting; the Publishing Dates keep the plan's weeks.
- When the plan runs short (fewer rows left than the window needs), card what exists and say so: *"your plan has
  [n] videos left — say 'refresh my attraction game plan' when you want the next 90 mapped."*

## 3. The card (the spec's vocabulary, exactly)
| Field | What goes in |
|---|---|
| **Topic** | the exact title from the plan (the member can refine it later — the System ID keeps the card findable) |
| **Format** | `Long-Form` |
| **Status** | `Idea` (the Monday Kickoff moves this week's to `Scripted` when it drafts it) |
| **Pillar** | the lane name — `Niche: Problem` · `Niche: Situation` · `Niche: Future` · `Interview` · `Model` — never an OS pillar name here |
| **Guest** | interviews only — the guest's name from the pipeline (or the candidate to invite) |
| **Context** | `• Pillar: Authority` (niche lanes; `· Story angle` noted for a Why I Switched) / `• Pillar: Proof` (Interview) / `• Pillar: Perspective` (Model) first; then `• What: …` and `• Outcome: …` from the plan's FOR · PAIN · SIGNAL note, ≤12 words a bullet |
| **Recording Date** | that week's filming day (`Filming window:`); `not set yet` → the week's Monday; a `Booked` interview → its Recording date |
| **Publishing Date** | the plan's publish day for that week; default Recording Date + 2 days; never earlier than recording |
| **Resource Assets** | the two CTAs: the book-a-call line (`identity/content-pillars.md`'s line 1) · the keyword (`identity/publishing.md → Keyword:` first, `content-pillars.md`'s CTA line second) · the live resource's name (`memory/magnets.md → ## Current magnet`) |
| **System ID** | the calendar row's own (`yt-YYYY-MM-w[n][a/b]` — the plan's week and slot, `yt-2026-11-w2a`); a fresh one only when the row has none, written back to the row; never changed after |
| **References · Script · SEO** | empty at seed — `yt-make-video` fills them (real links only) |
Card icon 🎬. The row's page body stays empty at seed; the Monday Kickoff and `yt-make-video` write the sections.

## 4. Find-first, count-check, say so
- Before creating any card: System ID → exact title → near match (the spec's two-way sync). Found → update, never a
  twin. A card the member deleted stays deleted (note it once: *"skipping [title] — you took it off the board"*).
- After the batch: count the cards in the window and say it plainly — *"your next 30 days — 5 videos, 2 of them
  interviews — are on the board ✓"*. A failed write is named and retried once; never silent.
- Never a card without a date; never the whole 90 days; never a loose idea.

## 5. The rolling rule — who tops it up, when
- **The Monday Kickoff** (every run, scheduled or on demand): after drafting this week's video, re-count the window
  from today; pull the next calendar row(s) until 30 days are visible; one line in its note: `🗓 BOARD: next 30
  days topped up ([n] cards)`.
- **`yt-make-video` at publish** and **"update my attraction video board"**: the same count and pull.
- **A plan refresh** (`yt-gameplan` on "refresh my attraction game plan"): the new calendar's rows replace
  un-started `Idea` rows and cards inside the window only when the titles changed; `Scripted` and later rows and
  cards are never touched; the member hears one line about what moved.
- **Status, one truth:** a row's Status in the Brain's calendar and its card's Status on the board move together —
  the Monday Kickoff flips both to `Scripted`, `yt-make-video` to `Recorded` and `Published`; a row is never
  deleted (a dropped video is `Status: dropped`, its card removed only by the member).
- Without a board (Notion not connected or declined): nothing here runs; the Game Plan calendar is the window
  and the Monday Kickoff drafts straight from it.

## 6. Plain words (what the member hears)
"your next 30 days", "your board", "filming date", "your interview slot" — never "window", "System ID",
"properties", "the spec". If they ask what the small tag is: *"that's how I find your card even if you rename
it — just leave it be."*
