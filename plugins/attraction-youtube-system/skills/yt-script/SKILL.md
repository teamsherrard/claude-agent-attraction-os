---
name: yt-script
description: >
  Script Studio for the attraction channel — writes the full teleprompter-ready script for a chosen
  idea in the member's own spoken voice, in one of the four attraction formats (Why I Switched ·
  Pain Point Series · Model Breakdown · Niche Breakdown) or the interview intro and outro, on Mike's
  structure: the pain-point hook, the resource CTA inside minute one, the value, the warm
  book-a-call CTA a third of the way in, the payoff, the next video. Pulls real stories from the
  story bank and marks them used; Why I Switched never names the old brokerage; model scripts
  explain mechanics, never compensation figures. Runs the 3-state compliance gate, saves the script
  in the video's folder, and writes the content-log row at Scripted. Triggers on "write my
  attraction script", "write the attraction script for this", "script my why I switched video",
  "write my model breakdown script", "script my pain point video", "script the interview intro",
  "write my attraction script for [title]".
---

# Script Studio — the video, in the member's voice, ready to read

Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` — the doctrine (#1), the Brain (#2), the 3-state gate (#3),
voice (#5), sourcing (#6), docs (#7). The Brain Contract (`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`):
this skill writes the **content-log row at Scripted**, stamps a story's **Used-where**, and nothing else.

**Lazy-load:** `references/format-playbooks.md` (the four formats + interview beats) at Step 2;
`references/script-format.md` (layout, conventions, the Short cut) at Step 3; doctrine §8 (structure) and §10
(the two CTAs) only if a line needs re-grounding. Never the whole doctrine.

> **One chat = one video.** Normally Step 2 of make-video. A member can also come straight here with their own
> idea ("script my why I switched video") — this chat becomes the video's chat. Gather what is missing, plainly.

## Step 1 — Gather (read; never re-ask)
- **The idea package** — from ideation / make-video (title · bucket · hook · avatar · pain · signal · thumbnail
  text) or the member's own. If their own: shape the title and angle with them in one exchange, assign the
  bucket (Problem · Situation · Future · Interview · Model), then write.
- **The Brain:** `brain.md`, then only three more files now — the rest open at Step 2 once the format is chosen:
  `identity/voice.md` (tone, hard-avoids) **and `voice-print.md`** (spoken cadence, signature phrases, never-say —
  the primary reference for a read-aloud script; empty = proceed on `voice.md`, never invent a personality) ·
  `identity/compliance.md` (the gate below — its first line, `Status:`).
  **Opened at Step 2, by the format's Pull list:** `avatars.md` (the viewer, their pain in their words) ·
  `offer.md` (the resource — `memory/magnets.md → ## Current magnet` first when it exists; `seeds` → the resource
  CTA is the Partner Call) · `identity/channel.md` → the CTA line and the booking link · `story-bank.md` (stories
  tagged to this pain or beat — rotate; check `content-log.md` for recent use) · `proof.md` (real lines only,
  consent respected) · `journey.md` (Why I Switched only — the wall, never the company) · `brokerage-model.md`
  (Model Breakdown only — mechanics; empty → *"say 'explain my model to me' first so the breakdown is accurate"*
  → `attraction-brokerage-model`, stop) · `memory/objections.md` (the objection this video answers) ·
  `memory/intel.md` (a dated fact to cite, if relevant).
- **Research facts** — only sourced ones from the Brief or the member (`(source, date)`); anything else is
  `[double-check before filming]`, never a guess.
- **Compliance, 3-state (`identity/compliance.md` — read at Step 1, its first line `Status:`):** a script is public. **unset → stop:** *"Before I write
  anything you'll say on camera, I need your compliance basics — three minutes"* → `attraction-compliance`.
  set → write, apply, remind once. confirmed → write, apply.
- Missing local Brain → `attraction-brain-sync` first; a tool error is never "no Brain."

