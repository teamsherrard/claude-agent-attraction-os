# Where this plugin saves (the Brain's drive map, applied)

This plugin creates **no workspace root of its own.** Every file lands inside the member's existing workspace
(`Agent Attraction OS` by default — renameable; **located by `config.md → Workspace ID`, then the
`_attraction-workspace.md` marker, never by name**) in the buckets the Brain's `drive-map.md` defines. Google
Drive or OneDrive — the provider is in `config.md`; the operation mapping is
`${CLAUDE_PLUGIN_ROOT}/shared/connectors.md` (a byte-identical copy of the Brain's `connectors.md`; a release check
verifies they match). **Beside every document, its text goes to `~/attraction-brain/exports/`** (the Brain syncs
`exports/*.txt`; the Brain Board's YouTube page reads them): `channel-kit-YYYY-MM-DD.txt` ·
`youtube-game-plan-YYYY-MM-DD.txt` · `youtube-kickoff-YYYY-MM-DD.txt` · `youtube-review-YYYY-MM-DD.txt` ·
`youtube-read-YYYY-MM-DD.txt` (the deep dive and the on-demand video read — `yt-analytics`).

## The buckets this plugin uses
```
[Organization] OS/
├── 01 · AI Brain/                   ← the Brain (`_engine/`, incl. exports/) and the Week 3 Kit — READ here, pushed through attraction-brain-sync
├── 02 · Brand/                      ← READ here: the YouTube banner the Week 3 brand kit already made (`banner-youtube.png`) — the Channel Page points the member to it; this plugin writes nothing here
├── 03 · Content/
│   ├── Long-Form/                   ← THIS PLUGIN'S HOME
│   │   ├── 🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD      (yt-gameplan; dated; newest is current; text → exports/youtube-game-plan-YYYY-MM-DD.txt)
│   │   ├── Channel Page — [Name] — YYYY-MM-DD              (yt-setup; text → exports/channel-kit-YYYY-MM-DD.txt — the export's older file name is kept)
│   │   ├── YouTube Deep Dive — [Month YYYY] — YYYY-MM-DD      (yt-analytics; dated; text → exports/youtube-read-YYYY-MM-DD.txt)
│   │   ├── Monthly Channel Review — [Month YYYY] — YYYY-MM-DD (yt-triggers' scheduled run; dated; text → exports/youtube-review-YYYY-MM-DD.txt)
│   │   └── YYYY-MM-DD · [Video Title]/                     (created when the video is drafted or made, never before)
│   │         ├── Kickoff Brief — [title] — YYYY-MM-DD      (the Monday Kickoff — the brief, the script start or the interview guide, the thumbnail sheet, the title-and-description start; the Kickoff's NOTE → exports/youtube-kickoff-YYYY-MM-DD.txt)
│   │         ├── Script                                    (yt-script)
│   │         ├── SEO Package — [title] — YYYY-MM-DD        (yt-seo)
│   │         ├── Thumbnail Brief — [title] — YYYY-MM-DD    (yt-thumbnail — the thumbnail sheet for Higgsfield; or the Monday Kickoff, when it drafted the week's video)
│   │         ├── Lead Map — [title] — YYYY-MM-DD           (yt-leads — only when the guide exists, built in Week 2)
│   │         ├── Repurposing Pack — [title] — YYYY-MM-DD   (yt-repurpose)
│   │         ├── Model Breakdown — [title] — YYYY-MM-DD    (yt-model-breakdown — model videos only)
│   │         ├── Interview Prep — [guest] — YYYY-MM-DD     (yt-interview — interviews only)
│   │         └── the three thumbnails (1280×720)           (made by the member in Higgsfield from the thumbnail sheet; the member drops them here and says "my thumbnail is done")
│   ├── Graphics/                    ← carousels, designed posts, proof cards (the Design Studio) — never a video's thumbnails
│   └── Guides/
│         └── Starter Resource — YYYY-MM-DD   (yt-leads — ONCE, in Week 5, the fallback while no Week 2 guide exists; a loose dated file beside the Lead Magnet plugin's campaign folders (Week 2 onward), never inside one)
└── 06 · Materials/                  ← the brokerage deck, past videos — READ for model content, never written
```
No tracker spreadsheets. No Idea Bank, Content Map, Calendar, Keyword Map, or Performance Log — the system is
chat-driven and reads state live (the Brain, the content log, the channel, the board if they have one).

## Naming (exact — predictable, sortable)
- Game Plan: `🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` (demo: `… — DEMO — YYYY-MM-DD`)
- Channel page: `Channel Page — [Name] — YYYY-MM-DD` (to the member "your Channel Page" — never a kit; its export keeps the file name `channel-kit-YYYY-MM-DD.txt`)
- Video folder: `YYYY-MM-DD · [Video Title]` (date = the day the Kickoff Brief or the script was made, whichever came first; Title Case; no emojis or slashes)
- Deep dive: `YouTube Deep Dive — [Month YYYY] — YYYY-MM-DD`
- Monthly review (the scheduled run): `Monthly Channel Review — [Month YYYY] — YYYY-MM-DD`
- Starter resource: `Starter Resource — YYYY-MM-DD` (`yt-leads`; `03 · Content/Guides/`; the fallback — built once, in Week 5, only while no Week 2 guide exists)
- Docs inside a video folder — FIXED names: `Kickoff Brief — [title] — YYYY-MM-DD` · `Script` · `SEO Package — [title] — YYYY-MM-DD` ·
  `Thumbnail Brief — [title] — YYYY-MM-DD` · `Lead Map — [title] — YYYY-MM-DD` · `Repurposing Pack — [title] — YYYY-MM-DD` ·
  `Interview Prep — [guest] — YYYY-MM-DD` · `Model Breakdown — [title] — YYYY-MM-DD`
- Exports (the text beside the document, in `~/attraction-brain/exports/`): `channel-kit-YYYY-MM-DD.txt` · `youtube-game-plan-YYYY-MM-DD.txt` ·
  `youtube-kickoff-YYYY-MM-DD.txt` · `youtube-review-YYYY-MM-DD.txt` · `youtube-read-YYYY-MM-DD.txt`
Dates are always `YYYY-MM-DD` so folders sort. Same name, same spot, every time.

## Where state lives (the system is essentially stateless)
- What's been made / published → `memory/content-log.md` (YouTube rows) + the public channel
- What performed → the member's Studio screenshots or export (`yt-analytics`), never a stored sheet
- What to film next → the Game Plan calendar in the Brain (`memory/content-calendar.md → ## Long-form (YouTube)`, the
  90 days) and, when the member has one, the content board in Notion — the working board (the 🎬 YouTube
  tab: the next 30 days, dated, kept full by the Monday Kickoff); the Brain Board is the read-only map of the same
  month, re-rendered on every push; ideas are generated fresh from the plan + the Brain + research + the idea backlog
- The plan anchors → `identity/channel.md`; the full title bank and calendar → the Game Plan doc; live-data
  status and dated performance blocks → `identity/channel.md` (`yt-analytics`); the setup journey's resume stamp
  → `identity/channel.md`'s `Setup:` line
- Interview guests and status → `memory/interview-pipeline.md`
- Filming dates → the plan's dated rows (the first video at least three days after the plan is built — `yt-gameplan`'s first-date rule), mirrored on the content board if they have one, or their real calendar — never a spreadsheet
- The board's link → `identity/publishing.md → Content board:`; that file absent (the member skipped Week 4) → `identity/channel.md → Board:` — every reader looks in that order
- The scheduled workflows' task ids and the email answer → `config.md`'s `## YouTube (Week 5)` block only (an older
  `## YouTube (Week 4)` heading is the same block, renamed on the next write)
