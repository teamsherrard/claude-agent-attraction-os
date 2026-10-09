# Changelog

All notable changes to the Agent Attraction OS marketplace. Versions are per plugin; the repo `VERSION` is the marketplace release.

## [0.3.1] — 2026-10-09

### Cowork sync warnings cleared (this marketplace only; the realtor repo is untouched)
- attraction-ai-brain 0.2.1: `hooks.json` carries only the `hooks` key; the explanatory note that used to sit in a `$comment` field lives in `hooks/README.md`. claude.ai's hook schema dropped the unknown field with a warning on every sync; the SessionStart hook itself was always stored and is unchanged.
- realtor-riverside-editor 0.4.3 (the vendored realtor 0.4.2 plus two trims): the `studio-navigator` and `studio-publish` descriptions were 1455 and 1312 characters. claude.ai stores a description cut at 1024, which in Cowork silently dropped the navigator's resume triggers ("finish my video", "pick up where we left off", "continue my edit"). Both rewritten under 1024 characters as folded block scalars with the resume triggers kept; everything else in the plugin is byte-identical to the realtor source apart from the Brain-home rule.
- Gate: check 8 now fails on any description over 1024 (the vendored exemption is gone); new check 15 fails a `hooks.json` with any top-level key other than `hooks`. `vendor-riverside.sh` lists over-limit descriptions after a re-vendor so the trims get re-applied.

## [0.3.0] — 2026-10-09

### Shared document renderer v2 (Brain, Admin, Conversion, Events, Lead Magnet, Short-Form, YouTube)
- `render_doc.py` (byte-identical in all seven plugins; Riverside untouched): real Word styles in the house look (`Title`, `Heading 1`, `Heading 2` — the Word navigation pane and the Google Docs outline now work), a larger type scale (body 11pt at 1.2 line spacing, chapter titles 20pt, part titles 24pt, sub-bands 12.5pt, tables 10pt, cover 30pt), a running header + `Page X of Y` footer from page 2 (cover / title page carries neither), an "In this part" linked chapter list on every part opener, tables with a tinted bold header row that repeats across pages + alternating rows + horizontal hairlines only, callouts as indented accent-bar blocks, keep-with-next on headings / kickers / a label directly above a table and widow control on body text, one optional accent colour (default near-black) used only for the title rule, part kickers, callout bar and table-header tint, and a sub-band cap of 80 characters that warns instead of silently rendering dashes. The structured-text grammar is unchanged — every existing input re-renders without edits.
- `brain-book-spec.md` step 6 passes the member's primary brand colour from `brand-visual.md` as the accent (omitted when none is recorded); the zero-warning rule now includes the sub-band warning. `doc-formatting.md` (Brain, Admin, Conversion, Events) and the YouTube `doc-format.md` describe the v2 look.
- `docs/demo/`: the three demo documents re-rendered as v2 files; `measure_book.py` counts paragraph callouts and estimates pages on the v2 type scale; `BOOK-RENDER-TEST.md` §8 records the before/after.
- Versions: attraction-ai-brain 0.2.0, attraction-ai-admin 0.2.0, maa-claude-support 0.1.1, attraction-conversion-sales 0.1.1, attraction-events-workshops 0.1.1, attraction-lead-magnet 0.1.1, attraction-shortform-system 0.1.1, attraction-youtube-system 0.1.1.

### Book spec + calculator (2026-10-09)
- `brain-book-spec.md`: the per-chapter minimums bind in demo mode exactly as in a real build, no bracket placeholders in a demo, the money chapter always carries the three scenarios. `attraction-rev-share-calculator`: when the member defers ("explain mine to me") it runs the three scenarios on the strictest generic default mechanics instead of stopping — the gap that left the demo Book's Chapter 11 thin.

### Knowledge base moved to a private repo (2026-10-09)
- The 103 lesson transcripts now live in teamsherrard/claude-agent-attraction-knowledge (private) and this repo is public so Cowork can add it as a marketplace without a GitHub connection; `README.md`, the master game plan, the build brief and the Support `source-map.md` point there.


### Scheduled agents: eleven → nine (user decision, 2026-10-08)
- The Agent Movement Watcher is removed as a scheduled agent. Its research-only run is now the Prospect Radar's on-demand news scan (`attraction-prospect-radar` Job 3: "scan agent movement", "what's moving in my market", "refresh my prospect intel"), writing the same seven-column rows to `memory/intel.md` with a `News scan:` run line. No task, no consent card, no `Agent Movement Watcher task` key; the watcher task-prompt reference file is deleted.
- The Weekly Recruiting CEO Review is removed as a scheduled agent. It stays as `admin-recruiting-scorecard`'s CEO mode, run on demand ("run my CEO review", "what happened in recruiting this week"); `admin-attraction-setup` no longer offers it. No task, no `Weekly CEO Review task` / `CEO Review slot` keys; the CEO-review task-prompt reference file is deleted. The Admin owns four scheduled agents.
- Every contract, template, plan, Support, Short-Form, YouTube, Conversion, and demo-brain mention updated; the intel ledger's source is now "the Prospect Radar's news scan (on demand)".

## [0.2.0] — 2026-10-09

### attraction-events-workshops 0.1.0 — first build (new)
- Plugin 9: `ev-navigator`, `ev-strategy`, `ev-live`, `ev-virtual`, `ev-evergreen`, `ev-promo`, `ev-registration`, `ev-runofshow`, `ev-followup`, `ev-analytics`; the events doctrine from lessons 73–77 and Mike's workshop-ops lifecycle; `ghl-workflow-table.md` (Trigger → Action → Outcome); the Post-Event Follow-Up scheduled agent, consent-armed per event.

### Design Studio — all 14 Claude Design skills (`aa-…-design`)
- Week 2: `aa-offer-stack-design`, `aa-offer-assets-design`, `aa-product-mockup-design`, `aa-carousel-design`, `aa-funnel-design`, `aa-lead-magnet-design`. Week 4: no design skill — a thumbnail is a `yt-thumbnail` brief pasted into the member's Brand HQ project. Week 6: `aa-recognition-design`, `aa-event-design`, `aa-playbook-design`, `aa-course-design`, `aa-ebook-design`. Upload files in `design-studio/_dist/` (regenerated by the build; not tracked).

### Docs
- `docs/setup-guide.md` (the Week 1 Setup Guide copy), `docs/playbooks/playbook-1-agent-attraction-brain.md` (Playbook 1 copy), `docs/plans/BOOK-RENDER-TEST.md` + `docs/demo/` (the Brain Book render test and demo brain).

### Brain, Admin, Conversion seams
- Events rows in the OS contract; `admin-pipeline` scans event blocks for request lines; Conversion reads the next event from `memory/events.md`; the Brain template gains the events block, the Events content-log convention, and `03 · Content/Events/` in the drive map.

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
- Week 1 Design Package: `aa-logo-design`, `aa-style-sheet-design`, `aa-brand-kit-design`, the Agent Attraction Design System, START-HERE, and the build in `design-studio/_dist/`.

### Repo
- `docs/BRAIN-CONTRACT.md` (OS-wide ownership, locked vocabularies, request shapes, config registry, 11 scheduled agents), `docs/plans/` (the two game plans, the build brief, the seam log, the status report), `knowledge/transcripts/` (103 lessons + manifest, private), `scripts/check-release.sh` with checks 8–13.

