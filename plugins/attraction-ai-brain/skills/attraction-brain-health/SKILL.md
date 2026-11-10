---
name: attraction-brain-health
description: >
  Audits an Agent Attraction Brain for completeness and quality, then tells the member exactly what
  to add to make every other skill work better. Scans the identity files, the memory ledgers,
  config, and the workspace's Brand folder, scores the first-run set (the twelve setup writes, the
  derived "who your story speaks to", the three spoken answers), checks the brand chat has run and the
  brand kit is in place, reports what each later week will add without demanding it early, and
  recommends the one highest-impact next step. Never scolds; never reports by-design placeholders as
  problems. Trigger on: "check my attraction brain", "is my attraction brain complete", "what's missing
  from my attraction brain", "attraction brain health", "audit my attraction brain", "how good is my
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
profile · journey (the story with its turning points, the leader moment, the WHY) · strategy (what they
can teach, the mistakes they see) · story-bank (the six setup seeds developed) · proof (honest — zero proof
with one true line is ✅) · offer (`Status: seeds` counts as complete in Week 1; `finalized by member` or
the Week 2 build counts as complete after) · positioning (the drafted seed line counts as complete in
Week 1) · goals (`seeds` with the four numbers counts as complete in Week 1; `locked` after "set my
attraction goals") · voice · voice-samples (the three spoken answers) · voice-print (built from them) ·
avatars (DERIVED — ✅ when it names a primary group from the member's answers with the framing line;
never judged on whether the member "chose").

**Week 3 brand (two items, judged separately, never counted against the twelve; before Week 3 — `config.md → Cohort week` under 3, or the offer still at seeds — both read "coming in Week 3, with Claude Design", never a nudge):**
- **Brand direction set** = `brand-visual.md` holds an Inventory and a Creative direction (the Week 3
  brand chat ran). ⬜ → *"your brand is the next thing — say 'my attraction brand direction' in a new chat, six
  minutes."*
- **Brand kit present in `02 · Brand`** = a logo file + a style sheet + at least one profile graphic all
  exist there (the Design Package skills `aa-logo-design` → `aa-style-sheet-design` → `aa-brand-kit-design`).
  In front of the member it is always "your brand kit", never file names: ✅ *"your brand kit is in
  place"* · 🟡 (some of the three) *"your brand kit is partly there — [the missing piece] is next"* · ⬜
  *"your brand kit is the next thing to build — in Week 3, paste your Design Package brief into Claude Design, then
  upload your Week 3 Kit there for your offer kit, the guide and the page"* (the
  brief is in `brand-visual.md`; `attraction-brand-direction` regenerates it on request). Headshot
  present in `02 · Brand`? Note it the same way, one line.

**Compliance (on demand — the one thing that blocks public output):** three-state. `set` or
`confirmed` = ✅; `unset` = ⬜ and **always the first recommendation**, in the member's words: *"paste
your brokerage's compliance page link and say 'paste my compliance link' — two minutes — and every
public tool is unblocked."* Never a defect; never counted against the twelve.

