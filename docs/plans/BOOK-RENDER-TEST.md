# Brain Book render test — what the spec + renderer actually produce (Agent N)

*Date: 2026-10-08 · Plugin: `attraction-ai-brain` v0.1.0 · Spec: `plugins/attraction-ai-brain/shared/brain-book-spec.md` · Renderer: `plugins/attraction-ai-brain/shared/render_doc.py` (python-docx 1.2.0 present on this Mac) · Nothing under `plugins/` was touched.*

**The question:** the previous cohort's biggest failure was broken documents, sometimes 2–3 pages. The bar is a Brain Book of 10+ pages of real value. Does the current spec + renderer, fed a properly built Brain, actually produce that — and if not, what exactly changes?

**Headline:** with a complete demo Brain, the renderer produces an estimated **43–57-page** Book (16,005 words, 18 chapters, 26 tables, 22 insight callouts, a linked 22-row contents page, zero TOC warnings, no raw markup). The same Brain rendered the way **Setup Phase 8 would render it at the end of Week 1** (research skipped, Week 2–3 files not yet built) still produces an estimated **34–38 pages** (9,383 words). The renderer is not the 2–3-page problem. The spec has three concrete defects that a real build will hit (one of them a guaranteed gate FAIL on every complete Brain), and the most likely remaining cause of a 2–3-page document is upstream of both — a truncated or summarized structured-text assembly that the renderer cannot detect. Fixes below.

Open the results: `docs/demo/📕 Taylor Brooks's Agent Attraction Brain Book — DEMO — 2026-10-08.docx` (the full demo), `docs/demo/📕 Taylor Brooks's Agent Attraction Brain Book — DEMO (Week 1 first run) — 2026-10-08.docx` (the Phase 8 state), `docs/demo/🎯 Taylor Brooks's 90-Day Attraction Scorecard — DEMO — 2026-10-08.docx`. The demo Brain itself is at `docs/demo/taylor-brooks/attraction-brain/` (34 files, template-exact); the renderer inputs and the measurement script are in its `exports/` folder so the render can be reproduced in one command.

---

## 1. Method

