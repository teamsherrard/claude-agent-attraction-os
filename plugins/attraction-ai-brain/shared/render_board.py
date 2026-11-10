#!/usr/bin/env python3
"""
render_board.py — the member's Brain Board, rendered from their Agent Attraction Brain.

One self-contained HTML file (opens in any browser, no internet needed): the map of the Brain, the
goals tracker, today's three moves, this week's build, the open items, and a full page for every part
of the Brain and every weekly system — all read from the Brain's own files. Nothing here edits the
Brain; it only reads. Stdlib only, so it runs wherever python3 runs (no python-docx needed).

Usage:
  python3 render_board.py <brain_dir> --out "<folder>/🧠 Name's Brain Board — YYYY-MM-DD.html"
                          [--week N] [--today YYYY-MM-DD] [--template board-template.html]

  --week   caps the lit systems at cohort week N (a system of a later week renders as "coming");
           default: config.md → Cohort week, else inferred from what is built.
  --today  the date the board is rendered for (the sync skill passes the member's date); default:
           today on the member's clock (config.md → Timezone), or for a demo brain the newest daily
           scorecard row + 1 day.
The output is one self-contained page: the board (needs scripts) plus a plain quick view that shows
wherever scripts can't run, such as a cloud-drive preview. Python only, nothing to install.
Exit 2 when brain.md is missing (never render an empty Brain). Prints the output path on success.
"""
import re, os, sys, json, argparse, glob, html
import datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
DEMO_TAG = re.compile(r'\s*\((?:[^()]*illustrative[^()]*|demo[^()]*|[^()]*—\s*demo[^()]*)\)', re.I)

# ───────────────────────── small helpers ─────────────────────────
def read(path):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except OSError:
        return ''

def clean(s, demo):
    s = (s or '').replace('\\"', '"').replace('\\#', '#').replace('\\-', '-').replace('\\_', '_')
    if demo:
        s = DEMO_TAG.sub('', s)
        s = re.sub(r'\s*\[[^\]]*\bdemo\b[^\]]*\]', '', s, flags=re.I)
    s = re.sub(r'`([^`]*)`', r'\1', s)
    s = re.sub(r'\s*\*\(([^)]*)\)\*', r' (\1)', s)        # *(note)* → (note)
    s = re.sub(r'\[([^\]]+)\]\((?:https?:)?[^)]*\)', r'\1', s)  # [text](url) → text
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s

def is_template(text):
    """A shipped template still full of [placeholders] is not member content."""
    return len(re.findall(r'\[[^\]\n]{2,40}\]', (text or '')[:2500])) >= 4

def strip_md_header(text):
    """Drop the DEMO line, the '# Title' and the leading italic owner notes of a Brain file."""
    lines = text.split('\n')
    out = []
    started = False
    for l in lines:
        s = l.strip()
        if not started:
            if not s or s.startswith('DEMO BRAIN') or s.startswith('# ') or (s.startswith('*') and s.endswith('*')) or s.startswith('> ') :
                continue
            started = True
        out.append(l)
    return '\n'.join(out)

def md_to_book(text, demo, drop_sections=(), keep_sections=None):
    """Brain markdown → the Book-style text the board renders (## bands, | kv | rows, • bullets, >> quotes)."""
    text = strip_md_header(text)
    out, prev_cols, cur = [], None, None
    keep = True
    for raw in text.split('\n'):
        l = raw.rstrip()
        s = l.strip()
        m = re.match(r'^(#{2,4})\s+(.*)$', s)
        if m:
            title = clean(re.sub(r'\s*\(.*?\)\s*$', '', m.group(2)), demo) if '(' in m.group(2) and len(m.group(2)) > 60 else clean(m.group(2), demo)
            cur = title
            keep = (keep_sections is None or any(title.lower().startswith(k.lower()) for k in keep_sections)) and not any(title.lower().startswith(d.lower()) for d in drop_sections)
            if keep:
                out.append(''); out.append(('## ' if len(m.group(1)) == 2 else '### ') + title); prev_cols = None
            continue
        if not keep:
            continue
        if not s:
            out.append(''); prev_cols = None; continue
        if re.match(r'^\|?\s*:?-{2,}', s):
            continue
        if s.startswith('|'):
            cells = [clean(c, demo) for c in s.strip('|').split('|')]
            if prev_cols is not None and prev_cols != len(cells):
                out.append('')
            prev_cols = len(cells)
            out.append('| ' + ' | '.join(cells) + ' |'); continue
        m = re.match(r'^[-*]\s+\*\*(.+?):\*\*\s*(.*)$', s) or re.match(r'^\*\*(.+?):\*\*\s*(.*)$', s)
        if m:
            label, val = clean(m.group(1), demo), clean(m.group(2), demo)
            if not val:
                out.append(''); out.append('### ' + label); prev_cols = None; continue
            if len(label) > 48:
                if prev_cols is not None: out.append('')
                prev_cols = None
                out.append('**' + label + ':** ' + val); continue
            if prev_cols not in (None, 2): out.append('')
            prev_cols = 2
            out.append('| ' + label + ' | ' + val + ' |'); continue
        prev_cols = None
        m = re.match(r'^[-*]\s+(.*)$', s)
        if m:
            out.append('• ' + clean(m.group(1), demo)); continue
        m = re.match(r'^(\d+)\.\s+(.*)$', s)
        if m:
            out.append(m.group(1) + '. ' + clean(m.group(2), demo)); continue
        if s.startswith('>'):
            out.append('>> ' + clean(s.lstrip('> '), demo)); continue
        out.append(clean(s, demo))
    txt = '\n'.join(out)
    txt = re.sub(r'\n{3,}', '\n\n', txt).strip('\n')
    return txt

def md_section(text, heading_prefix):
    """The body of the '## heading…' section whose heading starts with the prefix (case-insensitive)."""
    lines = text.split('\n'); grab = False; out = []
    for l in lines:
        s = l.strip()
        if s.startswith('## '):
            if grab: break
            grab = s[3:].strip().lower().startswith(heading_prefix.lower())
            continue
        if grab: out.append(l)
    return '\n'.join(out).strip()

def kv(text, key):
    """The value after **key:** on any line, or after a plain `key:` that opens a line (the templates write
    `Status: …`, `Join-gated package allowed: …`, `Host: …` unbolded) — up to the next ' · **' pair or the line end."""
    bold = re.search(r'\*\*' + re.escape(key) + r':?\*\*:?\s*(.+)', text)
    plain = re.search(r'^[ \t]*(?:[-*][ \t]+)?' + re.escape(key) + r':[ \t]*(\S.*)$', text, re.M)
    m = min((x for x in (bold, plain) if x), key=lambda x: x.start(), default=None)  # the earliest line wins: a file's header Status beats a later section's
    if not m: return ''
    v = m.group(1)
    v = re.split(r'\s+·\s+\*\*', v)[0]
    return v.strip()

def first_kv(text, keys):
    for k in keys:
        v = kv(text, k)
        if v: return v
    return ''

def table_under(text, heading_prefix):
    """Rows (lists of cells) of the first markdown table under a heading; header row first."""
    body = md_section(text, heading_prefix) if heading_prefix else text
    rows = []
    for l in body.split('\n'):
        s = l.strip()
        if s.startswith('|') and not re.match(r'^\|\s*:?-{2,}', s):
            rows.append([c.strip() for c in s.strip('|').split('|')])
        elif rows and not s.startswith('|'):
            break
    return rows

def num(s, default=0):
    m = re.search(r'-?\d[\d,]*(?:\.\d+)?', s or '')
    if not m: return default
    try:
        v = m.group(0).replace(',', '')
        return float(v) if '.' in v else int(v)
    except ValueError:
        return default

def date_in(s):
    m = re.search(r'(20\d\d)-(\d\d)-(\d\d)', s or '')
    if not m: return None
    try: return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError: return None

def latest_export(brain, prefix):
    files = sorted(glob.glob(os.path.join(brain, 'exports', prefix + '*.txt')))
    return files[-1] if files else ''

def nice_date(d):
    return d.strftime('%a %b ') + str(d.day)

def long_date(d):
    return d.strftime('%B ') + str(d.day) + d.strftime(', %Y')

# ───────────────────────── parsers: the exports ─────────────────────────
def parse_book(txt, demo):
    """The Brain Book export: {n: {'title','tag','body'}} from the SECTION bands and the TOC."""
    secs = {}
    for m in re.finditer(r'^SECTION (\d) — ([^:\n]+?)\s*::\s*(.+)$', txt, re.M):
        secs[int(m.group(1))] = {'title': m.group(2).strip(), 'tag': clean(m.group(3), demo), 'body': ''}
    parts = re.split(r'^═+\n(SECTION \d — [^\n]+)\n═+\n', txt, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        n = int(re.match(r'SECTION (\d)', parts[i]).group(1))
        body = parts[i + 1]
        lines = []
        for l in body.split('\n'):
            s = l.strip()
            if s.startswith('(illustrative') or s.startswith('[[') : continue
            m = re.match(r'^─+\s*(.+?)\s*─+$', s)
            if m: lines.append(''); lines.append('## ' + clean(m.group(1), demo)); continue
            if s.startswith('|'):
                cells = [clean(c, demo) for c in s.strip('|').split('|')]
                if [c.lower() for c in cells] == ['label', 'value']: continue
                lines.append('| ' + ' | '.join(cells) + ' |'); continue
            if s.startswith('Signature line:'):
                lines.append('• ' + clean(s.split(':', 1)[1], demo)); continue
            lines.append(clean(s, demo) if s else '')
        secs.setdefault(n, {'title': parts[i].split('— ', 1)[1], 'tag': '', 'body': ''})
        secs[n]['body'] = re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip('\n')
    return secs

def band_case(s):
    """AN ALL-CAPS BAND → sentence case, keeping day and month names and 'I' capitalized."""
    t = s[0] + s[1:].lower()
    keep = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'zoom', 'skool', 'circle')
    for w in keep:
        t = re.sub(r'\b' + w + r'\b', w.capitalize(), t)
    t = re.sub(r'\bi\b', 'I', t)
    return t

def parse_offer_doc(txt, demo):
    """The Partner Offer export: name, one-liner, promise, and the bands as ## sections."""
    lines = txt.split('\n')
    head = [l.strip() for l in lines[:8] if l.strip()]
    doc = {'name': head[0] if head else '', 'oneliner': clean(head[1], demo) if len(head) > 1 else '', 'promise': clean(head[2], demo) if len(head) > 2 else ''}
    body = []
    started = False
    for l in lines:
        s = l.strip()
        m = re.match(r'^─+$', s)
        if m: continue
        if re.match(r'^[A-Z][A-Z0-9 ,’\'—:\-]{6,}$', s) and len(s) < 70:
            started = True
            body.append(''); body.append('## ' + band_case(s) if not re.search(r'[a-z]', s) else '## ' + s); continue
        if not started: continue
        if s.startswith('|'):
            body.append('| ' + ' | '.join(clean(c, demo) for c in s.strip('|').split('|')) + ' |'); continue
        m2 = re.match(r'^─+\s*(.+?)\s*─+$', s)
        if m2: body.append(''); body.append('### ' + clean(m2.group(1), demo)); continue
        body.append(clean(s, demo) if s else '')
    doc['body'] = re.sub(r'\n{3,}', '\n\n', '\n'.join(body)).strip('\n')
    return doc

# ───────────────────────── parsers: the Brain files ─────────────────────────
def parse_config(md):
    c = {'demo': 'Demo brain:** yes' in md or '**Demo brain:** yes' in md, 'week': None, 'blocks': {}, 'provider': kv(md, 'Storage provider')}
    tzm = re.search(r'\b(UTC|[A-Za-z]+/[A-Za-z0-9_+\-/]+)\b', kv(md, 'Timezone'))
    c['tz'] = tzm.group(1) if tzm else ''
    w = kv(md, 'Cohort week')
    if w: c['week'] = num(w, None)
    for m in re.finditer(r'^## ([A-Za-z &\-]+?)\s*\(Week (\d)\)[^\n]*\n((?:(?!^## ).*\n?)*)', md, re.M):
        name, week, block = m.group(1).strip(), int(m.group(2)), m.group(3).strip()
        if block and '[' not in block.split('\n')[0]:
            c['blocks'][name.lower()] = {'week': week, 'line': clean(block.split('\n')[0].lstrip('- '), c['demo'])}
    return c

