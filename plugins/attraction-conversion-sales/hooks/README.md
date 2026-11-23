# Hooks — Conversion & Sales

`hooks.json` carries ONE hook: on every message the member sends (`UserPromptSubmit`), a shell `grep` over the message looks for Stacy / sales trainer / train me / drill me / role-play and, when found, prints a routing note telling Claude that Stacy is this plugin's `stacy-sales-trainer` skill — not a Notion agent, not a person, not anything outside the plugin.

Why: on 2026-11-22 the owner's first "Launch Stacy, my sales trainer" ran before the trigger existed; Claude wrote a project-memory note guessing Stacy might be a Notion agent, and every later chat read that note first and went to Notion instead of the skill. Skill descriptions alone could not win against the memory. The hook fires before the model decides, so it does.

Rules: only the `hooks` key at the top level (claude.ai drops any other and warns); POSIX `sh` + `grep` only (no Python — a fresh Mac prompts for developer tools); the note is for Claude, never shown to the member as-is.
