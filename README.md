# Agent Attraction OS — Team Sherrard's Claude marketplace for agent attraction

The plug-and-play AI systems behind the **Master Agent Attraction** cohort: for real estate agents who attract other agents into a
cloud-brokerage organization (eXp, REAL, LPT, Epique, any cloud brokerage) or who build a local team or brokerage.

Install the marketplace in Claude Cowork: **Customize → Plugins → ＋ (beside Personal plugins) → Add marketplace →** paste
`teamsherrard/claude-agent-attraction-os`. Install Plugin 1 first, toggle **Sync automatically**, then say **"Set up my attraction brain."**

## The plugins (install in this order, one per cohort week)

> **Available in the marketplace today: Plugins 1 to 6.** (The Design Studio is a Claude Design skill set you upload, not
> a plugin you install.) Plugins 7 to 9 are built and being fixed and optimized on the `wip/all-plugins` branch; they
> return to this marketplace one by one as the cohort reaches them. Install Plugins 1 and 2 in Week 1, Plugin 3 in
> Week 2, Plugins 4 and 5 in Week 4, Plugin 6 in Week 5 — each one as its week arrives, not before.

| # | Plugin | Week | What it is |
|---|---|---|---|
| 1 | `attraction-ai-brain` | 1 | The Agent Attraction Brain: who you are as a leader, who you attract, what you have to give, your numbers, your voice and brand, your rules. Every other system reads it. Includes the Daily Agent Attraction Debrief, Prospect Radar, the Brokerage Model Expert, the Rev Share Calculator, the Top-50 ledger, on-the-go Capture, and the Brain Board (the Brain as a living map with the goals tracker, re-rendered on every push). |
| 2 | `maa-claude-support` | 1 | The help desk, pointed at the 6-week calendar and Mike's full lesson knowledge base. |
| – | Design Studio | 3, 6 | A Claude Design **skill set**, not a plugin: ten `aa-…-design` skills in `design-studio/` (rewired 2026-11-09 to the three Week 3 files — the Week 3 Kit, the guide, the Design Package brief). Week 3: logo · style sheet · brand kit · offer kit (digital product mockup first) · guide PDF · opt-in page · social graphics (the six kit posts, team and promo templates) · video kit with the pop-up set. Week 6: events · Value Vault. Digital-only, a coaching brand for agents. Upload files: the numbered zips in `design-studio/_dist/` and on each GitHub release. |
| 3 | `attraction-lead-magnet` | 2 | Lead magnets and opt-in funnels pointed at agents — install in Week 2. Offer-first: it builds your Partner Offer in the same session if it isn't built yet, recommends ONE magnet built from it (say yes, or ask for the next best), and writes the magnet and the sales funnel outline, then puts the page and the guide's outline into your Week 3 Kit — the one file (your offer is in it too) you upload to Claude Design in Week 3; it writes your bios first. By the end of this week you have ONE lead magnet, written and designed, with its funnel outline (tangible) — and your unique value proposition broken down: your offer explained in detail and how to create it, its name, the marketing language to use, and where to host it (intangible). |
| 4 | `attraction-shortform-system` | 4 | The Short-Form Attraction Engine — install in Week 4. One sitting: your profiles and two keywords confirmed, one question (which day you can block three hours to film), your Short-Form Game Plan — two Reels you film and one carousel you post, every week from week one, about one post in ten asking for the guide — your Notion board with the four weeks, ONE draft-only Monday Week Plan switched on with your one yes (the week in one package), Metricool connected, your first Reel scripted for Instagram's free Edits app, then it stops. Reels, stories, carousels, industry-news green screen, publishing, analytics. Requires Plugins 1 and 3. |
| 5 | `realtor-ai-editing-studio` | 4 | The AI Editing Studio — install in Week 4 with Short-Form. Claude edits your Reels and long videos inside your own Riverside account (cuts, hook, audio, captions, music, B-roll, your Week 3 Video Brand Kit), every change verifiable, nothing published without your yes. Never writes titles, captions or descriptions. Riverside is the only editor (editing inside Instagram's Edits app is not part of the program; filming in it is). Vendored from the realtor marketplace; requires Plugin 1 and a Riverside Grow plan or higher. |
| 6 | `attraction-youtube-system` | 5 | The Long-Form Authority Engine — install in Week 5 (date to be confirmed). One sitting: your channel optimized for the agents you want to attract, your YouTube Game Plan on the 8-video cycle (one video a week to start, two the step-up), your next 30 days on the YouTube tab of your Notion board (each card with a real video to watch first and a six-step publish checklist), one draft-only workflow switched on with your one yes (your Monday Kickoff — every Monday, this week's video drafted onto its card; on the first Monday of the month, last month reviewed too) with a short email note when your mail is connected, your first video. Requires Plugin 1; it builds on Plugins 3 and 4 when you have run them, and from your Brain alone when you have not. |
| 7 | `attraction-conversion-sales` | 6 | Conversion & Sales — install in Week 6. One sitting, no questions: your enrollment call script (full and 30-minute) on Mike's sequence of events, your partner presentation that bridges the gap, your objection playbook (the fifteen in your words, with your brokerage's real answers), ONE draft-only workflow switched on with your one yes (your Morning Call Prep — every partner call on today's calendar prepped at 7:00; Mondays your follow-ups for the week with a reason each; on the 1st, anyone who went quiet), then hands you to Stacy in a new chat. The Sales Trainer, Stacy, plays the agent, throws the objections, scores you honestly and makes you say it again — by voice in your project or by text. Call prep before every call, the debrief after, 3-way edification, conversation starters and DM replies in your voice. Nothing is sent without you. Requires Plugin 1. |
| 8 | `attraction-ai-admin` | later (to be confirmed) | The pipeline, the follow-up queue, the scorecard, the CEO review. |
| 9 | `attraction-events-workshops` | later (bonus, to be confirmed) | Live, virtual, and evergreen events that attract agents. |

Every plugin reads the Brain through the contract in `docs/BRAIN-CONTRACT.md` and ships a `shared/brain-contract.md` naming the files it reads and owns.

## Where things are
- `plugins/` — the Cowork plugins. `design-studio/` — the Claude Design skill set. Mike's transcripts live in the separate private repo `teamsherrard/claude-agent-attraction-knowledge` (never in this public repo, never in a plugin).
- `docs/plans/` — the build plans (`01-ai-brain-plugin-gameplan.md`, `02-agent-attraction-os-master-gameplan.md`, `BUILD-BRIEF.md`).
- `scripts/check-release.sh` — the pre-release gate (run after `git add`, never inside a commit chain). `scripts/build-plugin-zip.sh` — the upload-zip builds in `dist/`.
- `CHANGELOG.md`, `VERSION`, `SECURITY.md`, `LICENSE.md`.

This repo is independent of `teamsherrard/claude-agent-os` (the realtor marketplace). Nothing here imports from it; a member can run both.
