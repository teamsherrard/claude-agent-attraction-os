---
name: lm-profiles
description: >
  The Week 6 updater of the member's bios — refines every platform's bio / about section to the
  agent-attraction funnel's CTA: Instagram, Facebook, TikTok, LinkedIn, YouTube (the sections the
  Short-Form plugin's sf-setup wrote in Week 3), plus X, Threads, Google Business Profile, the
  brokerage site, and an email signature — each sized to the platform's real limit (count shown),
  passing the 5-question profile test (who you are · who you help · the outcome · why believe you
  · what next) with ONE link (the funnel, else the booking link) and one identity line everywhere.
  Reads the Brain, saves the pack as a styled doc, updates identity/profiles.md inside sf-setup's
  headings (creates it only if absent). 3-state compliance gate; license display never cut. Copy
  only.
  Trigger on: "update my attraction bios", "bios for attracting agents", "recruiter bio", "align my profiles
  to my funnel", "my Instagram bio for agents", "LinkedIn about for agent attraction", "optimize
  my profiles for attraction".
---

# Platform Profiles — one identity, every platform, aligned to the funnel

You refine the member's ENTIRE bio stack in one run — every platform, every character limit, one consistent
identity, one link that points at the funnel. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` (plain +
warm, Brain first, copy-only, compliant, write-back law) and `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md`.
The three laws and who owns `profiles.md`: `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

**Ownership, said once (the coordinator's ruling):** `identity/profiles.md` is **written first by the
Short-Form plugin's `sf-setup` in Week 3** — bios are Week 2–3 homework. This skill is the **designated Week 6
updater** of the same file: it reads it if present, refines each platform's bio to the funnel's CTA **inside
the same `## <Platform>` section headings** (never renames, reorders, or deletes one), appends sections only
for platforms `sf-setup` doesn't cover, and **creates the file only if it is absent** (the member skipped
Week 3) — with the same headings `sf-setup` uses: `## Instagram` · `## Facebook` · `## TikTok` · `## LinkedIn`
· `## YouTube`, in that order.

**Why this matters (`07-instagram/87`):** the profile is the "recruiting landing page" — agents check it
before they ever reach out, and a poorly optimized profile is a missed conversation. The bio formula Mike
teaches: who you are and how you help → who you help → credibility → a call to action with free resources →
one link. In Week 3 that link was the booking link or a DM hook; in Week 6 it becomes the funnel.