1. **Built a complete demo Brain** for the house demo world — Taylor Brooks · Real Broker · Austin, TX · licensed 2021 (6th year) · former high-school teacher · the open-house + Sunday follow-up routine · 2 agents today (Priya Nair, Marcus D.) · goal 25 in 12 months — following `references/brain-template/attraction-brain/` file-for-file (20 identity files, 13 memory files, `brain.md`, `config.md` with `Demo brain: yes`, both READMEs). Every file opens with the spec's banner line; every figure is tagged "(illustrative — demo)"; the former brokerage is "a franchise office"; the only real brokerage named is Taylor's own; competitors, teams and sponsors are fictional ("the Lakeline team", "Jordan"); no source attributions anywhere. The Brain is developed, not transcribed (the echo test): every journey beat carries "what it means / how to use it", every story is written out in Taylor's voice, the why-join-me exists in three lengths, the offer is built, the framework and leadership audit are filled — because the spec says a demo Book renders all eighteen chapters FILLED. Identity files total ~16,300 words of source.
2. **Assembled the Book's structured text** exactly per `brain-book-spec.md` + `brain-doc.md` + `doc-formatting.md`: cover title block (title line + credential meta line + date + the demo cover line), the `[[TOC]] … [[/TOC]]` block with 4 PART rows and 18 `CHAPTER N — TITLE :: summary` rows written for Taylor, CAPS bands wrapped in `═` rules, `──── Label ────` sub-bands, `•` bullets, `1.` steps, `Label:` lead-ins, `>> ` callouts (1–2 per chapter, Chapter 13 opening on the why-line, Chapter 10 on the UVP, Chapter 11 on the weekly activity), pipe-row tables everywhere the contract mandates one, second-person voice, and the Chapter 18 open-items table + workshop map.
3. **Rendered** with the spec's flags: `render_doc.py input.txt "📕 Taylor Brooks's Agent Attraction Brain Book — DEMO — 2026-10-08.docx" --title "Taylor Brooks's Agent Attraction Brain Book" --subtitle "Taylor Brooks · Austin, TX" --eyebrow "Agent Attraction Brain · Demo"`, stderr captured. The Scorecard the same way with `--title "90-Day Attraction Scorecard"` (legacy mode — no `[[TOC]]`, so no cover break).
4. **Built a second variant** of the same Brain's Book — the **Week-1 first-run** state Setup Phase 8 actually produces: Chapters 7, 8, 15 as the spec's designed placeholders, Chapter 16 as Stop-16 basics + the placeholder line, Chapter 10 in "(so far)" mode, Chapter 9 at the one seed line, Chapter 4 as the six one-line Stop-6 seeds, Chapter 13 without the execution framework, Chapter 5 without the voice-print, Chapter 18 with the corresponding fourteen rows. This is the Book a cohort member holds at the end of Week 1.
5. **Measured** by extracting the `.docx` back through python-docx in document order (`exports/measure_book.py`): words per section (and words excluding the demo tags), tables and rows, callouts (the shaded single-cell tables), sub-bands/bullets/numbered/label paragraphs, `pageBreakBefore` and hard page breaks, TOC hyperlinks and bookmarks, the footer PAGE field, the byline count, raw-markup scan, `[confirm:]` count.
6. **Estimated pages two ways** (no LibreOffice/Word on this Mac; a Pages.app AppleScript export timed out twice; a textutil→HTML→headless-Chrome proxy timed out three times — both abandoned within bounds): (a) the task's formula — ceil(words ÷ 380) per section, every forced break starting a new page; (b) a layout model using the renderer's real geometry — Letter, 6.5 in × 9.1 in usable (655 pt), 10.5 pt Arial at 1.16 line spacing (~95 chars/line), 7 pt paragraph gaps, table rows at the renderer's proportional column widths with 9.5 pt text, +60 pt per chapter head. (b) is the better estimate; (a) over-counts because tables pack more words per inch than prose. **Both are estimates.**
7. **Ran the verification gate by hand** (the demo swaps for checks 6, 15, 16), read Chapters 2, 6, 7, 8, 9 for the anti-fluff swap test, and grepped the extracted text for banned words, real brokerage/competitor names, earnings-claim phrasing, and dollar figures by chapter.

## 2. The numbers

