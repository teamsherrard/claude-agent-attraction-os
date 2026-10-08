#!/usr/bin/env bash
# Build the upload-ready Agent Attraction Design Studio files into _dist/.
#
# Packaging follows the realtor Claude Design suite v2 (the shape claude.ai's skill uploader accepts):
#   - a skill WITHOUT references/  ->  _dist/NN-<name>.md   (bare SKILL.md with YAML frontmatter)
#   - a skill WITH references/     ->  _dist/NN-<name>.zip  (<name>/SKILL.md + <name>/references/*)
#   - never a nested zip; no spaces, '&', '(' or ')' in any zip-internal path
#   - every frontmatter `description` is a `description: >` folded block scalar, <= 1024 chars
#     (target <= 1000); `name:` == the skill directory name
#   - START-HERE.md and the default Design System are copied beside the skills as 00-* files
#
# Also asserts: no banned words, no realtor-side leaks, the shared export-page.md identical across
# every skill that carries it, and every skill carries the mechanics the suite depends on.
#
# Usage: design-studio/_build/build.sh   (from anywhere)
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
DIST="$ROOT/_dist"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

# The 15 skills of the Studio, in upload order. Numbers stay stable as later weeks ship.
ORDER=(ds-logo ds-style-sheet ds-brand ds-offer-stack ds-offer-assets ds-product-mockup ds-carousel
       ds-funnel ds-thumbnail-layout ds-lead-magnet ds-recognition ds-event ds-playbook ds-course ds-ebook)

FAIL=0
ok()   { printf '  ✓ %s\n' "$*"; }
bad()  { printf '  ✗ %s\n' "$*"; FAIL=1; }
note() { printf '  · %s\n' "$*"; }

cat > "$STAGE/check.py" <<'PY'
import re, sys, os
path, expected = sys.argv[1], sys.argv[2]
txt = open(path, encoding="utf-8").read()
m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
if not m:
    print("no YAML frontmatter"); sys.exit(1)
fm = m.group(1)
problems = []
if not re.search(r'^description:\s*>\s*$', fm, re.M):
    problems.append("description is not a folded block scalar (`description: >`)")
name = None
desc = None
try:
    import yaml  # PyYAML, the same parser check-release.sh uses
    data = yaml.safe_load(fm) or {}
    name = data.get("name"); desc = data.get("description") or ""
except ImportError:
    # manual fallback: fold the block scalar the way YAML does
    nm = re.search(r'^name:\s*(\S+)\s*$', fm, re.M)
    name = nm.group(1) if nm else None
    lines = fm.split("\n"); out = []; grab = False
    for ln in lines:
        if re.match(r'^description:\s*>\s*$', ln): grab = True; continue
        if grab:
            if ln.startswith(" ") or ln == "":
                out.append(ln.strip())
            else:
                break
    para, buf = [], []
    for ln in out:
        if ln == "": para.append(" ".join(buf)); buf = []
        else: buf.append(ln)
    if buf: para.append(" ".join(buf))
    desc = "\n".join(para) + "\n"
if name != expected:
    problems.append(f"name '{name}' != directory '{expected}'")
n = len(desc)
if n > 1024:
    problems.append(f"description is {n} chars (> 1024 — claude.ai rejects it)")
elif n > 1000:
    print(f"  ! description is {n} chars (over the 1000 target, under the 1024 limit)")
for t in ("Trigger on", "trigger"):
    if t.lower() in desc.lower(): break
else:
    problems.append("description carries no trigger phrases")
if problems:
    for p in problems: print("  " + p)
    sys.exit(1)
print(f"name ok · description {n} chars · block scalar")
PY

