---
name: lm-profiles
description: >
  Writes the member's bio / about section for EVERY platform, aligned to their agent-attraction funnel —
  Instagram, TikTok, Facebook, LinkedIn, YouTube, X, Threads, Google Business Profile, the brokerage site,
  plus an email signature — each sized to that platform's real character limit (count shown, never over),
  passing the 5-question profile test (who you are · who you help · the outcome · why believe you · what to
  do next) with ONE link (the funnel, else the booking link) AND one identity line on every platform so AI
  answers can find the same leader everywhere. Reads everything from the Agent Attraction Brain, saves the
  pack as a styled doc, and writes the finals to identity/profiles.md — the one owner; the Short-Form
  plugin's sf-setup reads it if present. 3-state compliance gate; license display never cut for space.
  Copy only — never logs into any platform.
  Trigger on: "attraction bios", "bios for attracting agents", "recruiter bio", "align my profiles to my
  funnel", "my Instagram bio for agents", "LinkedIn about for agent attraction", "YouTube channel
  description for agents", "optimize my profiles for attraction", or any bio/about request from a leader
  attracting agents.
---

# Platform Profiles — one identity, every platform, sized to fit

You write the member's ENTIRE bio stack in one run — every platform, every character limit, one consistent
identity aligned to the funnel. Apply `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` (plain + warm, Brain
first, copy-only, compliant, write-back law) and `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md`. The three
laws and the `profiles.md` shape: `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

**Why this matters (`07-instagram/87`):** the profile is the "recruiting landing page" — agents check it
before they ever reach out, and a poorly optimized profile is a missed conversation. The bio formula Mike
teaches: who you are and how you help → who you help → credibility → a call to action with free resources →
one link.

## Step 0 — Load, never ask
Pull the Brain (house rule 2 — pull before concluding anything is missing), then read: `brain.md` quick-ref,
`identity/compliance.md` (**the gate first — unset stops here**; license display rules — some states and
provinces require the license number or the brokerage name in public profiles: whatever `compliance.md` says
appears in EVERY long-form bio and never gets cut for space; recruiting scope), `identity/profile.md` (name,
brokerage, what they're building, market, years, socials, booking link), `identity/positioning.md` (the one
line, the messaging pillars), `identity/offer.md` (the UVP one-liner "I help [agent type] achieve [outcome]
through [mechanism]" — if Status is seeds, build the line from `positioning.md`'s seed and say Week 2 sharpens
it), `identity/avatars.md` (the type of agent, in plain words), `identity/voice.md` (tone + signature
phrases), `identity/proof.md` (real numbers only, dated), `identity/brand-visual.md` (tagline), and
`memory/magnets.md` → `## Current magnet` (the live funnel URL).
**The CTA + link (one per bio):** the live funnel URL from `magnets.md` → else their booking link
(`brain.md` quick-ref) → else a DM hook ("DM me GUIDE for the comparison guide"). Never more than one CTA per bio.
If a real bio already exists in `identity/profiles.md`, this is an UPDATE — show what changes and why, never
silently rewrite.

## Step 1 — The identity line (the AI-search key — build it FIRST)
One sentence, used VERBATIM near the top of every platform:
**"[First Last] — helps [type of agent] [outcome] · [Brokerage as compliance.md requires] · [City]."**
(e.g. "Taylor Brooks — helps agents in years 1–5 build a business that doesn't reset every January · Real
Broker · Austin.")
Why (say it to the member in one line, labeled as the system's doctrine): AI assistants and search engines
recommend people they can identify consistently — the same name + who they help + brokerage + city,
word-for-word, on every profile is what lets "who should I talk to about joining a team in [city]" answers
triangulate to THEM. Confirm the identity line with the member once (your turn — one word), then never vary it.
Outcome, never compensation: "build a business that doesn't reset" is an outcome; "earn rev share" is not.

## Step 2 — The 5-question profile test (every bio passes it, in order)
The cohort's rule: every profile must answer five questions (built from `07-instagram/87`'s bio formula):
1. **Who are you?** — the identity line, or its compressed form.
2. **Who do you help?** — the type of agent, by stage, in plain words (never a protected characteristic).
3. **What outcome?** — one outcome, not a feature (copywriting KB principle 2).
4. **Why believe you?** — one credibility fact from `proof.md` only (never invented; the upline's labeled as
   the upline's if the member's own is thin).
5. **What do I do next?** — the one CTA + the one link.
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
| TikTok | Bio | 80 chars |
| X | Bio | 160 chars |
| Threads | Bio | 500 chars |
| Facebook | Page intro | 101 chars |
| Facebook | Page About | ~255 chars |
| LinkedIn | Headline | 220 chars |
| LinkedIn | About | up to 2,600 (first 300 carry the hook — the fold; team leaders and broker-owners read here) |
| YouTube | Channel description | up to 1,000 (first ~150 show in search — identity line + hook there) |
| Google Business Profile | Business description | 750 (first 250 show — hand to `lm-gbp` if they want the full kit) |
| Brokerage site / team site | About | 200–300 words, long-form, proof-woven, the leader lane |
| Email | Signature block | name · identity line · phone · the one link · the compliance line |

Platform notes that earn the expert badge: Instagram counts line breaks + emoji against the 150; LinkedIn's
first 300 characters decide whether About gets expanded — and LinkedIn is where team leaders and broker-owners
live, so the About there speaks to them; YouTube's description is SEARCHED — work "agents," the type, and the
city in naturally; the long-form bios are written in first person, warm, "you"-forward (copywriting KB
principle 5), and carry the mirror in one line (former brokerage never named). Instagram highlights
(`07-instagram/87`): suggest four — the guide · how we work together · the community · the member as a person.

## Step 4 — Deliver + write back (atomic)
1. Render ONE doc per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md` §4 (render_doc.py): each platform as
   a section, the paste-ready text in a copy block, the character count under it, the 5-question check as one
   line. Name: **"🪪 [Name]'s Platform Profiles — [YYYY-MM-DD]"** → save to the workspace's **`02 · Brand/`**
   (find-or-create), hand the DIRECT link. Compliance stamp per house rules #5 (`set` → one reminder).
2. Write the finals to **`~/attraction-brain/identity/profiles.md`** (create it from the locked shape in
   `shared/brain-contract.md` if the Brain predates it): identity line at top, the one link, then each
   platform's final text + date. Push (write → push → verify — the write-back law). This file has ONE owner —
   this skill; the Short-Form plugin's `sf-setup` reads it if present (its bio slot), and the Design Studio's
   `ds-brand` reads it through the Brain Book. Every other system now quotes the same identity.
3. Close with the checklist: *"Paste each one into its platform — start with Instagram and LinkedIn. When
   your guide goes live, your offer sharpens, or your brokerage changes, say 'update my attraction bios' and
   I'll refresh the whole stack."*
