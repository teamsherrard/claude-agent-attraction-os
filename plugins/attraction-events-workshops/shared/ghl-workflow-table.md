# The workflow table — Trigger → Action → Outcome (how every event automation is documented)

*From Mike's workshop-ops skill: "every workflow documented as Trigger → Action → Outcome." This plugin never
builds a workflow in GoHighLevel (or Follow Up Boss, a list tool, Zoom, or a page host). It writes the table;
the member — or the VA or leader they hand it to — builds it. Read by `ev-registration`, `ev-followup`,
`ev-evergreen`, `ev-virtual`, and `ev-live` at the step that documents an automation. The delegation principle
applies: anyone who wasn't in the room should be able to build the workflow from the table alone.*

## The shape (one table per sequence; one row per step)
```
| # | Trigger | Filter / condition | Action | Outcome | Owner |
|---|---|---|---|---|---|
| 1 | Form submitted (registration) | tag = [code]-[yyyy-mm]-registered | send confirmation email + text; add to calendar invite; add to list | registrant confirmed and on the list | VA |
| 2 | 24 hours before start | tag = registered | send reminder email + text | reminder delivered | VA |
| 3 | 1 hour before start | tag = registered | send text with the link | link in hand | VA |
| 4 | Attendance report imported (day 1, 9:00) | attended = yes | remove registered, add [code]-[yyyy-mm]-attended; start the attended sequence | attended sequence running | member |
| 5 | Attendance report imported (day 1, 9:00) | attended = no | add [code]-[yyyy-mm]-no-show; start the no-show sequence | no-show sequence running | member |
| 6 | Replied, asked a question, or booked | any | add [code]-[yyyy-mm]-engaged (or -booked); stop the group sequence for them; notify the member | hand-written touch instead of the automation | member |
| 7 | Day 7 sequence complete | no reply, no booking | add to the weekly newsletter list; remove from the event sequence | on the list for good | VA |
```
Columns are fixed. `Trigger` is an event the tool can see (a form, a date, an import, a reply, a tag change).
`Filter / condition` is a tag or a field, in the member's tag convention (`events-doctrine.md` §14 — never a tag
without a stage). `Action` is what the tool does (send · tag · move · notify · add to list). `Outcome` is the
state the person is in afterwards, in plain words. `Owner` is who builds and checks it (member · VA · a leader).

## Rules
- **One automation per row; one sequence per table.** Registration (confirmation + reminders) · attended ·
  no-show · engaged/hot (the hand-off to a human) · cold (to the list) · evergreen (registered → watched → booked).
- **Every message an action sends is a draft the plugin already wrote**, named by its title in the follow-up or
  registration doc — the table references copy, it never contains it.
- **Humans on the hot path.** Any reply, question, or booking removes the person from the group automation and
  puts a hand-written touch in the member's hands (the Daily Follow-Up Queue drafts it once the AI Admin is
  installed; the member sends it). The automation never pitches, never adds a "last chance," never escalates.
- **Stop conditions are explicit.** Every sequence ends: on a reply, on a booking, or at day 7 into the newsletter.
  Nothing loops; nothing runs past the replay window.
- **Tags, not stages.** The table moves CRM tags. Pipeline stages in the Brain move only through the locked
  request shapes in `brain-contract.md`, by the AI Admin, for named agents.
- **Compliance inside the automation.** Every email the table sends carries the compliance footer the
  registration doc specifies; no income language anywhere; the Meta Employment note if any step is an ad.
- **A test row.** The last row of every table is `Test | the member submits the form themselves | every step fires
  in order; the test contact is deleted after | verified YYYY-MM-DD | member`. An untested workflow is not built.
- **Tool-agnostic.** GoHighLevel is Mike's tool (`15-advanced-scaling/76`); the same table builds in Follow Up
  Boss, a list tool's automations, or a Zoom + spreadsheet hand process. The `Action` column names the tool's own
  words where the member told us the tool (`config.md → CRM`, the Lead Magnet block's `List tool`, the Events
  block's `Registration host`).
