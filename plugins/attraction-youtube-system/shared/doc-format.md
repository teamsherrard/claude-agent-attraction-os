# Document Format — the house style for EVERY saved document

Every deliverable is rendered to a **clean, formatted `.docx`** in one neutral house style — the same look for
every member (no colour, no per-member branding). The skill writes the **structured text** defined below (CAPS
section bands, `•` bullets, `Label:` lead-ins, simple aligned tables); the shared renderer turns that into real
Word formatting — headings, bullet lists, tables — automatically. **Do NOT save flat `text/plain`.**

## Saving — render the structured text to a styled `.docx`
1. Assemble the doc as structured text (the skeletons below); write it to a temp file in the session's
   scratchpad (never the member's workspace), e.g. `doc.txt`.
2. Render it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Member · Niche]"`
   → the house style automatically: **Arial**, **near-black** text, real **headings** (from the bands), real
   **bullet lists** and **tables**, thin light-grey rules.
3. Upload the **`.docx`** to the right bucket of the member's workspace (per the Brain's `drive-map.md`, this
   plugin's home is `03 · Content/Long-Form/`, located by workspace ID; the Starter Resource alone goes to
   `03 · Content/Guides/`) — the structured text was only the renderer's input; the deliverable is the `.docx`.
4. **Four of these documents are read by the Brain Board as text** (the owner, 2026-11-14): the Channel Page Kit,
   the YouTube Game Plan, each Kickoff Brief and each Monthly Channel Review. In the same run, write the same
   structured text to `~/attraction-brain/exports/` — `channel-kit-YYYY-MM-DD.txt` · `youtube-game-plan-YYYY-MM-DD.txt`
   · `youtube-kickoff-YYYY-MM-DD.txt` · `youtube-review-YYYY-MM-DD.txt` (the Brain syncs `exports/*.txt`) — then
   push. The export sits beside the `.docx`, never instead of it; a doc saved without its export is half-saved.

