---
name: yt-thumbnail
description: >
  The Thumbnail Build Sheet for the Agent Attraction YouTube System (Week 5) — writes the sheet, never
  the image. From the title, lane and face it drafts three directions in the chat (expression, 3–5
  words that differ from the title, one supporting element, the highest-contrast brand pairing),
  scores them on lesson 97's rules, recommends one, and hands back ONE lean build sheet — the layout
  chosen, the words, the expression to shoot, the brand tokens from the Week 3 Final kit, placeholders
  — pasted into the member's brand project in Claude Design (claude.ai/design, or a Design canvas
  inside Cowork). Strategy stays in the chat; no separate thumbnail design skill; three thumbnails per
  video so YouTube can test them; no image generation. Trigger on: "thumbnail brief for my attraction
  video", "thumbnail for my attraction video", "thumbnail directions for my agent video", "brief my
  attraction thumbnail", "thumbnail for my agent interview", "thumbnail for my model breakdown for
  agents".
---

# Thumbnail Build Sheet — the two most overlooked, most important components (`08-youtube/97`)

If they don't click, they don't watch; the thumbnail and the title are the first impression that decides
whether anyone ever sees the member's leadership. This skill writes the sheet; the member pastes it into their
brand project in Claude Design (claude.ai/design, or a Design canvas inside Cowork), which makes the images. There
is no separate thumbnail design skill. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. Read `references/swipe-file-patterns.md` at Step 2 (not before).

**Week 5 rules that bind every sheet** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **A LEAN BUILD SHEET** (the owner, 2026-11-11): what Claude Design needs and nothing else — the layout chosen, the
  3–5 words, the expression to shoot, the brand tokens from `identity/brand-visual.md`'s Final kit (Week 3), the
  placeholders, the output. **Strategy stays in the chat:** why this direction, the scores, what to watch.
- **Where it goes:** "your brand project in Claude Design (claude.ai/design, or a Design canvas inside Cowork)" —
  the project the Week 3 brand chat made. Never any other name for it.
- **Member-facing words:** Week 5; "your thumbnail sheet"; plain and warm; never a skill id or a file path in a
  sentence to the member.

> **Part of the video package.** Normally called by `yt-make-video` once the title is locked (before filming,
> so the member can film the expression). Standalone works too: ask for the title, the bucket, and whether a
> guest is in it, then run. The Monday Kickoff drafts the same sheet for the week's video; a sheet already in the
> video's folder or on the card stands unless the title changed — check it, never rewrite it.

## Step 1 — Gather (from the chat and the Brain, never re-asked)
- The locked **title**, the **bucket** (Problem · Situation · Future · Interview · Model), the **avatar**, and
  the emotion the title carries (fear to avoid or outcome to reach — `97`).
- `identity/brand-visual.md` — the Final kit (Week 3): the colour pairings, the display font, the headshot set and
  which expressions exist, the logo rule. The sheet carries the tokens by name and value, nothing more. No Final
  kit yet (the Week 3 brand chat has not run) → the sheet says "your headshot, one dark text colour, no accent",
  and one line to the member that the Week 3 brand chat makes it on-brand — never a detour to build the brand
  first.
- `identity/compliance.md` — the first line, `Status:` (the gate below), then the brokerage logo rule and name
  display; AI-likeness disclosure if the face is a clone render (a Claude Design composition from a real headshot
  is not a clone; say which it is).
- For an interview: the guest's name as written and their consent (from `memory/interview-pipeline.md`).

