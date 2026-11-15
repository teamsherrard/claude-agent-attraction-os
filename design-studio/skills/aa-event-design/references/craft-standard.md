# The Craft Standard — how every Agent Attraction design piece gets made

*Shared, word for word, by all ten `aa-…-design` skills. Read it FIRST — before any other reference and
before you build. Each skill's own references give a piece its specifics (sizes, sections, file names);
this file is the floor under all of them. Where a piece's own reference gives a number, that number wins.
Everything here is for you. None of this vocabulary is ever said to the member.*

## 0. The order of work (never skipped, never reordered)

1. **Read** everything yourself (§1). No form, no questions.
2. **Plan** the piece in six private lines (§2).
3. **Build the smallest real thing first** — the master, at its exact size, with the real words.
4. **Look** at the actual render, name what is wrong, fix it, look again (§8).
5. **Score** it against the gate (§10). Below the bar it is rebuilt, never shown.
6. **Roll** the rest of the set from the master, running 4 and 5 on every render.
7. **Present** finished work, in plain words, with your recommendation (§11).

A piece that skipped step 4 is a draft, however good its code looks.

## 1. Told, not asked — how every skill opens (the owner's rule, binding)

The member is a busy real estate leader, often 60 to 75, who is following a program. They do not want to
be interviewed by a design tool, and a form field cuts a pasted brief off after a few hundred characters.

- **Your first reply is never a form, a question card, a multiple choice, a list of upload slots or a
  "decide for me" menu.** It is one line, then work.
- **Read first.** The project's attached files, this conversation, and in Cowork the member's Brain and
  workspace. The brief, the kit, the guide, the Design System, the logo and the photos are almost always
  already there.
- **Open with ONE line** that says what you found and what you are building, then build in the same reply:
  *"I have your brief, your kit and your logo. I'm building your banner and your first post now."*
- **A missing optional thing gets the default, not a question.** Say it in the same line only when it
  changes what they will see: *"No photos here yet, so I'm building on your brand colours — drop photos
  into the chat any time and I'll work them in."* Platforms: all of them. Pieces: the whole set. Mode:
  the full build. Language: the Book's. How bold: the brief's energy number. Finish: the locked look's.
