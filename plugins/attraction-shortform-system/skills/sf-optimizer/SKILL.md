---
name: sf-optimizer
description: >
  The Week 4 post optimizer for attraction content: takes ONE short-form post aimed at agents and rewrites
  the hook, the retention moments, and the ask so it stops the member's ideal agent and leads them one rung
  up the ask ladder; then packages it natively for Instagram + Facebook, TikTok, YouTube Shorts, and LinkedIn
  (captions, hashtags, titles, cover text, on-screen cues) in the member's voice. Every ask uses one of the
  two keywords — GUIDE for the guide, the offer's word for the invitation — and every caption's call line is
  the kit's CALLS TO ACTION line. Every other short-form skill calls this as its packaging step. Text only;
  never posts. Trigger on: "optimize my attraction reel", "rewrite this hook for agents", "captions for my
  attraction post", "make this sound less like recruiting", "package this for agents on every platform",
  "sharpen the ask on this reel", "rewrite my CTA for agents", or whenever a short-form attraction workflow
  reaches its packaging step.
---

# The Attraction Post Optimizer

One post in, a stronger post out: a hook the ideal agent stops for, a middle that holds, an ask that climbs
exactly one rung, and native packaging for each platform. The test on every line is Mike's: does this read
as a leader worth following, or as someone recruiting? (`07-instagram/86`). The same post never goes out
with one identical caption pasted everywhere.

**Apply** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` (if you speak to the member, keep it plain; usually
another skill invoked you) and `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md`.

**Week 4 rules that bind every package** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **Two keywords, never more.** `GUIDE` delivers the guide (`memory/magnets.md → ## Current magnet`); the offer's
  `Comment keyword:` (`identity/offer.md`) is the invitation. Both sit on `publishing.md`'s `Keyword:` line
  (`GUIDE · [the offer's word]`). No other word in any caption, title or cue, on any platform.
- **The call ask follows the law:** the person · their help · free · to run the method — never the brokerage, never
  compensation. Join register (`offer.md → Join-gated package allowed: yes` or `unknown`): *"If you want my help running
  this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."* Open register
  (`no`): *"I'll walk you through it, free, no strings."* The caption's last line, the pop-up and the end card are the
  kit's CALLS TO ACTION table (chapter 7 of the newest `exports/week3-kit-*.txt`), verbatim.
- **Scalable by design.** No caption promises the member's time per partner — no in-person days beside the member, no
  chat group, no one-to-one calls, no "call me any time". Partners get recorded lessons, templates, the community, the
  weekly group call only when `operations.md` shows the member already runs one.
- **The whole method.** A teaching caption names the step of `offer.md → ## The framework` the post taught and the
  guide as where the rest lives.

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first (pull via **attraction-brain-sync** if the local copy is empty;
only if the cloud has none, send them to the Agent Attraction Brain setup). Open only:
- `identity/voice.md` + `identity/voice-samples.md` + `identity/voice-print.md` — cadence, phrases, the
  words they never use; captions must sound like their real writing
- `identity/avatars.md` — the one agent this post is for
- `identity/positioning.md` + `identity/offer.md` — the promise; `## The framework` (the step a teaching post gave),
  the `Comment keyword:` line (the invitation word), `Join-gated package allowed:` (the register of the call line)
- `memory/magnets.md → ## Current magnet` — the guide (GUIDE): the resource every ask points at; no live guide yet → the
  ask is the call line in the law's shape, never a demanded guide
- the newest `exports/week3-kit-*.txt` — chapter 7's CALLS TO ACTION table: the caption line, the pop-up, the spoken
  line, the end card, the story line, the bio link (the words every package quotes)
- `identity/profile.md` — handles, booking link, market (one local tag is fine for a local team leader; the
  viewer is an agent anywhere, so the city is never the lead)
- `identity/publishing.md` — the `Keyword:` line (`GUIDE · [the offer's word]` — the two keywords), `Platforms
  (priority order):`, the posting tool
- `identity/content-pillars.md` — the pillar vocabulary, the member's takes and topic seeds
- `memory/content-performance.md` (if `sf-analytics` has written it) — the hook shapes and asks that produced
  DMs last cycle; lean on them
- `identity/compliance.md` — its first line, `Status:` (Step 6)
Hashtags and hooks are generated fresh per post; they are never stored in the Brain.

## Step 2 — Read the platform rules
Read `references/platform-rules.md` (this skill's canonical spec: caption structure, hashtag logic, lengths,
the ask map). Apply it exactly.

