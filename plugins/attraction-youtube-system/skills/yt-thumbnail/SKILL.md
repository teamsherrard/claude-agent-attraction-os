---
name: yt-thumbnail
description: >
  The Thumbnail Brief for the Agent Attraction YouTube System — writes the brief, never the image. From
  the video's title, lane, face, text rule, and composition it drafts three directions (the expression, the
  3–5 word text that differs from the title, one supporting element, brand colors at highest contrast),
  scores each on lesson 97's rules (and Mike's swipe-file patterns once that pending file lands — the skill
  says so), recommends one, and hands back a paste-ready brief the member pastes into their Brand HQ
  project in Claude Design; there is no separate thumbnail design skill. Three thumbnails per video so
  YouTube can test them. Reads the Brain's brand-visual and compliance files. No image generation here.

  Trigger on: "thumbnail brief", "thumbnail for my attraction video", "thumbnail directions", "thumbnail
  text options for this", "brief my thumbnail", "score my thumbnail", "which thumbnail should I use",
  "thumbnail for my interview", "thumbnail for my model breakdown".
---

# Thumbnail Brief — the two most overlooked, most important components (`08-youtube/97`)

If they don't click, they don't watch; the thumbnail and the title are the first impression that decides
whether anyone ever sees the member's leadership. This skill writes the brief; the member pastes it into their Brand HQ project in Claude Design, which
makes the images (there is no separate thumbnail design skill). Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.
Read `references/swipe-file-patterns.md` at Step 2 (not before).

> **Part of the video package.** Normally called by `yt-make-video` once the title is locked (before filming,
> so the member can film the expression). Standalone works too: ask for the title, the bucket, and whether a
> guest is in it, then run.

## Step 1 — Gather (from the chat and the Brain, never re-asked)
- The locked **title**, the **bucket** (Problem · Situation · Future · Interview · Model), the **avatar**, and
  the emotion the title carries (fear to avoid or outcome to reach — `97`).
- `identity/brand-visual.md` — colors, display font, the headshot set and which expressions exist; the
  Design System file name if one is recorded (none yet, and no Brand HQ project → the fallback line in Step 4).
- `identity/compliance.md` — the first line, `Status:` (the gate below), then the brokerage logo rule and name
  display; AI-likeness disclosure if the face is a clone render (a Claude Design composition from a real headshot is not a clone; say which it is).
- For an interview: the guest's name as written and their consent (from `memory/interview-pipeline.md`).

## Step 2 — Three directions, each on one idea
Read `references/swipe-file-patterns.md`. Draft three directions; each one states:
- **Text** (3–5 words, NOT the title's words — `97`): the curiosity, the emotion, or the clarity angle.
- **Face and expression:** which headshot family (concern · surprise · confidence · delight), eyes toward text.
- **Composition:** face position and size (~a third of the frame), text block, one supporting element max
  (the guest's face for interviews; a map or product only when it supports the title without repeating it).
- **Color:** the brand pairing with the highest contrast; text on the background, never on the face.
- **The feeling the viewer gets:** "this is me, I need to watch this" in one line.

Bucket defaults: **Interview** → two faces, the guest's transformation word ("FIRST DEAL · 90 DAYS") ·
**Model** → one face, the question word ("WORTH IT?", "READ THIS FIRST") · **Problem** → concern face, the
mistake named · **Situation** → "this is you" phrasing · **Future** → confident face, the outcome.

## Step 3 — Score against the patterns (show the score, plain words)
Score each direction 0–2 on: curiosity · emotion · clarity · text differs from the title · 3–5 words ·
expression matches · contrast · simplicity · mobile legibility (9 criteria, 18 max). Say in one line where
each loses points. Recommend one as the primary and keep all three (YouTube's Test & Compare runs three — `97`).
State the swipe-file status honestly: *"Mike's swipe file isn't in yet; these are scored on his lesson rules
and I'll re-score when it lands."* Never claim a pattern the reference does not hold.

## Step 4 — The brief (paste-ready, for Claude Design)
Deliver this block in chat and save it as **Thumbnail Brief — [title] — YYYY-MM-DD** in the video's folder
under `03 · Content/Long-Form/` (rendered through `shared/render_doc.py`); the finished images come back from
Claude Design into the same video folder ("push this to my Drive" there, or the member drops them in — the
Brain's drive map puts a video's thumbnails next to its script, never in a Graphics bucket):
```
THUMBNAIL BRIEF — "[title]"
Run in: your Brand HQ project in Claude Design — paste this whole brief into a new chat there (Design System file + Brain Book attached, per your Design Studio START-HERE) and ask for the three thumbnails; no Brand HQ project or Design System yet → paste it into any Claude Design chat with your headshot attached, or hand it to your designer — the brief is complete on its own; there is no separate thumbnail design skill
VIDEO: bucket · the type of agent it's for · the emotion of the title
BRAND: colors (hex) · display font · headshot set to use · logo rule
DIRECTION 1 (primary · score x/18): text · face/expression · composition · color · feeling
DIRECTION 2 (score x/18): …
DIRECTION 3 (score x/18): …
RULES THE DESIGN MUST KEEP: 3–5 words · text ≠ title · face ≈ 1/3 · one supporting element · legible at 320px
OUTPUT: three 1280×720 thumbnails, one per direction — back into this video's folder under Content → Long-Form
```
Hand-off line to the member: *"paste this into a new chat in your Brand HQ project in Claude Design — it builds all three; upload them as a
test set in YouTube Studio and we read the click-through after a month."* **No Brand HQ project or Design System
yet** (`brand-visual.md` records neither): one line instead — *"paste this into any Claude Design chat with your
headshot attached, or hand it to your designer — the brief is complete on its own."* Never a detour to build
the brand first.

## Step 5 — After a month (when asked, or from `yt-analytics`)
CTR under the 6–10% band after 30 days → new title and new thumbnail (`97`); note which directions keep
winning so the style settles. `yt-analytics` reads the packaging; this skill only writes the next brief.

## Compliance gate (3-state)
Before the brief goes out: `identity/compliance.md`'s first line, `Status:` — `unset` → keep the brief in chat, say plainly the rules
are not set yet and no public packaging ships until they are; `set` → apply, remind once; `confirmed` → apply.
No "#1 / best" words, no other brokerage's logo, no compensation numbers in the text, brokerage name only as
the file requires, AI-likeness disclosure if a clone render is used.

## Rules
- No image generation, no prompt for an image model, no external tool — the brief only.
- Never invent a headshot the member does not have; if the needed expression is missing, say which to shoot.
- Plain language: "your thumbnail brief", never the skill or file names in front of the member.
