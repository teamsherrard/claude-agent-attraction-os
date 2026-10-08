---
name: sales-booking-page
description: >
  Sales OPS: the Partner Call booking page, written. The event name, the description in the member's
  positioning, the five qualifying questions from Mike's booking flow with the member's brokerage named,
  the confirmation-page copy, where the link lives (bio, video descriptions, signature), and a
  paste-ready design brief for the Design Studio's ds-funnel booking shape. Public copy, so the
  compliance gate runs first; no superlatives without a dated proof line; no compensation anywhere.
  The member pastes it into Calendly or GoHighLevel; nothing is published for them. Trigger on: "write
  my booking page", "partner call booking page", "booking page copy for agents", "qualifying questions
  for my calendar", "book-a-call page for agents", "my calendar description", "design brief for my
  booking page", "application page copy".
---

# Booking Page — the page an agent reads before they give you thirty minutes

The booking page is the filter and the first impression. Mike's own: a one-on-one Zoom call, a line on
what the group does for agents, and five required questions that hand him "all the ammunition" before the
call starts (`10-presentation-delivery/42`; bonus: Calendly). This skill writes every word of the
member's version and the brief the Design Studio turns into the page.

**Write-and-prepare.** Copy and a brief; the member pastes into their tool or hands the brief to Claude
Design (`ds-funnel`, booking shape). Nothing is published from here.

## Step 0 — How we speak
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md` and `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`.
Zero to one question; "just make it" is the expected input.

## Step 1 — Load the Brain (never ask what it knows)
`~/attraction-brain/brain.md`, then `identity/sales-system.md` (the event, length, the form as set — if
absent, run with Mike's five questions and say `sales-system-setup` locks them), `identity/positioning.md`
and `identity/offer.md` (the one line and the three things they provide), `identity/avatars.md` (who the
page speaks to), `identity/proof.md` (the only source of any claim), `identity/profile.md` (name, brokerage,
market), `identity/brand-visual.md` (for the brief), `identity/voice.md`, `identity/compliance.md`.
Missing locally → `attraction-brain-sync`. A tool error is never "no Brain".

## Compliance gate — before a word is written (this page is public)
`identity/compliance.md` **unset** → stop: *"Before I write anything an agent will read, I need your
compliance basics — three minutes: say 'set up my compliance'."* **set** → apply every rule; remind once to
confirm. **confirmed** → apply. Applied rules: brokerage name exactly as it must appear, license display
where required, no compensation or income language, no superlative ("record-breaking", "#1",
"fastest-growing") without a dated source in `proof.md`, the recruiting-scope line if the member attracts
across states or provinces, nothing negative about anyone.

## The copy (all of it, paste-ready, in the member's voice)
1. **Event name** — *"[Organization] Partner Call — [30] min"* (from `sales-system.md`).
2. **The description (2–4 lines)** — Mike's shape: who it is with ("a one-on-one Zoom call with me, [Name]"),
   what they will see ("how we help [type of agent] [the outcome in `positioning.md`]"), the energy ("I'm
   excited to meet you") — "communicate with energy; don't be a bland dud." One proof line from `proof.md`
   if a dated one exists; otherwise none.
3. **The five questions** — exactly as locked in `sales-system.md` (or Mike's five with the brokerage
   named), each marked required, the type and length of each field noted for the tool.
4. **Confirmation-page copy (3 lines)** — "You're booked. Watch for the confirmation with your Zoom link —
   and if you can, reply with the one thing you most want to get out of our call." Plus the pre-call
   video promise if `sales-show-up` has set one.
5. **Where the link lives** — Instagram bio (with the link-in-bio label), every YouTube description's CTA
   line (the YouTube system's wording), the email signature block in `operations.md`, the lead magnet's
   thank-you step (the Lead Magnet plugin, Week 6), the weekly model call invite.
6. **The "who this is for / not for" block (optional, recommended)** — three lines each, from
   `avatars.md`: for the agent types the member serves; not for agents already at the brokerage or already
   sponsored (the question-1 filter, said kindly).

## The design brief for `ds-funnel` (booking shape) — paste-ready, one block
*"Build the Partner Call booking page (booking shape) for [Name] · [Organization] · [Brokerage as it must
appear]. Brand: [from brand-visual.md — colours, type, the logo file in 02 · Brand]. Headline: [the one
line]. Subhead: [the outcome for the agent type]. Proof strip: [up to three dated lines from proof.md, or
'none — omit the strip']. Embedded calendar: [Calendly / GHL link]. Form questions below the embed: [the
five]. FAQ (three): what we'll cover · who this is for · who it isn't for. Footer: [brokerage name, license
display line, the compliance disclaimer if required]. No compensation, no income language, no superlatives
beyond the proof strip. Mobile first."*
The member uploads their Brain Book to Claude Design with it; the brief is the whole hand-off.

## Save and confirm
Render the copy per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` via
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/booking-page.txt "Booking Page Copy — [Name] — [YYYY-MM-DD].docx" --title "Partner Call Booking Page" --subtitle "[Name] · [Organization]"`
(read back, no `<w:` markup; `RENDERER-UNAVAILABLE` → install nothing, upload the `.md`), upload to the
workspace's `05 · Offer` folder, push nothing else (this skill writes no Brain file — the page settings
already live in `sales-system.md`; the live URL goes in the `## Conversion & Sales` block's `Booking page`
key when `sales-system-setup` runs). Confirm with the link and: *"Paste the description and questions into
[tool]; hand the brief to Claude Design for the page. Your turn."*

## Demo mode
Fictional member, "(illustrative — demo)" on any figure, DEMO in the filename.

## Quality bar
The delete test on every line; the any-agent test (a description that fits any leader at any brokerage is
rewritten with the member's positioning); no placeholder brackets; every claim traceable to `proof.md`;
the five questions intact; the energy is theirs, not a template's.