## Step 2 — Choose the format (`references/format-playbooks.md`)
Open the chosen format's **Pull** files now (the Step 1 list) — only that format's.
Bucket → format: Situation with the member's own story → **Why I Switched** · Problem / Situation → **Pain Point
Series** · Model → **Model Breakdown** · Problem / Future deep teach → **Niche Breakdown** · Interview → the
**intro (recorded last) + outro + joint CTA** (the question map and the guest's prep belong to `yt-interview`).
Each playbook fixes the beats, the length, the hook formulas that fit, the proof and story pulls, and the lines
that never appear.

## Step 3 — Write the long-form script (`references/script-format.md` + doctrine §8)
- **HOOK (0:00–0:15/0:30)** — the pain point in the first ten seconds, **written word for word** (`/94`): call
  out the viewer's situation → the tension or question → what they'll have by the end. Never "welcome back," a
  long intro, or a credentials dump. It matches the title and thumbnail's promise.
- **RESOURCE CTA (inside minute one)** — the channel's resource line from `channel.md`, in the member's voice:
  "grab the [resource], link in the description." No resource yet → the warm Partner Call line here and the
  mid CTA becomes the lighter reminder.
- **VALUE** — 3–5 clear sections; each answers *what they need to know · why it matters · what to do*; tactical
  enough to use today; a real story or an agent's win woven where it lands (`/93`, draft: "this is legit"); bullets
  for lists; no tangents. Model scripts: mechanics and fit, never figures.
- **CALL CTA (~a third to halfway in)** — the warm invite to a private one-on-one call, value-named, never the
  brokerage name as the pitch (`/94`, `/98`). Rotate the phrasing across videos.
- **PAYOFF** — deliver the promise; the reassurance the avatar came for.
- **NEXT VIDEO (the very end)** — the next logical video on the channel (an interview on the same pain, the
  model explained, the lane's playlist) — the last thing said (`/99`).
- **CHAPTERS** — timestamped from the sections (they feed the SEO package).
- Cues: `[brackets]` = delivery / b-roll · `>>` = on-screen text · `(source, date)` = not read aloud.

**Length:** ~140 spoken words per minute. Default 10–15 minutes (`/94`); Why I Switched 8–12; Model Breakdown
12–20; Niche Breakdown 10–20; interview intro 45–75 seconds, outro 30–45. Write the word count to fit.
Value-dense; cut filler; easy to *speak*.

## Step 4 — Voice (critical)
Write for the ear in their spoken cadence: their sentence length, their verbatim signature phrases, their
energy; honor every never-say and hard-avoid. Read it aloud as them — a line that sounds salesy, hyped, or
un-sayable in their mouth gets rewritten. **Stories:** use a banked story in the open or the close before any
example you would invent; anonymize agents and clients unless consent is on file; **stamp its Used-where** in
`story-bank.md`. A new story the member tells in chat → use it and offer to bank it (`attraction-story-bank`).
**Ship it complete — no blanks, no homework:** never `[add your story]`; every line filmable as written.

## Step 5 — The Short cut (30–45 s)
One vertical cut from the strongest moment: the pain in line one → one point → the invite. Caption + 3–5
hashtags per `shared/seo-knowledge-base.md`. (Repurposing makes three more after publish.)

## Step 6 — Compliance + fact-check (before saving)
1. Every stat, quote, brokerage fact, or agent result is sourced `(source, date)` or flagged
   `[double-check before filming]`; no invented numbers; no testimonial without consent.
2. The gate, applied: cardinal rules (no negative word about a brokerage or person) · no compensation figures,
   rev-share tiers, stock numbers, or income · no earnings implication (any unavoidable figure is illustrative,
   labeled, with the disclaimer) · the former brokerage unnamed · brokerage name and license where
   `compliance.md` requires them (the description block, not the script) · AI-likeness disclosure if a clone
   will read it · recruiting scope respected in the CTA. Fix anything flagged; never ship it.

## Step 7 — Save, log, push (write → push → verify)
1. The video folder `03 · Content/Long-Form/YYYY-MM-DD · [Title]/` (resolve per
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-setup/references/drive-structure.md`; create only now). Render on the Script
   skeleton (`references/script-format.md` → `${CLAUDE_PLUGIN_ROOT}/shared/doc-format.md`) via `render_doc.py`;
   upload as **`Script`**. Confirm plainly: *"Saved under Content → Long-Form → [video] → Script."*
2. **The content-log row at Scripted** (`memory/content-log.md`, the locked shape): Date · Platform `YouTube` ·
   Format `long-form` (or `interview`) · **Pillar** = Authority (Problem / Situation / Future), Proof
   (Interview), or Perspective (Model) · Topic / hook = `[bucket] final title` · Avatar · Story used · CTA =
   `resource: [name] · call` · Status `Scripted` · Link `—`. If `yt-interview` or `yt-model-breakdown` already
   wrote this video's row at `Idea`, **update that row** — never a second one. A captured idea the member brought
   straight here → mark its `ideas.md` row used now (make-video does this otherwise).
3. Stamp the story's Used-where. Push via `attraction-brain-sync`; verify. Save fails → say it is not saved,
   keep the script visible, retry once, stop.

## Hand-off
*"Script's ready. Next: the thumbnail brief (so you film the expression it needs), then the SEO package and
your lead map."* → `yt-thumbnail` · `yt-seo` · `yt-leads`. Interviews → `yt-interview` for the question map and
the guest's prep.
