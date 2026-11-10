---
name: lm-package
description: >
  Writes the LEAD MAGNET half of the member's Week 3 Kit — the one file they upload to Claude Design in
  Week 3 — and hands it to the Brain's kit builder: the guide's page outline and the guide word for word,
  the opt-in page and the thank-you page word for word with their structure, the messaging (headline,
  hook, button, keyword, call line, the bios and the DMs when written, the words we don't use) and the
  design brief for the guide and the page with plain builder notes. Assembled from the finished
  documents, never rewritten; no document of its own — the kit is the deliverable. Runs on its own at
  the end of the Week 2 sitting and again when the bios or the delivery kit are written. Also records
  "the PDF is done" (Status designed, the download link). Trigger on: "add my guide to my kit", "rebuild
  my lead magnet package", "my lead magnet package", "design brief for my guide", "make my guide a PDF",
  "the PDF is done", "my guide is designed".
---

# The lead magnet half of the Week 3 Kit

A member finishing Week 2 holds **three things**: their offer, their guide (the PDF agents download) and **one
Week 3 Kit** they upload to Claude Design. The kit is built by the Brain's `attraction-week3-kit`; its Part A is
the offer, its Part B is the lead magnet — the guide and the page word for word, the messaging and the design brief
for the guide and the page. **This skill writes Part B's text and hands it to the kit builder. It saves no document
of its own, never rewrites a word of copy, and never renders a page, a PDF, an image or a mockup.**

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #3 (this is the ONE skill in the
plugin that writes design direction — the design brief inside Part B), #10. The three laws:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`. Output rules: `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`.

## When it runs
- **At the end of the Week 2 sitting**, right after the sales funnel outline and before the navigator's finish
  line — the navigator hands over the two texts just written; no welcome, no question. The kit builder then saves
  the one kit with both parts.
- **"add my guide to my kit" / "rebuild my lead magnet package"** on any later day — after "refresh my guide" or
  "refresh my page", or whenever the member wants the current version. `lm-delivery` and `lm-profiles` call it
  themselves after they save, so the kit carries the DMs and the bios too.
- **"the PDF is done" / "my guide is designed"** → Step 4 only; nothing is assembled or rewritten.
- "What do I upload to Claude Design" belongs to the Brain's kit builder (`attraction-week3-kit`); when it lands
  here, run Steps 0–3 and let the kit builder answer with the kit.

## Step 0 — Find the campaign (silent)
Pull the Brain (house rule 2). Read `memory/magnets.md` → the row the member means (the newest `written`,
`designed` or `live` row, or the one they named) → its campaign folder, and the row's intake block (`Funnel doc:`,
`Kit doc:`, `Reach:`). Three states:
- **No written magnet** → one line and the way back: *"Let's write the guide first — say 'set up my lead magnet
  for agents' and it goes into your Week 3 Kit at the end of that sitting."* → `lm-navigator`.
- **A magnet but no page outline** (`Funnel doc: —`, no `opt-in-funnel-[slug]-*.txt` in `exports/`) → *"Your guide
  needs its page before it goes in the kit — let's write that first."* → `lm-funnel`, then back here.
- **Both present** → Step 1.

