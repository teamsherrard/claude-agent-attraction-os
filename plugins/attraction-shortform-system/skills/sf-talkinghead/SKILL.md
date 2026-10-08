---
name: sf-talkinghead
description: >
  Attraction Reels — 30–60 second talking-head scripts for the agents the member attracts, across the five
  pillars (Authority · Perspective · Story · Proof · Personality) and Mike's four content types (value,
  behind-the-scenes leadership, personal brand, storytelling). Three modes: a topic list from the member's
  pillars; ready-to-film scripts (hook three ways, word-for-word plus a bullet version, shots, captions) that
  pull a real story from the story bank and end on one rung of the CTA ladder with the keyword; and the 30-day
  calendar (2 attraction · 2 authority · 1 story a week, batch days). Built for batching. Text only. Trigger
  on: "attraction reel", "reel for agents", "script my attraction reels", "script my first attraction reel",
  "talking head for agents", "script this week's agent reels", "my 30-day attraction calendar", "attraction
  content calendar", "plan my month of attraction reels", "what should I film for agents", "hooks for my
  attraction reel".
---

# Attraction Reels — Talking Head

The member, talking to camera, to one agent — teaching, taking a stand, telling their story, showing proof, or
just being themselves. This is the batchable format: hand them topics, script the ones they choose, lay out the
month, and they film several in one sitting.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — plain, warm, never technical; the member,
never "the agent". **The doctrine** is `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` — lazy-load §5–§9 at
the phase that needs them.

Three modes (pick from what they said; never ask which):
- **"What should I film?"** → Phase 1 (the topic list), let them pick.
- **"Script these" / a named topic / "my first attraction reel"** → Phase 2.
- **"My 30-day calendar" / "plan my month"** → Phase 3 (then offer to script the first five).

---

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first (follow its laws), then:
- `identity/content-pillars.md` — the five pillars mapped to them (written by `sf-setup`). **Missing →** this
  plugin's setup hasn't run: *"Let's set your pillars first — say 'set up my attraction short-form'; two minutes,
  then every Reel knows what it's for."* Don't improvise pillars here.
- `identity/publishing.md` — the keyword, what it opens, the weekly mix, cadence, batch day, posting tool
- `identity/avatars.md` — who this is for, their pain in their words, what they'd need to hear
- `identity/journey.md` (incl. `## Why join me` if written) · `identity/strategy.md` — the story beats, the known-for
- `identity/positioning.md` — the one line "why I'm here"; what stays for the private call (never in a Reel)
- `identity/voice.md` + `identity/voice-samples.md` — tone + their real phrasing
- `identity/voice-print.md` — their SPOKEN voice: scripts are read aloud, so write for the ear in their cadence
  and signature phrases (empty → voice.md alone; never fabricate)
- `identity/story-bank.md` — a real story matching the pillar, avatar, and pain; weave it in; **stamp its
  Used-where** after delivery (the one line this skill writes there). Empty → write without one; never invent
- `identity/proof.md` — wins with consent for Proof Reels (first name / initials otherwise)
- `identity/offer.md` — the resource for the Resource rung (Status `seeds` → fall back to the free thing they give
  today or "book a call"; never demand the Week 2 offer)
- `identity/compliance.md` — the third law, three-state
- `memory/content-log.md` — what's covered; which pillar is light this week/month
- `memory/ideas.md` (tags `shortform`, `story`) — the member's own ideas go to the TOP; mark `used` once scripted
- `memory/objections.md` — an objection heard this month is a Perspective Reel waiting to happen
- `memory/content-performance.md` — what worked (the Friday ledger from `sf-analytics`); lean on it for hooks,
  pillars, and rungs. Skip if it doesn't exist yet

**Read the Brain; never re-ask what it knows.** If `~/attraction-brain/` is missing, pull it with
`attraction-brain-sync` (never assume no Brain). Only if the cloud has none: "set up my attraction brain."

## Step 2 — Read the reference files (at the phase that needs them)
1. `references/topic-guide.md` — building the topic list by pillar, balancing from the log
2. `references/script-guide.md` — the hook ×3, the 30–60s script, the bullet version, the shots, the CTA rung
3. `references/calendar-guide.md` — the 30-day calendar, the weekly mix, the batch plan

---

## Phase 1 — The topic list (by pillar, balanced from the log)
**Read `references/topic-guide.md`.** Produce ~8–10 topics the member can choose from: the member's own ideas
first (from `ideas.md`), then the pillar they're lightest on this month, then the rest — never more than three
from one pillar. Each topic: a working **hook** (one line) · the **pillar** · **who it's for** (the avatar, one
line) · the **story or proof it can carry** (a story-bank hook, a win with consent, or "none — straight teach")
· the **rung** it ends on · one line of **why this is strong for you**. Speak to an agent's *problem*, never a
brokerage feature. Present simply:
> "Here are strong ones for this week — I've leaned on [pillar] because you've been light there. Tell me the
> numbers you want to film and I'll script them. Your turn."
**If they're unsure or say "you pick"** (house rules #8 + `${CLAUDE_PLUGIN_ROOT}/shared/advisor-playbook.md`):
choose the top 3 yourself — one line of why each — and offer to script them now.

## Phase 2 — Scripts (for the chosen topics; default five, or the one they named)
**Read `references/script-guide.md`.** For EACH Reel, use these exact section names:
- **THE BRIEF** — pillar · for whom · story used (hook from the bank, or none) · rung + keyword.
- **THE HOOK — 3 ways** — three options, each sayable in one breath (~8–12 words), styles labelled (question ·
  contrarian · number/stakes · mistake · callout · curiosity-gap — never three of the same), the strongest marked
  with one line why. The first word is the hook. Never "stop scrolling", never "hey guys", never credentials first.
