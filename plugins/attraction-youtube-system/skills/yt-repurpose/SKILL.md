---
name: yt-repurpose
description: >
  The Repurposing Engine for the Agent Attraction YouTube System (Week 5) — every long-form video
  becomes clips, posts, emails and conversation starters. From the script or transcript it writes 3
  Shorts scripts, 1 carousel spec, 5 story frames, 1 email, 1 blog post and 3 conversation starters
  (personal openers for agents in the member's Top-50 — to the sales system when it arrives, to the
  Brain's ideas file until then), every ask one of the two CTAs in Mike's shape. Written assets only.
  The three clips are queued so the Monday short-form plan fills the week's Reel slots with them
  (two a week at most), never extra posts. Logs the derived pieces in the content log. Compliance
  gate before anything public; no compensation numbers anywhere. Trigger on: "repurpose my
  attraction video", "repurpose this interview", "turn my agent video into posts", "shorts from my
  attraction video", "conversation starters from this video", "repurposing pack for this attraction
  video", "clips and posts from my model breakdown".
---

# Repurposing Engine — one recording, every asset, plus the conversations

Long-form earns the trust; the clips, posts, and emails carry it everywhere else; the conversation starters
turn it into agent conversations (the long-form cohort doc: "every video becomes conversation starters").
Writing only — no editing. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §8 (the video structure) and §10
(the two CTAs) of `${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. **Two CTAs, in the law's shape, on every piece:** the guide
(*"[what the guide holds, one clause]. Comment GUIDE and I'll send it."* — the funnel URL where a link can go) on
most pieces; the call (join register — `Join-gated package allowed: yes` or `unknown` — *"If you want my help
running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*;
open register — `no` — *"I'll walk you through it, free, no strings."*) on about one in four and on every proof
piece; the exact lines from the Week 3 Kit's chapter 7 CALLS TO ACTION table (`exports/week3-kit-*.txt`, newest;
absent → the law's sentences on the same shapes). Never the brokerage as the reason; compensation never; nothing
promises the member's time per partner — no standing one-to-one, no chat group, no weekend beside them, no
response time. To the member: plain words; other plugins by condition or by phrase, never by name.

> **One chat = one video.** Normally Step 9 of `yt-make-video`, after publish. For a video made outside the
> system, run it in that video's chat with the transcript pasted or the editor's section map.

## Input
The script or transcript (the editor's section map and its flagged best 30–45s when there is one), the video
link, and the Brain — `brain.md`, then only three more files now, the rest at the piece that uses them:
`identity/compliance.md` (the first line, `Status:`), `identity/voice.md`, `memory/content-log.md` (this video's
row, written at script and updated at publish — the pillar, avatar, story, and CTA every derived row inherits).
**Opened later:** the Shorts (1) → `identity/avatars.md` (the agent's question or fear the hooks open on) · the
asks in 1–5 → `identity/offer.md`'s header (`Join-gated package allowed:` — the register) · `exports/week3-kit-*.txt`
(newest — the CALLS TO ACTION table) · the keyword from `identity/publishing.md`'s `Keyword:` line first (`GUIDE ·
[the offer's word]`), `content-pillars.md` second · the resource (`memory/magnets.md → ## Current magnet` — the
guide, GUIDE, the funnel URL) · the conversation starters (6) → `memory/top-50.md` (read only) · the clip queue
(at Save) → `memory/content-calendar.md` (this video's row in `## Long-form (YouTube)` — its System ID; the
`## Clips from your videos (YouTube)` section) and `config.md` (the `## Short-Form (Week 4)` block and its `Week
Plan task:` line — which closing line the member hears).

## Produce the Repurposing Pack
1. **Shorts scripts (3)** (read `identity/avatars.md`, the register, the kit and the resource file now) — 30–45s
   each (about 75–115 words), three distinct moments (the strongest line, the one tip, the "watch out"), each
   **written word for word for the camera** — the member films it as it stands. Each: a hook that opens on
   the agent's question or fear (one line, one breath) → one point → the ask (the guide on two, the call on one,
   the kit's lines) → caption + hashtags (the ask as the caption's last line — the kit's caption row). For
   interviews, Short 1 is the guest's flagged moment with the transformation line as the hook. These three are
   the member's **clips**: they are queued for the week (the clip queue, below) — Monday's plan drafts up to two
   of the week's Reels from them, so they fill Reel slots and never add a post; the editor (Plugin 5) edits
   what is filmed ("edit my reel").
2. **Carousel spec (1)** — 6–8 slides, cover hook → one idea per slide → the CTA slide (one of the two asks, the
   kit's words); the Short-Form system turns it into the lean build sheet and the slides ("attraction carousel";
   LinkedIn PDF for team leaders and broker-owners).
3. **Story frames (5)** — one line each, a sequence: the question · the honest answer · the proof moment ·
   the invite (the kit's story lines — *"Reply GUIDE and I'll send it."* · *"Reply and I'll send you the link."*)
   · the poll or question box. The Short-Form system posts the week's stories from these ("attraction stories").
4. **Email (1)** — subject + a short, warm email to the member's agent list: the one takeaway, the link, the
   ask in the law's shape (the guide, or the call on a proof piece). Draft only; never a promise of the member's
   time.
5. **Blog post (1)** — 600–900 words, the video embedded at the top, keyword-led H1 from
   `${CLAUDE_PLUGIN_ROOT}/shared/seo-knowledge-base.md`, H2s from the chapters, the two CTAs at the end — the
   guide with its funnel URL, the call with the booking link in the law's shape.
6. **Conversation starters (3)** (read `memory/top-50.md` now, read-only) — personal, selfless, value-first
   openers that use this video as the reason to reach out: one for a cold agent, one for an acquaintance, one for
   a past conversation. Each is two or three sentences in the member's voice, names a specific moment of the
   video that fits that person's situation, asks one easy question, and never pitches, never mentions
   compensation, never forces a call, never promises the member's time; where a next step belongs it is the
   law's shape — the person · their help · free · to run this. Name the Top-50 rows each fits (read-only — this
   skill never writes `top-50.md`).

## The conversation-starter hand-off (by condition — "when your sales system arrives")
- If the Conversion plugin's `cv-conversation-starter` is available in this session, hand the three starters to it
  — each with the video title and the hook (the moment of the video) it came from, plus the video link and the
  matched Top-50 names; it personalizes per channel and relationship state, and the member sends. This skill
  never queues, sends, or tracks sends. To the member: *"your sales system takes these from here."*
- If it is not installed, append the three starters to `~/attraction-brain/memory/ideas.md` yourself — this skill is
  the file's designated appender for exactly these rows (the OS contract and the file's own header name it) — in the
  locked row shape: Logged = today · Tag `general` · Idea = the starter text + "conversation starter from [video
  title] — [the hook it came from]" · Avatar / pain · Status `open`. Nothing else in that file, ever. Push via
  `attraction-brain-sync` (write → push → verify). The Daily Debrief reads them; the sales system takes the open
  rows and marks them used when it arrives in a later week. Say which happened, in one plain line: *"when your
  sales system arrives it takes these — until then the starters are in your ideas file."*

