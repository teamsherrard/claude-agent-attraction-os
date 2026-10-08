# Virtual Workshop Launch Kit — the builder's skeleton (replace when Team Mike's kit lands)

*The cohort doc lists a Week 6 bonus asset: "Virtual Workshop Launch Kit: workshop launch checklist, promo
calendar, registration page and slide templates, run-of-show script, follow-up sequences." It is not yet
produced. This file is the skeleton `ev-virtual` fills in for each event, built from `15-advanced-scaling/75`
and Mike's workshop-ops phases. When the real kit arrives, its content replaces this file and the skill reads
it the same way. Every timing below is the builder's default, not a vault number (doctrine §17).*

## 1. The launch checklist (T-14 → T+10)
| When | What | Owner | Done when |
|---|---|---|---|
| T-14 | Event Brief approved (`ev-strategy`); the room settings chosen | member | brief in the event folder |
| T-14 | Registration page copy written (`ev-registration`) → built in Claude Design (`aa-funnel-design`, registration shape) → live on the member's host; test-submitted once | member / VA | the confirmation email arrived for the test |
| T-14 | Confirmation + reminder workflow built from the table (`shared/ghl-workflow-table.md`) | VA | test row verified |
| T-14 | Promo graphic, countdown stories, slide template briefed (`ev-promo`, `ev-runofshow` → `aa-event-design`) | member | files in `02 · Brand` / the event folder |
| T-13 → T-1 | Promo calendar runs (`references/promo-calendar.md` in `ev-promo`): posts, stories, emails, DMs | member + agents + speakers | each row ticked |
| T-12 | Partners sent the share line (`lm-partnerships`) | member | partner replies logged by the member |
| T-10 | Personal invites to the pipeline list (the Admin's match-back / the Top-50) | member | sent, by the member |
| T-7 | Speakers briefed in writing (teach one thing; no pitching; the two cardinal rules); their posts scheduled by them | member | reply received |
| T-3 | Run-of-show rehearsed with the chat moderator; slides final; replay page ready (hidden) | member + moderator | one dry run |
| T-1 | 24-hour reminder email + text (from the registration doc) | the workflow | sent |
| T-0 | 1-hour text with the link; doors open 5 minutes early with music and a welcome slide | the workflow / host | — |
| T-0 | The event (60 min); recording on; the moderator's engaged list | host + moderator | recording saved |
| T+1 9:00 | The follow-up (`ev-followup`; the Post-Event Follow-Up agent if on — explicit yes, draft-only): attended / no-show / hot / cold; the share pack to the agents | member | drafts loaded; hot messages sent by the member |
| T+3 · T+7 | Value touch; the warm invite; replay window closes | the workflow | sequence complete |
| T+10 | Numbers and debrief (`ev-analytics`) | member | block updated; report in the folder |

## 2. The promo calendar
Owned and written by `ev-promo` (`skills/ev-promo/references/promo-calendar.md`, the virtual T-14 version).

## 3. The registration page and slide templates
- Registration page: `ev-registration` writes the copy and the form; the Design Studio's `aa-funnel-design`
  (registration shape) builds it; the static form rule applies.
- Slides: `ev-runofshow` writes the slide brief; `aa-event-design` builds the deck (title · the promise · one slide per
  teaching beat · the do-this-now slide · the Q&A slide · the iceberg slide · the book-a-call slide with the QR
  · the resource slide · the compliance strip where required).

## 4. The run-of-show script (60 minutes, chat-heavy)
| Minute | Beat | Chat prompt |
|---|---|---|
| 0–5 | Energy open · who the member is (one mirror line) · the promise · "stay to the end for [the resource]" | "Drop where you're joining from" |
| 5–8 | The pain, in their words (avatars.md) | "Drop a 1 if you've ever [the pain]" |
| 8–23 | Teaching block 1 (the first thing they'd show a new agent — offer.md "Teach first") | "Type 'yes' if you've tried this" |
| 23–26 | Do-this-now: the one step they take tonight | "What's your version? Drop it" |
| 26–41 | Teaching block 2 (the system behind block 1) | "Drop a 2 if this is the gap for you" |
| 41–51 | Block 3 or a live demo (the member's own numbers labeled; an agent's win with consent) | "Questions for the Q&A — drop them now" |
| 51–57 | Q&A from the chat (the moderator reads them) | — |
| 57–60 | The light transition (doctrine §7, virtual wording) → "book a call" (the link pinned) → the resource link → thank you | "Drop 'link' and [the moderator] sends the booking page" |
The minute-level version for this event is written by `ev-runofshow`.

## 5. The follow-up sequences
Owned and written by `ev-followup`: attended (day 1 · 3 · 7) · no-show (day 1 · 3 · 7) · hot (personal, within
24 hours) · cold (into the newsletter) · the agents' share pack — each documented as a Trigger → Action → Outcome
table for the member's GoHighLevel or list tool.
