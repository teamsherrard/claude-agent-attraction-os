---
name: lm-delivery
description: >
  Writes everything that DELIVERS the member's agent-attraction lead magnet from their own
  accounts — the ManyChat GUIDE keyword flow (comment reply, the DM that sends the link, the
  qualifier, the hand-off, one follow-up), the delivery email they send by hand or load into their
  list tool, and the 3-frame story that offers the guide — in the member's voice, pointed at the
  live funnel, the warm optional call offered after the download, never before. The Resource rung
  of the Short-Form plugin's CTA ladder (Follow → Comment → DM → Resource → Conversation → Call).
  Draft-only — nothing is sent or posted; the member pastes the copy into their own ManyChat,
  email, and story. 3-state compliance gate; no compensation, no model talk in a DM.
  Trigger on: "deliver my guide", "how do I deliver my agent lead magnet", "ManyChat copy for my
  guide", "GUIDE keyword copy", "DM that sends my guide", "delivery email for my
  guide", "story that offers my guide".
---

# Delivery Kit — the DM, the email, and the story that hand the guide over

The page catches agents who click; this kit catches the ones who **comment, reply, or DM** — which is most
of them. Mike's rule (`15-advanced-scaling/73`): use ManyChat automations to deliver free resources
("comment [keyword] below to get this"), require an email for access, and always give value first. The
Short-Form plugin's CTA ladder (Week 3) puts the GUIDE keyword on every authority Reel from then on; this kit
is what fires when someone uses it — and until that engine arrives, the member runs the same keyword by hand
in DMs, story replies, and comments on what they already post (the week rule: Week 3 is never "missing").

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #4 (download first, the call
after), #5 (the gate; no compensation or model talk in a DM — `02-prospect-targeting/19`: never explain the
model by DM), #12 (draft-only). Copy standard: `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md` → "Emails,
DMs, and the newsletter." The three laws: `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Step 0 — What's live (silent)
Pull the Brain (house rule 2). Read `memory/magnets.md` → `## Current magnet` (name, funnel URL, download
link, keyword). **No live funnel URL yet** → write the kit anyway with the booking link as the fallback link
and say in one line that the funnel link slots in the moment the page is up (never block delivery on design).
**No booking link on file either** → the DM sends the guide's own shared link (the PDF in their drive, "anyone
with the link"), and the call line reads "message me here and I'll send you times" (house rules #2's one line, once).
**No written magnet** → `lm-navigator` with the way-back line.
Read `identity/compliance.md` (**the gate — unset stops here**; a DM template is public), `identity/voice.md`
+ `voice-samples.md` Sample 4 and later (how they type — DMs are typed; Samples 1–3 are the spoken answers —
for the spoken voice use `voice-print.md`), `identity/avatars.md` (the type of agent and the one
qualifier question that mirrors their pain), `identity/operations.md` (follow-up cadence, the booking link,
the email signature), `identity/profile.md` (handles), and `identity/offer.md` → the header's `Join-gated package
allowed:` line (at `no` or `unknown` every hand-off line in the DMs is what the member teaches, never a package for
joining — house rules #5).

## Step 1 — The DM that sends the guide (by hand today; the same copy loads into ManyChat in Week 3)
Members don't have ManyChat in Week 2 — the cohort's templates (PARTNER · GUIDE · SCALE · GROWTH) arrive with
Week 3's materials as importable flows. So the first block is the **by-hand DM script** the member sends from
their own phone today, and the same copy becomes the GUIDE flow's messages when they import it (label the block
"paste into ManyChat when you have it — Week 3"). Keyword rule of one: GUIDE delivers the magnet; nothing else
rides on it. Write:
1. **The public comment reply** (under their comment, ≤ 1 line): *"Sent it to your DMs 👋"* — in their voice.
2. **DM 1 — the delivery** (the moment they comment): warm, one line of what the guide is, **the link** (the
   funnel URL — the opt-in captures the email; never a bare download link that skips the list), and the
   privacy line (*"private list, nobody's contacted on your behalf"*).
3. **DM 2 — the qualifier** (after they've grabbed it, same day): ONE question that mirrors the type of
   agent's pain (`avatars.md`) — *"Quick one so I send you the right stuff: are you weighing a move right
   now, or just reading ahead?"* Never "what brokerage are you at" as the opener; never a pitch.
4. **DM 3 — the human hand-off** (if they answer): the member takes over by hand. Write the opening line that
   moves to a real conversation — the Conversation rung — and the warm, optional call line (Mike's register:
   *"happy to talk it through on a quick call — no pitch, I'll just answer your questions. If not, that's
   okay."*). Compensation and the model stay off DMs entirely; that's the call.
5. **The no-reply follow-up** (3 days later, once): one line of value (the single most useful page of the
   guide) and nothing else. Then stop — the nurture sequence (`lm-nurture`) carries the rest by email.
Each message ≤ 3 short lines, typed-voice, no links except in DM 1. Note for the member: Instagram's
automation rules change — they check ManyChat's current policy on comment-triggered DMs before switching it on.

## Step 2 — The delivery email (sent by hand, or the first email in their list tool)
Subject (fifth-grade, specific, no "[Brokerage]"): *"Your [guide, by name] (and the one page to read first)"*.
Body: one warm line · the download link (the PDF — instant) · the one page to read first and why · the
privacy line · the warm optional call line with the booking link · the signature block from `operations.md`
with the compliance stamp. ≤ 150 words. **This is the only email that may carry the bare download link**,
because the person already opted in. Draft-only — the member sends it or loads it as the automated first
email; the plugin never sends.

## Step 3 — The 3-frame story (the member's own account, filmed or typed)
Frame 1 — the pain, in the type of agent's words, as a question (*"Still paying for leads that don't
close?"*). Frame 2 — the guide, with the mockup (from `lm-design`) and one line on why it's different (the
real thing, built from what I actually do). Frame 3 — the ask: *"DM me GUIDE and I'll send it"* (or the link sticker
to the funnel). Spoken voice from `voice-print.md` if filmed. No model talk, no comp, nothing about any other
brokerage. The Short-Form plugin's story rotation (Week 3) reuses this frame set; say so in one line.

## Step 4 — Deliver, save, log
1. Deliver the kit in chat as three labeled blocks (ManyChat · Email · Story), paste-ready.
2. Save `Delivery Kit — [Guide Name]` into the campaign folder (output standard §4–§6; fallback applies).
3. In `memory/magnets.md`, set the row's Keyword to `GUIDE` if blank (the Last reviewed column belongs to
   `lm-analytics`). **attraction-brain-sync PUSH.** Silent.
4. Close: *"Send the DM from your own phone this week — the same copy drops into your ManyChat GUIDE flow in Week 3 — drop the email into your list tool as the first
   message, and the story's ready to film. Say 'nurture sequence for agents' and I'll write what they get
   after this — the emails that keep you top of mind until they're ready."*

## Compliance pass (every message)
The two cardinal rules · no compensation, splits, rev share, stock, or income · no model explanation by DM ·
no earnings talk · the privacy line present · the compliance file's cross-border note applied as written
(recruiting scope is anywhere — never a limit) · the stamp on the email · `set` → one reminder. Never a bracket token.
