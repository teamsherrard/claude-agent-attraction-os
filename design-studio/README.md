# Design Studio — a Claude Design skill set, not a plugin

Claude Design (claude.ai/design) cannot run Cowork plugins; it accepts uploaded skill files. This
folder is the Agent Attraction Design Studio: the 10 `aa-…-design` skills that build and run the member's
LEADER brand (the brand agents follow — never a listing brand), plus the **Agent Attraction Design
System** every skill reads. Plan: `docs/plans/02-agent-attraction-os-master-gameplan.md` §3. House
rules: `docs/plans/BUILD-BRIEF.md`. Recycled from the realtor Claude Design suite v2 (read-only, on the
Desktop), with the realtor premise replaced by the leader premise. **All 10 are built and packaged** (the thumbnail skill was deleted: `yt-thumbnail` writes the brief, pasted into the member's Brand HQ project; on 2026-10-10 the user's decision took the set from 14 to 10 — three kit skills replaced eight single-piece skills, and the video kit joined).

## The ten skills, by the week the member uploads them

| # | Skill | Week | Brief / doc it consumes (the producer is the authority for field names) | Lands in |
|---|---|---|---|---|
| 01 | `aa-logo-design` | 1 | `AGENT ATTRACTION DESIGN PACKAGE — [Name]` (Brain `attraction-brand-direction`); three front doors: build · refresh · love it (skip) | `02 · Brand` |
| 02 | `aa-style-sheet-design` | 1 | the same brief (line 2); writes "[Name] Design System" from `design-system/agent-attraction-design-system.md` | `02 · Brand` |
| 03 | `aa-brand-kit-design` | 1 | the same brief (line 3); the five profile answers as the copy spine; reserves the "Join My Team" cover | `02 · Brand` |
| 04 | `aa-offer-kit-design` | 2 | six pieces, one skill: `FOR aa-offer-kit-design (the product mockup)` · `(the offer stack)` · `(the "Join My Team" one-pager)` (Brain `attraction-free-vs-paid`, saved as `Offer Stack Brief · [Member] · [date]`) · `FOR aa-offer-kit-design (the opportunity one-pager / the opportunity deck)` (`cv-presentation`) · the Partner Offer doc · the Model Positioning Sheet · the Lead Magnet system's `DESIGN BRIEF — [GUIDE NAME]` for guide shots; owns the canonical cover (`product-cover-flat.png` + `product-mockup-3d.png`). Kit run "design my offer kit": the cover and the stack object as masters, one checkpoint, then the rest | `05 · Offer` (the mockup in `05 · Offer/[Product]`; guide shots in the guide's folder) |
| 05 | `aa-lead-magnet-design` | 2 | `Lead Magnet — [Guide Name]` + `Design Brief — [Guide Name]` (`lm-magnet`, `lm-design`) | the guide's folder in `03 · Content/Guides` |
| 06 | `aa-funnel-design` | 2 | `Opt-In Funnel — [Guide Name]` (`lm-funnel`) · the booking brief + `Booking Page Copy — [Name] — [date]` (`sales-booking-page`) · `FOR aa-funnel-design (registration shape — [event name])` (`ev-registration`) | `03 · Content/Guides` (a registration page: the event's folder) |
| 07 | `aa-content-design` | 2 (used every week after) | two families, one skill: carousels from the Short-Form doc `[YYYY-MM-DD] · Carousel · [Short Topic]` (`sf-carousel`; its band `THE DESIGN BRIEF FOR AA-CONTENT-DESIGN`), the Week 2 "Why Join Me" five-slider from the Book's Chapter 9, an event's carousel from `FOR aa-event-design (promo set for …)` (`ev-promo`); recognition from `WIN WALL BRIEF — for aa-content-design` (`admin-newsletter`). Kit run "design my content" only when one brief covers several pieces | `03 · Content/Graphics/[month]` (recognition: `Graphics/Wins`; an event carousel: the event's folder) |
| 08 | `aa-video-kit-design` | 3 (any time after the style sheet) | the member's Design System + the Brain Book (UVP, the offer's comment keyword, the live magnet's name and keyword, the booking line, the compliance lines); no brief — the editor's Video Brand Kit v3 contract (`plugins/realtor-riverside-editor/shared/brand-wiring.md`: the canonical names, the zones, the eight `cta_pack` keys, `video-brand-spec.md`) is the spec. Upload with the Riverside plugin; the member says "register my video brand kit" in Cowork afterwards | `02 · Brand/Video Brand Kit` |
| 09 | `aa-event-design` | 6 | `FOR aa-event-design (promo set for [event name])` (`ev-promo`) · `FOR aa-event-design (workshop slides — [event name])` (`ev-runofshow`) | the event's folder in `03 · Content/Events` |
| 10 | `aa-value-vault-design` | 6 | four pieces, one skill: the member's own training (playbook · workbook · worksheet), lesson outline (course; hands the course box to the offer kit), manuscript or the Book's own chapters (ebook) — the canonical cover reused — and the partner onboarding roadmap from the Partner Offer's "First 30 days as a partner" table + the Book's How You Operate chapter (`FOR aa-offer-kit-design (the product mockup)` names the product). Kit run "design my value vault": the cover and the first inside page as masters, one checkpoint, then the rest | `05 · Offer/[Product]` (the roadmap: `05 · Offer/Onboarding`) |

The Brain's `attraction-brand-direction` skill hands the member a paste-ready **Design Package brief**
naming the Week 1 three in order with the skip rule ("skip aa-logo-design if you love your logo"). Every skill
reads its brief and the uploaded **Brain Book** ("the AI Brain file") first and asks only what they
cannot answer, in plain language; when it finishes it names the one line the member says back in the
system that wrote the brief (`'my digital product is built'`, `'the PDF is done'`, `'sent'`, `'register
my video brand kit'`…).

**The kit pattern (the three merged skills).** One directory, one SKILL.md holding the shared rules
(Design System first, the Brain Book, compliance, the verbatim law, exports, folders, the five golden
rules), a MODE ROUTER that never asks a menu when the phrase or the brief already names the piece, and
a KIT RUN that builds the pieces in a fixed order with ONE member checkpoint after the masters (the
offer kit: the canonical product cover and the transparent stack object; the content kit: the
carousel's cover + slide 2 and the first Win Wall post; the Value Vault: the cover and the first inside
page), then everything else without stopping. Each piece's craft lives in `references/<piece>.md`,
moved verbatim from the retired skill it came from, so a piece stays callable alone by its own phrase.

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
│   ├── aa-brand-kit-design/         SKILL.md + references/{asset-specs,export-page}.md
│   ├── aa-offer-kit-design/         SKILL.md + references/{product-mockup,mockup-craft,offer-stack,offer-assets,deck-and-document-craft,export-page}.md
│   ├── aa-lead-magnet-design/       SKILL.md + references/{guide-craft,mockup-craft,export-page}.md
│   ├── aa-funnel-design/            SKILL.md + references/{design-craft,copy-formulas,deploy-rules}.md  (the site packer, no export-page)
│   ├── aa-content-design/           SKILL.md + references/{carousel,carousel-craft,recognition,recognition-specs,export-page}.md
│   ├── aa-video-kit-design/         SKILL.md + references/{video-kit-specs,export-page}.md
│   ├── aa-event-design/             SKILL.md + references/{event-specs,export-page}.md
│   └── aa-value-vault-design/       SKILL.md + references/{playbook,playbook-specs,course,course-specs,ebook,ebook-specs,onboarding-roadmap,export-page}.md
├── _build/build.sh                ← packages + asserts; run it, leave _dist/ populated
└── _dist/                         ← upload-ready: 00-START-HERE.md · 00-agent-attraction-design-system.md ·
                                     01-aa-logo-design.zip … 10-aa-value-vault-design.zip
```

`references/export-page.md` is byte-identical across the 8 skills that carry it (the build asserts it);
each skill sets its own `KIT_REQUIRED` / `ZIP_NAME` / `EXPORT_NOTES_FILE` (the video kit's `EXPORT_NOTES_FILE`
is `video-brand-spec.md`, the file the editor reads). `mockup-craft.md` is shared by `aa-offer-kit-design`
and `aa-lead-magnet-design` the same way.

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
the realtor marketplace, or with the realtor design suite. Skill numbers are fixed by the 10-skill order
in the script.

## Mechanics kept from the realtor suite (proven in live tests there)

The three-path front door (fresh · refresh · love it) · an existing logo used exactly as-is, never
redesigned · the logo anchors the palette · two style-sheet options side by side · the Design System
file the other skills consume · intake pruning from the Brain file · the plain-language law on every
question · one Brand HQ project · attach the Design System + the AI Brain file to every chat · "push
this to my Drive" with the read-only export-list fallback · masters first, never stop to ask (the kit
skills stop exactly once, after the masters) · the
non-negotiables list · true-size specs and safe zones · the in-board exporter (Claude Design has no
picture export) · tweak panels with plain labels · refresh modes · demo mode · the verbatim law on every
doc-fed skill (the copy is the producer's; the design is the Studio's) · the Video Brand Kit v3.3 sync
contract with the Riverside editor (canonical names, zones, transparent full-canvas overlays, preview
sheets, the spec file, the eight CTA-pack keys).

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
allows it; the video kit carries no production or income figure anywhere), nothing negative about any
brokerage or person, no agent's name or face public without consent; one canonical cover per product,
reused by every mockup and every Value Vault file; the video kit's CTA pack speaks to agents (the
offer's keyword, the guide, the partner call), never to clients.

## Destinations (one answer per asset type — the Brain's `shared/drive-map.md` is the authority)

Brand kit → `02 · Brand` · the video kit → `02 · Brand/Video Brand Kit` · carousels, recognition
graphics, designed posts → `03 · Content/Graphics` · guides and funnel pages → `03 · Content/Guides`
(the guide's own campaign folder) · a video's thumbnails → that video's folder in `03 · Content/Long-Form`
· everything for an event → that event's folder in `03 · Content/Events/[code] · [Theme]/` · the offer
kit and every Value Vault product → `05 · Offer` (each product in its own folder; the onboarding
roadmap in `05 · Offer/Onboarding`).
