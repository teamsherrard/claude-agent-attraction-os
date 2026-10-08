# Agent Attraction Design System — default template (v1.0)

*The uploadable Design System for the Agent Attraction Design Studio. Attach this file to your Brand HQ
project in Claude Design. `ds-style-sheet` fills it with YOUR values and saves the result as
"[First Last] Design System" — from then on, every `ds-` skill reads your copy, never this template.*

**What this is.** A design system is the durable record of a brand's execution values: colours, fonts,
spacing, how the logo is used, how photos are treated, the reusable components every graphic is built
from, and the voice the copy is written in. The Brain decides the *direction* (your brand-visual
inventory and direction, your voice, your compliance rules); this file holds the *execution values*
that make every piece match. **No colour, font, or name in this template is a brand** — every member
value is left as `[member value]` and is filled by `ds-style-sheet` from your approved style sheet and
your Brain Book. The defaults that ARE real (spacing, scale, safe zones, component rules, the laws)
hold for every member unless their style sheet says otherwise.

---

## 0. How a member copy is made (instructions for `ds-style-sheet`)

1. Copy this file whole. Keep every section, heading, token name, and rule; change values only.
2. Fill every `[member value]` from the approved style sheet (the winning option) and the Brain Book
   (Snapshot · The Leader · Your Voice & Brand · Your Agent Avatars · Your Proof · Compliance).
3. Where the member skipped something, write the safe default and mark it `(default — change anytime)`;
   never leave a bracket in a saved copy.
4. Rename the title to **"[First Last] Design System"**, stamp `Created: YYYY-MM-DD · from the Agent
   Attraction Design System v1.0`, and save it in Claude Design as a native Design System under that
   name (compile the tokens, logo and photo cards, type roles with hierarchy examples, components, and
   voice cards). Export the filled file as `design-system.md` into the workspace's `02 · Brand`.
5. Before compiling, preview the tokens on one light piece and one dark piece; fix the range first if
   it turns monotone or murky.
6. On any later change (`ds-style-sheet` refresh mode), change the value here AND in the native Design
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
| Direction / feel | `[the two or three words from the brief]` |

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

**Rules:** the logo is placed as-is, never redrawn, stretched, recoloured outside the palette, given
effects, or set on a busy photo without a solid shape behind it. **The brokerage mark** is a quiet chip
in ONE consistent position (a corner or inside the contact cluster), never beside the member's logo as
a partner, shown only where the compliance block requires it, and never drawn from memory.

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
Week 6 by the Lead Magnet system; empty until then]`.

**Copy laws:** the member speaks as "I" (organization pieces may say "we"); the people they attract are
"agents" or "partners"; outcomes, never features; what the member will SHOW, never what a partner will
EARN; no splits, caps, stock, tiers, rev-share, or income words; never a negative word about another
brokerage or person; a former brokerage is "a franchise" or "an independent"; the Partner Offer is a
Week 2 line, the free guide a Week 6 line — never written as if they exist before they do.

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
| Logo | `logo-*.png/.svg` · `org-logo-*` · `logo-spec.md` | `ds-logo` (or the member's loved logo, uploaded as-is) |
| Style sheet + system | `style-sheet.pdf` · `design-system.md` | `ds-style-sheet` |
| Brand kit | `profile-*.png` · `banner-*.png` · `highlight-*.png` · `post-*.png` · `story-*.png` · `cover-join-my-team.png` · `signature-*.png` · `end-screen-youtube.png` · `background-*.png` · `brand-kit-captions.md` | `ds-brand` |
| Headshots | `headshots/` | the member |

The Brain's health check counts the brand kit as present when `02 · Brand` holds a logo file, the
style sheet, and at least one profile graphic. Later `ds-` skills (offer assets, carousels, thumbnails,
the Value Vault) read this registry and never re-ask for anything in it.

---

## 11. Change log and the handshake with the Brain

| Date | Change | By |
|---|---|---|
| `[YYYY-MM-DD]` | Created from the Agent Attraction Design System v1.0 | `ds-style-sheet` |

**The handshake:** the Brain owns direction (`brand-visual.md`: inventory and direction) and the Brain
Book carries it; this Design System owns execution values. When they disagree, the member decides — and
says **"update my attraction brand direction"** in their Brain so the Book matches the kit. Nothing here
is edited in the Brain's files by a design skill; nothing in the Brain is edited by this file.
