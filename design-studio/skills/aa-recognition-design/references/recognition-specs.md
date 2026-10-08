# Recognition Specs — part of the aa-recognition-design skill

Read in full before building any piece.

## 1. THE RECOGNITION POINTS → STATUS WORDS (`16-implementation-scaling/82` + the Admin's win list)

| Win (as the Admin logs it) | Status word on the piece | Notes |
|---|---|---|
| joined the organization | **WELCOME** | the welcome set; the organization is the hero |
| closed their first deal | **FIRST DEAL** | the warmest piece — "nobody cares at most brokerages", said in the member's way, never as a dig |
| attracted their first agent | **FIRST PARTNER** | Mike's trophy moments start here (first · 10 · 100) |
| a company-level award | **AWARD** + the award's name exactly as the brokerage names it | as stated in the brief; never an award the member invented |
| a production milestone the agent stated | **MILESTONE** / **CLOSED #N** / **N DEALS** | only the figure the agent stated, consent on file |
| a leadership step | **LEADER** | "now leading the Tuesday call" |
| showing up (streaks, training finished) | **SHOWED UP** / **12 CALLS STRAIGHT** / **TRAINING DONE** | the small wins that keep people (`13-team-building-duplication/65`) |
| a personal moment they chose to share | **MARRIED** / **NEW BABY** / **NEW CITY** | only with the agent's explicit yes; never inferred from social |
| capped | **CAPPED** | ONLY where the Compliance chapter's rev-share marketing policy allows it; the word alone, never the figure; otherwise MILESTONE |

## 2. PIECES & TRUE SIZES

**Every piece is ONE inline `<svg data-file="…">`** at its exact size (see the export-page reference).
Opaque by design — the ground IS the artwork.

| Piece | File | Size | Notes |
|---|---|---|---|
| Win Wall post | `win-[firstname]-post.png` | 1080×1080 (brief default) · 1080×1350 via tweak | the kit's win template, swapped |
| Win Wall story | `win-[firstname]-story.png` | 1080×1920 | key text out of the top/bottom ~250 px; a designed tag plate |
| Welcome post · story | `welcome-[firstname]-post.png` · `-story.png` | as above | WELCOME + first name + "joined [organization]" |
| Private congratulations card | `card-[firstname].png` | 1080×1080 | sent by text with the member's video message; no contact bar |
| Certificate | `certificate-[firstname].png` + PDF via the Export menu | US Letter landscape 11×8.5 in → 3300×2550 px at 300 DPI, bleed 0.125 in (3375×2625 with bleed), safe margin 0.375 in | print-ready; A4 landscape via tweak |
| Monthly Win Wall roundup | `winwall-[YYYY-MM].png` | 1080×1350 | 4–6 tiles; posted wins only |

Instagram's grid crops a 4:5 post to 3:4 — keep the status word, the face, and the name inside the
central 1080×1080 region and the central ~1012 px width. Type floors at 1080 width: status word
110–150 px heavy; the first name 60–80 px; the detail line 34–40 px, never under ~32 px; eyebrow
24–28 px bold; the contact bar and compliance strip the only small lines (~24 px).

## 3. ANATOMY — THE WIN WALL POST (the kit's formula, restated)

1. **The photo window, 55–70% of the canvas** — the agent's photo (consent on file), full head with
   air, wearing the Design System's photo treatment; (a) full-bleed top, fading into the brand band, or
   (b) the kit's win-card frame on the rich ground. **Interlocked**, never two stacked rectangles.
2. **The status word, the type hero** — two-tone or the Design System's metallic, inside the
   centre-square safe region.
3. **The first name** beside or under the status word (the surname only with consent and only where
   the member wants it).