def parse_goals(md, demo):
    g = {'why': '', 'today': 0, 'twelve': 0, 'long': 0, 'hours': 0, 'q_start': None, 'q_end': None, 'status': '', 'first_agent': '', 'hours_split': '', 'intangibles': [], 'rows_3060': [], 'rows_12': [], 'weekly': []}
    m = re.search(r'Status:\s*([^\n*]+)', md)
    if m:
        g['status'] = m.group(1).strip()
        ds = re.findall(r'20\d\d-\d\d-\d\d', m.group(1))
        if len(ds) >= 3: g['q_start'], g['q_end'] = date_in(ds[1]), date_in(ds[2])
        elif len(ds) == 2: g['q_start'], g['q_end'] = date_in(ds[0]), date_in(ds[1])
    why = md_section(md, 'The why')
    g['why'] = clean(why.strip().strip('"').split('\n')[0], demo) if why else ''
    for r in table_under(md, 'Your numbers')[1:]:
        if len(r) < 2: continue
        k, v = r[0].lower(), r[1]
        if 'today' in k: g['today'] = num(v)
        elif '12 months' in k or 'next 12' in k: g['twelve'] = num(v)
        elif 'long-term' in k or 'long term' in k: g['long'] = num(v)
        elif 'hours' in k: g['hours'] = num(v)
    g['rows_3060'] = [[clean(c, demo) for c in r] for r in table_under(md, '30-60-90')]
    g['rows_12'] = [[clean(c, demo) for c in r] for r in table_under(md, '12-month milestones')]
    fa = md_section(md, 'First agent')
    g['first_agent'] = clean(re.split(r'"?\s*→', fa.split('\n')[0].strip())[0].strip().strip('"'), demo) if fa else ''
    hs = md_section(md, 'Hours')
    g['hours_split'] = clean(hs.split('\n')[0], demo) if hs else ''
    it = md_section(md, 'Intangibles')
    g['intangibles'] = [clean(x.strip('- ').strip(), demo) for x in it.split('\n') if x.strip().startswith('-')] if it else []
    wk = md_section(md, 'Weekly activity')
    g['weekly'] = [clean(x.strip('- ').strip(), demo) for x in wk.split('\n') if x.strip().startswith('-')] if wk else []
    return g

def parse_scorecard(md, demo):
    s = {'targets': [], 'weekly': [], 'daily': [], 'slice_conv': 2, 'slice_follow': 2, 'ratios': ''}
    s['targets'] = [[clean(c, demo) for c in r] for r in table_under(md, 'Targets')]
    s['weekly'] = [[clean(c, demo) for c in r] for r in table_under(md, 'Weekly rows')]
    s['daily'] = [[clean(c, demo) for c in r] for r in table_under(md, 'Daily rows')]
    m = re.search(r'Daily slice:\s*(\d+)\s*conversations?(?:\s*(?:/|and)\s*(\d+)\s*follow)?', md, re.I)
    if m:
        s['slice_conv'] = int(m.group(1)); s['slice_follow'] = int(m.group(2) or 2)
    m = re.search(r'^Ratios:\s*(.+)$', md, re.M)
    if m: s['ratios'] = clean(m.group(1), demo)
    return s

def parse_pipeline(md, demo):
    p = {'rows': [], 'counts': ''}
    for r in table_under(md, 'Board')[1:]:
        if len(r) >= 7: p['rows'].append({'agent': clean(r[0], demo), 'type': clean(r[1], demo), 'stage': clean(r[2], demo), 'owner': clean(r[4], demo), 'next': clean(r[5], demo), 'due': clean(r[6], demo)})
    m = re.search(r'^(Identified \d+[^\n]*)$', md, re.M)
    if m: p['counts'] = clean(m.group(1), demo)
    return p

def parse_org(md, demo):
    o = {'count': num(kv(md, 'Agents in the organization')), 'asof': kv(md, 'As of'), 'rows': []}
    for r in table_under(md, None)[1:]:
        if len(r) >= 6 and r[0] and not r[0].startswith('-'):
            o['rows'].append({'agent': clean(r[0], demo), 'joined': clean(r[1], demo), 'status': clean(r[5], demo), 'notes': clean(r[-1], demo)})
    return o

def parse_debriefs(md, demo):
    m = re.search(r'^## (20\d\d-\d\d-\d\d)\s*·\s*([^\n]+)\n((?:(?!^## ).*\n?)*)', md, re.M)
    if not m: return None
    d = {'date': date_in(m.group(1)), 'score': clean(m.group(2), demo), 'lines': {}, 'moves': []}
    for l in m.group(3).split('\n'):
        mm = re.match(r'^([A-Za-z\'’\- ]+?):\s*(.*)$', l.strip())
        if mm: d['lines'][mm.group(1).strip().lower()] = clean(mm.group(2), demo)
    tm = d['lines'].get("tomorrow's three moves", '')
    d['moves'] = [clean(x.strip(), demo) for x in re.split(r'\s*\d+\.\s+', tm) if x.strip()]
    return d

def parse_exec(md, demo):
    e = {'year': [[clean(c, demo) for c in r] for r in table_under(md, 'The year')],
         'kpis': [[clean(c, demo) for c in r] for r in table_under(md, 'Weekly KPIs')],
         'rhythm': [[clean(c, demo) for c in r] for r in table_under(md, 'CEO rhythm')],
         'nonneg': []}
    nn = md_section(md, 'Three weekly non-negotiables')
    e['nonneg'] = [clean(re.sub(r'^\d+\.\s*', '', x.strip()), demo) for x in nn.split('\n') if re.match(r'^\d+\.', x.strip())] if nn else []
    return e

def parse_offer_md(md, demo):
    o = {'status': kv(md, 'Status'), 'join_gated': kv(md, 'Join-gated package allowed'), 'name': '', 'uvp': '', 'host': kv(md, 'Host'), 'community': kv(md, 'Community name'), 'link': kv(md, 'Link'), 'branches': [], 'program': {}}
    prog = md_section(md, 'The program')
    for key in ('Name', 'Type', 'For', '90-day outcome', 'Format', 'Cadence', 'Duration', 'Costs the agent', 'Not this'):
        v = kv(prog, key)
        if v: o['program'][key] = clean(re.sub(r'\s*\((?:the program and|alternates|outcome-based)[^)]*\)', '', v), demo)
    o['name'] = clean(re.split(r'\s*\(', o['program'].get('Name', ''))[0], demo) if o['program'].get('Name') else ''
    u = md_section(md, 'UVP')
    if u:
        q = re.search(r'"([^"\n]{20,})"', u)
        if q: o['uvp'] = clean(q.group(1), demo)
    br = md_section(md, 'Content branches')
    for l in br.split('\n'):
        m = re.match(r'^-\s+\*\*(.+?)\*\*\s*(?:\([^)]*\))?\s*[—-]?\s*(.*)$', l.strip())
        if m: o['branches'].append((clean(m.group(1), demo), clean(m.group(2), demo)))
    o['status'] = clean(o['status'], demo); o['join_gated'] = clean(o['join_gated'], demo); o['link'] = clean(o['link'], demo)
    o['community'] = clean(re.split(r'\s+—\s+|\s+\(', o['community'])[0], demo)
    return o

def parse_brand(md, demo):
    b = {'feel': '', 'swatches': [], 'fonts': '', 'logo': '', 'tagline': '', 'package': [], 'brief_date': None, 'direction_done': False, 'reaction': ''}
    d = md_section(md, 'Direction')
    if d and '[' not in (kv(d, 'Feel (the member\'s own sentence)') or kv(d, 'Feel')):
        b['direction_done'] = True
    feel = first_kv(d, ["Feel (the member's own sentence)", 'Feel'])
    b['feel'] = clean(feel.strip('"'), demo)
    for m in re.finditer(r'([A-Za-z /]+?)(?:\s*\([^)]*\))?:\s*(#[0-9A-Fa-f]{6})\s*[—-]\s*([^·\n(]+?)(?:\s*\(([^)]*)\))?(?=\s*·|\s*$)', d, re.M):
        role, hexc, name, note = m.group(1).strip(), m.group(2).upper(), m.group(3).strip(), (m.group(4) or '').strip()
        b['swatches'].append((hexc, name[0].upper() + name[1:], (role.lower() + (': ' + note if note else '')).strip()))
    b['fonts'] = clean(first_kv(d, ['Font direction', 'Fonts']), demo)
    b['logo'] = clean(first_kv(d, ['Logo direction', 'Logo']), demo)
    b['tagline'] = clean(first_kv(d, ['Tagline (options or the chosen one)', 'Tagline']), demo)
    b['reaction'] = clean(kv(d, "Member's reaction"), demo)
    pk = md_section(md, 'The Design Package')
    for m in re.finditer(r'\[( |x|X)\]\s*`?([a-z\-]+)`?\s*\[([^\]]*)\]', pk):
        b['package'].append((m.group(2), m.group(1).lower() == 'x', m.group(3)))
    m = re.search(r'## Design Package brief \(last issued (20\d\d-\d\d-\d\d)', md)
    if m: b['brief_date'] = date_in(m.group(1))
    return b

def parse_magnets(md, demo):
    m = {'name': '', 'keyword': '', 'funnel': '', 'download': '', 'for': '', 'status': '', 'asof': ''}
    cur = md_section(md, 'Current magnet')
    line = next((l for l in cur.split('\n') if l.strip().startswith('**')), '')
    if line and '[Magnet Name]' not in line:
        mm = re.match(r'\*\*(.+?)\*\*', line)
        m['name'] = clean(mm.group(1), demo) if mm else ''
        for seg in line.split(' · ')[1:]:  # each segment after the bold name is "key: value" (the locked shape writes "as of 2026-…" without a colon)
            r = re.match(r'\s*(keyword|funnel URL|download link|for|as of):?\s+(.+?)\s*$', seg.strip())
            if r: m[{'funnel URL': 'funnel', 'download link': 'download', 'as of': 'asof'}.get(r.group(1), r.group(1))] = clean(r.group(2), demo)
    for r in table_under(md, 'Magnets')[1:]:
        if len(r) >= 5 and r[1].strip() and (not m['name'] or r[1].strip() == m['name']):
            m['status'] = clean(r[4], demo).split('(')[0].strip() if r[4] else m['status']
            if not m['name']: m['name'] = clean(r[1], demo)
    return m

