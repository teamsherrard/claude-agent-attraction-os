#!/usr/bin/env bash
# Pre-release gate. Run BEFORE committing a release.
#
# Carried from the realtor marketplace. Catches the failure that shipped a plugin broken there: a version bump and a
# changelog entry were committed while the actual skill files stayed unstaged, so
# the marketplace served a plugin whose orchestrator pointed at skills that
# didn't exist and whose advertised deliverables were missing.
#
# Usage: scripts/check-release.sh [plugin-name]
#   No argument  -> checks every plugin (full marketplace release).
#   Plugin name  -> scopes the "is it staged?" and changelog checks to that plugin,
#                   so a single-plugin release is not blocked by other work in flight.
set -uo pipefail
cd "$(dirname "$0")/.."
SCOPE="${1:-}"
if [ -n "$SCOPE" ]; then
  [ -d "plugins/$SCOPE" ] || { echo "No such plugin: $SCOPE"; exit 2; }
  PATHSPEC="plugins/$SCOPE"
  echo "Scoped to: $SCOPE"
else
  PATHSPEC="plugins/"
  echo "Scope: all plugins"
fi
echo
FAIL=0
say() { printf '%s\n' "$*"; }
bad() { printf '  ✗ %s\n' "$*"; FAIL=1; }
ok()  { printf '  ✓ %s\n' "$*"; }

say "── 1. plugin.json version == marketplace registry version"
python3 - <<'PY' || FAIL=1
import json,sys,glob,os
reg={p["name"]:p["version"] for p in json.load(open(".claude-plugin/marketplace.json"))["plugins"]}
bad=False
for f in sorted(glob.glob("plugins/*/.claude-plugin/plugin.json")):
    d=json.load(open(f)); n=d["name"]
    if n not in reg:
        print(f"  ✗ {n}: built but NOT registered in marketplace.json"); bad=True
    elif reg[n]!=d["version"]:
        print(f"  ✗ {n}: plugin.json {d['version']} != registry {reg[n]}"); bad=True
    else:
        print(f"  ✓ {n} {d['version']}")
sys.exit(1 if bad else 0)
PY

say ""
say "── 2. no unstaged/untracked files inside a plugin being released"
DIRTY=$(git status --porcelain "$PATHSPEC" | grep -E '^( M|\?\?|_M| D)' || true)
if [ -n "$DIRTY" ]; then
  bad "plugin files not staged — these would NOT ship:"
  printf '%s\n' "$DIRTY" | sed 's/^/      /'
else
  ok "every plugin file is committed or staged"
fi

say ""
say "── 3. every skill a SKILL.md hands off to actually exists"
python3 - <<'PY' || FAIL=1
import glob,os,re,sys
bad=False
ALL={os.path.basename(d.rstrip("/")) for d in glob.glob("plugins/*/skills/*/")}
for plug in sorted(glob.glob("plugins/*/")):
    have={os.path.basename(d.rstrip("/")) for d in glob.glob(plug+"skills/*/")}
    if not have: continue
    for f in glob.glob(plug+"skills/*/SKILL.md"):
        txt=open(f).read()
        for ref in set(re.findall(r'\*\*((?:Support|Admin|Studio)\s+[A-Z][a-zA-Z]+)\*\*',txt)):
            w=ref.split()
            slug=f"{w[0].lower()}-{w[1].lower()}"
            if not slug.startswith(("support-","admin-","studio-")): continue
            # a handoff may legitimately name a skill in ANOTHER plugin (documented boundary)
            if slug in have or slug in ALL:
                continue
            print(f"  ✗ {f}: hands off to '{ref}' -> {slug} which exists in no plugin"); bad=True
if not bad: print("  ✓ no dangling skill handoffs")
sys.exit(1 if bad else 0)
PY

say ""
say "── 4. \${CLAUDE_PLUGIN_ROOT} references resolve"
python3 - <<'PY' || FAIL=1
import glob,os,re,sys
bad=False
for plug in sorted(glob.glob("plugins/*/")):
    for f in glob.glob(plug+"**/*.md",recursive=True):
        for ref in re.findall(r'\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)',open(f).read()):
            if not os.path.exists(os.path.join(plug,ref)):
                print(f"  ✗ {f}: missing {ref}"); bad=True
if not bad: print("  ✓ all plugin-root references resolve")
sys.exit(1 if bad else 0)
PY

say ""
say "── 5. shared files that must stay identical across plugins"
python3 - <<'PY' || FAIL=1
import glob,hashlib,collections,sys
bad=False
for name in ("render_doc.py","notion-board-spec.md","how-we-speak.md","ask-once-default.md","connectors.md","composio-data-engine.md"):
    paths=sorted(glob.glob(f"plugins/*/shared/{name}"))
    if len(paths)<2: continue
    by=collections.defaultdict(list)
    for p in paths: by[hashlib.md5(open(p,'rb').read()).hexdigest()].append(p)
    if len(by)>1:
        print(f"  ✗ {name} has drifted across plugins:")
        for h,ps in by.items():
            for p in ps: print(f"      {h[:8]}  {p}")
        bad=True
    else: print(f"  ✓ {name} identical across {len(paths)} plugins")
