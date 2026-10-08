---
name: lm-nurture
description: >
  Writes the email nurture for the member's agent list — the awareness → proof → CTA sequence an
  agent gets after downloading the lead magnet, and the weekly value newsletter that keeps the
  member top of mind until an agent is ready to move (Mike's lesson: the list is the one audience
  nobody can take away; the nurture is more value, more value, more value). In the member's voice-
  print, from their real stories, the Partner Offer as outcomes, and consented wins of agents in
  their organization; the call to action is warm and optional, never a pitch, never compensation.
  Draft-only — the member loads the sequence into their own list tool and sends the newsletter;
  the plugin never sends. Owns memory/list-growth.md. 3-state compliance gate.
  Trigger on: "nurture sequence for agents", "email sequence after my guide", "my weekly
  newsletter for agents", "email my agent list", "what do I send after they download the guide",
  "write this week's agent email".
---

# Nurture — the sequence after the guide, and the weekly newsletter

**Why (`15-advanced-scaling/73`, in Mike's words):** the email list is "the most valuable asset you will have
… as an attractor and as a leader." Platforms change and accounts get restricted; "you own this asset, it's
yours." It "keeps … top of mind, even when agents aren't ready to move today" — his readers
emailed to ask where the week's email was. His nurture strategy is "value, more value, more value"; the
strongest emails are the success stories of agents in the organization; the call to action is warm —
*"if you'd like to chat about partnering with me … book a private call and we'll see if I can help. If not,
that's okay."* This skill writes that.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #5 (the gate; emails are public),
#8 (their data, never generic), #12 (draft-only). Copy standard: `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md`
→ "Emails, DMs, and the newsletter." The three laws and the `list-growth.md` shape:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Two modes
- **A · THE SEQUENCE** — "nurture sequence for agents," "what do I send after they download": the 7-email
  sequence for one magnet, written once, loaded by the member into their list tool.
- **B · THIS WEEK'S NEWSLETTER** — "write this week's agent email," "my weekly newsletter": one email, this
  week, from what the member did and learned.

## Step 0 — Load (lazy)
Pull the Brain (house rule 2). `identity/compliance.md` (**the gate — unset stops here**; the stamp for the
signature; testimonial consent), `memory/magnets.md` → `## Current magnet` (the magnet the sequence follows;
funnel URL), `memory/list-growth.md` (list tool, newsletter day, what's already drafted — create the file from
the locked shape if the Brain predates it), `identity/voice-print.md` + `voice.md` + `voice-samples.md`
(newsletters read like the member talks — the voice-print is the primary source here), `identity/avatars.md`
(the type of agent, the pain, what they'd need to hear to believe), `identity/story-bank.md` (the real stories,
tagged by pain — read only here: never stamp Used-where; note the story used in `list-growth.md` instead),
`identity/proof.md` (agents helped — consent on file — and upline proof
labeled), `identity/offer.md` (the Partner Offer as outcomes; free vs paid said straight), `identity/journey.md`
(the mirror), `identity/operations.md` (booking link, signature, the weekly call), `memory/content-log.md`
(read only — this week's video or Reel to point the newsletter at), `memory/debriefs.md` (read only — what
happened this week, for mode B).

**First run only, one question (your turn — one word):** *"Which tool holds your email list — [the CRM from
config.md if it does email] or something like Mailchimp, ConvertKit, GoHighLevel? (If none yet, I'll write
everything so it drops into any of them.)"* Write the answer to `list-growth.md` → List tool. Never ask again.

## Mode A — The sequence (7 emails, awareness → proof → CTA)
One email every 2–3 days after the download; each ≤ 200 words, one idea, one link at most, fifth-grade
reading level, the member's voice. The arc:
1. **Day 0 — the guide, and the one page to read first.** (If `lm-delivery` already wrote the delivery email,
   reuse it verbatim here as email 1.)
