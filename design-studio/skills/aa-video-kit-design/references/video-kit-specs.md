# Video Kit Specs — part of the aa-video-kit-design skill

Read in full before building any piece. The zones, the canonical names, the render rule, the engine
notes, and the spec fields are the sync contract with the member's AI Editing Studio (Riverside) — they
were measured on real edits, not assumed. Change the words on a piece to the member's; never change a
number here.

## 1. THE ZONES — build to these numbers (they are where the editor puts things)

**The editor's text rule, which every zone obeys:** the editor types ONE line, never wraps, at 64 px on
16:9 and 72 px on 9:16, centred on the FRAME centre line (x 960 on 16:9, x 540 on 9:16) at y 845 on 16:9
and y 250 on 9:16. A character is about 0.55 × the type size wide, so a zone's character budget = zone
width ÷ (0.55 × size). The editor shortens the words, never the type — so state every empty zone's
rectangle and budget in the spec. Panels are **100% opaque** (never below 95%); transparency is for the
space AROUND the element, never inside it.

**16:9 (1920×1080).** The member fills the top two-thirds of a horizontal frame, so everything lives in
the LOWER THIRD.

- **Hook banner:** a wide bar, x 160 → 1760, y 770 → 920 (150 tall), corners and accent to the brand.
  The bar carries NO logo mark, kicker, tagline, or sample headline inside it: a mark at either end gets
  typed over on a long hook. The **empty zone is exactly x 320 → 1600 (1,280 px), centred on x 960,
  centre y 845** — up to ~35 characters at 64 px. If the brand wants its mark on the hook, it sits as a
  small tab ABOVE the bar's right corner (x 1600 → 1760, y 710 → 766), never inside the bar.
  High-contrast field (a dark panel for white type, or light for dark type — pick from the brand and
  keep it for every piece).
- **Name strip:** bottom-left, x 96 → 1150 (about 55% of the frame), y 860 → 1010 (150 tall). Line 1:
  the name, 64 px+ bold. Line 2: the role line · the brokerage on ONE line at 40 px+ ("Team leader ·
  The Lakeline Collective · Real Broker, LLC" — the role line is who the member is to agents, from the
  Book's five profile answers; the regulated title only where the Book confirms it; the brokerage only
  where the member's rules require it on video). About 48 characters fit at 40 px: when the role line
  plus the required brokerage runs longer, shorten the role line ("Team leader · Real Broker, LLC") —
  never the brokerage, never the type. Logo mark or headshot circle at the left end, no taller than the
  strip. The licence number, where required, lives on the CTA banner and the end card — the strip stays
  two lines, 150 tall. This is the piece agents notice first on other leaders' videos; make it feel like
  a broadcast lower third, not a label.
- **Emphasis pop-up:** centred, x 360 → 1560 (about 62%), y 770 → 920. **Empty zone x 400 → 1520
  (1,120 px), centre x 960 / y 845** — ONE line at 64 px, ~30 characters. A short phrase or a short
  numeric string ("Day 30 · the check-in", "3 calls a week") is typed into this same zone — there is no
  separate stat-card file — so a short numeric string must read as well as a phrase. Same family as the
  hook banner but visibly the "smaller sibling".
- **CTA banner (primary):** x 160 → 1760, y 740 → 950 (210 tall). Baked: the Book's EXACT CTA line at
  64 px. If the line is ≤ 22 characters, the pill sits on the same row at the right; otherwise use the
  two-row layout: row 1 the CTA line full width (y 764 → 828), row 2 the pill (56 tall, 44 px text) at
  the left with the compliance line at 32 px to its right, both vertically centred (y 852 → 908). The
  pill carries the link or handle in the accent colour with text in the panel colour (white on a
  saturated accent fails 4.5:1). If a headshot is attached and showHeadshot is on, a 120 px circle crop
  sits at the left end and the ask shifts right by 150 px; if NO headshot is attached, build without the
  circle and say so — never a placeholder, stock face, or generated face on an exported piece. It
  appears while the member SAYS the CTA and holds to the last frame, so it must read in three seconds.
- **CTA pack variants:** the primary banner's EXACT geometry (x 160 → 1760, y 740 → 950, 210 tall)
  WITHOUT the compliance line, one short ask ≤ 34 characters + the pill, a leading glyph from the icon
  family at the left end. The primary's row rule applies unchanged: an ask of ≤ 22 characters may share
  its row with the pill; anything longer is the two-row layout (row 1 the ask full width, row 2 the pill
  at the left). A one-row band with a 32-character ask is exactly what clips "Comment GUIDE for the free
  guide" to "…for the free gu". The pill never touches the words; if it still would, shorten the ask,
  never the type.
- **Safe margin:** nothing within 5% of any edge (96 px sideways, 54 px top and bottom).

**9:16 (1080×1920).** Captions live in the lower-centre, the face sits in the middle, and the platform
draws its icon rail down the right edge, so every piece lives in the TOP ZONE and stays out of the
right 12%.

- **Hook banner:** the bar x 60 → 1020, y 160 → 340 (180 tall), with its RIGHT 70 px (x 950 → 1020) a
  solid accent block that the platform's icons may cover. The **empty zone is exactly x 140 → 940 (800
  px), centred on x 540, centre y 250**: ONE line at 72 px, **≤ 20 characters**.
