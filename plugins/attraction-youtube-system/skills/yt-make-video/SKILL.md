---
name: yt-make-video
description: >
  Make This Attraction Video — the end-to-end production flow of the Agent Attraction YouTube System. Run it
  in a new chat that becomes the video (one chat = one video). From a chosen idea it locks the packaging
  (title, hook, bucket), writes the script in the member's voice, builds the thumbnail brief and the SEO
  package with the book-a-call CTA, maps the resource, fills the content-board card, and after the member
  films and publishes it writes the content-log row and repurposes the video. Works for niche videos,
  interviews, and model breakdowns; hands the edit to the Riverside Studio by name. Never posts, never
  publishes; the compliance gate runs before anything public.

  Trigger on: "make my attraction video", "produce my attraction video", "let's make the agent video",
  "build this attraction video", "make this interview video", "make this model breakdown video", "start the
  video for this idea", or when a chosen attraction idea is pasted into a fresh chat.
---

# Make This Video — one chat = one video

This chat IS the video. One simple step at a time, confirm before moving on, everything saves to this
video's folder. The member only ever feels "we're making my video." Apply
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §8 (the video structure) and §10 (the two CTAs) of
`${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`
(read `brain.md` first · write then push via `attraction-brain-sync` · `compliance.md` before anything public).

> If the member wants one piece only (just the script, just the SEO, just the thumbnail brief), jump to that
> skill; never force the whole sequence.

## Step 0 — Set up the video
Confirm the idea/title and its **bucket** (Problem · Situation · Future · Interview · Model — the content-log
Pillar cell carries Authority / Proof / Perspective by the mapping in `brain-contract.md`). If it came from
`~/attraction-brain/memory/ideas.md`, mark that row Used now (this is where an idea becomes a video); if it drew
on a `memory/intel.md` row, mark that row's `Used?` column now too. Read
`brain.md`, then `identity/content-pillars.md` (cadence, the two CTAs), `identity/avatars.md`,
`identity/voice.md`, `identity/story-bank.md` (pick one story, unused recently — the content-log says which
are fresh), `memory/content-log.md` (no repeats), `identity/compliance.md` (status now, so an `unset` is known
before work starts). Resolve the save spot: `03 · Content/Long-Form/{YYYY-MM-DD · Title}/` (naming per
`${CLAUDE_PLUGIN_ROOT}/skills/yt-setup/references/drive-structure.md`). Say where it saves in plain words and
suggest naming the chat after the video. Missing local Brain → `attraction-brain-sync` first; a tool error is
never "no Brain".

**Interview?** Run `yt-interview` first if the guest is not yet in `memory/interview-pipeline.md` at Booked
or later. **Model breakdown?** Run `yt-model-breakdown` (it gates on `identity/brokerage-model.md`).

## Step 1 — Lock the packaging (before the script)
Run the competitive read (via `yt-research`'s method, budgeted ≤5 searches): the top 3–5 real videos agents
find for this exact question — `link · channel · ~views · what works · what's missing · how ours is more
useful`. Real links only; the cardinal rules apply to how competitors are described (what is missing, never
what is wrong with them). Then lock the **title** (the viewer's question, pain or desire named — `97`), the
**hook** (the first 15–30s, straight into the question, no "welcome back"), and the **story** from the bank.
Give the member the references in chat: *"watch these three before you film — here's what each does well."*

## Step 2 — Script
`yt-script` writes the full teleprompter script in the member's voice on the structure: hook → resource CTA
around the first minute → body → book-a-call CTA a third to halfway in and again at the end → the next-video
pointer (`98`, `99`). Format by bucket (Why I Switched · Pain Point · Model Breakdown · Niche Breakdown;
interviews follow `yt-interview`'s beats). `yt-script` writes the content-log row at Scripted and stamps the
story's Used-where. Save as **Script**. Offer the 30–45s Short cut now.

## Step 3 — Thumbnail brief
`yt-thumbnail`: three directions scored, one recommended, the paste-ready brief for the Design Studio's
`ds-thumbnail-layout`. Do this BEFORE filming so the member shoots the expression the brief needs.

## Step 4 — SEO package
`yt-seo`: three titles, the description with the two CTAs in the first three lines, chapters, tags,
hashtags, pinned comment, playlist and end-screen notes. Save as **SEO Package**.

## Step 5 — The resource
`yt-leads`: the CTA and resource for this video (which guide or keyword the description points to; if the
Lead Magnet plugin has not built one yet, the book-a-call CTA carries it and the resource line names what is
coming). Save as **Lead Map** only if a resource was mapped.

## Step 6 — The board card (if they have the board — before filming)
If `identity/publishing.md` has a `Content board:` link, find this video's card (System ID → exact title →
near match) and fill it per `${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`: script, SEO, thumbnail
brief, the references, Status → Scripted. No board or `declined` → skip silently, never nag.

## Step 7 — Film and edit (hand-off by name)
The member records (Riverside; interviews on separate tracks). The edit is the Riverside Studio's job:
`studio-longform` for a solo video, `studio-interview` for a guest; the Studio returns the section map and the
flagged best 30–45 seconds. Nothing here edits video.

## Step 8 — Publish → the content-log row (the fix this fork carries)
When the member says it is live, ask for the link, then **update this video's `memory/content-log.md` row**
(the one written at script): Status `Published`, Link, the CTA used, the story used; if no row exists,
append one in the locked shape (Date · Platform `YouTube` · Format `long-form` or `interview` · Pillar =
Authority / Proof / Perspective by the bucket · Topic/hook = `[bucket] final title` · Avatar · Story used · CTA ·
Status · Link). Flip the board card to Published and top up the
two-week window from the Game Plan. Push via `attraction-brain-sync` and say the save happened, or that it
did not. For an interview, move its `memory/interview-pipeline.md` row to Published and hand the guest their
three distribution sentences (`yt-interview` Step 6).

## Step 9 — Repurpose
`yt-repurpose`: 3 Shorts, 1 carousel, 5 stories, 1 email, 1 blog, 3 conversation starters; it writes its own
content-log rows. Then: *"next week, say 'what's my next attraction video' and we pick from the plan."*

## Compliance gate
Before the script, the SEO package, or the thumbnail brief leaves the chat: `identity/compliance.md` —
`unset` → stop at that step, say plainly the rules are not set, keep drafts private; `set` → apply and remind
once; `confirmed` → apply. Never "if empty, proceed".

## Rules
- One step at a time; 2–4 questions per stop; "your turn" hand-offs; no file paths or skill names in front
  of the member.
- Never post, publish, send, or schedule. Never invent a view count, a stat, or a quote.
- Done = the folder holds Script · Thumbnail Brief · SEO Package · (Lead Map) · Repurposing Pack, the
  content-log row is Published, the Brain is pushed.
