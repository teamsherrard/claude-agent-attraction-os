# Agent Attraction OS — Team Sherrard's Claude marketplace for agent attraction

The plug-and-play AI systems behind the **Master Agent Attraction** cohort: for real estate agents who attract other agents into a
cloud-brokerage organization (eXp, REAL, LPT, Epique, any cloud brokerage) or who build a local team or brokerage.

Install the marketplace in Claude Cowork: **Customize → Personal Plugins → Browse Plugins → ＋ → Add marketplace →** paste
`teamsherrard/claude-agent-attraction-os`. Install Plugin 1 first, toggle **Sync automatically**, then say **"Set up my attraction brain."**

## The plugins (install in this order, one per cohort week)

| # | Plugin | Week | What it is |
|---|---|---|---|
| 1 | `attraction-ai-brain` | 1 | The Agent Attraction Brain: who you are as a leader, who you attract, what you have to give, your numbers, your voice and brand, your rules. Every other system reads it. Includes the Daily Agent Attraction Debrief, Prospect Radar, the Brokerage Model Expert, the Rev Share Calculator, the Top-50 ledger, and on-the-go Capture. |
| 2 | `maa-claude-support` | 1 | The help desk, pointed at the 6-week calendar and Mike's full lesson knowledge base. |
| – | Design Studio | 1–2, 6 | A Claude Design **skill set**, not a plugin: all 14 `aa-…-design` skills built (the Design Package, offer assets, recognition, events, the Value Vault; a Week 4 thumbnail is a `yt-thumbnail` brief pasted into the Brand HQ project). See `design-studio/`. |
| 3 | `attraction-shortform-system` | 3 | The short-form attraction engine. |
| 4 | `realtor-riverside-editor` | 3 | The AI Editing Studio on Riverside, the same plugin as the realtor marketplace, reads whichever Brain you have. Install it once. |
| 5 | `attraction-youtube-system` | 4 | The long-form authority engine. |
| 6 | `attraction-conversion-sales` | 5 | Agent Intel, Conversation Starter, the partner call, the Objection Handling Coach, call audits, follow-up. |
| 7 | `attraction-ai-admin` | 5 | The pipeline, the follow-up queue, the scorecard, the CEO review. |
| 8 | `attraction-lead-magnet` | 6 | Lead magnets and opt-in funnels pointed at agents. |
| 9 | `attraction-events-workshops` | 6 | Live, virtual, and evergreen events that attract agents. |

Every plugin reads the Brain through the contract in `docs/BRAIN-CONTRACT.md` and ships a `shared/brain-contract.md` naming the files it reads and owns.

## Where things are
- `plugins/` — the Cowork plugins. `design-studio/` — the Claude Design skill set. `knowledge/` — Mike's transcripts (private, never shipped in a plugin).
- `docs/plans/` — the build plans (`01-ai-brain-plugin-gameplan.md`, `02-agent-attraction-os-master-gameplan.md`, `BUILD-BRIEF.md`).
- `scripts/check-release.sh` — the pre-release gate (run after `git add`, never inside a commit chain). `scripts/build-plugin-zip.sh` — the upload-zip builds in `dist/`.
- `CHANGELOG.md`, `VERSION`, `SECURITY.md`, `LICENSE.md`.

This repo is independent of `teamsherrard/claude-agent-os` (the realtor marketplace). Nothing here imports from it; a member can run both.
