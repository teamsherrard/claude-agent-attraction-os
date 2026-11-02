#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
measure_book.py — the executable half of the Agent Attraction Brain Book's verification gate.

Usage:
  python3 measure_book.py "<book.docx>" [--json] [--demo | --real]

Extracts the rendered .docx back out in document order (python-docx — the renderer's own dependency; this
script never installs anything) and prints, per section: words against the spec's TARGET and MAXIMUM, the
tables, the callouts and the page estimate; then every gate check it can run by machine
(shared/brain-book-spec.md → "The verification gate": checks 1–8, 11–13 and the demo checks). The checks it
cannot run — the grounding audit, the cardinal rules, derived-never-chosen, voice fidelity, the swap test —
are read by hand. Exit code 1 on any FAIL, 0 otherwise. Demo mode is detected from the cover line unless
forced with --demo / --real.

The page estimate, two ways, the gate takes the larger: (a) the renderer's layout — 11pt Arial body at 1.2
line spacing (~92 characters a line over 6.5in), 10pt table text, a 72pt section header, the forced page
break before every band — against a 655pt usable page; (b) words ÷ 380 per section. Plus the cover and the
contents page. FAIL above 15 pages, WARN above 13.
"""
import sys, re, json, math, zipfile, argparse

try:
    from docx import Document
    from docx.oxml.ns import qn
except ImportError:
    sys.stderr.write(
        "RENDERER-UNAVAILABLE: python-docx is not installed in this environment. DO NOT install it, do not run\n"
        "pip, do not retry — run the gate by hand from the spec's checklist instead.\n")
    sys.exit(2)

TAG = "(illustrative — demo)"
DEMO_COVER = "Demo document — illustrative data, not researched."
BAND_RE = re.compile(r'^(SECTION \d+|CHAPTER \d+|PART [IVXLC]+)$')
EXPECTED = ["WHO YOU ARE", "YOUR STORY", "YOUR BROKERAGE STORY", "YOUR UNIQUE APPROACH", "YOUR PROOF",
            "WHO YOUR STORY SPEAKS TO", "YOUR NUMBERS", "YOUR VOICE", "WHAT'S NEXT"]
# section number → (target, MAXIMUM) in words — the spec's section table
LIMITS = {1: (80, 200), 2: (250, 400), 3: (150, 300), 4: (200, 400), 5: (150, 300),
          6: (150, 300), 7: (60, 150), 8: (150, 320), 9: (40, 150)}
BOOK_TARGET, BOOK_MAX = 1500, 3500
DEMO_RANGE = (2000, 2600)
PAGE_WARN, PAGE_FAIL = 13, 15
USABLE_PT = 655.0

JARGON = [  # (label, regex) — a hit anywhere in the Book's text is a FAIL
    ("downline", r'\bdownlines?\b'),
    ("three-way call", r'\b(?:three|3)[- ]way\b'),
    ("unique value proposition / UVP", r'unique value proposition|\bUVPs?\b'),
    ("funnel", r'\bfunnels?\b'),
    ("doctrine", r'\bdoctrine\b'),
    ("spec-speak", r'labeled as such|labelled as such|never here|the files behind it'),
    ("persona / avatar / tier / schema", r'\b(?:personas?|avatars?|tiers?|schema)\b'),
    ("banned word", r'\bunlock(?:s|ed|ing)?\b|\bsupercharge|game-changer|\brevolutionary\b|secret weapon'),
    ("beat (a story moment)", r'\bbeats?\b'),
]
MONEY_FAIL = re.compile(r'\$\s?\d|\d\s?%|\b\d[\d,]*\s?(?:dollars?|usd|bucks)\b|\b\d+k\b', re.I)
MONEY_WARN = re.compile(r'\b(?:splits?|caps?|stock|payouts?|earnings|income|commissions?)\b', re.I)
CUT_FAIL = re.compile(r'\b(?:booking link|CRM|compliance|Design Package|scheduled tasks?|consent|private call)\b', re.I)
CUT_FAIL_9 = re.compile(r'\b(?:booking link|CRM|compliance|scheduled tasks?|consent|private call)\b', re.I)
COMMAND = re.compile(r'\b(?:say|type)\s*:?\s*["“‘\']', re.I)
QUOTED = re.compile(r'["“]([^"”]{2,80})["”]')
_ABBR = re.compile(r'\b(?:e\.g|i\.e|vs|etc|Mr|Mrs|Ms|Dr|St|No|a\.m|p\.m|U\.S)\.$', re.I)


def sentences(text):
    parts = re.split(r'(?<=[.!?])["”’)\]]*\s+(?=\S)', text.strip())
    out = []
    for p in parts:
        if out and _ABBR.search(out[-1]):
            out[-1] += ' ' + p
        else:
            out.append(p)
    return [p for p in out if p.strip()]


def wc(s):
    return len(s.split())


def para_info(el):
    txt = "".join(t.text or "" for t in el.iter(qn('w:t'))).strip()
    pPr = el.find(qn('w:pPr'))
    style = ''
    if pPr is not None:
        ps = pPr.find(qn('w:pStyle'))
        if ps is not None:
            style = (ps.get(qn('w:val')) or '').lower()
    pb = pPr.find(qn('w:pBdr')) if pPr is not None else None
    callout = pb is not None and pb.find(qn('w:left')) is not None and pPr.find(qn('w:shd')) is not None
    pbb = pPr is not None and pPr.find(qn('w:pageBreakBefore')) is not None
    hardbr = any(br.get(qn('w:type')) == 'page' for br in el.iter(qn('w:br')))
    hl = len(el.findall('.//' + qn('w:hyperlink')))
    bm = len(el.findall(qn('w:bookmarkStart')))
    runs = el.findall(qn('w:r'))
    bold0, t0 = False, ''
    if runs:
        rPr = runs[0].find(qn('w:rPr'))
        bold0 = rPr is not None and rPr.find(qn('w:b')) is not None
        t0 = "".join(t.text or "" for t in runs[0].iter(qn('w:t')))
    if callout: kind = 'callout'
    elif style.startswith('title'): kind = 'title'
    elif style.startswith('heading1'): kind = 'h1'
    elif style.startswith('heading2'): kind = 'h2'
    elif txt.startswith(TAG): kind = 'demo'
    elif t0.startswith('•'): kind = 'bullet'
    elif bold0 and t0.rstrip().endswith(':'): kind = 'label'
    else: kind = 'body'
    return dict(text=txt, kind=kind, pbb=pbb, hardbr=hardbr, hl=hl, bm=bm)


def new_section(name, kind, kicker=''):
    return dict(name=name, kind=kind, kicker=kicker, paras=[], tables=[], callouts=[], hl=0, bm=0, hardbr=0, pbb=0)


def parse(path):
    doc = Document(path)
    blocks = []
    for el in doc.element.body:
        tag = el.tag.split('}')[1]
        if tag == 'p':
            blocks.append(('p', para_info(el)))
        elif tag == 'tbl':
            rows = []
            for tr in el.findall(qn('w:tr')):
                rows.append(["".join(t.text or "" for t in tc.iter(qn('w:t'))).strip() for tc in tr.findall(qn('w:tc'))])
            blocks.append(('tbl', rows))
    sections = []
    cur = new_section('COVER', 'cover')
    i = 0
    while i < len(blocks):
        kind, payload = blocks[i]
        if kind == 'p':
            p = payload
            if p['kind'] == 'h1' and p['text'] == 'CONTENTS':
                sections.append(cur); cur = new_section('CONTENTS', 'toc'); i += 1; continue
            if BAND_RE.match(p['text']) and i + 1 < len(blocks) and blocks[i + 1][0] == 'p' and blocks[i + 1][1]['kind'] == 'h1':
                title = blocks[i + 1][1]['text']
                sections.append(cur)
                cur = new_section(title, 'section', kicker=p['text'])
                cur['pbb'] += 1 if p['pbb'] else 0
                cur['bm'] += blocks[i + 1][1]['bm']
                i += 2; continue
            cur['paras'].append(p)
            cur['hl'] += p['hl']; cur['bm'] += p['bm']
            cur['hardbr'] += 1 if p['hardbr'] else 0; cur['pbb'] += 1 if p['pbb'] else 0
            if p['kind'] == 'callout': cur['callouts'].append(p['text'])
        else:
            cur['tables'].append(payload)
        i += 1
    sections.append(cur)
    s0 = doc.sections[0]
    footer = " ".join(p.text for p in s0.footer.paragraphs)
    header = " ".join(p.text for p in s0.header.paragraphs)
    return sections, footer, header


def section_text(s):
    return "\n".join([p['text'] for p in s['paras']] + [c for t in s['tables'] for r in t for c in r])


def layout_pages(s):
    h = 72.0 if s['kind'] == 'section' else 0.0
    for p in s['paras']:
        t = p['text']
        if not t: continue
        if p['kind'] == 'h2': h += 30
        elif p['kind'] == 'demo': h += 13.2 + 6
        elif p['kind'] == 'callout': h += max(1, math.ceil(len(t) / 86.0)) * 13.2 + 20
        elif p['kind'] == 'bullet': h += max(1, math.ceil(len(t) / 88.0)) * 13.2 + 4
        else: h += max(1, math.ceil(len(t) / 92.0)) * 13.2 + 6
    for t in s['tables']:
        ncol = max(len(r) for r in t)
        lens = [max((len(r[c]) if c < len(r) else 0) for r in t) for c in range(ncol)]
        wts = [max(4, min(l, 60)) for l in lens]; tot = float(sum(wts))
        widths = [max(0.55 * 72, 468.0 * w / tot) for w in wts]
        sc = 468.0 / sum(widths); widths = [w * sc for w in widths]
        for r in t:
            rl = 1
            for ci, cell in enumerate(r):
                cpl = max(6, int(widths[ci] / 5.2))
                rl = max(rl, math.ceil(len(cell) / cpl) if cell else 1)
            h += rl * 12.0 + 9
        h += 8
    return max(1, math.ceil(h / USABLE_PT)), round(h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx"); ap.add_argument("--json", action="store_true")
    g = ap.add_mutually_exclusive_group(); g.add_argument("--demo", action="store_true"); g.add_argument("--real", action="store_true")
    a = ap.parse_args()
    sections, footer, header = parse(a.docx)
    full_text = "\n".join(section_text(s) for s in sections)
    cover = next((s for s in sections if s['kind'] == 'cover'), None)
    toc = next((s for s in sections if s['kind'] == 'toc'), None)
    secs = [s for s in sections if s['kind'] == 'section']
    demo = a.demo or (not a.real and DEMO_COVER in full_text)

    results = []          # (status, check, detail)
    def fail(c, d): results.append(("FAIL", c, d))
    def warn(c, d): results.append(("WARN", c, d))
    def ok(c, d=""): results.append(("PASS", c, d))

    # ---- per-section measure -------------------------------------------------------
    rows = []; total = 0; est_pages = 0
    for s in sections:
        text = section_text(s); words = wc(text); total += words
        lp, hpt = layout_pages(s); sp = max(1, math.ceil(words / 380.0)) if words else 1
        if s['kind'] == 'toc':
            entries = [p for p in s['paras'] if p['hl'] > 0]
            lp = 1 if len(entries) <= 12 else 2; sp = lp
        pages = max(lp, sp); est_pages += pages
        num = None
        m = re.match(r'^(?:SECTION|CHAPTER) (\d+)$', s['kicker'] or '')
        if m: num = int(m.group(1))
        tgt, mx = LIMITS.get(num, (None, None)) if num else (None, None)
        status = ''
        if mx is not None:
            if words > mx: status = 'OVER MAX'; fail("length", f"{s['kicker']} — {s['name']}: {words} words, maximum {mx}")
            elif words < tgt: status = 'thin'; warn("length", f"{s['kicker']} — {s['name']}: {words} words, target {tgt} (thin — fix from the Brain file, never pad)")
            else: status = 'ok'
        rows.append(dict(section=(f"{s['kicker']} — {s['name']}" if s['kicker'] else s['name']), kind=s['kind'], words=words,
                         target=tgt, maximum=mx, status=status, tables=len(s['tables']), callouts=len(s['callouts']),
                         layout_pages=lp, layout_pt=hpt, words_pages=sp, pages=pages))
    if total > BOOK_MAX: fail("length", f"whole Book {total} words, maximum {BOOK_MAX}")
    elif total < BOOK_TARGET: warn("length", f"whole Book {total} words, target {BOOK_TARGET}+")
    else: ok("length", f"whole Book {total} words (target {BOOK_TARGET}+, maximum {BOOK_MAX})")
    if demo:
        if DEMO_RANGE[0] <= total <= DEMO_RANGE[1]: ok("demo length", f"{total} words inside the demo target {DEMO_RANGE[0]}–{DEMO_RANGE[1]}")
        else: warn("demo length", f"{total} words, demo target {DEMO_RANGE[0]}–{DEMO_RANGE[1]}")
    if est_pages > PAGE_FAIL: fail("pages", f"estimated {est_pages} pages (maximum {PAGE_FAIL})")
    elif est_pages > PAGE_WARN: warn("pages", f"estimated {est_pages} pages (warn above {PAGE_WARN}, fail above {PAGE_FAIL})")
    else: ok("pages", f"estimated {est_pages} pages (cover + contents + the sections; fail above {PAGE_FAIL})")

    # ---- 1. bracketed tokens · 4. raw markup ---------------------------------------
    br = re.findall(r'\[[^\]\n]{1,100}\]', full_text)
    if br: fail("bracketed token", "; ".join(br[:6]))
    else: ok("bracketed token", "none")
    if '<w:' in full_text: fail("raw markup", "'<w:' found in the extracted text")
    else: ok("raw markup", "none")

    # ---- 2 + 12. bands and their order ---------------------------------------------
    titles = [s['name'] for s in secs]; kickers = [s['kicker'] for s in secs]
    if titles != EXPECTED: fail("bands", f"expected the nine sections in order; got {titles}")
    else: ok("bands", "the nine sections, in order")
    old = [k for k in kickers if not k.startswith('SECTION')]
    if old: fail("band labels", f"kickers must be SECTION 1–9; found {old}")
    elif kickers != [f"SECTION {i}" for i in range(1, 10)]: fail("band labels", f"kickers out of sequence: {kickers}")
    else: ok("band labels", "SECTION 1 through SECTION 9")
    parts = [s for s in sections if (s['kicker'] or '').startswith('PART')]
    if parts: fail("bands", f"PART bands present: {[s['name'] for s in parts]}")

    # ---- 3. byline once --------------------------------------------------------------
    subtitle = footer.split('\t')[0].split('  ·  ')[0].strip() if footer else ''
    all_paras = [p['text'] for s in sections for p in s['paras']]
    if subtitle:
        n_sub = sum(1 for t in all_paras if t == subtitle)
        if n_sub != 1: fail("byline once", f"the byline '{subtitle}' appears {n_sub} times in the body (cover only = 1)")
        else: ok("byline once", f"'{subtitle}' on the cover only")
        cred = ''
        if cover:
            ct = [p['text'] for p in cover['paras'] if p['text']]
            if subtitle in ct and ct.index(subtitle) + 1 < len(ct): cred = ct[ct.index(subtitle) + 1]
        if cred:
            n_c = sum(1 for t in all_paras if cred in t)
            if n_c != 1: fail("credential line once", f"'{cred[:60]}' appears {n_c} times")
            else: ok("credential line once", cred[:70])
    else:
        warn("byline once", "no footer byline found — is this a book-mode render?")

    # ---- 11. contents page -----------------------------------------------------------
    if toc is None: fail("contents", "no CONTENTS page")
    else:
        entries = [p for p in toc['paras'] if p['hl'] > 0]
        if len(entries) != 9: fail("contents", f"{len(entries)} linked rows (nine expected)")
        else:
            bad = [e['text'] for e, exp in zip(entries, EXPECTED) if e['text'].strip() != f"SECTION {EXPECTED.index(exp) + 1} — {exp}"]
            if bad: fail("contents", f"rows do not match the bands character-for-character: {bad}")
            else: ok("contents", "nine linked rows, in order, matching the bands")
        summaries = []
        for idx, p in enumerate(toc['paras']):
            if p['hl'] > 0 and idx + 1 < len(toc['paras']) and toc['paras'][idx + 1]['hl'] == 0 and toc['paras'][idx + 1]['text']:
                summaries.append(toc['paras'][idx + 1]['text'])
        long = [f"{wc(x)} words: {x[:50]}…" for x in summaries if wc(x) > 12]
        if len(summaries) < 9: fail("contents summaries", f"{len(summaries)} summaries (nine expected, at most twelve words each)")
        elif long: fail("contents summaries", "over twelve words: " + " | ".join(long))
        else: ok("contents summaries", "nine summaries, each at most twelve words")
        if toc['hl'] != 9: fail("contents links", f"{toc['hl']} hyperlinks (nine expected)")
        if any(p['kind'] == 'h1' for s in sections for p in s['paras'] if p['text'] == 'CONTENTS' and s is not toc):
            fail("contents", "more than one CONTENTS")

    # ---- 5. the tables ----------------------------------------------------------------
    def data_rows(t): return t[1:] if t else []
    by_num = {int(re.search(r'\d+', s['kicker']).group()): s for s in secs if re.search(r'\d+', s['kicker'] or '')}
    s1 = by_num.get(1)
    if s1 and s1['tables']:
        dr = data_rows(s1['tables'][0])
        if not (8 <= len(dr) <= 12): fail("section 1 table", f"{len(dr)} rows (8 to 12)")
        else: ok("section 1 table", f"{len(dr)} rows")
        longv = [r[0] for r in dr if len(r) > 1 and wc(r[1]) > 15]
        if longv: fail("section 1 values", f"over 15 words: {longv}")
        else: ok("section 1 values", "every value at most 15 words")
        offer_rows = [r[0] for r in dr if 'offer' in r[0].lower()]
        if offer_rows: fail("section 1 rows", f"rows Section 9 carries: {offer_rows}")
        dup = [r[0] for r in dr if re.search(r'teach|speaks to|voice', r[0], re.I)]
        if dup: fail("section 1 rows", f"rows Sections 4, 6 or 8 carry: {dup}")
    else: fail("section 1 table", "missing")
    s4 = by_num.get(4)
    if s4 and s4['tables'] and len(data_rows(s4['tables'][0])) >= 1: ok("section 4 table", f"{len(data_rows(s4['tables'][0]))} strategy rows")
    else: fail("section 4 table", "the strategies table needs at least one real row")
    s5 = by_num.get(5)
    if s5 and ((s5['tables'] and len(data_rows(s5['tables'][0])) >= 1) or 'no agents helped yet' in section_text(s5).lower()):
        ok("section 5 table", "the agents-helped table (or the one honest line)")
    else: fail("section 5 table", "the agents-helped table or the one honest line is missing")
    s7 = by_num.get(7)
    if s7 and s7['tables'] and len(data_rows(s7['tables'][0])) == 4: ok("section 7 table", "four rows")
    else: fail("section 7 table", "the numbers table must have exactly four rows")

    # ---- 6. money ---------------------------------------------------------------------
    body_text = "\n".join(section_text(s) for s in secs)
    mf = MONEY_FAIL.findall(body_text)
    if mf: fail("no money", f"figures found: {mf[:6]}")
    else: ok("no money", "no money figure, percentage or dollar amount")
    mw = sorted(set(w.lower() for w in MONEY_WARN.findall(body_text)))
    if mw: warn("money words", f"read by hand: {mw}")

    # ---- 7. plain words: sentences, jargon, commands ----------------------------------
    long_paras = []
    for s in secs:
        n = int(re.search(r'\d+', s['kicker']).group())
        for p in s['paras']:
            if p['kind'] not in ('body', 'label', 'bullet', 'callout'): continue
            t = p['text']
            if n == 8 and t[:1] in '"“': continue          # verbatim speech is exempt
            if len(sentences(t)) > 4: long_paras.append(f"S{n}: {len(sentences(t))} sentences — {t[:55]}…")
    if long_paras: fail("four sentences", " | ".join(long_paras[:8]))
    else: ok("four sentences", "no paragraph over four sentences (verbatim speech in Section 8 exempt)")
    all_text = "\n".join(section_text(s) for s in sections)
    hits = []
    for label, rx in JARGON:
        m = re.findall(rx, all_text, re.I)
        if m: hits.append(f"{label}: {sorted(set(x if isinstance(x, str) else x[0] for x in m))[:4]}")
    for word, explain in (("upline", r'upline\b[^.\n]{0,90}sponsor'), ("the model", r'the model\b[^.\n]{0,90}brokerage')):
        occ = [m.start() for m in re.finditer(word, all_text, re.I)]
        if occ and not re.search(explain, all_text[occ[0]:occ[0] + 160], re.I):
            hits.append(f"'{word}' used without a plain explanation at its first appearance")
    po = [n for n, s in by_num.items() if n != 9 and 'Partner Offer' in section_text(s)]
    if po: hits.append(f"'Partner Offer' outside Section 9: sections {po}")
    if hits: fail("jargon", " | ".join(hits))
    else: ok("jargon", "none of the jargon list")
    cmd = [f"S{n}: {m.group(0)}" for n, s in by_num.items() if n != 9 for m in COMMAND.finditer(section_text(s))]
    if cmd: fail("commands", "outside Section 9: " + ", ".join(cmd[:6]))
    s9 = by_num.get(9)
    phrases = sorted(set(q.strip() for q in QUOTED.findall(section_text(s9)))) if s9 else []
    if len(phrases) > 3: fail("commands", f"Section 9 carries {len(phrases)} distinct quoted phrases (at most three): {phrases}")
    elif not cmd: ok("commands", f"only in Section 9 — {len(phrases)} distinct phrase(s): {phrases}")

    # ---- 8. nothing that was cut (Section 9 may NAME a later-week item — the brief, the offer — in one line)
    cut = sorted(set(m.lower() for n, s in by_num.items() if n != 9 for m in CUT_FAIL.findall(section_text(s))))
    if s9: cut += sorted(set(m.lower() for m in CUT_FAIL_9.findall(section_text(s9))))
    if cut: fail("nothing cut", f"found: {cut}")
    else: ok("nothing cut", "no compliance, operations, consent or private-call text")

    # ---- 13. the state rule (the machine part) ----------------------------------------
    if s4:
        t4 = section_text(s4)
        if 'turns this page' in t4 and 'turned this page' in t4: fail("state rule", "Section 4 carries both the forward and the past-tense opener")
        elif 'turns this page' in t4 or 'turned this page' in t4: ok("state rule", "Section 4 opener: " + ("Week-1 state" if 'turns this page' in t4 else "post-offer state"))
        else: warn("state rule", "Section 4 has no opener line")
    if s9:
        nb = sum(1 for p in s9['paras'] if p['kind'] == 'bullet')
        if nb != 3: fail("state rule", f"Section 9 has {nb} bullets (exactly three)")
        else: ok("state rule", "Section 9: three bullets")
        if not s9['callouts']: warn("state rule", "Section 9 has no callout (the one next thing to type)")

    # ---- callouts: one per section, none in Section 1 ----------------------------------
    for n, s in by_num.items():
        c = len(s['callouts'])
        if n == 1 and c: fail("callouts", "Section 1 carries a callout (none allowed)")
        elif n != 1 and c > 1: fail("callouts", f"Section {n} carries {c} callouts (one)")
        elif n != 1 and c == 0: warn("callouts", f"Section {n} has no callout")

    # ---- 14. voice (the machine part) --------------------------------------------------
    s8 = by_num.get(8)
    if s8:
        sig = [p for p in s8['paras'] if p['text'].startswith('Signature line')]
        if len(sig) != 3: fail("voice", f"{len(sig)} 'Signature line:' lines (three)")
        subs = [p['text'] for p in s8['paras'] if p['kind'] == 'h2']
        want = ["Why I'm excited about agent attraction", "My why", "Why someone should partner with me"]
        if [x.strip() for x in subs] != want: fail("voice", f"sub-bands {subs} (expected {want})")
        answers = []
        for idx, p in enumerate(s8['paras']):
            if p['kind'] == 'h2' and idx + 1 < len(s8['paras']): answers.append(s8['paras'][idx + 1]['text'])
        off = [f"{wc(x)} words" for x in answers if not (50 <= wc(x) <= 95)]
        if len(answers) < 3: fail("voice", "fewer than three dictated answers")
        elif off: warn("voice", f"dictated answers outside the 60–80-word core: {off}")
        else: ok("voice", "three signature lines, three dictated answers at their core length")
        srcs = [p['text'][-60:] for p in s8['paras'] if re.search(r'\(dictated|— demo, fictional\)', p['text'])]
        if srcs: fail("voice", f"source tag after an answer: {srcs}")

    # ---- demo checks / the real-build tripwire ----------------------------------------
    eyebrow = cover['paras'][0]['text'] if cover and cover['paras'] else ''
    eyebrow = next((p['text'] for p in cover['paras'] if p['text']), '') if cover else ''
    if demo:
        tag_lines = [(n, [p['text'] for p in s['paras'] if p['kind'] == 'demo']) for n, s in by_num.items()]
        bad = [n for n, lines in tag_lines if len(lines) != 1]
        first_bad = [n for n, s in by_num.items() if not s['paras'] or s['paras'][0]['kind'] != 'demo']
        n_tags = full_text.count(TAG)
        if bad: fail("demo tag line", f"sections without exactly one demo line: {bad}")
        if first_bad: fail("demo tag line", f"the demo line is not the first line under the band in sections {first_bad}")
        if n_tags != 9: fail("demo tag count", f"'{TAG}' appears {n_tags} times (exactly nine: once under each band)")
        elif not bad and not first_bad: ok("demo tag", "one sanctioned line under each of the nine bands, nowhere else")
        variants = []
        for s in sections:
            for p in s['paras']:
                t = p['text']
                if p['kind'] == 'demo' or t == DEMO_COVER or t == eyebrow: continue
                if re.search(r'illustrative|—\s?demo|\bdemo\b', t, re.I): variants.append(t[:70])
            for t in s['tables']:
                for r in t:
                    for c in r:
                        if re.search(r'illustrative|—\s?demo|\bdemo\b', c, re.I): variants.append(c[:70])
        if variants: fail("demo tag variants", f"inline tags or variants: {variants[:6]}")
        else: ok("demo tag variants", "no inline tag, no variant")
        dated = [n for n, s in by_num.items() for p in s['paras'] if p['kind'] == 'demo' and re.search(r'\b(19|20)\d\d\b', p['text'])]
        if dated: fail("demo tag on a date", f"sections {dated}")
        if DEMO_COVER not in full_text: fail("demo watermark", "the verbatim cover line is missing")
        if 'DEMO' not in eyebrow.upper(): fail("demo watermark", f"the eyebrow does not say DEMO: '{eyebrow}'")
        if DEMO_COVER in full_text and 'DEMO' in eyebrow.upper(): ok("demo watermark", "cover line verbatim; eyebrow carries DEMO")
    else:
        trip = []
        if TAG in full_text: trip.append("the demo tag")
        if DEMO_COVER in full_text: trip.append("the demo cover line")
        if 'DEMO' in eyebrow.upper(): trip.append("a DEMO eyebrow")
        if trip: fail("real-build tripwire", ", ".join(trip) + " in a non-demo render")
        else: ok("real-build tripwire", "no demo marks")

    # ---- the hand checks the script cannot run ----------------------------------------
    hand = ["grounding audit (every proper noun and number traced)", "cardinal rules (nothing negative about a named party; no former brokerage named)",
            "derived, never chosen; anywhere, never a place (Section 6's framing line; the market in Section 1 only)",
            "voice fidelity (the answers verbatim; the read-back ran)", "the anti-fluff swap test on Sections 2, 4 and 6"]

    # ---- output ------------------------------------------------------------------------
    fails = [r for r in results if r[0] == 'FAIL']; warns = [r for r in results if r[0] == 'WARN']
    if a.json:
        print(json.dumps(dict(file=a.docx, demo=demo, total_words=total, estimated_pages=est_pages, sections=rows,
                              checks=[dict(status=s, check=c, detail=d) for s, c, d in results], hand_checks=hand,
                              verdict='FAIL' if fails else 'PASS'), indent=1, ensure_ascii=False))
    else:
        print(f"Brain Book measure — {a.docx}\nmode: {'DEMO' if demo else 'real'} · {total} words · estimated {est_pages} pages\n")
        print("| Section | Words | Target – max | Status | Tables | Callouts | Est. pages (layout / words) |")
        print("|---|---|---|---|---|---|---|")
        for r in rows:
            tm = f"{r['target']} – {r['maximum']}" if r['maximum'] else "—"
            print(f"| {r['section']} | {r['words']} | {tm} | {r['status'] or '—'} | {r['tables']} | {r['callouts']} | {r['pages']} ({r['layout_pages']} / {r['words_pages']}) |")
        print()
        for s, c, d in results:
            mark = {'PASS': '✓', 'WARN': '·', 'FAIL': '✗'}[s]
            print(f"  {mark} {s:4} {c}: {d}")
        print("\n  read by hand: " + " · ".join(hand))
        print(f"\nVERDICT: {'FAIL — ' + str(len(fails)) + ' check(s)' if fails else 'PASS'} ({len(warns)} warning(s))")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
