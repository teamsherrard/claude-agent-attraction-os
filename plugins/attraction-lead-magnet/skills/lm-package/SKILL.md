---
name: lm-package
description: >
  Builds the member's LEAD MAGNET PACKAGE — the one file they upload to Claude Design in Week 3: the
  Partner Offer as copy, the lead magnet word for word with its page outline, the opt-in page and the
  thank-you page word for word with their structure, the messaging (one-liner, headline, hook, button,
  keyword, call line, bios and DMs when written) and the design brief (what to build, who reads it,
  the brand from the Design Package brief or a clean neutral default, cover, page rules, mockup, when
  it's done). Assembled from the finished documents, never rewritten; saved to the campaign folder,
  dated, newest wins. Runs on its own at the end of the Week 2 session and again when the bios or the
  delivery kit are written. Also records "the PDF is done". Trigger on: "build my lead magnet
  package", "my lead magnet package", "rebuild my package", "what do I upload to Claude Design",
  "design brief for my guide", "make my guide a PDF", "the PDF is done", "my guide is designed".
---

# The Lead Magnet Package — the one file for Week 3's design session

In Week 3 the member opens Claude Design, uploads **one file** (plus the Design Package brief their brand chat
wrote) and gets the guide PDF with its cover, the opt-in page and the thank-you page built from it. That file is
the **Lead Magnet Package**: the offer, the guide, the page, the messaging and the build notes — copy, outline,
structure and messaging, nothing designed. **This skill assembles; it never rewrites a word of copy and never
renders a page, a PDF, an image or a mockup.** The words were finished by the skills that wrote them.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #3 (this is the ONE skill in the
plugin that writes design direction — Part V of the package IS the design brief), #10. The three laws:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. Output rules: `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`.

## When it runs
- **At the end of the Week 2 session**, right after the sales funnel outline and before the navigator's finish
  line — the navigator hands over the two texts just written; no welcome, no question.
- **"build my lead magnet package" / "rebuild my package"** on any later day — after "refresh my guide" or
  "refresh my page", or whenever the member wants the current one. `lm-delivery` and `lm-profiles` call it
  themselves after they save, so the Week 3 upload carries the DMs and the bios too.
- **"what do I upload to Claude Design"** → hand them the newest package (and remind them of the Design
  Package brief from their brand chat); build it first if none exists.
- **"the PDF is done" / "my guide is designed"** → Step 5 only; nothing is assembled or rewritten.

## Step 0 — Find the campaign (silent)
Pull the Brain (house rule 2). Read `memory/magnets.md` → the row the member means (the newest `written`,
`designed` or `live` row, or the one they named) → its campaign folder, and the row's intake block (`Funnel
doc:`, `Package doc:`). Three states:
- **No written magnet** → one line and the way back: *"Let's write the guide first — say 'set up my lead magnet
  for agents' and the package comes at the end of that sitting."* → `lm-navigator`. Never package a guide that
  doesn't exist.
- **A magnet but no funnel outline** (`Funnel doc: —`, no `Opt-In Funnel — [Guide Name]` doc) → *"Your guide
  needs its page before the package is complete — let's write that first, then I'll pack everything."* →
  `lm-funnel`, then back here. The package needs both.
- **Both present** → Step 1.

## Step 1 — Gather the parts (read, never rewrite)
Take each part from the first place it exists, in this order:
1. **The texts handed over in this session** (the navigator's run: the guide and the page just written).
2. **`~/attraction-brain/exports/`** — the structured texts the writers keep there, newest of each:
   `partner-offer-YYYY-MM-DD.txt` (the Brain's offer skill), `lead-magnet-[slug]-YYYY-MM-DD.txt`,
   `opt-in-funnel-[slug]-YYYY-MM-DD.txt`, `delivery-kit-[slug]-YYYY-MM-DD.txt`, `platform-profiles-YYYY-MM-DD.txt`
   (`[slug]` = the Guide Name in lower case, spaces as hyphens, punctuation dropped — output standard §2).
3. **The documents themselves, read back through the storage connector** — `Lead Magnet — [Guide Name]`,
   `Opt-In Funnel — [Guide Name]`, `Delivery Kit — [Guide Name]` in the campaign folder; `🪪 [Name]'s Platform
   Profiles — …` in `02 · Brand`; the Partner Offer document in `05 · Offer`.

A part that exists nowhere is **skipped with one honest line inside the package** (*"Bios: not written yet — say
'update my attraction bios' and rebuild the package."*) — never invented, never a bracket token. The guide and
the page are never skipped (Step 0).

From the Brain, read: `identity/offer.md` (`## The program`, the UVP one-liner, `## The framework` and its
one line, the deliverables, the `Why now`, `## How to talk about it` — the 30-second explanation, the video intro
line, the `Comment keyword:`, the `Lead-magnet seed:` line — and the header's `Join-gated package allowed:`);
`identity/brand-visual.md` (the Final kit · the Direction · the `## Design Package brief` block — before Week 3
all three are normally empty, and that is fine); `identity/compliance.md` (the first line `Status:` — `unset`
means the public documents could not have been written, so say so and stop at the way back — and the stamp:
brokerage name, license display, disclaimer verbatim; the logo rule); `identity/profile.md` (name, brokerage as
required, headshot location, handles); `brain.md` quick reference (the booking link); `memory/magnets.md` →
`## Current magnet` (keyword, funnel URL, download link).

