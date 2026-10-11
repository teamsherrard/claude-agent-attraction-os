# Agent Attraction Design System — default template (v1.0)

*The uploadable Design System for the Agent Attraction Design Studio. Attach this file to your Brand HQ
project in Claude Design. `aa-style-sheet-design` fills it with YOUR values and saves the result as
"[First Last] Design System" — from then on, every `aa-…-design` skill reads your copy, never this template.
Section 12 is the house style library: the named looks every skill applies, chosen from the Creative
direction your Brain wrote, never asked of you.*

**What this is.** A design system is the durable record of a brand's execution values: colours, fonts,
spacing, how the logo is used, how photos are treated, the reusable components every graphic is built
from, and the voice the copy is written in. The Brain decides the *direction* (your brand-visual
inventory and direction, your voice, your compliance rules); this file holds the *execution values*
that make every piece match. **No colour, font, or name in this template is a brand** — every member
value is left as `[member value]` and is filled by `aa-style-sheet-design` from your approved style sheet and
your Brain Book. The defaults that ARE real (spacing, scale, safe zones, component rules, the laws)
hold for every member unless their style sheet says otherwise.

---

## 0. How a member copy is made (instructions for `aa-style-sheet-design`)

1. Copy this file whole. Keep every section, heading, token name, and rule; change values only.
2. Fill every `[member value]` from the approved style sheet (the winning option) and the Brain Book
   (Snapshot · The Leader · Your Voice & Brand — including its Creative direction block · Your Agent
   Avatars · Your Proof · Compliance). Record the ONE look the sheet locked (§12) and the Creative
   direction it came from; later skills apply that look's devices and never re-derive it.
3. Where the member skipped something, write the safe default and mark it `(default — change anytime)`;
   never leave a bracket in a saved copy.
4. Rename the title to **"[First Last] Design System"**, stamp `Created: YYYY-MM-DD · from the Agent
   Attraction Design System v1.0`, and save it in Claude Design as a native Design System under that
   name (compile the tokens, logo and photo cards, type roles with hierarchy examples, components, and
   voice cards). Export the filled file as `design-system.md` into the workspace's `02 · Brand`.
5. Before compiling, preview the tokens on one light piece and one dark piece; fix the range first if
   it turns monotone or murky.
6. On any later change (`aa-style-sheet-design` refresh mode), change the value here AND in the native Design
   System, add a change-log row, re-export `design-system.md`.

---

## 1. Identity card

| Field | Value |
|---|---|
| Member (the leader) | `[First Last]` |
| Organization name | `[name — or "none; just my name"]` |
| Logo versions | `[one: my name · two: my name + my organization's name]` |
| Brand shape | `[one brand, my name, with a leader lane (default) · separate leader brand]` |
| Market · attracts in | `[City, Region · local / statewide / national / listed states]` |
| Brokerage (the vehicle; compliance mark only) | `[exact name as compliance requires]` |
| Brokerage palette we stay distinct from | `[their colour family, in plain words + codes if known]` |
| Compliance state | `[unset · set · confirmed YYYY-MM-DD]` |
| Brand language(s) | `[e.g., English · English + Spanish · Français (CA)]` |
| Leads with (the brand formula) | `[authority · relatability · aspiration — the one the Brain says is strongest today]` |
| Known for | `[one line from the Brain's "The Leader" chapter]` |
| Primary type of agent | `[in plain words, from the Brain's avatar chapter — never the word "avatar" on a graphic]` |
| Tagline | `[chosen · parked]` |
| Direction / feel | `[the mood line from the brief's Creative direction — one sentence]` |
| Creative direction (from the Brain) | `[energy 1–5 · type: classic / modern / bold · colour story: dominant · support · accent · photo: clean cut-out / moody / bright · the three motifs · the avoid list's member-specific line]` |
| Locked look (§12) | `[one named look from the house style library — picked by aa-style-sheet-design from the brief's three recipes; every later skill applies it]` |
| Examples studied | `[what the member dropped into Brand HQ: past pieces, their current profile, brands they like — direction only, never copied · or "none"]` |

**Rules that hold in every copy:** the brokerage is never the brand; the organization's name is never
the brokerage's name; the leader brand stays visually distinct from the brokerage's own colours; the
selling brand (when separate) never carries recruiting language; the leader brand never carries
compensation numbers.

