#!/usr/bin/env bash
# The AI Editing Studio (Riverside) is ONE plugin shared by both marketplaces. Its source of truth is the realtor repo.
# This script re-vendors it here and re-applies the Brain-home patch (house-rules.md rule + `<Brain home>` paths).
# Run after any Riverside release in the realtor repo. Back-port the Brain-home patch there to make this a plain copy.
set -euo pipefail
SRC="${1:-/Users/riyabidani/Downloads/realtor-ai-brain/plugins/realtor-riverside-editor}"
cd "$(dirname "$0")/.."
rm -rf plugins/realtor-riverside-editor && cp -R "$SRC" plugins/realtor-riverside-editor
echo "Vendored from $SRC — now re-apply the Brain-home patch if the source does not carry it yet (see git log for the patch commit)."
