---
name: attraction-brain-migrate
description: >
  Upgrades a member's Agent Attraction Brain to the latest structure when the system changes how
  the Brain is organized. The plugin (skills) auto-updates from the marketplace, but the member's
  Brain DATA does not reshape itself — this skill safely migrates an older Brain to the current
  schema (adding files, renaming, moving fields) without losing any content, then pushes the result
  to their cloud workspace. Also repairs a current-schema Brain that is missing a structural file.
  Trigger on: "upgrade my attraction brain", "migrate my attraction brain", "is my attraction brain
  up to date", "my attraction brain looks out of date", "fix my attraction brain structure", or run
  this after a plugin update if a skill reports the Brain schema is behind. Do NOT trigger when the
  member wants to change their information ("update my offer" / "update my brand" / "update my
  story") — those edit content via the phase skills, not the Brain's structure.
---

# Agent Attraction Brain — Migration

**The problem this solves:** when we ship a structural change (a new required file, a renamed file,
a moved field), the new *skills* arrive automatically via the marketplace — but each member's
*Brain* (`~/attraction-brain/`, mirrored in their workspace) is still in the old shape. This skill
upgrades the Brain to match, safely, and **pushes the upgraded Brain** so the change survives the
session. Members never hear the word "migrate" — in front of them this is *"a quick tune-up"*
(per `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`).

## Step 1 — Compare versions
1. PULL first if local is missing (**attraction-brain-sync**). Read `~/attraction-brain/config.md`
   → **`Schema`** (the version the Brain is in; accept the key spelled `Brain schema` as the same
   field on any Brain and normalize it to `Schema` on write).
2. The **current schema this skill targets is: `aa-1.0`** *(maintainers: bump this line when you add
   a migration below; the template's `config.md`, this line, and the Book spec's stamp must always
   agree — `check-release.sh` tests it).*
3. **If the Brain's schema == current →** run the **repair pass** (Step 2b), then tell the member
   *"Your Brain is up to date — nothing to change."* (or *"…I added one missing file, nothing was
   lost"*). Stop.
4. **If the Brain's schema is behind →** apply each migration below in order, from the Brain's
   version up to current.
5. **Always protect first:** before changing anything, take a **snapshot** via
   `attraction-brain-sync` (SNAPSHOTS). Never migrate without a restore point in the cloud.
6. **Never run against the Realtor Brain.** `~/realtor-brain/` and the workspace marked
   `_workspace.md` are a different system with its own migrate skill; this skill touches only
   `~/attraction-brain/` and the `_attraction-workspace.md` workspace.

## Step 2 — Apply migrations (in order)
Apply only the steps newer than the Brain's current schema. After each, update **`Schema`** in
`config.md`. Preserve ALL existing content — migrations add, rename, and move; they never delete
data and never overwrite a filled file with a template.

### MIGRATIONS LOG
*(Maintainers: every time the Brain structure changes, bump "current schema" above and add an entry
here describing the exact transformation. Each entry is idempotent and safe to re-run.)*

- **→ `aa-1.0` (baseline, 2026-10):** the first Agent Attraction Brain structure (plan §4) —
  `identity/` (profile · journey · avatars · prospect-intel · positioning · offer · brokerage-model ·
  voice · voice-samples · voice-print · proof · story-bank · brand-visual · content-pillars · goals ·
  execution-framework · leadership · operations · compliance · strategy), `memory/` (top-50 · conversations ·
  pipeline · organization · scorecard · objections · debriefs · capture-log · content-log · ideas · intel ·
  intel-reports/ · deadlines), `config.md` (the registry keys in `shared/brain-contract.md`: Schema · Storage
  provider · Workspace name / ID / link · Timezone · CRM · Setup progress · Debrief time · Daily Debrief task ·
  Agent Movement Watcher task · Workspace shared with · Realtor Brain bridge · Demo brain · Cohort week — plus the
  supporting fields Owner account · Brain home · Locale · Last synced), `brain.md`,
  `exports/`. No legacy Brains exist; this is the starting point. No migration needed.

### Step 2b — Repair pass (runs on every invocation, including current-schema Brains)
A Brain can be on the right schema and still be missing a structural file (a failed push, a manual
deletion, a plugin that expected a ledger before it existed). For every file in the `aa-1.0` list
above that is **absent**, create it from the shipped template header
(`attraction-brain-setup` → `references/brain-template/attraction-brain/…`). Never touch a file
that exists. In `brain.md`, add any file-map line that is missing (descriptions per the template
`brain.md`), leaving every existing line and every quick-reference value exactly as it is. Report
repairs in one plain line.

## Step 3 — Finalize
- Confirm `config.md` now reports the current `Schema`.
- Run a quick read of `brain.md` + two identity files to confirm nothing broke.
- **PUSH** the changed files through **attraction-brain-sync** (write → push → verify). A migration
  that is not pushed is undone the moment the session ends.
- Tell the member: *"Your Brain is on the latest structure — every skill keeps working, and nothing
  was lost."* Offer nothing else; housekeeping ends here.

## Note for maintainers
This is the safety net that lets the Brain structure evolve across hundreds of installed members.
**Process when changing Brain structure:** (1) change the template + skills, (2) bump "current
schema" here, (3) add a MIGRATIONS LOG entry with the exact transform, (4) update the schema stamp
in the template `config.md` and `brain-book-spec.md`, (5) bump the plugin version + ship. Members
run "upgrade my attraction brain" (or a skill prompts them) and upgrade safely.
