---
name: sf-comment-to-dm
description: >
  The comment-to-DM engine for attracting agents (Week 4): the ask ladder on TWO keywords only — GUIDE
  (the guide, sent with the copy the lead magnet plugin wrote) and the offer's comment keyword (the
  invitation word). Writes the one-page keyword sheet, the CTA bank in the kit's words, the DM bank
  for both words plus the story reply, and the ManyChat Build Sheet the member follows in their own
  account this week (ManyChat is part of the program, never connected to Claude, never asked about);
  never a pitch or compensation, the brokerage never the reason. Owns the Keyword Follow-up Queue
  (Tue/Thu, by phrase; reads keyword comments when Instagram is connected); draft-only. Trigger on:
  "keyword for this reel", "comment to DM for agents", "my DM bank", "set up my ManyChat", "my ManyChat
  build sheet", "my ManyChat copy", "keyword automation", "my keyword sheet", "an agent commented my
  keyword", "an agent DMed me from a reel", "my keyword follow-ups", "turn on my keyword queue".
---

# Comment to DM — the two keywords, the ask ladder and the DM bank (Week 4)

Short-form is not about views. The path is Awareness → Recognition → Familiarity → Trust → Curiosity →
Conversation, and the asks climb the same way: Follow → Comment → DM → Resource → Conversation → Call.
The member has **two keywords, never more**: **GUIDE** sends the guide (the Resource rung — the magnet the
lead magnet plugin built in Week 2, delivered by the DM flow that plugin already wrote), and **the offer's
`Comment keyword:`** (BUYERS, say) is the invitation word — it opens the one-pager and the call link. One
word rides on every Reel so a comment becomes a message and a message becomes a human conversation.
Nothing on this ladder pitches. The brokerage, the model, and compensation are answered on a private call,
never in a DM (`02-prospect-targeting/19`: say as little as you have to in text; the model is explained on a
private call) — and the brokerage is never the reason to talk.

**Apply** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and `${CLAUDE_PLUGIN_ROOT}/shared/mike-frameworks.md`
§8 (the ladder). Every DM template here is **public-facing** (an agent outside the organization reads it), so
the compliance gate applies before any of it is delivered. The Brain Contract
(`${CLAUDE_PLUGIN_ROOT}/shared/brain-contract.md`) names what this skill writes: the `Keyword:` and `ManyChat:`
lines of `identity/publishing.md`, interim conversation rows, its one task line (`Keyword Queue task:`) in
`config.md`, and its texts in `~/attraction-brain/exports/`. To the member: plain words — never a skill id, a file
name, or a path; told, not asked (the owner, 2026-11-14) — a question only for a fact the Brain cannot hold.

## The two keywords (the rule every writer follows)

| Word | Where it comes from | What it opens | The DM it triggers |
|---|---|---|---|
| **GUIDE** | `memory/magnets.md → ## Current magnet` (set in Week 2; the Resource rung) | the guide — the DM carries the funnel link (the opt-in captures the email) | the lead magnet plugin's **Delivery Kit** — its comment reply, DM 1 (the link), DM 2 (one question), DM 3 (the human hand-off), the no-reply follow-up — kept at `~/attraction-brain/exports/delivery-kit-*.txt`; **reused verbatim, never rewritten here** |
| **the offer's word** | `identity/offer.md`, the header's `Comment keyword:` line (coined with the offer) | the invitation — the one-pager and the call link | this skill's six messages (Step 3) |

