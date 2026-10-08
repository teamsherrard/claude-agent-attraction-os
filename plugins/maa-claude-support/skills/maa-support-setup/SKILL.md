---
name: maa-support-setup
description: >
  One-time configuration for MAA Claude Support itself — two minutes, run once after installing the
  plugin. Records the little that support needs: the member's cohort start date (the Tuesday
  onboarding opened — so "what week am I in" works across the Thanksgiving gap and graduation),
  whether they're a fast-action buyer (bonus Week 7), their name if the Brain lacks it, and a
  snapshot of what's installed. Creates support's two memory files (support-log, claude-updates) and
  records the escalation doors — including Mike's support portal URL, which is [NOT SET] until
  entered here and must be set before launch. Reads the Brain first and never re-asks what's known.
  Trigger on: "set up my support", "set up MAA support", "configure support", "support setup", "set
  my cohort start date", "set the support portal" — or OFFERED at the END of a support session when
  the member has an attraction Brain but no support config yet. Never a detour before their question
  is resolved; never without a Brain.
---

# Support Setup — two minutes, once

Support mostly works with ZERO setup — help, teaching, diagnosis, and Ask-Mike need nothing. This
skill adds the personal layer: week tracking, the log files, and a confirmed escalation path.

**Read first:** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/plain-language.md`.

## Preflight

The attraction Brain must exist (`~/attraction-brain/` with `config.md`, schema `aa-1.0`) —
support's files live inside it so `attraction-brain-sync` carries them to the member's cloud
drive automatically. **Pull first** if sync is installed (house rule #6 — the local desk may be
stale or empty). No attraction Brain → this isn't the first step; route `maa-support-onboard`
(which routes `attraction-brain-setup`) and come back after. A `~/realtor-brain/` folder is NOT a
substitute — never write support's block into it.

## The steps

1. **Read before asking.** From the Brain: name (`identity/profile.md`), timezone (`config.md`).
   From `${CLAUDE_PLUGIN_ROOT}/shared/cohort-kb.md`: the cohort 1 calendar and the program doors
   (portal, Circle). Never re-ask any of it.
2. **Ask the ONE real question:** *"What Tuesday did your cohort open? (It's on your welcome
   email — for cohort 1 that's November 3, 2026. If you're not sure, tell me roughly when you
   joined and I'll work it out.)"* Unknown → store the best answer with `approx: true`;
   `maa-support-cohort` phrases weeks softly when approximate. If the date matches cohort 1,
   the off week (Nov 23–29) and graduation (Dec 17) come from the kb automatically.
3. **One optional follow-up, only if natural:** *"Did you buy on the workshop call, paid in full?
   That's the fast-action option that includes the bonus Week 7 in January."* Yes / no / not
   sure → `Fast-action buyer: yes | no | [NOT SET]`. Never adjudicate — their purchase
   confirmation is the truth; "not sure" stays `[NOT SET]` and the cohort lane points them there.
4. **Write the config block** — append to `~/attraction-brain/config.md` (this block is the ONE
   sanctioned support write outside the two log files; it touches nothing else in the file):

   ```markdown
   ## MAA Support (Plugin 2)
   - Support: set up YYYY-MM-DD
   - Support desk: attraction                     # which help desk answers generic phrases on this machine
   - Cohort start: YYYY-MM-DD  (approx: false)   # the Tuesday the cohort opened
   - Off weeks: 2026-11-23..2026-11-29            # from cohort-kb for cohort 1; else [NOT SET]
   - Graduation: 2026-12-17                       # from cohort-kb; else [NOT SET]
   - Fast-action buyer: [NOT SET]                 # yes | no | [NOT SET]
   - Configured: YYYY-MM-DD · plugin vX.Y.Z
   - Snapshot at setup: [plugins seen installed, one line — e.g. attraction-ai-brain, maa-claude-support]
   - Realtor Brain also present: yes | no
   - Portal: [NOT SET: Mike's support portal URL]
   - Community: [from cohort-kb or NOT SET]
   ```

5. **Create the two support files** (with headers, if missing):
   - `~/attraction-brain/memory/support-log.md` — `| date | category | question | fix | resolved |`
   - `~/attraction-brain/memory/claude-updates.md` — *"Digest of Claude changes that matter to this
     system. Newest first."*
6. **Record the doors — and say what's missing.** The support portal is `[NOT SET]` in
   `cohort-kb.md` until Mike's team provides the URL (the realtor desk's Freshdesk portal was
   suspended on 2026-09-25 and is NOT reused). This is a LAUNCH BLOCKER for Mike's team, not the
   member's problem: tell the member plainly *"the ticket door isn't wired into me yet — if
   anything needs a human before it is, I'll hand you the same ticket for the Circle thread, and
   I've logged the gap."* Never invent a URL, never mention a support email. When the URL is
   provided, re-running this skill records it (and `cohort-kb.md` is updated in the next plugin
   release). Any other `[NOT SET]` door (Circle link, call times) → "check your welcome email."
7. **Hand them the habit:** *"You're set. Two things to remember, ever: when anything confuses or
   breaks, say* **'help'** *— and when you want to know what Mike said about something, ask me
   that. Works great in voice mode from your phone too."*

Push after the write (sync's push rule). Re-running later is safe: it updates the existing block
in place (correcting a start date, recording the portal, refreshing the snapshot) — it never
duplicates the block and never touches anything else in `config.md`. Close per house rule #6:
log `setup` complete.
