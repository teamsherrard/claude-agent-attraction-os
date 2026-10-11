# Output Standard — saving the magnet, the funnel, and everything built for them: organized + well formatted

Every document this plugin makes lands in the member's cloud workspace (Google Drive **or** OneDrive — the
same place their Brain lives), in the right folder, named consistently, and formatted so it looks genuinely
good. When a skill says "save to the workspace (output standard)," it means this.

Two non-negotiables: **(1) a magnet and everything built for it live together in one campaign folder; (2) each
doc is clean and scannable — never a wall of text.**

---

## 1. Where it goes — the workspace folder structure

Campaign docs live in the member's workspace under **`03 · Content/Guides/`** (the Brain's drive map assigns
lead magnets and guides there) — one dated campaign folder per magnet, so a magnet and the page, brief, kit,
and sequence that serve it always sit together:

```
[Workspace]/                                   (located by ID — see §3)
├── 02 · Brand/
│     ├── 📍 [Name]'s Google Business Profile Kit — 2026-12-16.docx     (lm-gbp)
│     └── 🪪 [Name]'s Platform Profiles — 2026-12-16.docx              (lm-profiles)
├── 03 · Content/
│   └── Guides/
│       ├── 2026-12-16 · The Five-Step Sunday Routine/     (one campaign — created when the magnet is built)
│       │     ├── Lead Magnet — The Five-Step Sunday Routine.docx           (lm-magnet, built first)
│       │     ├── Opt-In Funnel — The Five-Step Sunday Routine.docx         (lm-funnel, built second)
│       │     ├── Design Brief — The Five-Step Sunday Routine.docx          (lm-design)
│       │     ├── Delivery Kit — The Five-Step Sunday Routine.docx          (lm-delivery)
│       │     ├── Nurture Sequence — The Five-Step Sunday Routine.docx      (lm-nurture)
│       │     └── Lead Magnet Report — The Five-Step Sunday Routine — 2027-01-13.docx   (lm-analytics)
│       ├── Weekly Newsletter — 2026-12-18.docx                 (lm-nurture — standing, dated)
│       └── List Growth Report — 2027-01-13.docx                (lm-analytics — standing, dated)
└── 04 · Agents/
    └── Prospects/
          └── Partner Outreach Kit — 2026-12-17.docx            (lm-partnerships)
```

A "campaign" = one magnet (the one the member picked from `lm-magnet-ideas`' three recommendations, built
from their own offer — the example below is the demo member's) + the funnel and kits that serve it. Build several over time — each gets its own dated folder.
Find-or-create; never duplicate a folder. No `Listings`, no `Market` — this OS has nothing to do with either.

## 2. Naming convention (use everywhere — no exceptions)

| Thing | Pattern | Example |
|---|---|---|
| Campaign folder | `YYYY-MM-DD · [Guide Name]` | `2026-12-16 · The Five-Step Sunday Routine` |
| Lead magnet doc | `Lead Magnet — [Guide Name]` | `Lead Magnet — The Five-Step Sunday Routine` |
| Funnel doc (the member hears "your sales funnel outline") | `Opt-In Funnel — [Guide Name]` | `Opt-In Funnel — The Five-Step Sunday Routine` |
| Design brief | `Design Brief — [Guide Name]` | |
| Delivery kit | `Delivery Kit — [Guide Name]` | |
| Nurture sequence | `Nurture Sequence — [Guide Name]` | |
| Per-magnet report | `Lead Magnet Report — [Guide Name] — YYYY-MM-DD` | |
| Newsletter | `Weekly Newsletter — YYYY-MM-DD` | |
| List report | `List Growth Report — YYYY-MM-DD` | |
| Partner kit | `Partner Outreach Kit — YYYY-MM-DD` | |
| GBP kit · Profiles | `📍 [Name]'s Google Business Profile Kit — YYYY-MM-DD` · `🪪 [Name]'s Platform Profiles — YYYY-MM-DD` | |

Guide Name = the magnet's name, 2–6 plain words (Title Case) — a checklist or a plan is still named this way,
and the Design Studio keys on these exact doc-name prefixes (`Lead Magnet — ` · `Opt-In Funnel — ` · `Design
Brief — `), so they never change. The date is the build date (ISO, so folders sort on their own).
Every doc in a campaign shares the same Guide Name so the set is unmistakable. Regenerated standing docs carry
a new date; **the newest date is the current one** (the connector cannot overwrite). After a verified upload,
the superseded older copy of a standing doc may be trashed; campaign docs are never trashed. A demo build
(a fictional member, explicitly framed) appends ` — DEMO` to the folder and every doc name and saves only into
the demo workspace — never into a real member's Guides folder.

## 3. How to create folders + docs (the member's storage connector)
- **Which connector:** read `Storage provider` from `~/attraction-brain/config.md` — `google` → the Google Drive
  connector; `microsoft` → the Microsoft 365 / OneDrive connector. If it says `READ-ONLY (org-gated)`, don't
  attempt the save — deliver in chat and say once, plainly, that their admin needs to enable write access.
- **Locate the workspace the way attraction-brain-sync does:** `config.md → Workspace ID` when present (IDs
  survive renames — always locate by ID, never by name), else the sync skill's locate ladder (the
  `_attraction-workspace.md` marker). Then find-or-create `03 · Content` → `Guides` → the campaign folder.
