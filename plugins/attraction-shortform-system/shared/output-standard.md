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
│     └── Profiles & Bios — 2026-11-18                         (Doc — from sf-setup)
└── 03 · Content/
      ├── Short-Form/
      │     ├── 2026-11 · November/                            (month folder — create as needed)
      │     │     ├── 2026-11-18 · Reel · The Year I Almost Quit        (Doc — a talking-head script)
      │     │     ├── 2026-11-18 · Reels · Week 1 Batch                 (Doc — a batch of scripts)
      │     │     ├── 2026-11 · 30-Day Calendar                         (Doc)
      │     │     ├── 2026-11-19 · Green Screen · Brokerage Fee Change  (Doc)
      │     │     └── 2026-11-19 · Stories · Tuesday Set                (Doc)
      │     └── Performance/
      │           ├── 2026-11-01–14 · Performance Review               (Doc — sf-analytics)
      │           ├── 2026-11-21 · Weekly Content Performance          (Doc — the Friday note)
      │           └── 2026-11-30 · Short-Form Deep Dive                (Doc — sf-analytics, monthly)
      └── Graphics/
            └── 2026-11 · November/
                  └── 2026-11-20 · Carousel · Why I Left               (Doc — the spec aa-carousel-design reads)
```

Don't pre-create empty month folders — create the current month's folder the first time you save into it.
Storage-agnostic: the same map on Google Drive or OneDrive (`shared/connectors.md` in the Brain plugin maps
"the storage connector" to the real one; never tell a Microsoft member that Google Drive is required).

## 2. Naming convention (use everywhere — no exceptions)

| Thing | Pattern | Example |
|---|---|---|
| Month folder | `YYYY-MM · Month` | `2026-11 · November` |
| Single Reel script | `YYYY-MM-DD · Reel · [Short Topic]` | `2026-11-18 · Reel · The Year I Almost Quit` |
| Batch of scripts | `YYYY-MM-DD · Reels · [Batch name]` | `2026-11-18 · Reels · Week 1 Batch` |
| 30-day calendar | `YYYY-MM · 30-Day Calendar` | `2026-11 · 30-Day Calendar` |
| Green screen | `YYYY-MM-DD · Green Screen · [Short Topic]` | `2026-11-19 · Green Screen · Brokerage Fee Change` |
| Story set | `YYYY-MM-DD · Stories · [Day / theme]` | `2026-11-19 · Stories · Tuesday Set` |
| Carousel / LinkedIn doc | `YYYY-MM-DD · Carousel · [Short Topic]` | `2026-11-20 · Carousel · Why I Left` |
| Profiles & bios | `Profiles & Bios — YYYY-MM-DD` | `Profiles & Bios — 2026-11-18` |
| Performance doc | `YYYY-MM-DD–DD · Performance Review` | `2026-11-01–14 · Performance Review` |
| Friday note | `YYYY-MM-DD · Weekly Content Performance` | `2026-11-21 · Weekly Content Performance` |
| Deep dive | `YYYY-MM-DD · Short-Form Deep Dive` | `2026-11-30 · Short-Form Deep Dive` |
| Weekly ideas + hook bank | `YYYY-MM-DD · Attraction Ideas + Hook Bank` | `2026-11-17 · Attraction Ideas + Hook Bank` |
| Weekly routine | `YYYY-MM-DD · Weekly Routine` | `2026-11-17 · Weekly Routine` |
| Keyword sheet + DM bank | `YYYY-MM-DD · Keyword Sheet + DM Bank` | `2026-11-18 · Keyword Sheet + DM Bank` |
| Film-day plan | `YYYY-MM-DD · Film-Day Plan` | `2026-11-18 · Film-Day Plan` |
| Publishing queue | `YYYY-MM-DD · Publishing Queue` | `2026-11-24 · Publishing Queue` |

Everything in the Short-Form bucket except the performance documents lives in the month folder
(`03 · Content/Short-Form/[YYYY-MM · Month]/`); the performance review, the Friday note, and the deep dive live in
`03 · Content/Short-Form/Performance/` (no month folder).

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
(Carousel docs use SLIDE 1 / SLIDE 2 … + DESIGN BRIEF FOR DS-CAROUSEL + the IG/FB block + the LINKEDIN block;
story docs use STORY 1 / STORY 2 … with the category, the text overlay, the sticker, and the reply CTA; the
calendar uses WEEK 1 → WEEK 4 tables; performance docs use the review structure from `sf-analytics`' own
reference. Same formatting rules throughout.)

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