- The two CTAs → the Week 3 Kit's chapter 7 CALLS TO ACTION table (`exports/week3-kit-*.txt`), mirrored into
  `identity/channel.md → ## The CTA line`; the two keywords → `identity/publishing.md → Keyword:`

## Saving — resolve, never duplicate
1. Get the workspace ID from `config.md`; find `03 · Content` → `Long-Form` by label inside it (create `Long-Form`
   only if missing — the Brain's setup normally made it).
2. Find this video's folder by name; if missing, create it (only when the video is actually being drafted or made —
   the Monday Kickoff creates it for the Kickoff Brief; `yt-script` reuses it).
3. Before creating a doc, check the folder for one of that name — a re-run of an undated doc saves `Script — v2`
   (the connector cannot overwrite) and tells the member; dated docs simply get today's date, newest is current.
4. Render through `shared/render_doc.py` per `shared/doc-format.md`; upload the `.docx`; write the same text to the
   document's `exports/` file; push via `attraction-brain-sync` (the push re-renders the Brain Board); confirm the
   location in plain words: *"Saved in your workspace under Content → Long-Form → [video]."* Never a path, never an ID.
5. Only CONTENT files are saved. Research briefs, idea batches, and outlier scans stay in chat — regenerated,
   never stored.

## Never
- Never create `[Member] — YouTube System/` or any parallel root. Never string-match the workspace name.
- Never read outside the workspace folder (the member's whole Drive is off limits).
- Never the realtor workspace (`_workspace.md` marker) — a different system.
- Never write media; sync pulls Brain text only.
