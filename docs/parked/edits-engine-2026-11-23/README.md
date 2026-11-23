# Parked: the Instagram Edits engine of the AI Editing Studio (2026-11-23)

## What this is

The second editing engine of `plugins/realtor-ai-editing-studio` (the AI Editing Studio, Plugin 10): Claude driving
Instagram's free **Edits for Mac** app through its built-in automation server and the `insta-edits` bridge, from the
Code tab of the Claude desktop app on the member's own Mac. Everything here is an unchanged copy of the files as they
were vendored from the realtor repo at Studio 0.7.4:

- `shared/edits-engine.md` — the engine playbook (how every craft runs on Edits)
- `shared/edits-quirks.md` — known traps of the automation server
- `shared/edits-grade-strategy.md` — the Adjust-panel grade decided from frame measurements
- `shared/edits-tool-map.md` — job → Edits tool
- `shared/edits-tool-reference.md` — the tool signatures
- `shared/edits-catalogs.md` — the caption styles, fonts, music and effects catalogs
- `scripts/edits/` — `build_reel.py` (the whole reel line in one command), `edits_drive.py` (one tool call at a time),
  `render_card.swift`, `frame_stats.swift`, `dump_catalogs.py`, and their README

The member-facing passages (the engine question in setup, the five-step install, the Edits routes in the navigator,
the `## Engine` section of every craft skill, the `edits` block of `config/editor-config.example.json`) were removed from
the shipped plugin by `scripts/strip-edits-engine.py`; they are not copied here because they are recoverable from the
realtor source in one command (below).

## Why it is parked

Owner decision, 2026-11-23: the cohort's AI Editing Studio is **Riverside only**. In the owner's words, the Edits engine is
"complicated, probably won't work for most people" — a Mac-only install with a terminal step, a pasted token and an app
that has to stay open, for a cohort that edits from Cowork, the web and iPads. "Don't delete anything, keep it on the
side" — so it lives here, untouched.

**Not parked:** members FILMING on their phone in Instagram's free Edits app (the teleprompter named by the Short-Form
and YouTube sittings, and by `studio-record`). That is a different thing and stays everywhere.

## Where it still lives

- The realtor marketplace plugin (`teamsherrard/claude-agent-os`, `plugins/realtor-ai-editing-studio`), which keeps both
  engines. The cohort copy is vendored from it by `scripts/vendor-riverside.sh`.
- The standalone `edits-reel` skill in the owner's private workspace (`claude-home/skills/edits-reel`).

## How to bring it back

The vendor script re-copies the plugin from the realtor source (both engines) and then applies the downstream patches
listed in its header. Patch 4 is the strip. To ship the Edits engine again in this marketplace:

1. Open `scripts/vendor-riverside.sh` and remove (or comment out) the `python3 scripts/strip-edits-engine.py` call at the
   end, plus item 4 in the header list.
2. Re-run `scripts/vendor-riverside.sh` — the fresh copy carries the engine files, the setup steps and the config block.
3. Restore the plugin description, keywords and README wording for two engines (the realtor source has them).
4. Update `plugins/maa-claude-support` (the Support plugin follows every member-visible change) and run
   `scripts/check-release.sh realtor-ai-editing-studio`.

This folder can then be deleted; it is only a safety copy.
