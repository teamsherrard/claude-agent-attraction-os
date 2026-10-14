# The workflows consent card — one card, three workflows, created only on the yes

Used by `yt-setup` Step 8 (the journey's fourth step) and by the stand-alone turn-on phrases ("turn on my
attraction Monday kickoff" → `yt-briefing`; "turn on my monthly YouTube review" → `yt-triggers`; "add YouTube
to my weekly performance report" → `yt-analytics`). Every workflow here follows the OS rule every scheduled
agent follows (`docs/BRAIN-CONTRACT.md`, the Admin's setup card): offered in plain words, created only on an
explicit yes, draft-only, adopted before created (never a twin), verified after creating, its line written to
`config.md`'s `## YouTube (Week 4)` block and pushed, `declined` honored forever, stoppable in one sentence.
Never silently. Nothing any of them does sends, posts, publishes, or moves a pipeline stage.

## The card (say it once, then wait — "your turn")
> "Three scheduled notes, all read-only — nothing is sent, posted, or published on its own:
> **Your Monday Kickoff** (every Monday at 9:00 am — on by default). It reads your plan and your board, drafts
> this week's video onto its card — the brief, the start of the script or the interview guide, the thumbnail
> brief, the start of the SEO package — notes it in your Brain, and keeps your next 30 days on the board. You
> open the card and finish the video.
> **Your Friday performance note** — your Short-Form system's Friday note gets a YouTube section: videos vs
> the plan, which videos agents named this week, your interview pipeline, one packaging fix. On whenever that
> note is on.
> **Your Monthly Channel Review** (the 1st at 8:00 am — off by default). Your month by lane, which videos
> brought agent conversations, and the one move; you can run it any time by asking.
> Keep the defaults — Kickoff on, YouTube in the Friday note, the monthly review off — or tell me which to
> change and the times. Different times are fine; the Kickoff can land as a draft email instead of a note.
> **Your turn.**"

Defaults on "yes" / "defaults" / "keep it": Monday Kickoff ON at 9:00 am Mondays · Friday section ON (when the
Friday note exists) · Monthly review OFF (offered, not declined). A demo Brain never gets a task. The member
hears "your Monday Kickoff", "your Friday note", "your monthly review" — never a task id or a skill name.

## Provisioning, in order (each: adopt → create → verify → record → push)
1. **Monday Kickoff** (owner `yt-briefing`) — `list_scheduled_tasks` first; a task with id
   `attraction-monday-kickoff` exists → adopt it (write its id; never a twin). Else `create_scheduled_task`
   with `taskId: attraction-monday-kickoff`, `cronExpression: 0 9 * * 1` (the hour from their answer, in their
   local time from `config.md → Timezone`, no timezone math), the `prompt` set **verbatim** from
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-briefing/references/weekly-task-prompt.md`. Verify with
   `list_scheduled_tasks` (present, enabled, a `nextRunAt`) — not there → say so plainly; never claim a schedule
   that did not save. Write `Monday Kickoff task: attraction-monday-kickoff · runs Mondays [time]` and, if
   chosen, `Monday Kickoff delivery: email draft`. "Not yet" → `Monday Kickoff task: declined`; it still runs
   on demand ("run my attraction kickoff").
2. **The Friday section** (the task is owned by the Short-Form System's `sf-analytics`; this plugin only
   appends, never creates) — read the `Weekly Content Performance task:` line in `config.md`'s
   `## Short-Form (Week 3)` block (the locked key; it lives there, never on `publishing.md`).
   **A task id** → `update_scheduled_task` on that id, appending the block in
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-analytics/references/friday-youtube-section.md` verbatim into the prompt's
   `YouTube section` slot the Short-Form System left; verify with `list_scheduled_tasks`; write
   `YouTube section: added YYYY-MM-DD`.
   **`not offered yet`, no line, or no Short-Form block** → nothing to append to yet: write
   `YouTube section: pending — the Friday note is not on yet` and say in one line: *"your Friday note isn't
   switched on yet — when you say 'set up my Friday performance note' it switches on, and the next time we talk
   I add YouTube to it."* (Every launch of this plugin — `yt-setup`'s READY BRIEF, `yt-triggers`' registry,
   `yt-analytics` — re-reads the line and appends the moment the Friday task exists.)
   **`declined`** → the member said no to the Friday note: write `YouTube section: declined`; offer nothing more.
   **Never create a second task.**
3. **Monthly Channel Review** (owner `yt-triggers`) — on "yes, turn it on": `list_scheduled_tasks` first (adopt
   `attraction-monthly-youtube-review` if it exists); else `create_scheduled_task` with `taskId:
   attraction-monthly-youtube-review`, `cronExpression: 0 8 1 * *` (the day and hour from their answer, local
   time), the `prompt` set **verbatim** from
   `${CLAUDE_PLUGIN_ROOT}/skills/yt-triggers/references/monthly-review-task-prompt.md`; verify; write
   `Monthly review task: attraction-monthly-youtube-review · runs the 1st [time]`. Left off (the default) →
   `Monthly review task: off (offered YYYY-MM-DD)` — it runs on demand any time ("run my monthly YouTube
   review") and switches on later with "turn on my monthly YouTube review". "Never" → `declined`.
Then push via `attraction-brain-sync` and verify — a crash between creating a task and writing its id is how
duplicate tasks are born. Confirm once, plainly: *"Done — your Monday Kickoff is on; the first one lands Monday
at 9. [YouTube joins your Friday note / I'll add YouTube to your Friday note once it's on.] Say 'stop my
attraction kickoff' any time, and 'turn on my monthly YouTube review' whenever you want the monthly one."*

## The `## YouTube (Week 4)` block (locked spelling — `shared/brain-contract.md`)
`Installed:` · `Plugin version:` · `Layer: identity/channel.md` ·
`Monday Kickoff task:` (`not offered yet` → `attraction-monday-kickoff · runs Mondays [time]` · `declined` · `paused`) ·
`Monthly review task:` (`not offered yet` → `attraction-monthly-youtube-review · runs the 1st [time]` · `off (offered YYYY-MM-DD)` · `declined`) ·
`YouTube section:` (`not offered yet` → `added YYYY-MM-DD` · `pending — the Friday note is not on yet` · `declined`) ·
optional `Monday Kickoff delivery: email draft`. Nothing else, ever. (`Weekly ideas task` was retired on
2026-10-13 — nothing provisions it; the Monday Kickoff carries this week's video and the ideas.)

## Stop · pause · change (one sentence each; never a second task)
- "stop my attraction kickoff" → `delete_scheduled_task` on the saved id, write `declined`, push.
- "pause my Monday kickoff" → disable it, write `paused`, push. "change my kickoff time" → `update_scheduled_task`,
  re-verify, update the line, push.
- "stop my monthly YouTube review" → delete, write `declined`, push (through `yt-triggers`).
- Removing the Friday section → `update_scheduled_task` on the Short-Form task (the same path in reverse) and
  `YouTube section: declined`.
Never claim a stop, a pause, or an update that did not save.