## The clip queue — the three Shorts land in the week's Reel slots (the owner, 2026-11-14)
A video feeds the member's week instead of adding to it. This skill queues the three Shorts scripts in the Brain's
calendar file, `memory/content-calendar.md`, in its LAST section — this plugin's third section there, after
`## Long-form (YouTube)` and `## Kickoff briefs (YouTube)`, and written by this skill alone:

```
## Clips from your videos (YouTube)
*Appended by the YouTube System's repurposing pack ("repurpose my attraction video"), one row per clip script, never edited afterwards. A clip is QUEUED until a short-form row above carries its System ID in `Carries` (`clip: [System ID]`) — the Monday Week Plan drafts up to two of the week's Reels from queued clips, so a video feeds the week instead of adding to it. Nobody marks a row here as used: the short-form row is the mark.*

| Added | From video | Clip | Hook | Script doc | System ID |
|---|---|---|---|---|---|
```

- **One row per Shorts script — three per pack**, appended below the last row, after the pack is saved. `Added` =
  today (`YYYY-MM-DD`) · `From video` = the video's exact title · `Clip` = `1`, `2` or `3` (the pack's order) ·
  `Hook` = that Short's hook, one line, no `|` · `Script doc` = the saved pack's link · `System ID` = the video's
  System ID plus `-c1` · `-c2` · `-c3`.
- **The video's System ID** is the one on its row in the same file's `## Long-form (YouTube)` section (found by
  title — exact, then near). A video made outside the plan has no row: use `yt-` and its publish date
  (`yt-2026-11-12`; a second one the same day ends `b`).
- **Appended, never edited afterwards — by anyone.** A clip is QUEUED until a row of the short-form table in the
  same file carries its System ID in the `Carries` cell (`clip: [System ID]`); it is USED from then on. That
  short-form row is the only mark: nobody writes "used" here, re-words a hook, or deletes a row. This skill never
  touches the short-form table, `## Week briefs`, or another row of this section.
- **The same video run again** (its System ID is already in the section) → no second set of rows; the pack and
  the clips text below are rewritten, the rows stand as they are.
