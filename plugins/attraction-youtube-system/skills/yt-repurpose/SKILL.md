---
name: yt-repurpose
description: >
  The Repurposing Engine for the Agent Attraction YouTube System — every long-form video becomes clips, posts,
  emails, and conversation starters. From the script or transcript it writes 3 Shorts scripts, 1 carousel
  spec, 5 story frames, 1 email, 1 blog post, and 3 conversation starters (personal openers the member sends
  to agents in their Top-50, handed to the Conversion plugin's cv-conversation-starter by name, or saved to
  the Brain's ideas file if it is not installed). Written assets only — the Riverside Studio cuts the actual
  clips from this pack's chosen moments. Writes the content-log rows for the derived pieces. Compliance gate
  before anything public; no compensation numbers anywhere.

  Trigger on: "repurpose my attraction video", "repurpose this interview", "turn my agent video into posts",
  "shorts from my attraction video", "conversation starters from this video", "repurposing pack for this
  attraction video", "clips and posts from my model breakdown".
---

# Repurposing Engine — one recording, every asset, plus the conversations

Long-form earns the trust; the clips, posts, and emails carry it everywhere else; the conversation starters
turn it into agent conversations (the Week 4 doc: "every video becomes conversation starters"). Writing
only — no editing. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, §8 (the video structure) and §10 (the two CTAs) of
`${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md`, and `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

> **One chat = one video.** Normally Step 9 of `yt-make-video`, after publish. For a video made outside the
> system, run it in that video's chat with the transcript pasted or the Riverside section map.

## Input
The script or transcript (the Studio's section map and its flagged best 30–45s when there is one), the video
link, and the Brain — `brain.md`, then only three more files now, the rest at the piece that uses them:
`identity/compliance.md` (the first line, `Status:`), `identity/voice.md`, `memory/content-log.md` (this video's
row, written at script and updated at publish — the pillar, avatar, story, and CTA every derived row inherits).
**Opened later:** the Shorts (1) → `identity/avatars.md` (the agent's question or fear the hooks open on) · the
invites in 1–5 → `identity/content-pillars.md` (the two CTAs; the keyword itself from `identity/publishing.md`'s
`Keyword:` line first, `content-pillars.md` second) and the resource (`memory/magnets.md → ## Current magnet` first
when it exists, `identity/offer.md` second) · the conversation starters (6) → `memory/top-50.md` (read only).

## Produce the Repurposing Pack
1. **Shorts scripts (3)** (read `identity/avatars.md`, `identity/content-pillars.md`, and the resource file now) — 30–45s each, three distinct moments (the strongest line, the one tip, the
   "watch out"). Each: a hook that opens on the agent's question or fear → one point → the warm invite (book
   a call or the resource) → caption + hashtags. For interviews, Short 1 is the guest's flagged moment with
   the transformation line as the hook. The Riverside Studio's `studio-repurpose` cuts these from the
   recording using the moments named here.
2. **Carousel spec (1)** — 6–8 slides, cover hook → one idea per slide → the CTA slide; design through the
   Short-Form System's `sf-carousel` / the Design Studio's `ds-carousel` (LinkedIn PDF for team leaders and
   broker-owners).
3. **Story frames (5)** — one line each, a sequence: the question · the honest answer · the proof moment ·
   the invite (keyword or link) · the poll or question box. Hand to `sf-stories` if installed.
4. **Email (1)** — subject + a short, warm email to the member's agent list: the one takeaway, the link, the
   invite. Draft only.
5. **Blog post (1)** — 600–900 words, the video embedded at the top, keyword-led H1 from
   `${CLAUDE_PLUGIN_ROOT}/shared/seo-knowledge-base.md`, H2s from the chapters, the two CTAs at the end.
6. **Conversation starters (3)** (read `memory/top-50.md` now, read-only) — personal, selfless, value-first openers that use this video as the
   reason to reach out: one for a cold agent, one for an acquaintance, one for a past conversation. Each is
   two or three sentences in the member's voice, names a specific moment of the video that fits that
   person's situation, asks one easy question, and never pitches, never mentions compensation, never forces
   a call. Name the Top-50 rows each fits (read-only — this skill never writes `top-50.md`).

## The conversation-starter hand-off
- If the Conversion plugin's `cv-conversation-starter` is available in this session, hand the three starters to it
  by name — each with the video title and the hook (the moment of the video) it came from, plus the video link and
  the matched Top-50 names; it personalizes per channel and relationship state, and the member sends. This skill
  never queues, sends, or tracks sends.
- If it is not installed, hand the three starters to `attraction-capture` (it owns `memory/ideas.md`) to append in
  the file's locked row shape — Tag `general`, Idea = the starter text + "conversation starter from [video title] —
  [the hook it came from]", Avatar / pain, Status `open` — so the Daily Debrief and the Week 5 plugin pick them up.
  This skill never writes `ideas.md` itself. Say which happened, in one plain line.

## Rules
- Everything in the member's voice; the same sourced facts as the video — never a new stat, never a number
  from memory; former brokerages unnamed; the two cardinal rules on every line.
- No compensation numbers in any public piece. The email to the member's own agent list may reference the
  model only as the video did.
- Nothing is posted, sent, or scheduled here. Publishing is the Short-Form System's job (`sf-publish`), with
  the member's go.

## Save, log, push
Save one **Repurposing Pack — [title] — YYYY-MM-DD** in the video's folder (`03 · Content/Long-Form/`),
rendered through `shared/render_doc.py` per `shared/doc-format.md`. Append `memory/content-log.md` rows in
the locked shape for the derived pieces — three `reel` rows (Platform `Shorts / Reels`), one `carousel` row
(Platform `Instagram` or `LinkedIn`), one `story` row ("5 stories", Platform `Instagram`), one `email` row
(Platform `Email`), one `blog` row (Platform `Blog`) — Topic / hook `[repurposed] from "[source title]" — [angle]`,
Status `Scripted`, Link = the pack, Pillar and Avatar from the source row. (`email` and `blog` are in the Format
enum by the coordinator's ruling; the conversation starters are not logged here — they go to the Conversion
plugin or `ideas.md`, above.)
Push via `attraction-brain-sync`; say what saved and what did not.

## Compliance gate (3-state)
`identity/compliance.md`'s first line, `Status:`, before the pack leaves the chat: `unset` → draft stays private, plain line that
the rules are not set; `set` → apply, remind once; `confirmed` → apply. No earnings claims, brokerage name
and license display where the file requires it on posts, AI-likeness disclosure on any clone clip.
