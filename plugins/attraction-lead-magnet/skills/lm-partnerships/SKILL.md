---
name: lm-partnerships
description: >
  Writes the member's strategic-partner outreach for agent attraction — the lenders, mortgage
  brokers, title and escrow officers, inspectors, appraisers, coaches, vendors, and other leaders
  who talk to agents every day and hear their frustrations first (Mike's strategic partnerships
  lesson). Selfless and value-first: positioned as helping agents succeed, never "send me
  recruits"; gives each partner something to pass along (the comparison guide, an event invite, a
  training), a thank-you for every introduction, and a partner ledger in memory/list-growth.md.
  The list comes from the member's own sphere (named by them, never scraped); writes the first
  message, the follow-up, and the thank-you in their voice. Draft-only — the member sends every
  message. 3-state compliance gate; no referral fees, no compensation talk, nothing about any
  other brokerage.
  Trigger on: "partner outreach for attraction", "reach out to lenders about agents", "strategic
  partners for agent attraction", "who can send me agents", "partner message for my guide", "thank
  a partner for an introduction", "my partner list".
---

# Strategic Partnerships — borrowed trust, warm introductions

**Mike's lesson (`15-advanced-scaling/77`):** "nobody does it, but we've attracted a ton of agents by doing
this." Industry partners — lenders, mortgage brokers, title reps, inspectors, appraisers, coaches, anyone who
"consistently interacts with multiple agents across brokerages" — hear about agents' frustrations before
anyone else. "One introduction from a trusted partner is worth" more than a week of cold outreach. How to make
it work: educate them on who you help, **position it as helping agents succeed, not recruiting** — *"if you
run into anybody struggling with production, support, or training, feel free to send them my way; I'd love to
help, and it's free"* — give them resources to pass along, get them to share your events with their lists, and
**thank and recognize them for every introduction**. When those agents close more deals, the partner wins too.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) — #1, #5 (the gate; a partner message is
public-facing), #9, #12 (draft-only). Copy standard: `${CLAUDE_PLUGIN_ROOT}/shared/copywriting-kb.md` →
"Emails, DMs, and the newsletter." The three laws and the partners-table shape:
`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`.

## Step 0 — Load (lazy)
Pull the Brain (house rule 2). `identity/compliance.md` (**the gate — unset stops here**; recruiting scope;
the inducement line — nothing the member writes offers a referral fee or an inducement), `identity/profile.md`
(name, brokerage as required, market, booking link), `identity/offer.md` (what the member gives agents — as
outcomes — and the UVP one-liner; this is what the partner needs to be able to repeat), `identity/avatars.md`
(the type of agent, so the partner knows who to send), `identity/proof.md` (one credibility line; agents
helped, consent), `identity/voice.md` + `voice-samples.md`, `identity/operations.md` (signature, the weekly
call — the thing partners can invite agents to), `memory/magnets.md` → `## Current magnet` (the guide they can
pass along), `memory/list-growth.md` → `## Partners` (who's already listed; create the file from the locked
shape if the Brain predates it).

## Step 1 — The list (the member's own sphere — never researched, never scraped)
One question, their turn: *"Name the industry people you already trust and talk to — your lender, the
mortgage broker who closes your deals, your title or escrow rep, an inspector, a coach, another leader you
respect. First names and roles are plenty; three to eight is the sweet spot."* If they're unsure, prompt by
role (Mike's list above) — never suggest a real person. Write each to the partners table as `listed`. If the
CRM (`config.md`) holds tags like "vendor" or "lender," say they can pull from there — the member brings the
names; the plugin never reads contacts to build this list.

## Step 2 — The messages (one set, personalized per partner by role)
For each partner (or each role, if they'd rather personalize by hand), in the member's voice, ≤ 120 words each:
1. **The first message** (text, DM, or email — whatever they'd normally use with this person): one line of
   genuine appreciation for the relationship · what the member has been doing — *"I've been helping agents
   who are [the pain, in plain words] get [the outcome]"* (from `offer.md`, as outcomes) · the ask, selfless:
   *"If you run into an agent who's struggling with [production / support / training], feel free to send them
   my way — I'd love to help, and it costs them nothing."* · one thing the partner can pass along (the guide's
   funnel link, the weekly call, an event) · no model, no brokerage pitch, no comp. **Never "send me
   recruits," never a referral fee or any inducement** (compliance-doctrine §6).
2. **The resource to pass along** (one short paragraph the partner can forward verbatim): what the guide is
   and why it's fair ("honest about every model, including his"), the link, "no pitch."
3. **The follow-up** (2–3 weeks later, once): one agent-win story (consent) or one new resource, and a thank-you
   for keeping an eye out. Value, not a nudge.
4. **The thank-you for an introduction** (the one message that keeps partners sending): specific — who they
   introduced, what the member did for that agent, genuine gratitude; "give credit where it's due." If the
   member hosts a weekly call or an event, an invitation to be recognized there.
5. **The event ask** (if an event exists — the Events plugin writes the event; this writes the partner line):
   *"Would you send this to your agents? It's a free training on [topic], no brokerage talk."*

## Step 3 — Deliver, save, log
1. Deliver in chat, one block per partner (or role), paste-ready.
2. Save `Partner Outreach Kit — [YYYY-MM-DD]` into `04 · Agents/Prospects/` (output standard §4–§6; fallback
   applies).
3. `memory/list-growth.md` → `## Partners`: a row per partner (`[first name] · [role] · listed · [what they
   pass along] · 0 · —`); when the member says they sent it → `reached out`; an introduction → `Intros so far`
   +1 and `active`; a thank-you sent → `thanked`. **attraction-brain-sync PUSH.** Silent. (An agent a partner
   introduces becomes a Top-50 row through the Brain's capture skill — not this file.)
4. Close: *"Send these in your own words from your own phone — they're drafts, and these are your people.
   When someone sends an agent your way, say 'thank a partner' and I'll write it. Every introduction goes in
   your list so you remember who's been good to you."*

## Compliance pass
The two cardinal rules (nothing about any brokerage, sponsor, or person) · no compensation, rev share, or
income · no referral fees or inducements of any kind · recruiting scope (a partner outside the scope is still
a partner; the agents they'd send must be inside it — say so in one line) · franchise look-period rule if a
partner is a broker-owner the member means to approach (`02-prospect-targeting/26`) · the stamp on any email ·
`set` → one reminder · never a bracket token. Draft-only; the member sends.
