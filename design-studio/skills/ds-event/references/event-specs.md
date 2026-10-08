# Event Specs — part of the ds-event skill

Read in full before building any piece.

## 1. THE EVENT BRIEF (the shape this skill expects — the Events plugin writes it)

```
EVENT BRIEF — for ds-event (Claude Design)
Event: [title] · Format: live local / virtual / evergreen
When: [date] · [time] · [timezone]   (evergreen: "on demand")
Where: [venue + address] / "on Zoom — the link arrives after you register" / "watch on demand"
Topic (the hot topic agents care about): [one line] · Who it's for: [type of agent — career stage / production]
Free: yes · Seats or deadline (real): [n seats / registration closes date — or none]
Hosts: [member] [+ co-hosts] · Guest speakers: [name · their one-line credential as they state it · consent on file · photo supplied]
What they leave with (three real things): • … • … • …
Registration: [link] / comment the word [KEYWORD]
Pieces wanted: [feed flyer · story flyer · print flyer · registration post · countdown stories · speaker cards · zoom background · starting-soon · event banner · replay · slides]
Run-of-show (for the slides): [section · minutes · the how-to it teaches · the template/script/number it hands over]; interactive beats: […]; the close: the iceberg line in the member's words + "book a call with me"
Brand: use the Design System · Compliance: [brokerage display rule · "NOT SET YET"] · Brokerage-neutral: yes (live local)
Caption / promo copy (paste): […]
```
`ev-promo` writes the promo lines, `ev-runofshow` the run-of-show, `ev-registration` the page copy (that
one goes to `ds-funnel`). A brief in another shape is read for these fields; only the missing ones are
asked.

## 2. THE THREE FORMATS (`15-advanced-scaling/74` · `75` · `76`)

| Format | Mike's frame | Pieces this skill builds | Must-haves |
|---|---|---|---|
| **Live local** | be the one at the front of the room; fill it with personal invites + your agents sharing + one promo video; real value; networking and Q&A at the end; the iceberg close | feed + story + PRINT flyers · registration post · countdown set · speaker cards · event banner (the photo backdrop) · slides | brokerage-neutral title/hero/venue line; the venue address in full; the QR as-is on print |
| **Virtual** | a Zoom room and a clear topic; reach across markets; chat engagement; follow-up matters more | feed + story flyers · registration post · countdown set · Zoom background · starting-soon · "we're live" story · replay graphic · slides with chat beats | the timezone on every piece; the recruiting-scope line respected in "who it's for" |
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
| Countdown stories ×6 | `countdown-7days.png` · `-3days` · `-tomorrow` · `-today` · `-live` · `-replay` | 1080×1920 | the number the hero; plates for the countdown + link stickers |
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
   at matching scale with consent.
7. **What you'll leave with** — three short lines, each a real thing ("the 3-video YouTube starter
   plan", "my open-house follow-up script", "a 30-day content calendar").
8. **The ask** — "Save your seat" as the CTA button + the link or "comment [WORD]".
9. **The proof chip** — one real credential from the Book, or none.
10. **The compliance strip** — the brokerage name as the display rule says; the chip where required;
    the only place the brokerage appears on a local event's flyer.

**Brokerage-neutral (live local):** the title, the hero, the venue line, and the who-it's-for line carry
no brokerage name or mark; "agents from every brokerage welcome" may be said; co-hosts from other
organizations are credited by name and organization only as they state it.

## 5. THE COUNTDOWN SET

Six stories on one ground (the flyer's register flipped, so the feed and the stories alternate): the
number as the hero (7 · 3 · TOMORROW · TODAY · LIVE NOW · REPLAY), the title treatment under it, the
date chip, a designed tinted plate for the countdown sticker (days 7 and 3) and the link sticker
(every frame), the member's small cut-out. The "live now" frame carries the Zoom line or the venue;
the "replay" frame the replay link or keyword. Key text out of the top and bottom ~250 px.

## 6. THE SLIDE DECK — RECIPE (from the run-of-show; the iceberg close; never a pitch slide)

**Structure (the run-of-show's order wins; this is the backbone):**
1. **Cover** — the title treatment, the hosts, the date (evergreen: no date).
2. **Who's in the room** — the type of agent and the pain, one slide ("you're two years in, paying
   for leads, and still guessing where the next deal comes from").
3. **What you'll leave with** — the three real things (the same three as the flyer).
4. **Teaching sections** (3–5; a section divider opens each) — per section: the claim slide (one
   sentence) → the how-to slide(s) (the steps; the real template, script, or sheet shown as a figure;
   any number with its source and period, charted when it is data) → the example slide (a real
   story from the member's story bank or a partner's result with consent, every size of win).
5. **Interactive beats** (virtual: "drop a 1 in the chat if…", a poll slide; live: "turn to the
   person beside you — 60 seconds") — at least one per section; a plain slide with the prompt large.
6. **Q&A** — one slide, the question prompt large.
7. **The iceberg close** — ONE slide: "what you learned today is the tip of the iceberg" + the three
   things below the water in the member's words (the systems · the mentorship · the community and the
   call cadence from the Book's Offer chapter). No brokerage name as the pitch, no compensation word,
   no "come join us at [brokerage]".
8. **The invitation** — "if you want the how behind this, let's have a conversation — book a call
   with me" + the booking link (QR on a live deck) · live: "come find me after".
9. **Thank you + contact** — the member's name, the organization, the handle, the booking link, the
   compliance strip.

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
Form fields (from ev-registration): [first name · email · phone (optional) · one question]
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