## Step 2 — Three directions, each on one idea (in the chat)
Read `references/swipe-file-patterns.md`. Draft three directions; each one states:
- **Text** (3–5 words, NOT the title's words — `97`): the curiosity, the emotion, or the clarity angle.
- **Face and expression:** which headshot family (concern · surprise · confidence · delight), eyes toward text.
- **Composition:** face position and size (~a third of the frame), text block, one supporting element max
  (the guest's face for interviews; a map or product only when it supports the title without repeating it).
- **Colour:** the Final kit pairing with the highest contrast; text on the background, never on the face.
- **The feeling the viewer gets:** "this is me, I need to watch this" in one line.

Bucket defaults: **Interview** → two faces, the guest's transformation word ("FIRST DEAL · 90 DAYS") ·
**Model** → one face, the question word ("WORTH IT?", "READ THIS FIRST") · **Problem** → concern face, the
mistake named · **Situation** → "this is you" phrasing · **Future** → confident face, the outcome.

## Step 3 — Score against the patterns (in the chat, plain words)
Score each direction 0–2 on: curiosity · emotion · clarity · text differs from the title · 3–5 words ·
expression matches · contrast · simplicity · mobile legibility (9 criteria, 18 max). Say in one line where
each loses points. Recommend one as the primary and keep all three (YouTube's Test & Compare runs three — `97`).
State the swipe-file status honestly: *"Mike's swipe file isn't in yet; these are scored on his lesson rules
and I'll re-score when it lands."* Never claim a pattern the reference does not hold. The scores and the why stay
here — never on the sheet.

## Step 4 — The lean build sheet (paste-ready, for Claude Design)
Deliver this block in chat and save it as **Thumbnail Brief — [title] — YYYY-MM-DD** in the video's folder
under `03 · Content/Long-Form/` (rendered through `shared/render_doc.py`; the doc name is unchanged so the board
and the Kickoff find it); when they have the board it is the card's 🖼 THUMBNAIL BRIEF section (`yt-make-video`
writes the card; replaced in place, never stacked). The finished images come back from Claude Design into the same
video folder (the member drops them in — the Brain's drive map puts a video's thumbnails next to its script, never
in a Graphics bucket):
```
THUMBNAIL BUILD SHEET — "[title]"
Paste into: your brand project in Claude Design (claude.ai/design, or a Design canvas inside Cowork). Ask for the three thumbnails.
VIDEO: [bucket] · for [the type of agent] · the title's emotion: [fear to avoid / outcome to reach]
BRAND (your Final kit): background [name · hex] · text [name · hex] · accent [name · hex, or none] · display font [name] · headshot [the set · the expression] · logo [where the compliance file says, or none]
THUMBNAIL 1 — the chosen layout
   Text: [3–5 words, not the title's]
   Face: [headshot family · expression to shoot · eyes toward the text] · about a third of the frame · [left / right]
   Text block: [upper / side, opposite the face] · [pairing]
   Supporting element: [one, or none] ([the guest's headshot for an interview — name as written])
THUMBNAIL 2: [text] · [expression] · [the one change from 1]
THUMBNAIL 3: [text] · [expression] · [the one change from 1]
RULES: 3–5 words · text ≠ title · face ≈ 1/3 · one supporting element · legible at 320px · [compliance: brokerage mark where required; no other brokerage's mark]
OUTPUT: three 1280 by 720 PNGs, one per thumbnail · save them into this video's folder (Content → Long-Form → [video])
```
Nothing else on the sheet — no scores, no why, no swipe-file note, no avatar backstory; those are the chat's
(Step 3). Hand-off line to the member: *"paste this into your brand project in Claude Design — it builds all
three; upload them as a test set in YouTube Studio and we read the click-through after a month."* The expression
to shoot is the line to say before filming.

## Step 5 — After a month (when asked, or from `yt-analytics`)
CTR under the 6–10% band after 30 days → new title and new sheet (`97`); note which directions keep winning so
the style settles. `yt-analytics` reads the packaging; this skill only writes the next sheet.

## Compliance gate (3-state)
Before the sheet goes out: `identity/compliance.md`'s first line, `Status:` — `unset` → keep the sheet in chat,
say plainly the rules are not set yet and no public packaging ships until they are; `set` → apply, remind once;
`confirmed` → apply. No "#1 / best" words, no other brokerage's logo, no compensation numbers in the text,
brokerage name only as the file requires, AI-likeness disclosure if a clone render is used.

## Rules
- No image generation, no prompt for an image model, no external tool — the sheet only.
- Never invent a headshot the member does not have; if the needed expression is missing, say which to shoot.
- Plain language: "your thumbnail sheet", never the skill or file names in front of the member.
