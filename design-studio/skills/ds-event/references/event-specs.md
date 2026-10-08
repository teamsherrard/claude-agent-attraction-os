# Event Specs — part of the ds-event skill

Read in full before building any piece.

## 1. THE EVENT BRIEFS (the two shapes the Events plugin writes — the producers own the field names)

`ev-promo` writes the first block (the graphics); `ev-runofshow` the second (the slides). Both arrive
pasted in chat and also sit in the event's folder (`03 · Content/Events/[code] · [Theme]/`): the DESIGN
BRIEF band of `Promo Calendar & Copy · [code] · [date]` and the SLIDE BRIEF band of `Run-of-Show ·
[code] · [date]`. Read the fields exactly as written below — never rename one, never ask for one the
block already carries.

**From `ev-promo` — the graphics:**
```
FOR ds-event (promo set for [event name])
Member: [name] · [brokerage, as compliance.md displays it, footer only] · [market]
Event: [name] · [live local / virtual / evergreen] · [date · time · timezone] · [Zoom / venue + address] · free · for [type of agent — career stage / production]
Hosts: [the member + co-hosts] · Guest speakers: [name · their one-line credential as they state it · consent on file · photo supplied — or none]
What they leave with (three real things): • … • … • …
Registration: [the page link — or "comment the word [KEYWORD]"] · Seats or deadline (real): [n seats / closes [date] — or none]
Pieces: 1. feed graphic (announcement) 2. story set (7 countdown frames, text above) 3. speaker spotlight card 4. [carousel 3–5 slides] 5. the banner / photo-spot backdrop (live only)
Copy on each: [verbatim from Step 3 — headline, sub-line, CTA]
Brand: [from brand-visual.md — logo, colours, type; or "Design Package first: ds-logo → ds-style-sheet → ds-brand"]
Required line (verbatim): [the compliance footer / brokerage name as required] · Brokerage-neutral: [yes (live local) / n/a]
Never on the graphic: splits, caps, stock, rev share, income, another brokerage's name, "recruiting."
Ad note: if any piece becomes a paid ad — Meta Employment special-ad-category; the brokerage's ad policy applies.
```
("text above" = the seven stories' on-screen lines and the sticker each names, from the promo doc's
STORIES band — they arrive inside **Copy on each**.)

**From `ev-runofshow` — the slides:**
```
FOR ds-event (workshop slides — [event name])
Member: [name] · [market] · [brokerage, compliance strip only where required]
Event: [event name] · [live local / virtual / evergreen] · [date · time · timezone] · [Zoom / venue] · booking link: [from operations.md or the Conversion block] · registration link or keyword: [for the resource / replay slide]
Deck: [n] slides, 16:9, the brand from brand-visual.md [or "Design Package first"]
1. Title — [event name] · [date] · [member name]
2. The promise — "[the transformation]"
3. Who this is for — three lines in their words
4–[n]. One slide per teaching beat: [title · the one line · the visual (template / screenshot / diagram)]
[n]. Do-this-now — the one step, big
[n]. Proof — [the agent's win, consented, first name only] / the member's own numbers, labeled
[n]. Q&A — the three questions
[n]. The iceberg — above the water: what you got today · below: mentorship · systems · community (never money)
[n]. Book a call / Come talk to us — the QR + the link [+ the scope line for a virtual room]
[n]. Your resource — [the guide / the slides] · the keyword or the QR
[n]. Thank you + the speakers' names
Compliance strip (where required, verbatim): [from compliance.md]
Never on a slide: splits, caps, stock, rev share, income, another brokerage's name or logo, "recruiting," "opportunity."
```

