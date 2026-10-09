# Brain Doc Formatting — render deliverables as clean, formatted .docx

How the Brain's skills save documents (the Partner Offer, the Scorecard, the Why Join Me doc, the Model Positioning Sheet) so
they're organized in Drive and genuinely look good. When a skill says "save as a clean doc (doc-formatting
standard)," it means this. **Every deliverable is rendered to a formatted `.docx` in one neutral house style —
the same clean look for every member (no colour, no per-member branding).**

## How to save — render structured text to a styled `.docx`
The skill writes the **structured text** (the grammar below: CAPS section dividers, `•` bullets, `Label:`
lead-ins); the shared renderer turns it into real Word formatting — headings, bullet lists, tables —
automatically.
1. Assemble the deliverable as structured text; write it to a temp file, e.g. `/tmp/doc.txt`.
2. Render it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Agent · City]"`
   (optional `--accent HEX` — the member's primary brand colour, see the look below; omit it for the neutral default)
   → produces the house style: **Arial**, **near-black** text, real **headings** (true Word heading styles, so
   the navigation pane and the Google Docs outline work), **bullet lists**, **tables**, thin light-grey rules,
   and a header/footer with `Page X of Y`. *(If the script prints `RENDERER-UNAVAILABLE` — `python-docx` is not
   installed — do exactly what it says: **install nothing, never run pip, never retry the command**; save the
   same structured text as a `.md` file, upload THAT to the same folder, and tell the member in one plain line
   that the styled version needs the renderer. Delivery never stops.)*
**NEVER upload the raw structured text as the deliverable.** The structured text (CAPS bands, `────`
rules, `Label:` lead-ins) is the RENDERER'S INPUT, not a document. If a Google Doc ever shows literal
`════`/`────` dash lines as text, the raw input was uploaded instead of the rendered file — that is a
FAILED delivery: re-render and upload the `.docx` (ONE corrective re-upload — if it happens again,
stop and tell the member instead of re-uploading in a loop). **The one sanctioned exception** is the renderer's
own fallback: when `render_doc.py` exits with `RENDERER-UNAVAILABLE`, the structured text is saved as a `.md`
FILE (a plain file, not a converted Google Doc) and uploaded with the one-line note — that is what the script
instructs, and it is the whole fallback chain: `render_doc.py` → `.md` upload + the note → done. No
`pip install`, no second renderer, no retry loop; a package install in a sandbox can block for many minutes
and looks like a hang. A plain-text wall pasted into chat is still not an acceptable output at any step.
**Build + verify (EVERY document):** build ONLY via `render_doc.py` — never hand-write document XML, never
reach for another document tool when the renderer is unavailable (the `.md` fallback above is the path). Before uploading, read the finished `.docx` text back and check:
(a) no raw `<w:` markup in the content — if you see any, the build is corrupt: rebuild; (b) **depth matches
the deliverable — member-facing guides and the master AI Brain doc are FULL, multi-page documents that
render the COMPLETE source content, never summaries.** Rich brain + thin render (a full brain under
~2,000 words) = a FAILED render — rebuild with the full content before uploading. Agents pay a premium
for this system; the documents must feel like it.
3. Upload the **`.docx`** to the member's **workspace**, in the folder `shared/drive-map.md` assigns that
   deliverable type (content → `03 · Content/…`;
   the master doc and the scorecard → `01 · AI Brain`; offer documents → `05 · Offer`; prospect research → `04 · Agents/Prospects`). Confirm in plain words with the real
   location: *"Saved to your Drive → [workspace] → [folder] → [name]."*

## Naming
`[Deliverable] · [Subject] · [Date]` — Title Case, ISO dates. Examples:
- `Partner Offer · [Member] · 2026-11-14`
- `Top-50 · [Member] · 2026-11-14`
- `Why Join Me · [Member] · 2026-11-14`

## The look the renderer produces (one neutral standard for every member)
- **Arial** everywhere (never a serif). **Near-black** titles / headings / body; **dark grey** only for the
  small byline / kickers / footnotes.
- **Type scale:** body **11pt** at 1.2 line spacing, 6pt after, widow/orphan control on · section headings
  (real `Heading 1`) **14pt** bold tracked caps over a thin light-grey rule · sub-bands and ALL-CAPS
  sub-labels (real `Heading 2`) **12.5pt** bold · title **30pt** (`Title` style) · table text **10pt** ·
  eyebrow / kickers **9.5pt** grey tracked · small print 8.5–9.5pt grey. Book mode: chapter titles **20pt**
  and part titles **24pt** (both `Heading 1`, with a 9.5pt / 10pt kicker above), contents entries 11pt with
  9.5pt grey summaries. Headings, kickers and a `Label:` line directly above a table are keep-with-next —
  a heading never ends a page.
- **Header + footer** on every page after the first (the title page / cover carries neither): the document
  title top-right; the subtitle + eyebrow bottom-left; **`Page X of Y`** bottom-right — live fields that
  Word and Google Docs both update.
- Section headings: bold black + a thin light-grey underline. **Real** bullet lists. **Real** tables
  (bold header row on a light tint of the accent, white / off-white alternating rows, hairline horizontal
  rules only plus the outer frame, header row repeats when a table crosses a page). `>> ` callouts (book
  mode) are indented blocks with an accent bar on the left over a very light tint.
- **One optional accent colour (`--accent HEX`, default near-black `111111`)** — the only member-specific
  element: it colours the title rule, the PART kickers, the callout bar and the table-header tint, nothing
  else. Pass the member's primary brand colour when `identity/brand-visual.md` records one (the Brain Book
  build does — `brain-book-spec.md` step 6); a colour too light to read on white falls back to near-black
  for text and keeps the tint. **No other member branding.**