# ───────────────────────── the shape of the board (what never changes) ─────────────────────────
SYSTEMS = [
    ('brand', 'BRAND', 3, 'Your brand direction', 'Plugin 1 · the Brain’s brand chat · the Design Studio in Claude Design'),
    ('offer', 'OFFER', 2, 'Your Partner Offer', 'Plugin 1 · the Brain’s offer builder'),
    ('lead-magnet', 'LEAD MAGNET', 2, 'Your lead magnet and its funnel', 'Plugin 3 · Lead Magnets & Opt-In Funnels'),
    ('short-form', 'SHORT-FORM', 3, 'Your short-form system', 'Plugin 4 · the Short-Form Attraction Engine'),
    ('youtube', 'YOUTUBE', 4, 'Your YouTube system', 'Plugin 6 · the Long-Form Authority Engine'),
    ('conversion', 'CONVERSION', 5, 'Your conversion system', 'Plugin 7 · the Conversation & Conversion Engine'),
    ('ai-admin', 'AI ADMIN', 5, 'Your AI Admin', 'Plugin 8 · the AI Admin for agent attraction'),
    ('events', 'EVENTS', 6, 'Your events and workshops', 'Plugin 9 · Events & Workshops'),
]
READS = {
    'brand': ['who-you-are', 'your-story', 'your-voice'],
    'offer': ['what-you-teach', 'your-story', 'your-proof', 'who-you-help', 'your-voice', 'your-brokerage'],
    'lead-magnet': ['offer', 'what-you-teach', 'who-you-help', 'your-story', 'your-proof', 'your-voice'],
    'short-form': ['offer', 'what-you-teach', 'your-story', 'your-proof', 'who-you-help', 'your-voice', 'lead-magnet'],
    'youtube': ['offer', 'what-you-teach', 'your-brokerage', 'your-story', 'your-proof', 'who-you-help', 'your-numbers', 'your-voice'],
    'conversion': ['who-you-help', 'your-story', 'your-brokerage', 'your-proof', 'your-voice', 'your-numbers', 'offer'],
    'ai-admin': ['your-numbers', 'your-voice', 'who-you-help', 'your-proof'],
    'events': ['offer', 'what-you-teach', 'who-you-help', 'your-proof', 'your-voice', 'your-numbers'],
}
SYS_ACTIONS = {
    'brand': [('show my design package brief', 'Re-opens the brief to paste into Claude Design.'), ('update my attraction brand direction', 'Change anything: a colour, the tagline, the logo call.')],
    'offer': [('refine my partner offer', 'Change the name, the steps, the first 30 days, the weekly rhythm. One card, say yes.'), ('build my Week 3 kit', 'The one file for Claude Design in Week 3: your offer, everything that promotes it, and your guide and page once they are written.'), ('paste my compliance link', 'Closes the open question on join-gated packages from your brokerage’s own rules.')],
    'lead-magnet': [('finish my agent lead magnet', 'Picks up exactly where this campaign stopped.'), ('add my guide to my kit', 'Puts the guide and the page into your Week 3 Kit, the one file for Claude Design.'), ('deliver my guide', 'The keyword flow for ManyChat, the delivery email, and the story that offers it.')],
    'short-form': [('set up my attraction short-form', 'The whole Week 3 journey in one sitting, with nothing re-asked.')],
    'youtube': [('set up my YouTube for agents', 'One channel question, then no stops: the channel, the Game Plan, the board, the workflows, the first video.')],
    'conversion': [('launch conversion', 'Reads your Brain and your Top 50 and routes you: a call tomorrow, an objection you heard, a pasted transcript.'), ('set up my sales system', 'The Partner Call machine: the booking calendar, the application questions, the pipeline stages in your CRM, the reminders.')],
    'ai-admin': [('set up my attraction admin', 'Reads your Brain, calendar and inbox and hands you the first brief before it asks anything.'), ('my morning brief', 'On demand, any day.')],
    'events': [('plan my agent event', 'One recommendation with the why; it resumes wherever an event already stands.')],
}
INNER = [
    ('who-you-are', 'WHO YOU ARE', 'Who you are', 'From Conversation 1 · questions 1 to 9', ['offer', 'lead-magnet', 'short-form', 'youtube', 'conversion', 'ai-admin', 'events'],
     [('check my attraction brain', 'Audits your whole Brain and names the one thing to add.'), ('import my attraction materials', 'An old deck, a bio or a CRM export: it reads them so you type less.')], 'identity/profile.md', ()),
    ('your-story', 'YOUR STORY', 'Your story', 'From Conversation 1 · questions 7, 12 and 13 · Conversation 3 · and your spoken WHY', ['lead-magnet', 'short-form', 'youtube', 'conversion', 'events'],
     [('add an attraction story', 'File a new moment, tagged with the agent it lands with and where it gets used.'), ('refresh my attraction story bank', 'Re-mines your answers for the stories a video, a call or an objection can use.')], 'identity/journey.md', ('Use it', 'Why join me')),
    ('your-brokerage', 'YOUR BROKERAGE', 'Your brokerage story', 'From Conversation 1 · questions 9 to 11 and 13', ['conversion', 'youtube', 'lead-magnet'],
     [('capture this for my attraction brain', 'Anything that changes at your brokerage, in one line from the car; it lands in the right file.'), ('paste my compliance link', 'The rules come from your brokerage’s own page. No questions.')], 'identity/brokerage-model.md', ()),
    ('what-you-teach', 'WHAT YOU TEACH', 'Your unique approach', 'From Conversation 2 · questions 14 to 17', ['offer', 'lead-magnet', 'short-form', 'youtube', 'conversion', 'events'],
     [('refine my partner offer', 'Change anything about the program this page became.'), ('check my attraction brain', 'If a strategy is missing here, the audit will say so.')], 'identity/strategy.md', ()),
    ('your-proof', 'YOUR PROOF', 'Your proof', 'From Conversation 3 · questions 18 to 22', ['lead-magnet', 'short-form', 'youtube', 'conversion', 'events'],
     [('my agent proof', 'Add a result, a review from an agent, or a partner’s written OK.'), ('attraction win', 'Log a win from the car. It lands here, dated.')], 'identity/proof.md', ()),
    ('who-you-help', 'WHO YOU HELP', 'Who your story speaks to', 'Worked out from your answers · never asked', ['offer', 'lead-magnet', 'short-form', 'youtube', 'conversion', 'ai-admin', 'events'],
     [('refine who I attract', 'Sharpen the picture once your content starts pulling a different kind of agent.'), ('add a second avatar', 'When a second group keeps showing up in your conversations.')], 'identity/avatars.md', ()),
    ('your-numbers', 'YOUR NUMBERS', 'Your numbers', 'From Conversation 4 · questions 23 to 26', ['ai-admin', 'conversion', 'youtube', 'short-form'],
     [('am I on pace to my join target', 'The honest answer from your scorecard, in one line.'), ('refresh my attraction plan', 'At the end of the quarter: the next 90 days from what actually happened.')], '', ()),
    ('your-voice', 'YOUR VOICE', 'Your voice', 'The three answers you gave out loud, kept as you said them', ['lead-magnet', 'short-form', 'youtube', 'conversion', 'ai-admin', 'events'],
     [('refresh my attraction voice print', 'After a few weeks of content, re-read how you actually talk.'), ('add my writing samples to my attraction brain', 'A text, a caption, an email, a post: how you write to agents.')], 'identity/voice.md', ()),
    ('whats-next', 'WHAT’S NEXT', 'What’s next', 'Rewritten every time a week lands', [], [], '', ()),
]
FUNNEL_ORDER = ['Hero — the pre-headline, your video, the attraction line, and the opt-in button.', 'Problem — the pain in the agent’s own words.', 'Product — the guide and what’s inside; the opt-in button again.', 'Who I am.', 'Journey — your story, the turning point.', 'Offer — what you teach and your weekly call, in the register your brokerage allows.', 'Why join me — the lesson and the mentorship, never a package.', 'Proof — your results as your Brain states them; a partner’s result only with their written OK.', 'The organization — what you do together, and who’s in it.', 'Book a call — the second path, for the agent who is already ready.', 'Opt-in — the last button, the same words every time.']

def state_of(sysid, ctx):
    """built · now · soon for a system, from the Brain's own files (then capped by the cohort week)."""
    cfg, offer, mag, brand = ctx['config'], ctx['offer_md'], ctx['magnets'], ctx['brand']
    st = 'soon'
    if sysid == 'brand':
        st = 'built' if brand['direction_done'] else 'soon'
    elif sysid == 'offer':
        st = 'built' if re.match(r'(built|finalized)', offer['status'], re.I) else 'soon'
    elif sysid == 'lead-magnet':
        if mag['name']:
            live = mag['funnel'] and 'not live' not in mag['funnel'].lower() and mag['funnel'].startswith('http')
            st = 'built' if (live or mag['status'] == 'live') else 'now'
        elif ctx['brain_magnet'] and 'not live' in ctx['brain_magnet'].lower():
            st = 'now'
    elif sysid == 'short-form':
        st = 'built' if ('short-form' in cfg['blocks'] or (ctx['pillars_md'] and '[' not in ctx['pillars_md'][:600] and '**Content pillars' in ctx['pillars_md'])) else 'soon'
    elif sysid == 'youtube':
        st = 'built' if ('youtube' in cfg['blocks'] or ctx['files'].get('identity/channel.md')) else 'soon'
    elif sysid == 'conversion':
        st = 'built' if (any(k.startswith('conversion') for k in cfg['blocks']) or ctx['files'].get('identity/sales-system.md')) else 'soon'
    elif sysid == 'ai-admin':
        st = 'built' if any(k.startswith('ai admin') for k in cfg['blocks']) else 'soon'
    elif sysid == 'events':
        st = 'built' if (any(k.startswith('events') for k in cfg['blocks']) or re.search(r'^## .*\d{4}-\d\d-\d\d', ctx['files'].get('memory/events.md', ''), re.M)) else 'soon'
    week = ctx['week']
    syswk = next(w for i, _, w, _, _ in SYSTEMS if i == sysid)
    if week and syswk > week and st != 'soon' and ctx['demo']:  # a demo renders its cohort week; a real member's built system is built
        st = 'soon'
    return st

def status_rows(rows):
    return '\n'.join('@status: %s | %s | %s' % (a, b, c) for a, b, c in rows)

def build_inner(ctx):
    demo, book, files = ctx['demo'], ctx['book'], ctx['files']
    pages = []
    for n, (pid, label, title, source, feeds, actions, fname, drop) in enumerate(INNER, start=1):
        sec = book.get(n, {})
        body = ''
        if sec.get('body'):
            body = sec['body']
            if pid == 'what-you-teach' and ctx['offer_built']:
                body = '@note: In Week 2 this page became your Partner Offer, %s. The offer page holds the program; this page holds the raw material it came from.\n@link: offer | Open your Partner Offer\n\n' % (ctx['offer_md']['name'] or 'your program') + body
        if pid == 'your-numbers':
            body = (body + '\n\n' if body else '') + '@link: goals | Open your goals and your tracker'
        if pid == 'whats-next':
            body = ctx['whats_next_body']
        extra_md = files.get(fname, '') if fname and not is_template(files.get(fname, '')) else ''
        if pid == 'your-voice':
            vp = files.get('identity/voice-print.md', '')
            if vp and not is_template(vp): extra_md = (extra_md + '\n\n## How you talk\n' + strip_md_header(vp)) if extra_md else vp
        if extra_md:
            conv = md_to_book(extra_md, demo, drop_sections=drop)
            if conv:
                body = (body + '\n\n## Everything on file\n' if body else '') + conv
        if not body:
            body = '@note: Nothing is written here yet. Your Brain fills this page in Week 1.'
        tag = sec.get('tag', '')
        meta = ['Section %d of 9 in your Brain Book' % n, source] + (['Demo'] if demo else [])
        pages.append({'id': pid, 'label': label, 'title': title, 'tagline': tag, 'meta': meta, 'feeds': feeds, 'actions': [{'p': p, 'n': q} for p, q in actions], 'body': body})
    return pages

