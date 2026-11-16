# Stack Map — the Agent Attraction OS, plugin by plugin (Tier 1)

The concierge's brain: what each plugin does, the phrases that start it, what it depends on, how it
fails, and who fixes what. **Support routes here instead of answering "how do I make a reel" itself
— the system already has a skill for almost everything.**

## The OS at a glance — 9 Cowork plugins + the Design Studio skill set

Sales copy says "12 systems." The honest count: **9 Cowork marketplace plugins + the Design
Studio, which is a Claude Design SKILL SET (uploaded zips), not a plugin** — Claude Design cannot
run plugins. The Creative Studio plugin (the two Higgsfield "employees") is NOT part of this build
(Mike, 2026-10-08) — but the cohort's members do make their YouTube thumbnails in Higgsfield themselves, on
their own account, from the sheet `yt-thumbnail` writes (the owner, 2026-11-14).

> **Launch cut (2026-11-03): the marketplace carries Plugins 1 and 2, and since 2026-11-08 Plugin 3 (Lead Magnet, Week 2).**
> The rest are built and parked on the `wip/all-plugins` branch while they are fixed and optimized; they return to the
> marketplace one by one as the cohort reaches them. Until a plugin is back, the desk says **"coming"** and never tells a
> member to install it.

| # | Plugin (install week) | Prefix | Skills | Status | Front door (say this) |
|---|---|---|---|---|---|
| 1 | **Agent Attraction Brain** (W1) | `attraction-` | 27 | **BUILT** | "Set up my **attraction** brain" |
| 2 | **MAA Claude Support** (W1) — this plugin | `maa-support-` | 9 | **BUILT** | "MAA help" / "help" / "I'm stuck" / "what did Mike say about…" |
| – | **Design Studio** (Claude Design skill set, NOT a plugin) — W3 the Design Package (logo · style sheet · brand kit) + the offer kit · lead magnet · funnel · content + the video kit (uploaded with Riverside), W6 events · the Value Vault (incl. the partner onboarding roadmap); YouTube thumbnails are NOT designed here — the member makes them in Higgsfield from the sheet `yt-thumbnail` writes (there is no thumbnail design skill) | `aa-…-design` | 10 | **live** — ten upload zips the member gets from Circle and uploads at claude.ai/customize/skills in Week 3 (on `main` since 0.24.0; rebuilt for quality 2026-11-14) | "design my attraction logo" inside Claude Design, or a Design canvas in Cowork |
| 3 | **Lead Magnet** (W2 — install this week, run AFTER "build my partner offer") | `lm-` | 11 | **live** — in the marketplace since 2026-11-08 (0.6.0; since 0.9.0 the guide and the page go into the Week 3 Kit — the one file the member uploads to Claude Design — and the page outline has no document of its own); everything it writes lands in the member's cloud workspace and on their Brain Board | "launch my lead magnet plugin" / "set up my lead magnet for agents" |
| 4 | **Short-Form** (W4) | `sf-` | 15 | **live** — on main since 2026-11-14: one sitting, run as an interview (one step a reply; four questions the member answers in their own words; it waits after each), two keywords, the kit's six posts first, the first three Reels built on the member's answers, Notion board, nine draft-only workflows (four switched on with the member's Yes on the card, five by phrase) | "set up my attraction short-form" |
| 5 | **AI Editor — Riverside** (W4, with Short-Form — its video kit is designed in Week 3; the SAME plugin as the realtor marketplace, install once) | `studio-` | 28 | **live** — in the marketplace since 2026-11-14 (0.4.5; vendored from the realtor marketplace with the Brain-home patch) | "set up my video editor" / "edit my reel" |
| 6 | **YouTube** (W5 — date to be confirmed) | `yt-` | 19 | **live** — on main since 2026-11-14: one sitting, run as an interview (one step a reply; four questions about the member's own videos), the Channel Page, the Game Plan with the first three videos built on the member's answers, the YouTube tab (a real reference video and a publish checklist on every card), two draft-only workflows | "set up my YouTube for agents" |
| 7 | **Conversion & Sales** (W6 — date to be confirmed) | `cv-` / `sales-` | 19 | **coming** — not in the marketplace yet (launch cut 2026-11-03); built, parked on `wip/all-plugins` | "launch conversion" / "I have a call with [name]" / "set up my sales system" |
| 8 | **AI Admin** (W6 — date to be confirmed) | `admin-` | 8 | **coming** — not in the marketplace yet (launch cut 2026-11-03); built, parked on `wip/all-plugins` | "set up my attraction admin" |
| 9 | **Events & Workshops** (W7, bonus — date to be confirmed) | `ev-` | 10 | **coming** — not in the marketplace yet (launch cut 2026-11-03); built, parked on `wip/all-plugins` | "plan my workshop" / "plan my agent event" |

(The cohort doc's Creative Studio and Team & Retention plugins were both removed on 2026-10-08. The numbers above are the
marketplace's — 1 Brain · 2 Support · 3 Lead Magnet · 4 Short-Form · 5 Riverside · 6 YouTube · 7 Conversion & Sales · 8 AI
Admin · 9 Events; the Design Studio is unnumbered — and the Setup Guide uses the same scheme. Renumbered 2026-10-10 when the
Lead Magnet moved from Week 6 to Week 2.) Every plugin is built; a plugin
the member has not installed yet: say so honestly — *"that one switches on in Week N; until then the Brain and this week's
plugins are the whole stack"* — never pretend a skill exists. The front-door phrases above are each plugin's real trigger phrases.

**Install order:** Plugin 1 FIRST (everything reads it) → Plugin 2 → then each week's plugins
as that week opens — Week 2 adds Plugin 3 (the Lead Magnet) — one sitting that builds the offer first if it isn't built. The Design Studio skills are uploaded at claude.ai/customize/skills (ten zips from the Design Studio release, https://github.com/teamsherrard/claude-agent-attraction-os/releases/latest), not installed from the marketplace.

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
| "Set up my attraction brain" / "build my agent attraction brain" / "launch the agent attraction OS" / first-run (four conversations + three voice answers, one question at a time; about 45 minutes to an hour) | `attraction-brain-setup` | 1 |
| "Is my attraction brain complete / what's missing" | `attraction-brain-health` | 1 |
| "Load / save / back up / restore my attraction brain" · new computer | `attraction-brain-sync` | 1 |
| "Upgrade / migrate my attraction brain" · after plugin updates | `attraction-brain-migrate` | 1 |
| "Import my realtor brain / my recruiting deck / my brokerage onboarding docs / my CRM export" | `attraction-import` | 1 |
| "Who am I as a leader / my story / my journey / my why" | `attraction-brand-persona` | 1 |
| "Capture my voice" (spoken) / "add my writing samples" (written) / "add my proof / agents I've helped" | `attraction-voice-print` / `attraction-voice-proof` | 1 |
| "Add a story to my bank / my story bank" | `attraction-story-bank` | 1 |
| "My attraction brand direction" / my visual brand / the Design Package brief (the Week 3 brand chat, alongside Claude Design — never before Week 3) | `attraction-brand-direction` | 3 |
| "My 60-second why-join-me story" | `attraction-why-join-me` | 1 |
| "Who should I attract / who does my story speak to / refine my agent avatars" (derived from the Brain — never a type to pick; on demand) | `attraction-persona-map` | 1 |
| "Who's moving in my market / agent movement / where do agents gather" · "scan agent movement" (the news scan, on demand) | `attraction-prospect-radar` | 1 |
| "My top 50 / add [name] to my list / who's next" | `attraction-top-50` | 1 |
| "How does my model actually work / explain rev share / caps / stock" (private-call material) | `attraction-brokerage-model` | 1 |
| "How do I position my brokerage without pitching / the 2-minute model script" | `attraction-model-positioning` | 1 |
| "Build my UVP / my partner offer / my value stack" (Week 2 — the Partner Offer is a program definition: name and type, the framework, the structure, the deliverables, Day 1; shown as ONE offer card the member says yes to, then a readable document — a one-page At a glance first, the agent-facing pages 2,000–3,200 words. Since 2026-11-02: the name is outcome-based — the outcome plus the mechanism in an agent's words, two alternates offered, never a club, portal or collective; ONE question when the Brain can't answer it — does the brokerage restrict offering a package as a reason to join (`Join-gated package allowed: yes · no · unknown`; "I don't know" is fine); and the member's own pages are chapter 8 of the Week 3 Kit, not the document: how to create it, start with your upline, the brokerage rule, the marketing language, where to host it (Skool recommended, Circle the alternative), the content branches the Week 3–4 plans read first) | `attraction-offer` | 1 |
| "What should I give away vs charge for" | `attraction-free-vs-paid` | 1 |
| "Run my rev-share scenarios" (illustrative, never a promise) | `attraction-rev-share-calculator` | 1 |
| "Set my attraction goals / lock my plan / my scorecard / am I on track" (on demand after setup — setup captures only the four numbers) | `attraction-goals` | 1 |
| "My 12-month plan / weekly KPIs / the CEO rhythm" | `attraction-execution-framework` | 1 |
| "Am I ready to lead / leadership audit" | `attraction-leadership-audit` | 1 |
| "My hours / booking link / CRM / call cadence" (Week 2 — the booking page itself is built by the Conversion plugin's `sales-booking-page`) | `attraction-operations` | 1 |
| "Paste my compliance link" / my compliance rules / can I say this publicly (on demand, never at setup) | `attraction-compliance` | 1 |
| "I just talked to an agent / heard an objection / got a win / have an idea" (on the go) | `attraction-capture` | 1 |
| "Run my debrief / what requires my attention today" · the Daily Agent Attraction Debrief | `attraction-debrief` | 1 |
| "What did Mike say about ___" / "ask Mike" / "which lesson covers ___" | `maa-support-cohort` (the Ask-Mike lane → `shared/kb/kb-index.md`) | 2 |
| "Help" / "I'm stuck" / any Claude question or breakage | `maa-support-navigator` | 2 |
| "design my attraction logo" / my style sheet / my brand kit / my offer kit (the stack, the mockup, the one-pager, the deck) / my carousel / my win wall / my video brand kit / my event flyer / my value vault (my playbook, my course, my ebook, my onboarding roadmap) | an `aa-…-design` skill INSIDE Claude Design — `aa-logo-design` · `aa-style-sheet-design` · `aa-brand-kit-design` · `aa-offer-kit-design` · `aa-lead-magnet-design` · `aa-funnel-design` · `aa-content-design` · `aa-video-kit-design` · `aa-event-design` · `aa-value-vault-design` (the Brain's brand-direction skill writes the Week 3 brief; a thumbnail is a `yt-thumbnail` brief pasted into the brand project in Claude Design) | – |
| "set up my attraction short-form" (the whole Week 4 sitting, run as an interview: profiles and the two keywords confirmed → four questions answered in the member's own words → the Game Plan built on them, opening with the kit's six posts → the Notion board with 30 days mapped → the workflows and the posting tool → the first Reel, its opening chosen by the member) · "redo my short-form setup" (the whole sitting again, updating in place) · "confirm my attraction profiles" · "my attraction keywords" · "attraction reel ideas" · "script my attraction reels" (asks ONE question first, then writes) · "today's stories" · "attraction carousel" · "plan my attraction week" · "my ManyChat build sheet" · "comment to DM for agents" | `sf-setup` · `sf-ideas` · `sf-talkinghead` · `sf-stories` · `sf-carousel` · `sf-weekly-routine` · `sf-comment-to-dm` | 4 |
| "build my short-form game plan" · "plan my next 30 days of reels" · "update my short-form game plan" · "update my pillars" (also asks any interview question the member skipped) · "change my cadence" | `sf-gameplan` (the Short-Form Game Plan — pillars with angles, the member's own answers leading them, the hook bank, the two keywords, the dated 30-day calendar; built inside setup after the interview, updated on demand) | 4 |
| "map my next 30 days" · "my attraction content board" · "update my short-form board" | `sf-board` (mapping mode seeds the calendar as dated cards on the one shared Notion board) | 4 |
| "run my week plan" · "turn on my Monday week plan" · "stop my Monday week plan" · "my attraction workflows" (the nine short-form workflows — four switched on with the member's Yes on the card, five by phrase — their status, the one-sentence stop) | `sf-week-plan` (the Monday Week Plan) | 4 |
| "turn on my daily stories" · "stop my daily stories" (by phrase, not on the card) | `sf-stories` | 4 |
| "how's my content doing" · "which reels got agent DMs" · "add my numbers" · "run my attraction deep dive" (the Monthly Deep Dive, by phrase) | `sf-analytics` | 4 |
| "edit my reel" / "edit my YouTube video" / "edit my interview" · "set up my video editor" · any edit ask | `studio-navigator` (it translates + routes: `studio-reel`, `studio-longform`, `studio-interview`, `studio-setup`) | 5 |
| "set up my YouTube for agents" (the whole Week 5 sitting, run as an interview: the Channel Page → four questions about the member's own videos → the Game Plan with the first three videos built on their answers → the YouTube tab → the two workflows → the first video) · "redo my YouTube setup" · "walk me through my channel page" · "script my first three videos" (one script a reply, each from the member's own words) · "make my attraction video: [title]" · "my video is published" · "connect my YouTube numbers" · "how did my video do" | `yt-setup` · `yt-script` · `yt-make-video` · `yt-analytics` | 6 |
| "my attraction game plan for YouTube" · "refresh my attraction game plan" (also asks any interview question the member skipped) · "attraction video ideas" · "research this attraction topic" · "write my attraction script" (asks ONE question first) · "build my agent interview pipeline" · "book my agent interview" · "model breakdown for agents" · "SEO for my attraction video" · "repurpose my attraction video" · "triage my attraction comments" · "thumbnail for my attraction video" | `yt-gameplan` · `yt-ideation` · `yt-research` · `yt-script` · `yt-interview` · `yt-model-breakdown` · `yt-seo` · `yt-repurpose` · `yt-leads` · `yt-thumbnail` (a sheet for Higgsfield — the member makes the thumbnail there, never in Claude Design) | 6 |
| "agent intel on [name]" · "conversation starter" · "prep my call" · "my enrollment script" · "question funnel" · "my presentation" · "set up a 3-way" · "role-play objections" · "audit my call" · "follow-up plan for [agent]" · "reactivate quiet agents" (front door: "launch conversion") | `cv-navigator` → `cv-agent-intel` · `cv-conversation-starter` · `cv-call-prep` · `cv-enrollment-script` · `cv-question-funnel` · `cv-presentation` · `cv-three-way` · `cv-objection-coach` · `cv-debrief` · `cv-follow-up` · `cv-reactivation` | 7 |
| "set up my sales system" · "write my booking page" · "set up my show-up sequence" · "my call block" · "setter script" · "my sales scorecard" | `sales-system-setup` · `sales-booking-page` · `sales-show-up` · `sales-call-block` · `sales-setter` · `sales-scorecard` | 7 |
| "set up my attraction admin" · "my attraction pipeline" / "move [agent] to [stage]" · "my follow-up queue" · "my attraction brief" / "run my morning brief" · "my recruiting scorecard" / "run my CEO review" · "monthly KPI review" · "team wins newsletter" · "VA task pack" · "my morning brief" · "who's due today" / "draft my follow-ups" · "my pipeline at a glance" · "mirror my CRM" · "set up my VA packs" · "call my admin [name]" | `admin-attraction-setup` · `admin-pipeline` · `admin-follow-up-queue` · `admin-daily` · `admin-recruiting-scorecard` · `admin-monthly-review` · `admin-newsletter` · `admin-va-tasks` | 8 |
| "launch my lead magnet plugin" / "set up my lead magnet for agents" · "build my lead magnet for agents" · "lead magnet ideas" / "which lead magnet should I make" · "set up my attraction funnel" · "nurture sequence for agents" | `lm-navigator` → the `lm-*` skills (the offer first if it isn't built → magnet ideas, ONE from the offer → magnet → funnel → design → delivery → nurture → partnerships → gbp → profiles → analytics) | 3 |
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
| Short-Form (4) | `profile · journey · strategy · avatars · positioning · operations · goals · offer · story-bank · proof · voice* · brand-visual · brokerage-model · compliance · content-log · objections · ideas · intel · top-50 · conversations (read-only) · magnets (## Current magnet) · content-performance` | `identity/content-pillars.md` (sf-gameplan — the Game Plan, run inside sf-setup; its `## In your words` section holds the member's own interview answers, appended by sf-setup and sf-talkinghead), `identity/publishing.md` (sf-setup creates it; sf-gameplan the strategy lines), `identity/profiles.md` (the five sections — `lm-profiles` writes the file first in Week 2; `sf-setup` confirms it and refreshes a bio only when the offer, the proof or the link changed; `yt-setup` fills `## YouTube`), `memory/content-calendar.md` (sf-gameplan — the 30-day window; sf-week-plan keeps it rolling), `memory/content-log` (SF rows), `memory/content-performance.md` (sf-analytics), the `## Short-Form (Week 4)` block in `config.md` (`Week Plan task` · `Week Plan slot` · `Weekly Content Performance task` · `Daily Stories task` · `Daily Stories time`) |
| Riverside (5) | `brand-visual · voice · profile · content-log · compliance` | `memory/content-log` (edit status), `editor/` state inside the sync allowlist; no `config.md` block |
| YouTube (6) | same as Short-Form + `content-pillars · publishing (Content board: · Keyword:) · brokerage-model · prospect-intel · leadership · organization · pipeline (read-only) · scorecard (read-only) · interview-pipeline` | `memory/content-log` (YT rows), `identity/channel.md`, `memory/interview-pipeline.md`, `memory/content-calendar.md` — the `## Long-form (YouTube)` section (yt-gameplan; the Monday Kickoff flips Status) and `## Kickoff briefs (YouTube)` (the Monday Kickoff) — never the short-form table or `## Week briefs`, `profiles.md → ## YouTube`, `publishing.md → Content board:` (yt-board), the `## YouTube (Week 5)` block in `config.md`; `identity/channel.md → ## In your words` holds the member's own answers from the Week 5 interview |
| Conversion (7) | `top-50 · avatars · offer · positioning · brokerage-model · objections · story-bank · proof · compliance · voice* · profile · journey · prospect-intel · operations · conversations · pipeline · debriefs · intel · intel-reports · organization · goals · scorecard (read-only) · brand-visual · sales-system · sales-funnel · magnets (## Current magnet) · events (the Next event: line)` | `memory/conversations` (its logging skills; the `Stage after` cell = the stage request), `memory/pipeline` (direct until the Admin registers; `STAGE MOVE REQUESTED` / `NEXT MOVE REQUESTED` after), `memory/objections` (handlers, heard-rows, the `## Practice log`), `memory/intel-reports/`, `identity/sales-system.md` (sales-system-setup), `memory/sales-funnel.md` (sales-scorecard), the `## Conversion & Sales` block in `config.md`; Top-50 touch cells as an interim appender until the Admin registers |
| AI Admin (8) | `operations · goals · execution-framework · compliance · voice* · profile · story-bank · proof · brand-visual · offer · top-50 · conversations · pipeline · organization · scorecard · debriefs · deadlines · content-log · capture-log · intel · objections · ideas · intel-reports · follow-up-queue · sales-funnel · list-growth · events (the dual scan with debriefs)` | `memory/pipeline` (`admin-pipeline` — stage moves, the source of stage), `memory/follow-up-queue`, `scorecard` (weekly rows, eleven columns), `deadlines`, `memory/organization` (from Week 5), the `## AI Admin (Week 5)` block in `config.md` (first line `AI Admin: set up [date]` = the OS-wide Admin-installed signal); never a Top-50 cell, never `conversations.md` |
| Lead Magnet (3) | `brain.md · avatars · offer · positioning · proof · compliance · brand-visual · voice* · story-bank · profile · journey · operations · brokerage-model · objections · ideas (leadmagnet rows) · top-50 (counts only) · config` — read-only | `memory/magnets.md` (`## Current magnet` is what every other CTA reads), `memory/list-growth.md`, `identity/profiles.md` (lm-profiles writes it FIRST in Week 2 — the five Short-Form headings plus its own extra platforms; sf-setup refreshes the five sections in Week 3), the `leadmagnet` rows' Status in `ideas.md`, the `## Lead Magnet (Week 2)` block in `config.md`; never `offer.md`, never `voice.md`, never a scorecard row |
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
| Monday Week Plan | Mon 7:00 am | `sf-week-plan` — the week's posts drafted from the Game Plan's calendar into the board cards and a week brief (the member's own answers lead a hook where one fits); its note opens with "Last week you got [n] of [m] out" when something went out; keeps 30 days visible; on the card | 4 |
| Batch Prep | the evening before the batch day, 6:00 pm | `sf-batch-publish` — the teleprompter doc, the week's scripts grouped by outfit and location; on the card | 4 |
| Wednesday Brokerage News Watch | Wed 8:00 am | `sf-greenscreen` — three to six real, linked headlines with a 30-second take each; on the card | 4 |
| Monthly Calendar Refill | the last Friday of the month, 5:00 pm | `sf-gameplan` — the next thirty days from the pillars and what performed; on the card | 4 |
| Daily Stories | daily | `sf-stories` — three story ideas each morning as a draft; by phrase, not on the card | 4 |
| Monday Kickoff | Mon | `yt-briefing` — this week's video drafted onto its board card, into the Brain and the video's folder (opening on the member's own line when their answer names that video); tops the board up to 30 days; on `yt-setup`'s card (task id `attraction-monday-kickoff`) | 5 |
| Monthly Channel Review | monthly (the 1st) | `yt-triggers` — the month by lane, which videos brought agent conversations, the one move; switched on with the member's Yes on `yt-setup`'s card; task id `attraction-monthly-youtube-review` | 5 |
| Morning Brief | daily | `admin-daily` owns it; `admin-attraction-setup` provisions it (task id `attraction-admin-morning-brief`) — it extends the Debrief, never a second debrief — offered with the Daily Follow-Up Queue on setup's ONE consent card, after the member has seen their first brief (2026-10-18) | 6 |
| Daily Follow-Up Queue | daily | `admin-follow-up-queue` — same card as the Morning Brief; its rows are the brief's follow-ups section, drafts included | 6 |
| Call Block Prep | daily | `cv-call-prep` | 6 |
| Cold-Lead Reactivation | 30 days | `cv-reactivation` | 6 |
| Monthly KPI Review | monthly | `admin-monthly-review` | 6 |
| Team Wins Newsletter | Thu | `admin-newsletter` | 6 |
| Post-Event Follow-Up | after each event | `ev-followup` | 7 |

Fifteen in all since 2026-11-14 evening (`docs/BRAIN-CONTRACT.md`): the Short-Form plugin alone runs nine — four switched on by the member's Yes on `sf-setup`'s card (Monday Week Plan · Batch Prep · Wednesday Brokerage News Watch · Monthly Calendar Refill) and five by phrase (keyword follow-up queue · mid-week nudge · monthly deep dive · daily stories · quarterly profile audit; win and milestone posts ride inside the Monday plan; the Daily Engagement List and the Friday performance note were retired that evening) —
each created on that Yes, each draft-only, each ending with a push that rebuilds the Brain Board — "the
Monday plan never ran" usually means the card never got its Yes (`Week Plan task: later`), the member stopped it (`paused`), or the task was never created
(tree #10). The YouTube workflows — the Monday Kickoff and the Monthly Channel Review — are both switched on by the member's Yes on `yt-setup`'s card and recorded in the `## YouTube (Week 5)` block with its `Email me:` line (mirrored from the Short-Form block when it exists; set from the connected mail, never asked) — "my Monday kickoff never ran" is the same diagnosis (`Monday Kickoff task: later` or `paused`, or no task). The Weekly Attraction Ideas note was retired 2026-10-13 (the Kickoff carries the ideas). Two things members may
EXPECT to be scheduled are not, on purpose: the
Prospect Radar's news scan (`attraction-prospect-radar` — "scan agent movement") and the Weekly Recruiting CEO
Review (`admin-recruiting-scorecard` CEO mode — "run my CEO review") run on demand, with no task, no consent card,
and no config key. (Heidi's Wednesday Circle post is a Team-Mike scheduled task, not a member agent.)

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
- The Daily Debrief is a Cowork scheduled task created ONLY with the member's yes — on demand ("turn on my daily debrief") or from the AI Admin's Week 5 card, never inside Brain setup (the owner's ruling, 2026-11-02).
- **The Week 1 shape (2026-11-02):** Brain setup is four conversations (who you are as a leader · your unique approach · your story and your proof · your current and future state) asked ONE plain question at a time — Mike's 26 questions — plus three spoken answers that build the voice; it never asks which type of agent they attract (derived: "your skills attract any agent; these are the agents who'll relate most"), where they can attract, their CRM, booking link, compliance, scheduled tasks, operations or brand. The brand is a Week 3 chat ("my attraction brand direction"), alongside Claude Design ("my attraction brand direction"); compliance is on demand ("paste my compliance link" reads their brokerage's page); the tools conversation is Week 2. The Brain Book is nine short sections, at most fifteen pages. "It didn't ask about my brand / CRM / compliance" in Week 1 = working as designed.

### Plugin 2 — MAA Claude Support — BUILT (this plugin)
- Needs nothing to help. Needs a Brain to log and to track weeks (`maa-support-setup`).
- Its only writes: `memory/support-log.md`, `memory/claude-updates.md`, the config block.

### Design Studio — Claude Design skill set (W3 · W6) — BUILT
- NOT a plugin. 10 `aa-…-design` zips uploaded at claude.ai/customize/skills + the Agent Attraction
  Design System set up inside Claude Design: Week 3 `aa-logo-design` · `aa-style-sheet-design` · `aa-brand-kit-design`;
  Week 3 (with the Design Package) `aa-offer-kit-design` (the product mockup, the offer stack, the one-pager, the deck, the welcome pack, the
  comparison sheet) · `aa-lead-magnet-design` · `aa-funnel-design` · `aa-content-design` (carousels + recognition);
  Week 3 `aa-video-kit-design` (the Riverside editor's overlays — upload with the Riverside plugin; "register my video
  brand kit" in Cowork afterwards); Week 6 `aa-event-design` · `aa-value-vault-design` (playbook · course · ebook · the
  partner onboarding roadmap). Each kit skill runs one piece by its phrase, or the whole kit with one checkpoint. Reads the uploaded Brain Book, never `~/attraction-brain/`.
- Known modes: a zip rejected = description over 1024 chars or a nested zip (tree #11); "the skill
  isn't in Design's list" = wrong account/workspace (FAQ Q38); "it doesn't look like my brand" =
  the design system was never set up in Design (the root fix).

### Plugin 3 — Lead Magnet (W2, after the Partner Offer session) — BUILT
- Depends on: Brain (`offer` — the Partner Offer, a program definition since Brain 0.3.0: the magnet is cut from ONE
  framework step and the funnel presents the program by name, type and cadence — `avatars`, `compliance`,
  `brand-visual`, `voice`).
  **Offer-first, one sitting (v0.2.0, 2026-10-10):** "launch my lead magnet plugin" builds the offer first if
  it is still at seeds (the navigator runs the Brain's `attraction-offer` inside the session — the member never
  comes back later — one offer card, shown not asked), then recommends ONE lead magnet built from that
  offer and Mike's lessons (`lm-magnet-ideas` — the three kinds weighed silently: a tool, a plan, a decision or
  proof piece; one download-ready card under 120 words, no lesson codes in chat; "another idea" shows the next
  best, one at a time — never three at once, Mike's ruling of 2026-11-02), the member says yes, and the magnet
  document and the sales funnel outline follow. No
  default magnet; no two members' magnets alike (non-disparagement rules apply — cardinal rule #1; a
  comparison-shaped guide only when it fits the offer). Writes `identity/profiles.md` FIRST (the bios;
  Short-Form confirms and refreshes its five sections in Week 4); `memory/magnets.md → ## Current magnet` (mirrored as the
  `Live magnet:` line in `brain.md`) is what every Week 3–6 CTA reads.
  **The Week 2 outcome, Mike's words (the plugin's opening message states it; Support repeats it verbatim):**
  "By the end of this week you have ONE lead magnet, written and designed, with its funnel outline (tangible)
  — and your unique value proposition broken down: your offer explained in detail and how to create it, its
  name, the marketing language to use, and where to host it (intangible)."
- Known modes: "it's asking me to build my offer" = the session order working (the offer gets built right
  there, then the magnet — nothing to finish first); "it only gave me one option" = by design — say yes, or
  "another idea" for the next best, one at a time (never three); "it asked me about my brokerage's rules" =
  the one question Week 2 asks when the Brain can't answer it — whether a package may be offered as a reason
  to join; "I don't know" is a fine answer (the offer is still written as a join package, Mike's model, with one check open for
  the compliance desk; only "not allowed" moves the public lines to what the member teaches); "it renamed my program" = the naming rule — the
  name is outcome-based, the member can pick an alternate or keep their own; "it skipped the compliance step"
  = it folds compliance in right before the public document, never earlier; the funnel link reads "not live
  yet" until the member's design step deploys the page; the traffic engines (Short-Form W3, YouTube W4) plug
  in later — never "missing".

### Plugin 4 — Short-Form (W4) — LIVE 0.7.3 (Week 4 · the sitting is an interview and waits after every step · two keywords · the kit first · nine workflows, four on with the Yes on the card · three Reels a week to start · Graphics · Reels · Calendar tabs · the Brain Board on every push)
- Depends on: Brain (avatars, positioning, story-bank, proof, compliance; the Week 2 offer's keyword, its framework and its "teach first" line; the live lead magnet). **The posting tool is part of the program** — Metricool or GoHighLevel, connected inside the sitting; copy-paste is only what a member does until it is connected. ManyChat is required and set up by the member in their own account from the build sheet — never connected to Claude. Notion holds the board — without it the calendar lives in the Game Plan and the Brain, nothing is lost, and the Connect button appears in the chat.
- **The one phrase is the whole sitting, about 35 minutes, in this order:** the welcome plays the member back from their Brain → profiles and the two keywords confirmed (the bios were written in Week 2; GUIDE opens the guide, the offer's own word is the invitation) → **the interview: four questions, one per reply** (the first thing agents ask them on the phone · how they would explain the first step of their method · what they do off the clock · the day and place they can film) → the five pillars and the week shown with the member's own words inside them ("Does that sound like you?") → the Short-Form Game Plan (thirty hooks, the next 30 days dated, opening with the six posts designed in Week 3; the first three Reels are the member's three answers, marked "your words") → the Notion content board with those 30 days mapped → the scheduled workflows on ONE consent card and its Yes (switched on: Monday Week Plan · Batch Prep · Wednesday Brokerage News Watch · Monthly Calendar Refill; by phrase: keyword follow-up queue, mid-week nudge, monthly deep dive, daily stories, quarterly profile audit — all draft-only; a short email to the member's own address when something is ready) → the posting tool → the first Reel, its opening chosen by the member → the close: "what you did today" and the first win of the week.
- **How every reply is built (since 0.6.0 and 0.7.0):** it opens with a win line ("✓ …" — what the member just said or did), shows what was built, hands the member ONE thing that is theirs (a question about them, a choice about their content, or two minutes in their own account) and stops on "Your turn." Nothing more is built until they answer. A second call resumes exactly where it stopped — inside the interview, at the next unanswered question (the `Short-form setup:` line in `publishing.md`; the answers under `content-pillars.md → ## In your words`).
- **What it asks and what it never asks:** it asks about the member (never anything from Week 1's 26 questions — what the Brain holds is played back first) and one fact, Metricool or GoHighLevel. It never asks about email, platforms, which workflows, or ManyChat.
- Known modes: **"it's asking me questions"** = by design (FAQ Q71) · **"it stopped — is it stuck?"** = it is waiting; the last line says "Your turn" (tree #13) · **"it built everything while I was away"** = an older version (before 0.6.0): update the plugin · **"I skipped a question"** = "update my pillars" asks it again · **"I don't want the questions"** = "do it all" builds from the Brain · **"it asked me something I already told it in Week 1"** = it should not — log it · nothing auto-posts — approval is the last gate; "it didn't post" is usually an unapproved queue ·
  "it skipped the board" = Notion not connected (it says how, never blocks; "map my next 30 days" once connected) ·
  "my Monday plan never ran" = the card never got its Yes, or the task was never created (tree #10) · "where
  is my calendar" = section 6 of the Game Plan in Content → Short-Form, and on the board if they have one · "where are my answers" = on the Brain Board with the pillars ("In your words"), in the plan beside each Reel ("your words"), and at the top of that Reel's card.

### Plugin 5 — AI Editor, Riverside (W4, installed with Short-Form) — vendored (the same plugin as the realtor marketplace)
- Depends on: Brain (`brand-visual`, `voice`, `compliance`) + the **Riverside connector on the
  member's own account**. No Descript, ever.
- Known modes: connector connected but reads fail → tree #12; edits persist in Riverside, state in
  the Brain's `editor/` allowlist.

### Plugin 6 — YouTube (W5, date to be confirmed) — LIVE 0.7.2 (rewired 2026-11-14: Week 5, the two CTAs in Mike's shape, one video a week to start, the YouTube tab, two workflows + the email note, the Brain Board on every push)
- Depends on: Brain + the Week 2 files (the offer's content branches, the guide, the Week 3 Kit's calls-to-action table, the YouTube bio from the kit) + the Short-Form setup from Week 4 (`content-pillars`, the Notion board — "YouTube wants my pillars" means run the short-form setup first). House rhythm: one chat = one video. Cadence: one video a week for the first month, two the step-up the monthly review proposes.
- **The sitting, about 40 minutes, in this order:** the welcome and the one fact question (the channel link, or "starting fresh") → the Channel Page (three pieces to paste into YouTube Studio) → **the interview: four questions, one per reply** (which of their three topics they could talk about for twenty minutes · who they would sit down with on camera first · which of their stories to tell at full length · the day they can film a full video — each asks one thing) → the first three videos shown, built on those answers ("Does that sound like you?") → the Game Plan → the YouTube tab on the board (30 days — four or five videos at one a week) → the two workflows + the email note on one card and its Yes → the close: the first video by title, "what you did today", the first win of the week. It resumes from `channel.md`'s `Setup:` stamp — inside the interview, at the next unanswered question (the answers under `channel.md → ## In your words`); the Kickoff drafts the week's video every Monday.
- **Same shape as short-form:** every reply opens with a win line, hands the member one thing that is theirs and stops on "Your turn." It never repeats Week 1 or Week 4 — when the short-form answers are on file it plays one back ("last week you told me agents ask you…") instead of asking. A guest the member names is a first name and a candidate only: nothing is published and nobody is contacted in the sitting.
- Known modes: **"it's asking me questions"** = by design (FAQ Q71) · **"it stopped — is it stuck?"** = it is waiting; the last line says "Your turn" (tree #13) · **"I skipped a question"** = "refresh my attraction game plan" asks it again · **"'script my first three videos' only wrote one"** = by design since 0.7.0: one script a reply, each from the member's own words; "write all three" does the rest at once · "it skipped the board" =
  Notion not connected (it says how, never blocks) · "my Monday kickoff never ran" = the card never got its Yes, or the task was never created (tree #10).
- Thumbnails are made by the member in Higgsfield, from the sheet `yt-thumbnail` writes (three directions: the prompt to paste, which of their own photos to upload, the three to five words) — never a Claude Design job (the owner, 2026-11-14). The channel banner is the brand kit's, from Week 3.
- **On every video card** (0.4.0): one real reference video to watch first (found on YouTube and checked before it is written; the last column of the YouTube tab; "it gave me no reference" = nothing close was found, the card carries YouTube's own search and the next Kickoff looks again) · a six-step publish checklist for YouTube Studio ("my video is published" moves the card). **Live numbers** are a separate two-minute step by phrase ("connect my YouTube numbers") — never part of setup, never used by a scheduled run. **Clips:** "repurpose my attraction video" queues three clip scripts; the Monday Week Plan turns up to two into that week's Reels. The edit is the Riverside editor when installed ("edit my YouTube video").

### Plugin 7 — Conversion & Sales (W6 — date to be confirmed) — BUILT, not in the marketplace yet
- Depends on: Brain (`top-50`, `avatars`, `offer`, `positioning`, `brokerage-model`, `objections`,
  `compliance`). Objection role-play runs in Claude Voice — the member talks, Claude plays the agent.
- Known modes: "it won't give me an income number on the call script" = compliance gate (no
  earnings claims) working as designed.

### Plugin 8 — AI Admin (W6 — date to be confirmed) — BUILT, not in the marketplace yet
- Depends on: Brain (`operations`) + Gmail + Google Calendar (or Microsoft 365). Never auto-sends.
  Owns pipeline stage moves; "the stages look different in two places" = log it.
- Setup is value-first (2026-10-18): "set up my attraction admin" shows the member's first Morning Brief and
  pipeline at a glance before asking anything, then ONE consent card (Morning Brief + Daily Follow-Up Queue, plus
  the Daily Debrief if it isn't on). It never asks a name, a VA, or a CRM question ("call my admin [name]", "set up
  my VA packs", "mirror my CRM" on demand). "It asked me nothing" is by design; "it didn't show my calendar" = that
  connector isn't connected — the brief names it once at the end; connect it and say "my morning brief".

### Plugin 9 — Events & Workshops (W7, bonus — date to be confirmed) — BUILT, not in the marketplace yet

*Team & Retention was removed from the OS on 2026-10-08 (not built). `memory/organization.md` stays in the Brain; capture and the AI Admin write joins to it. The Lead Magnet moved to Week 2 (Plugin 3, above) on 2026-10-10.*
- Reads the Brain's `offer`/`avatars`/`compliance`; Events writes the promo content, event tooling (Zoom,
  registration page) is the member's own.

## What changed lately — and what a member will notice (read this before answering "why is it different now?")
A member who updates a plugin mid-cohort meets a sitting that behaves differently from the one a friend described.
These are the changes they can feel, newest first. Answer in their words, never in version numbers unless they ask.
| Since | What changed | What the member notices | Where to send them |
|---|---|---|---|
| 0.32.x (Short-Form 0.7.x · YouTube 0.7.x) | Both content sittings run as an interview | "It asked me four questions" · "it quoted me back" · "my first three Reels / videos are things I said" · "it says ✓ and tells me what I did" | FAQ Q71 · Q72 · Q73–Q78 |
| 0.30.0 (Short-Form 0.6.0 · YouTube 0.6.0) | One step a reply, then it waits | "It stopped and said 'Your turn'" · "it didn't build anything while I was away" | FAQ Q70 · tree #13 |
| 0.29.0 (YouTube 0.5.0) | "Script my first three videos" | Three videos for one filming day, with a film-day sheet | FAQ Q69 |
| 0.28.0 (YouTube 0.4.0 · Short-Form 0.5.0) | A real reference video and a six-step publish checklist on every video card · "connect my YouTube numbers" as its own step · thumbnails made in Higgsfield · clips from a video feed that week's Reels | "There's a video to watch on my card" · "it told me to make my thumbnail in Higgsfield" | FAQ Q64 · Q66 · Q67 · Q68 |
| 0.27.x (Short-Form 0.4.x) | The posting tool is part of the program · four workflows on one card · no engagement list, no Friday note | "It asked Metricool or GoHighLevel" | FAQ Q53 · Q56 · Q62 |
**The one-line answer to "why is my setup asking me things now?":** it used to build from your Brain and ask you to
approve; now it asks you for the few things only you can say — and builds on your own words.
**"My friend's didn't do this"** → they are on an older version: update the plugin (Customize → Plugins), then say
the setup phrase again; a finished setup is never re-run unless they say "redo my short-form setup" / "redo my
YouTube setup".

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
| My debrief / scheduled agent never ran | Consent never given, or the Cowork task was never created (the news scan and the CEO review are on demand, never scheduled) | Diagnostics tree #10 |
| A Claude Design zip won't upload | Description > 1024 chars or a nested zip | Diagnostics tree #11 |
| Docs come out unstyled/ugly | Deliverables render via the shared styled-doc pipeline | Log as bug via `maa-support-escalate` |
| A skill wants a tool the member has not set up (ManyChat, Metricool or GoHighLevel, Notion) | All three are part of the program since 2026-11-14, none blocks a sitting: ManyChat is set up in the member's own account from the build sheet and is never connected to Claude; the posting tool gets its Connect button in the chat (copy-paste only until it is connected); Notion gets its Connect button in the chat and the calendar is safe in the Game Plan meanwhile | Give the one phrase: "my ManyChat build sheet" · "connect my posting tool" · "map my next 30 days" |
| "It says it sent/saved/booked it — I can't find it" | Claimed-done ≠ done: verify with one cheap read | Diagnostics tree #9 |
| "Do I need Higgsfield / the AI clone / the Thumbnail Employee?" | Higgsfield: yes, for YouTube thumbnails from Week 5 — the member's own account, `yt-thumbnail` writes the sheet. The AI clone and the "employees": not in this OS | FAQ Q48 · Q64; log the ask for the clone |
| "Where's the listing / market update skill?" | Not part of agent attraction; those are realtor-cohort plugins | Honest answer; if they're in both cohorts, that's the realtor stack |


## Two support desks (dual-cohort members)

If the realtor marketplace is also installed, two help desks exist. This desk answers anything about agents, attraction, recruiting, the organization, partner calls, or an MAA week; the Social Agent OS desk answers buyers, sellers, listings, market updates, and SAO weeks. Explicit phrases: *MAA help* / *attraction help* → this desk; *SAO help* → the other. When the words don't decide, the navigator asks once and remembers (`config.md → Support desk`).
