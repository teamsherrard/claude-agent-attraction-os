# SessionStart hook — the Brain's global awareness

Global brain-awareness for the Agent Attraction Brain. SessionStart command output is injected into session context: if a local attraction brain exists it loads the index; otherwise it instructs Claude to pull the brain from the member's cloud workspace via attraction-brain-sync. Distinct from the realtor Brain's hook (different folder, different marker) so both Brains can coexist on one machine. Excluded from the zip-upload build (zip validation rejects hooks); verify live via the GitHub-marketplace install. Cloud PUSH after writes is handled by skills per the Brain Contract, not by a hook.

`hooks.json` carries ONLY the `hooks` key: claude.ai validates plugin hooks against a strict schema and drops any other top-level field (such as a `$comment` note) with a sync warning. Keep notes here, not in the JSON.
