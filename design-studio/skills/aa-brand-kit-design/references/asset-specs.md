# Asset Specs — part of the aa-brand-kit-design skill

Read in full before building any piece.

## RENDER EVERY PIECE AT ITS TRUE SIZE

Build each piece as its OWN frame at the exact pixel dimensions below, clearly labelled with the
platform + size, grouped by platform, so the member can export each one ready to post. Respect every
safe area. Only build the platforms the member selected.

**The size contract:** each frame's canvas is EXACTLY the stated pixels — never letterboxed, padded,
or "close" — and type is sized for the piece's real display size. A wrong-sized frame is a failed
piece no matter how pretty it is.

**Build in priority order** (so an interrupted run still leaves a usable core): 1) profile pictures,
2) banners, 3) the three post templates, 4) stories, 5) highlight covers, 6) the Join My Team cover,
7) bonus pieces (signature, end screen, backgrounds), 8) the organization family (below). Establish
ONE master look on the YouTube banner and the win post, then reuse it across the set — the organization
family inherits it exactly. Never more than ~6 full-size frames per render.

**Every piece is ONE inline `<svg data-file="…">`** at its exact size (see the export-page reference)
from its first render, with no background rect on transparent pieces (the profile pictures, posts,
banners, covers, and backgrounds are opaque by design — their ground IS the artwork; only the logo
files are transparent).

### Profile pictures (square, circle-safe — up to 3 options)
The platform crops these to a circle: keep the face or mark centred inside a safe circle with margin.
Give up to **3 options** — the headshot on the brand's dark ground, the headshot on the light tint,
and the mark on a brand field — each ONE square that also reads well circle-cropped. 1080×1080
(`profile-1.png`, `profile-2.png`, `profile-3.png`); YouTube's copy at 800×800 (`profile-youtube.png`).
Recognizable at 40px: one bold element, never a composition.

### Banners — the positioning statement
The #1 failure is a small cluster of content marooned in empty dark space with copy missing. Fix it
two ways: include EVERY element on the checklist, and size things BIG so the layout fills the space.

**Every banner MUST carry ALL of these — the five profile answers, placed:**
1. The member's **logo** (a corner) — or the organization's version where the Design System says.
2. The member's **name, LARGE** — the dominant element. *(who you are)*
3. The **role line** under the name ("Team leader · The Lakeline Collective", "Mentor to new agents",
   what they are known for). *(who you are)*
