# The one card — ONE workflow (the Monday Kickoff, the month's review inside it) and the email note, switched on with the card's Yes

`yt-setup` Step 8 (the journey's fourth step) says this card ONCE and the member answers "Yes". The same card is said
by `yt-briefing` (Step 5) and `yt-triggers` (Job 1) on an older install whose block holds no task lines yet — this file
is the one place the card lives; nobody paraphrases it. Every workflow here follows the OS rule every scheduled task
obeys (the Brain's `how-we-speak.md` and the Admin's precedent): **told, not asked** (the owner, 2026-11-14 evening —
members follow the program; the card is one statement of what is switched on, closed by "Say Yes"; never "all, some,
or not yet", never "want me to email you?", never a choice between defaults, never a menu of extras), **created only
on the explicit Yes**, draft-only, adopted before created, verified after, recorded in the Brain, stoppable in one
sentence. **Mike, 2026-11-22: "one scheduled task a week."** The Monthly Channel Review is no longer its own task: it runs inside
the Kickoff on the first Monday of each month (the Kickoff prompt's step 5b), and on demand ("run my monthly channel
review"). **Mike, 2026-11-23: the Kickoff drafts ONE video a week IN FULL** — the bullet breakdown with the hook
scripted word for word AND the full teleprompter script (8 to 12 minutes) in one package; an interview week is the
question list, no script; no reference video and no competitor summary in anything it leaves. "Drafted" on the card
below means that. To the member: "your Monday Kickoff", "your month reviewed", "a short note to your inbox" — never
a task id, a skill name or a file path.

## Before the card (read, never ask)
Open `~/attraction-brain/config.md` now: `Timezone`; the `## YouTube (Week 5)` block (an older `## YouTube (Week 4)`
heading is the same block — rename it on this write); the `## Short-Form (Week 4)` block's `Email me:` line (an older
`(Week 3)` heading is the same block, read as such and never renamed here). Check once whether the member's mail is
connected (Gmail or Outlook tools present in this session) — inside setup that check was made at Step 5, when the
`Email me:` line was first written: read the line. Three facts decide the card's email sentence and the
`Email me:` line — nothing is asked:
- the Short-Form block holds an `Email me:` line → **mirror it** into the YouTube block, and let the card's email
  sentence follow the value: `yes …` → the YouTube notes come the same way the short-form notes do;
  `no (no mail connected)` → the no-mail sentence below; an older plain `no` (the member stopped their notes
  there) is honoured — the fourth sentence below — and no email is sent on it. A mirrored value never outranks the fact in front of you: mail not
  connected in this session → `no (no mail connected)`; mail connected and the Short-Form line still reads
  `no (no mail connected)` → `yes YYYY-MM-DD`;
- no Short-Form line, mail connected → `Email me: yes YYYY-MM-DD`;
- no Short-Form line, no mail connected → `Email me: no (no mail connected)`; the card takes the no-mail sentence below.
The time is Mondays 9:00 am, the member's local time (`config.md → Timezone`). A member who
names another hour inside their Yes ("yes — Mondays at 7") gets that hour; the day never changes (the Kickoff is
Mondays, the review the 1st — a member who names another day gets the hour and one line: *"It runs Mondays — I've
set it for 7."*); nothing about the times is asked.

## The card (said once — its own message, at most 70 words before "Say Yes")
**The card is its own short message** (the owner's review, 2026-11-14): nothing else is in that message — no
announce line, no recap, no housekeeping; inside setup ONE line stands above it, the win line for the board step
the member just finished, by what is true (the board was built → *"✓ Step 3 of 5 — done. You approved your plan,
and your next 30 days are on your content board."* · the board is waiting on Notion, or an older `declined` skipped it →
*"✓ Step 3 of 5 — done. You approved your plan — your next 30 days are mapped in it."* — nothing about Notion here: it was said
once, at the board step) — and nothing follows "Say
Yes and I'll set it up." Inside
setup it is its own reply, sent only after the member's Yes at the board step's stop — never in the same reply as
the board. Plain words only (never "month by lane", never "the hook", never "SEO"; the review is said as what it
does — "last month's videos reviewed, and your one next step"). This shape; the member's own times fill it:
> "Here's what I'm switching on for you. **Your Monday Kickoff** — Mondays at 9:00 am: this week's video, drafted
> [on its card | for you]; on the first Monday of each month, last month's videos reviewed and your one next step.
> It only drafts; nothing posts or publishes on its own. [the email sentence] Say **Yes** and I'll set it up."
(A member at two videos a week — the pace they chose — hears "videos" and "their cards" wherever the card or the
confirming line says "video" and "its card".)
**The email sentence — one of four, by the facts above:**
- mail connected, no Short-Form line → *"I'll email you a short note when it's ready."*
- the Short-Form block's line is `yes …` → *"I'll email you a short note when it's ready, the same way your
  short-form notes come."*
- no mail connected → *"It leaves a short note in Cowork and on your Brain Board — connect Gmail or Outlook to
  get it by email."*
- an older plain `no` mirrored from the Short-Form block → *"It leaves a short note in Cowork and on your Brain
  Board, the same way your short-form notes do."*
The longest version (no mail connected) is 70 words before "Say Yes"; never add a clause that takes the card past 70.

Wait for the Yes — the one reply this card needs, and the explicit yes every scheduled workflow needs. Nothing is
created before it. Never a menu, never created without a Yes. **Anything but a Yes:** a question
about the card → one plain answer ("What's a workflow?" → the line `yt-setup` prints under "If the member asks"),
then only the card's last line again ("Say Yes and I'll set it up."); "not now" or a no → nothing is created,
`Monday Kickoff task:` is written `later` (`Monthly review task:` stays `inside kickoff` — the review rides inside the
Kickoff whenever that is on), one line — *"Nothing's switched on. Say 'turn on my attraction Monday kickoff' any
time."* — and whatever was running carries on (inside setup:
straight to the first video); the card is never said a second time. **A demo Brain never gets a task:** the card
is said and the Yes noted, no task is made, the Kickoff line stays `later`, and in place of the confirming line below
say one line — *"This is a demo Brain, so nothing is scheduled — on a real Brain that Yes switches on your Monday
Kickoff."* — and nothing after it, anywhere in the sitting, says that something
runs on Mondays or on the 1st. (Inside setup each of these lines is said once, as the line that opens the close —
`yt-setup` Step 9, item 0.)

## On the Yes — provision the ONE task, then push once
1. **Monday Kickoff** — `list_scheduled_tasks`; adopt `attraction-monday-kickoff` if it exists (never a twin), else
   `create_scheduled_task` with `taskId: attraction-monday-kickoff`, `title: Your Monday Kickoff` (the name the
   member sees in their Scheduled list), `description: Drafts this week's YouTube video in full every Monday, and
   reviews the month on the first Monday — draft only, nothing is published.` (the tool requires one), `cronExpression: 0 9
   * * 1` (or the member's hour), local time, the prompt **verbatim** from
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-briefing/references/weekly-task-prompt.md`. Verify (present, enabled, a
   `nextRunAt`). Write `Monday Kickoff task: attraction-monday-kickoff · runs Mondays [time]`.
2. **The month's review rides inside it** — write `Monthly review task: inside kickoff` (keep `paused` if the member
   had stopped the review); an older `attraction-monthly-youtube-review` task exists → delete it, say nothing.
3. **`Email me:`** — the value decided above, written now (mirrored, `yes YYYY-MM-DD`, or `no (no mail connected)`).
   Nothing is sent during setup; the Kickoff sends ONE short email per run to the member's own address while the
   line says yes (a send that cannot complete is never retried: the run writes `Email me: no (no mail connected)`
   and goes on to its note).
4. Push via `attraction-brain-sync` (the push rebuilds the Brain Board) and confirm in one line (never on a demo
   Brain — no task was made): *"Set. Mondays your week's video is drafted [onto its card | for you] — and it keeps
   your board 30 days ahead; on the first Monday of the month, your month reviewed too[; a short note comes to your
   inbox each time]. Say 'stop my attraction kickoff' any time."* ("onto its card" and the 30-days clause only when
   a board exists. **Inside setup this line is said ONCE — as the win line that opens the close**, with its last
   sentence, never here and there both.)
A task that failed to save is named in one line and its line reads `later` — never a schedule that did not save;
its phrase ("turn on my attraction Monday kickoff") retries it.

## The config block — locked spelling, this order
`config.md → ## YouTube (Week 5)`: `Installed:` · `Plugin version:` · `Layer: identity/channel.md` · `Monday Kickoff
task:` · `Monthly review task:` · `Email me:`. **A task line holds exactly one of three values** (the same vocabulary
as the Short-Form block): a task id — the workflow is on (`attraction-monday-kickoff · runs Mondays [time]`) · `paused` — the member
stopped it; its phrase brings it back · `later` — not switched on yet (the card did not get its Yes, or the task did
not save). **`Monthly review task:` is the exception since 2026-11-22:** it holds `inside kickoff` (the review runs
in the Kickoff's first-Monday run) or `paused` (the member stopped the review alone); an older task id there means
an older Brain — delete that task and write `inside kickoff` on the next write. A reader treats any
value that is not a task id as not on, so an older file's placeholder still reads correctly; a writer normalizes
such a value to `later` on its next write. `Email me:` is `yes YYYY-MM-DD` · `no (no mail connected)` (an older plain
`no` mirrored from the Short-Form block is honoured). Nothing else, ever; no brackets in the block (the Brain Board
reads a task line as `<Label> task: <task id> …`). Any line beyond the six locked ones that an older block carries
(the two retired on 2026-11-14 included) is dropped on the next write, and an older `## YouTube (Week 4)` heading is
renamed on the same write.

## Stop · pause · change (by the owning skill — never a second task)
- "Stop my attraction kickoff" / "pause my Monday kickoff" → disable the task (`update_scheduled_task`, or delete it),
  re-verify, write `Monday Kickoff task: paused`, push, one line. "Turn on my attraction Monday kickoff" switches it
  on from `paused` or `later` (the phrase is the member's explicit yes): adopt or create, verify, write the task id
  line, push.
- "Stop my monthly channel review" → `Monthly review task: paused` (the Kickoff skips the first-Monday review),
  push, one line; "turn on my monthly channel review" → `inside kickoff`, one line (*"Your month's review runs
  inside your Monday Kickoff on the first Monday — back on."*). Never a task of its own. "Run my monthly channel
  review" runs it in chat any time.
- "Change my kickoff time" → `update_scheduled_task` on the saved id with the new cron, re-verify, write the new time
  on the line, push.
- `Email me:` is never a question and never a switch the card offers: it mirrors the Short-Form block when that block
  holds a line, else it follows the connected mail. A run that finds no connected mail at send time writes
  `no (no mail connected)` and says so once; a run that finds mail connected again writes `yes YYYY-MM-DD` — unless
  the Short-Form block's line is an older plain `no`, which is honoured.
