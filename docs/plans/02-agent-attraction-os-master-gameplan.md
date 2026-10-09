# Agent Attraction OS — Master Game Plan (the 10 other plugins + the Design Studio skill set)

*Master Agent Attraction (MAA) cohort · companion to `01-ai-brain-plugin-gameplan.md` · drafted 2026-10-08*
*Sources: the seven MAA documents (Week 1–6 breakdowns, "The Agent Attraction Cohort", "Launching & Scaling"), the realtor
marketplace at `teamsherrard/claude-agent-os` (read only), the Claude Design suite v2 on the Desktop, and the SAO AI Clone /
Thumbnail docs already in Downloads.*

> Same scope rule as Plugin 1: brand-new repo `claude-agent-attraction-os`, nothing in the realtor repo is edited or linked.
> Same inherited house rules (§11 of the Brain plan) and backend structure (§12) apply to every plugin below, unstated.

---

## 0. The OS at a glance (9 Cowork plugins + 1 Claude Design skill set · 9 scheduled agents)

**Count, stated once:** the cohort doc says "12 plugins." Nine are real Cowork marketplace plugins (Team & Retention was removed by the user on 2026-10-08). The Design Studio is NOT a plugin: Claude Design cannot run plugins, it only accepts uploaded skill files. It ships as 15 upload-ready Claude Design skills plus the Agent Attraction Design System, packaged like the realtor design suite v2. The Creative Studio (the two Higgsfield employees) is REMOVED from this build per the user (2026-10-08): it is not a plugin either, and it is parked for now. Sales copy can keep saying "12 systems"; the Setup Guide and Support stack map say "9 plugins + the Design Studio skills."

| # | Plugin (install week) | Prefix | Skills | Build type | Forks |
|---|---|---|---|---|---|
| 1 | AI Brain (W1) | `attraction-` | 26 | duplicate + rebuild interview | realtor-ai-brain · workshop aa-* skills |
| 2 | Support (W1) | `maa-support-` | 9 | **mechanical fork** + repoint | cohort-claude-support |
| – | **Design Studio (Claude Design SKILL SET, not a plugin)** (W1 Design Package: logo · style sheet · brand; W2 offer assets; W6 Value Vault) | `aa-…-design` | 14 | duplicate + 4 new · ALL 14 BUILT (the thumbnail skill was deleted; `yt-thumbnail` writes the brief) | Claude Design suite v2 (Desktop) |
| 3 | Short-Form (W3) | `sf-` | 13 | duplicate + fold + 2 new | realtor-shortform-system |
| 4 | AI Editor, Riverside (W3) | `studio-` | 28 | **vendored, same plugin** + the Brain-home rule | realtor-riverside-editor |
| 5 | YouTube (W4) | `yt-` | 19 | duplicate + fold + 3 new (`yt-thumbnail` is a Claude Design brief, no Higgsfield) | realtor-youtube-system |
| 6 | Conversion & Sales (W5) | `cv-` / `sales-` | 19 | **new build** on Mike's frameworks | workshop aa-zoom-call-prep (seed) |
| 7 | AI Admin (W5) | `admin-` | 8 | duplicate + re-stage (setup is its own skill) | realtor-ai-admin |
| 8 | Lead Magnet (W6) | `lm-` | 11 | duplicate + 6 new | realtor-lead-capture |
| 9 | Events & Workshops (W6) | `ev-` | 10 | new build from workshop-ops · BUILT v0.1.0 | anthropic-skills:workshop-ops |

**Not carried into this OS at all (user, 2026-10-08):** the Listing Launch plugin and the Market System plugin. Agent attraction has nothing to do with listings or market updates. They are not forked, not referenced by any MAA skill or stack map, and the realtor copies are untouched.

**Two corrections to the cohort doc's "ship as-is" rows.** The Riverside editor and the Support plugin cannot ship as-is: both
hard-code `~/realtor-brain/` paths, the realtor sync skill, realtor compliance, and (Support) the realtor plugin stack map. A member
who only has the Attraction Brain would get "no Brain found." Each needs a mechanical fork: copy, rename the plugin, re-point every
Brain path and skill reference, swap the stack map and calendar. No creative work, half a day each, but it is a build item.

---

## 1. The cross-plugin contract (define once, every plugin obeys)

**Numbering, one scheme everywhere (marketplace, README, Support stack map):** 1 Brain · 2 Support · 3 Short-Form · 4 Riverside · 5 YouTube · 6 Conversion & Sales · 7 AI Admin · 8 Lead Magnet · 9 Events; the Design Studio is unnumbered (a Claude Design skill set).

**Prefixes are the collision guard.** `yt-`, `sf-`, `lm-`, `cv-`, `sales-`, `aa-…-design`, `ev-`, `admin-`, `studio-`,
`maa-support-`, `attraction-` never overlap with the realtor plugins' `youtube-`, `shortform-`, `leadcapture-`, `realtor-`. Trigger
phrases are the second guard: every skill's trigger list is diffed against the realtor marketplace before release (new
`check-release.sh` check), and generic phrases ("set up my brain", "make a reel", "edit my video") are reserved for the realtor
side unless the member has only the attraction OS installed, in which case the Support plugin's stack map resolves them.

**Brain files each plugin reads and owns** (the §4 read contract from the Brain plan, completed for every plugin; `docs/BRAIN-CONTRACT.md` is the source of truth and carries the full detail — this table mirrors it):

