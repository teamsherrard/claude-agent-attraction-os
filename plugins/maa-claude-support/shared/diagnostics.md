# Diagnostics — the decision trees (Tier 3)

Run by `maa-support-diagnose`. Rules of engagement: cheapest check first · one step at a time · look
but never touch (house rule #1) · translate everything (plain-language.md) · two failed fixes →
`maa-support-escalate`. A "check" here means READ (list a folder, read a file, one cheap connector
read, one screenshot) — never write, never reconfigure.

Openers that route here and which tree: "brain isn't working" → #1 · "no Brain found" but they
built one (and they also run Mike's realtor plugins) → #1b · "can't see my email/calendar/files"
→ #2 · "typed it, nothing happened" → #3 · "Claude is slow/stuck/down" → #4 · "doesn't sound like
me / output is off / it won't say the number" → #5 · "chat too long / disappeared" → #6 · "can't
read my folder" → #7 · "I don't see Cowork" → #8 · "it says it sent it but nothing arrived" → #9A
· "my debrief / scheduled agent never ran" → #10 · "my Claude Design skill won't upload /
isn't in Design" → #11 · "Riverside won't connect / can't see my recording" → #12. **No tree
fits?** Don't force one — fall back to the navigator's rule: T2 lookup via the source map's
official indexes, and if confidence stays low, `maa-support-escalate`. Never bend a tree around a
symptom it wasn't built for.

## Tree #1 — "My brain isn't working" (the big one)

1. **Does the attraction brain exist here?** List `~/attraction-brain/` — and judge by `brain.md`,
   not the folder: a folder WITHOUT `brain.md` counts as never-built (stray files prove nothing).
   - Missing / no `brain.md` → **first, the two-Brains check:** does `~/realtor-brain/` exist?
     Yes → tree #1b before anything else (they may have built the WRONG brain, or the right one
     answered to the wrong phrase). No → ask one question: "Have you done 'set up my attraction
     brain' before, on any computer?"
     - Never → route **`attraction-brain-setup`** ("let's build it — one guided session").
     - Yes, on another machine / before → route **`attraction-brain-sync`** restore ("your permanent
       copy lives in your own cloud drive — let's pull it down; takes minutes").
2. **Is it populated or placeholder?** Read `brain.md` + spot-check `identity/profile.md`,
   `identity/avatars.md`, `identity/voice.md`. Mostly `[set later]` / empty → route
   **`attraction-brain-health`** ("the brain exists but it's running on fumes — a quick health check
   will show the 2–3 things worth filling in first"). Remember what's LEGITIMATELY empty in Week
   1: offer, positioning, content pillars, channel — those are built in later weeks, never a gap.
3. **Is it stale vs the cloud?** If sync is set up, a quick pull-check via **`attraction-brain-sync`**
   (newest-wins makes this safe). Symptom "it lost what I added yesterday (on my other
   machine/session)" → this, almost always. Clean pull but the content still absent → the OTHER
   machine may hold an unpushed write: open it there, say "save my attraction brain," then pull
   again here.
4. **Schema current?** If any skill reported "brain looks out of date" → route
   **`attraction-brain-migrate`**. Reassure: migrate renames/reorganizes WITHOUT losing content.
   Schema line should read `aa-1.0`.
5. **A tool error is never "no Brain."** A skill that hit a connector/file error and SUGGESTED
   setup is misreading its own error — never re-run setup over a real Brain; fix the error (tree
   #2 / #7) and retry.
6. Still broken with a healthy-looking brain → the problem is the SKILL, not the brain → tree #3,
   then escalate with the brain-health one-liner attached.

## Tree #1b — "No Brain found" when BOTH Brains are installed (realtor + attraction)

The two stacks are built to coexist (`stack-map.md`, "Two Brains on one machine"). The failure is
almost always a PHRASE or a FOLDER mix-up, never data loss.

1. **Which plugin answered?** Ask for the exact phrase they typed, or a screenshot. "Set up my
   brain" / "load my brain" / "check my brain" → the REALTOR plugin claimed it (that phrase is
   reserved for it by design). Fix: hand them the attraction phrase — *"say 'set up my attraction
   brain'"* (or "load / check / save my attraction brain"). Confirm it fires. Done; log it.
2. **Which folders exist?** List both `~/realtor-brain/` and `~/attraction-brain/`.
   - Only `~/realtor-brain/` with `brain.md` → the attraction brain was never built here. Two
     routes, member picks: **`attraction-brain-setup`** (which offers the Realtor Brain bridge:
     `attraction-import` pulls profile, market, voice, proof, brand, operations read-only — a real
     head start) or **`attraction-brain-sync`** restore if they built it on another machine.
   - Both exist → the brain IS there; go back to step 1 (it was the phrase) or tree #1 step 2+.
   - `~/attraction-brain/` exists but the markers are crossed (a `_workspace.md` where
     `_attraction-workspace.md` should be, or the attraction `config.md` pointing at the realtor
     workspace) → a real sync-ladder fault: **`maa-support-escalate`** with both `config.md` files
     named (never edit either).
3. **"It's reading my realtor stuff in the attraction skills"** (buyers/sellers/listings showing up
   in attraction output) → the attraction skill read the wrong Brain (a hook/session-start mix) →
   one fresh chat, invoke the attraction skill by its own phrase; recurring → escalate as a bug
   with the skill name. Never suggest deleting either Brain.
4. **Attraction brain present, realtor brain missing, and the member is in the REALTOR cohort
   too** → that's the realtor plugin's own support (`cohort-claude-support`, "help" there); point
   them to it warmly — this plugin only diagnoses the attraction stack.

## Tree #2 — Connector trouble (Google / Microsoft, Riverside, Metricool, ManyChat, CRM)

1. **Which account do they THINK is connected?** One question: "Which email did you connect —
   personal or work?" (Wrong-account is ~a third of these.)
2. **Cheap read test** on the failing connector: list today's calendar / one recent Drive file /
   one Riverside project list. Works → the connector is fine; the real issue is the ask or the
   skill → tree #3. **Server-class error while clearly signed in** (e.g. Microsoft's
   "SearchPlatformResolutionFailed") → that's the provider's servers, NOT the connection: use
   error-codes' Microsoft row (browse-don't-search + the onedrive.com split test) — reconnecting
   fixes nothing here.
