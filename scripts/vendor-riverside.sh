#!/usr/bin/env bash
# The AI Editing Studio is ONE plugin shared by both marketplaces. Its source of truth is the realtor repo.
# This script re-vendors it here and re-applies the Brain-home patch (house-rules.md rule + `<Brain home>` paths).
# Run after any Riverside release in the realtor repo. Back-port the Brain-home patch there to make this a plain copy.
#
# Downstream patches re-applied after each vendor:
#   1. Brain-home patch — shared/house-rules.md "The Brain-home rule" + the sync-skill wording there and in studio-setup, + every
#      `~/realtor-brain` → `<Brain home>` in the .md and .json files ONLY (resolves ~/attraction-brain/ first). NEVER touch the
#      .py scripts: since upstream 0.7.1 they resolve the Brain folder at run time, so they are a plain copy.
#   3. skills/studio-publish/SKILL.md — the description's tail "; usually reached through studio-navigator" is dropped (≤ 1,024).
#   2. .claude-plugin/plugin.json — description trimmed to ≤ 1,000 characters (claude.ai refuses plugin updates above 1,024) and the
#      version bumped one patch above the realtor source (0.5.0 → 0.5.1), equal to the marketplace registry entry.
#   4. Riverside only — run `python3 scripts/strip-edits-engine.py` after vendoring (the call at the end of this script does it);
#      the Edits engine (Instagram Edits for Mac, driven from the Code tab) is parked in docs/parked/edits-engine-2026-11-23/
#      (owner, 2026-11-23: "complicated, probably won't work for most people"). The script deletes the shared/edits-*.md
#      files and scripts/edits/, sets the config example to Riverside only, removes every member-facing Edits-engine
#      passage by asserted exact-string replacement, rewrites plugin.json (description, keywords, version 0.7.5), and exits 1
#      the moment an anchor is missing, so a re-vendor that changed the upstream text is caught, never half-stripped.
#      Members FILMING on their phone in the Edits app (the teleprompter) is a different thing and stays. To ship the
#      engine again, drop this patch (see the parked folder's README).
set -euo pipefail
SRC="${1:-/Users/riyabidani/Downloads/realtor-ai-brain/plugins/realtor-ai-editing-studio}"
cd "$(dirname "$0")/.."
rm -rf plugins/realtor-ai-editing-studio && cp -R "$SRC" plugins/realtor-ai-editing-studio
echo "Vendored from $SRC — now re-apply the Brain-home patch if the source does not carry it yet (see git log for the patch commit)."

# claude.ai stores a skill description cut at 1024 characters and Cowork warns on every sync. The realtor source carries
# two that are longer (studio-navigator 1455, studio-publish 1312); this marketplace keeps them trimmed (CHANGELOG 0.3.1).
# Re-apply the trims (git log for the commit) for anything listed here, then run scripts/check-release.sh.
python3 - <<'PYCHK'
import glob,re
for f in sorted(glob.glob("plugins/realtor-ai-editing-studio/skills/*/SKILL.md")):
    fm=re.match(r'^---\n(.*?)\n---',open(f,encoding="utf-8").read(),re.S)
    m=re.search(r'^description:\s*>?\s*\n?((?:.*\n?)*?)(?=^[a-z_-]+:|\Z)',fm.group(1),re.M|re.S) if fm else None
    n=len(" ".join((m.group(1) if m else "").split()))
    if n>1024: print(f"  TRIM NEEDED (>1024): {f} ({n} chars)")
PYCHK

# Patch 4 — Riverside only (owner, 2026-11-23). Asserted exact-string strip; exits 1 on a missing anchor.
python3 scripts/strip-edits-engine.py