- **Folder (Google):** `create_file` with `mimeType: application/vnd.google-apps.folder` and the right
  `parentId`; capture the returned `id` to use as the parent for what goes inside it. (Microsoft: the
  connector's create-folder call under the same path.)
- **Document:** write the structured text to a temp file, then render it to a styled `.docx` and upload that:
  `python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/doc.txt "[Doc Name].docx" --title "[Title]" --subtitle "[Name · Brokerage · City]" --eyebrow "Agent Attraction Lead Magnet"`,
  then upload the resulting **`.docx`** into the right folder. The structured text is only the renderer's
  input; the deliverable is the `.docx` — **never upload the raw text.**
- **Find-or-create:** before creating any folder, list the parent and reuse it if it already exists. Every
  campaign doc saves into the **same campaign folder** the magnet created.

## 4. Formatting — the renderer makes it a clean, formatted `.docx`

The skill writes the **structured text** below; the shared renderer (`render_doc.py`) turns it into a clean,
formatted Word doc — real headings, bullet lists, tables, light-grey rules — in **one neutral house style**
(Arial, pure-black text, no colour, no per-client branding). *(If the script prints `RENDERER-UNAVAILABLE` —
`python-docx` is not installed — do exactly what it says: **install nothing, never run pip, never retry the
command**; save the same structured text as a `.md` FILE, upload THAT to the same folder, and tell the member
in one plain line that the styled version needs the renderer. That is the whole fallback chain: render → `.md`
upload + the note → done. No second renderer, no retry loop. A plain-text wall pasted into chat is still not an
acceptable output at any step.)* Write the structured text like this:
- **Title line**, a light **meta line** (name · brokerage · city · date), then **a one-line PURPOSE line** so
  the member instantly knows what this is and what to do with it — e.g. *"Your page copy + structure, ready
  for your design step. This doc is the words; the page is built separately."* Then a blank line.
- **Section headers in ALL CAPS**, each wrapped by a divider rule (`────────────────────────────────────────────`).
  The appendix headings keep a `════════════════════════════════════════════` rule by convention (the renderer
  styles both the same way). *(The renderer turns the ALL-CAPS bands into real headings.)*
- **Never write a line of copy in capitals** — not a title, not a pull quote, not the text after a label. The
  renderer makes a heading out of any line that is mostly capitals, so capitals belong to the band headings
  only. Emphasis is the design step's job.
- **Keep the deliverable clean; push the hand-off + compliance to the END as a clearly-labelled appendix**
  (`▸ NEXT — HAND TO YOUR DESIGN STEP` and `▸ COMPLIANCE`). The reader goes top-to-bottom without tripping over
  instructions. Only the `lm-design` brief contains design direction; every other doc just names the assets.
- **Generous blank-line spacing**; **bullets** with `•`, one idea per line; dates and counts as digits.
- Label each piece (`Headline:`, `Subhead:`, `CTA button:`, `Subject:`) on its own line — the renderer bolds
  an inline label. The design-cue labels in §5 ("The labels") use the same form; a **list label** (`Checklist:`,
  `Script:`, `FAQ:` …) stands alone on its line and prints in the `.docx` as a plain short line with its items
  as bullets beneath it — that is correct: the `.docx` is the member's record, and the design step is where a
  label becomes a page element and never prints as a label.
- **Build + verify, every document:** read the finished `.docx` text back — no raw `<w:` markup, no literal
  `────` lines as body text, every band a heading, and **full depth** (a guide renders its complete content,
  never a summary).

## 5. The document skeletons

**Read the skeletons right:** `...` is where your copy goes. Any note in parentheses that names a Brain file,
says "only if / else delete / skip," or gives a count or a quality reminder is guidance for YOU — it is never
written into the doc. Band headings (the ALL-CAPS line after a rule) carry only the words shown. A section
marked conditional is either fully written or entirely absent — never a placeholder line. **No `[` bracket
token ever appears in a deliverable.** The word floors and the quality gates for the two campaign docs live in
their writers (`lm-magnet` and `lm-funnel`); the skeletons here are the grammar the Design Studio reads.

### The labels (the design cues — shared by the magnet doc and the funnel doc)

A label is a line that starts with the label's exact words and a colon. The Design Studio's `aa-lead-magnet-design`
and `aa-funnel-design` recognise each one and turn it into the matching page element; **a label never prints
as a label** — the text after it is the copy, verbatim. Two forms, and every label is one or the other:
- **Inline** — `Label: the text` on one line.
- **List** — `Label:` alone on its line, then one `•` line per item directly beneath it, until a blank line or
  the next label. A fill-in blank inside an item is written as `____` (four underscores).

Every label is optional unless a skeleton says otherwise; a label with nothing true to say is **omitted**, never
left empty or placeholdered. The text after `Image idea:`, `Video:` (when it says to record) and `Booking embed:`
is direction for the designer or an asset, not copy — it never appears on the designed page; everything else
after a label is copy.

| Label | Form | What the writer puts there | What the design step makes of it |
|---|---|---|---|
| `Title:` | inline | the guide's title — the promise in the reader's words | the cover's title, the single largest element |
| `Subtitle:` | inline | who it is for (by stage) and the result | the cover's subtitle |
| `Byline:` | inline | the member's name line, the brokerage as compliance requires | the cover's byline |
| `Hook:` | list (≤ 3) | the three lines that earn the read | the cover's hook, set as three short lines |
| `How to use this:` | list (2) | the two lines that end the opening page | the opening page's closing strip |
| `Pull quote:` | inline | one line worth setting large | set large on the page |
| `Callout:` | inline | a one-sentence aside | a callout panel |
| `Checklist:` | list (3–7) | one item per line | real boxes, one per item |
| `Template rows:` | list | the fill-in rows; `____` marks a blank | fill-in lines a reader can write on |
| `Script:` | list | the word-for-word lines, one per line; two voices as `Me: …` / `Agent: …` | message bubbles or a script card |
| `Source:` | inline | the citation for a number on the page | a footnote line, small but legible |
| `Image idea:` | inline | one plain line describing the page's visual | the page's illustration or mockup direction |
| `Next step:` | inline | the page's one action | the page's closing strip |
| `Call to action:` | inline | one of the guide's three calls to action (the closing page's carries the booking link) | a quiet strip on the two earlier pages; the ONE button on the closing page |
| `Proof:` | list | real, consented results, one per line — or one plain line that there is none yet | a proof row on the page |
| `Pre-headline:` | inline | one attention line above the hero headline — a question or a fact aimed at the type of agent, never a scarcity claim | the small line above the headline |
| `Headline:` | inline | the section's headline (the hero's is the page's promise) | the section's headline |
| `Subhead:` | inline | the hero's supporting line | the hero's subhead |
| `Video:` | inline | the URL of the member's video — the 2-to-3-minute video sales letter when they have one, else the 60-second why-join-me — or exactly `record the 60-second why-join-me` | a responsive embed; with the record note, the cut-out headshot in its place |
| `Attraction line:` | inline | one bold sentence under the video that tells them why to press play | the bold line under the embed (or the headshot) |
| `CTA button:` | inline | the button's words in quotes | the button |
| `Trust line:` | inline | one line under the hero button | the small line under the button |
| `Bullets:` | list | one line per item | the section's list or cards |
| `Why partner title:` · `Why partner:` | inline · list (6–8) | "Why partner with [first name]" and the short credibility bullets under it | a credibility block beside the headshot |
| `Sneak peek title:` · `Sneak peek:` | inline · list (6–8) | "A sneak peek inside [the program name]" and one sentence per thing an agent gets | the program's peek-inside block (cards or a list) |
| `How it works:` | list (3) | the three steps to join, in plain words | three numbered steps inside the Book-a-call area |
| `What we'll cover:` | list (5–6) | what the call covers, in the member's voice | the list beside the booking embed, repeated under the thank-you page's call line |
| `Booking embed:` | inline | the booking link | the embedded calendar when the link embeds, else a button to it |
| `YouTube:` | list (2–3) | `URL — one line` per video, only when the member's channel exists | two or three video embeds with their lines; omitted entirely when absent |
| `Optional qualifier:` | inline | `off`, or the one extra pop-up field switched on: `years licensed` or `where are you today: new · 1 to 3 years · 3 plus` | the extra field in the pop-up and the static form, only when switched on |
| `FAQ:` | list | `question — answer` pairs, one per line | an accordion or stacked pairs |
| `Contact:` · `Socials:` · `Last updated:` · `Compliance:` | inline | the back page / footer lines | the back page or the footer |

