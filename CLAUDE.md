# Agent Attraction OS marketplace — working rules for Claude

This is `teamsherrard/claude-agent-attraction-os`, Team Sherrard's PUBLIC Claude Code plugin marketplace for the agent-attraction cohort (marketplace name `teamsherrard-agent-attraction`). Cohort members install one plugin per week in Cowork. Every push to `main` is a release they will pull.

## Read first
- `START-HERE.md` and `README.md` (the plugin order is the cohort week order)
- `docs/setup-guide.md` and `docs/BRAIN-CONTRACT.md`
- `docs/plans/` (build plans), `docs/playbooks/` (member-facing), `docs/demo/`
- `CHANGELOG.md` and `VERSION` for the current release

## Layout
- `.claude-plugin/marketplace.json` — the registry. Every plugin's version here must equal its `plugins/<name>/.claude-plugin/plugin.json`.
- `plugins/` — attraction-ai-brain, attraction-ai-admin, attraction-lead-magnet, attraction-shortform-system, attraction-youtube-system, attraction-conversion-sales, attraction-events-workshops, maa-claude-support, and realtor-riverside-editor.
- `plugins/realtor-riverside-editor` is VENDORED from `teamsherrard/claude-agent-os` by `scripts/vendor-riverside.sh`, which copies from a local clone of that repo and then re-applies this repo's small downstream patches (the Brain-home path and two description trims; read the script header). Fix editor bugs upstream first, then re-vendor; in a cloud session run the script against a fresh clone of claude-agent-os. Direct edits here are only for those documented downstream patches. (README's statement that this repo is independent of claude-agent-os has this one exception.)
- `design-studio/` — the `aa-*-design` skills (Claude Design only).
- `scripts/check-release.sh` — the release gate. `scripts/build-plugin-zip.sh` — builds zips into `dist/` (gitignored, absent in a fresh clone).

## Release rules (the gate enforces most of these; the rest are house rules)
1. Releases go directly to `main`. One commit per release: code + version bump + `CHANGELOG.md` entry + `VERSION`.
2. Run `scripts/check-release.sh [plugin]` AFTER `git add` and BEFORE `git commit`, as its own command. Never pipe it inside a commit chain. It must be fully green before you commit.
3. Every skill `description:` must be ≤1024 characters. Over-limit skills are SILENTLY SKIPPED at install. This repo's own skills use YAML block scalars (`>`); keep that style, and never let a folded line split a hyphenated word. The gate checks lengths and hyphen splits (the vendored editor is exempt from the style check). Marketplace card descriptions must be ≤500 characters.
4. NEVER edit the realtor marketplace (`teamsherrard/claude-agent-os`) from this repo, and never copy realtor-specific wording into these plugins. The two products share lineage but are separate.
5. Interview-style skills collect raw material for the current week only. Do not ask for a later week's deliverable (for example, do not ask for the partner offer in Week 1; branch once for members who already have one).
6. The Lead Magnet plugin is offer-first: build the UVP/offer document, then propose grounded magnet ideas, then write. Never a cookie-cutter default magnet.
7. This repo is public. It never contains client names, pricing, credentials, or the maintainer's private notes. Those live in the private repos `teamsherrard/claude-agent-attraction-knowledge` (HCC references) and `teamsherrard/claude-workspace` (memory, demos).

## Working from a cloud session (claude.ai/code, the Claude app, iPad)
- Plugins cannot be installed or invoked as `/skill-name` in a cloud session. To test a skill's logic, read its `SKILL.md` and follow it step by step as if it had been invoked. The gate script and its Python checks run normally.
- The maintainer's project memory lives in `teamsherrard/claude-workspace` (`memory/MEMORY.md`). Three ways to reach it, in order of preference: (a) if `claude-workspace` is attached to this session as a second repository, read its clone directly (look for a sibling `claude-workspace/` folder next to this repo's clone); (b) if the environment variable `WORKSPACE_TOKEN` is set, fetch a file with the command below; (c) otherwise, when a task depends on decisions recorded there, say so and ask the user to paste the file instead of guessing.
  `GH_TOKEN="$WORKSPACE_TOKEN" gh api repos/teamsherrard/claude-workspace/contents/memory/MEMORY.md -H "Accept: application/vnd.github.raw"`
- Work on a branch and open a PR when a change is risky or untested. Push to `main` only for a release that passed the gate.
- `gh pr` and `gh issue` do not work in cloud sessions (GraphQL is blocked). Use the web UI's Create PR button or `gh api` REST calls.

## Sibling repos (never edit them from here)
- `teamsherrard/claude-agent-os` — the realtor marketplace (public), upstream of the vendored Riverside editor.
- `teamsherrard/claude-agent-attraction-knowledge` — private HCC references for this cohort.
- `teamsherrard/claude-workspace` — private: memory, demos, upload-zip skill banks, brand assets.
