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
   plugin's home is `03 · Content/Long-Form/`, located by workspace ID) — the structured text was only the
   renderer's input; the deliverable is the `.docx`.

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
- Section headings: bold black + a thin light-grey underline. **Real** bullet lists. **Real** tables: near-black
  header row (white text) + light alternating rows. **No colour, no member branding** — one standard for all.
- The YouTube Game Plan carries `Powered by Mike Sherrard Coaching Inc Frameworks` (top byline + footer).
- Demo documents (house rules #12) carry `— DEMO —` in the filename and the meta line *"Demo document —
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

### YouTube Game Plan (the flagship — stamped)
Member-facing lines say *your Authority lane* / *your Proof lane* / *your Perspective lane* — never "(Authority in
the log)"; the log vocabulary stays in `brain-contract.md`.
```
YOUTUBE GAME PLAN — [MEMBER NAME]
Known for: [niche]  ·  Attracting: [avatar 1] · [avatar 2]  ·  Prepared [Month Year]
Powered by Mike Sherrard Coaching Inc Frameworks


════════════════════════════════════════════
READ THIS FIRST
════════════════════════════════════════════
{where the channel is + the verdict · the insight · the plan in one line · the 90-day target in conversations and calls}

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
   RESOURCE CTA (inside minute 1) — {"grab the [resource], link in the description" — from offer.md}
   VALUE — {as long as it needs to be, as short as it can be; bullets}
   CALL CTA (~1/3 in) — {the warm invite to book a private call — the value named, never the brokerage}
   PAYOFF + NEXT VIDEO — {deliver the promise; point to the next logical video}


════════════════════════════════════════════
THE FIRST 90 DAYS   (the 8-video cycle: 3 niche · 1 model · 4 interviews · {cadence}/week)
════════════════════════════════════════════
   Week 1 · Video 1 — {exact title}   (Problem)
   Week 1 · Video 2 — {exact title}   (Interview · {guest})
   Week 2 · Video 1 — {…}   (Situation)
   …  (one video per row; cycle boundaries marked; interviews batched where the member records in sittings)


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


────────────────────────────────────────────
{closing — one honest paragraph: consistency before optimization; three years; chapter one}
Powered by Mike Sherrard Coaching Inc Frameworks
```

### Script (the four formats + interview)
TITLE/meta → bands for `HOOK · 0:00` → `RESOURCE CTA · ~0:45` → numbered `1 · LABEL · MM:SS` body sections
(3–5) → `CALL CTA · ~{1/3 in}` → `PAYOFF` → `NEXT VIDEO` → heavy band `CHAPTERS` → heavy band `45-SECOND SHORT` →
footer with the stories used and the compliance line. Interview scripts carry `INTRO (record last)` ·
`QUESTION MAP` · `OUTRO + JOINT CTA`. Detailed skeleton:
`${CLAUDE_PLUGIN_ROOT}/skills/yt-script/references/script-format.md`.

