# Agent Attraction OS — Overnight Build Report and Strategic Game Plan

*Written for Riya and Mike · 2026-10-09 · repo `claude-agent-attraction-os` · status at the end of the overnight run, updated after the "keep working" session (v0.2.0)*

> Sections 1–3 are the status (what is built, verified, and left). Sections 4–8 are the strategic advice you asked for:
> what to add, remove, optimize, fix, and what nobody is thinking about yet.


## 1. What is built

Repo `claude-agent-attraction-os`, tag `v0.2.0`, release gate green, upload zips in `dist/` and `design-studio/_dist/`. The realtor repo was read only; nothing in it changed.

| # | Plugin | Skills | Shared files | Built from | State |
|---|---|---|---|---|---|
| 1 | `attraction-ai-brain` | 26 | 16 (doctrine ×4 from the transcripts, Book spec, drive map, contract, renderer) + a 49-file Brain template | realtor Brain, rebuilt interview | built · reviewed · fixed |
| 2 | `maa-claude-support` | 9 | 15 + the 103-card lesson knowledge base | cohort support fork | built · reviewed · fixed |
| 3 | `attraction-shortform-system` | 13 | 11 (attraction doctrine, Composio engine, board spec) | realtor short-form fork | built · reviewed · fixed |
| 4 | `realtor-riverside-editor` | 28 | 36 | vendored as-is + the Brain-home rule | vendored |
| 5 | `attraction-youtube-system` | 19 | 12 (attraction YouTube doctrine, SEO KB, Composio engine, board spec) | realtor YouTube fork | built · reviewed · fixed |
| 6 | `attraction-conversion-sales` | 19 | 8 (conversion doctrine, contract, house rules) | new, from the Week 5 lessons | built · reviewed · fixed |
| 7 | `attraction-ai-admin` | 8 | 8 | realtor Admin, cut to the organization side | built · reviewed · fixed |
| 8 | `attraction-lead-magnet` | 11 | 7 (copywriting KB for an agent audience) | realtor lead capture fork | built · reviewed · fixed |
| 9 | `attraction-events-workshops` | 10 | 9 (events doctrine from lessons 73–77, the GHL workflow table) | new, from Mike's workshop-ops system | built · reviewed · fixed |
| – | Design Studio (Claude Design skill set) | all 15 + the design system | realtor design suite v2 | built · reviewed · build green |

Totals: 143 Cowork skills across 9 plugins (115 new or rewritten, 28 vendored) plus 15 Claude Design skills, 103 lesson transcripts split into 16 modules and cited by `module/lesson` in every doctrine file, 103 knowledge-base cards, 11 scheduled agents with named owners, one OS-wide contract (`docs/BRAIN-CONTRACT.md`), the Setup Guide copy and Playbook 1 copy in `docs/`, about 90 commits.

**Not built, by decision:** Team & Retention (removed), Creative Studio / Higgsfield (parked). **Written as copy, not yet designed:** the Setup Guide (`docs/setup-guide.md`) and Playbook 1 (`docs/playbooks/playbook-1-agent-attraction-brain.md`); Playbooks 2–6 are not written.

## 2. What was verified, and how

- **Per-plugin seam reviews** (seven reviewers, one per plugin): setup-to-phase-skill parity, file ownership against the contract, template headings against the locked shapes, every doctrine citation resolved against the transcript files (Brain + Support 692, Conversion 157, YouTube 203, Short-Form 175, Lead Magnet 57, Admin 21), every "Say it like Mike" quote verified verbatim (298), hand-offs by name (0 dangling), trigger collisions against the 154 realtor skills (0 outside the Support desk, which shares generic help phrases by design and routes with a two-desks rule), plain-language scans, usage discipline (every skill now opens at most four Brain files up front).
- **Release gate** (`scripts/check-release.sh`, 13 checks): versions match the registry, everything committed, hand-offs exist, plugin-root references resolve, six shared files byte-identical across plugins, descriptions ≤1024 and folded, no realtor paths or retired engines leak, no trigger collisions, every plugin carries a Brain contract and consent-gates its scheduled tasks, Composio kept in both content engines, no routes to removed systems, the Design Studio builds. Green at `v0.1.0`.
- **The Brain Book render test** (`docs/plans/BOOK-RENDER-TEST.md`, renders in `docs/demo/`): a complete demo Brain (Taylor Brooks) rendered through the real renderer. Full Book ≈43–57 pages (16,005 words, 18 chapters, 26 tables); the Week 1 first-run state ≈34–38 pages (9,383 words); the 90-Day Scorecard 2–3 pages. The 2–3-page failure of the last cohort is not the renderer. The test found three spec gaps (a truncated single-block emission renders silently as a short Book; gate check 7 failed on the goals rev-share rows; three Week 1 chapters thin) and they are applied in the spec and setup.
- **Not verified, said plainly:** no live Cowork run on a real member yet; page counts are estimates (no LibreOffice on this Mac); whether Claude Design consumes the uploaded design-system file directly; the Riverside vendored copy against a member who has only the attraction Brain (the rule is written, not exercised).