| Plugin | Reads | Owns (writes) |
|---|---|---|
| Brain | everything | all `identity/` except `content-pillars · publishing · profiles · channel · sales-system`; `memory/top-50` (the mirror rule: once the Admin registers, Stage from `pipeline`, Last touch from `conversations`, Next move · Due from the Board; before that the touch cells are appended by capture + the Conversion logging skills); `scorecard` (Targets; daily rows by the Debrief; weekly rows by the check-in until `admin-recruiting-scorecard`); `debriefs`; `objections` (heard-rows); `ideas` (+ import's `## Past content (imported)`); `intel`; `capture-log`; `deadlines` (until Admin); interim rows in `conversations` and `organization` and interim stage moves in `pipeline` (via capture, until Conversion / AI Admin) |
| Support | `config`, `brain.md`, every plugin's `config` block, the Brain template | `memory/support-log`, `memory/claude-updates`, the `## MAA Support (Plugin 2)` block in `config.md` |
| Design Studio | the Brain Book (uploaded), `brand-visual`, `offer`, `positioning`, `avatars`, `proof` | nothing in the engine (assets go to `02 · Brand`, `05 · Offer`) |
| Short-Form | `profile · journey · strategy · avatars · positioning · operations · goals · offer · story-bank · proof · voice* · brand-visual · brokerage-model · compliance · content-log · objections · ideas · intel · top-50 · conversations (read-only) · magnets (## Current magnet) · content-performance` | `identity/content-pillars.md` (sf-setup; `sf-ideas` → Hooks bank), `identity/publishing.md` (sf-setup; designated lines by sf-publish · sf-board · sf-comment-to-dm), `identity/profiles.md` (sf-setup writes first; yt-setup fills `## YouTube`; lm-profiles updates), `memory/content-log` (SF rows), `memory/content-performance.md` (sf-analytics), the `## Short-Form (Week 3)` block; stamps story-bank Used-where, ideas `used`, the intel `Used?` column (sf-greenscreen); interim conversation rows via sf-comment-to-dm (through capture) |
| Riverside | `brand-visual · voice · profile · content-log · compliance` | `memory/content-log` (edit status), `editor/` state inside the sync allowlist; no `config.md` block |
| YouTube | same as Short-Form + `content-pillars · publishing (Content board: · Keyword:) · brokerage-model · prospect-intel · leadership · organization · pipeline · scorecard (read-only) · interview-pipeline` | `memory/content-log` (YT rows incl. yt-repurpose rows), `identity/channel.md` (yt-setup; yt-gameplan → `## Game Plan anchors`; yt-analytics → `Live data:` + dated `## Performance` blocks), `memory/interview-pipeline.md` (yt-interview), the `## YouTube (Week 4)` block, `profiles.md → ## YouTube`, `publishing.md → Content board:` (yt-board); stamps story-bank Used-where, ideas `used`, intel `Used?`; yt-repurpose appends conversation-starter rows to `ideas.md` while Conversion is absent |
| Conversion | `top-50 · avatars · offer · positioning · brokerage-model · objections · story-bank · proof · compliance · voice* · profile · journey · prospect-intel · operations · conversations · pipeline · debriefs · intel · intel-reports · organization · goals · scorecard (read-only) · brand-visual · sales-system · sales-funnel · magnets (## Current magnet)` | `memory/conversations` (its logging skills; `Stage after` = the stage request), `memory/pipeline` (direct until the Admin registers; `STAGE MOVE REQUESTED` / `NEXT MOVE REQUESTED` after), `memory/objections` (handlers; heard-rows from cv-objection-coach and cv-debrief; the `## Practice log` section), `memory/intel-reports/` (briefs + the follow-up and reactivation plan files), `identity/sales-system.md` (sales-system-setup; sales-call-block → Window + `## Call block`), `memory/sales-funnel.md` (sales-scorecard), the `## Conversion & Sales` block (incl. `Setter`); Top-50 touch cells as a designated interim appender until the Admin registers |
| AI Admin | `operations · goals · execution-framework · compliance · voice* · profile · story-bank · proof · brand-visual · offer · top-50 · conversations · pipeline · organization · scorecard · debriefs · deadlines · content-log · capture-log · intel · objections · ideas · intel-reports · follow-up-queue · sales-funnel · list-growth ("Calls booked from the funnel")` | `memory/pipeline` (admin-pipeline — stage moves, the source of stage; the Board's Next move · Due), `memory/follow-up-queue`, `scorecard` (weekly rows, eleven columns), `deadlines`, `memory/organization` (maintained from W5), the `## AI Admin (Week 5)` block (first line `AI Admin: set up [date]` = the OS-wide Admin-installed signal); never a Top-50 cell, never `conversations.md` |
| Lead Magnet | `brain.md · avatars · offer · positioning · proof · compliance · brand-visual · voice* · story-bank · profile · journey · operations · brokerage-model · objections · ideas (leadmagnet) · top-50 (counts only) · config · 06 · Materials` — read-only | `memory/magnets.md` (`## Current magnet` is what every other CTA reads), `memory/list-growth.md` (read by `attraction-goals` weekly mode and `admin-recruiting-scorecard` for "Calls booked from the funnel"), `identity/profiles.md` as the Week-6 updater (lm-profiles), the `leadmagnet` rows' Status in `ideas.md`, the `## Lead Magnet (Week 6)` block; never `offer.md`, never `voice.md` |
| Events | `avatars · offer · positioning · proof · compliance · top-50 · organization` | `memory/events.md`, `memory/pipeline` (event stages, requested through the Admin), `memory/content-log` (event content) |

One owner per file. A reader never writes a file it does not own. Every write pushes. Every file above ships in the Brain template as an
empty placeholder in its owner's locked shape. The Support plugin's `stack-map.md` carries this table so diagnostics can tell "Brain file
missing" from "plugin not installed."

**Pipeline stages, locked once** (the cohort doc has two vocabularies; this is the one every plugin uses):
`Identified → Conversation → Call booked → Call held → 3-way → Joined → Onboarded → Active`. The AI Admin owns stage moves;
Conversion, Events, and the Debrief request moves through it (or write directly if Admin is not installed yet, with the same vocabulary).

**Scheduled agents and their owners** (every agent is provisioned by its owning skill, with the member's explicit yes, never silently; the YouTube briefing lesson):

| Agent | Cadence | Owner skill | Week |
|---|---|---|---|
| Daily Agent Attraction Debrief | daily | `attraction-debrief` (Brain) | 1 |
| Weekly Content Performance | Fri | `sf-analytics` owns the task; `yt-analytics` appends its section from Week 4 | 3 |
| Morning Brief | daily | `admin-daily` owns it; `admin-attraction-setup` provisions it (task id `attraction-admin-morning-brief`); it extends the Debrief, never a second debrief | 5 |
| Daily Follow-Up Queue | daily | `admin-follow-up-queue` | 5 |
| Call Block Prep | daily | `cv-call-prep` | 5 |
| Cold-Lead Reactivation | 30 days | `cv-reactivation` | 5 |
| Monthly KPI Review | monthly | `admin-monthly-review` | 6 |
| Team Wins Newsletter | Thu | `admin-newsletter` | 6 |
| Post-Event Follow-Up | after each event | `ev-followup` | 6 |

Nine in all. Two modes the cohort doc describes as weekly agents are on demand instead (user, 2026-10-08): the Prospect
Radar's news scan (`attraction-prospect-radar` — "scan agent movement", writes `memory/intel.md`) and the Weekly Recruiting
CEO Review (`admin-recruiting-scorecard` CEO mode — "run my CEO review"). Neither has a task, a consent card, a config key,
or a task prompt file.

**Compliance gate, OS-wide.** Every public-facing skill in every plugin reads `identity/compliance.md` (3-state) before output and
appends: no income claims or rev-share earnings, non-disparagement of brokerages and people, brokerage name and license display, AI-likeness
disclosure on clone content, state/province recruiting scope, and the Meta "Employment" special-ad-category note on anything that becomes an ad.

---

## 2. Plugin 2 — Support (`cohort-claude-support` → `maa-claude-support`)

**Status:** mechanical fork + knowledge repoint. **9 skills kept 1:1** (navigator, setup, onboard, cohort, teach, diagnose, account, escalate, whatsnew).

| What changes | Detail |
|---|---|
| `shared/cohort-kb.md` | the MAA 6-week calendar (Nov 3 → Dec 17, Thanksgiving off, Week 7 bonus Jan 5), Tue/Thu call structure, Heidi's Wednesday posts, homework per week, playbooks and bonus assets per week |
| `shared/stack-map.md` | the 12 MAA plugins, install order, prefixes, the Brain-file ownership table from §1, every scheduled agent and its owner |
| `shared/source-map.md` | **Bella's transcripts** (Loom space, via the Atlassian connector once authorized) as the answer source: "what did Mike say about 3-way calls" returns the answer plus the lesson to rewatch |
| `maa-support-teach` | adds ManyChat templates, Claude Design, Claude Voice role-play, the CRM options (GHL / Follow Up Boss / Sheets) |
| `maa-support-diagnose` | adds: clone doesn't look like me, Thumbnail Employee output off-brand, "no Brain found" with both Brains installed (the marker/trigger disambiguation), Riverside fork pointing at the wrong Brain |
| `maa-support-account` | the honest monthly stack cost with optional ManyChat + Metricool |
| Freshdesk | the realtor desk's escalation door was HTTP 403 (suspended) on 2026-09-25; the MAA fork must not inherit a dead door. Decide: fix billing or point escalation at Mike's portal only |

**Ideas worth adding:** "Ask Mike" mode inside `maa-support-cohort` (the full transcript KB answered in Mike's voice using the existing
mike-sherrard-voice rules) is the backlog item the cohort doc rates highest; it is a knowledge-base change, not a new skill.

---

## 3. Design Studio — a Claude Design skill set, not a plugin (`aa-…-design`, 14 skills)

**Structural fact first.** Claude Design skills are uploaded `.md` files inside claude.ai/design, not Cowork marketplace plugins. The
"Design Studio Plugin" is therefore two things: (a) a folder in the repo, `design-studio/`, holding 14 upload-ready skill files plus
the **Agent Attraction Design System** (the uploadable design-system file Claude Design consumes), packaged with `_dist/` the same way
the realtor suite v2 is; and (b) a thin Cowork-side convention: Brain skills that need a design hand the member a paste-ready
design brief and name the `aa-…-design` skill to run. Nothing else is installable here. The Setup Guide must say this plainly.

| Skill | Status | From | Attraction-specific change |
|---|---|---|---|
| `aa-logo-design` | ADJUST | 1 Logo Designer | leader-brand prompt: "logo for you as a leader, not your listings"; three-path front door kept (fresh / refresh / love it) |
| `aa-style-sheet-design` | KEEP | 2 Brand Style Guide | existing-logo path kept; writes the Design System file the other 13 consume |
| `aa-brand-kit-design` | ADJUST | 3 Social Media Kit | profile + banner graphics across IG / FB / LinkedIn / YouTube with the recruiter CTA; the 5-question profile test baked into the copy slots |
| `aa-funnel-design` | ADJUST | 7 Sales Funnel Pages (+references) | three funnel shapes: opt-in (lead magnet), Partner Call booking, workshop registration; Netlify static-decoy-form rule carried; GHL-ready copy blocks |
| `aa-lead-magnet-design` | ADJUST | 8 Lead Magnet Designer | first magnet template = the Honest Brokerage Comparison Guide (factual, cited, dated, no ranking language); cover-only and 3D mockup modes kept |
| `aa-offer-stack-design` | **NEW** | none | the 3D offer stack: what the offer includes and what each piece is worth; reads the Brain Book's offer chapter; never prices rev share |
| `aa-offer-assets-design` | **NEW** | 6 Presentations (deck half) | "Join My Team" 1-pager, the opportunity deck, the welcome pack, the comparison sheet (comparison sheet is model-positioning output, compliance-gated) |
| `aa-product-mockup-design` | **NEW** | 8's 3D mockup mode (expanded) | the digital product mockup: 3D ebook and course box, device screens, bundle shots; Week 2 promise |
| the member's Brand HQ project in Claude Design (a `yt-thumbnail` brief; no separate thumbnail skill) | ADJUST | 12 Video Brand Kit (thumbnail section) | thumbnail layouts built from Mike's swipe-file patterns; fed by `yt-thumbnail`'s brief |
| `aa-carousel-design` | ADJUST | 5 Social Media Graphics | carousels from `sf-carousel` copy; LinkedIn PDF law kept (team leaders and broker-owners live there) |
| `aa-recognition-design` | **NEW** | 5 (templates) | Win Wall posts, first-deal and cap announcements, certificates; reads `recognition-log` |
| `aa-event-design` | ADJUST | 6 Presentations + 5 | flyers, registration graphics, countdown stories, workshop slides for the Events plugin |
| `aa-playbook-design` | ADJUST | 8 + 4 Print Kit | Value Vault: designed playbook, workbook, worksheet from any training the member writes |
| `aa-course-design` | **NEW** | none | Value Vault: course structure, module workbooks, certificates, cover art |
| `aa-ebook-design` | ADJUST | 8 | Value Vault: a short book from the member's story and method |

**Not carried:** 10 Monthly Market Report Kit, 11 Listing Launch Kit (seller assets), 14 Link in Bio (optional later; the cohort doc's
"Partner With Me" 5-page site idea would replace it).

**Ideas:** the cohort backlog's rename (`attraction-funnel-design`, split by funnel type) is already reflected above. Add the
"Why Join Me" 5-slide carousel as a Week 2 quick-win recipe inside `aa-carousel-design`: it is the shareable proof asset the workshop
review recommended, and every member posting it in Week 2 is retargeting content.

**Inputs needed:** the AAM brand (Agent Attraction brand kit) for the Design System default, Mike's thumbnail swipe file (Week 4), and the Value Vault template set.

---

## 4. Plugin 3 — Short-Form (`sf-`, 13 skills)

Forks `realtor-shortform-system` (15 skills). The realtor plugin's shared doctrine (`mike-frameworks.md`, `advisor-playbook.md`,
`publishing-guide.md`, `output-standard.md`, `composio-data-engine.md`) copies over; `mike-frameworks.md` is rewritten for attraction.

| Skill | Status | From | Attraction-specific change |
|---|---|---|---|
| `sf-setup` | ADJUST | shortform-setup | the "value first, plumbing last" rewrite (unshippable in the realtor repo) lands here CLEAN: writes `identity/content-pillars.md` (the 5 pillars: Authority · Perspective · Story · Proof · Personality) + bios on IG / FB / TikTok / LinkedIn with the recruiter CTA; Metricool connect is a later step with its own connect flow |
| `sf-board` | KEEP | shortform-board | same Notion board; status vocab locked OS-wide |
| `sf-talkinghead` | ADJUST (folds `shortform-scripts` + `shortform-video-plan`) | | 30–60s Reel scripts in the four content types (value, leadership, personal brand, storytelling); the 30-day calendar lives here |
| `sf-carousel` | ADJUST | shortform-carousel | "Why I Left My Brokerage" (story, never names the old brokerage), pain-point, myth-busting; hands design to `aa-carousel-design` |
| `sf-greenscreen` | ADJUST | shortform-greenscreen | reaction scripts on brokerage news and model comparisons (fed by the Prospect Radar's news scan, on demand); cardinal rules enforced |
| `sf-stories` | **NEW** | none | the 4-category daily story rotation (behind the scenes of leading · agent wins · personal · opportunity), the Story Prompt Deck, story-reply CTAs that hand to ManyChat |
| `sf-ideas` | ADJUST (folds `shortform-search-research`) | | weekly ideas + the 30-hook bank for the niche; research is what agents search, not buyers |
| `sf-weekly-routine` | **NEW** (absorbs the routine half of video-plan) | | 3–5 Reels a week, stories daily; 2 attraction, 2 authority, 1 story; batch days; the engagement routine |
| `sf-comment-to-dm` | **NEW** | none | the escalating CTA ladder (Follow → Comment → DM → Resource → Conversation → Call); sets the ManyChat keyword per Reel; writes the DM copy bank the importable templates use; hands qualified conversations to `cv-dm-flow` |
| `sf-optimizer` | KEEP | shortform-optimizer | hook, retention, CTA rewrite |
| `sf-publish` | ADJUST (folds `shortform-metricool`) | | captions, hashtags, scheduling; bring-your-own (Metricool / GHL / manual) with a real connect flow |
| `sf-batch-publish` | KEEP (folds `shortform-batch` film-day plan) | | |
| `sf-analytics` | ADJUST | shortform-analytics | which Reels and stories produced agent DMs; OWNS the Weekly Content Performance scheduled agent; the Studio pack / "add my numbers" path kept |

**Dropped:** `shortform-video-plan`'s local-search-demand premise (buyers and sellers) has no attraction equivalent; its calendar function moves into `sf-talkinghead`.

**Ideas:** the Launching doc's "personal posts on passions and hobbies" belongs in `sf-stories`' personal category and in the Brain's profile
interview (one question: "what do you do outside real estate that other agents would relate to?"). LinkedIn posts for the Team Leader and
Broker Owner personas (never recorded in the old MAA) are a cheap add to `sf-carousel` (PDF document posts already exist in the design skill).

**Bonus asset, not a plugin:** the ManyChat sequences (PARTNER, GUIDE, SCALE, GROWTH, story reply, DM qualifier, event, follow-up). We author
the copy bank and keyword sheet from `sf-comment-to-dm`'s output standard; the importable flow files need a ManyChat account to export from (Mike's).

---

## 5. Plugin 4 — AI Editor, Riverside (`studio-`, 28 skills)

**Mechanical fork of `realtor-riverside-editor` v0.4.1.** No creative changes. What the fork touches:

- **Decision (user, 2026-10-08): ONE plugin, not two.** The Studio is vendored into this repo under its own name and version (`scripts/vendor-riverside.sh`) with a single addition, the Brain-home rule in `house-rules.md`: use `~/attraction-brain/` when it exists, else `~/realtor-brain/`, and call that Brain's sync skill; every `editor/` path resolves against `<Brain home>`. Back-port that rule to the realtor repo so the two copies are byte-identical. A member who installed it from the realtor marketplace does not install it again (Support says so).
- No skills removed (same plugin). `studio-listing` simply goes unused by attraction-only members.
- `brand-wiring.md` reads the Attraction brand kit (Video Brand Kit v3.3 shape, generated by the member's Brand HQ project in Claude Design (a `yt-thumbnail` brief; no separate thumbnail skill) + `aa-brand-kit-design`).
- `cta-pack.md` swaps the realtor CTAs for the attraction ladder (book a call, DM the keyword, grab the guide).
- `editor/` state (config, jobs, b-roll library) is added to the attraction sync allowlist on day one (the audit found it outside the realtor allowlist, so it forgot everything after session one in Cowork).
- The compliance line in `studio-check` adds: no income claims on cards or captions; AI-likeness disclosure if a clone clip is cut in.

**The doors MAA leans on** (named in the Setup Guide): navigator, setup, reel, longform, interview, captions, broll, music, hook, repurpose, publish, rescue. The other 16 stay installed and reachable.

---

## 6. Plugin 5 — YouTube (`yt-`, 19 skills)

Forks `realtor-youtube-system` (19 skills). The shared doctrine (`youtube-doctrine.md`, Mike's 30-section realtor KB) is **replaced**, not edited:
`shared/attraction-youtube-doctrine.md` is written from the Week 4 vault (9 lessons), the VIP day framework (Problem → Situation → Future
niche pillars, interviews, model breakdowns, the 8-video cycle 3 + 1 + 4, the 180-day plan) and the title/thumbnail/CTA lessons. `seo-knowledge-base.md`
is re-keyed to what agents search (comparisons, rev share, switching, sponsor questions).

| Skill | Status | Change |
|---|---|---|
| `yt-setup` | ADJUST (folds `youtube-channel`) | channel positioned for attraction: banner brief, about, playlists by pillar, upload defaults, CTA; writes `identity/channel.md` |
| `yt-gameplan` | ADJUST | the 3-pillar map (niche authority · interviews · model/opportunity) + the first 90 days on the 8-video cycle; goal-math from the Brain's scorecard |
| `yt-ideation` | ADJUST | the 7 title formulas + agent pain points, ideas bucketed Problem / Situation / Future / Interview / Model |
| `yt-research` | ADJUST | what agents search; brokerage news; what the member's avatar is asking |
| `yt-outliers` | ADJUST | outlier attraction channels and videos, what made them work (cardinal rules: never name a competitor's flaw) |
| `yt-script` | ADJUST | the four formats: Why I Switched (story, old brokerage unnamed), Pain Point Series, Model Breakdown, Niche Breakdown; voice-print |
| `yt-interview` | **NEW** | guest list from the organization + Top-50, the hook-and-transformation title rule ("How Kevin built…"), question sets, edification lines, the guest's distribution ask; writes `memory/interview-pipeline.md`; hands the edit to `studio-interview` |
| `yt-model-breakdown` | **NEW** | comparison and explainer videos with accurate, dated model data from `brokerage-model.md`; no trash talk; the "answer what they're already researching" list (Explained · vs · Should you join · How rev share works · Questions to ask a sponsor) |
| `yt-thumbnail` | **NEW** | writes the thumbnail brief (title, pillar, face, text rule from Mike's swipe-file patterns) for the member's Brand HQ project in Claude Design (a `yt-thumbnail` brief; no separate thumbnail skill) in Claude Design; 3 directions scored against the patterns |
| `yt-seo` | ADJUST | title, description, chapters, pinned comment, book-a-call CTA; keyword set re-keyed |
| `yt-make-video` | KEEP | end to end; one chat = one video; now calls yt-thumbnail |
| `yt-repurpose` | ADJUST | 3 Shorts, 1 carousel, 5 stories, 1 email, 1 blog, plus **conversation starters** (the Week 4 doc adds "every video becomes conversation starters" → hands 3 openers to `cv-conversation-starter`) |
| `yt-leads` | ADJUST (folds `youtube-comments`) | the CTA and lead magnet per video; comment triage routes to ManyChat keyword and flags prospects into `top-50` |
| `yt-analytics` | ADJUST | which videos produced agent DMs, comments, booked calls; appends its section to the Weekly Content Performance agent from Week 4 |
| `yt-coach` | KEEP | delivery coaching from a transcript |
| `yt-consistency` | KEEP | cadence 1 long-form a week + interviews |
| `yt-briefing` | KEEP, off by default, **asks before provisioning**, draft-only | |
| `yt-board` | KEEP | same Notion board as Short-Form |
| `yt-triggers` | ADJUST | the scheduled tasks list (weekly ideas, performance, monthly review), each provisioned with consent |

**Dropped:** `youtube-market-report` (seller content; slot goes to model breakdowns).
**Fix carried in, not inherited:** the realtor YouTube plugin never writes `content-log.md`; the fork writes a row at script, at publish, and at repurpose.

---

## 7. Creative Studio (Higgsfield employees) — REMOVED from this build

Parked per the user on 2026-10-08: not a plugin, not in scope for now. Nothing is built, and no skill routes to a `cs-` skill.
Where the plan referenced it: `yt-thumbnail` uses the member's Brand HQ project in Claude Design (a `yt-thumbnail` brief; no separate thumbnail skill) design brief as its only path; `aa-product-mockup-design` ships
without the animation hand-off; `studio-broll` uses Riverside's stock library only; Events and Lead Magnet ad creatives are design
briefs for Claude Design. The SAO clone and thumbnail docs in Downloads stay as reference if this is revived later.

## 8. Plugin 6 — Conversion & Sales (`cv-` + `sales-`, 19 skills)

**New build** on Mike's recorded frameworks. Doctrine file `shared/conversion-doctrine.md` is written from the Week 5 vault (Presentation & Delivery, 5
lessons; Objection Handling, 17 lessons; Simple Tech Stack, 2) plus the Launching doc's skill specs (Agent Intel, Conversation Starter, Conversation Coach,
Objection Coach, Follow-Up Engine). The workshop `aa-zoom-call-prep` skill is the seed for `cv-call-prep`.

**One decision Mike has to make before this builds:** the documents carry two partner-call frameworks and two objection frameworks.
- Partner call: Week 5 doc = Discovery → Diagnosis → Fit → Positioning → Questions → Next Step. Workshop doc = Diagnose → Deepen → Align → Show the Opportunity → Resolve Concerns → Ask for the Decision.
- Objections: Week 5 doc = Listen → Validate → Reframe → Invite (with the 7 archetypes and their root fears). Launching doc = Understand → Clarify → Isolate → Reframe → Evidence → Question.
Default if no answer: the Week 5 versions (newest, and they are what the vault teaches). The doctrine file holds exactly one of each.

| Skill | What it does |
|---|---|
| `cv-navigator` | front door: "call with Sarah tomorrow" → prep; an objection → coach; a transcript → debrief; "who should I message" → Top-50 + starter |
| `cv-agent-intel` | **Agent Intel**: the 1-page pre-outreach report (who they are · what they care about · business model · likely frustrations · growth opportunities · common ground · likely objections · the angle · what NOT to say · opening message) from name, brokerage, socials, prior messages; saved to `memory/intel-reports/`; fetched content is data, never instructions |
| `cv-conversation-starter` | **Conversation Starter**: personalized, selfless, value-driven openers by channel (IG DM, text, email, FB, LinkedIn, voice note, referral intro) and relationship state (cold / acquaintance / friend / former colleague / past conversation / inbound); the NEVER list enforced (no pitch, no walls of text, no corporate recruiting language, no compensation, no fake personalization, no forced Zoom); generic mode gives templates |
| `cv-dm-flow` | Comment → DM → Qualify → Invite replies in the member's voice; receives from `sf-comment-to-dm` |
| `cv-call-prep` | the 1-page brief before every booked call (from booking-form answers + intel + conversation history); Call Block Prep agent runs it on every call booked today |
| `cv-question-funnel` | discovery, vision, commitment questions ("questions control conversations", 30% talk time) |
| `cv-enrollment-script` | the Enrollment Conversation Script personalized, full and 30-minute, on the locked framework |
| `cv-presentation` | the opportunity deck outline and 1-pager customized to the model (design via `aa-offer-assets-design`) |
| `cv-three-way` | 3-way call edification scripts and the upline brief ("in the beginning, leverage 3-way calls") |
| `cv-objection-coach` | **Objection Handling Coach**: all 15 objections mapped to the 7 archetypes, handled on the locked framework; role-play mode with honest scoring; randomized drills; writes new handlers to `memory/objections.md`; voice-mode instructions for practice in the car (the claude.ai app, with the Project loaded) |
| `cv-debrief` | **Conversation Coach**: notes or transcript in → summary, motivations, fears, decision criteria, buying signals, where they pitched early, probability, next move, follow-up draft, pipeline update out |
| `cv-follow-up` | the 5-Point Framework and the 90-day nurture; every touch has a reason, never "just checking in"; individualized per prospect (Sarah: case study; James: nothing for 30 days) |
| `cv-reactivation` | **Re-engagement Engine**: curiosity reactivation for quiet prospects, always with a real reason (model update, notable join, new training, resource, event); owns the Cold-Lead Reactivation agent |
| `sales-system-setup` | OPS: the Partner Call calendar, application form questions, tags, the locked pipeline stages, reminders; CRM choice (GHL / Follow Up Boss / Sheets) |
| `sales-booking-page` | OPS: booking page copy and qualifying questions (design via `aa-funnel-design` booking shape) |
| `sales-show-up` | OPS: confirmation, 24h and 1h reminders, pre-call video script, no-show recovery; draft-only |
| `sales-setter` | OPS: DM and phone qualification scripts for a VA or setter |
| `sales-call-block` | OPS: the daily call block and capacity math (calls per week vs hours from the Brain) |
| `sales-scorecard` | OPS: calls booked, show rate, presentations, 3-ways, closes, by source; feeds the Brain scorecard |

**Ideas worth adding now (cheap, high value):** Objection Capture ("I just heard a new one") as a mode of `cv-objection-coach`; a Fathom / Zoom transcript
drop into `cv-debrief` as the Call-Recording-to-Pipeline workflow; the Switching Transition Plan one-pager (license transfer, listings, MLS, email, signage)
as a `cv-follow-up` asset that kills "I have closings to finish" (needs the inducement-rules review the cohort doc flags). The Full Call Simulator is the
Week 7 fast-action bonus and stays out of v1.

---

## 9. Plugin 7 — AI Admin (`admin-`, 8 skills)

Forks `realtor-ai-admin` (17 skills) down to the attraction layer (8 skills: the seven below plus `admin-attraction-setup`). The realtor admin stays the realtor's admin; this one only runs the organization.

| Skill | From | Change |
|---|---|---|
| `admin-daily` | admin-briefing + admin-wrap | morning brief: agent inquiries, calendar, follow-ups due, content due, one coaching note; EXTENDS the Brain's Daily Debrief (same scorecard, richer inbox and calendar reads) |
| `admin-pipeline` | admin-memory + admin-matchback | the prospect ledger with the locked stages; CRM-aware (GHL / FUB / Sheets via bring-your-own connector or Composio), Brain memory is the fallback and the truth |
| `admin-follow-up-queue` | admin-chase + admin-confirmations | every prospect due a touch, drafted in the member's voice; nothing sends without approval; owns the Daily Follow-Up Queue agent |
| `admin-recruiting-scorecard` | admin-recruiting-scorecard | weekly KPIs vs targets; CEO mode = the Weekly Recruiting CEO Review (bottleneck, recommendation, next week's target) |
| `admin-newsletter` | new | the weekly Team Wins email, draft-only; owns the Thursday agent |
| `admin-va-tasks` | admin-filing + admin-vendors (shape) | posting prep, data entry, database cleanup, weekly reporting handoffs for a VA |
| `admin-monthly-review` | admin-recruiting-scorecard (monthly mode) | the month vs the 30-60-90 plan; next targets; owns the Monthly KPI Review agent |

**Dropped:** scheduling, inbox, sweep, dispatch (the Brain's `attraction-capture` covers on-the-go), feedback, prep, setup (folded into `admin-daily` first run), the realtor front door.
**Carried fix:** `admin-core.md` and the briefing prompt read `~/attraction-brain/`; the Microsoft mapping in `connectors.md` applies unchanged.

---

## 10. Team & Retention — REMOVED

Removed from the OS by the user on 2026-10-08. Not built. `memory/organization.md` stays in the Brain (capture and the Admin plugin write joins to it); the Design Studio's `aa-recognition-design` reads it for Win Wall posts.

## 11. Plugin 8 — Lead Magnet (`lm-`, 11 skills)

Forks `realtor-lead-capture` (5 skills, shipped v0.24.0). The copywriting KB and output standard copy over; the first magnet is locked.

| Skill | Status | Change |
|---|---|---|
| `lm-navigator` | KEEP | checks the offer exists (Week 2), locks the first magnet, routes |
| `lm-magnet` | ADJUST | writes the magnet in the member's voice; first = **the Honest Brokerage Comparison Guide** (factual, cited, dated, no ranking, no disparagement; "honest" means transparent about trade-offs, never critical of a named brokerage; compliance-gated hard) |
| `lm-funnel` | ADJUST | opt-in page, thank-you, book-a-call step; design via `aa-funnel-design`; static decoy form rule |
| `lm-gbp` | KEEP | GBP positioned for attraction, posts pointed at the magnet |
| `lm-profiles` | KEEP | social bios aligned to the funnel (shares the 5-question profile test with `sf-setup`; one owner: `sf-setup` writes `identity/profiles.md` first in Week 3, `lm-profiles` is the Week 6 updater) |
| `lm-magnet-ideas` | **NEW** | next magnet from the persona map and what converted (Switching checklist, Sponsor questions, Rev-share explainer, 90-day plan template) |
| `lm-design` | **NEW** | the styled PDF brief for `aa-lead-magnet-design` (cover + 3D mockup) |
| `lm-delivery` | **NEW** | the DM, email, and story that deliver the magnet (ManyChat GUIDE keyword copy) |
| `lm-nurture` | **NEW** | awareness → proof → CTA email sequence and the weekly newsletter; draft-only; list building is the Week 6 vault's first scaling lesson |
| `lm-partnerships` | **NEW** | outreach to lenders, coaches, vendors, other leaders (the Leveraging Partnerships lesson) |
| `lm-analytics` | **NEW** | opt-in rate, list growth, magnet-to-call conversion (manual numbers or Composio where connected) |

**Idea:** the public Rev Share Calculator page ("how many agents replace your commission income?") is the cohort doc's strongest MAA lead magnet and is Mike's, not the member's; it belongs in the internal ops track, not this plugin.

---

## 12. Plugin 9 — Events & Workshops (`ev-`, 10 skills)

**New build** from `anthropic-skills:workshop-ops` (Mike's own workshop ops skill) and the Week 6 vault's Live / Virtual / Evergreen lessons, plus the Launching doc's `/launch-event` spec.

| Skill | What it does |
|---|---|
| `ev-navigator` | front door; picks the format from the goal and the member's capacity |
| `ev-strategy` | live (local mastermind, brokerage-neutral networking, AI or social workshop) vs virtual training vs evergreen webinar; theme and positioning; the brokerage-neutral rule |
| `ev-live` | the local event playbook: venue, run-of-show, co-hosts, follow-up |
| `ev-virtual` | the virtual workshop playbook (the Virtual Workshop Launch Kit is its reference) |
| `ev-evergreen` | the evergreen webinar: script outline, registration, replay, automated follow-up |
| `ev-promo` | the promo calendar and copy: emails, DMs, texts, posts, stories (draft-only; creative briefs go to `aa-event-design`) |
| `ev-registration` | registration page copy → `aa-funnel-design` (registration shape); form questions |
| `ev-runofshow` | outline + slide brief → `aa-event-design`; the pitch-free "invite to a conversation" close |
| `ev-followup` | attended / no-show / hot / cold sequences; moves attendees into the pipeline; owns the Post-Event Follow-Up agent |
| `ev-analytics` | registrations, show rate, conversations, calls booked per event |

---

## 13. Build sequencing (parallel-agent plan, after approval)

The user's intent: approve the plans, then build everything at once with multiple agents. The dependencies that constrain parallelism:

1. **Sprint 0 (serial, one agent, 2 days):** repo scaffold, marketplace.json, scripts, the shared mechanics copied once (`how-we-speak`, `ask-once-default`, `connectors`, `doc-formatting`, `render_doc.py`), the Brain template and `brain-contract.md` template, the locked vocabularies (pipeline stages, content-log row, scorecard block, config registry). Everything downstream imports from here, so it goes first.
2. **Doctrine pass (parallel, one agent per doctrine file, blocked on the transcripts):** attraction, persona, brokerage-models, compliance, short-form frameworks, YouTube, conversion, retention. Each agent gets the relevant vault module transcripts and the matching week doc.
3. **Plugin build (parallel, one agent per plugin, each in its own worktree):** 11 agents, each briefed with: the plan section above, its doctrine file, the Brain contract, §11 house rules, and the realtor source plugin path (read only). Mechanical forks (Riverside, Support) finish in hours; new builds (Conversion, Events) take the longest.
4. **Seam pass (serial, one agent):** trigger-collision diff, Brain-file ownership check, scheduled-agent consent check, compliance 3-state check, description-length check, `check-release.sh` green.
5. **Prove it:** one demo brain (fictional member) run through Weeks 1–6 end to end; Cowork cold test on a real member for Week 1 and Week 2; release.

Ship dates follow the cohort's record-ahead rule: Brain + Support + the three Design Package skills (`aa-logo-design`, `aa-style-sheet-design`, `aa-brand-kit-design`, because brain + brand both land in Week 1) by Oct 30; the rest of Design Studio by Nov 6; Short-Form + Riverside fork by Nov 13; YouTube by Nov 20 (before Thanksgiving); Conversion + Admin by Dec 4; Lead Magnet + Events by Dec 11.

---

## 13b. The transcript knowledge base (103 videos, incoming)

The user is delivering transcripts of Mike's ~103 agent attraction training videos. They are the single most valuable input to this
build: every doctrine file, the Support plugin's answer source, and the voice of every skill come from them. Handling:

- **Where they live:** `knowledge/transcripts/<module>/<nn>-<lesson-title>.md`, one file per video, with a `manifest.md` mapping each file to
  its vault module, week, and lesson number (the module and lesson lists in the Week 1–6 docs are the index). Private repo; never shipped
  inside a plugin zip. Derived doctrine files cite lessons by `module/lesson` so every rule in a skill is traceable to what Mike actually said.
- **The doctrine pass (Sprint 1):** one agent per doctrine file reads only its module's transcripts plus the matching week doc and writes the
  file in Mike's framing and vocabulary (his phrases, his cardinal rules, his examples), under the grounding law: nothing enters a doctrine file
  that a transcript or a week doc does not support. Files: `attraction-doctrine` (W1 modules), `persona-doctrine` (Market Analysis module),
  `brokerage-models` + `positioning-doctrine` (W2 modules), `shortform-doctrine` (W3 modules), `attraction-youtube-doctrine` (W4 module),
  `conversion-doctrine` (W5 modules, all 17 objection lessons), `retention-doctrine` (W6 modules).
- **Mike's voice in the skills:** the existing `mike-sherrard-voice` rules plus a per-doctrine "how Mike says it" block (signature phrases,
  what he never says) so a skill's coaching lines read as his, while member-facing outputs still use the member's voice-print.
- **Support's "what did Mike say about…":** `source-map.md` points at the transcript folder; answers quote the lesson and name the video to rewatch.
- **Not in scope:** editing or distributing the transcripts themselves; the old ChatGPT-era Minimum Tech Stack lesson is excluded per the cohort doc.

**Editor engine, stated once:** the AI Editor plugin is the Riverside engine only. The retired Descript-based plugin is not forked, referenced, or routed to anywhere in this OS.

## 14. Decisions needed from Mike (beyond the Brain plan's list)

1. **Lock one partner-call framework and one objection framework** (§8). Default: the Week 5 doc versions.
2. **Transcripts access**: authorize the Atlassian connector for the Loom space, or have Bella export. Blocks every doctrine file.
3. **Design Studio**: it is a Claude Design skill set (uploaded files + a Design System), never a plugin; confirmed by the user 2026-10-08. Still needed: the AAM brand kit for the default Design System.
4. **Riverside and Support forks**: confirm the mechanical fork (they cannot ship as-is).
5. **CRM scope for v1**: Brain-memory pipeline as the truth with GHL / Follow Up Boss / Sheets sync as bring-your-own, or a specific CRM first.
6. **Freshdesk**: fix billing or re-point escalation.
7. Mike's thumbnail swipe file with pattern notes (for the member's Brand HQ project in Claude Design (a `yt-thumbnail` brief; no separate thumbnail skill)).
8. **Inducement-rules review** before the Switching Transition Plan and the Earnings Comparison one-pager ship (cohort doc flags it; both stay out of v1 until cleared).
9. **Voice-mode role-play** is a claude.ai app feature, not a Cowork skill: confirm the Objection Coach ships text role-play plus app instructions.