def build_outer(ctx):
    demo, offer, mag, brand, cfg = ctx['demo'], ctx['offer_md'], ctx['magnets'], ctx['brand'], ctx['config']
    pages = []
    for sysid, label, week, title, plugin in SYSTEMS:
        st = ctx['states'][sysid]
        tag, line, body = '', '', ''
        if sysid == 'brand':
            if st == 'built':
                tag = '“%s”' % brand['feel'] if brand['feel'] else 'Decided in your Week 3 brand chat; the kit is built in Claude Design.'
                kit_left = [l for l, ok, note in brand['package'] if not ok]
                line = 'Direction set' + (' and the brief issued' if brand['brief_date'] else '') + ('. The kit itself is not in 02 · Brand yet.' if kit_left else '. The kit is in 02 · Brand.')
                rows = [('The brand chat: your inventory, one plain question at a time', 'done', ''), ('The creative direction, derived from your Brain and your three spoken answers', 'done', brand['reaction'] and ('your reaction: ' + brand['reaction']) or '')]
                rows.append(('The Design Package brief', 'done' if brand['brief_date'] else 'soon', ('issued ' + long_date(brand['brief_date']) + ', saved in 02 · Brand') if brand['brief_date'] else 'not issued yet'))
                for l, ok, note in brand['package']:
                    rows.append((('The logo' if 'logo' in l else 'The style sheet' if 'style' in l else 'The brand kit') + ', in Claude Design', 'done' if ok else 'soon', note))
                body = status_rows(rows)
                if brand['feel']: body += '\n\n## The feel, in your words\n>> “%s”' % brand['feel']
                if brand['swatches']: body += '\n\n## Colours (proposed by your Brain; the style sheet confirms)\n' + '\n'.join('@swatch: %s | %s | %s' % s for s in brand['swatches'])
                body += '\n\n' + md_to_book(ctx['files'].get('identity/brand-visual.md', ''), demo)
            else:
                tag = 'Your brand is Week 3’s chat, run alongside Claude Design.'
                line = 'Your creative direction, then the logo, the style sheet and the kit in Claude Design.'
                body = status_rows([('The brand chat: your inventory, one plain question at a time', 'soon', ''), ('The creative direction, derived from your Brain and your three spoken answers', 'soon', 'you just say yes'), ('The Design Package brief for Claude Design', 'soon', ''), ('The logo, the style sheet and the brand kit', 'soon', 'three runs in Claude Design')]) + '\n\n## What lands on this board when it’s done\nThis dot turns green. Your colours, fonts, logo call and tagline appear on this page.'
        elif sysid == 'offer':
            if st == 'built':
                doc = ctx['offer_doc']
                title = offer['name'] or (doc and doc['name']) or title
                tag = 'Your Partner Offer: the program an agent partners with you for, and your own pages on how to build it, where to host it and how to talk about it.'
                line = 'Named, defined and written.' + (' Lives inside %s.' % offer['community'] if offer['community'] else '')
                if doc and doc['body']:
                    body = ('>> ' + doc['oneliner'] + '\n\n' if doc['oneliner'] else '') + '@toc\n' + doc['body']
                else:
                    body = md_to_book(ctx['files'].get('identity/offer.md', ''), demo)
            else:
                tag = 'Built in Week 2 from what you can teach: one card, you say yes, the document builds.'
                line = 'Your program: named, defined and written. Week 2.'
                seeds = md_to_book(ctx['files'].get('identity/offer.md', ''), demo, keep_sections=('What worked for them', 'The three layers', 'The mistakes agents'))
                body = status_rows([('The offer card: an outcome-based name with two alternates, the type, who it is for, the 90-day outcome, the format and cadence, a named framework of 3 to 7 steps', 'soon', 'shown, not asked'), ('The Partner Offer document, with your pages: how to create it, start with your upline, the brokerage rule, where to host it, the marketing language, your content branches', 'soon', '')]) + ('\n\n## What it will build from\n' + seeds if seeds else '')
        elif sysid == 'lead-magnet':
            if st in ('built', 'now'):
                title = 'Your lead magnet and its funnel'
                tag = ('%s, written. The funnel is live.' % mag['name']) if st == 'built' else ('%s, written. The funnel is not live yet.' % (mag['name'] or 'Your guide'))
                line = 'The guide is written; the funnel is live.' if st == 'built' else 'The guide is written. Design, the page and delivery are left.'
                rows = [('Your Partner Offer', 'done' if ctx['offer_built'] else 'soon', offer['name'] or ''), ('ONE lead magnet recommended; you said yes', 'done', mag['name'] or ''), ('The guide, written', 'done' if mag['status'] in ('written', 'designed', 'live') or mag['name'] else 'soon', ''), ('The guide, designed in Claude Design', 'done' if mag['status'] in ('designed', 'live') else 'soon', ''), ('The opt-in page, live', 'done' if st == 'built' else 'soon', mag['funnel'] if mag['funnel'] and 'not live' not in mag['funnel'] else 'the outline is the copy; the design keys on it'), ('Delivery: the keyword flow, the delivery email, the 3-frame story', 'done' if st == 'built' else 'soon', '')]
                body = ('>> By the end of this week you have ONE lead magnet, written and designed, with its funnel outline — and your unique value proposition broken down: your offer explained in detail and how to create it, its name, the marketing language to use, and where to host it.\n@note: Mike’s words for Week 2.\n\n' if (ctx['week'] or 0) <= 2 else '') + '## Where it stands\n' + status_rows(rows)
                body += '\n\n## The guide\n' + '\n'.join('| %s | %s |' % kvp for kvp in [('Name', mag['name'] or '—'), ('Keyword', (mag['keyword'] + ' — “Comment %s and I’ll send it.” It never changes once content has used it.' % mag['keyword']) if mag['keyword'] else '—'), ('For', mag['for'] or '—'), ('Funnel', mag['funnel'] or 'not live yet'), ('Download', mag['download'] or 'not live yet')] if kvp[1])
                body += '\n\n## The funnel outline: the opt-in page, in the order it reads\n' + '\n'.join('%d. %s' % (i + 1, t) for i, t in enumerate(FUNNEL_ORDER)) + '\n\nEvery opt-in button opens the one pop-up (first name, email, phone). Submitting lands on the thank-you page with the instant download and the invitation to a call. The compliance stamp is the footer of both.'
                mg = ctx['files'].get('memory/magnets.md', '')
                if mg: body += '\n\n## On file\n' + md_to_book(mg, demo, drop_sections=('Current magnet', 'Intake'))
            else:
                tag = 'Week 2: ONE guide, written and designed, with its funnel. Built from your offer.'
                line = 'ONE guide and its funnel, built from your offer. Week 2.'
                body = status_rows([('ONE lead magnet recommended from your offer; you say yes', 'soon', 'never three to choose from'), ('The guide, written in your voice', 'soon', ''), ('The sales funnel outline: the opt-in page, the pop-up, the thank-you page', 'soon', ''), ('Your guide and page go into your Week 3 Kit, the one file for Claude Design', 'soon', ''), ('The delivery flow and the nurture', 'soon', '')]) + '\n\n## What lands on this board when it’s done\nThis dot turns amber while the funnel is being built, then green when it is live.'
        elif sysid == 'short-form':
            tag = 'Lights up in Week 3. This page shows what the system will hand you and what it already knows about you.' if st == 'soon' else 'Your pillars, your calendar and your weekly rhythm, from your Brain.'
            line = 'Your pillars, a 30-day calendar and the board. Lights up in Week 3.' if st == 'soon' else 'Pillars, the 30-day calendar and the board are built.'
            branches = ctx['offer_md']['branches']
            if st == 'soon':
                body = '## What you’ll have at the end of Week 3\n' + status_rows([('Your profiles, optimized on every platform you use, as a copy-paste pack', 'soon', 'step 1'), ('The Short-Form Game Plan: who you attract, the one-liner, the keyword, the two CTAs, five pillars with three angles each, the format mix and weekly cadence, a 30-hook bank, a dated 30-day calendar of twenty posts, the daily stories rhythm', 'soon', 'step 2'), ('Your Notion content board with the next 30 days mapped as dated cards; one board, shared with YouTube in Week 4', 'soon', 'step 3'), ('Three scheduled workflows from one consent card: the Monday Week Plan, the Friday note, optional daily stories; drafted, never posted without you', 'soon', 'step 4'), ('Your first Reel: the script, the hook, the caption and the comment-to-DM flow', 'soon', 'step 5')])
                if branches: body += '\n\n## Your pillars will come from your content branches first\nThe Game Plan builds its pillars, angles and titles from the branches of your offer before anything else, then from the rest of your Brain.\n' + '\n'.join('• ' + b[0] for b in branches)
                body += '\n\n## What lands on this board when it’s done\nThis dot turns green. Your pillars and the next 30 days appear on this page, and your weekly content target starts counting on your Goals page.'
            else:
                body = md_to_book(ctx['pillars_md'], demo) if not is_template(ctx['pillars_md']) else '@note: Built; the pillars file is still being written.'
                if cfg['blocks'].get('short-form'): body = '@note: ' + cfg['blocks']['short-form']['line'] + '\n\n' + body
        elif sysid == 'youtube':
            yt = ctx['yt_name']
            tag = ('Lights up in Week 4.' + (' Your channel is already named: %s.' % yt if yt else '')) if st == 'soon' else 'Your channel, your Game Plan and your board, from your Brain.'
            line = 'Your channel, the Game Plan and your first video. Lights up in Week 4.' if st == 'soon' else 'The channel, the Game Plan and the board are built.'
            if st == 'soon':
                knows = []
                if ctx['org']['rows']: knows.append('Your interview lane starts with ' + ' and '.join(r['agent'] for r in ctx['org']['rows'][:2]) + ', and the agents on your Top 50.')
                if ctx['offer_md']['branches']: knows.append('Your niche lanes come from your content branches: ' + ', '.join(b[0].lower() for b in ctx['offer_md']['branches'][:3]) + '.')
                knows.append('Your model lane is your brokerage story, told the way you tell it.')
                if ctx['goals']['twelve']: knows.append('Your goal-math starts from %d agents in twelve months.' % ctx['goals']['twelve'])
                body = '## What you’ll have at the end of Week 4\n' + status_rows([('Your channel, optimized for the agents you attract, as copy-paste blocks', 'soon', ('channel name on file: ' + yt) if yt else ''), ('The YouTube Game Plan on Mike’s three categories, niche authority, interviews and model, and the 8-video cycle: three niche lanes, the interview lane from your organization and your Top 50, the model lane, about fifty titles, the goal-math from your numbers', 'soon', ''), ('The same Notion board, YouTube view: the next 30 days of videos mapped at your cadence', 'soon', ''), ('Three scheduled workflows from one consent card, the Monday Kickoff on by default; draft-only', 'soon', ''), ('Your first video: the idea, the research, the script in your voice, the thumbnail brief and the SEO package', 'soon', '')]) + '\n\n## What it already knows\n' + '\n'.join('• ' + k for k in knows) + '\n\n## What lands on this board when it’s done\nThis dot turns green. The channel link, the three lanes and the next 30 days of videos appear here.'
            else:
                ch = ctx['files'].get('identity/channel.md', '')
                body = (md_to_book(ch, demo) if ch and not is_template(ch) else '') or ('@note: ' + cfg['blocks'].get('youtube', {}).get('line', 'Built.'))
        elif sysid == 'conversion':
            tag = 'Lights up in Week 5. Conversations, calls and the partner call, run from your Brain and your Top 50.' if st == 'soon' else 'Your conversations, calls and the partner call, from your Brain.'
            line = 'Conversations, calls and the partner call. Lights up in Week 5.' if st == 'soon' else 'Built: the partner call machine.'
            pipe = ctx['pipeline']
            waiting = ''
            if pipe['rows']:
                conv = [r['agent'] for r in pipe['rows'] if r['stage'].lower().startswith('conversation')]
                idn = [r['agent'] for r in pipe['rows'] if r['stage'].lower().startswith('identified')]
                waiting = '\n\n## What it will find waiting\n%d agent%s already on your pipeline' % (len(pipe['rows']), '' if len(pipe['rows']) == 1 else 's') + (': %d in conversation (%s)' % (len(conv), ', '.join(conv)) if conv else '') + (', %d identified (%s)' % (len(idn), ', '.join(idn)) if idn else '') + '.'
            body = ('## What you’ll have in Week 5\n' + status_rows([('Agent Intel: a pre-call brief on any agent you’re about to talk to', 'soon', ''), ('The Conversation Starter and the DM-to-call flow, in your voice', 'soon', ''), ('Call prep for every booked call, and the partner call with the enrollment script', 'soon', ''), ('The three-way call with your upline, prepared', 'soon', ''), ('The Objection Handling Coach, fifteen objections with role-play, and the Conversation Coach that audits a call from a pasted transcript', 'soon', ''), ('Follow-up and re-engagement for the agent who went quiet', 'soon', ''), ('Sales OPS: your booking page, the application questions, the locked pipeline stages in your CRM, show-up reminders, the setter, your call block and the scorecard', 'soon', ('booking link on file: ' + ctx['booking']) if ctx['booking'] else '')]) + '\n\n## How it uses your Brain\nThe partner call opens with your story, not the model. Proof is quoted exactly as your Brain states it. The brokerage conversation is a second call, with the documents. Every draft reads your voice page first.' + waiting + '\n\n## What lands on this board when it’s done\nThis dot turns green, and calls booked and calls held start counting from your CRM on your Goals page.') if st == 'soon' else (md_to_book(ctx['files'].get('identity/sales-system.md', ''), demo) or '@note: Built.')
        elif sysid == 'ai-admin':
            tag = 'Lights up in Week 5. The Morning Brief, the pipeline and the follow-up queue, drafted every day, sent only by you.' if st == 'soon' else 'Your Morning Brief, your pipeline and your follow-up queue.'
            line = 'Your Morning Brief and the pipeline. Lights up in Week 5.' if st == 'soon' else 'The Morning Brief runs every day.'
            tgt = ctx['goals_data']['activity'] or 'your weekly activity'
            body = ('## What you’ll have in Week 5\n' + status_rows([('Your first Morning Brief, handed to you before it asks anything: today’s calls with a prep line each, agent inquiries with reply drafts, the follow-ups due drafted in your voice, content due, the week so far, three moves, one coaching note', 'soon', ''), ('Your pipeline at a glance on the locked stages, with your CRM', 'soon', ''), ('One consent card: the Morning Brief and the Daily Follow-Up Queue every morning, plus your Daily Debrief if it isn’t on', 'soon', 'drafted, never sent without you'), ('The weekly scorecard and the Weekly Recruiting CEO Review; the Team Wins newsletter; VA task packs; the Monthly KPI Review', 'soon', '')]) + '\n\n## What it measures you against\nYour own numbers: ' + tgt + '. Under 400 words a morning, no questions.\n\n## What lands on this board when it’s done\nThis dot turns green. The Today tile starts coming from the Morning Brief instead of last night’s debrief, and the weekly rows on your Goals page are written for you every Friday.') if st == 'soon' else ('@note: ' + next((b['line'] for k, b in cfg['blocks'].items() if k.startswith('ai admin')), 'Built.'))
        elif sysid == 'events':
            tag = 'Lights up in Week 6. Live, virtual and evergreen events that teach, with the invite to a conversation as the close.' if st == 'soon' else 'Your events, from the brief to the follow-up.'
            line = 'Live, virtual and evergreen events. Lights up in Week 6.' if st == 'soon' else 'Your first event is planned.'
            first = ('A workshop on %s, live, the way you teach it. The guide is the hand-out; the call is the close. Proposed from your offer; the Event Brief decides it with you.' % (ctx['known_for'] or 'what you teach')) if ctx['known_for'] else ''
            body = ('## What you’ll have in Week 6\n' + status_rows([('The Event Brief: the objective, the audience from who your story speaks to, the transformation, the topic aligned with your offer, brokerage-neutral positioning', 'soon', ''), ('The format, recommended with the why: a live local workshop, a virtual training on Zoom, or an evergreen webinar', 'soon', 'never a menu'), ('The run-of-show, the registration copy, the promo calendar, drafted and never sent', 'soon', ''), ('The follow-up sequence into your pipeline, and the analytics', 'soon', '')]) + (('\n\n## The obvious first event, from your Brain\n' + first) if first else '') + '\n\n## What lands on this board when it’s done\nThis dot turns green, and by then the whole outer ring is lit: the picture of the system you built in six weeks.') if st == 'soon' else (md_to_book(ctx['files'].get('memory/events.md', ''), demo) or '@note: Built.')
        meta = ['Week %d · %s' % (week, {'built': 'built', 'now': 'this week', 'soon': 'coming'}[st]), plugin] + (['Demo'] if demo else [])
        pages.append({'id': sysid, 'label': label, 'week': 'W%d' % week, 'state': st, 'title': title, 'tagline': tag, 'line': line, 'meta': meta, 'reads': READS[sysid], 'actions': [{'p': p, 'n': q} for p, q in SYS_ACTIONS[sysid]], 'body': body})
    return pages