Every other default word is retired: an older `Keyword:` line in `identity/publishing.md` that still holds a
retired word is rewritten to `GUIDE · [the offer's word]` on the next run and pushed — the one line this skill
writes there. **A keyword never changes once content has used it** (the kit's rule); a member who wants a
different invitation word before any content used it changes it where it lives ("refine my partner offer"),
and this sheet follows. No offer word yet (`offer.md` at `Status: seeds`) → GUIDE alone, and the call rung
uses the booking line; say in one line that the invitation word arrives with the offer ("build my partner
offer"). No guide yet (`## Current magnet` empty) → the offer's word alone and the call; say "launch my lead
magnet plugin" once. Neither → every ask is the booking line, said once, never nagged.

## Hand-off point
Once the conversion plugin is installed (its `## Conversion & Sales` block exists in `config.md`), this skill
hands the conversation to `cv-dm-flow` at the agent's FIRST reply, with the Reel, the keyword, the resource
promised, and the reply text; it never qualifies in parallel. Before that plugin exists, this skill qualifies
and logs as written below. To the member it is "when that plugin is installed", never a name.

## Five jobs (detect from the message)
- **A · THE KEYWORD FOR THIS REEL** — "what's the ask on this reel", "keyword for this reel": pick the rung
  and the word for one post (the calendar row's `CTA (rung · KEYWORD)` cell is the default).
- **B · THE KEYWORD SHEET + DM BANK** — "my keyword sheet", "my DM bank": build the set once;
  refresh it when the offer, the guide or the funnel URL changes.
- **C · A CONVERSATION STARTED** — "an agent commented GUIDE", "she DMed me from the reel": write the human
  reply, qualify, and hand off or log.
- **D · THE KEYWORD FOLLOW-UP QUEUE** — "my keyword follow-ups", "turn on / stop my keyword queue": who used a
  keyword since last time, the next DM drafted (Step 6).
- **E · SET UP MY MANYCHAT** — "set up my ManyChat", "my ManyChat build sheet", "my ManyChat copy", "keyword
  automation": the ManyChat Build Sheet the member follows in their own account (Step 3b). ManyChat is part of the
  program (the owner, 2026-11-14): set up this week, never connected to Claude — nothing here needs its connector or a
  paid plan for it; until it is live the member replies by hand from the DM bank. **This job runs only when
  the member asks for it — never inside the setup sitting (the owner, 2026-11-17).**

The daily engagement routine — fifteen minutes, same time every day — is the Game Plan's text (section 3) and the
weekly routine planner's checklist, never a scheduled list of agents (the owner, 2026-11-14). "Who should I engage
with today" → one line pointing at the routine; a conversation that starts from it is Job C.

## Step 1 — Load the Brain
Read `~/attraction-brain/brain.md` first (pull via **attraction-brain-sync** if the local copy is empty — a
pull is the whole Brain, `exports/*.txt` included). Then only what the job needs:
- `identity/publishing.md` — `Keyword:` (`GUIDE · [the offer's word]`), `What it opens:`, `ManyChat:`
  (`set up YYYY-MM-DD` → the flows run; `not yet — set it up this week (build sheet YYYY-MM-DD)` → the member replies
  by hand from the DM bank until it is live; never asked, never "optional", no opt-out value)
- `identity/offer.md` — the header's `Comment keyword:` and `Join-gated package allowed:` lines (the register
  of every call line: `yes` or `unknown` = the join register, `no` = the open register), `## The framework`
  (the method the help is FOR — named in every call ask), `## Value stack` (what "my help" is: the recorded
  lessons, the templates, the community — never the member's time)
- `memory/magnets.md → ## Current magnet` — the guide's name, the funnel URL, its keyword (GUIDE)
- `exports/delivery-kit-*.txt` (newest) — the GUIDE DM flow, quoted, never rewritten; absent → the sheet's
  GUIDE row reads *"not written yet — say 'deliver my guide'"*
- `exports/week3-kit-*.txt` (newest) → chapter 7's **CALLS TO ACTION** table — the caption line, the spoken
  line, the story reply, the bio link and the DM reply for each of the two asks, taken **verbatim**; absent →
  the lines are built on the same shapes from the offer and the magnet, and one line says "rebuild my kit"
- `memory/content-calendar.md` — the rows this week (Job A: the rung and word a row already carries is that
  Reel's default); `memory/content-log.md` — the posts of the last fourteen days (Job D)
- **The member's Instagram comments, when connected** (Job D only): the data engine
  (`${CLAUDE_PLUGIN_ROOT}/shared/composio-data-engine.md`) exposes them for a Business or Creator account —
  `INSTAGRAM_GET_IG_USER_MEDIA` (the member's recent posts) → `INSTAGRAM_GET_IG_MEDIA_COMMENTS` (text · username ·
  timestamp per comment). Read-only: `INSTAGRAM_POST_IG_COMMENT_REPLIES` exists and is **never used** — nothing is
  sent on the member's behalf. Not connected → what the member logs ("add my comments" / "an agent commented
  GUIDE"), said in one line. To the member: "your Instagram connection", never a tool name.
- `identity/avatars.md` — who each word is for and their pains (the qualifier questions mirror them)
- `identity/journey.md` (`## Why join me`) + `identity/positioning.md` — how the member talks about
  partnering, in their words
- `identity/voice.md` + `identity/voice-samples.md` (Sample 4 and later — DMs are typed) — every DM sounds
  like them, not like software
- `identity/operations.md` — the booking link and the call cadence
- `identity/compliance.md` — its first line, `Status:` — the gate (Step 4)
- `memory/top-50.md` + `memory/conversations.md` — before replying to a named agent, check whether they are
  already in a conversation (never restart one that exists); Job D reads them whole
- `memory/objections.md` — the answers that worked, for a reply that hits a known objection
- `config.md` — the `## Short-Form (Week 4)` block (an older heading with the earlier week number is the same block) for this
  skill's one task line (`Keyword Queue task:`) and `Email me:`; `Timezone`

## Step 2 — The ladder (every Reel sits on exactly one rung, with one of the two words)

| Rung | The ask, spoken and in the caption (the kit's words) | What it earns | The word |
|---|---|---|---|
| **Follow** | "follow for the next one" · "save this" · "send this to an agent who needs it" | reach and recognition | none |
| **Comment** | *"Comment GUIDE and I'll send you [the guide, in three words]."* · *"Comment [WORD] and I'll send you how I run this."* | a signal, a DM opens | GUIDE · the offer's word |
| **DM** | *"DM me GUIDE."* · *"If this is your year, DM me [WORD]."* | a private channel | GUIDE · the offer's word |
| **Resource** | the guide — *"[what the guide holds, one clause]. Comment GUIDE and I'll send it."* | trust, a reason to come back | GUIDE |
| **Conversation** | one human question about their situation | the real relationship | — |
| **Call** | the law's line: *"If you want my help running this — the lessons, the templates, the community — partner with me and it's free. Grab [the call]."* (open register: *"I'll walk you through it, free, no strings."*) | the partner call | the offer's word → the one-pager + the booking line |

**The call-to-action law (Mike, 2026-11-10) on the Call rung and on every call line:** the person · their help
· free · to run this. The method is named ("running this", "your first weekend", the framework's one line); the
brokerage is never the reason; compensation never. **Scalable by design (doctrine §10e):** "my help" is the
recorded lessons, the templates, the community (the weekly group call only when the member already runs one) —
never the member's personal time, never a standing one-on-one, never "I pick up every call".

**The rule of one:** one Reel, one ask — never two. The word is said on camera at the end, written as the
caption's last line, and pinned as the first comment. **Which ask, by pillar** (the call-ask rule, house rules #13:
; the invitation — the offer's own word, or the kit's call line — on about one post in
four, most naturally a Proof piece or a "what you get" piece; a Proof piece may carry the guide instead): Authority →
GUIDE · Perspective → follow, save or share (or GUIDE) · Story → GUIDE or the invitation · Proof → the invitation or
GUIDE · Personality → follow only. The six designed kit posts keep exactly the asks the kit printed (Posts 1, 2 and
5 the guide; Posts 3, 4 and 6 the call). Never skip rungs: a first-time viewer
is never told "book a call" — the call comes after a conversation (`mike-frameworks.md` §8).

## Step 3 — The keyword sheet and the DM bank (Job B; Job A picks one row)
**THE KEYWORD SHEET — one page, nothing more:** the two words · what each opens · the DM each triggers.
```
THE KEYWORD SHEET
[Member Name] · [Organization] · [Date]

———————————————————————————————
GUIDE
Opens:  [the guide's title] — the link to [the funnel page]
Said:  "[what the guide holds, one clause]. Comment GUIDE and I'll send it."
Caption, last line:  "Comment GUIDE and I'll send you [the guide, in three words]."     Story:  "Reply GUIDE and I'll send it."
The DM it triggers:  [the Delivery Kit's comment reply + DM 1, quoted — or "not written yet — say 'deliver my guide'"]

———————————————————————————————
[THE OFFER'S WORD]
Opens:  the one-pager and the invitation to talk — [the booking line]
Said:  "If you want my help running this, free, [the booking line]."
Caption, last line:  "Want my help running this, free? [the booking line]"     Story:  "Reply and I'll send you the link."
The DM it triggers:  [this sheet's message 1 — the one-pager, then the call line in the law's shape]

———————————————————————————————
THE STORY REPLY
Sticker or question box → "Reply GUIDE and I'll send it." (the guide) · "Reply and I'll send you the link." (the call)
The reply:  thank · answer in one line · one question back; GUIDE → the Delivery Kit's DM 1

———————————————————————————————
Exactly these — two words and the story reply — trigger a DM; nothing else.
MANYCHAT:  [set up YYYY-MM-DD · not yet — set it up this week; say 'set up my ManyChat' for the steps]     THE STAMP:  [from compliance.md]
```
Kept at `~/attraction-brain/exports/keyword-sheet-YYYY-MM-DD.txt` (the Brain Board reads the two words and their
lines from it), then pushed.

**THE CTA BANK (page one of the saved document):** fifteen ask lines in the member's voice, three per pillar,
each on the rung that fits (the ask map in `${CLAUDE_PLUGIN_ROOT}/skills/sf-optimizer/references/platform-rules.md`,
read on the two words) — the spoken line (one breath, the word said once) and its caption line (the word written
once, last line). The guide lines and the call lines are the kit's CALLS TO ACTION lines **verbatim** (the same
words every time); a pillar variant changes only the clause before the ask. Authority → GUIDE (*"comment GUIDE
and I'll send you the one-page version we use"*) · Perspective → follow, save or share (*"send this to the agent
who's panicking about it"*), or GUIDE · Story → GUIDE, or the invitation with the offer's word (*"if this is where
you are, DM me [WORD]"*) · Proof → the invitation (*"want to know what she changed? If you want my help running
this, free, [the booking line]."*), or GUIDE · Personality → follow only. Every line is tied to a thing that exists (the guide in `## Current
magnet`; the one-pager and the call from the offer); none names the model or the money. `sf-talkinghead`,
`sf-carousel`, `sf-greenscreen`, `sf-week-plan`, `set-up-my-metricool-and-post` and `sf-optimizer` take their CTA line from this
bank once it exists; until then they take it from the kit's table on the same rules.

**THE DM BANK — two flows plus the story reply:**
- **GUIDE** — the lead magnet plugin's Delivery Kit, quoted from `exports/delivery-kit-*.txt`: the public comment
  reply · DM 1 the delivery (the funnel link, the privacy line) · DM 2 the one qualifier question · DM 3 the
  human hand-off and the warm optional call line · the no-reply follow-up. Never rewritten here; a change goes
  through "deliver my guide".
- **The offer's word** — six messages in the member's voice, each under 60 words, written here:
  1. **Auto-reply** (the ManyChat one): acknowledge, send the one-pager (the kit's Join My Team one-pager — the
     designed file in their Offer folder, or its text) and the call line in the law's shape, no questions.
  2. **The human follow-up** (sent by the member, same day): one real observation about *their* content or
     comment, one question about their situation. No link, no pitch.
  3. **The qualifier** (three questions, one at a time, never a form): where are you now (production and
     brokerage type, in their words) · what are you working toward this year · what is in the way. These mirror
     the five pains; the answers are what gets logged.
  4. **The bridge to the guide** (when the answer shows a pain the guide solves): "I wrote the whole method
     down; want it?" then GUIDE's DM 1.
  5. **The invite to a call** (after they ask about partnering, or the qualifier shows fit and readiness): the
     law's line — *"If you want my help running this — the lessons, the templates, the community — partner with
     me and it's free. Grab [the call]."* (open register: *"If you want my help running this, grab [the call] —
     I'll walk you through it, free, no strings."*). Never "let's hop on a Zoom" as the first message; never the
     brokerage as the reason.
  6. **The graceful no** (not a fit or not now): a real thank-you, one useful thing, the door left open. "Parked"
     is fit and timing, never disrespect.
- **Story reply** — the reply to a story poll, question box, or "ask me anything" (`07-instagram/89`): thank,
  answer in one line, ask one back; *"Reply GUIDE and I'll send it"* when the story offered the guide.
- **DM qualifier** — the three questions above, as three short messages.

**The NEVER list (every message):** no pitch · no compensation, rev share, splits, caps, or fees · no
brokerage-to-brokerage comparison and never a negative word about another brokerage or person
(`03-model-positioning/13`) · the brokerage never the reason to talk · no promise of the member's personal time
(no standing one-on-one, no chat group, no "I pick up every call" — the help is the lessons, the templates, the
community) · no walls of text · no corporate recruiting language ("opportunity," "join my team") · no fake
personalization (if you have not read their profile, do not pretend you have) · no forced Zoom · no income
promises; the model, the money, and the paperwork are "a call conversation."

**The ManyChat hand-over (the member's own account — part of the program, the owner, 2026-11-14):** two automations
and the story reply — nothing else; any other flow in the cohort's template asset stays unused. The copy goes to the
member as the **ManyChat Build Sheet** (Step 3b), to be followed this week; this skill writes copy and build steps, it
never connects to, configures, or sends through ManyChat — the member never connects ManyChat to Claude, and nothing
here needs its connector or a paid plan for it. One note for the member: Instagram's automation rules change — check
ManyChat's current policy on comment-triggered DMs before switching an automation on.

## Step 3b — The ManyChat Build Sheet (Job E — the member follows it in their own ManyChat, this week)
Plain words, in this order, nothing the member has to figure out. The sheet — and the chat hand-over — open with the
owner's line (2026-11-14), in this shape: *"ManyChat is how your two keywords answer themselves. Set it up this week:
install ManyChat (the free plan starts you — upgrade only if ManyChat itself asks you to for Instagram automations),
import Mike's templates from your Materials folder, put GUIDE and [WORD] in with your links — your build sheet walks
you through it step by step. You don't connect ManyChat to Claude: nothing here needs its connector or a paid plan for
it. Until it's live, reply by hand from your DM bank."* Never a question, never an opt-out, never
"connected". Then the steps:
1. **Install the template first** — Mike's sequence template, the cohort's bonus asset in the member's Materials
   folder (`06 · Materials`): import it into their own ManyChat account before building anything.
2. **Automation one — GUIDE.** Trigger: a comment containing GUIDE on any post, a DM containing GUIDE, or the story
   reply. Messages: the Delivery Kit's DM 1 (the guide's download link from `memory/magnets.md → ## Current magnet` —
   the funnel link, so the opt-in captures the email), DM 2 (the one question), DM 3 (the human hand-off) — reused
   from `exports/delivery-kit-*.txt`, never rewritten; the public comment reply under their comment. Button labels
   exactly: "Send me the guide" · "Got it 👍". What to paste where: Automation → Keywords → GUIDE → the message;
   Automation → Story reply → GUIDE → the same message.
3. **Automation two — the invitation word.** Trigger: a comment or DM containing the offer's `Comment keyword:`.
   Messages: this skill's message 1 — the one-pager (the designed file's link, or the funnel link when the page
   carries it) and the call line in the law's shape (*"If you want my help running this — the lessons, the
   templates, the community — partner with me and it's free. Grab [the call]."*; open register: *"I'll walk you
   through it, free, no strings."*); then the human follow-up, sent by hand, never automated. Button labels exactly:
   "Send me the one-pager" · "Book the call". Paste: Automation → Keywords → [WORD] → the message.
4. **The story-reply trigger:** the story's sticker text is the ask ("Reply GUIDE and I'll send it." · "Reply and
   I'll send you the link."); the reply fires the matching automation; anything else the member answers by hand.
5. **The one-line test:** *"comment GUIDE on your own post from a second account and watch the DM arrive."*
6. **The plan, said once:** the free plan starts you; upgrade only if ManyChat itself asks you to for Instagram
   automations — never a price from memory.
Deliver in chat as the numbered sheet; save it beside the keyword sheet as `YYYY-MM-DD · ManyChat Build Sheet`
(`03 · Content/Short-Form/[YYYY-MM · Month]/`, per the output standard) and keep its text at
`~/attraction-brain/exports/manychat-build-sheet-YYYY-MM-DD.txt`. **The `ManyChat:` line of `identity/publishing.md`
is this skill's** (the contract grants it): when the sheet is written → `ManyChat: not yet — set it up this week
(build sheet YYYY-MM-DD)`; when the member says it is live ("ManyChat's set up", "I did the ManyChat") → `ManyChat:
set up YYYY-MM-DD`; there is no opt-out value — ManyChat is part of the program. Push (**attraction-brain-sync**). This job
never runs inside setup (the owner, 2026-11-17) — the member asks for it: "set up my ManyChat". Compliance (Step 4) applies: every message in the sheet is public-facing — at `unset` the sheet waits
for the gate and the line still reads `not yet — set it up this week`.

## Step 4 — Compliance (three-state, before anything is delivered)
Read the first line of `identity/compliance.md` — `Status:` (the Brain writes `Status:` first, then `Gate:`).
`unset` → **stop**: *"these DM templates go to agents outside your organization, so I need your compliance
basics first; say 'set up my attraction compliance' and it takes three minutes."* Deliver nothing public. `set`
→ apply every rule and remind once per session. `confirmed` → apply. Append the compliance stamp (house rules
#4 — built from `identity/compliance.md`) only where a template names the brokerage; the income disclaimer never
appears because no template mentions income. "If empty, proceed" is banned.

## Step 5 — A conversation started (Job C): reply, qualify, hand off or log
1. Check `memory/top-50.md` and `memory/conversations.md` for the agent's name first.
2. Write the human reply (message 2 above; for a GUIDE commenter the Delivery Kit's next message) in the member's
   voice; if they already answered a qualifier question, write the next one, not the first one again. An agent
   who asks how to partner gets the law's call line — the person, their help, free, to run this.
3. **When it is real** (they answered the qualifier, or asked how to partner, or asked for the call):
   - **If the conversion plugin is installed** → hand to **`cv-dm-flow`** by name with: the agent's name and
     handle, which Reel and which word started it, the resource promised, the thread so far, the pains they
     named, and the rung they are on. `cv-dm-flow` owns the conversation from here.
   - **If it is not installed yet** → log one row to `memory/conversations.md` in the locked shape (Date ·
     Agent · Type · Channel = DM · what they said, short, their words · objection heard · pain · next step ·
     Stage after = `Conversation`), through **`attraction-capture`** when it is present (it is the interim
     owner of that ledger), otherwise appended directly in that exact shape; and add or update the agent in
     the Top-50 through **`attraction-top-50`** (Notes: `Source: instagram · via reel: [title]` — or `via story:
     [theme]` for a story reply; `instagram` is the locked Source value that `sf-analytics` and the conversion
     scorecard read by that exact word; Stage = `Conversation`). Stage vocabulary is locked: Identified →
     Conversation → Call booked → Call held → 3-way → Joined → Onboarded → Active. Then push via
     **attraction-brain-sync**; if the push fails, say it is not saved, retry once, stop.
4. Never send anything. The member sends every DM themselves; this writes the words.

## Step 6 — The Keyword Follow-up Queue (Job D — by phrase, Tuesdays and Thursdays)
Who commented or DMed a keyword since last time, with **the next DM in the ladder drafted — never sent.** On
demand ("my keyword follow-ups") or on a schedule (`attraction-sf-keyword-queue` — one of the five by-phrase workflows, never named in the sitting)
1. **Since when:** the newest `exports/keyword-queue-*.txt` date (none → the last seven days).
2. **Who — real when Instagram is connected through the data engine:** `INSTAGRAM_GET_IG_USER_MEDIA` (the posts of
   the last fourteen days) → `INSTAGRAM_GET_IG_MEDIA_COMMENTS` (text · username · timestamp) → keep the comments
   containing GUIDE or the offer's word (and story replies, when the connection exposes them) since the last run;
   read-only — `INSTAGRAM_POST_IG_COMMENT_REPLIES` is never used. Plus `memory/conversations.md` rows since then with
   Channel = comment or DM naming a word, and Top-50 rows whose Notes read `Source: instagram · via reel:` / `via
   story:` with a `Next move` due. Not connected → the queue works from what the member logged ("add my comments",
   "an agent commented GUIDE") and says so in one line (*"this is from what you've told me — say 'add my comments'
   and paste them, or connect your Instagram and I'll read them"*).
3. **For each agent:** the handle · the post · the word · where they are on the ladder (commented · got the guide
   · answered the question · asked about partnering · went quiet) → **the next message**, in the member's voice: a GUIDE commenter gets the
   Delivery Kit's next message (quoted); an offer-word commenter gets this skill's next message (Step 3); a reply
   that asked how to partner gets the law's call line; anyone already handed to the conversion plugin is listed
   as "with your conversation flow", no draft. Each under 60 words; the NEVER list on every one.
4. **Save + push:** the queue to `~/attraction-brain/exports/keyword-queue-YYYY-MM-DD.txt`, then
   **attraction-brain-sync PUSH**. Nothing is sent, logged as sent, or moved a stage — the member sends, then
   tells this skill ("she replied"), and Job C takes it from there. The scheduled run ends the owner's three ways
   (verbatim in the task prompt): the note in Cowork, ONE email to the member's own address only when `Email me:`
   is `yes`, the push.
**Provision / stop:** read the `Keyword Queue task:` line in `config.md`'s Short-Form block (a line is found by its
label or by its task id). A task id → on; say so. `paused` → they stopped it; the phrase brings it back (`later` or any other value → not on). It is
created only with the member's yes — their phrase is the consent — and never silently. On the
member's phrase ("turn on my keyword queue") → a statement, never an offer or a question (the owner, 2026-11-14:
told, not asked): *"Switching on your keyword follow-up queue — Tuesdays and Thursdays, 9:00 am; name another time
any time."* Then `list_scheduled_tasks` first (adopt an existing `attraction-sf-keyword-queue`, never a twin), else
`create_scheduled_task` with `taskId: attraction-sf-keyword-queue`, `cronExpression: [minute] [hour] * * 2,4`
(Tuesdays and Thursdays, default 9:00 am, `config.md → Timezone`), the `prompt` **verbatim** from
`references/keyword-queue-task-prompt.md`. Verify with `list_scheduled_tasks` (present, enabled, a `nextRunAt`) —
never claim a schedule that did not save. Write `Keyword Queue task: attraction-sf-keyword-queue`, push, verify;
confirm once: *"On. Say 'stop my keyword queue' any time."* Stop / pause → `delete_scheduled_task` (or disable), write
`paused`, push, one line. Never a second task. A demo Brain never gets a task. An older block's
two retired engagement lines (the contract names them) are deleted on this skill's next write.

## Step 7 — Save
Deliver in chat. The keyword sheet's text always goes to `exports/keyword-sheet-YYYY-MM-DD.txt` and is pushed
(**attraction-brain-sync** — write → push → verify; the push re-renders the Brain Board, which shows the two
words). Offer to save the full set (the CTA bank first, then the keyword sheet, then the DM bank) per
`${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`: render to `.docx` (`shared/render_doc.py`) →
`03 · Content/Short-Form/[YYYY-MM · Month]/`, named `[YYYY-MM-DD] · Keyword Sheet + DM Bank`; the ManyChat Build
Sheet (Job E) beside it as `[YYYY-MM-DD] · ManyChat Build Sheet`, its text in
`exports/manychat-build-sheet-YYYY-MM-DD.txt`. Close with the one next step: *"say the word on camera at the end of every Reel — GUIDE on most, [WORD] on the ones that invite;
I'll write the human replies as they come in. Your Brain Board is updated."*

## Quality checklist
- [ ] Brain loaded; the offer's word, the guide, the register, the voice and the booking link taken from it,
      nothing re-asked; seeds and an empty magnet respected with one line each
- [ ] Two words only — GUIDE and the offer's word; no retired default anywhere (the `Keyword:` line fixed and
 the 90/10 rule (house rules #13): about one post in ten carries a keyword ask — Comment GUIDE, or the offer's word with the call line in the law's shape; every other post asks only for a follow, a save, a share or a comment on the topic; never two asks on one post
      (most naturally a Proof piece or a "what you get" piece), never two asks on one post
- [ ] The GUIDE flow quoted from the Delivery Kit, never rewritten; the offer word's six messages under 60 words
      in the member's voice; the story reply; the NEVER list kept on every one
- [ ] The keyword sheet one page — exactly the two words and the story reply; its text in `exports/`; the CTA lines
      the kit's lines verbatim; every call line in the law's shape (the person · their help · free · to run this),
      never the brokerage, never the member's time
- [ ] The ManyChat Build Sheet in order (the owner's opening line · the template first · GUIDE · the invitation word ·
      the story reply · the test · the plan once), the GUIDE messages quoted from the Delivery Kit, saved beside the
      keyword sheet and its text in `exports/`; ManyChat told as part of the program — set up this week, never
      connected to Claude, no opt-out, never asked about; the `ManyChat:` line written (`not yet — set it up this
      week (build sheet YYYY-MM-DD)` → `set up YYYY-MM-DD`)
- [ ] Comments read only through the member's connected Instagram (the two read tools; the reply tool never), else
      from what the member logged, said in one line
- [ ] Compliance read first; `unset` blocked delivery; no compensation anywhere
- [ ] Conversation handed to `cv-dm-flow` by name when installed, or logged in the locked shape and added to the
      Top-50; nothing sent
- [ ] The Keyword Follow-up Queue provisioned by the member's phrase (a statement, never an offer), by its exact
      task id; an existing task adopted; verified; its line written and pushed; stop honored in one sentence; every
      run saved to `exports/` and pushed so the Brain Board shows it; no engagement list anywhere (the routine is the
      Game Plan's text)
