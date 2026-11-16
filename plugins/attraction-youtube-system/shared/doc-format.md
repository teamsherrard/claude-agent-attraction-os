# Document Format — the house style for EVERY saved document

Every deliverable is rendered to a **clean, formatted `.docx`** in one neutral house style — the same look for
every member (no colour, no per-member branding). The skill writes the **structured text** defined below (CAPS
section bands, `•` bullets, `Label:` lead-ins, simple aligned tables); the shared renderer turns that into real
Word formatting — headings, bullet lists, tables — automatically. **Do NOT save flat `text/plain`.**

**How to read this file — it is long; never read it whole (usage discipline, house rule #8).** Read the part above
`## Per-doc skeletons` once (the saving steps, the look, the grammar). Then read ONLY the skeleton you are about to
fill: search this file for its heading and read from that heading to the next `###`. The skeletons, by heading:
`### YouTube Game Plan` · `### Script` · `### First Batch — Film Day` · `### Channel Page` · `### Kickoff Brief` ·
`### SEO Package` · `### Interview Prep` · `### Thumbnail Sheet` · `### Lead Map` · `### Starter Resource` ·
`### Model Breakdown` · `### YouTube Deep Dive` · `### Monthly Channel Review` · `### Repurposing Pack`. A skeleton
you are not filling in this run is never opened.

## Saving — render the structured text to a styled `.docx`
1. Assemble the doc as structured text (the skeletons below); write it to a temp file in the session's
   scratchpad (never the member's workspace), e.g. `doc.txt`.
2. Render it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Member · Niche]"`
   → the house style automatically: **Arial**, **near-black** text, real **headings** (from the bands), real
   **bullet lists** and **tables**, thin light-grey rules.
3. Upload the **`.docx`** to the right folder of the member's workspace (per the Brain's `drive-map.md`, this
   plugin's home is `03 · Content/Long-Form/`, located by workspace ID; the Starter Resource alone goes to
   `03 · Content/Guides/`) — the structured text was only the renderer's input; the deliverable is the `.docx`.
4. **Four texts are kept for the Brain Board** (the owner, 2026-11-14), written to `~/attraction-brain/exports/`
   in the same run and then pushed (the Brain syncs `exports/*.txt`): the Channel Page as
   `channel-kit-YYYY-MM-DD.txt` (the file name is unchanged — other files read it) · the YouTube Game Plan as
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
   Monday Week Plan drafts the week's Reels from it, and the clips are queued in the Brain's calendar
   (`memory/content-calendar.md → ## Clips from your videos (YouTube)`).

**If the renderer prints `RENDERER-UNAVAILABLE`** (python-docx is not in this environment): do exactly what it
says — **do not install anything, do not run pip, do not retry the command** (a package install can block for
many minutes in a sandbox and looks like a hang). Build the same `.docx` ONCE with the **docx skill**, matching
the look below. If that also fails, STOP and tell the member plainly that the document renderer is unavailable
in this session, keep the full content visible in chat so nothing is lost, and state the next step — *"Everything
is here in the chat. Ask for it again in a new chat and it saves as a document."* — a statement, never a question.
Never "just upload the text."

**NEVER upload the raw structured text as the deliverable.** The CAPS bands and `────`/`════` rules are the
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
Runtime ~12 min  ·  For: the 0–2 year agent  ·  Lane: Situation  ·  2026-12-04
```

**Section band** — standard header wrapped top + bottom by a 44-char `─` rule, label in CAPS, ` · ` timestamp:
```
────────────────────────────────────────────
HOOK  ·  0:00
────────────────────────────────────────────
```

**Major block** — for big structural blocks (Chapters, the Short, top-level parts) use the heavy `═` rule:
```
════════════════════════════════════════════
CHAPTERS   (paste into the description)
════════════════════════════════════════════
```

**Cue lines** — non-spoken notes on their OWN line, indented 3 spaces:
```
   >> ON SCREEN:  Taylor Brooks · Austin
   [PAUSE]
   FACT:  from the brokerage's onboarding guide, 2026-09