4. **The detail line** — the brief's one line, in the member's words, what the agent DID.
5. **The organization name** (and the organization's logo version where two exist).
6. **The slim contact bar** — the member's booking link · handle — with the **compliance strip**
   (brokerage name as the display rule says, the chip where required).
7. **Optional:** the member's small cut-out across the seam (off by default).

**The empty window** (no photo yet): the kit's framed photo window with a small "[Agent]'s photo"
label in brand type — designed, never app UI.

## 4. ANATOMY — THE WELCOME SET

- **WELCOME** as the status word; the agent's first name; the line **"joined [organization]"** — the
  organization is the hero (agents follow people, `03-model-positioning/17`); the brokerage appears
  only as the display rule requires ("[Team], brokered by [Brokerage]" where that is the rule).
- **The member's one line about them** — who they are and why the member is glad ("a second-year agent
  in Round Rock who runs the best open houses I've seen"), from the brief or the member's words; never a
  line about where they came from, never a production claim.
- The agent's photo (or the designed window), the organization's logo, the contact bar + compliance
  strip. Post + story. The story carries a designed plate for the tag.

## 5. ANATOMY — THE PRIVATE CONGRATULATIONS CARD

A 1080×1080 card the member sends with a video message or a text (Mike: as personal as possible). The
agent's first name, the win, two lines in the member's voice (from the Book's voice cards), the
member's signature line (name · role), the organization's mark. No contact bar; the compliance strip
only if the member says they'll post it. The card is a gift, not a post — warmer, quieter.

## 6. THE CERTIFICATE — PRINT MECHANICS (the print-kit rules apply)

- **Trim 11×8.5 in landscape**, bleed 0.125 in on every edge (background art runs into the bleed),
  all type and the logo at least 0.375 in inside the trim. 300 DPI. Print-safe colour (rich brand
  solids; no neon). Reversed light-on-dark type ≥ 8 pt at a regular-or-heavier weight; no hairlines.
- **Anatomy, top to bottom:** the organization's logo (or the member's when there is one version) ·
  the title line ("CERTIFICATE OF ACHIEVEMENT" / "OF COMPLETION" / "OF RECOGNITION" — one of these;
  never a title that implies an official body) · an eyebrow naming the milestone ("First deal",
  "100 partners", "[Award name]") · **the agent's FULL NAME, the largest element** · one line of what
  it honours, in the member's words · the date · the organization name · the member's printed name and
  role line over a signature rule (a real signature image only if uploaded) · the brokerage chip where
  the display rule requires it, small, one position.
- **Craft:** the Design System's accent as a frame rule or a corner device; the metallic token (when
  one exists) on the title or the name; a quiet pattern from the toolkit at low strength; generous
  margins. Never a drawn seal, ribbon, or crest that mimics an official certification.
- **Trophy moments** (`16-implementation-scaling/82`): first partner · 10 · 100 partners — the same
  certificate with the milestone eyebrow; the member may pair it with a physical trophy; the
  certificate carries no compensation word.
- **Hand-off to the printer:** export the PDF with bleed from the Export menu; tell the printer the
  trim is 11×8.5 in and bleed is included; 100–110 lb uncoated cover or a linen stock; the file
  previews in RGB — ask the printer to match the brand colours.

## 7. THE MONTHLY WIN WALL ROUNDUP

One 1080×1350 piece: a title band ("[Organization] · [Month] wins"), a grid of 4–6 tiles (each: the
agent's treated photo · first name · status word), the member's one line of thanks, the contact bar +
compliance strip. Only wins already posted with consent; a held win never appears. Tiles share one
crop and one treatment so the grid reads as one family; the register alternates with the previous
roundup.

## 8. CONSENT AND CLAIMS — RECAP

- A name goes public only with consent on file (the brief's line, or the Book's Proof chapter "OK to
  use publicly?" = yes). "Ask first" → built, HELD, excluded from the export.
- A production figure only when the agent stated it and consent covers it; income, rev share, splits,
  caps (except the gated word), stock — never.
- The agent's former brokerage never named; a win never framed against any brokerage or person.
- Company-level awards as the brokerage names them, exactly as stated; never an award invented.
- No protected characteristic on any piece.