## Step 3 — Get the post (never re-ask what was passed)
From the invoking skill you already have the hook, the script or talking points, the format (talking head /
green screen / carousel / story), the pillar, and which of the two keywords it carries. The keyword rule, one
sentence: the member has TWO keywords and no more — `GUIDE` (the guide, set in Week 2) and the offer's `Comment
keyword:` (the invitation; e.g. BUYERS) — both on the `Keyword:` line of `identity/publishing.md`; the ManyChat flows
and the keyword sheet (`sf-comment-to-dm`) are written for those two words, so a post never carries a third.
Invoked directly: ask for the post (paste or topic + hook) and the format in one message; infer the pillar and the
rung and confirm them in one line.

**Modes:** FIX (rewrite only), PACKAGE (captions only), or BOTH (default when the post is new).

## Step 4 — FIX: hook, retention, ask (show before → after → why, one line each)
- **The hook (first three seconds).** A bold line, a real moment, a specific mistake, a before-and-after, or
  a contrarian take the avatar would stop for. On-screen text from frame one. **Never "stop scrolling."**
  Never a brokerage feature. Rewrite until it names the agent's problem or the leader's experience.
- **Retention (the middle).** One idea per video, taught in full: an Authority post has to work on its own,
  never "DM me for the rest." Cut throat-clearing; front-load the value; two or three on-screen cues at the
  moments that reinforce the spoken line; 30–60 seconds.
- **The ask (the last line only).** One ask from the ladder in `sf-comment-to-dm`, said once, written once; the
  words from the kit's CALLS TO ACTION table. **The call-ask rule (house rules #13):** (*"Comment GUIDE and I'll send you [the guide, in three words]."*); the invitation — the offer's own word, or the
  kit's call line in the law's shape (*"Want my help running this, free? [the booking line]"* — the person, their
 the 90/10 rule (house rules #13): about one post in ten carries a keyword ask — Comment GUIDE, or the offer's word with the call line in the law's shape; every other post asks only for a follow, a save, a share or a comment on the topic; never two asks on one post
  or a "what you get" piece (a Proof piece may carry the guide instead); never two asks on one post; a kit post keeps
  exactly the ask the kit printed. By pillar: Authority → GUIDE · Perspective → follow, save or share (or GUIDE) ·
  Story → GUIDE or the invitation · Proof → the invitation or GUIDE · Personality → follow. **No compensation, rev
  share, splits, caps, or income words anywhere; nothing that promises the member's time per partner.**
- **The leader test and the any-agent test** on the whole thing: a prospect sees a leader; no line could
  have been written by any leader at any brokerage.
- **Cardinal rules** (`03-model-positioning/13`): no negative word about another brokerage or person; a
  former brokerage is "a franchise" or "an independent."

## Step 5 — PACKAGE: the platform versions
The platforms are never asked (the owner, 2026-11-14): **Instagram + Facebook always** (both — every Reel and every
graphic; Facebook Reels is the same video reposted); the **TikTok and YouTube Shorts blocks ride along** for the
optional reposts of the same video — produced, never asked about, nothing new to make; **LinkedIn only when
`identity/avatars.md` includes team leaders or broker-owners** (the LinkedIn clause of `publishing.md → Platforms`).
Produce the blocks per `references/platform-rules.md`:
- **Video assets** (video formats only): cover text (3–6 words) and 2–3 on-screen cues (≤6 words each);
  text instructions for the editor, never rendered.
- **Instagram + Facebook** — caption (hook line first, 2–4 lines of substance, the ask last — the kit's caption
  line with one of the two keywords, verbatim), 3–5 hashtags (agent and topic tags; one local tag only when the member leads a local team).
- **TikTok** — one line, no line breaks, keyword-led, hashtags inline.
- **YouTube Shorts** — search-led title under 70 characters ending in #Shorts, 2–3 line description with
  the booking link, tags.
- **LinkedIn** (when the avatar is a team leader or broker-owner) — a 3–6 line text post that stands alone
  without the video, no hashtags beyond two, the ask as a question ("want the guide? comment GUIDE").
- **The pop-up and the end card** (video formats, from the same table): the name card in the first three seconds · one
  mid-video pop-up, six words or fewer (`Comment GUIDE · free guide` / `My help, free · [the call in three words]`) ·
  the end card in the last five seconds (the guide's title · Comment GUIDE · the stamp, or the call's headline · the
  booking line · the stamp) — never over the face, never in the lower quarter. The PNGs exist (the Week 3 pop-up set).
Everything in the member's voice, speaking to one agent ("you"), never "you guys."

## Step 6 — Compliance (three-state, the third law)
Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`).
`unset` → **deliver the FIX but not the PACKAGE**: *"the captions are public,
so I need your compliance basics before they go out; say 'set up my attraction compliance' and it takes three
minutes."* `set` → apply the rules, remind once per session. `confirmed` → apply. Append the stamp (house
rules #4 — built from `identity/compliance.md`) where the brokerage name or license display rule applies; strip any
claim to avoid. "If empty, proceed" is banned; a `[Brokerage Name]` placeholder is a FAIL.

## Step 7 — Deliver
Copy-paste-ready blocks, labeled, no preamble inside them: the rewritten hook and ask with the one-line why
· VIDEO ASSETS · INSTAGRAM + FACEBOOK · TIKTOK · YOUTUBE SHORTS · LINKEDIN (if used). With the posting tool connected
(`identity/publishing.md → Posting tool: … connected`), one line in the Yes shape — *"Scheduling this at your best time
— say Yes."* — and hand to `sf-publish`; never schedule without the Yes; the tool not yet connected → `sf-publish`
Job A (the posting tool is not optional; copy-paste only as the fallback line). This skill writes no Brain row; the
skill that ships the post does.

## Quality checklist
- [ ] Brain read; nothing re-asked; voice matched to the samples; the post speaks to one avatar
- [ ] Hook rewritten with before → after → why; no "stop scrolling"; no brokerage feature in the open
- [ ] Middle teaches in full; two or three on-screen cues; one idea
- [ ] One ask, one rung, one of the two keywords (GUIDE · the offer's word), last line only, the kit's line verbatim; the
      call ask in the law's shape; no compensation; nothing promising the member's time per partner; cardinal rules kept
- [ ] Each platform has its own packaging; TikTok one line; Shorts title under 70 with #Shorts; 3–5 hashtags
- [ ] Compliance state read and acted on; stamp applied where required; no placeholders