- **The section is not there yet** (a Brain older than it) → add it at the very end of the file exactly as shown
  above (the Brain template's own words: the heading, its one italic line, the header row and the rule line under
  it), then the three rows; not a byte above it changes. An empty first row the template left (`| | | | | | |`)
  is simply filled. **The file itself is missing** → write no rows (this plugin never
  creates that file); the scripts stay in the pack and the member hears the second closing line.
- **The clips' text, for a Monday run that opens no document:** in the same run write the pack's title line and
  its `SHORTS (3)` band, exactly as the pack has them (SHORT 1 · SHORT 2 · SHORT 3 — the hook, the script word for
  word, the ask, the caption and hashtags), to `~/attraction-brain/exports/youtube-clips-[the video's System
  ID].txt` (the Brain syncs `exports/*.txt`). It sits beside the pack, never instead of it.
- **What happens next is not this skill's work:** the Monday Week Plan (the Short-Form system's, on its schedule
  or on "run my week plan") drafts up to two of the week's Reels from the queued clips — the newest video first,
  clip 1 before 2 before 3 — and puts what those slots held back in the member's ideas. The six designed posts
  and the news slot are never replaced; at least one Reel a week stays the plan's own; a week with nothing queued
  runs as it always did.

**The member hears it once, plainly — the pack's closing line** (a statement, never a question; never "System
ID", a file name or a skill name):
- The Monday plan is on (`config.md` holds a `## Short-Form (Week 4)` block — an older `(Week 3)` heading is the
  same block — and its `Week Plan task:` line holds a task id): *"Your three clips are queued. Monday's plan puts
  them into your Reel slots, two a week at most, so this video feeds your week instead of adding to it."*
- No Short-Form block (or its Monday plan is not on — the line reads `paused` or `later`): *"Your three clip
  scripts are in this pack, ready to film whenever you like."* The rows are written all the same — they wait.

## Rules
- Everything in the member's voice; the same sourced facts as the video — never a new stat, never a number
  from memory; former brokerages unnamed; the two cardinal rules on every line.
- No compensation numbers in any public piece. The email to the member's own agent list may reference the
  model only as the video did.
- Two keywords only — GUIDE and the offer's word; every call line in the law's shape from the kit; any older
  keyword of the plugin's own is retired and replaced, said so in one line.
- Nothing is posted, sent, or scheduled here. Posting is the Short-Form system's job, with the member's go. The
  three clips reach it through the clip queue — never by handing the member a phrase to say; the carousel and
  the stories go by phrase ("attraction carousel", "attraction stories") — it exists by Week 5.
- Clips never add posts: they are queued, and the member's week keeps its number (three posts a week by default).

## Save, queue, log, push
Save one **Repurposing Pack — [title] — YYYY-MM-DD** in the video's folder (`03 · Content/Long-Form/`),
rendered through `shared/render_doc.py` per `shared/doc-format.md`. Then the clip queue, in this order: the
clips' text to `exports/`, the three rows in the calendar's last section (the pack's link in `Script doc` — a
pack that did not save queues nothing). Append `memory/content-log.md` rows in
the locked shape for the derived pieces — the three clips are NOT logged here when they were queued for the
Short-Form System (it logs each clip once, when the Monday plan drafts it into a Reel slot — one clip, one row,
never two); only when the Short-Form System is not set up do the clips get three `reel` rows (Platform `Shorts /
Reels`) here — then one `carousel` row
(Platform `Instagram` or `LinkedIn`), one `story` row ("5 stories", Platform `Instagram`), one `email` row
(Platform `Email`), one `blog` row (Platform `Blog`) — Topic / hook `[repurposed] from "[source title]" — [angle]`,
CTA = the rung and its word (`guide · GUIDE` / `call · [the offer's word]`), Status `Scripted`, Link = the pack,
Pillar and Avatar from the source row. (`email` and `blog` are in the Format enum by the coordinator's ruling; the
conversation starters are not logged here — they go to the sales system or `ideas.md`, above. A clip the Monday
plan drafts into a Reel slot gets its own row there, written by that plan — never a second row here, and these
rows are never edited to match; a carousel or story the member re-makes through the Short-Form system likewise.)
Push via `attraction-brain-sync` — the calendar, the clips' text and the log in one push (the push re-renders
the Brain Board); say what saved and what did not, then the pack's closing line (the clip queue, above) as the
last thing the member reads.

## Compliance gate (3-state)
`identity/compliance.md`'s first line, `Status:`, before the pack leaves the chat: `unset` → draft stays private,
plain line that the rules are not set, and nothing is queued (a private draft is not a clip — the rows are written
when the pack is saved); `set` → apply, remind once; `confirmed` → apply. No earnings claims,
brokerage name and license display where the file requires it on posts, AI-likeness disclosure on any clone clip.