| Section | Spec range (words) | Full demo: words | tables | callouts | est. pages (layout / words÷380) | Week-1 run: words | tables | est. pages | Verdict (Week-1) |
|---|---|---|---|---|---|---|---|---|---|
| COVER | — | 40 | 0 | 0 | 1 / 1 | 47 | 0 | 1 / 1 | — |
| CONTENTS | — | 533 | 0 | 0 | 2 / 2 | 556 | 0 | 2 / 2 | — |
| PART I — WHO YOU ARE | 40–80 | 77 | 0 | 0 | 1 / 1 | 77 | 0 | 1 / 1 | in band |
| CHAPTER 1 — SNAPSHOT | 100–150 | 332 | 1 | 1 | 1 / 1 | 332 | 1 | 1 / 1 | above band |
| CHAPTER 2 — THE LEADER | 250–400 | 617 | 0 | 2 | 1 / 2 | 617 | 0 | 1 / 2 | above band |
| CHAPTER 3 — YOUR JOURNEY | 350–600 | 935 | 0 | 1 | 2 / 3 | 935 | 0 | 2 / 3 | above band |
| CHAPTER 4 — YOUR STORY BANK | 400–800 | 1457 | 1 | 1 | 3 / 4 | 365 | 1 | 1 / 1 | THIN (below floor) |
| CHAPTER 5 — YOUR VOICE & BRAND | 300–500 | 1221 | 2 | 1 | 3 / 4 | 1062 | 2 | 3 / 3 | above band |
| PART II — WHO YOU ATTRACT | 40–80 | 69 | 0 | 0 | 1 / 1 | 59 | 0 | 1 / 1 | in band |
| CHAPTER 6 — YOUR AGENT AVATARS | 500–900 | 1403 | 3 | 1 | 3 / 4 | 1403 | 3 | 3 / 4 | above band |
| CHAPTER 7 — YOUR MARKET'S AGENT LANDSCAPE | 500–900 | 744 | 1 | 1 | 2 / 2 | 105 | 0 | 1 / 1 | placeholder (exempt) |
| CHAPTER 8 — WHERE THEY GATHER | 250–450 | 465 | 1 | 1 | 1 / 2 | 101 | 0 | 1 / 1 | placeholder (exempt) |
| PART III — WHAT YOU OFFER | 40–80 | 71 | 0 | 0 | 1 / 1 | 71 | 0 | 1 / 1 | in band |
| CHAPTER 9 — YOUR MODEL, POSITIONED | 350–600 | 2065 | 0 | 2 | 4 / 6 | 158 | 0 | 1 / 1 | THIN (below floor) |
| CHAPTER 10 — YOUR OFFER | 300–600 | 1381 | 4 | 2 | 3 / 4 | 338 | 1 | 1 / 1 | in band |
| CHAPTER 11 — THE MONEY, HONESTLY | 300–500 | 384 | 1 | 1 | 1 / 2 | 384 | 1 | 1 / 2 | in band |
| CHAPTER 12 — YOUR PROOF | 200–400 | 441 | 1 | 1 | 1 / 2 | 441 | 1 | 1 / 2 | above band |
| PART IV — HOW YOU WIN | 40–80 | 70 | 0 | 0 | 1 / 1 | 70 | 0 | 1 / 1 | in band |
| CHAPTER 13 — YOUR 12-MONTH AND 90-DAY PLAN | 400–700 | 860 | 5 | 2 | 3 / 3 | 358 | 2 | 2 / 1 | THIN (below floor) |
| CHAPTER 14 — YOUR WEEKLY ACTIVITY | 150–300 | 400 | 2 | 1 | 1 / 2 | 344 | 1 | 1 / 1 | above band |
| CHAPTER 15 — YOUR CONTENT PILLARS | 200–400 | 571 | 1 | 1 | 2 / 2 | 96 | 0 | 1 / 1 | placeholder (exempt) |
| CHAPTER 16 — HOW YOU OPERATE | 150–300 | 924 | 2 | 1 | 2 / 3 | 466 | 1 | 2 / 2 | above band |
| CHAPTER 17 — COMPLIANCE | 150–250 | 538 | 0 | 1 | 2 / 2 | 538 | 0 | 2 / 2 | above band |
| CHAPTER 18 — YOUR OPEN ITEMS | 100–300 | 407 | 1 | 1 | 1 / 2 | 460 | 1 | 2 / 2 | above band |
| **TOTAL** | spec: 5,000–6,500+ (floor 3,000; Week-1 w/o research 3,600) | **16,005** | 26 | 22 | **43 / 57** | **9,383** | 15 | **34 / 38** | both far above every floor |

| Document | Words | Tables | Breaks | Pages (estimate) |
|---|---|---|---|---|
| 🎯 90-Day Attraction Scorecard (legacy mode, no cover/TOC) | 791 words (768 without tags) | 4 tables / 26 rows | 0 forced breaks | layout model 2.05 pages → **2–3 pages** (words÷380 = 2.08) |

Structure, both Book variants: 18 `CHAPTER` bands + 4 `PART` bands, sequential and in the right parts · 22 TOC hyperlinks resolving to 22 bookmarks · 2 hard page breaks (after the cover, after the contents) + 21 `pageBreakBefore` (every band except PART I, which follows the contents break) · footer PAGE field present · byline "Taylor Brooks · Austin, TX" once · credential line once · `<w:` in text: none · `[confirm:]`: none · renderer stderr: empty on all renders. Demo tags "(illustrative — demo)": 102 in the full Book (2.2% of the word count — the "no tags" column shows the count without them).

**The page estimate, honestly:** full demo Book **≈ 43 pages** by the layout model (57 by words÷380); Week-1 first run **≈ 34** (38); Scorecard **2–3**. The structural floor alone is 1 cover + 2 contents + 4 part-title pages + 18 chapter starts = 25 pages before any chapter spills; the question was never whether the Book reaches 10 pages but whether those pages hold content — and the chapter word counts say they do. Treat ±15% as the error band; Word and Google Docs will paginate slightly differently from each other.

