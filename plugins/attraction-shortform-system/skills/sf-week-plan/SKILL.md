---
name: sf-week-plan
description: >
  The Monday Week Plan (Week 4) — the ONE scheduled workflow, the week in one package: each Monday it
  drafts this week's three posts from the Game Plan's calendar — the scripts for the two Reels (the cards the
  member films from), the carousel's caption (a designed kit post while they last), at most one industry
  story to react to when there is a good one — keeps the four weeks mapped, fills one Reel slot from a clip
  of the member's videos first (never an extra post), drafts recognition words for a new partner or
  consented win, and puts the asks on the 90/10 rule. Also owns the optional Mid-week Nudge and the
  registry of every short-form workflow. Draft-only; on only with the member's yes; runs on demand too.
  Trigger on: "run my week plan", "draft this week's attraction posts", "my attraction week plan", "turn on
  my Monday week plan", "stop my Monday week plan", "turn on my mid-week nudge", "what's due this week", "my
  short-form scheduled workflows", "my attraction workflows", "email me my notes".
---

# The Monday Week Plan — the week in one package (Week 4)

**Mike, 2026-11-22: "one, where it's like, here's your weekly package that has the prep and has any sort of green
screen articles."** This is the ONE scheduled workflow of the short-form system. Each Monday it drafts the week the
Game Plan already dated — **two Reels and one carousel**: the two Reel scripts (the cards the member reads from while
they film, word for word, with the filming line: *"Film on your phone in Instagram's free Edits app — it has a
teleprompter built in: paste the script, press record, read."*), the carousel's caption (a designed kit post while
the six last — "post, don't make"; otherwise its slides), and **at most one industry story to react to when there is
a good one** (industry news, lead generation, new agents struggling — never a brokerage headline; nothing when there
is nothing good) — on the board when they have one, in the Brain always. It keeps the four weeks mapped (the
monthly refill, the Batch Prep cards and the Wednesday news watch all ride inside it now; those three tasks were
retired on 2026-11-22). **The asks follow the 90/10 rule** (house rules #13): the month's one keyword post asks for
the guide or the call; every other post asks for a follow, a save, a share or a comment. Each run also scans the
Brain for a new partner or a consented win and drafts the recognition words. **When the member's videos have clips
waiting, one of the week's two Reels may be drafted from a clip first** — a video feeds the week, it never adds a
post (Job B, step 2b). It is the
scheduled half of the short-form rhythm; `sf-weekly-routine` is the member-run half (the batch block, the
engagement slot, the check-in) and plans around these drafts when this ran.

**Apply house rules** (`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`) and the Brain Contract
(`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`): this skill appends to `memory/content-calendar.md` (the
Monday rows' Status and the `## Week briefs` section; new rows only to keep 30 days mapped; and three cells —
Working title · Hook · Carries — of a Reel slot it drafts from a queued clip), writes `content-log.md`
rows at `Scripted`, appends one `returned` row to `memory/ideas.md` per topic a clip displaced, fills board cards, and touches `config.md` only on its own lines (the Monday Week Plan's, the
Mid-week Nudge's, and `Email me:` when the member asks for or stops the emails). The doctrine for the drafts is
`${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md` §7–§9 (lazy-load at Job B); the call-to-action law and the
scalability rule bind every line (Rules, below).

> **Two ways it runs.** On a schedule, Mondays — only with the member's explicit yes (setup Step 5's consent card,
> or Job A here). Or on demand, any day ("run my week plan", "draft this week's attraction posts"). **Draft-only,
> always:** nothing is posted, scheduled, sent, or moved on its own; the member films, approves, and posts.

## Four jobs (detect from the message)
- **A · PROVISION / STOP** — "turn on my Monday week plan", "stop my Monday week plan", "pause my week plan", "turn
  on my mid-week nudge", "stop my mid-week nudge".
- **B · THE WEEK, NOW** — "run my week plan", "draft this week's attraction posts", "my attraction week plan":
  the same work the scheduled run does, in chat, today.
- **C · THE REGISTRY** — "my short-form scheduled workflows", "my attraction workflows", "email me my notes" /
  "stop emailing me": every short-form workflow and its status (below).
- **D · THE MID-WEEK NUDGE, NOW** — "what's due this week", "my mid-week nudge": the count and today's script.

## Job A — Provision only on a yes; stop in one sentence (the Week Plan and the Mid-week Nudge)
The block is `~/attraction-brain/config.md → ## Short-Form (Week 4)` (an older heading with the earlier week number is the same block
— read it, never create a second one). Each workflow has one line holding exactly one of three values: a task id (on) · `paused` (the
member stopped it; its phrase brings it back) · `later` (not switched on yet); any other value in an older block reads as
not on. This skill's lines: `Week Plan task:` · `Week Plan slot:` · `Midweek Nudge task:` (update a line in place, never add a twin; a line is also found by its task id value).
1. **The Monday Week Plan** — read its line. **A task id** → it is on; say so in one line. **`paused`** → they stopped it;
   honored (its phrase brings it back). **`later` / no line / any other value** (the consent card's Yes normally switched it on)
   → on the member's phrase ("turn on my Monday week plan") switch
   it on as a statement, never an offer, never a question (the owner, 2026-11-14: told, not asked): *"Switching on
   your Monday Week Plan — Mondays, 7:00 am; name another time any time."* (The Yes given on setup's consent card IS
   this consent — setup provisions it without asking.)
2. **On the phrase (or setup's Yes)** → `list_scheduled_tasks` first (adopt an existing `attraction-sf-week-plan`, never a twin), else
   `create_scheduled_task` with `taskId: attraction-sf-week-plan`, `cronExpression: 0 [hour] * * 1` (the hour they
   chose, default 7:00 am, in `config.md → Timezone`, no timezone math), and the `prompt` set **verbatim** from
   `references/week-plan-task-prompt.md`. Verify with `list_scheduled_tasks` (present, enabled, a `nextRunAt`); not
   there → say so plainly, never claim a schedule that did not save. Write `Week Plan task:
   attraction-sf-week-plan` and `Week Plan slot: Mondays [time]`, push via `attraction-brain-sync`, verify.
   Confirm once: *"On. Say 'stop my Monday week plan' any time."*
3. **Stop / pause** → `delete_scheduled_task` (or disable for pause) on the saved id; write `paused`;
   push; confirm in one line. Never a second task. A demo Brain never gets a task.
4. **The Mid-week Nudge (by phrase — one of the five by-phrase workflows — never named in the sitting):** "turn on my mid-week nudge" → read `Midweek Nudge
   task:` (a task id → on, say so; `paused` → they stopped it, the phrase brings it back). On the phrase →
   state it (*"Switching on your mid-week nudge — Wednesdays, [the Week Plan's hour]."*), `list_scheduled_tasks` first
   (adopt an existing `attraction-sf-midweek-nudge`), else `create_scheduled_task` with `taskId:
   attraction-sf-midweek-nudge`, `cronExpression: 0 [hour] * * 3` (Wednesdays, the Week Plan's hour unless they name
   one), the `prompt` **verbatim** from `references/midweek-nudge-task-prompt.md`; verify; write `Midweek Nudge task:
   attraction-sf-midweek-nudge`; push; confirm: *"On. Say 'stop my mid-week nudge' any time."* Stop → delete,
   `paused`, push, one line. Setup never names the five by-phrase workflows (Mike, 2026-11-22); each switches on by its phrase.
5. **Keep the saved task current.** Whenever this skill runs in chat and `Week Plan task:` holds a task id:
   `list_scheduled_tasks`, read that task's saved prompt (its `path`), and when it is not the block
   `references/week-plan-task-prompt.md` ships today — an older one has no clip-queue step — replace it with
   `update_scheduled_task` (`prompt` only, verbatim from the reference; the same task id, the schedule untouched),
   verify, and say nothing unless it failed. It is the workflow the member already said Yes to, still draft-only:
   never a second task, never a new consent card.

## Job B — The week, drafted (the scheduled run does exactly this)
**Read:** `brain.md` · `config.md` (timezone, locale; the Short-Form block's `Email me:` line) ·
`memory/content-calendar.md` (the rows dated this week — Monday to Sunday of the run date — and the whole mapped
window; and its last section, `## Clips from your videos (YouTube)` — the clip queue, read-only) · `identity/publishing.md` (`Content board:`, `Keyword:` — both words, `GUIDE · [the offer's word]`, `What it
opens:`, `Cadence:`, `Weekly mix:`, `Batch day(s):`) · `identity/offer.md` (the header's `Comment keyword:` and
`Join-gated package allowed:` lines — the register of every call line; `## The framework` — the method the help is
for; `## Content branches`; the program name) · `exports/week3-kit-*.txt` (newest — chapter 7: the six post outlines
and the **CALLS TO ACTION** table, whose lines every ask takes verbatim; absent → the asks come from the keyword
sheet or the offer on the same shapes, and one line says "rebuild my kit") · `exports/keyword-sheet-*.txt`
(newest — the two words and their lines) · the newest `exports/week-plan-*.txt` (its date is "since the last run")
· `identity/content-pillars.md` (the angles, `## In your words` — the member's own answers lead a hook where one
fits, marked "your words"; the hooks bank) · `identity/compliance.md` (the first line, `Status:`).
Then, per post, only the files the draft needs: `identity/voice-print.md` · `voice.md` · `voice-samples.md` ·
`avatars.md` · `story-bank.md` (the story the row carries; stamp Used-where) · `proof.md` (the `OK to use publicly?`
column; `## Seeds`) · `memory/organization.md` (joins since the last run) · `memory/debriefs.md` (wins named since
the last run) · `memory/magnets.md → ## Current magnet` · the optimizer's
rules (`${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md`) · the story deck
(`${CLAUDE_PLUGIN_ROOT}/skills/sf-stories/references/story-prompt-deck.md`) · `identity/operations.md` (the weekly
model call day — a story proposes itself) · for a slot drafted from a clip, the clip's script
(`exports/youtube-clips-*.txt`, else the row's `Script doc` link) and `memory/ideas.md` (the row it gains). The board (a `Content board:` URL) is read as data — cards the member
moved, renamed, or deleted are their decisions.
1. **No calendar, or nothing dated this week** → say so in one line and point at the Game Plan (*"say 'plan my next 30
   days of reels' and I'll map the month first"*); draft nothing from thin air (queued clips wait for a mapped week
   — they fill slots, they never make one).
2. **Compliance three-state** (the drafts are public once filmed): `unset` → build the week's list, write no
   scripts or captions (no slot is drafted, so no clip is placed — the queue waits), say in one line that the drafts
   need the compliance basics ("set up my attraction compliance"); `set` → apply and remind once; `confirmed` → apply.
2b. **The clip queue first — clips from the member's videos fill Reel slots; they never add a post** (the owner,
   2026-11-14). Read the calendar's last section, `## Clips from your videos (YouTube)` — the YouTube system's,
   one row per clip (`Added` · `From video` · `Clip` · `Hook` · `Script doc` · `System ID`); read-only here, never
   a byte written in it. A clip is **queued** while no row of the short-form table carries its System ID in its
   `Carries` cell (any row, any Status — a `dropped` row still counts, so a clip the member dropped never comes
   back); once a row carries it, it is **used** — that row is the only mark. No such section, or nothing queued →
   skip this step: the week runs exactly as it always has.
   - **The slots a clip may take:** this week's rows still at `Idea` whose Format is `talking head`. Never a kit
     post, never a green-screen row (the news slot), never a carousel, never a row at `Scripted` or later.
      - **How many:** one clip Reel a week at most — one of the week's two Reels stays the plan's own (Mike,
     2026-11-22: two Reels and one carousel, nothing added). Count the week's Reels (`dropped` aside): two or more
     → one clip · one → none. A clip that a row of this week already carries counts toward the number. Three posts a week stays
     three posts a week.
   - **Which clips:** the newest video first (the latest `Added`; on a tie, the rows lower in the section), and
     within a video clip 1, then 2, then 3.
   - **Which slots first:** date order — a Story or Personality row only when no other slot is left, so the Reel
     that stays the plan's own is the member's own story whenever the week has one.
   - **Drafting a slot from a clip.** Read the clip's script from its script doc: the clips' text in the Brain
     first (`exports/youtube-clips-[the clip's System ID without its -c1 / -c2 / -c3].txt`, the block `SHORT
     [n]`), else the row's `Script doc` link through the storage connector. The clip's hook (its `Hook` cell — the
     script's own opening line when the pack was rebuilt and the two differ) becomes the row's **Hook** and
     **Working title**; the row's **Carries** cell becomes `clip: [the clip's System ID]`; its Date · Day · Format
     · Pillar · CTA cell · own System ID do not change. The clip's script becomes the Reel's script, word for
     word, on the card and in the week's doc, with ONE change: its closing ask is the row's ask (the CTA cell —
     what the call-ask rule gave this week), in the kit's line for that rung; the clip's own ask never overrides
     it and never adds a second. The gate and the cardinal rules apply to a clip's script like any draft (a line
     that breaks one is fixed and named in one line). Then the package exactly as step 3 writes it: the brief (it
     carries a clip from "[video title]") · the hook three ways, the clip's first and marked · the bullet version
     · the CTA line · the captions with the row's ask as the last line.
   - **Nothing is lost.** The topic the slot held goes back to the member's idea bank: ONE row appended to
     `memory/ideas.md` in its locked shape — Logged = today · Tag `shortform` · Idea = the old working title and
     hook, what it carried, then `returned from [the row's date]` · Avatar / pain when the topic named one ·
     Status `open`. (A `starter` topic is not returned — the starter bank still holds it.) The 30-day top-up and
     the next calendar window read the member's open ideas first, so it comes back on its own.
   - **A clip whose script cannot be read** (no clips text, the doc will not open) stays queued; the next queued
     clip is tried; none readable → the slot is drafted as the plan wrote it, and one line says so under what was
     left for the member.
3. **For each row dated this week** (three: the carousel and the two Reels): the brief (pillar · for whom · story or
   proof carried · rung + the word) · **the hook three ways** (styles labeled, the strongest marked) · **the script**
   (30–60 s, ~80–150 words, written for speech in their cadence) or **talking points** for a green screen (facts
   with a source, the cardinal rules read back) or **slide copy** for a carousel · **the bullet version** · **the
   CTA line — the 90/10 rule** (house rules #13): the month's one keyword post (the kit's guide carousel, or the
   kit's call post when its week comes) carries the kit's line verbatim — the guide (*"[what the guide holds, one
   clause]. Comment GUIDE and I'll send it."*) or the call (*"If you want my help running this, free, [the booking
   line]."* — the law's shape; open register *"I'll walk you through it, free, no strings"*); **every other post ends
   on a soft ask in the member's voice** — a follow, a save, a share or a comment on the topic (*"follow if you want
   to learn how to [the outcome] without [the pain]"*); never two asks on one post; never the brokerage as the reason
   · **the filming line, once per Reel** — *"Film on your phone in Instagram's free Edits app — it has a teleprompter
   built in: paste the script, press record, read."* ·
   **the captions** per the optimizer's rules (Instagram + Facebook with the ask as the last line, TikTok one line,
   YouTube Shorts title/description/tags, cover text). **A kit post row first** (its Format or Carries cell says `kit post`, or its title is one of the six — the guide carousel · five problems, five fixes · my story · what you get · proof · book the call) — it sits at `Ready to Post` from the day the calendar was written, and this step still handles it: it is **post, don't make**:
   no hook, no script — the designed file is in the member's Offer folder. Draft only its caption from chapter 7's
   outline (the post's `Caption:` line and its ask from the CALLS TO ACTION table), the platform lines, the stamp,
   and a one-line posting note (which file, which size); never re-design or rewrite the slides; its Status stays `Ready to Post` (designed; only the posting is left — never downgrade it; nothing was recorded; posting flips it to `Published`). Then every other row: one already at `Scripted` or later → leave it; say so; a slot step 2b gave a clip → drafted from the clip as 2b says, never from the topic it held.
4. **One industry story, at most (optional):** read `memory/intel.md` (dated, sourced rows, unused first); on
   demand only, one live search (≤ 2 queries) — a scheduled run reads the intel file alone. Keep ONE item only when
   it is real, from the last 30 days, and about industry news, lead generation or new agents struggling — **never a
   brokerage headline** (Mike, 2026-11-22: "it can be dangerous… not brokerage headlines"). Write it as *"If you'd
   rather react to the news this week, swap it in for Reel 2:"* with the source (title · outlet · date · link), a
   word-for-word hook and four talking points, the cardinal rules read back (never a negative word about a
   brokerage or a person). Nothing good → nothing written, nothing said. **Stories are not drafted** — one optional
   line in the Game Plan is all; the Daily Stories Prompt runs by phrase.
4b. **The recognition scan (the Win & Milestone posts — inside this run, never a task of its own):** what is new
   since the last run (the newest `exports/week-plan-*.txt` date; none → the last seven days): a new partner in
   `memory/organization.md` (a `Joined` date since then), a win named in `memory/debriefs.md` or captured to
   `identity/proof.md → ## Seeds`, a consented result added to `identity/proof.md → ## Agents already helped`. For
   each: the recognition words in the shape of the team templates the member designed with their brand (welcome a
   new partner · agent win · team milestone) — the caption · the story line · the slide copy (the name · what
   happened · the member's one line · the program name · the stamp). **The consent gate:** an agent is named or
   pictured only with their written OK on file (proof.md's `OK to use publicly?` column, or the organization row's
   Notes); without it the draft is marked *"needs [First]'s OK before it goes out"* with the one-line ask the member
   can send (*"Mind if I celebrate this on my page this week — one post, first name only? Say the word."*). The
   drafts join the week's doc (RECOGNITION THIS WEEK) and the board as cards (pillar Proof, or Personality for a
   milestone; Format `Graphic` — the designed team post, or `Talking Head` when they would rather say it on camera; Status `Scripted`), one content-log row each (Topic beginning `[recognition]`).
   The graphic itself the member makes in Claude Design ("design my team posts" / "my welcome post for [Name]" — the
   designed masters, a name-and-photo swap); the close says that in one line. No wins, no joins → nothing drafted,
   nothing said.
5. **The board** (a `Content board:` URL): find each row's card by System ID; write the full package into the card
   body (sections replaced, never stacked); Status → `Scripted`; the Publishing Date stays the calendar's. Not
   found → create it per the spec (`${CLAUDE_PLUGIN_ROOT}/shared/notion-board-spec.md`) with the row's System ID.
   **A Reel drafted from a clip is an ordinary card on the 🎞 Reels tab** — the same card, found by the row's own
   System ID: its Topic becomes the clip's hook, Format `Talking Head`, the package in the locked sections, and
   **📎 SOURCES names the video** (*a clip from your video "[video title]" — clip [n] of 3*, with the pack's link);
   never a second card, never the clip's System ID in a title.
      **Keep four weeks mapped (the monthly refill rides here):** if fewer than four weeks of calendar rows sit ahead of
   today, append the next week's rows to `memory/content-calendar.md` in the locked shape — one carousel (the next
   kit post while they last, else one outlined from the guide's pages) and two Reels (one that teaches or takes a
   stand, one that shows who they are), the asks on the 90/10 rule, from the Game Plan's angles, the hooks bank, the
   member's ideas, the starter bank last (`starter` marked) — and seed them as `Idea` cards, then count-check. No board → skip the board steps silently; the calendar and the brief are the record.
6. **Write back, then push:** one `content-log.md` row per drafted post in the locked shape (Status `Scripted`;
   Topic / hook begins `[talking head]` / `[green screen]` / `[LinkedIn doc]`; a clip Reel's ends `— clip from
   "[video title]"`); the calendar rows' Status → `Scripted` (a clip slot's Working title, Hook and Carries cells
   written in the same edit — nothing else in the row, nothing in the `(YouTube)` sections); a dated block under `## Week briefs` in `memory/content-calendar.md` (the week's titles · the clips placed, each with its video and the date it took, and the topics returned to the idea bank · the story set in one line · what was left undrafted and why); the story-bank Used-where; `ideas.md` rows → `used` (and the `returned` rows of step 2b appended). Save the
   week's doc per the output standard as `[YYYY-MM-DD] · Week Plan` in `03 · Content/Short-Form/[YYYY-MM · Month]/`,
   and keep its text at `~/attraction-brain/exports/week-plan-YYYY-MM-DD.txt` (the Brain Board reads this week's
   rows from it). Push via `attraction-brain-sync` **marked as the run's closing push**, verify — the sync rebuilds
   the Brain Board and refreshes the Brain Book's "What's next" page and gives back their two links; relay them. A
   failed push: say it is NOT saved, keep the drafts visible, retry once, stop. The scheduled run then tells the
   member the owner's three ways (the note in Cowork · one email to their own address only when `Email me:` is `yes` ·
   the push) — the task prompt carries the steps verbatim; in chat, the close below is the note.
7. **Close** (the scheduled run leaves this as its final message; in chat, say it). **It opens with the member's
   win when there is one** (the owner, 2026-11-15 — the student has to feel the win was theirs; the task prompt
   prints the counting rule): *"Last week you got all [m] out — a full week."* / *"Last week you got [n] of [m] out
   — '[a title]' is live."* — counted from the calendar's `Published` rows of last week; no line when none went out
   or it is the first week; never a guilt line, never a view count. Then, short (Mike, 2026-11-22: less is more): *"Your week is drafted
   — two Reels and your carousel for the week of [date][, on your board]. Film on [day]: '[Reel 1]' and '[Reel 2]'
   — the scripts are in your package; your carousel goes out [day]. [One of this week's Reels is a clip script from
   '[video title]' — film it as written.] [There's one industry story in your package if you'd rather react to the
   news.] [Plus a welcome post for [First] — needs her OK.] When a Reel is filmed, open a new chat and say 'edit my
   reel' — your AI Editing Studio edits it. Your Brain Board and your Brain Book are updated — here they are: [the
   Board link] · [the Book link]."* (Drop the clauses that do not apply; a rebuild that failed is named plainly with
   "refresh my brain board" — never claimed. Never a count of what is still waiting, never "System ID", no phrases
   to learn.)

## Job C — The registry (every short-form workflow)
Read `config.md`'s Short-Form block, call `list_scheduled_tasks`, and show — in plain words, never task ids:

| Workflow | When | Switched on | Owner | Task id |
|---|---|---|---|---|
| Monday Week Plan — the week in one package (the two Reel scripts and cards, the carousel's caption, at most one industry story, the four weeks kept mapped, the recognition scan) | Mondays, 7:00 am | by the consent card's Yes | this skill | `attraction-sf-week-plan` |
| Keyword Follow-up Queue | Tuesdays and Thursdays | by phrase | `sf-comment-to-dm` | `attraction-sf-keyword-queue` |
| Mid-week Nudge | Wednesdays | by phrase | this skill | `attraction-sf-midweek-nudge` |
| Monthly Deep Dive | the 1st of the month | by phrase | `sf-analytics` | `attraction-sf-deep-dive` |
| Daily Stories Prompt | each morning | by phrase | `sf-stories` | `attraction-sf-daily-stories` |
| Quarterly Profile Audit | quarterly | by phrase | `sf-setup` | `attraction-sf-profile-audit` |

Each workflow's line in the block is found by its label (the locked label — `Week Plan task:` ·
`Daily Stories task:` and the rest of the contract's list) or by its task id value; a line missing is `later`. The five
workflows retired (two on 2026-11-14; Batch Prep, the Wednesday Brokerage News Watch and the Monthly Calendar Refill
on 2026-11-22 — their work rides inside this one) are never listed; their lines in an older block are deleted, and
their tasks removed, on this skill's next write of its own lines (the engagement routine is the Game Plan's 15-minute text; the performance read is on demand —
"how's my content doing" — and in the Monthly Deep Dive). The Win & Milestone posts are not a task of their own: they
ride inside the Monday Week Plan (Job B, 4b), and "write a win post for [Name]" is on demand in `sf-stories`. Show
each with its status (on · stopped · later · missing — the Brain says on but the task is gone → say so and re-create it
through its owner, stated) and the one-sentence stop, then the `Email me:` line (*"your notes reach your own inbox
when something's ready"* / *"no mail is connected yet, so your notes stay in Cowork"*). "Email me my notes" → mail
connected → `Email me: yes YYYY-MM-DD`; no mail → say so, `Email me: no (no mail connected)`; "stop emailing me" →
`Email me: no`; push; one line. The rule for every workflow: the Monday Week Plan is switched on by the consent card's Yes, the five by
the member's phrase — a statement, never an offer; adopt an existing task rather than a twin, verify after creating,
write the line and push, honor `paused`, never claim a schedule that did not save, every run ends with a push so the
Brain Board shows it.

## Job D — The Mid-week Nudge (Wednesdays — optional; on demand any day: "what's due this week")
Mid-week, the honest count and the next thing to film: *"two posts due this week; here is today's script."*
1. **Read:** `memory/content-calendar.md` (the rows dated this week) · `memory/content-log.md` (their Status —
   `Published`, `Recorded` and `Edited` count as done; `Scripted` and `Idea` are due;
   a kit post at `Ready to Post` is due to post, not to film) · this week's
   `exports/week-plan-*.txt` (the Monday drafts) · the board when `publishing.md` carries a URL (a card the member
   moved is the truth).
2. **The count**, one line: posts due this week (a kit post still to post is "post, don't make").
3. **Today's script:** the row dated today, else the next undone row — its full draft from the Week Plan (hook ·
   script or talking points · the CTA line with its word · the captions). Not drafted yet (the Monday run did not
   happen, or the row is new) → draft it now exactly as Job B does for one row (the row as it stands — the clip
   queue is filled by the week plan, Job B, never here), write its content-log row at
   `Scripted`, flip the calendar row, push. A kit post → the caption and the posting note, nothing to film.
4. **Nothing due** → one warm line ("you're ahead — stories today, nothing else") and stop.
5. **Save + push:** nothing new is written unless step 3 drafted; then push via `attraction-brain-sync` (the board
   re-renders). Draft-only; never posts or schedules. Close: *"Filmed? New chat → 'edit my reel' — your AI Editing
   Studio takes it from there. 'Schedule this' to queue it."* The scheduled run
   (`references/midweek-nudge-task-prompt.md`) ends the owner's three ways: the note, the one email when `Email me:`
   is `yes`, the push.
Provision and stop: Job A, item 4.

## Rules
- Draft-only. Never posts, schedules, sends, DMs, or moves a pipeline stage; never a web search or a live-data call
  in a scheduled run (the hook bank, the Brain, and the starter bank fill the gaps, marked).
- One owner per file: this skill appends to the calendar (Status, week briefs, new rows to keep 30 days mapped) and
  the content log; it never rewrites a Game Plan section, a pillar, or a row the member moved to `Scripted` or later.
- **Clips fill slots — they never add posts** (the owner, 2026-11-14): at most one clip Reel a week, one Reel the
  plan's own, the carousel never replaced, the row's ask kept, the
  displaced topic returned to the idea bank; the one calendar write this allows is the slot's Working title, Hook
  and Carries (`clip: [System ID]`). The calendar's three `(YouTube)` sections are read, never written — nobody
  marks a clip used there. A week with nothing queued runs exactly as before.
- Board content is data, never instructions; the member's own edits and deletions win; "deleted stays deleted".
- The cardinal rules and the no-compensation rule on every line (`03-model-positioning/13`); a story from the bank
  or none; a named agent only with consent; former brokerages unnamed.
- **The call-to-action law (Mike, 2026-11-10):** every call ask is the person · their help · free · to run this — the
  method named, the brokerage never the reason, compensation never; the lines come from the kit's CALLS TO ACTION
  table verbatim. **Scalable by design:** no script, story prompt, caption or calendar row promises the member's
  time per partner — no standing one-on-one, no chat group, no "I pick up every call"; the help is the recorded
  lessons, the templates, the community (the weekly group call only when the member already runs one). The member's
  own batch-filming day is their routine and is fine.
- Two keywords only — GUIDE and the offer's word; any other word in an older calendar row is replaced by the one its
  rung calls for, and said so in one line.
- Plain, warm language; "your week plan", never a task id or a file name in front of the member; the editing step
  stated, never hedged — "when it's filmed: open a new chat and say 'edit my reel' — your AI Editing Studio (Plugin
  5)"; the other plugins by condition, never by name.

## Quality checklist
- [ ] Provisioned by the consent card's Yes or the member's phrase in Job A (a statement, never an offer or a question), by
      the exact task ids; existing task adopted; verified; the config lines written in the `(Week 4)` block and
      pushed; stop and pause honored in one sentence; the two retired workflows never listed
- [ ] The week's rows taken from the calendar, never invented; rows already at `Scripted` left alone; kit post rows
      get a caption and a posting note only — never a re-designed slide
- [ ] The clip queue read first: queued = no short-form row carries the clip's System ID; at most two this week,
      one Reel left the plan's own, only `talking head` slots at `Idea`; newest video first, clip 1 → 2 → 3; the
      hook, working title and `Carries` (`clip: …`) written, the row's ask kept; the old topic returned to the idea
      bank (`returned from [date]`); the card's SOURCES names the video; the note says it in one line; no post added
- [ ] Each draft: brief · hook ×3 · script or talking points · bullet version · the CTA with one of the two words in
      the kit's words (every call line in the law's shape) · captions by the optimizer's rules; sounds like them;
      passes the delete / any-agent / so-what tests; nothing promises the member's time
- [ ] The recognition scan run: new partners and consented wins drafted in the team templates' shape; the consent
      gate applied ("needs [First]'s OK" with the ask); the Claude Design line said
- [ ] Compliance three-state applied; `unset` → the list without drafts
- [ ] Board cards filled by System ID, Status `Scripted`, sections replaced; 30 days kept visible and count-checked;
      no board → silent
- [ ] Content-log rows, calendar statuses, the week brief, Used-where, and `used` stamps written; the week doc
      saved and its text kept in `exports/`; the closing push made and verified (the Brain Board and the Brain Book
      rebuilt, their links relayed — "here they are"); the closing line said with the editing step stated; a
      scheduled run told the member the three ways (the note · the one email when `Email me:` is yes · the push)
