---
name: yt-make-video
description: >
  Make This Attraction Video — the end-to-end production flow of the Agent Attraction YouTube
  System (Week 5). One chat = one video: locks the packaging (title, hook, lane), picks up the
  Monday Kickoff's drafts, writes the script in the member's voice with the two CTAs (the Week 2
  guide, the call in the law's shape), writes the thumbnail sheet for Higgsfield and the SEO package,
  fills the board card in its locked order, states the editing next step (the editor, Plugin 5), and
  after publish writes the content-log row and hands Reels and carousels to the short-form system by
  phrase. Never posts or publishes; compliance read before anything public, never a stop. Trigger
  on: "make my attraction video", "produce my attraction video", "let's make the agent video",
  "build this attraction video", "make this agent interview video", "make this model breakdown video
  for agents", "start the attraction video for this idea", "my video is published", or a chosen
  attraction idea pasted into a fresh chat.
---

# Make This Video — one chat = one video

This chat IS the video. One simple step at a time, each announced and then built — never a "shall I go on?"
between steps — and everything saves to this video's folder. The member only ever feels "we're making my video." Apply
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §8 (the video structure) and §10 (the two CTAs) of
`${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`
(read `brain.md` first · write then push via `attraction-brain-sync` · `compliance.md` before anything public).

**Week 5 rules that bind every video** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **Two CTAs, two keywords.** The resource is the Week 2 guide — `memory/magnets.md → ## Current magnet` (keyword
  GUIDE; its funnel URL on description line 2 and in the pinned comment; the spoken line may say "comment GUIDE
  and I'll send it"). The call is the booking link on description line 1, in the law's shape. The second keyword
  is the offer's `Comment keyword:` (`identity/offer.md`); both sit on `identity/publishing.md`'s `Keyword:` line.
  Never a third word.
- **The call ask follows the law** — the person · their help · free · to run the method; never the brokerage as
  the reason, never compensation. Join register (`offer.md → Join-gated package allowed: yes` or `unknown`):
  *"If you want my help running this — the lessons, the templates, the community — partner with me and it's
  free. Grab [the call]."* Open register (`no`): *"I'll walk you through it, free, no strings."* The method
  (`offer.md → ## The framework`) is named every time. The spoken lines, the video pop-ups and the end cards come
  from the Week 3 Kit's chapter 7 CALLS TO ACTION table (the newest `exports/week3-kit-*.txt`), verbatim — never
  a new join line of this plugin's own.
- **Scalable by design** (the Brain's doctrine §10e). No line in a script, a description or a pinned comment
  promises the member's time per partner — no in-person days beside the member, no chat group, no one-to-one
  calls, no response times. Partners get the recorded lessons, the templates, the community, and the weekly
  group call only when `identity/operations.md` shows the member already runs one.
- **The offer first.** Titles and lanes from `offer.md → ## Content branches`; hook material from `## The
  framework`; the promise from `## The program`'s 90-day outcome; the story's spine from `identity/journey.md →
  ## Why join me`. Then the Brain's other signals, research third, the starter bank last.
- **Cadence** is the `Cadence:` line of `identity/channel.md → ## Game Plan anchors` — one video a week the
  default for the first month, two the step-up. This chat makes one video regardless.
- **Member-facing words:** Week 5; "your content board", "the YouTube tab at the top of your board"; the editing next
  step stated, never hedged (Plugin 5 — "when it's filmed: 'edit my YouTube video'"); the short-form system by
  phrase; never a skill id, a file path or a task id in a sentence to the member; plain words — "your thumbnail
  sheet" (the member makes the thumbnail in Higgsfield), "your title and description" (never "the SEO package"),
  "three ways to open" (never "the hook three ways"), "your eight-video plan", "your Channel Page".

> If the member wants one piece only (just the script, just the title and description, just the thumbnail sheet),
> jump to that skill; never force the whole sequence.

## Step 0 — Set up the video
State the idea/title and its **bucket** — no title in the member's words → this week's video: the calendar row
dated this week (the one the Monday Kickoff drafted), else the next `Idea` row; say which in one line, never
"which video?" — (Problem · Situation · Future · Interview · Model — the content-log
Pillar cell carries Authority / Proof / Perspective by the mapping in `brain-contract.md`). Read `brain.md`, then
only three more files now — the rest open at the step that uses them: `identity/compliance.md` (the first line,
`Status:` — so an `unset` is known before work starts), `memory/content-log.md` (no repeats; this video's row if
`yt-interview` or `yt-model-breakdown` already wrote one), `identity/avatars.md` (the viewer this video is for).
Resolve the save spot: `03 · Content/Long-Form/{YYYY-MM-DD · Title}/` (naming per
`${CLAUDE_PLUGIN_ROOT}/skills/yt-setup/references/drive-structure.md`). Say where it saves in plain words and
suggest naming the chat after the video. Missing local Brain → `attraction-brain-sync` first; a tool error is
never "no Brain".

**The channel trailer** ("make my attraction video: my channel trailer" — a new channel's first row on the plan,
week one's first row, a card like any other): the same flow, sized down — a 60 to 90 second script (who you help ·
what you cover · the invite, in the law's shape), one thumbnail sheet, the title and description; its content-log
row carries Pillar `Authority` and `[Trailer]` at the start of the Topic cell (it is not one of the eight), and its
card's Pillar cell stays empty (the spec's options are never extended).

**Drafted by the Monday Kickoff already?** This video's content-log row is at `Scripted` with Link `—` and no
`Script` doc in its folder, or its board card sits at `Scripted` with a script START (not a full script), or the
folder holds a `Kickoff Brief — [title] — …` → **pick up the drafts, never redo them:** the brief's title, bucket,
story, and CTAs are the package (Step 1 only confirms them and runs the competitive read); the script start's
hook and CTA lines open the script (Step 2 writes the rest); the thumbnail sheet stands unless the title
changed (Step 3 is a check, not a rewrite); the SEO start is completed with the chapters (Step 4). Say so in one
line: *"your Monday Kickoff already drafted the start — I'm picking up from there."* Setup's first video arrives
the same way when the board was seeded: the card exists at `Idea`; the title is locked, nothing else is drafted.

**Opened later:** Step 1 → `identity/offer.md` · `identity/voice.md` · `identity/story-bank.md` ·
`memory/magnets.md` (the live guide) · the newest `exports/week3-kit-*.txt` (chapter 7) · (an interview)
`memory/interview-pipeline.md` · (only if the idea came from them) `memory/ideas.md` · `memory/intel.md` · Step 2
→ `identity/publishing.md` (the `Keyword:` line) · `identity/content-pillars.md` · Step 6 → `identity/publishing.md`
(the `Content board:` line). The script, thumbnail, SEO, lead-map, and repurposing skills open their own files in
their own step — never here.

## Step 1 — Lock the packaging (before the script)
**Read now:** `identity/offer.md` — the header (`Join-gated package allowed:` = the register of every call ask;
`Comment keyword:`), `## Content branches` (which branch this title serves — a title off every branch is a flag,
not a stop), `## The framework` (the step this video teaches, in full), `## The program` (the 90-day outcome the
hook can promise — shown, never earned) · `identity/voice.md` (the hook in their voice) · `identity/story-bank.md`
(one story, unused recently — the content-log says which are fresh) · `memory/magnets.md → ## Current magnet`
(the Week 2 guide: its title, GUIDE, its funnel URL) · the newest `exports/week3-kit-*.txt` → chapter 7's CALLS
TO ACTION table (the spoken resource line, the spoken call line, the pop-ups, the end cards — every CTA in this
chat quotes it).
**Interview?** Open `memory/interview-pipeline.md`; run `yt-interview` first if the guest is not yet there at
Booked or later. **Model breakdown?** Run `yt-model-breakdown` (it gates on `identity/brokerage-model.md`).
**No guide yet?** `## Current magnet` empty (nothing, or the template's placeholder — the member skipped the
Week 2 session) → one warm line, *"say 'launch my lead magnet plugin' and your guide becomes the thing every
video hands out"*; meanwhile `yt-leads` builds the Starter Resource (its 1a) once, the fallback, so the script,
the description and the pinned comment in this chat still name a real file. Never a demand; never the call as
the resource.
**Start from the card's reference video** (the owner, 2026-11-15: every card already carries one real YouTube
video close to its idea — the row's `Reference video` cell in `memory/content-calendar.md → ## Long-form (YouTube)`,
or the card's `Reference Video` link). Re-run the "is it real" check on it once
(`${CLAUDE_PLUGIN_ROOT}/skills/yt-research/references/research-method.md`, the reference-video steps): gone → it is
replaced by the read below; still there → it is the first candidate. No reference on file (an ad-hoc title, an
older row) → the read below finds all three.
Run the competitive read (via `yt-research`'s method, budgeted ≤5 searches): the top 3 (2–4) real videos agents
find for this exact question — `link · channel · ~views (as seen) · date seen · what works · what's missing · the
one thing we do better`. Real links only — each returned by a search in this chat and checked as a real, public
video; a count that cannot be seen is left off; the cardinal rules apply to how other channels are described (what
is missing, never what is wrong with them). **The closest of the three is the card's reference video:** the one
already there is confirmed, or a closer one replaces it — then the row's cell and the card's `Reference Video` link
are updated. **Live numbers only when they are already there:** `identity/channel.md → Live data: active …` on
file and the tools in this session → the data engine's recipe 4 gives exact views and dates
(`${CLAUDE_PLUGIN_ROOT}/shared/composio-data-engine.md`); otherwise the web search, silently — never a sign-in or
an ask here, at most one closing line naming *"connect my YouTube numbers"*. Then lock the **title** (the
viewer's question, pain or desire named — `97`), the **hook** (the first 15–30 s, straight into the question, no
"welcome back"), and the **story** from the bank. Give the member the references in chat: *"watch these three
before you film — the first is the one on your card; here's what each does well."*
Once the title locks — still the start of the video chat, never pick time — if the idea came from
`~/attraction-brain/memory/ideas.md`, open it and mark that row Used now (this is where an idea becomes a video);
if it drew on a `memory/intel.md` row, mark that row's `Used?` column now too.

## Step 2 — Script
**Read now:** `identity/publishing.md` → the `Keyword:` line (`GUIDE · [the offer's word]` — the keyword's single
source) · `identity/content-pillars.md` (its CTA line mirrors the kit; its cadence line is the short-form cadence
— the YouTube cadence is the Game Plan anchor in `identity/channel.md`).
`yt-script` writes the full teleprompter script in the member's voice on the structure: hook → the guide ask
inside minute one ("comment GUIDE" or "link in the description") → body → the call ask in the law's shape a
third to halfway in and again at the end → the next-video pointer (`98`, `99`). Format by bucket (Why I Switched ·
Pain Point · Model Breakdown · Niche Breakdown; interviews follow `yt-interview`'s steps). `yt-script` writes the
content-log row at Scripted and stamps the story's Used-where. Save as **Script**. Name the strongest 30–45 s
moment for the first Short (your AI Editing Studio cuts it at the edit; the Reels themselves are the short-form
system's — Step 9).

## Step 3 — The thumbnail sheet (for Higgsfield)
`yt-thumbnail`: three directions scored in the chat, one recommended, and the ONE sheet — for each direction the
image prompt to paste (the scene, the expression, the background, the brand's colours in plain words, a 16:9 frame
at 1280×720 with clear space for the words), which of the member's own photos to upload, and the 3 to 5 words to
add. The member makes the thumbnail in Higgsfield — say it in the sheet's own words: *"Take this to Higgsfield,
where you make your thumbnails: upload your photo, paste the prompt, add the words. Drop the finished thumbnail
into this video's folder and say 'my thumbnail is done'."* A thumbnail sheet is never pasted anywhere else. Do
this BEFORE filming so the member shoots the expression the sheet needs.

## Step 4 — SEO package
`yt-seo`: three titles, the description — line 1 the call in the law's shape with the booking link, line 2 the
guide's funnel URL, line 3 the compliance and contact line — chapters, tags, hashtags, the pinned comment (the
guide's link + "comment GUIDE"),
playlist and end-screen notes. Save as **SEO Package**.

## Step 5 — The resource
`yt-leads`: the CTA pair for this video, quoted from the kit's table — the resource line names the live guide
(or the fallback Starter Resource from Step 1) and the funnel URL the description points to; the call line in the
law's shape. Save as **Lead Map** only when the Week 2 guide exists; the Starter Resource needs no map.

## Step 6 — The board card (if they have the board — before filming)
Open the board line now — `identity/publishing.md → Content board:`; that file absent (the member skipped Week
4) → `identity/channel.md → Board:`. A URL → find this video's card (System ID → exact
title → near match) and write the card page in the locked order of `${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`
— **🎯 THE HOOK** (the hook three ways, the chosen one first and in bold; the title) · **🎬 SCRIPT** (the full
script) · **🖼 THUMBNAIL BRIEF** (the thumbnail sheet for Higgsfield) · **🔍 SEO PACKAGE** · **🧲 THE RESOURCE** (the guide, GUIDE,
the funnel URL, the booking line) · **📚 REFERENCE VIDEO — WATCH THIS FIRST** (the closest video first, as the spec lays it out — the
titled link, the video playable on the card, Why this one — now with **the one thing to do better**, written from
what Step 1 actually read; then the line **Two more worth your time** and the other two, each `titled link ·
channel · the one thing to do better`; the `References` field holds the three; never a negative word about a
channel or its brokerage) · **🎙 GUEST** (interviews only) · **📋 ASSETS & NOTES** (b-roll, the compliance lines to
say) · **✅ PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO** (the owner, 2026-11-14: uploading is where older members get
stuck — six real to-do items, `- [ ]`, in Studio's own order, each with its click path and THIS video's own values:
**1 Title** — Details → Title: the chosen title, printed · **2 Description** — Details → Description: the
description, with line 1 the call and the booking link, line 2 the guide, line 3 the compliance and contact line ·
**3 Thumbnail** — Details → Thumbnail → Upload file: the thumbnail made in Higgsfield, from this video's folder ·
**4 Playlist** — Details → Playlists: the playlist by its exact name (the lane's, from `channel.md`) · **5 End
screen** — Video elements → Add an end screen: the next video and the playlist the SEO package names (a first
video: the playlist alone), and Subscribe ·
**6 Pinned comment** — after it is public: the pinned comment from the SEO package, then ⋮ → Pin; under the six,
*"All six ticked? Say 'my video is published' and I'll move this card to Published."* Boxes the member already
ticked stay ticked; the system never ticks one) ·
**📊 AFTER IT'S OUT** (left empty — the Monthly Channel Review, or "how did my video do", writes it). A section already there (the Kickoff's
start) is **replaced in place, never stacked**; the workspace links go in the columns; Status → `Scripted`; the
card's Topic renamed to the final title if it changed. No board or `declined` → skip silently, never nag.

## Step 7 — Film and edit (the editing step is stated, never hedged)
The member records (a guest on separate tracks). Nothing here edits video. Say the next step as a fact (the owner,
2026-11-14 evening — Plugin 5 was installed in Week 4; it is part of the process): *"When it's filmed: open a new
chat and say 'edit my YouTube video' (or 'edit my interview') — that opens your AI Editing Studio (Plugin 5), which
edits inside your own Riverside account. Not installed yet? Install Plugin 5 from the same marketplace first, then
say 'set up riverside' once."* The edit returns the section map (the chapters) and the flagged best 30–45 seconds
(the first Short). When they say it is filmed → flip this video's row in `memory/content-calendar.md → ## Long-form
(YouTube)` and the board card to `Recorded` (the section absent → nothing to flip); push. When the edit is done and
the video waits to go out → flip the calendar row and the card to `Ready to Post` (the content-log row reads
`Edited`, the editor's word; the board says `Ready to Post`); push.

## Step 8 — Publish → the content-log row (the fix this fork carries)
**The phrase is "my video is published"** (the card's own last line says it; "it's live", "I uploaded it" and the
like are the same thing). Which video: the one this chat is about; in a fresh chat, the card at `Ready to Post` or
`Recorded` with the nearest date — said in one line, never asked unless two fit equally. **The six boxes never
block it:** read the card's ✅ PUBLISH IT; anything still unticked → one plain line naming it (*"Two steps are still
open on its card: the end screen and the pinned comment."*), and carry on.
When the member says it is live, ask for the link once (only when they did not give it), then **update this video's `memory/content-log.md` row**
(the one written at script): Status `Published`, Link, the CTA used (`resource: [the guide's name] · call`), the
story used; if no row exists, append one in the locked shape (Date · Platform `YouTube` · Format `long-form` or
`interview` · Pillar = Authority / Proof / Perspective by the bucket · Topic/hook = `[bucket] final title` · Avatar ·
Story used · CTA · Status · Link). Flip this video's row in `memory/content-calendar.md → ## Long-form (YouTube)`
to `Published`, flip the board card to `Published` (📊 AFTER IT'S OUT is written by the Monthly Channel Review, or when they ask
"how did my video do"), and top up
the board to its next 30 days from the Game Plan
(`${CLAUDE_PLUGIN_ROOT}/skills/yt-board/references/thirty-day-mapping.md`, the rolling rule — the Monday Kickoff
does the same every week). Push via `attraction-brain-sync` and say the save happened, or that it did not.
Remind them of the one paste: the pinned comment from the SEO package (the guide's funnel URL + "comment GUIDE").
For an interview, move its `memory/interview-pipeline.md` row to Published and hand the guest their three
distribution sentences (`yt-interview` Step 6).

## Step 9 — After it's out: the Reels, the posts, the conversations
- `yt-repurpose` writes the pack from the script or transcript — the three Shorts moments, the carousel spec, the
  story frames, the email to the member's agent list, the blog post, the three conversation starters — every ask
  one of the two CTAs in the law's shape, and its content-log rows. Written assets only.
- **The Reels, the carousel and the stories** are then the short-form system's (on their machine since Week 4) —
  hand by phrase, with this video's title: *"say 'script my attraction reels from [title]', or 'attraction
  carousel from [title]', or 'attraction stories from [title]'"*. The first Short is the moment the edit flagged.
- **The conversation starters** go to the sales system *"when it arrives — until then they sit in your ideas
  file"* (`yt-repurpose` appends them there).
Then: *"next week, say 'what's my next attraction video' and we pick from the plan — or wait for Monday: your
Kickoff drafts it onto your board for you."*

## Compliance (3-state — never a stop, never a detour)
`identity/compliance.md`'s first line, `Status:` (read at Step 0). **`unset`** → make the whole video package
anyway: the script, the thumbnail sheet, the title and description are written, delivered and saved, each **stamped
"hold until your compliance basics are set"** (the line under the document's title; the disclosure block's place
kept as one bracketed line, never invented), and the member is told ONCE, at the close of the chat — never in the
middle of a step: *"One thing before this video goes out: say 'paste my compliance link' — two minutes — so your
brokerage's wording is on it."* **`set`** → apply, and remind once at the close to confirm with the brokerage.
**`confirmed`** → apply. Never "if empty, proceed" without the stamp and the line; never a hand-off to the
compliance skill mid-video. Apply, in every state = the two cardinal rules · no compensation figures · the former
brokerage unnamed · the brokerage name and license as the file says (or their held place) · a named agent only
with consent · nothing that promises the member's time per partner.

## Rules
- One step at a time, each stated and built; "your turn" only on a fact the Brain cannot hold (the live link at
  publish), one at a time; no file paths, skill names or task ids in front of the member.
- Never post, publish, send, or schedule. Never invent a view count, a stat, or a quote. Every CTA quotes the kit.
- Done = the folder holds Script · Thumbnail Brief (the thumbnail sheet) · SEO Package · (Lead Map) · the written
  repurpose pieces, the card page is in the locked order, the content-log row is Published, the Brain is pushed.
