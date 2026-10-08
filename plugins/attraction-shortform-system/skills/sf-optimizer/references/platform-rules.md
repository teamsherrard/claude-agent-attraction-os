# Platform Rules — packaging an attraction post per platform

The single source of truth for how a short-form post aimed at agents is packaged on each platform. Every
short-form skill in this plugin applies it (through `sf-optimizer`). Update it here and every workflow
inherits the change.

Core principle: **one idea, native packaging per platform.** The hook and the ask are shared; the caption,
hashtags, and metadata are not. The viewer is **an agent, anywhere** — not a buyer, not a seller, not a
local consumer — so keywords and tags are about the agent's problem and the member's niche, never the city
first.

Follows `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md`: 3–5 searchable hashtags on every platform;
captions and hooks never say "stop scrolling"; captions are simple, clear, and end on one ask
(`07-instagram/90`).

---

## Instagram Reels + Facebook Reels
One caption serves both; one Facebook tweak noted at the end.

**Caption structure:**
1. **Line 1 = the hook**, rewritten for reading: the only part most people see before "…more" (~125
   characters). It names the agent's problem or the leader's moment.
2. **2–4 short lines of substance** — the point of the video in the member's voice; one thing the video
   did not say, so the caption earns its read.
3. **The ask, last line** — one rung, one keyword: "comment GUIDE and I'll send it" · "DM me PARTNER" · "if
   this is you, message me" · "follow for the next one."

- **Length:** ~80–160 words. Line breaks between thoughts. Speak to one agent ("you").
- **Emoji:** sparingly, only if it is in `voice-samples.md`.

**Hashtags (Instagram): 3–5, no more.** Blend:
- **1–2 agent-audience tags** — `#realestateagent`, `#realtorlife`, `#newrealtor`, `#realestateteamleader`
- **1–2 topic/niche tags** — the member's lane (`#realestatemarketing`, `#realestatecoaching`,
  `#aiforrealtors`, `#openhousestrategy`)
- **1 local tag, only when the member leads a local team or local brokerage** — `#[City]Realtors`
- Mid-size, searchable tags over million-post giants. No follow-bait. Never a brokerage hashtag that reads as
  a recruiting ad.

**Facebook tweak:** same 3–5 tags; the booking link can be pasted directly; slightly more conversational is
fine. If the post will ever be boosted or run as an ad, note the Meta "Employment" special-ad-category rule
(the Ads note line in `identity/compliance.md`).

---

## TikTok
A search and discovery engine; agents search it like Google.

- **ONE LINE. NO LINE BREAKS.** The posting tools strip them; write one flowing sentence.
- **Keyword-led and conversational** — lead with what an agent would search ("switching brokerages,"
  "real estate agent burnout," "[niche] for realtors"), keep it native, not polished.
- The ask woven in at the end, one keyword, no formal sign-off.
- **Hashtags: 3–5 inline**, lowercase: 1–2 agent-audience (`#realestateagent`, `#realtortok`), 1–2 niche,
  1 broad (`#realestate`) — only one broad tag.
- **On-screen note:** a keyword overlay on the opening frame helps TikTok index the video.

---

## YouTube Shorts
Indexed by Google and YouTube — the SEO play of the four.

- **Title:** search-friendly, keyword-front, under 70 characters, ends with `#Shorts`. Shape: `Why Agents
  Leave Their Brokerage in Year Two #Shorts` · `The DM Script That Books Partner Calls #Shorts`.
- **Description:** 2–3 lines: a keyword-rich sentence restating the point, one line of value, the ask with
  the booking link (links are clickable here). 2–3 natural keywords, never stuffed.
- **Hashtags:** 3–5 in the description including `#Shorts`.
- **Tags** (the separate keywords field): a handful of searchable phrases — the niche, the problem, the
  member's name and organization name.

---

## LinkedIn (team-leader and broker-owner avatars)
LinkedIn is where producers and leaders read; the video is optional there.

- **A 3–6 line text post that stands alone** without the video: the hook as line one, a short story or the
  one tactical point, the ask as a question ("what's your take?" · "want the checklist? comment GUIDE").
- **No more than two hashtags.** Professional tone, still the member's voice. Never a brokerage pitch.

---

## Video assets (video formats only; not carousel)
Produced once per video, for the editor, as text:
- **Cover text** — the bold 3–6 word overlay on the first frame; it teases the payoff, never summarizes.
  Examples: "I almost quit in year two" · "The DM script that books calls" · "What leading 40 agents taught me."
- **On-screen cues** — 2–3 overlays (≤6 words each) at the beats that reinforce the spoken line: the
  mistake, the turning point, the one tactic.
Text instructions only; never rendered here.

---

## The ask map (one rung per post, from `sf-comment-to-dm`'s ladder)

| Pillar | Default rung | The ask |
|---|---|---|
| **Authority** (what I teach) | Resource | "comment [KEYWORD] and I'll send it" (variants GUIDE / GROWTH / SCALE once the sequences run) — tied to a real resource in `offer.md`; seeds only → "DM me and I'll walk you through it" |
| **Perspective** (industry take) | Comment | "agree or disagree? tell me below" · "follow for the next one" |
| **Story** (the journey) | DM | "if this is where you are, DM me PARTNER; happy to share what I'd do" |
| **Proof** (agent wins, culture) | DM | "want to know how [first name] did it? DM me" — permissioned wins only |
| **Personality** | Follow | "follow for the real side" — nothing more |
| **The direct call-rung — at most one post a month** (an OS rule, not a Week 3 lesson) | Call | "if it makes sense, let's talk; link in bio" — never on a Personality post |

Rules: one keyword per post, said once on camera and written once in the caption; the keyword is pinned as the
first comment; every resource ask points to something that exists; **no compensation, rev share, splits, caps,
fees, or income words in any caption on any platform** — those are a call conversation. The keyword rule, one
sentence: The member has ONE primary keyword, chosen once in `sf-setup` (the `Keyword:` line in
`identity/publishing.md`); GUIDE · GROWTH · SCALE · PARTNER are the four sequence names from Mike's ManyChat
templates — per-Reel variants that default to the primary keyword's flow until the member runs those templates
in their own ManyChat. The GUIDE and PARTNER in this file's examples are those variants.

---

## Cross-platform rules (apply to all)
- **Never one identical caption across platforms.** Different lengths, different tag logic, same ask.
- **3–5 hashtags max**, agent and niche first; the city only for a local-team leader.
- **Never "stop scrolling."** Never "join my team." Never a brokerage feature as the hook.
- **Speak to one agent.** Name their problem; the member is the guide, not the hero.
- **Cardinal rules on every line** (`03-model-positioning/13`): no negative word about another brokerage or
  person; a former brokerage is "a franchise" or "an independent."
- **Permission** on any named agent or their numbers (the consent column in `proof.md`; the Testimonial consent
  line in `identity/compliance.md`).
- **Voice first** — read it back against `voice-samples.md`; if it sounds like marketing, rewrite.
- **Compliance last** — the stamp per house rules #4 (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`, built from
  `identity/compliance.md`) where required; `unset` on its first line (`Status:`) means the captions do not ship.
- **Text only** — any visual is described in words for the member's design tool; never rendered here.
