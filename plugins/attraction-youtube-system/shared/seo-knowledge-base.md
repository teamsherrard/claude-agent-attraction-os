# SEO Knowledge Base — YouTube for agent attraction

Distilled from current YouTube SEO mechanics, re-keyed to what **real estate agents** search when they are
deciding who to learn from and who to partner with. The **SEO Engine** (`yt-seo`), **Ideation**, and the
**Game Plan** apply this. **The attraction doctrine wins where they differ**
(`${CLAUDE_PLUGIN_ROOT}/shared/attraction-youtube-doctrine.md` §9 titles and thumbnails, §10 CTAs and
descriptions, §11 the bingeworthy channel, §14 measurement, §15 what never goes public).

## Ranking factors (priority order)
1. Watch time · 2. Audience retention · 3. CTR (thumbnail + title) · 4. Engagement (comments, shares, saves,
subs) · 5. Metadata relevance · 6. Search-intent satisfaction. YouTube ranks on **satisfying intent, not keyword
density**; a majority of views come from recommendations, and CTR + retention decide reach. Mike's three
(`/94`): impressions · click-through rate · average view duration.

## What agents search (classify every video)
- **Informational** — "how to [outcome] as a real estate agent", "how does rev share work", "what is a cloud
  brokerage", "how to choose a sponsor", "should I join a team or go solo" → the Problem and Model buckets; most
  common and most valuable.
- **Commercial / comparison** — "[brokerage] review", "[brokerage] vs [brokerage]", "best brokerage for new
  agents [year]", "is [brokerage] worth it" → the Model bucket; high intent, cardinal rules apply (facts only,
  Mike's comparison warning).
- **Transactional / decision** — "join [brokerage]", "[brokerage] sponsor", "how to switch brokerages", "[brokerage]
  onboarding" → the Model bucket; the bottom of the funnel; book-a-call CTA first in the description.
- **Navigational** — the member's name, their organization's name, "[name] YouTube" → the channel page and the
  about section must answer it (`yt-setup`).
- **Career-stage** — "first year real estate agent tips", "real estate agent not making money", "how to get
  your first listing", "real estate agent burnout", "real estate agent part time" → the Situation bucket.
Favor **long-tail** (3+ words): less competition, better-fit viewers. A new channel lives on long-tail.

## The agent-search keyword library (swap in the member's niche, model, and avatar)
- **Brokerage and model:** "[brokerage] explained", "[brokerage] review [year]", "[brokerage] vs [brokerage]",
  "should I join [brokerage]", "[brokerage] for new agents", "how does revenue share work", "rev share real
  estate explained", "cloud brokerage vs traditional brokerage", "how to choose a sponsor [brokerage]",
  "questions to ask a sponsor", "[brokerage] pros and cons", "do not join [brokerage]"
- **Switching:** "how to switch brokerages", "changing brokerages as a real estate agent", "what happens to my
  listings when I switch brokerages", "leaving my team real estate", "should I leave my brokerage"
- **Career stage:** "new real estate agent tips", "first 90 days real estate agent", "real estate agent not
  getting clients", "part time real estate agent", "real estate agent plateau", "how to scale a real estate
  business", "real estate team vs solo"
- **Niche skills (the member's known-for):** "[niche] for real estate agents" (social media · YouTube ·
  Instagram · AI · lead generation · listings · luxury · open houses · database · video), "[niche] real estate
  agent [year]", "how to get leads [niche]"
- **Future / leverage:** "passive income for real estate agents", "how to build a real estate team", "real
  estate agent exit strategy", "agent attraction real estate", "building an organization real estate"
- **Interviews (searchable angle):** "[outcome] part time real estate", "[guest's niche] real estate success
  story", "how [type of agent] closed [N] deals"
Mike's rule holds here too: never broad single words ("realtor", "real estate"); video- and
niche-specific phrases only.

## Titles (doctrine §9 is the source of truth)
Use the seven formulas (§9) and the psychology of the click: curiosity · emotion · clarity; bold and emotional
beats complex and clever. Then the mechanics:
- **Front-load the primary phrase** in the first ~30 characters; **50–65 characters** (one promise, never two
  ideas stapled with a colon).
