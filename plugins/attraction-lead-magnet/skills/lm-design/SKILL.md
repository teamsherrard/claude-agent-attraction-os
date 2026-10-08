---
name: lm-design
description: >
  Writes the paste-ready design brief that turns the member's written agent-attraction lead magnet
  into a styled PDF with a cover and a 3D mockup — for the Design Studio's ds-lead-magnet skill in
  Claude Design (ds-product-mockup for the mockup alone). Reads the finished magnet doc and the
  brand from identity/brand-visual.md (logo, colors, fonts, headshot; the leader brand distinct
  from the brokerage's colors; the brokerage logo where compliance requires it), names the files
  to upload (the magnet doc + the newest Brain Book), and states what the designer must not change
  (copy verbatim, one page per PAGE block, the compliance stamp, the dated line). Saves the brief
  in the campaign folder; marks the magnet "designed" once the member confirms the PDF. Brief only
  — never renders anything.
  Trigger on: "design brief for my guide", "make my comparison guide a PDF", "mockup for my agent
  lead magnet", "cover for my guide", "hand my guide to design", "3D mockup of my guide".
---

# Design Brief — the hand-off to the Design Studio

The magnet is written; now it needs to look like something an agent wants to open. **This skill writes the
brief, nothing else** — the Design Studio's **`ds-lead-magnet`** (cover + interior + 3D mockup) and
**`ds-product-mockup`** (the mockup alone) do the designing, inside the member's Claude Design workspace.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #3 (this is the ONE skill in the
plugin that writes design direction, because the brief IS the deliverable), #10. The three laws:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Step 0 — Find the magnet (silent)
Pull the Brain (house rule 2). Read `memory/magnets.md` → the row the member means (the newest `written`, or
the one they named) and open its `Lead Magnet — [Guide Name]` doc in the campaign folder (output standard
§1). **No written magnet** → one line and the way back: *"Let's write the guide first — say 'set up my lead
magnet for agents' and the brief comes right after."* → `lm-navigator`. Never brief a guide that doesn't exist.

## Step 1 — Read the brand (lazy)
- `identity/brand-visual.md` → **Final kit** (logo file in `02 · Brand`, colors with roles, fonts, headshot),
  **Direction** (feel in 2–3 words, references, tagline), **Brokerage brand constraints** (what must appear,
  where, how big — and the brokerage's own colors, which ours stay distinct from). If the Final kit is empty
  (the Design Package hasn't run), say so in one line — *"Your brand kit isn't built yet — the Design Package
  is Week 1's design session; I'll write the brief from your direction and the designer can run the kit
  first."* — and brief from Direction. Never invent a hex code.
- `identity/compliance.md` → the stamp (brokerage name, license display, disclaimer verbatim) and the logo
  rule. The gate already passed when the magnet was written; re-check `Status` isn't `unset` — a design can't
  ship a guide that can't.
- `identity/profile.md` → name, brokerage as required, headshot location.
- `brain.md` quick-ref → the newest Brain Book's name (the designer reads it for the voice and the brand).

## Step 2 — Write the brief (paste-ready, one block)
In chat, as one block the member copies into Claude Design, **and** rendered to the campaign folder as
`Design Brief — [Guide Name]` (output standard §4). Sections, in this order:

```
DESIGN BRIEF — [GUIDE NAME]
[Name] · [Brokerage] · [Date]
Paste this into your Claude Design workspace with the ds-lead-magnet skill loaded. Upload: Lead Magnet — [Guide Name].docx and 📕 [Name]'s Agent Attraction Brain Book — [newest date].docx.

────────────────────────────────────────────
WHAT TO BUILD
•  A styled PDF of the guide: cover + one interior page per "── PAGE N - TITLE ──" block + the closing page ("How [First name] helps next") + the compliance footer.
•  A 3D mockup of the finished guide (cover art, slight angle, transparent background) for the opt-in page, Reels, and stories — plus a flat cover image.
•  Format: letter / A4 per Locale, portrait; phone-readable at 100%.

────────────────────────────────────────────
WHO READS IT
[the type of agent, by stage, in one line] · they open it on a phone, from a Reel or a bio link · tone: [feel from brand-visual.md — e.g. calm-premium, not salesy].

────────────────────────────────────────────
THE BRAND (from the kit — do not improvise)
Logo: 02 · Brand/[file] · Colors: [#hex role · #hex role · #hex role] · Fonts: [Heading] / [Body] · Headshot: 02 · Brand/[file]
Brokerage mark: [where it must appear and relative size — from compliance.md] · the brokerage's colors ([#hex]) are NOT the palette; ours stay distinct.
Tagline (if any): "[ ]"

────────────────────────────────────────────
COVER
Title: [the guide's title, exactly] · Subtitle: [the promise line, exactly] · "By [Name], [Brokerage as required]" · "Last updated [Month YYYY]" (keep it — the guide is dated on purpose).
No ranking language, no stars, no "best," no other brokerage's name or logo anywhere.

────────────────────────────────────────────
INTERIOR RULES (the designer must not change these)
•  Copy VERBATIM from the doc — every word, including the source notes in parentheses and the "verify current" line on page 1. Nothing added, nothing cut, no "punching up."
•  One page per PAGE block, in order; the four model pages in the SAME layout (same length, same blocks) — a longer or bolder page for the member's own model reads as a pitch.
•  The questions page (page 7) designed as a checklist the reader can screenshot.
•  The closing page carries the booking link as a button and the social handles; nothing else gets a button.
•  The compliance footer on every page: [the stamp, verbatim from compliance.md].
•  Photos: the member's headshot on the closing page; real photos of the organization only if supplied — never stock people, never another brokerage's event.
•  Accessibility: body text ≥ 11pt, contrast that passes on a phone.

────────────────────────────────────────────
THE MOCKUP
3D book/booklet mockup of the cover, slight angle, soft shadow, transparent background (PNG) · a square crop for Instagram · a 9:16 crop for stories (the Short-Form plugin uses these) · the flat cover as a separate PNG.

────────────────────────────────────────────
WHEN IT'S DONE
Save the PDF, the mockup PNGs, and the flat cover into 03 · Content/Guides/[campaign folder]/ · upload the PDF somewhere linkable (the thank-you page's download button points at it) · then tell me "the PDF is done" so I can mark it and the funnel can go live.

════════════════════════════════════════════
▸ COMPLIANCE
[the stamp — set or confirmed only; never a bracket token]
```

Write the real values in — never a `[` bracket token in the brief the member copies. Where the kit is empty,
write the Direction values and say "from your brand direction — the kit will replace these."

## Step 3 — Deliver, save, mark
1. Deliver the brief in chat as one copyable block, then: *"Paste that into Claude Design with the Lead
   Magnet Designer skill loaded, upload the two files it names, and it'll build the PDF and the mockup. When
   it's done, say 'the PDF is done' and I'll mark it so your page can go live."*
2. Save `Design Brief — [Guide Name]` into the campaign folder (output standard §6; fallback applies).
3. **When the member confirms the PDF exists:** in `memory/magnets.md`, move the row's Status to `designed`
   (never backwards) and set `## Current magnet` → download link if they give it. **attraction-brain-sync
   PUSH** (write → push → verify). Silent — never name the file.

## Never
- Render anything yourself (a page, a PDF, an image, a mockup) — the brief is the deliverable.
- Change the guide's words to "fit the design." The doc is the truth; the design serves it.
- Invent a color, a font, or a logo. Empty kit → Direction values, labeled.
- Put another brokerage's name or mark on the cover or anywhere; rank anything; add stars or "best."
