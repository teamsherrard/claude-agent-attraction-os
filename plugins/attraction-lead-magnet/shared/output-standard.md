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
│       ├── 2026-12-16 · Honest Brokerage Comparison Guide/     (one campaign — created when the magnet is built)
│       │     ├── Lead Magnet — Honest Brokerage Comparison Guide.docx           (lm-magnet, built first)
│       │     ├── Opt-In Funnel — Honest Brokerage Comparison Guide.docx         (lm-funnel, built second)
│       │     ├── Design Brief — Honest Brokerage Comparison Guide.docx          (lm-design)
│       │     ├── Delivery Kit — Honest Brokerage Comparison Guide.docx          (lm-delivery)
│       │     ├── Nurture Sequence — Honest Brokerage Comparison Guide.docx      (lm-nurture)
│       │     └── Lead Magnet Report — Honest Brokerage Comparison Guide — 2027-01-13.docx   (lm-analytics)
│       ├── Weekly Newsletter — 2026-12-18.docx                 (lm-nurture — standing, dated)
│       └── List Growth Report — 2027-01-13.docx                (lm-analytics — standing, dated)
└── 04 · Agents/
    └── Prospects/
          └── Partner Outreach Kit — 2026-12-17.docx            (lm-partnerships)
```

A "campaign" = one magnet (the Honest Brokerage Comparison Guide first; whatever `lm-magnet-ideas` picks
after) + the funnel and kits that serve it. Build several over time — each gets its own dated folder.
Find-or-create; never duplicate a folder. No `Listings`, no `Market` — this OS has nothing to do with either.

## 2. Naming convention (use everywhere — no exceptions)

| Thing | Pattern | Example |
|---|---|---|
| Campaign folder | `YYYY-MM-DD · [Guide Name]` | `2026-12-16 · Honest Brokerage Comparison Guide` |
| Lead magnet doc | `Lead Magnet — [Guide Name]` | `Lead Magnet — Honest Brokerage Comparison Guide` |
| Funnel doc | `Opt-In Funnel — [Guide Name]` | `Opt-In Funnel — Honest Brokerage Comparison Guide` |
| Design brief | `Design Brief — [Guide Name]` | |
| Delivery kit | `Delivery Kit — [Guide Name]` | |
| Nurture sequence | `Nurture Sequence — [Guide Name]` | |
| Per-magnet report | `Lead Magnet Report — [Guide Name] — YYYY-MM-DD` | |
| Newsletter | `Weekly Newsletter — YYYY-MM-DD` | |
| List report | `List Growth Report — YYYY-MM-DD` | |
| Partner kit | `Partner Outreach Kit — YYYY-MM-DD` | |
| GBP kit · Profiles | `📍 [Name]'s Google Business Profile Kit — YYYY-MM-DD` · `🪪 [Name]'s Platform Profiles — YYYY-MM-DD` | |

Guide Name = 2–6 plain words (Title Case). The date is the build date (ISO, so folders sort on their own).
Every doc in a campaign shares the same Guide Name so the set is unmistakable. Regenerated standing docs carry
a new date; **the newest date is the current one** (the connector cannot overwrite). After a verified upload,
the superseded older copy of a standing doc may be trashed; campaign docs are never trashed.

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
- **Keep the deliverable clean; push the hand-off + compliance to the END as a clearly-labelled appendix**
  (`▸ NEXT — HAND TO YOUR DESIGN STEP` and `▸ COMPLIANCE`). The reader goes top-to-bottom without tripping over
  instructions. Only the `lm-design` brief contains design direction; every other doc just names the assets.
- **Generous blank-line spacing**; **bullets** with `•`, one idea per line; dates and counts as digits.
- Label each piece (`Headline:`, `Subhead:`, `CTA:`, `Subject:`) on its own line — the renderer bolds the labels.
- **Build + verify, every document:** read the finished `.docx` text back — no raw `<w:` markup, no literal
  `────` lines as body text, every band a heading, and **full depth** (a guide renders its complete content,
  never a summary).

## 5. The document skeletons

**Read the skeletons right:** `...` is where your copy goes. Any note in parentheses that names a Brain file,
says "only if / else delete / skip," or gives a count or a quality reminder is guidance for YOU — it is never
written into the doc. Band headings (the ALL-CAPS line after a rule) carry only the words shown. A section
marked conditional is either fully written or entirely absent — never a placeholder line. **No `[` bracket
token ever appears in a deliverable.**

**Lead Magnet doc** — the guide content (the designed PDF is built separately at the design step):
```
LEAD MAGNET — [GUIDE NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Last updated [Month YYYY] — brokerage plans change; verify anything current with the brokerage itself.
Your guide content, ready for your design step. This doc is the words; the PDF is built separately.

────────────────────────────────────────────
THE PROMISE
What this guide delivers, in one or two lines · who it's for (the type of agent, by stage — never a protected characteristic).

────────────────────────────────────────────
THE GUIDE   (page by page)
── PAGE 1 - [TITLE] ──
   •  ...the actual, genuinely useful content...
── PAGE 2 - [TITLE] ──
   •  ...
(5–9 body pages of real value — the comparison guide is 7, plus an optional 8th story page — never a tease.
Keep each page-title line in that exact `── PAGE N - TITLE ──` form — a short title of plain words with the
hyphen separator (`?`, `:` and `&` are fine) and keep the text between the dashes under 70 characters — any
longer and the renderer prints the dashes literally as body text instead of making a subheading. Every fact
that isn't the member's own experience carries its source: "(my brokerage's [document], [Month YYYY])" ·
"(per Mike Sherrard's lesson)" · "([source], [Month YYYY])".)

────────────────────────────────────────────
HOW [FIRST NAME] HELPS NEXT
A soft, no-pressure close in the member's voice — what they actually give agents who partner with them (outcomes, never compensation), and the one next step: book a call to talk it through. (The booking link belongs here and on the thank-you page only.)

════════════════════════════════════════════
▸ NEXT — HAND TO YOUR DESIGN STEP
This doc is the guide content. Your design step — the Lead Magnet Designer skill (ds-lead-magnet) in your
Claude Design workspace — turns it into the branded PDF, one page per PAGE block, copy verbatim. Say "design
brief for my guide" and I'll write the brief it needs. Upload this doc plus your newest Agent Attraction Brain Book.
Assets to gather:  logo · headshot · any photos of you with your organization.

════════════════════════════════════════════
▸ COMPLIANCE
Brokerage name and license display as compliance.md requires · the brokerage disclaimer verbatim, if any ·
the income disclaimer only if earnings were mentioned (they should not be).   (ONLY when compliance.md is
set or confirmed — unset blocks the whole doc; never paste a bracket token.)
```

**Opt-In Funnel doc** — the opt-in page copy, section by section:
```
OPT-IN FUNNEL — [GUIDE NAME]
[Name] · [Brokerage] · [City] · [Date]   ·   Gives away: [the magnet above]
Your page copy + structure, ready for your design step. This doc is the words; the page is built separately.

────────────────────────────────────────────
SECTION 1 — HERO
Headline: ...        (= the magnet's promise)
Subhead: ...         (who it's for, by stage · why it's different · zero pitch)
CTA button: "Get the Free Guide"

────────────────────────────────────────────
SECTION 2 — THE PROBLEM
The pain, named: ...   (the agent's most acute pain in their words — avatars.md "biggest problem, in their words" + the magnet's framing page)
What it costs to get wrong: ...   (the wrong brokerage for the wrong reasons; another year of the same)
There's a better way: ...   (one line that bridges into the guide)

────────────────────────────────────────────
SECTION 3 — THE GUIDE  (what's inside + value · mockup left or right)
[ guide mockup / cover sits LEFT or RIGHT of this stack ]
What you'll get:
   •  ...   (4–7 concrete outcomes, one per guide page — never teases)
Why it's worth more than free: ...   (honest about every model, including mine — the thing no recruiting deck does)
CTA button: "Get the Free Guide"   (mid-page repeat)

────────────────────────────────────────────
SECTION 4 — ABOUT [FIRST NAME]  (WHO they are — the leader)
The mirror: ...   (one journey beat → the agent's present-day version — journey.md / story-bank.md)
Why I'm qualified: ...   (one credibility line from proof.md — never invented; the upline's proof labeled as the upline's)
How I work with an agent: ...   (3 steps max — the first 30 days as a partner, from offer.md)
Welcome video: 30–60s, sits LEFT or RIGHT — optional; leave it out at the design step if there's no clip
   Talking outline (spoken voice): (1) who I am + who I help  (2) what the guide gives you  (3) "grab it below" — no pitch

────────────────────────────────────────────
SECTION 5 — WHY PARTNER WITH [FIRST NAME]  (the PARTNER OFFER — outcomes, never compensation)
What you get when you partner with me: ...   (what's included, each as an outcome — offer.md; "and everything [Brokerage] provides — I walk you through that on a call")
What I do differently: ...   (the unique mechanism, tied to the pain)
The transformation: ...   (where they are → where they could be; framed as what the member will SHOW, never what the agent will EARN)

────────────────────────────────────────────
SECTION 6 — THE ORGANIZATION  (what it's like inside)
What we do together: ...   (the recurring call, the group, the training, recognition — only what exists today, from offer.md / operations.md)
Who's in it: ...   (the kinds of agents, by stage — organization size only if proof.md states it, with the date)
Why that matters to you: ...   (not doing it alone — Mike's fifth pain)

────────────────────────────────────────────
SECTION 7 — PROOF / RESULTS
Agents I've helped: ...   (2–4, real only from proof.md, consent on file — first name or initials · situation · what happened)
The numbers: ...   (only what proof.md states — organization size, years, agents helped — with the date)
From the group above me: ...   (upline proof, labeled as the upline's — "our group has…" — only if proof.md holds it)
Proof photo strip: 8–12 real photos, auto-scrolling horizontal strip (slow) — the weekly call · events · agents' wins · the community · recognition moments. Skip it if fewer than ~6 usable photos.
Photo types for the strip: ...   (the kinds of photos to pull — the member picks the files at the design step; real, theirs to use, agent OK where faces show)

────────────────────────────────────────────
SECTION 8 — FOLLOW ALONG   (socials + YouTube)
(ONLY if they have channels — else delete this whole section.)
Channels: ...   (real handles/links from profile.md — YouTube, Instagram, TikTok, LinkedIn…)
Follow for more free value: ...   (real follower counts only if the member stated one)
(Opt-in stays the primary CTA — these are secondary trust links, not a rival button.)

────────────────────────────────────────────
SECTION 9 — THE OPT-IN   (flow: button → pop-up → thank-you page)
Top 3 you'll get: ...   (quick recap — full stack is in §3)
Mini-FAQ (3 one-liners, the member's voice):
   •  Is this a recruiting pitch?: ...
   •  Will anyone know I downloaded this?: ...
   •  I'm not planning to move — is this for me?: ...
CTA button: "Get the Free Guide"

THE OPT-IN POP-UP   (every CTA button on the page opens this)
Pop-up headline: ...   (the promise in one line)
Form: First name · Email · Phone
Contact line: ...   (one honest sentence under Phone — what the member will do with it, from operations.md's follow-up cadence)
Reassurance: Free. Instant. Private — nobody's contacted on your behalf. Unsubscribe anytime.
Submit button: "Get the Free Guide"

THE THANK-YOU PAGE   (where submitting lands)
Confirmation: ...   (warm, in the member's voice)
Download button: ...   (the DIRECT LINK to the guide PDF — an INSTANT DOWNLOAD, NEVER "check your inbox")
The call, offered: ...   (one warm, optional line + the booking link — "no pitch, I'll just answer your questions"; the download never depends on it)
Where to find me: ...   (one soft line — social handles / website)
Footer: the same compliance stamp as the page

════════════════════════════════════════════
▸ NEXT — HAND TO YOUR DESIGN STEP
This doc is the copy + structure. Your design step — the funnel skill (ds-funnel, its opt-in shape) in your
Claude Design workspace — builds the page from these exact sections and takes it live on Netlify (upload this
doc, the magnet doc, and your newest Agent Attraction Brain Book); or host it yourself (your site /
GoHighLevel / Carrd). The form must be a real static Netlify form (the rule is in the funnel guide) or no
lead is ever captured — test-submit once before sending traffic.
Assets to gather:  guide mockup/cover (The Guide §3) · 8–12 proof-strip photos (Proof §7) · headshot (About) ·
   30–60s welcome video (About §4, if filming one — outline's in the section) · social handles (§8, if used) ·
   logo (header/footer) · the finished guide PDF uploaded somewhere linkable (the thank-you page's download
   button points at it) · your booking link (the thank-you page).   Real people + real photos only.

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
