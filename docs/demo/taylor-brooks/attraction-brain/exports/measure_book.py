#!/usr/bin/env python3
"""Measure + verify a rendered Brain Book (.docx) — words per chapter, tables, callouts,
page breaks, TOC links, demo checks. Output JSON + a markdown table."""
import sys, re, json, math, zipfile
from docx import Document
from docx.oxml.ns import qn

PATH = sys.argv[1]
MODE = sys.argv[2] if len(sys.argv) > 2 else "book"   # book | legacy
doc = Document(PATH)
body = doc.element.body

CHAP_RE = re.compile(r'^(PART [IVXLC]+|CHAPTER \d+)$')
TAG = "illustrative — demo"

def para_text(p):
    return "".join(t.text or "" for t in p.iter(qn('w:t')))

def is_callout_table(tbl):
    rows = tbl.findall(qn('w:tr'))
    if len(rows) != 1: return False
    cells = rows[0].findall(qn('w:tc'))
    if len(cells) != 1: return False
    shd = cells[0].find('.//' + qn('w:shd'))
    return shd is not None and shd.get(qn('w:fill')) == 'F3F4F6'

# Walk body in order
blocks = []   # (kind, text, meta)
for el in body:
    tag = el.tag.split('}')[1]
    if tag == 'p':
        txt = para_text(el).strip()
        pPr = el.find(qn('w:pPr'))
        # v2 renderer: a ">> " callout is a paragraph with a left accent border + shading (v1: a shaded 1-cell table)
        pb = pPr.find(qn('w:pBdr')) if pPr is not None else None
        if pb is not None and pb.find(qn('w:left')) is not None and pPr.find(qn('w:shd')) is not None:
            blocks.append(('tbl', [[txt]], {'callout': True})); continue
        pbb = pPr is not None and pPr.find(qn('w:pageBreakBefore')) is not None
        hardbr = any(br.get(qn('w:type')) == 'page' for br in el.iter(qn('w:br')))
        hl = len(el.findall('.//' + qn('w:hyperlink')))
        bm = len(el.findall(qn('w:bookmarkStart')))
        runs = el.findall(qn('w:r'))
        kind2 = 'body'
        if runs:
            r0 = runs[0]; rPr = r0.find(qn('w:rPr'))
            bold = rPr is not None and rPr.find(qn('w:b')) is not None
            sz = rPr.find(qn('w:sz')) if rPr is not None else None
            szv = int(sz.get(qn('w:val'))) if sz is not None else 0
            t0 = "".join(t.text or "" for t in r0.iter(qn('w:t')))
            if t0.startswith('•'): kind2 = 'bullet'
            elif re.match(r'^\d+\.\s', t0): kind2 = 'numbered'
            elif bold and szv == 24 and txt and not CHAP_RE.match(txt): kind2 = 'subband'
            elif bold and t0.rstrip().endswith(':'): kind2 = 'label'
        blocks.append(('p', txt, {'pbb': pbb, 'hardbr': hardbr, 'hl': hl, 'bm': bm, 'k2': kind2}))
    elif tag == 'tbl':
        rows = []
        for tr in el.findall(qn('w:tr')):
            rows.append([ "".join(t.text or "" for t in tc.iter(qn('w:t'))).strip() for tc in tr.findall(qn('w:tc'))])
        blocks.append(('tbl', rows, {'callout': is_callout_table(el)}))

# Segment into sections: cover, toc, then PART/CHAPTER sections
sections = []   # dict(name, kind, paras, tables, callouts, words, words_notag, pbb, hardbr)
cur = {'name': 'COVER', 'kind': 'cover', 'paras': [], 'tables': [], 'callouts': [], 'pbb': 0, 'hardbr': 0, 'hl': 0, 'bm': 0}
i = 0
while i < len(blocks):
    kind, payload, meta = blocks[i]
    if kind == 'p':
        txt = payload
        if txt == 'CONTENTS' and MODE == 'book':
            sections.append(cur); cur = {'name': 'CONTENTS', 'kind': 'toc', 'paras': [], 'tables': [], 'callouts': [], 'pbb': 0, 'hardbr': 0, 'hl': 0, 'bm': 0}
        elif CHAP_RE.match(txt) and i + 1 < len(blocks) and blocks[i+1][0] == 'p':
            title = blocks[i+1][1]
            sections.append(cur)
            cur = {'name': f"{txt} — {title}", 'kind': 'part' if txt.startswith('PART') else 'chapter',
                   'paras': [], 'tables': [], 'callouts': [], 'pbb': 0, 'hardbr': 0, 'hl': 0, 'bm': 0}
            cur['pbb'] += 1 if meta['pbb'] else 0
            cur['bm'] += blocks[i+1][2]['bm']
            i += 2; continue
        cur['paras'].append(txt)
        cur.setdefault('fp', {}); cur['fp'][meta['k2']] = cur['fp'].get(meta['k2'], 0) + 1
        cur['pbb'] += 1 if meta['pbb'] else 0
        cur['hardbr'] += 1 if meta['hardbr'] else 0
        cur['hl'] += meta['hl']; cur['bm'] += meta['bm']
    else:
        if meta['callout']:
            cur['callouts'].append(payload[0][0])
        else:
            cur['tables'].append(payload)
    i += 1