## Step 2 — Assemble the package (structured text, output standard §4)
Copy is **verbatim** from the parts — nothing added, nothing cut, no "punching up", no title changed. Strip
each source document's own appendix (its `▸ NEXT …` and `▸ COMPLIANCE` bands); the package carries one appendix
at the end. Part bands are CAPS bands wrapped by rules (they become the headings); **every heading inside a part
is written as a sub-band — `──── THE PROMISE ────`, `──── SECTION 1 — HERO ────` — so it sits under its part**;
the guide's `── PAGE N - TITLE ──` lines stay as they are. Never a line of copy in capitals; never a `[` bracket
token; no skill ids anywhere in the file.

```
LEAD MAGNET PACKAGE — [GUIDE NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Built from: Partner Offer [date] · Lead Magnet [date] · Opt-In Funnel [date] (· Delivery Kit [date] · Platform Profiles [date] when present)
Everything your Week 3 design session needs in one file: your offer, your guide, your page, your messaging and the build notes. Upload this file to Claude Design in Week 3 together with your Design Package brief. The words are final; the design serves them.

────────────────────────────────────────────
HOW TO USE THIS IN WEEK 3
•  Open Claude Design, start one project for your lead magnet, and upload this file and your Design Package brief (your brand, from the Week 3 brand chat; without it the brief in Part V uses the clean neutral look).
•  Ask for the three pieces in Part V one at a time: the guide PDF with its cover, the opt-in page, the thank-you page. Say "copy verbatim from the package" — nothing added, nothing cut.
•  Save the PDF into your Guides folder, share it "anyone with the link", and tell me "the PDF is done". When the page is live, tell me "my funnel is live" with the link.

────────────────────────────────────────────
WHAT'S INSIDE
•  Part I — The offer: what the guide leads to.
•  Part II — The lead magnet: the page outline, then the guide word for word.
•  Part III — The opt-in page and the thank-you page: the structure, then the copy word for word.
•  Part IV — The messaging: the marketing language, the bios and the DMs.
•  Part V — The design brief: what to build and how.

────────────────────────────────────────────
PART I — THE OFFER
──── WHAT THE GUIDE LEADS TO ────
Program: [name · type · for · the 90-day outcome · format · cadence — from ## The program]
The one line: [the UVP one-liner]
The method: [## The framework → the one line]
Steps:
   •  [step 1 — what you do · the tool or template]      (every step, in order; the step the guide is cut from marked "— this guide")
   •  ...
What an agent gets:
   •  [the deliverables as outcomes, one per line]
Why now: [the offer's Why now, verbatim — the one honest reason; or omit the label]
How I talk about it: [the 30-second explanation]
Video intro: [the video intro line]
Comment keyword: [the offer's keyword] · Guide keyword: GUIDE
Register: [at Join-gated package allowed: yes → "the program is offered to agents who partner with me" · at no or unknown → "every public line is what I teach, my story and how I mentor — never a package for joining"]

────────────────────────────────────────────
PART II — THE LEAD MAGNET
──── THE OUTLINE ────
Title: [the guide's title, exactly]
Promise: [the subtitle line]
Pages:
   •  Cover — [title] · [subtitle]
   •  Page 1 — [the opening title]: [one line on what it does]
   •  Page N — [title]: [one line]      (one per PAGE block, in order)
   •  How [First name] helps next — the close, with the one booking button
   •  The back page — contact, socials, the compliance line
The copy follows, word for word, exactly as the guide document reads.
──── THE PROMISE ────
[the Lead Magnet doc's THE PROMISE band, verbatim: Title · Subtitle · Byline · Hook]
──── THE GUIDE ────
[every ── PAGE N - TITLE ── block, verbatim, in order]
──── HOW [FIRST NAME] HELPS NEXT ────
[verbatim]
──── THE BACK PAGE ────
[verbatim]

────────────────────────────────────────────
PART III — THE OPT-IN PAGE AND THE THANK-YOU PAGE
──── THE STRUCTURE ────
The page reads in this order; every opt-in button opens the one pop-up; submitting lands on the thank-you page.
   •  1 Hero · 2 The problem · 3 The product · 4 Who I am · 5 The journey · 6 The offer · 7 Why join me · 8 Proof · 9 The organization · 10 Book a call · 11 The opt-in
   •  The pop-up: first name · email · phone (optional) · the reassurance line · the button
   •  The thank-you page: the confirmation · the instant download button · the call, offered · where to find me · the footer
The copy follows, word for word, exactly as the sales funnel outline reads.
──── SECTION 1 — HERO ────
[verbatim]
... (every section band, THE OPT-IN POP-UP, THE THANK-YOU PAGE and FOOTER, verbatim, in order)

────────────────────────────────────────────
PART IV — THE MESSAGING
──── THE MARKETING LANGUAGE ────
The one line: [the UVP one-liner]
Headline: [the hero headline] · Pre-headline: [the hero pre-headline] · Subhead: [the hero subhead]
Hook:
   •  [the cover's three lines]
Attraction line: [from the hero]
CTA button: "Get the Free Guide" · Keyword: GUIDE
The call: [the closing page's call to action, with the booking link — or the "email me at …" / "message me on Instagram @…" fallback exactly as the guide carries it]
Why now: [the offer's Why now, verbatim — or omit the label]
──── THE BIOS ────
[each platform's bio from the Platform Profiles pack, verbatim, one labelled block per platform — or the one honest line that they are not written yet]
──── THE DMS AND THE DELIVERY EMAIL ────
[the Delivery Kit's comment reply, DM 1–3, the delivery email, the 3-frame story — verbatim — or the one honest line]
──── WORDS WE DON'T USE ────
   •  No compensation, splits, revenue share, stock or income figures anywhere public.
   •  No ranking, no stars, no "best", no other brokerage's name or logo.
   •  [the register line from Part I]
   •  No invented urgency — the one honest why-now above is the only one.
   •  The type of agent is a career stage, production level, model or mindset — never a protected characteristic.

────────────────────────────────────────────
PART V — THE DESIGN BRIEF
DESIGN BRIEF — [GUIDE NAME]
[Name] · [Brokerage] · [Date]
──── WHAT TO BUILD ────
•  A styled PDF of the guide: the cover + one interior page per "── PAGE N - TITLE ──" block in Part II + the closing page ("How [First name] helps next") + the back page; the compliance footer on every page.
•  The opt-in page, section for section from Part III, every opt-in button opening the one pop-up.
•  The thank-you page from Part III: the instant download button pointing at the finished PDF, the call offered, the footer.
•  A cover image for the opt-in page, Reels and stories: the flat cover page exported from the PDF (a 3D mockup only if the tool can export it as a picture — the flat cover is the dependable version).
•  Format: letter or A4 to match where you are, portrait; phone-readable at 100%.
──── WHO READS IT ────
[the type of agent, by stage, in one line] · they open it on a phone, from a Reel or a bio link · tone: [the feel from the Design Package brief when it exists — else "calm and useful, never salesy"].
──── THE BRAND ────
From your Design Package brief (do not improvise): Logo: 02 · Brand/[file] · Colours: [hex and role, each] · Fonts: [heading] / [body] · Headshot: 02 · Brand/[file] · Tagline: "[ ]"
  — or, before the Week 3 brand chat: a clean neutral look — the member's headshot, one dark text colour, no accent unless the member names one, the brokerage logo only where compliance requires it; the Week 3 kit restyles everything.
Brokerage mark: [where it must appear and relative size — from the compliance file]; the brokerage's own colours are not the palette — ours stay distinct.
──── THE COVER ────
Title: [exactly as Part II] · Subtitle: [exactly] · "By [Name], [Brokerage as required]" · "Last updated [Month YYYY]" when the guide carries that line (keep it — it is dated on purpose).
No ranking language, no stars, no "best", no other brokerage's name or logo anywhere.
──── THE GUIDE PAGES ────
•  Copy verbatim from Part II — every word, including the source notes in parentheses and the "verify current" line on page 1. Nothing added, nothing cut.
•  One page per PAGE block, in order. A comparison-shaped guide's model pages in the same layout (same length, same blocks). A checklist page with real boxes; a plan or template page with real fill-in rows; a mini-course lesson page with its template in full.
•  The labelled lines become page elements and never print as labels: the pull quote set large, the callout a panel, the checklist real boxes, template rows fill-in lines, scripts message bubbles, the source a footnote, the image idea the page's visual, the next step the closing strip.
•  The page the reader will screenshot (the checklist, the system at a glance, the questions) legible in one phone screenshot.
•  The closing page carries the booking link as the ONE button, plus the social handles; nothing else gets a button.
•  The compliance footer on every page: [the stamp, verbatim].
•  Photos: the member's headshot on the closing page; real photos of the organization only if supplied — never stock people, never another brokerage's event.
•  Body text 11pt or larger; contrast that passes on a phone.
──── THE OPT-IN PAGE AND THE THANK-YOU PAGE ────
•  Sections in Part III's order, copy verbatim, every section's own headline; the Hero's video embed (or the cut-out headshot where the Video line says to record); the Book-a-call area as the booking embed or a button to the link.
•  Every opt-in button opens the one pop-up (first name · email · phone optional); the button words exactly "Get the Free Guide".
•  The form must really send the name and email — test-submit once before any traffic; a page that looks right can still capture nothing.
•  The thank-you page's download is an instant download of the finished PDF — never "check your inbox"; the call offered under it, optional.
•  The compliance stamp is the footer of both pages.
──── THE MOCKUP ────
The flat cover as its own page in the PDF (export that page as the cover image) · if the tool exports pictures: a square crop for Instagram, a 9:16 crop for stories, and a 3D booklet mockup with a soft shadow. The flat cover is enough to go live.
──── WHEN IT'S DONE ────
Save the PDF (and any cover images) into the same Guides folder as the guide in your drive · share the PDF "anyone with the link" — that link is the thank-you page's download button · tell me "the PDF is done" · when the page is live, test-submit the form once and tell me "my funnel is live" with the link.

════════════════════════════════════════════
▸ COMPLIANCE
[the stamp — set or confirmed only; never a bracket token]
```