### Channel Page Kit
```
CHANNEL PAGE KIT — [MEMBER NAME]
[Channel handle]  ·  Known for: [niche]  ·  [YYYY-MM-DD]

──────────────── CHANNEL DESCRIPTION ────────────────
   >> PASTE INTO:  Studio → Customization → Basic info → Description (opening paragraph)
{2–3 sentences: who it's for (the avatar) · what they'll learn · the cadence}

──────────────── ABOUT SECTION ────────────────
   >> PASTE INTO:  same field, directly below the description
{who it serves · the lanes by name · one real proof line · the resource + the booking link · the disclosure block}

──────────────── LINKS ────────────────
   •  {Booking link} — the Partner Call
   •  {Resource} — {the lead magnet, or the community}
   •  {ONE social}

──────────────── CHANNEL KEYWORDS ────────────────
   >> PASTE INTO:  Studio → Settings → Channel → Basic info
{8–12 agent-search phrases}

──────────────── PLAYLISTS ────────────────
   •  {Model explained}:  {one-line description}
   •  {Agent success stories}:  {…}
   •  {Problem lane}:  {…}   •  {Situation lane}   •  {Future lane}

──────────────── BANNER BRIEF   (for aa-brand-kit-design in Claude Design) ────────────────
Headline:  {who it's for + what they get}
Subline:  {cadence / the invite}
   >> Build with aa-brand-kit-design; finished image → Customization → Branding → Banner; copy → 02 · Brand

──────────────── UPLOAD DEFAULTS ────────────────
   >> SET ONCE IN:  Studio → Settings → Upload defaults
{default description: booking link line 1 · resource line 2 · the disclosure block · default tags · category · visibility · language}

──────────────── THE CTA LINE   (every video — the value named, never the brokerage) ────────────────
Resource (inside minute 1):  "{the free thing, in your voice — 'link in the description'}"
Call (a third of the way in):  "{the warm invite to a private one-on-one call — the value named, 'I'd love to hear where you're at'}"

──────────────── CHANNEL TRAILER ────────────────
{new channel: "say 'make my attraction video: my channel trailer'" · existing: the strongest recent video, named}

────────────────────────────────────────────
Compliance — cardinal rules · no compensation figures · disclosure present · [status].  ✓
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
{line 1: Book a private one-on-one call: [link]}
{line 2–3: the resource link · contact line if listed}
{150–300 word summary in the member's voice}

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
"{the resource link + one question inviting agents to comment their situation}"

──────────────── END SCREEN + CARD ────────────────
End screen:  {the next logical video} + subscribe  ·  Card:  {the resource, at the moment the script points to it}  ·  Playlist:  {the lane}

──────────────── WHY THESE   (three plain sentences, for you — not for pasting) ────────────────
{the phrase the title targets and the evidence seen · which tags carry real demand · why the description order is the conversion order}

──────────────── DISCLOSURE BLOCK   (paste at the end of the description) ────────────────
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

──────────────── QUESTION MAP   (not a script — the five beats, any order) ────────────────
   BEFORE — {what business was like before: 2–3 open questions}
   THE SHIFT — {what made them decide to move, what the hesitation was: 2–3}
   SINCE — {what it has been like since partnering — support, training, community, in their words: 2–3}
   THE RESULTS — {outcomes in their words — freedom, support, the category of result; never a figure they did not volunteer: 1–2}
   ADVICE — {for an agent standing where they stood: 1–2}
   {TYPE-SPECIFIC BEATS — new agent: the first-30-days routine · turnaround: what was missing before (no names, no blame) · top producer: what changed in leverage and time · team leader / broker-owner: what they kept, what overhead disappeared · first agent attracted: how that conversation happened}
   Interviewer rules:  the guest is the star · never interrupt · let emotion sit · add a layer only after they finish · redirect on camera if they knock a brokerage or a person (that part is cut)

──────────────── INTRO   (record LAST, after you know the story — 45–75 s) ────────────────
{the transformation as the title promises it → who this is for → two or three specific things coming → one honest line edifying the guest → the resource CTA in one breath → "let's get into it"}

──────────────── OUTRO + JOINT CTA   (30–45 s) ────────────────
{thank the guest and name the one thing to take from them → "if you want to know exactly how {guest} did this and get their support and mine for free, click the link in the description and book a private call" → the next video (another interview on the same pain, or the model explained) → the end screen}

──────────────── THE INVITE   (DM or email, in your voice — you send it) ────────────────
{why them · the 30–45 minute format · the recording link · "you are the story" · the one prep line: "think about where you were before and the moment things changed"}
Consent line:  {the plain okay to publish, use clips, and share their name as written}

──────────────── THE GUEST'S DISTRIBUTION ASK   (send when it goes live) ────────────────
{the three sentences: share it to your story · post it with a line of your own · send it to three agents who are where you were — with the link and the clips}

────────────────────────────────────────────
Compliance — cardinal rules on every cut (the guest's answers too) · no compensation figures · former brokerage unnamed · consent recorded · disclosure in the description · [status].  ✓
```

### Thumbnail Brief (`yt-thumbnail` → pasted by the member into their Brand HQ project in Claude Design; there is no separate thumbnail design skill)
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

### Lead Map (`yt-leads` — only when a resource exists)
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
{the exact Partner Call invite + booking link}
(We map the content; your Lead Magnet system writes and designs it in Week 6.)
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
BOOK-A-CALL CTA + NEXT VIDEO

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
PART 5 — YOUR NEXT 30 DAYS   (keep · fix · ~8 exact titles on the 3+1+4 mix · THE ONE MOVE, repeated)
════════════════════════════════════════════
════════════════════════════════════════════
APPENDIX — THE FULL NUMBERS
════════════════════════════════════════════
```
Structure and method: `${CLAUDE_PLUGIN_ROOT}/skills/yt-analytics/references/deepdive-guide.md`.

### Repurposing Pack
```
{VIDEO TITLE} — REPURPOSING PACK
From the long-form script  ·  {YYYY-MM-DD}

════════════════ SHORTS (3) ════════════════
SHORT 1 — {angle}
   {hook → one point → the invite}

════════════════ CAROUSEL (1) ════════════════
Slide 1 {…} | Slide 2 {…} | …   (copy only — designed from this in your short-form system or your Brand HQ project in Claude Design)

════════════════ STORIES (5) ════════════════
   1.  {…}

════════════════ EMAIL (1) ════════════════
Subject:  {…}
{body + the invite}

════════════════ BLOG (1) ════════════════
Title:  {…}
{body}

════════════════ CONVERSATION STARTERS (3)   (personalised per agent — you send) ════════════════
   1.  {an opener the member can send an agent who'd care about this video — no pitch}
```

Same shape every time, in the member's own voice. This is the standard for what lands in their workspace.
