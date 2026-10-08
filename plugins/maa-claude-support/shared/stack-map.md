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
| 2 | **MAA Claude Support** (W1) — this plugin | `maa-support-` | 9 | **BUILT** | "Help" / "I'm stuck" / "what did Mike say about…" |
| 3 | **Design Studio** (Claude Design skill set, NOT a plugin) — W1/2 Design Package (logo · style sheet · brand), W2 offer assets, W6 Value Vault | `ds-` | 15 | coming W2 | paste a brief into claude.ai/design; "design my logo" inside Design |
| 4 | **Short-Form** (W3) | `sf-` | 13 | coming W3 | "Set up my short-form engine" |
| 5 | **AI Editor — Riverside** (W3) | `studio-` | 28 | coming W3 | "Set up my studio" / "edit my reel" |
| 6 | **YouTube** (W4) | `yt-` | 19 | coming W4 | "Set up my YouTube engine" |
| 8 | **Conversion & Sales** (W5) | `cv-` / `sales-` | 19 | coming W5 | "Set up my conversion engine" |
| 9 | **AI Admin** (W5) | `admin-` | 7 | coming W5 | "Set up my AI admin" |
| 11 | **Lead Magnet** (W6) | `lm-` | 11 | coming W6 | "Build my lead magnet" |
| 12 | **Events & Workshops** (W6) | `ev-` | 10 | coming W6 | "Plan my workshop" |