## 3. What is left

1. **Cold test** the Week 1 setup on a real member (Opus, medium effort, one sitting) and the Design Package in Claude Design. Nothing replaces this.
2. **Mike's decisions** (section 4 below).
3. **Playbooks 2–6** (copy, then design), and the Claude Design layout of the Setup Guide and Playbook 1.
4. **Riverside back-port** of the Brain-home rule into the realtor repo so the two copies are byte-identical; the vendored copy also carries two over-long descriptions that belong to the realtor repo to fix.
5. **Support plugin placeholders** before Nov 3: portal URL, Circle link, call times, refund policy, video links.
6. **Mike's thumbnail swipe file** and **his keyword sheet** (the ManyChat variants ship as defaults until then).

---

## 4. Decisions only you or Mike can make (blocking or near-blocking)

1. **Riverside back-port.** The Studio is one plugin on two marketplaces. The vendored copy here carries one added rule (use the attraction Brain when it exists). I did not edit the realtor repo, because your "never touch the old plugins" rule outranks convenience. Until the same rule is added there, the two copies differ by that one section, and a member who installed the Studio from the realtor marketplace will not get the rule. Smallest safe move: a single commit in the realtor repo adding the Brain-home section to `house-rules.md` and `<Brain home>` in paths, released as a patch version, then re-vendor here with `scripts/vendor-riverside.sh`.
2. **Partner-call framework labels** (Conversion doctrine §3): step-five label, default call length (60 until mastered, then 30 vs the workshop's "30-minute Partner Call" promise), and the objection framework label. The plugin ships with defaults and says so.
3. **The "5-Point Framework"** is named in the course docs and defined nowhere. The follow-up skill is built on lesson 85's five principles. Mike should confirm or supply his five.
4. **Support plugin placeholders**: support portal URL (the Freshdesk account was suspended on 2026-09-25; nothing here points at it), Circle link, call times, refund policy, the Circle video links. All marked `[NOT SET]` and the setup skill asks for them.
5. **Two curriculum facts changed in the build and the course docs should follow:** the Brain intake is seven conversations and about 64 questions in roughly 50 minutes (the cohort doc still says "about 25 questions, 15 min"), and the Design Package is Week 1 homework (the Week 2 breakdown still lists it under Week 2).
6. **Mike's thumbnail swipe file** with pattern notes: the thumbnail skill scores against lesson 97 only until it arrives.
7. **Inducement rules review** before the Switching Transition Plan ships (it is built but gated behind a config flag).

## 5. What is missing from the plan (add these)

- **A one-command "install my OS" path.** Nine plugins installed one at a time is nine support tickets per member. The marketplace lists them in order, but a single Setup Guide page with the exact click path and a "what week am I in, what do I install" line in Support is the minimum. Longer term: the cohort doc's one-click install idea.
- **A cold-test script for the Week 1 setup on a real member before Nov 3.** Every past cohort's worst bugs were found live. The demo brain is rendered; a real human run on Opus with the usage diet on is still the only proof the 50-minute interview fits one session.
- **"Which Brain?" guard in every member-facing door.** Insiders who own both marketplaces will hit it first. The hook, Support's diagnose tree, and the trigger phrases handle it; the Setup Guide must say it in one sentence: "Say *set up my attraction brain*, not *set up my brain*."
- **The Playbooks and the Setup Guide are not software and are not built.** Six designed playbooks plus the Setup Guide are Claude Design deliverables on the Oct 30 and weekly ship dates. They need an owner now.
- **Mike's own proof assets inside the skills.** The transcripts carry Mike's numbers (600+ calls a year, 98%, 157 frontline agents). They appear as "Mike says" in the knowledge base, which is correct, but no skill uses them as teaching examples with his permission flagged. Decide whether the skills may quote Mike's numbers to members as his, and where.
- **Email delivery for the scheduled agents.** Every scheduled agent is draft-only by policy, which is right for anything that reaches a prospect. The Daily Debrief and the CEO Review are for the member only; consider letting those two email the member their own brief (Gmail cannot send; Outlook can). Today they write to the Brain and the member opens Cowork.
- **A member-facing "what my OS does" dashboard.** The cohort doc's Attraction OS dashboard artifact (pipeline, KPIs, projection, content calendar) is the single most visible proof of "software, not a course." It is one artifact fed by files the plugins already write. Cheap, high-perceived-value, not built.

## 6. What to remove or simplify

- **Nineteen Conversion skills is a lot of doors.** The navigator hides them, but the Setup Guide should teach five phrases, not nineteen skills: "intel on Sarah", "what do I say to Sarah", "prep my call", "here's the transcript", "she went quiet". Everything else is reached from those.
- **Three scheduled agents in Week 5 plus two in Week 6 is more automation than a new member will tolerate in a week.** Ship Call Block Prep and the Daily Follow-Up Queue in Week 5; move Cold-Lead Reactivation, the CEO Review, and the Monthly Review to a "turn on when you have 20 prospects" prompt. The skills already provision only with a yes, so this is a curriculum choice, not a code change.
- **The Weekly Content Performance task is owned by Short-Form and extended by YouTube.** Correct, but two plugins editing one scheduled task is a seam. If it misbehaves live, give each plugin its own Friday task and let the Debrief read both.
- **Drop the "Studio pack" manual-numbers path from the sales pitch.** Keep it in the skills (it is the fallback when Composio is not connected) but sell the connected path; the manual path reads as a downgrade.

## 7. What to optimize or tweak before Nov 3

- **Usage cost of Week 1.** Setup is ~64 questions in 16 stops plus the Book build with research. The usage diet is in, but the Book's research pass runs the Prospect Radar's landscape research, which is the most search-heavy step in the OS. For the first cohort, run the Book's research chapter in "light" mode (cite the member's own answers, defer the researched landscape to the Week 2 Prospect Radar run) unless the member asks. One line in the spec.
- **The 20-second rule for every scheduled-task consent prompt.** Each agent asks for its own yes at setup. Five asks across the cohort is fine; two asks in the same session is not. Setup asks once for the Debrief; everything else asks when its week arrives.
- **Plain-language audit of the Setup Guide against the skills' actual phrases.** The skills were written to a trigger list; the Guide must use the same words or members will say the wrong thing.
- **Riverside's compliance read.** The Studio reads `identity/compliance.md` by the realtor field names. The attraction compliance file has more fields (earnings, non-disparagement, AI-likeness). The Studio's gate still passes or fails on the disclaimer and license fields, which exist in both. Fine for now; a future Studio release should read the attraction fields too.