**If the renderer prints `RENDERER-UNAVAILABLE`** (python-docx is not in this environment): do exactly what it
says — **do not install anything, do not run pip, do not retry the command** (a package install can block for
many minutes in a sandbox and looks like a hang). Build the same `.docx` ONCE with the **docx skill**, matching
the look below. If that also fails, STOP and tell the member plainly that the document renderer is unavailable
in this session, keep the full content visible in chat so nothing is lost, and offer to save it next session.
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
Runtime ~12 min  ·  For: the 0–2 year agent  ·  Bucket: Situation  ·  2026-12-04
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
Member-facing lines say *your Authority lane* / *your Proof lane* / *your Perspective lane* — never "(Authority in
the log)"; the log vocabulary stays in `brain-contract.md`.
```
YOUTUBE GAME PLAN — [MEMBER NAME]
Known for: [niche]  ·  Attracting: [avatar 1] · [avatar 2]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks


════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{where the channel is + the verdict · the insight · the plan in one line · the cadence: one video a week for the first month, two the step-up · the 90-day target in conversations and calls}

   ──── YOUR NEXT 7 DAYS ────
   1.  {the first video to record — exact title}
   2.  {the first interview to invite — guest + the transformation}
   3.  {the one channel-page fix, or "channel page: say 'set up my channel for agents'"}


════════════════════════════════════════════
CHANNEL AUDIT
════════════════════════════════════════════
{scaled to their video count — for a fresh channel a short "starting clean" note}
   What's working ......... {…}
   What's missing ......... {which of the three categories is absent · CTA · playlists · packaging}
   Positioning read ....... {does a first-time visitor know who it's for and why to reach out?}


════════════════════════════════════════════
YOUR POSITIONING
════════════════════════════════════════════
Who the channel is for:  {the avatar, in their words}
What you'll be known for:  {from strategy.md / offer.md}
The one line:  {"[Name] helps [avatar] [outcome] through [mechanism]"}
Why I'm building this:  {the why-line from journey.md → ## The WHY, in the member's voice — drafted and labeled "(draft)" when the Brain has not written it; never a question}
What's missing for {avatar} — and how I bridge it:  {the bridge-the-gap line — the agents' problem, never a word against another team or brokerage}
Why me — for a new agent · for a seasoned agent:  {from ## Why join me / leadership.md; one line each}


════════════════════════════════════════════
YOUR THREE NICHE LANES   (the Problem · Situation · Future buckets — your Authority lane)
════════════════════════════════════════════
   PROBLEM — {name}  ·  Playlist: "{playlist}"
   Who it pulls in: {avatar} · Pain: {one of the five} · Why it builds authority: {one line}
   SITUATION — {name}  ·  Playlist: "{playlist}"
   {…}
   FUTURE — {name}  ·  Playlist: "{playlist}"
   {…}


════════════════════════════════════════════
YOUR INTERVIEW LANE
════════════════════════════════════════════
Playlist: "{Agent success stories}"   (your Proof lane)
   #    GUEST                 TRANSFORMATION (THE TITLE HOOK)                      SOURCE
   1    {name}                {How … built … while …}                              {organization / top-50}
   …    (6–10 candidates, by relatability across types)


════════════════════════════════════════════
YOUR MODEL LANE
════════════════════════════════════════════
Playlist: "{[Model] explained}"
   {the answer-what-they're-researching list: explained · should you join · how [component] works · ask a sponsor these questions · do NOT join if}   (your Perspective lane)
   {Mike's comparison warning, one line — comparisons only on the member's explicit choice}


════════════════════════════════════════════
THE TITLE BANK   (~50 exact titles, bucketed)
════════════════════════════════════════════
   PROBLEM
   #    EXACT TITLE                                        FOR · PAIN · SIGNAL
   1    {title}                                            {avatar · pain · the real signal}
   …    (12–15)
   SITUATION   (12–15)
   FUTURE   (6–8)
   INTERVIEW   (8–10 — the guest list above, titled)
   MODEL   (6–8)


════════════════════════════════════════════
YOUR GOAL → THE PLAN   (conversations and calls, never income)
════════════════════════════════════════════
From your goals:  {90-day calls held target} calls held · {conversations target} conversations
Your ratios:  conversations → calls {x} · calls booked → held {y}   ({member's own / labeled assumption})
YouTube's share:  {n}% of conversations this quarter → {N} conversations from the channel
Per video:  at {cadence}/week that's ~{n} conversations per video — {the honest read: achievable / ambitious}
Leading indicators you control:  videos published · interviews recorded · CTAs placed · comments answered · DMs started
{assumptions stated · a credible path, never a promise}


════════════════════════════════════════════
THE VIDEO STRUCTURE   (every video)
════════════════════════════════════════════
   HOOK (0:00–0:15) — {the pain point, in the member's voice — written word for word}
   RESOURCE CTA (inside minute 1) — {the guide: the kit's spoken resource line, verbatim — "comment GUIDE" / "link in the description"; the funnel URL from memory/magnets.md → ## Current magnet}
   VALUE — {as long as it needs to be, as short as it can be; bullets; the method's steps (offer.md → ## The framework) are the teaching material}
   CALL CTA (~1/3 in) — {the kit's spoken call line, verbatim, in the call-to-action law's shape — the person · their help · free · to run this (house rules #15; the register from offer.md's Join-gated package allowed:) — never the brokerage, never a promise of your time}
   PAYOFF + NEXT VIDEO — {deliver the promise; point to the next logical video}


════════════════════════════════════════════
YOUR CADENCE
════════════════════════════════════════════
One video a week for the first month — {the honest read from goals.md's hours}. Two a week is the step-up Mike
recommends (his team read about four times the growth of one); your monthly review proposes it once a month at one
has held, or sooner when your hours clearly carry it or you ask. The 8-video cycle holds at either pace — one cycle in
eight weeks at one a week, in four at two. {the short-form cadence is its own line in your publishing layer — never this one}


════════════════════════════════════════════
THE FIRST 90 DAYS   (the 8-video cycle: 3 niche · 1 model · 4 interviews · one a week to start)
════════════════════════════════════════════
   ──── YOUR FIRST 30 DAYS   (four or five videos at one a week — onto your board) ────
   Video 1 · week 1 — {exact title}   (Problem · niche)
   Video 2 · week 2 — {exact title}   (Interview · {guest})
   Video 3 · week 3 — {exact title}   (Situation · niche)
   Video 4 · week 4 — {exact title}   (Model)
   {Video 5 · week 5, when the window holds it — the next niche title; a Why I Switched may go early, as Mike's own did}
   ──── THE REST OF THE CYCLE, AND THE NEXT   (weeks 6–13) ────
   Video 6 · week 6 — {exact title}   (Interview · {guest})
   …  (one video per row; cycle boundaries marked — one cycle every eight weeks at one a week; interviews batched
       where the member records in sittings; at two a week the same order runs two rows per week — eight or nine
       videos in the first 30 days)


════════════════════════════════════════════
DAYS 91–180   (the direction)
════════════════════════════════════════════
   91–120  Double down — {the topics to cluster if they win}
   121–150 Compounding assets — {the evergreen model and career-transition videos to make}
   151–180 The machine — {1/week + 4–5 short-form/week + 1–2 interviews/month + weekly review}


════════════════════════════════════════════
THE SCOREBOARD   (90-day, from your goals)
════════════════════════════════════════════
   Leading:  videos published {n} · interviews recorded {n} · conversations from YouTube {n} · calls booked {n}
   Lagging:  CTR 6–10% after month one · average view duration {tracked} · subscribers {tracked, not targeted} · agents partnered {from goals}
   Compliance:  {status · open items that block publishing, if any}


════════════════════════════════════════════
SOURCES   (what was searched, and when)
════════════════════════════════════════════
   What agents search ..... {each phrase searched → what was seen · as seen YYYY-MM-DD}   (≤10 searches)
   Outlier scan ........... {channels read · the videos that qualified · ~views as seen · YYYY-MM-DD}   (≤8 searches)
   Your own signal ........ {objections · captured ideas · comments · intel rows used}
   Budget used:  {n} of 18  ·  Unresearched titles: {n — labeled in the bank, or "none"}  ·  Re-run: {on your next 7 days / not needed}
   {demo mode: "Demo — nothing searched; every signal illustrative"}


────────────────────────────────────────────
{closing — one honest paragraph: consistency before optimization; three years; chapter one}
Powered by Mike Sherrard Coaching Inc Frameworks
```

