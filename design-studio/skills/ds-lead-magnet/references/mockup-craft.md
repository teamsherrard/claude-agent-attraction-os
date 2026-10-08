# Mockup Craft — the product as a real object (shared by ds-product-mockup and ds-lead-magnet)

Read in full before rendering any mockup, cover, or device shot.

## THE CANONICAL-COVER RULE (one cover, everywhere — never a second design)

A product has exactly ONE cover, and every shot of it reproduces that cover faithfully:
- **A designed cover already exists** (a guide built by `ds-lead-magnet`, a product built by the
  Value Vault skills, or a cover the member uploads) → REUSE it exactly. Never redesign, restyle,
  "improve", or recolour it for the mockup. A mockup that doesn't match the actual download or the
  actual product breaks trust at the exact moment of delivery.
- **No cover exists yet** (Week 2: the product is mapped, built in Week 6) → design the cover now from
  the brief's cover line and subtitle, and say plainly: *"This cover IS your product's cover — when the
  Value Vault builds the product in Week 6, it reads this file and keeps it."* Save it as the flat cover
  so the later skill can pick it up.
- **Two different covers in one project** is a failure: find the newer, confirm with the member in one
  line, retire the other from every shot.

## THE COVER (what makes it look published)

- **The title is the promise** — the brief's cover line, exactly; the single largest element on the
  cover (at least 3× body size); 7 words or fewer. A longer title keeps the member's words and splits
  into a short dominant line + a subtitle.
- **The subtitle names the payoff** — the brief's subtitle (under 10 words).
- **The byline** — "By [Name]" with the brokerage only as the compliance block requires it on a cover;
  the member's logo or mark, small; the organization's mark on group products where the Design System's
  logo card says.
- **Dated on purpose** when the product is dated (a comparison guide carries "Last updated [Month
  YYYY]"); a current-year badge on an evergreen product only if the member wants it — never a fake
  edition number.
- **The visual** — a brand field, the toolkit texture, the oversized mark device, or a real photo the
  member dropped (with a scrim behind any text). Never a stock person, never a generated face, never
  a house-and-key visual on a leader's product.
- **THE THUMBNAIL TEST (mandatory):** judge the cover at phone-thumbnail size (~150px wide). If the
  title isn't instantly readable and the brand isn't recognizable there, rebuild the cover BEFORE any
  shot is rendered — the cover reappears small on the funnel, in the stack, and in the feed.

## THE SHOT LIBRARY (pick the shots the product's format earns)

| Format | Hero shot | Supporting shots |
|---|---|---|
| **Ebook · guide** | a paperback or booklet at a slight angle: visible page thickness, the spine carrying the title and the member's name, a soft contact shadow | the flat cover · a phone showing page 1 · the open-spread shot (two interior pages) |
| **Playbook · workbook** | a spiral-bound or soft-cover workbook, slightly thicker, a tab or two showing | the flat cover · a tablet with a filled worksheet page · the stack-of-three shot |
| **Course** | the course box (a boxed set with the title on its face and spine) beside a laptop whose screen shows the module list | the flat cover · the phone showing lesson 1 · the box alone |
| **Bundle** (the product + its templates, checklists, scripts) | the composed group: the hero product front and centre, the supporting pieces fanned behind it at the same angle and light | each piece alone when the stack or the funnel needs it |
| **Device screens** (any format) | a phone and a laptop at one consistent angle, each showing the product's first real page — never a blank screen, never lorem ipsum | the phone alone (for stories), the laptop alone (for the deck) |

**Every shot obeys the same geometry:** one angle (three-quarter by default, the member can rotate),
one light source, one shadow softness, one floor — so shots from different sessions sit together on a
page. Claude Design's mockup preview has rotate / tilt / backdrop sliders: set a strong default and
tell the member in plain words — *"drag the sliders above the product to angle it how you like, then
save."*

## THE TRANSPARENT LAW (what makes a shot usable)

- The hero and device shots ship as **transparent-background PNGs** — the object and its soft shadow
  only, no floor, no backdrop, no stage. A mockup locked on a white box is unusable on a funnel hero,
  a dark slide, or a brand ground.
- The **flat cover** ships as its own full-quality PNG at the product's page ratio — it becomes page
  one of the product and the share image.
- The **social and story versions** are the exception: the product on the brand ground with the title
  and the honest status line — opaque by design.
- Build every exportable piece as ONE inline `<svg data-file="…">` at its exact size (the export-page
  contract): no background rect on transparent pieces; preview grounds live behind the SVG, never in it.

## HONESTY RULES (a mockup is a promise)

- **No fake badges.** No "bestseller", "#1", review stars, "as seen on", award ribbons, "10,000
  downloads", or edition numbers the product hasn't earned.
- **The status line is the brief's** — *"included when you partner with me"* · *"first version with my
  first partners"* · *"coming this quarter"* — never "available now" for a product that isn't built.
- **Real screens only.** A device shows the product's actual first page (built from the brief's outline
  or the guide's page 1), never a mock dashboard, never a fake table of contents the product won't have.
- **No page-count or lesson-count claims** on the cover unless the brief states them.
- **No compensation anywhere** — the product is what the member gives, never what a partner earns.
- **No other brokerage's name or mark** on any cover or screen; the member's brokerage only as the
  compliance block requires.

## THE FALLBACK (never ship a broken object)

If a dimensional render comes out warped, soft, or low-quality, fall back to a near-flat cover with a
subtle tilt and a soft shadow — it still reads as a product. A clean flat shot always beats a bent book.

## REFRESH (the cover changes, the shots follow)

When the cover changes (a new subtitle, a new year, the Value Vault's final version), re-render every
shot from the new flat cover and re-export under the SAME file names, so the stack, the one-pager, the
funnel, and every post that embedded the old files pick up the new ones without rewiring.
