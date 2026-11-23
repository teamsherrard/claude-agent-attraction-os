#!/usr/bin/env python3
"""Downstream patch 4 of scripts/vendor-riverside.sh — make the vendored AI Editing Studio Riverside only.

Owner decision (2026-11-23): the cohort's copy of plugins/realtor-ai-editing-studio ships ONE engine, Riverside. The
Instagram Edits engine (Edits for Mac driven from the Code tab) is parked, unchanged, in
docs/parked/edits-engine-2026-11-23/ — "don't delete anything, keep it on the side". The realtor source keeps both engines;
this script is re-run after every re-vendor. Members FILMING on their phone in Instagram's Edits app (the teleprompter)
is a different thing and is kept everywhere.

Run from the repo root:  python3 scripts/strip-edits-engine.py
Standard library only. Idempotent: a second run changes nothing and exits 0.

Every member-facing passage is removed by an EXACT-STRING replacement that is asserted: if an anchor is missing and the
replacement is not already in place, the script prints the file and the anchor and exits 1, so a re-vendor that changed
the upstream text is caught instead of shipping a half-stripped plugin.
"""
import json
import os
import re
import shutil
import sys

PLUGIN = "plugins/realtor-ai-editing-studio"
NEW_VERSION = "0.7.6"
DISPLAY_NAME = "Agent Attraction AI Editing Studio (Plugin 5)"  # the realtor copy keeps its own name; two identical names showed side by side in Cowork (owner, 2026-11-23)

# Any line still carrying one of these is Edits-ENGINE text (filming on the phone in the Edits app never matches them).
ENGINE_MARKER = re.compile(
    r"\bEdits\b(?! \(teleprompter)|edits-engine\.md|edits-tool-map|edits-catalogs|edits-quirks|edits-grade-strategy|"
    r"edits-tool-reference|build_reel|scripts/edits|insta[-_]edits|default_engine: \"edits\"|`edits`|\"edits\"|"
    r"second engine|two engines|Two engines|both engines"
)

DELETE_FILES = [
    "shared/edits-engine.md",
    "shared/edits-quirks.md",
    "shared/edits-grade-strategy.md",
    "shared/edits-tool-map.md",
    "shared/edits-tool-reference.md",
    "shared/edits-catalogs.md",
]
DELETE_DIRS = ["scripts/edits"]

# The one-line engine footnote under the title of every craft reference (the § target differs per file).
ENGINES_NOTE = re.compile(
    r"> \*\*Engines\.\*\* This file is the craft rule for both engines; the Riverside calls in it are the Riverside "
    r"engine's\. On the Instagram Edits engine \(`default_engine: \"edits\"`\), the same rule is carried out with the "
    r"moves in `edits-engine\.md` § [^\n]*\n\n"
)
ENGINES_NOTE_FILES = [
    "audio", "batch", "boundaries", "brand-wiring", "broll-ladder", "caption-style", "clean-cut", "content-types",
    "cost-discipline", "craft-contract", "creative-direction", "cta-pack", "dos-and-donts", "effects-menu",
    "final-check", "footage-intake", "footage-look", "frame-qa", "graphics-style", "hook", "house-rules", "interview",
    "layouts", "music", "plain-language", "podcast", "preflight-check", "publishing", "recording", "repurpose", "rescue",
    "revisions", "sections", "trailer",
]
# The two engine PACKS carry a different footnote.
PACK_NOTE = (
    "> **Engines.** This is the Riverside engine pack. The Instagram Edits engine pack is `edits-engine.md` (playbooks) "
    "+ `edits-tool-map.md` (tools) + `edits-catalogs.md` + `edits-quirks.md`.\n\n"
)

# The `## Engine` section of every craft and director skill (one paragraph, one line).
ENGINE_SECTION = re.compile(r"## Engine\n\nRead `default_engine` in `<Brain home>/editor/config\.json`[^\n]*\n\n")
ENGINE_SECTION_SKILLS = [
    "studio-audio", "studio-batch", "studio-broll", "studio-captions", "studio-check", "studio-color",
    "studio-direction", "studio-energy", "studio-fluff", "studio-graphics", "studio-hook", "studio-interview",
    "studio-library", "studio-listing", "studio-longform", "studio-music", "studio-podcast", "studio-publish",
    "studio-record", "studio-reel", "studio-repurpose", "studio-rescue", "studio-review", "studio-sections",
    "studio-trailer", "studio-transcript",
]

SETUP_DESCRIPTION = """description: >-
  Setup for the AI Editing Studio. The first skill a real estate agent runs. Connects Riverside
  (records, edits, publishes; Cowork, the web, the desktop app; Grow plan) in two clicks with no
  key, then pulls the agent's brand from their Realtor AI Brain, writes it where the editor needs
  it, picks the caption look, registers the Video Brand Kit cards, sets the posting route, and
  gets them ready to edit with no technical setup. Stock B-roll works out of the box; free stock
  keys are OPTIONAL. Trigger on: "set up my video editor", "set up my video studio", "set up
  riverside", "connect riverside", "get me started editing", "onboard me to the editor",
  "register my video brand kit", or any first-run request for the editor.
"""

PLUGIN_DESCRIPTION = (
    "The AI Editing Studio: a full-time video editor inside the agent's Claude, on Riverside (their own account; "
    "Cowork, the web, the desktop app; no per-edit AI credits). 28 skills in five stages: DIRECT (creative direction, "
    "record coach, transcript read, section map), CUT (remove the fluff, hook finder, rescue cut, interview edit), "
    "POLISH (audio, color and look, captions, music, B-roll, B-roll library, brand graphics, energy), REPURPOSE "
    "(reels, weekly batch, podcast, trailer), SHIP (quality check, review and revise, publish), plus setup, a navigator "
    "that resumes stopped edits, and three recipes (long-form, reel, listing). Every change is verified by revision "
    "diffs and timeline reads before one 1080p export. Publishing only on an explicit yes. It never writes titles, "
    "descriptions, chapter names, or captions. Requires Plugin 1 and a Riverside Grow plan."
)