sections.append(cur)

def wc(s): return len(s.split())
def strip_tags(s):
    s = re.sub(r'\((?:[^()]*?)illustrative — demo[^()]*\)', '', s)
    s = s.replace('illustrative — demo', '')
    return s

summary = []
total = total_notag = 0
for s in sections:
    texts = list(s['paras']) + s['callouts'] + [c for t in s['tables'] for r in t for c in r]
    joined = "\n".join(texts)
    words = wc(joined); words_nt = wc(strip_tags(joined))
    table_rows = sum(len(t) for t in s['tables'])
    prose_words = wc("\n".join(s['paras'] + s['callouts']))
    table_words = wc("\n".join(c for t in s['tables'] for r in t for c in r))
    # simple estimate (task formula): words/380, forced break = +1 page start
    simple_pages = max(1, math.ceil(words / 380.0)) if s['kind'] in ('chapter', 'part', 'toc', 'cover') else 0
    # layout estimate (renderer v2): body lines ~ 92 chars/line at 11pt Arial over 6.5in; line = 11*1.2=13.2pt + 6pt para gap
    usable_pt = 655.0
    h = 0.0
    for p in s['paras']:
        if not p: continue
        lines = max(1, math.ceil(len(p) / 92.0)); h += lines * 13.2 + 6
    for c in s['callouts']:
        lines = max(1, math.ceil(len(c) / 86.0)); h += lines * 13.2 + 20   # indented accent-bar block
    for t in s['tables']:
        ncol = max(len(r) for r in t)
        # emulate renderer widths: proportional to max cell len per col (4..60), floor 0.55in
        lens = [max((len(r[c]) if c < len(r) else 0) for r in t) for c in range(ncol)]
        wts = [max(4, min(l, 60)) for l in lens]; tot = float(sum(wts))
        widths = [max(0.55*72, 468.0 * w / tot) for w in wts]
        sc = 468.0 / sum(widths); widths = [w * sc for w in widths]
        for r in t:
            rl = 1
            for ci, cell in enumerate(r):
                cpl = max(6, int(widths[ci] / 5.2))   # 10pt Arial ~5.2pt avg char
                rl = max(rl, math.ceil(len(cell) / cpl) if cell else 1)
            h += rl * 12.0 + 9
        h += 8
    if s['kind'] == 'chapter': h += 72   # kicker + 20pt title + rule
    if s['kind'] == 'part': h += 60
    layout_pages = max(1, math.ceil(h / usable_pt)) if s['kind'] in ('chapter', 'part') else None
    # tag discipline: numbered facts must be tagged (chapters only). We count paragraphs/cells with $ or % or digit-numbers
    numbered = [x for x in texts if re.search(r'(\$\d|\d+%|\b\d{2,}\b)', x)]
    untagged = [x for x in numbered if TAG not in x and 'illustrative' not in x]
    summary.append({'section': s['name'], 'kind': s['kind'], 'words': words, 'words_no_tags': words_nt,
                    'prose_words': prose_words, 'table_words': table_words,
                    'tables': len(s['tables']), 'table_rows': table_rows, 'callouts': len(s['callouts']),
                    'page_break_before': s['pbb'], 'hard_breaks': s['hardbr'], 'hyperlinks': s['hl'], 'bookmarks': s['bm'],
                    'simple_pages': simple_pages, 'layout_pages': layout_pages, 'layout_pt': round(h),
                    'numbered_blocks': len(numbered), 'untagged_numbered': untagged[:8], 'fingerprint': s.get('fp', {})})
    total += words; total_notag += words_nt

# Global checks
full_text = "\n".join(("\n".join(s['paras'] + s['callouts'] + [c for t in s['tables'] for r in t for c in r])) for s in sections)
with zipfile.ZipFile(PATH) as z:
    xml = z.read('word/document.xml').decode('utf8')
    footer = [n for n in z.namelist() if 'footer' in n]
    ftxt = "".join(z.read(n).decode('utf8') for n in footer)
checks = {
    'raw_w_markup_in_text': ('<w:' in full_text),
    'chapters_found': [s['section'] for s in summary if s['kind'] == 'chapter'],
    'parts_found': [s['section'] for s in summary if s['kind'] == 'part'],
    'toc_hyperlinks': sum(s['hyperlinks'] for s in summary if s['kind'] == 'toc'),
    'bookmarks_total': sum(s['bookmarks'] for s in summary),
    'hard_page_breaks': sum(s['hard_breaks'] for s in summary),
    'page_break_before_count': sum(s['page_break_before'] for s in summary),
    'footer_has_PAGE_field': ('PAGE' in ftxt),
    'byline_count': full_text.count('Taylor Brooks · Austin, TX'),
    'credential_line_count': full_text.count('6th year · building a downline'),
    'demo_cover_line': ('Demo document — illustrative data, not researched.' in full_text),
    'tag_count': full_text.count(TAG),
    'confirm_markers': len(re.findall(r'\[confirm:', full_text)),
    'total_words': total, 'total_words_no_tags': total_notag,
    'total_tables': sum(s['tables'] for s in summary), 'total_callouts': sum(s['callouts'] for s in summary),
}
print(json.dumps({'sections': summary, 'checks': checks}, indent=1, ensure_ascii=False))