---

## 2. Colour tokens

| Token | Plain name | Value | Role | Rule |
|---|---|---|---|---|
| `colour.dark` | Dark anchor | `[#hex · name]` | the dark-register ground; text on light grounds | never pure #000000 unless the direction is Editorial Black & White |
| `colour.light` | Light ground | `[#hex · name]` | the light-register ground | a TINT of the palette (cream, paper, stone), never default #FFFFFF |
| `colour.primary` | Brand colour | `[#hex · name]` | the hue the brand is known by; bands, devices, the mark | sits visibly outside the brokerage's colour family |
| `colour.accent` | Accent | `[#hex · name]` | the punch: one highlighted word, a rule, the CTA pill | ONE accent hit per zone of a piece; never carries white text if it is light or metallic |
| `colour.mid-1` | Working mid-tone | `[#hex · name]` | tinted fields, tiles, chips | used ON pieces, not just displayed as a swatch |
| `colour.mid-2` | Second mid-tone (optional) | `[#hex · name — or "none"]` | a second tint for range | optional |
| `colour.neutral` | Warm neutral | `[#hex · name]` | borders, quiet labels, the compliance strip | never the lead of a piece |
| `colour.metallic` | Metallic (optional) | `[light #hex → deep #hex — or "none"]` | foil accents, a status word, a monogram | shown as a light→deep gradient; deepened toward its shadow tone on white |
| `colour.ink` | Text on light | `[defaults to colour.dark]` | body text on light grounds | body text is only ever dark-on-light or light-on-dark |
| `colour.paper-text` | Text on dark | `[defaults to colour.light]` | body text on dark grounds | same law |

**Mix ratio (default — change on the sheet):** `[60% ground · 25% brand colour · 10% mid-tones ·
5% accent]`. The accent is the smallest number by design.

**The two registers.** Every kit ships in both: the **dark register** (`colour.dark` ground,
`colour.paper-text` type, the accent as the punch) and the **light register** (`colour.light` ground,
`colour.ink` type, the same accent). **Quota:** at least about one third of any kit's pieces on each
register; type, accents, logo treatment, and devices identical across both.

**The pairing test (print it, then prove it):** every swatch's label is set in the colour that actually
goes on it; unreadable = the pairing fails and the swatch is darkened or lightened. No two swatches
read as near-duplicates. Metallics never carry white text.

**Distinct-from-brokerage line (printed on the sheet, carried here):** `[“Stays distinct from
[brokerage]’s [colour family]”]`.

---

## 3. Type scale

| Role | Token | Font | Weight · case · tracking | Used for |
|---|---|---|---|---|
| Heading | `type.heading` | `[font — real, available, covers the brand language]` | `[e.g., Bold · ALL CAPS · +0.04em]` | names, status words, headlines, the drama band |
| Body | `type.body` | `[font]` | `[e.g., Regular · sentence case]` | support lines, captions on pieces, document body |
| Accent (optional) | `type.accent` | `[script or display face — or "none"]` | never all caps, never body text; one short line at a time | a first name, a signature line, one word of emphasis |
| Technical (optional) | `type.technical` | `[mono face — or "none"]` | regular | figures, dates, licence numbers; never headlines, never banner copy |

**Scale at 1080px width (posts, covers, stories):** headline 110–150px heavy · support 34–40px, never
below ~32px · CTA line 56–72px · eyebrow label 24–28px bold, high contrast. **Banner rows at 2560px
width (YouTube; scale proportionally for Facebook and LinkedIn):** role and who-you-help rows 34–44px,
weight 700, full contrast — never thin, letter-spaced, mid-tone; the name as a massive display moment;
the compliance strip the only thin line. **Documents (US Letter covers and pages):** body 11–12pt,
headings roughly 3× body, kicker above headings.

**Type laws:** the script or decorative face is never set in all caps and never carries body text; any
ALL-CAPS heading gets a touch of extra letter spacing; every face is verified to render the brand
language's full character set, including accented capitals; the font name recorded here is the font
actually rendered.

---

## 4. Spacing, geometry, and safe zones

