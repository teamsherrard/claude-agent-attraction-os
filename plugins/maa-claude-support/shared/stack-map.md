# Stack Map — the Agent Attraction OS, plugin by plugin (Tier 1)

The concierge's brain: what each plugin does, the phrases that start it, what it depends on, how it
fails, and who fixes what. **Support routes here instead of answering "how do I make a reel" itself
— the system already has a skill for almost everything.**

## The OS at a glance — 9 Cowork plugins + the Design Studio skill set

Sales copy says "12 systems." The honest count: **9 Cowork marketplace plugins + the Design
Studio, which is a Claude Design SKILL SET (uploaded zips), not a plugin** — Claude Design cannot
run plugins. The Creative Studio (the two Higgsfield employees) is REMOVED from this build per
Mike (2026-10-08): not a plugin, parked.

| # | Plugin (install week) | Prefix | Skills | Status | Front door (say this) |
|---|---|---|---|---|---|
| 1 | **Agent Attraction Brain** (W1) | `attraction-` | 26 | **BUILT** | "Set up my **attraction** brain" |
| 2 | **MAA Claude Support** (W1) — this plugin | `maa-support-` | 9 | **BUILT** | "MAA help" / "help" / "I'm stuck" / "what did Mike say about…" |
| – | **Design Studio** (Claude Design skill set, NOT a plugin) — W1 Design Package (logo · style sheet · brand), W2 offer assets, W6 recognition · events · Value Vault; a Week 4 thumbnail is a brief from `yt-thumbnail` pasted into the member's Brand HQ project (there is no thumbnail design skill) | `aa-…-design` | 14 | **all 14 BUILT** (upload files in `design-studio/_dist`) | paste a brief into claude.ai/design; "design my attraction logo" inside Design |
| 3 | **Short-Form** (W3) | `sf-` | 13 | **BUILT** | "set up my attraction short-form" |
| 4 | **AI Editor — Riverside** (W3; the SAME plugin as the realtor marketplace, install once) | `studio-` | 28 | **vendored** | "set up my video editor" / "edit my reel" |
| 5 | **YouTube** (W4) | `yt-` | 19 | **BUILT** | "set up my YouTube for agents" |
| 6 | **Conversion & Sales** (W5) | `cv-` / `sales-` | 19 | **BUILT** | "launch conversion" / "I have a call with [name]" / "set up my sales system" |
| 7 | **AI Admin** (W5) | `admin-` | 8 | **BUILT** | "set up my attraction admin" |
| 8 | **Lead Magnet** (W6) | `lm-` | 11 | **BUILT** | "set up my lead magnet for agents" |
| 9 | **Events & Workshops** (W6) | `ev-` | 10 | **BUILT** | "plan my workshop" / "plan my agent event" |

(The cohort doc's Creative Studio and Team & Retention plugins were both removed on 2026-10-08. The numbers above are the
marketplace's — 1 Brain · 2 Support · 3 Short-Form · 4 Riverside · 5 YouTube · 6 Conversion & Sales · 7 AI Admin · 8 Lead
Magnet · 9 Events; the Design Studio is unnumbered — and the Setup Guide uses the same scheme.) Every plugin is built; a plugin
the member has not installed yet: say so honestly — *"that one switches on in Week N; until then the Brain and this week's
plugins are the whole stack"* — never pretend a skill exists. The front-door phrases above are each plugin's real trigger phrases.

**Install order:** Plugin 1 FIRST (everything reads it) → Plugin 2 → then each week's plugins
as that week opens. The Design Studio skills are uploaded at claude.ai/customize/skills (zips),
not installed from the marketplace.

**Not part of this OS at all:** the realtor marketplace's Listing Launch, Market System, Descript
editor, realtor YouTube / short-form / AI admin / lead capture plugins. They belong to the Social
Agent OS (realtor) cohort. Never route a MAA ask to them.

## Two Brains on one machine (members who are ALSO in the realtor cohort)

Some members run Mike's realtor marketplace too. Both stacks coexist on purpose:

| | Realtor (Social Agent OS) | Agent Attraction OS (this) |
|---|---|---|
| Local brain folder | `~/realtor-brain/` | `~/attraction-brain/` |
| Workspace marker | `_workspace.md` | `_attraction-workspace.md` |
| Workspace default name | the realtor's | `Agent Attraction OS` |
| Schema line in `config.md` | the realtor's numbering | `Schema: aa-1.0` |
| Sync skill | `realtor-brain-sync` | `attraction-brain-sync` |
| Support plugin | `cohort-claude-support` (`support-*`) | `maa-claude-support` (`maa-support-*`) |
| The generic phrase | **"set up my brain"** → the REALTOR plugin | **"set up my attraction brain"** / "build my agent attraction brain" / "launch the agent attraction OS" → this OS |