### Script (the four formats + interview)
TITLE/meta → bands for `HOOK · 0:00` → `RESOURCE CTA · ~0:45` → numbered `1 · LABEL · MM:SS` body sections
(3–5) → `CALL CTA · ~{1/3 in}` → `PAYOFF` → `NEXT VIDEO` → heavy band `CHAPTERS` → heavy band `45-SECOND SHORT` →
footer with the stories used and the compliance line — both CTAs the kit's CALLS TO ACTION lines, verbatim, in the
law's shape (house rules #15 and #17): the guide inside minute one, the call a third in. Interview scripts carry `INTRO (record last)` ·
`QUESTION MAP` · `OUTRO + JOINT CTA`. Detailed skeleton:
`${CLAUDE_PLUGIN_ROOT}/skills/yt-script/references/script-format.md`.

### Channel Page Kit (`yt-setup` — saved as `Channel Page Kit — YYYY-MM-DD`; the text also kept at `exports/channel-kit-YYYY-MM-DD.txt` so the Brain Board can read it)
```
CHANNEL PAGE KIT — [MEMBER NAME]
[Channel handle]  ·  Known for: [niche]  ·  [YYYY-MM-DD]

──────────────── CHANNEL DESCRIPTION ────────────────
   >> PASTE INTO:  Studio → Customization → Basic info → Description (opening paragraph)
{2–3 sentences: who it's for (the avatar) · what they'll learn · the cadence}

──────────────── ABOUT SECTION ────────────────
   >> PASTE INTO:  same field, directly below the description
{opens with the entity line — your kit's chapter 6 YouTube bio (identity/profiles.md → ## YouTube), confirmed; refreshed only when the offer, the proof or the funnel URL changed · the lanes by name · one real proof line · the call line in the law's shape + the booking link · the guide + its funnel URL · the disclosure block}

──────────────── LINKS ────────────────
   •  {Booking link} — the call, labeled in the law's shape (your help, free, to run this)
   •  {The guide's funnel URL} — the Week 2 guide (memory/magnets.md → ## Current magnet) · the Starter Resource only if the Week 2 guide was skipped and the first video's lead step built the fallback
   •  {ONE social}

──────────────── CHANNEL KEYWORDS ────────────────
   >> PASTE INTO:  Studio → Settings → Channel → Basic info
{8–12 agent-search phrases}

──────────────── PLAYLISTS ────────────────
   •  {Model explained}:  {one-line description}
   •  {Agent success stories}:  {…}
   •  {Problem lane}:  {…}   •  {Situation lane}   •  {Future lane}

──────────────── BANNER BRIEF   (a lean build sheet for your brand-kit skill in Claude Design) ────────────────
Headline:  {who it's for + what they get}
Subline:  {cadence / the invite}
   >> Paste into your brand project in Claude Design (claude.ai/design, or a Design canvas inside Cowork) and run your brand-kit skill (aa-brand-kit-design); finished image → Customization → Branding → Banner; copy → 02 · Brand
   (page order + final copy + placeholders only — the strategy stays in the chat)

──────────────── UPLOAD DEFAULTS ────────────────
   >> SET ONCE IN:  Studio → Settings → Upload defaults
{default description: the kit's call line + the booking link on line 1 (the law's shape) · the guide's funnel URL on line 2 · the disclosure block last · default tags · category · visibility · language}

──────────────── THE CTA LINE   (every video — your kit's CALLS TO ACTION table, verbatim) ────────────────
Resource (inside minute 1):  "{the kit's spoken resource line — the guide: 'comment GUIDE' / 'link in the description'}"
Call (a third of the way in):  "{the kit's spoken call line, in the law's shape — join register: 'If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call].' · open register: 'I'll walk you through it, free, no strings.' — never the brokerage}"
Pop-ups:  {the kit's video pop-up lines — the guide's and the call's}   ·   End cards:  {the kit's end-card lines}

──────────────── CHANNEL TRAILER ────────────────
{new channel: "say 'make my attraction video: my channel trailer'" · existing: the strongest recent video, named}

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · disclosure present · [status].  ✓
```

