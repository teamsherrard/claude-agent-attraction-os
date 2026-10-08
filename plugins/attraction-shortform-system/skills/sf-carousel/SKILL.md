---
name: sf-carousel
description: >
  Attraction carousels — swipe posts for agents when the member doesn't want to film: the "Why I Left My
  Brokerage" story (the old brokerage never named, no digs), pain-point carousels, and myth-busting carousels,
  plus a LinkedIn PDF document-post version for team leaders and broker-owners. Writes the cover hook, the
  slide-by-slide copy, the CTA slide with the keyword, the Instagram + Facebook caption and the LinkedIn post,
  and a design brief handed to aa-carousel-design by name. Spec only — never renders a slide. Trigger on: "attraction
  carousel", "carousel for agents", "why I left my brokerage carousel", "my why-I-left post", "pain-point
  carousel for agents", "myth-busting carousel for agents", "LinkedIn document post for team leaders", "a
  swipe post for agents", "I don't want to film an attraction post", or any non-video attraction post.
---

# Attraction Carousel (spec only)

The no-filming format. A written swipe post that an agent saves, shares, and — when it's the "Why I Left" story —
sees themselves in. The member gets the copy and a design brief; the Design Studio builds the slides.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`). **Doctrine:**
`${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §5–§6, §8, §11 (lazy-load at Phase 2).

> **We map; we never design (house rules #3).** This skill outputs the *words and the brief* only. The brief is
> handed to **`aa-carousel-design`** (Claude Design) by name — or, if the Design Studio isn't installed, the member
> pastes the copy into claude.ai/design. If you ever feel tempted to render a slide — don't.

Three jobs, three types:
- **"Why I Left My Brokerage"** — a **Story** carousel. The wall → the turning point → what the member built →
  who they help now. The former brokerage is never named ("a franchise", "an independent", "a team"); not one
  negative word about it or anyone there. The post is about the problem, never the company.
- **Pain-point** — **Authority / Perspective.** Names one of the five pains in the avatar's words, why it
  happens, and the fix the member actually uses.
- **Myth-busting** — **Perspective.** A belief that keeps agents stuck, why people believe it, the truth, the
  proof. Never a myth "about [named brokerage]" — a myth about the business.
Each has a **LinkedIn document-post** version (a PDF, 8–12 pages, bigger type) written for team leaders and
broker-owners when the member's avatars include them.

---

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first, then:
- `identity/content-pillars.md` — the pillars (missing → send to `sf-setup` in one warm line)
- `identity/publishing.md` — the keyword, what it opens, platforms (is LinkedIn on the list?)
- `identity/avatars.md` — who it's for; their problem in their words; team leader / broker-owner present?
- `identity/journey.md` — the three beats + the `## Why join me` block (the Why-I-Left spine, if written)
- `identity/story-bank.md` — the real stories; the "why I left" story if it's there; stamp Used-where after
- `identity/positioning.md` — the one line "why I'm here"; what stays for the private call
- `identity/proof.md` — proof for the myth-busting truth and the pain-point fix (consent respected)
- `identity/offer.md` — the resource for the Resource rung (`seeds` → the free thing they give today / "book a call")
- `identity/voice.md` + `identity/voice-samples.md` — tone + their written phrasing (carousels are read, not heard)
- `identity/brand-visual.md` — colours, fonts, feel, logo state → the design brief, in words
- `identity/compliance.md` — the third law, three-state
- `memory/content-log.md` — avoid a recent carousel topic; which pillar is light
- `memory/ideas.md` (tag `shortform`) · `memory/objections.md` — a myth or a pain the member heard this month
- `memory/content-performance.md` — what worked (from `sf-analytics`); skip if it doesn't exist yet

**Read the Brain; never re-ask what it knows.** `~/attraction-brain/` missing → pull with
`attraction-brain-sync`; only if the cloud has none, "set up my attraction brain."

## Step 2 — Read the reference file
`references/carousel-guide.md` — the three structures, the LinkedIn version, the design brief, what gets saved.

---

## Phase 1 — Pick the type + the job
If the member named it, go. If not, recommend ONE (house rules #8): the **Why I Left** story if their journey
hasn't been posted yet and `journey.md` has the beats (it's the most-shared attraction post a leader can make);
a **pain-point** on the avatar's #1 pain if they're light on Authority; a **myth-busting** one if an objection
came up this month. One line of why, then the backups. Decide the **rung**: the keyword (Comment / DM) for
pain-point and myth-busting; "save this and send it to an agent who needs it" or "DM me 'call'" for Why I Left.
Confirm in one friendly line — *"your turn"*.

## Phase 2 — Build the carousel spec
**Read `references/carousel-guide.md`.** Produce, as clean copyable text:
- **THE BRIEF** — type · pillar · for whom · story used · rung + keyword.
- **COVER (slide 1)** — the hook: the agent's problem or the surprise, in their words. Bold, short. No logo-only
  cover, no "swipe →" as the whole slide.
- **SLIDE 2 → N−1** — **7–9 slides total.** One idea per slide, a header line + 1–2 lines max, momentum slide to
  slide; the last content slide pays off the cover's promise. Why I Left follows the story structure in the
  guide; pain-point and myth-busting follow theirs.
- **FINAL SLIDE — the CTA** — one rung, the keyword where it fits: *"Comment **PARTNER** and I'll send you what I
  built."* / *"Save this. Send it to an agent who's where I was."* Never the model, never numbers.
- **THE LINKEDIN VERSION** (when LinkedIn is on their platforms or an avatar is a team leader / broker-owner) —
  the same story reframed for a leader who carries a team ("adult daycare", retention, leverage): 8–12 pages,
  one idea per page, bigger type; plus the **LinkedIn post copy** (150–200 words, a first line that stands on
  its own, no hashtag wall, the ask = "message me" or the keyword — LinkedIn has no comment automation).
- **THE DESIGN BRIEF FOR AA-CAROUSEL-DESIGN** — in words: the slide count and sizes (Instagram 4:5; LinkedIn document
  PDF), which slide is the hook and which is the CTA, the colours / fonts / feel from `brand-visual.md` (hex and
  names, exactly as the file has them — never invented), the logo rule, where the brokerage name goes if
  compliance requires it. Words only — never a rendered example.

## Phase 3 — Captions (Instagram + Facebook; LinkedIn post)
Read `${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md` and produce the **Instagram +
Facebook** block (caption + 3–5 hashtags + the FB tweak) with the CTA line carrying the keyword. (Carousels aren't
a TikTok/Shorts format — skip those.) The LinkedIn post copy comes from Phase 2.

## Phase 4 — Compliance pass (third law, three-state)
the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`): `unset`
→ the spec stays in chat as a private draft with the plain line; `set` → apply + remind once; `confirmed` →
apply. Apply: brokerage name/license as the file says; **the two cardinal rules** (`03-model-positioning/13`) —
read the Why I Left back slide by slide and remove anything that characterizes the old brokerage or anyone
there; former brokerage unnamed; no compensation; no earnings; no "#1/best" without a source; a named agent only
with consent; any real-estate example fair-housing safe.

## Phase 5 — Deliver + hand to design
One clean, copy-paste package: the slides, the final slide, the LinkedIn version (if any), the caption(s), the
design brief. Close with the hand-off, by name:
> "Here's your carousel. Say **'design my carousel'** and the Design Studio (`aa-carousel-design`) builds the slides in
> your brand from this brief — or paste the slides into claude.ai/design yourself. Then post with the caption
> below. Want another one?"
If a posting tool is connected (`identity/publishing.md`), offer to schedule it once the slides exist, per
`${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` (carousels usually take the hybrid path) — only with explicit
approval. Offer the content board (house rules #10), status `Scripted` until the slides exist.

## Phase 6 — Save + log + push
1. **Save the doc** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` — rendered `.docx` to
   `03 · Content/Graphics/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Carousel · [Short Topic]` (this is the doc
   `aa-carousel-design` reads).
2. **Log it:** append one row (two if a LinkedIn version was written) to `~/attraction-brain/memory/content-log.md`
   in the locked shape:
   `| [date] | Instagram · Facebook | carousel | [Pillar] | [carousel · type] [cover hook] | [avatar] | [story hook or —] | [rung · KEYWORD] | Scripted | |`
   `| [date] | LinkedIn | carousel | [Pillar] | [LinkedIn doc] [cover hook] | [team leader / broker-owner] | … | DM · message me | Scripted | |`
3. **Stamp** the story's `Used-where`; flip any `ideas.md` row used to `used`. **Push** (write → push → verify).
Then: *"Saved your carousel to your workspace (Content → Graphics → [month]) and logged it."*

---

## Quality checklist
- [ ] Brain read; nothing re-asked; pillars from `content-pillars.md`
- [ ] **No design rendered** — copy + a brief handed to `aa-carousel-design` by name
- [ ] Cover is the agent's problem or the surprise; 7–9 slides; one idea per slide; skimmable; pays off the cover
- [ ] Why I Left: the former brokerage unnamed, not one negative word, the point is the problem and the turn
- [ ] Pain-point / myth-busting: real fix, real truth, real proof (consent) — nothing invented
- [ ] One rung on the final slide; the keyword where it fits; never the model or the money
- [ ] LinkedIn version written when an avatar is a team leader / broker-owner; post copy ≤200 words
- [ ] Design brief uses `brand-visual.md` values exactly, in words
- [ ] Compliance three-state applied; cardinal rules read back slide by slide
- [ ] Saved to `03 · Content/Graphics`, logged in the locked shape, pushed
