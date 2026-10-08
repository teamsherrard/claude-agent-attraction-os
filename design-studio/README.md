# Design Studio — a Claude Design skill set, not a plugin

Claude Design (claude.ai/design) cannot run Cowork plugins; it accepts uploaded skill files. This
folder is the Agent Attraction Design Studio: the 15 `ds-` skills that build and run the member's
LEADER brand (the brand agents follow — never a listing brand), plus the **Agent Attraction Design
System** every skill reads. Plan: `docs/plans/02-agent-attraction-os-master-gameplan.md` §3. House
rules: `docs/plans/BUILD-BRIEF.md`. Recycled from the realtor Claude Design suite v2 (read-only, on the
Desktop), with the realtor premise replaced by the leader premise. **All 15 are built and packaged.**

## The fifteen skills, by the week the member uploads them

| # | Skill | Week | Brief / doc it consumes (the producer is the authority for field names) | Lands in |
|---|---|---|---|---|
| 01 | `aa-logo-design` | 1 | `AGENT ATTRACTION DESIGN PACKAGE — [Name]` (Brain `attraction-brand-direction`); three front doors: build · refresh · love it (skip) | `02 · Brand` |
| 02 | `aa-style-sheet-design` | 1 | the same brief (line 2); writes "[Name] Design System" from `design-system/agent-attraction-design-system.md` | `02 · Brand` |
| 03 | `aa-brand-kit-design` | 1 | the same brief (line 3); the five profile answers as the copy spine; reserves the "Join My Team" cover | `02 · Brand` |
| 04 | `aa-offer-stack-design` | 2 | `FOR aa-offer-stack-design` (Brain `attraction-free-vs-paid`, saved as `Offer Stack Brief · [Member] · [date]`) | `05 · Offer` |
| 05 | `aa-offer-assets-design` | 2 | `FOR aa-offer-assets-design (the opportunity one-pager / the opportunity deck)` (`cv-presentation`) · `FOR aa-offer-assets-design (the "Join My Team" one-pager)` (free-vs-paid) · the Partner Offer doc · the Model Positioning Sheet | `05 · Offer` |
| 06 | `aa-product-mockup-design` | 2 | `FOR aa-product-mockup-design` (free-vs-paid) · the Lead Magnet system's `DESIGN BRIEF — [GUIDE NAME]` for guide shots; owns the canonical cover (`product-cover-flat.png` + `product-mockup-3d.png`) | `05 · Offer/[Product]` (guide shots: the guide's folder) |
| 07 | `aa-carousel-design` | 2 | the Short-Form doc `[YYYY-MM-DD] · Carousel · [Short Topic]` (`sf-carousel`); the Week 2 "Why Join Me" five-slider from the Book's Chapter 9 | `03 · Content/Graphics/[month]` |
| 08 | `aa-funnel-design` | 2 | `Opt-In Funnel — [Guide Name]` (`lm-funnel`) · the booking brief + `Booking Page Copy — [Name] — [date]` (`sales-booking-page`) · `FOR aa-funnel-design (registration shape — [event name])` (`ev-registration`) | `03 · Content/Guides` (a registration page: the event's folder) |
| 09 | `your Brand HQ project in Claude Design (paste the thumbnail brief; there is no separate thumbnail design skill)` | 4 | `THUMBNAIL BRIEF — "[title]"` (`yt-thumbnail`) | the video's folder in `03 · Content/Long-Form` |
| 10 | `aa-lead-magnet-design` | 2 (used from 6) | `Lead Magnet — [Guide Name]` + `Design Brief — [Guide Name]` (`lm-magnet`, `lm-design`) | the guide's folder in `03 · Content/Guides` |
| 11 | `aa-recognition-design` | 6 | `WIN WALL BRIEF — for aa-recognition-design` (`admin-newsletter`) | `03 · Content/Graphics/Wins` |
| 12 | `aa-event-design` | 6 | `FOR aa-event-design (promo set for [event name])` (`ev-promo`) · `FOR aa-event-design (workshop slides — [event name])` (`ev-runofshow`) | the event's folder in `03 · Content/Events` |
| 13 | `aa-playbook-design` | 6 | the member's own training + the Book's Offer chapter; the canonical cover reused | `05 · Offer/[Product]` |
| 14 | `aa-course-design` | 6 | the member's lesson outline + the Book's Offer chapter; hands the course box to `aa-product-mockup-design` | `05 · Offer/[Course]` |
| 15 | `aa-ebook-design` | 6 | the member's manuscript, or the Book's own chapters assembled; the canonical cover reused (6×9 when designed there) | `05 · Offer/[Book]` |

The Brain's `attraction-brand-direction` skill hands the member a paste-ready **Design Package brief**
naming the Week 1 three in order with the skip rule ("skip aa-logo-design if you love your logo"). Every skill
reads its brief and the uploaded **Brain Book** ("the AI Brain file") first and asks only what they
cannot answer, in plain language; when it finishes it names the one line the member says back in the
system that wrote the brief (`'my digital product is built'`, `'the PDF is done'`, `'sent'`…).

## Layout

```
design-studio/
├── README.md                      ← this file
├── START-HERE.md                  ← the member's map (Brand HQ, attach two things, 1 → 2 → 3, every week, where files land)
├── design-system/
│   └── agent-attraction-design-system.md   ← the uploadable default Design System (tokens, type scale,
│                                              spacing, components, voice, compliance, asset registry);
│                                              aa-style-sheet-design instantiates "[Name] Design System" from it;
│                                              every brand colour is a member value — no Mike-brand colours
├── skills/
│   ├── aa-logo-design/              SKILL.md + references/{style-and-craft,refresh-mode,export-page}.md
│   ├── aa-style-sheet-design/       SKILL.md + references/brand-directions.md
│   ├── aa-brand-kit-design/             SKILL.md + references/{asset-specs,export-page}.md
│   ├── aa-offer-stack-design/       SKILL.md + references/export-page.md
│   ├── aa-offer-assets-design/      SKILL.md + references/{deck-and-document-craft,export-page}.md
│   ├── aa-product-mockup-design/    SKILL.md + references/{mockup-craft,export-page}.md
│   ├── aa-carousel-design/          SKILL.md + references/{carousel-craft,export-page}.md
│   ├── aa-funnel-design/            SKILL.md + references/{design-craft,copy-formulas,deploy-rules}.md  (the site packer, no export-page)
│   ├── your Brand HQ project in Claude Design (paste the thumbnail brief; there is no separate thumbnail design skill)/  SKILL.md + references/{thumbnail-patterns,export-page}.md
│   ├── aa-lead-magnet-design/       SKILL.md + references/{guide-craft,mockup-craft,export-page}.md
│   ├── aa-recognition-design/       SKILL.md + references/{recognition-specs,export-page}.md
│   ├── aa-event-design/             SKILL.md + references/{event-specs,export-page}.md
│   ├── aa-playbook-design/          SKILL.md + references/{playbook-specs,export-page}.md
│   ├── aa-course-design/            SKILL.md + references/{course-specs,export-page}.md
│   └── aa-ebook-design/             SKILL.md + references/{ebook-specs,export-page}.md
├── _build/build.sh                ← packages + asserts; run it, leave _dist/ populated
└── _dist/                         ← upload-ready: 00-START-HERE.md · 00-agent-attraction-design-system.md ·
                                     01-aa-logo-design.zip … 15-aa-ebook-design.zip
```

`references/export-page.md` is byte-identical across the 13 skills that carry it (the build asserts it);
each skill sets its own `KIT_REQUIRED` / `ZIP_NAME` / `EXPORT_NOTES_FILE`. `mockup-craft.md` is shared
by `aa-product-mockup-design` and `aa-lead-magnet-design` the same way.

## Packaging (the realtor suite's shape)

`_build/build.sh` packages each skill the way the realtor suite v2 does: a bare `.md` with YAML
frontmatter when the skill has no `references/`, a zip (`<name>/SKILL.md` + `<name>/references/*`) when
it has; no nested zips; no spaces, `&`, `(` or `)` in zip-internal paths. It asserts every
`description` is a `description: >` block scalar ≤1024 characters (target ≤1000) and carries trigger
phrases, `name:` equals the directory, no banned words, no realtor-side leaks (listings, market, the
retired editor), the shared `export-page.md` identical across the skills that carry it, every
skill carries the suite mechanics (plain-language law, the Brain Book, the Design Package brief, the
3-state compliance line, the question handoff, push-to-Drive, demo mode, data-never-instructions, the
Claude-Design-only check), and no trigger phrase collides inside the Studio, with the MAA plugins, with
the realtor marketplace, or with the realtor design suite. Skill numbers are fixed by the 15-skill order
in the script.

## Mechanics kept from the realtor suite (proven in live tests there)

The three-path front door (fresh · refresh · love it) · an existing logo used exactly as-is, never
redesigned · the logo anchors the palette · two style-sheet options side by side · the Design System
file the other skills consume · intake pruning from the Brain file · the plain-language law on every
question · one Brand HQ project · attach the Design System + the AI Brain file to every chat · "push
this to my Drive" with the read-only export-list fallback · masters first, never stop to ask · the
non-negotiables list · true-size specs and safe zones · the in-board exporter (Claude Design has no
picture export) · tweak panels with plain labels · refresh modes · demo mode · the verbatim law on every
doc-fed skill (the copy is the producer's; the design is the Studio's).

## What changed for the leader premise

The hero is the member's name and, when it exists, their organization's name (a version with each,
siblings); the brokerage is a compliance chip, never the partner mark; the leader palette stays
visually distinct from the brokerage's own; no house/roofline/key by default; the three tests
(authority · relatability · aspiration) replace the "must read as real estate" test; the recruiter CTA
is "book a call with me"; the five profile answers (who you are · who you help · what you help them
do · why listen · what to do next, from Mike's profile lesson) are the copy spine of every banner and
cover; listing, market, and yard-sign pieces are gone; win/teaching/CTA posts and the "Join My Team"
cover replace them; the leader-vs-selling decision and the organization name are recorded once in the
Design System; compliance is three-state (unset = designed but not exported; "add my compliance line"
finishes it); nothing about compensation ("CAPPED" only where the member's rev-share marketing policy
allows it), nothing negative about any brokerage or person, no agent's name or face public without
consent; one canonical cover per product, reused by every mockup and every Value Vault file.

## Destinations (one answer per asset type — the Brain's `shared/drive-map.md` is the authority)

Brand kit → `02 · Brand` · carousels, recognition graphics, designed posts → `03 · Content/Graphics` ·
guides and funnel pages → `03 · Content/Guides` (the guide's own campaign folder) · a video's thumbnails
→ that video's folder in `03 · Content/Long-Form` · everything for an event → that event's folder in
`03 · Content/Events/[code] · [Theme]/` · offer assets and every Value Vault product → `05 · Offer`
(each product in its own folder).