# ───────────────────────── the numbers, the day, the week ─────────────────────────
def parse_date_cell(c):
    d = date_in(c)
    return d

def derive_goals(ctx):
    g, sc, today = ctx['goals'], ctx['scorecard'], ctx['today']
    t = {'conv': 0, 'held': 0, 'booked': 0, 'joins': 0, 'content': 0, 'agents': 0}
    for r in sc['targets'][1:]:
        if len(r) < 4: continue
        k = r[0].lower()
        if 'agents' in k: t['agents'] = num(r[2])
        elif 'conversation' in k: t['conv'] = num(r[2]); t['wconv'] = num(r[3])
        elif 'calls' in k: t['held'] = num(r[2]); m = re.search(r'(\d+)\s*booked', r[3]); t['booked'] = int(m.group(1)) if m else num(r[3])
        elif 'join' in k: t['joins'] = num(r[2])
        elif 'content' in k: t['content'] = num(r[2]); t['wcontent'] = sum(int(x) for x in re.findall(r'\d+', r[3])) or 0
    def rowvals(r): return [num(c) for c in r[1:6]] if len(r) >= 6 else [0, 0, 0, 0, 0]
    weekly = [(parse_date_cell(r[0]), rowvals(r), r[6] if len(r) > 6 else '') for r in sc['weekly'][1:]]
    daily = [(parse_date_cell(r[0]), rowvals(r), r[6] if len(r) > 6 else '') for r in sc['daily'][1:]]
    weekly = [w for w in weekly if w[0]]; daily = [d for d in daily if d[0]]
    last_wk = max((w[0] for w in weekly), default=None)
    covered_until = (last_wk + dt.timedelta(days=6)) if last_wk else None
    so = [0, 0, 0, 0, 0]
    for _, v, _ in weekly: so = [a + b for a, b in zip(so, v)]
    for d, v, _ in daily:
        if not covered_until or d > covered_until: so = [a + b for a, b in zip(so, v)]
    monday = today - dt.timedelta(days=today.weekday())
    wk = [0, 0, 0, 0, 0]
    for d, v, _ in daily:
        if d >= monday: wk = [a + b for a, b in zip(wk, v)]
    score = (weekly[-1][2] if weekly else (daily[-1][2] if daily else '')).lower()
    day = ((today - g['q_start']).days + 1) if g['q_start'] else 0
    quarter = (g['q_start'].strftime('%b ') + str(g['q_start'].day) + ' → ' + g['q_end'].strftime('%b ') + str(g['q_end'].day)) if g['q_start'] and g['q_end'] else ''
    slice_days = []
    for i in range(5):
        d = monday + dt.timedelta(days=i)
        row = next((v for dd, v, _ in daily if dd == d), None)
        st = 'done' if (row and row[0] >= sc['slice_conv']) else ('today' if d == today else '')
        slice_days.append({'d': 'MTWTF'[i], 's': st})
    agents_now = ctx['org']['count'] or g['today']
    # pace against the 30-60-90 ramp (piecewise linear from the lock to day 30, 60, 90)
    def expected(start, d30, d60, d90, d):
        pts = [(0, start), (30, d30), (60, d60), (90, d90)]
        if d <= 0: return start
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if d <= x1: return y0 + (y1 - y0) * (d - x0) / float(x1 - x0)
        return d90
    actual_map = {'conversations': so[0], 'calls held': so[2], 'joins': so[3], 'content shipped': so[4], 'agents in organization': agents_now}
    pace = []
    for r in g['rows_3060'][1:]:
        if len(r) < 4 or not r[0]: continue
        key = r[0].strip().lower()
        if key not in actual_map: continue
        start = g['today'] if key.startswith('agents') else 0
        exp = expected(start, num(r[1]), num(r[2]), num(r[3]), day) if day else start
        exp_i = int(exp + 0.5)
        act = actual_map[key]
        st = 'on pace' if (exp_i == 0 and act <= 0) or (act >= exp_i and not (exp_i > 0 and act >= 1.5 * exp_i)) else ('ahead' if (exp_i == 0 and act > 0) or (exp_i > 0 and act >= 1.5 * exp_i) else 'behind')
        pace.append({'label': r[0].strip(), 'actual': act, 'expected': exp_i, 'd90': num(r[3]), 'status': st})
    # the pipeline funnel, in the locked stage order
    stages = ['Identified', 'Conversation', 'Call booked', 'Call held', '3-way', 'Joined', 'Onboarded', 'Active', 'Parked']
    counts = {}
    cl = ctx['pipeline']['counts']
    for st_ in stages:
        m = re.search(re.escape(st_) + r'\s+(\d+)', cl)
        if m: counts[st_] = int(m.group(1))
    if not counts:
        for r in ctx['pipeline']['rows']:
            for st_ in stages:
                if r['stage'].lower().startswith(st_.lower()): counts[st_] = counts.get(st_, 0) + 1
    funnel = [{'stage': st_, 'n': counts.get(st_, 0)} for st_ in stages if st_ != 'Parked'] + ([{'stage': 'Parked', 'n': counts['Parked']}] if counts.get('Parked') else [])
    # week by week: the Friday rows, then the current partial week
    weeks = [{'label': d.strftime('%b ') + str(d.day), 'conv': v[0], 'booked': v[1], 'held': v[2], 'joins': v[3], 'content': v[4], 'partial': False} for d, v, _ in sorted(weekly, key=lambda w: w[0])]
    if any(d >= monday for d, _, _ in daily) and not any(w[0] == monday for w in weekly):
        weeks.append({'label': monday.strftime('%b ') + str(monday.day), 'conv': wk[0], 'booked': wk[1], 'held': wk[2], 'joins': wk[3], 'content': wk[4], 'partial': True})
    acts = []
    if t.get('wconv'): acts.append('%d conversations' % t['wconv'])
    if t.get('booked'): acts.append('%d calls booked' % t['booked'])
    fu = re.search(r'Follow-ups:\s*(\d+)', ctx['files'].get('identity/goals.md', ''))
    if fu: acts.append('%s follow-ups' % fu.group(1))
    ctext = next((r[3] for r in sc['targets'][1:] if len(r) >= 4 and 'content' in r[0].lower()), '')
    if ctext and ctext != '—': acts.append(ctext.strip() + ' of content')
    activity = ' · '.join(acts) + (' · every week' if acts else '')
    return {'activity': activity, 'pace': pace, 'funnel': funnel, 'weeks': weeks, 'wconv': t.get('wconv', 0),'today': agents_now, 'twelve': g['twelve'], 'longTerm': g['long'], 'hours': g['hours'], 'day': day, 'quarter': quarter, 'score': score,
            'q90': {'conv': t['conv'], 'held': t['held'], 'joins': t['joins'], 'content': t['content'], 'agents': t['agents']},
            'sofar': {'conv': so[0], 'booked': so[1], 'held': so[2], 'joins': so[3], 'content': so[4]},
            'week': {'conv': wk[0], 'booked': wk[1], 'held': wk[2], 'joins': wk[3], 'content': wk[4], 'tconv': t.get('wconv', 0), 'tbooked': t.get('booked', 0), 'tcontent': t.get('wcontent', 0)},
            'slice': slice_days, 'slice_conv': sc['slice_conv'], 'weekly_rows': sc['weekly'], 'daily_rows': sc['daily'], 'monday': monday}

def derive_week(ctx):
    today, ops, ex, pipe = ctx['today'], ctx['files'].get('identity/operations.md', ''), ctx['exec'], ctx['pipeline']
    gd = ctx['goals_data']; monday = gd['monday']
    daily = {date_in(r[0]): r for r in gd['daily_rows'][1:] if date_in(r[0])}
    call_block = clean(kv(ops, 'Call block'), ctx['demo'])
    model_call = clean(kv(ops, 'Weekly model call (if they host one)') or kv(ops, 'Weekly model call'), ctx['demo'])
    sunday = re.search(r'(the Sunday block[^·\n]*)', ops, re.I)
    friday = next((r[1] for r in ex['rhythm'][1:] if len(r) > 1 and 'weekly' in r[0].lower()), '')
    follow_day = re.search(r'follow-ups?\s*\((\w+day)\)', ctx['goals']['hours_split'] or '', re.I)
    days = []
    for i in range(7):
        d = monday + dt.timedelta(days=i); name = d.strftime('%a').upper()
        parts = []
        if d < today and d in daily:
            r = daily[d]; v = [num(c) for c in r[1:6]]
            if v[0]: parts.append('%d conversation%s' % (v[0], '' if v[0] == 1 else 's'))
            if v[1]: parts.append('%d call%s booked' % (v[1], '' if v[1] == 1 else 's'))
            if v[2]: parts.append('%d call%s held' % (v[2], '' if v[2] == 1 else 's'))
            if v[4]: parts.append('%d content' % v[4])
            if len(r) > 7 and r[7]: parts.append(r[7])
            state = 'done'
        elif d == today:
            parts.append('Your three moves' if ctx['moves'] else 'Today'); state = 'today'
        else:
            state = ''
            wd = d.strftime('%A')
            sched = model_call.split(' — ', 1)[1] if ' — ' in model_call else model_call
            if model_call and wd.lower() in sched.lower():
                tm = re.search(r'(\d{1,2}(?::\d\d)?\s*[ap]m)', sched); parts.append(model_call.split(' — ')[0].split(',')[0].strip() + ((' ' + tm.group(1)) if tm else ''))
            if call_block and wd.lower() in call_block.lower():
                tm = re.search(r'(\d{1,2}(?::\d\d)?\s*[–-]\s*\d{1,2}(?::\d\d)?)', call_block); parts.append('call block' + (' ' + tm.group(1) if tm else ''))
            if friday and wd.lower() in friday.lower(): parts.append(friday.replace(wd, '').strip(' ,') + ' weekly check-in')
            if follow_day and follow_day.group(1).lower() == wd.lower(): parts.append('follow-ups hour')
            if wd == 'Sunday' and sunday: parts.append(sunday.group(1).strip())
            due = [r['agent'] for r in pipe['rows'] if date_in(r['due']) == d]
            if due: parts.append('due: ' + ', '.join(due))
        days.append({'d': name, 'n': d.day, 's': state, 't': ' · '.join(parts) if parts else '—'})
    return days

