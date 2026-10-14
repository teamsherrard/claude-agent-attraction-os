---
name: sf-talkinghead
description: >
  Attraction Reels: 30 to 60 second talking-head scripts for the agents the member attracts, across
  the five pillars (Authority, Perspective, Story, Proof, Personality) and Mike's four content types
  (value, behind-the-scenes leadership, personal brand, storytelling). Two jobs: a topic list from the
  Game Plan's calendar and the member's pillars; ready-to-film scripts (hook three ways, word-for-word
  plus a bullet version, shots, captions) that pull a real story from the story bank and end on one
  rung of the CTA ladder with the keyword. The 30-day calendar itself lives in the Short-Form Game
  Plan (asked for here, it is updated there). Built for batching. Text only. Trigger on: "attraction
  reel", "reel for agents", "script my attraction reels", "script my first attraction reel", "talking
  head for agents", "script this week's agent reels", "my 30-day attraction calendar", "attraction
  content calendar", "plan my month of attraction reels", "hooks for my attraction reel".
---

# Attraction Reels — Talking Head

The member, talking to camera, to one agent — teaching, taking a stand, telling their story, showing proof, or
just being themselves. This is the batchable format: hand them topics, script the ones they choose, lay out the
month, and they film several in one sitting.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — plain, warm, never technical; the member,
never "the agent". **The doctrine** is `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` — lazy-load §5–§9 at
the phase that needs them.

Three modes (pick from what they said; never ask which):
- **"What should I film?"** → the calendar first (the front door rule below): this week's rows from the Game Plan
  are the list; `sf-ideas` when the week has no rows or they want fresh research.
- **"Script these" / a named topic / "my first attraction reel"** → Phase 2 (setup hands over row 1 of the
  calendar as the topic — one Reel, no question stop).
- **"My 30-day calendar" / "plan my month"** → Phase 3: the calendar lives in the Short-Form Game Plan — hand to
  `sf-gameplan` (UPDATE mode, section 6), then offer to script the first five.

---

## Front door rule
"What should I film this week?" is answered by the member's own plan first: `memory/content-calendar.md`'s rows dated this week (the Game Plan dated them; the Monday Week Plan may already have drafted them — a row at `Scripted` has its script on the board and in the Content folder). When the week has rows, Phase 1 lists them (plus the member's own `ideas.md` rows) and offers to script the ones still at `Idea`. When the week has no rows, say one line — "Let's find this week's five first" — and hand to `sf-ideas` (research + the week's five + the hook bank), or "plan my next 30 days of reels" to map the month.

## Step 1 — Load the Brain (four files; the rest open at the phase that uses them)
Read `~/attraction-brain/brain.md` first (follow its laws), then only these three:
- `identity/content-pillars.md` — the five pillars with their angles and the hooks bank (written by the Game Plan
  inside the short-form setup). **Missing →** this plugin's setup hasn't run: *"Let's set your pillars first — say
  'set up my attraction short-form'; then every Reel knows what it's for."* Don't improvise pillars here.
- `memory/content-calendar.md` — the Game Plan's rows (this week's first; a row carries its pillar, hook, CTA,
  story, and System ID — the script is written against the row and the board card is found by that ID)
- `identity/avatars.md` — who this is for, their pain in their words, what they'd need to hear
- `identity/story-bank.md` — a real story matching the pillar, avatar, and pain; weave it in; **stamp its
  Used-where** after delivery (the one line this skill writes there). Empty → write without one; never invent

Everything else opens at the phase that uses it (each phase lists its own "open now"); a file already open stays
open — never re-read one. **Read the Brain; never re-ask what it knows.** If `~/attraction-brain/` is missing,
pull it with `attraction-brain-sync` (never assume no Brain). Only if the cloud has none: "set up my attraction
brain."

## Step 2 — Read the reference files (at the phase that needs them)
1. `references/topic-guide.md` — building the topic list by pillar, balancing from the log
2. `references/script-guide.md` — the hook ×3, the 30–60s script, the bullet version, the shots, the CTA rung
3. `references/calendar-guide.md` — the 30-day calendar, the weekly mix, the batch plan