| Token | Value | Note |
|---|---|---|
| `space.unit` | 8px | every margin and gap is a multiple |
| `space.margin.post` | 72–96px at 1080 width | one consistent vertical rhythm per piece |
| `space.cta-band` | 14–18% of the canvas height | the CTA band gets real height |
| `radius` | `[e.g., 0px sharp · 12px soft · pill]` | one radius per brand; pills for buttons and chips |
| `rule.weight` | `[e.g., 2px]` | accent rules and dividers; one or two weights, never three |
| `grid` | `[e.g., 12 columns, 24px gutter]` | align everything to it |
| `logo.clear-space` | ≥ the height of the mark (or the tallest letter) | on every side |
| `logo.min-size` | `[e.g., 120px wide on screen; 1 inch in print]` | if you can't read it, it's too small |
| `headshot.shape` | `[arch · circle · rounded square]` | the one branded frame for the member's photo |

**Safe zones (platform truth, not taste):** YouTube banner 2560×1440 with ALL content inside the
centred 2560×423 strip · Facebook cover 1640×624 with the name, positioning line, CTA, and contact
inside the centre ~1200px · LinkedIn 1584×396, clear of the bottom-left profile spot · Instagram feed
1080×1350 with headline, face, and footer inside the central ~1012px width AND the central 1080×1080 ·
stories 1080×1920 with key text out of the top and bottom ~250px · YouTube end screen 1920×1080 with
the bottom ~90px clear · profile pictures circle-safe with margin · highlight icons 60–75% of the circle.

**Reserve zones:** text, photos, buttons, logos, sticker plates, and the compliance strip each own clear
space on every piece; nothing overlaps, nothing truncates; cut-outs leave the frame at the bottom edge
only, full head with air above.

---

## 5. Logo cards

| Card | File (in `02 · Brand`) | Where it is used |
|---|---|---|
| Primary | `logo-primary.png` / `.svg` | the style sheet header, covers, the signature |
| Horizontal · Stacked | `logo-horizontal.*` · `logo-stacked.*` | wherever the primary doesn't fit the space |
| Mark alone | `logo-mark.*` · `logo-mark-favicon.png` | profile pictures, highlight "About me", favicons, the oversized ghost device |
| One-colour (dark · light) | `logo-onecolour-dark.*` · `logo-onecolour-light.*` | print, stamps, embroidery, one-colour surfaces |
| Built for dark grounds | `logo-reversed.*` | the dark register (never a filter inversion) |
| Content header | `logo-header.*` | the bar at the top of posts, banners, video cards |
| Organization version (when two) | `org-logo-*` | group surfaces: win posts, culture pieces, the Join My Team cover |
| Brokered-by lockup (compliance variant, only when the brokerage logo was uploaded) | `logo-brokered-lockup.*` | only the surfaces where the compliance block requires the brokerage mark beside the member's own (signage, print, a profile banner in a strict jurisdiction); never the primary, never a partner lockup |

**Rules:** the logo is placed as-is, never redrawn, stretched, recoloured outside the palette, given
effects, or set on a busy photo without a solid shape behind it. **The brokerage mark** is a quiet chip
in ONE consistent position (a corner or inside the contact cluster), never beside the member's logo as
a partner, shown only where the compliance block requires it, and never drawn from memory. **The
brokered-by lockup** is the one sanctioned exception, and it is subordinate by construction: the member's
mark first, a hairline divider, then a small "BROKERED BY" eyebrow over the brokerage mark at no more than
40% of the member's mark height — it exists only when the brokerage logo was uploaded and only where
compliance requires it. **The mark stays vector-clean:** texture, foil, and grounds live on the piece,
never inside the logo file.

---

## 6. Photo treatment

- **Frame:** the member's headshot sits in `headshot.shape`, tinted or bordered in a brand colour.
- **Cut-outs:** background removed, full head with air, standing INTO the design; exit the frame at the
  bottom edge only or fade deliberately.
- **Treatment law:** a real photo never sits raw behind text — it wears `[duotone wash in colour.primary
  · darkened toward colour.dark · a scrim where text sits]`.
- **Trust surfaces vs content surfaces:** the clean headshot on the profile picture, the signature, and
  the About cover; expressive shots on CTA and teaching pieces.
