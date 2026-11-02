# Plan — the Business Planning skill (Week 0, prep week)

*Mapped 2026-11-02 from Mike's decision: onboarding becomes Week 0, a prep week. The member builds their business plan first, then the Brain in Week 1 reads it. Nothing here is built yet.*

## 1. What it is, in one breath

Phase 0 of the Brain process. The business plan is a component of the Agent Attraction Brain, not a separate product: one skill inside the Brain plugin, `attraction-business-plan`, that a member runs in prep week as the first sitting of building their Brain. Week 1's setup is the second sitting of the same process: it continues from the plan, never re-asks it, and the Book, the dashboard and the Brain's weekly skills all read and refresh the same files. About 20 minutes, one question at a time. It produces three things: a Business Plan document, a Vision & Business Dashboard (one visual file that opens in a browser), and a seed the Week 1 Brain setup imports so the member is never asked their numbers twice.

Phrases: "build my business plan" · "my prep week plan" · "business planning" · "my vision board" · "refresh my dashboard".

## 2. Where it sits (one process, two sittings a week apart)

- **Week 0 (prep).** Install Plugin 1, say "build my business plan". No Brain, no Drive required (Drive is offered, not required; without it the files land in the member's Downloads and the seed stays local).
- **Week 1.** Brain setup's first step finds the prep-week seed and imports it: Mike's Conversation 4 (agents today, 12-month goal, long-term goal, hours) becomes a one-line confirm instead of four questions; the WHY from prep week pre-fills the WHY question. The Book's "Your numbers" section renders from the same plan.
- **Every week after.** "refresh my dashboard" re-renders the dashboard from the scorecard's actuals, so the rings fill as the cohort goes. The Friday check-in and the Daily Debrief write the actuals they already write; nothing new to log.
- **Week 6 (scaling).** The plan is revisited: the same skill in update mode.

## 2b. One launch, routed by state (the order and the sync)

Launching the Brain plugin ("launch the AI Brain plugin", "set up my attraction brain", "build my business plan") always does the next thing and nothing else:
- **Nothing built yet (prep week):** the business planning questions (section 3), then the Business Plan document and the Vision & Business Dashboard. Done for the week.
- **Plan built, no Brain (Week 1):** one line, "I have your plan from prep week", then Mike's four conversations and the three voice answers, the Book, and the Brain Board (section 4d). The plan's numbers and WHY are already in and never re-asked.
- **Both built:** refresh whichever board changed and say what's next.
- **Skipped prep week:** launching in Week 1 runs the plan questions first, then rolls straight into the Brain in the same sitting or the next.

## 3. The interview (four short conversations, one question per message)

Mike's rules apply: one plain question at a time, "your turn" at the end of each conversation, "I don't know" moves on, no agent-type question, no "where can you attract" question, no CRM, calendar, compliance or scheduling.

**Conversation 1 — Where you are**
1. Your name, your brokerage, your market (one line).
2. How many closings in the last 12 months, roughly?
3. Where does most of your business come from today? (two sources)
4. How many agents are in your revenue share organization today? (zero is a real answer)
5. What's the single biggest frustration in your business right now?

**Conversation 2 — Your vision**
6. Your big WHY: who are you doing this for?
7. If this works, what does your life look like 12 months from now? (in your words)
8. And three years from now?
9. What does "freedom" mean to you, specifically?
10. When agents talk about you, what do you want to be known for? (one line)

**Conversation 3 — Your numbers**
11. How many agents do you realistically want to attract in the next 12 months?
12. Your long-term goal: how big an organization?
13. Proposed from 11: your 90-day join target, and the conversations → calls → joins ratios (defaults shown; confirm or change).
14. Optional: your estimate of a typical attracted agent's production, for the money picture (skip is fine).
15. Your plan mechanics: "explain mine" runs the model expert later; the default is the strictest generic mechanics, labelled.

**Conversation 4 — Your commitments**
16. Hours per week you can fully commit to agent attraction.
17. Proposed from 11, 13 and 16: the weekly activity you control (conversations, calls, follow-ups, content pieces); confirm or change.
18. Your three non-negotiables for the week, one always content (proposed; confirm, and name the day for each).

Eighteen questions, eight of them pre-answered with a recommended default so "yes" works.

## 4. The three outputs

### 4a. The Business Plan document (the renderer, book style, 8 to 12 pages)
Cover · At a glance (one table: 12-month goal · 90-day target · weekly activity · the three non-negotiables · the next step) · Where you are · Your vision (the WHY, the 12-month and 3-year pictures, the known-for line) · Your 12-month goal and the money, honestly (three illustrative scenarios from the rev-share calculator logic, no earnings promise, the compliance line) · Your 90-day plan (three 30-day blocks with a "done when") · Your weekly scoreboard (the targets, the ratios) · Your three non-negotiables · The four quarters · What happens in Week 1. Saved as "Business Plan · [Name] · [date].docx".

### 4b. The Vision & Business Dashboard (one file, opens in any browser)
A single self-contained HTML file rendered by a new `shared/render_dashboard.py` from the plan's structured text, no internet needed, premium dark look with one accent colour (the member picks from four in one question, or the default), printable to one page.
- **Vision board** (top): the WHY as the headline · the 12-month picture and the 3-year picture as two cards · the known-for line · the people they're doing it for · six photo tiles: the member drops up to six photos into the plan folder and says "refresh my dashboard"; until then the tiles carry their own words, never stock images or generated faces.
- **Business board** (below): the 12-month organization goal as a progress ring (0 at prep week) · the 90-day targets as three counters (conversations, calls, joins) · the weekly scoreboard (targets, and actuals once the Brain exists) · the three non-negotiables with their days · the four-quarter roadmap · the three money scenarios as bars, each labelled illustrative · the compliance line in the footer.
- Saved as "Vision & Business Dashboard · [Name].html" beside the plan; opened for the member with one click; refreshed on demand from the scorecard.

### 4c. The Brain seed (what Week 1 imports)
Written into `~/attraction-brain/` (created if absent), in the template's own shapes: `identity/goals.md` (Status: planned in prep week; the targets, ratios, weekly activity, non-negotiables), `memory/scorecard.md` (the Targets block), `identity/profile.md` seeds (name, brokerage, market, organization size, hours), `identity/journey.md` seed (the WHY, the vision lines), and `business-plan.md` at the root pointing at the two files. Brain setup's Step 0 treats "a prep-week seed with no brain.md" as "import the plan, then start Conversation 1"; the sync to Drive happens when setup chooses the provider.

### 4d. The Brain Board (the visual of the Brain itself)
A second file from the same renderer, built the moment the Book renders and refreshed on demand ("refresh my brain board"): who they are at a glance · their story as a timeline of turning points · their unique approach as the skills they can teach · a proof wall (achievements, agents helped) · who their story speaks to · the numbers rings from the plan · their voice as three signature lines · what's next. As the weeks add the offer, the lead magnet, the pillars, the channel and the pipeline, those tiles light up, so by Week 6 the board is a picture of the whole system they built. Saved as "Brain Board · [Name].html" beside the Book.

## 5. Doctrine and guard rails
- No earnings promise anywhere; every money figure labelled illustrative; the member's own numbers tagged as theirs.
- Attract anywhere; no agent-type selection; the plan is about the member's skills, hours and targets.
- The brokerage's plan mechanics stay generic unless the member supplies their document (the model expert, Week 2).
- Plain language; no file names or skill names out loud; demo mode tags figures and renders both outputs for the demo member.

## 6. What gets built (one agent pass, after the Brain rebuild lands)
1. `plugins/attraction-ai-brain/skills/attraction-business-plan/` — SKILL.md + references: `interview-guide.md`, `plan-doc.md` (the document contract and floors), `dashboard-spec.md` (the sections, the data contract, the refresh rule) and `brain-board-spec.md` (the Brain Board's tiles and which Brain file feeds each).
2. `plugins/attraction-ai-brain/shared/render_dashboard.py` — structured text in, one self-contained HTML file out, two layouts (the Vision & Business Dashboard, the Brain Board); demo renders of both checked in.
3. Brain setup: the state router of section 2b (plan first, then the Brain, never re-asking), the Conversation 4 confirm, the Brain Board rendered after the Book; the Book's "Your numbers" reads goals.md as today.
4. `attraction-goals` and `attraction-rev-share-calculator`: read the plan when present, update it rather than rebuild it.
5. The scorecard writers (the Friday check-in, the Debrief) unchanged; "refresh my dashboard" reads what they write.
6. Docs: setup guide Week 0 row, the Support desk's Week 0 (cohort-kb, stack-map, diagnose "I built my plan, now what"), the master plan, the contract (goals.md may be seeded in Week 0), the demo renders (docx + html) for Taylor.
7. Gate, versions, changelog.

## 7. Decisions for Mike and Riya before the build
1. Dashboard as a self-contained HTML file from the plugin (recommended: instant, no design tool needed in Week 0) versus a Claude Design board (needs the design system, which does not exist until Week 1).
2. The money picture in Week 0: include the three illustrative scenarios (recommended; it is the plan's engine) or defer to the Brain.
3. The accent colour: one question with four choices, or the cohort's palette for everyone until their brand exists in Week 1.
4. Photos on the vision board: the member's own, dropped into the folder (recommended), or none.