Write the real values in — never a `[` bracket token in the file the member uploads. Where the brand kit is
empty (the normal Week 2 case), write the neutral-look line and say the Week 3 kit replaces it; never invent a
hex code, a font or a logo. The register line (Part I) and the "words we don't use" list (Part IV) are written
from the offer's `Join-gated package allowed:` value — at `no` or `unknown` nothing in the package may read
"join me and get X".

## Step 3 — Save, deliver, log
1. **Render** the text with the shared renderer (output standard §3–§4):
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/package.txt "Lead Magnet Package — [Guide Name] — YYYY-MM-DD.docx" --title "Lead Magnet Package — [Guide Name]" --subtitle "[Name · Brokerage · City]" --eyebrow "Agent Attraction Lead Magnet · the Week 3 upload"`
   and upload the `.docx` into the **campaign folder** (output standard §6; the fallback chain applies —
   `RENDERER-UNAVAILABLE` or no sandbox → the plain-document upload and its one line). Read the finished
   document back once: every part a heading, every sub-band a subheading, full depth (the whole guide and the
   whole page, never a summary). Dated name: a rebuild is a new dated copy; **the newest date is current**.
2. **Keep the text** at `~/attraction-brain/exports/lead-magnet-package-[slug]-YYYY-MM-DD.txt` (the Brain
   syncs `exports/*.txt`, so a rebuild on another day starts from it).
3. **Deliver in chat** — the link, the title, and five plain lines: what is inside (the five parts in a breath),
   that this is the one file for Claude Design in Week 3 with the brand brief, where it lives ("your Guides folder,
   beside the guide"), that "rebuild my package" refreshes it, and what is not in it yet (the bios or the DMs, with
   the phrase that writes each). Never the full text in chat; never a file path spoken as a path.
4. **Log it (silently):** in `memory/magnets.md` the row's intake block gets `Package doc: YYYY-MM-DD` (replace an
   older stamp). **attraction-brain-sync PUSH** (write → push → verify — the Brain Board picks it up). Never
   narrate this or name the file (house rules #1).

## Step 4 — When another skill calls it (silent)
The navigator (end of the Week 2 session), `lm-delivery` and `lm-profiles` (after they save) run Steps 1–3 with
no welcome and no question; the caller adds one line to its own close (*"your Lead Magnet Package is rebuilt, so
Week 3 has these too"*). If the gather fails (no exports, connector down) the caller says so in one line and
names "rebuild my package" for later — never a stop, never a retry loop.

## Step 5 — "the PDF is done" / "my guide is designed" (record only)
In `memory/magnets.md`, move the row's Status to `designed` (never backwards) and set `## Current magnet` →
download link when the member gives it. **attraction-brain-sync PUSH.** One line back: *"Recorded — your guide is
designed. When the page is live, say 'my funnel is live' with the link and every system points at it."* Nothing
is rewritten or rebuilt.

## Never
- Rewrite, shorten, "improve" or re-title any copy while assembling. The documents are the truth; the package is
  the carrier.
- Render a page, a PDF, an image or a mockup. The package is the deliverable; Claude Design builds in Week 3.
- Invent a colour, a font, a logo or a hex code. Empty kit → the neutral-look line, labelled.
- Put another brokerage's name or mark anywhere; rank anything; add stars or "best"; print a bracket token; name a
  skill id in front of the member; package a guide without its page outline.

## Quality checklist
- [ ] Both campaign documents present (the guide and the page outline); the offer read; compliance `set` or `confirmed`
- [ ] Parts I–V all present; a missing optional part carries its one honest line and the phrase that writes it
- [ ] Copy verbatim; the source appendices stripped; one `▸ COMPLIANCE` appendix at the end
- [ ] Part bands as CAPS bands with rules; every inner heading a `──── sub-band ────`; no copy line in capitals; no `[` token
- [ ] The register line and the "words we don't use" list match `Join-gated package allowed:`
- [ ] Rendered, uploaded to the campaign folder with the dated name, read back at full depth; the text kept in `exports/`
- [ ] Chat = link + title + five lines; `Package doc:` stamped; pushed