## Step 1 — Gather the parts (read, never rewrite)
Take each part from the first place it exists, in this order:
1. **The texts handed over in this session** (the navigator's run: the guide and the page just written).
2. **`~/attraction-brain/exports/`** — newest of each: `lead-magnet-[slug]-YYYY-MM-DD.txt`,
   `opt-in-funnel-[slug]-YYYY-MM-DD.txt`, `delivery-kit-[slug]-YYYY-MM-DD.txt`, `platform-profiles-YYYY-MM-DD.txt`
   (`[slug]` per output standard §2).
3. **The guide document read back through the storage connector** (`Lead Magnet — [Guide Name]` in the campaign
   folder) when its text is not in `exports/`; the page outline has no document of its own — its text lives in
   `exports/` only.

A part that exists nowhere is **skipped with one honest line inside Part B** (*"Bios: not written yet — say 'update
my attraction bios' and they join the kit."*) — never invented, never a bracket token. The guide and the page are
never skipped (Step 0).

From the Brain, read: `identity/offer.md` (`## The program` and the UVP one-liner — one line each, so Part B can
say what the guide leads to; the `Lead-magnet seed:` line; `Comment keyword:`; the header's `Join-gated package
allowed:`), `identity/compliance.md` (the first line `Status:` — `unset` means the public documents could not have
been written, so say so and stop at the way back — and the stamp), `identity/profile.md` (name, brokerage as
required, headshot location, handles), `brain.md` quick reference (the booking link), `memory/magnets.md` →
`## Current magnet` (keyword, funnel URL, download link) and the intake block's `Reach:`.

## Step 2 — Write Part B (structured text, output standard §4)
Copy is **verbatim** from the parts — nothing added, nothing cut, no "punching up", no title changed, page titles
exactly as the guide writes them (never re-cased). Strip each source document's own appendix (its `▸ NEXT …` and
`▸ COMPLIANCE` bands); the kit carries one appendix at its end. **Every heading is a sub-band `──── LIKE THIS ────`**
(the kit's PART B band is written by the kit builder); the guide's `── PAGE N - TITLE ──` lines stay as they are.
Never a line of copy in capitals; never a `[` bracket token; no skill ids anywhere.

```
──── YOUR GUIDE: THE OUTLINE ────
What it leads to: [the program's name and type · the UVP one-liner — one line]
Title: [the guide's title, exactly] · Promise: [the subtitle line]
Pages:
   •  Cover — [title] · [subtitle]
   •  Page 1 — [the opening title, exactly as written]: [one line on what it does]
   •  Page N — [title, exactly as written]: [one line]      (one per PAGE block, in order)
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
──── THE OPT-IN PAGE AND THE THANK-YOU PAGE: THE STRUCTURE ────
The page reads in this order; every opt-in button opens the one pop-up; submitting lands on the thank-you page.
   •  1 Hero · 2 The problem · 3 The product · 4 Who I am · 5 The journey · 6 The offer · 7 Why join me · 8 Proof · 9 The organization · 10 Book a call · 11 The opt-in
   •  The pop-up: first name · email · phone (optional) · the reassurance line · the button
   •  The thank-you page: the confirmation · the instant download button · the call, offered · where to find me · the footer
The copy follows, word for word, exactly as the sales funnel outline reads.
──── SECTION 1 — HERO ────
[verbatim]
... (every section band, THE OPT-IN POP-UP, THE THANK-YOU PAGE and FOOTER, verbatim, in order)
──── THE MESSAGING FOR THE GUIDE ────
Headline: [the hero headline] · Pre-headline: [ ] · Subhead: [ ]
Hook:
   •  [the cover's three lines]
Attraction line: [from the hero]
CTA button: "Get the Free Guide" · Keyword: GUIDE
The call: [the closing page's call to action — the booking link, or the Reach: answer (the email or the @handle) exactly as the guide carries it]
──── THE BIOS ────
[each platform's bio from the Platform Profiles pack, verbatim, one labelled block per platform — or the one honest line]
──── THE DMS AND THE DELIVERY EMAIL ────
[the Delivery Kit's comment reply, DM 1–3, the delivery email, the 3-frame story — verbatim — or the one honest line]
──── WORDS WE DON'T USE ────
   •  No compensation, splits, revenue share, stock or income figures anywhere public.
   •  No ranking, no stars, no "best", no other brokerage's name or logo.
   •  [the register line — at yes or unknown: "the program is what an agent receives when they partner with me" · at no: "every public line is what I teach, my story and how I mentor"]
   •  No invented urgency — the one honest why-now is the only one.
   •  The type of agent is a career stage, production level, model or mindset — never a protected characteristic.
──── DESIGN BRIEF — [GUIDE NAME] ────
What to build: a styled PDF of the guide — the cover, one interior page per "── PAGE N - TITLE ──" block, the closing page ("How [First name] helps next"), the back page, the compliance footer on every page · the opt-in page, section for section, every opt-in button opening the one pop-up · the thank-you page with the instant download button pointing at the finished PDF, the call offered, the footer · a cover image for the opt-in page, Reels and stories (the flat cover page exported from the PDF; a 3D mockup only if the tool exports pictures) · letter or A4, portrait, phone-readable at 100%.
Who reads it: [the type of agent, by stage, in one line] · on a phone, from a Reel or a bio link · tone: [the feel from the Design Package brief when it exists — else "calm and useful, never salesy"].
The brand: from your Design Package brief (do not improvise) — or, before the Week 3 brand chat, a clean neutral look: the member's headshot, one dark text colour, no accent unless the member names one, the brokerage logo only where compliance requires it. Brokerage mark: [where it must appear — from the compliance file]; the brokerage's own colours are not the palette.
The cover: Title: [exactly] · Subtitle: [exactly] · "By [Name], [Brokerage as required]" · "Last updated [Month YYYY]" when the guide carries that line. No ranking language, no stars, no "best", no other brokerage's name or logo anywhere.
The guide pages: copy verbatim — every word, including the notes in parentheses · one page per PAGE block, in order (a comparison-shaped guide's model pages in the same layout; a checklist page with real boxes; template rows as fill-in lines; a mini-course lesson page with its template in full) · the labelled lines become page elements and never print as labels (the pull quote set large, the callout a panel, the checklist real boxes, template rows fill-in lines, scripts message bubbles, the source a footnote, the image idea the page's visual, the next step the closing strip) · the page the reader will screenshot legible in one phone screenshot · the closing page carries the booking link as the ONE button, plus the social handles · the compliance footer on every page: [the stamp] · photos: the member's headshot on the closing page, real photos of the organization only if supplied — never stock people · body text 11pt or larger.
The opt-in page and the thank-you page: sections in the order above, copy verbatim, every section's own headline · the Hero's video embed, or the cut-out headshot where the Video line says to record · the Book-a-call area as the booking embed or a button to the link · every opt-in button opens the one pop-up (first name · email · phone optional), the button words exactly "Get the Free Guide" · the form must really send the name and email — test-submit once before any traffic · the thank-you page's download is an instant download of the finished PDF, never "check your inbox" · the compliance stamp is the footer of both pages.
The mockup: the flat cover as its own page in the PDF (export that page as the cover image) · if the tool exports pictures: a square crop for Instagram, a 9:16 crop for stories, a 3D booklet mockup with a soft shadow.
When it's done: save the PDF and any cover images into your Guides folder · share the PDF "anyone with the link" — that link is the thank-you page's download button · tell me "the PDF is done" · when the page is live, test-submit the form once and tell me "my funnel is live" with the link.
If a web person builds the page: a real form on the page itself — first name, email, phone (optional) — that sends the entry to the member before the thank-you shows, never a form drawn by a script after the page loads · a hidden "are you a robot" field, and a plain fallback (the member's email) if the send fails · test-submit once and confirm the entry arrived before any traffic.
```

Write the real values in — never a `[` bracket token. The `──── DESIGN BRIEF — [GUIDE NAME] ────` line is written
exactly, in capitals (the design skills key on it). The register line follows the offer's `Join-gated package
allowed:` value — at `no` nothing in Part B may read "join me and get X"; at `yes` and `unknown` the join register
reads consistently.

## Step 3 — Hand it to the kit, log, say one line
1. **Keep the text** at `~/attraction-brain/exports/kit-magnet-[slug]-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`;
   the kit builder reads the newest).
2. **Run the Brain's `attraction-week3-kit`** (silent — its Step 3): it assembles the one kit (Part A the offer, Part
   B this text), saves `Week 3 Kit — [First Last] — YYYY-MM-DD` to the home base folder beside the Brain Book,
   trashes the superseded copy, and hands back the link. If the Brain plugin predates the kit builder, say so in one
   line (*"update your Brain plugin — Check for updates — and say 'rebuild my kit'"*); never render a kit here.
3. **Log it (silently):** in `memory/magnets.md` the row's intake block gets `Kit doc: YYYY-MM-DD` (replace an older
   stamp). **attraction-brain-sync PUSH** (write → push → verify). Never narrate this or name the file.
4. **Say one line** (the navigator's finish line carries it when it called you): *"Your guide and your page are in
   your Week 3 Kit — the one file for Claude Design, in your home base folder beside your Brain Book."* Never the
   full text in chat.

## Step 4 — "the PDF is done" / "my guide is designed" (record only)
In `memory/magnets.md`, move the row's Status to `designed` (never backwards) and set `## Current magnet` →
download link when the member gives it. **attraction-brain-sync PUSH.** One line back: *"Recorded — your guide is
designed. When the page is live, say 'my funnel is live' with the link and every system points at it."*

## Never
- Save a "Lead Magnet Package", a page document or any document of its own — the guide is the member's document;
  the kit is the Brain's. Rewrite, shorten or re-title any copy while assembling. Render anything. Invent a colour,
  a font, a logo or a hex code. Put another brokerage's name or mark anywhere; rank anything; print a bracket token;
  name a skill id in front of the member; build Part B without the page outline.

## Quality checklist
- [ ] The guide and the page outline present; compliance `set` or `confirmed`; the register read
- [ ] Part B complete; a missing optional part carries its one honest line and the phrase that writes it; copy verbatim; page titles as written; every heading a sub-band; the `DESIGN BRIEF —` line literal
- [ ] Text kept in exports/; the kit builder run; `Kit doc:` stamped; pushed; one line in chat
