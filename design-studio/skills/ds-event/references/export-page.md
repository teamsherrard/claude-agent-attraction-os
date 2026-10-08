# The Export Page — how files leave Claude Design (shared by every Design Studio skill that exports pictures (identical copy in each skill))

Read in full when you are about to build the final files.

## CLAUDE DESIGN HAS NO PICTURE EXPORT — THE BOARD EXPORTS ITSELF

Claude Design's Export menu writes HTML and PDF, not pictures. So the board carries its own exporter:
the LAST page of the board is the **export page** — one button, a status line under it, and (for
`ds-logo`) the hand-off package text. One click renders every piece to a transparent PNG at its exact
size, writes the SVG twin where one is wanted, and downloads ONE zip with the canonical names. This is
the only way the member ever exports. Never tell them to export frame by frame, never point them at
the Export menu for pictures, never suggest a browser extension.

**Button labels (plain language):** `ds-logo` → **"Download your logo files"** (zip:
`logo-files.zip`). `ds-brand` → **"Download the kit"** (zip: `brand-kit.zip`).

**The contract that makes the button work — build every piece this way from its first render:**
- Every deliverable is ONE inline `<svg>` with `width`, `height`, and `viewBox` at the exact canvas
  size and `data-file="<canonical name>"` (for example `data-file="logo-primary.png"`,
  `data-file="banner-youtube.png"`). Add `data-svg="1"` on any piece that must ALSO ship as an SVG
  (every logo version); the exporter writes `logo-primary.svg` beside the PNG. One SVG per page,
  nothing else exportable on that page.
- Everything the piece needs lives INSIDE that SVG: shapes, text, the logo as `<image href>`, a
  headshot as a clipped `<image>`, an internal `<style>` for the text. Style with attributes or that
  internal style — never from the page's CSS, because the exporter renders the SVG on its own and page
  CSS does not reach it. Tweak tokens are fine as `fill="var(--brand-accent)"`: the exporter bakes the
  current values into the file.
- **Transparent pieces carry no background rect, no stage, no label inside the SVG.** A logo file with
  a white box behind it is a failed export. Preview grounds (the dark/white boards you present on) are
  separate layers BEHIND the SVG on the page. Anything decorative that must not ship carries
  `data-export="skip"`.
- Fonts come from the page's `@font-face` rules (the Google Fonts link or the Design System's fonts);
  the exporter embeds them, so the PNG shows the real typeface and the SVG carries the font with it.
  Images are fetched and embedded at export time.
- Hand-off text sits on the export page in `<script type="text/plain" id="export-notes">…</script>`;
  the button writes it out as the file named in `EXPORT_NOTES_FILE` (`logo-spec.md` for ds-logo,
  `brand-kit-captions.md` for ds-brand).
- The button reports `N files packed — complete` or lists the MISSING canonical names. The check
  compares against `KIT_REQUIRED` in the script — set that list to the exact names this build owes
  (add the organization set, team pieces, or optional pieces when you build them).
- Test it: the member clicks the button at the end of the last stage and reads you the status line.
  "Complete" is the finish line; anything else you fix before presenting.

**The 30-second TRANSPARENCY CHECK (you cannot see the exported file yourself) — tell the member:**
open `logo-primary.png` (or `banner-youtube.png`) on their computer; around the artwork they should
see a checkerboard, one flat colour, or nothing — NOT a solid white or black rectangle. If they see a
box, they say which file and you fix that piece; they click Download again.

**The exporter — paste it on the export page verbatim (no libraries; tested in Chrome, Sept 2026;
the SVG twin and the notes file are the two additions for this suite):**