- **People:** the member (and a co-leader, if any); the member's agents only with their permission, in
  win posts and culture imagery. Never a generated face, never a stock person, never a fabricated
  office, crowd, or event.

---

## 7. Components

| Component | What it is | Tokens | Rule |
|---|---|---|---|
| **CTA button** | the pill or highlighted line "Book a call with me" | `colour.accent` fill or `colour.primary`; `type.heading` | the only button on a piece; the booking link or handle sits under it |
| **Eyebrow label** | the small bold label above a headline | `type.heading` 24–28px | high contrast, never thin mono caps |
| **Proof chip** | one real credential, number, or agent result as a quiet pill | `colour.mid-1` plate, `colour.ink` | only from the Brain's Proof chapter; none = no chip; never "#1 / best / fastest-growing" without a dated source |
| **Win card** | the frame or plate a recognition post is built on (status word + agent + detail) | `[frame / ribbon / plate]` in `colour.primary` + metallic | the status word is the type hero; the agent's photo window fills 55–70%; zones interlock |
| **Quote device** | how an agent's testimonial is set | quotation marks in `colour.accent`, attribution in `type.body` | verbatim, with consent on file; one quote per piece |
| **Contact bar** | the slim bottom bar: booking link · handle · email | `colour.neutral` rule, `type.body` | one per piece, never cramped |
| **Compliance strip** | brokerage name · licence · chip, as the compliance block requires | `type.technical` or `type.body` small; `colour.neutral` | present on every public piece; the thinnest line; never floating |
| **Sticker-zone plate** | the designed tinted plate that reserves a story's poll/question/link zone | `colour.mid-1` at low opacity, label in `type.body` | never a dashed developer-style box |
| **Highlight tile** | the branded tile behind a highlight-cover icon | `colour.primary` or `colour.light`; icon in the contrasting colour | icon fills 60–75% of the circle |
| **Section band** | a full-width band on the style sheet or a document | alternating `colour.dark` / `colour.light` / tints | light-dark-light-dark rhythm; one drama band per sheet |
| **Photo window** | the designed empty frame that stands in for a photo | the win-card frame or `headshot.shape` | reads designed when empty; never app UI |
| **Brokerage chip** | the required brokerage mark | as supplied | quiet corner, one position, where required only |
| **Toolkit** | the brand's pattern · texture · accent device · oversized mark | `[describe each as built on the sheet]` | from the sheet only; never invent a new device on a later piece |
| **Graphic-elements trio** | the three named devices the style sheet locks: the **mark device** (the mark or emblem used as art), the **shape device** (a chevron, a parallelogram, a diamond lattice, a bracket), the **texture or gradient device** | from the locked look (§12) | every later piece draws from these three before anything else |
| **Gradient headline** | one headline word or line filled with the look's two-hue gradient | `colour.primary → colour.accent` (or the look's pair) | at most ONE gradient line per piece; the rest of the type is solid |
| **Gold numeral** | a milestone count or a year set huge in the metallic | `colour.metallic`, `type.heading` at display scale | only a real number from the Book; foil on dark, deepened on light |
| **Chevron** | the triple chevron that points at a headline or bullets a row | `colour.accent` or paper-text | one direction per piece; never a chevron wall |
| **Brushed stroke** | a dry-brush swipe behind a word, a photo, or a corner | `colour.primary` or `colour.accent` at full strength | one or two per piece; behind, never over, the type |
| **Taped-photo frame** | a photo in a plain frame with two tape corners, slightly tilted | `colour.light` frame, tape in `colour.neutral` | the welcome template's photo window; the photo may be greyscale |
| **Vertical text rail** | one word or short line set vertically along an edge ("WELCOME", the organization's word) | `type.heading`, `colour.metallic` or `colour.accent` | the only vertical text on a piece |
| **Pill button** | the rounded-ended button that carries one action ("Send me a DM", "Book a call with me", "Schedule your place") | `colour.accent` fill or a 2px outline; label in `type.heading` | the only button on a piece |
| **Organization URL footer** | the slim footer row: the organization's mark, its URL (or the booking link), the brokerage chip in a corner | `type.body` small, `colour.neutral` rule | present on every organization piece; the chip only where compliance requires |

---

## 8. Voice cards

**Sounds like:** `[2–4 lines from the Brain's voice chapter]` · **Never sounds like:** `[the never-say
list; the recruiter register ("opportunity call", "let's talk about [brokerage]")]` · **Banned words
everywhere:** unlock · supercharge · game-changer · revolutionary · secret weapon · leverage as a verb.
**Signature phrases:** `[three the member actually says]`.

**The five profile answers (the copy slots every piece fills — from Mike's profile lesson):**

| Slot | Fill from | Current value |
|---|---|---|
| Who you are | Snapshot · The Leader | `[name + role line, e.g., "Team leader · The Lakeline Collective"]` |
| Who you help | the primary type of agent | `[in plain words, e.g., "agents in years 2–5 who are paying for leads"]` |
| What you help them do | the one-line why · known for · what you have to give (so far) | `[e.g., "build a pipeline that doesn't need a lead bill"]` |
| Why listen | Your Proof (real, with permission) | `[one credential or result — or "none yet (no chip)"]` |
| What to do next | the primary CTA | `["Book a call with me" + booking link]` |

**The two CTAs:** primary = `["Book a call with me" — link]`; second = `[the guide keyword — set in
Week 2 by the Lead Magnet system, right after the offer; empty until then]`.

**Copy laws:** the member speaks as "I" (organization pieces may say "we"); the people they attract are
"agents" or "partners"; outcomes, never features; what the member will SHOW, never what a partner will
EARN; no splits, caps, stock, tiers, rev-share, or income words; never a negative word about another
brokerage or person; a former brokerage is "a franchise" or "an independent"; the Partner Offer is a
Week 2 line and the free guide follows it in the same week — never written as if they exist before they do.

---

## 9. Compliance block

**State:** `[unset · set · confirmed YYYY-MM-DD]` — unset means no public piece is exported until the
Brain's compliance basics are set ("set up my attraction compliance"); "if empty, proceed" is banned.

**Every public piece carries:** brokerage name `[exactly as required]` · licence `[number · where it
must appear]` · brokerage mark `[where required, how large relative to the member's own mark]` ·
required disclaimer `[verbatim — or "none required (confirmed with [who], [date])"]`.

**Always:** no earnings or compensation content; the two cardinal rules (never talk badly about another
brokerage or another person); agent testimonials verbatim with consent; targeting by career stage,
production, model, and mindset — never a protected characteristic; any piece turned into a paid ad to
attract licensed agents may fall under Meta's Employment special ad category and the brokerage's rule on
ads — flag it. This is assistance, not legal advice; the member confirms with their brokerage.

---

## 10. Asset registry (what lives in `02 · Brand`)

| Set | Files | Built by |
|---|---|---|
| The brief | `Design Package Brief · [Name] · [date].md` | the Brain (`attraction-brand-direction`) saves it here through the storage connector; the newest date is current; it is also kept inside the Brain, so "show my design package brief" reprints it any time |
| Logo | `logo-*.png/.svg` · `org-logo-*` · `logo-brokered-lockup.*` (only when the brokerage logo was uploaded) · `logo-spec.md` | `aa-logo-design` (or the member's loved logo, uploaded as-is) |
| Style sheet + system | `style-sheet.pdf` · `design-system.md` | `aa-style-sheet-design` |
| Brand kit | `profile-*.png` · `banner-*.png` · `highlight-*.png` · `post-*.png` · `story-*.png` · `cover-join-my-team.png` · `signature-*.png` · `end-screen-youtube.png` · `background-*.png` · `brand-kit-captions.md` | `aa-brand-kit-design` |
| Organization family (the people side of the kit) | `org-post-milestone.png` · `org-post-anniversary.png` · `org-post-member-of-month.png` · `org-post-welcome-single.png` · `org-post-welcome-4up.png` · `org-post-welcome-grid16.png` · `org-post-dm-cta.png` · `org-story-welcome.png` · `org-story-dm-cta.png` · `org-thumbnail-master.png` · `org-profile-photo.png` · `org-profile-mark.png` · `org-profile-logo.png` | `aa-brand-kit-design` (the organization set when the organization has a name; the personal set, same names, on the member's own lockup when it does not) |
| Video Brand Kit | `Video Brand Kit/` — `hook-*.png` · `lower-third-*.png` · `emphasis-*.png` · `cta-*.png` (the primary + the eight-ask pack) · `end-screen.png` · `icons/` · `video-brand-spec.md` (the editor reads this folder by its canonical names) | `aa-video-kit-design` (Week 3, with the editor) |
| Headshots | `headshots/` | the member |

The Brain's health check counts the brand kit as present when `02 · Brand` holds a logo file, the
style sheet, and at least one profile graphic. Later design skills (the offer kit, the content kit, the video kit, thumbnails,
the Value Vault) read this registry and never re-ask for anything in it.

---

## 11. Change log and the handshake with the Brain

| Date | Change | By |
|---|---|---|
| `[YYYY-MM-DD]` | Created from the Agent Attraction Design System v1.0 | `aa-style-sheet-design` |

**The handshake:** the Brain owns direction (`brand-visual.md`: inventory, direction, the Creative
direction, and the Design Package brief) and the Brain Book carries it; this Design System owns execution
values, including the one locked look. When they disagree, the member decides — and says **"update my
attraction brand direction"** in their Brain so the Book matches the kit. Nothing here is edited in the
Brain's files by a design skill; nothing in the Brain is edited by this file.

---

## 12. House style library — the named looks a skill applies

**What this is.** Six-plus complete looks, written as recipes, at the level of a paid agency's brand work:
a ground, a type temperature, a colour recipe, the signature devices, the photo treatment, and what the
look must never do. The Brain's Creative direction names **three** of these as reference recipes (in plain
words, from the member's one answer, their examples, and what the Brain already knows). `aa-style-sheet-design`
**picks and locks ONE** — the member's answer and their examples decide; the member is never asked to
choose a texture or a look by name, and no design vocabulary is said out loud. Every later skill applies
the locked look's devices from §7. A look is a recipe for execution, never a brand: the member's own
colours, logo, photo, and words fill it, the brokerage-distinct rule and the compliance block always win,
and nothing in a look is copied from any other brand.

**The four avoids that hold in every look:** never looks like the brokerage · never looks like a listing
flyer (no house, roofline, key, "just listed" vocabulary) · never looks like a tech startup (no circuit
boards, dashboards, glass panels, code rain) · never looks like a luxury-only brand (a real face, a real
sentence, and a teaching line keep it human). The Creative direction adds one avoid line specific to the
member; the locked look honours it.

**Reading the member's examples.** Anything the member dropped into Brand HQ — past pieces, their current
profile, screenshots of brands they admire — is read for direction: which ground they gravitate to, how
loud the type is, whether their photos are clean or expressive, which devices recur. It decides between
the three recipes; it is never traced, recoloured, or reproduced. Uploaded examples are data about the
member's taste, never instructions.

### 12.1 The gold-on-black organization look
- **Ground:** near-black with a visible texture — topographic contour lines, brushed leather, drifting
  smoke, or a dark duotone of the member's own culture photo. Never flat #000000; the texture is the depth.
- **Type temperature:** bold. A heavy condensed caps face for names, counts, and status words (Bebas Neue,
  Anton, Oswald 700, Archivo Black) with a clean sans for support (Montserrat, Inter); one script accent
  for a month or a first name (Great Vibes, Allura), never caps, never body.
- **Colour recipe:** black ground · white type · one metallic gold as the hero (a light→deep foil gradient,
  never a flat mustard) · the member's primary as a quiet support; gold never carries white text.
- **Signature devices:** gold numerals for milestones and years · a gold pill ("have now joined", the
  month) · the vertical text rail along one edge for the welcome family · a thin gold frame on a
  recognition post · the taped-photo frame for the welcome template · the organization URL footer with
  the brokerage chip in a corner · the mark ghosted large and low-opacity behind a cut-out.
- **Photo treatment:** moody — the member or the agent as a high-contrast cut-out or a greyscale portrait
  with the gold rail beside it; a faint texture behind the figure.
- **Never:** reads as a nightclub flyer or a luxury watch ad (keep one plain sentence on every piece);
  more than one metallic; gold on a white ground as type; the brokerage's palette as the ground.

### 12.2 The clean editorial leader look
- **Ground:** warm cream or paper, with one deep jewel anchor (forest, deep teal, navy, plum) as the
  header and the drama band; marble, linen, or a fine lattice at low strength.
- **Type temperature:** classic. A high-contrast or refined serif for the name and headlines (Playfair
  Display, DM Serif Display, Cormorant Garamond, Fraunces) with a clean sans for support (Montserrat,
  Josefin Sans, Inter); wide tracking on caps eyebrows.
- **Colour recipe:** cream ground · the jewel anchor · one metallic (brass, champagne, copper) as a thin
  rule and the mark · a soft mid-tone (sage, dusty gold, stone) for tiles. The metallic is deepened on
  cream and glows on the jewel.
- **Signature devices:** hairline metallic rules and a thin frame · a diamond or lattice motif at the
  edges · a skyline or horizon line only when the member attracts locally · the arch headshot frame · the
  numbered font roles (01 · 02) set in the metallic · the quote device with large serif quotation marks.
- **Photo treatment:** clean cut-out, evenly lit, on the jewel ground; or a full-colour portrait in the
  arch.
- **Never:** tips into luxury-only (a teaching line and a warm first-person sentence on every piece);
  a listing flyer (no house illustration, no "just listed"); thin pale type on cream that fails the
  pairing test.

### 12.3 The bold gradient coach look
- **Ground:** a deep saturated field (aubergine, midnight navy, charcoal violet) with a soft city or shape
  silhouette at low opacity; or, in the light register, warm white with one gradient block.
- **Type temperature:** bold. A heavy condensed italic or a strong display sans for headlines (Anton,
  Bebas Neue, Barlow Condensed 800, Kanit 800) with a rounded or geometric sans for support (Poppins,
  Montserrat, Plus Jakarta Sans).
- **Colour recipe:** the member's two or three brand hues as ONE gradient (warm→cool, e.g. orange →
  magenta → violet, or the member's own pair) · white for the rest of the type · the dark field · one
  pill colour for the button.
- **Signature devices:** the gradient headline (one line per piece) · the pill button ("Send me a DM",
  "Book a call with me") · stacked chevrons pointing at the headline · a soft neon ring or arc behind the
  cut-out · a small 3D object only when the member's story calls for one (a course box, a phone), never
  decoration for its own sake.
- **Photo treatment:** bright and expressive — the member mid-gesture, pointing, laughing, cut out and
  standing into the field with a subtle rim light.
- **Never:** a gradient on every line (rainbow); glass panels, dashboard widgets, or code rain (tech
  startup); a shouted headline with no plain sentence under it; more than one gradient per piece.

### 12.4 The brushed-stroke bold look
- **Ground:** two grounds that alternate — a dark textured ground (denim, leather, dry-brush smoke) and a
  cream textured ground (paper grain, a faint halftone) — so the set reads light-dark-light-dark on its own.
- **Type temperature:** bold. A tall condensed display face for headlines (Bebas Neue, Oswald, Anton)
  with a sturdy humanist sans for support (Source Sans 3, Work Sans, Barlow); the two-tone headline is
  the signature: one word in the accent, the rest in cream or black ("PRO" + "TIPS").
- **Colour recipe:** black · cream · ONE strong accent (a deep red, a burnt orange, a marigold) · a darker
  shade of the accent for depth. Three working colours, used hard.
- **Signature devices:** one or two brushed strokes behind a word, a corner, or a profile photo · the
  triple chevron (">>>") bracketing section titles · small "+" marks and hairline diagonals as punctuation
  · a thin ring around the mark in the profile circle · a hairline rule under a two-tone headline.
- **Photo treatment:** moody — grainy, slightly desaturated cut-outs with a stroke behind them; two
  co-leaders flank a headline.
- **Never:** reads as a gym or a sports team (no jersey numbers, no mascots); more than two strokes on a
  piece; the accent on the brokerage's hue; a stroke running over the type.

### 12.5 The navy-and-gold emblem look
- **Ground:** deep navy or charcoal with a marble or flowing-ink texture at real strength; white
  rounded cards for the light register.
- **Type temperature:** classic-modern. A geometric or grotesk sans with wide tracking for the
  organization name (Josefin Sans, Montserrat, Raleway at +0.2em) with an italic serif for the tagline
  (Cormorant Garamond Italic, Playfair Display Italic) and a clean sans for body (Roboto, Inter).
- **Colour recipe:** navy · two golds (a flat gold and a foil gradient) · white · nothing else. Gold is
  the mark; navy is the room.
- **Signature devices:** the illustrated single-weight emblem (a creature or figure drawn in one line
  weight, with a simplified version for profile size) · gold parallelogram or diagonal strokes in two
  corners · the "[Organization] by [Name]" construction (the organization name as the hero line, "BY
  [FIRST LAST]" as the tracked descriptor) · swatch cards with the metallic rendered as foil · the 3×2
  logo-variations grid over dark and over white.
- **Photo treatment:** clean cut-out, arms crossed or at ease, on the navy; the emblem ghosted behind.
- **Never:** the emblem becomes a cartoon mascot or gains a second line weight; gold type on white
  without deepening; the brokerage's navy (shift hue or depth until a stranger would not confuse them).

### 12.6 The bright accent creator look
- **Ground:** light paper grey or warm white for the sheet and the light register; near-black for the
  dark register; a quiet dot grid or a soft colour blob behind the cut-out.
- **Type temperature:** modern. A black-weight geometric sans for headlines (Archivo Black, Poppins 900,
  Plus Jakarta Sans 800) with the same family at regular for body; an outlined word paired with a solid
  word ("JOIN" outlined, "MY WEEKLY" solid) as the signature headline.
- **Colour recipe:** near-black · white · ONE electric accent (lime, cyan, marigold) · one supporting
  mid-tone (a muted teal, a sand). The accent is loud and rare.
- **Signature devices:** the pill button in the accent · a label box in the accent behind one headline
  word · the bracket or avatar-style mark used as a sticker · the dot grid · a two-tone thumbnail (a
  yellow label + white condensed words on the accent gradient).
- **Photo treatment:** bright — an expressive cut-out (pointing, a wink, hands up) on the accent field;
  the profile circle pairs the mark on dark with the photo on the accent.
- **Never:** a software-company look (no circuit grids, no device mock-ups as the ground, no "AI" glow);
  the accent as body text; more than one accent.

### 12.7 The warm paper mentor look
- **Ground:** warm cream paper with a visible grain; a deep green, oxblood, or charcoal as the anchor band.
- **Type temperature:** classic. A warm serif for headlines (Fraunces, Lora, Libre Caslon) with a quiet sans
  for body (Inter, Source Sans 3); a hand-written accent for one word only (Caveat, Kalam).
- **Colour recipe:** cream · the anchor · a copper or clay accent · a sage or stone mid-tone. Soft, never
  pale: every swatch passes the pairing test.
- **Signature devices:** the taped-photo frame · a hand-drawn underline rule · a kraft or index-card
  plate for the win card · a small stamp-style mark · a numbered routine ("1 · 2 · 3") in the accent.
- **Photo treatment:** clean, warm, natural light; the member at a table, a whiteboard, a doorway — never
  staged luxury.
- **Never:** a wedding-stationery read (keep the headline weight real and the sentences plain); a
  listing flyer; the hand-written face in caps or as body.

### 12.8 How a skill applies a look
1. Read the Creative direction block in the brief (mood · energy 1–5 · type temperature · colour story ·
   photo treatment · three motifs · the avoid list · three reference recipes). The recipes are named in
   the member's plain words and map to the looks above; the first named is the Brain's own pick.
2. `aa-style-sheet-design` locks ONE look (its two options are two executions of that look; a second
   recipe may lead Option 2 only when the member's examples pull clearly toward it) and records it here
   in §1. It never asks the member to choose a texture, a finish, or a look by name.
3. Every later skill applies the locked look: its ground, its type temperature within the recorded fonts,
   its devices from §7, its photo treatment. The member's three motifs become the content of the devices
   (the routine as the numbered device, the market as the place device, the organization's idea as the
   mark device). Nothing new is invented on a later piece.
4. The locked inputs always win over the look: the member's exact codes, the logo as-is, the
   brokerage-distinct rule, the compliance block, the real fonts rule (§3), the four avoids and the
   member's own avoid line.
5. Energy sets the volume, not the look: energy 1–2 = quiet grounds, lighter weights, more air; 3 = the
   recipe as written; 4–5 = the drama band on more pieces, the heaviest weight in the recipe, the
   expressive photo on every content piece.