The section-specific inline labels the skeletons name (`The pain, named:`, `What I do:`, `Where I was:`,
`Program:`, `Statement:`, `What the call is:` …) follow the same rule: bold lead-in in the `.docx`, never printed
as a label on the page.

**Lead Magnet doc** — the guide content (the designed PDF is built separately at the design step). The
architecture is the same for every shape; the floors are in `lm-magnet`:
```
LEAD MAGNET — [GUIDE NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Last updated [Month YYYY] — (when the magnet states facts that can change — brokerage plans, platform rules, tools) verify anything current with the source itself.
Your lead magnet content, ready for your design step. This doc is the words; the PDF is built separately.

────────────────────────────────────────────
THE PROMISE
Title: ...            (the promise in the reader's words, 7 words or fewer — it becomes the funnel's headline; never the member's jargon)
Subtitle: ...         (who it is for, by stage — never a protected characteristic — and the result; one line)
Byline: ...           (the member's name, the brokerage as compliance.md requires it)
Hook:
   •  ...             (three lines at most — specific and lived, from the member's own experience or consented proof; never "in this guide you will learn")
   •  ...
   •  ...

────────────────────────────────────────────
THE GUIDE   (page by page)
── PAGE 1 - [THE OPENING TITLE] ──
   ...the opening: why this exists, in the member's voice — the moment they were where the reader is, what they tried, what changed, what the reader will have by the last page; one real proof line only if proof.md holds a consented one...
   Pull quote: ...                    (optional)
   Image idea: ...                    (optional)
   How to use this:
      •  ...                          (always — the last thing on the page, two lines)
      •  ...
── PAGE 2 - [TITLE] ──
   ...one idea in a sentence · the how · a real example from the member's own routine...
   Script:  /  Template rows:  /  Checklist:     (the how, whenever it is one of these — items as • lines beneath)
   Callout: ...                       (optional)
   Source: ...                        (whenever a number appears on the page)
   Pull quote: ...                    (optional)
   Image idea: ...                    (optional)
   Next step: ...                     (the one thing the reader does today)
   Call to action: ...                (ONE body page only — the page that most needs a walkthrough; no link)
── PAGE 3 - [TITLE] ──
   ...
(4–8 body pages in all — PAGE 2 up to PAGE 9 — in the picked shape's order from the magnet writer's reference. Every body page carries at least one of: a number with its Source, a Script, Template rows, a Checklist, or a true story. Keep each page-title line in that exact `── PAGE N - TITLE ──` form — a short title of plain words with the hyphen separator (`?`, `:` and `&` are fine) and keep the text between the dashes under 70 characters — any longer and the renderer prints the dashes literally as body text instead of making a subheading. Every fact that isn't the member's own experience carries its source: "(my brokerage's [document], [Month YYYY])" · "(per Mike Sherrard's lesson)" · "([source], [Month YYYY])".)
── PAGE N - WHAT TO DO NEXT ──
   ...the whole system, then the first step this week...
   Checklist:
      •  ...                          (exactly five lines — the whole system the reader can screenshot)
      •  ...
      •  ...
      •  ...
      •  ...
   Next step: ...                     (the first step this week)
   Call to action: ...                (the second of three; no link — "the link's on the last page")

────────────────────────────────────────────
HOW [FIRST NAME] HELPS NEXT
   ...a soft, no-pressure close in the member's voice — what they actually give agents who partner with them (outcomes, never compensation), the brokerage line ("and everything [Brokerage] provides — I walk you through that on a call")...
   Proof:
      •  ...                          (one real, consented point — or omit the label)
   Call to action: ...                (the third of three — with the booking link: the ONLY booking link in the guide, which the thank-you page also carries)

────────────────────────────────────────────
THE BACK PAGE
Contact: ...                          (email · phone · website — only what profile.md / operations.md hold)
Socials: ...                          (real handles only — omit the line if none)
Last updated: ...                     (when the shape states facts that can change — else omit)
Compliance: ...                       (brokerage name and license display as compliance.md requires; the disclaimer verbatim if any)

════════════════════════════════════════════
▸ NEXT — HAND TO YOUR DESIGN STEP
This doc is the guide content. Your design step — the Lead Magnet Designer skill (aa-lead-magnet-design) in your
Claude Design workspace — turns it into the branded PDF: the promise becomes the cover, each PAGE block one
page, the close and the back page, copy verbatim; the labelled lines (pull quotes, checklists, scripts,
template rows, image ideas) become the page elements and never print as labels. Say "design brief for my
guide" and I'll write the brief it needs. Upload this doc plus your newest Agent Attraction Brain Book.
Assets to gather:  logo · headshot · any photos of you with your organization · the sheet or template the guide hands over, if you have it as a file.

════════════════════════════════════════════
▸ COMPLIANCE
Brokerage name and license display as compliance.md requires · the brokerage disclaimer verbatim, if any ·
the income disclaimer only if earnings were mentioned (they should not be).   (ONLY when compliance.md is
set or confirmed — unset blocks the whole doc; never paste a bracket token.)
```