4. The **who-you-help row** — the types of agent in plain words with chevron bullets ("New agents ·
   Agents paying for leads · Top producers"). *(who you help)*
5. The **positioning line** — one sentence: who you help + what you help them do, in their voice
   ("I help agents in years 2–5 build a pipeline that doesn't need a lead bill"). *(what you help them do)*
6. The **proof chip** — ONE real credential, number, or agent result from the Book's Proof chapter, as
   a quiet pill. **None in the Book = no chip.** Never invented, never "#1" without a dated source.
   *(why listen)*
7. The **CTA button** — "Book a call with me" (the Book's primary CTA, verbatim). *(what to do next)*
8. The **contact line** — booking link · @handle (· email).
9. The **member's photo, large** — the cut-out (see photo treatment).
10. The **compliance strip** — brokerage name and license exactly as the Book's Compliance chapter
    requires, the brokerage chip anchored in a corner or the contact cluster if required — the single
    thin, least-important line on the banner.
11. A **rich background** — the member's treated culture photo when provided, else the brand gradient +
    the toolkit texture + the oversized mark device.

If any of items 2–10 is missing, the banner is WRONG — add it before presenting.

**Photo treatment (fix the "weird headshot").** A clean **cut-out of the member (background removed)**
placed in its own column and sized large, OR a straight rounded-rectangle photo panel — NOT a tall
awkward arch, a partial outline, or an odd mask. **THE FULL-HEAD RULE:** the ENTIRE head is visible —
top of the hair to the shoulders — with clear air above. If the composition would clip the head, scale
the photo DOWN or reposition it. Expressive shots on content pieces; the clean headshot on trust pieces.

- **YouTube banner — 2560 × 1440 full canvas, ALL content inside the centred 2560 × 423 safe strip**
  (`banner-youtube.png`). YouTube rejects uploads smaller than 2048×1152, so the file is the full
  canvas — but every element lives inside the vertically centred 2560×423 strip, because that strip is
  all that shows on desktop (TVs see the full canvas; phones slightly more than the strip). Design the
  strip exactly like the other banners — one wide, fully filled band: logo + role line + who-you-help
  row (left), **name + positioning line + CTA + contact + proof chip** (centre), the **large photo**
  (right). Then EXTEND the brand background (gradient, texture, the treated photo, the ghost mark —
  background art only, never content) to fill the full 1440 height edge to edge. NEVER draw a dashed
  safe-area box, guide lines, or empty margins.
- **THE BLEED IS DESIGNED, NOT EMPTY.** The canvas outside the strip is finished background art at
  real, arm's-length strength. The TV crop must look like a deliberate wide shot.
- **NO GUIDE-COSPLAY ON FINAL ART.** Never a thin full-perimeter keyline box around content, never
  corner dots or handles that read as selection UI.
- **NO SYSTEM LABELS ON ARTWORK.** Internal codes and spec labels never render inside a piece.
- **Facebook cover — 1640×624** (`banner-facebook.png`). Same wide, fully filled layout with ALL items;
  leave room for the profile-photo overlap at the bottom-left. **Mobile crop trap:** phones show only
  roughly the CENTRE 1200×624 — keep the name, positioning line, CTA, and contact line inside that
  centre zone (background art still runs full width); park only sacrificeable elements near the edges.
- **LinkedIn banner — 1584×396** (`banner-linkedin.png`). Same layout with ALL items; keep content clear
  of the bottom-left profile-photo spot. Team leaders and broker-owners live on LinkedIn — this banner
  is not a sparse afterthought.

**THE COVER TEMPLATE (Facebook + LinkedIn — one mandatory recipe):** divide the canvas into three
columns. **LEFT (~30%):** logo + role line + who-you-help row, stacked, at banner-row weight. **CENTRE
(~40%):** the name huge + the positioning line + the CTA button with the contact line under it + the
proof chip — the full cluster, together, aligned. **RIGHT (~30%): THE PHOTO COLUMN — reserved
exclusively for the cut-out.** No button, text, or logo may enter the photo column, and the photo may
not leave it — that boundary is what kills the recurring truncated-button failure. The cut-out fills its
column bottom-anchored, full head with air. The compliance strip runs along the bottom edge of the
left or centre column, never under the photo. (Instagram has no banner; its profile is the picture, the
bio, and the highlight covers.)

> KEEP COUNTS LOW FOR SPEED: at most **3 templates per set** below. The tweaks panel swaps the
> status, headline, and format from the same design.

### Feed-post templates — the three jobs (1080×1350 portrait default; square via tweak)
Instagram's profile grid shows 3:4 tiles, so a 1080×1350 post loses ~34px off EACH SIDE in the grid —
keep headlines, faces, and the footer inside the central ~1012px width AND inside the central
1080×1080 region. That double-safe zone survives the grid, square re-crops, and every feed.

**FEED-POST TYPE SCALE & SPACING (at 1080 width — when in doubt, text goes BIGGER):** headline
110–150px heavy; support 34–40px and never below ~32px; the CTA band's line 56–72px; eyebrows 24–28px
BOLD in a high-contrast colour. Outer margins ~72–96px with ONE vertical rhythm; the CTA band gets real
height (~14–18% of the canvas). **THE SQUARE-CROP RULE:** the eyebrow + the FULL headline (and the
face) sit inside the centre-square region; footer and CTA bands may run to the edges.

1. **The Agent-win post** (`post-win.png`) — the culture, proven. **The formula:** (a) **Full-bleed** —
   the agent's photo (with permission) fills the top 55–70% and FADES into a rich brand band below; or
   (b) **Framed window** — the photo sits in the win-card frame from the Design System on a rich brand
   ground. **The zones INTERLOCK** (the photo fading into the band, the frame overlapping it, or the
   member's small cut-out across the seam) — two stacked rectangles that never touch is a failed post.
   **The status word is the type hero** — "WELCOME", "FIRST DEAL", "MILESTONE", "CLOSED #10", "AWARD" (via
   the winStatus tweak; "CAPPED" only where the Book's Compliance chapter's rev-share marketing policy
   allows it) — two-tone or metallic, with the agent's first name beside it, a one-line detail
   ("3 buyers under contract in her first 60 days" — the member's own words, never an invented number),
   and ONE slim contact bar with the compliance strip. **The empty template still looks DESIGNED:** the
   placeholder IS the framed window with a small "Your agent's photo" label in brand type; NEVER app UI
   in the artwork. Nothing about what the agent earns.
2. **The Teaching post** (`post-teach.png`) — authority. The member's expressive cut-out on a clean
   brand ground, a big headline that is ONE real thing they know how to do (from the Book's known-for or
   "what you have to give (so far)" — "The 7pm text that turns sign-ins into buyers"), a one-line
   support, a soft CTA ("Save this · Book a call with me"), the contact bar + compliance strip.
3. **The CTA post** (`post-cta.png`) — one type of agent, one pain, one action. The cut-out, a bold
   question or statement aimed at the **primary type of agent** in the Book, in Mike's pain wording
   ("Paying for leads and still guessing where the next deal comes from?"), the button "Book a call with
   me", the contact bar + compliance strip. **THE AVATAR TEST:** the three posts speak to three
   different types of agent from the Book — or, with one avatar, to three different pains of the five —
   never three variations of one message. **ONE-STEP CTA:** a single frictionless action; a keyword CTA
   ("DM me the word CALL") is fine; "grab my guide" only once a guide exists (Week 2, after the offer).

### Story templates — 1080×1920, 3 max
- **Agent-win story** (`story-win.png`) — the win formula vertically (photo full-bleed-with-fade or the
  win frame on the rich ground), the status word, the agent's name, the contact/compliance line.
- **About / "meet your sponsor" story** (`story-about.png`) — the member's cut-out, the role line, the
  positioning line, and a question-sticker zone ("ask me anything about going full-time").
- **CTA story** (`story-cta.png`) — the pain headline + "Book a call with me" + a link-sticker zone.
- Keep key text out of the top/bottom ~250px (UI zones). **Stories fill the canvas like posters, not
  forms** — no contiguous empty region over ~25%. **Sticker zones are DESIGNED, not drawn as code:** a
  subtle tinted plate with a small plain label in brand type, never a dashed developer-style box. **The
  cut-out never touches text.**

### Instagram highlight covers — 1080×1080, up to 5, icon centred in a circle-safe area
One consistent line-icon style in the brand colours on the brand-tinted tile. **THE ICON SIZE LAW:**
the icon FILLS the circle — **60–75% of the diameter**, chunky strokes, crisp at ~77px. **THE 80-PIXEL
TEST:** shrink to an 80px circle — if the icon isn't instantly identifiable, scale it UP and thicken it.
Named to the five topics from Mike's profile lesson (a mini website for your recruiting), or the
member's own: **About me** (`highlight-about.png`, their monogram or a person icon) · **Agent wins**
(`highlight-wins.png`, a trophy or a rising line) · **Culture** (`highlight-culture.png`, people or a
flame) · **Free value** (`highlight-value.png`, an open book or a gift — the guide's own cover fills it in
Week 2, once the Lead Magnet plugin writes it) · **Partner with me** (`highlight-partner.png`, a handshake or an open door). Optional extras via
request: Training, Events, Behind the scenes.

### The "Join My Team" 1-pager cover — US Letter portrait, 2550×3300 (`cover-join-my-team.png`)
The front door of the member's offer: a designed cover page that carries the five answers on one
sheet — the member's name (or the organization's lockup) and role line, the positioning line, the
who-you-help row, the proof chip if real, the member's cut-out or the treated culture photo, the
booking link in FULL plain text with "Book a call with me", and the compliance strip + any required
disclaimer. **The body is reserved by design:** a quiet labelled band ("What you get — built in
Week 2") — `aa-offer-kit-design` (its one-pager piece) fills the page from the Partner Offer. Title in the member's words
("Partner with Taylor", "Join The Lakeline Collective"), default "Join my team". Nothing about
splits, caps, stock, or earnings — ever — on this page.

### Bonus pieces (round out the kit like a full agency package)
- **Email signature** (`signature-light.png`, `signature-dark.png`) — a polished horizontal signature
  designed at 600×200, exported at 1200×400 (2×), with FIVE mandatory anchors: (1) the member's photo
  (clean circle) with a brand accent ring, left; (2) name + role line; (3) the stacked contact block
  (phone · email · booking link · @handle) with small brand-colour icons; (4) **THE BRAND FOOTER ROW, in
  this order: the member's OWN mark FIRST, then the "Book a call with me" line, then the brokerage chip
  and license as required** (non-negotiable #1); (5) a divider or accent rule. A light and a dark version.
- **YouTube end screen** (`end-screen-youtube.png`) — 1920×1080, built around YouTube's clickable
  elements: EXACTLY ONE clear 16:9 **next-video rectangle** (left/centre) and ONE **circular subscribe
  placeholder** (right), never duplicated, each with a bold prompt and a pointing device (an arrow or
  the member's gaze toward the circle) so it sells the click. Keep the bottom ~90px clear for the scrub
  bar. Around them: the brand gradient, the logo, the member's cut-out, "Watch the next one" and
  "Subscribe" prompts, the compliance line beside the logo. Not a flat dark box with two outlines.
- **Vertical backgrounds** (`background-1.png`, `background-2.png`, `background-3.png`) — three
  branded 1080×1920 grounds the member layers reels and stories on: a brand texture, a brand-colour
  field, and a treated culture-photo field (or a second texture when no photo exists).

### The organization family — the people side of the kit (organization set, or the personal set)
Built after the bonus pieces, on the locked look's devices only (the Design System §7 and §12: gradient
headline · gold numeral · chevron · brushed stroke · taped-photo frame · vertical text rail · pill button
· organization URL footer). The **organization set** (the Book records an organization name) fronts every
piece with the organization's lockup and its URL footer; the **personal set** (no organization name) uses
the same canonical names on the member's own lockup, the handle and booking link in the footer, and
skips the member-of-the-month, 4-up, 16-grid, and `org-profile-logo.png` pieces until a named
organization exists. Every piece: the compliance strip as the Book requires, the brokerage chip in ONE
corner only where required, at most two devices beside the type and the photo, the feed-post type scale
and the double-safe zone above.

- **Milestone post** (`org-post-milestone.png`, 1080×1350) — the Book's organization number (the
  Snapshot's "organization today" line) set 400–600px tall in the numeral device (foil on dark; deepened
  on light), the word under it in the heading face ("AGENTS" / "PARTNERS"), a pill or a rule carrying
  **"have now joined [the organization's name / me]"**, the organization's lockup, the footer. The count
  is never rounded, never invented, never "CAPPED" unless the Book's rev-share marketing policy allows it.
  No organization number in the Book = no milestone post.
- **Anniversary post** (`org-post-anniversary.png`, 1080×1350) — the member's photo (half-body, treated)
  with "[N] YEAR(S) AT [BROKERAGE]" or "[N] YEARS OF [THE ORGANIZATION]" as a two-tone or gradient
  headline, the number from the Book; the brokerage's name set in the kit's type as a fact (never its
  logo as the hero, never its colours); the footer.
- **Member-of-the-month template** (`org-post-member-of-month.png`, 1080×1350) — the look's thin frame
  around the piece, the agent's cut-out (or a designed window) over the mark ghosted large and
  low-opacity, the agent's name in tracked caps, **the organization's own title** as the type hero
  (default "MEMBER OF THE MONTH"), the month in the accent face, the footer. Swap photo · name · month.
- **Welcome post — single / template** (`org-post-welcome-single.png`, 1080×1350) — the **vertical text
  rail** ("WELCOME TO [THE ORGANIZATION'S WORD]" — the Book's phrase, default "WELCOME TO THE TEAM")
  along the right edge in the metallic or the accent; the new agent's photo in the **taped-photo frame**
  (tilted 2–4°, two tape corners, greyscale allowed) or as a cut-out; the name as the type hero, bottom
  left; the lockup and the footer. The empty template shows a designed photo window with "Your new
  partner's photo" in brand type — never app UI.
- **Welcome post — 4-up** (`org-post-welcome-4up.png`, 1080×1350) — one welcome headline across the
  top (the gradient or metallic treatment the look allows), four cut-outs in staggered vertical panels
  that overlap by 10–15%, first names optional under each, the footer.
- **Welcome post — 16-grid** (`org-post-welcome-grid16.png`, 1080×1350) — a 4×4 grid of equal headshot
  tiles (one tint over all sixteen so mixed photos read as one set, 12–16px gutters) filling the
  left ~80%, the vertical rail down the right edge, the lockup + URL + chip footer along the bottom.
- **"Send me a DM" post** (`org-post-dm-cta.png`, 1080×1350) — the member's expressive cut-out, a
  two-line question for the primary type of agent in Mike's pain wording ("Want to become a modern
  agent?"), the **pill button** carrying the offer's comment keyword when the Book holds one ("DM me the
  word CALL"), else "Send me a DM"; one or two chevrons pointing at the headline; the footer. One
  action only; no compensation word.
- **Thumbnail master** (`org-thumbnail-master.png`, 1280×720) — the two-tone headline (one word in the
  accent or the gradient line, the rest in cream or white; four words max, 120–160px), the expressive
  cut-out on one side (two co-leaders flank it when there are two), the mark small in a corner, one
  device (a stroke or a chevron), the look's texture at real strength. Readable at 240px wide; the
  face never clipped; the headline inside the centre 70%.
- **Profile-circle set** (`org-profile-photo.png` · `org-profile-mark.png` · `org-profile-logo.png`,
  1080×1080 each, circle-safe) — the member's photo with the look's device behind it (a brushed stroke,
  a ring, the texture), the mark alone inside a thin ring on the dark ground, the organization's logo
  centred on its field. One bold element each; recognisable at 40px.
- **Stories with a button** (`org-story-welcome.png` · `org-story-dm-cta.png`, 1080×1920) — the welcome
  story (the rail, the taped frame or cut-out, the name) and the DM story (the question, the pill
  button, a designed sticker plate for the link or question sticker); key text out of the top and
  bottom ~250px; posters, not forms.