### Kickoff Brief (the Monday Kickoff — `yt-briefing`, scheduled or on demand; saved as `Kickoff Brief — [title] — YYYY-MM-DD` in the video's folder; the text also kept at `exports/youtube-kickoff-YYYY-MM-DD.txt` so the Brain Board can read it; the same sections are written into the video's board card under the card page's emoji headings, Status → Scripted)
Member-facing: the start of the week's video, done for them — never a full production run. The script START is
labeled as a start; the full script, the chapters, and the competitive read belong to the video's own chat. The
sections run in the locked long-form card page's order (`notion-board-spec.md`): 🎯 THE HOOK · 🎬 SCRIPT · 🖼 THUMBNAIL
BRIEF · 🔍 SEO PACKAGE · 🧲 THE RESOURCE · 📚 REFERENCES · 🎙 GUEST · 📋 ASSETS & NOTES · 📊 AFTER IT'S OUT — on the card
each section is replaced in place, never stacked; a card seeded from the calendar already holds THE HOOK and ASSETS &
NOTES (the brief), and the Kickoff fills the rest.
```
KICKOFF BRIEF — "{title}"
Week of {Monday's date}  ·  For: {the type of agent}  ·  Bucket: {Problem / Situation / Future / Interview / Model}  ·  Recording: {date}  ·  Publishing: {date}

──────────────── THE HOOK ────────────────
Title:  {the exact title}
{the hook three ways — the chosen one first and in bold: the viewer's situation → the tension → what they'll have by the end}

──────────────── SCRIPT START   (finish it: say "make my attraction video: {title}") ────────────────
[HOOK — 0:00]   {the chosen hook, written word for word}
[RESOURCE CTA — inside minute 1]   {the kit's spoken resource line, verbatim — the guide: "comment GUIDE" / "link in the description"}
SECTION MAP:   1 · {label} — {what it delivers}   ·   2 · {…}   ·   3 · {…}   (3–5; the method's steps from the offer's ## The framework are the teaching material)
[CALL CTA — ~1/3 in]   {the kit's spoken call line, verbatim, in the call-to-action law's shape — the person · their help · free · to run this; never the brokerage, never a promise of your time}
   {an interview slot: INTERVIEW GUIDE instead — the outcome sentence · the five steps with the type-specific questions · the edification lines · the casual CTA in the law's shape · the invite draft · the consent line · the distribution ask}

──────────────── THUMBNAIL BRIEF ────────────────
{the paste-ready lean build sheet — three directions scored, one recommended — the same block saved as its own doc; pasted into your brand project in Claude Design}

──────────────── SEO PACKAGE START ────────────────
Title options (3):  {…}
Description, lines 1–2:  {line 1 the kit's call line + the booking link (the law's shape) · line 2 the guide's funnel URL}   ·   Summary (~150 words):  {…}
Tags:  {…}   ·   Hashtags:  {…}   ·   Pinned comment:  {the guide's funnel URL + one question}   ·   Chapters: after the script   ·   Disclosure block: last

──────────────── THE RESOURCE ────────────────
{this video's resource — the guide by name, the keyword GUIDE, the funnel URL, where it lives (memory/magnets.md → ## Current magnet) · the call: the booking link}

──────────────── REFERENCES — WATCH THESE 3 FIRST ────────────────
{left for the video's own chat — the competitive read (yt-make-video) fills it; the Kickoff writes one line: "filled when you make the video"}

──────────────── GUEST   (interviews only) ────────────────
{the guest · the transformation the title promises · the question map · their three distribution sentences · the consent state}

──────────────── ASSETS & NOTES   (the brief) ────────────────
Who it's for and the pain:  {the type of agent · one of the five pains, in their words}
Why this week:  {the plan's signal — demand · a dated news item · an objection heard · a proven outlier · a gap · starter}
Story to use:  {the story-bank hook — unused recently}
B-roll and filming notes:  {…}   ·   Compliance lines to say:  {license display · brokerage name, as compliance.md says}

──────────────── AFTER IT'S OUT ────────────────
{empty — your Monthly Channel Review, or "how did my video do", writes the live link, the numbers and the agents who named the video}

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · former brokerage unnamed · disclosure in the description · [status].  ✓
```

