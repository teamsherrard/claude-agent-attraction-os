# [Member First Name] — Agent Attraction Brain · Index
*Last updated: [Month Year] · Agent Attraction Brain v[x.y] · Schema aa-1.0*

> **This is the index. Every skill reads this file first.**
> **This Brain lives in the member's cloud workspace** (Google Drive or OneDrive — see `config.md` for the
> provider + workspace folder ID). The local copy at `~/attraction-brain/` is synced down each session. After
> you change anything here, it gets pushed back (via `attraction-brain-sync`, write → push → verify) so it
> persists. An unsynced write is a lost write.

## How to use this Brain (the laws)
1. **READ this first.** For depth on any topic, open the specific file listed under "The files" below.
   Never ask the member for anything already in the Brain. Never re-research what is current in the Brain.
2. **WRITE back what you learn, then PUSH immediately** (write → push → verify, one atomic step):
   - An agent conversation → `memory/conversations.md` (dated row; its `Stage after` cell is the stage request once the AI Admin exists — before Week 5 capture moves the `memory/pipeline.md` stage itself)
   - A named agent worth building a relationship with → `memory/top-50.md`
   - An objection heard, and what answered it → `memory/objections.md`
   - A win (yours, or an agent you helped) → `identity/proof.md` (Seeds section)
   - A story seed → `identity/story-bank.md` (Seeds section)
   - A content idea → `memory/ideas.md` · Anything published or scripted → `memory/content-log.md`
   - Brokerage or industry news → `memory/intel.md` · A date or follow-up → `memory/deadlines.md`
   - The day's numbers → `memory/scorecard.md` (the Daily Debrief appends the daily row) · the debrief itself → `memory/debriefs.md`
   On-the-go captures route through **attraction-capture**. One owner per file (`shared/brain-contract.md`);
   a reader never rewrites a file it does not own.
3. **STAY COMPLIANT.** Before anything public-facing (a post, a script, a bio, a DM template, an email, an
   ad), read `identity/compliance.md` — its FIRST line, `Status:`, is the verdict (the worst field's state;
   the `Gate:` line under it names why). It is **three-state**: `confirmed` → apply its rules and disclaimer ·
   `set` → apply and remind the member once to confirm · `unset` → **stop and say plainly that compliance
   is not set yet; do not produce the public piece** ("if empty, proceed" is banned). The attraction rules
   that always apply: no income or rev-share earnings claims, never talk badly about another brokerage or
   person, brokerage name and license display as the file says, compensation stays off public content.
4. **SOUND LIKE THEM.** Read-aloud output (scripts, reels, interview answers) reads `identity/voice-print.md`
   and `identity/voice.md`. Anything that can carry a story checks `identity/story-bank.md` for a real story
   that matches the avatar and the pain, weaves it in their voice, then stamps its **Used-where**. Former
   brokerages are never named in a story ("a franchise", "an independent"). Never fabricate a voice, a story,
   a quote, a testimonial, a production number, or a rev-share figure.
5. **THE WEEK RULE.** The Partner Offer is Week 2; content pillars, the bios, and the publishing layer Week 3;
   the channel Week 4; the sales system, the pipeline, and the AI Admin Week 5; the lead magnet and onboarding
   Week 6. A later-week file that is empty is not a gap; say which week builds it.

If `~/attraction-brain/` is missing, pull it with **attraction-brain-sync** first. A tool error is never
"no Brain". Only if the cloud search genuinely finds nothing: suggest "Set up my attraction brain."

