---
name: yt-repurpose
description: >
  The Repurposing Engine for the Agent Attraction YouTube System (Week 5) — a long video becomes
  clip scripts and conversation starters. From the script or transcript it writes 3 clip scripts the
  member films and 3 conversation starters (openers the member sends to agents on their Top 50),
  plus 1 email only when the member has a list; a carousel, story frames or a blog post only on the
  member's own words. Every ask is one of the two CTAs in Mike's shape. Written assets only. The
  three clip scripts are queued so the Monday short-form plan fills the week's Reel slots with them
  (two a week at most), never extra posts. Logs the derived pieces in the content log. Compliance
  gate before anything public; no compensation numbers anywhere. Trigger on: "repurpose my
  attraction video", "repurpose this interview", "turn my agent video into posts", "shorts from my
  attraction video", "conversation starters from this video", "repurposing pack for this attraction
  video", "clips and posts from my model breakdown".
---

# Repurposing Engine — one recording, every asset, plus the conversations

Long-form earns the trust; the clips, posts, and emails carry it everywhere else; the conversation starters
turn it into agent conversations (the long-form cohort doc: "every video becomes conversation starters").
Writing only — no editing: nothing here is cut from the video. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`,
§8 (the video structure) and §10 (the two CTAs) of `${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`,
and `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. **Two CTAs, in the law's shape, on every piece:** the guide
(*"[what the guide holds, one clause]. Comment GUIDE and I'll send it."* — the funnel URL where a link can go) on
most pieces; the call (join register — `Join-gated package allowed: yes` or `unknown` — *"If you want my help
running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."*;
open register — `no` — *"I'll walk you through it, free, no strings."*) on about one in four and on every proof
piece; the exact lines from the Week 3 Kit's chapter 7 CALLS TO ACTION table (`exports/week3-kit-*.txt`, newest;
absent → the law's sentences on the same shapes). **Two guards:** the lessons, the templates and the community
are named only when `identity/offer.md → ## Value stack` lists them — an offer still at seeds, or no kit on file →
the plain line, *"If you want my help with this, it's free. [the booking line]."*; and the guide ask is written only
when `memory/magnets.md → ## Current magnet` holds a guide — never "comment GUIDE" for a guide that does not
exist. Never the brokerage as the reason; compensation never; nothing promises the member's time per partner — no
standing one-to-one, no chat group, no weekend beside them, no response time. To the member: plain words; other
plugins by condition or by phrase, never by name; the editor is "your AI Editing Studio"; and what this skill
writes for Reels is always "clip scripts" — words to film — never "clips", which a member hears as pieces already
cut from their video.

> **One chat = one video.** Normally Step 9 of `yt-make-video` — after publish, on the member's Yes. For a video made outside the
> system, run it in that video's chat with the transcript pasted or the editor's section map.

## Input
The script or transcript (the editor's section map and its flagged best 30–45s when there is one), the video
link, and the Brain — `brain.md`, then only three more files now, the rest at the piece that uses them:
`identity/compliance.md` (the first line, `Status:`), `identity/voice.md`, `memory/content-log.md` (this video's
row, written at script and updated at publish — the pillar, avatar, story, and CTA every derived row inherits).
**Which video:** the one this chat is about; in a fresh chat with no title given, the newest YouTube row at
`Published` in the content log, said in one line. A video made in the system is never asked about — its folder
holds the script and its row holds the link. A video made outside it: *"Paste the video's link and its
transcript, and I'll write the pack."*
**Opened later:** the clip scripts (1) → `identity/avatars.md` (the agent's question or fear the hooks open on) ·
the asks → `identity/offer.md`'s header (`Join-gated package allowed:` — the register) and its `## Value stack` ·
`exports/week3-kit-*.txt` (newest — the CALLS TO ACTION table) · the keyword from `identity/publishing.md`'s
`Keyword:` line first (`GUIDE · [the offer's word]`), `content-pillars.md` second · the resource
(`memory/magnets.md → ## Current magnet` — the guide, GUIDE, the funnel URL) · the email (2) →
`memory/list-growth.md` (read only — the list tool and the list size) · the conversation starters (3) →
`memory/top-50.md` (read only) · the clip queue (at Save) → `memory/content-calendar.md` (this video's row in
`## Long-form (YouTube)` — its System ID; the `## Clips from your videos (YouTube)` section) and `config.md` (the
`## Short-Form (Week 4)` block and its `Week Plan task:` line — which closing line the member hears).

## Produce the Repurposing Pack
**What the pack holds — only pieces the member can use:** the three clip scripts and the three conversation
starters, always; one email only when the member has a list to send it to; a blog post only when the member asks
for one. A swipe post and stories are not written here — the short-form system writes its own from the Brain and
does not read this pack; the closing reply names its two phrases once. A piece that is not written gets no band
in the document, no content-log row, and no mention.
1. **Clip scripts (3)** (read `identity/avatars.md`, the register, the kit and the resource file now) — 30–45s
   each (about 75–115 words), three distinct moments (the strongest line, the one tip, the "watch out"), each
   **written word for word for the camera** — the member films it as it stands; nothing is cut from the video
   here. Each: a hook that opens on the agent's question or fear (one line, one breath) → one point → the ask (the
   guide on two, the call on one, the kit's lines) → caption + hashtags (the ask as the caption's last line — the
   kit's caption row). For interviews the three are the member's own to-camera scripts about what the guest
   taught, the first opening on the transformation line; the guest's own best moment is the editor's to cut from the
   recording, on the member's phrase ('cut reels from this') — never re-filmed, never one of these three. They are queued for the week (the clip queue, below) —
   the short-form Monday Week Plan drafts up to two of the week's Reels from them, so they fill Reel slots and
   never add a post; the AI Editing Studio edits what is filmed ("edit my reel"). In the document their band is
   still headed `SHORTS (3)`; to the member they are "your three clip scripts".
2. **Email (1) — only when the member has a list** (`memory/list-growth.md` names a list tool and its list size is
   above zero): subject + a short, warm email to that list — the one takeaway, the link, the ask in the law's
   shape (the guide, or the call on a proof piece). Draft only; never a promise of the member's time. No list on
   file → no email, and nothing is said about it.
3. **Conversation starters (3)** (read `memory/top-50.md` now, read-only) — personal, selfless, value-first
   openers that use this video as the reason to reach out: one for a cold agent, one for an acquaintance, one for
   an agent the member has talked with before. Each is two or three sentences in the member's voice, names a
   specific moment of the video that fits that person's situation, asks one easy question, and never pitches,
   never mentions compensation, never forces a call, never promises the member's time, never assumes a result or
   a past call; where a next step belongs it is the law's shape — the person · their help · free · to run this.
   When the Top-50 holds names, name the rows each fits (read-only — this skill never writes `top-50.md`); an
   empty list → none named, and nothing is said about it.
- **A blog post — only on the member's own words** ("a blog post from this video"): 600–900 words, the video
  embedded at the top, keyword-led H1 from `${CLAUDE_PLUGIN_ROOT}/shared/seo-knowledge-base.md`, H2s from the
  chapters, the two CTAs at the end — the guide with its funnel URL, the call with the booking link in the law's
  shape. Never written by default: the Brain holds no blog for any member.

## The conversation-starter hand-off (by condition)
**To the member, one true line, once** — in the closing reply: *"Your three conversation starters are in your
pack — each is ready to send, in your own words, to an agent you know."* Never "your sales system", never a later
week or a plugin that is not installed: the member sends them, when they choose. (Run inside `yt-make-video`, this
line is the one mention in that chat — that skill adds none of its own.)
- If the Conversion plugin's `cv-conversation-starter` is available in this session, hand the three starters to it
  — each with the video title and the hook (the moment of the video) it came from, plus the video link and the
  matched Top-50 names; it personalizes per channel and relationship state, and the member sends. This skill
  never queues, sends, or tracks sends.
- If it is not installed, append the three starters to `~/attraction-brain/memory/ideas.md` yourself — this skill is
  the file's designated appender for exactly these rows (the OS contract and the file's own header name it) — in the
  locked row shape: Logged = today · Tag `general` · Idea = the starter text + "conversation starter from [video
  title] — [the hook it came from]" · Avatar / pain · Status `open`. Nothing else in that file, ever. Push via
  `attraction-brain-sync` (write → push → verify). This is bookkeeping for a later plugin: nothing reads these
  rows today, and they are never mentioned to the member.

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
ID", a file name or a skill name; always "clip scripts", never "clips"):
- The short-form Monday plan is on (`config.md` holds a `## Short-Form (Week 4)` block — an older `(Week 3)`
  heading is the same block — and its `Week Plan task:` line holds a task id): *"Your three clip scripts are saved
  in your pack. Your Monday Week Plan puts up to two of them into the week's Reels for you to film — they take
  the place of two Reels, so this video feeds your week instead of adding to it."*
- No Short-Form block (or its Monday plan is not on — the line reads `paused` or `later`): *"Your three clip
  scripts are in this pack, ready to film whenever you like."* The rows are written all the same — they wait.

## Rules
- Everything in the member's voice; the same sourced facts as the video — never a new stat, never a number
  from memory; former brokerages unnamed; the two cardinal rules on every line.
- No compensation numbers in any public piece. The email — written only when the member has a list — may
  reference the model only as the video did.
- Two keywords only — GUIDE and the offer's word; every call line in the law's shape from the kit; any older
  keyword of the plugin's own is replaced silently — never announced to the member.
- Nothing is posted, sent, or scheduled here. Posting is the Short-Form system's job, with the member's go. The
  three clip scripts reach it through the clip queue — never by handing the member a phrase to say. A swipe post
  and stories are the short-form system's own, written from the Brain — this pack holds neither; its two phrases
  ("attraction carousel", "attraction stories") are named once in the closing reply, and only when the Short-Form
  block is on file.
- Clip scripts never add posts: they are queued, and the member's week keeps its number (three posts a week by
  default).
