# The AI Brain file — one document, everywhere

Every member gets **ONE master document**: the **📕 [Name]'s Agent Attraction Brain Book**, a premium render of
their whole Brain saved to their workspace (`01 · AI Brain`). **It is "the AI Brain file"** — the one file every
Agent Attraction Design Studio skill (`ds-*`, in Claude Design) and the Lead Magnet skills ask the member to
upload, because those tools cannot read `~/attraction-brain/`. One doc, everywhere.

The full contract — chapters, pipeline, grounding laws, demo mode, verification gate, regeneration rules — is
**`shared/brain-book-spec.md`**. This file holds only the rules every skill needs when it *points at* the Book.

## The rules
- **It is a render, never a source.** The markdown files in `identity/` and `memory/` stay the truth. The Book is
  always rebuildable and never holds a fact the Brain doesn't. Nothing is ever edited in the Book and not in the Brain.
- **Name:** `📕 [Name]'s Agent Attraction Brain Book — YYYY-MM-DD` (`.docx`, via `shared/render_doc.py`,
  `--eyebrow "Agent Attraction Brain"`). Dated; **newest = current**; never a second differently-named master doc.
- **Where:** the workspace's `01 · AI Brain` (per `shared/drive-map.md`), then push via `attraction-brain-sync`.
- **When it regenerates:** end of Setup (Phase 8) · after the Partner Offer is built in Week 2 · after the brand kit
  lands in `02 · Brand` · after a Prospect Radar run · whenever the Brain materially changes · "show me my Brain" /
  "regenerate my Brain Book". A build's own write-backs never trigger another build.
- **Which file to take to Claude Design:** this one. Download it from the workspace (or let Claude Design read it
  through the storage connector). When a member asks "which file do I upload?", the answer is the newest-dated
  Brain Book in `01 · AI Brain` — **never a DEMO-watermarked one**, never the raw `_engine` files.
- **The Design Studio also reads** `brand-visual.md`, `offer.md`, `positioning.md`, `avatars.md`, `proof.md` through
  the Book's chapters; keep those chapters full, never summarized (the spec's invariant).
- **Open items are a page, not a gap.** Everything unfilled (a Week 2 offer, an unset compliance field, no brand kit
  yet) renders on the Book's "Your open items" page with the week or the phrase that fills it — so nothing on the
  page reads as something the member failed to do.
- **Never narrate a failed render.** The member only ever sees the finished Book and its direct link.
