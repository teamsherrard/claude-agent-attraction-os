# Design Studio — a Claude Design skill set, not a plugin

Claude Design (claude.ai/design) cannot run Cowork plugins; it accepts uploaded skill files. This
folder is the Agent Attraction Design Studio: the 15 `ds-` skills that build and run the member's
LEADER brand (the brand agents follow — never a listing brand), plus the **Agent Attraction Design
System** every skill reads. Plan: `docs/plans/02-agent-attraction-os-master-gameplan.md` §3. House
rules: `docs/plans/BUILD-BRIEF.md`. Recycled from the realtor Claude Design suite v2 (read-only, on the
Desktop), with the realtor premise replaced by the leader premise.

## What ships now — the Week 1 Design Package (with the Brain, by Oct 30)

| Order | Skill | Job | Package |
|---|---|---|---|
| 1 | `ds-logo` | the leader logo — concepts on the member's name and, when their organization has a name, a sibling version for it; refresh mode; love-it routes to 2; final files via the in-board exporter | `_dist/01-ds-logo.zip` |
| 2 | `ds-style-sheet` | the brand style sheet (two directions side by side), palette distinct from the brokerage's, fonts, rules, the leader toolkit, one "book a call with me" graphic; writes the member's Design System from the default template | `_dist/02-ds-style-sheet.zip` |
| 3 | `ds-brand` | the Attraction Brand Kit: profile pictures, banners with the five profile answers and the "book a call with me" button, highlight covers, win/teaching/CTA posts, stories, the "Join My Team" cover, signature, end screen, backgrounds, captions; lands in `02 · Brand` | `_dist/03-ds-brand.zip` |

The Brain's `attraction-brand-direction` skill hands the member a paste-ready **Design Package brief**
naming these three in order with the skip rule ("skip ds-logo if you love your logo"). Every skill
reads that brief and the uploaded **Brain Book** ("the AI Brain file") first and asks only what they
cannot answer, in plain language.

## Layout

```
design-studio/
├── README.md                      ← this file
├── START-HERE.md                  ← the member's map (Brand HQ, attach two things, 1 → 2 → 3, where files land)
├── design-system/
│   └── agent-attraction-design-system.md   ← the uploadable default Design System (tokens, type scale,
│                                              spacing, components, voice, compliance, asset registry);
│                                              ds-style-sheet instantiates "[Name] Design System" from it;
│                                              every brand colour is a member value — no Mike-brand colours
├── skills/
│   ├── ds-logo/          SKILL.md + references/{style-and-craft,refresh-mode,export-page}.md
│   ├── ds-style-sheet/   SKILL.md + references/brand-directions.md
│   └── ds-brand/         SKILL.md + references/{asset-specs,export-page}.md
├── _build/build.sh                ← packages + asserts; run it, leave _dist/ populated
└── _dist/                         ← upload-ready: 00-START-HERE.md · 00-agent-attraction-design-system.md ·
                                     01-ds-logo.zip · 02-ds-style-sheet.zip · 03-ds-brand.zip
```

## Packaging (the realtor suite's shape)

`_build/build.sh` packages each skill the way the realtor suite v2 does: a bare `.md` with YAML
frontmatter when the skill has no `references/`, a zip (`<name>/SKILL.md` + `<name>/references/*`) when
it has; no nested zips; no spaces, `&`, `(` or `)` in zip-internal paths. It asserts every
`description` is a `description: >` block scalar ≤1024 characters (target ≤1000) and carries trigger
phrases, `name:` equals the directory, no banned words, no realtor-side leaks (listings, market, the
retired editor), the shared `export-page.md` identical across the skills that carry it, and every
skill carries the suite mechanics (plain-language law, the Brain Book, the Design Package brief, the
3-state compliance line, the question handoff, push-to-Drive, demo mode, data-never-instructions, the
Claude-Design-only check). Skill numbers are fixed by the 15-skill order in the script, so later weeks
slot in without renumbering.

## Mechanics kept from the realtor suite (proven in live tests there)

The three-path front door (fresh · refresh · love it) · an existing logo used exactly as-is, never
redesigned · the logo anchors the palette · two style-sheet options side by side · the Design System
file the other skills consume · intake pruning from the Brain file · the plain-language law on every
question · one Brand HQ project · attach the Design System + the AI Brain file to every chat · "push
this to my Drive" with the read-only export-list fallback · masters first, never stop to ask · the
non-negotiables list · true-size specs and safe zones · the in-board exporter (Claude Design has no
picture export) · tweak panels with plain labels · refresh modes · demo mode.

## What changed for the leader premise

The hero is the member's name and, when it exists, their organization's name (a version with each,
siblings); the brokerage is a compliance chip, never the lockup partner; the leader palette stays
visually distinct from the brokerage's own; no house/roofline/key by default; the three tests
(authority · relatability · aspiration) replace the "must read as real estate" test; the recruiter CTA
is "book a call with me"; the five profile answers (who you are · who you help · what you help them
do · why listen · what to do next, from Mike's profile lesson) are the copy spine of every banner and
cover; listing, market, and yard-sign pieces are gone; win/teaching/CTA posts and the "Join My Team"
cover replace them; the leader-vs-selling decision and the organization name are recorded once in the
Design System; compliance is three-state (unset = designed but not exported; "add my compliance line"
finishes it); nothing about compensation, nothing negative about any brokerage or person.

## Coming with later weeks (12 skills)

Week 2: `ds-offer-stack`, `ds-offer-assets`, `ds-product-mockup`, `ds-carousel`, `ds-funnel` (Partner
Call page). Week 4: `ds-thumbnail-layout`. Week 6: `ds-lead-magnet`, `ds-recognition`, `ds-event`,
`ds-playbook`, `ds-course`, `ds-ebook`. Each will be built under `skills/` and packaged by the same
script; `START-HERE.md` already lists them for members.