- **THE SCRIPT** — word-for-word, written for speech, **30–60 seconds (~80–150 words, show the count)**. Shape:
  hook → the turn → 2–3 beats of real substance (the story's point, the teach, the take, the proof) → the CTA
  line with the keyword, said plainly. Every line sayable in one breath; in their spoken cadence.
- **THE BULLET VERSION** — the same Reel as 5 riff beats (hook and CTA word-for-word). Most members film from
  this — give it equal weight.
- **THE SHOTS** — one line per beat: where to stand, what to show, the one b-roll to grab (a screenshot of the
  call for Proof, the kitchen table for Story — simple, phone-filmed).
- **THE CTA** — the rung, in their words, with the keyword: *"Comment **PARTNER** and I'll send you the whole
  thing."* One rung per Reel; the call only after a conversation; never the model by DM.
- **THE CAPTIONS** — hand hook + script + format `talking head` + pillar + rung + keyword to the optimizer's
  rules (`${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md`): Instagram + Facebook caption
  with the CTA line and 3–5 hashtags · TikTok one-line · YouTube Shorts title/description/tags · cover text + 2–3
  on-screen cues. Do not write your own hashtag rules here.
After all Reels: **THE BATCH NOTE** — which to film in one session (same outfit, same spot), and the one to post
first. A **Story** Reel pulls its story from the bank, told in their words, former brokerage never named; a
**Proof** Reel names an agent only with consent on file.

## Phase 3 — The 30-day calendar (lives here)
**Read `references/calendar-guide.md`.** Twenty Reels, four weeks of five, in the member's weekly mix (default
**2 attraction · 2 authority · 1 story** — attraction = Proof + Personality, authority = Authority + Perspective)
plus "stories daily" as a standing line. Each entry: # · day · hook · pillar · for whom · story/proof carried ·
rung + keyword. Week 1 establishes who they are (one Story Reel, one Authority on the known-for, one Proof, one
Personality, one Perspective). The member's own ideas and this month's objections land early. Then **THE BATCH
PLAN** (which sessions, how many hours — Mike's Monday-plan / Tuesday-record / Wednesday-edit rhythm, or
alternate Saturdays) and **THE THREE TO FILM FIRST**. Close: *"Pick your first five and say 'script these'."*
(The ongoing routine is `sf-weekly-routine`; film-day logistics are `sf-batch-publish`.)

## Phase 4 — Compliance pass (third law, three-state)
`identity/compliance.md`: `unset` → the scripts stay in chat as private drafts, with the plain line that
nothing goes out until compliance is set; `set` → apply + remind once; `confirmed` → apply. Apply: brokerage
name/license as the file says; **the two cardinal rules** (`03-model-positioning/13`); no compensation (splits,
caps, stock, rev-share, income); no earnings claims; no "#1/best" without a source; consent on any named agent;
former brokerages unnamed; any real-estate example fair-housing safe. Strip or rewrite; never ship risky lines.

## Phase 5 — Deliver
Clean copy-paste packages, friendly chat around them, short. Offer, in one line each and only where it applies:
the Riverside edit (*"record it and say 'edit my reel' — captions, clean cut, done"*, `studio-reel`); scheduling
through their tool per `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` — only with explicit approval; the
content board (house rules #10).

## Phase 6 — Save + log + push
For each scripted Reel (or the calendar):
1. **Save the doc** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` — rendered `.docx` to
   `03 · Content/Short-Form/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Reel · [Short Topic]` (a batch:
   `· Reels · [Batch name]`; the calendar: `[YYYY-MM] · 30-Day Calendar`).
2. **Log it:** append one row per Reel to `~/attraction-brain/memory/content-log.md` in the locked shape:
   `| [date] | Instagram · TikTok · Shorts · FB | reel | [Pillar] | [talking head] [hook] | [avatar] | [story hook or —] | [rung · KEYWORD] | Scripted | |`
   (Calendar entries log as `Idea`.)
3. **Stamp** the story's `Used-where` in `identity/story-bank.md`; flip any `ideas.md` row used to `used`.
4. **Push** (write → push → verify). Then: *"Saved your [N] Reels to your workspace (Content → Short-Form →
   [month]) and logged them so we never repeat a story."* If a save fails: say it's not saved, keep it visible,
   retry once, stop.

---

## Quality checklist
- [ ] Brain read; pillars from `content-pillars.md`; nothing re-asked
- [ ] Topics balanced by pillar from the log; member's own ideas first; every topic speaks to an agent's problem
- [ ] Each Reel: brief · hook ×3 (mixed styles) · 30–60s script with word count · bullet version · shots · one rung + the keyword
- [ ] Sounds like them (`voice-print.md`); talks to one agent ("you"); the delete / any-agent / so-what tests pass
- [ ] Story pulled from the bank (never invented), former brokerage unnamed, Used-where stamped; Proof only with consent
- [ ] No compensation, no earnings, no negative word about any brokerage or person; compliance three-state applied
- [ ] Captions via the optimizer rules; the CTA line carries the keyword
- [ ] Calendar: 20 Reels, 4 × 5, the weekly mix honoured, stories daily, batch plan, three-to-film-first
- [ ] Saved to `03 · Content/Short-Form`, logged in the locked row shape, pushed; text only
