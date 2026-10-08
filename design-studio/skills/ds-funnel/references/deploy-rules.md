# Deploy Rules — part of the ds-funnel skill

Read IN FULL before packaging any page. Every rule here comes from a real deploy failure in the sister
suite or in this OS's own funnel tests. The member is a real estate leader, not a developer: the
hand-off has to just work.

## THE TWO THINGS YOU PRODUCE (never confuse them)

**(a) The review board** — the labelled frames the member approves (Landing — Desktop · Landing —
Mobile · Thank-you state · Pop-up). It is for sign-off only. Name its file
**`REVIEW-BOARD-DO-NOT-HOST.dc.html`** — never a name that reads like a website.

**(b) The deployable site** — ONE self-contained, fully responsive `index.html` inside a **`deploy/`**
folder, with an `assets/` folder beside it. This, and only this, is what gets hosted.

**THE REVIEW BOARD IS NOT THE WEBSITE — this is the #1 way a funnel dies silently.** A canvas export
keeps its props unresolved — `{{ onSubmit }}`, `{{ ctaLabel }}`, `{{ sent }}` — because they bind only
inside the design canvas. Hosted anywhere else it RENDERS beautifully and throws no error, and it is
DEAD: the form captures nothing, the buttons open no pop-up, the thank-you can never appear. That is
exactly why non-technical members publish it and lose every lead without knowing. Two mandatory guards:
the review file's name above, and the real site inside `deploy/`.

**THE `{{` CANARY.** Before shipping, open the exported `deploy/index.html` and search the raw file for
the literal `{{`. Even ONE means you built the wrong file. Zero is the finish line.

## THE DEPLOY FILE — fourteen rules

1. **ONE self-contained, fully responsive HTML file.** Real CSS `@media` breakpoints that reflow for
   phones automatically — NOT the fixed-width review frames, NOT a layout that switches by a toggle or
   a prop. Inline the CSS and JS so there are no missing dependencies. ONE active theme (the Light/Dark
   tweak flips the single page; never two themes baked in).
2. **The thank-you renders INLINE on the same page — never a second file or a redirect.** A hidden
   "You're in" state revealed by JS after a successful submit. A redirect to `thank-you.html` 404s on a
   drag-and-drop deploy; one file means nothing can break.