---

## Phase 1 — The topic list (by pillar, balanced from the log)
**Read `references/topic-guide.md`.** **Open now:** `memory/ideas.md` (tags `shortform`, `story` — the member's own
ideas go to the TOP; mark `used` once scripted) · `memory/content-log.md` (what's covered; which pillar is light this
week/month) · `memory/objections.md` (an objection heard this month is a Perspective Reel waiting to happen) ·
`memory/content-performance.md` (what worked — the Friday ledger from `sf-analytics`; lean on it for hooks, pillars,
and rungs; skip if it doesn't exist yet) · `identity/publishing.md` (the keyword, what it opens, the weekly mix).
Produce ~8–10 topics the member can choose from: this week's calendar rows still at `Idea` first (the plan they
already said yes to), then the member's own ideas (from `ideas.md`), then the pillar they're lightest on this
month, then the rest — never more than three from one pillar. Each topic: a working **hook** (one line) · the **pillar** · **who it's for** (the avatar, one
line) · the **story or proof it can carry** (a story-bank hook, a win with consent, or "none — straight teach")
· the **rung** it ends on · one line of **why this is strong for you**. Speak to an agent's *problem*, never a
brokerage feature. Present simply:
> "Here are strong ones for this week — I've leaned on [pillar] because you've been light there. Tell me the
> numbers you want to film and I'll script them. Your turn."
**If they're unsure or say "you pick"** (house rules #8 + `${CLAUDE_PLUGIN_ROOT}/shared/advisor-playbook.md`):
choose the top 3 yourself — one line of why each — and offer to script them now.

