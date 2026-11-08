#!/usr/bin/env python3
"""measure_copy.py — the executable half of the Lead Magnet plugin's quality gates (stdlib only).

Usage:
  python3 measure_copy.py <structured-text.txt> --kind magnet|funnel|email|other

Reads the structured text a skill wrote for render_doc.py and reports, in plain lines:
  words in total and per band (the ALL-CAPS section bands), against the kind's floors;
  the count of `Call to action:` lines (a magnet carries exactly three);
  bracket tokens, raw markdown, banned phrases and leaks (income claims, splits, rev-share figures,
  "join my brokerage", fake scarcity, "check your inbox", the banned word "beats");
  a reading-grade estimate (Flesch-Kincaid) — aim for grade 8 or under: Mike's "say it so a
  fifth-grader follows" rule, measured instead of guessed.
Exit code 0 always: the skill reads the ✗ lines and fixes the text, then re-runs. Nothing is edited here.
"""
import re, sys

FLOORS = {'magnet': (1800, 3500), 'funnel': (900, 1800), 'email': (120, 2400), 'other': (0, 10**9)}
BAND = re.compile(r'^[A-Z0-9][A-Z0-9 ,.&:\'’—–\-()/]{4,}$')
LEAKS = [
    (r'\bbeats\b', 'the banned word "beats"'),
    (r'check your inbox', '"check your inbox" (the guide is an instant download)'),
    (r'\b(spots? left|only \d+ spots|limited spots|countdown|ends (tonight|today|at midnight)|last chance)\b', 'fake scarcity'),
    (r'\bjoin (my|our) brokerage\b', '"join my brokerage"'),
    (r'\b(six|seven)[- ]figure', 'an income claim'),
    (r'\$\s?\d[\d,]*(k|,000)?\s*(a|per|/)\s*(month|year|deal)', 'an income figure'),
    (r'\b(\d{2,3}\s?%|\d{2}/\d{2})\s*(split|commission split)', 'a split figure'),
    (r'\brev(enue)?[- ]share\b[^.\n]{0,40}\b\d+\s?%', 'a rev-share figure'),
    (r'\bcap\b[^.\n]{0,20}\$\s?\d', 'a cap figure'),
]

def syllables(word):
    w = re.sub(r'[^a-z]', '', word.lower())
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', w)
    w = re.sub(r'^y', '', w)
    groups = re.findall(r'[aeiouy]{1,2}', w)
    return max(1, len(groups))

def grade(text):
    sents = max(1, len(re.findall(r'[.!?]+(\s|$)', text)))
    words = re.findall(r"[A-Za-z][A-Za-z'’\-]*", text)
    if not words: return 0.0
    syl = sum(syllables(w) for w in words)
    return round(0.39 * len(words) / sents + 11.8 * syl / len(words) - 15.59, 1)

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    path = sys.argv[1]
    kind = sys.argv[sys.argv.index('--kind') + 1] if '--kind' in sys.argv else 'other'
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')
    body_lines = [l for l in lines if not re.match(r'^[═─]{6,}', l)]
    body = '\n'.join(body_lines)
    words = len(re.findall(r"[A-Za-z][A-Za-z'’\-]*", body))
    lo, hi = FLOORS.get(kind, FLOORS['other'])
    ok = lambda c: '✓' if c else '✗'
    print(f"── measure_copy · {kind} · {path}")
    print(f"  {ok(lo <= words <= hi)} words: {words} (floor {lo}, ceiling {hi})")
    # per band
    cur, counts, order = None, {}, []
    for l in body_lines:
        s = l.strip()
        if BAND.match(s) and len(s.split()) <= 12 and not s.startswith('|'):
            cur = s; order.append(s); counts[cur] = 0; continue
        if cur: counts[cur] += len(re.findall(r"[A-Za-z][A-Za-z'’\-]*", l))
    for b in order: print(f"    · {b[:48]:<48} {counts[b]} words")
    ctas = len(re.findall(r'^Call to action:', body, re.M))
    if kind == 'magnet': print(f"  {ok(ctas == 3)} calls to action: {ctas} (exactly three)")
    brackets = re.findall(r'\[[^\]\n]{1,60}\]', body)
    print(f"  {ok(not brackets)} bracket tokens: {len(brackets)}" + (f" — e.g. {brackets[0]}" if brackets else ''))
    raw = re.findall(r'(^#{1,3} |\*\*|`)', body, re.M)
    print(f"  {ok(not raw)} raw markdown in the body: {len(raw)}")
    caps = [l for l in body_lines if len(l.split()) > 12 and l == l.upper() and re.search(r'[A-Z]', l)]
    print(f"  {ok(not caps)} copy written in capitals: {len(caps)}")
    hits = []
    for pat, label in LEAKS:
        for m in re.finditer(pat, body, re.I): hits.append((label, body[max(0, m.start()-30):m.end()+30].replace('\n', ' ')))
    print(f"  {ok(not hits)} leaks and banned phrases: {len(hits)}")
    for label, ctx in hits[:12]: print(f"    ✗ {label}: …{ctx}…")
    g = grade(body)
    print(f"  {'✓' if g <= 8 else '!'} reading grade (Flesch-Kincaid): {g} (aim for 8 or under; a plain rewrite of the longest sentences usually does it)")
    print("  read by hand: the hook test · one idea per page · real proof with consent · the member's voice · nothing invented")

if __name__ == '__main__':
    main()
