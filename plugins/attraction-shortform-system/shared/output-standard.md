# Output Standard — saving content to the workspace, organized + cleanly formatted

Every document the Short-Form System creates lands in the member's own workspace (Google Drive or OneDrive), in
the Brain's folder map, with a consistent name, and formatted so it looks genuinely good. This file is the
standard. When a skill says "save to the workspace (output standard)," it means this.

Two non-negotiables: **(1) it goes to the right folder with the right name; (2) it's clean and scannable — never a
wall of text.**

---

## 1. Where it goes — the Brain's drive map, never a parallel root

The workspace is `Agent Attraction OS/` (renameable — **always located by the `Workspace ID` in
`~/attraction-brain/config.md`, then the `_attraction-workspace.md` marker, never by name**). The Brain plugin
built the six folders at setup; this plugin only creates month sub-folders inside them. Never create a
`[Member] — Short-Form System/` root — that is the seam the audit found.

```
Agent Attraction OS/
└── 03 · Content/                                               (no bios document — the bios live in the kit and the Brain)
      ├── Short-Form/
      │     ├── Taylor's Short-Form Game Plan — 2026-11-17            (Doc — from sf-gameplan; the bucket root, dated, newest is current)
      │     ├── 2026-11 · November/                            (month folder — create as needed)
      │     │     ├── 2026-11-18 · Reel · The Year I Almost Quit        (Doc — a talking-head script)
      │     │     ├── 2026-11-18 · Reels · Week 1 Batch                 (Doc — a batch of scripts)
      │     │     ├── 2026-11-23 · Week Plan                            (Doc — the Monday Week Plan's drafts)
      │     │     ├── 2026-11 · 30-Day Calendar                         (Doc — a calendar-only refresh; the calendar itself is the Game Plan's section 6)
      │     │     ├── 2026-11-19 · Green Screen · Brokerage Fee Change  (Doc)
      │     │     ├── 2026-11-19 · Green Screen · News Watch            (Doc — the Wednesday news watch, sf-greenscreen)
      │     │     ├── 2026-11-18 · ManyChat Build Sheet                 (Doc — sf-comment-to-dm; followed in the member's own ManyChat)
      │     │     └── 2026-11-19 · Stories · Tuesday Set                (Doc)
      │     └── Performance/
      │           ├── 2026-11-01–14 · Performance Review               (Doc — sf-analytics, the on-demand read when a doc is asked for)
      │           └── 2026-11-30 · Short-Form Deep Dive                (Doc — sf-analytics, monthly)
      └── Graphics/
            └── 2026-11 · November/
                  └── 2026-11-20 · Carousel · Why I Left               (Doc — the spec aa-content-design reads)
```

**Beside the Drive doc — the Brain's `exports/`.** The texts the Brain Board shows are also kept at
`~/attraction-brain/exports/` (the Brain syncs `exports/*.txt`; the board is re-rendered from them on every push):
the Game Plan as `short-form-game-plan-YYYY-MM-DD.txt` (`sf-gameplan`), each Week Plan as `week-plan-YYYY-MM-DD.txt`
(`sf-week-plan`), each performance read ("how's my content doing") as `short-form-performance-YYYY-MM-DD.txt`
(`sf-analytics`), the keyword sheet as `keyword-sheet-YYYY-MM-DD.txt` and the ManyChat build sheet as
`manychat-build-sheet-YYYY-MM-DD.txt` (`sf-comment-to-dm`), each news watch as `news-watch-YYYY-MM-DD.txt`
(`sf-greenscreen`).
Written in the same run as the doc, then pushed; never instead of the doc. Read, never written: `week3-kit-*.txt`.

Don't pre-create empty month folders — create the current month's folder the first time you save into it.
Storage-agnostic: the same map on Google Drive or OneDrive (`shared/connectors.md` in the Brain plugin maps
"the storage connector" to the real one; never tell a Microsoft member that Google Drive is required).

## 2. Naming convention (use everywhere — no exceptions)