3. **Auth error on the read** → the link expired. Plain words: "The link between Claude and your
   [Google/Microsoft/Riverside/…] needs a refresh — 60 seconds." Then BRING THE BUTTON TO THEM
   (house rule #5): surface the connector's Connect card right in this chat (directory inline, or
   one gentle call so the card renders) — the member clicks, signs in on the provider's page,
   done; verify with the cheap read again. Card won't surface → route the OWNER: Google/Microsoft
   → the walkthrough in `maa-support-teach` (card-first, article-guided Settings as fallback) ·
   Riverside → **`studio-setup`** (tree #12) · Metricool → **`sf-setup`** · the CRM → the
   `admin-*` / `sales-system-setup` connect step · ManyChat is NOT a connector (bonus templates
   on their own account — their ManyChat login, nothing to reconnect in Claude).
4. **Read works but the SKILL can't see the thing** (folder/calendar/project) → scope or location:
   confirm the exact folder/calendar name they expect; commonly the file lives outside the
   `Agent Attraction OS/` workspace folder (see tree #7 for Mac-protected folders).
4b. **"My posts never went out" (publish failure)** — auth is the LAST suspect, not the first:
   ① did they APPROVE the batch? (nothing auto-posts — an unapproved queue is the #1 cause) →
   ② are the posts sitting in Metricool's own planner? (cheap read) → ③ the tool's own status
   page → ④ then reconnect → ⑤ still failing → the TOOL's own support via `escalation.md`'s
   third-party row (Mike's team can't fix Metricool's side).
5. **Work-account blocked by their brokerage's IT** (admin-blocked messages) → not fixable here:
   offer the personal-account path or the IT letter via **`maa-support-escalate`** (FAQ Q17).

## Tree #3 — "I typed it and nothing happened" (trigger/install/not-shipped-yet)

1. **What EXACTLY did they type, and where?** (Cowork vs Chat matters — the system lives in
   Cowork. In Chat → that's the whole answer; move them to Cowork.)
2. **Does that plugin exist YET?** `stack-map.md`: Plugins 1 and 2 are built; the rest switch on
   with their week. A Week 1 member asking for `yt-script` isn't broken — *"the YouTube engine
   switches on in Week 4; this week it's the Brain."* Say it warmly, log the ask. (A Design
   Studio `ds-*` ask → that's an upload into Claude Design, not a plugin install — tree #11.)
3. **Is the plugin installed?** Check whether the owning plugin's skills appear in YOUR available
   skill listing (`stack-map.md` knows the owner; if its skills aren't in your context, it isn't
   installed here). For version questions, the member's plugin settings panel is the truth — ask
   for a screenshot of it; there is no marketplace lookup from inside a session. Not installed →
   install from Mike's official marketplace link (`cohort-kb.md`; `[NOT SET]` → the welcome-email
   pointer), then retry.
4. **Phrasing missed the trigger** → hand them the exact phrase from `stack-map.md`'s router
   ("say: *build my agent avatars*") and confirm it fires. The generic realtor phrases ("set up
   my brain", "make a reel", "edit my video") are reserved for the realtor plugins — if those are
   ALSO installed, the attraction phrase is required (tree #1b).
5. **Right skill, wrong state** — skill fired but immediately asked for setup/brain/compliance →
   that's the dependency chain working (brain first, compliance set before anything public);
   route per its message.
6. **Updates pending** → have them refresh/update plugins (marketplace), retry once. Still dead
   with correct phrase + installed plugin → **`maa-support-escalate`** with the exact phrase tried.

## Tree #4 — "Claude is slow / stuck / down / erroring on everything"

1. **STATUS FIRST** (house rule #2): status.claude.com. Incident → plain words, their work is
   safe, nothing to fix, try again later. Log, done.
2. **Scope it:** everything, or one job? One question: "Is it acting up on everything, or just
   this one task?"
   - One task → error text/screenshot → `error-codes.md`; retry once; two fails → escalate.
   - Everything, status clean → 3.
3. **The usual suspect: a marathon chat.** Long chat = slow chat. Fresh chat, invoke the same
   skill; Brain carries context (FAQ Q27).
4. **The boring checklist**, one at a time: is the desktop app current · restart the app ·
   is their internet OK. (Never uninstall/reinstall as a support step — that's escalate-level.)
5. Still broken → **`maa-support-escalate`** (this pattern = real bug or account state; humans).

## Tree #5 — "Output is off" (doesn't sound like me / generic / wrong facts / it refuses)

1. **Which kind of off?** Voice · genericness · wrong facts about them · a refusal (won't make it
   public, won't state a number) · wrong LOOK (a Design output off-brand). One screenshot or paste
   of the offending output.
2. **Voice off** → brain depth: `identity/voice.md` + voice-samples thin? → route
   **`attraction-voice-proof`** (written) / **`attraction-voice-print`** (spoken). (FAQ Q21.)
3. **Generic content** → avatars / positioning / story-bank thin → **`attraction-brain-health`** for
   the highest-impact gaps. Content that could be any agent's = the any-agent test failing =
   feed the Brain (the story bank especially).
4. **Wrong facts about their business / brokerage** → find where the Brain says it: it's either
   stale (route the owning skill — `attraction-brand-persona`, `attraction-brokerage-model`,
   `attraction-operations`) or was never captured. A wrong fact about their brokerage MODEL →
   `attraction-brokerage-model` re-ingests their materials (never let a skill wing a model fact).
5. **A refusal is usually a gate, not a fault:**
   - "I can't make that public until compliance is set" → the 3-state compliance gate; route
     **`attraction-compliance`**. "If empty, proceed" is banned OS-wide — never tell them to bypass it.
   - "I won't state what you'll earn" / numbers labelled illustrative → the no-earnings-claims rule;
     **`attraction-rev-share-calculator`** gives scenarios, never promises. Working as designed.
   - "I won't name their former brokerage / compare negatively" → the two cardinal rules
     (`03-model-positioning/13`). Working as designed; explain in Mike's framing.
   - A skill INVENTED a stat, quote, testimonial, or production number → that's a real bug Mike
     wants → **`maa-support-escalate`** with the output attached, even if you also fix the piece.
6. **Wrong LOOK on a design** (logo/style sheet/offer stack off-brand) → not a Brain problem:
   the Agent Attraction Design System isn't set up in Claude Design, or the Brain Book uploaded
   to Design is stale → re-upload the current Book, set the design system (FAQ Q38's pro move).
   The Brain's `brand-visual.md` wrong → `attraction-brand-direction`.

## Tree #6 — Sessions & "my chat disappeared / it forgot everything"

1. **Check BEFORE reassuring:** does `~/attraction-brain/brain.md` exist? WITH a Brain → reassure
   with confidence (FAQ Q4/Q5): chats are workbenches; the Brain + their cloud drive are the
   memory. WITHOUT a Brain (day-one member) → be honest instead: *"Right now nothing saves your
   work between chats — that's exactly what the Brain fixes, and it's the next setup step.
   Let's build it."* Never recite "nothing is lost" to someone with nowhere for it to be saved.
2. **Looking for a DELIVERABLE from that chat?** Deliverables live in the `Agent Attraction OS/`
   workspace folder (the Book, the scorecard, intel reports, scripts), not in the chat — find it
   there with them.
3. **Looking for a conversation with an agent, an objection, a name, an idea that was only ever
   said in chat?** Honest answer: chat text doesn't persist, THIS time it may be gone — then teach
   the fix so it never happens again: "capture this" (`attraction-capture`) writes it to the
   right ledger (top-50, conversations, objections, ideas) in one line.
4. **"It forgot who I am"** → that's tree #1 (brain missing/unsynced on this machine), not memory.

## Tree #7 — "Claude can't read my folder/file" (Mac privacy)

1. Confirm the path: Downloads / Desktop / Documents are Mac-protected per-app (known repo
   issue). Two doors, member picks:
   - **Grant once:** System Settings → Privacy & Security → Files & Folders (or Full Disk Access)
     → allow for the Claude app, then restart the app. Screenshot-guide them through it.
   - **Move instead** (recommended default): work from the brain folder and the workspace
     folders the system already uses (`06 · Materials` for brokerage decks, CRM exports, recordings) — no
     permissions dance, and sync covers it.
2. File uploaded to chat vs on disk confusion → teach the difference in one line; for system jobs
   the file wants to BE in the workspace folder.
3. Granted access and still blocked → restart app, retry once → **`maa-support-escalate`**.

## Tree #8 — "I don't see Cowork" (availability, not breakage)

1. **Where are they looking?** One question + screenshot: browser or desktop app, and which
   plan? (Both matter; neither is guessable.)
2. **Fetch, don't recall:** availability by plan/surface changes — fetch the mapped articles
   ("Cowork on web / desktop / mobile" + the pricing page via `source-map.md`) and answer from
   today's truth.
3. **If their plan genuinely lacks it** → that's a plan decision, warmly → `maa-support-account`
   (which fetches before recommending).
4. **If their plan has it but the button's missing** → the boring checklist: right account
   signed in · app current · restart. Still missing with a qualifying plan → **`maa-support-escalate`**
   (Anthropic-side rollout/account state; not fixable from here).

## Tree #9 — "It says it sent/saved/booked it, but it doesn't exist"

1. **Verify the artifact with one cheap read** — the email in Sent, the doc in the workspace, the
   event on the calendar, the row in `memory/top-50.md` or `memory/conversations.md`. Found → it's a
   WHERE problem; show them.
2. **Absent** → it was a draft-that-never-sent (by design: nothing sends without a yes) or a
   hallucinated claim. Don't relitigate — redo the action through the owning skill, watch it
   confirm, THEN reassure. Log it (real bug signal if a skill claimed completion falsely).
3. **"It said it saved to my Brain but my other machine doesn't have it"** → the write landed but
   the PUSH didn't (an unsynced write is a lost write) → `attraction-brain-sync` push from the
   machine that has it; recurring → escalate as a sync bug.

## Tree #10 — "My scheduled agent never ran" (Debrief, Weekly Content Performance, any owned agent)

Every scheduled agent in this OS is created by its OWNER skill (`stack-map.md` table) only after
the member says yes, and it's draft-only. "Never ran" has four causes, cheapest first — but first
rule out the two that were never scheduled: "my agent movement watcher never ran" → the Prospect
Radar's news scan runs on demand, say "scan agent movement"; "my CEO review never ran" → say "run
my CEO review". Neither has a task; that is by design, not a failure.

1. **Was the yes ever given?** Ask one question: "When you set up [the Brain / Short-Form / the
   Admin…], did it ask whether to switch on the [Daily Debrief / Friday performance note / Morning
   Brief] — and did you say yes?" Many members skipped it on purpose (fine) or setup ended before
   that stop (Stop 16 for the Debrief). No yes → route the OWNER skill to provision it now
   (`attraction-debrief`, `sf-analytics`, `admin-attraction-setup`…). Support never creates a
   scheduled task itself.
2. **Does the task EXIST?** Cowork's scheduled-tasks panel (screenshot if unsure; the member's
   panel is the truth, support can't list it for them). Yes was given but no task → the creation
   step failed silently → owner skill again, watch it confirm; fails twice → escalate.
3. **Task exists, never produced anything** → its dependencies at run time: connector expired at
   the run hour (tree #2) · usage limit hit at the run hour (`maa-support-account`) · brain unsynced
   on the machine where it runs (tree #1) · the Debrief reads `top-50`/`conversations`/`scorecard`
   — all empty = it ran and had nothing to say (check `memory/debriefs.md` for a dated row).
4. **It "sent" something** → it can't; every agent is draft-only. A member expecting an email or
   post from an agent is expecting a feature the OS deliberately doesn't have (doctrine §8).
5. Schedule fine, deps fine, still silent → re-create via the owner skill → still dead →
   **`maa-support-escalate`** with the task name, cadence, and the last run date they see.

## Tree #11 — Claude Design skill upload failures (the Design Studio is uploaded zips, not a plugin)

1. **Which error, exactly?** Screenshot of the upload dialog at claude.ai/customize/skills.
2. **"Invalid zip" / rejected on upload:**
   - **Description over 1024 characters** — the upload limit on a skill's `description`. The
     cohort's `ds-*` zips ship checked under the limit; a member who EDITED a SKILL.md (or got a
     zip from anywhere but the official download) can trip it → re-download the official zip,
     upload untouched. Edited on purpose → the owner (Mike's team) fixes the description; ticket
     naming the skill.
   - **Nested zip** (a zip inside a zip, or a zipped FOLDER containing the skill folder) — Safari
     auto-unzips and members re-zip the parent; Windows "Send to → Compressed folder" on a
     folder-of-a-folder does the same. The skill must be ONE folder with `SKILL.md` at its top,
     zipped once. Fix: fresh download, upload exactly as downloaded (never unzip/re-zip; Safari
     "open safe files" off, or use Chrome). FAQ Q39 ladder (size sanity: ~10–40 KB; 1 KB = an
     error page wearing a zip name = broken link, report it).
   - **A bare `.md` uploaded** → always the whole zip (FAQ Q30).
3. **Uploaded fine but missing in Design's "Your skills" panel** → FAQ Q38 in order: same
   account/workspace on both screens → listed + toggled on at customize/skills → reopen Design,
   check the panel filter → still gone, screenshots of both + escalate. Two bypasses meanwhile:
   attach the zip straight into the Design chat ("use this skill"), or run the thinking in a
   regular chat and carry the result into Design.
4. **"The design doesn't look like my brand"** → not an upload problem: the Agent Attraction
   Design System isn't set up in Design, or the Brain Book uploaded is stale (tree #5 step 6).
5. **"Where do I install the Design Studio PLUGIN?"** → there isn't one, by design (Claude Design
   can't run plugins). Teach once, warmly; hand the official Design starter from `resource-library.md`.

## Tree #12 — Riverside connector issues (the AI Editor, Plugin 5)

1. **Is Plugin 5 installed and is it Week 3+?** Not yet → honest "switches on in Week 3"; log.
2. **Is the Riverside connector added and signed in?** Cheap read: list projects/recordings via
   the connector. Auth error → tree #2 step 3 (Connect card, member signs in on Riverside's own
   page). Never a Descript connector — a member mentioning Descript was reading the realtor cohort's
   material; the MAA editor is Riverside only.
3. **Connected but "can't see my recording"** → the recording is in a different Riverside studio
   or account than the one connected (studios are per-account; ask which login they record under)
   · still processing on Riverside's side (give it time; their dashboard shows status) · the
   project name differs from what they typed (one cheap search by name).
4. **"It edited the wrong Brain's brand"** (realtor captions/colours on attraction content) →
   the editor's config points at `~/realtor-brain/` (the realtor system's folder); route **`studio-setup`** to re-pull from
   `~/attraction-brain/brand-visual.md` — and log it (a fork pointing at the wrong Brain is a bug).
5. **Riverside's own outage / plan limit / export failure** → Riverside's status and support
   (third-party row in `escalation.md`); Mike's team can't fix Riverside's side. Draft the message.
6. Two failed reconnects → **`maa-support-escalate`** with the connector state and the project name.
