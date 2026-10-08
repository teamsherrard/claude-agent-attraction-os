---
name: lm-funnel
description: >
  Step 2 of the Lead Magnet plugin — maps the opt-in page that gives the member's agent-attraction
  lead magnet away. Reads the finished magnet so the page presents exactly what the guide
  delivers, then writes the full copy section by section for an agent audience: Hero, The Problem,
  The Guide + mockup, About the leader + welcome video, Why Partner (the Partner Offer as
  outcomes, never compensation), The Organization, Proof + photo strip, Socials (only if they have
  channels), The Opt-in with a mini-FAQ — in the member's voice. One job on the page: the opt-in
  (pop-up: first name, email, phone). The thank-you page carries the instant download AND the
  book-a-call step. Hard 3-state compliance gate; the static Netlify form rule for aa-funnel-design. COPY
  + STRATEGY ONLY — never designs or hosts.
  Trigger on: "write the page for my comparison guide", "opt-in page for agents", "attraction
  funnel copy", "the page that gives away my agent lead magnet", "set up my attraction funnel"
  when a guide exists.
---

# Opt-In Funnel Mapper (Step 2 — copy + strategy only)

The opt-in page. One job: get the agent to grab the guide. Every section pushes toward that — and nothing
else on the page (house rules #4). The opt-in itself is a **two-step flow**: every CTA button opens the
**opt-in pop-up** (first name, email, phone), and submitting lands on the **thank-you page** with the guide as
an instant download **and the call, offered** underneath it.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`). The three laws and what this skill
owns: `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

> **We write the copy + strategy; we never design or host (house rules #3).** This produces the page's *words
> and structure* — the design (turning it into a built page) is the Design Studio's **`aa-funnel-design`** skill in
> its opt-in shape, and hosting is the member's own tool. Pour 100% of the effort here into making the copy
> + strategy genuinely great.

---

## Step 1 — Get the magnet first (alignment is non-negotiable — house rules #7)
This page gives away a specific lead magnet, so it must read it:
- Read `~/attraction-brain/memory/magnets.md` → the row with status `written` or `designed` and no funnel URL
  (or the one the navigator or the magnet skill named), then open its **Lead Magnet doc** in the campaign
  folder (`03 · Content/Guides/[campaign]/`, output standard §1). If several qualify and none was named, take
  the one without a funnel, else the newest. Read it — its **promise** and its **page list** drive the headline
  and the opt-in bullets, and its **type of agent and the pain on its framing page** are what the Problem
  section speaks to (house rules #7).
- **If no magnet exists yet,** this is the cold start the front door owns: say its line verbatim (*"Let's do
  it — the page's whole job is to give away your free guide, so I'll write the guide first and then the page
  basically writes itself. Same sitting, both done."*) and run `lm-navigator` Steps 0–5 (the Brain pull, the
  offer + compliance checks, the lock, the intake) — the guide gets built, then it comes back here. Never
  guess a magnet; the page and the guide must line up exactly.

## Step 2 — Load the Brain (lazy)
Read `~/attraction-brain/brain.md` first. **If `~/attraction-brain/` is missing, pull it first — never assume no
Brain** (house rules #2). Then:
- `identity/compliance.md` — **the gate, before a word** (house rules #5). `unset` → stop with the plain
  message. Note the stamp lines, the recruiting scope, and the testimonial-consent rule.
- `identity/offer.md` — the **WHY PARTNER** section: what's included (as outcomes), the unique mechanism,
  the transformation, the first 30 days as a partner (the About section's "how I work" steps). Never
  compensation.
- `identity/proof.md` — real agents helped (consent on file), organization today with its date, upline proof
  labeled as the upline's — for About (one line) and Proof (the block). Never invented.
- `identity/profile.md` — name, brokerage as compliance requires, booking link, **social handles** (drives the
  conditional Socials section — skip it entirely if there are none).
- `identity/avatars.md` — the type of agent (must match the magnet's) and their biggest problem in their
  words; the objections to expect (feeds the mini-FAQ).
- `identity/journey.md` + `identity/story-bank.md` — the mirror beat for About (former brokerage unnamed).
- `identity/positioning.md` — the one-line "why I'm here"; what stays for the private call.
- `identity/voice.md` + `identity/voice-samples.md` — write the whole page in their real voice.
- `identity/voice-print.md` — **only for the welcome-video talking beats in §4** (said on camera, so write
  those 3 beats for the ear in their spoken cadence). Empty → write the beats from `voice.md`.
- `identity/operations.md` — the follow-up cadence (for the pop-up's honest contact line), the weekly call and
  onboarding steps (The Organization section), the booking link (the thank-you page).

**Read the Brain; never re-ask (house rules #2).**

## Step 3 — Read the references (this is where the quality comes from)
- `references/funnel-guide.md` — **read "The strategy underneath" FIRST** (the one big idea, the pain + the
  fear, the 3 reasons an agent won't opt in, the emotional arc), then the section-by-section structure, then
  the **static form rule** for the appendix. The strategy is what separates an "okay" page from one that converts.
- `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md` — how to write each line so it persuades, not just informs.

---

## Phase 1 — Confirm what it's giving away (and match its reader)
In one line — a plain message, never a question box (house rules #1) — confirm the magnet this page gives
away (its name + promise), so the member sees the page and the guide are the same story. If they want a
different angle on the headline, note it — but the promise must still match what the guide delivers. **Match
the magnet's reader:** the page speaks to the same type of agent the guide was written for, in the same words.

## Phase 2 — Map the page (full copy — value-led, NOT a recruiting pitch)
Following `references/funnel-guide.md` + the copywriting KB, write the **complete copy** for each section, in
the member's voice, compliance-safe. **Lead with honesty + the leader's real experience, not hype** — the page
earns the opt-in by being the most useful, most candid thing the agent has seen from anyone at any brokerage.
**A thin page reads like a recruiting deck; a substantive one reads like a leader** — so pull the RICH stuff
from the Brain: the Partner Offer as outcomes, what the organization actually does each week, real agents
helped. The sections:

1. **HERO** — the **headline** (= the magnet's core promise), a **subhead** (expand the promise + who it's
   for, by stage + remove doubt — "written by a working agent and leader, not a recruiting department"), and
   the **CTA button** ("Get the Free Guide"). 90% of whether they stay.
2. **THE PROBLEM** — name the agent's single most acute pain in their words and agitate it honestly (the real
   cost of choosing on the wrong number, or of another switch that changes nothing), then turn the corner:
   there's a better way to decide, and this guide is it. Source: the magnet's framing page + `avatars.md`.
   Never a named brokerage, never a protected characteristic.
3. **THE GUIDE — what's inside + its value (with the mockup)** — 4–7 concrete "here's exactly what you'll get"
   bullets from the magnet's pages (real outcomes, never teases) + why it beats what they'd find elsewhere
   (honest about every model, including mine). **Note the guide mockup/cover sits left or right.** Repeat the CTA.
4. **ABOUT [FIRST NAME] — WHO they are** — **the mirror** (one journey beat → the agent's present-day version),
   **why they're qualified** (one credibility line from `proof.md`; the upline's labeled as the upline's),
   **how they work with an agent** (3 steps max — the first 30 days as a partner from `offer.md`).
   Humble-confident, human. **The WELCOME VIDEO slot — always written, always optional, no question asked.**
   Spec it structurally (*"welcome video, 30–60s, sits left/right of this section — optional; leave it out
   at the design step if there's no clip"*) and write its **talking-script outline** (3 beats, for the ear,
   in their spoken voice: who I am + who I help → what the guide gives you → grab it below, no pitch). A face
   on camera is the strongest trust element on the page; the slot simply disappears if they never film it.
   Never autoplays with sound; never a rival CTA.
5. **WHY PARTNER WITH [FIRST NAME] — the PARTNER OFFER** — straight from `offer.md`, as **outcomes**: what's
   included (each line what the agent gets, not what the member does), the unique mechanism tied to the pain,
   the transformation (framed as what the member will SHOW, never what the agent will EARN), and the
   brokerage line ("and everything [Brokerage] provides — I walk you through that on a call"). **No splits,
   caps, tiers, stock, rev share, or income** (house rules #5). Free vs paid said straight if it applies.
   The section most recruiting pages get wrong by listing features. (Distinct from §4: that's WHO, this is WHAT.)
6. **THE ORGANIZATION — what it's like inside** — the un-fakeable section. Only what exists today, from
   `offer.md` / `operations.md`: the weekly call, the group, the training, recognition; who's in it by stage;
   the count only if `proof.md` states it with a date; why that matters (not doing it alone). VALUE, not a
   pitch. (Real photos of the call, events, the community go here at the design step — note it in the assets.)
7. **PROOF / RESULTS** — a **dedicated** proof block from `proof.md` (real only, consent on file): 2–4 short
   results (first name or initials + situation + what happened), the numbers as stated with their dates,
   upline proof labeled — all tied back to the agent's pain. **Note the PROOF PHOTO STRIP here** — a
   horizontal, auto-scrolling strip of the member's real photos (the weekly call, events, agents' wins, the
   community, recognition moments). Spec it structurally — *"photo strip: 8–12 real photos, auto-scrolling"* —
   and list the **types** (the member picks the files at the design step — don't ask mid-build, don't invent a
   list). **Real photos only, theirs to use — agents' faces need the agent's OK.** Fewer than ~6 usable photos
   → skip the strip. If proof is thin or `proof.md` is still placeholders: one real result if there is one,
   otherwise honest experience only — **never invent.** The section stays; it just gets smaller.
8. **FOLLOW ALONG — socials + YouTube** — **CONDITIONAL: include ONLY if the member has channels**
   (`profile.md`). If none, **skip this section entirely** — no empty block. Real handles/links only; a
   follower count only if the member stated one; "follow for more free value." **Opt-in stays the one primary
   CTA** — no Subscribe button, no autoplaying embed.
9. **THE OPT-IN** — name the magnet + a one-line promise, a **quick recap of the top 3 "what you'll get"**, a
   **3-question mini-FAQ** right at the ask (*"Is this a recruiting pitch?"* → no, it's the guide, fair to
   every model · *"Will anyone know I downloaded this?"* → no, the list is private, nobody's contacted on your
   behalf · *"I'm not planning to move — is this for me?"* → then it's the thing to read before you ever
   decide — one honest line each, the member's voice, the third adapted to the magnet's reader), and the
   **CTA button**. Then write the two states that follow — the whole flow is **button → pop-up → thank-you
   page** (house rules #4):
   - **The OPT-IN POP-UP** — every CTA button opens this one modal: a short headline (restate the promise),
     the **form fields (`First name` · `Email` · `Phone`)**, one honest **contact line** under Phone from
     `operations.md`'s follow-up cadence (*"I'll text or call once to make sure you got it — no drip, no
     pressure."*), the **reassurance** ("Free. Instant. Private — nobody's contacted on your behalf.
     Unsubscribe anytime."), and the submit button. Pop-up micro-copy rules: copywriting KB.
   - **The THANK-YOU PAGE** — where submitting lands: a warm confirmation in the member's voice + **the direct
     link to the guide (the PDF) as a big instant-download button, first** (never "check your inbox") — then
     **the call, offered**: one warm, optional line + the booking link from `profile.md` / `operations.md`
     (*"Want to talk through where you're at? Book a call — no pitch, I'll just answer your questions."*),
     one soft "here's where to find me" line (social handles / website), and the same compliance stamp as the
     page footer. The download never depends on booking. **No "book a call" button anywhere on the opt-in
     page itself** — the thank-you page is where the call lives.

## Phase 3 — Note the assets (design is a SEPARATE skill)
This skill ends at the **copy + strategy** — that's the whole deliverable. **Do NOT write design direction;**
the Design Studio's **`aa-funnel-design`** (opt-in shape) reads this exact doc (uploaded, or via the storage
connector) and builds + deploys the page section for section, copy verbatim. Close with the output standard's
`▸ NEXT — HAND TO YOUR DESIGN STEP` appendix: the assets to gather (guide mockup/cover · 8–12 proof-strip
photos · headshot · the 30–60s welcome video if filming · social handles · logo · the finished guide PDF
uploaded somewhere linkable · the booking link) **and the static form rule** — the one line that no lead is
ever captured without a real static Netlify form in the deployed HTML, with the test-submit canary. The full
rule text is in `references/funnel-guide.md`; carry its "the rule" block into the appendix verbatim.

## Phase 4 — Compliance pass (house rules #5)
Run the full page (and the pop-up + thank-you page) through **house rules #5**: the two cardinal rules ·
no ranking · compensation off the page · no earnings talk · real proof with consent · targeting by stage ·
recruiting scope (a page that invites agents from outside `compliance.md` → scope is flagged) · the Meta
"Employment" note in the appendix if any of this will become an ad. Then the stamp as the page footer **and
the thank-you page footer**. `set` → one reminder to confirm with their brokerage. Never paste a bracket token.

## Phase 5 — Deliver + save (paired with the magnet)
1. **Deliver in chat** — all the sections of copy, cleanly laid out and ready to use.
2. **Save to the workspace** following `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`: into the **same
   campaign folder** as the magnet, save `Opt-In Funnel — [Guide Name]` (rendered to a styled `.docx` via the
   shared renderer; read it back). Confirm the location in plain words. If the save fails, the output
   standard's fallback applies — say it's not saved, retry once, the chat copy is the deliverable; keep going.
3. **Log it (silently):** in `memory/magnets.md`, note the funnel doc against the magnet's row (Campaign
   folder column already set; funnel URL stays "not live yet" until the member confirms the page is up, then
   it becomes the URL and Status → `live` and `## Current magnet` gets the URL). **attraction-brain-sync
   PUSH** (write → push → verify). This skill never writes `content-log.md`.
4. **Close the loop:** *"That's your funnel copy — every section, ready to go. Next, upload this doc, the
   magnet doc, and your newest Brain Book to the **funnel skill** in your Claude Design workspace — it builds
   the page from these exact sections and takes it live. One thing that matters: test-submit the form once
   before you send anyone to it, and tell me the live link so every other system points at it."*
5. **Point traffic at it (one line, no new work):** the free places to put the link once it's live — the
   ManyChat GUIDE keyword and the DM / email / story that deliver it (*"say 'deliver my guide' and I'll
   write them"*), their **bios** (`lm-profiles`), their **Google Business Profile** post (`lm-gbp`), and
   every video description and Reel caption (the YouTube and Short-Form systems drive the traffic; this page
   catches it).

---

## Quality checklist
- [ ] Read the actual magnet first; **page promise = magnet promise = what's delivered** (house rules #7); same type of agent
- [ ] Compliance gate passed before writing (unset blocks); recruiting scope respected
- [ ] **Strategy applied first** (one big idea · the pain + the fear · the 3 reasons an agent won't opt in, dissolved · the emotional arc)
- [ ] All sections present, in order (Hero · Problem · The Guide · About · Why Partner · The Organization · Proof · [Socials] · Opt-in · Thank-you)
- [ ] Hero headline clear, outcome-led, specific, no hype; **ONE primary CTA ("Get the Free Guide") repeats ~3×**
- [ ] PROBLEM names + agitates the agent's real pain in their words before any offer; no named brokerage
- [ ] THE GUIDE value-stacks the pages (concrete outcomes) + **notes the mockup sits left/right**
- [ ] ABOUT = WHO (the mirror, one credibility line, how I work) · WHY PARTNER = the Partner Offer as outcomes — two distinct sections; **no compensation, no earnings**
- [ ] Welcome-video slot written as optional (no question asked) + 3-beat spoken outline (voice-print.md)
- [ ] THE ORGANIZATION describes only what exists today; counts only as proof.md states them, dated
- [ ] PROOF is a dedicated block from proof.md — real only, consent on file, upline proof labeled; small and honest if thin
- [ ] SOCIALS included ONLY if the member has channels (else omitted cleanly); opt-in stays the one primary CTA
- [ ] Mini-FAQ (3 one-liners incl. the privacy line) sits in the opt-in section, in the member's voice
- [ ] Opt-in flow = button → pop-up (First name · Email · Phone + honest contact line + reassurance) → thank-you page with the instant-download link FIRST, then the call offered with the booking link; **no call button on the opt-in page**
- [ ] PROOF photo strip specified (8–12 real photos, auto-scrolling; agents' consent) — or skipped honestly
- [ ] Voice matches `voice.md` + `voice-samples.md`; fifth-grade reading level; honest where others pitch
- [ ] No design direction written (aa-funnel-design owns it); assets-to-gather + the static form rule in the appendix
- [ ] Compliance pass done per house rules #5 (the stamp on the page footer and the thank-you footer; no bracket tokens; set → one reminder)
- [ ] Saved into the same campaign folder as the magnet (or the fallback said plainly); magnets.md updated and pushed
