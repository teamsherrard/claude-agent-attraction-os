DEMO BRAIN — fictional member, illustrative data — never publish.

# Exports — session staging only (your real documents live in your workspace)

This local folder is just **temporary staging while a document is being built**, plus the archive of prior
quarters' goals. It is wiped when the session ends — nothing durable lives here.

**Your finished documents live in your cloud workspace** (Google Drive or OneDrive), in the folder each one
belongs to: your Agent Attraction Brain Book and your 90-Day Attraction Scorecard in `01 · AI Brain`, your
brand kit in `02 · Brand`, content in `03 · Content`, prospect research and your organization's documents in
`04 · Agents`, your offer documents in `05 · Offer`. Ask for any document and it gets fetched, or you get told
exactly where it is.

These are polished *outputs*, not the source of truth — the canonical data lives in the Brain's
`identity/` and `memory/` files, so any document can always be regenerated.

**Demo note:** the renderer inputs used for the demo renders are kept here on purpose
(`brain-book-DEMO-2026-11-02.txt` — the nine-section Brain Book in the **Week-1 state** the member holds at the end
of Setup (the spec's STATE RULE: no offer row, the forward opener in Section 4, three bullets in Section 9, one demo
line under each `SECTION` band, no `--accent` because the brand chat has not run in that state): `--title "Taylor's
Agent Attraction Brain Book" --subtitle "Taylor · Austin, TX" --eyebrow "Agent Attraction Brain · Demo"`;
`scorecard-DEMO-2026-10-08.txt`; `partner-offer-DEMO-2026-10-18.txt` — the Partner Offer in the readable shape of
2026-10-18: `--title "The Sunday Table" --subtitle` the UVP line `--eyebrow "Partner Offer · Demo" --accent 1F4D3A`)
so each render can be reproduced with `plugins/attraction-ai-brain/shared/render_doc.py`. The rendered `.docx`
files are one folder up in `docs/demo/`. The older eighteen-chapter demo Books (2026-10-08) and their inputs were
removed on 2026-11-02 — the Book is nine sections now. The gate's executable half lives with the renderer:
`python3 plugins/attraction-ai-brain/shared/measure_book.py "<book.docx>"` prints per-section words against the
targets and maxima, the page estimate and every machine check (it moved out of this folder on 2026-11-02). The
rhythm line in Section 7 is the setup arithmetic on the demo's numbers (25 in 12 months → a first-quarter target of 4 →
about three conversations a week at the default ratios), rendered as proposed — the locked plan in `goals.md` is a
later-week fact the Week-1 state does not show.