**Week-by-week optional set — report as "what the week you're in adds", never as gaps:**
| Week | Files | Built by | How to report it |
|---|---|---|---|
| 1 (optional) | leadership · execution-framework | `attraction-leadership-audit` · `attraction-execution-framework` | "available whenever you want it" — one line, only if they ask what else exists |
| 2 | offer finalized · positioning full · brokerage-model · prospect-intel · why-join-me story · goals locked · operations (hours, booking link, CRM — the booking page built with the Conversion plugin's `sales-booking-page`) · `memory/top-50` seeded · then, after the offer session: magnets · list-growth · profiles | `attraction-offer` · `attraction-model-positioning` · `attraction-brokerage-model` · `attraction-prospect-radar` · `attraction-why-join-me` · `attraction-goals` · `attraction-operations` · `attraction-top-50` · the Lead Magnet plugin (`lm-navigator`, which builds the offer first) | before Week 2: say nothing unless asked; in or after Week 2: "ready to build" with the trigger phrase; the lead magnet: "say 'launch my lead magnet plugin' — it builds your offer first" |
| 3 | content-pillars · publishing · content-calendar · content-performance (profiles refreshed) | the Short-Form plugin's setup (profiles → the Game Plan → the board → the workflows) | "arrives with your Short-Form system" |
| 4 | channel · interview-pipeline | the YouTube plugin | "arrives with your YouTube system" |
| 5 | conversations · pipeline · follow-up-queue filling · sales-system · sales-funnel · intel-reports/ | the Conversion and AI Admin plugins | "fills as you talk to agents" |
| 6 | organization (fills as agents join) | `attraction-capture` and the AI Admin (organization); the Week 6 Retention & Duplication lessons | "fills as agents join; Week 6 builds the onboarding path" |
If `config.md` carries a `Cohort week` line (whichever plugin stamps it), use it; otherwise infer
nothing and report the Week 1 bar only. **Never demand a later week's deliverable early and never call it
missing.**

**The quick-reference mirror (part of the quick-ref refresh this skill owns):** when `offer.md` is finalized and
carries `## The program`, `brain.md`'s `**Program:**` line must read `[name] · [type] · [cadence]` in the same
words, and `**UVP (one line):**` must match `## UVP`'s first line; a line still reading "not built yet" or
carrying different words is stale — refresh both from `offer.md` (write → push → verify) and say nothing about
it beyond the housekeeping line. Never edit `offer.md` for this. An older `offer.md` without the block → leave the
`Program:` line as it is; it is not a gap. The same refresh applies to the `Primary avatar:` line (from
`avatars.md`'s header) and `This week's activity target:` (from `goals.md` once locked).

**Memory ledgers** (top-50 · conversations · pipeline · organization · scorecard · objections ·
debriefs · content-log · ideas · intel · deadlines): these fill as the member works — never penalize
sparse content; only flag a FILE that is missing entirely (that is a structure problem for
`attraction-brain-migrate`, reported as the one housekeeping line). Two ledgers get one positive
nudge each when empty after setup: `top-50` (*"say 'build my top 50'"*) and `scorecard` (*"say 'set my
attraction goals' to lock your targets, then 'weekly check-in' on Friday"*).

**Connectors and rhythm** (from `config.md`): storage ✓ · email · calendar · the Daily Debrief
scheduled (task id present) or not — never a defect; *"'turn on my daily debrief' any time"* · CRM named
or not (a Week 2 topic).

**Quality, not just presence (the thin check on the twelve):** a file is 🟡 if it fails the echo
test (the answer pasted under a heading, undeveloped), the any-agent test (could be any agent
anywhere), or holds `[FILL IN LATER]` / template brackets. `proof.md` is never 🟡 for being short
if it is honest — zero proof with one true line is ✅. `voice-samples.md` with typed answers but no spoken
ones is 🟡 with the one upgrade line *"'capture my attraction voice' — five minutes out loud"*.

Compute an overall completeness % on the twelve, and a one-line grade.

## Step 3 — Report + recommend
Present, warm and specific:
- **Overall:** *"Your Brain is 80% complete — a strong foundation."*
- **✅ Solid:** the domains that are good, in human words ("your story", "what you can teach", "who your
  story speaks to").
- **🟡 Could be richer:** thin ones, with the one thing to add to each.
- **⬜ Missing — biggest wins first**, ordered by impact. Always first if unset: **compliance**
  (blocks public output; *"paste my compliance link"*). Then: **the brand chat** (*"my attraction brand
  direction"*), **the brand kit** (*"paste your Design Package brief into Claude Design"*), **the spoken
  voice** (every script sounds like them), **proof** (reused everywhere), **story bank below six** (*"add
  an attraction story"*), **goals not locked** (*"set my attraction goals"*).
- **This week adds:** one line naming what the current week builds and the phrase to type — from the
  table above, never framed as a gap.
- **One recommended next action:** the single highest-impact thing, with the exact phrase to type.
- **Housekeeping, last, one line, only if needed:** a missing ledger file or an old schema →
  *"Whenever you've got a minute, say 'upgrade my attraction brain' — takes a minute, nothing is lost."*

Keep it short enough to read on a phone. Don't invent data — only report what's actually in the
files and the folder listing. Never ask where they attract or which type of agent they want. Offer the
Project Seatbelt once if `config.md` shows it was never delivered (per `shared/project-instructions.md`'s
delivery rule).