### SEO Package
```
{VIDEO TITLE} — SEO PACKAGE
For {avatar}  ·  Bucket {Problem / Situation / Future / Interview / Model}  ·  {YYYY-MM-DD}

──────────────── TITLE OPTIONS ────────────────
1.  {option — formula #}
2.  {option}
3.  {option}

──────────────── THUMBNAIL TEXT ────────────────
{3–5 words, different from the title}  ·  (the brief goes to Claude Design via the Thumbnail Brief)

──────────────── DESCRIPTION ────────────────
{line 1: the kit's call line, verbatim, + the booking link — the law's shape: the person · their help · free · to run this (the join register on Join-gated package allowed: yes or unknown; the open register only on no) — never the brokerage}
{line 2: the guide → its funnel URL ("Free: [the guide's name] → [funnel URL]"; "Questions to Ask Before You Choose a Sponsor" only when the Week 2 guide was skipped) · line 3: a contact line only if operations.md lists it}
{150–300 word summary in the member's voice — no compensation words (splits, caps, fees, rev-share tiers, stock, income), no promise of your time}

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
"{the guide's funnel URL + one question inviting agents to comment their situation — never a keyword of the plugin's own}"

──────────────── END SCREEN + CARD ────────────────
End screen:  {the next logical video} + subscribe  ·  Card:  {the resource, at the moment the script points to it}  ·  Playlist:  {the lane}

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

──────────────── THE GUEST'S DISTRIBUTION ASK   (send when it goes live) ────────────────
{the three sentences: share it to your story · post it with a line of your own · send it to three agents who are where you were — with the link and the clips}

────────────────────────────────────────────
Compliance — cardinal rules on every cut (the guest's answers too) · no compensation figures · former brokerage unnamed · consent recorded · disclosure in the description · [status].  ✓
```