sys.exit(1 if bad else 0)
PY


say ""
say "── 8. SKILL.md descriptions ≤ 1024 chars and block-scalar; names match directories"
python3 - <<'PY2' || FAIL=1
import glob,os,re,sys,yaml
bad=False
for f in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
    txt=open(f,encoding="utf-8").read()
    m=re.match(r'^---\n(.*?)\n---',txt,re.S)
    if not m: print(f"  ✗ {f}: no frontmatter"); bad=True; continue
    d=os.path.basename(os.path.dirname(f))
    vendored = "/realtor-riverside-editor/" in f
    try: fm=yaml.safe_load(m.group(1))
    except Exception as e:
        if vendored:
            nm=re.search(r'^name:\s*(\S+)',m.group(1),re.M); ds=re.search(r'^description:\s*>?\s*\n?((?:.*\n?)*)',m.group(1),re.M)
            fm={"name":nm.group(1) if nm else None,"description":(ds.group(1) if ds else "")}
        else:
            print(f"  ✗ {f}: frontmatter does not parse ({e})"); bad=True; continue
    if fm.get("name")!=d: print(f"  ✗ {f}: name '{fm.get('name')}' != dir '{d}'"); bad=True
    desc=fm.get("description","") or ""
    if len(desc)>1024: print(f"  ✗ {f}: description {len(desc)} chars (>1024)"); bad=True
    if not vendored and not re.search(r'^description:\s*>',m.group(1),re.M): print(f"  ✗ {f}: description is not a folded block scalar (description: >)"); bad=True
if not bad: print("  ✓ every SKILL.md: name==dir, description ≤1024, block scalar")
sys.exit(1 if bad else 0)
PY2

say ""
say "── 9. no realtor-side paths, names, or retired engines leak into this OS"
python3 - <<'PY2' || FAIL=1
import glob,re,sys
pats={"~/realtor-brain":r"~/realtor-brain(?!/\S*\s*(?:is|\(|—|-|:|,)?\s*(?:a different|read-only|the realtor))","Social Agent OS":r"Social Agent OS","_workspace.md (realtor marker)":r"(?<![a-z-])_workspace\.md","realtor-brain-sync":r"realtor-brain-sync","Descript":r"\bDescript\b","listing-launch / market-system":r"realtor-listing-launch|realtor-market-system"}
allow=re.compile(r"realtor brain bridge|read-only|never|not this|different system|a separate|do not|don't|legacy|the realtor plugin|coexist|side by side|retired|REMOVED",re.I)
bad=[]
for f in glob.glob("plugins/**/*.md",recursive=True)+glob.glob("plugins/**/*.json",recursive=True):
    for n,l in enumerate(open(f,encoding="utf-8"),1):
        for name,pat in pats.items():
            if re.search(pat,l) and not allow.search(l): bad.append(f"{f}:{n}: [{name}] {l.strip()[:100]}")
if bad:
    print("  ✗ realtor-side references found (allowed only in lines that mark them as the OTHER system):")
    for b in bad[:40]: print("      "+b)
    sys.exit(1)
print("  ✓ no realtor paths, markers, or retired engines leak")
PY2

say ""
say "── 10. trigger phrases do not collide with the realtor marketplace"
python3 - <<'PY2' || FAIL=1
import glob,re,sys,os
REALTOR="/Users/riyabidani/Downloads/realtor-ai-brain/plugins"
if not os.path.isdir(REALTOR): print("  · realtor marketplace not on this machine; skipped"); sys.exit(0)
def triggers(f):
    txt=open(f,encoding="utf-8").read()
    m=re.match(r'^---\n(.*?)\n---',txt,re.S)
    if not m: return set()
    return {t.strip().lower() for t in re.findall(r'"([^"]{4,60})"',m.group(1))}
theirs={}
for f in glob.glob(REALTOR+"/*/skills/*/SKILL.md"):
    for t in triggers(f): theirs.setdefault(t,f.split("/plugins/")[1])
bad=[]
for f in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
    for t in triggers(f):
        if t in theirs: bad.append(f"{f}: \"{t}\" also triggers realtor {theirs[t]}")
if bad:
    print("  ✗ trigger phrases shared with the realtor marketplace (reword with 'attraction' / 'agent attraction' / 'my organization'):")
    for b in bad[:60]: print("      "+b)
    sys.exit(1)
print("  ✓ no trigger phrase collides with the realtor marketplace")
PY2


