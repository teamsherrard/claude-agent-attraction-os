# Design Craft — part of the ds-funnel skill

Read IN FULL before designing any page. The specs are the ones proven in the sister suite's funnel
skill; the audience is an agent tapping in from a Reel, a bio link, or a video description — on a phone,
sceptical, and tired of sponsors.

## BUILD IT LIKE AN EXPERT (specific specs, not vibes)

- **Grid & width.** Centre all content in a max-width column (~1140–1200px desktop) with equal side
  gutters; a 12-column grid; everything aligned to it. Colour bands run full-bleed; their inner content
  stays in the column. Nothing floats off-grid or drifts to one side.
- **Type scale (a real hierarchy).** Hero H1 huge and tight — ~64–80px desktop / ~36–44px mobile,
  line-height ~1.05, heavy, with ONE word in the accent (the Design System's `type.heading`). Section H2
  ~36–44px. Body ~17–18px at line-height ~1.6. A small **eyebrow label** above each headline (~13px,
  uppercase, letter-spaced, in the accent — "02 · THE GUIDE"). Max two brand fonts; contrast with weight
  and size, not extra fonts.
- **Spacing & rhythm (8-pt system).** ~100–140px vertical padding per section on desktop (~56–72px
  mobile), consistent gaps, a steady rhythm down the page. Whitespace reads premium; cramped or random
  spacing is the #1 amateur tell.
- **Section rhythm — alternate, don't repeat.** Adjacent sections carry different grounds (the Design
  System's light tint → paper → the dark anchor or the brand colour → the tint) so each reads as its own
  beat; two-column blocks alternate image-left / image-right. Every section gets an eyebrow + a clear
  headline.
- **Colour discipline (60/30/10).** ~60% the light ground, ~30% the brand colour and tints, ~10% the
  accent — reserved for the CTAs, the eyebrows, and key highlights so the buttons truly pop. Text is
  high-contrast (ink on light, paper on dark) — never grey-on-grey.
- **Components, consistent everywhere.** One radius scale from the Design System (cards and inputs ~16px
  or the brand's radius, buttons the brand's pill or 8px), one soft shadow for elevated cards and forms,
  1px hairline dividers, inputs with visible labels and comfortable height (~52px). Buttons get bold
  labels and a trailing arrow. The same components on the page, the pop-up, and the thank-you state.
- **Imagery treatment.** Consistent rounded corners + a subtle shadow on photos; a scrim behind any text
  over an image; never stretch, squish, or distort. The mockup gets a soft realistic shadow and sits large
  and balanced in the hero.
- **Polish that signals "designed":** the eyebrows, section numbers (01 / 02 / 03), a short accent rule
  under headlines, one simple icon style, a slim trust strip under the hero (the dated proof line + the
  brokerage chip where required — or just the brokerage line when no proof exists; never an invented
  rating).
- **Reference calibre:** the restraint and polish of a top studio landing page — confident, spacious,
  premium. Never a copy of a specific site.

**Amateur tells to eliminate:** flat default type with no scale · grey-on-grey text · everything
centre-aligned · cramped or uneven spacing · off-grid floating elements · inconsistent radii · clip-art
icons · too many colours · heavy drop-shadows · tiny body text · big empty dead zones · a stock
"happy agents" photo.

## ART DIRECTION — PREMIUM, ON-BRAND, CONVERSION-CLEAN

Pull the member's logo, colours, fonts, and toolkit devices through the whole page so it matches the
banners, posts, and guide they already have. Execute the page in the brand's direction (calm-premium,
bold-modern, editorial…) — backgrounds, accents, type, and finish consistent with it. The leader palette,
visibly distinct from the brokerage's own; the brokerage's mark only where the compliance stamp puts it.

- **One cohesive system** — one accent, one button style, one type hierarchy, one section spacing,
  buttons identical everywhere.
- **Strong hierarchy, generous whitespace** — one dominant headline per section, calm spacing, never a
  wall of text.
- **Real, legible imagery** — the member's cut-out (from the kit), the guide's canonical mockup, the
  offer stack object, the member's real photos (the weekly call, events, agents' wins — with their
  permission), the toolkit's devices, simple icons. Never repeat one photo to fill space.
- **Use ONLY the member's uploaded photos for realistic imagery — never fabricate it.** This tool can't
  fetch stock or render believable photos; with none, design with brand fields, gradients, the pattern,
  the logo, and the headshot cut-out. A clean brand-colour layout always beats a fake-looking crowd.
- **RESERVE ZONES — nothing overlaps.** Headline, subhead, form, button, photo, mockup, and footer each
  get clear space with real gaps; text never runs under a photo or a button. The #1 cause of a messy page.
- **Buttons look clickable** — solid high-contrast fill, generous padding, a clear label, consistent
  everywhere; the primary CTA the most prominent element on each screen, in the brand's brightest accent
  even if that is the one place it appears. A button that blends into its section kills conversion.
- **Balance every section — no awkward dead space.** In the hero, the headline + CTA on one side and the
  visual on the other, both filling their side and vertically centred; the mockup or cut-out sized to
  anchor its half. A section that looks empty gets its content enlarged or its layout tightened.
- **Premium, not template-y** — polished, restrained, the kind of page that says "this person has a
  standard".

## THE HERO PER SHAPE (80% of the result)

- **Opt-in:** the magnet's promise as the headline (the doc's, verbatim), the subhead, the button
  **"Get the Free Guide"**, and the **guide's canonical 3D mockup** as the hero visual — large, premium,
  the first thing the eye hits beside the headline; optionally the member's cut-out beside it. The
  mockup comes from `ds-lead-magnet` (`guide-mockup.png`) — reproduce that cover faithfully; design a
  cover yourself only when none exists yet, and say it becomes the guide's cover. On mobile the mockup
  stays prominent but the headline + CTA lead. A light directional cue (the member's gaze, an arrow)
  points at the button.
- **Partner Call booking:** the one line as the headline (the Sales system's), the outcome for the
  type of agent as the subhead, the member's cut-out large (this page is about a person), the button
  **"Book a call with me"** that scrolls to the calendar, the dated proof strip under it or nothing.
- **Workshop registration:** the workshop's promise as the headline, the date · time · format line as
  a designed strip, the member's cut-out (and the co-host's when there is one), the button
  **"Save my seat"**, a quiet "free · live on Zoom / at [venue]" line. Honest urgency only — a real
  date, a real seat count the member stated.

## THE PROOF PHOTO STRIP (the moving part of the opt-in page)

Under the proof block: one horizontal row of the member's real photos (the doc's list, 8–12, consistent
height ~200–240px desktop / ~140px mobile, rounded, even gaps) that glides slowly and continuously left
— CSS-only: the track duplicated once for a seamless loop, `@keyframes` translateX from 0 to −50%,
~40–60s per loop, pauses on hover, a static row under `prefers-reduced-motion`. No JS carousel
libraries. Fewer than ~6 photos → no strip, say so once. Agents' faces need the agent's OK (the doc
says so).

## THE WELCOME-VIDEO SLOT (opt-in About section — only when the doc kept the line)

Beside the About copy on the side the doc names: a 16:9 embed frame with a poster (the member's frame,
an on-brand play button), **never autoplay with sound**, never a rival CTA. Ship it as an embed
placeholder the member fills with their YouTube link; if the doc dropped the line, there is NO slot —
never an empty frame.

## THE STICKY MOBILE CTA

A persistent bottom bar on phones carrying the one CTA (full-width, ~48px tall, the accent), in the
easy thumb zone — never covering the form's submit button or the thank-you's download button.