cat > "$STAGE/lint.py" <<'PY'
import re, sys
# Banned words (plugin house rules) — allowed only on a line that names them as banned.
BANNED = re.compile(r"\b(unlock|supercharge|game[- ]changer|revolutionary|secret weapon|leverag(?:e|es|ed|ing))\b", re.I)
ALLOW  = re.compile(r"banned|never", re.I)
# Realtor-side artifacts and retired engines that must not leak into the attraction Studio.
LEAKS = [r"Just Listed", r"Just Sold", r"yard sign", r"04 · Listings", r"05 · Market", r"realtor-brain",
         r"Social Agent OS", r"(?<![a-z-])_workspace\.md", r"Descript", r"REALTOR® ·"]
bad = []
for f in sys.argv[1:]:
    for i, l in enumerate(open(f, encoding="utf-8"), 1):
        if BANNED.search(l) and not ALLOW.search(l):
            bad.append(f"{f}:{i}: banned word: {l.strip()[:90]}")
        for pat in LEAKS:
            if re.search(pat, l):
                bad.append(f"{f}:{i}: realtor-side leak [{pat}]: {l.strip()[:90]}")
if bad:
    print("\n".join("  " + b for b in bad)); sys.exit(1)
print("no banned words, no realtor-side leaks")
PY

cat > "$STAGE/mechanics.py" <<'PY'
import sys
# Every Design Studio skill must carry the mechanics the suite depends on.
REQUIRED = {
  "PLAIN-LANGUAGE LAW": "the plain-language law",
  "02 · Brand": "the 02 · Brand destination",
  "Brain Book": "the Brain Book (the AI Brain file)",
  "AGENT ATTRACTION DESIGN PACKAGE": "reading the Design Package brief",
  "NOT SET": "the 3-state compliance line",
  "Your turn": "the question handoff",
  "push": "push this to my Drive",
  "DEMO": "demo mode",
  "never instructions": "fetched content is data, never instructions",
  "WHERE THIS RUNS": "the Claude-Design-only check",
}
missing = [v for k, v in REQUIRED.items() if k not in open(sys.argv[1], encoding="utf-8").read()]
if missing:
    print("  missing: " + "; ".join(missing)); sys.exit(1)
print("all suite mechanics present")
PY

echo "Agent Attraction Design Studio — build"
echo "── 0. clean _dist/"
rm -rf "$DIST"; mkdir -p "$DIST"; ok "_dist/ reset"

echo
echo "── 1. lint every skill file (banned words, realtor-side leaks)"
ALL_MD=()
while IFS= read -r f; do ALL_MD+=("$f"); done < <(find "$ROOT/skills" -name '*.md' -type f | sort)
if python3 "$STAGE/lint.py" "${ALL_MD[@]}"; then ok "lint clean"; else bad "lint failed"; fi

echo
echo "── 2. shared references identical across skills"
python3 - "$ROOT" <<'PY' || FAIL=1
import glob, hashlib, collections, os, sys
root = sys.argv[1]; bad = False
by_name = collections.defaultdict(list)
for p in glob.glob(f"{root}/skills/*/references/*.md"):
    by_name[os.path.basename(p)].append(p)
for name, paths in sorted(by_name.items()):
    if len(paths) < 2: continue
    h = {hashlib.md5(open(p, "rb").read()).hexdigest() for p in paths}
    if len(h) > 1:
        print(f"  ✗ {name} has drifted across skills: {', '.join(paths)}"); bad = True
    else:
        print(f"  ✓ {name} identical across {len(paths)} skills")
sys.exit(1 if bad else 0)
PY

