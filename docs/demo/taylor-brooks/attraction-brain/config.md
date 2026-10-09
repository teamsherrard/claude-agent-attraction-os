DEMO BRAIN — fictional member, illustrative data — never publish.

# Config
*operational settings for this member's Agent Attraction Brain — the one key registry; every skill reads these exact keys*

## Registry (locked spelling — `shared/brain-contract.md`)
- **Schema:** aa-1.0  *(structure version — the template, this line, and `attraction-brain-migrate` always agree; migrate pushes after it bumps this)*
- **Storage provider:** google  *(demo — simulated; this demo Brain has no live connector)*
- **Workspace name:** Agent Attraction OS — DEMO
- **Workspace ID:** demo-no-workspace  *(demo — this Brain lives in the repo at `docs/demo/taylor-brooks/`; a real build captures the folder ID at first sync)*
- **Workspace link:** none (demo — no cloud workspace)
- **Timezone:** America/Chicago  *(timezone lives here and only here)*
- **CRM:** other — a Google Sheet named "Agent tracker"  *(the system of record for contacts; the Brain's ledgers are the AI's working memory, never the CRM)*
- **Setup progress:** complete  *(resume reads this stamp — a stamped fact beats inference)*
- **Debrief time:** 6:00 pm, America/Chicago
- **Daily Debrief task:** declined  *(demo brains never get a scheduled task — "set up my daily debrief" switches it on for a real Brain)*
- **Workspace shared with:** nobody
- **Realtor Brain bridge:** none
- **Demo brain:** yes  *(Taylor Brooks is a fictional demo member — `shared/brain-book-spec.md` DEMO BRAINS; this Brain never mixes with a real one)*
- **Cohort week:** 1  *(demo — the later-week files are filled so the demo shows the finished product)*

## Supporting fields (not registry keys; mechanics only)
- **Brain home (permanent):** the workspace's `01 · AI Brain/_engine/` in a real build. Demo: `docs/demo/taylor-brooks/attraction-brain/` in the repo.
- **Owner account:** none (demo)
- **Locale:** USA · USD · sq ft — every skill formats numbers and dates to this
- **Plugin version:** 0.1.0 — the Agent Attraction Brain version that last touched this brain
- **Brain created:** September 2026 (setup completed 2026-09-29) · **Last full review:** October 2026 (Book regenerated 2026-10-08) · **Last synced:** never (demo — local only)

## Connectors this Brain uses
*Setup confirms these. A skill that needs one and finds it missing tells the member to connect it rather than
failing silently. Google-world members use the Google rows; Microsoft-world members use the Microsoft 365
connector for storage + email + calendar (`shared/connectors.md`). Email is draft-only on both providers, always.*

- [x] **Google Drive** *(google)* — the Brain's permanent home *(demo — simulated)*
- [x] **Gmail** *(google)* — the Daily Debrief reads it; follow-up drafts land here *(draft-only — it cannot send)* *(demo — simulated)*
- [x] **Google Calendar** *(google)* — the Daily Debrief reads today's and tomorrow's calls *(demo — simulated)*
- [ ] **Microsoft 365** *(microsoft)* — not used
- [ ] **CRM connector** — none; the Google Sheet is exported to `06 · Materials` on request
- [ ] **Zoom** — meeting links on partner calls *(demo: Zoom is the call room; Google Meet is the fallback)*

## Later plugins register here (one block each, written by that plugin's setup; the Brain never edits them)
*Short-Form (Week 3) · AI Editor (Week 3) · YouTube (Week 4) · Conversion & Sales (Week 5) · AI Admin (Week 5) ·
Lead Magnet (Week 6) · Events (Week 6). An empty block means "not installed yet", never "broken".*

## Short-Form (Week 3) — demo
- **sf-setup:** content pillars written 2026-10-06 (demo) · keyword: ROUTINE · posting tool: manual