def derive_open(ctx):
    demo, files, offer, brand, mag = ctx['demo'], ctx['files'], ctx['offer_md'], ctx['brand'], ctx['magnets']
    items = []
    if ctx['states']['lead-magnet'] == 'now':
        items.append({'node': 'lead-magnet', 'short': 'Funnel not live', 'text': 'Your funnel is not live. %s is written; the design, the page build and the delivery flow are the steps left.' % (mag['name'] or 'The guide'), 'phrase': 'finish my agent lead magnet'})
    if ctx['offer_built'] and offer['link'] and 'not set up' in offer['link'].lower():
        host = offer['host'].split(' (')[0].strip() or 'your community platform'
        items.append({'node': 'offer', 'short': host + ' not set up', 'text': '%s is not set up on %s yet. The 20-minute list is on your Partner Offer page under Where to host it.' % (offer['community'] or 'Your community', host), 'how': '20 minutes, by hand; the cohort’s link is in your Week 2 materials'})
    if ctx['offer_built'] and offer['join_gated'].lower().startswith('unknown'):
        items.append({'node': 'offer', 'short': 'The brokerage rule', 'text': 'Your brokerage’s rule on join-gated packages is still being checked. Until the desk confirms, every public line leads with what you teach, your story and your mentorship.', 'phrase': 'paste my compliance link'})
    prof = files.get('identity/profile.md', '')
    m = re.search(r'"([^"\n]{12,})"\s*\(drafted', prof) or re.search(r'"([^"\n]{12,})"[^\n]*drafted — confirm', ctx['book'].get(1, {}).get('body', ''))
    if m:
        items.append({'node': 'who-you-are', 'short': 'One line to confirm', 'text': 'One line is drafted, not yours yet: “%s” Say it your way, or confirm it.' % clean(m.group(1), demo), 'phrase': 'check my attraction brain'})
    for r in table_under(files.get('identity/proof.md', ''), 'Agents already helped')[1:]:
        if len(r) >= 5 and r[0].strip() and not r[-1].strip().lower().startswith('yes'):
            items.append({'node': 'your-proof', 'short': '%s’s written OK' % clean(r[0], demo).split(' ')[0], 'text': '%s’s written OK is needed before their result goes in print. Until then it is said on calls only.' % clean(r[0], demo), 'phrase': 'my agent proof'})
    left = [l for l, ok, note in brand['package'] if not ok]
    if ctx['states']['brand'] == 'built' and left:
        items.append({'node': 'brand', 'short': 'The brand kit', 'text': 'The brand kit is not in 02 · Brand yet: %d Claude Design run%s left (%s).' % (len(left), '' if len(left) == 1 else 's', ', '.join('the logo' if 'logo' in l else 'the style sheet' if 'style' in l else 'the kit' for l in left)) + (' The brief was issued %s.' % long_date(brand['brief_date']) if brand['brief_date'] else ''), 'phrase': 'show my design package brief'})
    comp = kv(files.get('identity/compliance.md', ''), 'Status').lower()
    if comp.startswith('set'):
        items.append({'node': 'your-brokerage', 'short': 'Confirm compliance', 'text': 'Your compliance rules are set from your brokerage’s page but not yet confirmed with the compliance desk. One email closes it.', 'how': 'one email to the compliance desk, then say so in any chat'})
    elif comp.startswith('unset') or not comp:
        items.append({'node': 'your-brokerage', 'short': 'Compliance not set', 'text': 'Your compliance rules are not set yet; nothing public can ship until they are.', 'phrase': 'paste my compliance link'})
    if not ctx['goals']['status'].lower().startswith('locked'):
        items.append({'node': 'your-numbers', 'short': 'Lock your targets', 'text': 'Your 90-day targets are not locked yet. The tracker starts counting the day they are.', 'phrase': 'set my attraction goals'})
    if 'drafted from their replies — confirm' in files.get('identity/voice.md', ''):
        items.append({'node': 'your-voice', 'short': 'Signature phrases to confirm', 'text': 'Your signature phrases are drafted from your replies, not confirmed. Keep the ones you actually say.', 'phrase': 'refresh my attraction voice print'})
    return items

def derive_changed(ctx):
    today, ch = ctx['today'], {}
    def recent(s):
        d = date_in(s); return d is not None and abs((today - d).days) <= 7
    if ctx['offer_built'] and recent(ctx['offer_md']['status']): ch['offer'] = 'Built this week: named, defined and written.'; ch['what-you-teach'] = 'Became your Partner Offer.'
    if ctx['states']['lead-magnet'] == 'now': ch['lead-magnet'] = 'The guide written; the funnel in progress.'
    if ctx['states']['brand'] == 'built' and ctx['brand']['brief_date'] and recent(ctx['brand']['brief_date'].isoformat()): ch['brand'] = 'The Design Package brief issued.'
    for k, b in ctx['config']['blocks'].items():
        sid = {'short-form': 'short-form', 'youtube': 'youtube', 'conversion': 'conversion', 'ai admin': 'ai-admin', 'events': 'events'}.get(k.split(' (')[0].strip().lower(), '')
        if sid and ctx['states'].get(sid) == 'built' and recent(b['line']): ch[sid] = 'Set up this week.'
    ch['whats-next'] = 'Rewritten for this week.'
    return ch