**Opt-In Funnel doc** — the opt-in page copy, section by section, in the page's order. Eleven sections, then
the pop-up, the thank-you page, and the footer. The opt-in is the page's primary job and its button repeats
top (§1), middle (§3) and bottom (§11) with the same words; the Book-a-call area (§10) is the secondary path for
the agent who is already ready. Every section carries its own `Headline:` so the design step never has to
invent one. The floors are in `lm-funnel`:
```
OPT-IN FUNNEL — [GUIDE NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Gives away: [the magnet above]
Your sales funnel outline — the opt-in page copy + strategy, section by section, the pop-up, and the thank-you page — ready for your design step. This doc is the words; the page is built separately.

────────────────────────────────────────────
SECTION 1 — HERO
Pre-headline: ...             (one line above the headline — a question or a fact aimed at the type of agent; never a scarcity claim)
Headline: ...                 (the promise in the reader's words — the magnet's title or its promise line; passes the hook test)
Subhead: ...                  (who it is for, by stage, and the result — one or two short lines)
Video: ...                    (the URL of the member's video — the 2-to-3-minute video sales letter when they have one, else the 60-second why-join-me — or exactly: record the 60-second why-join-me)
Attraction line: ...          (one bold sentence under the video that tells them why to press play)
CTA button: "Get the Free Guide"
Trust line: ...               (one line under the button — who wrote this, that it is free and private)

────────────────────────────────────────────
SECTION 2 — THE PROBLEM
Headline: ...
The pain, named: ...          (the agent's most acute pain in their words — avatars.md "biggest problem, in their words" + the magnet's opening page)
What it costs: ...            (another year of the same; the mistake the magnet exists to prevent)
There's a better way: ...     (one line that bridges into the guide)
Pull quote: ...               (optional)

────────────────────────────────────────────
SECTION 3 — THE PRODUCT
Headline: ...
Bullets:
   •  ...                     (one line per guide page, each a real outcome — never a tease; 4–9 lines)
Why it's worth more than free: ...   (the one thing only this leader could have written)
Image idea: the guide's mockup, LEFT or RIGHT of this stack
CTA button: "Get the Free Guide"

────────────────────────────────────────────
SECTION 4 — WHO I AM
Headline: ...
What I do: ...
Who I help: ...
Credential: ...               (one real line from proof.md / profile.md — never invented; the upline's labeled as the upline's)
Why partner title: ...        ("Why partner with [first name]")
Why partner:
   •  ...                     (6–8 short credibility bullets — years · production only as proof.md allows and as what the member will SHOW · what they teach · who they have helped, consent on every agent named · never an income claim)
Image idea: the headshot

────────────────────────────────────────────
SECTION 5 — THE JOURNEY
Headline: ...
Where I was: ...              (journey.md beat 1 — the former brokerage never named)
What I tried: ...             (beat 2 — the wall)
What changed: ...             (beat 3 — what they built or decided, what it produced)
Pull quote: ...               (optional)
Image idea: ...               (optional — a real photo)

────────────────────────────────────────────
SECTION 6 — THE OFFER
Headline: ...
Program: ...                  (the program's name · its type — offer.md "## The program")
Bullets:
   •  ...                     (what an agent gets, each line an outcome — only what exists today)
The framework: ...            (one line — offer.md "## The framework" → "One line")
The first 30 days: ...        (one line)
The brokerage line: ...       ("and everything [Brokerage] provides — I walk you through that on a call")
Sneak peek title: ...         ("A sneak peek inside [the program name]")
Sneak peek:
   •  ...                     (6–8 one-sentence bullets of what an agent gets — the Partner Offer's deliverables table, each an outcome, not a feature; only what exists today or "built with my first partners")
Image idea: ...               (optional — the offer stack object when the Design Studio built one)

────────────────────────────────────────────
SECTION 7 — WHY JOIN ME
Headline: ...
Statement: ...                (the why-join-me statement — journey.md "## Why join me" when written; else from the offer's "why now")
Pull quote: ...               (optional)

────────────────────────────────────────────
SECTION 8 — PROOF
Headline: ...
Proof:
   •  ...                     (2–4 real results, consent on file — first name or initials · situation · what happened — or ONE line that says plainly there are none yet)
YouTube:
   •  ...                     (ONLY when the member's channel exists — 2–3 lines, each `URL — one line on the video`; no channel → omit the label entirely, never a placeholder)
Image idea: ...               (the proof photo strip: 8–12 real photos — the weekly call · events · agents' wins · the community — or omit the line)

────────────────────────────────────────────
SECTION 9 — THE ORGANIZATION
Headline: ...
What we do together: ...      (the recurring call, the group, the training, recognition — only what exists today)
Who's in it: ...              (by stage; the count only if proof.md states it, with the date)
Why that matters to you: ...  (not doing it alone — Mike's fifth pain)
Image idea: ...               (optional — real photos of the call, events)

────────────────────────────────────────────
SECTION 10 — BOOK A CALL
Headline: ...
What the call is: ...         (in the member's voice — length, where, what to bring; no pitch)
What it isn't: ...
Bullets:
   •  ...                     (the three questions the call answers)
How it works:
   •  ...                     (exactly three steps, plain words: grab the guide or book the call → the 20-minute call → onboarding Day 1, from the Partner Offer's Day 1 sequence)
   •  ...
   •  ...
What we'll cover:
   •  ...                     (5–6 bullets in the member's voice — your business and your week · how the training and the weekly call work · what onboarding looks like · your 90-day game plan · your questions about the model, answered on the call, never on a page)
Booking embed: ...            (the booking link)
CTA button: "Book a call with me"

────────────────────────────────────────────
SECTION 11 — THE OPT-IN
Headline: ...                 (the magnet named + its promise)
Bullets:
   •  ...                     (the top 3 you'll get — the full stack is §3)
FAQ:
   •  Is this a recruiting pitch? — ...
   •  Will anyone know I downloaded this? — ...
   •  ... — ...               (the third adapted to the magnet's reader)
CTA button: "Get the Free Guide"

THE OPT-IN POP-UP   (every opt-in button on the page opens this)
Pop-up headline: ...   (the promise in one line)
Form: First name · Email · Phone
Optional qualifier: off   (default — fewer fields win; or the ONE field the member switched on: `years licensed` · `where are you today: new · 1 to 3 years · 3 plus`)
Contact line: ...   (one honest sentence under Phone — what the member will do with it, from operations.md's follow-up cadence)
Reassurance: Free. Instant. Private — nobody's contacted on your behalf. Unsubscribe anytime.
Submit button: "Get the Free Guide"

THE THANK-YOU PAGE   (where submitting lands)
Confirmation: ...   (warm, in the member's voice)
Download button: ...   (the DIRECT LINK to the guide PDF — an INSTANT DOWNLOAD, NEVER "check your inbox")
The call, offered: ...   (one warm, optional line + the booking link — "no pitch, I'll just answer your questions"; the download never depends on it; the design step repeats §10's "What we'll cover" list under this line)
Where to find me: ...   (one soft line — social handles / website)
Footer: the same compliance stamp as the page

FOOTER
Contact: ...                  (email · phone · website — from profile.md / operations.md)
Socials: ...                  (real handles only — omit the line if none)
Compliance: ...               (the stamp, verbatim)

════════════════════════════════════════════
▸ NEXT — HAND TO YOUR DESIGN STEP
This doc is the copy + structure. Your design step — the funnel skill (aa-funnel-design, its opt-in shape) in your
Claude Design workspace — builds the page from these exact sections and takes it live on Netlify (upload this
doc, the magnet doc, and your newest Agent Attraction Brain Book); or host it yourself (your site /
GoHighLevel / Carrd). The form must be a real static Netlify form (the rule is in the funnel guide) or no
lead is ever captured — test-submit once before sending traffic.
Your video: (only when the Video line says to record) say "my why join me story" in your Brain and it writes the 60-second script; film it, upload it, and paste the link at the design step — until then the page shows your headshot in that spot. A longer 2-to-3-minute version of the same story works there too, once you have one.
Assets to gather:  the guide's mockup/cover (The Product §3) · 8–12 proof-strip photos (Proof §8) · headshot (Hero and Who I Am) ·
   the video link (Hero §1, if filmed) · 2–3 YouTube links (Proof §8, only if you have a channel) · social handles (the footer, if used) · logo (header/footer) · the finished guide PDF
   uploaded somewhere linkable (the thank-you page's download button points at it) · your booking link (Book a Call §10 and the thank-you page).   Real people + real photos only.

════════════════════════════════════════════
▸ COMPLIANCE
(same rule as the magnet doc — set or confirmed only; the page footer and the thank-you footer carry the stamp)
```