| Thing | Pattern | Example |
|---|---|---|
| Month folder | `YYYY-MM · Month` | `2026-11 · November` |
| The Short-Form Game Plan (the bucket root, not a month folder) | `[Name]'s Short-Form Game Plan — YYYY-MM-DD` (demo: `… — DEMO — YYYY-MM-DD`) | `Taylor's Short-Form Game Plan — 2026-11-17` |
| Single Reel script | `YYYY-MM-DD · Reel · [Short Topic]` | `2026-11-18 · Reel · The Year I Almost Quit` |
| Batch of scripts | `YYYY-MM-DD · Reels · [Batch name]` | `2026-11-18 · Reels · Week 1 Batch` |
| Week plan (the Monday workflow) | `YYYY-MM-DD · Week Plan` | `2026-11-23 · Week Plan` |
| 30-day calendar (a calendar-only refresh; otherwise section 6 of the Game Plan) | `YYYY-MM · 30-Day Calendar` | `2026-11 · 30-Day Calendar` |
| Green screen | `YYYY-MM-DD · Green Screen · [Short Topic]` | `2026-11-19 · Green Screen · Brokerage Fee Change` |
| News watch (the Wednesday workflow — three to six cited headlines with a take each) | `YYYY-MM-DD · Green Screen · News Watch` | `2026-11-19 · Green Screen · News Watch` |
| Story set | `YYYY-MM-DD · Stories · [Day / theme]` | `2026-11-19 · Stories · Tuesday Set` |
| Carousel / LinkedIn doc (a lean build sheet) | `YYYY-MM-DD · Carousel · [Short Topic]` | `2026-11-20 · Carousel · Why I Left` |
| Performance doc (the on-demand read, when a doc is asked for) | `YYYY-MM-DD–DD · Performance Review` | `2026-11-01–14 · Performance Review` |
| Deep dive | `YYYY-MM-DD · Short-Form Deep Dive` | `2026-11-30 · Short-Form Deep Dive` |
| Weekly ideas + hook bank | `YYYY-MM-DD · Attraction Ideas + Hook Bank` | `2026-11-17 · Attraction Ideas + Hook Bank` |
| Weekly routine | `YYYY-MM-DD · Weekly Routine` | `2026-11-17 · Weekly Routine` |
| Keyword sheet + DM bank (the CTA bank is its first page) | `YYYY-MM-DD · Keyword Sheet + DM Bank` | `2026-11-18 · Keyword Sheet + DM Bank` |
| ManyChat build sheet (`sf-comment-to-dm` — followed in the member's own ManyChat account; no connector in Cowork) | `YYYY-MM-DD · ManyChat Build Sheet` | `2026-11-18 · ManyChat Build Sheet` |
| Film-day plan | `YYYY-MM-DD · Film-Day Plan` | `2026-11-18 · Film-Day Plan` |
| Publishing queue | `YYYY-MM-DD · Publishing Queue` | `2026-11-24 · Publishing Queue` |
| Brain export — the Game Plan's text (`sf-gameplan`) | `exports/short-form-game-plan-YYYY-MM-DD.txt` | `exports/short-form-game-plan-2026-11-17.txt` |
| Brain export — a Week Plan's text (`sf-week-plan`) | `exports/week-plan-YYYY-MM-DD.txt` | `exports/week-plan-2026-11-23.txt` |
| Brain export — a performance read's text ("how's my content doing", `sf-analytics`) | `exports/short-form-performance-YYYY-MM-DD.txt` | `exports/short-form-performance-2026-11-21.txt` |
| Brain export — the keyword sheet's text (`sf-comment-to-dm`) | `exports/keyword-sheet-YYYY-MM-DD.txt` | `exports/keyword-sheet-2026-11-18.txt` |
| Brain export — the ManyChat build sheet's text (`sf-comment-to-dm`) | `exports/manychat-build-sheet-YYYY-MM-DD.txt` | `exports/manychat-build-sheet-2026-11-18.txt` |
| Brain export — a news watch's text (`sf-greenscreen`) | `exports/news-watch-YYYY-MM-DD.txt` | `exports/news-watch-2026-11-19.txt` |

Everything in the Short-Form bucket except the Game Plan and the performance documents lives in the month folder
(`03 · Content/Short-Form/[YYYY-MM · Month]/`); the Game Plan lives at the bucket root (dated, newest is current);
the performance review and the deep dive live in `03 · Content/Short-Form/Performance/` (no month folder).

Topic = 3–6 plain words (Title Case), no punctuation soup. Dates are ISO (`YYYY-MM-DD`) so files sort on their
own. **Dated filenames; the newest is current** — the storage connectors are create-only, so a regenerated doc
is a new dated file and the older one may be trashed after a verified upload (never a snapshot).

## 3. How to create folders + docs (the storage connector)
- **Folder:** create a folder with the right parent (the bucket's folder inside the workspace found by ID);
  capture the returned id to use as the parent for what goes inside it.
- **Document:** write the structured text to a temp file in the scratchpad, render it to a styled `.docx`, and
  upload that:
  `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" <scratchpad>/doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Member · Organization]"`,
  then upload the resulting **`.docx`**. The structured text is only the renderer's input.
- Find-or-create: before creating a folder, list the parent and reuse the folder if it already exists — never
  make duplicate "November" folders.
- **Microsoft members:** if `config.md` says `READ-ONLY (org-gated)`, say the save is not possible in one plain
  line, keep the content in chat, and offer the Brain's rescue path — never fail silently.

## 4. Formatting — the renderer makes it a clean, formatted `.docx`

The skill writes the **structured text** below; the shared renderer (`render_doc.py`) turns it into a clean Word
doc — real headings, bullet lists, light-grey rules — in **one neutral house style** (Arial, pure-black text, no
colour, no per-member branding). *If its dependency (`python-docx`) is unavailable, build the same `.docx` with the
docx skill, matching that look — never tell the member to install anything, never stop to install it yourself.*

Write the structured text like this, every time:
- **Title line** at the top, then a light **meta line** (member · organization · date). Then a blank line.
- **Section headers in ALL CAPS**, each preceded by a divider line of em dashes
  (`———————————————————————————————`) and followed by a blank line.
- **Generous blank-line spacing** between blocks. Never run sections together.
- **Bullets** with `•`; sub-points or steps with `—`. One point per line.
- **Cues, hooks, and labels on their own lines** (e.g. `HOOK (read word-for-word)` then the hook on the next
  line). Scripts and captions never run together as a paragraph blob.
- **Copy blocks the member will paste** (captions, hashtags, bios) sit under a clear label.
- **No** Markdown symbols (`#`, `**`, backticks) or emoji walls in the body — the renderer applies the formatting
  from the structure (caps headers, dividers, `•` bullets, `Label:` lead-ins).

(Visual *brand design* is the Design Studio's job — these are clean working documents.)

## 5. The canonical document skeleton
Every content doc follows this shape (fill with what the workflow already produced for chat):

```
[FORMAT] · [TOPIC]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE BRIEF
Pillar: [Authority / Perspective / Story / Proof / Personality]
For: [the agent avatar, one line]   ·   Story used: [hook or none]
CTA rung: [Follow / Comment / DM / Resource / Conversation / Call]   ·   Keyword: [GUIDE / the offer's word]   ·   Call line (when the rung is the call): [from the kit's CALLS TO ACTION table, verbatim]

———————————————————————————————
THE CONTENT (hook ×3 + script / talking points / slides / story lines)
...

———————————————————————————————
INSTAGRAM + FACEBOOK
Caption:
...
Hashtags:
...

———————————————————————————————
TIKTOK
Caption (one line, no line breaks):
...

———————————————————————————————
YOUTUBE SHORTS
Title:
...
Description:
...
Tags:
...

———————————————————————————————
COMPLIANCE
[the stamp from compliance.md — brokerage name / license / disclaimer as required; "none required" if so]
```
(Carousel docs are LEAN BUILD SHEETS — §5a has the skeleton: SLIDE 1 … SLIDE N, the caption blocks, the sizes, the brand
pointer and a short THE DESIGN BRIEF FOR AA-CONTENT-DESIGN band; no THE BRIEF band, no strategy in the doc;
story docs use STORY 1 / STORY 2 … with the category, the text overlay, the sticker, and the reply CTA; the
calendar uses WEEK 1 → WEEK 4 tables; performance docs use the review structure from `sf-analytics`' own
reference. Same formatting rules throughout.)

## 5a. The other skeletons (every named document has a shape; a thin one is a fail)
The content skeleton in §5 covers a Reel, a green screen, a carousel, and a story set. The documents below are the
premium set a Week 4 member actually opens and keeps — each has its own bands, and a floor. Same house grammar
(§4). The skill that owns the doc fills every band; an empty band is written as a real line ("none yet", "not
available"), never left blank.

**The Short-Form Game Plan** (`sf-gameplan` — the Week 4 flagship, built inside setup; stamped) — floor: nine
sections at their floors (1 · 150 · 2 · 400 · 3 · 200 · 4 · 250 · 5 · 150 · 6 · 400 · 7 · 100 · 8 · 100 · 9 · 50
words), the six kit posts first then twelve dated calendar rows at the default three a week (twenty at five), five pillars with three
angles each, thirty hooks; ~3,500–5,000 words. Demo mode tags every figure "(illustrative — demo)". **Its text is also
kept at `~/attraction-brain/exports/short-form-game-plan-YYYY-MM-DD.txt`**, then pushed (the Brain Board reads it).
```
[NAME]'S SHORT-FORM GAME PLAN
Attracting: [the primary type] · [the second]  ·  Known for: [niche]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks

———————————————————————————————
READ THIS FIRST
[the opening sentence: where your short-form is today, and the verdict]
Your first two weeks: post the six you already have designed — nothing to film yet.
[two more sentences: the insight · the plan in one line]
First post to film: [the first Reel after the six designed posts — working title · date, written "Tue, Dec 1"]   ·   Batch day: [day]   ·   Compliance: [status — one line if unset]

———————————————————————————————
1. POSITIONING FOR SHORT-FORM
Who I'm talking to: [the agent, their pain in their words, the mirror moment]
The one line: "[Name] helps [agent] [outcome] through [mechanism]"
The job of short form: Awareness → Recognition → Familiarity → Trust → Curiosity → Conversation
The two keywords: GUIDE → the guide (the DM sends it)   ·   [the offer's word] → the one-pager and the invitation to talk
The two CTAs: 1. Book a call — [the booking line, word for word from the kit]   2. The guide — "Comment GUIDE and I'll send you [the guide, in three words]."
Why I'm building this: [the why-line, in their voice]

———————————————————————————————
2. THE FIVE PILLARS — THREE ANGLES EACH
AUTHORITY — what I teach
[two-line summary]
• [hook] · for [agent] · [pain] · built on [a teach / a story / a win]   (×3)
PERSPECTIVE — what I believe · STORY — where I've been · PROOF — what's happening in my world · PERSONALITY — who I am off the clock   (same shape)

———————————————————————————————
3. THE FORMAT MIX AND THE WEEKLY CADENCE
[N] posts a week — three to start, five the step-up · the mix: one attraction · one authority · one story (two · two · one at five), stories every day
Formats: talking head [what for] · green screen [what for] · carousel [what for] · stories [what for]
Platforms: Instagram and Facebook, both — every Reel and every graphic; LinkedIn for the carousels when you attract team leaders; TikTok and YouTube Shorts take the same video any time you want more reach
Batch day: [day · the rhythm]   ·   The 15-minute routine: [the moves, the time of day]

———————————————————————————————
4. THE HOOK BANK
THE HOOKS FOR YOUR DATED POSTS
[one line per dated post, in date order: the date, written "Tue, Nov 17" · the hook · who it is for]
MORE HOOKS WHEN YOU NEED THEM
[the rest of the thirty, grouped AUTHORITY · PERSPECTIVE · STORY · PROOF · PERSONALITY — each: the hook · who it is for · the ask in words ("Comment GUIDE" / "Comment [WORD]" / "Follow")]

———————————————————————————————
5. THE TWO CTAs AND THE COMMENT-TO-DM FLOW
The ladder: Follow / save / share → Comment → DM → Resource → Conversation → Call   ·   one post, one ask
| Where it goes | Ask for the guide | Ask for the call |
[the rows — caption, last line · comment keywords · video pop-up · spoken line · end card · story · bio link · DM reply — copied word for word from the kit]
What each kind of post asks for: Authority — "Comment GUIDE" · Perspective — a follow, a save or a share (or "Comment GUIDE") · Story — "Comment GUIDE" or the invitation · Proof — the invitation or "Comment GUIDE" · Personality — "Follow"
The rule: "Comment GUIDE" is the ask on most posts. The invitation — "Comment [WORD]", or your call line — is the ask on about one post in four, most naturally a proof post or a "what you get" post. Never two asks on one post. Your six designed posts keep exactly the asks printed on them.
The two keywords: GUIDE → the guide · [the offer's word] → the one-pager and the invitation   ·   the full keyword sheet: "my keyword sheet"
ManyChat: ManyChat is how your two keywords answer themselves. Set it up this week: install ManyChat (the free plan starts you — upgrade only if ManyChat itself asks you to for Instagram automations), import Mike's templates from your Materials folder, put GUIDE and [WORD] in with your links — your build sheet walks you through it step by step. You don't connect ManyChat to Claude: nothing here needs its connector or a paid plan for it. Until it's live, reply by hand from your DM bank.   ·   the steps: "my ManyChat build sheet"

———————————————————————————————
6. THE 30-DAY CALENDAR   ([date] → [date])
GRAPHICS — THE SIX POSTS YOU ALREADY HAVE   (post, don't make — the Graphics tab on your board; designed in Week 3, waiting in your Offer folder)
| Date | What | The hook | The ask | Status |
[six rows — the guide carousel · five problems, five fixes · my story · what you get · proof · book the call; one every two or three days — Date written "Tue, Nov 17" · What = the format and the working title ("Carousel — The guide") · The hook = the post's first slide or headline · The ask in words, exactly as the kit printed it ("Comment GUIDE" / "Comment [WORD]") · Status Ready to Post]
This week you only post — nothing to film.   [the one line under every week made only of designed posts]
REELS — [n] ROWS AT YOUR CADENCE   (the Reels tab on your board)
| Date | What | The hook | The ask | Status |
[the Reel rows in the same five columns — six at the default three a week, fourteen at five; What = "Reel — [working title]" (or "Green screen — …", "Carousel — …") · The ask in words: "Comment GUIDE", "Comment [WORD]" or "Follow" · no Reel dated earlier than the day after the batch day that films it; the first Reels cover what the six designed posts don't]
STORIES, DAILY: [the four-category rotation · morning / midday / evening]
THE BATCH PLAN: [sessions · what films together · hours]
THE THREE TO FILM FIRST: 1. [the Reel's title, why]  2. [...]  3. [...]

———————————————————————————————
7. WHAT WE MEASURE
Any time you ask "how's my content doing", and each month in your deep dive, five numbers: [people who saw you · Reels posted of the cadence · story days of seven · keyword comments · conversations started] · calls booked from content · the benchmark · where the numbers come from · the compliance line

———————————————————————————————
8. YOUR SCHEDULED WORKFLOWS   (all draft-only — nothing posts, sends, or schedules on its own; each [when · what it produces · on since / stopped])
Switched on: Monday Week Plan (Mondays, 7:00 am) · Batch Prep (the evening before your batch day, 6:00 pm) · Wednesday Brokerage News Watch (Wednesdays, 8:00 am) · Monthly Calendar Refill (the last Friday of the month, 5:00 pm)
There are five more — a keyword follow-up queue, a mid-week nudge, a monthly deep dive, a daily stories prompt and a quarterly profile check — they're there if you want them; say the word any time.
I'll email you a short note at your own address when something's ready.   [or: No mail is connected yet, so your notes stay in Cowork.]

———————————————————————————————
9. NEXT STEPS
1. Post your six designed posts on their dates.
2. Film on your batch day, [day].
3. When it's filmed, open a new chat and say "edit my reel".
4. Set up ManyChat from your build sheet — say "my ManyChat build sheet" and I'll print it.
[then, one line each and only where it applies: compliance not set · ideas built without a fresh search]

———————————————————————————————
SOURCES
[what agents are asking — each search → what was seen · as seen YYYY-MM-DD]   ·   Budget used: [n] of 8   ·   Starter rows: [n]   ·   Unresearched rows: [n]   (demo: "nothing searched")

———————————————————————————————
[closing — one honest paragraph: be consistent, not complicated]
COMPLIANCE
[the stamp]
```

**Member-facing words only in this document.** The Brain file `memory/content-calendar.md` keeps its locked eleven
columns (`# | Date | Day | Format | Pillar | Working title | Hook | CTA | Carries | Status | System ID`); in the document
the calendar is the five columns above, dates are written "Tue, Nov 17" (never 2026-11-17), and none of "rung",
"carries", "branch", "the OS default", "the kit's CALLS TO ACTION table, verbatim" or a System ID appears anywhere.

**The bios have no document** (the owner's ruling, 2026-11-14 — the former profile pack is retired): they live in
chapter 6 of the kit and in `identity/profiles.md`. A bio `sf-setup` refreshes (only when the offer, the proof or the
funnel URL changed) is shown in chat as a copy block under a clear label, written back to `profiles.md` and pushed.

**The Carousel build sheet** (`sf-carousel` → `03 · Content/Graphics/[month]/`, named `YYYY-MM-DD · Carousel · [Short
Topic]`) — a LEAN BUILD SHEET for the Design Studio's content skill (the owner, 2026-11-11): page order + final copy +
placeholders only; ~300–600 words. **Strategy never goes in it** — why this hook, the rung, what to watch, the pillar
it fills go in the chat reply and the content-log row. The band `THE DESIGN BRIEF FOR AA-CONTENT-DESIGN` stays (the
design skill keys on it) and stays short.
```
CAROUSEL · [TOPIC]
[Member Name] · [Organization] · [Date]

———————————————————————————————
SLIDE 1   (the hook, under 12 words)
[final copy]
SLIDE 2 … SLIDE N   (one idea per slide; the last slide the ask — "Comment GUIDE and I'll send it." or the call line from the kit's table)
[final copy, one slide per band]

———————————————————————————————
INSTAGRAM + FACEBOOK
Caption:   [final copy — the last line the ask]
Hashtags:   [3–5]

———————————————————————————————
LINKEDIN   (document post)
Caption:   [final copy]

———————————————————————————————
THE DESIGN BRIEF FOR AA-CONTENT-DESIGN
Sizes:   1080 by 1350 (slides) · 1080 by 1920 (a story crop, if asked)
Brand:   your Design Package brief (02 · Brand) — or the clean neutral look before it exists
Placeholders:   [headshot on slide N] · [screenshot of …] · [the guide cover on the last slide]
Copy:   verbatim from the slides above · the stamp on the last slide or in the caption

———————————————————————————————
COMPLIANCE
[the stamp]
```

**The Week Plan** (the Monday Week Plan, `sf-week-plan`) — floor: every calendar row dated this week drafted
(brief · hook ×3 · script or talking points · bullet version · CTA · captions), the seven-day story set, any
recognition post for a new partner or a win the Brain logged (named or pictured only with the agent's written OK), the
board count; ~900–2,500 words (three posts at the default cadence, five at five). **Its text is also kept at
`~/attraction-brain/exports/week-plan-YYYY-MM-DD.txt`**, then pushed (the Brain Board reads it).
```
WEEK PLAN · [WEEK OF DATE]
[Member Name] · [Organization] · [Monday date]

———————————————————————————————
THE WEEK AT A GLANCE
| Day | Post (working title · pillar · format) | Status | Board |
THE BATCH DAY: [day]

———————————————————————————————
POST 1 — [working title]   (THE BRIEF · THE HOOK — 3 WAYS · THE SCRIPT · THE BULLET VERSION · THE SHOTS · THE CTA · THE CAPTIONS — the §5 content shape)
POST 2 … POST [n]   (three at the default cadence, five at five)

———————————————————————————————
STORIES THIS WEEK   (seven days: what to capture · overlay · sticker · reply CTA)

———————————————————————————————
LEFT FOR YOU   (anything undrafted and why)

———————————————————————————————
COMPLIANCE
```

**The 30-Day Calendar** (section 6 of the Game Plan — `sf-gameplan`; saved on its own only on a calendar-only
refresh) — floor: 12 numbered, dated rows at the default three a week (20 at five), every cell filled, a batch plan with hours;
~800–1,000 words.
```
30-DAY CALENDAR · [MONTH YYYY]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE MONTH AT A GLANCE
[one paragraph: what this month establishes and why this order — the mix in force, the keyword, the batch rhythm]

———————————————————————————————
THE SIX KIT POSTS, THEN THE REELS   (the kit posts carry Story and Proof; the first Reels cover Personality, Perspective and the Authority teach — an agent who finds you this month can answer the five profile questions from the feed)
| Date | What | The hook | The ask | Status |
[the same five member-facing columns as the Game Plan's section 6, dates written "Tue, Nov 17"; "This week you only post — nothing to film." under a week made only of designed posts — six kit rows, then the Reel rows at the cadence — six at the default three a week, fourteen at five; the member's own ideas and this month's objections land in the first two weeks of Reels]

———————————————————————————————
STORIES, DAILY
[the four-category rotation runs every day regardless — one line]

———————————————————————————————
THE BATCH PLAN
Session 1: [day · the Reels that film together · same outfit, same spot · hours]   Session 2: [...]

———————————————————————————————
THE THREE TO FILM FIRST
1. [#, one line why]   2. [...]   3. [...]

———————————————————————————————
COMPLIANCE
[the stamp]
```

**Attraction Ideas + Hook Bank** (`sf-ideas`) — floor: exactly 3 + 15 + 30 at the default three a week (5 + 15 + 30 only when `Cadence:` says five), five to eight cited findings; ~1,200–1,600 words.
```
ATTRACTION IDEAS + HOOK BANK · [WEEK OF DATE]
[Member Name] · [Organization] · [Date]

———————————————————————————————
WHAT AGENTS ARE ASKING RIGHT NOW
1. "[the phrase as an agent typed it]" · HIGH / MEDIUM / EMERGING · [where it was seen · when] · [pillar it feeds]
[five to eight — the citations every idea below points at by number]

———————————————————————————————
THIS WEEK'S THREE   [THIS WEEK'S FIVE only when the cadence is five]
1. [the title the way a person would say it] · [the angle, one line] · [pillar] · [for whom] · [format] · [the ask — GUIDE · the invitation · follow] · [finding #]
[three at the default cadence, on one attraction · one authority · one story — five, on 2 · 2 · 1, only at five a week]

———————————————————————————————
THE BANK   (fifteen more, three per pillar, same columns)
AUTHORITY · PERSPECTIVE · STORY · PROOF · PERSONALITY

———————————————————————————————
THE 30-HOOK BANK   (six per pillar, under 12 words, no two the same shape, never "stop scrolling")
AUTHORITY: 1–6 · PERSPECTIVE: 1–6 · STORY: 1–6 · PROOF: 1–6 · PERSONALITY: 1–6

———————————————————————————————
THE ONES THAT REPEAT   (two or three named weekly series)

———————————————————————————————
WHAT TO SKIP   (three things that read as recruiting — and what to post instead)

———————————————————————————————
COMPLIANCE
```

**Keyword Sheet + DM Bank** (`sf-comment-to-dm`, Job B) — floor: the one-page keyword sheet (two words, what each
opens, the DM each triggers), the CTA bank (15 lines), six messages for each of the two keywords (each under 60
words), the story reply, the qualifier, the paste sheet; ~1,000–1,500 words. **The sheet's text is also kept at
`~/attraction-brain/exports/keyword-sheet-YYYY-MM-DD.txt`**, then pushed.
```
KEYWORD SHEET + DM BANK
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE TWO KEYWORDS   (one page — never a third word)
GUIDE → the guide, instantly (the DM with the download link) · said on camera at the end · the caption's last line · pinned as the first comment
[THE OFFER'S WORD] → the one-pager and the invitation to talk (the call link) · the invitation word, on about one post in four — most naturally a Proof piece or a "what you get" piece
ManyChat: [set up YYYY-MM-DD — Mike's template installed, the build sheet followed / not yet — set it up this week; replying by hand from the DM bank until it's live] — the member's own account; you don't connect ManyChat to Claude

———————————————————————————————
THE CTA BANK   (fifteen lines, three per pillar, each on its rung)
AUTHORITY — GUIDE:   Spoken: [...]   Caption: [...]   (×3)
PERSPECTIVE — follow, save or share (or GUIDE) (×3) · STORY — GUIDE or the invitation (×3) · PROOF — the invitation or GUIDE (×3) · PERSONALITY — follow (×3)
THE RULE: GUIDE is the ask on most posts. The invitation (the offer's own word, or the kit's call line) is the ask on about one post in four — most naturally a Proof piece or a "what you get" piece. A Proof piece may carry the guide instead. Never two asks on one post. The six designed kit posts keep exactly the asks the kit printed.
THE CALL LINE (the call-to-action law's shape — the person · their help · free · to run this; copied from the kit's CALLS TO ACTION table): [...]

———————————————————————————————
THE DM BANK — GUIDE
1. Auto-reply (the guide's link) · 2. The human follow-up · 3. The qualifier (three messages, one at a time) · 4. The bridge to the method · 5. The invite to a call (the law's line) · 6. The graceful no
THE DM BANK — [THE OFFER'S WORD]   (the same six — the one-pager first, the call second)
THE STORY REPLY · THE DM QUALIFIER

———————————————————————————————
THE MANYCHAT BUILD SHEET
[its own document — "YYYY-MM-DD · ManyChat Build Sheet", below; one line here naming it and where it is]

———————————————————————————————
COMPLIANCE
```

**ManyChat Build Sheet** (`sf-comment-to-dm` — `YYYY-MM-DD · ManyChat Build Sheet`; the member follows it in their OWN
ManyChat account this week after installing Mike's template — ManyChat is part of the program and is never connected
to Claude: the plugin writes the sheet and never claims to run it, never says "connected", never "optional"; setup
hands it over inside its Game Plan step and "my ManyChat build sheet" prints it any time) — floor: the owner's opening
line, the two keywords and the story reply, each with trigger · message 1 · button text · message 2 · the tag · the human
follow-up; ~400–700 words. **Its text is also kept at `~/attraction-brain/exports/manychat-build-sheet-YYYY-MM-DD.txt`**,
then pushed.
```
MANYCHAT BUILD SHEET
[Member Name] · [Organization] · [Date]

———————————————————————————————
WHY, IN ONE BREATH
ManyChat is how your two keywords answer themselves. Set it up this week: install ManyChat (the free plan starts you — upgrade only if ManyChat itself asks you to for Instagram automations), import Mike's templates from your Materials folder, put GUIDE and [WORD] in with your links — this sheet walks you through it step by step. You don't connect ManyChat to Claude: nothing here needs its connector or a paid plan for it. Until it's live, reply by hand from your DM bank.

———————————————————————————————
BEFORE YOU START
[Mike's template installed in your ManyChat · your Instagram connected to ManyChat as a Business or Creator account · the guide's download link and the one-pager link to hand]

———————————————————————————————
AUTOMATION 1 — GUIDE   (a comment on any post)
Trigger:   a comment containing GUIDE   ·   Message 1:   [text]   ·   Button:   [text → the guide's link]   ·   Message 2:   [text]   ·   Tag:   guide
The human follow-up (you send it, never automated):   [the DM bank's message 2]

———————————————————————————————
AUTOMATION 2 — [THE OFFER'S WORD]   (a comment on any post)
Trigger · Message 1 · Button (→ the one-pager) · Message 2 (the call line, in the call-to-action law's shape) · Tag · the human follow-up

———————————————————————————————
AUTOMATION 3 — THE STORY REPLY
Trigger:   a reply to a story   ·   Message 1:   [text]   ·   the human follow-up

———————————————————————————————
WHERE EACH FIELD LIVES
[one line per step, in the member's words, using Mike's template's names where they apply]

———————————————————————————————
COMPLIANCE
[the stamp — the brokerage name as required in the DM signature, if any]
```

**The Performance Read** (`sf-analytics`, on demand — "how's my content doing", "review my attraction week"; the same
five numbers each month inside the deep dive; no weekly note — the owner, 2026-11-14) — floor: one page,
~250–400 words, every number sourced or "not available". Delivered in chat and **its text kept at
`~/attraction-brain/exports/short-form-performance-YYYY-MM-DD.txt`**, then pushed (the Brain Board shows its numbers); a
doc (`YYYY-MM-DD–DD · Performance Review`) only when the member asks for one.
```
PERFORMANCE READ · [WEEK OF DATE]
[Member Name] · [Organization] · [date]

———————————————————————————————
THIS WEEK IN FIVE NUMBERS
People who saw you: [n] · Reels posted: [n] of [cadence] · Story days: [n] of 7 · Keyword comments: [n] · Conversations started: [n] (from your log)
Source: [your Instagram, pulled today / the posting tool / "numbers not available this week — add them"]

———————————————————————————————
WHAT STARTED CONVERSATIONS
[the post + keyword → DMs → conversations logged → calls booked; "none yet" is a real line, never a guess]

———————————————————————————————
BEST POST · WEAKEST POST · BEST HOOK SHAPE
[one line each, with the why]

———————————————————————————————
THE ONE CHANGE
[exactly one]

———————————————————————————————
NEXT WEEK'S ROWS   (the mix in force)
1. [hook · pillar · format · the ask]   [... one row per post at the cadence — three by default]

———————————————————————————————
THE POST TO REPURPOSE
[the one post · the one way to give it a second life — a carousel of its steps, a story set, a follow-up Reel, a re-cut ("edit my reel" in a new chat)]

———————————————————————————————
THE STEP UP   (only when a month at three a week has held — three Reels posted in each of the last four weeks; omitted otherwise)
A month at three a week has held — you're ready for five. Say "change my cadence" and I'll remap the month on five a week.
```

**Weekly Routine** (`sf-weekly-routine`) — floor: the seven-day table, the batch block with a start time, seven
story prompts, the engagement checklist with a time of day, the empty check-in table; ~400–600 words.
```
WEEKLY ROUTINE · [WEEK OF DATE]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE WEEK AT A GLANCE
| Day | What posts (Reel + pillar, or "stories only") | Story prompt | Engagement slot | Minutes |
[Monday → Sunday]

———————————————————————————————
THE BATCH BLOCK · THE DAILY STORY HABIT (seven prompts, one interactive element) · THE ENGAGEMENT ROUTINE (the time of day) · THE CHECK-IN TABLE (empty, for the end of the week)

———————————————————————————————
COMPLIANCE
```

**Film-Day Plan** (`sf-batch-publish`, FILM DAY — also the Batch Prep workflow's doc, the evening before the
batch day) — floor: a run sheet row and a teleprompter card per video (the keyword on each, large), an honest total
time; ~400–900 words (three Reels at the default cadence, five at five).
```
FILM-DAY PLAN · [DATE]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE SESSION AT A GLANCE · THE GROUPS (location → outfit → format) · THE RUN SHEET (order · video # · hook's first line · pillar · format · location · minutes)
WHAT TO WEAR · WHAT TO BRING · THE TELEPROMPTER CARDS (hook word for word · four or five steps · the ask with its keyword, large) · BETWEEN EVERY VIDEO · THE SAFETY NET · AFTER THE SHOOT

———————————————————————————————
COMPLIANCE   (permission confirmed on every named agent; no unconsented names on a screenshot)
```

**News Watch** (`sf-greenscreen`'s Wednesday workflow — `YYYY-MM-DD · Green Screen · News Watch`) — floor: three to
six REAL headlines from the last 30 days, each cited (title · outlet · date · the link) and found by a live web
search — never invented, never older; a 30-second take each in the member's angle (a take, never a dig — the cardinal
rules); ~500–900 words. **Its text is also kept at `~/attraction-brain/exports/news-watch-YYYY-MM-DD.txt`**; the week's green-screen calendar row and board card filled with the best take, the alternates inside the card with their links (one card, never one per headline).
```
NEWS WATCH · [WEEK OF DATE]
[Member Name] · [Organization] · [Wednesday date]

———————————————————————————————
THIS WEEK'S HEADLINES   (three to six, newest first)
1. [title] · [outlet] · [date] · [link]
   The take (30 seconds, read word for word): [the member's angle — what it means for the agent watching; facts only]
   Pillar: Perspective · Rung: [Comment GUIDE / the call line]   ·   Pop-up: [six words or fewer]
[2 … 6]

———————————————————————————————
FILM THESE FIRST
[the two takes to film this week, one line each on why]

———————————————————————————————
SOURCES   (every link as searched · as seen YYYY-MM-DD; "no headline worth a take this week" is a real line, never a filler)

———————————————————————————————
COMPLIANCE
[the stamp — never a negative word about a brokerage or a person]
```

## 5b. The Deep Dive Report (the monthly analytics deliverable — stamped)
The one document that isn't content: the monthly deep dive from `sf-analytics`. Same house grammar, this fixed
shape (mirrors the YouTube plugin's report so the two dives read as one ritual). `sf-analytics` owns the numbers
and the exact section list; this is the frame it fills:
```
SHORT-FORM DEEP DIVE — [MEMBER NAME] · [ORGANIZATION]  ·  [MONTH YYYY]
Window: [dates]  ·  Sources: [live Instagram + YouTube data · the posting tool · screenshots]  ·  [N] posts reviewed
Powered by Mike Sherrard Coaching Inc Frameworks


════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{3 plain sentences: where you stand · your biggest strength · your biggest fix}

>> THE ONE MOVE:  {one sentence — the single cheapest, fastest change that matters most this month}

   ──── DO THESE THREE THIS WEEK ────
   1.  {a specific action}   2.  {…}   3.  {…}


════════════════════════════════════════════
YOUR NUMBERS AT A GLANCE   (this window vs last)
════════════════════════════════════════════
   Followers · Reels published ({n}/wk vs 3–5) · Story days ({n}/7) · Reach · Typical Reel · Skip rate ·
   Saves + shares · Profile visits · Link taps · Keyword comments · Agent DMs started · Conversations · Calls booked
   (each "not available" line says what connection would make it available)


════════════════════════════════════════════
PART 1 — YOUR ACCOUNT
════════════════════════════════════════════
   1.1 HOW YOU GREW · 1.2 WHAT'S PULLING — BY PILLAR AND BY FORMAT (Authority · Perspective · Story · Proof ·
   Personality × Reel · story · carousel · green screen; your mix vs one attraction · one authority · one story at three a week (2 · 2 · 1 at five)) ·
   1.3 YOUR BEST HOOKS (word for word, with skip rate) · 1.4 WHO'S WATCHING (agents vs consumers — the verdict) ·
   1.5 WHEN TO POST · 1.6 WHAT TURNS INTO CONVERSATIONS (keyword comments → DMs → conversations → calls, which
   Reels and stories produced agent DMs) · 1.7 STORIES (replies, exits, poll results) · 1.8 WHAT AGENTS ARE
   ASKING (questions in comments → next Reels) · 1.9 WHERE VIEWS STOP TURNING INTO DMs (the one break + the fix)
   · 1.10 HOW OFTEN YOU POST


════════════════════════════════════════════
PART 2 — OTHER LEADERS AGENTS IN YOUR MARKET FOLLOW
════════════════════════════════════════════
   Observable facts with sources, what they do that you don't, what you do better — never a verdict on a person
   or a brokerage (the cardinal rules).


════════════════════════════════════════════
PART 3 — WHAT AGENTS SEARCH AND ASK
════════════════════════════════════════════
   YouTube searches · AI-assistant answers · rising phrases · this week's brokerage and industry news → Reel ideas


════════════════════════════════════════════
PART 4 — THE OPENINGS   (what agents want that nobody in your lane is posting)
════════════════════════════════════════════
   3–5 openings: what we found · why it matters to you · do this (hook · format · pillar · week) · the proof


════════════════════════════════════════════
PART 5 — YOUR NEXT 30 DAYS
════════════════════════════════════════════
   KEEP DOING · FIX · THE PLAN (the week's mix — one attraction · one authority · one story at three a week, 2 · 2 · 1 at five; stories daily) · POST AT · THE ONE MOVE


════════════════════════════════════════════
APPENDIX — THE FULL NUMBERS
════════════════════════════════════════════
   A. every post, best to worst (hook · format · pillar · reach · saves · shares · skip % · keyword comments · DMs)
   B. your audience in full   C. search results we pulled


────────────────────────────────────────────
Sources — live data pulled {date} · the posting tool · screenshots · {N} searches.  Compliance — checked.  ✓
Powered by Mike Sherrard Coaching Inc Frameworks
```
The stamp is a byline + footer only — never inside a caption, bio, or script block the member pastes out.

## 6. The save flow (end of every content workflow)
1. Build the doc's structured text following §4–§5; write it to a temp file in the scratchpad.
2. Find-or-create the bucket folder and the month folder (§1) inside the workspace found by ID.
3. **Render** the text to a styled `.docx` via `${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py` (§3), then upload
   that `.docx` with the §2 name into the folder.
4. Confirm in plain language + give the location:
   *"Saved to your workspace → Content → Short-Form → November. Here's the doc: [link]."*
5. The content-log row (the workflow already writes it, then pushes) is the index; the Doc is the readable copy.
6. **The Brain Board's texts:** the Game Plan, a Week Plan, a performance read, the keyword sheet, the ManyChat build sheet and a news watch also
   write their text to `~/attraction-brain/exports/` under the names in §2, in the same run — then the push (write →
   push → verify) re-renders the Brain Board. A doc saved without its export is half-saved. The push that closes a
   sitting is marked as the closing push; the sync returns the Brain Board's and the Brain Book's links, which the
   close relays — "here they are".

Keep delivering the copy-paste version in chat too — the member often films or posts right away. The doc is
the organized record they (and anyone helping them) can always find.