def build_extras(ctx):
    demo, gd, g, today = ctx['demo'], ctx['goals_data'], ctx['goals'], ctx['today']
    br, week = ctx['brain_md'], ctx['week']
    # ── at a glance ──
    knows = []
    who = ' · '.join(x for x in [ctx['name'], clean(kv(br, 'Brokerage'), demo), clean(kv(br, 'Market'), demo), clean(kv(ctx['files'].get('identity/profile.md', ''), 'Licensed'), demo)] if x)
    if who: knows.append('| Who you are | %s |' % who)
    if ctx['known_for']: knows.append('| What you teach | %s |' % ctx['known_for'])
    if ctx['offer_built'] and ctx['offer_md']['name']: knows.append('| Your program | %s%s |' % (ctx['offer_md']['name'], (', inside ' + ctx['offer_md']['community']) if ctx['offer_md']['community'] else ''))
    av = clean(kv(br, 'Primary avatar'), demo)
    if av: knows.append('| Who your story speaks to | %s |' % re.sub(r'\s*\(your skills[^)]*\)\s*$', '', re.sub(r'^who .*?never chosen:\s*', '', av)))
    if g['twelve']: knows.append('| Your numbers | %d today · %d in twelve months · %d long term · %d hours a week |' % (gd['today'], g['twelve'], g['long'], g['hours']))
    voice = clean(kv(br, 'Voice in one line'), demo).strip('"')
    if voice: knows.append('| Your voice | %s |' % voice)
    built = [t for i, _, _, t, _ in SYSTEMS if ctx['states'][i] == 'built']
    now = [t for i, _, _, t, _ in SYSTEMS if ctx['states'][i] == 'now']
    where = 'Week %d of 6%s.' % (week, (', day %d of your first quarter' % gd['day']) if gd['day'] else '')
    where += ' Built: your Brain' + (', ' + ', '.join(t.lower() for t in built) if built else '') + '.'
    if now: where += ' This week: ' + ', '.join(t.lower() for t in now) + '.'
    streak = 0
    daily = {date_in(r[0]): num(r[1]) for r in gd['daily_rows'][1:] if date_in(r[0])}
    d = today - dt.timedelta(days=1)
    while d in daily and daily[d] >= gd['slice_conv']:
        streak += 1; d -= dt.timedelta(days=1)
    docs = []
    for prefix, label, where_ in (('brain-book', 'Your Agent Attraction Brain Book', 'home base → 01 · AI Brain'), ('partner-offer', 'Your Partner Offer', 'home base → 01 · AI Brain'), ('scorecard', 'Your 90-Day Attraction Scorecard', 'home base → 01 · AI Brain')):
        f = latest_export(ctx['brain'], prefix)
        if f: docs.append('| %s | %s · %s |' % (label, where_, ('rendered ' + long_date(date_in(os.path.basename(f)))) if date_in(os.path.basename(f)) else 'on file'))
    if ctx['brand']['brief_date']: docs.append('| The Design Package brief | home base → 02 · Brand · issued %s |' % long_date(ctx['brand']['brief_date']))
    if ctx['magnets']['name']: docs.append('| %s, your guide | your Lead Magnet folder · %s |' % (ctx['magnets']['name'], ctx['magnets']['status'] or 'written'))
    cfgmd = ctx['files'].get('config.md', '')
    provider = {'google': 'Google Drive', 'microsoft': 'OneDrive'}.get((ctx['config']['provider'] or '').split(' ')[0].lower(), 'your cloud workspace')
    dbtask = clean(kv(cfgmd, 'Daily Debrief task'), demo).lower()
    dbtime = clean(kv(cfgmd, 'Debrief time'), demo).split(',')[0] or '6:00 pm'
    debrief_on = bool(dbtask) and not dbtask.startswith(('declined', 'off', 'no', 'not'))
    ctx['debrief_on'] = debrief_on; ctx['dbtime'] = dbtime
    stays = ('Every time any of your systems writes to your Brain — your offer, your guide, your content plans, your pipeline, a capture from the car, the evening debrief — your Brain saves to %s and this board is rebuilt from it. You never update the board by hand.' % provider)
    stays += (' Your daily debrief runs at %s, so the board also rebuilds every evening from your calendar and inbox, on days you never open Cowork.' % dbtime) if debrief_on else (' Your daily debrief is off. Say “turn on my daily debrief” and this board also rebuilds every evening at %s from your calendar and inbox, on days you never open Cowork.' % dbtime)
    stays += ' Work you do in Claude Design, like your logo or your guide’s PDF, lands in your %s folders; the next time any system opens your Brain it notices and this board catches up.' % provider
    glance = {'eyebrow': 'YOUR BRAIN · AT A GLANCE', 'title': '%s’s Brain at a glance' % ctx['first'], 'tagline': 'What your Brain knows, where you are, and how to talk to it.',
              'meta': ['Week %d of 6' % week] + (['Day %d of your first quarter' % gd['day']] if gd['day'] else []) + ['%d of 9 sections written · %d of 8 systems built' % (ctx['sections_written'], len(built))],
              'actions': [{'p': 'open my attraction brain', 'n': 'The short brief: what it knows, the week you’re in, what to type next.'}, {'p': 'show me my Brain', 'n': 'Regenerates your Brain Book from what’s on file.'}, {'p': 'just talked to an agent', 'n': 'One line from the car; it lands in the right file.'}, {'p': 'check my attraction brain', 'n': 'The audit: what’s thin, and the one thing to add.'}],
              'body': '## What your Brain knows\n' + '\n'.join(knows) + '\n\n## Where you are\n' + where + '\n@systems' + '\n\n## How this board stays current\n' + stays + ('\n\n## New since last week\n@changed' if len(ctx['changed']) > 1 else '') + (('\n\n## Your streaks\n| %d conversations a day | %d day%s running. Today keeps it alive. |' % (gd['slice_conv'], streak, '' if streak == 1 else 's')) if streak else '') + (('\n\n## Your documents\n' + '\n'.join(docs)) if docs else '')}
    # ── goals and the tracker ──
    vision = []
    twelve_pic = next((r[-1] for r in ctx['exec']['year'][1:] if r and r[0].lower().startswith('q4')), '')
    yr_focus = next((r[1] for r in ctx['exec']['year'][1:] if r and r[0].lower().startswith('q4')), '')
    if g['twelve']: vision.append('| Twelve months from now | %d agents in your organization.%s |' % (g['twelve'], (' ' + yr_focus[0].upper() + yr_focus[1:] + '.') if yr_focus else ''))
    longrow = next((r[1] for r in table_under(ctx['files'].get('identity/goals.md', ''), 'Your numbers')[1:] if 'long' in r[0].lower()), '')
    if longrow: vision.append('| Three years from now | %s |' % clean(longrow, demo))
    if ctx['known_for']: vision.append('| What you want to be known for | %s |' % ctx['known_for'])
    whofor = clean(kv(ctx['files'].get('identity/journey.md', ''), 'Who they are doing this for'), demo).strip('"').split(' · ')[0]
    if whofor: vision.append('| Who you are doing this for | %s |' % whofor)
    if g['first_agent']: vision.append('| Your first agent | %s |' % g['first_agent'])
    nums = ['| Agents in your organization today | %d |' % gd['today'], '| Agents you want to attract in the next 12 months | %d |' % g['twelve'], '| Your long-term goal | %d |' % g['long'], '| Hours a week you can fully commit | %d%s |' % (g['hours'], (': ' + g['hours_split'].split(': ', 1)[-1]) if g['hours_split'] else '')]
    stand = ['| Measure | So far (day %d) | Day 30 | Day 60 | Day 90 |' % gd['day']]
    mapso = {'conversations': gd['sofar']['conv'], 'calls held': gd['sofar']['held'], 'joins': gd['sofar']['joins'], 'content shipped': gd['sofar']['content'], 'agents in organization': gd['today']}
    for r in g['rows_3060'][1:]:
        if len(r) >= 4 and r[0]:
            so = mapso.get(r[0].strip().lower(), '—')
            stand.append('| %s | %s | %s | %s | %s |' % (r[0], so, r[1], r[2], r[3]))
    wk = gd['week']
    thisweek = ['| Controllable | Target a week | So far |', '| Conversations | %s | %d |' % (wk['tconv'], wk['conv']), '| Calls booked | %s | %d |' % (wk['tbooked'], wk['booked']), '| Calls held | — | %d |' % wk['held'], '| Content | %s | %d |' % (wk['tcontent'], wk['content'])]
    rows = []
    if gd['weekly_rows']: rows.append('\n'.join('| ' + ' | '.join(r) + ' |' for r in gd['weekly_rows']))
    if gd['daily_rows']: rows.append('\n'.join('| ' + ' | '.join(r) + ' |' for r in gd['daily_rows']))
    pipe = ['| Agent | Stage | Next move | Due |'] + ['| %s | %s | %s | %s |' % (r['agent'], r['stage'], r['next'], (nice_date(date_in(r['due'])) if date_in(r['due']) else r['due'])) for r in ctx['pipeline']['rows']]
    orgline = ''
    if ctx['org']['rows']: orgline = 'Your organization: ' + ', '.join('%s (joined %s, %s)' % (r['agent'], r['joined'], r['status']) for r in ctx['org']['rows']) + '.'
    year = ['| Quarter | Focus | Joins | Agents at the end |'] + ['| %s | %s | %s | %s |' % (r[0], r[1], r[2], r[3]) for r in ctx['exec']['year'][1:] if len(r) >= 4]
    plan = []
    if g['twelve']: plan.append('| Your 12-month goal | %d agents in your organization |' % g['twelve'])
    if gd['q90']['joins'] or gd['q90']['conv']: plan.append('| Your 90-day target | %s |' % ' · '.join(x for x in [('%d joins' % gd['q90']['joins']) if gd['q90']['joins'] else '', ('%d agents in your organization' % gd['q90']['agents']) if gd['q90']['agents'] else '', ('%d conversations' % gd['q90']['conv']) if gd['q90']['conv'] else '', ('%d calls held' % gd['q90']['held']) if gd['q90']['held'] else ''] if x))
    if gd['activity']: plan.append('| The activity you control | %s |' % gd['activity'])
    if ctx['exec']['nonneg']: plan.append('| Your three non-negotiables | %s |' % ' · '.join(x.rstrip('.') for x in ctx['exec']['nonneg']))
    plan.append('| The next step | %s |' % ctx['next_step'])
    goals_body = ('>> “%s”\n' % g['why'] if g['why'] else '') + '@tracker\n'
    if gd['pace']: goals_body += '\n## Where you stand against your plan\n@pace\n'
    goals_body += '\n## Your plan at a glance\n' + '\n'.join(plan)
    if gd['weeks']: goals_body += '\n\n## Week by week\n@chart\n'
    goals_body += '\n## Your pipeline\n@funnel\n'
    goals_body += ('\n## Your vision\n' + '\n'.join(vision) if vision else '') + '\n\n## Your numbers\n' + '\n'.join(nums)
    if len(stand) > 1: goals_body += '\n\n## Your first 90 days: where you stand\n' + '\n'.join(stand) + '\nRamped on purpose: month one builds the habit, month two compounds, month three converts.' + ((' The score is your Brain’s, from your own rows: %s.' % gd['score']) if gd['score'] else '')
    goals_body += '\n\n## This week, so far\n' + '\n'.join(thisweek)
    if rows: goals_body += '\n\n## Your rows so far\n' + '\n\n'.join(rows)
    if len(pipe) > 1: goals_body += '\n\n## Where every prospect stands\n' + '\n'.join(pipe) + ('\n' + ctx['pipeline']['counts'] if ctx['pipeline']['counts'] else '') + ((' ' + orgline) if orgline else '')
    if len(year) > 1: goals_body += '\n\n## The year, in four quarters\n' + '\n'.join(year)
    if ctx['exec']['nonneg']: goals_body += '\n\n## Your three non-negotiables, every week\n' + '\n'.join('%d. %s' % (i + 1, x) for i, x in enumerate(ctx['exec']['nonneg']))
    if g['intangibles']: goals_body += '\n\n## The intangibles you also track\n' + '\n'.join('• ' + x for x in g['intangibles'])
    goals_body += '\n\n## How the score works\nEvery evening the Daily Debrief counts the day and scores it against your daily slice: Ahead (150% of the slice or more), On pace, or Behind. Never a grade, never a percentage. Every Friday the weekly check-in rolls the days into one row and gives you one thing for next week. The first Monday of each month the audit replaces the assumed ratios with your real ones. At the end of the quarter the plan refreshes from what actually happened.' + ((' Ratios on file: %s.' % ctx['scorecard']['ratios']) if ctx['scorecard']['ratios'] else '')
    goals_body += '\n\n@note: The money scenarios from your plan stay off this board on purpose. They are private-call material, illustrative, and never a promise of what anyone will earn. Ask for your scorecard any time to see them.'
    goals = {'eyebrow': 'YOUR BUSINESS · THE PLAN AND THE TRACKER', 'title': 'Your business plan and tracker', 'tagline': 'Where you stand against the plan you set%s, what has to be true by day 30, 60 and 90, and the activity you control.' % ((' on day %d of 90' % gd['day']) if gd['day'] else ''),
             'meta': [('Targets ' + g['status'].split(' (')[0]) if g['status'] else 'Targets not locked yet', 'Rows written by your Daily Debrief and the Friday check-in'] + (['Every figure illustrative · demo'] if demo else []),
             'actions': [{'p': 'attraction weekly check-in', 'n': 'Friday: rolls the week into one row, scores it, and gives you one thing for next week.'}, {'p': 'am I on pace to my join target', 'n': 'The honest answer, in one line.'}, {'p': 'run my debrief', 'n': 'Counts today and writes tomorrow’s three moves.'}, {'p': 'refresh my attraction plan', 'n': 'End of quarter: the next 90 days from what actually happened.'}],
             'body': goals_body}
    # ── today ──
    db = ctx['debrief']
    fu = ['| Agent | Next move | Due |'] + ['| %s | %s | %s |' % (r['agent'], r['next'], nice_date(date_in(r['due'])) if date_in(r['due']) else r['due']) for r in sorted(ctx['pipeline']['rows'], key=lambda r: date_in(r['due']) or dt.date.max) if date_in(r['due']) and 0 <= (date_in(r['due']) - today).days <= 7]
    tbody = '## Your three moves\n@moves\n\n## Your week\n@week'
    if len(fu) > 1: tbody += '\n\n## Follow-ups due this week\n' + '\n'.join(fu)
    if db:
        rowsdb = [(k, v) for k, v in [('What you counted', db['lines'].get('counted', '')), ('Conversations', db['lines'].get('conversations', '')), ('Agent needs', db['lines'].get('agent needs', '')), ('Yesterday’s moves', db['lines'].get("yesterday's moves", '')), ('Stage moves waiting on your word', db['lines'].get('stage moves requested', ''))] if v and v.lower() != 'none']
        if rowsdb: tbody += '\n\n## From your debrief, %s\n' % long_date(db['date']) + '\n'.join('| %s | %s |' % kvp for kvp in rowsdb)
    wkrows = ['| | ' + ' | '.join(d['d'].title() for d in ctx['week_strip'][:5]) + ' | Week so far | Target |']
    dailymap = {date_in(r[0]): [num(c) for c in r[1:6]] for r in gd['daily_rows'][1:] if date_in(r[0])}
    for label, idx, tgt in (('Conversations', 0, gd['week']['tconv']), ('Calls booked', 1, gd['week']['tbooked']), ('Content shipped', 4, gd['week']['tcontent'])):
        cells = []
        for i in range(5):
            d = gd['monday'] + dt.timedelta(days=i)
            cells.append(str(dailymap[d][idx]) if d in dailymap else ('·' if d >= today else '0'))
        wkrows.append('| %s | %s | %d | %s |' % (label, ' | '.join(cells), [gd['week']['conv'], gd['week']['booked'], 0, 0, gd['week']['content']][idx], tgt))
    tbody += '\n\n## This week so far\n' + '\n'.join(wkrows) + '\n\n@link: goals | Open your goals and your tracker'
    today_doc = {'eyebrow': 'TODAY · ' + nice_date(today).upper(), 'title': 'Your three moves today' if ctx['moves'] else 'Today', 'tagline': (('From last night’s debrief. Three moves, your week, and who is waiting on a reply.' if db else 'No debrief yet. Run one tonight and tomorrow’s three moves appear here.') + ('' if ctx.get('debrief_on') else ' Your daily debrief is off: say “turn on my daily debrief” and this page writes itself every evening.')),
                 'meta': (['Written by your Daily Debrief, %s' % long_date(db['date']), 'Scored %s' % db['score'] + ((': ' + db['lines']['counted']) if db['lines'].get('counted') else '')] if db else ['No debrief on file']) + (['Demo'] if demo else []),
                 'actions': [{'p': 'run my debrief', 'n': 'Any evening, on demand: it counts the day and writes tomorrow’s three moves.'}, {'p': 'turn on my daily debrief', 'n': '6 pm every day as a scheduled task, only with your yes.'}, {'p': 'just talked to an agent', 'n': 'Log a conversation from the car; the stage moves on your word.'}],
                 'body': tbody}
    open_doc = {'eyebrow': 'WAITING ON YOU', 'title': 'Open items', 'tagline': '', 'meta': ['Read from your Brain · ' + nice_date(today), 'Clears itself as each one lands'] + (['Demo'] if demo else []), 'body': '@openlist'}
    return {'glance': glance, 'goals': goals, 'today': today_doc, 'open-items': open_doc}

def build_whats_next(ctx):
    now = [(i, t) for i, _, _, t, _ in SYSTEMS if ctx['states'][i] == 'now']
    soon = sorted([(w, i, t) for i, _, w, t, _ in SYSTEMS if ctx['states'][i] == 'soon'])
    lines = ['## This week']
    if now:
        for i, t in now: lines.append('• Finish %s: say "%s".' % (t.lower(), SYS_ACTIONS[i][0][0]))
    elif soon:
        w, i, t = soon[0]; lines.append('• %s: say "%s".' % (t, SYS_ACTIONS[i][0][0]))
    for o in ctx['open'][:3]:
        lines.append('• ' + o['text'].split('. ')[0] + '.')
    if soon:
        nxt = [s for s in soon if not now or s[1] != now[0][0]]
        if nxt:
            w, i, t = nxt[0]; lines += ['', '## Next', '• %s, in Week %d: say "%s".' % (t, w, SYS_ACTIONS[i][0][0])]
    lines += ['', '## Any time', '• "just talked to an agent" from the car. "show me my Brain" to refresh your Book. "run my debrief" to close the day.']
    return '\n'.join(lines)

def member_now(tz):
    """The member's clock: the config.md timezone when the system can resolve it, else this machine's clock (a cloud sandbox usually runs on UTC, so the date can be a day off in the evening — the sync skill passes --today for that)."""
    if tz:
        try:
            from zoneinfo import ZoneInfo
            return dt.datetime.now(ZoneInfo(tz)), True
        except Exception:
            pass
    return dt.datetime.now(), False