# (file, old, new) — exact strings. new == "" deletes the passage.
REPLACEMENTS = [
    # ---------------------------------------------------------------- shared/
    ("shared/riverside-playbooks.md", PACK_NOTE, ""),
    ("shared/tool-map.md", PACK_NOTE, ""),
    ("shared/house-rules.md",
     " On Edits the project itself persists on the Mac; the Brain and config still go to Drive.", ""),
    ("shared/house-rules.md",
     " The log is `rs-<editId>.md` on Riverside and `ed-<projectId>.md` on Edits, with `rev <n>` replaced by the "
     "export file name on Edits.", ""),
    ("shared/brand-wiring.md",
     "- `default_engine` (top level of the config, `\"riverside\"` or `\"edits\"`) decides which video editor owns a "
     "plain \"edit my video\" when both are installed.\n", ""),
    ("shared/publishing.md",
     "On Edits the Studio never posts; route the file to the Short-Form System's tool or the agent's share sheet.\n\n",
     ""),
    ("shared/cost-discipline.md",
     "**The agent does the last 20% by hand in their editor (Riverside or Edits)**",
     "**The agent does the last 20% by hand in Riverside**"),
    ("shared/cost-discipline.md",
     "or tweak anything yourself in your editor (Riverside or Edits) — want me to show you the 20%?",
     "or tweak anything yourself in Riverside — want me to show you the 20%?"),
    ("shared/music.md",
     "Edits level: −26 dB (its library masters are hot), ducking on, only songs whose `license.isRoyaltyFree` is true "
     "render.\n\n", ""),
    ("shared/caption-style.md",
     "Edits has no caption position or size tool; the style is one of the catalog names (Word Highlight Box by "
     "default) and the accent is set with `setCaptionHighlightColor`.\n\n", ""),
    ("shared/broll-ladder.md",
     "On Edits there is no stock search inside the server; own footage under `~/Movies`, then Pexels downloads with "
     "the agent's key; icons and emoji cards go in the upper corners, never on the face.\n\n", ""),
    ("shared/audio.md",
     "## What the Riverside engine cannot do (Edits has ducking and voice enhance)",
     "## What Riverside cannot do"),
    ("shared/frame-qa.md",
     "Rung 0 on Edits: `captureFrame` returns real rendered frames and `frameSheet(path)` reads the exported file: "
     "these ARE the render.\n\n", ""),
    ("shared/batch.md",
     " On Edits skip the podcast step and say so; long-form on Edits is not yet proven: say so and get the yes.", ""),
    ("shared/effects-menu.md",
     " On Edits: a whoosh from the built-in library on every zoom, and a 0.2 s dissolve at most where two takes jar "
     "(edits-engine.md § Energy).", ""),
    ("shared/dos-and-donts.md",
     "On the Instagram Edits engine transitions and sound effects DO exist (use them sparingly per `edits-engine.md`), "
     "and posting does NOT: the share sheet in Edits posts.\n\n", ""),
    ("shared/final-check.md",
     " **Edits:** `getSound(id)` shows `reduceNoise` ≥ 50 and `enhanceVoice` ≥ 30 on every speech piece, and the "
     "export's `loudness` peak is under −1 dBFS.", ""),
    ("shared/final-check.md",
     " **Edits:** `getColor(id).grade` shows contrast 0.10–0.20, saturation 1.06–1.12, brightness ≤ 0.08 (the "
     "`applyAdjust` 12 / 8 / 4 lift), or the measured moves logged from `edits-grade-strategy.md`.", ""),
    ("shared/final-check.md",
     " **Edits:** the captions re-read after the cut (`captions()`), the lead-in and tail cut in the `ed-` log; retake "
     "flags do not exist, so the blooper hunt is by transcript.", ""),
    ("shared/final-check.md",
     " **Edits:** −26 dB with `setDucking(video, 0.5)`, `license.isRoyaltyFree` true, the music elements spanning the "
     "final length (`elements` content music).", ""),
    ("shared/final-check.md",
     " **Edits:** `getTransformKeyframes(id)` shows the zoom pairs (scale 1.06 / 1.10 / 1.14) at the rate, a whoosh "
     "element at each zoom.", ""),
    ("shared/final-check.md",
     " **Edits:** `getCanvas` says 9:16 (or 16:9) at 30 fps; every pass in `ed-<projectId>.md` matches the timeline "
     "(`elements` counts) and the exported file exists.", ""),
    ("shared/final-check.md",
     " **Edits:** captions present in ONE catalog style with the accent set (`captions()` count ≥ 1, `fontName` set), "
     "lower third, not over the face on the viewed frame; position and width are not controllable and are N/A.", ""),
    ("shared/final-check.md",
     " Edits: `setExportSettings` 1080x1920 (or 1920x1080) HD, `exportStatus` complete, `probeMedia` on the file.",
     ""),
    ("shared/final-check.md",
     "is yours to finish by hand in your editor (Riverside, or the open Edits project), free.",
     "is yours to finish by hand in Riverside, free."),
    # ---------------------------------------------------------------- skills/ (crafts and directors)
    ("skills/studio-library/SKILL.md",
     "the editor's media panel (Riverside or\n  Instagram Edits), or files they drop in",
     "the editor's media panel in Riverside, or files they drop in"),
    ("skills/studio-longform/SKILL.md", " \"edit my YouTube video in Edits\",", ""),
    ("skills/studio-longform/SKILL.md",
     " Riverside: Playbook A/B in riverside-playbooks.md; Edits: edits-engine.md instead.", ""),
    ("skills/studio-longform/SKILL.md",
     "it is a review draft + the edit link (Riverside) or the exported file path plus the open Edits project (Edits); "
     "the spec", "it is a review draft + the edit link; the spec"),
    ("skills/studio-longform/SKILL.md",
     " Edits: the log is `ed-<projectId>.md`; log missing → read `elements`, `captions()` and the exports folder, then "
     "`build_reel.py resume`.", ""),
    ("skills/studio-graphics/SKILL.md",
     "\"my card or name strip is covering my face\",\n  \"add my graphics in Edits\". Part of",
     "\"my card or name strip is covering my face\". Part of"),
    ("skills/studio-trailer/SKILL.md", " \"make a trailer in Edits\",", ""),
    ("skills/studio-color/SKILL.md", ", \"color grade this in Edits\". Part of", ". Part of"),
    ("skills/studio-energy/SKILL.md",
     "(Riverside: a licensed sound; Edits: built-in effects)", "(a licensed sound the agent uploads once)"),
    ("skills/studio-energy/SKILL.md",
     "Transitions and a sound-effect library are not on the connector (Riverside only; Edits has both); the free",
     "Transitions and a sound-effect library are not on the connector; the free"),
    ("skills/studio-captions/SKILL.md",
     "face\", \"add captions in Edits\". Part of", "face\". Part of"),
    ("skills/studio-music/SKILL.md",
     "library (Riverside's, or royalty-free tracks on Instagram Edits) (business, lifestyle,",
     "library (Riverside's: business, lifestyle,"),
    ("skills/studio-music/SKILL.md",
     "right level: a set level per engine, quieter on a long-form,",
     "right level: -18 dB on a reel, -22 dB on a long-form,"),
    ("skills/studio-music/SKILL.md",
     "comes from an uploaded sound (Riverside) or the built-in sound effects\n  (Instagram Edits). Never a copyrighted "
     "song.", "comes from an uploaded sound. Never a copyrighted song."),
    ("skills/studio-music/SKILL.md", ", \"add music in Edits\"", ""),
    ("skills/studio-music/SKILL.md",
     "-22 dB on a long-form (Riverside; on Edits −26 dB with ducking on), faded in and out",
     "-22 dB on a long-form, faded in and out"),
    ("skills/studio-publish/SKILL.md",
     "Posts or schedules a finished edit on Riverside; on Instagram Edits it hands over the\n  exported file (the agent "
     "shares from Edits, or the Short-Form System's tool posts it) and never\n  posts. Posts to the agent's connected "
     "social channels",
     "Posts or schedules a finished edit on Riverside, to the agent's connected\n  social channels"),
    ("skills/studio-publish/SKILL.md", ", \"export it from Edits\"", ""),
    ("skills/studio-batch/SKILL.md", " \"do the whole week in Edits\",", ""),
    ("skills/studio-batch/SKILL.md",
     "| 4 | Optional: the podcast audio (on Edits skip it and say so; long-form on Edits is not yet proven: say so and "
     "get the yes) | `podcast.md` |", "| 4 | Optional: the podcast audio | `podcast.md` |"),
    ("skills/studio-podcast/SKILL.md",
     "Riverside's hosting (Riverside engine only). Episode titles", "Riverside's hosting. Episode titles"),
    ("skills/studio-sections/SKILL.md",
     " On Edits there are no timeline markers: the section times go into the hand-back only.", ""),
    ("skills/studio-repurpose/SKILL.md", " \"cut reels from this in Edits\",", ""),
    ("skills/studio-listing/SKILL.md", " \"edit my listing in Edits\",", ""),
    ("skills/studio-listing/SKILL.md",
     "clips in your Riverside media panel, or under ~/Movies on Edits, files to upload",
     "clips in your Riverside media panel, files to upload"),
    ("skills/studio-listing/SKILL.md",
     "correct the transcript in Riverside, or with editCaption on Edits, before captions",
     "correct the transcript in Riverside before captions"),
    ("skills/studio-listing/SKILL.md",
     "which hangs the editor (Riverside; Edits uses transform keyframes safely).", "which hangs the editor."),
    ("skills/studio-listing/SKILL.md",
     "A review draft with the edit link (Riverside) or the exported file path plus the open Edits project (Edits) and "
     "the spec.", "A review draft with the edit link and the spec."),
    ("skills/studio-listing/SKILL.md",
     " Edits: the log is `ed-<projectId>.md`; log missing → read `elements`, `captions()` and the exports folder, then "
     "`build_reel.py resume`.", ""),
    ("skills/studio-reel/SKILL.md", " \"make a reel in Edits\",", ""),
    ("skills/studio-reel/SKILL.md",
     " Riverside: Playbook A/B in riverside-playbooks.md; Edits: edits-engine.md instead.", ""),
    ("skills/studio-reel/SKILL.md",
     "and the edit link (Riverside) or the exported file path plus the open Edits project (Edits) (`boundaries.md`)",
     "and the edit link (`boundaries.md`)"),
    ("skills/studio-reel/SKILL.md",
     "A review draft: the edit link (Riverside) or the exported file path plus the open Edits project (Edits), the "
     "spec", "A review draft: the edit link, the spec"),
    ("skills/studio-reel/SKILL.md",
     " Edits: the log is `ed-<projectId>.md`; log missing → read `elements`, `captions()` and the exports folder, then "
     "`build_reel.py resume`.", ""),
    # ---------------------------------------------------------------- studio-navigator
    ("skills/studio-navigator/SKILL.md",
     "The friendly front door for the AI Editing Studio (Riverside or Instagram Edits engine): 28",
     "The friendly front door for the AI Editing Studio (on Riverside): 28"),
    ("skills/studio-navigator/SKILL.md",
     "this skill translates. It reads which engine they chose, turns any plain-English request into one",
     "this skill translates. It turns any plain-English request into one"),
    ("skills/studio-navigator/SKILL.md",
     "from the checkpoint log,\n  Riverside's revision history, or the open Edits project.",
     "from the checkpoint log or\n  Riverside's revision history."),
    ("skills/studio-navigator/SKILL.md",
     "\"I have a video in Riverside\", \"edit\n  this in Edits\", \"make me a reel\"",
     "\"I have a video in Riverside\", \"make me a reel\""),
    ("skills/studio-navigator/SKILL.md",
     "1. **Which video?** — **Riverside:** a recording in their Riverside",
     "1. **Which video?** — a recording in their Riverside"),
    ("skills/studio-navigator/SKILL.md",
     " **Edits:** a file under `~/Movies` (their `edits.footage_dir`; newest file wins when they say \"my video\"), a "
     "file they drop anywhere (copy it into the footage folder first; Edits refuses Downloads and Desktop), or an "
     "\"anyone with the link\" Drive link (fetch it into the footage folder with `curl -L "
     "\"https://drive.google.com/uc?export=download&id=<id>&confirm=t\"`). A Drive FOLDER with several clips is a "
     "batch (`studio-batch`).", ""),
    ("skills/studio-navigator/SKILL.md",
     "## Which engine? (read this before anything else)\n\n"
     "The Studio is the video editor, on one of two engines. Read `default_engine` in `<Brain home>/editor/config.json`:\n"
     "- **`riverside`** — the main path: edits in the agent's Riverside account, from any Claude surface (Cowork, the "
     "web, the desktop app), and publishes on a yes.\n"
     "- **`edits`** — the optional second engine: Instagram's free Edits app on the agent's Mac, driven only from the "
     "Code tab of the Claude desktop app (or the terminal) on that Mac — never from Cowork's cloud, the web or a phone. "
     "Every craft runs by `${CLAUDE_PLUGIN_ROOT}/shared/edits-engine.md`; a reel is `scripts/edits/build_reel.py`. It "
     "never posts.\n"
     "- Saying an engine's name in the request always wins (\"edit this in Edits\", \"do it in Riverside\"). An engine "
     "named that has no block in the config yet → `studio-setup` for that engine only (Step ½ + Step 1B or 1A), then "
     "continue the request. No config at all = `studio-setup`. An older `\"descript\"` = retired: treat as unset and "
     "let setup ask.\n"
     "- **An Edits agent not on their Mac right now** (Cowork, iPad, phone): say so warmly and offer Riverside if it "
     "is set up, else *\"Edits runs from the Code tab of this same Claude app on your Mac. Open the Code tab there and "
     "say 'edit my video in Edits'.\"* Never try to reach Edits from elsewhere. Someone in Cowork asking to SET UP "
     "Edits gets the same line (setup's Step ½), never an attempt.\n\n",
     "## The editor (read this before anything else)\n\n"
     "The Studio edits in the agent's Riverside account, from any Claude surface (Cowork, the web, the desktop app), "
     "and publishes on a yes. Read `<Brain home>/editor/config.json`: no config, or no `riverside` block = "
     "`studio-setup`, then continue the request. An older `default_engine` that is not `riverside` (a retired engine) "
     "= treat as unset and let setup write it.\n\n"),
    ("skills/studio-navigator/SKILL.md",
     "**Riverside:** do **one** cheap `platform_list_studios`.", "Do **one** cheap `platform_list_studios`."),
    ("skills/studio-navigator/SKILL.md",
     "and route to `studio-setup` (Step 1A).", "and route to `studio-setup` (Step 1)."),
    ("skills/studio-navigator/SKILL.md",
     "**Edits:** `~/Library/Python/3.9/bin/insta-edits doctor` (or `appState` through the `edits` tools).\n"
     "- **\"Edits app installed ✗\" / \"Automation server ✗\"** → *\"Open Edits and switch on Settings › Automation › "
     "Enable Automation Server, then say 'go'.\"* Not installed at all → `studio-setup` (Step 1B).\n"
     "- **\"Sign-in ✗ token rejected\"** → the token was regenerated or pasted twice: *\"Copy the token in Edits' "
     "Automation settings again and paste it once into the terminal I'll open.\"* (`set-token`).\n"
     "- **All ✓** = connected. Carry on. The project the script opens is the one you edit; leave Edits open.\n\n", ""),
    ("skills/studio-navigator/SKILL.md",
     "| `studio-publish` (on Edits: the file + the share sheet or the Short-Form System's tool; the Studio never posts "
     "there) |", "| `studio-publish` |"),
    ("skills/studio-navigator/SKILL.md",
     "0. **Edits engine:** the project is still on their Mac. `appState`; if it says `home`, `projects` and "
     "`openProject` the newest matching name. Read the checkpoint log `<Brain home>/editor/jobs/ed-<projectId>.md`; say "
     "what landed in one line; then `scripts/edits/build_reel.py resume` (music → graphics → check → export) with the "
     "same hook, CTA and brand flags, or hand to the craft that stopped. An import that answers \"no commit\" = "
     "`closeProject` → `openProject`, then resume. Skip the Riverside steps below.\n", ""),
    ("skills/studio-navigator/SKILL.md",
     "- **Asks for something the engine can't do.** Riverside: transitions, SFX, exact-frame VFX, fake a real place, "
     "import from a link. Edits: posting or scheduling, interviews with speaker layouts, podcast export, caption "
     "placement, anything from Cowork or claude.ai. Never a flat \"can't.\"",
     "- **Asks for something the editor can't do.** Transitions, SFX, exact-frame VFX, faking a real place, importing "
     "from a link. Never a flat \"can't.\""),
    ("skills/studio-navigator/SKILL.md",
     "every row has the warm redirect — and offer the other engine when it has the thing.",
     "every row has the warm redirect."),
    ("skills/studio-navigator/SKILL.md",
     "(a Riverside edit, or an Edits project that only references your file)", "(a Riverside edit)"),
    # ---------------------------------------------------------------- studio-setup
    ("skills/studio-setup/SKILL.md",
     "description: >-\n"
     "  Setup for the AI Editing Studio. The first skill a real estate agent runs. Connects Riverside,\n"
     "  the main path (records, edits, publishes; Cowork, the web, the desktop app; Grow plan) in two\n"
     "  clicks with no key, then pulls the agent's brand from their Realtor AI Brain, writes it where\n"
     "  the engine needs it, picks the caption look, registers the Video Brand Kit cards, sets the\n"
     "  posting route, and gets them ready to edit with no technical setup. The optional second\n"
     "  engine, Instagram's free Edits app for Mac (no per-edit fees), is set up only from the Code\n"
     "  tab of the Claude desktop app on that Mac in a guided five-minute install. Stock B-roll works\n"
     "  out of the box; free stock keys are OPTIONAL. Trigger on: \"set up my video editor\", \"set up my\n"
     "  video studio\", \"set up riverside\", \"connect riverside\", \"set up edits\", \"set up instagram\n"
     "  edits\", \"connect edits\", \"switch my editor to edits\", \"get me started editing\", \"onboard me to\n"
     "  the editor\", \"register my video brand kit\", or any first-run request for the editor.\n",
     SETUP_DESCRIPTION),
    ("skills/studio-setup/SKILL.md",
     "**Riverside is the main path** (Cowork, the web, the desktop app) and is set up first. **Instagram Edits is the "
     "optional second engine** for Mac users, set up and used only from the Code tab of the Claude desktop app on that "
     "Mac — it is included in their plan, nothing extra to buy.",
     "**Your editing runs in Riverside** (Cowork, the web, the desktop app) — connect it and we're set. One editor, "
     "never a choice to make."),
    ("skills/studio-setup/SKILL.md",
     "you only ADD the engine block (`riverside` or `edits`) and fill anything blank",
     "you only ADD the `riverside` block and fill anything blank"),
    ("skills/studio-setup/SKILL.md",
     "look for `<Brain home>/editor/config.json` and its `default_engine`. **Riverside: a filled `riverside.studio_id` "
     "AND `platform_list_studios` returns that studio = already set up. Edits: `edits.bridge_installed: true` AND, in "
     "the Code tab, `/usr/bin/python3 -m insta_edits doctor` all ✓ = already set up (in Cowork the block alone counts: "
     "Edits is used from the Code tab).**",
     "look for `<Brain home>/editor/config.json`. **A filled `riverside.studio_id` AND `platform_list_studios` returns "
     "that studio = already set up.**"),
    ("skills/studio-setup/SKILL.md",
     "3. Only if there's **no** engine block (or the engine's health check returns a real error) do you run the full "
     "setup below. \"Switch my editor to Edits/Riverside\" = run Step ½ and Step 1 for the new engine only; everything "
     "else stays.",
     "3. Only if there's **no** `riverside` block (or the health check returns a real error) do you run the full setup "
     "below."),
    ("skills/studio-setup/SKILL.md",
     "## Step ½ — The engine (Riverside is the main path)\n\n"
     "Two engines, same editor, same brand, same craft. **Riverside is the main path**: it works from Cowork, the web "
     "and the desktop app, it records, edits and publishes, and it connects in two clicks. **Instagram Edits is the "
     "optional second engine**: free, runs in Instagram's Edits app on the agent's Mac, and is driven only from the "
     "Code tab of the Claude desktop app on that Mac (the same app, the same plan, nothing extra to buy) after a guided "
     "five-minute install. Decide from where they are:\n\n"
     "- **In Cowork, on the web, on an iPad, on Windows — anywhere but the Code tab on a Mac:** set up **Riverside** "
     "(Step 1A) without asking. Once it is connected, mention Edits ONCE, in one line: *\"There's also a free option, "
     "Instagram's Edits app, for Mac users who use the Code tab of this app. Whenever you want it, open the Code tab on "
     "your Mac and say 'set up Instagram Edits' — I'll walk you through it there.\"* `default_engine: \"riverside\"`.\n"
     "- **In the Code tab on a Mac:** ask the one question, recommendation first: *\"Two ways to edit: your Riverside "
     "account (recommended — works everywhere, records and publishes too) or Instagram's free Edits app on this Mac. "
     "Riverside, Edits, or both?\"* Riverside → Step 1A. Edits → Step 1B. Both → 1A then 1B; `default_engine` stays "
     "`\"riverside\"` unless they say Edits should own a plain \"edit my video\".\n"
     "- **Someone in Cowork asks for Edits** (\"set up edits\", \"edit this in Edits\"): never try — Edits can only be "
     "reached from the Code tab on the Mac it runs on. Say: *\"Edits runs from the Code tab of this same Claude app on "
     "your Mac — it's included in your plan, nothing to buy. Open the Code tab (left sidebar → Code), pick any folder "
     "when it asks, and say 'set up Instagram Edits'. I'll walk you through it there in about five minutes. Here, I'll "
     "edit in Riverside.\"* If Riverside isn't set up either, set it up now.\n\n"
     "Write `default_engine: \"riverside\"` or `\"edits\"`. Saying an engine's name in any later request always wins "
     "over the config.\n\n",
     "## Step ½ — The editor (one, stated, never asked)\n\n"
     "There is one editor, Riverside, on every surface (Cowork, the web, the desktop app). Never ask which editor. Say "
     "it in one line — *\"Your editing runs in Riverside — connect it and we're set.\"* — and write `default_engine: "
     "\"riverside\"`.\n\n"),
    ("skills/studio-setup/SKILL.md",
     "## Step 1 — Connect the engine (the only required connection)\n\n### Step 1A — Riverside (the main path)\n\n",
     "## Step 1 — Connect Riverside (the only required connection)\n\n"),
    ("skills/studio-setup/SKILL.md",
     "This engine doesn't import from links.", "Riverside doesn't import from links."),
    ("skills/studio-setup/SKILL.md",
     "### Step 1B — Instagram Edits (the optional second engine; the Code tab on a Mac only)\n\n"
     "Run this ONLY in the Code tab (or the terminal) of the Claude desktop app on the agent's Mac. Anywhere else, give "
     "the Code-tab line from Step ½ and stop. Everything is free, it takes about five minutes, and only one step needs "
     "their hands. Needs an Apple silicon Mac on macOS 15.1 or newer. Open with one line: *\"Five small steps; I do "
     "four of them. You install Edits and paste one code — that's it.\"*\n\n"
     "1. **Install Edits for Mac** (their hands): *\"Download Edits from edits.com/desktop — a direct download, not the "
     "App Store — open it, sign in with your Instagram account, and leave it open.\"* Then: *\"In Edits, open Settings, "
     "then Automation, and switch on 'Enable Automation Server'. A box called Access token appears, with a Copy button. "
     "Leave that window open.\"* Add: *\"Keep Edits open whenever we edit; it's the editor.\"*\n"
     "2. **The bridge** (you do this; it lets Claude see all 274 editing tools, where connecting Edits directly leaves "
     "32): run `pip3 install --user insta-edits`. If the Mac asks to install the \"command line developer tools\", tell "
     "them to click Install and wait, then run it again.\n"
     "3. **The access token** (their hands only). Open a terminal tab for them with `/usr/bin/python3 -m insta_edits "
     "set-token` typed and waiting. Then, step by step: *\"1. In Edits' Automation settings, click Copy next to Access "
     "token. 2. Click once inside the black terminal window I opened. 3. Press Cmd-V once, then Return. Nothing appears "
     "as you paste — that's on purpose, it's a secret.\"* The token is like a password: never ask for it in chat and "
     "never let them paste it in chat; if it lands in chat anyway, have them click Regenerate in Edits and paste the "
     "new one in the terminal.\n"
     "4. **Connect and check** (you do this): `claude mcp add --scope user --transport stdio edits -- /usr/bin/python3 "
     "-m insta_edits serve`, then `/usr/bin/python3 -m insta_edits doctor`. All ✓ = connected: say *\"You're connected "
     "to Edits!\"* A ✗ on Sign-in = the token was pasted twice or regenerated: run set-token again. A ✗ on Automation "
     "server = Edits is closed or the switch is off. The `mcp__edits__*` tools appear in the NEXT Code session; the "
     "scripts under `${CLAUDE_PLUGIN_ROOT}/scripts/edits/` work right away.\n"
     "5. **Footage folder** (you do this): Edits only reads files under `~/Movies`. Create `~/Movies/edits-footage` and "
     "say: *\"Drop any video you want edited in here (or give me a Drive link and I'll fetch it).\"* Record "
     "`edits.footage_dir`, `exports_dir` (`~/Movies/edits-exports`), `cards_dir` (`~/Movies/edits-cards`), "
     "`bridge_installed: true`.\n\n"
     "Then go on to Step 2 (or back to Step 1A if they chose both). Edits never posts: they share from Edits' share "
     "sheet, or the Short-Form System's posting tool takes the export.\n\n", ""),
    ("skills/studio-setup/SKILL.md",
     " On Edits, captions use the chosen caption style's own face (`edits.caption_style`, default `Word Highlight "
     "Box`), and cards use the system font or a brand font the agent has installed on the Mac (`importAccountFont`); "
     "store the PostScript name in `brand.fonts.heading` only when it is installed.", ""),
    ("skills/studio-setup/SKILL.md",
     "### Step 2a — Write the brand into their Riverside studio (once; Riverside engine only — on Edits skip to Step "
     "2½)", "### Step 2a — Write the brand into their Riverside studio (once)"),
    ("skills/studio-setup/SKILL.md",
     "**On Edits:** the kit files have to be ON THE MAC, under `~/Movies`. Make `~/Movies/edits-cards/kit/` and get the "
     "kit into it: if Drive is connected and the files can be fetched from `02 · Brand/Video Brand Kit/`, do it; "
     "otherwise say, in one line, *\"Download your Video Brand Kit (the 'Download the kit' button in Claude Design, or "
     "the folder in your Drive) and unzip it into `~/Movies/edits-cards/kit` — tell me when it's there.\"* Then record "
     "each file's path in `brand.assets.*` under the same keys as below (`hook_9x16`, `cta_9x16`, `emphasis_9x16`, "
     "`cta_pack.<ask>_9x16`, `icons_dir`…), write the 9:16 zones from the spec as `brand.assets.zones.hook_9x16 = "
     "{\"y\": <zone centre ÷ 1920>, \"max_chars\": <the budget>}` (same for `emphasis_9x16`; kit v3 = 0.13 / 20), and "
     "skip every media-id step below. Edits places transparent full-frame PNGs with `addOverlay` as they are, and the "
     "reel script (`scripts/edits/build_reel.py`) reads `brand.assets` itself: the hook banner with the words typed "
     "into its zone, the CTA banner held to the last frame, the emphasis panel on pop-ups. No kit = cards are rendered "
     "natively (`scripts/edits/render_card`).\n\n", ""),
    ("skills/studio-setup/SKILL.md",
     "clips already in Riverside's media panel (Riverside) or a folder under `~/Movies` (Edits), and/or uploads",
     "clips already in Riverside's media panel, and/or uploads"),
    ("skills/studio-setup/SKILL.md",
     "3. **Caption look** for shorts → Riverside: show the named looks", "3. **Caption look** for shorts → show the named looks"),
    ("skills/studio-setup/SKILL.md",
     " Edits: offer three catalog styles in one line (Word Highlight Box, bold boxed word, the default · Word "
     "Highlight, lighter · Simple, calm) and save the pick to `edits.caption_style`; the accent colour comes from the "
     "brand.", ""),
    ("skills/studio-setup/SKILL.md",
     " **On Edits the Studio never posts:** `publish_route` is `\"shortform-tool\"` when that tool is connected, else "
     "`\"manual\"` (they share from Edits' share sheet); say so in one line.", ""),
    ("skills/studio-setup/SKILL.md",
     " Riverside only: then check `social_get_connected_platforms(studioId)`",
     " Then check `social_get_connected_platforms(studioId)`"),
    ("skills/studio-setup/SKILL.md",
     "5. **Which editor is your default?** Already answered in Step ½ (`riverside` or `edits`). If an older config "
     "still says `descript`, overwrite it with the Step ½ answer and mention it in one line.",
     "5. **Which editor is your default?** Riverside, always (`default_engine: \"riverside\"`, Step ½). If an older "
     "config says anything else (a retired engine), overwrite it and mention it in one line."),
    ("skills/studio-setup/SKILL.md",
     " **On Edits** the whoosh and the music bed come from Edits' built-in libraries (nothing to add), and a free "
     "Pexels key (`edits.pexels_key`) is the one optional upgrade for stock cutaways.", ""),
    ("skills/studio-setup/SKILL.md",
     "a little energy, and (on Riverside) I can post it to your channels", "a little energy, and I can post it to your channels"),
    ("skills/studio-setup/SKILL.md",
     "`default_engine`, the engine block (`riverside` or `edits`), the `brand` block",
     "`default_engine`, the `riverside` block, the `brand` block"),
    ("skills/studio-setup/SKILL.md",
     "If Edits was set up too, add: *\"For Edits, say it here in the Code tab: 'edit my video in Edits'.\"*\n\n", ""),
    # ---------------------------------------------------------------- README.md
    ("README.md",
     "# The AI Editing Studio (Plugin 10) — Riverside or Instagram Edits engine",
     "# The AI Editing Studio (Plugin 10) — on Riverside"),
    ("README.md",
     "on the agent's own Riverside account, with no per-edit AI credits. Riverside posts on a yes; on Instagram Edits "
     "the agent shares the exported file.",
     "on the agent's own Riverside account, with no per-edit AI credits. Riverside posts on a yes."),
    ("README.md",
     "**Claude edits · the engine renders (Riverside, or Instagram's free Edits app on the agent's Mac) · the agent "
     "approves.**", "**Claude edits · Riverside renders · the agent approves.**"),
    ("README.md",
     "One editor, two engines. Riverside is the main path (Cowork, the web, the desktop app); Instagram Edits is the "
     "optional second engine for Mac users, set up and driven from the Code tab of the Claude desktop app on that Mac. "
     "The agent picks at setup (`default_engine`: `riverside` or `edits`); saying an engine's name in a request always "
     "wins. The craft doctrine is identical on both; `shared/edits-engine.md` says how each craft runs on Edits, and "
     "`scripts/edits/build_reel.py` runs the whole reel line there in one command.\n\n",
     "One editor, one engine: Riverside, from Cowork, the web and the desktop app. (This marketplace ships the Studio "
     "Riverside only; the realtor source carries a second, Mac-only engine that is parked here under "
     "`docs/parked/` by the owner's decision of 2026-11-23.)\n\n"),
    ("README.md",
     "| | `studio-publish` — Publish | Posts or schedules on the agent's yes (Riverside); on Edits the agent shares the "
     "exported file, using the owning plugins' copy |",
     "| | `studio-publish` — Publish | Posts or schedules on the agent's yes, using the owning plugins' copy |"),
    ("README.md",
     "**Riverside engine:** Riverside Grow or higher", "Riverside Grow or higher"),
    ("README.md",
     "**Instagram Edits engine (the optional second engine):** Instagram's free Edits app for Mac (Apple silicon, "
     "macOS 15.1+) with its Automation Server on, the free open-source `insta-edits` bridge, and the Code tab of the "
     "Claude desktop app (or the terminal) on that same Mac — included in the agent's Claude plan, nothing extra to "
     "buy. Riverside is the main path; this engine is optional. No editing subscription and no per-edit fees; the only "
     "cost is the agent's Claude plan. Footage lives under `~/Movies`. Not reachable from Cowork's cloud, claude.ai, "
     "an iPad or Windows.\n\n"
     "Settings for both live in `<Brain home>/editor/config.json`.",
     "Settings live in `<Brain home>/editor/config.json`."),
    ("README.md", "## What it cannot do (and says so)\n\nRiverside engine:\n", "## What it cannot do (and says so)\n\n"),
    ("README.md",
     "Instagram Edits engine:\n"
     "- It never posts or schedules: the agent shares from Edits' share sheet, or the Short-Form System's posting tool "
     "takes the exported file.\n"
     "- No interview layouts, no podcast export, no caption position or size control (captions sit in the lower third "
     "in the chosen style). Long-form 16:9 runs on the same tools but is not yet proven end to end.\n"
     "- No stock search inside Edits' server: own footage under `~/Movies`, or Pexels downloads with the agent's free "
     "key.\n"
     "- Only royalty-free library songs render through the automation export; licensed ones play in Edits but export "
     "silent, so the music craft checks the licence flag.\n\n"
     "Both: it cannot hear or watch playback. It verifies with timeline reads, revision diffs or rendered frames, and "
     "the exported file",
     "It cannot hear or watch playback. It verifies with timeline reads, revision diffs, and the exported file"),
    ("README.md",
     "- **v0.6.0** — renamed `realtor-ai-editing-studio` (was `realtor-riverside-editor`): one AI editor, two engines. "
     "Existing installs: uninstall the old name and install the new one; settings in `<Brain home>/editor/config.json` "
     "carry over untouched. Readiness audit of the two-engine design applied.\n\n"
     "- **v0.5.0** — second engine: Instagram Edits for Mac. Setup asks which engine; every skill carries an `## "
     "Engine` section; `shared/edits-engine.md`, `edits-tool-map.md`, `edits-catalogs.md`, `edits-quirks.md`, "
     "`edits-grade-strategy.md`; `scripts/edits/` (reel builder, driver, card renderer, frame measurer); music "
     "audition and Adjust-panel grade from measurements; proven live on a 96-second talking head.\n\n",
     "- **v0.7.5 (this marketplace)** — Riverside only. The second, Mac-only engine added upstream in v0.5.0 is not "
     "shipped to the cohort (owner decision 2026-11-23; parked under `docs/parked/`, re-applied by "
     "`scripts/strip-edits-engine.py` after every re-vendor).\n\n"
     "- **v0.6.0** — renamed `realtor-ai-editing-studio` (was `realtor-riverside-editor`). Existing installs: "
     "uninstall the old name and install the new one; settings in `<Brain home>/editor/config.json` carry over "
     "untouched.\n\n"),
]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def fail(path, anchor):
    print(f"\n✗ anchor missing in {path}:\n--- anchor ---\n{anchor}\n--- end ---")
    print("The upstream text changed since this patch was written. Fix the anchor in scripts/strip-edits-engine.py "
          "(the Edits engine is parked in docs/parked/edits-engine-2026-11-23/) and run again.")
    sys.exit(1)


