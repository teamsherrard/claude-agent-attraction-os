# Config
*operational settings for this member's Agent Attraction Brain — the one key registry; every skill reads these exact keys*

## Registry (locked spelling — `shared/brain-contract.md`)
- **Schema:** aa-1.0  *(structure version — the template, this line, and `attraction-brain-migrate` always agree; migrate pushes after it bumps this)*
- **Storage provider:** [google | microsoft]  *(set once at setup — see `shared/connectors.md`)*
- **Storage:** [ok | READ-ONLY (org-gated)]  *(a separate key from `Storage provider` — written by `attraction-brain-sync` when a provider's write actions are admin-disabled; every save then says so in one plain line)*
- **Workspace name:** [display name — default "Agent Attraction OS"; the member may rename it freely]
- **Workspace ID:** [captured at first sync — IDs survive renames; ALWAYS locate by ID, then by the `_attraction-workspace.md` marker, never by name]
- **Workspace link:** [the direct URL — hand this to the member to bookmark]
- **Timezone:** [e.g., America/Chicago]  *(timezone lives here and only here)*
- **CRM:** [none | kvCORE | Follow Up Boss | GoHighLevel | Lofty | other — name it]  *(the system of record for contacts; the Brain's ledgers are the AI's working memory, never the CRM)*
- **Setup progress:** [not started | Step 1 done | Phase 1 done | Phase 2 done | Phase 3 done | Phase 4 done | Phase 5 done | Phase 6 done | Phase 7 done | complete]  *(resume reads this stamp — a stamped fact beats inference)*
- **Debrief time:** [default 6:00 pm, member timezone]
- **Daily Debrief task:** [task id | declined]  *(provisioned only with the member's explicit yes; draft-only)*
- **Agent Movement Watcher task:** [task id | declined | later]  *(offered in Week 2 by `attraction-prospect-radar`; same consent rule)*
- **Workspace shared with:** [nobody | names — the member's choice at setup Stop 16]
- **Realtor Brain bridge:** [none | declined | pulled YYYY-MM-DD]  *(read-only; never written back)*
- **Demo brain:** [no | yes]  *(yes only when the member explicitly asked for a fictional demo — `shared/brain-book-spec.md`; a demo brain never mixes with a real one)*
- **Cohort week:** [1–6, optional — the Support plugin reads it]

## Keys the later plugins register (locked spelling — each lives in its owner's block below; the Brain never writes them)
*Listed here so the registry is complete and every skill spells them the same way:* `Weekly Content Performance task` (Short-Form block — `sf-analytics` fills it, `yt-analytics` reads it there and nowhere else) · `Call Block Prep task` · `Cold-Lead Reactivation task` (Conversion & Sales block — `cv-call-prep`, `cv-reactivation`) · `AI Admin` (the stamp `AI Admin: set up [date]`, the FIRST line of the AI Admin block — the Conversion plugin and `attraction-capture` detect the Admin by a heading that starts with `## AI Admin` plus this line, and from then on request stage moves and Top-50 touch updates instead of writing them) · `Morning Brief task` · `Daily Follow-Up Queue task` · `Weekly CEO Review task` · `Monthly KPI Review task` · `Team Wins Newsletter task` (AI Admin block) · `Installed` · `Plugin version` · `Member code` · `Registration host` · `Post-Event Follow-Up task` (Events block — `ev-navigator` creates the block; `ev-strategy` writes `Member code`, `ev-registration` `Registration host`, `ev-followup` the task line: `not offered yet` → `ev-post-event-follow-up · armed for YYYY-MM-DD 9:00` · `declined` · `later`) · `Support desk` (MAA Support block — `attraction`).

## Supporting fields (not registry keys; mechanics only)
- **Brain home (permanent):** the workspace's `01 · AI Brain/_engine/`. Local `~/attraction-brain/` is a per-session working copy — Cowork wipes it between sessions; an unsynced write is a lost write.
- **Owner account:** [which Google / Microsoft account holds the workspace — checked when it can't be found]
- **Locale:** [country · currency · units — e.g., USA · USD · sq ft; every skill formats numbers and dates to this]
- **Plugin version:** [x.y — the Agent Attraction Brain version that last touched this brain]
- **Brain created:** [Month Year] · **Last full review:** [Month Year] · **Last synced:** [date, or "never"]

## Connectors this Brain uses
*Setup confirms these. A skill that needs one and finds it missing tells the member to connect it rather than
failing silently. Google-world members use the Google rows; Microsoft-world members use the Microsoft 365
connector for storage + email + calendar (`shared/connectors.md`). Email is draft-only on both providers, always.*

- [ ] **Google Drive** *(google)* — the Brain's permanent home
- [ ] **Gmail** *(google)* — the Daily Debrief reads it; follow-up drafts land here *(draft-only — it cannot send)*
- [ ] **Google Calendar** *(google)* — the Daily Debrief reads today's and tomorrow's calls
- [ ] **Microsoft 365** *(microsoft)* — OneDrive + Outlook Mail + Outlook Calendar in one connector *(write actions: [enabled / org-gated / untested])*
- [ ] **CRM connector** — [name, if their CRM has one; otherwise exports land in `06 · Materials`]
- [ ] **Zoom** — meeting links on partner calls *(optional; Google Meet / Teams is the fallback)*

## Later plugins register here (one block each, written by that plugin's setup; the Brain never edits them)
*An empty or missing block means "not installed yet", never "broken". Headings and keys are locked by each owner's `shared/brain-contract.md`:*
- `## MAA Support (Plugin 2)` — `Support: set up [date]` · `Cohort start` · `Support desk: attraction` · `Portal` (plus the setup's own lines: `Off weeks` · `Graduation` · `Fast-action buyer` · `Configured` · `Snapshot at setup`)
- `## Short-Form (Week 3)` — `Installed` · `Plugin version` · `Layer: identity/publishing.md` · `Weekly Content Performance task` (`not offered yet` → task id · `declined`)
- *AI Editor, Riverside (Week 3)* — registers no block; its state lives under `editor/` inside the sync allowlist
- `## YouTube (Week 4)` — `Installed` · `Plugin version` · `Layer: identity/channel.md` · `Monday Kickoff task` · `Weekly ideas task` · `Monthly review task` · `YouTube section` (+ `Monday Kickoff delivery: email draft` if chosen)
- `## Conversion & Sales` — `Call Block Prep task` · `Call Block Prep time` · `Cold-Lead Reactivation task` · `Booking page` · `Partner call length` · `Setter`
- `## AI Admin (Week 5)` — `AI Admin: set up [date]` (the stamp, first line) · `Assistant name` · `Morning Brief task` · `Morning Brief time` · `Daily Follow-Up Queue task` · `Follow-Up Queue time` · `Weekly CEO Review task` · `CEO Review slot` · `Monthly KPI Review task` · `KPI Review day` · `Team Wins Newsletter task` · `Newsletter slot` · `CRM mirror` · `VA`
- `## Lead Magnet (Week 6)` — `Installed` · `List tool` · `Live data`
- `## Events (Week 6)` — `Installed` · `Plugin version` · `Member code` · `Registration host` · `Post-Event Follow-Up task` (`not offered yet` → `ev-post-event-follow-up · armed for YYYY-MM-DD 9:00` · `declined` · `later`) — created by `ev-navigator` on its first run; no timezone here
Timezone is never stored in any block — it lives in the registry above, once.
