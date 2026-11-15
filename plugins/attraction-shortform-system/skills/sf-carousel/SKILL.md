---
name: sf-carousel
description: >
  Attraction carousels for Week 4 — swipe posts for agents when the member doesn't want to film: the
  "Why I Left My Brokerage" story (the old brokerage never named), pain-point carousels that
  teach a step of the member's own method, and myth-busting carousels, plus a LinkedIn PDF document
  post for team leaders and broker-owners. Writes the cover hook, the slide-by-slide copy, the CTA slide
  with one of the two keywords (GUIDE for the guide, the offer's word for the invitation), the captions,
  and saves ONE lean build sheet the member's Claude Design content skill turns into slides. Spec only —
  never renders a slide; the six kit posts are already designed. Trigger on: "attraction carousel",
  "carousel for agents", "why I left my brokerage carousel", "my why-I-left post", "pain-point carousel
  for agents", "myth-busting carousel for agents", "LinkedIn document post for team leaders", "a swipe
  post for agents", "I don't want to film an attraction post", or any non-video attraction post.
---

# Attraction Carousel (spec only)

The no-filming format. A written swipe post that an agent saves, shares, and — when it's the "Why I Left" story —
sees themselves in. The member gets the copy, in chat and as one lean build sheet; their Claude Design content skill
builds the slides from that sheet.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`). **Doctrine:**
`${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §5–§6, §8, §11 (lazy-load at Phase 2).

> **We map; we never design (house rules #3).** This skill outputs the *words and the build sheet* only. The sheet is
> read by the Design Studio's content skill (`aa-content-design` keys on the doc name and the band `THE DESIGN BRIEF
> FOR AA-CONTENT-DESIGN`); to the member it is always "your Claude Design content skill" — never the id. No Design
> Studio → the member pastes the sheet into Claude Design (claude.ai/design, or a Design canvas inside Cowork). If you ever feel tempted to render a slide — don't.

**Week 4 rules that bind every carousel** (the rewire brief, 2026-11-14 — where older text disagrees, these win):
- **The six kit posts are already designed** (chapter 7 of the Week 3 Kit; the finished graphics sit in the member's
  Offer folder): Post 1 the guide carousel · Post 2 five problems, five fixes · Post 3 my story · Post 4 what you get
  · Post 5 proof · Post 6 book the call. They are the Game Plan's first rows — "post, don't make". A request that IS
  one of them → *"that one's made — it's in your Offer folder; post it"*, never rewritten here. This skill writes the
  carousels that come after them.
- **Two keywords, never more.** `GUIDE` delivers the guide (`memory/magnets.md → ## Current magnet`); the offer's
  `Comment keyword:` (`identity/offer.md`) is the invitation. Both sit on `publishing.md`'s `Keyword:` line. No other
  word on a slide or in a caption, ever.
- **The call ask follows the law:** the person · their help · free · to run the method — never the brokerage, never
  compensation. Join register (`offer.md → Join-gated package allowed: yes` or `unknown`): *"If you want my help running
  this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."* Open register
  (`no`): *"I'll walk you through it, free, no strings."* The caption's last line is the kit's CALLS TO ACTION table
  (chapter 7 of the newest `exports/week3-kit-*.txt`), verbatim.
- **Scalable by design.** No slide or caption promises the member's time per partner — no in-person days beside the
  member, no chat group, no one-to-one calls, no "call me any time"; partners get recorded lessons, templates, the
  community, the weekly group call only when `operations.md` shows the member already runs one.
- **The whole method.** A pain-point carousel's fix is three steps of `offer.md → ## The framework` (or one page of the
  guide); the guide is the resource every ask points at.
- **The doc handed to Claude Design is a LEAN BUILD SHEET** (the owner, 2026-11-11): slide 1 … slide N with the final
  copy and the placeholders, the caption(s), the sizes, the brand pointer, the band kept but short. Strategy — why this
  hook, the rung, what to watch — lives in the chat reply and the content-log row, never in the doc.

Three jobs, three types:
- **"Why I Left My Brokerage"** — a **Story** carousel. The wall → the turning point → what the member built →
  who they help now. The former brokerage is never named ("a franchise", "an independent", "a team"); not one
  negative word about it or anyone there. The post is about the problem, never the company.
- **Pain-point** — **Authority / Perspective.** Names one of the five pains in the avatar's words, why it
  happens, and the fix the member actually uses.
- **Myth-busting** — **Perspective.** A belief that keeps agents stuck, why people believe it, the truth, the
  proof. Never a myth "about [named brokerage]" — a myth about the business.
Each has a **LinkedIn document-post** version (a PDF, 8–12 pages, bigger type) written for team leaders and
broker-owners when the member's avatars include them. The "Why I Left" story is the long form of the kit's Post 3 (My
story, five slides, already designed) — same spine, told in full; it never contradicts the kit's lines.

---

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first, then:
- `identity/content-pillars.md` — the pillars and their angles (written by the Game Plan inside setup; missing →
  "say 'set up my attraction short-form'" in one warm line)
- `memory/content-calendar.md` — a carousel row dated this week is the default topic
- `identity/publishing.md` — the two keywords (`Keyword: GUIDE · [the offer's word]`), what each opens, the LinkedIn
  clause of `Platforms` (on only when the avatars hold team leaders or broker-owners — never asked), `Content board:`
- `identity/avatars.md` — who it's for; their problem in their words; team leader / broker-owner present? (the one
  condition for the LinkedIn version)
- `identity/journey.md` — the three turning points + the `## Why join me` block (the Why-I-Left spine, if written)
- `identity/story-bank.md` — the real stories; the "why I left" story if it's there; stamp Used-where after
- `identity/positioning.md` — the one line "why I'm here"; what stays for the private call
- `identity/proof.md` — proof for the myth-busting truth and the pain-point fix (consent respected)
- `identity/offer.md` — `## The framework` (the method's steps — a pain-point carousel's fix), `## Content branches` (the
  angles), the `Comment keyword:` line (the invitation word), `Join-gated package allowed:` (the register of the call ask)
- `memory/magnets.md → ## Current magnet` — the guide (GUIDE): its title and pages; the resource every ask points at. No
  live guide yet → one warm line, *"say 'launch my lead magnet plugin' and your guide becomes what every post hands
  out"*; the ask falls back to the call line in the law's shape
- the newest `exports/week3-kit-*.txt` — chapter 7: the six post outlines (never rewritten here) and the CALLS TO ACTION
  table (the caption line · the story line · the DM reply) every ask quotes; chapter 3's one-breath statement for the
  Why I Left spine
- `identity/voice.md` + `identity/voice-samples.md` — tone + their written phrasing (carousels are read, not heard)
- `identity/brand-visual.md` — only to confirm the Design Package exists (the Week 3 brand chat); the build sheet
  points at it ("your Design Package brief") and never restates hex codes or fonts
- `identity/compliance.md` — the third law, three-state
- `memory/content-log.md` — avoid a recent carousel topic; which pillar is light
- `memory/ideas.md` (tag `shortform`) · `memory/objections.md` — a myth or a pain the member heard this month
- `memory/content-performance.md` — what worked (from `sf-analytics`); skip if it doesn't exist yet

**Read the Brain; never re-ask what it knows.** `~/attraction-brain/` missing → pull with
`attraction-brain-sync`; only if the cloud has none, "set up my attraction brain."

## Step 2 — Read the reference file
`references/carousel-guide.md` — the three structures, the LinkedIn version, the lean build sheet, what gets saved.

---

## Phase 1 — Pick the type + the job
If the member named it, go. If not, recommend ONE (house rules #8): the **Why I Left** story if their journey
hasn't been posted yet and `journey.md` has the turning points (it's the most-shared attraction post a leader can make);
a **pain-point** on the avatar's #1 pain if they're light on Authority; a **myth-busting** one if an objection
came up this month. One line of why, then the backups. Decide the **rung**: GUIDE (comment, the guide) for
pain-point and myth-busting; for Why I Left, "save this and send it to an agent who's where I was" on the last slide
and the call line in the caption (the kit's story close — *"If any of this sounds like your year, message me."* — then
*"Want my help running this, free? [the booking line]"*). One line, a statement, never a menu and never a Yes line: *"I'm writing [the type] —
[why]; name another any time."* — then write it.

## Phase 2 — Write the carousel (the words), then the lean build sheet
**Read `references/carousel-guide.md`.** Write the copy first, as clean copyable text:
- **COVER (slide 1)** — the hook: the agent's problem or the surprise, in their words. Bold, short. No logo-only
  cover, no "swipe →" as the whole slide.
- **SLIDE 2 → N−1** — **7–9 slides total.** One idea per slide, a header line + 1–2 lines max, momentum slide to
  slide; the last content slide pays off the cover's promise. Why I Left follows the story structure in the
  guide; pain-point (the fix = three steps of `## The framework`) and myth-busting follow theirs.
- **FINAL SLIDE — the CTA** — one rung, one of the two keywords: *"Comment **GUIDE** and I'll send you [the guide, in
  three words]."* / *"Save this. Send it to an agent who's where I was."* (Why I Left). Never the model, never numbers,
  never a third word.