Rules: the two sync ladders can never find each other's workspace (different markers). A member
who says "set up my brain" with both installed gets the realtor interview — that's not a bug, it's
the reserved phrase; hand them "set up my attraction brain." A realtor Brain is a HEAD START here:
`attraction-import` pulls profile, market, voice, proof, brand-visual, and operations from
`~/realtor-brain/` read-only. Never suggest deleting either Brain.

## The master router — "I want to ___"

| Member says (any variant) | Route to | Plugin |
|---|---|---|
| "Set up my attraction brain" / "build my agent attraction brain" / "launch the agent attraction OS" / first-run | `attraction-brain-setup` | 1 |
| "Is my attraction brain complete / what's missing" | `attraction-brain-health` | 1 |
| "Load / save / back up / restore my attraction brain" · new computer | `attraction-brain-sync` | 1 |
| "Upgrade / migrate my attraction brain" · after plugin updates | `attraction-brain-migrate` | 1 |
| "Import my realtor brain / my recruiting deck / my brokerage onboarding docs / my CRM export" | `attraction-import` | 1 |
| "Who am I as a leader / my story / my journey / my why" | `attraction-brand-persona` | 1 |
| "Capture my voice" (spoken) / "add my writing samples" (written) / "add my proof / agents I've helped" | `attraction-voice-print` / `attraction-voice-proof` | 1 |
| "Add a story to my bank / my story bank" | `attraction-story-bank` | 1 |
| "My visual brand / brand direction / the Design Package brief" | `attraction-brand-direction` | 1 |
| "My 60-second why-join-me story" | `attraction-why-join-me` | 1 |
| "Pick my niche / build my agent avatars / who should I attract" | `attraction-persona-map` | 1 |
| "Who's moving in my market / agent movement / where do agents gather" · the Agent Movement Watcher | `attraction-prospect-radar` | 1 |
| "My top 50 / add [name] to my list / who's next" | `attraction-top-50` | 1 |
| "How does my model actually work / explain rev share / caps / stock" (private-call material) | `attraction-brokerage-model` | 1 |
| "How do I position my brokerage without pitching / the 2-minute model script" | `attraction-model-positioning` | 1 |
| "Build my UVP / my partner offer / my value stack" (Week 2) | `attraction-offer` | 1 |
| "What should I give away vs charge for" | `attraction-free-vs-paid` | 1 |
| "Run my rev-share scenarios" (illustrative, never a promise) | `attraction-rev-share-calculator` | 1 |
| "Set my 90-day targets / my scorecard / am I on track" | `attraction-goals` | 1 |
| "My 12-month plan / weekly KPIs / the CEO rhythm" | `attraction-execution-framework` | 1 |
| "Am I ready to lead / leadership audit" | `attraction-leadership-audit` | 1 |
| "My hours / booking link / CRM / call cadence" | `attraction-operations` | 1 |
| "My compliance rules / can I say this publicly" | `attraction-compliance` | 1 |
| "I just talked to an agent / heard an objection / got a win / have an idea" (on the go) | `attraction-capture` | 1 |
| "Run my debrief / what requires my attention today" · the Daily Agent Attraction Debrief | `attraction-debrief` | 1 |
| "What did Mike say about ___" / "ask Mike" / "which lesson covers ___" | `maa-support-cohort` (the Ask-Mike lane → `shared/kb/kb-index.md`) | 2 |
| "Help" / "I'm stuck" / any Claude question or breakage | `maa-support-navigator` | 2 |
| "design my attraction logo" / my style sheet / my offer stack / my product mockup / my playbook / my ebook / my course | an `aa-…-design` skill INSIDE Claude Design (the Brain's brand-direction skill writes the brief; a thumbnail is a `yt-thumbnail` brief pasted into the Brand HQ project) | – |
| "set up my attraction short-form" · "attraction reel ideas" · "script my attraction reels" · "attraction stories" · "attraction carousel" · "plan my attraction week" · "comment to DM for agents" | `sf-setup` · `sf-ideas` · `sf-talkinghead` · `sf-stories` · `sf-carousel` · `sf-weekly-routine` · `sf-comment-to-dm` | 3 |
| "how is my attraction content doing" · "set up my Friday performance note" (the Weekly Content Performance agent) | `sf-analytics` | 3 |
| "edit my reel" / "edit my YouTube video" / "edit my interview" · "set up my video editor" · any edit ask | `studio-navigator` (it translates + routes: `studio-reel`, `studio-longform`, `studio-interview`, `studio-setup`) | 4 |
| "my attraction game plan for YouTube" · "attraction video ideas" · "research this attraction topic" · "write my attraction script" · "build my interview pipeline" · "model breakdown video" · "SEO for my attraction video" · "repurpose my attraction video" · "triage my attraction comments" · "thumbnail brief" | `yt-gameplan` · `yt-ideation` · `yt-research` · `yt-script` · `yt-interview` · `yt-model-breakdown` · `yt-seo` · `yt-repurpose` · `yt-leads` · `yt-thumbnail` (a Claude Design brief) | 5 |
| "agent intel on [name]" · "conversation starter" · "prep my call" · "my enrollment script" · "question funnel" · "my presentation" · "set up a 3-way" · "role-play objections" · "audit my call" · "follow-up plan for [agent]" · "reactivate quiet agents" (front door: "launch conversion") | `cv-navigator` → `cv-agent-intel` · `cv-conversation-starter` · `cv-call-prep` · `cv-enrollment-script` · `cv-question-funnel` · `cv-presentation` · `cv-three-way` · `cv-objection-coach` · `cv-debrief` · `cv-follow-up` · `cv-reactivation` | 6 |
| "set up my sales system" · "write my booking page" · "set up my show-up sequence" · "my call block" · "setter script" · "my sales scorecard" | `sales-system-setup` · `sales-booking-page` · `sales-show-up` · `sales-call-block` · `sales-setter` · `sales-scorecard` | 6 |
| "set up my attraction admin" · "my attraction pipeline" / "move [agent] to [stage]" · "my follow-up queue" · "my attraction brief" / "run my morning brief" · "my recruiting scorecard" / "run my CEO review" · "monthly KPI review" · "team wins newsletter" · "VA task pack" | `admin-attraction-setup` · `admin-pipeline` · `admin-follow-up-queue` · `admin-daily` · `admin-recruiting-scorecard` · `admin-monthly-review` · `admin-newsletter` · `admin-va-tasks` | 7 |
| "launch my lead magnet plugin" / "set up my lead magnet for agents" · "build my brokerage comparison guide" · "set up my attraction funnel" · "nurture sequence for agents" | `lm-navigator` → the `lm-*` skills (magnet ideas → magnet → design → funnel → delivery → nurture → partnerships → gbp → profiles → analytics) | 8 |
| "plan my workshop" / "plan my agent event" / "host a training for agents" · "follow up after my agent event" | `ev-navigator` → the `ev-*` skills (`ev-followup` owns the Post-Event Follow-Up agent) | 9 |
| "My workbook / playbook worksheet from the course" | Finished it → `attraction-import` (reads it, files every answer) · not started → the Brain's interviews ARE the worksheet | 1 |

## Brain files each plugin reads and owns (the cross-plugin contract)

One owner per file. A reader never writes a file it doesn't own. Every write pushes. **This table is
how diagnose tells "Brain file missing" from "plugin not installed":** if a plugin's OWN file is
missing, that plugin's setup never ran; if a file it only READS is missing, the owner's skill is the
fix.

| Plugin | Reads | Owns (writes) |
|---|---|---|
| Brain (1) | everything | all `identity/` except `content-pillars · publishing · profiles · channel · sales-system`; `memory/top-50` (owner `attraction-top-50`; once the Admin registers it mirrors Stage / Last touch / Next move · Due from `pipeline` and `conversations`), `scorecard` (Targets; daily rows by the Debrief; weekly rows by the check-in until `admin-recruiting-scorecard`), `debriefs`, `objections` (heard-rows), `ideas`, `intel`, `capture-log`, `deadlines` (until the AI Admin), interim rows in `conversations` and `organization` and interim stage moves in `pipeline` (via capture, until Conversion / AI Admin) |
| Support (2) | `config`, `brain.md`, every plugin's `config` block, the Brain template (to know which files should exist) | `memory/support-log`, `memory/claude-updates`, the `## MAA Support (Plugin 2)` block in `config.md` (`Support desk: attraction`) |
| Design Studio (–) | the Brain Book (uploaded), `brand-visual`, `offer`, `positioning`, `avatars`, `proof` | nothing in the engine (assets go to the workspace's `02 · Brand`, `05 · Offer`) |
| Short-Form (3) | `profile · journey · strategy · avatars · positioning · operations · goals · offer · story-bank · proof · voice* · brand-visual · brokerage-model · compliance · content-log · objections · ideas · intel · top-50 · conversations (read-only) · magnets (## Current magnet) · content-performance` | `identity/content-pillars.md` (sf-setup), `identity/publishing.md`, `identity/profiles.md` (sf-setup writes first; `yt-setup` fills `## YouTube`; `lm-profiles` updates), `memory/content-log` (SF rows), `memory/content-performance.md` (sf-analytics), the `## Short-Form (Week 3)` block in `config.md` |
| Riverside (4) | `brand-visual · voice · profile · content-log · compliance` | `memory/content-log` (edit status), `editor/` state inside the sync allowlist; no `config.md` block |
| YouTube (5) | same as Short-Form + `content-pillars · publishing (Content board: · Keyword:) · brokerage-model · prospect-intel · leadership · organization · pipeline (read-only) · scorecard (read-only) · interview-pipeline` | `memory/content-log` (YT rows), `identity/channel.md`, `memory/interview-pipeline.md`, `profiles.md → ## YouTube`, `publishing.md → Content board:` (yt-board), the `## YouTube (Week 4)` block in `config.md` |
| Conversion (6) | `top-50 · avatars · offer · positioning · brokerage-model · objections · story-bank · proof · compliance · voice* · profile · journey · prospect-intel · operations · conversations · pipeline · debriefs · intel · intel-reports · organization · goals · scorecard (read-only) · brand-visual · sales-system · sales-funnel · magnets (## Current magnet) · events (the Next event: line)` | `memory/conversations` (its logging skills; the `Stage after` cell = the stage request), `memory/pipeline` (direct until the Admin registers; `STAGE MOVE REQUESTED` / `NEXT MOVE REQUESTED` after), `memory/objections` (handlers, heard-rows, the `## Practice log`), `memory/intel-reports/`, `identity/sales-system.md` (sales-system-setup), `memory/sales-funnel.md` (sales-scorecard), the `## Conversion & Sales` block in `config.md`; Top-50 touch cells as an interim appender until the Admin registers |
| AI Admin (7) | `operations · goals · execution-framework · compliance · voice* · profile · story-bank · proof · brand-visual · offer · top-50 · conversations · pipeline · organization · scorecard · debriefs · deadlines · content-log · capture-log · intel · objections · ideas · intel-reports · follow-up-queue · sales-funnel · list-growth · events (the dual scan with debriefs)` | `memory/pipeline` (`admin-pipeline` — stage moves, the source of stage), `memory/follow-up-queue`, `scorecard` (weekly rows, eleven columns), `deadlines`, `memory/organization` (from Week 5), the `## AI Admin (Week 5)` block in `config.md` (first line `AI Admin: set up [date]` = the OS-wide Admin-installed signal); never a Top-50 cell, never `conversations.md` |
| Lead Magnet (8) | `brain.md · avatars · offer · positioning · proof · compliance · brand-visual · voice* · story-bank · profile · journey · operations · brokerage-model · objections · ideas (leadmagnet rows) · top-50 (counts only) · config` — read-only | `memory/magnets.md` (`## Current magnet` is what every other CTA reads), `memory/list-growth.md`, `identity/profiles.md` as the Week-6 updater (lm-profiles), the `leadmagnet` rows' Status in `ideas.md`, the `## Lead Magnet (Week 6)` block in `config.md`; never `offer.md`, never `voice.md`, never a scorecard row |
| Events (9) | `avatars · offer · positioning · proof · compliance · top-50 · operations · organization` (+ read-only: `voice* · story-bank · journey · brand-visual · profile · goals · scorecard · pipeline · conversations · magnets · list-growth · content-log · intel · ideas`) | `memory/events.md` (one block per event, counts only; the header's `Next event:` line), `memory/content-log` (event rows), the `## Events (Week 6)` block in `config.md`; `memory/pipeline` only before the Admin registers — after, requests only (`STAGE MOVE REQUESTED` + the block's `Stage moves requested:` line, `NEXT MOVE REQUESTED`); never `top-50`, `conversations`, `scorecard`, `list-growth`, `magnets`, `organization`, or any `identity/` file |

**Pipeline stages, locked OS-wide:** `Identified → Conversation → Call booked → Call held → 3-way →
Joined → Onboarded → Active`. The AI Admin owns stage moves; Conversion, Events, and the Debrief
request moves through it (or write directly with the same vocabulary if Admin isn't installed
yet). A member seeing two vocabularies = a bug worth logging.

## Scheduled agents and their owners

Every agent is provisioned by its owning skill, **with the member's explicit yes, never silently**,
and is draft-only (nothing sends, posts, or publishes on its own). "It never ran" almost always
means the yes was never given or the Cowork task was never created — diagnostics tree #10.

| Agent | Cadence | Owner skill | Week |
|---|---|---|---|
| Daily Agent Attraction Debrief | daily | `attraction-debrief` (Brain) | 1 |
| Agent Movement Watcher | weekly | `attraction-prospect-radar` (Brain) | 2 |
| Weekly Content Performance | Fri | `sf-analytics` owns the task; `yt-analytics` appends its section from Week 4 | 3 |
| Morning Brief | daily | `admin-daily` owns it; `admin-attraction-setup` provisions it (task id `attraction-admin-morning-brief`) — it extends the Debrief, never a second debrief | 5 |
| Daily Follow-Up Queue | daily | `admin-follow-up-queue` | 5 |
| Call Block Prep | daily | `cv-call-prep` | 5 |
| Cold-Lead Reactivation | 30 days | `cv-reactivation` | 5 |
| Weekly Recruiting CEO Review | weekly | `admin-recruiting-scorecard` (CEO mode) | 6 |
| Monthly KPI Review | monthly | `admin-monthly-review` | 6 |
| Team Wins Newsletter | Thu | `admin-newsletter` | 6 |
| Post-Event Follow-Up | after each event | `ev-followup` | 6 |

Eleven in all (`docs/BRAIN-CONTRACT.md`). (Heidi's Wednesday Circle post is a Team-Mike scheduled task, not a member agent.)

## Per-plugin notes: dependencies & known failure modes

### Plugin 1 — Agent Attraction Brain (the keystone) — BUILT
- **Everything depends on this.** If any MAA skill says Brain files are missing → route
  `attraction-brain-setup` (never built) or `attraction-brain-sync` (built but this machine/session
  doesn't have it). A tool error is never "no Brain" — never suggest re-running setup because of an error.
- **Sync is the #1 concept:** Cowork's local desk is wiped between sessions; the CLOUD copy is the
  permanent home — **Google Drive OR Microsoft OneDrive** (`config.md`'s "Storage provider" line
  says which). Write → push → verify is atomic; reads are newest-wins; older cloud copies act as
  version history. "My brain lost everything" is almost always "run the sync pull," not data loss.
- **Migrate after updates:** plugins auto-update from the marketplace, Brain DATA doesn't reshape
  itself. Skill reports schema-behind → `attraction-brain-migrate`. Schema is `aa-1.0`.
- **Compliance is 3-state** (set / unset / confirmed): an UNSET compliance file BLOCKS public output
  with a plain message — that's the gate working, not a bug. Route `attraction-compliance`.
- **Later-week deliverables are never demanded early:** a Week 1 skill that mentions the offer or
  the content pillars is collecting raw material and saying which week builds it. "It skipped my
  offer" in Week 1 = working as designed.
- The Daily Debrief is a Cowork scheduled task created at setup Stop 16 ONLY with the member's yes.

### Plugin 2 — MAA Claude Support — BUILT (this plugin)
- Needs nothing to help. Needs a Brain to log and to track weeks (`maa-support-setup`).
- Its only writes: `memory/support-log.md`, `memory/claude-updates.md`, the config block.

### Design Studio — Claude Design skill set (W1 · W2 · W6) — BUILT
- NOT a plugin. 14 `aa-…-design` zips uploaded at claude.ai/customize/skills + the Agent Attraction
  Design System set up inside Claude Design. Reads the uploaded Brain Book, never `~/attraction-brain/`.
- Known modes: a zip rejected = description over 1024 chars or a nested zip (tree #11); "the skill
  isn't in Design's list" = wrong account/workspace (FAQ Q38); "it doesn't look like my brand" =
  the design system was never set up in Design (the root fix).

### Plugin 3 — Short-Form (W3) — BUILT
- Depends on: Brain (avatars, positioning, story-bank, compliance). Publishing = bring-your-own
  (Metricool, or manual). The ManyChat sequences are a bonus-asset import on the member's own
  ManyChat account, not a plugin feature.
- Known modes: nothing auto-posts — approval is the last gate; "it didn't post" is usually an
  unapproved queue.

### Plugin 4 — AI Editor, Riverside (W3) — vendored (the same plugin as the realtor marketplace)
- Depends on: Brain (`brand-visual`, `voice`, `compliance`) + the **Riverside connector on the
  member's own account**. No Descript, ever.
- Known modes: connector connected but reads fail → tree #12; edits persist in Riverside, state in
  the Brain's `editor/` allowlist.

### Plugin 5 — YouTube (W4) — BUILT
- Depends on: Brain + `content-pillars` (written by `sf-setup` in Week 3 — "YouTube wants my
  pillars" means run the short-form setup first). House rhythm: one chat = one video.
- Thumbnails are a Claude Design brief (`yt-thumbnail`), not a Higgsfield job.

### Plugin 6 — Conversion & Sales (W5) — BUILT
- Depends on: Brain (`top-50`, `avatars`, `offer`, `positioning`, `brokerage-model`, `objections`,
  `compliance`). Objection role-play runs in Claude Voice — the member talks, Claude plays the agent.
- Known modes: "it won't give me an income number on the call script" = compliance gate (no
  earnings claims) working as designed.

### Plugin 7 — AI Admin (W5) — BUILT
- Depends on: Brain (`operations`) + Gmail + Google Calendar (or Microsoft 365). Never auto-sends.
  Owns pipeline stage moves; "the stages look different in two places" = log it.

### Plugin 8 — Lead Magnet (W6) · Plugin 9 — Events (W6) — BUILT

*Team & Retention was removed from the OS on 2026-10-08 (not built). `memory/organization.md` stays in the Brain; capture and the AI Admin write joins to it.*
- All read the Brain's `offer`/`avatars`/`compliance`; Lead Magnet's first magnet is the Honest
  Brokerage Comparison Guide (non-disparagement rules apply — cardinal rule #1); Events writes
  the promo content, event tooling (Zoom, registration page) is the member's own.

## Cross-cutting known issues (any plugin)

| Symptom | Reality | Fix route |
|---|---|---|
| "It forgot everything from yesterday" | Chats are workbenches; the Brain is the memory | Teach §3 doctrine; anything missing → `attraction-capture` |
| "Brain missing" on a machine that had it | Fresh Cowork desk; the cloud copy is fine | `attraction-brain-sync` pull |
| "No Brain found" but they built one — and they also run the realtor plugins | Wrong plugin answered (marker/phrase disambiguation) | Diagnostics tree #1b |
| Claude can't read a folder (often Downloads/Desktop on Mac) | The Mac protects those folders per-app | Diagnostics tree #7 |
| Connector "connected" but reads fail | Expired login or wrong Google account | Diagnostics tree #2 |
| "Nothing happened when I typed it" | Plugin not installed (or not shipped yet this week), or phrasing missed the trigger | Diagnostics tree #3 |
| A skill refuses to make anything public | Compliance is UNSET (3-state gate) | `attraction-compliance`; never "just proceed" |
| A skill refuses to state an income / rev-share number | No-earnings-claims rule; every number is illustrative and labelled | Working as designed; `attraction-rev-share-calculator` for scenarios |
| My debrief / watcher never ran | Consent never given, or the Cowork task was never created | Diagnostics tree #10 |
| A Claude Design zip won't upload | Description > 1024 chars or a nested zip | Diagnostics tree #11 |
| Docs come out unstyled/ugly | Deliverables render via the shared styled-doc pipeline | Log as bug via `maa-support-escalate` |
| A skill wants a tool the member skipped (ManyChat, Metricool, Notion…) | Bring-your-own tools are optional by design | Offer the setup path, or the manual path |
| "It says it sent/saved/booked it — I can't find it" | Claimed-done ≠ done: verify with one cheap read | Diagnostics tree #9 |
| "Do I need Higgsfield / the AI clone / the Thumbnail Employee?" | Parked — not in this OS | Honest answer; log the ask |
| "Where's the listing / market update skill?" | Not part of agent attraction; those are realtor-cohort plugins | Honest answer; if they're in both cohorts, that's the realtor stack |


## Two support desks (dual-cohort members)

If the realtor marketplace is also installed, two help desks exist. This desk answers anything about agents, attraction, recruiting, the organization, partner calls, or an MAA week; the Social Agent OS desk answers buyers, sellers, listings, market updates, and SAO weeks. Explicit phrases: *MAA help* / *attraction help* → this desk; *SAO help* → the other. When the words don't decide, the navigator asks once and remembers (`config.md → Support desk`).
