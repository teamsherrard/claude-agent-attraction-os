# Ebook Specs — part of the aa-ebook-design skill

Read in full before building any page.

## 1. THE STRUCTURE (`04-value-proposition/34`: past · transformation · mission · value · vision)

| Part | Chapters | Source (manuscript path / assembled path) | Rules |
|---|---|---|---|
| Front matter | cover · title page · imprint · "why I wrote this" · contents (built last) | the why-line from the Book's Journey chapter | the imprint carries the compliance line, the version and date, "© [year] [member]" |
| **Part 1 · The story** | 1 Where I started · 2 The hardest stretch · 3 The turning point | the manuscript's story chapters / the Journey's three beats + the story blocks that belong to each beat | the mirror: the wall, never the company; former brokerages "a franchise", "an independent", "a team"; the "who relates to this" line may close each chapter in the member's words |
| **Part 2 · The method** | one chapter per strategy that worked (3–6) | the manuscript's method chapters / the Offer chapter's "what worked" rows + the teach-first lessons | each chapter: what it involved · the result the member can stand behind · the lesson · the real sheet or script as a figure page; results as the member stated them, never rounded up |
| **Part 3 · The people** | partners' stories (2–8) | the manuscript's case chapters / the Proof chapter's agents-helped rows + consented testimonials + the story bank's "an agent I helped won something" blocks | consent on file for every name, photo, and quote; every size of win (`06-content-framework/40`); each story told for the agent who'll relate to it; a first name and a type of agent, the surname only with consent |
| **Part 4 · What's next** | 1 The mission and the vision · 2 What partnering looks like · 3 The invitation | the "Why join me" long version / the same block from the Book's Model chapter; the How You Operate chapter for the day-to-day | "value" means support and systems, never money; the income disclaimer verbatim if an organization-building line appears; the invitation = the primary CTA + the booking link |
| Back cover | the one-breath why · the headshot · contact in full · the compliance line | the Book's Journey chapter one-breath line | the brokerage chip where required |

**Length, honestly:** a manuscript of 6–7k words lands at ~24 pages at 6×9; 15–18k words at ~60. The
assembled path lands at ~20–30 pages and is called "the shorter edition" out loud.

## 2. PAGE ANATOMY AT 6×9 IN (1800×2700 px at 300 DPI; bleed 0.125 in when the member will print)

- **Margins:** inside 0.75 in · outside 0.625 in · top 0.75 in · bottom 0.875 in; one text column of
  ~4.4 in; 28–34 lines per page.
- **Body:** a readable serif or the Design System's body face at 10.5–11.5 pt, leading 1.4; body is
  only ever dark-on-light (the light tint, never default white when printing on screen; white for a
  printed edition).
- **Running heads:** the book title on the left-hand page, the chapter title on the right, in the
  Design System's eyebrow style at 8–9 pt; **folios** (page numbers) at the outside of the foot.
- **Part dividers:** full-page, the dark register, the part number large in the heading face, the
  part name, one line from the member; the toolkit's texture at low strength.
- **Chapter openers:** the chapter number large, the title, a pull line (one sentence of the member's,
  set at 14–16 pt), the text starting a third of the way down the page.
- **Figure pages:** the sheet, script, or routine set as the thing itself on a plate with a one-line
  caption; a "try this" box in the Design System's component style where the step is given.
- **Portrait pages (Part 3):** the partner's photo in the Design System's frame (consent), the first
  name and type of agent as a label, the story; no photo → the designed window.
- **Pull quotes:** one per chapter at most, the member's own line, the quote device from the toolkit.
- **The invitation page:** the primary CTA large ("Book a call with me"), the booking link in full
  plain text, the member's headshot, the one-breath why; the compliance line in the foot.

**Type laws:** all-caps headings get extra letter spacing; the script face never carries body text or
captions; accents survive every heading; the body face verified at reading size for the brand
language. Widows and orphans cleaned; hyphenation sane; no page ends on a heading.

## 3. THE COVER — RULES WHEN DESIGNED HERE (otherwise reused exactly)

**The ratio rule first:** an existing `product-cover-flat.png` (letter ratio by `aa-product-mockup-design`'s
default) means the book is set at US Letter so the cover is reused untouched; a cover designed here is
built at the book's page ratio (6×9 by default) and saved as `product-cover-flat.png` at that ratio.

The title is story- or promise-led, seven words or fewer, the largest element (≥ 3× the subtitle); the
subtitle names the payoff ("what I'd tell the agent I used to be"); the member's name as the author;
a real photo of the member in the Design System's treatment (an expressive shot reads as a person; the
clean headshot reads as a leader — the Book's "leads with" line decides) or a brand graphic; the
organization's mark small; the brokerage only where the display rule puts it on a cover. **THE
THUMBNAIL TEST** at 150 px: the title reads and the brand is recognizable — it becomes the 3D mockup in
the offer stack. No fake badges, stars, or "bestseller" marks; no income word. Exported as
`product-cover-flat.png` and announced as canonical.

## 4. THE HAND-OFF TO DS-PRODUCT-MOCKUP

```
FOR aa-product-mockup-design — book
Product: [book title] · Format: ebook · Cover: product-cover-flat.png (canonical, in 05 · Offer/[Book title]/)
Pieces wanted: the 3D paperback (product-mockup-3d.png, transparent) · a phone/tablet screen · the bundle shot when the playbook or course exists
Spine text: [title · member name] · Page count: [n]
Status line for the graphic: "Included when you partner with me" / "Coming this quarter"
Never on the mockup: an outcome or income line, another brokerage's name, a fake review or rating.
```

## 5. CONSENT, CLAIMS, AND THE CARDINAL RULES — RECAP

- A partner's name, photo, result, or quote appears only with consent on file (the Book's Proof
  chapter "OK to use publicly?" = yes, or the manuscript says consent is on file); otherwise a first
  initial and a type of agent, or the story is left out — never invented, never embellished.
- Results exactly as stated; no rounding up; no income, rev share, split, cap, or stock word anywhere.
- Former brokerages never named; nothing negative about any brokerage, sponsor, team, or person.
- A type of agent, never a protected characteristic; no claim about who "belongs" anywhere.
- The income disclaimer verbatim where Part 4 mentions building an organization; the compliance line
  on the imprint and the back cover; the AI-likeness line if any photo is a render (it never is here —
  real photos only).