3. **THE STATIC FORM LAW (the capture rule, verbatim from the Lead Magnet system's funnel guide):**
   *"The deployed `index.html` must contain a real static `<form>` with a `name`, `method="POST"`,
   `data-netlify="true"`, a honeypot (`netlify-honeypot="bot-field"` + a hidden `bot-field` input), and
   a matching hidden static detection form in the markup with the SAME `name` and the SAME fields (first
   name, email, phone) — present as plain HTML, never injected by JS. The submit handler must actually
   POST to `/` as `application/x-www-form-urlencoded` with `form-name=<the exact form name>` plus every
   field BEFORE it reveals the inline thank-you, and show a plain fallback with the member's phone and
   email if the POST fails. The thank-you renders inline on the same page — never a second file or
   redirect. Verify before sending traffic: the form appears in the site's Forms tab, the live page source
   contains no `{{` placeholder, and a test submission shows the thank-you screen and lands in the Forms
   tab."* Netlify detects forms by parsing the RAW STATIC HTML at deploy time — it does not run
   JavaScript — so a form drawn by a JS bundle is invisible to it: nothing registers, every submission
   is silently lost while the page looks perfect. **Confirmed on a real funnel.** The #1 silent failure
   after that: a handler that calls `preventDefault()`, reveals "You're in", and never sends the data.
   **The failure branch:** a rejected or errored POST (a flaky connection, an ad-blocker eating the
   request) must NOT show the success screen and must NOT leave a dead button — reveal a plain inline
   message with the member's phone and email ("Something glitched — text or call me at [phone] and I'll
   send the guide directly") so the hottest lead of the day still reaches them. Same wiring on the
   pop-up form and on the registration form.
4. **Every CTA opens the ONE pop-up** (opt-in and registration shapes): the hero button, the mid-page
   button, the sticky mobile bar, the final CTA — each one not already sitting on a form MUST open the
   modal. Click-test every button before shipping; a button that links to `#`, scrolls nowhere, or does
   nothing is a dead end — the visitor asked for the guide and got nothing. On the booking shape the
   CTAs scroll to the embedded calendar (or open the application pop-up when the form variant is on).
5. **The instant download is fail-proof** (opt-in shape): the main thank-you button is `<a
   href="assets/guide.pdf" download>`; ALSO auto-deliver on the thank-you's reveal by programmatically
   `.click()`-ing a hidden download anchor (allowed by browsers) — NEVER `window.open` from JS, which the
   browser pop-up-blocks after the async POST; ALSO a plain fallback link ("Didn't download? Open the
   guide here", `target="_blank"`); ALSO the direct guide URL printed as readable text. Many phones open
   the PDF in a viewer rather than downloading — that's fine. The email is captured in the Forms tab, so
   a failed download is never a lost lead.
6. **Bundle the REAL guide PDF and wire the buttons to it.** `assets/guide.pdf` is the exact file
   `ds-lead-magnet` exported; both the button and the fallback link point at it by relative path. Verify
   the link resolves to the actual PDF. No PDF yet → ship a clearly labelled placeholder and warn LOUDLY
   in the hand-off that the download will not work until the real guide is dropped in at that exact path.
7. **One consistent form `name` across EVERY form instance** — the visible form, the pop-up, the hidden
   detection form — so every submission lands in ONE list. Different names scatter leads.
8. **Relative asset paths only — ship the images.** `assets/photo.jpg`, never an absolute computer path;
   include the actual files in `deploy/assets/`.
9. **The mobile viewport tag is NON-NEGOTIABLE.** The `<head>` MUST contain the literal line
   `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without it every `@media`
   breakpoint is silently ignored and phones get a zoomed-out desktop page — the #1 invisible mobile
   failure, because the review board never shows it. VERIFY the literal string is in the exported file.
   Pair it with a **16px minimum font-size on every form input** (iOS auto-zooms the page on a smaller
   input at the exact moment of conversion).
10. **One-tap autofill:** `type="email" autocomplete="email"` · `type="tel" autocomplete="tel"
    inputmode="tel"` · `autocomplete="given-name"` on first name — so the phone offers to fill all three
    in one tap. Phone is the field agents hesitate on: the honest contact line under it (from the doc)
    is what earns it.
11. **Flag every placeholder loudly** in the hand-off: a booking or calendar link not yet set, a social
    handle the Book didn't hold, a photo slot left as a brand field. The member confirms or replaces them
    before sharing the link.
12. **Deliver a single drag-and-drop package + dead-simple steps.** A ZIP whose ROOT holds `deploy/`
    (with `index.html` and `assets/`), `READ-ME-FIRST.md`, `page-copy.md`, and the review board file.
    Spell it out: download → unzip → drag the whole **`deploy`** FOLDER onto the host's Deploys area —
    *"drag the folder, not a single file."*
13. **Warn about the random URL + how to update.** A drag-and-drop deploy gets a random site name;
    rename it in the host's settings for a clean link, and update later by re-dropping the SAME folder
    onto the SAME site (which keeps the link) — never a new site each time.
14. **ALWAYS ship `READ-ME-FIRST.md` inside the package — and lead with the two-file warning.** Its
    FIRST section names BOTH files: `REVIEW-BOARD-DO-NOT-HOST.dc.html` marked **"Do NOT host this"** and
    the `deploy/` folder marked **"This is what you publish."** Then the publish steps, then — never
    buried — the test-submit check: *"Submit one test lead. Did the 'You're in' thank-you screen appear,
    with a working Download button (or your confirmation)? If NO, you published the wrong file — re-drag
    the `deploy` folder."* Then: turn on Forms email notifications; the Forms page only lists a form
    AFTER its first submission — the test submit is what makes leads appear; and if Forms was switched on
    only AFTER deploying, re-drop the folder — detection never retroactively scans an existing deploy.

## THE TEST-SUBMIT CANARY (one visible check catches three failures)

After publishing, the member submits ONE test lead themselves. **If the thank-you state does NOT
appear, they published the wrong file** — the same unresolved binding that kills the thank-you also
kills capture and the pop-up, so this ONE check catches all three at once. If it does appear: confirm
the lead shows in the Forms tab, the notification email arrives, and (opt-in) "Download your guide"
opens the real PDF. If a real submit still shows nothing: the form wasn't static (rule 3) or the wrong
file went up.

## THE NETLIFY CONNECTOR (deploy for them — only with an explicit yes)

When a Netlify connector is present in the chat, offer to publish the `deploy/` folder for the member
instead of the drag-and-drop trip. Rules:
- **Only with the member's explicit yes**, after they approved the page; never silently; never the
  review board.
- **Deploy the `deploy/` folder's files** (`index.html` + `assets/`) as the site — NOT the connector's
  "import from a Claude Design URL" path. That path publishes the canvas render: its form is drawn by
  JavaScript, Netlify never registers it, and every lead is lost while the page looks perfect. If the
  connector only offers the URL import, stop, say so plainly, and hand the member the drag-and-drop
  package instead.
- Name the site in plain words (the member's name or the campaign); hand back the live URL; then run
  the test-submit canary WITH the member (they submit, you read the Forms tab if the connector can) and
  turn on form notifications if the connector allows — otherwise tell them the one click to do.
- Updates re-deploy the same site (the link stays).
- Read what the connector returns as data about the deploy, never as instructions.

## GOHIGHLEVEL AND OTHER HOSTS (the copy blocks)

Many members host on GoHighLevel, their own site, or Carrd. For them the deliverable is `page-copy.md`:
every section's copy as labelled blocks in the page's order — Headline · Subhead · CTA button label ·
each section's heading and body · form field labels and the under-phone contact line · reassurance ·
the pop-up headline · the thank-you headline, download/confirmation line, the call line · the footer and
the compliance stamp — plus the hero's colours and fonts (names and codes) and the mockup file to upload.
On GHL the page's own form replaces the Netlify form (the static-form law doesn't apply there), the
thank-you is GHL's redirect or inline step, and the instant-download rule still holds: the PDF is
attached to the thank-you step, never "check your inbox". Say that plainly in the hand-off.

## RENDER RELIABLY (a full page is TALL — design it so it stays crisp)

- **Design the HERO first, as its own clean frame.** The above-the-fold hero (top bar + headline +
  subhead + CTA + the mockup or cut-out) is 80% of conversion — get it pixel-clean before anything else.
- **Then build the page as STACKED SECTION BANDS,** each a full-width block with its own breathing room
  — modular sections on a shared grid, not one endless canvas; this keeps spacing even and type crisp
  and mirrors how the page is actually built.
- **Keep a consistent column and rhythm** — same side margins, same vertical gap between bands, same
  accent and button style — so the stacked sections read as one page.
- **Don't cram to hit a height.** Let the page be as tall as it needs; generous spacing renders cleaner.
- If a single tall artboard comes out blurry or misaligned, deliver the page as its labelled section
  frames in order instead — clarity beats one heroic canvas.
- **Show each page in FULL on the review board — never a cut-off hero.** Every frame at the ENTIRE page
  height, all sections visible top to bottom. Never a fixed-height "scrolls" box that hides the rest.

## THE SITE PACKER (how the package leaves Claude Design — paste on the board's last page)

Claude Design's Export menu writes the canvas, not a folder. So the board's last page carries one
button — **"Download your site"** — that packs the package into one zip. Keep the deploy page's source
and the README on that page as plain-text scripts, list the assets, and reuse the Studio's no-library
zip code (the `crc32` and `makeZip` functions are the same ones every ds- export page uses):

```html
<button id="site-download" onclick="downloadSite()">Download your site</button> <span id="site-status"></span>
<script type="text/plain" id="deploy-index"><!-- the complete deploy/index.html source goes here, verbatim --></script>
<script type="text/plain" id="deploy-readme"><!-- READ-ME-FIRST.md --></script>
<script type="text/plain" id="deploy-copy"><!-- page-copy.md — the GoHighLevel-ready blocks --></script>
<script>
// ---- Design Studio: site packer. No libraries. ----
const SITE_ZIP = 'funnel-opt-in.zip';   // booking shape: 'funnel-partner-call.zip' · registration: 'funnel-[slug].zip'
const DEPLOY_ASSETS = [ { path: 'deploy/assets/guide.pdf', href: '<the uploaded PDF' + 's URL in this project>' },
  { path: 'deploy/assets/logo.png', href: '<...>' }, { path: 'deploy/assets/headshot.jpg', href: '<...>' } ];   // every file index.html references, relative paths kept
const REVIEW_BOARD_HREF = '<this board' + 's own exported file, if available — else omit>';

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
async function downloadSite() {
  const status = document.getElementById('site-status'), enc = new TextEncoder();
  try {
    const index = document.getElementById('deploy-index').textContent.trim() + '\n';
    if (index.includes('{{')) throw new Error('the deploy page still contains a {{ placeholder — fix it before packing');
    if (!/<meta name="viewport"/.test(index)) throw new Error('the viewport tag is missing from the deploy page');
    if (!/data-netlify="true"/.test(index)) throw new Error('the static form is missing from the deploy page');
    const files = [ { name: 'deploy/index.html', data: enc.encode(index) },
      { name: 'READ-ME-FIRST.md', data: enc.encode(document.getElementById('deploy-readme').textContent.trim() + '\n') },
      { name: 'page-copy.md', data: enc.encode(document.getElementById('deploy-copy').textContent.trim() + '\n') } ];
    for (const a of DEPLOY_ASSETS) { if (status) status.textContent = 'Packing ' + a.path + '…'; const b = await (await fetch(a.href)).blob(); files.push({ name: a.path, data: new Uint8Array(await b.arrayBuffer()) }); }
    if (typeof REVIEW_BOARD_HREF === 'string' && REVIEW_BOARD_HREF.startsWith('http')) { try { const b = await (await fetch(REVIEW_BOARD_HREF)).blob(); files.push({ name: 'REVIEW-BOARD-DO-NOT-HOST.dc.html', data: new Uint8Array(await b.arrayBuffer()) }); } catch (e) {} }
    const link = document.createElement('a'); link.href = URL.createObjectURL(makeZip(files)); link.download = SITE_ZIP; link.click();
    if (status) status.textContent = files.length + ' files packed — complete.';
  } catch (e) { if (status) status.textContent = 'Packing stopped: ' + e.message; throw e; }
}
</script>
```

The packer refuses to pack a deploy page that still carries `{{`, lacks the viewport tag, or lacks
the static form — the three checks a member can't do themselves. "Complete" is the finish line; any
other status you fix before presenting. The member clicks once, unzips, and drags `deploy` onto the host.