say ""
say "── 11. every plugin carries shared/brain-contract.md and names its scheduled-task consent rule"
python3 - <<'PY2' || FAIL=1
import glob,os,re,sys
bad=False
for plug in sorted(glob.glob("plugins/*/")):
    name=os.path.basename(plug.rstrip("/"))
    if name=="realtor-riverside-editor":  # vendored as-is; carries house-rules.md Brain-home rule instead
        if not os.path.exists(plug+"shared/house-rules.md") or "Brain-home rule" not in open(plug+"shared/house-rules.md").read():
            print(f"  ✗ {name}: vendored Studio is missing the Brain-home rule in shared/house-rules.md"); bad=True
        continue
    if not os.path.exists(plug+"shared/brain-contract.md"):
        print(f"  ✗ {name}: no shared/brain-contract.md"); bad=True
    if name=="maa-claude-support": continue  # read-only desk: it provisions no tasks, only diagnoses them
    for f in glob.glob(plug+"skills/*/SKILL.md"):
        t=open(f,encoding="utf-8").read()
        if re.search(r"scheduled[- ]task|create_scheduled_task|scheduled agent",t,re.I) and not re.search(r"explicit (yes|consent)|with (the member's|their) (yes|consent|permission)|never (silently|without asking)|ask(s)? (before|first)|consent",t,re.I):
            print(f"  ✗ {f}: mentions a scheduled task but no consent rule"); bad=True
if not bad: print("  ✓ brain-contract.md present everywhere; scheduled tasks are consent-gated")
sys.exit(1 if bad else 0)
PY2

say ""
say "── 12. the content engines keep the Composio data engine; nothing routes to retired or removed systems"
python3 - <<'PY2' || FAIL=1
import glob,os,re,sys
bad=False
for plug in ("attraction-shortform-system","attraction-youtube-system"):
    if not os.path.exists(f"plugins/{plug}/shared/composio-data-engine.md"):
        print(f"  ✗ {plug}: shared/composio-data-engine.md missing (Composio is a required connector)"); bad=True
    hits=[f for f in glob.glob(f"plugins/{plug}/skills/*analytics*/SKILL.md") if "composio" in open(f,encoding="utf-8").read().lower()]
    if not hits: print(f"  ✗ {plug}: analytics skill does not reference the Composio data engine"); bad=True
pat=re.compile(r"\b(cs-(clone-setup|clone-styles|clone-reel|thumbnail-employee|thumbnail-score|headshots|broll|ad-creatives|product-animation|setup)|team-(onboarding|plug-in|duplication-kit|teach-to-attract|recognition|win-wall|culture-audit|community|survey|exit-interview|1on1)|org-analysis|realtor-ai-editor|edit-longform|edit-shortform|editor-navigator)\b")
allow=re.compile(r"removed|parked|not (in|part of) this|retired|never",re.I)
for f in glob.glob("plugins/**/*.md",recursive=True):
    if "realtor-riverside-editor" in f: continue
    for n,l in enumerate(open(f,encoding="utf-8"),1):
        if pat.search(l) and not allow.search(l): print(f"  ✗ {f}:{n}: routes to a removed/retired system: {l.strip()[:90]}"); bad=True
if not bad: print("  ✓ Composio kept in both content engines; no routes to removed systems")
sys.exit(1 if bad else 0)
PY2


say ""
say "── 13. Design Studio skill set builds clean (design-studio/_build/build.sh)"
if [ -x design-studio/_build/build.sh ]; then
  if bash design-studio/_build/build.sh >/tmp/ds-build.log 2>&1; then ok "design-studio: build.sh green ($(ls design-studio/_dist | wc -l | tr -d ' ') upload files)"; else bad "design-studio/_build/build.sh failed:"; tail -20 /tmp/ds-build.log | sed 's/^/      /'; fi
else
  say "  · no design-studio build script; skipped"
fi

say ""
say "── 6. top changelog entry names files that are actually committed/staged"
python3 - <<'PY' || FAIL=1
import re,subprocess,sys,os
cl=open("CHANGELOG.md").read()
m=re.search(r'^## \[([^\]]+)\].*?(?=^## \[)',cl,re.M|re.S)
if not m: print("  ✗ could not parse the top changelog entry"); sys.exit(1)
ver,body=m.group(1),m.group(0)
names=set(re.findall(r'`([a-z0-9][a-z0-9-]*(?:\.md|\.py|\.sh)?)`',body))
tracked=set(subprocess.run(["git","ls-files","plugins/"],capture_output=True,text=True).stdout.split())
staged=set(subprocess.run(["git","diff","--cached","--name-only"],capture_output=True,text=True).stdout.split())
known={os.path.basename(p) for p in tracked|staged}
known|={os.path.basename(os.path.dirname(p)) for p in tracked|staged}
# The changelog names skills by their SHORT name (brain-setup) while the directory
# carries the plugin prefix (realtor-brain-setup). Accept a suffix match so the repo's
# own long-standing naming convention isn't reported as a missing file.
def seen(n):
    return n in known or any(k.endswith("-"+n) or k == n for k in known)
missing=[n for n in names if ("-" in n or n.endswith((".md",".py"))) and not seen(n)
         and not n.endswith(("/",)) and len(n)>4]
if missing:
    print(f"  ✗ v{ver} names files/skills that are neither tracked nor staged:")
    for n in sorted(missing): print(f"      {n}")
    print("      (this is exactly how v0.4.1 shipped broken)")
    sys.exit(1)
print(f"  ✓ v{ver}: every named file is tracked or staged")
PY

say ""
if [ "$FAIL" -ne 0 ]; then say "RELEASE BLOCKED — fix the ✗ items above."; exit 1; fi
say "RELEASE OK — safe to commit."