2. **Day 2 — awareness: the mirror.** The member's own story beat for this type of agent (`journey.md` /
   `story-bank.md`), former brokerage never named. One lesson. No ask.
3. **Day 4 — awareness: the thing nobody told them.** One honest, useful teaching from the member's "what
   worked" (`offer.md` → Teach first) — the first lesson, not a tease. No ask.
4. **Day 7 — proof: an agent like them.** One real story of an agent in the organization (`proof.md`,
   consent on file, verbatim quote if there is one) — Mike's strongest email. If there is none yet: the
   member's own turnaround, honestly labeled; never invented. Soft line: "if you ever want to talk, reply."
5. **Day 10 — what partnering actually looks like.** The Partner Offer as outcomes (`offer.md`): what's
   included, the first 30 days, free vs paid said straight. **No compensation, no model.** The brokerage line.
6. **Day 13 — the questions.** The three questions agents ask most (`objections.md`), answered in one line
   each — the honest versions. Warm optional call line.
7. **Day 16 — the CTA, warm.** Mike's register verbatim-adapted: *"If you'd like to chat about partnering
   with me and getting [the real things — the weekly call, the training, the onboarding] for free, book a
   call and we'll see if I can help. If not, that's okay — the emails keep coming either way."* The booking
   link. Then they roll into the weekly newsletter.
Subject lines: specific, honest, no clickbait, no "[Brokerage]," no emoji walls. Every email: the privacy
line in the footer ("you're getting this because you grabbed [the guide]; unsubscribe any time"), the
signature block with the compliance stamp.

## Mode B — This week's newsletter (one email, value first)
Mike's recipe (`/73`): the week's video(s) with one takeaway each · one straight-value insight (a lesson, a
book, an event, a mindset shift — from `debriefs.md` / what the member tells you) · a success story of an
agent in the organization when there is one (consent; "anybody that comes from them joins under the agent I
interviewed" — say that to the member as the reason to feature partners) · one warm, optional call line. Same
day every week (`list-growth.md` → Newsletter day; propose one if blank — the day after their main video
drops). ≤ 300 words, skimmable, one idea per block, the member's spoken cadence. Never two asks.
Before writing: scan `content-log.md` for this week's content and `list-growth.md` for last week's topic so
you never repeat. `story-bank.md` isn't this plugin's to write — note which story the newsletter used in the
`list-growth.md` Note instead, so the next newsletter doesn't reuse it.

## Step 2 — Deliver, save, log
1. Deliver in chat — each email as `Subject:` + body, paste-ready for their tool.
2. Save: Mode A → `Nurture Sequence — [Guide Name]` into the campaign folder; Mode B → `Weekly Newsletter —
   [YYYY-MM-DD]` into `03 · Content/Guides/` (output standard §4–§6; fallback applies).
3. `memory/list-growth.md` (silent, then **attraction-brain-sync PUSH**): Mode A → a row in the sequence table
   (`[magnet] · 7 · drafted · [doc] · [date]`); when the member says it's loaded → `loaded by the member`;
   Mode B → Newsletter day set if it was blank, and a one-line Note on this week's topic under the weekly
   rows' latest row (no numbers — `lm-analytics` owns the numbers).
4. Close (A): *"Load these into [their tool] as a sequence that starts the moment someone grabs the guide —
   one every two or three days. Then say 'write this week's agent email' every week and I'll draft the
   newsletter from what you did."* Close (B): *"Send it on [day]. Next week, say the same thing and bring me
   one win from your group if you've got one — those are the emails agents forward."*

## Compliance pass (every email)
The two cardinal rules · no compensation, rev share, stock, or income · no earnings talk ("what the member
will SHOW, never what the agent will EARN") · consented, verbatim agent stories · former brokerages unnamed ·
recruiting scope respected · the stamp in the signature · unsubscribe line present · `set` → one reminder per
session · never a bracket token. The plugin never sends, schedules, or loads anything itself.
