---
name: sales-setter
description: >
  Sales OPS: the scripts and rules for a VA or setter who handles the member's inbound agent
  conversations. DM qualification (comment or keyword reply, the three qualifying questions, the
  selfless invite to the member's calendar), the phone qualification and confirmation call, the hard
  hand-off rules (what a setter never discusses: compensation, splits, caps, stock, rev share, other
  brokerages, other people), who goes straight to the member, and the hand-off note shape. Written in
  the member's voice for a human setter or a keyword sequence. Compliance gate first; nothing sends.
  Trigger on: "setter script", "scripts for my VA", "train my setter", "DM qualification script",
  "phone script for my assistant", "what my VA can and can't say to agents", "hand-off rules for my
  setter", "appointment setter for agent attraction", "qualify agents in the DMs".
---

# Setter Scripts — someone else opens the door; the member walks through it

The cohort's Sales OPS kit includes a setter script because the member cannot answer every DM at scale.
The rules come straight from Mike's doctrine: conversation starters are selfless and value-driven, never a
pitch; compensation is a private conversation with the member; the two cardinal rules apply to anyone who
speaks for the member (`03-model-positioning/13`); the booking form's five questions are the qualification
(`10-presentation-delivery/42`). A setter qualifies and books. They never present, never negotiate, never
explain the model.

**Write-and-prepare.** Scripts and rules for a human VA or a keyword sequence (the Week 3 ManyChat
templates); nothing is sent from here.

## Step 0 — How we speak
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`, `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`. One stop of 2–3 questions at most.

## Step 1 — Load the Brain
`~/attraction-brain/brain.md`, then `identity/sales-system.md` (the calendar link, the five questions, the
"no" rule), `identity/operations.md` (hours, response-time commitment, who is shared in), `identity/
avatars.md` (the types the member serves and the ones to pass through fast), `identity/positioning.md`
(the one line a setter may say about what the member does), `identity/voice.md` (the setter writes as the
member's team, in the member's register), `identity/compliance.md` (public), `config.md` (`Workspace shared
with`). Missing locally → `attraction-brain-sync`. A tool error is never "no Brain".
`${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md` for the DM-flow beats if needed (the member-run
version is `cv-dm-flow`; the setter version below is the narrower one).

## Stop 1 · Who and where (2–3 questions)
*"Who's setting — a VA, a team member, or a keyword sequence? Which inboxes — Instagram, Facebook, email,
phone? And do they write as you or as 'Team [Name]'?"* Defaults: a human VA, Instagram and email, signs as
"[First name] from [Name]'s team" (never impersonating the member in first person). **Your turn.**

## Compliance gate
`identity/compliance.md` unset → the rules doc is written (private), the scripts are not; say the three-
minute line. set → apply, remind once. confirmed → apply. Rules: brokerage name as required; no compensation
or income language at all; nothing about another brokerage or person; license line where the brokerage
requires it in outreach.

## The rules a setter signs (page one of the doc — the part that matters most)
**Never:** discuss compensation, splits, caps, fees, stock, revenue share, or "how the model works" ("that's
a [Name] conversation — it's what the call is for") · say anything about another brokerage, team, sponsor,
or person · promise results, income, leads, or support beyond the one positioning line · pretend to be
[Name] in the first person · pressure, deadline, or guilt · book someone who answered "no" to the
acknowledge question (the "no" rule) · message anyone who asked not to be contacted · research a prospect's
personal life (business profiles only, and only what they shared) · write anything into the member's Brain
(the setter leaves notes in the CRM or sheet; the member or the AI Admin logs them).
**Always:** reply inside the response-time commitment in `operations.md` · one question per message ·
lead with what the prospect said · offer the calendar link, never push it · pass the hand-off cases below
to the member the same day.

## Straight to the member (no qualifying, book or pass immediately)
A team leader or broker-owner · a top producer or an agent with a visible brand · anyone who asks about
compensation or the model · anyone unhappy, upset, or disputing something · anyone the member already knows
(a Top-50 name) · a referral from a partner · anyone who mentions another sponsor. The setter's line: *"That's
exactly what [Name] covers on the call — here's the calendar; want me to hold a time?"*

## The DM qualification script (keyword or comment → booked)
Written in the setter's voice, six short beats, one question each, with the member's actual phrasing:
1. **Open on their action** — "Saw your comment on [the reel's topic] / thanks for the keyword — glad it
   landed." (Never "I'd love to share an opportunity.")
2. **One real question about them** — "Quick one: how long have you been licensed, and where are you
   based?" (questions 3 and 4 of the form, conversationally).
3. **The brokerage question, lightly** — "Which brokerage are you with right now?" (question 2.)
4. **The why** — "What made [the content] resonate — what are you working on this year?" (question 5.)
5. **The selfless bridge** — a resource first when one fits (`offer.md`'s free pieces; the Lead Magnet when
   it exists): "Here's [resource] — it covers exactly that."
6. **The invite** — "[Name] does a 30-minute one-on-one for agents figuring this out. If that's useful,
   here's the calendar: [link]. No pitch — it's a conversation about what you're building." Then the
   acknowledge question's gist if they book: "it's about possibly partnering with [Name] at [Brokerage] —
   just so the call is useful."
Plus the three branch replies: **not interested** ("totally fine — I'll leave you with [resource]; door's
open"), **already at the brokerage / already sponsored** ("appreciate you saying — the call wouldn't be the
right fit then; [Name] still shares [the free content] every week"), **asks about money** (pass to the
member, beat 1 above).

## The phone scripts (two)
1. **Confirmation / qualification call for a booked agent** (3 minutes): confirm the time and the Zoom
   link, walk the five questions if the form was thin, set the expectation ("[Name] will have looked at what
   you shared; bring the questions you most want answered"), end with energy. Nothing about the model.
2. **Inbound call-back** (someone rang or left a number): the same three qualifying questions, the resource,
   the calendar — or the pass-through line.

## The hand-off note (what the setter leaves, every time)
One block in the CRM or sheet, the Top-50's columns so the Admin and the member read it without
translation: **Name · Type (one of the six, as the prospect described themselves) · Where (brokerage type ·
market) · Source (which reel / video / keyword / referral) · Stage (Conversation or Call booked) · What they
said (their words, two lines) · Next move · Due.** Never a note about a protected characteristic; never an
opinion about the prospect. The member (or `attraction-capture` / the AI Admin) logs it to the Brain.

## Save and confirm
Render the Setter Playbook per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` via
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/setter.txt "Setter Playbook — [Name] — [YYYY-MM-DD].docx" --title "Setter Playbook" --subtitle "[Name] · [Organization]"`
(read back; `RENDERER-UNAVAILABLE` → install nothing, upload the `.md`), upload to the workspace's `05 · Offer`
folder. Write the setter's name to the `Setter` key of the `## Conversion & Sales` block in `config.md` (this
plugin's block; create it in the brain contract's spelling if absent) and push; the workspace share itself
(`Workspace shared with`) is the member's choice through `attraction-operations` — say so in one line. Confirm: *"Your setter playbook is ready — the rules
page, the DM script with its three branches, the two phone scripts, and the hand-off note. Share it with
[setter]; they work from your CRM, never from your Brain. Your turn."*

## Demo mode
Fictional member and setter, "(illustrative — demo)", DEMO in the filename.

## Quality bar
A setter who follows the script can never say a number, name a competitor, or promise a result; every
message has one question; the invite is an offer, not a push; the hand-off note matches the Top-50's columns
exactly; the voice is the member's team, not a call centre.