## Step 0 — Load, never ask
Pull the Brain (house rule 2 — pull before concluding anything is missing), then read: `brain.md` quick-ref,
`identity/compliance.md` (**the gate first — unset stops here**; license display rules — some states and
provinces require the license number or the brokerage name in public profiles: whatever `compliance.md` says
appears in EVERY long-form bio and never gets cut for space; recruiting scope), **`identity/profiles.md`**
(what `sf-setup` wrote — the starting point for every section; note each section's current CTA and link),
`identity/profile.md` (name, brokerage, what they're building, market, years, socials, booking link),
`identity/positioning.md` (the one line, the messaging pillars), `identity/offer.md` (the UVP one-liner
"I help [agent type] achieve [outcome] through [mechanism]" — if Status is seeds, build the line from
`positioning.md`'s seed and say Week 2 sharpens it), `identity/avatars.md` (the type of agent, in plain
words), `identity/voice.md` (tone + signature phrases), `identity/proof.md` (real numbers only, dated),
`identity/brand-visual.md` (tagline), and `memory/magnets.md` → `## Current magnet` (the live funnel URL).
**The CTA + link (one per bio):** the live funnel URL from `magnets.md` → else their booking link
(`brain.md` quick-ref) → else a DM hook ("DM me GUIDE for the comparison guide"). Never more than one CTA per bio.
**Present file = an UPDATE:** show, per platform, what changes and why (usually: the link, the CTA line, the
identity line tightened to the finalized offer) — never silently rewrite; keep what `sf-setup` got right.

## Step 1 — The identity line (the AI-search key — build it FIRST)
One sentence, used VERBATIM as the first line of every platform's bio:
**"[First Last] — helps [type of agent] [outcome] · [Brokerage as compliance.md requires] · [City]."**
(e.g. "Taylor Brooks — helps agents in years 1–5 build a business that doesn't reset every January · Real
Broker · Austin.")
If `sf-setup` already wrote an identity line, start from it and tighten it to the finalized offer; say what
changed. Why (say it to the member in one line, labeled as the system's doctrine): AI assistants and search
engines recommend people they can identify consistently — the same name + who they help + brokerage + city,
word-for-word, on every profile is what lets "who should I talk to about joining a team in [city]" answers
triangulate to THEM. Confirm the identity line with the member once (your turn — one word), then never vary it.
Outcome, never compensation: "build a business that doesn't reset" is an outcome; "earn rev share" is not.

## Step 2 — The 5-question profile test (every bio passes it, in order)
The cohort's rule — shared with `sf-setup` — every profile must answer five questions (built from
`07-instagram/87`'s bio formula):
1. **Who are you?** — the identity line, or its compressed form.
2. **Who do you help?** — the type of agent, by stage, in plain words (never a protected characteristic).
3. **What outcome?** — one outcome, not a feature (copywriting KB principle 2).
4. **Why believe you?** — one credibility fact from `proof.md` only (never invented; the upline's labeled as
   the upline's if the member's own is thin).
5. **What do I do next?** — the one CTA + the one link (the funnel, now that it exists).
Short platforms compress 1–3 into one line; long platforms give each a sentence. A bio that fails any question
gets rewritten before it ships.

## Step 3 — Write the stack (limits are HARD — show the count under each, recount after any edit)
Every bio: identity line (or its compressed form) + the type of agent + the outcome + the one CTA. Voice per
`voice.md`. Grounding: ONLY facts from the Brain — never invent awards, years, organization counts, or
designations; a bio with a made-up stat is a compliance incident on a public profile. No splits, caps, rev
share, stock, or income. Nothing about any other brokerage. The brokerage name and license exactly as
`compliance.md` requires.

| Platform | Field | Hard limit |
|---|---|---|
| Instagram | Bio | 150 chars (line-broken, emoji sparingly, CTA + link label) |
| Facebook | Page intro | 101 chars |
| Facebook | Page About | ~255 chars |
| TikTok | Bio | 80 chars |
| LinkedIn | Headline | 220 chars |
| LinkedIn | About | up to 2,600 (first 300 carry the hook — the fold; team leaders and broker-owners read here) |
| YouTube | Channel description | up to 1,000 (first ~150 show in search — identity line + hook there) |
| X | Bio | 160 chars |
| Threads | Bio | 500 chars |
| Google Business Profile | Business description | 750 (first 250 show — hand to `lm-gbp` if they want the full kit) |
| Brokerage site / team site | About | 200–300 words, long-form, proof-woven, the leader lane |
| Email | Signature block | name · identity line · phone · the one link · the compliance line |

The first five are `sf-setup`'s sections, refined; the rest are this skill's additions. Platform notes that
earn the expert badge: Instagram counts line breaks + emoji against the 150; LinkedIn's first 300 characters
decide whether About gets expanded — and LinkedIn is where team leaders and broker-owners live, so the About
there speaks to them; YouTube's description is SEARCHED — work "agents," the type, and the city in
naturally; the long-form bios are written in first person, warm, "you"-forward (copywriting KB principle 5),
and carry the mirror in one line (former brokerage never named). Instagram highlights (`07-instagram/87`):
suggest four — the guide · how we work together · the community · the member as a person.

## Step 4 — Deliver + write back (atomic)
1. Render ONE doc per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` §4 (render_doc.py): each platform as
   a section, the paste-ready text in a copy block, the character count under it, the 5-question check as one
   line, and — for the five `sf-setup` platforms — a one-line "what changed" note. Name: **"🪪 [Name]'s
   Platform Profiles — [YYYY-MM-DD]"** → save to the workspace's **`02 · Brand/`** (find-or-create), hand the
   DIRECT link. Compliance stamp per house rules #5 (`set` → one reminder).
2. Update **`~/attraction-brain/identity/profiles.md`** the way the contract says: keep the header and every
   `## <Platform>` heading exactly as `sf-setup` wrote them; replace only the bio text inside each of the
   five sections with the final (identity line first), and end each touched section with
   `*Updated by the Lead Magnet plugin on YYYY-MM-DD — CTA → [the funnel]*`; append `## X` · `## Threads` ·
   `## Google Business Profile` · `## Brokerage site` · `## Email signature` AFTER the five if they don't
   exist (same heading pattern). **Absent file → create it** with the five headings in `sf-setup`'s order,
   then the additions (the shape is in `shared/brain-contract.md`). Push (write → push → verify — the
   write-back law). The Design Studio's `ds-brand` reads the bios through the Brain Book; `lm-gbp` reuses the
   Google section; every other system now quotes the same identity.
3. Close with the checklist: *"Paste each one into its platform — start with Instagram and LinkedIn. When
   your guide goes live, your offer sharpens, or your brokerage changes, say 'update my attraction bios' and
   I'll refresh the whole stack."*
