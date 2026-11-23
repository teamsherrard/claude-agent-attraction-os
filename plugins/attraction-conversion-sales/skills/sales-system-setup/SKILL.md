---
name: sales-system-setup
description: >
  Sales OPS, step one: sets up the Partner Call machine behind 10+ calls a day. The booking calendar
  (Calendly or GoHighLevel), the mandatory application-form questions from Mike's own booking flow, the
  "no" rule, the CRM tags and the locked pipeline stages mapped into GoHighLevel, Follow Up Boss, or
  Google Sheets, and the reminder schedule. Reads the CRM, hours, and booking link already in the Brain;
  asks only what it cannot know; writes identity/sales-system.md and renders the Sales System doc. Member
  configures the tools; nothing is created in a third-party system on their behalf. Trigger on: "set up
  my sales system", "set up my partner call calendar", "my application form questions", "map my pipeline
  stages to my CRM", "sales system setup", "set up my booking calendar for agents", "attraction CRM
  tags", "partner call setup", "sales ops setup".
---

# Sales System Setup — the calendar, the form, the tags, the stages, the reminders

Mike's booking flow is "unbelievably important… the questions you ask will save you an enormous amount of
time, frustration, and headache from the wrong people booking in" (`bonus/calendly`). This skill turns that
into the member's own system: one calendar event, five required questions, one rule for a "no", the locked
stages in whatever CRM they use, and a reminder schedule — written down once in the Brain so every other
Sales OPS skill and the AI Admin read the same setup.

**Write-and-prepare.** This skill writes the Brain and a document; it never creates events, forms, tags,
or fields inside Calendly, GoHighLevel, Follow Up Boss, or Sheets. It hands the member exact settings.

## Step 0 — How we speak, and ask once
Read `${CLAUDE_PLUGIN_ROOT}/shared/how-we-speak.md`, `${CLAUDE_PLUGIN_ROOT}/shared/ask-once-default.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md`. Three stops at most, 2–4 questions each, defaults on
"you decide", every stop ends "your turn". ~10 minutes.

## Step 1 — Load the Brain (never ask what it knows)
Read `~/attraction-brain/brain.md`, then `identity/operations.md` (**CRM**, booking link, working hours,
call block, call length, where, the 3-way partner, the follow-up cadence), `config.md` (`CRM`, `Timezone`,
the Conversion & Sales block if present), `identity/goals.md` (calls per week), `identity/profile.md`
(brokerage, organization name), `identity/positioning.md` (the one line for the event description),
`identity/compliance.md` (brokerage name as it must appear; the form is public — three-state on its first line,
`Status:`: **unset** → stop before Stop 2 and say "set up my attraction compliance", three minutes; **set** →
apply and remind once; **confirmed** → apply). If `identity/
sales-system.md` already exists, this is an update: show the READY BRIEF of what is set and change only
what they ask. Missing locally → pull via `attraction-brain-sync`. A tool error is never "no Brain".
Read `${CLAUDE_PLUGIN_ROOT}/shared/conversion-doctrine.md` only if the sequence-of-events detail is needed.

## Mike's doctrine for this system (`10-presentation-delivery/42`, `bonus/calendly`)
- **One event, one link, everywhere** — link in bio, YouTube descriptions, email signature.
- **Call length:** one hour "until you master the craft", then 30 minutes "and see if you can maintain your
  conversion rate". Zoom connected so the link lands in the invite; time zones auto-detected.
- **The five questions, all required** (the order matters — the first one is the filter):
  1. *"Do you acknowledge this is a discussion about joining my group at [Brokerage]? Please do not book if
     you are already at [Brokerage] or have already chosen a sponsor."* — yes / no.
  2. *"Which brokerage are you currently with?"* — one line.
  3. *"Where are you located?"* — one line.
  4. *"Are you currently a new agent, an experienced agent, a team leader, or a broker-owner?"* — multiple
     lines, "this sometimes requires context".
  5. *"Please share any information that will help me prepare for this meeting, including why you're
     interested."* — multiple lines; "people write novels", which is the whole point.
  Guests allowed (a team leader brings a partner, a couple books together).
