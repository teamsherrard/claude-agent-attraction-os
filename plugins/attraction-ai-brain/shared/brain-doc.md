# The AI Brain file — one document, everywhere

Every member gets **ONE master document**: the **📕 [Name]'s Agent Attraction Brain Book**, a short, structured
render of their Brain (nine sections, at most fifteen pages) saved to their workspace (`01 · AI Brain`). **It is
"the AI Brain file"** — the one file every Agent Attraction Design Studio skill (`aa-*-design`, in Claude Design)
and the Lead Magnet skills ask the member to upload, because those tools cannot read `~/attraction-brain/`. One
doc, everywhere. It tells those tools WHO the member is; the member's offer, brand, operations and compliance
live in their own places (below).

The full contract — the nine sections, the pipeline, the grounding laws, demo mode, the verification gate, the
regeneration rules — is **`shared/brain-book-spec.md`**. This file holds only the rules every skill needs when
it *points at* the Book.

## The rules
- **It is a render, never a source.** The markdown files in `identity/` and `memory/` stay the truth. The Book is
  always rebuildable and never holds a fact the Brain doesn't. Nothing is ever edited in the Book and not in the Brain.
- **Name:** `📕 [Name]'s Agent Attraction Brain Book — YYYY-MM-DD` (`.docx`, via `shared/render_doc.py`,
  `--eyebrow "Agent Attraction Brain"`). Dated; **newest = current**; never a second differently-named master doc.
- **Where:** the workspace's `01 · AI Brain` (per `shared/drive-map.md`), then push via `attraction-brain-sync`.
- **What it holds (the nine sections, in order):** Who you are · Your story · Your brokerage story · Your unique
  approach · Your proof · Who your story speaks to · Your numbers · Your voice · What's next. **What it never
  holds:** money math, compliance, operations, a scorecard, an open-items list, content pillars, landscape
  research, the brand kit, the Design Package brief, the program itself.
- **Where the rest lives — the reading map for any tool that used to read a longer Book:** the brand → the
  Design Package brief (`02 · Brand`, saved by `attraction-brand-direction`) and the Design System; the offer →
  the Partner Offer document (`05 · Offer`, written by `attraction-offer` in Week 2 — its At a glance page first);
  the day-to-day (the weekly call, the first 30 days) → the same Partner Offer document; compliance → the brief's
  compliance line, or `identity/compliance.md` through a Brain skill ("paste my compliance link"); operations →
  `identity/operations.md` (Week 2). A tool that needs any of those asks for that document, never for a longer Book.
- **When it regenerates:** the end of Setup · after the Partner Offer is built in Week 2 · after a material change
  to the member's story, approach, proof or voice · "show me my Brain" / "regenerate my Brain Book". The brand
  chat does not regenerate it (the Book carries no brand). A build's own write-backs never trigger another build.
- **Which file to take to Claude Design:** this one. Download it from the workspace (or let Claude Design read it
  through the storage connector). When a member asks "which file do I upload?", the answer is the newest-dated
  Brain Book in `01 · AI Brain` — **never a DEMO-watermarked one**, never the raw `_engine` files.
- **An older Book** (eighteen chapters, rendered before 2026-11-02) still reads as a Brain Book; a tool that finds
  the old chapter names may use them, and says "show me my Brain" refreshes it to the short shape.
- **Never narrate a failed render.** The member only ever sees the finished Book and its direct link.
