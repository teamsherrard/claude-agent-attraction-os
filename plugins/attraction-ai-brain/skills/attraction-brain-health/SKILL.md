---
name: attraction-brain-health
description: >
  Audits an Agent Attraction Brain for completeness and quality, then tells the member exactly what
  to add to make every other skill work better. Scans the identity files, the memory ledgers,
  config, and the workspace's Brand folder, scores the first-run set, checks the brand kit is in
  place, reports what each later week will add without demanding it early, and recommends the one
  highest-impact next step. Never scolds; never reports by-design placeholders as problems.
  Trigger on: "check my attraction brain", "is my attraction brain complete", "what's missing from
  my attraction brain", "attraction brain health", "audit my attraction brain", "how good is my
  attraction brain", "attraction brain checkup", or any request to review the state or completeness
  of the member's Agent Attraction Brain.
---

# Agent Attraction Brain — Health Check

Audits the member's Brain and returns a clear, encouraging report of what's strong and what to add
next. Never scolds — frames gaps as easy wins. **Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`
before you say anything:** no file names, paths, counts, or schema talk in front of the member;
"empty is normal" for everything that fills later; housekeeping is one plain line at the end.

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md`, then scan every file in `identity/` and `memory/` plus
`config.md`. If `~/attraction-brain/` is missing, PULL it first (**attraction-brain-sync**). If
there is genuinely no Brain anywhere, tell them to say **"set up my attraction brain"** and stop. A
tool error (auth, timeout, permission) is never "no Brain" — say which connector failed instead.

Then, with the storage connector, list (names only, never download) the workspace's **`02 · Brand`**
folder, scoped to the workspace by its folder ID.

## Step 2 — Score each domain
Mark each ✅ complete · 🟡 thin (present but sparse, generic, or an unanswered placeholder) · ⬜ empty.

**The first-run TWELVE (the only completeness bar — weight these heaviest):**
profile · journey · avatars · voice · voice-samples · proof · story-bank · positioning (the seed
one-liner counts as complete in Week 1) · offer (`Status: seeds` counts as complete in Week 1;
`finalized by member` or the Week 2 build counts as complete after) · goals · compliance (three-state:
`set` or `confirmed` = ✅; `unset` = ⬜ and always the first recommendation, because it blocks every
public skill) · brand-visual (Inventory + Direction blocks present).

**Week 1 brand kit (a completeness item, judged from the workspace, not the engine):**
"brand kit present in `02 · Brand`" = **a logo file + a style sheet + at least one profile
graphic** all exist there (the Design Package skills `ds-logo` → `ds-style-sheet` → `ds-brand`
ship in Week 1, so this is a Week 1 item, not a later one). In front of the member it is always
"your brand kit", never file names: ✅ *"your brand kit is in place"* · 🟡 (some of the three) *"your
brand kit is partly there — [the missing piece] is next"* · ⬜ *"your brand kit is the next
thing to build — paste your Design Package brief into Claude Design"* (the brief is in
`brand-visual.md`; `attraction-brand-direction` regenerates it on request). Headshot present in
`02 · Brand`? Note it the same way, one line.

**Week-by-week optional set — report as "what the week you're in adds", never as gaps:**
| Week | Files | Built by | How to report it |
|---|---|---|---|
| 1 (optional) | leadership · operations · content-engine | `attraction-leadership-audit` · `attraction-operations` · the Short-Form setup (Week 3) | "available whenever you want it" — one line, only if they ask what else exists |
| 2 | offer finalized · positioning full · brokerage-model · prospect-intel · why-join-me story · `memory/top-50` seeded | `attraction-offer` · `attraction-model-positioning` · `attraction-brokerage-model` · `attraction-prospect-radar` · `attraction-why-join-me` · `attraction-top-50` | before Week 2: say nothing unless asked; in or after Week 2: "ready to build" with the trigger phrase |
| 3 | content-pillars · publishing | the Short-Form plugin's setup | "arrives with your Short-Form system" |
| 4 | channel | the YouTube plugin | "arrives with your YouTube system" |
| 5 | conversations · pipeline · follow-up-queue filling | the Conversion and AI Admin plugins | "fills as you talk to agents" |
| 6 | onboarding · duplication-kit · organization | the Team & Retention plugin | "arrives with your Team system" |
If `config.md` carries a `Cohort week` line (whichever plugin stamps it), use it; otherwise infer
nothing and report the Week 1 bar only. **Never demand a later week's deliverable early and never call it
missing.**

**Memory ledgers** (top-50 · conversations · pipeline · organization · scorecard · objections ·
debriefs · content-log · ideas · intel · deadlines): these fill as the member works — never penalize
sparse content; only flag a FILE that is missing entirely (that is a structure problem for
`attraction-brain-migrate`, reported as the one housekeeping line). Two ledgers get one positive
nudge each when empty after setup: `top-50` (*"say 'build my top 50'"*) and `scorecard` (*"say
'weekly check-in' on Friday"*).

**Connectors and rhythm** (from `config.md`): storage ✓ · email · calendar · the Daily Debrief
scheduled (task id present) or not · CRM named or not.

**Quality, not just presence (the thin check on the twelve):** a file is 🟡 if it fails the echo
test (the answer pasted under a heading, undeveloped), the any-agent test (could be any agent
anywhere), or holds `[FILL IN LATER]` / template brackets. `proof.md` is never 🟡 for being short
if it is honest — zero proof with one true line is ✅.

Compute an overall completeness % on the twelve + the brand kit, and a one-line grade.

## Step 3 — Report + recommend
Present, warm and specific:
- **Overall:** *"Your Brain is 80% complete — a strong foundation."*
- **✅ Solid:** the domains that are good, in human words ("who you attract", "your stories").
- **🟡 Could be richer:** thin ones, with the one thing to add to each.
- **⬜ Missing — biggest wins first**, ordered by impact. Always first if empty: **compliance**
  (blocks public output; *"set up my attraction compliance"*). Then: **the brand kit** (*"paste your
  Design Package brief into Claude Design"*), **voice samples** (every script sounds like them),
  **proof** (reused everywhere), **story bank below six** (*"add to my story bank"*), **goals**
  (*"set my attraction goals"*).
- **This week adds:** one line naming what the current week builds and the phrase to type — from the
  table above, never framed as a gap.
- **One recommended next action:** the single highest-impact thing, with the exact phrase to type.
- **Housekeeping, last, one line, only if needed:** a missing ledger file or an old schema →
  *"Whenever you've got a minute, say 'upgrade my attraction brain' — takes a minute, nothing is lost."*

Keep it short enough to read on a phone. Don't invent data — only report what's actually in the
files and the folder listing. Offer the Project Seatbelt once if `config.md` shows it was never
delivered (per `shared/project-instructions.md`'s delivery rule).