- **Ask only two kinds of thing, in plain chat, one line:** a required file that is truly nowhere (name
  the Cowork phrase that makes it), or a fact only the member holds that is printed on the piece and
  cannot be defaulted (an event's date; which spelling of a name when two files disagree).
- **A real choice the member owns is shown as finished work, with your pick first:** *"Three directions.
  I'd choose the second — it stays readable at profile size. **Your turn**: which one, or which parts of
  which?"* Never ask them to choose before there is something to look at.
- **An unclear request takes the default piece, never a menu.** "Design my thing" builds the skill's main piece
  (the one its first trigger phrase names) and says so in the opening line; the member redirects in a word.
- **After they have seen real work, they change anything by saying so.** That is where "bolder", "a
  different colour" and "not that photo" belong — never in an intake.

## 2. The plan before the pixels (six lines, private, every piece)

1. **The job** — what this piece must make ONE agent believe or do. One sentence. If you need "and", it
   is two pieces.
2. **The viewer and the moment** — who is looking, where, how big it is on their screen, for how long (a
   feed post: an agent mid-scroll, about 400px wide, under two seconds).
3. **The reading order** — what is read first, second, third. Nothing else competes; everything else is
   quiet or gone.
4. **What makes it theirs** — the real detail no other leader has: their method's name, the line they
   actually say, their number, their motif. A piece that works with another name swapped in is not done.
5. **The look** — the locked look's ground, its type pairing, and at most two of its devices.
6. **The grid** — columns, margins, where the eye enters and where it leaves (on the action).

## 3. Type — where most pieces are won or lost

- **Two families at most** (a heading face and a text face), plus the look's script or hand accent for
  one short line when the look names one. Three weights at most on a piece.
- **The fonts must really load.** Use the faces the Design System records, loaded the way this canvas
  loads web fonts, each with a fallback of the same shape (a condensed face falls back to a condensed
  face, a serif to a serif). After the first render, check: a headline that came out in a default serif
  or a plain system sans means the font did not load — fix that before anything else. Exports wait until
  fonts are ready.
- **Real contrast between levels.** Neighbouring levels differ by at least 1.5× in size (120 over 36 is
  a hierarchy; 48 over 40 is mush). Three levels on a graphic — the hero, the support, the label — and
  fine print as the only fourth.
- **Big type is set tight; small caps are set open.** Display lines: line height 0.92–1.05, tracking 0
  to −0.025em (tighter as it grows; heavy condensed caps stay near 0). Caps labels and eyebrows: tracking
  +0.08 to +0.14em, weight 600 or more. Script and mixed-case serif names are never letter-spaced wide.
- **Support and body:** line height 1.35–1.5; 30–60 characters a line on a graphic, 55–75 in a document
  or a page; left-aligned unless the whole piece is a short centred statement (three lines or fewer);
  never justified.
- **Line breaks are designed.** Break a headline by sense, never mid-phrase, never leaving one word alone
  on the last line. Balance the lines (`text-wrap: balance` on headlines, `pretty` on body) and place the
  breaks yourself where a display line matters. Keep short words with their neighbour (a non-breaking
  space in "with me", in a name, before a final short word).
- **Real punctuation.** Curly quotes and apostrophes, an en dash in a range, × for "by", the regulated
  marks where they apply. No double spaces, no straight quotes, no ALL-CAPS sentences, no full stop on a
  headline, no exclamation marks the kit did not write.
- **Numbers:** aligned figures in any row of numbers (`font-variant-numeric: tabular-nums`).
- **Copy-fit — the words are fixed, so the box and the size move.** The member's name and the kit's
  lines are never shortened, never squeezed (no tracking below −0.03em, no horizontal scaling), never cut
  off with dots. Fit them by choosing the size from the length of the longest line, by planning a second
  line, or by giving the line more width. Estimate before you render — line width ≈ characters × size ×
  the face's width factor (plus tracking): condensed caps 0.42–0.48 · regular sans in mixed case
  0.52–0.58 · wide geometric sans in caps 0.66–0.74 · text serif in mixed case 0.48–0.54 — then confirm
  in the render. A long name gets its own planned layout (two lines, first over last), never a smaller
  everything.

## 4. Layout — a grid, one hero, and air

- **Write the grid down first:** columns and margins, then place. Every edge sits on a column line or a
  multiple of the 8px unit. Outer margin at least 6.5% of the short side on a post (72px at 1080), at
  least 5% inside a banner's safe strip, at least 0.75in on a document page.
- **One hero.** One element is unmistakably the biggest — at least twice the visual weight of anything
  else. If two things fight, the piece has no hierarchy; make one of them small or remove it.
- **A reading path.** The eye enters at the hero (or the face), moves in one direction, and ends on the
  action. A face looks into the piece, toward the words — never off the edge.
- **Group by distance.** Space inside a group is half or less of the space between groups (16 inside,
  40 or more between). Every gap comes from one scale: 8 · 16 · 24 · 40 · 64 · 96 · 144.
- **Few alignment lines.** One alignment per text block; two, at most three, shared vertical edges on a
  piece. Almost-aligned (off by 2 to 10px) is the commonest flaw there is — snap it.
- **Air is a material.** Around a third of a graphic is ground with nothing on it. Never fill a gap with
  an ornament; move the margins or enlarge the hero instead.
- **Edges are decisions.** Nothing important inside the safe margin; anything that leaves the canvas
  leaves it boldly (15% or more of it hidden), never by a few accidental pixels. No tangents: an edge
  never just kisses another edge or the frame.
- **Correct by eye.** Centre a triangle, a round letter, a script word by how it looks, not by its box;
  a circle beside a square is drawn 3–4% larger to look equal; caps in a pill sit a hair above centre.
- **A set is one system.** Same margins, same logo position, same footer on every sibling. Put the set
  side by side: the fixed parts must not jump, and the grounds alternate (the two registers).

## 5. Colour — roles, contrast, restraint

- **Only the Design System's colours, in their roles.** The accent is the smallest amount on the piece;
  one accent hit per zone.
- **Contrast is measured, not felt.** Text against its ground: 4.5 to 1 or better; heavy type at 48px
  and up: 3 to 1 or better. The accent carries text only where it passes. A photo behind text gets a
  scrim or a plate until the text passes.
- **It must read in grey.** Squint, or look at the render without colour: the hero is still the first
  thing seen. If everything is the same mid tone, add light-dark contrast, not another colour.
- **Tints and shades come from the palette** — the brand colour mixed toward the ground
  (`color-mix(in oklch, …)`), never a new hue pulled from the air.
- **Gradients only from the look's recipe:** two stops in one family, or the look's named pair, blended
  cleanly (`in oklch`), one angle across the whole set. Never a rainbow, never a grey dead middle.
- **Foil is drawn, not named:** a metallic is a light → mid → deep → mid gradient with one narrow
  highlight, on a dark ground; on a light ground it is the flat deep tone.
- **Almost no shadows.** When one earns its place it is large, soft, low and from one light direction.
  Never a hard grey drop shadow, never a glow, never a shadow on type — type gets legibility from a
  plate or a scrim.

## 6. The photo you actually have (never fake a cut-out)

Wherever a skill says "cut-out", read it through this section.

1. **A true cut-out** — the file itself has a see-through background. Use it as the hero standing into
   the design: full head with air above, leaving the frame at the bottom edge only, a ground shape or a
   soft contact shadow behind it, its edge tone at home on the ground.
2. **A normal photo** — a headshot with a studio wall, an office or a street behind it. **This is the
   usual case.** Never fake a cut-out from it: no rough shape cut round the head, no blend trick that
   eats the hair, no odd arch that clips a shoulder. Use the honest treatment the look calls for:
   - **The framed portrait** — the photo fills the brand's frame (arch, circle, rounded rectangle) edge
     to edge, eyes about a third of the way down, with a brand rule round it or a colour block offset
     behind it.
   - **The panel** — the photo runs full height down one side (35–45% of the width); its inner edge
     dissolves into the ground through a gradient mask, and the whole photo wears the brand wash (a
     duotone, or darkened toward the ground) so the room behind the member becomes texture.
   - **The window** — the photo sits in one of the look's own devices (the taped print, a tilted card).
   Then say once, plainly, and carry on: *"For the look where you stand right in the design, I need your
   photo with the background removed. On an iPhone: open the photo, press and hold on yourself, tap
   Share, then Save Image. Drop that file here and I'll swap it in."* Never block on it; never repeat it.
3. **No photo** — the piece is complete on type and the look's devices. It is designed to be finished,
   never a layout with a hole in it. A photo window appears only on a template the member fills later.

- A background-removal tool in this session? Use it, then inspect the hair and shoulder edge at double
  size. A chewed or haloed edge is worse than a frame — fall back to the framed portrait.
- **The quality floor:** a photo smaller than about 600px on its short side, soft, or cropped out of a
  group shot is used small (a quarter of the piece or less) or not at all. Say so once.
- **Faces:** eyes in the top third; the top of the head never cropped on a hero; never stretched (fill
  the frame by cropping, with the face held in view); never flipped when there is lettering in the shot;
  skin stays natural or takes the look's warm or dark wash — never a green or blue face.
- Never a generated face, a stock person, or an invented crowd, office or event.

## 7. Build it so it cannot break

- **Exact artboards.** One element per piece at its true pixel size, clipped to its own edges; scale it
  for viewing with a wrapper, never by resizing the piece.
- **Lay out with grid and flex and gaps.** Absolute positioning only for deliberate overlaps and for
  decoration. Text never sits in a box of fixed height that its words can outgrow.
- **Long strings are planned:** a link, a handle or an email gets its own line and its own size, is
  never broken mid-word, and a web address is shown without `https://` or `www.`.
- **Images:** a set size, cropped to fill, with the focal point named (a face held near the top). A
  missing image leaves a designed ground, never a broken-picture icon.
- **Vector for everything drawn:** marks, icons, devices, textures. Icons from ONE drawn family — one
  stroke weight, one corner style. Never an emoji as an icon or a bullet. Never two icon styles.
- **Textures are real artwork** — a drawn pattern, grain, contour lines, a brushed stroke — at visible
  strength. A flat colour is not a texture.
- **One radius, one or two rule weights, one shadow recipe** for the whole set (the Design System's).
- Everything an export needs is inside the piece; the export waits for fonts and pictures.

## 8. The look loop — you cannot judge a design from its code

1. **Render it and look at the real picture** — a screenshot or a preview of the canvas at full size,
   then at the size an agent will meet it: a post about 400px wide, a banner as the thin strip it is, a
   profile picture at 40px, a page on a phone.
2. **Name what is wrong, in this order.** Stop at the first class that fails, fix it, render, look again.
   - **Broken** — text clipped or spilling out of its box or off the canvas · things overlapping that
     should not · a font that fell back · a picture that did not load · a cropped head · a stray scroll
     bar · leftover placeholder words or a bracket.
   - **Wrong words** — a misspelling (check the member's name letter by letter against the brief) · a
     line that is not the kit's, word for word · a wrong link or handle · a missing compliance line.
   - **Weak order** — you cannot tell within a second what to read first · two things the same size ·
     the action hard to find.
   - **Loose** — uneven margins · almost-aligned edges · mixed gaps, radii or rule weights · one word
     alone on a line · cramped lines · tone-on-tone text · a tangent · a dead empty zone · a crowded one.
   - **Generic** — nothing on it that could only be this member's.
3. **Fix it in the build, render again, look again.** Two full passes at least on a master; one on every
   piece after it. A flaw you saw and left is a flaw you shipped.
4. **No way to see the render on this canvas?** Then measure instead, every time: each line's estimated
   width against its box (§3), lines × line height against the height, every box's right and bottom edge
   against the canvas less the margin, each text colour's contrast against its ground — and where scripts
   run, test the page itself for any element wider than its box or outside its artboard. This is your
   work; the member never hears about it.

## 9. The tells of machine-made design (kill on sight)

- Everything centred; everything in a rounded card with a soft shadow.
- A purple-to-blue gradient nobody chose; glass panels; glow; neon on black by default.
- Emoji as icons or bullets; sparkles, rockets, walls of tick marks.
- Three equal boxes with an icon each, on a personal brand.
- Placeholder words, a visible bracket, "Your Name Here", "Tagline".
- Every Word In Title Case; six type sizes; four fonts; thin grey text on colour.
- Blobs, dots and swooshes in the corners; "abstract tech" lines; decoration with no job.
- Invented proof: star ratings, badges, "as seen in" logos, countdown clocks, review avatars.
- The same padding and the same radius on every element — no rhythm, no hierarchy.
- A drawn or generated person, hand, handshake, lightbulb, target or rocket.
- A stretched logo or photo; a logo sitting in a white box on a coloured ground.
- A hero-sized headline that says nothing only this member could say.

## 10. The gate — score it before the member ever sees it

Score every master and every piece you present, 1 to 5, on five lines. **Each line is a 4 or a 5, or the
piece is rebuilt.** Score honestly: a first render is rarely above a 3, and a 5 is rare.

1. **The job** — a stranger agent gets the one message and the one action in three seconds, at real size.
2. **The order** — first, second and third read are unmistakable.
3. **The finish** — nothing broken; margins and alignment exact; type set the way a typesetter sets it.
4. **This member** — the name right, the words verbatim, a detail no other leader has; the locked look
   applied; nothing from the avoid list.
5. **Worth paying for** — a studio would charge for it, and the member would post it today, proudly.

The scores are yours. Never show or mention them.

## 11. What the member hears

- **Finished work, not process.** One line on what they are looking at, one line of thinking per piece
  in their own terms (*"the gold line is your Sunday-table idea"*), your pick when there is a choice,
  then **"Your turn."**
- Plain words: "colours", "fonts", "your photo", "the look". No design vocabulary, no list of what you
  checked, no scores, no "I noticed an issue and fixed it", no apology for an earlier version.
- **A change they ask for is made, looked at (§8) and shown** — on every piece it touches, not just one.
- Never "want me to continue?", never "should I also…?". The program says what gets built; build it.