- **THE LINKEDIN VERSION** (only when `identity/avatars.md` includes team leaders or broker-owners — the LinkedIn
  clause of `Platforms` is on; never asked) —
  the same story reframed for a leader who carries a team ("adult daycare", retention, leverage): 8–12 pages,
  one idea per page, bigger type; plus the **LinkedIn post copy** (150–200 words, a first line that stands on
  its own, no hashtag wall, the ask = "message me" or "comment GUIDE" typed in a reply — LinkedIn has no comment
  automation).

**Then the LEAN BUILD SHEET** — the one doc the member's Claude Design content skill reads (`references/carousel-guide.md`
→ "The lean build sheet" has the exact block order). It carries ONLY: one header line (`THE BRIEF` — type · pillar ·
for whom · story used · rung + keyword, as facts), the slides in order with their final copy and `[placeholders]`
(`COVER (slide 1)` · `SLIDE 2` … `FINAL SLIDE — the CTA`), `THE LINKEDIN VERSION` when written, the band
`THE DESIGN BRIEF FOR AA-CONTENT-DESIGN` — five short lines: the sizes (Instagram 1080 by 1350; the LinkedIn PDF, one
slide per page) · which slide is the hook and which the CTA · the brand pointer ("your Design Package brief") · the
logo and brokerage line as `compliance.md` requires · the stamp — then the `INSTAGRAM + FACEBOOK` block, the `LINKEDIN`
block and `COMPLIANCE`. **Never in the doc:** why this hook, why this rung, what to watch for, hex codes, font names,
the avatar's backstory, the research — strategy goes in the chat reply (Phase 5) and the content-log row (Phase 6).
Words only — never a rendered example.