## 8. What nobody is thinking about yet

- **Two cohorts, one member, one Google Drive.** The workspaces are separate and the markers are different, so sync is safe. The Notion content board is shared by design (one board per member). A member in both cohorts will see realtor and attraction content on one board; the status vocabulary is the same, the pillar vocabulary is not. Decide whether the board gets a "Cohort" column or two boards.
- **Compliance is per state and per brokerage, and the OS defaults to the strictest rule.** That protects you, and it also means a REAL or LPT member with a looser rev-share marketing policy gets a stricter default than their brokerage requires. The compliance skill lets them set their policy; the Setup Guide should tell them to.
- **Mike's voice in the skills vs the member's voice in outputs.** The support and coaching lines use Mike's framing; every member-facing output uses the member's voice-print. That boundary is written into every plugin. The risk is a coach line leaking into a reel script; the voice-proof skill is the catch, and it should be in the Week 3 and Week 4 routines by default.
- **The transcripts are the moat and they live in this repo.** Private repo, never zipped into a plugin, cards are derived. If the repo is ever made public or shared with a contractor, the `knowledge/` folder goes with it. Consider a separate private repo for `knowledge/` with a submodule or a copy step.
- **Retention after graduation.** Team & Retention is removed, which is the right call for a six-week build. The "join me and I give you this" promise (the Value Vault) still lands in Week 6 and depends on the Design Studio skills that are not built yet (aa-playbook-design, aa-course-design, aa-ebook-design, aa-product-mockup-design). That is the Week 6 critical path.
- **Insider members with both OS installed are your best testers and your most likely bug reporters.** Give three of them early access to the Week 1 build before Oct 30.
