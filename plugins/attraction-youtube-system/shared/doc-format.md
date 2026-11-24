# Document Format — the house style for EVERY saved document

Every deliverable is rendered to a **clean, formatted `.docx`** in one neutral house style — the same look for
every member (no colour, no per-member branding). The skill writes the **structured text** defined below (CAPS
section bands, `•` bullets, `Label:` lead-ins, simple aligned tables); the shared renderer turns that into real
Word formatting — headings, bullet lists, tables — automatically. **Do NOT save flat `text/plain`.**

**How to read this file — it is long; never read it whole (usage discipline, house rule #8).** Read the part above
`## Per-doc skeletons` once (the saving steps, the look, the grammar). Then read ONLY the skeleton you are about to
fill: search this file for its heading and read from that heading to the next `###`. The skeletons, by heading:
`### YouTube Game Plan` · `### Script` · `### Channel Page` · `### Kickoff Brief` ·
`### SEO Package` · `### Interview Prep` · `### Thumbnail Sheet` · `### Starter Resource` ·
`### Model Breakdown` · `### YouTube Deep Dive` · `### Monthly Channel Review` · `### Repurposing Pack`. A skeleton
you are not filling in this run is never opened. (The First Batch — Film Day skeleton was retired on 2026-11-23 with
"script my first three videos": one video a week, scripted in full — Mike.)

**Mike's rulings of 2026-11-23 bind every skeleton below** (`shared/house-rules.md` §0): the four pillars, the same
for every channel (the member's niche · helping struggling and new agents succeed · brokerage model breakdowns ·
agent interviews) — never "your three topics"; the first three videos exactly the blueprint · why I joined my
brokerage · an interview; **no channel trailer** in any document; **no reference video** in any document, card
section or export; **no competitor's channel, video or summary** in anything the member reads; one video a week
scripted IN FULL — both forms: the bullet breakdown with the hook scripted word for word, and the full
teleprompter script, 8 to 12 minutes; an interview is a question list, never a script.

## Saving — render the structured text to a styled `.docx`
1. Assemble the doc as structured text (the skeletons below); write it to a temp file in the session's
   scratchpad (never the member's workspace), e.g. `doc.txt`.
2. Render it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Member · what they are known for]"`
   → the house style automatically: **Arial**, **near-black** text, real **headings** (from the bands), real
   **bullet lists** and **tables**, thin light-grey rules.
3. Upload the **`.docx`** to the right folder of the member's workspace (per the Brain's `drive-map.md`, this
   plugin's home is `03 · Content/Long-Form/`, located by workspace ID; the Starter Resource alone goes to
   `03 · Content/Guides/`) — the structured text was only the renderer's input; the deliverable is the `.docx`.