def build_static(data):
    """The quick view: plain HTML shown only where the board's scripts cannot run (a cloud-drive preview, a mail viewer). Same data, nothing interactive, white page."""
    E = html.escape
    H, T, G = data['HEADER'], data['TILES'], data['GOALS']
    out = ['<h1>%s</h1>' % E(H['title']), '<p class="sub">%s · %s</p>' % (E(H['weekLine']), E(H['syncLine']))]
    out.append('<div class="how"><b>This is the quick view.</b> The full board — the map of your Brain, your tracker, a page for every part — opens in your web browser. <b>Download this file and open it</b> (the download button at the top of this preview), or say <b>“open my brain board”</b> to Claude.</div>')
    out.append('<h2>Where you stand</h2>')
    if T['goals']['empty']:
        out.append('<p>%s</p>' % E(T['goals']['empty']))
    else:
        if G['quarter']: out.append('<p>Your 90 days: %s%s.</p>' % (E(G['quarter']), (' · day %d' % G['day']) if G['day'] else ''))
        items = []
        for p in G['pace']:
            cls = 'warn' if p['status'] == 'behind' else 'ok'
            items.append('<li>%s: <b>%s</b> of %s by day 90 · <span class="%s">%s</span>%s</li>' % (E(p['label']), p['actual'], p['d90'], cls, E(p['status']), (' (about %s expected by now)' % p['expected']) if p['expected'] else ''))
        if items: out.append('<ul>%s</ul>' % ''.join(items))
        if T['goals']['line']: out.append('<p>%s</p>' % E(T['goals']['line']))
    out.append('<h2>%s</h2>' % ('Your three moves today' if data['MOVES'] else 'Today'))
    if data['MOVES']: out.append('<ul>%s</ul>' % ''.join('<li>%s</li>' % E(m) for m in data['MOVES']))
    else: out.append('<p>No debrief yet. Say “run my debrief” tonight and tomorrow’s three moves appear here.</p>')
    if T['today'].get('sub'): out.append('<p>%s</p>' % E(T['today']['sub']))
    w = T['week']
    out.append('<h2>%s</h2><p><b>%s</b> %s%s</p>' % (E(w['k']), E(w['big']), E(w['small']), (' Say “%s”.' % E(w['code'])) if w.get('code') else ''))
    out.append('<h2>Waiting on you</h2>')
    if data['OPEN']:
        out.append('<ul>%s</ul>' % ''.join('<li><b>%s.</b> %s%s%s</li>' % (E(o['short']), E(o['text']), (' (%s)' % E(o['how'])) if o.get('how') else '', (' Say “%s”.' % E(o['phrase'])) if o.get('phrase') else '') for o in data['OPEN']))
    else:
        out.append('<p>Nothing is waiting on you.</p>')
    out.append('<p class="foot">%s</p>' % E(H['foot']))
    return '\n'.join(out)

def main():
    ap = argparse.ArgumentParser(description='Render the Brain Board from an Agent Attraction Brain folder.')
    ap.add_argument('brain'); ap.add_argument('--out', required=True); ap.add_argument('--week', type=int); ap.add_argument('--today'); ap.add_argument('--template', default=os.path.join(HERE, 'board-template.html'))
    a = ap.parse_args()
    brain = os.path.abspath(a.brain)
    brain_md = read(os.path.join(brain, 'brain.md'))
    if not brain_md.strip():
        print('NO-BRAIN: %s has no brain.md — nothing to render.' % brain); sys.exit(2)
    names = ['config.md', 'identity/profile.md', 'identity/journey.md', 'identity/brokerage-model.md', 'identity/strategy.md', 'identity/offer.md', 'identity/proof.md', 'identity/avatars.md', 'identity/goals.md', 'identity/voice.md', 'identity/voice-print.md', 'identity/brand-visual.md', 'identity/execution-framework.md', 'identity/operations.md', 'identity/compliance.md', 'identity/content-pillars.md', 'identity/channel.md', 'identity/sales-system.md', 'memory/scorecard.md', 'memory/pipeline.md', 'memory/debriefs.md', 'memory/organization.md', 'memory/magnets.md', 'memory/events.md']
    files = {n: read(os.path.join(brain, n)) for n in names}
    config = parse_config(files['config.md']); demo = config['demo']
    goals = parse_goals(files['identity/goals.md'], demo)
    sc = parse_scorecard(files['memory/scorecard.md'], demo)
    daily_dates = [date_in(r[0]) for r in sc['daily'][1:] if date_in(r[0])]
    now_s, tz_ok = member_now(config.get('tz', ''))
    today = (date_in(a.today) if a.today else None) or ((max(daily_dates) + dt.timedelta(days=1)) if (demo and daily_dates) else now_s.date())
    ctx = {'brain': brain, 'files': files, 'config': config, 'demo': demo, 'today': today, 'brain_md': brain_md, 'goals': goals, 'scorecard': sc}
    ctx['name'] = clean(kv(brain_md, 'Name'), demo).split(' · ')[0] or 'You'
    ctx['first'] = ctx['name'].split(' ')[0]
    ctx['known_for'] = clean(kv(brain_md, 'Known for'), demo)
    ctx['booking'] = clean(kv(brain_md, 'Booking link'), demo).split(' ')[0]
    ctx['brain_magnet'] = clean(kv(brain_md, 'Live magnet'), demo)
    yt = re.search(r'YouTube\s*"([^"]+)"', files['identity/profile.md'] + brain_md)
    ctx['yt_name'] = yt.group(1) if yt else ''
    ctx['book'] = parse_book(read(latest_export(brain, 'brain-book')), demo) if latest_export(brain, 'brain-book') else {}
    ctx['offer_doc'] = parse_offer_doc(read(latest_export(brain, 'partner-offer')), demo) if latest_export(brain, 'partner-offer') else None
    ctx['offer_md'] = parse_offer_md(files['identity/offer.md'], demo)
    ctx['offer_built'] = bool(re.match(r'(built|finalized)', ctx['offer_md']['status'], re.I))
    ctx['brand'] = parse_brand(files['identity/brand-visual.md'], demo)
    ctx['magnets'] = parse_magnets(files['memory/magnets.md'], demo)
    if not ctx['magnets']['name'] and ctx['brain_magnet']:
        m = re.match(r'([^·]+)(?:·\s*keyword:?\s*([A-Z]+))?(?:\s*·\s*(.*))?', ctx['brain_magnet'])
        if m:
            ctx['magnets']['name'] = m.group(1).strip(); ctx['magnets']['keyword'] = m.group(2) or ''
            ctx['magnets']['funnel'] = 'not live yet' if 'not live' in ctx['brain_magnet'].lower() else (re.search(r'https?://\S+', ctx['brain_magnet']).group(0) if re.search(r'https?://\S+', ctx['brain_magnet']) else '')
    ctx['pillars_md'] = files['identity/content-pillars.md']
    ctx['pipeline'] = parse_pipeline(files['memory/pipeline.md'], demo)
    ctx['org'] = parse_org(files['memory/organization.md'], demo)
    ctx['debrief'] = parse_debriefs(files['memory/debriefs.md'], demo)
    ctx['exec'] = parse_exec(files['identity/execution-framework.md'], demo)
    ctx['week'] = None
    ctx['states'] = {i: state_of(i, ctx) for i, _, _, _, _ in SYSTEMS}
    inferred = max([w for i, _, w, _, _ in SYSTEMS if ctx['states'][i] in ('built', 'now')] or [1])
    ctx['week'] = a.week or (int(config['week']) if config['week'] else None) or inferred
    ctx['week'] = max(1, min(6, ctx['week']))
    ctx['states'] = {i: state_of(i, ctx) for i, _, _, _, _ in SYSTEMS}
    ctx['moves'] = ctx['debrief']['moves'] if ctx['debrief'] else []
    ctx['open'] = derive_open(ctx)
    ctx['goals_data'] = derive_goals(ctx)
    ctx['week_strip'] = derive_week(ctx)
    ctx['changed'] = derive_changed(ctx)
    ctx['sections_written'] = sum(1 for n in range(1, 10) if ctx['book'].get(n, {}).get('body')) or sum(1 for _, _, _, _, _, _, f, _ in INNER if f and files.get(f, '').strip() and '[' not in files.get(f, '')[:300])
    ctx['whats_next_body'] = build_whats_next(ctx)
    _now = [t for i, _, _, t, _ in SYSTEMS if ctx['states'][i] == 'now']
    _soon = sorted([(w, t) for i, _, w, t, _ in SYSTEMS if ctx['states'][i] == 'soon'])
    ctx['next_step'] = ('Finish ' + _now[0].lower()) if _now else (('%s, in Week %d' % (_soon[0][1], _soon[0][0])) if _soon else 'Keep the weekly rhythm')
    inner = build_inner(ctx); outer = build_outer(ctx); extra = build_extras(ctx)
    gd = ctx['goals_data']
    now_sys = next((d for d in outer if d['state'] == 'now'), None)
    soon_sys = next((d for d in sorted(outer, key=lambda x: x['week']) if d['state'] == 'soon'), None)
    if now_sys:
        tile_week = {'k': 'Week %d' % ctx['week'], 'big': 'Finish ' + now_sys['title'].lower().replace('your ', 'your ', 1) + '.', 'small': now_sys['line'], 'code': now_sys['actions'][0]['p'] if now_sys['actions'] else '', 'doc': now_sys['id']}
    elif soon_sys:
        tile_week = {'k': 'Next', 'big': soon_sys['title'] + '.', 'small': soon_sys['line'], 'code': soon_sys['actions'][0]['p'] if soon_sys['actions'] else '', 'doc': soon_sys['id']}
    else:
        tile_week = {'k': 'Week %d' % ctx['week'], 'big': 'Every system is built.', 'small': 'Keep the rhythm: two conversations a day, the weekly call, the content block.', 'code': 'run my debrief', 'doc': 'goals'}
    db = ctx['debrief']
    sub = ''
    if db and db['lines'].get('follow-ups due'):
        sub = 'Follow-ups due: ' + '; '.join(re.sub(r'\s*—\s*20\d\d-\d\d-\d\d', '', x).strip() for x in db['lines']['follow-ups due'].split(' · ')[:2])
    elif not db:
        sub = 'No debrief yet. Say “run my debrief” tonight.'
    stale = db and (today - db['date']).days > 1
    if stale: sub = ('From your debrief of %s. ' % nice_date(db['date'])) + sub
    tiles = {'goals': {'empty': ('Your targets aren\u2019t locked yet. Say \u201cset my attraction goals\u201d and this tile starts counting.' if not gd['q90']['conv'] and not gd['week']['tconv'] else ''), 'bars': [{'label': 'This week · conversations', 'v': gd['week']['conv'], 't': gd['week']['tconv']}, {'label': 'This week · calls booked', 'v': gd['week']['booked'], 't': gd['week']['tbooked']}, {'label': 'Quarter · joins', 'v': gd['sofar']['joins'], 't': gd['q90']['joins'], 's': next((p['status'] for p in gd['pace'] if p['label'].lower() == 'joins'), '')}],
                       'slice': gd['slice'], 'line': ('%d a day' % gd['slice_conv']) + ((' · day %d of 90' % gd['day']) if gd['day'] else '') + ((' · ' + gd['score']) if gd['score'] else '')},
             'today': {'k': nice_date(today), 'sub': sub}, 'week': tile_week}
    sync_line = 'Synced with your Brain · ' + (nice_date(today) if (a.today or not tz_ok) else nice_date(now_s.date()) + now_s.strftime(', %I:%M %p').replace(', 0', ', '))
    header = {'name': ctx['name'], 'first': ctx['first'], 'title': '%s’s Brain Board' % ctx['first'], 'weekLine': 'Week %d of 6' % ctx['week'] + ((' · day %d of your quarter' % gd['day']) if gd['day'] else ''),
              'segs': ['d'] * (ctx['week'] - 1) + ['n'] + [''] * (6 - ctx['week']), 'syncLine': sync_line,
              'sections': ctx['sections_written'], 'foot': 'Your Brain Board rebuilds itself from your Brain every time anything in it changes' + ((' · Demo: %s is fictional and every figure is illustrative' % ctx['name']) if demo else '')}
    data = {'HEADER': header, 'TILES': tiles, 'GOALS': {k: gd[k] for k in ('today', 'twelve', 'longTerm', 'hours', 'day', 'quarter', 'score', 'q90', 'sofar', 'pace', 'funnel', 'weeks', 'wconv')}, 'OPEN': ctx['open'], 'MOVES': ctx['moves'], 'WEEK': ctx['week_strip'], 'CHANGED': ctx['changed'], 'DAY': today.isoformat(), 'STAMP': today.isoformat(), 'INNER': inner, 'OUTER': outer, 'EXTRA': extra}
    tpl = read(a.template)
    if not tpl: print('NO-TEMPLATE: %s' % a.template); sys.exit(2)
    payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    page = tpl.replace('/*__BOARD_DATA__*/null', payload).replace('{{TITLE}}', header['title'].replace('<', '')).replace('<!--__BOARD_STATIC__-->', build_static(data))
    page = '<!doctype html>\n<html lang="en">\n' + page + '\n</html>\n'
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or '.', exist_ok=True)
    with open(a.out, 'w', encoding='utf-8') as f: f.write(page)
    print(a.out)

if __name__ == '__main__':
    main()