- Nothing is cut from the video here and nothing is promised as cut: a "clip" is always a script the member films.

## Save, queue, log, push
Save one **Repurposing Pack — [title] — YYYY-MM-DD** in the video's folder (`03 · Content/Long-Form/`),
rendered through `shared/render_doc.py` per `shared/doc-format.md` — only the bands of the pieces that were
written (no CAROUSEL or STORIES band; EMAIL and BLOG only when written). Then the clip queue, in this order: the
clips' text to `exports/`, the three rows in the calendar's last section (the pack's link in `Script doc` — a
pack that did not save queues nothing). Append `memory/content-log.md` rows in the locked shape for the derived
pieces that were written — the three clip scripts are NOT logged here when they were queued for the Short-Form
System (it logs each once, when the Monday plan drafts it into a Reel slot — one clip, one row, never two); only
when the Short-Form System is not set up do they get three `reel` rows (Platform `Shorts / Reels`) here — then
one `email` row (Platform `Email`) when an email was written and one `blog` row (Platform `Blog`) when the member
asked for one — Topic / hook `[repurposed] from "[source title]" — [angle]`, CTA = the rung and its word (`guide ·
GUIDE` / `call · [the offer's word]`), Status `Scripted`, Link = the pack, Pillar and Avatar from the source row.
(`email` and `blog` are in the Format enum by the coordinator's ruling; the conversation starters are not logged
here — they go to `cv-conversation-starter` or `ideas.md`, above. A clip the Monday plan drafts into a Reel slot
gets its own row there, written by that plan — never a second row here, and these rows are never edited to
match.)
Push via `attraction-brain-sync` — the calendar, the clips' text and the log in one push (the push re-renders
the Brain Board).
**What the member reads — short:** in its own chat the reply opens with the win, *"✓ '[title]' is out — you
filmed it and put it live."* (inside `yt-make-video` the publish reply has just said it — never twice); then what
saved and what did not, in a line; the conversation-starter line (above); only when the Short-Form block is on
file, *"For a swipe post or stories on this topic, say 'attraction carousel' or 'attraction stories' in a new
chat."* (inside `yt-make-video` this is still the one mention — that chat adds none of its own); and the pack's
closing line (the clip queue, above) as the last thing the member reads (inside `yt-make-video`, that chat's one
next-video line follows it). The pieces themselves are in
the document — never pasted into the chat.

## Compliance gate (3-state)
`identity/compliance.md`'s first line, `Status:`, before the pack leaves the chat: `unset` → never a stop: the pack is written, saved and stamped "hold until your compliance basics are set"; **the
three clip rows are NOT queued** (a held draft is never queued), and the closing line is this one instead of the two
above: *"One thing before these go out: say 'paste my compliance link' — two minutes. Then say 'repurpose my
attraction video' again and your three clip scripts go into your Monday Week Plan."* (no Short-Form block, or its
Monday plan not on → the line ends at "two minutes."); `set` → apply, remind once; `confirmed` → apply. No earnings claims,
brokerage name and license display where the file requires it on posts, AI-likeness disclosure on any clone clip.
