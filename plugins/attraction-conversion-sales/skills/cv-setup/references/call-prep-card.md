# Before the Morning Call Prep card — the time and the email sentence (read, never ask)

*Read by `cv-setup` when it creates the config block (the `Email me:` value) and again at Step 5, just before the
card. The same logic the YouTube and Short-Form systems use for their one card: three facts decide the `Email me:` line and the card's email sentence; nothing is asked. The card
itself and what happens on the Yes are printed in `SKILL.md` — this file only decides the two bracketed parts.*

## The time
**7:00 am, `config.md → Timezone`.** A member who names another hour inside their Yes ("yes — make it 6:30") gets
that hour; the day never changes (it runs every morning). Nothing about the time is asked. The hour is written by
`cv-call-prep` on the `Morning Call Prep time:` line when it provisions the task.

## The email sentence — one of four, by the facts
Open `config.md` now: the `Email me:` line of the `## YouTube (Week 5)` block, then of the `## Short-Form (Week 4)`
block (an older `(Week 3)` heading is the same block). Check once whether the member's mail is connected (Gmail or
Outlook tools present in this session — `${CLAUDE_PLUGIN_ROOT}/shared/connectors.md`).

| The facts | The `Email me:` value (written by `cv-setup` at block creation, refreshed by `cv-call-prep` on the Yes) | The card's email sentence |
|---|---|---|
| an earlier block holds `yes …` and mail is connected | mirror: `yes YYYY-MM-DD` | *"I'll email you a short note, like your Monday notes."* |
| an earlier block holds `no (no mail connected)` and mail is connected now | `yes YYYY-MM-DD` (the fact in front of you wins) | *"I'll email you a short note each morning."* |
| an earlier block holds an older plain `no` (the member stopped their notes) | `no` — honoured; nothing is sent | *"Your note waits in Cowork, like your Monday notes."* |
| no earlier line, mail connected | `yes YYYY-MM-DD` | *"I'll email you a short note each morning."* |
| mail not connected (whatever an earlier line says, unless it is the plain `no`) | `no (no mail connected)` | *"Your note waits in Cowork; connect Gmail or Outlook for email."* |

A mirrored value never outranks the fact in front of you. **The base card is 59 words; the longest card is the no-mail
one, 70 words before "Say Yes"** (the mirror sentence makes 69, the plain one 67); never add a clause that takes it
past 70. The note itself, when the line says yes, is the run's own short email to the member's **own** address — ≤ 7 lines, never to anyone else (the plugin's email rule:
a workflow's note to the member is sent; every other email is a draft). Nothing is sent during the sitting.

## The calendar
Check once whether the calendar connector is present (`connectors.md`: Google Calendar, or Microsoft 365 for
Outlook). Not connected → the card is still said; on the Yes no task is created, `cv-call-prep` writes `Morning Call
Prep task: later` and states the Connect line in one sentence (its rule — `cv-setup` mirrors it), and the Step 4 win
line says it starts the morning after the calendar is connected. Never a question, never a block.