```

**Bullets** — 3-space indent, `•`, two spaces: `   •  First point.`

**Footer** — a `─` rule, then sourcing + compliance:
```
────────────────────────────────────────────
Facts verified — {claim} ({source}, {date}).
Compliance — cardinal rules · no compensation figures · disclosure present · [status: set / confirmed].  ✓
```
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
- **One member word for a content lane: "lane".** A channel has five lanes — the three topics, the interview lane,
  the model lane — and the three niche ones are always **"your three topics"**. Never a second word for the same
  thing. The Week 4 pillars, when named, are "your Authority pillar", "your Proof pillar", "your Perspective pillar".
- **None of the system's own words anywhere in the document:** no "bucket", "SIGNAL", "FOR · PAIN · SIGNAL", "cycle
  position", "anchors", "unresearched", "starter", "rung", "avatar"; no skill name, no file name, no code or note
  beside a title. Plain replacements: "the agents you attract" · "your two calls to action" · "click-through rate" ·
  "not yet checked against search" · "from the starting list" · "your eight-video plan".
- **Dates in words** — "Mon, Dec 7" — never `YYYY-MM-DD` inside the document (the Brain's rows keep the real dates).
- **YOUR NEXT 7 DAYS is its own ruled block, right after READ THIS FIRST** — exactly three numbered lines, never a
  fourth: the first video by exact title · the first agent to invite for an interview · the one channel fix.
- **The 90-day calendar is one plain table** — `Week of` (the Monday of the week, in words) · `Video` (the exact
  title) · `Kind` (Niche / Interview / Model; a new channel's first row is its Trailer) · `Guest`.
- **The goal is four plain lines** with the member's numbers; every number the member did not state is labelled
  "(an assumption — change it any time)".
- **The title list is the LAST band** — MORE TITLES WHEN YOU NEED THEM — grouped by lane, plain titles only.
- **The codes stay in the Brain.** Each title's working notes (who it is for · the pain · why it is on the list)
  are never printed. They are kept in the Brain's copy of the plan only: the **TITLE NOTES** block appended to
  `exports/youtube-game-plan-YYYY-MM-DD.txt` after the document's text (its shape is under the skeleton) — where
  ideation and the Monday Kickoff read each title's why.
Everything inside `{…}` below is a note to the writer and is never printed.
```
YOUTUBE GAME PLAN — [MEMBER NAME]
Known for: [what you're known for]  ·  Attracting: [the first type of agent] · [the second]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks


════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{where your channel is today, and the verdict · the insight · the plan in one line · your pace: one video a week for the first month, two the step-up · your 90-day goal in conversations and calls}
{only when it applies, one plain line each: "Some of these titles are not yet checked against what agents search — say 'what are agents searching' and I check them." · "Your title list starts from the starting list; your own ideas and your comments replace it as they come in." · "Your two calls to action come from your offer for now — your kit's wording replaces them."}


════════════════════════════════════════════
YOUR NEXT 7 DAYS
════════════════════════════════════════════
   1.  YOUR FIRST VIDEO — "{the exact title}" · record it {the day, in words — "Sat, Nov 28"} · say "make my attraction video: {title}"
   2.  YOUR FIRST INTERVIEW — invite {the guest's first name}: {their story in one line} · say "set up an agent interview"   {no guest named yet: "invite the first agent you have helped"}
   3.  YOUR ONE CHANNEL FIX — {the one fix, in plain words — a channel not pasted yet: "paste the three pieces marked 'paste today' in your Channel Page"}


════════════════════════════════════════════
CHANNEL AUDIT
════════════════════════════════════════════
{scaled to the number of videos — for a new channel a short "starting clean" note}
   What's working ......... {…}
   What's missing ......... {which of the three kinds of video is absent · the two calls to action · playlists · titles and thumbnails}
   First impression ....... {can a first-time visitor tell who the channel is for and why to reach out?}


════════════════════════════════════════════
YOUR POSITIONING
════════════════════════════════════════════
Who the channel is for:  {the agents you attract, in their words}
What you'll be known for:  {from strategy.md / offer.md}
The one line:  {"[Name] helps [the type of agent] [outcome] through [how]"}
Your two calls to action:  1. The guide — "{the spoken guide line, word for word from the kit — '… Comment GUIDE and I'll send it.'}"   2. The call — "{the spoken call line, word for word from the kit, in the call-to-action law's shape}"
Why I'm building this:  {the why-line from journey.md → ## The WHY, in the member's voice — drafted and labeled "(draft)" when the Brain has not written it; never a question}
What's missing for {the agents you attract} — and how I bridge it:  {the bridge-the-gap line — the agents' problem, never a word against another team or brokerage}
Why me — for a new agent · for a seasoned agent:  {from ## Why join me / leadership.md; one line each}


════════════════════════════════════════════
YOUR THREE TOPICS   (three lanes on your channel, one playlist each — your Authority pillar)
════════════════════════════════════════════
   THE PROBLEM TOPIC — {its name}  ·  Playlist: "{playlist}"
   Who it's for: {the type of agent} · The pain it answers: {one of the five, in their words} · Why it builds trust: {one line}
   THE SITUATION TOPIC — {its name}  ·  Playlist: "{playlist}"
   {…}
   THE FUTURE TOPIC — {its name}  ·  Playlist: "{playlist}"
   {…}


════════════════════════════════════════════
YOUR INTERVIEW LANE   (your Proof pillar)
════════════════════════════════════════════
Playlist: "{Agent success stories}"
| # | Guest | Their story — the title | Where they come from |
|---|---|---|---|
| 1 | {name} | {How … built … while …} | {your organization / your Top 50} |
{6–10 guests, in the order to invite them}


════════════════════════════════════════════
YOUR MODEL LANE   (your Perspective pillar)
════════════════════════════════════════════
Playlist: "{[Model] explained}"
   {the videos that answer what agents are already researching: explained · should you join · how [one part] works · questions to ask a sponsor · do NOT join if}
   {Mike's comparison warning, one line — comparisons only on the member's explicit choice}


════════════════════════════════════════════
YOUR GOAL, IN FOUR LINES   (conversations and calls — never income)
════════════════════════════════════════════
   1.  Your 90-day goal: {n} calls held with agents.   {(from your goals) — or: (an assumption — change it any time)}
   2.  To hold {n} calls you book about {n} — about {x} of every 10 booked calls happen.   {(your own number) — or: (an assumption — change it any time)}
   3.  To book {n} calls you start about {n} conversations — about one call for every {y} conversations.   {(your own number) — or: (an assumption — change it any time)}
   4.  YouTube's part this quarter: about {n} of those conversations — roughly {n} a video at {one video a week}.   {(your own split) — or: (an assumption — change it any time)}
What you control each week: videos published · interviews recorded · both calls to action in every video · comments answered · messages started.
{one honest line — reachable, or ambitious; when ambitious, the first lever: two videos a week after a month at one · never a promise}   To lock your own numbers, say "set my attraction goals".


════════════════════════════════════════════
THE VIDEO STRUCTURE   (every video)
════════════════════════════════════════════
   THE OPENING (0:00–0:15) — {the pain point, in the member's voice — written word for word}
   THE GUIDE (inside minute 1) — {the kit's spoken guide line, word for word — "comment GUIDE" / "link in the description"}
   THE TEACHING — {as long as it needs to be, as short as it can be; the steps of the member's method are the teaching material}
   THE CALL (about a third in) — {the kit's spoken call line, word for word, in the call-to-action law's shape — the person · their help · free · to run this (house rules #15) — never the brokerage, never a promise of your time}
   THE PAYOFF + THE NEXT VIDEO — {deliver the promise; point to the next logical video}


════════════════════════════════════════════
YOUR CADENCE
════════════════════════════════════════════
One video a week for the first month — {the honest read from goals.md's hours}. Two a week is the step-up Mike
recommends (his team read about four times the growth of one); your monthly review proposes it once a month at one
has held, or sooner when your hours clearly carry it or you ask — say "change my YouTube cadence". Your eight-video
plan holds at either pace — once round in eight weeks at one a week, in four at two. {your short-form rhythm is separate — this is your YouTube pace}


════════════════════════════════════════════
YOUR FIRST 90 DAYS   (your eight-video plan: 3 niche · 1 model · 4 interviews — one a week to start)
════════════════════════════════════════════
The order of your eight: niche · interview · niche · model · interview · niche · interview · interview — then it starts again.
   ──── YOUR FIRST 30 DAYS   (these are on your content board) ────
| Week of | Video | Kind | Guest |
|---|---|---|---|
| {Mon, Dec 7} | {exact title} | Niche | — |
| {Mon, Dec 14} | {exact title} | Interview | {the guest's first name} |
| {Mon, Dec 21} | {exact title} | Niche | — |
| {Mon, Dec 28} | {exact title} | Model | — |
   ──── THE WEEKS AFTER ────
| Week of | Video | Kind | Guest |
|---|---|---|---|
| {Mon, Jan 4} | {exact title} | Interview | {guest} |
{one row per video to about week thirteen, in the order above — interview · niche · interview · interview close the first eight; two interviews may be recorded in one sitting; at two a week two rows share a week}
A month in, your monthly review asks whether two videos a week fits. Any time: say "change my YouTube cadence".
{a new channel only — its first row, before the eight: | {the week of the first filming day} | My channel trailer | Trailer | — |   and one line under the table: "Your trailer is 60 to 90 seconds; your eight-video plan starts the week after."}
{the week of the first row is the week of the first filming day — at least three days after the plan was built (yt-gameplan's first-date rule); never the day of the sitting}


════════════════════════════════════════════
DAYS 91–180   (the direction)
════════════════════════════════════════════
   91–120  Double down — {the topics to cluster if they win}
   121–150 Compounding assets — {the evergreen model and career-transition videos to make}
   151–180 The machine — {one or two videos a week + your short-form rhythm + 1–2 interviews a month + your Monthly Channel Review}


════════════════════════════════════════════
THE SCOREBOARD   (90 days, from your goals)
════════════════════════════════════════════
   What you do:  videos published {n} · interviews recorded {n} · conversations from YouTube {n} · calls booked {n}
   What follows:  click-through rate 6–10% after month one · average view duration {tracked} · subscribers {tracked, not targeted} · agents partnered {from goals}
   Compliance:  {status · anything that must be set before a video goes out}


════════════════════════════════════════════
WHAT I CHECKED, AND WHEN
════════════════════════════════════════════
   What agents search ..... {each phrase searched → what was seen · as seen {the date, in words}}   (up to 10 searches)
   Channels that work ..... {the channels read · the videos that stood out · views as seen · {the date}}   (up to 8 searches)
   What you told me ....... {the objections you hear · the ideas you captured · your comments · the news you saved}
   Searches run:  {n} of 18  ·  Titles not yet checked against search: {n, or "none"}   {when some are unchecked: Say "what are agents searching" and I check them.}
   {demo mode: "Demo — nothing searched; every example is illustrative"}


════════════════════════════════════════════
MORE TITLES WHEN YOU NEED THEM   (by lane — plain titles; pick any)
════════════════════════════════════════════
   ──── {THE PROBLEM TOPIC'S NAME} ────
   •  {exact title}
   •  {…}   {12–15 in all for this lane, the calendar's included}
   ──── {THE SITUATION TOPIC'S NAME} ────
   •  {…}   {12–15}
   ──── {THE FUTURE TOPIC'S NAME} ────
   •  {…}   {6–8}
   ──── YOUR INTERVIEW LANE ────
   •  {…}   {8–10 — the guest list above, titled}
   ──── YOUR MODEL LANE ────
   •  {…}   {6–8}
{nothing beside a title — no code, no note, no bracket; a title already on the 90-day calendar is not repeated here; about fifty titles across the calendar and this list}


────────────────────────────────────────────
{closing — one honest paragraph: consistency before optimization; three years; chapter one}
Powered by Mike Sherrard Coaching Inc Frameworks
```
**The Brain's copy only** — appended to `exports/youtube-game-plan-YYYY-MM-DD.txt` after the closing, never rendered
into the `.docx` and never shown to the member (this is where the codes stay):
```
TITLE NOTES   (the Brain's copy — not printed in the document)
{lane: Problem / Situation / Future / Interview / Model} · {exact title} · for {the type of agent} · {the pain — one of the five} · {why: demand / news (dated) / asked / proven / gap / unresearched / starter}{ · Seen on YouTube: {link} — only when the plan's research really returned a video on this question; a candidate for the card's reference video, still checked before use}
{one line per title — the calendar's titles first, in date order, then the list's}
```

### Script (the four formats + interview)
TITLE/meta → bands for `HOOK · 0:00` → `THE GUIDE ASK · ~0:45` → numbered `1 · LABEL · MM:SS` body sections
(3–5) → `THE CALL ASK · ~{1/3 in}` → `PAYOFF` → `NEXT VIDEO` → heavy band `CHAPTERS` → heavy band `THE FIRST SHORT` →
footer with the stories used and the compliance line — both CTAs the kit's CALLS TO ACTION lines, verbatim, in the
law's shape (house rules #15 and #17): the guide inside minute one, the call a third in. Interview scripts carry `INTRO (record last)` ·
`QUESTION MAP` · `OUTRO + JOINT CTA`. Detailed skeleton:
`${CLAUDE_PLUGIN_ROOT}/skills/yt-script/references/script-format.md`.

### First Batch — Film Day (`yt-script`, "script my first three videos" — saved as `First Batch — Film Day — YYYY-MM-DD` in `03 · Content/Long-Form/`; no export)
Member-facing, one page, large and plain: the day, the three videos, and what to do before, between and after.
```
YOUR FIRST BATCH — FILM DAY
{the day, in words — "Sat, Dec 12"}  ·  three videos, about {n} minutes of talking in all

──────────────── THE THREE, IN FILMING ORDER ────────────────
1.  {title} — about {n} minutes  ·  script: in this video's folder, and on its card
2.  {title} — about {n} minutes
3.  {title — the channel trailer goes last, when you are warmed up} — about {n} minutes
{each goes out on its own week — the dates on your plan do not change}

──────────────── BEFORE YOU RECORD ────────────────
•  Camera at eye level
•  Face a window — the light in front of you, never behind
•  A quiet room, or the microphone you already have
•  Your script in large type, right beside the lens
•  Record ten seconds and watch it back before you start

──────────────── BETWEEN VIDEOS ────────────────
•  Change your top, so three weeks of videos do not look like one afternoon
•  A sip of water; read the first line of the next script out loud once

──────────────── AFTER EACH VIDEO ────────────────
•  Five photos of your face for your thumbnail: a big smile · surprised · serious · pointing left · pointing right

──────────────── WHAT HAPPENS NEXT ────────────────
One video at a time: open a new chat and say "make my attraction video: {title}" — your script is already written,
so your thumbnail sheet, your title and description and your publish checklist are added. Then "edit my YouTube video".
```
Never a line that promises anyone the member's time; no interview is ever on this sheet (a guest is booked).

### Channel Page (`yt-setup` — the document "Channel Page — [Name]", saved as `Channel Page — [Name] — YYYY-MM-DD`; the text also kept at `exports/channel-kit-YYYY-MM-DD.txt` — the export's file name is unchanged because other files read it — so the Brain Board can read it)
To the member this document is **"your Channel Page"** — never a "kit": "your kit" always means the Week 3 Kit, and
"your brand kit" the Week 3 design pieces. It holds all nine pieces, in Studio's order, the click path above each;
the three the member pastes today are marked "paste today" (the chat shows only those three — `yt-setup` Step 4).
**Plain words only in every printed line:** no skill name, no file path, no folder code — "your guide", "your kit",
"your Brand folder", "your booking link". Everything inside `{…}` below is a note to the writer and is never printed.
```
CHANNEL PAGE — [MEMBER NAME]
[Channel handle, or "your new channel"]  ·  Known for: [what you're known for]  ·  [the date, in words]
{only while compliance is unset, one line:}  HOLD UNTIL YOUR COMPLIANCE BASICS ARE SET — say "paste my compliance link" (two minutes), then paste.
{only for a channel that does not exist yet, one line:}  First, create your channel — on YouTube click your picture, choose "Create a channel", and name it [the channel name]. Everything below pastes into it.

──────────────── 1 · CHANNEL DESCRIPTION   (paste today) ────────────────
   >> PASTE INTO:  Studio → Customization → Basic info → Description — the opening paragraph
{2–3 sentences: who it's for · what they'll learn · the rhythm ("a new video every week")}

──────────────── 2 · ABOUT SECTION   (paste today — the same field) ────────────────
   >> PASTE INTO:  the same Description field, directly below the opening paragraph
{opens with the YouTube bio from the kit, as written — refreshed only when the offer, the proof or the guide's link changed · who it serves · the lanes by name · one real proof line · the call line in the law's shape + the booking link · the guide + its link · the brokerage's wording, or its held place · pieces 1 and 2 together fit YouTube's 1,000-character description field}

──────────────── 3 · LINKS   (paste today) ────────────────
   >> PASTE INTO:  Studio → Customization → Basic info → Links
   •  {the booking link} — the call   (first)
   •  {the guide's link} — your free guide   (second; only when the Week 2 guide was skipped: the starter guide's link, once it exists)
   •  {ONE social}

──────────────── 4 · CHANNEL KEYWORDS ────────────────
   >> PASTE INTO:  Studio → Settings → Channel → Basic info → Keywords
{8–12 phrases agents search}

──────────────── 5 · PLAYLISTS ────────────────
   >> CREATE IN:  Studio → Content → Playlists → New playlist   (in this order — it is your homepage order)
   •  {Model explained}:  {one-line description}
   •  {Agent success stories}:  {…}
   •  {the Problem topic's playlist}:  {…}
   •  {the Situation topic's playlist}:  {…}
   •  {the Future topic's playlist}:  {…}

──────────────── 6 · CHANNEL BANNER ────────────────
   >> UPLOAD IN:  Studio → Customization → Branding → Banner
{the banner is found — this one line, nothing else:}  Your YouTube banner is already made — it's in your Brand folder from Week 3 (banner-youtube.png). Upload it in Studio: Customization → Branding → Banner.
{the banner is not found — this one line, then the three lines of words to hand over:}  Your banner comes from your brand kit — in your Claude Design project say "make my brand kit" and it builds your YouTube banner first; then upload it here.
{not found only}  Headline:  {who it's for + what they get}
{not found only}  Subline:  {the rhythm, or the invite in the law's shape}
{not found only}  Keep the words in the centre — TV, desktop and phone crop the banner differently.

──────────────── 7 · UPLOAD DEFAULTS   (paste today) ────────────────
   >> SET ONCE IN:  Studio → Settings → Upload defaults
{the default description: line 1 the kit's call line + the booking link (the law's shape) · line 2 the guide + its link · line 3 the compliance and contact line · the brokerage's wording last, or its held place · default tags · category Education · visibility · language}

──────────────── 8 · YOUR SPOKEN LINES   (every video — word for word from your kit) ────────────────
   >> SAY IN:  every video — nothing to paste
The guide (inside the first minute):  "{the kit's spoken guide line — 'comment GUIDE' / 'link in the description'}"
The call (a third of the way in):  "{the kit's spoken call line, in the law's shape — join register: 'If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call].' · open register: 'I'll walk you through it, free, no strings.' — never the brokerage}"
Pop-ups:  {the kit's video pop-up lines — the guide's and the call's}   ·   End cards:  {the kit's end-card lines}

──────────────── 9 · CHANNEL TRAILER ────────────────
   >> SET IN:  Studio → Customization → Layout → Video spotlight
{a new channel:}  Your trailer is the first video on your plan — say "make my attraction video: my channel trailer".   {an existing channel: the strongest recent video, named}

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · your brokerage's wording present · [status].  ✓   {unset → "Compliance — hold until your compliance basics are set · cardinal rules · no compensation figures · your brokerage's wording still to add."}
```

### Kickoff Brief (the Monday Kickoff — `yt-briefing`, scheduled or on demand; saved as `Kickoff Brief — [title] — YYYY-MM-DD` in the video's folder; the Brain Board's text is the Kickoff's NOTE, kept at `exports/youtube-kickoff-YYYY-MM-DD.txt` — never the brief; the same sections are written into the video's board card under the card page's emoji headings, Status → Scripted)
Member-facing: the start of the week's video, done for them — never a full production run. The script START is
labeled as a start; the full script, the chapters, and the competitive read belong to the video's own chat. The
sections run in the locked long-form card page's order (`notion-board-spec.md`): 🎯 THE HOOK · 🎬 SCRIPT · 🖼 THUMBNAIL
BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE · 📚 REFERENCE VIDEO · 🎙 GUEST · 📋 ASSETS & NOTES · ✅ PUBLISH IT · 📊 AFTER IT'S OUT — on the card
each section is replaced in place, never stacked; a card seeded from the calendar already holds THE HOOK, the
REFERENCE VIDEO and ASSETS & NOTES (the brief), and the Kickoff fills the rest — it never deletes or rewrites the
reference video, and it lays down the six publish boxes with their click paths.
```
KICKOFF BRIEF — "{title}"
Week of {Monday's date}  ·  For: {the type of agent}  ·  Lane: {Problem / Situation / Future / Interview / Model}  ·  Recording: {date}  ·  Publishing: {date}

──────────────── THE HOOK ────────────────
Title:  {the exact title}
{three ways to open — the chosen one first and in bold: the viewer's situation → the tension → what they'll have by the end}

──────────────── SCRIPT START   (finish it: say "make my attraction video: {title}") ────────────────
[HOOK — 0:00]   {the chosen hook, written word for word}
[THE GUIDE ASK — inside minute 1]   {the kit's spoken resource line, verbatim — the guide: "comment GUIDE" / "link in the description"}
SECTION MAP:   1 · {label} — {what it delivers}   ·   2 · {…}   ·   3 · {…}   (3–5; the method's steps from the offer's ## The framework are the teaching material)
[THE CALL ASK — ~1/3 in]   {the kit's spoken call line, verbatim, in the call-to-action law's shape — the person · their help · free · to run this; never the brokerage, never a promise of your time}
   {an interview slot: this block holds your own hook and the two ask lines only — the whole guide is in the GUEST block}

──────────────── THUMBNAIL BRIEF ────────────────
{your thumbnail sheet for Higgsfield — for each of the three directions the image prompt to paste, which of your photos to upload and the 3 to 5 words to add; one recommended — the same sheet saved as its own doc (the Thumbnail Sheet skeleton)}

──────────────── SEO PACKAGE START ────────────────
Title options (3):  {…}
Description, lines 1–3:  {line 1 the kit's call line + the booking link (the law's shape) · line 2 the guide's funnel URL · line 3 the compliance and contact line}   ·   Summary (~150 words):  {…}
Tags:  {…}   ·   Hashtags:  {…}   ·   Pinned comment:  {the guide's funnel URL + "comment GUIDE and I'll send it" + one question}   ·   Chapters: after the script   ·   Disclosure block: last

──────────────── THE RESOURCE ────────────────
{this video's resource — the guide by name, the keyword GUIDE, the funnel URL, where it lives (memory/magnets.md → ## Current magnet) · the call: the booking link}

──────────────── REFERENCE VIDEO — WATCH THIS FIRST ────────────────
▶ {the video's real title} — {channel} — {the clean watch link}
Why this one:  {closest match by title: the same question, made for agents / close, not exact: what differs / for the format: how a video like yours is run}
Watch for:  how it opens · where it asks for something · what it leaves out that you would say
{the card's own reference video, already on the card — the Kickoff re-checks the link still opens and finds a new one if it does not; a card with none gets one now (one search, the check); none found → "No close video found yet — here is YouTube's own search for this topic: {the search link}". Two more arrive with the full script (yt-make-video). Never a link that a search did not return and the check did not confirm; never a view count that was not seen.}

──────────────── GUEST   (interviews only) ────────────────
{the guest · the transformation the title promises · the outcome sentence · the five steps with the type-specific questions · the edification lines · the call line in the law's shape · the invite draft · the consent line and its state · the distribution ask (their three sentences)}

──────────────── ASSETS & NOTES   (the brief) ────────────────
Who it's for and the pain:  {the type of agent · one of the five pains, in their words}
Why this week:  {the plan's reason for this title, in plain words — what agents search · a dated news item · an objection you heard · a video that worked elsewhere · a gap on your channel · "from the starting list — not yet checked against search"}
Story to use:  {the story-bank hook — unused recently}
B-roll and filming notes:  {…}   ·   Compliance lines to say:  {license display · brokerage name, as compliance.md says}

──────────────── PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO ────────────────
{six tick boxes, in Studio's own order, each with where to click — the video's own values arrive when the full package is written ("make my attraction video"); never ticked by the system}
☐ 1 · Title — Details → Title: paste your chosen title
☐ 2 · Description — Details → Description: paste your description (line 1 your call and booking link · line 2 your guide · line 3 your compliance and contact line)
☐ 3 · Thumbnail — Details → Thumbnail → Upload file: the thumbnail you made in Higgsfield, from this video's folder (made all three, and Studio shows "Test & compare" there? Use it and upload the three — YouTube picks the winner)
☐ 4 · Playlist — Details → Playlists: tick {the playlist's exact name}
☐ 5 · End screen — Video elements → Add an end screen: the next video and the playlist your SEO package names (your first video: the playlist alone), and Subscribe
☐ 6 · Pinned comment — after it is public: post your pinned comment, then ⋮ → Pin
All six ticked? Say "my video is published" and I'll move this card to Published.

──────────────── AFTER IT'S OUT ────────────────
{empty — your Monthly Channel Review, or "how did my video do", writes the live link, the numbers and the agents who named the video}

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · former brokerage unnamed · disclosure in the description · [status].  ✓
```

### SEO Package
```
{VIDEO TITLE} — SEO PACKAGE
For {the type of agent}  ·  Lane: {Problem / Situation / Future / Interview / Model}  ·  {YYYY-MM-DD}

──────────────── TITLE OPTIONS ────────────────
1.  {option — formula #}
2.  {option}
3.  {option}

──────────────── THUMBNAIL TEXT ────────────────
{3–5 words, different from the title}  ·  (the three thumbnails are made in Higgsfield from your thumbnail sheet)

──────────────── DESCRIPTION ────────────────
{line 1: the kit's call line, verbatim, + the booking link — the law's shape: the person · their help · free · to run this (the join register on Join-gated package allowed: yes or unknown; the open register only on no) — never the brokerage}
{line 2: the guide → its funnel URL ("Free: [the guide's name] → [funnel URL]"; "Questions to Ask Before You Choose a Sponsor" only when the Week 2 guide was skipped)}
{line 3: the compliance and contact line — the brokerage name and license display as compliance.md requires, then the contact line operations.md lists (the handles, a phone or an email — only what is on file); the full disclosure block stays the LAST block}
{150–250 word summary in the member's voice — no compensation words (splits, caps, fees, rev-share tiers, stock, income), no promise of your time}

   CHAPTERS
   00:00  {…}
   01:00  {…}

   WATCH NEXT
   {the next logical video} · {the lane's playlist}

──────────────── TAGS ────────────────
{tag, tag, tag, …}

──────────────── HASHTAGS ────────────────
#{…}  #{…}  #{…}

──────────────── PINNED COMMENT ────────────────
"{the guide's funnel URL + "comment GUIDE and I'll send it" + one question inviting agents to comment their situation — never a keyword of the plugin's own}"

──────────────── END SCREEN + CARD ────────────────
End screen:  {the next logical video — a first video: the playlist alone} + subscribe  ·  Card:  {the resource, at the moment the script points to it}  ·  Playlist:  {the lane's playlist, by its exact name on the channel — the publish checklist's steps 4 and 5 paste these two}

──────────────── WHY THESE   (three plain sentences, for you — not for pasting) ────────────────
{the phrase the title targets and the evidence seen · which tags carry real demand · why the description order is the conversion order}

──────────────── DISCLOSURE BLOCK   (always the LAST block of the description) ────────────────
{brokerage name + license as required · the brokerage disclaimer verbatim · income disclaimer only if earnings were mentioned · AI-likeness line on clone content}
```

### Interview Prep (`yt-interview` — saved as `Interview Prep — [guest] — YYYY-MM-DD` in the video's folder)
Every section below is something `yt-interview` Steps 3–6 produce; a prep with only the question map is a thin
doc and a failed render.
```
INTERVIEW PREP — {GUEST NAME}
Transformation: {the title hook}  ·  Type: {new agent / turnaround / top producer / team leader / broker-owner / attracted their first agent / guest expert}  ·  For: {the type of agent this story lands with}  ·  Record: {date}  ·  Consent: {on file / asked YYYY-MM-DD / pending}

──────────────── THE OUTCOME THIS VIDEO DELIVERS ────────────────
{one line — "by the end, a {type of agent} watching should believe {X}" — what a viewer who has never heard of the guest leaves with}

──────────────── TITLE OPTIONS   (hook AND transformation — never "tell me your story") ────────────────
1.  {How {first name} {transformation} — and used {the mechanism}}   ← recommended
2.  {…}
3.  {…}
Thumbnail text (differs from the title, both faces):  {3–5 words}

──────────────── EDIFICATION LINES   (before the guest speaks — true facts only) ────────────────
{two lines in your voice: their stated result · who they were a year ago · why you wanted them on}

──────────────── QUESTION MAP   (not a script — the five steps, any order) ────────────────
   BEFORE — {what business was like before: 2–3 open questions}
   THE SHIFT — {what made them decide to move, what the hesitation was: 2–3}
   SINCE — {what it has been like since partnering — support, training, community, in their words: 2–3}
   THE RESULTS — {outcomes in their words — freedom, support, the category of result; never a figure they did not volunteer: 1–2}
   ADVICE — {for an agent standing where they stood: 1–2}
   {TYPE-SPECIFIC STEPS — new agent: the first-30-days routine · turnaround: what was missing before (no names, no blame) · top producer: what changed in leverage and time · team leader / broker-owner: what they kept, what overhead disappeared · first agent attracted: how that conversation happened}
   Interviewer rules:  the guest is the star · never interrupt · let emotion sit · add a layer only after they finish · redirect on camera if they knock a brokerage or a person (that part is cut)

──────────────── INTRO   (record LAST, after you know the story — 45–75 s) ────────────────
{the transformation as the title promises it → who this is for → two or three specific things coming → one honest line edifying the guest → the resource CTA in one breath → "let's get into it"}

──────────────── OUTRO + JOINT CTA   (30–45 s) ────────────────
{thank the guest and name the one thing to take from them → the joint call line in the law's shape — join register: "if you want my help running this the way {guest} did — the lessons, the templates, the community — partner with me and it's free; grab the call in the description" · open register: "I'll walk you through it, free, no strings — the link is in the description" — never the brokerage, never a promise of your time → the next video (another interview on the same pain, or the model explained) → the end screen}

──────────────── THE INVITE   (DM or email, in your voice — you send it) ────────────────
{why them · the 30–45 minute format · the recording link · "you are the story" · the one prep line: "think about where you were before and the moment things changed"}
Consent line:  {the plain okay to publish, use clips, and share their name as written}

──────────────── WHEN THEY SAY YES   (the booking — filled when the guest agrees) ────────────────
Two recording times:  {slot 1 — the day, in words, and the time}   ·   {slot 2}
The reply to send:  "{two lines in the member's voice: the two times, 'pick whichever suits you', the recording link comes the day before}"
Guest prep note:  {the copy block the member sends — what to expect · 30 to 45 minutes · the three questions they get first · how to look and sound good on camera}
On the day:  open a new chat and say "prep me for a guest recording"; when it's recorded, say "edit my interview".
Booked:  {the date, the time and the calendar title — "on your calendar" only when the member said yes to the hold}

──────────────── THE GUEST'S DISTRIBUTION ASK   (send when it goes live) ────────────────
{the three sentences: share it to your story · post it with a line of your own · send it to three agents who are where you were — with the link and the clips}

────────────────────────────────────────────
Compliance — cardinal rules on every cut (the guest's answers too) · no compensation figures · former brokerage unnamed · consent recorded · disclosure in the description · [status].  ✓
```

### Thumbnail Sheet (`yt-thumbnail` — the ONE shape, for Higgsfield; saved as `Thumbnail Brief — [title] — YYYY-MM-DD` in the video's folder — the file name is unchanged so the board and the Kickoff find it)
The cohort's members make their thumbnails in **Higgsfield** (the owner, 2026-11-14) — nowhere else. The
sheet carries, for each of the three directions, what the member takes there: the image prompt to paste, which of
their own photos to upload, and the 3 to 5 words to add. Strategy — the scores, the why, the patterns — stays in the
chat. This plugin writes words and prompts; it never makes an image. To the member it is "your thumbnail sheet".
```
THUMBNAIL SHEET — "{VIDEO TITLE}"
For Higgsfield, where you make your thumbnails: upload your photo, paste the prompt, add the words.
Video: {lane} · for {the type of agent} · the feeling: {the fear to avoid / the outcome to reach}
All three: a 16:9 frame at 1280×720, with clear space where the words go.

──────────────── THUMBNAIL 1   (the recommended one) ────────────────
Photo to upload:  {which of the member's own photos — named the way it is in their Brand folder — or, when the expression is missing, "take this one first: {the expression to shoot}"}
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
Rules — 3 to 5 words · the words differ from the title · your face about a third of the frame · one supporting element at most · readable on a phone · {compliance: your brokerage's mark where required; no other brokerage's mark; your AI-picture line where your compliance wording asks for one}
When they're made: drop the finished thumbnails into this video's folder (Content → Long-Form → {video}) and say "my thumbnail is done".
```

### Lead Map (`yt-leads` — only when the lead magnet exists, built in Week 2; the Starter Resource needs no map)
```
{VIDEO TITLE} — LEAD MAP
Offer {from offer.md}  ·  Avatar pain {one of the five}  ·  CTA {booking link}

──────────────── THE RESOURCE ────────────────
Name:     {title}
Format:   {checklist / playbook / guide}
Promise:  {the one outcome it delivers — the "give enough to get started" rule}

──────────────── PAGE-BY-PAGE ────────────────
PAGE 1 — {purpose}
   •  {content}

──────────────── CTA / NEXT STEP ────────────────
{the call line in the law's shape — your kit's, verbatim — + the booking link}
(We map the content; your Lead Magnet system — the Week 2 plugin — writes and designs it as a later campaign.)
```

### Starter Resource (`yt-leads` — the fallback for a member who skipped the Week 2 lead magnet: built ONCE, in Week 5, while `## Current magnet` is empty; saved as `Starter Resource — YYYY-MM-DD` in `03 · Content/Guides/`)
Questions only — the doc never answers them, never names a brokerage as the answer, never carries a figure. One
page, in the member's voice, for the primary avatar. Ten to twelve questions; the standard twelve live in
`yt-leads` 1a. Sub-band labels stay under 70 characters.
```
QUESTIONS TO ASK BEFORE YOU CHOOSE A SPONSOR
From {Member Name}  ·  For {the type of agent, in their words}  ·  {YYYY-MM-DD}

──────────────── WHY THESE QUESTIONS ────────────────
{3–4 sentences in the member's voice: you're choosing a sponsor, not just a brokerage · the brokerage is the vehicle, the leader is the growth · ask these of anyone you're considering — including me}

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
   (questions only — no split, cap, fee, tier, stock, or income figure appears here, not even as an example)

──────────────── THE NEXT STEP ────────────────
{one warm line in the member's voice, in the law's shape — "want these answered for your situation? grab a call — I'll walk you through it, free, no strings" → the booking link}

────────────────────────────────────────────
{the disclosure footer: brokerage name and license as compliance.md requires · the brokerage disclaimer verbatim · no income disclaimer — no earnings are mentioned}
Compliance — cardinal rules · brokerage-agnostic · no compensation figures · disclosure present · [status].  ✓
```

### Model Breakdown (`yt-model-breakdown` — saved as `Model Breakdown — [title] — YYYY-MM-DD` in the video's folder)
```
{VIDEO TITLE} — MODEL BREAKDOWN
For {the type of agent}  ·  Lane: Model  ·  Model file last reviewed {YYYY-MM-DD}  ·  {YYYY-MM-DD}

──────────────── THE SOURCED FACT SHEET ────────────────
   •  {fact used} — {source document, date}   (every fact; compensation figures never appear here or on camera)

──────────────── THE OUTLINE   (one band each — the two CTAs placed) ────────────────
HOOK (the question they typed) · THE GUIDE ASK · OVERVIEW (history, positioning) · HOW COMPENSATION IS STRUCTURED
(the concepts, no figures — "the exact numbers on a call") · TOOLS + THE GAPS YOUR VALUE PROPOSITION FILLS ·
SUPPORT + TRAINING · BEYOND CLOSINGS (the concepts) · CULTURE + COMMUNITY · WHO IT'S FOR · WHO IT'S NOT ·
THE CALL ASK (the law's shape) + NEXT VIDEO

──────────────── THE MYTHS THIS ANSWERS   (what agents keep asking, in their words) ────────────────
   •  "{the myth or fear}" → {the fact, with its source}
   {comparison videos only: Mike's caution stated to the member — facts only, sourced and dated, strengths and weaknesses of each, never a negative word about a brokerage or person}

──────────────── TITLE SET ────────────────
1.  {title}   2.  {title}   3.  {title}   ·  thumbnail text (differs from the title): {3–5 words}

──────────────── RE-MAKE REMINDER ────────────────
{re-make when the model changes or in 12 months — from the file's Last reviewed date}

────────────────────────────────────────────
Cardinal-rules read-back — {what was changed}.   Compliance — no compensation figures · disclosure in the description · [status].  ✓
```

### YouTube Deep Dive (`yt-analytics` — saved as `YouTube Deep Dive — [Month YYYY] — YYYY-MM-DD`; the text also kept at `exports/youtube-read-YYYY-MM-DD.txt` — its own name, never `youtube-review-*`; no credibility stamp)
```
YOUTUBE DEEP DIVE — [MEMBER NAME] — [MONTH YYYY]
Window: {last 90 days}  ·  Data: {live / Studio pack in or not / public reads}  ·  {YYYY-MM-DD}

════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{the verdict — three plain sentences}
   THE ONE MOVE ......... {exactly one action}
   DO THESE THREE THIS WEEK ......... 1. {…}  2. {…}  3. {…}
   YOUR NUMBERS AT A GLANCE   (each with its plain meaning)
   WHAT'S IN THIS REPORT   (pulled live · Studio pack · not available)

════════════════════════════════════════════
PART 1 — YOUR CHANNEL
════════════════════════════════════════════
   1.1 How you grew  ·  1.2 What's pulling — by lane  ·  1.3 Titles & thumbnails  ·  1.4 Your best openings
   1.5 Where viewers come from  ·  1.6 What viewers are saying  ·  1.7 Where views stop turning into calls
   1.8 How often you post & your channel page
   (every finding: what we found · why it matters to you · do this · the proof; numbers in tables)

════════════════════════════════════════════
PART 2 — OTHER ATTRACTION CHANNELS   (what they do well, never what is wrong with them)
════════════════════════════════════════════
════════════════════════════════════════════
PART 3 — WHERE YOU SHOW UP WHEN AGENTS SEARCH
════════════════════════════════════════════
════════════════════════════════════════════
PART 4 — THE OPENINGS   (3–5 four-line cards)
════════════════════════════════════════════
════════════════════════════════════════════
PART 5 — YOUR NEXT 30 DAYS   (keep · fix · the exact titles at your cadence — four or five at one a week, eight or nine at two · THE ONE MOVE, repeated)
════════════════════════════════════════════
════════════════════════════════════════════
APPENDIX — THE FULL NUMBERS
════════════════════════════════════════════
```
Structure and method: `${CLAUDE_PLUGIN_ROOT}/skills/yt-analytics/references/deepdive-guide.md`.

### Monthly Channel Review (`yt-triggers`'s scheduled run, or "run my monthly YouTube review" in chat — saved as `Monthly Channel Review — [Month YYYY] — YYYY-MM-DD`; the text also kept at `exports/youtube-review-YYYY-MM-DD.txt` so the Brain Board can read it; no live data unless connected; no credibility stamp; the same run writes each published card's 📊 AFTER IT'S OUT and one dated YouTube block in the Brain's performance ledger)
The live connection reads public data only; click-through rate, watch time and traffic sources live inside YouTube
Studio. So the review **uses the month's Studio screenshots when they are on record** (a `YouTube Studio numbers`
block for the month in the performance ledger — written by "add my attraction Studio numbers") **and says so**; when
they are not, it says in one line which three would have sharpened it; and **it always ends with the stated step**
that asks for next month's — told, never asked. Plain words: "by topic", "your eight-video plan", never "lane mix"
or "cycle position".
```
MONTHLY CHANNEL REVIEW — [MEMBER NAME] — [MONTH YYYY]
Window: {the month}  ·  Data: {the content log · the calendar · the interview pipeline · the conversations and the Top 50 · your Studio screenshots of {month}, or "no Studio screenshots this month"}  ·  {the date, in words}

──────────────── THE MONTH IN ONE LINE ────────────────
   {one sentence, kindly — a month on plan is a month on plan}

──────────────── WHAT SHIPPED ────────────────
   {pipe table: planned · published · by topic — niche · interview · model; where you are in your eight-video plan; the pace held or not}

──────────────── THE ATTRACTION SCOREBOARD ────────────────
   {pipe table: video · comments · conversations · calls booked — counted from the ledgers, never estimated; the agents who named a video}

──────────────── YOUR STUDIO NUMBERS   (only when this month's screenshots are on record) ────────────────
   From the Studio screenshots you added on {the date, in words}:
   {pipe table: video · impressions · click-through rate · average view duration · views}
   {one line: where your viewers came from and what they typed to find you · one line: where they left your top video}

──────────────── THE INTERVIEW PIPELINE ────────────────
   {candidates · invited · booked · recorded · published; who is overdue; the next guest to invite}

──────────────── THE DRAFTS WAITING ────────────────
   {the Monday Kickoff's drafts still at Scripted, by title — or omit}

──────────────── THE PACKAGING FIX ────────────────
   {one title or thumbnail to redo, and why — from this month's Studio numbers when they are on record; a month of click-through, never day one}
   {no Studio numbers for the month → this one line instead:}  No Studio screenshots this month — the Content table, the Reach page and your top video's retention graph would have told me which title to redo, where your viewers came from and where they left.

──────────────── WHERE MOMENTUM SLOWED ────────────────
   {name ONE — publishing · interviews · the break between views and conversations · the comment sweep}

──────────────── THE ONE MOVE ────────────────
   {exactly one action for next month}

──────────────── NEXT MONTH'S SLOTS ────────────────
   {the titles in order from the calendar, the interview to book first — four or five at one a week, eight or nine at two}
   {THE STEP-UP, when due — one line: two a week proposed, as a proposal the member answers: say "change my YouTube cadence"}

──────────────── TO MAKE NEXT MONTH'S REVIEW SHARPER ────────────────
To make next month's review sharper, take three screenshots in YouTube Studio in the last days of the month and drop them into a chat with the words "add my attraction Studio numbers":
   1.  Analytics → Content — the video table (impressions, click-through rate, average view duration, views).
   2.  Analytics → Reach — traffic source types and YouTube search terms.
   3.  Analytics → Engagement — the retention graph of your top video.

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · [status].  ✓
```

### Repurposing Pack
```
{VIDEO TITLE} — REPURPOSING PACK
From the long-form script  ·  {YYYY-MM-DD}

════════════════ SHORTS (3) ════════════════
SHORT 1 — {angle}
   {hook → one point → the ask: "comment GUIDE", or the kit's call line}

════════════════ CAROUSEL (1) ════════════════
Slide 1 {…} | Slide 2 {…} | …   (copy only — designed from this in your short-form system, or in your brand project in Claude Design — claude.ai/design, or a Design canvas inside Cowork)

════════════════ STORIES (5) ════════════════
   1.  {…}

════════════════ EMAIL (1) ════════════════
Subject:  {…}
{body + the kit's call line, in the law's shape}

════════════════ BLOG (1) ════════════════
Title:  {…}
{body}

════════════════ CONVERSATION STARTERS (3)   (personalised per agent — you send) ════════════════
   1.  {an opener the member can send an agent who'd care about this video — no pitch}
```

Same shape every time, in the member's own voice. This is the standard for what lands in their workspace.