4. **Four texts are kept for the Brain Board** (the owner, 2026-11-14), written to `~/attraction-brain/exports/`
   in the same run and then pushed (the Brain syncs `exports/*.txt`): the Channel Page as
   `channel-kit-YYYY-MM-DD.txt` (the file name is unchanged — `yt-setup`'s own walk-through reads it) · the YouTube Game Plan as
   `youtube-game-plan-YYYY-MM-DD.txt` (the document's text **plus the TITLE NOTES block** — the per-title working
   notes the document never prints; the Game Plan skeleton has its shape) · the Monday Kickoff as
   `youtube-kickoff-YYYY-MM-DD.txt` — **the Kickoff's note**, the short lines the Brain Board shows; one name and one
   meaning in every file (the Kickoff Brief itself is the document in the video's folder) · each Monthly Channel
   Review as `youtube-review-YYYY-MM-DD.txt`. The export sits beside the `.docx`, never instead of it; a doc saved
   without its export is half-saved.
   **A fifth text is kept the same way:** each YouTube Deep Dive, and each on-demand video read, as
   `youtube-read-YYYY-MM-DD.txt` (`yt-analytics`) — its own name, never `youtube-review-*`, which is the Monthly
   Channel Review's alone (`yt-triggers`).
   **And a sixth:** the three clip scripts of each repurposed video, as `youtube-clips-[the video's System ID].txt`
   (`yt-repurpose`) — each clip word for word with its ask, its caption and its hashtags; the Short-Form System's
   Monday Week Plan drafts the week's Reels from it, and the clip scripts are queued in the Brain's calendar
   (`memory/content-calendar.md → ## Clips from your videos (YouTube)`).

**If the renderer prints `RENDERER-UNAVAILABLE`** (python-docx is not in this environment): **install nothing, do
not run pip, do not retry the command** (a package install can block for many minutes in a sandbox and looks like a
hang). The renderer's own message suggests uploading the text; **in a chat, do this instead:** build the same
`.docx` ONCE with the **docx skill**, matching the look below. If that also fails, STOP, keep the full content
visible in chat so nothing is lost, and say — a statement, never a question, and never the word "renderer":
*"I couldn't save this as a document this time. Everything is here in the chat — ask for it again in a new chat and
it saves."* Never "just upload the text" in a chat. **A scheduled run is the one exception** (nobody is there to ask
again): it uploads the structured text as a `.md` file and says so in its note, as its task prompt says.

**In a chat, NEVER upload the raw structured text as the deliverable.** The CAPS bands and `────`/`════` rules are the
RENDERER'S INPUT, not a document — if a saved doc ever shows literal dash lines as text, the raw input was
uploaded: that is a FAILED delivery. Re-render and upload the `.docx` (ONE corrective re-upload; if it fails
again, stop and say so — never loop).
**Verify before uploading (every doc):** read the finished `.docx` back — (a) no raw `<w:` markup in the content
(corrupt build → rebuild); (b) depth matches the deliverable — a rich source rendered thin is a failed render,
rebuild with the full content. Members pay a premium; the documents must feel like it.

## The look the renderer produces (match it if you ever build by hand)
- **Arial** everywhere (never a serif). **Near-black (#111)** titles / headings / body — crisp, never grey; a
  legible **dark grey** only for the small byline + stamp.
- Section headings are real Word heading styles (`Heading 1` / `Heading 2` in the house look: bold near-black,
  a thin light-grey rule under section bands; body 11pt). **Real** bullet lists. **Real** tables: bold header row
  on a light tint, white / off-white alternating rows, hairline horizontal rules only, header row repeated when a
  table crosses a page. A running header + `Page X of Y` footer from page 2. **No member branding** — one
  standard for all; the renderer's optional accent-colour flag (used by the Brain Book build) is NOT passed by any
  YouTube skill, so YouTube documents stay near-black.
- Keep every ALL-CAPS sub-band label ≤ 80 characters: a longer label is rendered as body text with literal dashes
  and the renderer prints a WARNING — rewrite the label, never ship the warning.
- The YouTube Game Plan carries `Powered by Mike Sherrard Coaching Inc Frameworks` (top byline + footer).
- Demo documents (house rules #13) carry `— DEMO —` in the filename and the meta line *"Demo document —
  illustrative data, not researched."*

---

## The structured text the renderer reads (write the doc in this grammar)

**Title line** — first line, the doc's name in CAPS. Then a **meta line** of ` · `-separated facts, blank line:
```
WHY MOST NEW AGENTS QUIT IN YEAR ONE — AND HOW TO BE THE EXCEPTION
About 12 minutes  ·  For: agents in their first two years  ·  Fri, Dec 4
```

**Section band** — standard header wrapped top + bottom by a 44-char `─` rule, label in CAPS, ` · ` timestamp:
```
────────────────────────────────────────────
YOUR OPENING  ·  0:00
────────────────────────────────────────────
```

**Major block** — for big structural blocks (Chapters, the Short, top-level parts) use the heavy `═` rule:
```
════════════════════════════════════════════
CHAPTERS   (planned — the real times come from your edit)
════════════════════════════════════════════
```

**Cue lines** — non-spoken notes on their OWN line, indented 3 spaces:
```
   >> ON SCREEN:  Taylor Brooks · Austin
   [PAUSE]
   FACT:  from the brokerage's onboarding guide, September 2026
```

**Bullets** — 3-space indent, `•`, two spaces: `   •  First point.`

**Footer** — a `─` rule, then the sourcing line:
```
────────────────────────────────────────────
Facts checked — {claim} ({source}, {the date, in words}).
```
**The compliance check is run before saving and is never printed** — nothing negative about any brokerage or
person · no pay figures (no split, cap, fee, tier, stock or income number) · the brokerage's wording where the
member's compliance file asks for it. Its words ("cardinal rules", the status values `unset` / `set` / `confirmed`)
never reach a document. **Compliance `unset`** → a piece that goes public carries the one stamp line under its
title — "hold until your compliance basics are set" — and a document says it once, never twice.
The Game Plan also carries the **credibility stamp** (house rules #9): `Powered by Mike Sherrard Coaching Inc
Frameworks` — once as a byline under the title, once as the final footer line. Never inside a copy block the
member pastes out.

Rules: a blank line between every section · spoken text in plain sentences · CAPS + dividers + indents carry the
hierarchy · use only `─` (U+2500), `═` (U+2550), `•` (U+2022). Tight and scannable — readable at a glance.

---

## Per-doc skeletons (fill in, keep the shape)

### YouTube Game Plan (the flagship — stamped; `yt-gameplan`; the text also kept at `exports/youtube-game-plan-YYYY-MM-DD.txt` so the Brain Board can read it)
**A document the member reads, not a system file** (the owner, 2026-11-14 — the same treatment the Short-Form Game
Plan got). Only the document changed; the Brain's files keep their locked shapes (`identity/channel.md → ## Game
Plan anchors`, the rows of `memory/content-calendar.md → ## Long-form (YouTube)`). The rules of the document, checked
before it saves:
- **The member's words — the grouping is Mike's four pillars, by his word:** "your four pillars" (a video from the
  niche or the struggling-and-new-agents pillar is "a topic video"), "your interviews", "your model videos", "your
  blueprint", "your pace". Never "lane", "bucket", "cadence" or a content pillar's name (Authority…) in a printed line
  — the Brain's rows and the board keep their own codes (`Bucket`, `Lane`, `Cadence:`). The phrase that changes the pace is printed exactly as the member says it, "change my YouTube pace".
- **None of the system's own words anywhere in the document:** no "SIGNAL", "FOR · PAIN · SIGNAL", "cycle
  position", "anchors", "unresearched", "starter", "rung", "avatar", "SEO", "packaging", "hook", "CTR", "retention";
  no skill name, no file name, no code or note beside a title. Plain replacements: "the agents you want to attract"
  · "your two calls to action" · "how many people click" · "how long people keep watching" · "how it opens" · "not
  yet checked against search" · "a starting set" · "your eight-video plan".
- **Dates in words** — "Mon, Dec 7" — never `YYYY-MM-DD` inside the document (the Brain's rows keep the real dates).
- **YOUR NEXT 7 DAYS is its own ruled block, right after READ THIS FIRST** — exactly three numbered lines, never a
  fourth: the first video by exact title · the first interview (a first name only when a guest is named) · the one
  channel fix.
- **The 90-day calendar is one plain table** — `Week of` (the Monday of the week, in words) · `Video` (the exact
  title) · `Kind` (Topic / Interview / Model — never a trailer row) · `Guest`. (`Kind` is the printed word only — the
  Brain's row keeps its own `Bucket` and `Lane` cells.) **The first three rows are fixed:** the blueprint · Why I
  joined my brokerage · the interview (Mike, 2026-11-23).
- **The interview guest is anyone successful in the member's upline, downline or brokerage** (Mike, 2026-11-23); a
  guest is NAMED only when the member named them (an idea they saved for an interview, a guest they set up) **or the
  Brain holds them in the upline, downline or brokerage** (`organization.md`, `proof.md`). A name from the Top 50 is
  never put on the plan as a guest by the plan itself. Nobody under that rule → the nobody-named form, everywhere:
  each interview row is titled exactly "A conversation with an agent — guest to be named", there is no guest table
  and no invented name, and nothing is drafted to nobody. An interview is a question list, never a script.
- **No trailer, no reference video, no competitor** anywhere in the document (Mike, 2026-11-23): WHAT I CHECKED
  lists the phrases searched, never a channel or a video.
- **The goal prints only numbers the Brain holds** (`identity/goals.md`, the scorecard's Targets). Never a default
  number, an assumed rate, a share or a per-video figure; never a benchmark range; nothing that reads as a promised
  result. No target in the Brain → the one "not set yet" line.
- **Nothing promises a workflow.** The plan is written before the member has said Yes to the Monday Kickoff or the
  Monthly Channel Review, so the document names neither.
- **One missing thing is said once; three or more → one general line, never a list.**
- **The title list is the LAST band** — MORE TITLES WHEN YOU NEED THEM — grouped under the four pillars by name,
  plain titles only.
- **The codes stay in the Brain.** Each title's working notes (who it is for · the pain · why it is on the list)
  are never printed. They are kept in the Brain's copy of the plan only: the **TITLE NOTES** block appended to
  `exports/youtube-game-plan-YYYY-MM-DD.txt` after the document's text (its shape is under the skeleton) — where
  ideation and the Monday Kickoff read each title's why.
Everything inside `{…}` below is a note to the writer and is never printed.
```
YOUTUBE GAME PLAN — [MEMBER NAME]
Known for: [what you're known for]  ·  For: [the first type of agent] · [the second]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks


════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{where your channel is today — one true sentence from what was read, never a verdict nobody measured · the plan in one line · your pace: {one video a week to start — two a week is the next step | two videos a week — the pace you chose} · your 90-day goal in conversations and calls — only when your goals hold it}
{only when it applies, one plain line each — at most two; when all three apply, print this one line instead: "A few pieces are still to come — each is named where it belongs below.": "Some of these titles are not yet checked against what agents search — say "refresh my attraction game plan" and I check them." · "These titles are a starting set. Your own ideas, and the questions agents leave in your comments, replace them over time." · "Your two calls to action are written from your offer for now; your Week 3 Kit's wording replaces them when it is built."}


════════════════════════════════════════════
YOUR NEXT 7 DAYS
════════════════════════════════════════════
   1.  YOUR FIRST VIDEO — your blueprint, "{the exact title}" · {your full script is in this video's folder (written at setup's close) | your full script comes with "make my attraction video: {title}"} · you film it {the day, in words — "Sat, Nov 28"} on your phone in Instagram's free Edits app (it has a teleprompter)
   2.  YOUR FIRST INTERVIEW — your third video · invite {the guest's first name}: {their story in one line} · say "set up an agent interview" and I write your question list   {no guest named — the normal first-time member — this line reads: "2.  YOUR FIRST INTERVIEW — your third video · anyone successful in your upline, downline or brokerage · name them and say \"set up an agent interview\" — I write your question list, no script" — never "the first agent you have helped"}
   3.  YOUR ONE CHANNEL FIX — {the one fix, in plain words — a channel not pasted yet: "paste the three pieces marked 'paste today' in your Channel Page"; while your brokerage's wording is not on file yet: "say \"paste my compliance link\" (two minutes), then \"repair my channel for agents\", then paste the three pieces marked 'paste today' in your Channel Page"}   {nothing left to fix — this line reads: "3.  YOUR CHANNEL — set. Nothing to fix this week."}


════════════════════════════════════════════
YOUR CHANNEL TODAY
════════════════════════════════════════════
{scaled to the number of videos — a new channel: no rows, this one line: "You are starting clean — nothing to fix yet."}
   What's working ......... {…}
   What's missing ......... {which of the three kinds of video is absent · the two calls to action · playlists · titles and thumbnails}
   First impression ....... {can a first-time visitor tell who the channel is for and why to reach out?}


════════════════════════════════════════════
YOUR POSITIONING
════════════════════════════════════════════
Who the channel is for:  {the agents you want to attract, in their words}
What you'll be known for:  {from strategy.md / offer.md}
The one line:  {"[Name] helps [the type of agent] [outcome] through [how]"}
Your two calls to action:  1. The guide — "{the spoken guide line, word for word from the kit — '… Comment GUIDE and I'll send it.'}"   2. The call — "{the spoken call line, word for word from the kit, in the call-to-action law's shape}"   {no guide on file yet: the guide's line is left out — never "comment GUIDE" for a guide that does not exist}
Why I'm building this:  {the why-line from journey.md → ## The WHY, in the member's voice — drafted and labeled "(draft)" when the Brain has not written it; never a question}
What's missing for {the agents you want to attract} — and how I bridge it:  {the bridge-the-gap line — the agents' problem, never a word against another team or brokerage}
Why me — for a new agent · for a seasoned agent:  {from ## Why join me / leadership.md; one line each}


════════════════════════════════════════════
YOUR FOUR PILLARS   (the same four on every channel that attracts agents — one playlist each)
════════════════════════════════════════════
   PILLAR 1 — YOUR NICHE: {its name, from your Brain — e.g. lead generation through open houses}  ·  Playlist: "{the niche playlist, in search language}"
   Who it's for: {the type of agent} · The pain it answers: {in their words} · Why it builds trust: {one line} · Your blueprint — your first video — comes from here.
   PILLAR 2 — HELPING STRUGGLING AND NEW AGENTS SUCCEED  ·  Playlist: "Helping struggling and new agents succeed"
   Who it's for: {the type of agent} · The pain it answers: {in their words} · Why it builds trust: this casts the widest net.
   PILLAR 3 — BROKERAGE MODEL BREAKDOWNS  ·  Playlist: "{[Model] explained}"
   Why it builds trust: {one line — clarity, not hype; the details are below}
   PILLAR 4 — AGENT INTERVIEWS  ·  Playlist: "Agent interviews"
   Who: anyone successful in your upline, downline or brokerage · Why it builds trust: {one line — proof from people like them; the details are below}


════════════════════════════════════════════
YOUR INTERVIEWS
════════════════════════════════════════════
Playlist: "Agent interviews"
Your guest is anyone successful in your upline, downline or brokerage. An interview has no script — you get a question list.
| # | Guest | Their story — the title | Where they come from |
|---|---|---|---|
| 1 | {name} | {How … built … while …} | {your upline / your downline / your brokerage / someone you named} |
{up to 6–10 guests, in the order to invite them — only guests the rule above allows; "your downline" is printed only for a guest the Brain's organization file holds}
{NOBODY NAMED — the normal first-time member: no table and no invented names. Print this one paragraph instead: "You have not recorded an interview yet — every member starts here. Your third video is an interview, and your guest is anyone successful in your upline, downline or brokerage: your sponsor, a leader above you, an agent you admire. Each interview week is kept on your plan as "A conversation with an agent — guest to be named". Until you name a guest, that week's video is the next one from your topic pillars, so no week is empty. The day you name someone, say "set up an agent interview" — you get your question list, no script."}


════════════════════════════════════════════
YOUR MODEL VIDEOS   (how your brokerage's model works)
════════════════════════════════════════════
Playlist: "{[Model] explained}"
   {the videos that answer what agents are already looking up — only the ones that fit the member's own model: explained · should you join · how [one part] works · questions to ask a sponsor · do NOT join if}
   {Mike's comparison warning, one line — comparisons only on the member's explicit choice}


════════════════════════════════════════════
YOUR GOAL   (conversations and calls)
════════════════════════════════════════════
{print only numbers the Brain holds — never a default, an assumed rate, a share or a per-video figure}
   1.  Your 90-day goal: {n} calls held with agents.   (from your goals)
   2.  That takes about {n} conversations — about one call for every {y}.   {only when your goals hold that ratio — otherwise this line is left out}
   3.  Your videos' job is to start those conversations. Count them each week — after a month you have your own numbers.
{no target in the Brain — print this one line and none of the three above: "Your goal is not set yet — say "set my attraction goals" and this section fills in."}
What you control each week: videos published · interviews recorded, once a guest is named · both calls to action in every video · comments answered · messages started.
{your goals are on file but not locked yet — one line: To lock your own numbers, say "set my attraction goals".}


════════════════════════════════════════════
THE VIDEO STRUCTURE   (every video)
════════════════════════════════════════════
   THE OPENING (0:00–0:15) — {the pain point, in the member's voice — written word for word}
   THE GUIDE (inside minute 1) — {the kit's spoken guide line, word for word — "comment GUIDE" / "link in the description"; no guide on file yet → this part is left out}
   THE TEACHING — {as long as it needs to be, as short as it can be; the steps of the member's method are the teaching material}
   THE CALL (about a third in) — {the kit's spoken call line, word for word, in the call-to-action law's shape — the person · their help · free · to run this (house rules #15) — never the brokerage, never a promise of your time}
   THE PAYOFF + THE NEXT VIDEO — {deliver the promise; point to the next logical video}


════════════════════════════════════════════
YOUR PACE
════════════════════════════════════════════
{one a week — the start for every member who did not choose otherwise:} One video a week to start — {the honest read from goals.md's hours}. Two a week is the next step Mike recommends, after a good month at one a week, or sooner when you ask. To change your pace, say "change my YouTube pace". Your eight-video plan works at either pace: eight weeks at one a week, four weeks at two.
{two a week — only when the member chose it: print this instead:} Two videos a week — the pace you chose. Your eight-video plan goes once round in four weeks. To change your pace any time, say "change my YouTube pace".
{only when the Brain holds a short-form plan (identity/content-pillars.md), one more line: "Your short-form posts keep their own rhythm — this is your YouTube pace."}


════════════════════════════════════════════
YOUR FIRST 90 DAYS   (your eight-video plan: 3 topic videos · 1 model video · 4 interviews)
════════════════════════════════════════════
Your first three videos: your blueprint · why I joined my brokerage · an interview. Then: topic · interview · topic · interview · interview — and it starts again, with a model breakdown second time round.
      ──── YOUR FIRST 30 DAYS ────
| Week of | Video | Kind | Guest |
|---|---|---|---|
| {Mon, Dec 7} | {the blueprint's exact title} | Topic | — |
| {Mon, Dec 14} | Why I joined my brokerage | Topic | — |
| {Mon, Dec 21} | {exact title — or, when no guest is named, exactly: A conversation with an agent — guest to be named} | Interview | {the guest's first name — or "—"} |
| {Mon, Dec 28} | {exact title} | Topic | — |
   ──── THE WEEKS AFTER ────
| Week of | Video | Kind | Guest |
|---|---|---|---|
| {Mon, Jan 4} | {exact title — or the guest-to-be-named line} | Interview | {guest} |
{one row per video to about week thirteen, in the order above — topic · interview · interview close the first eight; two interviews may be recorded in one sitting; at two a week two rows share a week; never a trailer row}
{no guest named — one line under the table: "No guest named yet: until you name one, an interview week's video is the next one from your topic pillars, so no week is empty. Your guest is anyone successful in your upline, downline or brokerage — the day you name someone, say "set up an agent interview"."}
{one a week only — one line: After a good month at one a week, two a week is the next step. To change your pace any time, say "change my YouTube pace".}
{the week of the first row is the week of the first filming day — at least three days after the plan was built (yt-gameplan's first-date rule); never the day of the sitting}


════════════════════════════════════════════
DAYS 91–180   (the direction)
════════════════════════════════════════════
   91–120  More of what worked — {the topics to make more of, if they started conversations}
   121–150 Videos that keep working — {the model videos and career-change videos that stay useful for years}
   151–180 Keep the rhythm — {one or two videos a week + one or two interviews a month}


════════════════════════════════════════════
THE SCOREBOARD   (90 days)
════════════════════════════════════════════
   What you do:  {n} videos published at your pace · interviews recorded, as soon as a guest is named {a guest is named: the count} · {only when your goals hold it: {n} calls held}
   What you watch (never a promise):  how many people click your video when YouTube shows it · how long people keep watching · subscribers · the agents who reach out
   {only while your brokerage's wording is not on file, and only when line 3 of YOUR NEXT 7 DAYS has not already said it — one line, never the status word: Before your first video goes out: say "paste my compliance link" — two minutes — so your brokerage's wording is on it.}


════════════════════════════════════════════
WHAT I CHECKED, AND WHEN
════════════════════════════════════════════
   What agents search ..... {each phrase searched → the topic it pointed to · as seen {the date, in words} — never another channel, video, link or view count (Mike, 2026-11-23)}
   What you told me ....... {only what is on file: the ideas you saved · the questions agents asked you · your comments · the news you saved}
   Titles not yet checked against search:  {n, or "none"}   {when some are unchecked: Say "refresh my attraction game plan" and I check them.}
   {demo mode: "Demo — nothing searched; every example is illustrative"}


════════════════════════════════════════════
MORE TITLES WHEN YOU NEED THEM
════════════════════════════════════════════
Pick any, then say "make my attraction video:" and its title.
   ──── YOUR NICHE: {ITS NAME} ────
   •  {exact title}
   •  {…}   {12–15 in all for this pillar, the calendar's included}
   ──── HELPING STRUGGLING AND NEW AGENTS SUCCEED ────
   •  {…}   {15–20}
   ──── YOUR INTERVIEWS ────
   •  {…}   {6–10 — the guest list above, titled}   {nobody named → no titles; print this one line: "Your interview titles are written the day you name a guest."}
   ──── YOUR MODEL VIDEOS ────
   •  {…}   {6–8}
{nothing beside a title — no code, no note, no bracket; a title already on the 90-day calendar is not repeated here; about fifty titles across the calendar and this list when there is a guest list, fewer without one — never padded}


────────────────────────────────────────────
{closing — one honest paragraph: consistency before optimization; this is a long game and this is chapter one; never a promised result}
Powered by Mike Sherrard Coaching Inc Frameworks
```
**The Brain's copy only** — appended to `exports/youtube-game-plan-YYYY-MM-DD.txt` after the closing, never rendered
into the `.docx` and never shown to the member (this is where the codes stay):
```
TITLE NOTES   (the Brain's copy — not printed in the document)
{lane: Problem / Situation / Future / Interview / Model} · {exact title} · for {the type of agent} · {the pain — one of the five} · {why: demand / news (dated) / asked / proven / gap / unresearched / starter}
{one line per title — the calendar's titles first, in date order, then the list's; never a link to another channel's video — no reference videos (Mike, 2026-11-23)}
```

### Script (the four formats — ONE video, IN FULL, both forms; the interview is a question list)
**Mike, 2026-11-23: a video is scripted in full, in ONE package of two forms** — **(a) THE BREAKDOWN:** the bullet-point
breakdown of the video with **the hook scripted word for word** at its top (the hook is the one line written out in
full — Mike's own habit; then the points, one line each, the two asks in their places) · **(b) THE FULL SCRIPT:** the
teleprompter script, every word, **8 to 12 minutes** (about 140 spoken words a minute, so 1,100–1,700 words) — the
member pastes it into Instagram's free Edits app, presses record and reads. The `Script` doc holds both: the
breakdown first (one page), then the full script. This is `yt-script`'s **full mode**, run by setup for the first
video at its close and by the Monday Kickoff for each week's video.
TITLE and one meta line (about how many minutes · who it is for · the date, in words — never a kind code) → the one
line that tells the member how to read the page → heavy band `THE BREAKDOWN` (`YOUR HOOK — word for word`, then the
points) → heavy band `THE FULL SCRIPT` with its bands `YOUR OPENING · 0:00` → `THE GUIDE ASK · inside minute 1` →
the body sections (3–5) → `THE CALL ASK · about a third in` → `PAYOFF` → `NEXT VIDEO` → `CHAPTERS (planned — the
real times come from your edit)` → heavy band `THE FIRST SHORT` → the footer (the story used and the facts checked —
the compliance check is never printed). Both calls to action are the kit's CALLS TO ACTION lines, verbatim, in the
law's shape (house rules #15 and #17): the guide inside minute one, the call a third in. **An interview has no
script** — `yt-interview`'s question list (the Interview Prep) is the whole package for an interview week. **The
printed words are the detailed skeleton's** — `${CLAUDE_PLUGIN_ROOT}/skills/yt-script/references/script-format.md`
— and where this summary and that file differ, that file wins. Nothing in a script names the kind of video
("Bucket:", "Lane:"), says "b-roll" to the member ("extra footage"), or speaks of "the member"; "your hook" is the
member's word for the scripted first line. No reference video and no competitor's video anywhere on the page.
("script my first three videos" and its First Batch — Film Day sheet were retired on 2026-11-23: one video a week,
fully.)

### Channel Page (`yt-setup` — the document "Channel Page — [Name]", saved as `Channel Page — [Name] — YYYY-MM-DD`; the text also kept at `exports/channel-kit-YYYY-MM-DD.txt` — the export's file name is unchanged because `yt-setup`'s own walk-through reads it)
To the member this document is **"your Channel Page"** — never a "kit": "your kit" always means the Week 3 Kit, and
"your brand kit" the Week 3 design pieces. (The public page on YouTube is "your channel on YouTube" — never "your
channel page", which would give one name to two things.) It holds all eight pieces, in Studio's order, the click
path above each — **there is no trailer piece** (Mike, 2026-11-23: no channel trailer, anywhere). **Three are marked
"paste today"** — piece 1 (piece 2 goes with it, in the same box), piece 3 and piece 7 — and the chat shows only
those three (`yt-setup` Step 4).
**Plain words only in every printed line:** no skill name, no file path, no folder code — "your guide", "your kit",
"your Brand folder", "your booking link". **Never a bracket or a placeholder link in a piece the member pastes
today:** a fact the Brain does not hold (no booking link, no guide yet) leaves its line out; the one bracket allowed
is the held place for the brokerage's wording while compliance is `unset`. **The click paths are YouTube Studio's
own, checked against YouTube Help on 2026-11-21:** the description, the links, the banner and the picture are under
Customization → Profile and are saved with Publish (top right); Settings → Upload defaults ends with Save and
applies only to videos uploaded from a computer's browser.
Everything inside `{…}` below is a note to the writer and is never printed.
```
CHANNEL PAGE — [MEMBER NAME]
[Channel handle, or "your new channel"]  ·  Known for: [what you're known for]  ·  [the date, in words]
{only while compliance is unset, one line — said here once and nowhere else in the document:}  HOLD UNTIL YOUR COMPLIANCE BASICS ARE SET — say "paste my compliance link" (two minutes), then "repair my channel for agents", then paste.
{only for a channel that does not exist yet, one line:}  First, create your channel — on YouTube click your picture, choose "Create a channel", and name it {the channel name the Brain holds — or, with none on file, their own name}. Everything below pastes into it.   {while compliance is unset the line ends at the name}

──────────────── 1 · CHANNEL DESCRIPTION   (paste today — with piece 2, in one box) ────────────────
   >> PASTE INTO:  studio.youtube.com (YouTube Studio) → Customization → Profile → Description — the opening paragraph; then click Publish, top right
{2–3 sentences: who it's for · what they'll learn · the rhythm ("a new video every week")}

──────────────── 2 · ABOUT SECTION   (goes with piece 1 — the same box) ────────────────
   >> PASTE INTO:  the same Description box, directly below the opening paragraph; then Publish
{opens with the YouTube bio from the kit, as written — refreshed only when the offer, the proof or the guide's link changed · who it serves · the four pillars by name (your niche · helping struggling and new agents succeed · brokerage model breakdowns · agent interviews) · one real proof line, only when the Brain holds one · the call line in the law's shape + the booking link · the guide + its link · the brokerage's wording, or its held place · pieces 1 and 2 together fit YouTube's 1,000-character description box}

──────────────── 3 · LINKS   (paste today) ────────────────
   >> ADD IN:  Customization → Profile → Links → "Add link", one link at a time (its title, then its address); then Publish
   •  {the call's title} — {the booking link}   {each bullet is written Title — address; this one first; no booking link on file → this bullet is left out, never a bracket}
   •  {the guide's title} — {the guide's link}   {second; only when the Week 2 guide was skipped: the starter guide's link, once it exists; no guide yet → left out}
   •  {ONE social — its name} — {its link}

──────────────── 4 · CHANNEL KEYWORDS ────────────────
   >> PASTE INTO:  Settings → Channel → Basic info → Keywords; then Save
{8–12 phrases agents search}

──────────────── 5 · PLAYLISTS ────────────────
   >> CREATE IN:  Content → Playlists → New playlist   (four — one per pillar, in this order: it is the order on your channel's home page)
   •  {[Model] explained}:  {one-line description}
   •  Agent interviews:  {…}
   •  {the niche pillar's playlist, in search language}:  {…}
   •  Helping struggling and new agents succeed:  {…}

──────────────── 6 · CHANNEL BANNER ────────────────
   >> UPLOAD IN:  Customization → Profile → Banner image, then Publish
{the banner is found — this one line, nothing else:}  Your YouTube banner is already made — it's in your Brand folder from Week 3 (banner-youtube.png). Upload it in YouTube Studio: Customization → Profile → Banner image, then Publish.
{the brand kit is on record but the file is not in the folder — this one line:}  Your YouTube banner was made with your brand kit in Week 3 — it's the file banner-youtube.png, where you saved your brand kit. Upload it in YouTube Studio: Customization → Profile → Banner image, then Publish.
{the banner is not found — this one line, then the three lines of words to hand over:}  Your banner comes from your brand kit — in your Claude Design project say "make my brand kit" and it builds your YouTube banner first; then upload it here.
{not found only}  Headline:  {who it's for + what they get}
{not found only}  Subline:  {the rhythm, or the invite in the law's shape}
{not found only}  Keep the words in the centre — TV, desktop and phone crop the banner differently.

──────────────── 7 · UPLOAD DEFAULTS   (paste today — your default video description) ────────────────
   >> SET ONCE IN:  Settings → Upload defaults → Description; then Save (YouTube applies it only to videos uploaded from a computer's browser)
{the default description, and only that, as the one block to paste: line 1 the kit's call line + the booking link (the law's shape; no booking link on file → line 1 is left out, never a bracket) · line 2 the guide + its link · line 3 the compliance and contact line · the brokerage's wording last, or its held place}
Set these by hand on the same page — each has its own box:
   •  Tags:  {a small default set}
   •  Category:  Education
   •  Visibility:  {…}
   •  Language:  {…}

──────────────── 8 · YOUR SPOKEN LINES   (every video) ────────────────
   >> SAY IN:  every video — nothing to paste
The guide (inside the first minute):  "{the kit's spoken guide line — 'comment GUIDE' / 'link in the description' — no kit on file: built from the guide's own record}"
The call (a third of the way in):  "{the kit's spoken call line, in the law's shape — join register: 'If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call].' · open register: 'I'll walk you through it, free, no strings.' — never the brokerage; no kit on file: the law's shape from the offer}"
Pop-ups:  {the kit's video pop-up lines — the guide's and the call's}   ·   End cards:  {the kit's end-card lines}
Pop-ups are the few words that come up on screen while you say each line; the end card is your video's last screen. Both are added when the video is edited.

{no ninth piece — there is no channel trailer (Mike, 2026-11-23)}

{before saving, the compliance check — never printed: nothing negative about any brokerage or person · no pay figures · the brokerage's wording in place, or its held place while compliance is unset}
```

### Kickoff Brief (the Monday Kickoff — `yt-briefing`, scheduled or on demand; saved as `Kickoff Brief — [title] — YYYY-MM-DD` in the video's folder; the Brain Board's text is the Kickoff's NOTE, kept at `exports/youtube-kickoff-YYYY-MM-DD.txt` — never the brief; the same sections are written into the video's board card under the card page's emoji headings, Status → Scripted)
Member-facing: **the week's video, done IN FULL** (Mike, 2026-11-23: one video a week, fully — never a batch of
summaries, never a "start"): **THE BREAKDOWN** — the bullet points with the hook scripted word for word — and **THE
FULL SCRIPT** — the teleprompter script, 8 to 12 minutes — both in this one document (and the same `Script` saved in
the video's folder); the thumbnail sheet; the title and description started. An interview week with a named guest
is **the question list, no script** (the GUEST block). **No reference video, no competitor's video or summary**
anywhere in the brief. The sections run in the locked long-form card page's order (`notion-board-spec.md`). **The
document's bands are in the member's words; the card keeps the shared spec's headings** (a card-section heading is
never renamed here) — band → card section: YOUR HOOK → 🎯 THE HOOK · THE BREAKDOWN and THE FULL SCRIPT → 🎬 SCRIPT ·
YOUR THUMBNAIL SHEET → 🖼 THUMBNAIL BRIEF · YOUR TITLE AND DESCRIPTION → 🔍 SEO PACKAGE · YOUR GUIDE AND YOUR CALL →
🧲 THE RESOURCE · GUEST → 🎙 GUEST · NOTES FOR FILMING → 📋 ASSETS & NOTES · PUBLISH IT → ✅ PUBLISH IT · AFTER IT'S
OUT → 📊 AFTER IT'S OUT. On the card each section is replaced in place, never stacked; a card seeded from the
calendar already holds THE HOOK and ASSETS & NOTES (the brief), and the Kickoff fills the rest and lays down the six
publish boxes with their click paths. **An interview week with no guest named gets no brief of its own** (nothing is
drafted to nobody): the week's video is the next one from the member's topic pillars, and this brief is written for
that video. Everything inside `{…}` is a note to the writer and is never printed.
```
KICKOFF BRIEF — "{title}"
Week of {Monday's date, in words}  ·  For: {the type of agent}  ·  {A topic video: {the pillar's name} / An interview / A model video}  ·  Recording: {the day, in words}  ·  Publishing: {the day, in words}

──────────────── YOUR HOOK   (word for word) ────────────────
Title:  {the exact title}
{the hook, scripted word for word — the one line of the breakdown written out in full: the viewer's situation → the tension → what they'll have by the end}

════════════════════════════════════════════
THE BREAKDOWN   (the video in bullets — read this on the day)
════════════════════════════════════════════
   •  YOUR HOOK — {the hook again, word for word}
   •  THE GUIDE ASK — inside minute 1 — {the kit's spoken resource line, verbatim; no guide on file yet → left out}
   •  {section 1's label} — {its point, one line}
   •  {section 2's label} — {…}   {3–5 sections; the steps of the member's own method are the teaching material}
   •  THE CALL ASK — about a third in — {the kit's spoken call line, verbatim, in the call-to-action law's shape — the person · their help · free · to run this; never the brokerage, never a promise of your time}
   •  THE PAYOFF — {the promise delivered, one line}  ·  THE NEXT VIDEO — {its title}

════════════════════════════════════════════
THE FULL SCRIPT   (about {n} minutes — paste it into the Edits app's teleprompter, press record, read)
════════════════════════════════════════════
{the whole script, every word, 8 to 12 minutes — the Script skeleton's bands: YOUR OPENING · THE GUIDE ASK · the sections · THE CALL ASK · PAYOFF · NEXT VIDEO; the same text is saved as this video's Script}
   {an interview with a named guest: THE BREAKDOWN and THE FULL SCRIPT are left out — an interview has no script; the question list is in the GUEST block}

──────────────── YOUR THUMBNAIL SHEET ────────────────
{your thumbnail sheet for Higgsfield — for each of the three directions the image prompt to paste, which of your photos to upload and the 3 to 5 words to add; one recommended — the same sheet saved as its own doc (the Thumbnail Sheet skeleton)}

──────────────── YOUR TITLE AND DESCRIPTION   (started) ────────────────
Your title:  {the exact title}   ·   Spare titles (only if this one is slow after a month):  {two}
Description, lines 1–3:  {line 1 the kit's call line + the booking link (the law's shape) · line 2 the guide's link — no guide on file yet → left out · line 3 the compliance and contact line}   ·   Summary (about 150 words):  {…}
Tags:  {…}   ·   Hashtags:  {…}   ·   Pinned comment:  {the guide's link + "comment GUIDE and I'll send it" + one question; no guide on file yet → the question and the call alone}   ·   Chapters:  their names come with your script, their times after your edit
{the disclosure block is always the last block of the description}

──────────────── YOUR GUIDE AND YOUR CALL ────────────────
{this video's two calls to action — the guide by name, its keyword GUIDE and its link (from the Brain's current-guide record) · the call: the booking link; no guide on file yet → the call alone}

{no REFERENCE VIDEO band — Mike, 2026-11-23: no reference videos, anywhere}

──────────────── GUEST ────────────────
{this band only for an interview with a NAMED guest — anyone successful in the member's upline, downline or brokerage: the guest · the story the title promises · the outcome sentence · THE QUESTION LIST — the five steps with the questions for this kind of guest (no script: this list IS the week's package) · the two lines that introduce them · the call line in the law's shape · the invite draft · their okay to publish and its state · what to ask them to share (the three sentences) — no guest named → this band is left out and nothing is drafted to nobody}

──────────────── NOTES FOR FILMING ────────────────
Who it's for and the pain:  {the type of agent · the pain, in their words}
Why this week:  {the plan's reason for this title, in plain words — what agents search · a dated news item · a question an agent asked you · a gap on your channel · "from the starting set — not yet checked against search"; never another channel's video}
Story to use:  {one of your stories, not used recently — none on file → this line is left out}
Extra footage and filming notes:  {…}   ·   Your brokerage's lines to say:  {license display · brokerage name, as your compliance wording says}
When it's filmed, open a new chat and say "edit my YouTube video" (or "edit my interview") — your AI Editing Studio edits it.

──────────────── PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO ────────────────
{six tick boxes, in Studio's own order, each with where to click — the video's own values arrive when the full package is written ("make my attraction video"); never ticked by the system}
☐ 1 · Title — top right, Create → Upload videos → choose your edited file; then Details → Title: paste your title   {a first video only, add: "The first time, YouTube asks you to verify your account by a text or a call, at youtube.com/verify — you need it once, to add your own thumbnail and to upload a video longer than fifteen minutes."}
☐ 2 · Description — Details → Description: paste your description (line 1 your call and booking link · line 2 your guide · line 3 your compliance and contact line). If the box already holds your default lines, select everything in it and paste this over it.
☐ 3 · Thumbnail — Details → Thumbnail → Upload file: the thumbnail you made in Higgsfield, from this video's folder. If Studio shows "Test & compare" there and you made all three, upload the three — YouTube picks the winner.
☐ 4 · Playlist — Details → Playlists: tick {the playlist's exact name}. If it is not in the list yet, create it there, with this exact name. Then, lower on the same screen, Audience: "No, it's not 'Made for Kids'" — YouTube will not go on without an answer.
☐ 5 · End screen — Video elements → Add an end screen: the next video and the playlist named in your title and description (your first video: the playlist alone), and Subscribe
☐ 6 · Pinned comment — first make it public: Visibility → Public, then the button at the bottom right (Publish or Save); then, on the video's own page, post your pinned comment, then ⋮ → Pin
All six ticked? Say "my video is published"{with a content board, add: " and I'll move its card to Published"}.

──────────────── AFTER IT'S OUT ────────────────
{in the document this band is left out — a band with nothing in it is never printed (house rules #24); on the card its section stays, empty, until the video is out: "how did my video do" writes the live link, the numbers and the agents who named the video; the Monthly Channel Review writes the same when it is switched on}

{before saving, the compliance check — never printed: nothing negative about any brokerage or person · no pay figures · no former brokerage named · the disclosure block in the description}
```

### SEO Package
The member's words for this document are **"your title and description"** — the printed title and every band say
so. The `### SEO Package` heading above and the saved file's name, `SEO Package — [title] — YYYY-MM-DD`, are the
names other files find it by and stay as they are. The title is never re-chosen here: the one already chosen is
printed first, word for word, and the two spares sit under it. Everything inside `{…}` is a note to the writer
and is never printed.
```
{VIDEO TITLE} — YOUR TITLE AND DESCRIPTION
For {the type of agent}  ·  {A topic video: {the topic's name} / An interview / A model video}  ·  {the date, in words}
{only while compliance is unset, one line:}  HOLD UNTIL YOUR COMPLIANCE BASICS ARE SET — say "paste my compliance link" (two minutes) before this video goes out.   {line 3 and the disclosure block then keep their place as one bracketed line each, never invented}

──────────────── YOUR TITLE ────────────────
{the title already chosen, word for word — the one the script and the thumbnail were built on; none chosen yet → the recommended one, stated, never offered as a choice}

──────────────── SPARE TITLES   (only if this one is slow after a month) ────────────────
1.  {a spare title}
2.  {a spare title}

──────────────── THUMBNAIL WORDS ────────────────
{3–5 words, different from the title}  ·  (the three thumbnails are made in Higgsfield from your thumbnail sheet)

──────────────── DESCRIPTION ────────────────
{line 1: the kit's call line, verbatim, + the booking link — the law's shape: the person · their help · free · to run this (the join register on Join-gated package allowed: yes or unknown; the open register only on no) — never the brokerage; no booking link on file → left out, never a bracket}
{line 2: the guide — "Free guide — {the guide's title}: {its link} (or comment GUIDE and I'll send it)"; "Questions to Ask Before You Choose a Sponsor" and its download link only when the Week 2 guide was skipped; no guide yet → left out}
{line 3: the compliance and contact line — the brokerage name and license display as the member's compliance file requires, then the contact line their Brain lists (the handles, a phone or an email — only what is on file); the full disclosure block stays the LAST block}
{150–250 word summary in the member's voice — no pay words (splits, caps, fees, rev-share tiers, stock, income), no promise of your time}
{after the edit only: the chapters with their real times, the first at 00:00 — moved here from the block below}

   WATCH NEXT
   {2–3 of the member's own videos, the next logical one first; a first video, or none published yet → this block is left out — never a link to a video that does not exist}

──────────────── CHAPTERS — ADD AFTER YOUR EDIT ────────────────
{before the edit: the chapter NAMES alone, in order — outside the text to paste; a time is never estimated from a script. After the edit: the real times go beside the names, the block moves into the description above, and this band is left out}

──────────────── TAGS ────────────────
{four to six, specific — never a broad one}

──────────────── HASHTAGS ────────────────
#{…}  #{…}  #{…}

──────────────── PINNED COMMENT ────────────────
"{the guide's link + "comment GUIDE and I'll send it" + one real question inviting agents to comment their situation — never a keyword of the plugin's own; an interview: a line of thanks to the guest by name; no guide yet → the question and the call alone}"

──────────────── PLAYLIST AND END SCREEN ────────────────
Playlist:  {this video's playlist, by its exact name on the channel — step 4 of the publish steps uses it}
End screen:  {the next logical video — a first video: the playlist alone} + subscribe   {step 5 of the publish steps uses it}
Info card:  {another of your videos, or the playlist, at the moment the script points to it — never the guide and never an outside link; nothing to point to yet → this line is left out}

──────────────── WHY THESE   (three plain sentences, for you — not for pasting) ────────────────
{the phrase the title uses and where it was seen · why the description opens with the call and then the guide · the tags are simply the phrases agents type. Never a claim about demand, ranking or views that was not seen}

──────────────── DISCLOSURE BLOCK   (always the LAST block of the description) ────────────────
{brokerage name + license as required · the brokerage disclaimer verbatim · income disclaimer only if earnings were mentioned · AI-likeness line on clone content}

{no content board only — the six publish steps are printed here as the last block, with this video's own values and the editing line above them (the same six lines as in the Kickoff Brief skeleton, without the tick boxes' card wording); with a board they are on its card and this block is left out:}
──────────────── PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO ────────────────
When it's filmed, open a new chat and say "edit my YouTube video" (or "edit my interview") — your AI Editing Studio edits it.
{the six steps}
```

### Interview Prep (`yt-interview` — saved as `Interview Prep — [guest] — YYYY-MM-DD` in the video's folder)
Every section below is something `yt-interview` Steps 3–6 produce. **An interview has NO script — the question list
is the package** (Mike, 2026-11-23); the INTRO and OUTRO bands below are the points to hit in the member's own
words, never a script to read. **Written only for a NAMED guest — anyone successful in the member's upline, downline
or brokerage** (Mike, 2026-11-23: "if they have someone who did it with their value proposition, great — otherwise
just interview anyone successful"). Nobody named → no Interview Prep is written and nothing is drafted to nobody;
the member reads, word for word: *"No guest named yet, so this week's video is '[title]', from your topic pillars.
Your guest is anyone successful in your upline, downline or brokerage — the day you name someone, say 'set up an
agent interview'."* Two kinds of guest, two sets of questions: **an agent who joined the member**, and **any other
guest** (their sponsor, a leader in their upline, a peer at their brokerage, anyone successful they want to talk
with) — the second kind is never asked what made them move or what it has been like "since partnering", and their
title never says they used the member's method. Everything inside `{…}` is a note to the writer and is never printed.
```
INTERVIEW PREP — {GUEST NAME}
The story: {what the title promises}  ·  For: {the type of agent this story lands with}  ·  Recording: {the day, in words}  ·  Their okay to publish: {on file / asked {the date, in words} / not asked yet}

──────────────── THE OUTCOME THIS VIDEO DELIVERS ────────────────
{one line — "by the end, a {type of agent} watching should believe {X}" — what a viewer who has never heard of the guest leaves with}

──────────────── TITLE OPTIONS   (what changed for them) ────────────────
1.  {never a "tell me your story" title — an agent who joined you: How {first name} {what changed} — and used {the mechanism} · any other guest: How {first name} {does the thing} — {the constraint}}   ← recommended
2.  {…}
3.  {…}
Thumbnail words (different from the title; both faces on it):  {3–5 words}

──────────────── HOW YOU INTRODUCE YOUR GUEST   (before they speak — true facts only) ────────────────
{two lines in your voice — an agent who joined you: what they have said changed · who they were a year ago · why you wanted them on; any other guest: who they are and why you asked them}

──────────────── YOUR QUESTION LIST   (not a script — the five steps, any order; this is the whole package) ────────────────
{an agent who joined you:}
   BEFORE — {what business was like before: 2–3 open questions}
   THE SHIFT — {what made them decide to move, what the hesitation was: 2–3}
   SINCE — {what it has been like since partnering — support, training, community, in their words: 2–3}
   THE RESULTS — {what changed, in their words — freedom, time, support, a milestone; never a dollar or income figure: 1–2}
   ADVICE — {for an agent standing where they stood: 1–2}
{any other guest — these five instead, never the five above:}
   THEIR START — {how they got into the business: 1–2}
   THE METHOD — {the one thing they do that other agents should hear, step by step: 2–3}
   THE MISTAKE — {what they would skip if they started again: 1–2}
   WHAT IT CHANGED — {in their words, no figure: 1–2}
   ADVICE — {for an agent starting it this week: 1–2}
   {the extra steps for a guest who joined you — new agent: the first-30-days routine · turnaround: what they changed first (no names, no blame) · top producer: what changed in their time · team leader / broker-owner: what they kept, what overhead disappeared · attracted their first agent: how that conversation happened}
   While you film:  the guest is the star · never interrupt · let emotion sit · add a layer only after they finish · redirect on camera if they knock a brokerage or a person (that part is cut)

──────────────── YOUR INTRO — the points, not a script   (record LAST, after you know the story — 45–75 s) ────────────────
{bullets, in your own words on the day: the story as the title promises it → who this is for → two or three specific things coming → one honest line about the guest → the guide ask in one breath (only when a guide is on file) → "let's get into it"}

──────────────── YOUR OUTRO AND INVITATION — the points   (30–45 s) ────────────────
{bullets: thank the guest and name the one thing to take from them → your call line — the kit's spoken call line, word for word (no kit on file: the law's shape; the lessons, the templates and the community named only when the offer's value stack lists them) — with the lead-in "the way {guest} did" only for a guest who joined you; never the brokerage, never a promise of your time → the next video → the end screen}

──────────────── THE INVITE   (DM or email, in your voice — you send it) ────────────────
{why them · the 30–45 minute format · one line that the recording link comes the day before · "you are the story" · the one prep line — a guest who joined you: "think about where you were before and the moment things changed"; any other guest: "think about the one thing you do that other agents should hear"}
Their okay, in one line:  {the plain okay to publish, use clips, and share their name as written — and, for a guest who has not joined you, one honest sentence that the video ends with your own invitation to agents}

──────────────── WHEN THEY SAY YES   (the booking — filled when the guest agrees) ────────────────
Two recording times:  {slot 1 — the day, in words, and the time}   ·   {slot 2}
The reply to send:  "{two lines in the member's voice: the two times, 'pick whichever suits you', the recording link comes the day before}"
Guest prep note:  {the copy block the member sends — what to expect · 30 to 45 minutes · the first three questions of THIS guest's own question map, word for word · how to look and sound good on camera}
The day before:  open a new chat and say "prep me for a guest recording" — your AI Editing Studio sets up the recording and gives you the link to send {guest}. When it's filmed, open a new chat and say "edit my YouTube video" (or "edit my interview") — your AI Editing Studio edits it.   {only when the member's editor does not record a guest (yt-interview Step 6b, item 3), the first sentence reads instead: "Record this one on any video call that saves the recording, and send {guest} that link the day before."}
Booked:  {the date, the time and the calendar title — "on your calendar" only when the member said yes to the hold}

──────────────── WHAT TO ASK YOUR GUEST TO SHARE   (send when it goes live) ────────────────
{the three sentences: share it to your story · post it with a line of your own · send it to three agents — a guest who joined you: who are where you were; any other guest: who would use it — with the link and the clips}

{before saving, the compliance check — never printed: nothing negative about any brokerage or person in any cut (the guest's answers too) · no pay figures · no former brokerage named · their okay recorded · the disclosure block in the description}
```

### Thumbnail Sheet (`yt-thumbnail` — the ONE shape, for Higgsfield; saved as `Thumbnail Brief — [title] — YYYY-MM-DD` in the video's folder — the file name is unchanged so the board and the Kickoff find it)
The cohort's members make their thumbnails in **Higgsfield** (the owner, 2026-11-14) — nowhere else. The
sheet carries, for each of the three directions, what the member takes there: the image prompt to paste, which of
their own photos to upload, and the 3 to 5 words to add. One line of why for each direction stays in the chat; the
scoring is silent — no score, no why and no pattern note ever goes on the sheet. This plugin writes words and
prompts; it never makes an image. To the member it is "your thumbnail sheet". The kind of video is written in
plain words ("a topic video", "a conversation with an agent", "your brokerage, explained") — never a bucket or a
lane word. Everything inside `{…}` is a note to the writer and is never printed.
```
THUMBNAIL SHEET — "{VIDEO TITLE}"
For Higgsfield, where you make your thumbnails: upload your photo, paste the prompt, add the words.
Video: {the kind of video, in plain words — "a topic video" / "a conversation with an agent" / "your brokerage, explained"} · for {the type of agent} · the feeling: {the fear to avoid / the outcome to reach}
All three: a 16:9 frame at 1280×720, with clear space where the words go.

──────────────── THUMBNAIL 1   (the recommended one) ────────────────
Photo to upload:  {which of the member's own photos — named the way it is in their Brand folder, or one of the five they took on their filming day, named by what it shows ("your surprised photo from filming day") — or, when the expression is missing, "take this one first: {the expression to shoot}"}
Prompt to paste:
{one ready-to-paste paragraph: the scene · your expression · where you sit in the frame (about a third of it, left or right, eyes toward the open side) · the background · your brand's colours in plain words (the hex in brackets) · "16:9 frame, 1280×720, clear space on the {left / right / top} for text, no text in the image"}
Words to add (3–5):  {the words — never the title's}

──────────────── THUMBNAIL 2 ────────────────
Photo to upload:  {…}
Prompt to paste:
{the same shape — the one change from thumbnail 1}
Words to add (3–5):  {…}

──────────────── THUMBNAIL 3 ────────────────
Photo to upload:  {…}
Prompt to paste:
{the same shape — the one change from thumbnail 1}
Words to add (3–5):  {…}

────────────────────────────────────────────
Rules — 3 to 5 words · the words differ from the title · your face about a third of the frame · one supporting element at most · readable on a phone{only where the member's brokerage rules ask for it, add: " · your brokerage's mark, never another brokerage's · say it is an AI-made picture if your brokerage's rules ask you to"}
When they're made: drop the finished thumbnails into this video's folder (Content → Long-Form → {video}) and say "my thumbnail is done".
```

### Starter Resource (`yt-leads` — the fallback for a member who skipped the Week 2 lead magnet: built ONCE, in Week 5, while `## Current magnet` is empty; saved as `Starter Resource — YYYY-MM-DD` in `03 · Content/Guides/`)
Questions only — the doc never answers them, never names a brokerage as the answer, never carries a figure. One
page, in the member's voice, for the primary avatar. Ten to twelve questions — fewer when a question about a track
record the member does not have yet, or about something their own model does not have, is left out; never padded;
the standard twelve live in `yt-leads` 1a. Sub-band labels stay under 70 characters. **This page is handed to
agents, so nothing but its own words prints on it** — no check line, no note to the writer. Everything inside
`{…}` is a note to the writer and is never printed.
```
QUESTIONS TO ASK BEFORE YOU CHOOSE A SPONSOR
From {Member Name}  ·  For {the type of agent, in their words}  ·  {Month Year}
{only while compliance is unset, one line — for the member, removed before the page is shared:}  HOLD UNTIL YOUR COMPLIANCE BASICS ARE SET — say "paste my compliance link" (two minutes) before you share this page.

──────────────── WHY THESE QUESTIONS ────────────────
{3–4 sentences in the member's voice: you're choosing a sponsor, not just a brokerage · the brokerage is the vehicle, the leader is the growth · ask these of anyone you're considering}

──────────────── THE MODEL   (how it works, who it fits) ────────────────
   1.  {question}
   2.  {question}
   3.  {question}

──────────────── THE SPONSOR   (the person, not the company) ────────────────
   4.  {question}
   5.  {question}
   6.  {question}
   7.  {question}

──────────────── THE SUPPORT   (who, and for what) ────────────────
   8.  {question}
   9.  {question}

──────────────── THE MONEY   (what to ask, not what to expect) ────────────────
   10.  {question}
   11.  {question}
   12.  {question}
{questions only — no split, cap, fee, tier, stock or income figure appears here, not even as an example}

──────────────── THE NEXT STEP ────────────────
{one warm line in the member's voice, in the law's shape — "want these answered for your situation? grab a call — I'll walk you through it, free, no strings" → the booking link; no booking link on file → the member's own way to be reached, as the Brain holds it}

────────────────────────────────────────────
{the disclosure footer: brokerage name and license as the member's compliance file requires · the brokerage disclaimer verbatim · no income disclaimer — no earnings are mentioned; compliance unset → its held place, never invented}
{before saving, the compliance check — never printed on this page: nothing negative about any brokerage, sponsor or person · no brokerage named as the answer · no pay figures · the disclosure footer present}
```

### Model Breakdown (`yt-model-breakdown` — saved as `Model Breakdown — [title] — YYYY-MM-DD` in the video's folder)
To the member the file behind this video is "your model notes". A part about something the member's model does
not have (no revenue share, no sponsor, no equity in the model notes) is left out — never written as if it
existed. Everything inside `{…}` is a note to the writer and is never printed.
```
{VIDEO TITLE} — MODEL BREAKDOWN
For {the type of agent}  ·  A model video  ·  Your model notes were last checked {Month Year}  ·  {the date, in words}

──────────────── THE FACTS, WITH THEIR SOURCES ────────────────
   •  {fact used} — {source document, date}
{every fact the outline uses is listed here; pay figures never appear here or on camera}

──────────────── THE OUTLINE ────────────────
{each part below is its own sub-band, in this order, with its lines under it — the two calls to action in their places, quoted from the kit:}
   ──── YOUR OPENING ────
   {the question they typed, answered honestly — no "welcome back"}
   ──── THE GUIDE ASK ────
   {the kit's spoken guide line — only when a guide is on file}
   ──── OVERVIEW ────
   {history, and how the brokerage describes itself}
   ──── HOW PAY IS STRUCTURED ────
   {the ideas, no figures — "the actual numbers for your situation — we go through those on the call"}
   ──── TOOLS AND TECHNOLOGY ────
   {what is included · a gap is named only when the member's own program holds what fills it}
   ──── SUPPORT AND TRAINING ────
   {the brokerage's support, then the member's program as the offer states it}
   ──── BEYOND CLOSINGS ────
   {only what the model notes hold — the ideas, never a projected value or an earnings figure}
   ──── CULTURE AND COMMUNITY ────
   {what it actually feels like}
   ──── WHO IT'S FOR ────
   {said fairly}
   ──── WHO IT'S NOT FOR ────
   {said fairly}
   ──── THE CALL ASK ────
   {the kit's spoken call line, the method named, then "and the numbers for your situation — on the call" · the next video, only when a published video exists to point at}

──────────────── THE MYTHS THIS ANSWERS   (what agents keep asking, in their words) ────────────────
{only when the Brain holds what agents keep asking — nothing on file → this band is left out, never invented}
   •  "{the myth or fear}" → {the fact, with its source}
   {comparison videos only: Mike's caution stated to the member — facts only, sourced and dated, what each offers and who it fits, a trade-off named only for the member's own model; never a negative word about a brokerage or person}

──────────────── TITLE SET ────────────────
1.  {title}   2.  {title}   3.  {title}   ·  thumbnail words (different from the title): {3–5 words}

──────────────── WHEN TO RE-MAKE IT ────────────────
Re-make this video when your brokerage changes its model, or in a year — your model notes were last checked {Month Year}.

{before saving, the compliance check — never printed: nothing negative about any brokerage or person, by name or by hint · no pay figures · the disclosure block in the description}
```

### YouTube Deep Dive (`yt-analytics` — saved as `YouTube Deep Dive — [Month YYYY] — YYYY-MM-DD`; the text also kept at `exports/youtube-read-YYYY-MM-DD.txt` — its own name, never `youtube-review-*`; no credibility stamp)
**Written only when at least one video is published.** Nothing published yet → no document, no table of zeros and
no list of what is missing: the member reads the skill's own three lines (what they have built, their first video
by title and its recording day, and the phrase that makes it). The band names are the deep-dive guide's (1.8
says "your channel on YouTube", because "your Channel Page" is the name of the member's document). Everything
inside `{…}` is a note to the writer and is never printed.
```
YOUTUBE DEEP DIVE — [MEMBER NAME] — [MONTH YYYY]
The last 90 days  ·  Read from: {your live numbers / your Studio screenshots / what is public on your channel}  ·  {the date, in words}

════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{the verdict — three plain sentences}
   THE ONE MOVE ......... {exactly one action}
   DO THESE THREE THIS WEEK ......... 1. {…}  2. {…}  3. {…}
   YOUR NUMBERS AT A GLANCE
   {each number with its plain meaning — "how many people click", "how long people keep watching"}
   WHAT'S IN THIS REPORT
   {for each part, one of: read live · from your Studio screenshots · not available}

════════════════════════════════════════════
PART 1 — YOUR CHANNEL
════════════════════════════════════════════
   1.1 How you grew  ·  1.2 What's pulling — by content type  ·  1.3 Titles & thumbnails  ·  1.4 Your best openings
   1.5 Where viewers come from  ·  1.6 What viewers are saying  ·  1.7 Where views stop turning into calls
   1.8 How often you post & your channel on YouTube
{every finding: what we found · why it matters to you · do this · the proof; numbers in tables}

════════════════════════════════════════════
PART 2 — OTHER ATTRACTION CHANNELS   (what they do well, never what is wrong with them)
════════════════════════════════════════════
════════════════════════════════════════════
PART 3 — WHERE YOU SHOW UP WHEN AGENTS SEARCH
════════════════════════════════════════════
════════════════════════════════════════════
PART 4 — THE OPENINGS
════════════════════════════════════════════
{three to five openings, each a four-line card: what we found · why it matters to you · do this · the proof}
════════════════════════════════════════════
PART 5 — YOUR NEXT 30 DAYS
════════════════════════════════════════════
{keep · fix · the exact titles at your pace — four or five at one a week, eight or nine at two · THE ONE MOVE, repeated}
════════════════════════════════════════════
APPENDIX — THE FULL NUMBERS
════════════════════════════════════════════
```
Structure and method: `${CLAUDE_PLUGIN_ROOT}/skills/yt-analytics/references/deepdive-guide.md`.

### Monthly Channel Review (`yt-triggers`'s scheduled run, or "run my monthly channel review" in chat — saved as `Monthly Channel Review — [Month YYYY] — YYYY-MM-DD`; the text also kept at `exports/youtube-review-YYYY-MM-DD.txt` so the Brain Board can read it; never the live data connection — it reads what is on record; no credibility stamp; the same run writes each published card's 📊 AFTER IT'S OUT and one dated YouTube block in the Brain's performance ledger)
The live connection reads public data only; how many people click, how long they keep watching and how they found
a video live inside YouTube Studio. So the review **uses the month's Studio screenshots when they are on record** (a
`YouTube Studio numbers` block for the month in the performance ledger — written by "add my attraction Studio
numbers") **and says so**; when they are not, it says nothing about them in the body — the closing band is the one
place the screenshots are named (a missing thing is said once) — and **it ends with the stated step once a video is
published**, told, never asked. **The band names below are the task prompt's, word for word — the task prompt is
the source** (`skills/yt-triggers/references/monthly-review-task-prompt.md`, step 7); where this skeleton and the
prompt differ, the prompt wins. A band with nothing to say is left out — never "none", never a zero. Plain words:
"your four pillars", "a topic video", "interviews", "your model video", "your Game Plan", "your pace" — never
"lane", "cadence", "packaging", "pipeline", "ledger", "retention" or "click-through rate"; never another channel's
video. Everything
inside `{…}` is a note to the writer and is never printed — a band's "only when" note is one of them, so a band
label carries its name and nothing else.
```
MONTHLY CHANNEL REVIEW — [MEMBER NAME] — [MONTH YYYY]
{the month, in words}  ·  {only when they are on record: with your Studio screenshots of {month}}  ·  {the date, in words}

──────────────── THE MONTH IN ONE LINE ────────────────
   {one sentence, kindly — a month on plan is a month on plan; never "behind", never a grade}

──────────────── WHAT YOU PUT OUT ────────────────
   {pipe table: planned · published · by kind — topic videos · interviews · your model video; whether your pace held}
   {no new video in the month → no table, this one sentence instead: "No new video in {Month} — your next one is '{title}', set for {the day}."}

──────────────── WHO REACHED OUT ────────────────
   {this band only when a video was named — no video named → the band is left out}
   {pipe table: video · comments · conversations · calls booked — counted from the Brain's records, never estimated}

──────────────── YOUR STUDIO NUMBERS ────────────────
   {this band only when this month's screenshots are on record}
   From the Studio screenshots you added on {the date, in words}:
   {pipe table: video · how often YouTube showed it · how many people clicked · how long people kept watching · views}
   {one line: how people found the videos and what they typed · one line: where people stopped watching the most-watched video}

──────────────── YOUR INTERVIEWS ────────────────
   {this band only when a guest is named — nobody named → the band is left out and nothing about interviews is counted or said}
   {invited · booked · recorded · published; the next guest to invite}

──────────────── DRAFTS WAITING ────────────────
   {this band only when there is one — otherwise left out}
   {the Monday Kickoff's drafts that are not made into a video yet, by title — three or more → one general line, never a list}

──────────────── ONE TITLE TO REDO ────────────────
   {this band only when a click number is on record and calls for it}
   {one new title and the thumbnail note, and why — from this month's Studio numbers; a month of clicks, never day one; the 6–10% guide is named as Mike's own, from his lesson, never as an industry number}

──────────────── WHERE MOMENTUM SLOWED ────────────────
   {this band only when the Brain's records show it — a month that went to plan → the band is left out}
   {name ONE, kindly — publishing · interviews, only when a guest is named · views that did not turn into conversations}
   {fewer than three months of videos → one line instead: in the first three months making the videos is what counts. Never guilt.}

──────────────── YOUR ONE NEXT STEP ────────────────
   {exactly one action for next month — one sentence, doable, tied to the next videos on the Game Plan}

──────────────── NEXT ON YOUR PLAN ────────────────
   {the titles in order from the calendar — four or five at one a week, eight or nine at two; a guest to invite first only when one is named; an interview row with no guest named gives its week to the next topic video and nothing is said about it here}
   {the move to two a week, when due — the task prompt's fixed words, a proposal the member answers with "change my YouTube pace"}

──────────────── TO MAKE NEXT MONTH'S REVIEW SHARPER ────────────────
   {this band only when at least one video is published — the stated step, the task prompt's words:}
To make next month's review sharper, take three screenshots in YouTube Studio in the last days of the month and drop them into a chat with the words "add my attraction Studio numbers":
1.  In the left menu click Insights (it used to say Analytics), then the Content tab — screenshot that page.
2.  In the left menu click Content, point at your most-watched video and click Insights, then the Reach tab — screenshot it.
3.  Same video, the Engagement tab — screenshot it.

{before saving, the compliance check — never printed: no "cardinal rules" line and no status word at the foot of the review}
```
**Nothing published yet — the short review** (the task prompt's step 2b: no YouTube row at `Published` in the
content log — the normal state of a member's first weeks). The document has four bands and nothing else — THE MONTH
IN ONE LINE · YOUR NEXT VIDEO · NEXT ON YOUR PLAN · YOUR ONE NEXT STEP: no table, no counts, no Studio band, no
"drafts waiting", no "where momentum slowed", no screenshots step and no two-a-week line. Never a table of zeros,
never guilt, never an apology for being new. The lines are the task prompt's own; where this skeleton and the
prompt differ, the prompt wins:
```
MONTHLY CHANNEL REVIEW — [MEMBER NAME] — [MONTH YYYY]
{the month, in words}  ·  {the date, in words}

──────────────── THE MONTH IN ONE LINE ────────────────
   Your Game Plan is built and your first video is ready to make: "{title}", set for {the recording day, in words}.
   {{title} is the first row on the plan that is not an interview with no guest named; a date already past → "ready whenever you are" in place of "set for …" — never "overdue", never "behind"; a channel whose baseline shows videos already out → "your first video on this plan", never plain "your first video"}
   {no calendar and no Game Plan document → this one line instead, and the three bands below are left out: Your first video is next — say "build my attraction game plan" and I map it.}

──────────────── YOUR NEXT VIDEO ────────────────
   "{title}" — {the recording day, in words — or "ready whenever you are"}

──────────────── NEXT ON YOUR PLAN ────────────────
   {the next titles, in order}

──────────────── YOUR ONE NEXT STEP ────────────────
   Record "{title}" — say "make my attraction video: {title}" to get it ready to film.
```

### Repurposing Pack
**Only the bands of the pieces that were written** (`yt-repurpose`): the three clip scripts and the three
conversation starters, always; one email only when the member has a list to send it to; a blog post only when the
member asked for one. No swipe-post band and no stories band — the short-form system writes its own. To the member
the three are "your three clip scripts"; their band keeps the heading `SHORTS (3)` and the labels `SHORT 1` · `SHORT
2` · `SHORT 3`, because the Monday plan reads them from the pack's export by those names. Everything inside `{…}`
is a note to the writer and is never printed.
```
{VIDEO TITLE} — REPURPOSING PACK
From your video's script  ·  {the date, in words}

════════════════ SHORTS (3) ════════════════
SHORT 1 — {angle}
   {how it opens → one point → the ask: "comment GUIDE", or the kit's call line → the caption and hashtags}

{only when the member has a list:}
════════════════ EMAIL (1) ════════════════
Subject:  {…}
{body + the ask in the law's shape — the guide, or the kit's call line}

{only when the member asked for one:}
════════════════ BLOG (1) ════════════════
Title:  {…}
{body}

════════════════ CONVERSATION STARTERS (3)   (ready to send to an agent you know — you send) ════════════════
   1.  {an opener the member can send an agent who'd care about this video — no pitch}
```

Same shape every time, in the member's own voice. This is the standard for what lands in their workspace.
