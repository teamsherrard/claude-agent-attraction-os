# Copy Formulas — part of the aa-funnel-design skill

Read while placing the copy. On every shape the copy arrives LOCKED from the system that wrote it (the
Lead Magnet system's funnel doc, the Sales system's booking copy, the Events system's registration
copy) — these formulas are the FALLBACK for the rare page with no doc, and the discipline you hold the
layout to. Never offer "2–3 headline options" when a doc exists.

## THE CANONICAL PHRASES (never invent a variant, never ask the member to pick one)

- Opt-in: the button is **"Get the Free Guide"** — the one phrase the member's whole system uses (the
  page, the bio, the videos, the ManyChat keyword).
- Partner Call booking: **"Book a call with me"** — the Book's primary CTA, verbatim.
- Workshop registration: **"Save my seat"** (or the Events doc's phrase, verbatim).
- The thank-you's download button names the ACTUAL guide: *"Download the Honest Brokerage Comparison
  Guide"* — never a generic "your guide".
- The call, offered on the opt-in thank-you (the doc's line, in this register): *"Want to talk through
  where you're at? Book a call — no pitch, I'll just answer your questions. If not, that's okay."*

## HEADLINE SHAPES (fallback only — localize the MEANING, never translate word for word)

- **Opt-in (the comparison guide — the locked first campaign):** the magnet's promise, outcome-led, for
  this type of agent. *"The Honest Brokerage Comparison Guide."* · subhead: *"How cloud, franchise,
  flat-fee, and independent models actually work — the trade-offs of each (including mine), the
  questions to ask any sponsor, and nothing you can't check. Written by a working agent and leader, not a
  recruiting department."*
- **Opt-in (a later campaign):** *"Switch brokerages once — the checklist that makes it the last time."*
  · *"Your first 90 days at any brokerage, mapped week by week."*
- **Partner Call booking:** the one line said out loud (*"I help agents in years 2–5 build a pipeline
  that doesn't need a lead bill"*) · subhead: who it's for by stage + what the call is and isn't (*"30
  minutes, about your business, no pitch"*).
- **Workshop registration:** the outcome as the title (*"Build a 90-day plan you'll actually run — a
  free live workshop for agents in years 1–5"*) · subhead: date · time · format · "free".

## COPY DISCIPLINE — TIGHT, OUTCOME-LED, SKIMMABLE

Headlines ~6–10 words; subheads one or two short lines; benefits as short parallel bullets, not
paragraphs; button text 2–4 action words. The member's real proof only, dated; cut filler and clichés;
fifth-grade reading level. **Specifics are the proof:** a real routine, a real agent helped (consented),
a real number with its date — where there is none, be specific with facts, names of things, and steps;
never estimate a figure. Vague reads as recruiting; specific reads as a leader.

## THE FORM (every shape)

- Fields: **First name · Email · Phone** — three, nothing else; never "brokerage", never "production"
  (the booking shape adds the five qualifying questions ONLY where the Sales doc places them — in the
  calendar tool or on the application variant; the registration shape adds the Events doc's one sorting
  question, "Which best describes you?", and the one-thing question when the doc carries it — never more
  than five fields).
- **The honest contact line under Phone**, from the doc: *"I'll text or call once to make sure you got
  it — no drip, no pressure."* Never collect a phone silently.
- **Reassurance by the button**, from the doc: *"Free. Instant. Private — nobody's contacted on your
  behalf. Unsubscribe anytime."*
- A trust cue beside the form (a lock icon, "100% free") — never a rating the member doesn't have.

## THE MINI-FAQ (opt-in — three one-liners, in the opt-in section, the doc's words)

*"Is this a recruiting pitch?"* → No — it's the guide, and it's fair to every model, including mine.
*"Will anyone know I downloaded this?"* → No — the list is private, nobody's contacted on your behalf.
*"I'm not planning to move — is this for me?"* → Then it's the thing to read before you ever decide.
Three compact Q→A rows (question bold, answer one line), never a separate FAQ section.

## THE BOOKING PAGE'S THREE FAQs (the Sales doc's)

What we'll cover · who this is for · who it isn't for (agents already at the brokerage or already
sponsored — the question-1 filter, said kindly). Three rows, one line each.

## FUNNEL-KILLERS FOR AN AGENT AUDIENCE (the page fails if any survive)

- **A vague headline** ("Welcome" / "Join a winning team") instead of the magnet's promise or the one line.
- **A pitch for the brokerage.** The brokerage is one generic line — *"and everything [Brokerage]
  provides — I walk you through that on a call"* — never a features section, never its logo as a hero.
- **Compensation anywhere.** No split, cap, tier, stock, rev share, income, or "earn" — the single
  fastest way to turn a leader's page into a recruiter's.
- **A named former brokerage, or any brokerage's weakness.** "A franchise", "an independent"; trade-offs
  only on the member's own model.
- **Invented proof** — a count, a quote, a photo of people who aren't the member's.
- **The recruiter register** — "opportunity", "join my team", "let's talk about [brokerage]",
  "stop scrolling".
- **A "book a call" button on the opt-in page itself** — the call lives on the thank-you page.
- **Fake urgency** — countdowns, "only 2 spots" with no real limit; a workshop's real date and real seat
  count are the only urgency allowed.
- **Too many fields; more than one offer; a full site menu; a dead thank-you; a great desktop page with
  a broken mobile one; "check your inbox".**
- **A protected characteristic** in who-it's-for copy — stage, production, model, and mindset only.

## THE GOHIGHLEVEL-READY BLOCKS (the `page-copy.md` shape)

```
PAGE COPY — [Shape] — [Guide / Partner Call / Workshop name]
[Name] · [Brokerage as required] · [Date]   ·   Use these blocks in the page's order.

── TOP BAR ──
Logo: [file] · nothing else clickable

── HERO ──
Eyebrow: …   Headline: …   Subhead: …   CTA button: "…"   Hero visual: [guide-mockup.png / the cut-out]
Trust strip: [the dated proof line — or "none"] · [brokerage line as required]

── SECTION 2 — … ──   (one block per section, in the doc's order, copy verbatim)

── THE POP-UP ──
Headline: …   Fields: First name · Email · Phone   Contact line: …   Reassurance: …   Submit: "…"

── THE THANK-YOU ──
Headline: …   Download button: "Download the [Guide Name]" → assets/guide.pdf   (or: the confirmation lines)
The call, offered: …  [booking link]   Where to find me: …

── FOOTER ──
Name · logo · contact in full · handles · the compliance stamp verbatim

── BRAND VALUES ──
Fonts: [heading] / [body] · Colours: [#hex role · #hex role · #hex role] · Button: [accent #hex]

── HOSTING NOTES ──
On GoHighLevel the page's own form replaces the Netlify form; attach the PDF to the thank-you step
(instant download — never "check your inbox"); paste the compliance stamp in the footer.
```
