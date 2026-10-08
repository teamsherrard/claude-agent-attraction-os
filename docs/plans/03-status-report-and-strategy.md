# Agent Attraction OS — Overnight Build Report and Strategic Game Plan

*Written for Riya and Mike · 2026-10-09 · repo `claude-agent-attraction-os` · status at the end of the overnight run*

> Sections 1–3 are the status (what is built, verified, and left). Sections 4–8 are the strategic advice you asked for:
> what to add, remove, optimize, fix, and what nobody is thinking about yet.

<!-- STATUS SECTIONS ARE FILLED AT THE END OF THE RUN; STRATEGY SECTIONS BELOW ARE FINAL -->

## 1. What is built (filled at end of run)

## 2. What was verified, and how (filled at end of run)

## 3. What is left (filled at end of run)

---

## 4. Decisions only you or Mike can make (blocking or near-blocking)

1. **Riverside back-port.** The Studio is one plugin on two marketplaces. The vendored copy here carries one added rule (use the attraction Brain when it exists). I did not edit the realtor repo, because your "never touch the old plugins" rule outranks convenience. Until the same rule is added there, the two copies differ by that one section, and a member who installed the Studio from the realtor marketplace will not get the rule. Smallest safe move: a single commit in the realtor repo adding the Brain-home section to `house-rules.md` and `<Brain home>` in paths, released as a patch version, then re-vendor here with `scripts/vendor-riverside.sh`.
2. **Partner-call framework labels** (Conversion doctrine §3): step-five label, default call length (60 until mastered, then 30 vs the workshop's "30-minute Partner Call" promise), and the objection framework label. The plugin ships with defaults and says so.
3. **The "5-Point Framework"** is named in the course docs and defined nowhere. The follow-up skill is built on lesson 85's five principles. Mike should confirm or supply his five.
4. **Support plugin placeholders**: support portal URL (the Freshdesk account was suspended on 2026-09-25; nothing here points at it), Circle link, call times, refund policy, the Circle video links. All marked `[NOT SET]` and the setup skill asks for them.
5. **Events & Workshops plugin** is in the plan (Plugin 9) but was not on your overnight list, so it is not built. Week 6 ships without it unless you say otherwise.
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
- **Retention after graduation.** Team & Retention is removed, which is the right call for a six-week build. The "join me and I give you this" promise (the Value Vault) still lands in Week 6 and depends on the Design Studio skills that are not built yet (ds-playbook, ds-course, ds-ebook, ds-product-mockup). That is the Week 6 critical path.
- **Insider members with both OS installed are your best testers and your most likely bug reporters.** Give three of them early access to the Week 1 build before Oct 30.