- **The "no" rule:** a "no" on question 1 → delete the meeting and send the one-line note ("you said no to
  this — it's a requirement"). It protects the member's time; it is never rude.
- **Reminders:** 24 hours, 1 hour, 10 minutes (Mike used the templates; "if I were doing it today I'd
  personalize them" — `sales-show-up` writes those).
- **Availability:** as flexible as possible — "convenient for them, not you" — inside the member's real
  life (no evenings if that is family time). Mike's window was 10–2, eight 30-minute calls; the member's is
  set by `sales-call-block`.
- **After the call:** the recap email to everyone, the steps email to a yes, the welcome email on join, the
  strategy call booked in week one (`cv-debrief`, `cv-follow-up`, the Brain's operations file).

## Stop 1 · The calendar (2–3 questions)
Orient: *"First, the calendar. Three quick questions."* Propose from the Brain and let them confirm:
1. **Tool** — Calendly or GoHighLevel's calendar (or what `operations.md` already names). If unsure: Calendly
   when they have no CRM or use Follow Up Boss / Sheets; GHL's calendar when GHL is their CRM. Say why.
2. **Call length** — 60 minutes for the first 30 calls, then 30 (`${CLAUDE_PLUGIN_ROOT}/shared/
   conversion-doctrine.md` §3, DECISION NEEDED 2); propose from how many partner calls they have run
   (`memory/pipeline.md` counts; `profile.md`).
3. **Event name and description** — propose: *"[Organization] Partner Call — 30 min · one-on-one on Zoom with
   [Name]"* and a two-line description from `positioning.md` ("let me show you how we help [type of agent]
   [outcome]"). No superlatives without a dated source in `proof.md`.
**Your turn.**

## Stop 2 · The form and the "no" rule (2 questions)
Show the five questions with the member's brokerage and name filled in from `compliance.md` (the exact
brokerage name as it must appear). Ask: anything to add (one optional sixth question at most — "how did you
find me?" is the one worth adding, it feeds the by-source scorecard), and confirm the "no" rule in their
words. **Your turn.**

## Stop 3 · CRM, tags, stages, reminders (2–3 questions)
Read the CRM from `operations.md` (mirror `config.md → CRM`). Supported paths: **GoHighLevel**, **Follow Up
Boss**, **Google Sheets** (and "none → Sheets"). Propose the mapping and let them confirm:
- **Stage field, values verbatim (locked, OS-wide):** Identified · Conversation · Call booked · Call held ·
  3-way · Joined · Onboarded · Active · Parked. GHL → a pipeline with these stages; FUB → a custom field
  or stage tags with these exact names; Sheets → one column with these values (the sheet's columns mirror
  the Top-50's: Name · Type · Where · Source · Stage · Last touch · Next move · Due · Notes).
- **Tags:** `prospect-agent` · the type (one of the six: new agent · experienced low production · top
  producer · agent with a brand · team leader · broker-owner) · the source (youtube · instagram ·
  referral · sphere · event · lead-magnet · other) · `partner` on join. Never a tag that is a protected
  characteristic.
- **Reminders:** 24h · 1h · 10 min on; personalized copy from `sales-show-up`.
- **Who sees the bookings:** the member; a VA or setter if `config.md → Workspace shared with` names one
  (`sales-setter` writes their rules).
**Your turn.**

## Write `identity/sales-system.md` (the locked shape — every section, no brackets left)
```
# [Name] — Sales System
*identity · the Partner Call machine · owner: sales-system-setup (Conversion & Sales) · Status: set [YYYY-MM-DD]*
*Read by: sales-booking-page · sales-show-up · sales-setter · sales-call-block · sales-scorecard · cv-call-prep · the AI Admin. Booking link and call block mirror identity/operations.md.*

## Calendar
Tool: [Calendly | GoHighLevel | other] · Event: [name] · Length: [60 | 30] min · Where: [Zoom | Meet | Teams] · Link: [mirrors operations.md]
Window: [set by sales-call-block — "not set yet" until it runs] · Time zones: auto-detect on

## Application form (required, this order)
1. [the acknowledge question, brokerage named] — yes/no
2. Which brokerage are you currently with? — one line
3. Where are you located? — one line
4. New agent, experienced agent, team leader, or broker-owner? — multi-line
5. What will help me prepare, and why are you interested? — multi-line
[6. optional: How did you find me? — one line]
Guests: allowed

## The "no" rule
A "no" on question 1 → delete the meeting; send: "[one-line note in the member's voice]".

## CRM
System: [GoHighLevel | Follow Up Boss | Google Sheets] · Stage field values: Identified · Conversation · Call booked · Call held · 3-way · Joined · Onboarded · Active · Parked
Tags: prospect-agent · [type tags] · [source tags] · partner
Sheet columns (if Sheets): Name · Type · Where · Source · Stage · Last touch · Next move · Due · Notes

## Reminders
24h · 1h · 10 min — copy in the Show-Up Sequence doc (sales-show-up)

## Hand-offs
Booked call → cv-call-prep (Call Block Prep agent) · after the call → cv-debrief · yes → steps email · join → welcome + strategy call (operations.md onboarding)
```
Then register the plugin's block in `config.md` under **Later plugins register here** if it is absent — the
locked spelling from `${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`, and seed the three keys this skill owns
(`Booking page` · `Partner call length` · `Setter: none` until `sales-setter` names one):
```
## Conversion & Sales
- **Call Block Prep task:** [task id | declined | later]        (cv-call-prep writes this)
- **Call Block Prep time:** [default 7:00 am, member timezone]   (cv-call-prep writes this)
- **Cold-Lead Reactivation task:** [task id | declined | later]  (cv-reactivation writes this)
- **Booking page:** [URL from operations.md | not yet]
- **Partner call length:** [60 | 30]
- **Setter:** [none | name]
```
Never touch another plugin's block or a registry key; never overwrite a task key another skill has set. If `operations.md` has no booking link and the member
gave one now, say *"I'll note the link in your operations as well"* and hand it to `attraction-operations`
(its file; this skill never writes it).

## Render the Sales System doc (the deliverable they hold)
Structured text per `${CLAUDE_PLUGIN_ROOT}/shared/doc-formatting.md` (read it now): the event settings as a
table, the five questions as a numbered list ready to paste, the "no" note, the CRM mapping table, the tag
list, the reminder schedule, a one-page "set this up in 20 minutes" checklist for their tool (Calendly: event
→ invitee questions → required → Zoom → reminders; GHL: calendar → form → pipeline stages → tags; FUB /
Sheets: fields and columns). Then
`python3 "${CLAUDE_PLUGIN_ROOT}/shared/render_doc.py" /tmp/sales-system.txt "Sales System — [Name] — [YYYY-MM-DD].docx" --title "Sales System" --subtitle "[Name] · [Organization]"`,
read the `.docx` back (no `<w:` markup), upload to the workspace's `05 · Offer` folder (the brain contract's
bucket for the Sales OPS kit), hand the link.
`RENDERER-UNAVAILABLE` → install nothing, upload the `.md`, one line that the styled version needs the renderer.

## Write → push → verify, then confirm
Write `sales-system.md` and the `config.md` block, `attraction-brain-sync` PUSH, verify — one step. Confirm:
*"Your partner-call system is set: [tool], [length]-minute calls, the five questions, your stages mapped
into [CRM]. The doc with the paste-ready settings is in your home base. Next: 'write my booking page' for
the page copy, 'set up my show-up sequence' for the reminders, 'plan my call block' for the daily slots."*

## Demo mode
Fictional member, no real CRM, every setting "(illustrative — demo)", nothing written to a real Brain.

## Quality bar
No `[Brokerage]` placeholder survives (compliance.md supplies the name or the setup stops and says why); the
five questions are Mike's, in the member's voice; the stage names are the locked nine, spelled exactly; the
checklist fits their actual tool; nothing promised that the member must do in the tool is described as done.