- "real estate agent(s)" / "as a real estate agent" / the agent type when the search needs it — the viewer is
  an agent, and the phrase is what they type.
- Numbers lift CTR; `(year)` on model and "explained" videos so the yearly remake ranks (`/96`).
- 1–2 honest power words at most (truth · honest · exact · mistakes · explained). Never clickbait you don't deliver.
- Avoid: the phrase at the end, > 70 characters, clever-but-unsearchable, two ideas in one title, a brokerage or
  person named negatively, any compensation figure or earnings implication.
- Dated model titles get re-titled yearly; the "why I switched" and "N months in" videos get their year updated
  (`/92` — the publish date proves the history).

## Description (doctrine §10 is the source of truth)
- **Line 1 = the book-a-call link** ("Book a private one-on-one call: [link]") — above the fold, before anything.
- **Line 2–3 = the resource** (the lead magnet / playbook / free guide link; until Week 6 builds one, the
  community or the call again) and one contact line if `operations.md` lists it.
- Then a **150–300 word** summary in the member's voice, written for the viewer: who it's for, what they'll get,
  the niche phrase 2–3×, secondary phrases once each, natural language. **No compensation figures. No brokerage
  as the pitch** — the brokerage name appears where `compliance.md` requires it (the disclaimer block), not as
  the ask.
- **Chapters** that are descriptive and search-friendly ("How rev share actually works" not "Part 2").
- **Related videos** — the next logical video and the lane's playlist (§11), then 3–5 hashtags, then the
  compliance stamp (brokerage name and license display as required, the disclaimer verbatim, the income
  disclaimer only if earnings were mentioned, the AI-likeness line on clone content).
- **Pinned comment:** the resource link + one question that invites agents to comment their situation (comments
  are a ranking signal and a lead source for `yt-leads`).

## Tags (not a meaningful lever — don't oversell them)
A short, specific set in rough priority: the exact primary phrase · one variation · the long-tail version · 3–5
secondaries (the niche phrase, the model phrase, the avatar phrase). 2–5 words each. Never single generic
words, never a competitor's name as a tag, never misleading.

## Thumbnails (doctrine §9 is the source of truth)
This plugin writes **thumbnail text** (3–5 words, different from the title) and the brief for
`ds-thumbnail-layout` in Claude Design via `yt-thumbnail` — the member's face with a real expression, branded
contrasting colours, simple, visuals that support the title without repeating it. Three per video; let YouTube
test. Interview thumbnails: both faces, the transformation in 3–5 words. Model thumbnails: the model's name is
fine, numbers are not.

## Long-tail generation (append to the primary phrase)
`for new agents · for real estate agents · in [year] · explained · step by step · without [cold calling · paying
for leads · a team] · part time · in a small market · honest review · the truth`

## Channel-size strategy
- **Small (< 10K subs):** long-tail phrases, the member's niche + "for real estate agents", model component
  videos ("how [component] actually works") — the default for a new attraction channel.
- **Medium (10K–100K):** add medium-competition phrases ("[brokerage] explained", "should you join [brokerage]").
- **Large (100K+):** high-volume and branded series terms ("[model] explained [year]").

## Hashtags
Long-form: **3–5** (the niche phrase, "realestateagent", the model phrase, the avatar phrase). Short-form clips
from `yt-repurpose`: #Shorts + 2–4 niche + 1–2 timely.

## Advanced (engagement + watch time)
- Chapters → key moments in Google and better retention. Accurate captions (upload an SRT) → a clean
  transcript the algorithm and AI assistants read. Playlists per lane (one per bucket) → auto-play next, longer sessions. End
  screens (last 5–20s) → the next video and the playlist; cards → the resource mid-video. Reply to every
  comment; `yt-leads` triages them.
- **AI search:** Mike's point in `/91` — agents now ask AI assistants "best sponsor at [brokerage]" and
  "[brokerage] explained," and videos get cited. Accurate captions, clear on-screen text (held 1–3 s), a
  consistent entity line (the same name + niche + organization phrasing across the channel about section, the
  description template, and the member's profiles — reuse the Brain's bios), and consistent topical focus are
  what get a channel into those answers.
- **The yearly remake:** model and "explained" videos get remade or re-titled every year (`/96`) — the compounding
  deposit that keeps the member the go-to resource for their model.
