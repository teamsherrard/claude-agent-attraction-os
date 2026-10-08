# Course Specs — part of the aa-course-design skill

Read in full before building any piece.

## 1. THE PACKAGE MANIFEST

| Piece | File | Size | Export | Notes |
|---|---|---|---|---|
| Lesson title cards (one per lesson) | `lesson-[m]-[l]-card.png` | 1920×1080 | button | the first frame of each recording; video-safe |
| Lesson slide master + 3 examples | `slide-master.png` (+ the examples on the board) | 1920×1080 | button (master) | the member teaches from it |
| Course outline one-pager | `[course-slug]-outline.pdf` | US Letter portrait | Export menu | the syllabus |
| Module workbooks (one per module) | `[course-slug]-module-[n]-workbook.pdf` | US Letter portrait | Export menu | on the playbook mechanics |
| Certificate of completion | `[course-slug]-certificate.pdf` + `certificate-template.png` | US Letter landscape 11×8.5 in | Export menu + button | print-ready; per-agent names via refresh or `aa-recognition-design` |
| Product cover (canonical) | `product-cover-flat.png` | the product's cover size (the mockup's) | button — ONLY when designed here | reused exactly when `aa-product-mockup-design` built it |
| Course tile 16:9 | `course-tile-16x9.png` | 1280×720 | button | the course's picture on its page |
| Course tile square | `course-tile-square.png` | 1080×1080 | button | community platforms and posts |
| Module tiles | `module-[n]-tile.png` | 1280×720 | button | on the module tints |
| Notes | `course-notes.md` | — | button | manifest · module colours · what's thin · the mockup hand-off |

## 2. STRUCTURE RULES (the member's outline — never curriculum this skill writes)

- **3–7 modules, 2–5 lessons each.** Module 1 Lesson 1 = the Book's teach-first lesson 1. The Book's
  digital-product outline (3–7 parts, each "after this part you can…") maps to the modules.
- **Every lesson = one skill statement + one hand-over.** "After this lesson you can [do the thing]" +
  the sheet, script, or template it gives. A lesson with neither is flagged as thin, laid out with what
  exists, and never filled by the skill.
- **Every module = one tint** from the palette's working mid-tones (the Design System's `colour.mid-1`,
  `colour.mid-2`, and tints of `colour.primary`); the tint runs across the module's cards, tiles, and
  workbook tabs.
- **Where to get help** (from the Book's How You Operate chapter): the weekly call, the community, who
  to message — on the outline and every workbook's last page. Unset → an "ask me" line.
- **The 30-day line** (from the Book's Offer chapter, the first 30 days as a partner): which lessons
  land in which week — printed on the outline as a small table.

## 3. THE LESSON TITLE CARD (1920×1080 — anatomy)

Module number and name in the module's tint (an eyebrow, top-left) · the lesson number small · **the
lesson title** in the heading face at 80–120 px (one or two lines) · **the skill statement** at 40–48 px
("after this lesson you can…") · the member's clean headshot small in a corner (the Design System's
frame) · the organization's mark opposite · the course title treatment as a quiet footer line. Nothing
inside 5% of any edge (96 px sides, 54 px top and bottom); no thin type; the dark register by default
(the member cuts from the card to their face). A card with no words except the title fails the job —
the skill statement is what tells the agent why to watch.

## 4. THE LESSON SLIDE MASTER (1920×1080)

One master: the title position, the module-tint band, the footer (course title · page), the margins
(~80–100 px). Three example slides built on it: **a claim slide** (one sentence, huge), **a steps slide**
(numbered, verb-led, three to five), **a figure slide** (the sheet or script shown large, with one note).
The member duplicates the master per lesson; this skill does not build every lesson's deck — the
member teaches, the recording carries the lesson.

## 5. THE OUTLINE ONE-PAGER (US Letter portrait — anatomy)

The course title treatment · "for [type of agent]" · the member's welcome line with the headshot ·
the modules as bands in their tints, each listing its lessons with the skill statements and the
hand-over named · the 30-day table (week → lessons) · where to watch · where to get help · one real
proof line if the Book has one (never invented) · the compliance line in the footer. Dense but
readable: body 10–11 pt, bands with real air, one page.

## 6. THE MODULE WORKBOOK (US Letter portrait — on `aa-playbook-design`'s mechanics)

Cover (the module tile's composition, portrait) → imprint (the module, the course, the version and
date, the compliance line) → the module opener (the module's claim) → per lesson: the skill statement
as the kicker and title · the steps · the figure (the sheet or script as the real thing) · a fillable
page (3–6 prompts with ruled lines; a tracker table where the lesson has numbers) → the module
checklist (verb-led, real boxes, one page) → "bring this to the call" (the three things to bring to
the weekly call; the where-to-get-help line) → back cover. Print mechanics: bleed 0.125 in, safe
0.5–0.75 in, body 11–12 pt, kickers, reversed type ≥ 8 pt, page numbers, the module tab in its tint
on every page.

## 7. THE CERTIFICATE (US Letter landscape — print mechanics from the recognition specs)

Trim 11×8.5 in, bleed 0.125 in, safe 0.375 in, 300 DPI; reversed type ≥ 8 pt regular-or-heavier. The
organization's logo (or the member's) · "CERTIFICATE OF COMPLETION" · the course title · **the agent's
FULL NAME, the largest element** · "completed [course] with [member / organization]" · the date · the
member's printed name and role over a signature rule (a real signature only if uploaded) · the
brokerage chip where required · the Design System's accent as a frame rule or corner device; the
metallic token on the title when one exists. Never a drawn seal that mimics an official body; never an
outcome or income claim. The template carries a designed name line; the per-agent version is issued
through refresh mode or `aa-recognition-design`.

## 8. THE COVER AND THE TILES

- **The canonical cover:** reused exactly from `aa-product-mockup-design` when it exists (`product-cover-flat.png`
  beside `product-mockup-3d.png`, in the project or in `05 · Offer`). Designed here only when none exists: the title seven words or
  fewer, benefit- or skill-led, the largest element; the subtitle names the method; the member's name
  and the organization; the Design System's photo treatment on a real photo of the member or a brand
  graphic; the year small; the brokerage only where the rule puts it on a cover; the THUMBNAIL TEST at
  150 px; no fake badges or stars. Announced as canonical.
- **Tiles (16:9 and square):** the cover's composition re-laid for the format; the title reads at
  150 px; the member's face; the organization's mark; "for partners of [organization]" optional; no
  outcome or income line. **Module tiles** on the module tints with the module number large and the
  module name.

## 9. THE HAND-OFF TO DS-PRODUCT-MOCKUP (the course box is built there)

```
FOR aa-product-mockup-design — course box
Product: [course name] · Format: course · Cover: product-cover-flat.png (canonical, in 05 · Offer/[Course name]/)
Module colours: [n tints, hex] · Module names: […]
Pieces wanted: the course box · device screens (the 16:9 tile on a laptop, a lesson card on a phone) · the bundle shot (box + the module workbooks)
Status line for the graphic: "Included when you partner with me" / "Coming this quarter"
Never on the mockup: an outcome or income line, another brokerage's name.
```

## 10. RULES THAT HOLD ON EVERY PIECE

Skill statements, never promises · no compensation word · the member's own method only · former
brokerages never named · agent examples with consent only · the brokerage only as the compliance chip
· the AI-likeness line if lessons are recorded with a clone · a type of agent, never a protected
characteristic.