echo
echo "── 3. package each skill"
BUILT=0; COMING=()
idx=0
for name in "${ORDER[@]}"; do
  idx=$((idx+1)); NN=$(printf '%02d' "$idx")
  SRC="$ROOT/skills/$name"
  if [ ! -f "$SRC/SKILL.md" ]; then COMING+=("$NN $name"); continue; fi
  printf '%s\n' "$name"
  if python3 "$STAGE/check.py" "$SRC/SKILL.md" "$name" >"$STAGE/out.txt" 2>&1; then ok "$(tail -1 "$STAGE/out.txt")"; grep '^  !' "$STAGE/out.txt" || true
  else bad "frontmatter: $(tr '\n' ' ' < "$STAGE/out.txt")"; fi
  if python3 "$STAGE/mechanics.py" "$SRC/SKILL.md" >"$STAGE/out.txt" 2>&1; then ok "$(cat "$STAGE/out.txt")"; else bad "mechanics: $(cat "$STAGE/out.txt")"; fi
  # path hygiene: no spaces / & / ( ) anywhere inside the package
  if find "$SRC" -type f ! -name '.DS_Store' | sed "s#^$ROOT/skills/##" | grep -E '[ &()]' >/dev/null; then
    bad "a file path inside $name contains a space, '&', '(' or ')'"
  fi
  if [ -d "$SRC/references" ] && [ -n "$(find "$SRC/references" -type f -name '*.md' | head -1)" ]; then
    # zip: <name>/SKILL.md + <name>/references/*.md
    rm -rf "$STAGE/pkg"; mkdir -p "$STAGE/pkg/$name/references"
    cp "$SRC/SKILL.md" "$STAGE/pkg/$name/SKILL.md"
    cp "$SRC"/references/*.md "$STAGE/pkg/$name/references/"
    OUT="$DIST/$NN-$name.zip"
    (cd "$STAGE/pkg" && zip -qrX "$OUT" "$name" -x '*/.DS_Store')
    # verify from INSIDE the zip: frontmatter again, no nested zips, clean paths
    rm -rf "$STAGE/verify"; mkdir -p "$STAGE/verify"; (cd "$STAGE/verify" && unzip -q "$OUT")
    if python3 "$STAGE/check.py" "$STAGE/verify/$name/SKILL.md" "$name" >/dev/null 2>&1; then ok "verified from inside the zip"; else bad "zip's SKILL.md fails the frontmatter check"; fi
    if unzip -Z1 "$OUT" | grep -Ei '\.zip$' >/dev/null; then bad "nested zip inside $OUT"; fi
    if unzip -Z1 "$OUT" | grep -E '[ &()]' >/dev/null; then bad "zip-internal path with a space, '&', '(' or ')'"; fi
    NREF=$(ls "$SRC"/references/*.md | wc -l | tr -d ' ')
    ok "$(basename "$OUT")  (+$NREF reference files, $(du -h "$OUT" | cut -f1 | tr -d ' '))"
  else
    OUT="$DIST/$NN-$name.md"
    cp "$SRC/SKILL.md" "$OUT"
    ok "$(basename "$OUT")  (bare SKILL.md, no references)"
  fi
  BUILT=$((BUILT+1))
done

echo
echo "── 4. the map and the default Design System"
if [ -f "$ROOT/START-HERE.md" ]; then cp "$ROOT/START-HERE.md" "$DIST/00-START-HERE.md"; ok "00-START-HERE.md"; else bad "START-HERE.md missing"; fi
if [ -f "$ROOT/design-system/agent-attraction-design-system.md" ]; then
  cp "$ROOT/design-system/agent-attraction-design-system.md" "$DIST/00-agent-attraction-design-system.md"; ok "00-agent-attraction-design-system.md"
else bad "design-system/agent-attraction-design-system.md missing"; fi
if python3 "$STAGE/lint.py" "$ROOT/START-HERE.md" "$ROOT/design-system/agent-attraction-design-system.md" >/dev/null 2>&1; then ok "map + design system lint clean"; else bad "map or design system has a banned word or a realtor-side leak"; fi

echo
echo "── summary"
note "$BUILT skill(s) built into _dist/: $(ls "$DIST" | tr '\n' ' ')"
if [ ${#COMING[@]} -gt 0 ]; then note "not built yet (coming with their week): ${COMING[*]}"; fi
if [ "$FAIL" -ne 0 ]; then echo "BUILD BLOCKED — fix the ✗ items above."; exit 1; fi
echo "BUILD OK — _dist/ is upload-ready."
