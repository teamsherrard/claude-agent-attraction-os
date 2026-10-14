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
├── 02 · Brand/
│     └── Profile Optimization Pack — 2026-11-17                (Doc — from sf-setup Step 2; formerly "Profiles & Bios")
└── 03 · Content/
      ├── Short-Form/
      │     ├── Taylor's Short-Form Game Plan — 2026-11-17            (Doc — from sf-gameplan; the bucket root, dated, newest is current)
      │     ├── 2026-11 · November/                            (month folder — create as needed)
      │     │     ├── 2026-11-18 · Reel · The Year I Almost Quit        (Doc — a talking-head script)
      │     │     ├── 2026-11-18 · Reels · Week 1 Batch                 (Doc — a batch of scripts)
      │     │     ├── 2026-11-23 · Week Plan                            (Doc — the Monday Week Plan's drafts)
      │     │     ├── 2026-11 · 30-Day Calendar                         (Doc — a calendar-only refresh; the calendar itself is the Game Plan's section 6)
      │     │     ├── 2026-11-19 · Green Screen · Brokerage Fee Change  (Doc)
      │     │     └── 2026-11-19 · Stories · Tuesday Set                (Doc)
      │     └── Performance/
      │           ├── 2026-11-01–14 · Performance Review               (Doc — sf-analytics)
      │           ├── 2026-11-21 · Weekly Content Performance          (Doc — the Friday note)
      │           └── 2026-11-30 · Short-Form Deep Dive                (Doc — sf-analytics, monthly)
      └── Graphics/
            └── 2026-11 · November/
                  └── 2026-11-20 · Carousel · Why I Left               (Doc — the spec aa-content-design reads)
```

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
| Story set | `YYYY-MM-DD · Stories · [Day / theme]` | `2026-11-19 · Stories · Tuesday Set` |
| Carousel / LinkedIn doc | `YYYY-MM-DD · Carousel · [Short Topic]` | `2026-11-20 · Carousel · Why I Left` |
| Profile Optimization Pack (formerly Profiles & Bios) | `Profile Optimization Pack — YYYY-MM-DD` | `Profile Optimization Pack — 2026-11-17` |
| Performance doc | `YYYY-MM-DD–DD · Performance Review` | `2026-11-01–14 · Performance Review` |
| Friday note | `YYYY-MM-DD · Weekly Content Performance` | `2026-11-21 · Weekly Content Performance` |
| Deep dive | `YYYY-MM-DD · Short-Form Deep Dive` | `2026-11-30 · Short-Form Deep Dive` |
| Weekly ideas + hook bank | `YYYY-MM-DD · Attraction Ideas + Hook Bank` | `2026-11-17 · Attraction Ideas + Hook Bank` |
| Weekly routine | `YYYY-MM-DD · Weekly Routine` | `2026-11-17 · Weekly Routine` |
| Keyword sheet + DM bank (the CTA bank is its first page) | `YYYY-MM-DD · Keyword Sheet + DM Bank` | `2026-11-18 · Keyword Sheet + DM Bank` |
| Film-day plan | `YYYY-MM-DD · Film-Day Plan` | `2026-11-18 · Film-Day Plan` |
| Publishing queue | `YYYY-MM-DD · Publishing Queue` | `2026-11-24 · Publishing Queue` |

Everything in the Short-Form bucket except the Game Plan and the performance documents lives in the month folder
(`03 · Content/Short-Form/[YYYY-MM · Month]/`); the Game Plan lives at the bucket root (dated, newest is current);
the performance review, the Friday note, and the deep dive live in `03 · Content/Short-Form/Performance/` (no month
folder).

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
- **Bullets** with `•`; sub-points or beats with `—`. One point per line.
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
CTA rung: [Follow / Comment / DM / Resource / Conversation / Call]   ·   Keyword: [WORD]

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
(Carousel docs use SLIDE 1 / SLIDE 2 … + THE DESIGN BRIEF FOR AA-CONTENT-DESIGN + the IG/FB block + the LINKEDIN block;
story docs use STORY 1 / STORY 2 … with the category, the text overlay, the sticker, and the reply CTA; the
calendar uses WEEK 1 → WEEK 4 tables; performance docs use the review structure from `sf-analytics`' own
reference. Same formatting rules throughout.)

## 5a. The other skeletons (every named document has a shape; a thin one is a fail)
The content skeleton in §5 covers a Reel, a green screen, a carousel, and a story set. The documents below are the
premium set a Week 3 member actually opens and keeps — each has its own bands, and a floor. Same house grammar
(§4). The skill that owns the doc fills every band; an empty band is written as a real line ("none yet", "not
available"), never left blank.

**The Short-Form Game Plan** (`sf-gameplan` — the Week 3 flagship, built inside setup; stamped) — floor: nine
sections at their floors (1 · 150 · 2 · 400 · 3 · 200 · 4 · 250 · 5 · 150 · 6 · 400 · 7 · 100 · 8 · 100 · 9 · 50
words), twenty dated calendar rows (twelve at three a week), five pillars with three angles each, thirty hooks;
~3,500–5,000 words. Demo mode tags every figure "(illustrative — demo)".
```
[NAME]'S SHORT-FORM GAME PLAN
Attracting: [the primary type] · [the second]  ·  Known for: [niche]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks

———————————————————————————————
READ THIS FIRST
[three sentences: where your short-form is today and the verdict · the insight · the plan in one line]
First post to film: [row 1 — working title · date]   ·   Batch day: [day]   ·   Compliance: [status — one line if unset]

———————————————————————————————
1. POSITIONING FOR SHORT-FORM
Who I'm talking to: [the agent, their pain in their words, the mirror beat]
The one line: "[Name] helps [agent] [outcome] through [mechanism]"
The job of short form: Awareness → Recognition → Familiarity → Trust → Curiosity → Conversation
The keyword: [WORD] · what it opens: [the live guide / the free thing / the call]
The two CTAs: 1. Book a call — [link]   2. [resource] — comment [WORD]
Why I'm building this: [the why-line, in their voice]

———————————————————————————————
2. THE FIVE PILLARS — THREE ANGLES EACH
AUTHORITY — what I teach
[two-line summary]
• [hook] · for [agent] · [pain] · carries [teach / story / win]   (×3)
PERSPECTIVE — what I believe · STORY — where I've been · PROOF — what's happening in my world · PERSONALITY — who I am off the clock   (same shape)

———————————————————————————————
3. THE FORMAT MIX AND THE WEEKLY CADENCE
[N] Reels a week · the mix: 2 attraction · 2 authority · 1 story, stories daily (the OS default until Mike's decision)
Formats: talking head [what for] · green screen [what for] · carousel [what for] · stories [what for]
Platforms, in order: [Instagram Reels → TikTok → YouTube Shorts → Facebook Reels · LinkedIn for the carousel]
Batch day: [day · the rhythm]   ·   The 15-minute routine: [the moves, the time of day]

———————————————————————————————
4. THE HOOK BANK   (thirty — six per pillar, under 12 words, no two the same shape)
AUTHORITY: 1–6 · PERSPECTIVE: 1–6 · STORY: 1–6 · PROOF: 1–6 · PERSONALITY: 1–6   (each: hook · for whom · rung; `starter` where seeded)

———————————————————————————————
5. CTAs AND THE COMMENT-TO-DM FLOW
The ladder: Follow / save / share → Comment → DM → Resource → Conversation → Call   ·   one Reel, one rung, one keyword
The ask map: [pillar → rung, five lines] · the five ask lines, in my words · the call line (at most once a month)
The keyword: [WORD] → [what it opens] · by hand / ManyChat: [state]   ·   the full keyword sheet: "my keyword sheet"

———————————————————————————————
6. THE 30-DAY CALENDAR   ([date] → [date])
WEEK 1 — WHO I AM
| # | Date | Day | Format | Pillar | Working title | Hook | CTA (rung · WORD) | Carries |
[five rows]
WEEK 2 · WEEK 3 · WEEK 4   (same table)
STORIES, DAILY: [the four-category rotation · morning / midday / evening]
THE BATCH PLAN: [sessions · what films together · hours]
THE THREE TO FILM FIRST: 1. [#, why]  2. [#, why]  3. [#, why]

———————————————————————————————
7. WHAT WE MEASURE AND THE FRIDAY CHECK
[the five Friday numbers · calls booked from content · the benchmark · where the numbers come from · the compliance line]

———————————————————————————————
8. YOUR SCHEDULED WORKFLOWS   (all draft-only — nothing posts, sends, or schedules on its own)
Monday Week Plan — [when · what it produces · status]   ·   Friday performance note — [...]   ·   Daily stories — [...]

———————————————————————————————
9. NEXT STEPS
[the first Reel · the board · the keyword sheet · the film day · the research re-run if any row is unresearched]

———————————————————————————————
SOURCES
[what agents are asking — each search → what was seen · as seen YYYY-MM-DD]   ·   Budget used: [n] of 8   ·   Starter rows: [n]   ·   Unresearched rows: [n]   (demo: "nothing searched")

———————————————————————————————
[closing — one honest paragraph: be consistent, not complicated]
COMPLIANCE
[the stamp]
```

**The Profile Optimization Pack** (`sf-setup`, Step 2) — floor: every platform the member uses, each block with
where it goes; the five questions ticked per bio; ~600–1,000 words.
```
PROFILE OPTIMIZATION PACK
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE KEYWORD
[WORD] · what it opens · said on camera, written in every bio's last line

———————————————————————————————
INSTAGRAM
Name field (Edit profile → Name):   [...]
Bio (≤150):   [...]
Link in bio, in order:   1. [the lead magnet — action text]  2. [book a call]  3. [the YouTube channel — "added in Week 4" if none]  4. [the community]
Highlights:   About · Agent wins · Culture · Free value · Partner with me · [one passion] — [one line each on what goes in]
Pinned posts:   1. [...]  2. [...]  3. [...]

———————————————————————————————
FACEBOOK   (profile intro · page intro · About)
TIKTOK   (name · bio ≤80)
LINKEDIN   (headline ≤220 · About, 4–5 short paragraphs · Featured, in order)
THE LINK-IN-BIO PAGE   (its contents in order, each link's action text)
VISUALS   (one line: the brand kit's profile pictures and banners — 02 · Brand)

———————————————————————————————
COMPLIANCE
[the stamp — brokerage name / license as required]
```

**The Week Plan** (the Monday Week Plan, `sf-week-plan`) — floor: every calendar row dated this week drafted
(brief · hook ×3 · script or talking points · bullet version · CTA · captions), the seven-day story set, the board
count; ~1,500–2,500 words for five posts.
```
WEEK PLAN · [WEEK OF DATE]
[Member Name] · [Organization] · [Monday date]

———————————————————————————————
THE WEEK AT A GLANCE
| Day | Post (working title · pillar · format) | Status | Board |
THE BATCH DAY: [day]

———————————————————————————————
POST 1 — [working title]   (THE BRIEF · THE HOOK — 3 WAYS · THE SCRIPT · THE BULLET VERSION · THE SHOTS · THE CTA · THE CAPTIONS — the §5 content shape)
POST 2 … POST 5

———————————————————————————————
STORIES THIS WEEK   (seven days: what to capture · overlay · sticker · reply CTA)

———————————————————————————————
LEFT FOR YOU   (anything undrafted and why)

———————————————————————————————
COMPLIANCE
```

**The 30-Day Calendar** (section 6 of the Game Plan — `sf-gameplan`; saved on its own only on a calendar-only
refresh) — floor: 20 numbered, dated rows (12 at three a week), every cell filled, a batch plan with hours;
~800–1,000 words.
```
30-DAY CALENDAR · [MONTH YYYY]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE MONTH AT A GLANCE
[one paragraph: what this month establishes and why this order — the mix in force, the keyword, the batch rhythm]

———————————————————————————————
WEEK 1 — WHO I AM   (one post per pillar: an agent who finds you this week can answer the five profile questions from the feed)
| # | Date | Day | Format | Pillar | Working title | Hook | For | Carries (story / win / teach) | Rung · keyword |
[five rows]
WEEK 2 · WEEK 3 · WEEK 4   (same table; the member's own ideas and this month's objections land in Weeks 1–2)

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

**Attraction Ideas + Hook Bank** (`sf-ideas`) — floor: exactly 5 + 15 + 30, five to eight cited findings; ~1,200–1,600 words.
```
ATTRACTION IDEAS + HOOK BANK · [WEEK OF DATE]
[Member Name] · [Organization] · [Date]

———————————————————————————————
WHAT AGENTS ARE ASKING RIGHT NOW
1. "[the phrase as an agent typed it]" · HIGH / MEDIUM / EMERGING · [where it was seen · when] · [pillar it feeds]
[five to eight — the citations every idea below points at by number]

———————————————————————————————
THIS WEEK'S FIVE
1. [the title the way a person would say it] · [the angle, one line] · [pillar] · [for whom] · [format] · [rung · keyword] · [finding #]
[five, on the mix in force]

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

**Keyword Sheet + DM Bank** (`sf-comment-to-dm`, Job B) — floor: the CTA bank (15 lines), six messages for the
primary keyword (each under 60 words), the story reply, the qualifier, the paste sheet; ~1,000–1,500 words.
```
KEYWORD SHEET + DM BANK
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE KEYWORD
Keyword: [WORD] · What it opens: [the resource / the call] · Said on camera at the end · Written as the caption's last line · Pinned as the first comment
ManyChat: [connected / replying by hand / declined] · Variants once the templates run: GUIDE · GROWTH · SCALE · PARTNER (each defaults to the primary word's flow until then)

———————————————————————————————
THE CTA BANK   (fifteen lines, three per pillar, each on its rung)
AUTHORITY — Comment / Resource:   Spoken: [...]   Caption: [...]   (×3)
PERSPECTIVE — Follow / save / share (×3) · STORY — DM (×3) · PROOF — DM (×3) · PERSONALITY — Follow (×3)
THE CALL LINE (at most once a month): [...]

———————————————————————————————
THE DM BANK — [KEYWORD]
1. Auto-reply · 2. The human follow-up · 3. The qualifier (three messages, one at a time) · 4. The bridge to the resource · 5. The invite to a call · 6. The graceful no
THE DM BANK — GUIDE · GROWTH · SCALE · PARTNER   (the same six each, once the templates run)
THE STORY REPLY · THE DM QUALIFIER

———————————————————————————————
THE MANYCHAT PASTE SHEET
keyword · trigger (comment / DM / story reply) · message 1 · button text · message 2 · the tag · the human follow-up (sent by hand, never automated)

———————————————————————————————
COMPLIANCE
```

**Weekly Content Performance — the Friday note** (`sf-analytics`' scheduled agent; also "review my attraction
week") — floor: one page, ~250–400 words, every number sourced or "not available".
```
WEEKLY CONTENT PERFORMANCE · [WEEK OF DATE]
[Member Name] · [Organization] · [Friday date]

———————————————————————————————
THIS WEEK IN FIVE NUMBERS
People who saw you: [n] · Reels posted: [n] of [cadence] · Story days: [n] of 7 · Keyword comments: [n] · Conversations started: [n] (from your log)
Source: [your Instagram, pulled Friday / the posting tool / "numbers not available this week — add them Monday"]

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
NEXT WEEK'S FIVE   (the mix in force)
1. [hook · pillar · format · rung · keyword]   [...]   5. [...]

———————————————————————————————
YOUTUBE SECTION
[appended by your YouTube system from Week 4; omitted until then]
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
THE BATCH BLOCK · THE DAILY STORY HABIT (seven prompts, one interactive element) · THE ENGAGEMENT ROUTINE (the time of day) · THE CHECK-IN TABLE (empty, for Friday)

———————————————————————————————
COMPLIANCE
```

**Film-Day Plan** (`sf-batch-publish`, FILM DAY) — floor: a run sheet row and a teleprompter card per video, an
honest total time; ~600–900 words for five Reels.
```
FILM-DAY PLAN · [DATE]
[Member Name] · [Organization] · [Date]

———————————————————————————————
THE SESSION AT A GLANCE · THE GROUPS (location → outfit → format) · THE RUN SHEET (order · video # · hook's first line · pillar · format · location · minutes)
WHAT TO WEAR · WHAT TO BRING · THE TELEPROMPTER CARDS (hook word for word · four or five beats · the ask with its keyword, large) · BETWEEN EVERY VIDEO · THE SAFETY NET · AFTER THE SHOOT

———————————————————————————————
COMPLIANCE   (permission confirmed on every named agent; no unconsented names on a screenshot)
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
   Personality × Reel · story · carousel · green screen; your mix vs 2 attraction · 2 authority · 1 story) ·
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
   KEEP DOING · FIX · THE PLAN (2 attraction · 2 authority · 1 story a week, stories daily) · POST AT · THE ONE MOVE


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

Keep delivering the copy-paste version in chat too — the member often films or posts right away. The doc is
the organized record they (and anyone helping them) can always find.