def main():
    if not os.path.isdir(PLUGIN):
        print(f"run from the repo root; {PLUGIN} not found")
        sys.exit(2)
    applied = 0

    # 1. the engine's own files
    for rel in DELETE_FILES:
        p = os.path.join(PLUGIN, rel)
        if os.path.exists(p):
            os.remove(p)
            applied += 1
            print(f"  deleted {rel}")
    for rel in DELETE_DIRS:
        p = os.path.join(PLUGIN, rel)
        if os.path.isdir(p):
            shutil.rmtree(p)
            applied += 1
            print(f"  deleted {rel}/")
    scripts_dir = os.path.join(PLUGIN, "scripts")
    if os.path.isdir(scripts_dir) and not os.listdir(scripts_dir):
        os.rmdir(scripts_dir)

    # 2. the config example — Riverside only
    cfg_path = os.path.join(PLUGIN, "config/editor-config.example.json")
    cfg = json.loads(read(cfg_path))
    before = json.dumps(cfg, ensure_ascii=False)
    cfg["_comment"] = ("Saved to <Brain home>/editor/config.json by studio-setup. ONE config: the brand block is the "
                       "single source of truth for every video.")
    cfg["default_engine"] = "riverside"
    cfg["_default_engine_comment"] = ("Always 'riverside' (the agent's Riverside account, any Claude surface). Any other "
                                      "value is a retired engine: setup overwrites it.")
    cfg.pop("edits", None)
    cfg.pop("_caption_style_comment", None)
    cfg["_brand_comment"] = ("SINGLE SOURCE OF TRUTH for the editor's brand. Setup writes the captured colours/font "
                             "here. If blank, readers fall back to the Brain's identity/brand-visual.md, then tasteful "
                             "defaults. There is NO separate brand.json file.")
    cfg["_publish_route_comment"] = ("ONE posting route per post. 'riverside' = Riverside's connected accounts "
                                     "(studio-publish). 'shortform-tool' = the Short-Form System's "
                                     "Metricool/GoHighLevel/Buffer. 'manual' = the agent posts the exported file "
                                     "themselves. Values: riverside | shortform-tool | manual. Long-form YouTube can use "
                                     "'riverside' while reels use the short-form tool; never both for the same post.")
    if json.dumps(cfg, ensure_ascii=False) != before:
        write(cfg_path, json.dumps(cfg, ensure_ascii=False, indent=2) + "\n")
        applied += 1
        print("  config/editor-config.example.json → Riverside only")

    # 3. the one-line engine footnotes in shared/
    for name in ENGINES_NOTE_FILES:
        p = os.path.join(PLUGIN, "shared", name + ".md")
        text = read(p)
        new, n = ENGINES_NOTE.subn("", text)
        if n == 1:
            write(p, new)
            applied += 1
        elif n == 0 and "**Engines.**" in text:
            fail(p, "> **Engines.** … (the footnote is present but its wording changed)")
        elif n == 0 and "edits-engine.md" in text:
            fail(p, "> **Engines.** … edits-engine.md § …")
        elif n > 1:
            fail(p, f"expected one Engines footnote, found {n}")

    # 4. the `## Engine` section of every craft and director skill
    for skill in ENGINE_SECTION_SKILLS:
        p = os.path.join(PLUGIN, "skills", skill, "SKILL.md")
        text = read(p)
        new, n = ENGINE_SECTION.subn("", text)
        if n == 1:
            write(p, new)
            applied += 1
        elif "## Engine" in text or "default_engine" in text:
            fail(p, "## Engine\\n\\nRead `default_engine` in `<Brain home>/editor/config.json` …")

    # 5. exact-string replacements
    for rel, old, new in REPLACEMENTS:
        p = os.path.join(PLUGIN, rel)
        if not os.path.exists(p):
            fail(p, "(file missing)")
        text = read(p)
        if old in text:
            if text.count(old) != 1:
                fail(p, f"(anchor occurs {text.count(old)} times, expected once)\n{old}")
            write(p, text.replace(old, new))
            applied += 1
        elif new and new in text:
            continue  # already applied
        elif not new and not ENGINE_MARKER.search(text):
            continue  # a deletion already applied: the file carries no engine text any more (the sweep below re-checks)
        else:
            fail(p, old)

    # 6. plugin.json — description, version, keywords
    pj_path = os.path.join(PLUGIN, ".claude-plugin/plugin.json")
    pj = json.loads(read(pj_path))
    before = json.dumps(pj, ensure_ascii=False)
    pj["description"] = PLUGIN_DESCRIPTION
    pj["version"] = NEW_VERSION
    pj["displayName"] = DISPLAY_NAME
    pj["keywords"] = [k for k in pj.get("keywords", []) if k not in ("edits", "instagram edits", "mac")]
    assert len(pj["description"]) <= 1000, len(pj["description"])
    if json.dumps(pj, ensure_ascii=False) != before:
        write(pj_path, json.dumps(pj, ensure_ascii=False, indent=2) + "\n")
        applied += 1
        print(f"  plugin.json → {NEW_VERSION}, Riverside-only description ({len(pj['description'])} chars)")

    # 7. nothing engine-shaped may remain (filming on the phone in the Edits app is allowed and does not match)
    leftovers = []
    for root, _dirs, files in os.walk(PLUGIN):
        for fn in files:
            if not fn.endswith((".md", ".json")):
                continue
            p = os.path.join(root, fn)
            for i, line in enumerate(read(p).splitlines(), 1):
                if ENGINE_MARKER.search(line):
                    leftovers.append(f"{p}:{i}: {line.strip()[:120]}")
    if leftovers:
        print("\n✗ Edits-engine text still present:")
        for l in leftovers:
            print("   " + l)
        sys.exit(1)

    print(f"✓ strip-edits-engine: {applied} change(s) applied; the Studio is Riverside only.")


if __name__ == "__main__":
    main()
