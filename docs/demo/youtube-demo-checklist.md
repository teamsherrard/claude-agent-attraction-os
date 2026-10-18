# YouTube plugin — demo checklist (v0.12.0)

Run it on the demo Brain (Jack Smith) in Cowork. Everything the member hears is in bold; everything you check is a box.

## Before you start
- [ ] Marketplace re-synced in Cowork (claude-agent-attraction-os at v0.12.0 or later).
- [ ] Notion connected in Cowork (step 3 builds the board there; without it the plugin only explains how to connect).
- [ ] Google Drive connected (the Game Plan and the channel kit are saved to the workspace).
- [ ] Jack's Brain has its offer built (the Week 2 Partner Offer) so the channel copy and the CTAs read from a real program and a real lead magnet. If it isn't, the kit uses the Starter Resource fallback and says so.
- [ ] A fresh chat in the demo project.

## The run (one phrase, five steps, two "your turn" moments)
1. **Say:** `set up my YouTube for agents`
   Expect: a two-line hello, "Here's what I'm working from" (name, who he attracts, the method, the resource, the booking link), then the ONE question: *Do you already have a YouTube channel? Paste the link, or tell me you're starting fresh.* **Your turn.**
   - [ ] It did not ask anything the Brain already knows.
2. **Say (as Jack):** `starting fresh` (or paste a channel link to show repair mode)
   Expect: *Okay, cool, now I'm going to optimize your channel…* then the Channel Page Kit as copy-paste blocks: about text, playlists by lane (Problem · Situation · Future · Interview · Model), the banner brief, upload defaults, the two-CTA line, the channel trailer plan. Saved to Drive.
   - [ ] The copy mentions Jack's lead magnet and booking link, not placeholders.
3. Expect, with no input from you: *Okay, cool, now I'm going to build your YouTube Game Plan…* then the Game Plan document (the three niche lanes, the 8-video cycle, titles with dates, the WHY statements, the 90-day calendar). Saved to Drive.
   - [ ] One document, dated, with titles in Jack's niche (agents on the lead treadmill), none about buyers or sellers.
4. Expect, with no input from you: *Okay, cool, now I'm going to build your content board and put your next 30 days of videos on it…*
   Expect: the Content Dashboard found or created in Notion, a Long-form view, 4 to 9 Idea cards dated inside the next 30 days including interview slots, and a count-check line (*your next 30 days — N videos ✓*).
   - [ ] Open Notion on screen: the board exists, cards carry Pillar, dates, the two CTAs.
   - [ ] If Notion isn't connected it says so in plain words and keeps the calendar in the Brain; it does not stop.
5. Expect: *Okay, cool, now I'm going to set up your weekly workflows…* then the consent card: Monday Kickoff (on, Mondays 9:00), the Friday performance note's YouTube section, the Monthly Channel Review (off). **Your turn.**
   **Say (as Jack):** `yes` (or `yes, but Mondays at 8`)
   - [ ] It confirms what's on and when. On a demo Brain nothing is actually scheduled; it says so.
6. Expect: *Okay, cool, now let's make your first video.* It names the first title on the plan and the board and tells you the phrase.

## The first video (the second screen of the demo)
7. **Say:** `make my attraction video: [the title it named]`
   Expect: the competitive read, the script, the thumbnail brief, the SEO package, the lead step, written into the board card (Status → Scripted) and the Drive folder. The card is the whole video.
   - [ ] Show the Notion card filled before filming.

## Optional moves if there's time (each one phrase)
- `what attraction video should I film` — the ranked batch of ideas (Jack's own ideas first, then the Brain's signals, then research, the starter bank last).
- `run my attraction kickoff` — the Monday Kickoff on demand: this week's video drafted onto its card and 30 days topped up on the board.
- `update my attraction video board` — the rolling 30-day top-up.
- `SEO for my attraction video` — the description, chapters, tags, pinned comment for a given video.
- `thumbnail brief` — the brief you paste into Brand HQ in Claude Design.
- `repurpose my attraction video` — shorts, posts, and conversation starters (hands the starters to Conversion).
- `which videos brought me agents` — the analytics read (Composio connected) or the Studio-numbers path.

## If something looks off
- It asked a question the Brain answers → note it; that's a bug to report.
- No board step → Notion not connected; connect it and say `build my attraction content board`.
- The consent card names a skill or a task id → bug; it should only say "your Monday Kickoff", "your Friday note", "your monthly review".
- Titles about buyers, sellers or listings → bug; the channel is built to attract agents only.
