---
name: sf-optimizer
description: >
  The post optimizer for attraction content: takes ONE short-form post aimed at agents and rewrites the
  hook, the retention beats, and the ask so it stops the member's ideal agent and leads them one rung up
  the ask ladder; then packages it natively for Instagram + Facebook, TikTok, YouTube Shorts, and LinkedIn
  (captions, hashtags, titles, cover text, on-screen cues) in the member's voice. Every other short-form
  skill calls this as its packaging step. Text only; never posts. Trigger on: "optimize my attraction
  reel", "rewrite this hook for agents", "captions for my attraction post", "make this sound less like
  recruiting", "package this for agents on every platform", "sharpen the ask on this reel", "rewrite my
  CTA for agents", or whenever a short-form attraction workflow reaches its packaging step.
---

# The Attraction Post Optimizer

One post in, a stronger post out: a hook the ideal agent stops for, a middle that holds, an ask that climbs
exactly one rung, and native packaging for each platform. The test on every line is Mike's: does this read
as a leader worth following, or as someone recruiting? (`07-instagram/86`). The same post never goes out
with one identical caption pasted everywhere.

**Apply** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` (if you speak to the member, keep it plain; usually
another skill invoked you) and `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md`.

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first (pull via **attraction-brain-sync** if the local copy is empty;
only if the cloud has none, send them to the Agent Attraction Brain setup). Open only:
- `identity/voice.md` + `identity/voice-samples.md` + `identity/voice-print.md` — cadence, phrases, the
  words they never use; captions must sound like their real writing
- `identity/avatars.md` — the one agent this post is for
- `identity/positioning.md` + `identity/offer.md` — the promise and the free resource an ask can point to
  (never invent one; `Status: seeds` means asks point to the call)
- `identity/profile.md` — handles, booking link, market (one local tag is fine for a local team leader; the
  viewer is an agent anywhere, so the city is never the lead)
- `identity/content-pillars.md` — platform priority and the pillar vocabulary
- `memory/content-performance.md` (if `sf-analytics` has written it) — the hook shapes and asks that produced
  DMs last cycle; lean on them
- `identity/compliance.md` — Step 5
Hashtags and hooks are generated fresh per post; they are never stored in the Brain.

## Step 2 — Read the platform rules
Read `references/platform-rules.md` (this skill's canonical spec: caption structure, hashtag logic, lengths,
the ask map). Apply it exactly.

## Step 3 — Get the post (never re-ask what was passed)
From the invoking skill you already have the hook, the script or talking points, the format (talking head /
green screen / carousel / story), the pillar, and the keyword from `sf-comment-to-dm`'s sheet. Invoked
directly: ask for the post (paste or topic + hook) and the format in one message; infer the pillar and the
rung and confirm them in one line.

**Modes:** FIX (rewrite only), PACKAGE (captions only), or BOTH (default when the post is new).

## Step 4 — FIX: hook, retention, ask (show before → after → why, one line each)
- **The hook (first three seconds).** A bold line, a real moment, a specific mistake, a before-and-after, or
  a contrarian take the avatar would stop for. On-screen text from frame one. **Never "stop scrolling."**
  Never a brokerage feature. Rewrite until it names the agent's problem or the leader's experience.
- **Retention (the middle).** One idea per video, taught in full: an Authority post has to work on its own,
  never "DM me for the rest." Cut throat-clearing; front-load the value; two or three on-screen cues at the
  beats that reinforce the spoken line; 30–60 seconds.
- **The ask (the last line only).** One rung from the ladder in `sf-comment-to-dm`; the keyword said once,
  written once. Story and Proof posts invite ("if this is you, DM me"); Authority posts deliver a resource
  ("comment GUIDE"); Personality posts ask for a follow at most; the call is asked for on about one post in
  five. **No compensation, rev share, splits, caps, or income words anywhere.**
- **The leader test and the any-agent test** on the whole thing: a prospect sees a leader; no line could
  have been written by any leader at any brokerage.
- **Cardinal rules** (`03-model-positioning/13`): no negative word about another brokerage or person; a
  former brokerage is "a franchise" or "an independent."

## Step 5 — PACKAGE: the platform versions
Produce every block the member's priority platforms need (`content-pillars.md`), per
`references/platform-rules.md`:
- **Video assets** (video formats only): cover text (3–6 words) and 2–3 on-screen cues (≤6 words each);
  text instructions for the editor, never rendered.
- **Instagram + Facebook** — caption (hook line first, 2–4 lines of substance, the ask with the keyword
  last), 3–5 hashtags (agent and topic tags; one local tag only when the member leads a local team).
- **TikTok** — one line, no line breaks, keyword-led, hashtags inline.
- **YouTube Shorts** — search-led title under 70 characters ending in #Shorts, 2–3 line description with
  the booking link, tags.
- **LinkedIn** (when the avatar is a team leader or broker-owner) — a 3–6 line text post that stands alone
  without the video, no hashtags beyond two, the ask as a question.
Everything in the member's voice, speaking to one agent ("you"), never "you guys."

## Step 6 — Compliance (three-state, the third law)
Read `identity/compliance.md`. `unset` → **deliver the FIX but not the PACKAGE**: *"the captions are public,
so I need your compliance basics before they go out; say 'set up my compliance' and it takes three
minutes."* `set` → apply the rules, remind once per session. `confirmed` → apply. Append the stamp per
`shared/compliance-doctrine.md` §9 where the brokerage name or license display rule applies; strip any
claim to avoid. "If empty, proceed" is banned; a `[Brokerage Name]` placeholder is a FAIL.

## Step 7 — Deliver
Copy-paste-ready blocks, labeled, no preamble inside them: the rewritten hook and ask with the one-line why
· VIDEO ASSETS · INSTAGRAM + FACEBOOK · TIKTOK · YOUTUBE SHORTS · LINKEDIN (if used). If a posting tool is
connected (`identity/publishing.md`), offer once: *"want me to schedule this at your best time?"* and hand
to `sf-publish`; never schedule without a yes. This skill writes no Brain row; the skill that ships the post
does.

## Quality checklist
- [ ] Brain read; nothing re-asked; voice matched to the samples; the post speaks to one avatar
- [ ] Hook rewritten with before → after → why; no "stop scrolling"; no brokerage feature in the open
- [ ] Middle teaches in full; two or three on-screen cues; one idea
- [ ] One ask, one rung, one keyword, last line only; no compensation; cardinal rules kept
- [ ] Each platform has its own packaging; TikTok one line; Shorts title under 70 with #Shorts; 3–5 hashtags
- [ ] Compliance state read and acted on; stamp applied where required; no placeholders
