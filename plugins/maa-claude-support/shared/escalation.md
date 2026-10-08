# Escalation — the human handoff playbook

Used by `maa-support-escalate`. The promise to the member: **you will never write a support ticket
from scratch, and you will never explain your problem twice.**

## THE DOOR IS NOT WIRED YET — read this first (launch blocker)

The Mike-side escalation target for this cohort is **`[NOT SET: Mike's support portal URL]`**.
It MUST be set in `maa-support-setup` (and in `cohort-kb.md`'s doors table) before launch.

Why it is deliberately blank: the realtor cohort's support desk pointed at
support.mikesherrard.com (a Freshdesk portal). On 2026-09-25 that desk returned **HTTP 403 —
account suspended**. This plugin does NOT inherit that door; a dead ticket door is worse than an
honest "not wired yet." Until the portal is set:

- Mike-bound tickets go to the **Circle community** (the Thursday tech-Q&A thread, or Heidi's
  Wednesday check-in thread) with the same finished ticket text — and support says plainly that
  the ticket door isn't wired yet and the gap is logged.
- The Circle link may itself be `[NOT SET]` → "it's in your welcome email."
- `maa-support-whatsnew`'s link-health pass treats a `[NOT SET]` portal as a standing
  `[SUPPORT]` line at launch-gate severity until a URL is set AND answers 200.

Mike's rule carries over unchanged: when the portal IS set, it is the ONLY Mike-side channel ever
mentioned to members — **no support email address exists in any answer**, and the portal is
surfaced only at escalation moments, never advertised.

## When to escalate (any of these)

- Two failed fix attempts on the same symptom (house rule #8).
- Anthropic account territory: login loops, verification, billing/charges, plan state — we never
  poke accounts (house rule #10).
- A real bug: a skill violating its own rules (invented stat, quote, testimonial, or production
  number; an earnings claim; a former brokerage named in a story; a compliance gate bypassed;
  delivered unstyled output; broke mid-run reproducibly; a fork reading the wrong Brain).
- Brokerage IT blocks (admin-blocked connector) — needs the IT letter.
- Feature requests and "the system should…" ideas (escalate = capture these too; they're wanted).
- Program-policy questions support may not answer (refunds, pausing, transfers, Week 7
  eligibility disputes) — these are Mike's-team answers, always.
- Any time confidence is low and the member needs a real answer — "I don't know" routes here.

## Route by problem type

| Type | Goes to | How |
|---|---|---|
| System/plugin bugs, Brain problems support couldn't fix, cohort blockers, policy questions | **Mike's support portal** — `[NOT SET: Mike's support portal URL]` in `cohort-kb.md`; until set → the Circle community door, and say why | Ticket text built in chat, handed finished — member opens the portal, pastes, attaches their screenshot, submits |
| Anthropic account / billing / login — AND Anthropic PRODUCT bugs (the desktop app's own error popups, connector platform failures that persist) | **Anthropic's official support path** | Point to the Help Center's contact path (live via `source-map.md`); help them WRITE the message with the exact error text; never collect credentials/card details. ALSO log product bugs for Mike in parallel — his team can't patch Anthropic's app, but the pattern across members is exactly what Mike aggregates and raises |
| A bring-your-own TOOL's own fault (Riverside, Metricool, ManyChat, GoHighLevel / Follow Up Boss, Notion outage / account / billing) | **That tool's own support** | Draft the message for the member, ready to paste into the tool's help channel — Mike's team can't fix a third party's side, so don't route it to the portal |
| "Anyone else hit this?" / soft questions | **Circle community** (link in `cohort-kb.md`; `[NOT SET]` → welcome email) | Draft the post for them, ready to paste |
| Coaching-level questions (strategy, "is my offer good", "is this working") | **Tuesday's Q&A with Mike** (or Heidi's Wednesday thread so it lands on Thursday's agenda) | Not a ticket — tell them why live is better for this one; the Ask-Mike lane can hand them the lesson to rewatch first |
| Tech how-to that support couldn't land | **Thursday's tech Q&A with the coaches** | Post the question in Heidi's Wednesday thread so the coaches walk in knowing it |
| IT-blocked work account | Their brokerage IT | Draft the one-paragraph access-request letter (what the connector needs and why; nothing else) |

**The expectation line (use it when they want a human NOW):** the fastest way to a human IS the
portal ticket — there's no phone line, and I'll build the ticket for you right now. (Portal not
wired yet → *"the ticket door isn't live yet, so this goes to the Circle thread the coaches read
before Thursday's call — same ticket, same detail."*) Tuesday and Thursday calls are the live
doors for anything that isn't breakage.

## The bug report (build it FOR them, from the session)

Everything support already learned this session goes in — the member confirms, never re-types:

```
Subject: [MAA Support] <plain symptom> — <member name>

WHAT I WAS DOING: <plugin + skill, or Claude basic, in one line>
WHAT I TYPED/CLICKED: <their exact words / the trigger phrase tried>
WHAT HAPPENED: <symptom in plain words>
WHAT I EXPECTED: <one line>
EXACT ERROR (verbatim, if any): <raw text — the one place raw errors ARE welcome>
SCREENSHOT: <attached, if they gave one>
WHAT SUPPORT ALREADY TRIED: <tree + steps + what each check found>
SETUP SNAPSHOT: <OS · surface (Cowork desktop/web) · plugin(s) + versions if known ·
attraction brain one-liner (exists/populated/synced/schema aa-1.0) · realtor brain also present? y/n ·
connector states checked · cohort week>
WHEN: <date/time it happened, member's timezone>
```

Rules: the report is handed as FINISHED text — the member opens the portal link, pastes it as
the ticket (SUBJECT line = the ticket subject), attaches their screenshot in the form, and
submits it themselves · member reads before submitting; support never submits on their behalf ·
attach nothing they haven't seen · **the portal is the only Mike-side channel — never mention or
suggest any support email address** (Mike's rule) · portal `[NOT SET]` or down → the Circle door
with the same finished text.

## After submitting

1. Set expectations honestly: Mike's team replies through the portal's own notifications (or in
   the Circle thread) — no invented ETAs.
2. Log it (house rule #6) with `escalated` as the outcome — these rows are the #1 input to next
   release's FAQ.
3. If it was a bug: thank them properly. *"Reports like this are exactly how the system gets
   better for the whole cohort — this one goes straight to the fix list."*

## Mike's side of the loop (agency note, not member-facing)

Once the portal is set, tickets land there → monthly, the agency runs an insights pass in Claude
Code over tickets + (optionally) members' volunteered support-log lines: top repeat issues →
FAQ/doctrine additions, curriculum fixes, and bug queue. The support plugin is also a listening
post — that's why logging is non-negotiable. Decision still open for Mike (master plan §2): fix
the Freshdesk billing and reuse that portal, or stand up a new portal for MAA — either way the
URL goes into `maa-support-setup` and `cohort-kb.md` before Nov 3.