### Thumbnail Brief (`yt-thumbnail` → a lean build sheet the member pastes into their brand project in Claude Design — claude.ai/design, or a Design canvas inside Cowork — or, before that project exists, into any Claude Design chat with the headshot attached, or hands to their designer; page order + final copy + placeholders only, the strategy stays in the chat; the brief is complete on its own; there is no separate thumbnail design skill)
```
THUMBNAIL BRIEF — {VIDEO TITLE}
Bucket {…}  ·  Title text vs thumbnail text must differ  ·  3 directions

──────────────── DIRECTION 1 ────────────────
Text (3–5 words):  {…}
Face / expression:  {…}
Supporting visual:  {…}   (supports the title, never repeats it; interview = both faces)
Pattern it follows:  {from the swipe file, when loaded}
(DIRECTION 2, 3 — same shape; each scored against the patterns)
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
For {avatar}  ·  Bucket Model  ·  Model file last reviewed {YYYY-MM-DD}  ·  {YYYY-MM-DD}

──────────────── THE SOURCED FACT SHEET ────────────────
   •  {fact used} — {source document, date}   (every fact; compensation figures never appear here or on camera)

──────────────── THE OUTLINE   (one band each — the two CTAs placed) ────────────────
HOOK (the question they typed) · RESOURCE CTA · OVERVIEW (history, positioning) · HOW COMPENSATION IS STRUCTURED
(the concepts, no figures — "the exact numbers on a call") · TOOLS + THE GAPS YOUR VALUE PROPOSITION FILLS ·
SUPPORT + TRAINING · BEYOND CLOSINGS (the concepts) · CULTURE + COMMUNITY · WHO IT'S FOR · WHO IT'S NOT ·
THE CALL CTA (the law's shape) + NEXT VIDEO

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

### YouTube Deep Dive (`yt-analytics` — saved as `YouTube Deep Dive — [Month YYYY] — YYYY-MM-DD`; no credibility stamp)
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
PART 5 — YOUR NEXT 30 DAYS   (keep · fix · the next cycle's 8 exact titles on the 3+1+4 mix, four or five of them inside 30 days at one a week · THE ONE MOVE, repeated)
════════════════════════════════════════════
════════════════════════════════════════════
APPENDIX — THE FULL NUMBERS
════════════════════════════════════════════
```
Structure and method: `${CLAUDE_PLUGIN_ROOT}/skills/yt-analytics/references/deepdive-guide.md`.

### Monthly Channel Review (`yt-triggers`'s scheduled run, or "run my monthly YouTube review" in chat — saved as `Monthly Channel Review — [Month YYYY] — YYYY-MM-DD`; the text also kept at `exports/youtube-review-YYYY-MM-DD.txt` so the Brain Board can read it; no live data unless connected; no credibility stamp; the same run writes each published card's 📊 AFTER IT'S OUT and one dated YouTube block in the Brain's performance ledger)
```
MONTHLY CHANNEL REVIEW — [MEMBER NAME] — [MONTH YYYY]
Window: {the month}  ·  Data: {the content log · the calendar · the interview pipeline · the conversations and the Top 50 · what the member added}  ·  {YYYY-MM-DD}

──────────────── THE MONTH IN ONE LINE ────────────────
   {one sentence, kindly — a month on plan is a month on plan}

──────────────── WHAT SHIPPED ────────────────
   {pipe table: planned · published · by lane — niche · interview · model; the cycle position; the cadence held or not}

──────────────── THE ATTRACTION SCOREBOARD ────────────────
   {pipe table: video · comments · conversations · calls booked — counted from the ledgers, never estimated; the agents who named a video}

──────────────── THE INTERVIEW PIPELINE ────────────────
   {candidates · invited · booked · recorded · published; who is overdue; the next guest to invite}

──────────────── THE DRAFTS WAITING ────────────────
   {the Monday Kickoff's drafts still at Scripted, by title — or omit}

──────────────── THE PACKAGING FIX ────────────────
   {one title or thumbnail to redo, and why — a month of click-through on record, never day one; none on record → "say 'add my attraction Studio numbers'"}

──────────────── WHERE MOMENTUM SLOWED ────────────────
   {name ONE — publishing · interviews · the break between views and conversations · the comment sweep}

──────────────── THE ONE MOVE ────────────────
   {exactly one action for next month}

──────────────── NEXT MONTH'S SLOTS ────────────────
   {the titles in order from the calendar, the interview to book first — four or five at one a week, eight or nine at two}
   {THE STEP-UP, when due — one line: two a week proposed, as a proposal the member answers}

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