**Every other doc** (design brief, delivery kit, nurture sequence, newsletter, partner kit, GBP kit, profiles,
reports) uses the same grammar: title · meta · purpose line · CAPS bands · `Label:` lead-ins · the appendix
last. Their section lists live in each skill.

## 6. The save flow
1. Build the doc's structured text following §4–§5; write it to a temp file (e.g. `/tmp/doc.txt`).
2. Locate the workspace (§3), then find-or-create the folder §1 assigns (campaign docs: `03 · Content/Guides/`
   → `YYYY-MM-DD · [Guide Name]/`; the funnel and every kit save into the folder the magnet made).
3. **Render** the text to a styled `.docx` via `${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py` (§3), then upload
   that `.docx` with the §2 name. Read the finished `.docx` back once (§4's verify list).
4. Confirm in plain language + give the location:
   *"Saved to your workspace → Content → Guides → [campaign]. Here's the doc: [link]."*
5. **If the folder, render, or upload fails** (an error, a missing connector, a write-gated Microsoft
   workspace): say it is NOT saved, keep the copy visible, retry once. Still failing → say plainly, in one
   line — *"Your copy's all here in the chat; I couldn't save it to your workspace just now, so copy it
   somewhere safe or paste it straight into your design step."* — and **keep going** (compliance pass,
   hand-off). Never loop on retries, never upload the raw text, never treat a failed save as a failed build.
   The funnel can read the magnet from chat or from the member pasting it if the doc isn't in the workspace.

Deliver the copy in chat too — the member often takes it straight to their design step. The workspace docs
are the organized record they (and their assistant) can always find.