## Phase 3 — Captions (Instagram + Facebook; LinkedIn post)
Read `${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md` and produce the **Instagram +
Facebook** block (caption + 3–5 hashtags + the FB tweak) whose last line is the kit's CALLS TO ACTION caption line,
verbatim — the guide: *"Comment GUIDE and I'll send you [the guide, in three words]."*; the call (Why I Left, Proof):
*"Want my help running this, free? [the booking line]"*. (Carousels aren't a TikTok/Shorts format — skip those.) The
LinkedIn post copy comes from Phase 2.

## Phase 4 — Compliance pass (third law, three-state)
the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`): `unset`
→ the spec stays in chat as a private draft with the plain line; `set` → apply + remind once; `confirmed` →
apply. Apply: brokerage name/license as the file says; **the two cardinal rules** (`03-model-positioning/13`) —
read the Why I Left back slide by slide and remove anything that characterizes the old brokerage or anyone
there; former brokerage unnamed; no compensation; no earnings; no "#1/best" without a source; a named agent only
with consent; any real-estate example fair-housing safe.

## Phase 5 — Deliver + hand to design
In chat, one clean copy-paste package — the slides, the final slide, the LinkedIn version (if any), the caption(s) —
followed by **the strategy, three lines, chat only:** why this hook (the pain or the surprise it names) · the rung and
why (GUIDE for the guide; the call line where the piece earns it) · what to watch (saves and shares for a story, GUIDE
comments for a teach, DMs for the call). Close with the hand-off, in plain words:
> "Here's your carousel. Open your Claude Design content skill, upload the build sheet I saved (Content → Graphics →
> [month]) and say **'design my carousel'** — it builds the slides in your brand. Then post with the caption below.
> Say 'another carousel' any time."
If a posting tool is connected (`identity/publishing.md`), offer to schedule it once the slides exist, per
`${CLAUDE_PLUGIN_ROOT}/shared/publishing-guide.md` (carousels usually take the hybrid path) — only with explicit
approval. Offer the content board (house rules #10): Format `Carousel`, status `Scripted` until the slides exist.

## Phase 6 — Save + log + push
1. **Save the lean build sheet** per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` — rendered `.docx` to
   `03 · Content/Graphics/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Carousel · [Short Topic]` (the name is what the
   Claude Design content skill keys on — unchanged). The sheet, nothing else: no strategy section.
2. **Log it:** append one row (two if a LinkedIn version was written) to `~/attraction-brain/memory/content-log.md`
   in the locked shape — the strategy rides in the Topic / hook cell, one clause each:
   `| [date] | Instagram · Facebook | carousel | [Pillar] | [carousel · type] [cover hook] — why: [the pain or surprise it names] · watch: [saves / GUIDE comments / DMs] | [avatar] | [story hook or —] | [rung · GUIDE or the offer's word] | Scripted | |`
   `| [date] | LinkedIn | carousel | [Pillar] | [LinkedIn doc] [cover hook] — why: … · watch: replies | [team leader / broker-owner] | … | DM · message me | Scripted | |`
3. **Stamp** the story's `Used-where`; flip any `ideas.md` row used to `used`. **Push** (write → push → verify) through
   `attraction-brain-sync` the moment the row is written — every write pushes immediately; the push re-renders the
   member's Brain Board.
Then: *"Saved your build sheet to your workspace (Content → Graphics → [month]) and logged the carousel — your Brain
Board shows it."*

---

## Quality checklist
- [ ] Brain read; nothing re-asked; pillars from `content-pillars.md`
- [ ] **No design rendered** — the words in chat + ONE lean build sheet (slides · caption · sizes · brand pointer · the
      band kept short); strategy in the chat reply and the log row, never in the doc; a kit post never rewritten
- [ ] Cover is the agent's problem or the surprise; 7–9 slides; one idea per slide; skimmable; pays off the cover
- [ ] Why I Left: the former brokerage unnamed, not one negative word, the point is the problem and the turn
- [ ] Pain-point / myth-busting: real fix, real truth, real proof (consent) — nothing invented
- [ ] One rung on the final slide with one of the two keywords (GUIDE · the offer's word); the caption's last line is
      the kit's CALLS TO ACTION line; the call ask in the law's shape; never the model or the money
- [ ] Scalable: no slide promises the member's time per partner; a pain-point fix = three steps of the framework
- [ ] LinkedIn version written when an avatar is a team leader / broker-owner; post copy ≤200 words
- [ ] The build sheet points at "your Design Package brief" — no hex codes or font names restated
- [ ] Compliance three-state applied; cardinal rules read back slide by slide
- [ ] Saved to `03 · Content/Graphics` under the unchanged doc name, logged in the locked shape, pushed at once