## Quick reference (the fields every skill needs)
- **Name:** [First Last] · **Brokerage:** [name — or "independent"] · **Building:** [a downline at a cloud brokerage / a local team / a local brokerage / a mix]
- **Market:** [City, Region] · **Attracts in:** [local only / state or province / national / listed states]
- **Primary avatar:** [type + one line — e.g., "2–5 year agents paying for leads that don't convert"]
- **Known for:** [the one thing, from strategy.md]
- **Why I'm here (one line, out loud):** [from positioning.md]
- **Offer status:** [seeds (Week 2 builds the offer) / finalized by member]
- **Voice in one line:** [e.g., "Calm, practical, teacher energy — never hype"]
- **This week's activity target:** [conversations / calls / joins, from goals.md]
- **Organization today:** [N agents] · **12-month target:** [N agents]
- **Booking link:** [url] · **Primary CTA:** [e.g., "Book a call with me — [link]"] · **Socials:** [@instagram, @youtube, @tiktok]
- **Brand colors:** [#hex] / [#hex] / [#hex] · **Fonts:** [Heading] / [Body] · **Logo:** [loved as-is / refresh / building this week]
- **Compliance:** [confirmed / set / unset] · **Locale:** [country · currency · units — format every number and date to this (config.md)]

## The files
**identity/** — who the member is as a leader (set once, changes rarely)
- `identity/profile.md` — name, brokerage, market, agent type, years in, before-story, what they are building
- `identity/journey.md` — the three journey beats with "who relates to this", the leader moment, the WHY · the "Why join me" story at the end (Week 2, `attraction-why-join-me`)
- `identity/strategy.md` — what they want to be known for, growth focus, constraints, leaders they admire
- `identity/avatars.md` — the 1–3 Agent Avatars (type, pains, what they've tried, what they need to hear)
- `identity/prospect-intel.md` — RESEARCHED local agent landscape: brokerage footprint, moves, where they gather (sourced + dated; refreshed quarterly by Prospect Radar)
- `identity/positioning.md` — the model positioned without pitching: the one-line "why I'm here", the 2-minute model script, what stays for the private call
- `identity/offer.md` — what they have to give: the three layers (brokerage · upline · you), the value stack vs the five pains, free vs paid, the UVP one-liner (Status: seeds until Week 2)
- `identity/brokerage-model.md` — THEIR model explained in plain English, from their materials + `shared/brokerage-models.md` (private-call material)
- `identity/voice.md` — tone rules, sounds-like / never-sounds-like, signature phrases, primary CTA
- `identity/voice-samples.md` — real WRITTEN samples (how they type)
- `identity/voice-print.md` — the SPOKEN voice (how they talk) — read for every read-aloud script
- `identity/proof.md` — production wins, agents already helped (named, with result), organization size, reviews FROM AGENTS
- `identity/story-bank.md` — the Personal Story & Experience Bank, each story tagged persona · pain · use
- `identity/brand-visual.md` — Inventory (logo state, colors, fonts, headshots, name, leader vs selling brand) + Direction (feel, references, tagline) — the Design Package reads this
- `identity/content-pillars.md` — attraction content pillars, cadence, the two CTAs (written by the Short-Form System in Week 3; empty until then by design)
- `identity/publishing.md` — the short-form layer: platforms, cadence, the keyword, posting tool, best times, content board, link in bio (Short-Form-owned, Week 3; YouTube reads `Content board:` and `Keyword:` here)
- `identity/profiles.md` — THE bios file, one `##` per platform (Instagram · Facebook · TikTok · LinkedIn · YouTube) — `sf-setup` writes it in Week 3, `yt-setup` fills YouTube in Week 4, `lm-profiles` updates to the funnel's CTA in Week 6
- `identity/channel.md` — the YouTube channel: lanes and playlists, the CTA line, upload defaults, baseline, the Game Plan anchors, dated `## Performance` blocks (YouTube-owned, Week 4)
- `identity/sales-system.md` — the Partner Call machine: calendar, the five application-form questions, the "no" rule, CRM stage mapping, reminders (Conversion-owned, Week 5; mirrors the booking link in operations.md)
- `identity/goals.md` — 12-month milestones, 30-60-90 targets, the money scenarios (illustrative), weekly activity
- `identity/execution-framework.md` — the 12-month plan, weekly KPIs, monthly metrics, the CEO rhythm (built after goals lock)
- `identity/leadership.md` — From Agent to Leader readiness score + fix-first list (written by the Leadership Audit)
- `identity/operations.md` — hours, CRM, booking link, call cadence, onboarding steps (the AI Admin reads this)
- `identity/compliance.md` — the 3-state gate: license display, brokerage name rule, rev-share marketing policy, earnings disclaimer, recruiting scope, AI-likeness disclosure

**memory/** — what the member has done (grows daily)
- `memory/top-50.md` — the named prospect ledger: type · where they are · stage · last touch · next move
- `memory/conversations.md` — every agent conversation, dated (the AI's working memory, NOT the CRM — the member's CRM stays the system of record; when they conflict, the CRM wins)
- `memory/pipeline.md` — Identified → Conversation → Call booked → Call held → 3-way → Joined → Onboarded → Active
- `memory/organization.md` — agents in the organization: join date, status, retention notes
- `memory/scorecard.md` — the Targets block (attraction-goals) plus daily rows (the Daily Debrief) and weekly rows (the weekly check-in) against the 90-day targets
- `memory/objections.md` — objections heard + the answer that worked (the Short-Form System reads it for objection reels)
- `memory/debriefs.md` — the Daily Agent Attraction Debrief log: today's conversations, the score, tomorrow's three moves
- `memory/content-log.md` — everything published or scripted (check before creating, to avoid repeats)
- `memory/ideas.md` — content ideas captured on the go (read before generating new ideas; mark Used)
- `memory/intel.md` — brokerage and industry news from the Prospect Radar's news scan (on demand) and captures (dated, sourced)
- `memory/intel-reports/` — per-prospect pre-call briefs and the dated follow-up / reactivation plan files (the Conversion plugin writes them from Week 5)
- `memory/interview-pipeline.md` — the YouTube interview guest list and where each interview stands (YouTube-owned, Week 4)
- `memory/content-performance.md` — the Friday ledger: which Reels, stories, and keywords started agent conversations (Short-Form-owned, Week 3; YouTube appends its section from Week 4)
- `memory/follow-up-queue.md` — every prospect due a touch, with the reason, tomorrow's confirmations, the touch log (AI Admin-owned, Week 5)
- `memory/sales-funnel.md` — the weekly funnel by source: booked → held → 3-ways → joins, the constraint (Conversion-owned, Week 5)
- `memory/magnets.md` — every lead magnet and `## Current magnet`, the one every CTA points at (Lead Magnet-owned, Week 6; readers take the live guide from here first)
- `memory/list-growth.md` — the email list: nurture sequences, weekly opt-in rows, calls booked from the funnel, partners (Lead Magnet-owned, Week 6)
- `memory/events.md` — events run and their follow-up (Events-owned, Week 6) · `memory/support-log.md` · `memory/claude-updates.md` — the Support plugin's ticket log and Claude-changes digest
- `memory/capture-log.md` — anything capture could not classify (Open rows surface in the Debrief)
- `memory/deadlines.md` — what's due and when

**Existing materials** (old recruiting decks, bios, the brokerage's onboarding doc, a CRM export, past videos)
live in the workspace's **`06 · Materials`** folder — the member drops files there (or uploads in chat), then
says **"import my materials"**; `attraction-import` extracts each piece into the right file after they confirm.
A Realtor AI Brain, if one exists, is read once through the same skill and never written to.

**config.md** — the key registry: Schema aa-1.0 · Storage provider · Storage (ok · READ-ONLY (org-gated)) · Workspace name / ID / link · Timezone · CRM · Setup progress · Debrief time · Daily Debrief task · Workspace shared with · Realtor Brain bridge · Demo brain · Cohort week — then one block per later plugin (Short-Form · YouTube · Conversion & Sales · AI Admin · Lead Magnet · MAA Support), each with its own locked task keys; the `## AI Admin` block's first line `AI Admin: set up [date]` is how every other skill knows the Admin is installed
