# Changelog

All notable changes to the Agent Attraction OS marketplace. Versions are per plugin; the repo `VERSION` is the marketplace release.

## [0.1.0] — 2026-10-08

### attraction-ai-brain 0.1.0 — first build
- New marketplace teamsherrard-agent-attraction and Plugin 1, the Agent Attraction Brain (26 skills), built per `docs/plans/01-ai-brain-plugin-gameplan.md`.
- Mechanics forked once from the realtor Brain with new names: `attraction-brain-setup`, `attraction-brain-sync`, `attraction-brain-health`, `attraction-brain-migrate`, `attraction-import`, `attraction-capture`.
- Identity: `attraction-brand-persona`, `attraction-voice-print`, `attraction-voice-proof`, `attraction-story-bank`, `attraction-brand-direction`, `attraction-why-join-me`.
- Targeting and offer: `attraction-persona-map`, `attraction-prospect-radar`, `attraction-top-50`, `attraction-brokerage-model`, `attraction-model-positioning`, `attraction-offer`, `attraction-free-vs-paid`.
- Goals, ops, guardrails: `attraction-goals`, `attraction-execution-framework`, `attraction-rev-share-calculator`, `attraction-leadership-audit`, `attraction-operations`, `attraction-compliance`, `attraction-debrief`.
- Shared: `attraction-doctrine.md`, `persona-doctrine.md`, `brokerage-models.md`, `compliance-doctrine.md`, `brain-contract.md`, rewritten `drive-map.md`, `brain-book-spec.md`, `brain-doc.md`, `project-instructions.md`; `render_doc.py` and the connector layer carried 1:1.

### maa-claude-support 0.1.0 — first build
- Forked from the realtor cohort support plugin with every skill renamed `maa-support-*`; the MAA 6-week calendar, the Agent Attraction OS stack map, the two-desks rule for dual-cohort members, new diagnosis trees, the honest stack cost, an explicitly unset escalation door.
- The lesson knowledge base: 103 cards in `shared/kb/` (one file per vault module, verbatim quotes verified against the transcripts, the Loom link on every card) plus `kb-index.md`; "what did Mike say about…" answers from it and names the lesson to rewatch.

### attraction-shortform-system 0.1.0 — first build
- Forked from the realtor short-form system (`sf-*`): the five pillars Authority · Perspective · Story · Proof · Personality, value-first setup writing `content-pillars.md`, `publishing.md`, `profiles.md`; talking-head scripts with the 30-day calendar, carousels, green-screen, the daily story rotation (`sf-stories`), ideas and the 30-hook bank, the weekly routine, the comment-to-DM ladder with the ManyChat keyword (`sf-comment-to-dm`), optimizer, publish and batch publish through the member's own tool, analytics owning the Weekly Content Performance agent.
- Shared: the short-form attraction doctrine (`mike-frameworks.md`), the Composio data engine and the Notion board spec rewritten for agent attraction (byte-identical with the YouTube plugin).

### attraction-youtube-system 0.1.0 — first build
- Forked from the realtor YouTube system (`yt-*`): the attraction YouTube doctrine from the nine YouTube lessons, channel setup, the 3-lane game plan on the 8-video cycle, ideation, research, outliers, scripts in four formats, the agent interview strategy (`yt-interview`), model breakdowns with a hard data gate (`yt-model-breakdown`), thumbnail briefs for Claude Design (`yt-thumbnail`), SEO, make-video, repurpose with conversation starters, leads, analytics extending the Friday performance agent, coach, consistency, briefing (consent-first, draft-only), board, triggers. Writes content-log rows at script, publish, and repurpose.

### attraction-conversion-sales 0.1.0 — first build (new)
- Built from the Week 5 lessons: the conversion doctrine with the framework lock and the DECISION NEEDED blocks for Mike; `cv-navigator`, Agent Intel, Conversation Starter, DM flow, call prep (owns Call Block Prep), question funnel, enrollment script, presentation, 3-way calls, the Objection Handling Coach (15 objections, 5 modes), the Conversation Coach, follow-up, reactivation (owns Cold-Lead Reactivation), and the six Sales OPS skills.

### attraction-ai-admin 0.1.0 — first build
- Forked from the realtor AI Admin and cut to the organization side: `admin-attraction-setup`, `admin-daily` (the Morning Brief extending the Debrief), `admin-pipeline` (sole writer of stage moves), `admin-follow-up-queue`, `admin-recruiting-scorecard` (the Weekly Recruiting CEO Review), `admin-newsletter`, `admin-va-tasks`, `admin-monthly-review`.

### attraction-lead-magnet 0.1.0 — first build
- Forked from the realtor lead capture plugin for an agent audience (`lm-*`): the Honest Brokerage Comparison Guide locked as the first magnet, magnet ideas, design brief, funnel with the static-form rule, delivery, nurture, partnerships, GBP, profiles (Week 6 updater), analytics.

### realtor-riverside-editor 0.4.2 — vendored
- The same AI Editing Studio as the realtor marketplace, vendored by `scripts/vendor-riverside.sh`, with one added rule in `shared/house-rules.md`: the Studio uses `~/attraction-brain/` when it exists, else `~/realtor-brain/`, and calls that Brain's sync skill.

### Design Studio (Claude Design skill set, not a plugin)
- Week 1 Design Package: `ds-logo`, `ds-style-sheet`, `ds-brand`, the Agent Attraction Design System, START-HERE, and the build in `design-studio/_dist/`.

### Repo
- `docs/BRAIN-CONTRACT.md` (OS-wide ownership, locked vocabularies, request shapes, config registry, 11 scheduled agents), `docs/plans/` (the two game plans, the build brief, the seam log, the status report), `knowledge/transcripts/` (103 lessons + manifest, private), `scripts/check-release.sh` with checks 8–13.

