---
name: yt-thumbnail
description: >
  The Thumbnail Sheet for the Agent Attraction YouTube System (Week 5) — for Higgsfield, where the
  cohort's members make their thumbnails; writes the sheet, never the image. From the title, lane
  and face it drafts three directions in the chat (expression, 3–5 words that differ from the
  title, one supporting element, the highest-contrast brand pairing), scores them on lesson 97's
  rules, recommends one, and hands back ONE sheet: for each direction a ready-to-paste image prompt
  (16:9, 1280×720, clear space for the words), which of the member's own photos to upload, and the
  3 to 5 words to add. Strategy stays in the chat; three thumbnails per video so YouTube can test
  them. Trigger on: "thumbnail brief for my attraction video", "thumbnail for my attraction video",
  "thumbnail directions for my agent video", "brief my attraction thumbnail", "thumbnail for my agent
  interview", "thumbnail for my model breakdown for agents", "my thumbnail is done".
---

# Thumbnail Sheet — the two most overlooked, most important components (`08-youtube/97`)

If they don't click, they don't watch; the thumbnail and the title are the first impression that decides
whether anyone ever sees the member's leadership. This skill writes the sheet; **the member makes the thumbnail
in Higgsfield** (the owner, 2026-11-14: the cohort's members make their thumbnails there): they upload their own
photo, paste the prompt, add the words. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. Read `references/swipe-file-patterns.md` at Step 2 (not before).

**Week 5 rules that bind every sheet** (the owner's rulings of 2026-11-14 — where older text disagrees, these win):
- **The sheet is for Higgsfield, and it has ONE shape** (`${CLAUDE_PLUGIN_ROOT}/shared/doc-format.md`, the
  Thumbnail Sheet skeleton — the same block here, in the Kickoff Brief and on the card). For each of the three
  directions it carries exactly three things: **the image prompt to paste** (the scene, the member's expression, the
  background, the brand's colours in plain words, a 16:9 frame at 1280×720 with clear space where the words go),
  **which of the member's own photos to upload** as the reference, and **the 3 to 5 words to put on it**.
  **Strategy stays in the chat:** why this direction, the scores, what to watch.
- **A thumbnail sheet is never pasted anywhere else** — not a design project, not a design canvas. (The channel
  BANNER is a different thing: it comes with the Week 3 brand kit — `yt-setup`.)
- **Member-facing words:** Week 5; "your thumbnail sheet"; plain and warm; never a skill id or a file path in a
  sentence to the member.

> **Part of the video package.** Normally called by `yt-make-video` once the title is locked (before filming,
> so the member can film the expression). Standalone works too: ask for the title, the lane, and whether a
> guest is in it, then run. The Monday Kickoff drafts the same sheet for the week's video; a sheet already in the
> video's folder or on the card stands unless the title changed — check it, never rewrite it.

## Step 1 — Gather (from the chat and the Brain, never re-asked)
- The locked **title**, the **bucket** (Problem · Situation · Future · Interview · Model — printed on the sheet as
  the lane), the **avatar**, and the emotion the title carries (fear to avoid or outcome to reach — `97`).
- `identity/brand-visual.md` — the Final kit (Week 3): the colour pairings (named in plain words in the prompt, the
  hex in brackets), the headshot set and which expressions exist, the logo rule. No Final kit yet (the Week 3 brand
  chat has not run) → the prompts say "a plain dark background, no accent colour", the photo is "your best recent
  headshot", and one line tells the member that the Week 3 brand chat makes it on-brand — never a detour to build
  the brand first.
- `identity/compliance.md` — the first line, `Status:` (Compliance, below), then the brokerage logo rule and name
  display, and the AI-likeness rule: a thumbnail Higgsfield makes from the member's own photo is an AI-made picture
  of them — apply the file's AI-likeness line as written (and the platform's own label rule), and put it on the
  sheet's rules line when a disclosure is asked for.
- For an interview: the guest's name as written and their consent (from `memory/interview-pipeline.md`); a guest's
  photo is uploaded only with that consent.

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

## Step 4 — The thumbnail sheet (paste-ready, for Higgsfield)
Deliver this block in chat and save it as **Thumbnail Brief — [title] — YYYY-MM-DD** in the video's folder
under `03 · Content/Long-Form/` (rendered through `shared/render_doc.py`; the doc name is unchanged so the board
and the Kickoff find it); when they have the board it is the card's 🖼 THUMBNAIL BRIEF section (`yt-make-video`
writes the card; replaced in place, never stacked). The finished thumbnails come back from Higgsfield into the
same video folder (the member drops them in — the Brain's drive map puts a video's thumbnails next to its script,
never in a Graphics folder). **One shape, printed here exactly as the Thumbnail Sheet skeleton in
`shared/doc-format.md` prints it** (everything inside `{…}` is a note to the writer and is never printed):
```
THUMBNAIL SHEET — "{VIDEO TITLE}"
For Higgsfield, where you make your thumbnails: upload your photo, paste the prompt, add the words.
Video: {lane} · for {the type of agent} · the feeling: {the fear to avoid / the outcome to reach}
All three: a 16:9 frame at 1280×720, with clear space where the words go.

──────────────── THUMBNAIL 1   (the recommended one) ────────────────
Photo to upload:  {which of the member's own photos — named the way it is in their Brand folder — or, when the expression is missing, "take this one first: {the expression to shoot}"}
Prompt to paste:
{one ready-to-paste paragraph: the scene · your expression · where you sit in the frame (about a third of it, left or right, eyes toward the open side) · the background · your brand's colours in plain words (the hex in brackets) · "16:9 frame, 1280×720, clear space on the {left / right / top} for text, no text in the image"}
Words to add (3–5):  {the words — never the title's}

──────────────── THUMBNAIL 2 ────────────────
Photo to upload:  {…}
Prompt to paste:
{the same shape — the one change from thumbnail 1}
Words to add (3–5):  {…}

──────────────── THUMBNAIL 3 ────────────────
Photo to upload:  {…}
Prompt to paste:
{the same shape — the one change from thumbnail 1}
Words to add (3–5):  {…}

────────────────────────────────────────────
Rules — 3 to 5 words · the words differ from the title · your face about a third of the frame · one supporting element at most · readable on a phone · {compliance: your brokerage's mark where required; no other brokerage's mark; your AI-picture line where your compliance wording asks for one}
When they're made: drop the finished thumbnails into this video's folder (Content → Long-Form → {video}) and say "my thumbnail is done".
```
**Writing each prompt** — one paragraph the member pastes as it is, in plain words, no jargon: the person is "the
person in the uploaded photo" (their real face, never altered into someone else); the expression the direction
needs; their place in the frame; the background and ONE supporting element at most (a guest beside them for an
interview — the guest's own photo uploaded too, with consent); the Final kit's highest-contrast pairing named in
plain words ("deep navy background, warm yellow accent") with the hex in brackets; the frame — "16:9, 1280×720";
"leave clear space on the [side] for text"; "no text in the image" — the member adds the 3 to 5 words. Never
another brokerage's mark, never "#1 / best" words, never a compensation number, never a face that is not theirs.
Nothing else on the sheet — no scores, no why, no swipe-file note, no backstory; those are the chat's (Step 3).
**The hand-off line to the member, in these words:** *"Take this to Higgsfield, where you make your thumbnails:
upload your photo, paste the prompt, add the words. Drop the finished thumbnail into this video's folder and say
'my thumbnail is done'."* The expression to shoot is the line to say before filming.

## Step 4b — "My thumbnail is done"
The member says it once the finished thumbnails are in the video's folder. **Which video:** the one this chat is
making; in a fresh chat, the video whose card or content-log row is at `Scripted` or later with no thumbnail
noted — say which in one line; "your turn" only when two videos fit. Look in that video's folder for the image
files. **Found** → note them on the card's 🖼 THUMBNAIL BRIEF section, one line under the sheet, replaced in place,
never stacked: `Thumbnail made: [the file name(s)] · [the date, in words]` (the card found by System ID → exact
title → near match; the board line read from `identity/publishing.md → Content board:`, then `identity/channel.md →
Board:`; no board → nothing to write). Then one line, no question: *"Noted — your thumbnail is with this video."* — and, only
when three thumbnail files are in the folder, one more sentence: *"When you publish, upload all three if YouTube
Studio shows 'Test & compare' — YouTube picks the winner."*
**Not found** → one line: *"I don't see it in the folder yet — drop it into Content → Long-Form → [video] and say
'my thumbnail is done' again."* Nothing else is written; no Brain file changes.

## Step 5 — After a month (when asked, or from `yt-analytics`)
CTR under the 6–10% band after 30 days → new title and new sheet (`97`); note which directions keep winning so
the style settles. `yt-analytics` reads the packaging; this skill only writes the next sheet.

## Compliance (3-state — never a stop, never a detour)
Read `identity/compliance.md`'s first line, `Status:` — **`unset`** → the sheet is still written, delivered and
saved, stamped "hold until your compliance basics are set", and ONE line is said at the close: *"One thing before
this thumbnail goes on a video: say 'paste my compliance link' — two minutes — so your brokerage's wording is on
it."* (inside `yt-make-video` or the Monday Kickoff, that run says its own one line and this skill stays silent) ·
**`set`** → apply, remind once at the close to confirm with the brokerage · **`confirmed`** → apply. Applied in
every state: no "#1 / best" words, no other brokerage's logo, no compensation numbers in the words, the brokerage
name only as the file requires, the AI-likeness line where the file or the platform asks for one.

## Rules
- This skill makes no image and calls no image tool: it writes the sheet — the prompts, the photo to upload, the
  words — and the member makes the thumbnail in Higgsfield.
- Never invent a headshot the member does not have; if the needed expression is missing, say which to shoot.
- A thumbnail sheet goes to Higgsfield and nowhere else; the member-facing line never names another tool.
- Plain language: "your thumbnail sheet", never the skill or file names in front of the member.
