# Where this plugin saves (the Brain's drive map, applied)

This plugin creates **no workspace root of its own.** Every file lands inside the member's existing workspace
(`Agent Attraction OS` by default — renameable; **located by `config.md → Workspace ID`, then the
`_attraction-workspace.md` marker, never by name**) in the buckets the Brain's `drive-map.md` defines. Google
Drive or OneDrive — the provider is in `config.md`; the operation mapping is the Brain's `connectors.md`.

## The buckets this plugin uses
```
[Organization] OS/
├── 02 · Brand/                      ← the banner (built by ds-brand) lands here, by the member
├── 03 · Content/
│   ├── Long-Form/                   ← THIS PLUGIN'S HOME
│   │   ├── 🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD      (yt-gameplan; dated; newest is current)
│   │   ├── Channel Page Kit — YYYY-MM-DD                   (yt-setup)
│   │   └── YYYY-MM-DD · [Video Title]/                     (created when the video is made, never before)
│   │         ├── Script                (yt-script)
│   │         ├── SEO Package           (yt-seo)
│   │         ├── Thumbnail Brief       (yt-thumbnail)
│   │         ├── Lead Magnet Map       (yt-leads)
│   │         ├── Repurposing Pack      (yt-repurpose)
│   │         └── Interview Prep        (yt-interview — interviews only)
│   └── Graphics/                    ← thumbnails built in Claude Design (the member drops them)
└── 06 · Materials/                  ← the brokerage deck, past videos — READ for model content, never written
```
No tracker spreadsheets. No Idea Bank, Content Map, Calendar, Keyword Map, or Performance Log — the system is
chat-driven and reads state live (the Brain, the content log, the channel, the board if they have one).

## Naming (exact — predictable, sortable)
- Game Plan: `🎬 [Name]'s YouTube Game Plan — YYYY-MM-DD` (demo: `… — DEMO — YYYY-MM-DD`)
- Channel kit: `Channel Page Kit — YYYY-MM-DD`
- Video folder: `YYYY-MM-DD · [Video Title]` (date = the day the script was made; Title Case; no emojis or slashes)
- Docs inside a video folder — FIXED names: `Script` · `SEO Package` · `Thumbnail Brief` · `Lead Magnet Map` ·
  `Repurposing Pack` · `Interview Prep`
Dates are always `YYYY-MM-DD` so folders sort. Same name, same spot, every time.

## Where state lives (the system is essentially stateless)
- What's been made / published → `memory/content-log.md` (YouTube rows) + the public channel
- What performed → the member's Studio screenshots or export (`yt-analytics`), never a stored sheet
- What to film next → generated fresh from the Game Plan + the Brain + research + the idea backlog
- The plan anchors → `identity/channel.md`; the full title bank and calendar → the Game Plan doc
- Interview guests and status → `memory/interview-pipeline.md`
- Filming dates → the content board if they have one, or their real calendar — never a spreadsheet

## Saving — resolve, never duplicate
1. Get the workspace ID from `config.md`; find `03 · Content` → `Long-Form` by label inside it (create `Long-Form`
   only if missing — the Brain's setup normally made it).
2. Find this video's folder by name; if missing, create it (only when the video is actually being made).
3. Before creating a doc, check the folder for one of that fixed name — a re-run saves `Script — v2` (the
   connector cannot overwrite) and tells the member, so duplicates never scatter silently.
4. Render through `shared/render_doc.py` per `shared/doc-format.md`; upload the `.docx`; confirm the location in
   plain words: *"Saved in your workspace under Content → Long-Form → [video]."* Never a path, never an ID.
5. Only CONTENT files are saved. Research briefs, idea batches, and outlier scans stay in chat — regenerated,
   never stored.

## Never
- Never create `[Member] — YouTube System/` or any parallel root. Never string-match the workspace name.
- Never read outside the workspace folder (the member's whole Drive is off limits).
- Never the realtor workspace (`_workspace.md` marker) — a different system.
- Never write media; sync pulls Brain text only.