**What each field becomes — the promo brief (in the producer's order):**

| Brief field | Builds |
|---|---|
| Member: name · brokerage (as compliance.md displays it, footer only) · market | the member's name on every piece; the brokerage ONLY in the compliance strip; the market only where the brief's copy says it |
| Event: name | the title treatment — set once on the feed flyer, repeated on every piece and every slide |
| Event: live local / virtual / evergreen | the format (§2): which pieces exist, the timezone rule, the screens; the `format` tweak's default |
| Event: date · time · timezone | the date chip on every piece (virtual: the timezone mandatory; evergreen: "on demand", no date) |
| Event: Zoom / venue + address | the where line (§4 item 4) — the venue name and address in full on print; "on Zoom — link after you register"; "watch on demand" |
| Event: free | the FREE chip (§4 item 2) |
| Event: for [type of agent — career stage / production] | the who-it's-for line (§4 item 5), verbatim |
| Hosts: the member + co-hosts | the hosts' cut-outs (§4 item 6) — the member fronts the flyer, co-hosts at matching scale |
| Hosts: Guest speakers (name · credential as they state it · consent on file · photo supplied — or none) | one speaker card per guest (§3) and the countdown's speaker frame (§5): the credential verbatim, the photo as-is (none supplied → a typographic card), no consent on file → no card; "none" → no speaker cards, and the speaker frame carries the member |
| What they leave with (three real things) | the three leave-with lines on the flyers (§4 item 7); the same three lines the carousel's value slides carry (built by `ds-carousel`) |
| Registration: the page link — or "comment the word [KEYWORD]" | the ONE ask on every piece (§4 item 8) — "Save your seat" + the link, or "comment [KEYWORD]"; the QR on print; the link sticker plate on every story |
| Registration: Seats or deadline (real) | the seat chip or the "closes [date]" line only when the brief states one; "none" → nothing — never invented scarcity |
| Pieces 1. feed graphic (announcement) | the feed flyer (§4) and its story flyer; the print flyer too for a live local event; the registration post (the ask alone) |
| Pieces 2. story set (7 countdown frames, text above) | the countdown set (§5): the seven content frames in the brief's order, the brief's ≤2 lines on each verbatim, the sticker plate each names; an eighth replay frame only when the brief carries a replay line |
| Pieces 3. speaker spotlight card | the speaker card, one per guest named on the Hosts line |
| Pieces 4. [carousel 3–5 slides] | **`ds-carousel`** — never this skill. Hand the member one line: *"say 'design my carousel' and paste this promo brief — its event intake reads the carousel's lines."* It matches the flyer's title treatment and date chip, ships the LinkedIn PDF, and lands in the event's folder under `ds-carousel`'s canonical names |
| Pieces 5. the banner / photo-spot backdrop (live only) | the event banner (§7), live local only |
| Copy on each (verbatim from Step 3 — headline, sub-line, CTA) | verbatim on the piece — never rewritten; a line that will not fit is cut to its first clause and named |
| Brand | the Design System's tokens; "Design Package first" → stop and send them to `ds-logo → ds-style-sheet → ds-brand` |
| Required line (verbatim) | the compliance strip on every public piece, verbatim |
| Brokerage-neutral: yes (live local) / n/a | yes → no brokerage in the title, the hero, the venue line, or the who-it's-for line — the strip only (§4); n/a → the display rule as the Book's Compliance chapter says |
| Never on the graphic | the rules in §9, read back on every piece |
| Ad note | the Meta Employment special-ad-category note, said once, on any piece the member will boost or run as an ad |

**What each field becomes — the slides brief (in the producer's order):**

| Brief field | Builds |
|---|---|
| Member: name · market · brokerage (compliance strip only where required) | the footer (name · page) on every non-cover slide; the brokerage only in the compliance strip where the rule requires it |
| Event: event name · format · date · time · timezone · Zoom / venue | the title slide (the title treatment · the date — evergreen: no date); the format decides the interactive beats (virtual: chat prompts and a poll slide; live: "turn to the person beside you") and the invitation's wording |
| Event: booking link | the Book a call / Come talk to us slide — the QR + the link; the Thank you slide's contact line |
| Event: registration link or keyword | the Your resource slide (the keyword or the QR); the replay slide when the event has one |
| Deck: [n] slides, 16:9, the brand | the slide count and the master template (§6); "Design Package first" → stop and send them to `ds-logo → ds-style-sheet → ds-brand` |
| 1. Title | §6 item 1 — the title treatment, the hosts, the date |
| 2. The promise | §6 item 2 — the transformation, one line, big |
| 3. Who this is for | §6 item 3 — the three lines, verbatim |
| 4–[n]. One slide per teaching beat (title · the one line · the visual) | §6 item 4 — the beat's title, its one line, its visual as a figure (template / screenshot / diagram) |
| [n]. Do-this-now | §6 item 5 — the one step, big |
| [n]. Proof | §6 item 6 — the agent's win, consented, first name only; the member's own numbers labeled, charted when they are data |
| [n]. Q&A | §6 item 7 — the three questions |
| [n]. The iceberg | §6 item 8 — above the water · below the water; never money |
| [n]. Book a call / Come talk to us | §6 item 9 — the QR + the link [+ the scope line, verbatim, for a virtual room] |
| [n]. Your resource | §6 item 10 — the guide or the slides; the keyword or the QR |
| [n]. Thank you + the speakers' names | §6 item 11 — the speakers by name, the member's contact, the strip |
| Compliance strip (where required, verbatim) | the footer line on every non-cover slide where the rule requires it |
| Never on a slide | §9 plus "opportunity" — read back slide by slide |

The registration page's copy goes to `ds-funnel` (its own `FOR ds-funnel (registration shape — …)` block
from `ev-registration`); this skill hands `ds-funnel` the design block in §8. A brief in another shape is
read for these fields; only the missing ones are asked.

## 2. THE THREE FORMATS (`15-advanced-scaling/74` · `75` · `76`)

| Format | Mike's frame | Pieces this skill builds | Must-haves |
|---|---|---|---|
| **Live local** | be the one at the front of the room; fill it with personal invites + your agents sharing + one promo video; real value; networking and Q&A at the end; the iceberg close | feed + story + PRINT flyers · registration post · countdown set · speaker cards · event banner (the photo backdrop) · slides | brokerage-neutral title/hero/venue line; the venue address in full; the QR as-is on print |
| **Virtual** | a Zoom room and a clear topic; reach across markets; chat engagement; follow-up matters more | feed + story flyers · registration post · countdown set (its doors-open frame is the "we're live" story) · Zoom background · starting-soon · replay graphic (when the event has a replay) · slides with chat beats | the timezone on every piece; the recruiting-scope line respected in "who it's for" |
| **Evergreen** | recorded, on demand; Mike's gate (~250 agents + help) — the Events plugin decides | registration post + story · webinar cover · "watch now" graphic · slides built once, polished hard | no date ("on demand"); the same presentation for every viewer |

## 3. PIECES & TRUE SIZES

**Every graphic is ONE inline `<svg data-file="…">`** at its exact size (see the export-page
reference); the deck is 1920×1080 frames exported as a PDF from the Export menu.

| Piece | File | Size | Notes |
|---|---|---|---|
| Feed flyer | `flyer-post.png` | 1080×1350 | the master; headline, face, and the ask inside the central 1080×1080 and ~1012 px width |
| Story flyer | `flyer-story.png` | 1080×1920 | designed plate for the link sticker; key text out of the top/bottom ~250 px |
| Print flyer (live local) | `flyer-print.png` + PDF with bleed | 8.5×11 in (bleed 8.75×11.25; safe 8×10.5); 300 DPI | QR as-is with a quiet zone; address in full; reversed type ≥ 8 pt |
| Registration post | `registration-post.png` | 1080×1080 | one job: save your seat |
| Countdown stories ×7 (+1) | `countdown-01-pain-poll.png` · `-02-promise` · `-03-speaker` · `-04-do-this-now` · `-05-whos-coming` · `-06-countdown` · `-07-doors-open` (· `-08-replay` only with a replay line) | 1080×1920 | the brief's ≤2 lines on each, verbatim; the plate for the sticker each names (§5) |
| Carousel (Pieces 4) | `carousel-[event-slug]-NN.png` + the LinkedIn PDF — `ds-carousel`'s names | 1080×1350 | built by `ds-carousel`, never here |
| Speaker card | `speaker-[firstname].png` | 1080×1080 | consent; their credential as they state it |
| Zoom background | `zoom-background.png` | 1920×1080 | the centre (x 560→1360, y 120→1080) clear for the member; title small in a corner |
| Starting-soon screen | `starting-soon.png` | 1920×1080 | title · "starting at [time] [tz]" · the member's face · a quiet ground |
| Event banner (live local) | `event-banner.png` | 2400×800 layout the printer scales (tell them the final size) | the organization's logo large or repeating; the member's name; a brand ground that flatters phone photos |
| Replay graphics | `replay-post.png` · `replay-story.png` | 1080×1080 · 1080×1920 | "missed it? the replay" / "watch now" (evergreen) |
| Slide deck | `[event-slug]-slides.pdf` via the Export menu | 1920×1080 per slide | waves of ~6; the no-drift test |

Type floors at 1080 width: headline 96–140 px heavy · the date chip 48–60 px bold · support 34–40 px,
never under ~32 px · the compliance strip the only small line (~24 px). Slides: titles 64–88 px; dividers
96–120 px; big numbers 160–260 px; body 28–36 px; footer 16–20 px.

## 4. THE FLYER — ANATOMY (the copy spine, placed)

1. **The topic as a benefit headline** (the hero) — the member's words from the brief; the accent on
   one word.
2. **FREE** as a chip beside the headline (Mike: free, real value, no cost to share what's working).
3. **The date chip** — date · time · TIMEZONE (virtual: mandatory; live: the local zone is fine).
4. **Where** — the venue name and address (live), "on Zoom — link after you register" (virtual),
   "watch on demand" (evergreen).
5. **Who it's for** — one line, a type of agent by career stage or production; never a protected
   characteristic; never a brokerage.
6. **The hosts** — the member's expressive cut-out, full head with air, treated; co-hosts and guests
   at matching scale with consent (the brief's Hosts line: consent on file, photo supplied — or none).
7. **What you'll leave with** — three short lines, each a real thing ("the 3-video YouTube starter
   plan", "my open-house follow-up script", "a 30-day content calendar").
8. **The ask** — "Save your seat" as the CTA button + the link or "comment [WORD]" (the brief's
   Registration line); the seat or deadline line only when the brief states one.
9. **The proof chip** — one real credential from the Book, or none.
10. **The compliance strip** — the brokerage name as the display rule says; the chip where required;
    the only place the brokerage appears on a local event's flyer.

**Brokerage-neutral (live local):** the title, the hero, the venue line, and the who-it's-for line carry
no brokerage name or mark; "agents from every brokerage welcome" may be said; co-hosts from other
organizations are credited by name and organization only as they state it.

## 5. THE COUNTDOWN SET (the seven content frames `ev-promo` writes — never a bare number countdown)

`ev-promo`'s Stories are a 7-story countdown, one a day (the promo calendar names the day each one
posts: virtual T-13 → T-0, live T-21 → T-0); each carries ≤2 lines of on-screen text and names the
sticker to use. Those seven frames ARE the set. On every frame: one ground (the flyer's register flipped,
so the feed and the stories alternate), the title treatment and the date chip, the brief's lines verbatim
as the one copy slot, a designed tinted plate (never a dashed box) where the named sticker goes, the
link sticker plate wherever the frame asks for the link, the member's small cut-out where the frame has
no other face. Key text out of the top and bottom ~250 px. Every frame 1080×1920.

| # | Frame | File | The one copy slot (the brief's ≤2 lines) | The plate |
|---|---|---|---|---|
| 1 | The pain poll | `countdown-01-pain-poll.png` | the pain in the agent's words, as a question | the poll sticker plate (two answers) |
| 2 | The promise | `countdown-02-promise.png` | the transformation line | the link sticker plate |
| 3 | The speaker | `countdown-03-speaker.png` | "with [guest]" · one line of their proof as they state it (consent on file; their photo as-is) — a solo event: the member's own line | the link sticker plate; built so the speaker reposts it as-is |
| 4 | The do-this-now preview | `countdown-04-do-this-now.png` | one usable step from the training, real (the live calendar's story 4 may be the venue/room tease — the brief's text wins; the file name stays) | the link sticker plate |
| 5 | Who's coming | `countdown-05-whos-coming.png` | the social-proof line (a real count if the brief gives one; never an attendee's name) | the "I'm going" plate the member's agents repost over + the link plate |
| 6 | The countdown | `countdown-06-countdown.png` | the brief's line, the number the hero ("two days" · "tomorrow") | the countdown sticker plate |
| 7 | Doors open | `countdown-07-doors-open.png` | "doors open in an hour — link" (virtual) · "tonight — doors at [time]" (live) + the Zoom line or the venue | the link sticker plate (the "link up") |
| 8 — optional | The replay | `countdown-08-replay.png` | ONLY when the promo brief carries a replay line (a window or a link): the replay link or keyword | the link sticker plate |

No replay line → no replay frame (no replay is the Events plugin's default — a reason to show up live);
never invent one. The eighth frame never counts as one of the seven, and the set is never renumbered
into days ("7 days · 3 days · tomorrow") — the brief's content order is the order.

## 6. THE SLIDE DECK — RECIPE (from the run-of-show; the iceberg close; never a pitch slide)

**Structure (the run-of-show's brief lists the slides; its order wins — this is the backbone):**
1. **Title** — the title treatment, the hosts, the date (evergreen: no date).
2. **The promise** — "[the transformation]", one line, big.
3. **Who this is for** — the brief's three lines in their words, verbatim ("you're two years in, paying
   for leads, and still guessing where the next deal comes from").
4. **One slide per teaching beat** (3–5 beats; a section divider opens each) — the beat's title · its
   one line · its visual as a figure (the real template, screenshot, or diagram the brief names; any
   number with its source and period, charted when it is data) → the example when the run-of-show
   carries one (a real story from the member's story bank or an agent's win with consent, every size
   of win). **Interactive beats** sit at the run-of-show's chat prompts (virtual: "drop a 1 in the chat
   if…", a poll slide; live: "turn to the person beside you — 60 seconds") — a plain slide with the
   prompt large, at least one per section.
5. **Do-this-now** — the one step, big; the room does it.
6. **Proof** — the agent's win, consented, first name only / the member's own numbers, labeled as theirs.
7. **Q&A** — one slide, the three questions large.
8. **The iceberg** — ONE slide: above the water, what you got today; below the water, the three things
   in the member's words (mentorship · systems · community, and the call cadence from the Book's Offer
   chapter). Never money; no brokerage name as the pitch; no "come join us at [brokerage]".
9. **Book a call / Come talk to us** — the invitation: "if you want the how behind this, let's have a
   conversation" + the QR + the booking link [+ the scope line, verbatim, for a virtual room]; live:
   "come find me after".
10. **Your resource** — the guide or the slides; the keyword or the QR (the brief's registration link
    or keyword); the replay slide here when the event has one.
11. **Thank you + the speakers' names** — the speakers by name, the member's contact, the compliance
    strip.

**Counts:** a 45-minute virtual training ≈ 20–30 slides; a 90-minute live workshop ≈ 30–45; an
evergreen webinar ≈ 25–40. Build in waves of ~6; after every wave put the newest slide beside slide 2
— same title position, margins, footer, accent, craft — or fix it before continuing.

**Craft (the presentations rules):** one master template (title treatment, margins, accent, footer with
name + page); one idea per slide; the whole frame used in a balanced composition; layout variety
(divider · big statement · steps · figure · chart · quote · photo · two-column); real charts for every
number (bars from zero, source and period on the slide; teaching charts labelled "illustrative"); no
text walls; scrims under text on photos; talking points per slide in chat (2–4 bullets of what to SAY).

## 7. THE SCREENS

- **Zoom virtual background (1920×1080):** the brand ground at a quiet strength; the event title small
  in the top-left or top-right; the organization's mark in a corner; the centre clear for the member
  (Zoom mirrors the image — keep any text out of the centre and tell the member to turn off "mirror my
  video" if text reads backwards). Never busy; the member's face must read over it.
- **Starting-soon (1920×1080):** the title treatment, "starting at [time] [tz]", the member's face,
  "grab a coffee" or the member's own line, the agenda in three lines. Shown as the room fills.
- **The event banner (live local):** a wide layout the printer scales to the frame they own (a
  pull-up banner or a backdrop) — the organization's logo large, the member's name, the brand ground;
  built so phone photos in front of it read as the brand (Mike's example: everyone takes a picture in
  front of the banner and shares it).

## 8. THE DS-FUNNEL HAND-OFF (the registration page is built there, never here)

```
REGISTRATION PAGE DESIGN — for ds-funnel (registration shape)
Event: [title] · Format · When · Where (as on the flyer)
Title treatment: [font · size relation · the accent word] · Colour pairing: [ground · type · accent]
Hero: the feed flyer's composition (the member's cut-out [side] · the headline · the date chip)
Hosts treatment: [cut-out · matching scale for guests · consent noted]
Promise lines (three): • … • … • …
Form fields (from ev-registration): [First name · Email · Phone · "Which best describes you?" (six options) · the one-thing question when the doc carries it]
Thank-you state: "You're in — add it to your calendar" + the calendar link + "share this with an agent who needs it"
Compliance line: [verbatim] · Brokerage-neutral: [yes/no]
```

## 9. RULES THAT HOLD ON EVERY PIECE

- Real dates, real seats; never invented scarcity.
- The brokerage only in the compliance strip on a local event; never the pitch anywhere.
- Guests and room photos only with consent; never a stock crowd or a generated face.
- No compensation, split, cap, stock, rev-share, or income word on any piece or slide.
- The two cardinal rules; no protected characteristic in "who it's for".
- Attendees' names and emails never on a graphic; counts only, and only in the member's Brain.
- Any piece that becomes a paid ad: the Meta Employment special-ad-category note, said once.