## Phase 2 — Scripts (for the chosen topics; default five, or the one they named)
**Read `references/script-guide.md`.** **Open now — the writing step:** `identity/voice-print.md` (their SPOKEN voice:
scripts are read aloud, so write for the ear in their cadence and signature phrases; empty → `voice.md` alone; never
fabricate) · `identity/voice.md` + `identity/voice-samples.md` (tone + their real phrasing) · `identity/journey.md`
(incl. `## Why join me` if written) + `identity/strategy.md` (the story beats, the known-for) · `identity/positioning.md`
(the one line "why I'm here"; what stays for the private call — never in a Reel) · `identity/proof.md` (wins with
consent for Proof Reels; first name / initials otherwise) · `identity/offer.md` (the resource for the Resource rung;
Status `seeds` → fall back to the free thing they give today or "book a call"; never demand the Week 2 offer) ·
`identity/publishing.md` (the keyword, what it opens) if Phase 1 didn't open it.
For EACH Reel, use these exact section names:
- **THE BRIEF** — pillar · for whom · story used (hook from the bank, or none) · rung + keyword.
- **THE HOOK — 3 ways** — three options (one may come from `content-pillars.md → ## Hooks bank` when a bank hook
  fits this Reel), each sayable in one breath (~8–12 words), styles labelled (question ·
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
  thing."* One rung per Reel; the call only after a conversation; never the model by DM. The line comes from the
  CTA bank (`sf-comment-to-dm`'s sheet) when one exists; otherwise write it on the same rules.
- **THE CAPTIONS** — hand hook + script + format `talking head` + pillar + rung + keyword to the optimizer's
  rules (`${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md`): Instagram + Facebook caption
  with the CTA line and 3–5 hashtags · TikTok one-line · YouTube Shorts title/description/tags · cover text + 2–3
  on-screen cues. Do not write your own hashtag rules here.
After all Reels: **THE BATCH NOTE** — which to film in one session (same outfit, same spot), and the one to post
first. A **Story** Reel pulls its story from the bank, told in their words, former brokerage never named; a
**Proof** Reel names an agent only with consent on file.

## Phase 3 — The 30-day calendar (lives in the Game Plan)
The calendar is section 6 of the member's Short-Form Game Plan and `memory/content-calendar.md` is its home —
twenty dated posts over four weeks on the weekly mix, the daily stories line, the batch plan, the three to film
first (the rules are in `references/calendar-guide.md`, which the Game Plan reads). Asked for here ("my 30-day
attraction calendar", "plan my month of attraction reels"): say one line — *"your calendar lives in your Game
Plan — I'll map the next thirty days there"* — and run `${CLAUDE_PLUGIN_ROOT}/skills/sf-gameplan/SKILL.md` in
UPDATE mode scoped to section 6 (a new window from the day after the last mapped date; the board topped up by
`sf-board` when they have one). When it hands back, close: *"Pick your first five and say 'script these'."* (The
ongoing routine is `sf-weekly-routine`; the Monday drafts are `sf-week-plan`; film-day logistics are
`sf-batch-publish`.) Never build a second calendar here.

## Phase 4 — Compliance pass (third law, three-state)
**Open now:** the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then
`Gate:`): `unset` → the scripts stay in chat as private drafts, with the plain line that nothing goes out until
compliance is set; `set` → apply + remind once; `confirmed` → apply. Apply: brokerage name/license as the file
says; **the two cardinal rules** (`03-model-positioning/13`); no compensation (splits, caps, stock, rev-share,
income); no earnings claims; no "#1/best" without a source; consent on any named agent; former brokerages
unnamed; any real-estate example fair-housing safe. Strip or rewrite; never ship risky lines.

## Phase 5 — Deliver
Clean copy-paste packages, friendly chat around them, short. Offer, in one line each and only where it applies:
the Riverside edit (*"record it and say 'edit my reel' — captions, clean cut, done"*, `studio-reel`); scheduling
through their tool per `${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` — only with explicit approval; the
content board (house rules #10).

## Phase 6 — Save + log + push
For each scripted Reel:
1. **Save the doc** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` — rendered `.docx` to
   `03 · Content/Short-Form/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Reel · [Short Topic]` (a batch:
   `· Reels · [Batch name]`).
2. **Log it:** append one row per Reel to `~/attraction-brain/memory/content-log.md` in the locked shape:
   `| [date] | Instagram · TikTok · Shorts · FB | reel | [Pillar] | [talking head] [hook] | [avatar] | [story hook or —] | [rung · KEYWORD] | Scripted | |`
   A Reel scripted from a calendar row: flip that row's Status to `Scripted` in `memory/content-calendar.md`
   (the one cell this skill writes there) and, when they have the board, fill the row's card by its System ID
   (house rules #10).
3. **Stamp** the story's `Used-where` in `identity/story-bank.md`; flip any `ideas.md` row used to `used` (open it
   now if no earlier phase did).
4. **Push** (write → push → verify). Then: *"Saved your [N] Reels to your workspace (Content → Short-Form →
   [month]) and logged them so we never repeat a story."* If a save fails: say it's not saved, keep it visible,
   retry once, stop.

---

## Quality checklist
- [ ] Brain read — four files at Step 1, the rest at the phase that used them; pillars from `content-pillars.md`;
      nothing re-asked
- [ ] Topics balanced by pillar from the log; member's own ideas first; every topic speaks to an agent's problem
- [ ] Each Reel: brief · hook ×3 (mixed styles) · 30–60s script with word count · bullet version · shots · one rung + the keyword
- [ ] Sounds like them (`voice-print.md`); talks to one agent ("you"); the delete / any-agent / so-what tests pass
- [ ] Story pulled from the bank (never invented), former brokerage unnamed, Used-where stamped; Proof only with consent
- [ ] No compensation, no earnings, no negative word about any brokerage or person; compliance three-state applied
- [ ] Captions via the optimizer rules; the CTA line carries the keyword
- [ ] A calendar ask handed to the Game Plan (UPDATE, section 6) — never a second calendar built here; a Reel
      scripted from a row flips the row to `Scripted`
- [ ] Saved to `03 · Content/Short-Form`, logged in the locked row shape, pushed; text only
