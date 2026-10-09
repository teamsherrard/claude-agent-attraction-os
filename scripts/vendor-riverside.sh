#!/usr/bin/env bash
# The AI Editing Studio (Riverside) is ONE plugin shared by both marketplaces. Its source of truth is the realtor repo.
# This script re-vendors it here and re-applies the Brain-home patch (house-rules.md rule + `<Brain home>` paths).
# Run after any Riverside release in the realtor repo. Back-port the Brain-home patch there to make this a plain copy.
set -euo pipefail
SRC="${1:-/Users/riyabidani/Downloads/realtor-ai-brain/plugins/realtor-riverside-editor}"
cd "$(dirname "$0")/.."
rm -rf plugins/realtor-riverside-editor && cp -R "$SRC" plugins/realtor-riverside-editor
echo "Vendored from $SRC — now re-apply the Brain-home patch if the source does not carry it yet (see git log for the patch commit)."

# claude.ai stores a skill description cut at 1024 characters and Cowork warns on every sync. The realtor source carries
# two that are longer (studio-navigator 1455, studio-publish 1312); this marketplace keeps them trimmed (CHANGELOG 0.3.1).
# Re-apply the trims (git log for the commit) for anything listed here, then run scripts/check-release.sh.
python3 - <<'PYCHK'
import glob,re
for f in sorted(glob.glob("plugins/realtor-riverside-editor/skills/*/SKILL.md")):
    fm=re.match(r'^---\n(.*?)\n---',open(f,encoding="utf-8").read(),re.S)
    m=re.search(r'^description:\s*>?\s*\n?((?:.*\n?)*?)(?=^[a-z_-]+:|\Z)',fm.group(1),re.M|re.S) if fm else None
    n=len(" ".join((m.group(1) if m else "").split()))
    if n>1024: print(f"  TRIM NEEDED (>1024): {f} ({n} chars)")
PYCHK