- These are clean working documents. For a *visually designed* member-facing piece (e.g. a lead-magnet PDF),
  produce the clean copy here and the agent drops it into their design tool — branding lives there.

## The structured text the renderer reads (write the doc in this grammar)
- **Title line** at the top; a light **meta line** under it (agent · city · date); then a blank line.
- **Section headers in ALL CAPS**, each wrapped by a divider rule
  (`────────────────────────────────────────────`), then a blank line. *(The renderer turns these into real
  headings — the rule is just the marker; `─`, `═`, or `—` all work.)*
- **Generous blank-line spacing** between blocks. **Bullets** with `•`, one point per line.
- **Numbered steps** as `1.  …` lines, one step per line (an indented continuation line joins its step). Open
  a step with a plain word. Never open it with a capital letter followed only by capitals, digits and spaces
  up to a hyphen, dash or period — the renderer reads that run as a bold lead and splits the step there:
  `1. A 45-minute call` renders as a bold "A 45-" followed by "minute call". Write
  `1. The welcome call — 45 minutes …` instead. The one sanctioned bold lead is deliberate: ALL CAPS, ending
  in a dash (`1. WELCOME CALL — 45 minutes …`).
- **Labels and cues on their own lines** (e.g. `HOOK (read word-for-word)` then the hook on the next line) —
  scripts and captions never run together as a blob. **Copy the agent will paste** (captions, hashtags,
  descriptions) under a clear label, ready to grab.
- **Sub-headings inside a section** as `──── Label ────` (the label up to **80 characters**) → a real
  `Heading 2`. A longer label does NOT parse: it renders as body text WITH its literal dashes — a visible
  failure — and the renderer prints `WARNING: sub-band label is N characters (cap 80) …` on stderr; shorten
  the label and re-render (any renderer WARNING is a failed build).
- **Tables — pipe rows:** `| Week | Calls | Posts |` on one line per row (optional `| --- | --- |`
  separator after the header) → the renderer builds a real styled table (tinted bold header row that
  repeats across pages, alternating rows). A `Label:` line directly above the table stays on the same page
  as the table. Use for anything tabular: KPI dashboards, brand colours + roles, avatar-at-a-glance, money math.
- Plain structured text in the body (no Markdown `#`/`**`/backticks) — the renderer applies the formatting.

**BOOK MODE (long deliverables — the Agent Attraction Brain Book).** The renderer switches into book mode when
the input contains a `[[TOC]]` block (or `--book` is passed); everything below is inert in normal docs,
which render exactly as before:
- **Cover page** — the title block becomes page 1 (title, eyebrow, byline, date), then a page break.
- **Contents page** — a `[[TOC]] … [[/TOC]]` block right after the title/meta lines; one row per
  chapter as `Chapter Title :: one-line summary` (PART rows carry no summary). Renders as a linked
  CONTENTS beginning on page 2 — each row an internal link to its chapter — followed by a page break
  (with 18+ chapters the contents runs onto a second page; expected, and still one CONTENTS). Row text
  left of `::` must match the chapter band character-for-character; a mismatch prints
  `WARNING: TOC entry "…" has no matching heading` on stderr — treat any warning as a failed build.
- **`PART I — TITLE` / `CHAPTER N — TITLE` CAPS bands** get an eyebrow kicker, a page break before
  each, the bookmark the contents links to, and an outline level (Google Docs shows every chapter in
  its outline sidebar).
- **`>> ` insight callouts** — a line starting `>> ` renders as an indented key-insight block with an
  accent bar on the left over a very light tint (script cue heads `ON SCREEN` / `PAUSE` / `FACT:` stay
  cues even in book mode).
- **Part opener pages** — after a PART band's intro paragraph the renderer appends **"IN THIS PART"**, a
  linked list of that part's chapters (number · title · contents summary) built from the `[[TOC]]` rows.
- **Header + footer** (title · member line + eyebrow · `Page X of Y`) render automatically on every page
  after the cover.
- **Long inputs are appended band by band, never emitted in one block** — the renderer cannot tell a cut-off
  input from a finished one, so a Book's input file is written one PART/CHAPTER at a time and passes the
  structural pre-check (band and contents-row counts) before `render_doc.py` runs; the rule and the exact
  check live in `brain-book-spec.md`, build pipeline step 3.
The Book's full structure contract (what goes in the TOC rows, callout discipline, chapter labels)
lives in `brain-book-spec.md` — this file only documents the grammar.
