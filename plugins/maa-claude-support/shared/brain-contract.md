# Brain contract — MAA Claude Support (Plugin 2)

The three laws every Agent Attraction system obeys, as they apply to a READ-ONLY help desk:
1. **Read `~/attraction-brain/brain.md` first** (pull it with `attraction-brain-sync` if the local copy is missing); never ask the member what the Brain already knows.
2. **Write back only what support owns, then push.** This plugin writes exactly three things: `memory/support-log.md` (one line per resolved or escalated ticket: date · lane · what was wrong · what fixed it), the `## MAA Support (Plugin 2)` block in `config.md` (keys, exactly: `Support: set up` · `Support desk` · `Cohort start` · `Off weeks` · `Graduation` · `Fast-action buyer` · `Configured` · `Snapshot at setup` · `Realtor Brain also present` · `Portal` · `Community`), and nothing else. It never edits identity files, ledgers, or another plugin's config block; a fix is always routed to the skill that owns the file.
3. **Compliance is someone else's gate.** Support never produces public content, so it never stamps; it reads `identity/compliance.md`'s first line (`Status:`) only to diagnose "my content was blocked".

## Reads (all read-only)
`brain.md` · `config.md` (every plugin's block, to know what is installed and which scheduled tasks exist) · `identity/profile.md` (name, brokerage, timezone for plain-English answers) · `memory/debriefs.md` and `memory/scorecard.md` (only to answer "is my debrief running?") · the Brain template at the Brain plugin's `references/brain-template/` (to know which files should exist) · `shared/stack-map.md` (this plugin's own map of every file owner).

## Never
Never reads `~/realtor-brain/` (the Social Agent OS desk owns that system; see the two-desks rule in `stack-map.md`). Never creates, edits, or deletes a scheduled task (it diagnoses them and names the owning skill). Never runs another plugin's setup. Never sends a ticket anywhere until the portal is set in `maa-support-setup`.

## Hand-offs by name
Brain: `attraction-brain-setup` · `attraction-brain-sync` · `attraction-brain-health` · `attraction-brain-migrate` · `attraction-compliance` · `attraction-debrief`. Content: `sf-setup` · `yt-setup` · `studio-setup`. Conversion: `cv-navigator` · `sales-system-setup`. Admin: `admin-setup`. Lead Magnet: `lm-navigator`. The Design Studio is reached by its START-HERE page, not by a skill name.