## 3. The verification gate (spec, run by hand on the full demo render)

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Word count ≥ 5,000 (floor 3,000) | **PASS** | 16,005 (15,654 without tags). Week-1 variant 9,383 vs its 3,600 floor. |
| 2 | All 18 chapter headings + 4 Part bands | **PASS** | measured 18 + 4, exact titles |
| 3 | Byline once | **PASS** | cover only |
| 4 | No `<w:` markup | **PASS** | |
| 5 | Avatar structure | **PASS** | at-a-glance table, one sub-band per avatar (2), pains table per avatar, "Not the right fit" names no brokerage |
| 6 → demo | Every figure tagged; zero source attributions | **PASS** (interpretation noted) | production, money, ratio, count and landscape figures are tagged in prose, table headers and cells; dates, clock times, durations, chapter/step numbers and cells under a tagged header are not individually tagged (see fix 7). Zero attributions found. |
| 7 | Money discipline | **FAIL on render 1 → PASS on rebuild 1** | Every Chapter 11 figure tagged, stamp present, no earnings sentence. First render carried the rev-share figure in Chapter 13's 12-month table and Chapter 14's Targets table — **because the `goals.md` template and the scorecard Targets block put it there and the spec renders both "in full"**. Fixed on the input (rows now read "see Chapter 11 — private-call material"). Lead-cost figures ($1,100/month, $800–1,500/month) in Chapters 3, 6, 10 are not compensation and stay. |
| 8 | Cardinal rules | **PASS** | no negative characterization of any named party; former brokerage unnamed; competing models described by their honest pros |
| 9 | Tables where mandated | **PASS** | 26 tables: snapshot, story bank, inventory, colours, avatar at-a-glance + 2 pains, footprint, gather, what-worked, five pains, first 30 days, value stack, scenarios, agents helped, 12-month, 30-60-90, four quarters, CEO rhythm, monthly metrics, Targets, KPIs, cadence, follow-up, readiness, open items |
| 10 | Anti-fluff spot check (2, 6, 7, 8, 9) | **PASS (self-judged)** | every paragraph carries Taylor-specific facts; Chapter 7 is illustrative by demo rule but tied to Taylor's two avatars. The author judged his own text — the QA reviewer should re-read these five chapters. |
| 11 | Placeholders only where allowed, mirrored in Ch 18 | **PASS** | full demo: none. Week-1 variant: 7, 8, 15, 16 (allowed), Ch 10 in "(so far)" mode, all mirrored — but Chapter 9 at seed has **no designed placeholder in the spec** (fix 3). |
| 12 | Contents page: one, page 2, 18 rows, member-specific summaries | **PASS, with a physics note** | one CONTENTS, in order, swap-test-clean. At the renderer's spacing, 22 rows + summaries need ≈1,000 pt against 655 pt usable → the contents runs onto page 3 (fix 5). |
| 13 | Chapter labels sequential inside correct parts | **PASS** | |
| 14 | Zero unresolved-TOC warnings | **PASS** | stderr empty, all renders |
| 15 → demo | Zero real competitor/sponsor/team/vendor names | **PASS (interpretation noted)** | only Real Broker (own brokerage), TREC (regulator), and platforms used as tools (Instagram, YouTube, Zoom, Google Sheets, Claude Design); lead vendors, CRMs, coaches, teams, sponsors are all generic or fictional (fix 7) |
| 16 → demo | Watermark: filename + eyebrow + cover line; all 18 filled | **PASS** | the Week-1 test variant appends "· Week 1 first-run build" to the cover line on purpose — a real demo build keeps the line verbatim |
| 17 | `[confirm:]` ≤ 3, none in 7–8 | **PASS** | 0 |
| 18 | Open items match real gaps | **PASS** | 9 rows ↔ brand-visual kit "not yet", compliance's four open items, proof consent, brokerage-model "still needs", config Watcher/Debrief, offer digital product |