```html
<button id="kit-download" onclick="downloadKit()">Download your logo files</button> <span id="kit-status"></span>
<script>
// ---- Design Studio: one-click export. No libraries. ----
// Renders every <svg data-file="..."> on the page to a transparent PNG at its exact width/height,
// writes an .svg twin for every piece marked data-svg, bakes the current tweak tokens, embeds fonts
// and images, and packs everything into one zip.
const KIT_REQUIRED = ['logo-primary.png','logo-primary.svg','logo-horizontal.png','logo-horizontal.svg','logo-stacked.png','logo-stacked.svg',
  'logo-mark.png','logo-mark.svg','logo-mark-favicon.png','logo-onecolour-dark.png','logo-onecolour-dark.svg','logo-onecolour-light.png','logo-onecolour-light.svg',
  'logo-reversed.png','logo-reversed.svg','logo-header.png','logo-header.svg'];   // ds-brand: replace with the kit's canonical names
const ZIP_NAME = 'logo-files.zip';                 // ds-brand: 'brand-kit.zip'
const EXPORT_NOTES_FILE = 'logo-spec.md';          // ds-brand: 'brand-kit-captions.md'

const blobToDataURL = b => new Promise(res => { const fr = new FileReader(); fr.onload = () => res(fr.result); fr.readAsDataURL(b); });

async function fontFaceCSS() {
  const rules = [];
  for (const sheet of document.styleSheets) {
    let list = null;
    try { list = sheet.cssRules; } catch (e) { list = null; }
    if (list) { for (const r of list) if (r.constructor.name === 'CSSFontFaceRule') rules.push(r.cssText); }
    else if (sheet.href) { try { const css = await (await fetch(sheet.href)).text(); rules.push(...(css.match(/@font-face\s*{[^}]*}/g) || [])); } catch (e) {} }
  }
  const out = [];
  for (let rule of rules) {
    if (/unicode-range/.test(rule) && !/U\+0000/.test(rule)) continue;   // latin subsets only
    for (const m of [...rule.matchAll(/url\((["']?)([^)"']+)\1\)/g)]) {
      if (m[2].startsWith('data:')) continue;
      try { const b = await (await fetch(new URL(m[2], document.baseURI))).blob(); rule = rule.replace(m[0], `url(${await blobToDataURL(b)})`); } catch (e) {}
    }
    out.push(rule);
  }
  return out.join('\n');
}

function bakeVars(xml) {
  const cs = getComputedStyle(document.documentElement);
  return xml.replace(/var\((--[\w-]+)\)/g, (m, v) => (cs.getPropertyValue(v) || '').trim() || m);
}

async function svgToXml(svgEl, fontCSS) {
  const clone = svgEl.cloneNode(true);
  clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg'); clone.setAttribute('xmlns:xlink', 'http://www.w3.org/1999/xlink');
  clone.removeAttribute('style'); clone.removeAttribute('class'); clone.removeAttribute('data-file'); clone.removeAttribute('data-svg');
  clone.querySelectorAll('[data-export="skip"]').forEach(n => n.remove());
  for (const img of clone.querySelectorAll('image')) {
    const href = img.getAttribute('href') || img.getAttribute('xlink:href');
    if (href && !href.startsWith('data:')) { try { const b = await (await fetch(new URL(href, document.baseURI))).blob(); img.setAttribute('href', await blobToDataURL(b)); img.removeAttribute('xlink:href'); } catch (e) {} }
  }
  const style = document.createElementNS('http://www.w3.org/2000/svg', 'style'); style.textContent = fontCSS; clone.insertBefore(style, clone.firstChild);
  return bakeVars(new XMLSerializer().serializeToString(clone));
}

async function xmlToPng(xml, w, h, name) {
  const url = URL.createObjectURL(new Blob([xml], { type: 'image/svg+xml;charset=utf-8' }));
  const img = new Image();
  await new Promise((res, rej) => { img.onload = res; img.onerror = () => rej(new Error('could not render ' + name)); img.src = url; });
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  c.getContext('2d').drawImage(img, 0, 0, w, h); URL.revokeObjectURL(url);
  return new Promise(res => c.toBlob(res, 'image/png'));
}

function crc32(u8) { let crc = 0xFFFFFFFF; for (let i = 0; i < u8.length; i++) { let c = (crc ^ u8[i]) & 0xFF; for (let k = 0; k < 8; k++) c = c & 1 ? (c >>> 1) ^ 0xEDB88320 : c >>> 1; crc = (crc >>> 8) ^ c; } return (crc ^ 0xFFFFFFFF) >>> 0; }

function makeZip(files) {   // store-only zip: [{name, data: Uint8Array}]
  const enc = new TextEncoder(), parts = [], central = []; let offset = 0;
  for (const f of files) {
    const name = enc.encode(f.name), crc = crc32(f.data), n = f.data.length;
    const lh = new DataView(new ArrayBuffer(30));
    lh.setUint32(0, 0x04034b50, true); lh.setUint16(4, 20, true); lh.setUint16(6, 0x0800, true); lh.setUint16(8, 0, true); lh.setUint16(10, 0, true); lh.setUint16(12, 0x21, true);
    lh.setUint32(14, crc, true); lh.setUint32(18, n, true); lh.setUint32(22, n, true); lh.setUint16(26, name.length, true); lh.setUint16(28, 0, true);
    parts.push(new Uint8Array(lh.buffer), name, f.data);
    const cd = new DataView(new ArrayBuffer(46));
    cd.setUint32(0, 0x02014b50, true); cd.setUint16(4, 20, true); cd.setUint16(6, 20, true); cd.setUint16(8, 0x0800, true); cd.setUint16(10, 0, true); cd.setUint16(12, 0, true); cd.setUint16(14, 0x21, true);
    cd.setUint32(16, crc, true); cd.setUint32(20, n, true); cd.setUint32(24, n, true); cd.setUint16(28, name.length, true); cd.setUint16(30, 0, true); cd.setUint16(32, 0, true); cd.setUint16(34, 0, true); cd.setUint16(36, 0, true); cd.setUint32(38, 0, true); cd.setUint32(42, offset, true);
    central.push(new Uint8Array(cd.buffer), name);
    offset += 30 + name.length + n;
  }
  const cdSize = central.reduce((s, p) => s + p.length, 0);
  const eocd = new DataView(new ArrayBuffer(22));
  eocd.setUint32(0, 0x06054b50, true); eocd.setUint16(4, 0, true); eocd.setUint16(6, 0, true); eocd.setUint16(8, files.length, true); eocd.setUint16(10, files.length, true); eocd.setUint32(12, cdSize, true); eocd.setUint32(16, offset, true); eocd.setUint16(20, 0, true);
  return new Blob([...parts, ...central, new Uint8Array(eocd.buffer)], { type: 'application/zip' });
}

async function renderAll(onProgress) {
  const fontCSS = await fontFaceCSS(), enc = new TextEncoder();
  const files = [];
  for (const p of document.querySelectorAll('svg[data-file]')) {
    if (onProgress) onProgress('Rendering ' + p.dataset.file);
    const w = +p.getAttribute('width'), h = +p.getAttribute('height');
    const xml = await svgToXml(p, fontCSS);
    const blob = await xmlToPng(xml, w, h, p.dataset.file);
    files.push({ name: p.dataset.file, data: new Uint8Array(await blob.arrayBuffer()) });
    if (p.dataset.svg !== undefined) files.push({ name: p.dataset.file.replace(/\.png$/i, '.svg'), data: enc.encode(xml) });
  }
  const notes = document.getElementById('export-notes');
  if (notes) files.push({ name: EXPORT_NOTES_FILE, data: enc.encode(notes.textContent.trim() + '\n') });
  return files;
}

async function downloadKit() {
  const status = document.getElementById('kit-status');
  try {
    const files = await renderAll(t => { if (status) status.textContent = t + '…'; });
    const have = new Set(files.map(f => f.name)), missing = KIT_REQUIRED.filter(n => !have.has(n));
    const a = document.createElement('a'); a.href = URL.createObjectURL(makeZip(files)); a.download = ZIP_NAME; a.click();
    if (status) status.textContent = files.length + ' files packed' + (missing.length ? ' — MISSING: ' + missing.join(', ') : ' — complete.');
  } catch (e) { if (status) status.textContent = 'Export failed: ' + e.message; throw e; }
}
</script>
```

**Honest notes for the hand-off:** the SVG files keep their fonts embedded as data, which every
design tool and most sign shops accept; a printer who asks for "outlined text" converts it once in
their own software. If the tool's preview blocks the fonts from loading at export time, the PNG falls
back to a system font — the member tells you ("the font looks different in the file") and you re-run
the export after the fonts load.