(#7 was the Creative Studio and #10 Team & Retention — both removed. Numbering keeps the cohort doc's slots so the Setup Guide
and the playbooks agree.) "Coming" plugins: say so honestly — *"that one switches on in Week N;
until then the Brain and this week's plugins are the whole stack"* — never pretend a skill exists.
Exact front-door phrases for coming plugins are confirmed when each ships; the ones above are the
planned defaults.

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
| "Design my logo / style sheet / offer stack / product mockup / playbook / ebook / course" | a `ds-*` skill INSIDE Claude Design (the Brain's brand-direction skill writes the brief) | 3 |
| "Set up my short-form engine" · "give me reel ideas" · "talking-head scripts" · "stories" · "a carousel" · "my weekly routine" · "the comment-to-DM flow" | `sf-setup` · `sf-ideas` · `sf-talkinghead` · `sf-stories` · `sf-carousel` · `sf-weekly-routine` · `sf-comment-to-dm` | 4 |
| "How did my posts do" · the Weekly Content Performance agent | `sf-analytics` | 4 |
| "Edit my reel / my YouTube video / my interview" · "set up my studio" · any edit ask | `studio-navigator` (it translates + routes: `studio-reel`, `studio-longform`, `studio-interview`, `studio-setup`) | 5 |
| "My YouTube game plan" · "video ideas" · "research this topic" · "write my script" · "my interview plan" · "a model breakdown" · "SEO for this" · "repurpose this" · "YouTube leads/comments" · "a thumbnail" | `yt-gameplan` · `yt-ideation` · `yt-research` · `yt-script` · `yt-interview` · `yt-model-breakdown` · `yt-seo` · `yt-repurpose` · `yt-leads` · `yt-thumbnail` (Claude Design brief) | 6 |
| "Build an intel report on [agent]" · "a conversation starter for [agent]" · "prep my call" · "my enrollment script" · "question funnel" · "my presentation" · "set up a 3-way" · "role-play objections" · "audit my call" · "follow up with [agent]" · "reactivate cold leads" | `cv-agent-intel` · `cv-conversation-starter` · `cv-call-prep` · `cv-enrollment-script` · `cv-question-funnel` · `cv-presentation` · `cv-three-way` · `cv-objection-coach` · `cv-debrief` · `cv-follow-up` · `cv-reactivation` | 8 |
| "Set up my sales system / booking page / show-up sequence" | `sales-system-setup` · `sales-booking-page` · `sales-show-up` | 8 |
| "My pipeline / move [agent] to [stage]" · "my follow-up queue" · "my daily brief" · "my scorecard / CEO review" · "monthly KPI review" · "team wins newsletter" | `admin-pipeline` · `admin-follow-up-queue` · `admin-daily` · `admin-scorecard` · `admin-monthly-review` · `admin-newsletter` | 9 |
| "Build my lead magnet / opt-in / the Honest Brokerage Comparison Guide / nurture sequence" | the `lm-*` skills (magnet ideas → design → delivery → nurture → partnerships → analytics) | 11 |
| "Plan my virtual workshop / live event / evergreen webinar / event follow-up" | the `ev-*` skills (`ev-followup` owns the Post-Event Follow-Up agent) | 12 |
| "My workbook / playbook worksheet from the course" | Finished it → `attraction-import` (reads it, files every answer) · not started → the Brain's interviews ARE the worksheet | 1 |

## Brain files each plugin reads and owns (the cross-plugin contract)

One owner per file. A reader never writes a file it doesn't own. Every write pushes. **This table is
how diagnose tells "Brain file missing" from "plugin not installed":** if a plugin's OWN file is
missing, that plugin's setup never ran; if a file it only READS is missing, the owner's skill is the
fix.

| Plugin | Reads | Owns (writes) |
|---|---|---|
| Brain (1) | everything | all `identity/` except `content-pillars`, `memory/top-50`, `scorecard`, `debriefs`, `objections` (via capture), `ideas`, `intel`, `capture-log`, `deadlines` (until the AI Admin), interim rows in `conversations` and `organization` and interim stage moves in `pipeline` (via capture, until Conversion / AI Admin) |
| Support (2) | `config`, `brain.md`, every plugin's `config` block | `memory/support-log`, `memory/claude-updates`, the `## MAA Support (Plugin 2)` block in `config.md` |
| Design Studio (3) | the Brain Book (uploaded), `brand-visual`, `offer`, `positioning`, `avatars`, `proof` | nothing in the engine (assets go to the workspace's `02 · Brand`, `05 · Offer`) |
| Short-Form (4) | `profile · journey · avatars · positioning · story-bank · proof · voice* · compliance · content-log · objections` | `identity/content-pillars.md` (sf-setup), `memory/content-log` (SF rows), `identity/publishing` |
| Riverside (5) | `brand-visual · voice · profile · content-log · compliance` | `memory/content-log` (edit status), `editor/` state inside the sync allowlist |
| YouTube (6) | same as Short-Form + `content-pillars · brokerage-model · prospect-intel` | `memory/content-log` (YT rows), `identity/channel.md`, `memory/interview-pipeline.md` |
| Conversion (8) | `top-50 · avatars · offer · positioning · brokerage-model · objections · story-bank · proof · compliance` | `memory/conversations`, `memory/pipeline`, `memory/objections` (new handlers), `memory/intel-reports/` |
| AI Admin (9) | `operations · top-50 · conversations · pipeline · organization · scorecard · deadlines` | `memory/pipeline` (stage moves), `memory/follow-up-queue`, `scorecard` (weekly rows), `deadlines` |
| Lead Magnet (11) | `avatars · offer · positioning · proof · compliance · brand-visual` | `memory/magnets.md`, `memory/list-growth.md`, the second CTA line in `voice.md` |
| Events (12) | `avatars · offer · positioning · proof · compliance · top-50` | `memory/events.md`, `memory/pipeline` (event stages), `memory/content-log` (event content) |

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
| Daily Follow-Up Queue | daily | `admin-follow-up-queue` | 5 |
| Call Block Prep | daily | `cv-call-prep` | 5 |
| Cold-Lead Reactivation | 30 days | `cv-reactivation` | 5 |
| Weekly Recruiting CEO Review | weekly | `admin-scorecard` (CEO mode) | 6 |
| Monthly KPI Review | monthly | `admin-monthly-review` | 6 |
| Team Wins Newsletter | Thu | `admin-newsletter` | 6 |
| Post-Event Follow-Up | after each event | `ev-followup` | 6 |

(Heidi's Wednesday Circle post is a Team-Mike scheduled task, not a member agent.)

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

### Design Studio — Claude Design skill set (W2) — coming
- NOT a plugin. 15 `ds-*` zips uploaded at claude.ai/customize/skills + the Agent Attraction
  Design System set up inside Claude Design. Reads the uploaded Brain Book, never `~/attraction-brain/`.
- Known modes: a zip rejected = description over 1024 chars or a nested zip (tree #11); "the skill
  isn't in Design's list" = wrong account/workspace (FAQ Q38); "it doesn't look like my brand" =
  the design system was never set up in Design (the root fix).

### Plugin 4 — Short-Form (W3) — coming
- Depends on: Brain (avatars, positioning, story-bank, compliance). Publishing = bring-your-own
  (Metricool, or manual). The ManyChat sequences are a bonus-asset import on the member's own
  ManyChat account, not a plugin feature.
- Known modes: nothing auto-posts — approval is the last gate; "it didn't post" is usually an
  unapproved queue.

### Plugin 5 — AI Editor, Riverside (W3) — coming
- Depends on: Brain (`brand-visual`, `voice`, `compliance`) + the **Riverside connector on the
  member's own account**. No Descript, ever.
- Known modes: connector connected but reads fail → tree #12; edits persist in Riverside, state in
  the Brain's `editor/` allowlist.

### Plugin 6 — YouTube (W4) — coming
- Depends on: Brain + `content-pillars` (written by `sf-setup` in Week 3 — "YouTube wants my
  pillars" means run the short-form setup first). House rhythm: one chat = one video.
- Thumbnails are a Claude Design brief (`yt-thumbnail`), not a Higgsfield job.

### Plugin 8 — Conversion & Sales (W5) — coming
- Depends on: Brain (`top-50`, `avatars`, `offer`, `positioning`, `brokerage-model`, `objections`,
  `compliance`). Objection role-play runs in Claude Voice — the member talks, Claude plays the agent.
- Known modes: "it won't give me an income number on the call script" = compliance gate (no
  earnings claims) working as designed.

### Plugin 9 — AI Admin (W5) — coming
- Depends on: Brain (`operations`) + Gmail + Google Calendar (or Microsoft 365). Never auto-sends.
  Owns pipeline stage moves; "the stages look different in two places" = log it.

### Plugin 11 — Lead Magnet (W6) · Plugin 12 — Events (W6) — coming

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
