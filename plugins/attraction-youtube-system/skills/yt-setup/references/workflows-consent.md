# The one card — two workflows and the email note, switched on with the card's Yes

`yt-setup` Step 8 (the journey's fourth step) says this card ONCE and the member answers "Yes". The same card is said
by `yt-briefing` (Step 5) and `yt-triggers` (Job 1) on an older install whose block holds no task lines yet — this file
is the one place the card lives; nobody paraphrases it. Every workflow here follows the OS rule every scheduled task
obeys (the Brain's `how-we-speak.md` and the Admin's precedent): **told, not asked** (the owner, 2026-11-14 evening —
members follow the program; the card is one statement of what is switched on, closed by "Say Yes"; never "all, some,
or not yet", never "want me to email you?", never a choice between defaults, never a menu of extras), **created only
on the explicit Yes**, draft-only, adopted before created, verified after, recorded in the Brain, stoppable in one
sentence. To the member: "your Monday Kickoff", "your Monthly Channel Review", "a short note to your inbox" — never a
task id, a skill name or a file path.

## Before the card (read, never ask)
Open `~/attraction-brain/config.md` now: `Timezone`; the `## YouTube (Week 5)` block (an older `## YouTube (Week 4)`
heading is the same block — rename it on this write); the `## Short-Form (Week 4)` block's `Email me:` line (an older
`(Week 3)` heading is the same block, read as such and never renamed here). Check once whether the member's mail is
connected (Gmail or Outlook tools present in this session). Three facts decide the card's email sentence and the
`Email me:` line — nothing is asked:
- the Short-Form block holds an `Email me:` line → **mirror it** into the YouTube block, and let the card's email
  sentence follow the value: `yes …` → the YouTube notes come the same way the short-form notes do;
  `no (no mail connected)` → the no-mail sentence below; an older plain `no` (the member stopped their notes
  there) is honoured — *"Your notes wait for you in Cowork and on your Brain Board, the same way your short-form
  notes do."* — and no email is sent on it. A mirrored value never outranks the fact in front of you: mail not
  connected in this session → `no (no mail connected)`; mail connected and the Short-Form line still reads
  `no (no mail connected)` → `yes YYYY-MM-DD`;
- no Short-Form line, mail connected → `Email me: yes YYYY-MM-DD`;
- no Short-Form line, no mail connected → `Email me: no (no mail connected)`; the card's email sentence becomes one
  plain line: *"Your notes wait in Cowork and on your Brain Board — connect Gmail or Outlook to get them by email."*
The times are Mondays 9:00 am and the 1st at 8:00 am, the member's local time (`config.md → Timezone`). A member who
names another hour inside their Yes ("yes — Mondays at 7") gets that hour; the day never changes (the Kickoff is
Mondays, the review the 1st — a member who names another day gets the hour and one line: *"It runs Mondays — I've
set it for 7."*); nothing about the times is asked.

## The card (said once — its own message, at most 70 words before "Say Yes")
**The card is its own short message** (the owner's review, 2026-11-14): nothing else is in that message — no
announce line above it, no recap, no housekeeping — and nothing follows "Say Yes and I'll set them up." Inside
setup it is the last thing in the turn, sent once the board step's work has finished. Plain words only ("your month
by topic" — never "month by lane", never "the hook", never "SEO"). This shape; the member's own times fill it:
> "Here's what I'm switching on for you. **Your Monday Kickoff** — Mondays at 9:00 am: this week's video, drafted
> on its card. **Your Monthly Channel Review** — the 1st at 8:00 am: your month by topic and the one move. Both only
> draft; nothing posts or publishes on its own. [the email sentence] Say **Yes** and I'll set them up."
**The email sentence — one of four, by the facts above:**
- mail connected, no Short-Form line → *"I'll email you a short note when each is ready."*
- the Short-Form block's line is `yes …` → *"I'll email you a short note when each is ready, the same way your
  short-form notes come."*
- no mail connected → *"Your notes wait in Cowork and on your Brain Board — connect Gmail or Outlook to get them by
  email."*
- an older plain `no` mirrored from the Short-Form block → *"Your notes wait for you in Cowork and on your Brain
  Board, the same way your short-form notes do."*
The longest version is 67 words before "Say Yes"; never add a clause that takes the card past 70.

Wait for the Yes — the one reply this card needs, and the explicit yes every scheduled workflow needs. Nothing is
created before it. **Anything but a Yes:** a question about the card → one plain answer, then only the card's last
line again ("Say Yes and I'll set them up."); "not now" or a no → nothing is created, both task lines are written
`later`, one line — *"Nothing's switched on. Say 'turn on my attraction Monday kickoff' or 'turn on my monthly
YouTube review' any time."* — and whatever was running carries on (inside setup: straight to the first video); the
card is never said a second time. **A demo Brain never gets a task:** the card is said and the Yes noted, no task is
made, both lines stay `later`, and in place of the confirming line below say one line — *"This is a demo, so nothing
is scheduled — on a real Brain your Monday Kickoff and your Monthly Channel Review start here."* — and nothing after
it, anywhere in the sitting, says that something runs on Mondays or on the 1st.

## On the Yes — provision both, in this order, then push once
1. **Monday Kickoff** — `list_scheduled_tasks`; adopt `attraction-monday-kickoff` if it exists (never a twin), else
   `create_scheduled_task` with `taskId: attraction-monday-kickoff`, `title: Your Monday Kickoff` (the name the
   member sees in their Scheduled list), `description: Drafts this week's YouTube video onto its card every Monday
   — draft only, nothing is published.` (the tool requires one), `cronExpression: 0 9 * * 1` (or the member's
   hour), local time, the prompt **verbatim** from
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-briefing/references/weekly-task-prompt.md`. Verify (present, enabled, a
   `nextRunAt`). Write `Monday Kickoff task: attraction-monday-kickoff · runs Mondays [time]`.
2. **Monthly Channel Review** — the same: adopt `attraction-monthly-youtube-review`, else `create_scheduled_task` with
   that `taskId`, `title: Your Monthly Channel Review`, `description: Reads last month's YouTube work against your
   plan on the 1st and names the one move — draft only.`, `cronExpression: 0 8 1 * *` (or the member's hour), the
   prompt **verbatim** from
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-triggers/references/monthly-review-task-prompt.md`. Verify. Write `Monthly review
   task: attraction-monthly-youtube-review · runs the 1st [time]`.
3. **`Email me:`** — the value decided above, written now (mirrored, `yes YYYY-MM-DD`, or `no (no mail connected)`).
   Nothing is sent during setup; the Kickoff and the Review each send ONE short email per run to the member's own
   address while the line says yes.
4. Push via `attraction-brain-sync` (the push rebuilds the Brain Board) and confirm in one line (never on a demo
   Brain — no task was made): *"Set. Mondays your
   week's video is drafted onto its card; the 1st, your channel review lands[; a short note comes to your inbox each
   time]. Say 'stop my attraction kickoff' or 'stop my monthly YouTube review' any time."*
A task that failed to save is named in one line and its line reads `later` — never a schedule that did not save;
its phrase ("turn on my attraction Monday kickoff" · "turn on my monthly YouTube review") retries it.

## The config block — locked spelling, this order
`config.md → ## YouTube (Week 5)`: `Installed:` · `Plugin version:` · `Layer: identity/channel.md` · `Monday Kickoff
task:` · `Monthly review task:` · `Email me:`. **A task line holds exactly one of three values** (the same vocabulary
as the Short-Form block): a task id — the workflow is on (`attraction-monday-kickoff · runs Mondays [time]` ·
`attraction-monthly-youtube-review · runs the 1st [time]`) · `paused` — the member stopped it; its phrase brings it
back · `later` — not switched on yet (the card did not get its Yes, or the task did not save). A reader treats any
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
- "Stop my monthly YouTube review" → the same path → `Monthly review task: paused`; "turn on my monthly YouTube review"
  switches it on from `paused` or `later`. "Run my monthly YouTube review" runs it in chat any time, task or no task.
- "Change my kickoff time" → `update_scheduled_task` on the saved id with the new cron, re-verify, write the new time
  on the line, push.
- `Email me:` is never a question and never a switch the card offers: it mirrors the Short-Form block when that block
  holds a line, else it follows the connected mail. A run that finds no connected mail at send time writes
  `no (no mail connected)` and says so once; a run that finds mail connected again writes `yes YYYY-MM-DD` — unless
  the Short-Form block's line is an older plain `no`, which is honoured.