- **Emphasis pop-up:** x 100 → 980, y 160 → 340, same band; empty zone x 140 → 940 (the hook has cleared
  by the time a pop-up appears; they never share a moment).
- **CTA banner (primary):** x 60 → 1020, y 160 → 400 (240 tall), the right 70 px an accent block: a
  SHORT ask of ≤ 20 characters on ONE line at 72 px ("Book a call with me" fits; "Comment GUIDE for the
  free guide" → "Comment GUIDE"), the pill under it (60 tall, 44 px text), the compliance line at 44 px.
  Layout inside the 240: pad 20 · ask 72 · gap 12 · pill 60 · gap 12 · compliance 44 · pad 20. Show the
  member the shortened asks before rendering; the full line lives on the 16:9 banner and in the spec.
- **CTA pack variants (9:16):** the same template without the compliance line, y 160 → 340 (180 tall),
  the short ask + the pill. Layout inside the 180: pad 18 · ask 72 · gap 12 · pill 60 · pad 18 — the pill
  always UNDER the ask, never beside it.
- **Name strip (optional, default NOT built):** top-left, x 60 → 700, y 160 → 320. Build it only if the
  member asks; mark it "not built" in the manifest and spec.
- **Safe margin:** left 5% (54 px), **right 12% (nothing past x 950 except an accent block)**, top y 0 →
  160 clear (platform chrome), bottom 25% clear (captions + platform buttons).

## 2. PIECE BY PIECE

- **Hook banner** — the brand's signature bar. Accent stripe, the panel colour, and NOTHING ELSE inside
  the zone: no kicker line, no tagline, no sample headline. A baked word in the zone collides with the
  episode's headline. Energy level sets how loud the shape is, never whether words are in it.
- **Name strip** — text baked (name and role line never change per episode). Everything outside the
  strip transparent. One per person who fronts videos, on the same template (§8).
- **Emphasis pop-up** — the hook banner's smaller sibling, zone empty. Used a few times per long-form
  video beside a key phrase; the editor types the phrase.
- **CTA banner (primary)** — the Book's exact CTA line + pill + compliance line; the editor holds it to
  the last frame. Design the pill to look tappable.
- **CTA pack** — the same banner template, one file per ask a leader makes on camera (the eight keys
  and the attraction wording in the SKILL file's pack table). The words are baked, so the editor adds
  nothing on top.
- **End card** *(optional — offer it, never force it)* — the ONE opaque full-frame piece: the brand at
  its best for the last 3–5 seconds of a long-form video, with the CTA, link/handle, logo, the headshot
  as-is if they want it, and the compliance line. Reels do not use it. If the member's brand kit
  (`aa-brand-kit-design`) already has an end screen or closing look, match it.
- **End screen** — 1280×720, 16:9 long-form only (Shorts never show it), built around YouTube's
  clickable elements: a clear 16:9 rectangle zone (next video, ≈510×290 px) and a clear circle zone
  (subscribe, ≈150–196 px across), both at least 64 px off every edge, branded background, "Watch next" +
  "Subscribe" prompts BESIDE their zones, the brokerage name (and licence # where required) as ONE small
  line beside the logo, and the bottom ~90 px empty (the player's scrub bar sits there). One end screen
  per brand; reuse the brand kit's `end-screen-youtube.png` composition if it exists, at this size.
- **Icon pack** — twelve icons the editor pops beside a key word. One family: the same badge shape for
  all twelve (a rounded tile at the banners' radius for Straight/Rounded edges, a circle for Angled),
  the panel colour as the badge, the accent as the glyph, one bold shape with no thin strokes, no text,
  on a FULLY TRANSPARENT 400×400 canvas with ~10% clear space inside the edge. They must read at 100 px
  wide (the editor's size on a YouTube video) and at 150 px on a reel. Canonical names — keep them exact,
  the editor matches them to spoken words: `icon-arrow-up.png` (growth, a step up) ·
  `icon-arrow-down.png` (a drop, fewer) · `icon-check.png` (a tip, a done item) · `icon-pin.png` (a
  place, a market) · `icon-dollar.png` (the cost of leads, a fee — never the member's income) ·
  `icon-house.png` (a listing story, a home) · `icon-key.png` (a first deal, a closing) ·
  `icon-calendar.png` (a date, a deadline, the weekly call) · `icon-phone.png` (call or text, the
  partner call) · `icon-chart.png` (a scorecard, a trend) · `icon-star.png` (a win, a highlight) ·
  `icon-alert.png` (a warning, a mistake to avoid). TWELVE separate frames, each named `icon-<name>`; a
  contact sheet of them is for review only and is never exported as a deliverable. If the member asks
  for emoji on their videos, make them as icons in this pack.
- **Preview sheets** — MANDATORY, and the most important thing you present. The hook banner, the
  emphasis pop-up, the CTA banners, and the name strip share the SAME band, so they can never be shown
  at the same time — a single composite would pile four bars on top of each other. Each preview sheet is
  therefore a **2×2 GRID OF MOMENTS** on one canvas (`preview-16x9.png` at 1920×1080 = four 960×540
  tiles; `preview-9x16.png` at 1080×1920 = four 540×960 tiles), every tile the same talking-head base
  with ONE moment composited exactly where the editor will put it, at half scale: (1) HOOK — the hook
  banner with the sample headline typed in the zone in the editor font; (2) NAME — the name strip alone;
  (3) EMPHASIS — the emphasis pop-up with a sample phrase and one icon beside it; (4) CTA — the primary
  CTA banner. Label each tile in small plain type outside the frame ("Opening", "Name strip", "Pop-up",
  "Call to action"). Add `preview-cta-pack-16x9.png` (1920×1080, a 2×4 grid of the eight pack banners
  over the same base). **The base:** ask once — "Upload a screenshot from one of your videos (any frame
  where you're talking to camera)" — and use it if given; otherwise DRAW the stand-in yourself inside the
  tool: a mid-grey room gradient (#5A5A5A → #3A3A3A) and a flat head-and-shoulders silhouette in #8A8A8A
  with no facial features, head as an oval centred at x 960, y 190 → 560 on 16:9 (shoulders from y 560
  down), and at x 540, y 520 → 1000 on 9:16. Never search for, generate, or embed a photorealistic face;
  never use the member's headshot as the talking head. The preview sheets are OPAQUE (the base fills the
  frame) and are the ONLY frames that carry sample words — never an income or production line among
  them. Because each tile is half scale, THE 25% TEST is run at 50% zoom on these sheets.
- **Animated end card and logo sting** *(optional — not built in this Studio)* — the editor accepts two
  moving pieces, both full-frame and opaque: `animated/end-card-16x9.mp4` / `animated/end-card-9x16.mp4`
  (the end card brought to life — the panel wipes in, the logo settles — 4–6 s, under 20 MB) and
  `logo-sting.mp4` at the kit root (3–5 s). A member who makes them in any video tool names them exactly
  so and drops them in the kit folder; the manifest and the spec list them as "not built". Never
  animate a banner, strip, pop-up, or icon (§5).

## 3. THE BOARD — HOW THE CANVAS MUST LOOK (a contact sheet, not a scatter)

A kit of thirty-nine mostly-transparent frames looks like debris on a grey board: a small bar floating
in a big invisible rectangle, forty times over. Two rules fix that, and neither one changes a single
exported file.

**1. The stage (design-time only).** Inside EVERY overlay frame — hook, name strip, emphasis, CTA, the
sixteen CTA-pack frames, the twelve icons — draw a full-canvas stand-in video frame as a layer UNDER
the piece: the same base the preview sheets use, the mid-grey room gradient (#5A5A5A → #3A3A3A) with
the featureless head-and-shoulders silhouette in #8A8A8A placed exactly as the preview base describes
(icons: the gradient only, no silhouette). ONE project-wide tweak, **"Show stage"** (`showStage`,
default ON), switches the stage in every frame at once. ON: each frame on the board is a real-looking
video still with the piece sitting where the editor will put it, so every piece can be judged at a
glance and the board reads as a contact sheet. OFF: every overlay frame is see-through again, and the
export is the transparent full-canvas PNG the editor needs. The stage can never reach an export: the
Download button renders only each piece's SVG, and the stage is a separate layer BEHIND the SVG, never
inside it — nobody has to remember to switch anything off. The stage carries NO sample words: the hook
and emphasis zones stay empty, and sample words live on the preview sheets only. The frame's own
background stays NONE at all times; the stage is a layer, not a fill.

**2. The layout map (one row per build stage).** Every stage of the build is ONE ROW of frames; rows
stack top to bottom in this order; every row starts at the same left edge; equal gaps between frames
(about 120 px) and between rows (about 240 px); nothing else on the board.

| Row | Frames, left to right |
|---|---|
| 1 · Overview | `preview-16x9` · `preview-cta-pack-16x9` · `preview-9x16` · `video-brand-spec` |
| 2 · 16:9 core | `hook-16x9` · `lower-third-16x9` (then any co-host strips) · `emphasis-16x9` · `cta-16x9` |
| 3 · 16:9 CTA pack | `cta-subscribe-16x9` … `cta-follow-16x9` — eight, in the pack table's order |
| 4 · 16:9 closing | `end-screen` · `end-card-16x9` (if built) |
| 5 · 9:16 core | `hook-9x16` · `emphasis-9x16` · `cta-9x16` · `lower-third-9x16` (if built) |
| 6 · 9:16 CTA pack | `cta-subscribe-9x16` … `cta-follow-9x16` |
| 7 · 9:16 closing | `end-card-9x16` (if built) |
| 8 · Icons | the twelve icon frames in canonical order |
| 9 · Export | the export page: the **Download the kit** button, its status line, the spec text |

Put each stage's frames into their row as you build them — never "arrange later". If the tool will not
place a frame where you ask, keep the ORDER exact (the order above is the reading order) and tell the
member in one line that frames can be dragged into rows. Before presenting, delete every scratch,
empty, duplicate, or test frame: the finished board is these nine rows and nothing else, "Show stage"
ON, zoomed to fit, the overview row at the top.

## 4. VIDEO-SAFE DESIGN RULES

- **Readable in one second at phone size** — big type, high contrast, no subtle greys on video. **THE
  25% TEST (run it, don't guess):** view the preview sheet at 50% zoom (its tiles are half scale — that
  is a phone in a hand). Every word still readable, or the type gets bigger. Hard px floors: on
  1920×1080 — smallest text 32 px, name 64 px+, CTA line 64 px+; on 1080×1920 — smallest text 44 px, CTA
  line 72 px+.
- **Compression-safe colour** — uploaded video is chroma-compressed. Carry ALL text contrast in
  LIGHTNESS (light-on-dark or dark-on-light, 4.5:1 or stronger); never set text under ~60 px in
  saturated red or saturated blue. Saturated accents live in stripes, pills, badges, and the karaoke
  highlight, not in small type.
- **Panels are solid.** 100% opacity (never below 95%): a half-transparent panel over a moving
  background reads as a mistake.
- **No hairlines or fine texture** (they shimmer at video compression); solid shapes, confident
  weights, one corner style everywhere. **bannerEdge by energy level:** Calm & premium → Straight;
  Balanced → Rounded (24 px); Bold & punchy → Angled (left edge cut ~12°, plus a 48 px accent block).
- **The face is sacred.** Nothing in the middle of the frame on either format. On 16:9 the banners
  start at y 740 or lower; on 9:16 they end at y 400 or higher.
- **Transparency is real — and here is how.** Every overlay frame has NO background fill at all, and
  its SVG has no background rect either — the stage lives outside the SVG (remove/disable the frame
  background — do not set it to white, black, or the panel colour), and nothing is drawn outside the
  element's zone. NEVER paint a checkerboard, grey field, or "transparent-looking" pattern to simulate
  transparency — it exports as pixels and blocks the video. If a true see-through export isn't
  achievable in this project, say so and stop: an opaque "overlay" is not usable on video, and the
  editor's setup refuses a fully opaque hook, emphasis, name-strip, or CTA file.
- **Empty zones stay EMPTY** — sample words appear on the preview sheets only; the exported hook banner
  and emphasis pop-up carry none. **Never bake a placeholder** ("[Brokerage]", "[LICENCE #]", a dummy
  number, a labelled photo slot) into any exported piece: it ships on every video and the editor cannot
  remove it. Missing value → omit that element and flag it.
- **The leader palette, never the brokerage's.** The panel, accent, and glyph colours come from the
  member's Design System (visibly distinct from the brokerage's colour family by rule); the brokerage
  appears as text on the three compliance pieces only, never as a mark on a banner.

## 5. ENGINE NOTES — WHAT THE VIDEO EDITOR CAN AND CANNOT DO WITH THESE FILES (live-tested, Sept 2026)

Design to these facts; they were measured on real edits, not assumed.

- **Transparent PNG works. Transparent VIDEO does not.** In Riverside a PNG keeps its transparency
  perfectly: the speaker shows through every clear pixel. A transparent video (WEBM or MOV with an alpha
  channel) is flattened and the clear area turns SOLID BLACK. So every overlay is ALWAYS a PNG, and
  anything animated is ALWAYS full-frame and opaque.
- **The editor supplies the motion.** It slides the hook banner and name strip in from the left, pops
  the emphasis panel, the CTA banners and icons, and fades everything out. Design each piece as a clean
  still that looks right at rest; do not fake motion blur or build "in-between" frames.
- **If the member asks you to animate the banners, strips, pop-ups, or icons ("make the CTA banners
  move", "animated lower thirds"): do not build them.** Say why in one line — Riverside flattens any
  transparent video into a solid black box over their face, and their editor already slides, pops, and
  fades the still PNG pieces on every edit — and name the two moving pieces that DO work: the
  full-frame animated end card and the logo sting (§2, made outside this Studio). An animated banner
  exported as MP4 or WebM is a file they cannot use, and exporting it is wasted time.
- **Claude Design's Export menu has no PNG option** (it writes HTML and PDF). The kit's own Download
  button IS the picture export. If the member asks how to export PNGs, the answer is always the button
  — never the menu, never one frame at a time, never a browser extension.
- **The editor places every overlay full-canvas, centred, at 100%.** That is why each piece is drawn on
  the full frame in its zone: the file's own geometry IS the placement. There is no per-piece positioning
  to get wrong at edit time.
- **The headline and the emphasis phrase are typed by the editor, in ONE editor font,** centred on the
  frame centre line at y 845 (16:9) / y 250 (9:16), one line, 64 / 72 px, never wrapped. Riverside
  offers a fixed set of families, named WITH the weight where the family carries one: `Inter Bold`,
  `Poppins ExtraBold`, `Sora SemiBold`; `Montserrat`, `Oswald`, `Merriweather`, `DM Mono`, `Calistoga`
  (no suffix). Map the brand's headline font: heavy grotesque/display (Archivo Black, Anton, Bebas) →
  `Poppins ExtraBold`; humanist or system sans (Inter, SF, Helvetica, Lato) → `Inter Bold`; geometric
  (Futura, Montserrat, Gotham) → `Montserrat`; condensed → `Oswald`; serif → `Merriweather`;
  rounded/friendly display → `Calistoga`; mono → `DM Mono`. Never write a plain "Inter" or "Poppins" in
  the spec — the editor cannot resolve it. If Claude Design cannot load the brand font for the baked
  text, set the baked text in the editor font so baked and typed words match — and say so in the spec.
- **Character budgets:** about 0.55 × the type size per character. 16:9 hook zone (1,280 px) ≈ 35
  characters at 64 px; emphasis (1,120 px) ≈ 30; 9:16 zones (800 px) ≈ 20 at 72 px. Write the budgets
  into the spec.
- **One file, reused forever.** The editor registers each file once and reuses it on every video, so a
  rebrand is a file swap under the SAME name.
- **The eight pack keys are the editor's.** Its setup registers `cta-<variant>-16x9.png` and
  `cta-<variant>-9x16.png` under the keys `subscribe`, `comment`, `guide`, `call`, `book`, `dm`,
  `link`, `follow`, and its CTA rules pop the matching banner on the spoken ask ("comment [word]" →
  `comment`, "free guide" / "grab my guide" → `guide`, "book a call" / "partner call" → `book`, "DM
  me" → `dm`, "link below" / "link in bio" → `link`, "follow" → `follow`, "subscribe" → `subscribe`,
  "give me a call" / "let's talk" → `call`); co-host strips are found by `lower-third-16x9-<firstname>`.
  A renamed key is a banner the editor never finds.

## 6. THE VIDEO BRAND SPEC (design it as a clean one-pager AND save it as text in the kit folder)

A single reference sheet the editor's setup transcribes into config. Deliver it twice:
`video-brand-spec.png` (the designed one-pager, for people — a board page) and `video-brand-spec.md`
(the identical fields as plain text, written by the Download button INTO the kit folder — the file the
editor reads). Include exactly these fields with real values:

- **Identity + CTA (exactly as baked on the pieces):** the member's name · on-screen role line (the
  regulated title only where it applies) · brokerage (as the display rule says) · the organization's
  name · city or market (only when the member attracts locally) · website · **CTA line** (verbatim from
  `cta-*.png`) · **CTA detail** (the link / handle / keyword on the pill) · booking link · **compliance
  line** (verbatim, or "none required (confirmed with [who], [date])").
- **Colours:** background hex · primary hex · accent hex · panel colour (the banners' fill) — from the
  member's Design System tokens.
- **Fonts:** headline font · body font (the brand's real faces) · **editor font** — ONE family spelled
  exactly as the editor names it (§5); the editor uses it for the typed headline, the pop-up phrase, and
  the captions.
- **Style pack + caption look (two literal values the editor stores side by side):** Calm & premium →
  style pack `clean-minimal` + caption look `clean-minimal` (Inter Bold, soft shadow, size 76) ·
  Balanced or Bold & punchy → style pack `bold-kinetic` + caption look `bold-karaoke` (Poppins
  ExtraBold, outline, size 84) · a luxury / condensed-type brand → style pack `cinematic` + caption look
  `cinematic` (Oswald, UPPERCASE, size 80) · a member whose teaching leans on tables and scorecards may
  take style pack `data-rich` with caption look `bold-karaoke`. Write the values exactly as spelled here
  — the editor accepts only these strings.
- **Captions:** size on 1080×1920 by look (84 / 76 / 80) · ONE line at a time, 2–3 words, 80% of the
  frame width (the editor chunks the transcript itself) · case by energy level: Bold & punchy →
  UPPERCASE, others → Title Case · edge: a 3 px dark outline (bold) or a 40% shadow (calm) · base colour
  white · **karaoke highlight colour** = the accent, contrast-checked · reels = karaoke on; long-form
  YouTube = captions off, emphasis pop-ups instead. **Include a CAPTION PREVIEW STRIP on the
  one-pager:** one caption line in white with one word in the karaoke highlight, over a mid-brightness
  photo (the member's treated photo from the kit, never a stock scene).
- **Empty zones:** the exact rectangle of each empty zone in export pixels (hook 16:9 x 320 → 1600,
  y 770 → 920; emphasis 16:9 x 400 → 1520; hook/emphasis 9:16 x 140 → 940, y 160 → 340), the type size
  the editor uses in each (64 / 72), and the character budget (35 / 30 / 20).
- **CTA pack wording:** the eight asks and pills exactly as baked, both formats.
- **Placement rules:** 9:16 → everything in the top zone, captions lower-centre; 16:9 → everything in
  the lower third, name strip bottom-left.
- **Asset file names:** the canonical list, including the `icons/` and optional `animated/` folders,
  with "built / not built" against the optional pieces (9:16 name strip, end cards, animated end card,
  logo sting), and the organization's roster — every co-host's strip file and the first name it is
  registered under.
- **Never on the spec:** a production or income figure, a split, a cap, a rev-share line, a former
  brokerage.

## 7. LANGUAGE

The pieces and the spec are written in the member's brand language(s) from the Design System — the CTA
line, the role line (the regulated term where it applies — Québec: "courtier immobilier"), and the
caption spec all match, with accents rendering cleanly in the chosen faces. Bilingual brands get a
second complete set of every piece with baked words — name strip(s), the primary CTA banner, all eight
CTA-pack variants (pill text too: "Lien dans la description" / "Lien dans la bio"), end card, and end
screen — in the second language; the hook banner, emphasis pop-up, and icons carry no words and are
shared. Because the editor registers files by their EXACT canonical names, do NOT suffix file names:
export the primary-language set into `02 · Brand/Video Brand Kit/` and the second-language set, under
the SAME canonical names, into a sibling folder `02 · Brand/Video Brand Kit — FR/` (or `— ES`). Tell
the member the editor uses one language set at a time: to edit in the other language they say
"register my video brand kit from the FR folder" in Cowork and switch back the same way.

## 8. YOUR ORGANIZATION — solo, co-leaders, or co-hosts (design for how they actually work)

A leader's videos are not always solo: two co-leaders may front the organization together, and agents
in the member's organization co-host the weekly call, an interview, or a training. The brand STRUCTURE
lives in the Design System (the brand shape, the organization's name, the member's name) and the Book
(the co-leader, the people in the organization). Apply it in this skill wherever "the member" appears:

- **Solo** *(default)* — everything as written.
- **Co-leaders (equal billing — the Book says two people co-lead)** — on this kit, both names on the
  name strip's two lines when they front videos together ("Ana & Luis Reyes" / "Team leaders · The
  Reyes Collective · [Brokerage where required]"), and two small matched circle crops at the left end
  of the strip and the CTA banner, each no taller than the strip — never cut-outs, never a photo that
  breaks the band. Never favour one unless they say so.
- **Co-hosts from the organization** — the MEMBER's brand leads; the member fronts the hero placements;
  a co-host appears on their own strip for the videos they front or co-host.
- **Per-partner name strips** — the name strip ships one per person on the SAME template. The canonical
  `lower-third-16x9.png` (and the optional `-9x16`) ALWAYS exists and is the strip of the member (for
  equal co-leaders, ask once who fronts most videos); every co-host gets
  `lower-third-16x9-[firstname].png` (lowercase, no accents): their name on line 1, their role line as
  THEY state it on line 2 ("Partner · The Lakeline Collective", "Agent · [organization]") with the
  brokerage where the display rule requires it — never a production figure, never a former brokerage.
  The editor registers the canonical strip automatically and finds the extras by first name for
  interviews and co-hosted videos; the spec's roster lists every strip. The primary CTA banner and the
  CTA pack are the MEMBER's — one set with the member's keyword, guide, link, and @handle, in the
  member's "I" voice (the organization's own pieces may say "we"). A co-host who runs their own channel
  with their own handle gets a separate complete kit of their own (their own Brand HQ, their own
  canonical names) — never two people's handles in one kit. Ask which co-hosts; default to the names the
  member gives in intake.
- **Per-partner COLOURWAYS (the premium organization pattern):** on personal pieces, each co-leader may
  carry their own signature ground colour from the brand's palette — one on the deep green, the other
  on the deep plum — while the mark, type, layouts, and devices stay IDENTICAL, so every piece reads
  "same brand, their colour." Offer it when the palette has the range; never invent off-palette colours
  to make it work.
- **Who fronts THIS piece?** — an interview or a co-hosted training is fronted by whoever speaks; if the
  Book doesn't say, ask — one question, never assume.
- **Compliance** — team and organization advertising is regulated in many markets (the registered team
  name paired with the brokerage, brokerage prominence, each person's licence where required). Pull the
  rules from the Book's Compliance chapter; unset → the three-state rule in the SKILL file.
- **Missing co-host headshots** — on this kit the LOGO MARK takes that person's circle (no labelled
  placeholder — the strip ships on video); tell the member which strip to re-export once the photo
  exists, and that a co-host's photo goes on a strip only with their OK. Never generate a face, never a
  stock face, never substitute another person's photo.