Bounded-retry accounting: TOC re-renders 0; rebuild cycles 1 of 2 (check 7); research refreshes n/a (demo). Renderer quirks hit and fixed on the input, never the renderer: a numbered item beginning "1. A 45-minute …" rendered as a bold lead "A 45-" + " minute" (the numbered-lead regex accepts a short caps/digit run ending in a hyphen) — reworded.

## 4. Thin chapters — which, why, and what fixes it

**Full demo (all Week 2–3 files built): no chapter is thin.** Eleven chapters are *above* their spec band, several by 2–3× (Chapter 9 at 2,065 words vs 350–600, because the why-join-me long version alone is 500–800 words by its own skill's contract; Chapter 4 at 1,457 with seven stories written out; Chapter 10 at 1,381 with the five-pains, first-30-days and value-stack tables). This is "render the FULL content of every identity file — never compress" working as intended; the bands are simply calibrated for a thinner brain (fix 4).

**Week-1 first run (what Phase 8 produces): three chapters land under their floor, and the spec caused all three.**

| Chapter | Week-1 words | Floor | Why it is thin | Cause |
|---|---|---|---|---|
| 4 — Your Story Bank | 365 | 400 | Setup Stop 6 captures six seeds "one line each, just give me the scene"; the spec renders unfleshed seeds as one-liners in a table + a "Still to tell" list | spec/skill gap: nothing develops the seeds before the first Book |
| 9 — Your Model, Positioned | 158 | 350 | `positioning.md` holds only the Q36 seed line at Week 1; the model, the script and the why-join-me are Week 2 — and the spec names no placeholder for Chapter 9, so it renders heading + honest state + phrases | spec gap: Chapter 9 is "no placeholder allowed" yet has nothing to render on a first run |
| 13 — Your 12-Month and 90-Day Plan | 358 | 400 | goals only; the four-quarter table, non-negotiables, constraint and CEO rhythm come from `execution-framework.md`, which is "built after goals lock", not at setup | borderline — the floor assumes the framework |

Chapters 7, 8, 15 are the spec's own placeholders (≈100 words each) and 16 is "basics + placeholder" at 466 — all by design, all mirrored in Chapter 18. The Week-1 total, 9,383 words, is still 2.6× the 3,600 floor; the Book is long enough. The thin spots are quality, not length: a member paging to Chapter 9 on day one finds four sentences.

## 5. Proposed fixes (concrete edits — NOT applied; `plugins/` is under QA)

**Fix 1 — the most likely cause of a 2–3-page Book, and the renderer cannot see it.** The full structured text is 101 KB / ~16,000 words; even the Week-1 text is 62 KB. If the Finalize step emits it in one generation and the output is cut off, the renderer happily renders whatever arrived — a 3-page document with no error (there is no "last chapter missing" check in the renderer). The spec's gate (check 2) catches it only if the gate is actually run.
`brain-book-spec.md` → "The build pipeline", step 3, append:
> **Write the structured text to the temp file chapter by chapter — one append per PART or CHAPTER band, never one emission.** Before step 6, run the structural pre-check: the file contains 4 PART bands and CHAPTER 1–18 bands in order, every `[[TOC]]` row has a character-for-character band, and the last band is `CHAPTER 18 — YOUR OPEN ITEMS`. A file that fails the pre-check is incomplete — append the missing chapters; never render it.
(Optional renderer change for the owner, since it is byte-shared by five plugins: in book mode, print `WARNING: book has N chapter bands` to stderr when a `[[TOC]]` row count and band count differ — the gate already greps stderr.)

**Fix 2 — gate check 7 fails every complete Brain because of the goals template.** `goals.md`'s 12-month table has a "Rev share (illustrative…)" row, `memory/scorecard.md`'s Targets block has one too, and Chapters 13 and 14 render both "in full" — so a rev-share figure always appears outside Chapters 9 and 11, and check 7 fails on every build until a retry deletes it (or the bounded retries exhaust and the build STOPs).
`brain-book-spec.md` → Chapter 13 contract, after "the 12-month milestones **table**": add *"— whose rev-share row renders as 'see Chapter 11 — private-call material', never the figure"*; Chapter 14 contract, after "the Targets block from `scorecard.md` as a **table**": the same clause; verification gate #7: *"no compensation number appears outside Chapters 9 and 11 (the rev-share rows in Chapters 13–14 point at Chapter 11)"*.

**Fix 3 — the Week-1 thin chapters.**
(a) `skills/attraction-brain-setup/SKILL.md` → Phase 3, Stop 6, "Drafted, not asked": append *"— and each seed is developed, before the Book build, into a 60–120-word story block in the member's own words: the scene they gave, what it proves, where it gets used (the echo test — a seed pasted under a heading is not done)."* And `brain-book-spec.md` → Chapter 4: replace *"Seeds that were never fleshed out render as one-line seeds in a closing 'Still to tell' list"* with *"On a first run every Stop-6 seed renders as its developed 60–120-word block under its own sub-band; only seeds captured later (capture rows) render as one-liners in the closing 'Still to tell' list."* Expected effect: Chapter 4 on Week 1 goes from ~365 to ~800 words of real stories.
(b) `brain-book-spec.md` → Placeholders: add *"**Chapter 9 (positioning at seed)** → the one line as the `>> ` callout, then the lead line: *'Your model gets positioned in Week 2.'* Callout: `>> Say "position my model", "explain my model to me", and "why join me" — the vehicle and the reason, the two-minute script for your call, your model in plain English, and your why-join-me story in three lengths.` Then the 'What will appear here' list. Mirrored in Chapter 18."* And in the chapter table: *"350–600 at Week 2 · 1,200–2,000 once the why-join-me long version and the model are built · placeholder at seed"*.
(c) Chapter 13's floor: *"400–700 (250+ before `execution-framework.md` is built)"*.

**Fix 4 — the word bands mislead a builder into compressing.** Eleven chapters of a complete Brain exceed their upper bound by 2–3×; a model reading "300–500" for Chapter 5 next to a 1,200-word voice file will summarize, which the spec forbids elsewhere. `brain-book-spec.md` → chapter table header "Words" → "Words (minimum)"; drop the upper numbers or label them "typical first run"; "Totals" line → *"Week-1 first run: ≥ 3,600 without research, ≥ 4,400 with; complete Brain with the Week 2–3 files built: ≥ 5,000, typically 9,000–16,000 words / 30–45 pages — long is correct."*

**Fix 5 — the contents page is two pages.** 22 rows with summaries need ≈1,000 pt; a page holds 655. `brain-book-spec.md` verification #12: *"exactly one CONTENTS section, beginning on page 2"*; `doc-formatting.md` BOOK MODE bullet 2: note that with 18+ chapters the contents runs to a second page. (Renderer owner option: TOC entry spacing 7/1/7 pt → 4/0/4 pt and summary 9.5 → 9 pt fits 22 rows on one page.)

**Fix 6 — document the numbered-item quirk.** `doc-formatting.md` → the grammar list, under numbered steps: *"Start a numbered item with a word, not a short caps-and-digits run that ends in a hyphen ('1. A 45-minute call' renders as a bold lead 'A 45-'); write '1. The welcome call — 45 minutes …'."* (Renderer owner option: require two letters before the dash in the numbered-lead regex.)

**Fix 7 — demo rules, three clarifications.** `brain-book-spec.md` DEMO BRAINS: (a) *"every number"* → *"every production, money, ratio, count and landscape figure; dates, clock times, durations, chapter and step numbers, and table cells under a tagged header are exempt"*; (b) *"no real … vendor names"* → *"platforms used as tools (Instagram, YouTube, Zoom, Google Sheets) may be named; lead vendors, CRMs, coaches, competitors, sponsors and teams may not"*; (c) the demo cover line is verbatim — the Week-1 test file here deliberately suffixes it and would fail an exact-string check.

**Cosmetic, for the owner's judgment:** the renderer page-breaks before every PART band *and* every CHAPTER band, so each Part opener is a near-empty page carrying only its 40–80-word bridge (4 of the ~43 pages). Normal for a printed book; if unwanted, the renderer option is "no page break on the first CHAPTER after a PART band". And the cover reads "Taylor Brooks's Agent Attraction Brain Book / Taylor Brooks · Austin, TX" — the spec's `[Name]'s` + `[Name] · [Market]` repeats the full name and produces "Brooks's"; `[First name]'s` on the title reads better.

## 6. What was proven, and what was not

Proven with real renders: the renderer produces a long, linked, properly structured `.docx` from a complete structured text; the spec's structure (cover, contents, 4 parts, 18 chapters, callouts, tables, open items) works end to end; the demo rules can be met; the gate is runnable mechanically for 13 of 18 checks (the script is in `exports/measure_book.py`). Not proven: real pagination (two engines timed out — the estimates bracket 34–57 pages for the two Books; the truth is in that range, probably near the layout-model figures), and the anti-fluff judgment on my own prose (checks 10 and 12 need an independent read). Not tested: a live Phase 8 run inside Cowork — this test assembled the text by hand against the spec; the fixes above are about making that assembly survive a real session.

## 7. Files

- `docs/demo/📕 Taylor Brooks's Agent Attraction Brain Book — DEMO — 2026-10-08.docx` — full demo render (90 KB)
- `docs/demo/📕 Taylor Brooks's Agent Attraction Brain Book — DEMO (Week 1 first run) — 2026-10-08.docx` — the Phase 8 state (71 KB)
- `docs/demo/🎯 Taylor Brooks's 90-Day Attraction Scorecard — DEMO — 2026-10-08.docx` (41 KB)
- `docs/demo/taylor-brooks/attraction-brain/` — the demo Brain (brain.md, config.md, identity/ ×20, memory/ ×13, exports/)
- `docs/demo/taylor-brooks/attraction-brain/exports/brain-book-DEMO-2026-10-08.txt` · `brain-book-DEMO-week1-2026-10-08.txt` · `scorecard-DEMO-2026-10-08.txt` — the renderer inputs; re-render with `python3 plugins/attraction-ai-brain/shared/render_doc.py <input> <out.docx> --title "Taylor Brooks's Agent Attraction Brain Book" --subtitle "Taylor Brooks · Austin, TX" --eyebrow "Agent Attraction Brain · Demo"`
- `docs/demo/taylor-brooks/attraction-brain/exports/measure_book.py` — the measurement/gate script: `python3 measure_book.py <book.docx> book`

## 8. Renderer v2 re-render (2026-10-09)

The shared renderer was upgraded after the user reviewed the demo Book (real `Title` / `Heading 1` / `Heading 2` styles, 11pt body, 20pt chapter and 24pt part titles, running header + `Page X of Y` footer from page 2, "In this part" linked lists on every part opener, tinted repeating table headers with zebra rows and horizontal hairlines, accent-bar callouts, keep-with-next + widow control, optional accent colour, sub-band cap 80 with a warning). The three demo files were re-rendered from the unchanged inputs as `… — v2.docx` with accent `1F3A5F`; text content is identical to v1 apart from the four part lists (+520 words, the 18 contents summaries repeated once).

| Measure | v1 (2026-10-08) | v2 (2026-10-09) |
|---|---|---|
| Paragraph styles | all `Normal` (385) | `Title` 1 · `Heading 1` 23 · `Heading 2` 33 · `Normal` 372 |
| Tables with a repeating header row | 0 of 26 | 26 of 26 |
| Rows that cannot split across pages | 0 | 165 |
| keep-with-next / widow control | 0 / 0 | 114 / 377 |
| Internal links (contents + part lists) | 22 | 40 |
| Header / footer | footer, PAGE only, every page | first page blank · title header · subtitle + eyebrow and `Page X of Y` footer |
| Part-opener words | 77 / 69 / 71 / 70 | 227 / 162 / 187 / 231 |
| Pages (layout model, ±15%) | ≈43 | ≈48 (Week-1 run ≈35) |

Still not proven on this machine: real pagination (no Word or LibreOffice installed; Pages hung on launch) — the v2 files were validated by reopening with python-docx, a schema-order check of every hand-built element, and the measurement script. The "cosmetic" note in §5 (near-empty part openers) is resolved by the part lists.
