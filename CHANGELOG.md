# Changelog

All notable changes to the Agent Attraction OS marketplace. Versions are per plugin; the repo `VERSION` is the marketplace release.

## [0.38.1] — 2026-11-21

**A correction to the README and to the Support desk's stack map — behaviour unchanged (Support 0.2.9).** Both still said the marketplace carried only Plugins 1 to 3, with the rest parked on the wip branch. Plugins 4 (Short-Form), 5 (The AI Editing Studio) and 6 (YouTube) have been on main since 2026-11-14 and the registry lists all six; a member reading either text would have thought the editor was not out yet.
- The README callout now reads "Available in the marketplace today: Plugins 1 to 6", names the Design Studio as an uploaded skill set rather than a plugin, and gives each plugin's install week (1 and 2 in Week 1, 3 in Week 2, 4 and 5 in Week 4, 6 in Week 5).
- **Support 0.2.9:** the stack map's lead-in says the same — Plugins 1 to 6 carried, 7 to 9 parked and "coming". Its plugin table and the "What changed lately" rows were already right and are unchanged.

## [0.38.0] — 2026-11-21

**The editor plugin has a new name — The AI Editing Studio — and a readiness round (Editor 0.6.1 · Support 0.2.8).** The editor is one plugin with two engines (Riverside, or Instagram's free Edits app on the member's Mac), so "Riverside" no longer belongs in its id. The plugin is now `realtor-ai-editing-studio` and its listing reads "The AI Editing Studio (Plugin 10)". The skills, their phrases and the member's saved settings are unchanged.

**What a member who already installed it does, once:** open Customize → Plugins, remove the old editor plugin (its id was realtor-riverside-editor; its listing began "The AI Editing Studio - Riverside"), and install "The AI Editing Studio" from this marketplace. The editor's settings, brand block and checkpoint logs live in the Brain, so nothing has to be set up again ("set up my video editor" only confirms what is there). A member installing for the first time is not affected.

**Editor 0.6.1** (vendored from the realtor marketplace's 0.6.0, with exactly the two documented downstream patches re-applied; the folder, the marketplace entry, the release gate and the vendor script all follow the new id; the version stays one patch above the source)
- **A 33-point readiness audit applied across the skills and shared references:** limits that only belong to Riverside are now scoped to Riverside; every quality-gate blocker names its proof on Edits (a rendered frame or the exported file) as well as on Riverside; the long-form and trailer lines now have their Edits version; Edits trigger phrases ("edit this in Edits") are on the director skills; setup asks only the questions that engine needs.
- **The Edits reel builder keeps a checkpoint log**, takes a start and an end for a span of the recording, and resumes a stopped run without being told the clip again.
- **The example config no longer carries a block for the retired editor.**
- **One downstream trim:** the source's `studio-publish` description is 1,030 characters; here it is 981 (the "usually reached through the navigator" tail is dropped), because claude.ai cuts at 1,024.

**Support 0.2.8.** A new row in "What changed lately" (the new name, remove the old listing and install the new one once, settings untouched), a sentence on it in FAQ Q81, and the stack-map's Plugin 5 row.

**Not yet run live in Cowork.**

## [0.37.0] — 2026-11-21

**The editor gains a second engine: Instagram's free Edits app for Mac (Editor 0.5.1 · Support 0.2.7).** The AI Editing Studio (Plugin 5, Week 4) is still ONE plugin with the same 28 skills — now a member picks the engine that does the rendering. Riverside works exactly as before. The new engine is Instagram's Edits app on the member's own Mac: free, no per-edit fees (the only cost is their Claude plan), driven from Claude Code on that same Mac. It exports the finished video and never posts or schedules; the member shares it, or the Short-Form plugin's posting tool takes the file. It does not run in Cowork, on claude.ai, on an iPad or on Windows.

**Editor 0.5.1** (vendored from the realtor marketplace's 0.5.0 by `scripts/vendor-riverside.sh`, with exactly the two documented downstream patches re-applied: the Brain-home patch and the plugin description trimmed under 1,024 characters; the version is one patch above the source, as before)
- **Setup asks one question — which engine** (`default_engine`: `riverside` or `edits`) — and connects it: Riverside as before, or the Edits install on the Mac. Saying an engine's name in a request always wins ("edit this in Edits"); "switch my editor to edits" changes it. "set up my video editor" and "set up riverside" both still start setup.
- **26 of the 28 skills carry an Engine section** (setup and the navigator handle the engine choice themselves), so the same craft rules (clean cut, hook, captions, music, B-roll, brand graphics, quality gates) run on either engine; the new references `edits-engine.md`, `edits-tool-map.md`, `edits-catalogs.md`, `edits-quirks.md`, `edits-grade-strategy.md` and `edits-tool-reference.md` say how each craft is done on Edits.
- **New `scripts/edits/` folder** (Python 3, standard library only, plus two small Swift helpers): the reel builder (plan, build, resume), the driver, the card renderer and the frame measurer. Edits runs are checked on rendered frames and the exported file, the way Riverside runs are checked on revision diffs.
- **Edits limits stated plainly:** no stock search inside Edits' server (own footage under the Movies folder, or free stock downloads with an optional free key); only royalty-free songs export with sound, so the music skill checks the licence flag first.
- The compliance wording still names both setup phrases ("set up my compliance" / "set up my attraction compliance"), and the Brain-home rule still resolves `~/attraction-brain/` first.

**Support 0.2.7.** One short entry for the engine choice: the stack map (the Plugin 5 row, a "Two engines" note and a new row in "What changed lately"), FAQ Q81 ("Do I have to use Riverside? Can I use Instagram's Edits app?"), a line in Q11 (costs) and Q20 (where an Edits project lives), and the cohort notes.

**Docs.** The README plugin table and the setup guide's Week 4 lines.

**Not yet run live in Cowork** (the Edits engine is not reachable from Cowork by design — it is a Claude Code on a Mac path).

## [0.36.1] — 2026-11-17

**A correction to 0.36.0's own wording — the behaviour is unchanged (Short-Form 0.9.1 · YouTube 0.8.4 · Support 0.2.6).** 0.36.0 said the owner had been shown a made-up line on a question card in a live run. That was wrong: the owner was reading the Member Journey Map, where the Week 4 Game Plan step was described as "Builds the thirty-day plan and the ManyChat build sheet". The sitting still asks one question, in plain chat, and makes no ManyChat build sheet. What changed:
- The setup skill and the house rules no longer cite an incident that did not happen; the plain-chat rule is attributed to "told, not asked" (no menus), in the short-form and the YouTube setups.
- The support plugin no longer tells a member that a pop-up with choices, or that line, means an older version. A question about "off the clock" is the one true sign.
- In the sitting the plan has one name, **Game Plan** ("say Yes and I'll build your Game Plan on it — your next thirty days of posts").

## [0.36.0] — 2026-11-17

**One question, in plain chat: the "off the clock" question is gone, and so is the ManyChat build sheet from the Week 4 sitting (Short-Form 0.9.0 · YouTube 0.8.3 · Support 0.2.5 · Brain 0.9.20 · Lead Magnet 0.12.16).** The owner read the Week 4 sitting through. Its first question, *"What do you do off the clock that the people around you know you for?"* — "makes no sense remove it" — and the Game Plan step, described as *"Builds the thirty-day plan and the ManyChat build sheet"* — "what is this? I don't think we need this." (Corrected in 0.36.1: this entry first said the owner had seen that line on a question card in a live run. They had read it on the Member Journey Map.)

**Short-Form 0.9.0**
- **The sitting asks ONE question — the filming day.** *"Which day could you film every week — about an hour, in the same spot — and where is that: your office, your kitchen, your car?"* The "off the clock" question is deleted from the setup, the Game Plan and the house rules: no skill asks it, in any wording, and none asks who the member is, what they like or what they are known for. The Personality pillar is built from the Brain (life outside real estate, the "before real estate" line, the story bank) and read back with the other four for a Yes or a change; where the Brain holds little it is labelled a first draft. An answer a member already gave to an earlier version is kept and still used, and is never asked for again.
- **Plain chat only.** The question, every "Say Yes" line and the opening pick are sentences in the reply — never a question card, a pop-up, buttons or a multiple-choice box, and never a question tool. A menu is what "told, not asked" rules out, and a card needs options. The sitting keeps no task list of its own either.
- **No ManyChat build sheet in the sitting.** It is no longer written or handed over after the Game Plan, and the words "build sheet" are no longer said to the member. ManyChat is one plain line in the plan and in the close — set it up this week — and "set up my ManyChat" writes out the steps when the member asks.
- **The first Reel is the one that teaches the member's own method** (it was the Reel built on the off-the-clock answer).
- The welcome ("just one new question — which day you can film"), the resume lines, the close ("You chose your filming day…") and the completion checklist all say one question.

**YouTube 0.8.3.** The same plain-chat rule in the Week 5 sitting. Its two questions are unchanged.

**The shared ask-once rule** (word for word in four plugins — the reason the Brain and the Lead Magnet plugin carry a new number): the content sittings ask only blanket questions, one in Week 4 and two in Week 5, in plain chat.

**Support 0.2.5.** The stack map, a new row in "What changed lately", the FAQ (the setup questions and the ManyChat answers), tree #13, the doctrine and the cohort notes: one question for short-form; a question about "off the clock" is the sign of an older version; "set up my ManyChat" is the phrase for the ManyChat steps.

**Docs.** The setup guide and the short-form demo checklist.

**Not yet run live in Cowork.**

## [0.35.0] — 2026-11-16

**The Design Studio catches up: every design skill waits for a Yes, and nothing is designed as if the member already has agents (the ten `aa-…-design` skills · Support 0.2.4).** The owner asked for the Claude Design skills "based on all the updates that we've made so far". An audit of the ten found them untouched since 0.28.0 — and found that five of them still built their whole set in one go, the same "it did it all without me" the owner had named in the Cowork sittings.

**The shared craft standard (`craft-standard.md`, word for word in all ten skills).**
- **The one checkpoint is now in the order of work for every set-building run** (the owner, 2026-11-15: "it should WAIT for me to give direction or feedback"): build the master or two, show them, and stop — *"These two set the look for everything else. Say Yes and I'll build the rest — or name the one change. Your turn."* A change is re-rendered and shown, and the skill waits again. On the Yes the rest is built without another stop. Where a skill or a reference still says "the turn never ends at a checkpoint", that now means its internal stages after the Yes.
- **The win line and the close** (the owner: "the student also needs to feel a WIN"): the reply after a Yes, a pick or a change opens by saying what the member decided; after the finished set the close names what they did and one first use that takes minutes.
- **Never design as if the member already has agents** (the owner, 2026-11-16: "a lot of people in this group… have never attracted an agent in their life"): a welcome post, a win post, a milestone, a team photo or a testimonial is a ready template until the Book records someone, and is called that; never an invented agent, name, photo, number or quote; "the agents you want to attract"; a kit may carry one keyword, and one is what gets designed.

**The five skills that never stopped now have their checkpoint.** The brand kit (after the YouTube banner and the first post — for a member with nobody on their team yet, their welcome-post template), the lead magnet guide (after the cover, page 1 and one inside page), the opt-in page (after the hero, desktop and mobile), the video kit (after the first preview sheet) and the event set (after the feed flyer). The offer kit, the posts and the Value Vault already had it; the logo and the style sheet already open with a choice.

**Smaller.** The brand kit's "thumbnail master" is described as what it is — a look reference; each video's thumbnail is made in Higgsfield. "Drop a photo of your agents" reads "a photo from your next training or open house". The event hand-back has a form for a member with no agents to share the flyer. The Start Here page opens with a dated "what is new" line and says to replace an older set.

**Support 0.2.4.** The Design Studio notes, the known modes ("it made one or two pieces and stopped" · "it built everything without showing me first" = an older set · "my welcome post has an empty photo frame"), a row in "What changed lately", and FAQ Q80.

**The ten upload files are attached to this release.** Not yet run live in Claude Design.

## [0.34.2] — 2026-11-16

**Two read-throughs as a first-time attractor: what a member with no agents, no bios, no kit and no board would have heard (Short-Form 0.8.2 · YouTube 0.8.2 · Support 0.2.3).** Each read-through played two members through the whole sitting: the demo member, and someone who has never attracted an agent. The two questions held — nothing else is asked. What was wrong were sentences around them.

**Short-Form 0.8.2**
- **"Your bios are already written" was said to members with no bios.** The test was whether the profiles file exists, and the Brain creates that file empty in Week 1. It now tests for a real bio. The same for the setup stamp, which the Brain also scaffolds.
- **Proof for a member with no agent wins yet.** The proposal promised "your own results for now", but the Game Plan had no rule to build it from. Proof is now built from the member's own results, their method working in their own business and what they are building in the open — never "you have no proof", never an invented win.
- **"Two words" to a member with one, "your board" to a member without Notion, "six designed posts" to a member without the kit** — each remaining line (the welcome, the plan hand-over, the consent card, the board's count line, the close) now has its true form. The step count stays whole without a board ("Step 3 of 5 — your thirty days are safe in your Game Plan").
- **The first script** no longer points at a calls-to-action table or a pop-up set the member does not hold, and no longer says "with your keyword on the end" for a Reel whose ask is "follow".
- **"Update my pillars" asks nothing new.** It used to fill an empty pillar "one plain question at a time" — for a first-timer's Proof pillar that could only be "who have you helped?". It now rebuilds from the Brain and reads it back.
- **The welcome is a numbered list of the five steps**, in the same words the "Step n of 5" lines use, with "two questions, the same two every member gets" on its own line. The owner: "I'm still kind of confused with this process."
- "Does that sound like you?" is now a statement — "If that sounds like you, say Yes…" — so a sitting that promises two questions asks two. "Sign in" lines say a free account can be made in the same window. The welcome-or-win-post clause is said only to a member who has someone on their team. `unknown` on the join register reads as join in every line.

**YouTube 0.8.2**
- **The plan a first-timer opens no longer tells them to "invite the first agent you have helped".** With nobody on file: the first-week line keeps a place for a conversation and names the phrase; the guest table is one honest paragraph (the next agent they help, a winner from their upline's team, a peer); conversation rows read "guest to be named"; the playlist is "Conversations with agents", not "Agent success stories"; the close's third step does not say "invite your first guest".
- **Question 2 is now truly blanket:** "Which day could you film a full video every week — about an hour?" The remark about Reels is gone from the question (a member who skipped Week 4 has none).
- **The member's filming day is the rule itself**, not a patch beside it: the first-date rule and the 90-day phase read `Filming day:` first, so a later refresh or pace change keeps their day.
- No board: the announce line, the workflows card, the confirming line and "fill its card" each have a form that is true. A new channel: every "first video" line says which video it means (the trailer first). "Your two calls to action" is not printed above a block that holds one. The welcome is a numbered list.

**Both:** the phrases to come back or start again are now "continue my attraction short-form" · "redo my attraction short-form" · "continue my attraction YouTube setup" · "redo my attraction YouTube setup" — the word "attraction" keeps them out of the realtor plugins on a machine that has both.

**Support 0.2.3:** the same phrases and wording in the FAQ, the stack map and tree #13.

**Not yet run live in Cowork.**

## [0.34.1] — 2026-11-16

**Nothing speaks as if the member has already attracted agents (Short-Form 0.8.1 · YouTube 0.8.1 · Support 0.2.2 · Brain 0.9.19 · Lead Magnet 0.12.15).** The owner's worry on 0.34.0 was the first-time attractor: "a lot of people in this group… have never attracted an agent in their life." A read-through that plays such a member found the questions were now blanket, but some sentences were not.
- **The welcome's play-back** said "you attract [type]" and "you're known for [X]" as facts. It now reads "your story speaks to [type]; you want to be known for [X]" — the Brain's own words for those two fields — for every member. YouTube: "you're here to help [type]…".
- **"The agents you attract" is now "the agents you want to attract"** wherever a member reads it, in both plugins, the setup guide and the shared `how-we-speak.md` (four plugins). "LinkedIn… because you attract team leaders" reads "because team leaders are among the agents you want to attract".
- **A rule in both setups and both house-rule files:** never a sentence that assumes the member has attracted agents, has a team, or has agents they have helped; such a line is said only when the Brain holds one, and otherwise takes its honest other form — never a gap list, never an apology for being new.
- **The profiles step says a missing piece once, not three times.** No bios, or one keyword, is named once in the "Step 1 of 5" line with the phrase that creates it.
- **Keywords:** when the offer's word is also GUIDE the line reads "Your word is GUIDE — it sends your guide and opens the conversation" (it used to print GUIDE twice); a built offer with no word of its own is pointed at "refine my partner offer", not told to build an offer it already built.

**Not yet run live in Cowork.**

## [0.34.0] — 2026-11-16

**Two blanket questions, the same for every member (Short-Form 0.8.0 · YouTube 0.8.0 · Support 0.2.1 · Brain 0.9.18 · Lead Magnet 0.12.14).** The owner ran the short-form sitting live and it asked: *"You attract agents one to four years in… When one of them gets you on the phone, what's the first thing they ask you?"* The owner: *"this worries me… the questions could be different for each person, depending on what their situation is. There are a lot of people in this group that are first-time agent attractors, and they've never attracted an agent in their life. What would the question be in their situation? We need to make sure that they're blanket questions and the questions are the same across the board. Also, we don't really need more questions because they've already gone through a lot of this when they were building their AI brain."* The four-question interview added in 0.31.0 and 0.32.0 is replaced.

**The rule now, in both sittings.**
- **Exactly two questions, word for word the same for every member**, in the same order — nothing from the member's Brain is built into the question, and there is never a third.
- **A question must pass three tests:** every member can answer it, including one who has never attracted an agent · the Brain does not already hold it · the plan cannot be built without it.
- **Never a question that assumes experience** — what agents say to them, who they have helped, who they would sit down with.
- **Everything else is built from the Brain and read back** for a Yes or a change, each piece with where it came from ("from the story you told in Week 1"). That is how the member stays part of every step without a second interview.
- One step a reply, the win line, "your part" and the stop are unchanged. "Skip" still always works.

**Short-Form 0.8.0 — the two questions.** *"What do you do off the clock that the people around you know you for? Only what you're happy to have on camera."* (the Personality pillar — the one thing the Brain never asked) and *"Which day could you film every week — about an hour, in the same spot — and where is that?"* (the filming day). Then the five pillars are shown, each with where in the member's own Brain it came from, and the week; "Does that sound like you?"; then the plan. The questions about what agents ask them and about the first step of their method are gone — the Brain holds both. The first Reel is the plan's first Reel; the member still chooses how it opens. `sf-talkinghead` no longer asks a question before a script (it closes with "tell me how you'd open any of these and I'll rewrite it around your words"). The close no longer counts answers.

**YouTube 0.8.0 — the two questions.** *"Your channel covers three topics — they're the playlists on your Channel Page: [A], [B] and [C]. Which one could you talk about for twenty minutes with no notes?"* and *"Which day could you film a full video every week — about an hour? The same day as your Reels is fine."* The questions about who they would sit down with and which story to tell are gone: a guest is named in the plan only when the Brain already holds an agent they have helped (otherwise the plan says it starts the day they name someone), and the story comes from the Brain. `yt-script` no longer asks a question before a script, and "script my first three videos" writes all three again.

**Also in YouTube 0.8.0 — the rest of its walk-through** (a fresh reader followed the sitting reply by reply).
- **The member's filming day now drives every date.** It was saved but never read; the dates still came from the old rule. It is written to `channel.md → Filming day:` the moment it is given, and the first-date rule reads it first in all seven places.
- **Nothing is claimed that is not so:** no "your board is done" or "drafted on its card" for a member without Notion; no "there's a real video on your first card" when none was found; the Kickoff's "keeps your board 30 days ahead" is said after the Yes that switches it on, not before.
- **A new channel:** the first row of the plan is the trailer, so the topic the member picked is "your first full video" everywhere, not "your first video".
- A guest with no story on file is titled "A conversation with [first name]" instead of an invented transformation. Answering a skipped question later rebuilds only that video and moves no date. A skipped entry is never quoted or marked "your words". The workflows' confirming line is said once.

**Both setups:** "continue my short-form setup" and "continue my YouTube setup" are trigger phrases, and the sitting says so once, so a member who stops part-way knows how to come back.

**Shared `ask-once-default.md` (four plugins):** its last section is now "The content sittings ask two blanket questions". **Brain 0.9.18:** the channel template carries `Filming day:`.

**Docs and Support 0.2.1.** The setup guide (Weeks 4 and 5), both demo checklists, the stack map, the week guide, the doctrine page, tree #13 (the exact four sentences a setup may ask; "Question 1 of 4" means an older version) and FAQ Q69, Q70, Q71, Q74, Q75 and Q79.

**Not yet run live in Cowork.**

## [0.33.0] — 2026-11-15

**The support plugin catches up with everything, and both interview sittings are hardened by two independent walk-throughs (Support 0.2.0 · Short-Form 0.7.3 · YouTube 0.7.2 · Brain 0.9.17 · Lead Magnet 0.12.13).**

**MAA Claude Support 0.2.0 — a full pass against the plugins as they are today.** The owner asked for the agent-attraction support plugin to be updated for every change made so far. An audit of its 3,500 lines against the live skills found content that predated the last two weeks of changes, not only today's.
- **The interview, the waiting and the win** are now explained everywhere a member might ask: the stack map's notes for Plugins 4 and 6 (the order of each sitting, how every reply is built, what it asks and never asks, the known modes), the week guide for Weeks 4 and 5, the doctrine page (a new section, "Why the content setups ask questions and wait", with the one-breath answer and the picture for picture people) and the plain-language table.
- **A new troubleshooting tree, #13** — "my setup stopped, is asking me things, or did it all without me" — starting from the last line on the member's screen, and saying exactly which reports are the design working and which are defects to log.
- **A new table, "What changed lately — and what a member will notice"**, so support can answer "why is it different now?" and "my friend's didn't do this" (an older version: update the plugin).
- **FAQ:** seven new answers (Q73 "It stopped and says 'Your turn' — is it stuck?" · Q74 answering a skipped question later · Q75 where the answers go · Q76 a person, a brokerage or a number in an answer · Q77 "do it all" · Q78 changing an answer, a pillar, the pace or the filming day · Q79 "my setup is different from my friend's"), and four rewritten: Q17a (real numbers — "connect my YouTube numbers" and "how's my content doing", no weekly report that no longer exists), Q35 and Q43 (ManyChat: two keywords only, a Week 4 asset, the build sheet; the retired PARTNER / SCALE / GROWTH words are gone), Q36 and Q69 (the first batch writes one script a reply).
- **Every command a member is told to say was checked against the real skills.** Dead phrases replaced: "set up my short-form engine" → "set up my attraction short-form" · "optimize my profiles for agents" → "confirm my attraction profiles" · "how is my attraction content doing" → "how's my content doing" · "build my interview pipeline" → "build my agent interview pipeline" · "model breakdown video" · "thumbnail brief". New rows for "script my first three videos", "my video is published", "connect my YouTube numbers", "update my pillars", "refresh my attraction game plan", "redo my short-form setup" and "redo my YouTube setup".
- **Weeks corrected** to the map in force since 2026-11-14: short-form and the editor are Week 4 (several lines still said Week 3), YouTube is Week 5, Conversion & Sales and the AI Admin are Week 6, Events is Week 7; the vault's module-by-week summary; the scheduled-agent table (now with Batch Prep, the News Watch and the Calendar Refill).
- **Other stale lines:** thumbnails are a sheet for Higgsfield, never "a Claude Design brief"; the posting tool, ManyChat and Notion are part of the program, not "optional by design"; task lines read `later` or `paused`, never `declined`; the scheduled-agent tree now names the right switch-on phrase for each workflow and says truthfully that a short note IS emailed to the member's own address when their mail is connected.

**Short-Form 0.7.3 — the walk-through's remaining seventeen findings** (a fresh reader followed `sf-setup` reply by reply; 25 findings in all, eight fixed in 0.32.1).
- **Any posting pace is now defined** (the one serious gap). A member who says "two posts a week" at "Does that sound like you?" was promised it, but only three and five were defined. Now: the six designed posts go out first and last ⌈6 ÷ pace⌉ weeks; the Reels then rotate one that teaches · one story · one that shows who they are; the member's answered Reels take the first Reel rows; and every line that said "your first two weeks" uses the computed number.
- **Counts are true.** "Your own words in [n] of your five pillars" counts pillars (questions 1 to 3), never the filming-day answer, and matches the close; "You set your week" states the number the member chose, not the size of the calendar.
- **Nothing is claimed that is not so:** no "six designed posts" for a member with no kit (five lines); no "your board is done" for a board waiting on Notion, now or on a later visit; no "you switched on" on a demo Brain or after a "not now"; an opening the member only picked is "your pick", never "your words".
- **The consent card** answers a question or applies a change and asks again, instead of setting all four workflows aside for anything that is not a Yes. Its wording is plainer ("the page you read from while you film", "your filming day").
- **Resume** names the question to answer ("we're on Question 3 of 4") and never calls a skip an answer; a held bio no longer bypasses the interview.
- **The week is described in the pillar names the member was just shown**, not a second vocabulary. The Game Plan no longer repeats its own summary inside setup. "DM bank" is explained where it is first said.
- "redo my short-form setup" is now a trigger phrase.

**YouTube 0.7.2 — the first findings of its own walk-through** (still in progress).
- **Each of the four questions now asks ONE thing.** Three of them asked two ("which topic — and what's the first thing you'd say?"). Now: which topic · who they would sit down with · which story · which day. What the member would say first is asked where it is used, before that video's script is written; anything they volunteer is saved and used.
- A channel NAME on file with no link is played back and only the link is asked. A guide whose page is not live yet no longer leaves a placeholder link in a block the member pastes today. "Done" after pasting is recorded, so a later visit never tells them to paste again. Five pieces are left after the three, not six. House rule 12 now describes the interview. The 120-word guide applies to the short replies only. "redo my YouTube setup" is now a trigger phrase.

**Shared.** `ask-once-default.md`: inside an interview there is one question a reply and no follow-up after a pick.

**Not yet run live in Cowork.**

## [0.32.1] — 2026-11-15

**The first findings of an independent walk-through of the short-form interview (Short-Form 0.7.2 · YouTube 0.7.1 · Brain 0.9.16 · Lead Magnet 0.12.12 · Support 0.1.30).** A fresh reader followed `sf-setup` reply by reply for the demo member. What it found in the first four replies, fixed:
- **The welcome named things a member may not hold.** "Your offer, your guide, your six designed posts and your bios" was fixed text. It is now built from what is really on file, and dropped when fewer than two are there.
- **The profiles step claimed what it had just contradicted.** "Your bios are already written" and "your profiles and your two words are confirmed" were said even when there were no bios or only one keyword. The announcement and the "Step 1 of 5" line are now built from what the step found, and the duplicated "your profiles stand" sentence is gone.
- **"Pillars" and "hooks" were used before they were explained.** The first mention now reads "your five pillars (the five kinds of post you'll make) and the opening lines of your first Reels".
- **Question 2 asked two things and re-asked one of them.** The step the member would start an agent with is already in their Brain (`Teach first`), so it is played back and the question asks only for how they would say it — "a sentence or two", no longer "in a minute".
- **"I don't know" and "you pick" are a skip inside an interview** — the shared ask-once file said to offer options and ask for a confirm; its interview section now says otherwise.
- **A skipped answer can be given later.** "Update my pillars" (short-form) and "refresh my attraction game plan" (YouTube) now ask a skipped question first, and rebuild what it shapes on the answer.
- **YouTube: half an answer is an answer** — a topic with no first line, or a guest's name with nothing more, is taken as given.

**Not yet run live in Cowork.** The walk-through is still in progress.

## [0.32.0] — 2026-11-15

**The YouTube sitting is an interview too (YouTube 0.7.0 · Short-Form 0.7.1 · Brain 0.9.15 · Support 0.1.29).** The owner's ruling named both plugins: the short-form *and* the long-form YouTube plugin have to "feel almost like an interview" — the member "a part of making it happen". 0.31.0 rebuilt the Week 4 sitting; this release does the same for Week 5.

**YouTube 0.7.0 — the interview (`yt-setup` Step 6a, `yt-gameplan`, the house rules).**
- **Four questions, one per reply, numbered**, each asked after a line that plays back what is already on file: (1) which of the member's three topics they could talk about for twenty minutes with no notes — and the first thing they would say; (2) who they would love to sit down with on camera first, and what changed for that agent (a first name is enough); (3) which of their stories to tell at full length first; (4) their filming day, and whether one video a week is honest for them.
- **Nothing is asked twice.** Week 1's 26 questions and Week 4's four are never repeated: when the short-form answers are on file the sitting plays one back ("Last week you told me agents ask you '…' — people search for that, and it's going on your plan as a video") instead of asking.
- **Heard back, then put to work.** Each next reply opens with the member's own words, quoted, and what they became. The answers are saved verbatim and dated in a new section of the channel file, `## In your words`, pushed the moment they are given.
- **The plan is built on the answers.** The proposal shows the member's first three videos — their twenty-minute topic (video 1, its script opening on their own first line), their first guest, their story at full length — with their pace and filming day, then "Does that sound like you?"; nothing is researched or built before their Yes. In the plan document a video built on an answer shows "(your words)"; its board card opens with the member's own sentence.
- **The same rules of the asking** as short-form: about the member, never the machine · one question a reply · their words stay theirs (a named brokerage and any income figure left out of everything public; a guest is a first name and a candidate — never published, never contacted in the sitting) · "skip" always works and is never asked twice · a member who leaves after Question 2 comes back to Question 3.
- **After the sitting.** `yt-script` asks ONE question before a script written with the member in the chat ("if an agent asked you this over coffee, what would you say first?") unless their words for that video are already on file; "script my first three videos" now writes one script a reply, each from the member's own words. The Monday Kickoff reads `## In your words` and never asks.
- The welcome says "we build it together — it works like an interview"; the sitting is about forty minutes.

**Short-Form 0.7.1 — two skipped-answer cases.** When the member skipped the first question, the first Reel is no longer described as "the question you told me agents ask you"; when every answer was skipped, the direction line no longer claims their words are in the pillars.

**Brain 0.9.15.** The channel file's template gains the empty `## In your words` section.

**Docs and Support 0.1.29.** The setup guide's Week 5 section, the YouTube demo checklist (the four questions, the proposal) and FAQ Q70 and Q71 (both setups).

**Not yet run live in Cowork.**

## [0.31.0] — 2026-11-15

**The short-form sitting is an interview, and the member feels the win (Short-Form 0.7.0 · YouTube 0.6.1 · Brain 0.9.14 · Lead Magnet 0.12.11 · Support 0.1.28).** Three things the owner said after 0.30.0 made the sitting wait: *"we need to make sure there is a proper customer journey"*; *"the student also needs to feel a WIN that they did something to achieve the result"*; and that the short-form and YouTube plugins have to *"feel almost like an interview"* — the member *"involved… a part of making it happen and bringing that system, that product to life. That experience is a very important part of this process."* Waiting for a Yes is not involvement. This release rebuilds the Week 4 sitting around the member as the source.

**Short-Form 0.7.0 — the interview (`sf-setup` Step 3a, `sf-gameplan`, the house rules).**
- **Four questions, one per reply, numbered**, each asked after a line that plays back what the Brain already holds — so nothing from Week 1's 26 questions is asked again: (1) the first thing agents ask the member when they get them on the phone; (2) the one step of their method they would tell an agent to start with this week; (3) what they do off the clock; (4) the day and the place they can film every week (not asked when a filming day is already on file).
- **Heard back, then put to work where the member can see it.** Each next reply opens with the member's own words, quoted, and what they just became. The answers are saved verbatim and dated in a new section of the member's pillars file, `## In your words`, pushed the moment they are given — the Brain Board prints it with the pillars.
- **The plan is built on the answers.** The pillars are proposed with the member's words inside the pillars they answered for, then "Does that sound like you?" — nothing is built before their Yes. Each answer is angle one of its pillar; the three Reels built on them lead the calendar (the very first is the question agents ask them), carry `your words` in the calendar and show "(your words)" in the plan document; the board card of such a Reel opens with the member's own sentence.
- **The rules of the asking.** About the member, never about the machine (the 2026-11-14 ruling stands: no admin question, no menu, nothing about email, platforms, workflows or ManyChat) · one question a reply · typed or spoken, a sentence or two · their words stay theirs (tidied only to be sayable in one breath; a named brokerage or person and any income figure left out of everything public) · "skip" always works, is never asked twice and never draws a guilt line · at most one "say a little more" in a sitting · a member who leaves after Question 2 comes back to Question 3.
- **The member's part and the win.** Every reply after the first opens with a win line naming what the member just said or decided; every reply hands them one thing that is theirs (a question, a choice about their own content, or a two-minute action); the member chooses the opening of their first Reel (three options, or their own words) before it is scripted; the close opens with WHAT YOU DID TODAY — "You…" lines with real counts — and names the first win of the week, a designed post that only needs posting.
- **After the sitting.** `sf-talkinghead` asks ONE question before a script written with the member in the chat ("if an agent asked you this across the table, what would you say first?") — never in a scheduled run, never three in a chat. The Monday Week Plan and the Monthly Calendar Refill read `## In your words` and never ask; the Monday note opens with "Last week you got [n] of [m] out" when something went out; publishing a post is acknowledged ("✓ Your first one is out").

**YouTube 0.6.1 — the win lines and "your part"** on every step of the Week 5 sitting, the same close (what you did today; your first win), and "✓ '[title]' is published — that's your [n]th video out" when a video goes live. The YouTube sitting's own interview follows in the next release.

**Shared (all four plugins that carry it).** `ask-once-default.md` gains its last section, "The content sittings are interviews": told-not-asked is about the machine; the member's own content is asked for.

**Brain 0.9.14 · Lead Magnet 0.12.11.** The shared file above; the Brain's contract names `## In your words` and who may append to it.

**Docs and Support 0.1.28.** The setup guide's Week 4 section, the short-form demo checklist (the interview, the win lines, what a demo must not show) and FAQ Q70, the new Q71 ("Why is my short-form setup asking me questions?") and Q72 ("What does '✓ Step 2 of 5 — done' mean?").

**Not yet run live in Cowork.**

## [0.30.0] — 2026-11-15

**One step, then wait (Short-Form 0.6.0 · YouTube 0.6.0 · Support 0.1.27).** The owner launched the Week 4 short-form sitting, stepped away, and came back to find everything built — the profiles, the Game Plan, the board, right up to the workflows card: *"it ends up doing the entire work for me rather than waiting for me to give direction or feedback or answers… it should WAIT for me."* Both setup sittings are rewritten around that.

**The rule (`sf-setup`, `yt-setup`, both plugins' house rules; it wins over every older "no stop" line).**
- **One step per reply.** Each reply does one step, shows what it built or what it proposes, and ends on a stop line: *"Say **Yes** and I'll [the next step, in plain words] — or tell me what you'd change. **Your turn.**"* Nothing of the next step is read, built, saved or said until the member answers. A member who walks away comes back to exactly that line.
- **Direction comes before a big build.** What shapes a document is shown first and waits: the five pillars and the week before the Short-Form Game Plan; the three topics, the pace and the filming day before the YouTube Game Plan. The document is built on the member's Yes.
- **A change instead of a Yes** is made, shown (only what changed), saved, and followed by the same stop line. A question gets one plain answer and the stop line again. Silence is never a Yes.
- **Still told, not asked** (2026-11-14: "all that the student has to say is 'Yes'"). The stop is never a menu and never one of the old questions — no "all, some or not yet", no "want me to email you?", no platform or ManyChat question. The only word a member has to say is Yes — now at the end of each step instead of once.
- **"Do it all" / "don't stop"** runs the remaining steps without the stops, pausing only for the workflows card's Yes (and, in short-form, the posting-tool question) — only when the member says it; never offered.
- Each step still saves and stamps when it is built, so nothing is lost if the member leaves, and a later call opens on that step's stop line.

**Short-Form 0.6.0 — where it now stops.** After the welcome and the play-back ("Is that still right?") · after the profiles and the two words · after the pillars and the week are proposed (the Game Plan is NOT built yet) · after the Game Plan is built · after the board · the workflows card and its Yes · the posting tool · before the first Reel is scripted (the member can name a different one). `sf-gameplan` runs in two replies inside setup — Phases 1 to 3, the stop, then the build. "The one Yes" in the workflow tables now reads "the consent card's Yes", so no rule can be read as "only one stop". The house rule that a question is "2–4 related facts in one stop" is corrected to one plain question at a time.

**YouTube 0.6.0 — where it now stops.** After the channel question (or, with the channel on file, after the play-back) · after the Channel Page and its three pieces to paste · after the Game Plan's proposal (three topics, pace, filming day — nothing researched or built yet) · after the plan is built · after the board · then the workflows card and its Yes, and the close. The "about 350 words before the Yes" budget is replaced by "one step a reply, about 120 words outside the copy blocks". `yt-gameplan` starts only on the member's Yes and builds on what they approved or changed.

**Docs and Support.** The setup guide (Weeks 4 and 5), both demo checklists (each step's stop, and "two steps in one reply" added to what a demo must not show) and FAQ Q53, Q62 and the new Q70 ("It built everything while I stepped away. Can it wait for me?").

**Not proven yet.** Written from the owner's live run of the old behaviour; the new sittings have not been run in Cowork.

## [0.29.0] — 2026-11-15

**The YouTube plugin, audited by three independent readers and tightened (YouTube 0.5.0 · Short-Form 0.5.1 · Brain 0.9.13 · Support 0.1.26).** After 0.28.0 three read-only audits walked the plugin as the model that has to follow it — the setup sitting, one video's life from the Monday Kickoff to "my video is published", and the numbers, reviews and shared rules. They returned 75 findings; every one that was real is fixed here. One feature was added: the first batch.

**New: "script my first three videos" — the first batch.** The three videos a member films alone (interviews are booked, never batched) are scripted in one sitting: three different stories, three different ways of opening, the two calls to action in every script. Each script is saved in its video's folder and on its card; the three cards share ONE filming day while every publishing date stays on its own week; and a one-page film-day sheet says what to set up, what to change between videos and which five photos to take for the thumbnail. `yt-make-video` then builds the thumbnail sheet, the title and description and the publish checklist around a script it never rewrites, and reads "filmed or not" from the date instead of asking. Setup's close names the phrase in its second step.

**The reference video — what the audits changed.**
- **Clean the link first, then check it.** A raw search link (`watch?pp=…&v=[id]`) fails YouTube's check even for a real video, so real videos were being dropped; the two steps are swapped, and the usual card now costs one search and one check.
- **Nothing is claimed about a video nobody watched.** A search shows a title and a channel, not what is said inside. The competitive read, the outlier scan and "the one thing to do better" now speak about the title's promise unless the member pasted a transcript or described the video; a view count is written only when it was really seen (live numbers, a search result's own text, a screenshot). The outlier test is no longer run on counts that are not there: the member is shown the one-minute screenshot way instead.
- "Each has one real video to watch first — found on YouTube and checked." replaces "a close match", which overclaimed for a trailer or an interview slot; the card's own "Why this one" line carries the honest label. Inside setup the reference videos always take the search path.

**The Monday Kickoff — an unattended run that now agrees with itself.**
- **The pick.** `Scripted` meant three things, so the status alone no longer decides: already drafted this week → repeat that week's note and stop; a video to record this week → draft it; a video already packaged → say it is ready to film, never jump ahead; a first-batch script going out soon → finish what is missing and never touch the script; otherwise the next one forward.
- **One save, last.** The board is topped up before anything is saved, so the single push carries every row the run wrote.
- **The note cannot overflow.** Notices (no kit, no Notion, a failed save, no mail, a card taken off the board…) have one home — a bracket at the end of the first line, two at most — and never a line of their own. Two-video weeks and a check that cannot run are covered.
- **A card the member took off the board stays off.** Every run that creates cards records them (`carded:` under the calendar's Kickoff briefs), so a later run can tell "never made" from "removed"; a new card carries its calendar row's own ID.

**Live numbers — the last loopholes closed.** A deep dive or a read never puts a sign-in link or a click path in the middle of the job: it uses live numbers only when they are already active and otherwise ends with one line naming "connect my YouTube numbers". The contract, the house rules and both scheduled prompts now say the same thing — a scheduled run never calls the connection, whatever the `Live data:` line says — and the monthly review defines "numbers on record" once.

**Setup.** A word budget that can be met (about 350 words outside the three paste blocks, with a stated order of what to drop); one rule for a failed save; a welcome that does not promise a question when the channel is already on file; the three topic names chosen by the Game Plan's rule at the channel step and kept word for word by the plan; the first Kickoff's date read from the task itself; no promise of a tab order Notion cannot set on an existing board; the two scheduled tasks created with a plain title ("Your Monday Kickoff", "Your Monthly Channel Review") and the description the tool requires.

**Also.** Clips never add posts: four places that handed out "script my attraction reels from…" now point to the clip queue. The repurposing pack is written and held when compliance is unset, like every other skill. A model comparison names trade-offs only for the member's own model and never uses what agents who left have said. One set of script band names; the pinned comment always carries "comment GUIDE"; the publish checklist's thumbnail step mentions YouTube's Test & compare when all three were made.

**Lighter to run.** `doc-format.md` and `brain-contract.md` — the two longest shared files — now open with a reading rule: a skill reads the part it needs (its skeleton, its row, the shape it writes), never the whole file.

**Short-Form 0.5.1 · Brain 0.9.13 · Support 0.1.26.** The shared board spec and data engine carry the fixes above (identical in both content plugins); scheduled tasks get a plain title in the member's list; the Brain Board lists the first-batch phrase; FAQ Q69 ("Can I film several videos in one day?"), the setup guide and the demo checklist follow.

**Not proven yet.** Nothing here has been run live in Cowork. The audits read the files; they did not run a sitting.

## [0.28.0] — 2026-11-15

**YouTube, after a full simulated sitting and the owner's review (YouTube 0.4.0 · Short-Form 0.5.0 · Brain 0.9.12 · Support 0.1.25 · the Design Studio's style sheet).** The Week 5 sitting was run end to end for the demo member — the transcript, the Channel Page, the Game Plan, the board, a Monday Kickoff, a monthly review and one video — and everything it exposed is fixed here, together with five improvements and four owner rulings: thumbnails are made in Higgsfield, one real reference video on every card, a publish checklist on every card, and live numbers as a named step of their own.

**One real reference video on every card (the owner, 2026-11-15).** Every long-form card carries one real YouTube video, as close as possible to the card's idea, from the day the card is created — so a member watches a realistic example, and sees what other people who make videos for agents are doing, before planning their own. The board has a new `Reference Video` link column (the last column of the YouTube tab) and the card section is now `📚 REFERENCE VIDEO — WATCH THIS FIRST`: the titled link, the video playable on the card, "Why this one" with an honest label (closest match · close, not exact · for the format) and "Watch for". The research is a written recipe in `yt-research`'s method, checked against the real tools: a web search limited to youtube.com (typing `site:youtube.com` into the query returns articles, not videos), a check that the video is real and public before anything is written (YouTube's own oEmbed address returns the title and the channel; a missing video returns an error), a clean link, one search a card with a second only when the first found nothing, and never a view count that was not seen. Nothing found → the card says so and carries YouTube's own search for the topic; a made-up link is never written. `yt-board` finds it when it creates the card (setup included), the Monday Kickoff's top-up does the same, re-checks this week's link and prints it in its note (`▶ WATCH FIRST`), and `yt-make-video` confirms or replaces it and adds two more with "the one thing to do better". Each long-form row of the Brain's calendar gained a `Reference video` cell; an older board gets the column added in place. A demo's reference videos are real ones too.

**A publish checklist on every card (the owner, 2026-11-14: "uploading is where older members get stuck").** A new locked section, `✅ PUBLISH IT — SIX STEPS IN YOUTUBE STUDIO`: six tick boxes in Studio's own order — title, description, thumbnail, playlist, end screen, pinned comment — each with where to click and exactly what to paste for that video. `yt-make-video` fills it with the video's own values; the Kickoff's draft carries the six boxes; "my video is published" moves the card to Published. The long-form card page now has ten sections.

**Live numbers as a named step, never part of setup.** "connect my YouTube numbers" is its own two-minute chat with the exact clicks (three cases: not added yet · added but not signed in · already active); the setup close names it once, as one plain line; the research skills read live view counts only when the connection is already active and the member is in the chat; the Monday Kickoff and the Monthly Channel Review never call it.

**Thumbnails are made in Higgsfield.** `yt-thumbnail` writes a sheet for Higgsfield — three directions, the prompt to paste, which of the member's own photos to upload, the three to five words — and "my thumbnail is done" files the result; it is never a Claude Design job, and there is no thumbnail design skill. The setup guide, the FAQ (Q48, Q64), the stack map, the cohort knowledge base and three Support skills no longer say Higgsfield is "parked".

**What the simulated sitting changed in the YouTube plugin.**
- **The sitting is short where the member reads it.** Everything between the channel answer and "Say Yes" fits in about 450 words (it ran about 2,300): the nine channel pieces live in one document, **"your Channel Page"** (never a third "kit"), and the chat shows only **the three to paste today** — the description with the about section, the links, the upload defaults; "walk me through my channel page" takes the rest one at a time. The Game Plan hands over in two lines. The workflows card is at most 70 words before "Say Yes". The close is the first-video line, the Board-and-Book line, at most three numbered next steps, one compliance line when it applies — and nothing after it.
- **Dates that make sense.** The first video is recorded on the member's next filming day at least three days after the sitting (none on file → the Saturday after next) and published two days later; a card never says "record today"; a new channel's trailer is week one's first row; the first-video line says when the Monday Kickoff starts.
- **Nothing claimed that is not on file.** The welcome names only what exists (your offer, your guide, your bios); a member with no channel is told how to create one, in one line; a member who skipped Week 4 hears "building your content board", not "adding to" one, and the board link has a second home (`channel.md → Board:`); the Game Plan creates the calendar file when a Brain has none; at most ONE caveat line, naming what was missing and the phrase that fixes it.
- **No compliance detour.** With compliance `unset` the sitting builds everything, stamps the public pieces "hold until your compliance basics are set", and says so once, at the close — the Short-Form rule.
- **The banner is the one the brand kit made in Week 3** (no second brief); "start over" re-runs the whole setup in place; the leftover offers are statements; the usage tip names the Medium setting in plain words.
- **The Game Plan document, member-readable** — "your next 7 days" first, plain words for the three topics, the codes kept out of the document (they live in a TITLE NOTES block of the Brain's copy).
- **The Monthly Channel Review names the three Studio screenshots** it needs (Content · Reach · Engagement), and "add my attraction Studio numbers" records them as a `YouTube Studio numbers` block the next review reads.
- **Interviews get booked.** "book my agent interview" (and "[name] said yes"): two recording times stated, a ready reply and a prep note for the member to forward to the guest, and the recording step in the editor — nothing is sent from here.
- **The Monday Kickoff note is calm:** at most seven lines, a line with nothing to say is left out, one optional compliance line last.
- **One truth where files disagreed:** the 8-video order (niche · interview · niche · model · interview · niche · interview · interview), "change my YouTube cadence" as the one step-up phrase, the Kickoff's export name, description line 3 (the compliance and contact line), one thumbnail sheet, one board-count line; no skill id or file path inside a member's document; no pointer to a file that does not exist.

**A video now feeds the short-form week (Short-Form 0.5.0).** "repurpose my attraction video" queues three clip scripts in the Brain's calendar (`## Clips from your videos (YouTube)`, a third YouTube-owned section); the Monday Week Plan turns up to two of them into that week's Reels — a clip fills a slot the member already had, the displaced topic goes back to the ideas file, at least one Reel a week stays an original, and a clip is logged once. `sf-gameplan` keeps the YouTube sections when it builds its calendar second.

**The Brain (0.9.12).** The channel template mirrors the YouTube plugin's (the `Board:` line, the `not started` stamp, "Channel Page delivered"); the long-form calendar rows carry the `Reference video` cell; the performance ledger names the Studio numbers block; the contract lets YouTube create the calendar file. The Brain Board's YouTube page says "Your channel page", reads the board link from either home, shows this week's "Watch first" video, lists the new phrases, and no longer says "three workflows" where there are two.

**The Design Studio's style sheet, calmer (re-upload `02-aa-style-sheet-design.zip`).** The owner's live test read as "too much going on": page 1 is now two small direction cards and then ONE sheet of six plain bands — four text sizes, two font families, three brand colours shown large, two grounds — with the full system on page 2 for the later skills. A dry run then removed what still read busy: the colours band ends after the three swatches and one line; the lighter and darker versions and the do-and-don't picture moved to page 2; one header logo; a second logo version is one row, never a second grid.

**Docs and Support.** Setup guide section 7 (the reference video, the publish checklist, the live-numbers step, Higgsfield); the YouTube demo checklist rewritten for the new sitting; FAQ Q66–Q68 added and Q48, Q60 corrected; the stack map's Design Studio row (live, not "coming"), its short-form workflow counts (nine: four on with the one Yes, five by phrase) and its thumbnail lines; `docs/BRAIN-CONTRACT.md`.

**Not proven yet.** Nothing in this release has been run live in Cowork: the Notion `Reference Video` column and the playable video on a card, the "connect my YouTube numbers" clicks, and the Kickoff's web search inside a scheduled run are written from the connectors' own documentation and from tool checks made in a development session.

## [0.27.1] — 2026-11-14

**The audits' leftovers, and the design skills proven by dry run (Short-Form 0.4.1 · YouTube 0.3.1 · Brain 0.9.11 · Lead Magnet 0.12.10 · Support 0.1.24 · the Design Studio).** After 0.27.0 each content plugin was walked as a member who only says Yes, and every design skill except the logo was built for the demo member, rendered and looked at; this release carries what those passes found.

**Short-Form 0.4.1.** The three-a-week default is true everywhere (the ideas skill's "this week's five", the 2·2·1 mix and "exactly 20" survive only at the five-a-week step-up); one call-ask rule, the Week 3 Kit's own (GUIDE on most posts; the invitation on about one post in four, most naturally a proof piece or a "what you get" piece; never two asks; the six designed posts keep the asks the kit printed); daily stories are never board cards; log rows default to Instagram and Facebook; every phrase a member is told is one a skill really answers to ("update my pillars" and "change my cadence" are now declared); the workflow is "Batch Prep" (its day follows the batch day), and when it runs before Monday's plan it runs the week plan first instead of leaving an empty film day; a Reel is never dated before the batch day that films it. The Game Plan document reads like something a member can use: "your first two weeks: post the six you already have", a five-column calendar (date · what · the hook · the ask · status) with dates written as words, next steps that name the editing step and the ManyChat build sheet, and none of the system's internal vocabulary. The setup close is the Board-and-Book line plus five short numbered lines, said once (the first-Reel skill no longer repeats the close inside setup); a returning member whose posting tool is still pending is asked before the first Reel; "start over" after the setup phrase re-runs the sitting in place.

**YouTube 0.3.1.** The remaining offers are statements; the Game Plan reads the goal from the Brain instead of asking; "change my YouTube cadence" is a declared phrase with a short re-dating path; the on-demand read and the deep dive write their own export (`youtube-read-…`, which the Brain Board now reads) and leave `youtube-review-…` to the Monthly Channel Review; both scheduled runs keep `Email me:` true to whether mail is connected; "weekly review" is gone.

**Shared rules and the Brain.** `ask-once-default.md` no longer says "2–4 related questions per stop": a skill asks only what the Brain cannot hold, one plain question per turn; `how-we-speak.md`'s return visit closes with a statement, never "What do you want to build today?"; the data engine and the board spec agree with both plugins (the Studio phrase, "stories are never cards", an unconnected Notion leaves the board line empty). The Brain Board shows posting as pending while a chosen tool's connect is unfinished. The Week 3 Kit's rule for the call ask matches its own six posts. The Week 2 close and the kit both name the brand chat as the first step of Week 3.

**The Design Studio (re-upload the zips).** Nine dry runs — style sheet, brand kit, offer kit, guide, opt-in page, posts, video kit, event set, playbook — were built from the skills as written, rendered and inspected, and the instruction defects they exposed are fixed in the skills: sizes that were missing (the vertical name strip, the pop-up, the playbook's page and cover in pixels, the screenshot test), character budgets that overflowed, accent-on-ground pairings that fail contrast, a headline rule read as a ceiling, a grid-safe rule that made the footer jump between slides, print units that render quarter-size on a page canvas, and the last places a skill asked the member to "confirm". **The download button no longer fails on a piece that carries HTML text** (the exporter loads the piece from a data URL; a blob URL tainted the canvas). The shared craft standard gained what the runs taught: a saved picture is one SVG with its words set as SVG text, measure the real line before trusting a size, what yields when a piece's own list will not fit with a third of air, where a mid-tone accent may and may not carry text, and a display-serif width factor.

## [0.27.0] — 2026-11-14

**The YouTube plugin comes to main, rewired for Week 5 (YouTube 0.3.0 · Short-Form 0.4.0 · Brain 0.9.10 · Lead Magnet 0.12.9 · Support 0.1.23 · the Design Studio rebuilt).** Plugin 6
returns from `wip/all-plugins` rewired to `docs/plans/youtube-rewire-2026-11-14.md`: Week 5 (date to be confirmed)
throughout; one sitting (the channel kit built from the kit's YouTube bio and calls-to-action table, the YouTube Game
Plan from the offer's content branches on the 8-video cycle, the YouTube tab on the one Notion board with the rolling
30 days, one statement card that switches on two draft-only workflows with the member's one Yes (the Monday Kickoff and the Monthly Channel Review), the first video handed over by title, the
Brain Board rebuilt at the close). The two CTAs are the Week 2 guide and the call in Mike's law's shape; scalable
deliverables only; **one video a week is the default for the first month** (the owner, 2026-11-14), two the step-up
the Monthly Channel Review proposes. The board spec (identical in both content plugins) locks the long-form card page
(the hook · script · thumbnail brief · SEO package · the resource · references · guest · notes · after it's out). The
config block is `## YouTube (Week 5)` with the locked lines plus `Email me:` (the Short-Form block's answer counts);
the `Monday Kickoff delivery: email draft` line is retired; every workflow run leaves its Cowork note, writes its text
to `exports/`, emails the member one short note at their own address when mail is connected (never asked), and ends with a push. The Brain Board's YouTube page now shows
where it stands, the lanes, this week's video, the workflows, the last Monday Kickoff and the last monthly review.
Brain template, contract, Support syllabus (Week 5 live; the stale "twelve workflows" short-form lines corrected),
FAQ Q59–Q63, setup guide section 7 and the demo checklist moved with it.

**The owner's live-run rulings, the same evening (Short-Form 0.4.0):** process steps are told, not asked — the consent card is one statement closed by "Say Yes" (no "all, some, or not yet", no "want me to email you", no platform or ManyChat questions; the email note is part of the process when mail is connected); the Daily Engagement List and the Friday Performance Note are removed from the OS (short-form switches on four workflows with the one yes and keeps five by phrase; YouTube switches on two — the Friday YouTube section is gone, the monthly review carries its work); the board's tabs are Graphics · Reels · YouTube · Calendar ("This Week" confused a member); a designed post sits at `Ready to Post`, never `Recorded`; ManyChat is required, told, and never connected to Claude; platforms are never asked (Instagram and Facebook both, TikTok/Shorts optional reposts, LinkedIn from the avatars); the Game Plan's calendar bands read GRAPHICS and REELS. The shared `ask-once-default.md` carries the told-not-asked rule for every plugin. **A member now says Yes exactly once in each sitting** — on the workflows card, the one explicit yes a scheduled task needs: the Game Plan's two confirmation stops and the bio-refresh stop became statements (the pillars, the lanes and the cadence are stated and the plan is built in the same breath; any of them changes later by its phrase), and the only question left is a fact the Brain cannot hold (short-form: Metricool or GoHighLevel; YouTube: the channel link). A task line in `config.md` holds one of three values everywhere — a task id · `paused` · `later`; `declined`, `not offered yet` and `off (offered …)` are retired, and a reader treats anything that is not a task id as not on.
The close of every weekly sitting (Lead Magnet 0.12.9, Short-Form, YouTube) now hands over both files with their links — "your Brain Board and your Brain Book are updated — here they are": the sync skill gained a closing step (4b) that rebuilds the Board and runs the Book's new What's-next refresh (Section 9 only; Sections 1 to 8 carried over character-for-character), and the Book spec's state rule names the system states. The closes also state the editing next step (new chat → "edit my reel" / "edit my YouTube video" — Plugin 5), and the posting tool is one straight question (Metricool or GoHighLevel) with the Connect card put in the chat from Claude's connector directory.

**"There is no Design Package brief" — fixed at the source.** Nobody has a brief until the Week 3 brand chat runs; it was never part of the Week 1 Brain. The Brain Board used to tell a member whose brand chat had not run to say "show my design package brief" (and "refine my partner offer" before an offer existed, "finish my agent lead magnet" before a magnet was started): a system that has not started now offers the phrase that STARTS it ("my attraction brand direction" · "build my partner offer" · "launch my lead magnet plugin"). The brand chat itself never says a missing brief like an error — asked for a brief that does not exist it starts the chat with one warm line — and it is told, not asked: at most four questions (logo · colours and fonts · headshots · the organization's name), each skipped when the Brain or the Brand folder already answers it; "one brand or two?" is gone (one brand with a leader lane is stated on the card; "say 'two brands'" changes it); about five minutes. The setup guide, playbook 1, the Support syllabus and a new FAQ (Q63) say it plainly.

**The Design Studio, rebuilt for quality (all ten `aa-…-design` skills; re-upload the zips).** Every skill now carries one shared reference, `references/craft-standard.md` (byte-identical in all ten): the order of work; a told-not-asked opening (the first reply is one line and then the build — every intake form, "Decide for me" menu and upload-slot list is gone, in the skills and in their references; a form box had been cutting a pasted brief off at 400 characters); a six-line plan before any pixel; real type, layout and colour numbers; honest photo handling (a true cut-out only when the file has a see-through background — a normal headshot is framed or run as a panel, never faked); how to build so nothing breaks; **the look loop** (see the real render at full size and at the size an agent meets it, fix what is broken, wrong, weak, loose or generic, look again); and **the gate** (five lines scored before the member sees anything). Each skill opens with the five things that decide its piece and runs the look loop and the gate before its own checks. The logo skill presents **three** directions (not three to five), built in one colour first and proven at 40 pixels, with the model's own pick stated before "Your turn"; its craft reference gained how a mark is really constructed (the grid, six monogram moves, the 40-pixel proof) and a cast of real faces by temperature with spacing numbers. No brief anywhere now sends the member to the brand chat in one line (the old "three quick questions" bypass is removed). The Design System's photo rule matches.

## [0.26.0] — 2026-11-14

**The Short-Form plugin comes to main, rewired for Week 4 (Short-Form 0.3.0 · Brain 0.9.9 · Support 0.1.22).** Short-form
is WEEK 4 (the owner, 2026-11-14; Week 3 is the brand); YouTube and the later plugins shift a week, dates to be
confirmed. Plugin 4 rewired to the contract `docs/plans/shortform-rewire-2026-11-14.md`: one Week 4 sitting (profiles
and the two keywords confirmed — the bios were written in Week 2 — the Game Plan built from the offer's content
branches and the Week 3 Kit, whose six designed posts open the 30-day calendar, the Notion content board kept as the
working surface, one consent card, the first Reel, the Brain Board rebuilt at the close). Two keywords only (GUIDE and
the offer's own invitation word; PARTNER/SCALE/GROWTH retired); Mike's call-to-action law in every caption and ask;
scalable deliverables in every script and story prompt; carousels handed to Claude Design as lean build sheets.
Eleven draft-only scheduled workflows, six recommended on: the Monday Week Plan (which now also drafts any welcome or
win post the Brain earned that week, behind the consent gate), Sunday Batch Prep, the Daily Engagement List, the
Wednesday Brokerage News Watch (three to six REAL headlines from the last 30 days, cited with their links, a
30-second take each, onto the Notion board), the Friday performance note and the Monthly Calendar Refill; optional:
the keyword follow-up queue, the mid-week nudge, the monthly deep dive, daily stories, the quarterly profile audit.
"Email me": one short email to the member's own address when a workflow leaves something ready; every run leaves its
Cowork note and rebuilds the Brain Board. The owner's board rulings the same day: three Reels a week is the default for the first month (twelve dated posts — the six designed in Week 3 plus six to film; five is the step-up the Friday note proposes), the Notion board opens on a This Week tab (Short-Form, YouTube and Calendar are the other tabs, so the later YouTube plugin never mixes into the short-form list), every card page follows one locked layout (the hook, the script, the caption, the ask, filming notes, sources, after it's out), the news watch fills the week's green-screen card with the best story and keeps the alternates inside it (one card, never one per headline), and the config keys the workflows write are one locked list. The Brain Board's Short-Form page now shows the two keywords, the pillars,
this week's posts, the workflows switched on, the board link and the last Friday note. Setup guide, Support syllabus
(Week 3 = the brand and Design Package, Week 4 = short-form), stack map and the Brain template moved with it.
**The Riverside editor ships with it (Plugin 5, 0.4.5)** — vendored from the realtor marketplace as the same plugin, never a fork (the owner, 2026-11-14), with exactly two downstream patches: the Brain-home patch and its description trimmed under the 1,024 limit; its week labels, keyword examples and the Video Brand Kit path (`02 · Brand/Video Brand Kit`) already fit this OS — checked, nothing to change. Improvements to the editor happen upstream, then it is re-vendored; `scripts/vendor-riverside.sh` comes to main with the two-patch list. **Design Studio fix:** the ten skills' "where this runs" rule now counts Cowork's Design canvas (the Design tab, or a Design artifact beside the chat) as Claude Design and builds there in place, with a file-export fallback — the old rule refused inside the Claude app and sent members to claude.ai/design (found live 2026-11-14); a missing brief is asked for in plain chat, never a dead end and never through a question card (Claude Design's form fields cap at 400 characters and cut the Brain's brief off — seen live); the brief arrives as the file the Brain saves in the Brand folder, or pasted whole into the chat; the brand-week rule reads "one design project, either place"; zips rebuilt.

## [0.25.4] — 2026-11-09

**The call-to-action law (Lead Magnet 0.12.8 · Brain 0.9.8).** Mike: the CTAs must be angled at partnering with the
PERSON to get their direct help, free, to implement the strategy — never at the brokerage. One shape now, in every
call CTA the plugin writes (the guide's three, the page's Book-a-call area and thank-you line, the bios, the DMs,
the nurture, the kit's calls-to-action table, the offer's "what the call is"): the person · their help · free · to
run this — at the join register "partner with me and it's free", at the open register "I'll walk you through it,
free, no strings"; the method named every time; the brokerage never the reason; the help is the program's scalable
assets, never a 1:1 promise. The phrase bank's "1-on-1 session" line is gone.

## [0.25.3] — 2026-11-09

**No video question (Lead Magnet 0.12.7; the funnel design skill's zip rebuilt).** Mike's note: the "do you have a video
link?" question comes out of nowhere and leaves members wishing they had one. The funnel writer now asks nothing: the
top of the page is the member's cut-out headshot (`Video: headshot`), a link is used only when the Brain already
holds one, and no close line, build note, asset list or design hand-off mentions a video or a script. The `Video:`
label stays so older kits and the design step keep working.

## [0.25.2] — 2026-11-09

**The Brain Board always rebuilds at the end of the Lead Magnet sitting (Brain 0.9.7 · Lead Magnet 0.12.6).** Found in
the live demo: the sitting had pulled only the files it needed, so the final push could not draw the board from a
whole Brain and skipped it. Now a PULL is always the whole Brain (every identity, memory and exports file; a partial
local Brain counts as missing), the sync's board step completes the pull before rendering and never skips, the
sitting's last push (the kit's) rebuilds the board, and the finish line only claims an updated board when it is true.

## [0.25.1] — 2026-11-09

**Scalability, verified file by file; the method map; the blueprint gate (Brain 0.9.6 · Lead Magnet 0.12.5).** A
sweep found the old cadence shape still written into the Brain template, the offer template, the interview guide,
the Partner Offer floors, the kit's welcome-pack calendar line, the funnel and copy references and nine design
references: a welcome call, a group chat, a 1:1 rhythm, a response-time promise, "the first Saturday". Every one is
now the scalable form — a welcome video, the community, a self-serve Day 1, the recorded day-30 self-check — and
the weekly group call appears only when the member already runs one (Mike: no additional effort once it is built;
never invented as a default). The labels other skills key on (`Onboarding: Day 1`, `Group chat:`) keep their names
and change their contents. The offer skill gains THE METHOD MAP: every member's own system reconstructed from what
they actually do, each step with its action, timing, asset and countable output, a depth test (a partner could run
it without the member) and one question when the method is thin. The magnet skills gain INDIVIDUAL CRAFT (no two
members get the same guide; the next best is a different packaging, never a different topic) and THE BLUEPRINT
ARCHITECTURE with the "effectively done" gate: one page per framework step with the asset in full, the mistake and
the number to watch, every paragraph specific, fluff words banned, 2,500 to 5,500 words.

## [0.25.0] — 2026-11-09

**Mike's Week 2 review, applied (Brain 0.9.5 · Lead Magnet 0.12.4 · Support 0.1.21).** Doctrine §10e, obeyed by every
skill that writes the offer, the magnet or anything that promotes them. (1) SCALABLE BY DESIGN: every deliverable
works for ten partners as well as one — recorded lessons, templates, scripts, checklists, a community, ONE recurring
group call, a self-serve Day 1; in-person shadowing becomes a recorded walkthrough, a group chat the community, 1:1
rhythms the weekly call and a recorded day-30 self-check; the skill says in one line what it converted. The
cadence defaults, the deliverables rule, the type rule, the stack's "included" rule and the Partner Offer's
never-list all changed; the full digital product grows into a short recorded course. (2) THE UPLINE FIRST: when the
member's own assets are thin, the stack, the one-pager and the offer card lead with the upline's package so the
member can run the offer this week. (3) A REAL BOOKING LINK: the intake's last question sets up a free Calendly with
the member — one 30-minute Zoom event, Mike's five qualifying questions, reminders — and the pasted link is written
to the Brain; "email me" is only the fallback until then. (4) THE WHOLE METHOD: the ONE recommendation is the
complete blueprint of the member's framework (prepare · do · capture · follow up, every script and template inside,
the tonight-step first), one body page per step, 2,200 to 4,500 words; a single tactic is a page, never the magnet.
(5) The `no` register's output is stated plainly in the offer's close and in the Support FAQ: the same three files,
open to any agent, the invitation still the call.

## [0.24.1] — 2026-11-09

**Brain Board: the Lead Magnet page now shows the whole Week 2 (Brain 0.9.4).** The page opens with "Your three files"
(the offer, the guide, the Week 3 Kit — each with where it lives and a tick), "Where it stands" gains the sales
funnel outline, the bios and the kit as their own rows, a "Your Week 3 Kit" section lists the eight chapters and the
build date, and the funnel outline prints the member's REAL section headlines from the page text (the generic
descriptions only when no page exists yet; their wording is register-neutral now). The documents table lists the kit;
the lead magnet actions add "update my attraction bios" and "what do I upload to Claude Design". Found during the
live demo: the board had rendered the old generic page after the sitting, so the kit and the bios were invisible.

## [0.24.0] — 2026-11-09

**The Design Studio comes to main, rewired for the three Week 3 files (Support 0.1.20).** The ten Claude Design skills
(`design-studio/`) were written for seven separate Week 2 documents, a Week 1 brand and a "Brand HQ" project. They now
read the Week 3 Kit by chapter and band, the guide file and the Design Package brief (the contract:
`design-studio/_build/REWIRE-BRIEF-2026-11-09.md`); all design work is Week 3 in one member-named project, events and
the Value Vault Week 6. Two owner rulings applied everywhere: digital-only (no print pieces — business cards, signs,
flyers, postcards, letterhead are gone; a Zoom background and a title frame replace them) and a COACHING brand for
agents, never a realtor brand for consumers (house, key, skyline and "sold" cues banned; the member's face, the method
and the program name instead). The offer kit leads with the DIGITAL PRODUCT MOCKUP ("design my digital product", "mock
up my offer"), version one = template + one recording, never a course box unless chapter 2 says so; the model
comparison sheet is gone and the opportunity deck is the kit's call deck. The content skill is the SOCIAL GRAPHICS skill
with three modes: the six kit posts ("design my posts"), the team and promo templates ("design my team posts": welcome a
new partner, agent win, team milestone, quote card, weekly call reminder, reel cover, program promo) and the carousel
and recognition side doors. The video kit adds the POP-UP SET ("design my pop-ups": name card, guide pop-up, call pop-up,
two end cards, transparent, both orientations) beside the Riverside Video Brand Kit v3 contract. The register rule, the
verbatim law, the compliance stamp and the exact Cowork phrases to say back ("the logo is done" … "my offer kit is
designed" … "the PDF is done" … "my funnel is live" … "register my video brand kit") are in every skill. New Week 3
Start Here and README; the Design System file says whose brand this is; `build.sh` builds the ten zips and two map files
into `_dist/` (committed; attached to the GitHub release). Setup guide §5, the Support cohort KB and stack map point
members at the release and the new phrases.

## [0.23.3] — 2026-11-09

**Pre-demo audit of the Week 2 sitting — two independent read-throughs, 60 findings fixed (Brain 0.9.3 · Lead Magnet
0.12.3 · Support 0.1.19).** Demo-breakers: the guide's closing page treated `unknown` as the open register (every
member without a brokerage answer would have had a guide contradicting their page and kit) — now `yes`/`unknown` = the
join register everywhere, including the Brain Board's open item, the Support router and the nurture CTA; the kit
skill's own description said the kit carries the guide "word for word" (it never does — the guide is its own file)
and so did the Lead Magnet plugin's description, house rules, output standard and the Brain kit builder; the silent
bios step would have asked a question mid-sitting. Consistency: the Lead Magnet navigator now hands the offer skill
an explicit "Lead Magnet sitting — skip the kit" line; the offer skill gained a silent SHAPE UPGRADE for offers built
before 2026-11-09 (adds Differentiator, Proof plan, What my partners can offer, What I assumed, Lead-magnet seed, the
register) so an older Brain never prints empty lines into the kit; "refresh my guide" is a real trigger; the funnel
reads the intake's `Reach:` answer so the guide and the page point at the same place; the funnel's own close is
silent inside the sitting; the delivery kit is text only (the three-files rule); the UTM tags and the booking-tool
five questions now sit in the kit's build notes; the title cap is seven words everywhere; the Partner Offer reference
no longer describes member pages inside the document; "my offer kit is designed" is a real Week 3 trigger; Support's
week map (brand = Week 3), the Brain Board's labels and a dozen stale document names fixed.

## [0.23.2] — 2026-11-09

**Chapter 7 gets the social posts and every call to action (Brain 0.9.2 · Lead Magnet 0.12.2).** The Week 3 Kit's
Design Assets chapter now carries six social graphic post outlines (the guide carousel · five problems, five fixes ·
my story · what you get · proof · book the call, with slides, captions and sizes) and a CALLS TO ACTION table: the
guide ask and the call ask for captions, the two comment keywords (GUIDE and the offer's word), mid-video pop-ups,
spoken lines, end cards, stories, the bio link and the DM reply, with pop-up rules (six words, three seconds, never
over the face, the name card in the first three seconds). The design brief orders the posts and a transparent pop-up
set. The page budget is now measured, not guessed: a full demo kit rendered through Pages lands at 370 words a page
plus the cover and the contents page, so the kit holds at most 8,500 words; chapter targets re-set (7 ≤ 1,900),
chapter 5 no longer repeats the outline chapter 1 carries, chapter 8's content branches are names only, chapter 4's
picture ideas sit in the outline, bios capped (LinkedIn About 900 characters, Google 500). Fixed: the bios band label
that exceeded the renderer's 80-character cap and printed as body text. Demo build: 8,595 words → 25 pages.

## [0.23.1] — 2026-11-09

**Shorter chapter names (Brain 0.9.1 · Lead Magnet 0.12.1).** The kit's contents page now reads: Summary · Your Offer · Why
Join Me · Lead Magnet · Sales Funnel · Bios · Design Assets · Your Notes, each with a one-line gloss under ten words
(`attraction-week3-kit`, `lm-package`). Same chapters, same order, same budget.

## [0.23.0] — 2026-11-09

**Twenty-five pages, the bios inside (Brain 0.9.0 · Lead Magnet 0.12.0 · Support 0.1.18).** The owner's cap: the Week 3
Kit may not pass 25 pages, with nothing of substance lost; and the bios must be written automatically and live in the
kit as their own linked chapter.
- **The guide is no longer copied into the kit.** It is its own finished file, so Week 3 uploads two files — the kit and
  the guide — plus the Design Package brief. Chapter 4 of the kit keeps the guide's outline, the picture idea for each
  page and its design brief (`lm-package`, `attraction-week3-kit`, `house-rules.md` #3, the brand chat and health nudge,
  Support, `setup-guide.md`).
- **Eight chapters, no part-opener pages, a word budget per chapter and a fixed trimming order** (`attraction-week3-kit`
  "The page budget": the call deck, the welcome letter, the social lines and the content branches trim first; the
  summary, the page copy, the bios and the briefs' rules never). A standard-library one-liner measures words per chapter
  after assembling.
- **The bios are a step in the sitting and chapter 6 of the kit.** `lm-navigator` runs `lm-profiles` in a new silent mode
  after the page outline; every bio is sized to its platform (Instagram 150, Facebook intro 101, LinkedIn headline 220
  and About 2,600, YouTube 1,000, and the rest) with the count shown, built from the offer, who the member is and where
  they live, pointed at the page or the booking link. The separate "Platform Profiles" document is gone
  (`output-standard.md`, `brain-contract.md`); a standalone "update my attraction bios" shows the pack in chat and
  rebuilds chapter 7.
- The finish line names the two Week 3 uploads and the bios chapter; `lead-magnet-demo-checklist.md` says to count the
  pages and click "Your bios" in the contents.

## [0.22.0] — 2026-11-09

**Find anything in one click (Brain 0.8.0 · Lead Magnet 0.11.0).** The owner's second review of the live Week 2 files:
the Week 3 Kit was 25 pages of headings with no way in, and the Partner Offer was 13 pages because the member's own
pages sat behind the agent's. "If I want my lead magnet outline I have to scroll and scroll."
- **The Week 3 Kit is a book** (`attraction-week3-kit`, `lm-package`): a cover page that says "upload this, you do not
  have to read it", a CONTENTS page where every line is a link, then **chapter 1, the two-page summary** — the offer in
  one table, the lead magnet outline, the sales funnel outline, where everything lives, how to use it in Week 3 —
  before anything else. Part I (chapters 2–6) is the offer, Part II (chapters 7–10) the lead magnet; every chapter
  starts on its own page with a small kicker. The renderer's book grammar does this (`[[TOC]]`, `PART`/`CHAPTER` bands),
  so nothing changed in `render_doc.py`.
- **The Partner Offer is agent-facing only**: a cover, a linked contents page, At a glance and eleven sections, about
  8 to 10 pages. The member's pages — the marketing language, what I assumed, how to create it, start with your upline,
  the brokerage rule, where to host it, the content branches — stay in `offer.md` (new `## What I assumed` section in
  `offer-template.md` and the Brain template) and render as chapter 8 of the kit, "Your offer, for your eyes only".
  `attraction-offer`'s gate checks twelve bands and the contents block; `partner-offer-doc.md` carries the block.
- Support (`cohort-kb.md`) and `lead-magnet-demo-checklist.md` describe the new shape; the demo now says to open the kit
  and click a contents link.

## [0.21.0] — 2026-11-09

**The guide renders as a guide (Lead Magnet 0.10.0 · Brain 0.7.1).** The first live `Lead Magnet — …` document read like a
spec sheet: "Pull quote:", "Image idea:" and "Next step:" printed as bold labels, page headings in capitals, a
"ready for your design step" line on page one and a builder appendix at the end — not something a member could
export and hand to an agent, although the finish line told them to.
- **`render_doc.py` gains `--guide`** (shared, byte-identical in both plugins): a cover built from THE PROMISE
  (title, subtitle, the three hook lines, the byline, the date), one printed page per `── PAGE N - TITLE ──` block
  with the title in Title Case, the labels rendered as page elements (pull quotes large with an accent bar,
  callouts as panels, checklists with boxes, template rows as fill-in lines, scripts as bubbles, the next step as
  a strip, the call to action as a box, sources small), every `Image idea:` and both `▸` appendices left out, the
  back page centred, the compliance line in the footer. Book mode and the legacy look are untouched.
- `lm-magnet` renders the guide with `--guide --eyebrow "A free guide from [First Last]"` and reads it back for
  leaked labels; `output-standard.md` names the exception; `lead-magnet-demo-checklist.md` says what the opened
  document must look like.

## [0.20.0] — 2026-11-09

**Three files, never seven (Brain 0.7.0 · Lead Magnet 0.9.0 · Support 0.1.17).** The first live run of 0.19.0 ended
with seven document cards in one chat — the Partner Offer, a Why Join Me doc, a Value Stack doc, the Offer Package, the
guide, the Opt-In Funnel doc and the Lead Magnet Package. The owner's ruling: that overwhelms a real estate agent. A
member finishing Week 2 now holds **the offer** (the Partner Offer document), **the guide** (the PDF agents download)
and **one Week 3 Kit** (the one file for Claude Design). Everything else lives inside those or in the Brain.
- **`attraction-week3-kit`** (Brain; replaces the day-old offer-package skill): `Week 3 Kit — [First Last] — YYYY-MM-DD`
  in `01 · AI Brain` beside the Brain Book. Part A the offer (the why-join-me statement, the one line, why me, the five
  problems it solves, the stack with the free line and the up-front cost line, the proof plan, why now, what partners
  can offer, the small digital product, the copy for the one-pager · stack · mockup · call deck · welcome pack · social
  lines, the offer-kit design brief). Part B the lead magnet, written by the Lead Magnet plugin and included verbatim
  (the guide, the page, the messaging, the design brief with plain builder notes). Newest wins and the superseded copy
  is trashed, so the folder holds one kit. Stamped `## Week 3 Kit` in `offer.md`.
- **No more documents of their own:** `attraction-why-join-me` and `attraction-free-vs-paid` write the Brain only
  (the story and the stack appear in the Partner Offer's appendix and At a glance, and in the kit); `lm-funnel`
  keeps the page outline in `exports/` only (the member hears "your sales funnel outline is in your Week 3 Kit");
  `lm-package` writes the kit's lead magnet half and calls the Brain's kit builder instead of saving a Lead Magnet
  Package. The offer session skips the kit when the Lead Magnet plugin started the sitting, so the kit is built once,
  at the end, with both parts.
- Readers updated: `lm-navigator` (session order, resume table, finish line with the three files, routing — "what do I
  upload to Claude Design" is the Brain's), `lm-magnet`, `lm-delivery`, `lm-profiles` ("add my guide to my kit"),
  `house-rules.md` #3, `output-standard.md` (tree, naming, prefixes, appendices), `brain-contract.md` (both plugins;
  `Kit doc:` replaces `Package doc:` in the intake block, template and demo), `intake-questions.md`, `offer-template.md`,
  the Brain template (`offer.md`, `journey.md`), `attraction-doctrine.md`, `drive-map.md`, `render_board.py` (demo board
  re-rendered), `attraction-brand-direction`, `attraction-brain-health`; Support (`cohort-kb.md`, `faq.md`,
  `maa-support-onboard`, `stack-map.md`); `README.md`, `setup-guide.md`, `lead-magnet-demo-checklist.md` (count the
  cards: three).

## [0.19.0] — 2026-11-09

**The offer is a package, and the package is promoted (Brain 0.6.0 · Lead Magnet 0.8.0 · Support 0.1.16).** The
owner's review of the first live Week 2 outputs against Mike's five value-proposition lessons: a lead magnet is a
door, not the offer; the offer an agent joins, the digital product and the assets that promote the offer were never
produced in Week 2, and the "don't know" brokerage default hid the offer behind "what I teach".
- **New `attraction-offer-package`** (Brain): one file for the offer, `Offer Package — [Program Name] — YYYY-MM-DD` in
  `05 · Offer`. Part I the offer to join me (the why-join-me statement, the one line, why me, the five problems it
  solves, the value stack sorted free · included · discounted with the free line and the up-front cost line, the
  proof plan, the honest why now, what their partners can offer); Part II the digital product (version one now, the
  full build in Week 6); Part III the copy for every asset that promotes the offer (the Join My Team one-pager, the
  offer stack, the product mockup, the call deck, the welcome pack, bio line, captions, DM, the 60-second video
  script); Part IV the design brief for the offer kit. Assembled, never rewritten; stamped `## Offer Package` in
  `offer.md`; text kept in `exports/`.
- **The offer session now ends with the whole offer.** `attraction-offer` runs `attraction-why-join-me` and
  `attraction-free-vs-paid` in their new silent modes (zero questions) and then the package; both skills rebuild the
  package when they change. The Partner Offer document gains THE FIVE PROBLEMS THIS SOLVES (lesson 28's page), a
  twelve-row At a glance (What's free from day one · Why me), the `Proof plan:` (founding partners: a written OK and a
  60-second video at day 90 — lesson 33's "earn the first case studies"), `What my partners can offer:` (lesson 28's
  duplication), `Differentiator:` and the why-join-me statement in the appendix; the gate checks all of it.
- **The register default follows Mike's model.** `Join-gated package allowed: unknown` now keeps the join register
  ("when you join me you don't just get the brokerage, you also get…") with one open check; only a brokerage that
  says no opens it. Every reader in both plugins updated (`offer-template.md`, `partner-offer-doc.md`,
  `interview-guide.md`, `attraction-doctrine.md`, the Brain template, `brain-contract.md`, `lm-magnet`, `lm-funnel`,
  `lm-delivery`, `lm-nurture`, `lm-gbp`, `lm-partnerships`, `lm-profiles`, `lm-package`).
- **Lead Magnet fixes from the live run:** the technical form checklist no longer prints in the member-facing funnel
  appendix (it lives in plain words at the end of the Lead Magnet Package's Part V, for whoever builds the page);
  a `Reach:` question when the Brain holds no booking link, email or handle (never "message me on Instagram" with
  no handle — `intake-questions.md`, `brain-contract.md`); the funnel's word ceiling 1,800 → 2,400 (`measure_copy.py`,
  `lm-funnel`); the package quotes the why-join-me statement, the free line and the differentiator, keeps page
  titles as written, opens Part V with the literal `DESIGN BRIEF —` line, and the Offer section gains `What's free:`
  (`output-standard.md`); `lm-navigator` names both packages as the Week 3 uploads and routes "build my offer
  package".
- Support (`cohort-kb.md`, `faq.md`, `maa-support-onboard`, `stack-map.md`) and `setup-guide.md` say Week 2 ends
  with two files; `render_board.py` offers "build my offer package"; `drive-map.md` places it.

## [0.18.1] — 2026-11-09

**Hotfix — the 0.18.0 update was refused (Lead Magnet 0.7.1).** Members saw "Plugin couldn't be updated. Try again."
The one manifest that changed shape in 0.18.0 was `plugins/attraction-lead-magnet/.claude-plugin/plugin.json`: its
description grew from 971 to 1096 characters, past the 1024-character field limit claude.ai applies to descriptions.
- The plugin.json description is back under the limit (989 characters) with the Lead Magnet Package still named.
- `check-release.sh` check 1 now blocks any plugin.json description over 1024, next to the existing 500-character
  marketplace-card check and the 1024-character skill check.

## [0.18.0] — 2026-11-09

**The Lead Magnet Package (Lead Magnet 0.7.0 · Brain 0.5.10 · Support 0.1.15).** Week 2 now ends with ONE downloadable
file the member uploads to Claude Design in Week 3 — the offer, the guide and the page word for word, the messaging and
the design brief — so the Week 3 design session has everything in one upload (the owner's ask, 2026-11-09).
- **New `lm-package`** (replaces the design-brief skill; the plugin keeps 11 skills): assembles the **Lead Magnet
  Package** from the finished documents — Part I the offer as copy (`identity/offer.md`), Part II the page outline and
  the guide verbatim, Part III the structure and the opt-in page + thank-you page verbatim, Part IV the messaging (the
  one-liner, headline, hook, button, keyword, call line, the bios and the DMs when written, the words we don't use),
  Part V the design brief (what to build, who reads it, the brand from the Design Package brief or a clean neutral
  default, the cover, the page rules, the mockup, when it's done; it opens with the `DESIGN BRIEF — [GUIDE NAME]`
  line the parked Design Studio skills key on). Never rewrites copy; never renders. Saved to the campaign folder as
  `Lead Magnet Package — [Guide Name] — YYYY-MM-DD` (newest wins), kept in `~/attraction-brain/exports/`, stamped
  `Package doc:` in the magnet's intake block. Also keeps the "the PDF is done" record branch.
- **Wired into the sitting:** `lm-navigator` runs it after the funnel outline (session order step 5), resumes a
  campaign that has both docs but no package, routes "build my lead magnet package" · "my lead magnet package" ·
  "rebuild my package" · "what do I upload to Claude Design", and its finish line names the package as the Week 3
  upload. `lm-magnet` and `lm-funnel` keep their structured text in `exports/` (`lead-magnet-[slug]-…` ·
  `opt-in-funnel-[slug]-…`); `lm-delivery` and `lm-profiles` keep theirs too and rebuild the package silently after
  they save, so the DMs and the bios ride along. "refresh my page" rebuilds it.
- **Contracts:** `output-standard.md` (the folder tree, the naming row, the slug rule, the §5 appendices now point at
  the package, the `exports/` step in §6), `house-rules.md` #3 ("which file do I upload" = the package + the Design
  Package brief), `brain-contract.md` (both plugins; `Package doc:` in the intake block), `intake-questions.md`, the
  Brain template and demo `magnets.md`.
- **Week 3 hand-off, Brain side:** `attraction-brand-direction`'s brief and close name the package as the second
  upload; `attraction-brain-health`'s brand nudge too; `render_board.py` offers "build my lead magnet package" on the
  Lead Magnet page (demo board re-rendered).
- **Support:** `stack-map.md`, `cohort-kb.md` (and its leftover Week 1 brand lines — the brand kit, the Design Package
  walkthrough, the offer graphics — now read Week 3, consistent with 0.17.2), `faq.md` Q3, `maa-support-onboard`
  (Week 2 uploads nothing to Claude Design).
- Docs: `README.md`, `setup-guide.md` (§5 step 8, the Plugin 3 row, both checklists), `lead-magnet-demo-checklist.md`.

## [0.17.3] — 2026-11-08

**The Lead Magnet plugin's full quality pass (Lead Magnet 0.6.2).** Three independent reviews — the member's
experience end to end, the technical contracts and sync, and the copy against Mike's doctrine — plus the owner's own
checks. Everything confirmed is fixed; the decisions that are Mike's are listed in the review page.
- **Week 2 now ends cleanly without Claude Design.** The navigator's finish line (`plugins/attraction-lead-magnet/skills/lm-navigator/SKILL.md`)
  says what exists and where, how to export the guide as a clean PDF today and share it from the drive, the bios
  phrase, the delivery phrase, that the page goes live in Week 3, and the resume phrase. `lm-design` briefs for
  the Week 3 session, asks for a flat cover (Claude Design exports PDF, not pictures), and never names a skill id to
  the member. `lm-funnel` closes on "your page gets built in Week 3's design session"; the member-facing appendix in
  `shared/output-standard.md` names no Netlify. `lm-delivery` leads with the by-hand DM script; the ManyChat version
  is labelled for Week 3.
- **Mike's booking link, in Week 2.** No link on file → one line about a free Calendly (Mike's own setup, with his
  five questions and reminders in `skills/lm-funnel/references/funnel-guide.md`) and "set up my attraction
  operations"; every fallback reads "email me at …" or "message me on Instagram" — never "reply", since a page and
  a guide have nothing to reply to (`shared/house-rules.md`, `lm-magnet`, `lm-funnel`, `lm-delivery`, the intake).
- **The join-gated register everywhere.** `lm-nurture` (Day 10 and Day 16), `lm-delivery`, `lm-gbp` and
  `lm-partnerships` now read `Join-gated package allowed:` and switch to "what I teach" at `no`/`unknown`.
- **One honest why-now.** The blanket "no urgency" that contradicted Mike's offer anatomy is now "no invented
  urgency" with the offer's `Why now` reused verbatim (`shared/copywriting-kb.md`, the funnel guide, `lm-magnet`).
- **One name.** Title ≤ 7 words, set by `lm-magnet-ideas`, used as the cover title, the campaign folder and the
  headline (`shared/output-standard.md`, `lm-funnel`). House rule #9 no longer offers "1–2 alternatives".
- **Written voice for written things.** `lm-nurture` reads `voice.md` + the typed `voice-samples.md` (the
  voice-print only as a cadence check); `lm-gbp` and `lm-profiles` load the voice files they never did.
- **Shapes the board can read.** Every ledger row is shown as the literal pipe row (`lm-magnet`,
  `lm-magnet-ideas`, `lm-nurture`, `lm-partnerships`); `lm-delivery` stops writing into `lm-analytics`'s column;
  `lm-nurture` stops editing the append-only weekly table; the config block is three plain lines registered by
  whichever skill writes first (`Installed` · `Live data: not connected` · `GBP`), and the list tool lives in
  `memory/list-growth.md` only (`shared/brain-contract.md`, the Brain template's `config.md`).
- **Resume and update phrases exist.** "my funnel is live", "here's my live page link", "the PDF is done", "my
  guide is designed", "refresh my guide/page" now route (`lm-funnel`, `lm-design`, the navigator's table);
  `lm-funnel` lists the campaign folder before writing so a second sitting never duplicates the outline; the
  intake block carries `Funnel doc:`; `lm-profiles` treats the template's `[bio]` placeholders as a first write.
- **No cross-plugin dependencies.** `shared/lesson-index.md` (the 19 lessons this plugin may cite, generated from
  the Support KB index) replaces the reference to the Support plugin's file; `shared/connectors.md` ships here too.
- **Measured, not guessed.** New `shared/measure_copy.py` (stdlib): words against the floors, exactly three calls
  to action, bracket tokens, leaks (income, splits, "check your inbox", "beats"), the reading grade — the first
  step of both quality gates (`lm-magnet`, `lm-funnel`).
- **Less on the screen.** Documents arrive as the link, the title and five lines; the full text only on request
  (`lm-magnet`, `lm-funnel`, `shared/output-standard.md`). The opener carries the outcome, two lines and the card —
  the compliance ask moved to the gate, where it already ran; "about an hour; I go quiet while I write" is said up
  front. The analytics ask is a sentence, not a numbered list. `lm-gbp`'s status question carries its default.
- **Sandbox-unavailable path.** Any script failure → the structured text is uploaded as a plain document with one
  line, never "not saved" while the connector works (`shared/output-standard.md`, `shared/house-rules.md`).
- Also: the magnet guide's last "recommends three" passage; the REAL-naming quote replaced by the KB's wording;
  Mike's iceberg close as the closing page's shape; `Start with your upline` read by the magnet; the opt-in form is
  first name and email (phone optional); FAQ and trust lines marked "shape only — rewrite in the member's voice";
  `Testimonial video:` label; UTM source tags and a pre-headline swap test in the funnel appendix; newsletter
  cadence recorded (weekly floor, Mike's two to three a week); a two-round "another idea" cap the member hears;
  the older-offer refine trigger; one compliance duration (two minutes).
- **Brain (0.5.9):** `attraction-offer` writes `Lead-magnet seed: Step N — [name]` under `## How to talk about it`
  (the line the plugin reads, now actually written — `skills/attraction-offer/SKILL.md`, its interview guide, the
  Brain template's `identity/offer.md`); the offer card has a rejection branch (second no → keep seeds, name
  "refine my partner offer") and a plain gloss on the one brokerage question; the renderer parses the Current
  magnet line per field (a title containing " for " no longer breaks it), reads `keyword GUIDE` with or without
  the colon, and never prints the intake block on the board (`shared/render_board.py`); the template's intake
  block carries `Lane:`, `Mike's lesson:` and `Funnel doc:`.
- **Support (0.1.14):** `shared/stack-map.md` and `shared/cohort-kb.md` say ONE recommendation, Week 3 design
  assets, and how "designed" is kept this week; `shared/faq.md` likewise. New `docs/demo/lead-magnet-demo-checklist.md`
  for Tuesday's Week 2 demo. `docs/setup-guide.md` names the email list tool and the Calendly link in Week 2;
  `README.md` moves the Design Studio to Week 3.
  Versions: attraction-lead-magnet 0.6.2 · attraction-ai-brain 0.5.9 · maa-claude-support 0.1.14.

## [0.17.2] — 2026-11-08

**Brand and Claude Design move to Week 3 — the fix for the community thread.** Members finishing their Brain were
told, in the Brain setup's closing lines, to run "my attraction brand direction" the same week; that chat then sent
them to Claude Design to create a "Brand HQ" project and upload design skills. None of that is in Mike's Week 1 or
Week 2 training: Week 2 is the offer and the lead magnet, and the brand with Claude Design is Week 3. Every place
the OS said otherwise now says Week 3, and "Brand HQ" is gone as an instruction (a project of any name).
- `plugins/attraction-ai-brain/skills/attraction-brain-setup/SKILL.md`: the close names Week 2 ("build my partner
  offer", or "launch my lead magnet plugin" which builds the offer first) and says brand and Claude Design are
  Week 3 — nothing to do on them yet; the scaffold notes, the never-asks list and the front-door order agree.
- `plugins/attraction-ai-brain/skills/attraction-brand-direction/SKILL.md`: the Week 3 brand chat. A member who
  arrives while the offer is still at seeds hears one line — brand is Week 3's work, happy to do it now if they
  want — and is never told to open Claude Design, create a project or upload skills before Week 3. The brief
  reads "in your Week 3 Claude Design session"; examples are "shared", not "uploaded to Brand HQ".
- The brand template (`skills/attraction-brain-setup/references/brain-template/attraction-brain/identity/brand-visual.md`),
  `shared/brain-contract.md`, `shared/brand-doctrine.md`, `shared/how-we-speak.md`, `skills/attraction-brain-health/SKILL.md`
  (before Week 3 the two brand items read "coming in Week 3", never a nudge) and `shared/brain-book-spec.md`
  (the Book's Section 9: Week 2 first, the brand chat in Week 3; its callout is "build my partner offer").
- `plugins/attraction-ai-brain/shared/render_board.py`: the brand system sits in Week 3 on the map; the cohort-week
  cap applies to demo Brains only, so a real member's built system is never shown as "coming".
- Support (0.1.13): `shared/cohort-kb.md` (Week 1 plugs in the Brain and Support only; Week 3 adds the brand chat
  and the Design Package), `shared/stack-map.md`, `shared/faq.md`, `skills/maa-support-onboard/SKILL.md`, and a new
  `shared/error-codes.md` row for "it told me to go to Claude Design / Brand HQ right after my Brain".
- Member docs: `README.md`, `START-HERE.md`, `docs/setup-guide.md` (section 5 is Week 3; the checklist's brand
  items sit under Week 3), `docs/demo/brain-demo-checklist.md`, `docs/demo/youtube-demo-checklist.md`, the demo
  Brain's brand file.
- Lead Magnet (0.6.1): `plugins/attraction-lead-magnet/skills/lm-design/SKILL.md` briefs a clean neutral look when
  no brand exists yet (the normal Week 2 case) and says the Week 3 kit restyles it.
  Versions: attraction-ai-brain 0.5.8 · maa-claude-support 0.1.13 · attraction-lead-magnet 0.6.1.

## [0.17.1] — 2026-11-08

**The Brain Board reads a real member's offer.** The owner's check: when an agent builds their offer and their
lead magnet, the board must show it. The demo passed because its files bold every key; the real templates write
`Status: …`, `Join-gated package allowed: …`, `Host: …`, `Community name: …`, `Link: …` and compliance's first line
unbolded, which the renderer could not read — a member's finished offer would have rendered as "coming". Fixed
and proven on a template-shaped Brain (`plugins/attraction-ai-brain/shared/render_board.py`, Brain 0.5.7): a key
is read bold or plain, and the earliest line wins, so a file's header `Status:` beats a later section's.
- **The board keeps its pages between sessions.** The Book text and the Partner Offer text are the renderer's
  inputs for the member's pages and the offer page; they lived in `/tmp` and never reached the cloud, so every
  rebuild after the first session fell back to the raw files. Now `plugins/attraction-ai-brain/shared/brain-book-spec.md`,
  `plugins/attraction-ai-brain/skills/attraction-offer/references/partner-offer-doc.md` and
  `plugins/attraction-ai-brain/skills/attraction-goals/SKILL.md` write them to `~/attraction-brain/exports/`, and
  `plugins/attraction-ai-brain/skills/attraction-brain-sync/SKILL.md` carries `exports/*.txt` to
  `01 · AI Brain/_engine/exports/` on every push and pulls them back (`plugins/attraction-ai-brain/shared/drive-map.md`
  and the setup tree in `plugins/attraction-ai-brain/skills/attraction-brain-setup/SKILL.md` say so).
- Demo board re-rendered after the demo's keyword became GUIDE everywhere.
  Versions: attraction-ai-brain 0.5.7.

## [0.17.0] — 2026-11-08

**Plugin 3 — the Lead Magnet — returns to the marketplace, audited against the Brain it reads.** Members built
their Brains last week; Week 2 opens on the offer and the lead magnet. `plugins/attraction-lead-magnet` (0.6.0)
comes back from `wip/all-plugins` with every reference checked against the Brain as it stands today (the
2026-11-02 rebuild, the Brain Board, the cloud workspace), and `.claude-plugin/marketplace.json` lists it again.
- **Everything lands in the member's own cloud.** The plugin's `shared/brain-contract.md` now states the law its
  skills follow: every Brain write (`memory/magnets.md`, `memory/list-growth.md`, `identity/profiles.md`, the
  `brain.md` line, the `config.md` block) pushes through `attraction-brain-sync` the moment it is written and
  re-renders the member's Brain Board; every document is uploaded by the member's own Drive or OneDrive connector
  into its drive-map folder with the link in chat; all three Brain files are on the sync skill's pull allowlist,
  so a new session reads them back. `lm-profiles` and `lm-gbp` name the push step and say where the file landed;
  `shared/output-standard.md`'s confirmation line names the real folder, not always Guides.
- **The Brain Board reads the magnet.** `plugins/attraction-ai-brain/shared/render_board.py` (Brain 0.5.6)
  accepts the locked `as of YYYY-MM-DD` form of the Current magnet line; the demo Brain gains
  `docs/demo/taylor-brooks/attraction-brain/memory/magnets.md`, its keyword is GUIDE everywhere, and the demo
  board is re-rendered. The navigator's close tells the member the magnet is on their board.
- **Aligned with the Brain's rulings.** Compliance is read by its first line only — `Status:` is the verdict —
  and the bracket scan that could override a `set` verdict is gone (`shared/house-rules.md`, `lm-magnet`).
  Recruiting scope is anywhere, never a limit, never flagged (`lm-funnel`, `lm-delivery`, `lm-partnerships`).
  The booking link, call length and cadence come from the Brain; when `identity/operations.md` still reads
  "set in Week 2", every skill says the one phrase ("set up my attraction operations") once and falls back to
  the DM or email channel instead of a bracket — the funnel's `Booking embed:` reads `none yet — Week 5`
  (`lm-funnel` and its `references/funnel-guide.md`, `lm-magnet`, `lm-delivery`, `lm-nurture`, `lm-gbp`, the
  navigator's `references/intake-questions.md`). The offer is read by its current sections — the program, the
  framework, the core-promise line, and the upline and brokerage-rule pages whose wording the funnel, the bios
  and the DMs reuse — and the avatar fields by their real names (`lm-profiles`, `lm-magnet-ideas`).
- **One magnet, everywhere:** the last "recommends three, the member picks" passage, in
  `skills/lm-magnet/references/magnet-guide.md`, now matches the ONE-card rule.
- **No installed-plugin assumptions:** the design brief and the funnel outline stand on their own in Claude
  Design (the Design Studio's skills read the same documents when the member has them); the Google kit speaks
  of Reels "from Week 3"; the Events plugin is "Week 6" (`lm-design`, `lm-funnel`, `lm-gbp`, `lm-partnerships`).
- Support (0.1.12): `plugins/maa-claude-support/shared/stack-map.md` lists Plugin 3 as live. `README.md`,
  `docs/setup-guide.md` and `CLAUDE.md` name the three plugins on `main`. The Brain's `attraction-offer` reads
  the avatar fields that exist.
  Versions: attraction-lead-magnet 0.6.0 · attraction-ai-brain 0.5.6 · maa-claude-support 0.1.12.

## [0.16.1] — 2026-11-03

**The Brain Board on every paid plan, with nothing to install.** The owner's check before onboarding: members on
Pro — no Claude Code, no Max — must still get the board. Verified against Anthropic's current pages: Cowork is on
every paid plan and not on the free plan; since October 6 tasks on Pro, Max and Ultra run in Anthropic's cloud,
where plugins, connectors and scheduled tasks all run; and the renderer is Python only, no package, proven on
Python 3.9 (older than the sandbox's). What changed so the board holds up away from this machine:
- `plugins/attraction-ai-brain/shared/board-template.html` + `shared/render_board.py`: the page now carries a
  **quick view** — plain text on a white page: where they stand, today's three moves, this week, what is waiting on
  them, and how to open the full board — shown only where the board's scripts cannot run (a cloud-drive preview, a
  mail viewer, a code viewer). A one-line script flags the document when scripts do run, so the quick view never
  flashes on the real board.
- The output is a complete document (`<!doctype html>`), so Safari, Chrome and Edge render it in standards mode —
  the same mode as the artifact the owner reviewed.
- The board is rendered on the **member's clock**: `config.md → Timezone` decides "today" and the sync line. A cloud
  sandbox runs on UTC and would have flipped the day every evening. `--today` (the sync skill now passes it) wins; a
  demo brain keeps its scorecard date; an unknown zone prints the date without a clock time.
- `attraction-brain-sync` PUSH step 4 and `attraction-brain-setup`: pass `--today`; find `render_board.py` when
  `${CLAUDE_PLUGIN_ROOT}` is empty; the honest line when the session's code sandbox is unavailable ("workspace
  unavailable") — keep the previous board, say it once, never write the board by hand; and the hand-off tells the
  member how to open it (download the file and open it; the drive's preview shows only the quick view).
- `plugins/maa-claude-support/shared/error-codes.md`: two rows — the code sandbox that didn't start (files safe; new
  chat; reopen the app; Windows needs virtualization on; the board rebuilds on the next save) and "my Brain Board is
  just code / a blank page" (download and open; the quick view is deliberate).
- Member docs (`README.md`, `START-HERE.md`, `docs/setup-guide.md`, the demo checklist): the install path matches the
  current app — **Customize → Plugins → ＋ beside Personal plugins → Add marketplace**; the free plan has no Cowork
  and Claude Code is not needed; tasks run on Anthropic's servers. Demo board re-rendered.
  Versions: attraction-ai-brain 0.5.5 · maa-claude-support 0.1.11.

## [0.16.0] — 2026-11-03

**The launch cut: Plugins 1 and 2 only.** Cohort 1 is onboarded tomorrow; the owner's call is that members must not
install plugins that are still being fixed and optimized. `main` and the marketplace now carry **attraction-ai-brain
(0.5.4)** and **maa-claude-support (0.1.10)** only. The other seven plugins, the Design Studio skill set and the
vendor script are parked, unchanged, on the **`wip/all-plugins`** branch (pushed; nothing is lost) and return to the
marketplace one by one as the cohort reaches them.
- `.claude-plugin/marketplace.json` lists the two plugins. `README.md` and `CLAUDE.md` say where the rest live.
- `plugins/maa-claude-support/shared/stack-map.md` carries the launch note; every parked row reads **coming**, so the
  desk never tells a member to install a plugin that is not there.
- `scripts/check-release.sh` check 12 skips the content engines while they are parked.
- Members install with: Customize → Personal Plugins → Browse Plugins → ＋ → Add marketplace →
  `teamsherrard/claude-agent-attraction-os` → Install Plugin 1, Install Plugin 2, Sync automatically.

## [0.15.4] — 2026-11-03

**The Brain Board: a real business plan and tracker, and the board says how it stays current.** The owner's two
notes: the goal tracking needed to be a proper business planning and tracking section, and the member must never
have to update the board by hand. In `plugins/attraction-ai-brain/shared/render_board.py` and
`shared/board-template.html`:
- The goals page is now **Your business plan and tracker**: the why; the ring and bars; **Where you stand against
  your plan** — every 30-60-90 measure scored Ahead / On pace / Behind against the ramp the member locked (the
  plan's expected figure for today, the actual from their rows; the Brain's own three words, never a grade or a
  percentage); **Your plan at a glance** (the 12-month goal, the 90-day target, the activity they control, the three
  non-negotiables, the next step); **Week by week** — a bar chart of conversations a week against the target with
  the Friday rows and the week in progress, plus the weekly table; **Your pipeline** as a funnel in the locked stage
  order; then the vision, the numbers, the 30-60-90 table, this week, the rows, the prospects, the four quarters,
  the non-negotiables, the intangibles, how the score works. The tile is now "Your business · plan · tracker" and
  its quarter bar carries the pace word.
- **How this board stays current** on the At-a-glance page, read from `config.md`: every write by any system
  saves to the member's cloud and rebuilds the board; the daily debrief's state and time (with the one phrase to
  turn it on when it is off); Claude Design work lands in the folders and the next Brain session catches up. The
  Today page carries the same nudge when the debrief is off.
- The weekly activity line is built from the scorecard's targets (no more raw list text). Demo re-rendered.
  Versions: attraction-ai-brain 0.5.4.

## [0.15.3] — 2026-11-02

**The Brain Board, built for daily use.** In `plugins/attraction-ai-brain/shared/board-template.html` and
`shared/render_board.py`: a "Print this page" button on every page when the board is opened as a file (hidden
inside the claude.ai viewer, which cannot print) with a print stylesheet that prints only the open page; a
floating "Back to the top" button once a long page is scrolled; a copy button beside the This-week phrase on the
tile; search now also finds the open items and today's moves; a Brain with no locked targets gets a plain
empty state on the goals tile instead of "0 of 0"; moves from a debrief older than a day are labelled with that
debrief's date; the phone chips are grouped under "Your Brain" and "Your systems"; a board saved without its
data says so instead of failing silently; and the renderer skips any Brain file that is still the shipped
template, so a half-built Brain never shows placeholders. Demo re-rendered. Versions: attraction-ai-brain 0.5.3.

## [0.15.2] — 2026-11-02

**The Brain Board, tidier pages.** The owner's note: the Partner Offer page opened on a wall of identical pills.
In `plugins/attraction-ai-brain/shared/board-template.html` and `shared/render_board.py`: the contents of a long
page is now a numbered two-column "Contents" box, not pills; the Partner Offer's sub-bands and the Brain files'
`###` headings render as sub-headings instead of top-level entries (16 entries, not 23); the promise quote comes
before the contents; the "reads from your Brain" chips are lighter and sit in their own row; the section pages
keep their sentence-case titles (the title-casing bug turned "What's next" into "What'S Next"); labels longer
than 48 characters render as a bold lead instead of a cramped key column; a label with no value becomes a
sub-heading; bracketed demo tags are stripped; the "Everything on file" block folds away by default and opens
on a click; the two bottom map labels no longer touch. Demo re-rendered. Versions: attraction-ai-brain 0.5.2.

## [0.15.1] — 2026-11-02

**The Brain Board, easier to see.** The owner's rule: most members are older agents, so the board reads at a
glance. In `plugins/attraction-ai-brain/shared/board-template.html`: body text 17px at medium weight (Manrope 500),
map labels 18px, every tile, chip, legend and document size up one to two steps, bigger checkboxes and day
markers, brighter secondary text on the dark board and darker on the white pages; the "coming" systems are no
longer faint grey hollows but mint-ringed discs with light labels, and their dashed spokes and ring are brighter.
Demo re-rendered: `docs/demo/🧠 Taylor Brooks's Brain Board — DEMO — 2026-10-08.html`. Versions:
attraction-ai-brain 0.5.1.

## [0.15.0] — 2026-11-02

**The Brain Board — the member's Brain as a living map, always in sync.** The user's ruling: the board has to be
valuable, something the agent opens daily and comes back to, show the business goals and the goals tracker from
the plan, and update whenever anything in the Brain changes.

- **New `plugins/attraction-ai-brain/shared/render_board.py`** (stdlib only, no python-docx) renders one
  self-contained HTML page from a Brain folder: the map (the member in the centre, the nine parts of the Brain as
  the inner ring, the eight weekly systems as the outer ring, lit by state); four tiles above it (the goals
  tracker — the 12-month ring, this week's conversations and calls against target, the quarter's joins, the daily
  slice; today's three moves from the last Debrief; this week's build with the phrase to type; the open items);
  and a full right-hand DOCUMENT page for every dot, tile and the centre — the Book's nine sections verbatim plus
  "everything on file", the Partner Offer in full with the member's own pages, the brand direction with swatches,
  the lead magnet and its funnel, the coming systems with what they already know, the goals page from goals.md ·
  execution-framework.md · scorecard.md · pipeline.md · organization.md, today from debriefs.md, and the open
  items derived from real lines in the files (funnel not live, host not set up, join-gated rule unknown, a
  drafted line to confirm, a partner's written OK, the brand kit, compliance set-not-confirmed, targets unlocked,
  signature phrases drafted). Search over every page and every phrase to say; checkable moves and open items
  (kept per browser); related nodes light up on the map; white paper pages over the dark map; phone layout.
  `--week N` caps the lit systems for demos; `--today` sets the day. Money scenarios stay off the board.
- **New `shared/board-template.html`** — the page the renderer fills (`/*__BOARD_DATA__*/`); never edit the output.
- **Always current:** `attraction-brain-sync` re-renders the board on EVERY push (new PUSH step 4 and a Rule),
  so a write from any plugin — the offer, the magnet, the pillars, the pipeline, a capture from the car —
  reaches the board without anyone asking. `attraction-brain-setup` renders it right after the Book at the
  close, and "open my brain board" / "refresh my brain board" is the manual way (front door + description).
- **Docs:** the Brain Board in `shared/brain-contract.md` (documents produced), `shared/drive-map.md`
  (`01 · AI Brain`), `docs/BRAIN-CONTRACT.md` (the write protocol), `docs/setup-guide.md` (what Week 1 hands
  you), `docs/demo/brain-demo-checklist.md` (the close + the optional move), and the rendered demo
  `docs/demo/🧠 Taylor Brooks's Brain Board — DEMO — 2026-10-08.html` (Week 2, day 10 of the demo quarter).
- Versions: attraction-ai-brain 0.5.0.

## [0.14.0] — 2026-11-02

### The Lead Magnet and the offer on Mike's notes (the owner's written feedback on Week 2, 2026-11-02)
- `lm-magnet-ideas` (Lead Magnet 0.5.0) recommends ONE lead magnet on one card under 120 words (the name, the promise in one line, why this one for this member in two lines); "yes" builds it, "another idea" shows the next best, one at a time, never three at once. The three kinds (a tool, a plan, a decision or proof piece) stay as the skill's own reasoning. `lm-navigator`, `lm-magnet`, `lm-funnel`, `shared/house-rules.md` (rules 1, 5 and 11), `shared/output-standard.md`, the Lead Magnet contract, the plugin and marketplace descriptions and the Brain template's `memory/magnets.md` follow.
- The Week 2 outcome statement, in Mike's words, opens the Lead Magnet welcome and sits in `plugins/maa-claude-support/shared/cohort-kb.md`, `stack-map.md`, `docs/setup-guide.md` and `README.md`: by the end of the week, ONE lead magnet written and designed with its funnel outline (tangible), and the unique value proposition broken down: the offer explained in detail and how to create it, its name, the marketing language, and where to host it (intangible).
- `attraction-offer` (Brain 0.4.1): the naming rule (the outcome plus the mechanism, in words an agent says; the "I need that" test and the "says what it solves" test; banned name words such as collective, club, portal, hub and network; two alternate names on the card, the member picks; a community name is the home the program lives in, never the program's name). The brokerage rule: one Week 2 question, "does your brokerage restrict offering a package as a reason to join?", stored in `identity/offer.md` as `Join-gated package allowed: yes | no | unknown`; "no" or "unknown" switches every public line to the teach-first register (what you teach, your story, your mentorship, offered to any agent). The Partner Offer document gains the member's own pages: how to create it (a checklist), start with your upline (and the three signs you are ready to build your own), the brokerage branch, the marketing language (three one-liners, the 30-second explanation, a DM line, a bio line, a video intro line, in the member's voice), where to host it (Skool recommended, Circle as the alternative, one community, one welcome post, one weekly call; the affiliate link is a placeholder until the cohort sets it), and the content branches (five to seven segments of the UVP with three topics each). `references/interview-guide.md`, `offer-template.md` and `partner-offer-doc.md` carry the shapes; `shared/brain-contract.md` and `docs/BRAIN-CONTRACT.md` the ownership rows.
- The UVP is the foundation of the content: `sf-gameplan` (Short-Form 0.2.2) and `yt-gameplan` (YouTube 0.2.2) build pillars, angles, lanes and titles from `identity/offer.md → ## Content branches` first, the Brain's signals second, the starter banks last.
- Design Studio: `design-studio/skills/aa-offer-kit-design` and `aa-lead-magnet-design` read one guide and the outcome-based program name; the member's own pages never appear on an agent-facing piece.
- Support (0.1.10): the Skool affiliate link placeholder (`[NOT SET]`) in `cohort-kb.md`; the new modes in `stack-map.md`.
- Demo: the Partner Offer re-run under the rules. "The Sunday Table" failed the "says what it solves" test (it names a gathering) and stays as the name of the group; the program is "Buyers From Open Houses" with two alternates recorded. Rendered as `docs/demo/💼 Taylor Brooks's Partner Offer — DEMO — 2026-11-02.docx` (input `docs/demo/taylor-brooks/attraction-brain/exports/partner-offer-DEMO-2026-11-02.txt`); the 2026-10-18 render retired. The Brain Book demo is untouched (Week 1 state).
- Versions: attraction-ai-brain 0.4.1 · attraction-lead-magnet 0.5.0 · attraction-shortform-system 0.2.2 · attraction-youtube-system 0.2.2 · maa-claude-support 0.1.10.

## [0.13.0] — 2026-11-02

### The Brain setup rebuilt on Mike's notes (the owner's written feedback, 2026-11-02)
- `attraction-brain-setup` (Brain 0.4.0): the interview is Mike's 26 questions in his order and his wording, one plain question per message with "your turn" at the end, in four conversations (who you are as a leader · your unique approach · your story and your proof · your current and future state), then three answers out loud by voice dictation (why you're excited about agent attraction · your WHY · why someone should partner with you). Who their story speaks to is worked out from the answers and never asked. The setup never asks about CRM, booking or calendar links, scheduled tasks and their timing, compliance, the operations rhythm, the brand, which type of agent, or where they can attract: the brand is a second Week 1 chat (`attraction-brand-direction`), compliance is a pasted brokerage link (`attraction-compliance`), the booking link, CRM and tools are Week 2. Four things the interview is for, stated at the top: core and story feed the brand and the content; experience feeds the UVP; the brokerage story feeds the content; the upline feeds the UVP. "I don't know" is a placeholder and the next question; one consult list (the WHY, the sponsor, the strategy, the 12-month number); two allowed follow-ups in the whole setup; no "Ready?" bundling, no read-backs, no confirmation rounds. About 32 turns, 45 minutes to an hour; only five files reach the cloud before question 1; each conversation checkpoints, pushes and stamps. The word "beats" is gone from every plugin (`shared/how-we-speak.md` bans it).
- The Agent Attraction Brain Book is short and structured: nine sections (Who you are · Your story · Your brokerage story · Your unique approach · Your proof · Who your story speaks to · Your numbers · Your voice · What's next) on at most fifteen pages, a target and a maximum per section, paragraphs of at most four sentences, plain words (no downline, no unexplained upline, no "the model", no UVP, no funnel), commands only in the last section, the three spoken answers in Section 8, and a state rule so a Week 1 Book renders the Week 1 state. `shared/brain-book-spec.md` is the contract; `shared/measure_book.py` is the gate the close runs on the rendered file; `shared/render_doc.py` renders SECTION bands. Demo re-rendered at the end-of-Week-1 state: `docs/demo/📕 Taylor Brooks's Agent Attraction Brain Book — DEMO — 2026-11-02.docx` (2,564 words, about 13 pages; input in `docs/demo/taylor-brooks/attraction-brain/exports/brain-book-DEMO-2026-11-02.txt`).
- Brain template: `identity/avatars.md` is derived ("your skills attract any agent; these are the agents who will relate most", never a place); `identity/goals.md` seeds the four numbers and one proposed weekly rhythm; `identity/operations.md`, `compliance.md` and `brand-visual.md` carry status lines only at setup; the Realtor Brain bridge is one question at the import step. `attraction-brand-persona`, `attraction-persona-map` (DERIVE mode), `attraction-story-bank`, `attraction-voice-proof`, `attraction-voice-print`, `attraction-import`, `attraction-prospect-radar`, `attraction-brand-direction`, `attraction-operations` and `attraction-offer` aligned; `shared/ask-once-default.md` carries the one-question-per-turn carve-out (identical in every plugin).
- Downstream contract fixes from the rebuild: `sf-gameplan` now writes the Brain's `Filming window:` line (Short-Form 0.2.1; the YouTube readers and `yt-board/references/thirty-day-mapping.md` repointed, YouTube 0.2.1); Events no longer reads the deleted geography field (`ev-navigator`, `ev-strategy`, `ev-virtual`, `ev-promo`; Events 0.1.4); `admin-recruiting-scorecard` and `sales-scorecard` never score against targets that are not locked yet (Admin 0.3.1, Conversion 0.1.5); recruiting-scope exclusions reworded to licensing notes only; `lm-delivery` reads the typed voice sample (Lead Magnet 0.4.1); the Friday slot defaults to 4:00 pm when operations is untouched; `design-studio/skills/aa-content-design` sources the Why Join Me five-slider from the Offer document. The vendored editor is untouched; its phrase patch is logged in `docs/plans/SEAM-LOG.md`.
- Docs: `docs/setup-guide.md`, `docs/playbooks/playbook-1-agent-attraction-brain.md`, `START-HERE.md`, the Support desk's `plugins/maa-claude-support/shared/cohort-kb.md` and `stack-map.md` (Support 0.1.9) describe the new setup; new `docs/demo/brain-demo-checklist.md` (what to say, in order, with the demo member's answers).
- Versions: attraction-ai-brain 0.4.0 · attraction-shortform-system 0.2.1 · attraction-youtube-system 0.2.1 · attraction-conversion-sales 0.1.5 · attraction-ai-admin 0.3.1 · attraction-events-workshops 0.1.4 · attraction-lead-magnet 0.4.1 · maa-claude-support 0.1.9.

## [0.12.0] — 2026-10-18

### The AI Admin journey, shown not asked (the user's verdict on the live demo: "messy and not valuable")
- `admin-attraction-setup` (Admin 0.3.0): two messages. A two-line hello, then the member's first Morning Brief built for real from the Brain, the calendar and the inbox (today's calls with prep, agent inquiries with reply drafts, the follow-ups due with the message drafted in the member's voice, content due, the week so far against target, three moves, one coaching note) and the pipeline at a glance; then one consent card (Morning Brief and the Daily Follow-Up Queue right after it, plus the Daily Debrief if it is not on), the registry block written silently with defaults, and a five-phrase hand-over. No step numbers, no config on screen, no name, VA or CRM questions ("call my admin [name]", "set up my VA packs", "mirror my CRM" on demand). The Morning Brief is one artifact whether run at setup, on demand ("my morning brief") or by the scheduled task; the queue's rows are the brief's follow-ups section with their drafts.
- Registry keys, task ids, cron defaults, ownership, the request shapes and draft-only consent are unchanged. The setup guide, the Support desk, the contracts and the plans describe the new journey.
- Versions: attraction-ai-admin 0.3.0 · attraction-ai-brain 0.3.5 · maa-claude-support 0.1.8.

## [0.11.0] — 2026-10-18

### The offer step shown, not asked; three different magnets; a readable Partner Offer (the user's verdict on the live run: "the journey, the ideas, the doc, all of it needs improvements")
- `attraction-offer` (Brain 0.3.4): the member sees one message, an offer card of about 150 words drafted from the Brain (name and promise, who it is for, the method as a chain, five things they get, the weekly rhythm, the 90-day outcome) and one line, "Does this feel like you? Say yes, or change anything." No numbered decisions, no assumptions block, no four-line menu in chat; the assumptions live on the document's last page. On yes the document builds silently and, when the Lead Magnet plugin started the session, hands straight to the ideas.
- The Partner Offer document is re-shaped for the agent reading it: a cover with the tagline, an at-a-glance page (ten rows), then who this is for · the promise told once · the method in N steps · inside the program for 90 days · what you get · your first 30 days · how we work together · proof · why now · your next step, and an appendix for the member's own content lines and "what I assumed". The method appears in full once; no taxonomy lectures; paragraphs of three sentences; one demo note on the cover with a short "(demo)" marker on figures. 2,000 to 3,200 words with floors per section and the same substance gate. Demo re-rendered (3,435 words) and the 2026-10-10 demo retired.
- `lm-magnet-ideas` (Lead Magnet 0.4.0): three genuinely different magnets by rule, one from each lane (a tool, a plan, a decision or proof piece), never two from the same framework step; each a card with a real lead-magnet title, a one-sentence promise, who it is for, what is inside and why it converts in plain words; lesson citations recorded in the Brain, never printed in chat; a title search check against what agents actually type; one recommendation, one reply. `lm-navigator` wraps the card and the cards; house rules, the intake and the writer's shapes updated.
- Versions: attraction-ai-brain 0.3.4 · attraction-lead-magnet 0.4.0 · maa-claude-support 0.1.7.

## [0.10.0] — 2026-10-13

### The Short-Form and YouTube journeys (the user's verdict on the live demos: "the sequencing and journey doesn't make any sense; it's missing Notion, the scheduled workflows and the game plan")
- `sf-setup` now runs one clear journey, each step announced: (1) profile optimization across every platform the member uses (bios, name fields, link in bio and the order of its links, highlights, pinned posts) as one Profile Optimization Pack; (2) the NEW Short-Form Game Plan (`sf-gameplan`: positioning, the five pillars with three angles each, the format mix and cadence, a 30-hook bank, the CTAs and the comment-to-DM flow, a dated 30-day calendar of twenty posts plus the stories rhythm, the Friday measures, the workflows; a hard gate before delivery; it owns the pillars file now and writes the dated calendar into the Brain's new content calendar file); (3) the Notion board found or created with the next 30 days mapped as dated Idea cards (`sf-board`); (4) one consent card for three draft-only workflows (the NEW Monday Week Plan `sf-week-plan` on by default, the Friday Content Performance on, Daily Stories off by default, each with its task-prompt reference); (5) the first Reel. The posting-tool connect stays the optional last item.
- `yt-setup` mirrors it: the Channel Page Kit as copy-paste blocks, the Game Plan inline, the board with the next 30 days of videos including the interview slots (the shared board spec's window is 30 days for both engines now), one consent card (the Monday Kickoff on by default, the Friday YouTube section, the Monthly Channel Review off by default; the never-provisioned weekly-ideas task retired), then the first video. `yt-gameplan` writes the dated calendar into the Brain; the Monday Kickoff keeps 30 days on the board and drafts the week's video onto its card.
- Scheduled agents OS-wide now count thirteen, eleven on by default with the member's yes and two off by default, listed with owners and task ids in the OS contract, the Brain contract, the master plan, the Support desk and the setup guide. The Brain template gains the content calendar file and the channel file's setup stamp.
- Versions: attraction-ai-brain 0.3.3 · attraction-shortform-system 0.2.0 · attraction-youtube-system 0.2.0 · maa-claude-support 0.1.6.

## [0.9.0] — 2026-10-10

### The program block feeds every system (the user's sync rule: the UVP, the program and the lead magnet feed everything)
- Every reader of the offer outside the offer skill now reads the v0.7.0 program blocks (the program, the framework, the structure, support and community, the deliverables table, the Day 1 lines, the lead-magnet seed line) with the fallback to the older Partner Offer block: the Lead Magnet navigator, ideas, writer, funnel, nurture and profiles (the magnet is cut from one named framework step; the funnel's offer section carries the program's name, type and cadence); the Design Studio's offer kit (the stack's tiers are the deliverables, the one-pager and deck carry the framework line), funnel and value vault (the course outline mirrors the structure, the onboarding roadmap reads Day 1); Conversion's presentation, call prep and enrollment script (type, cadence, the 90-day outcome, Day 1 as "what happens next"); Events (a workshop topic is one framework step taught live); YouTube and Short-Form (the framework line as hook material); the Brain's free-vs-paid, model positioning, why-join-me and brain-health (the Program quick-reference line refreshed when stale); the Support desk's Week 2 rows; the OS contract's read rows; Book Chapter 1 lists the Program line once finalized.
- Versions: attraction-ai-brain 0.3.2 · attraction-conversion-sales 0.1.4 · attraction-events-workshops 0.1.3 · attraction-lead-magnet 0.3.1 · attraction-shortform-system 0.1.6 · attraction-youtube-system 0.1.6 · maa-claude-support 0.1.5.

## [0.8.0] — 2026-10-10

### Lead magnet and funnel copy, dialled in (user ask: "super high-quality copy, a really good hook, context, ending, calls to action")
- `lm-magnet`: one document architecture for every shape, with floors: the cover (a title in the reader's words, a three-line lived hook), the opening page (the context and "how to use this"), 4 to 8 body pages of one idea each where every page carries a sourced number, a script, a template, a checklist or a true story, the "what to do next" page, the "how [first name] helps next" close, the back page; exactly three calls to action, all a conversation, the booking link only on the closing page; a 17-check gate; 1,800 to 3,500 words. Design-cue labels (pull quote, callout, checklist, template rows, script, source, image idea, next step) travel inside the doc and `aa-lead-magnet-design` turns each into its page element.
- `lm-funnel`: the sales funnel outline carries eleven sections in order (the hero with a pre-headline, the video and the attraction line · the problem · the product · who I am with "why partner with [name]" · the journey · the offer with "a sneak peek inside [program]" · why join me · proof with the optional YouTube block · the organization · book a call with "how it works" · the opt-in with the FAQ); the opt-in repeats top, middle and bottom and the book-a-call area is the second path (house rule 4 rewritten); the booking step gains "what we'll cover"; a 20-line CTA bank; a 15-check gate. `aa-funnel-design` consumes every label (video embed or headshot fallback, booking embed, FAQ, the optional qualifier field). Drawn from HCC's Agent Attraction Funnel Guide, compliance-cleaned.

### Week 1 brand: creative direction, a brief that never disappears, the HCC house style
- `attraction-brand-direction`: one plain question replaces the direction interview; examples go into Brand HQ; the Brain derives a Creative direction block (mood, energy, type, colours, photos, three motifs, the avoid list, three reference looks) the member reacts to once; the Design Package brief v2 carries it, is saved to the Brand folder, and "show my design package brief" reprints it. `attraction-brain-setup` prints the full brief as its last words. Book Chapter 5 renders both (400+ when set).
- The design system gains a seven-look house style library and a device glossary. `aa-logo-design` adds the 3×2 variations grid over dark and white, the subordinate brokered-by lockup, the "[Organization] by [Name]" construction, foil and gradient finishes and emblem marks. `aa-style-sheet-design` follows the HCC sheet skeleton (header, brand info, variations, swatch cards, type roles and text styles, the graphic-elements trio, applications). `aa-brand-kit-design` adds the organization family (milestone, anniversary, member of the month, welcome single / 4-up / 16-grid, the DM CTA post, the thumbnail master, the profile-circle set, stories).

### Content starter banks from HCC's Agent Attraction Video List
- `yt-gameplan` and `yt-ideation`: a 42-title starter bank (the four-month arc plus eight interview angles), every title compliance-cleaned and tagged by lane, pillar, agent type and pain; the Game Plan offers it as the default arc when the member has no titles of their own; the WHY statements join channel positioning. `sf-ideas`: a 30-hook starter bank by pillar and the eight-principle check on the week's five. One logistics title dropped.
- Versions: attraction-ai-brain 0.3.1 · attraction-lead-magnet 0.3.0 · attraction-youtube-system 0.1.5 · attraction-shortform-system 0.1.5.

## [0.7.0] — 2026-10-10

### The Partner Offer is a program definition (the user's verdict on the live demo: the 1,000-word offer was "very not good")
- `attraction-offer` (Brain 0.3.0): the Partner Offer document is now a 14-section program definition with word floors (2,500 to 4,000 words): the promise · what this is (name, one of six program types, who it is for, the 90-day outcome, format, cadence, duration, cost to the agent, what it is not) · the named framework (3 to 7 steps with the tool and where it is taught) · the problems it solves · how the program is built (phases, live vs recorded) · what you get (6+ deliverables across the three layers) · the first 30 days with the Day 1 sequence · support and community · the three layers · the playbook and the lead-magnet seed line · proof · why now · how to talk about it · next step and the compliance line. A 14-check verification gate runs before delivery (type, name, framework, phases, onboarding, deliverables, brackets, length, compensation words, proof). The interview adds the program questions (type and format, cadence, framework name, program name, recorded vs live, support), each pre-answered with a recommended default.
- `identity/offer.md` gains `## UVP`, `## The program`, `## The framework`, `## Structure`, `## Support & community`, the deliverables table, the Day 1 lines and the `Program name:` / `Program type:` header lines; `brain.md` gains the `Program:` quick-reference line (written at finalize); Book Chapter 10 carries the program block, the framework table and the structure outline (700+ words when finalized). Ownership rows updated in the Brain contract and the OS contract.
- Demo: `docs/demo/` gains the rendered Partner Offer for the demo member (4,813 words: "The Sunday Table", a mentorship program on the Five-Step Sunday Routine) with its renderer input in the demo exports folder.
- Readers of the new blocks (Lead Magnet, Conversion, Events, YouTube, Short-Form, the Design Studio's offer kit, funnel and value vault, and the Brain's own siblings) are repointed in the next release.

## [0.6.0] — 2026-10-10

### Design Studio: 14 → 10 skills + the video kit (user decision, 2026-10-10)
- The Claude Design skill set goes from 14 skills to 10. The three Week 1 skills (`aa-logo-design`, `aa-style-sheet-design`, `aa-brand-kit-design`) are exactly as they were. Three kit skills replace eight single-piece skills, whose directories are gone: `aa-offer-kit-design` merges the former offer stack, offer assets, and product mockup skills (pieces in kit order: the product mockup with the one canonical cover, the 3D offer stack, the "Join My Team" one-pager, the opportunity deck, the welcome pack, the model comparison sheet — the three sources' compliance rules kept word for word); `aa-content-design` merges the former carousel and recognition skills (every carousel rule — 4:5, the grid-safe hook cover, the LinkedIn PDF version law, the story echo, the Why Join Me five-slide quick win — and every recognition rule — consent, no figure unless stated, never against another brokerage); `aa-value-vault-design` merges the former playbook, course, and ebook skills and adds the partner onboarding roadmap. Upload order and zip numbers: 01 logo · 02 style sheet · 03 brand kit · 04 offer kit · 05 lead magnet · 06 funnel · 07 content · 08 video kit · 09 event · 10 Value Vault (`build.sh`).
- The kit pattern: one SKILL.md holds the shared rules (Design System first, the Brain Book, compliance, the verbatim law, exports, folders, the five golden rules word for word), a mode router that never asks a menu when the phrase or the brief already names the piece, and a kit run — "design my offer kit" / "design my content" (only when one brief covers several pieces) / "design my value vault" — that builds the pieces in a fixed order with ONE checkpoint after the masters (the offer kit: the canonical product cover and the transparent stack object; show them, get a yes, then everything else without stopping). Each retired skill's body moved verbatim into the merged skill's references (`product-mockup.md`, `offer-stack.md`, `offer-assets.md`, `carousel.md`, `recognition.md`, `playbook.md`, `course.md`, `ebook.md`) beside its old references (`mockup-craft.md`, `deck-and-document-craft.md`, `carousel-craft.md`, `recognition-specs.md`, `playbook-specs.md`, `course-specs.md`, `ebook-specs.md`; `export-page.md` and `mockup-craft.md` byte-identical across skills). Nothing about a piece got shorter; a piece stays callable alone by its own phrase; the union of the old trigger phrases is kept; every description is a folded block scalar under 1000 characters with no hyphen split.
- The partner onboarding roadmap (new, `onboarding-roadmap.md` in the Value Vault): the Day 1 → Week 1 → Week 2 → Week 3 → Day 30 poster with what you do / what I do / done when per stop, the new-partner welcome checklist with real checkboxes, and the "where to show up" card (the weekly call, the group chat, the member's booking line, the first lesson), built from the Partner Offer's "First 30 days as a partner" table and the Book's How You Operate chapter in the locked Design System; print-kit mechanics like the playbook; a missing week is labelled "set in your Brain", never invented; nothing about compensation; lands in `05 · Offer/Onboarding`. Triggers: "design my onboarding roadmap", "my partner onboarding poster", "new partner checklist", "where to show up card", "my 30-day partner roadmap".
- The video kit (new, `aa-video-kit-design`, Week 3, uploaded with the Riverside plugin; it can run any time after the style sheet exists): the realtor cohort's Video Brand Kit v3.3 recycled with the editor's sync contract kept whole — the canonical file names, the zones and their numbers, transparent full-canvas overlays, the preview sheets, the export page ("Download the kit"; Claude Design has no PNG export; the button writes the Video Brand Spec text file, video-brand-spec.md, into the zip), the build-order limit, the video-safe rules, the engine notes, the Video Brand Spec fields, the self-check, the tweaks — verified read-only against the vendored editor's `brand-wiring.md` (the assets block, the canonical names, the eight `cta_pack` keys subscribe · comment · guide · call · book · dm · link · follow), `cta-pack.md`, `graphics-style.md`, and `studio-setup` (which registers the kit from `02 · Brand/Video Brand Kit/`). Adapted to agent attraction: the member is a leader attracting agents; the intake reads the member's locked Design System and the Brain Book first (the style sheet's colours and fonts, the UVP one-liner, the offer's comment keyword, the live lead magnet's name and keyword, the booking line, the compliance lines) and asks only what they cannot answer; the CTA pack keeps the same eight keys and bakes attraction defaults overridden by the Brain's own words (subscribe "Subscribe for more", comment "Comment [keyword]", guide "Comment GUIDE for the free guide", call "Let's talk, link below", book "Book a partner call", dm "DM me [keyword]", link "Link in bio", follow "Follow for more"); the compliance line on the three pieces that carry it comes from the attraction compliance file with the income rule (no production or income figure anywhere in the kit); the Teams section became "Your organization" (per-partner name strips for co-hosts); export lands in `02 · Brand/Video Brand Kit/`; the hand-off says "set up riverside" or "register my video brand kit" in Cowork. No Riverside file was edited.
- Repointed hand-offs, by name: the Brain's free-vs-paid briefs now read `FOR aa-offer-kit-design (the offer stack)`, `(the product mockup)`, and `(the "Join My Team" one-pager)` (`attraction-free-vs-paid`); the Conversion presentation briefs `FOR aa-offer-kit-design (the opportunity one-pager / the opportunity deck)` (`cv-presentation`, its contract); the Admin's `WIN WALL BRIEF — for aa-content-design` (`admin-newsletter`, its task prompt, `admin-core.md`, its contract); the Short-Form carousel doc's band `THE DESIGN BRIEF FOR AA-CONTENT-DESIGN` (`sf-carousel`, `carousel-guide.md`, `output-standard.md`, `house-rules.md`, `mike-frameworks.md`, `publishing-guide.md`, its contract); `yt-interview`, `yt-repurpose`; the Events promo brief's carousel line (`ev-promo`); the Lead Magnet design brief (`lm-design`). The deliverable titles the plugins key on are unchanged. Older briefs whose header names a retired skill read the same way (the fields are identical).
- Support: `stack-map.md` (the Design Studio row reads 10 — gate check 14 — the router row lists the ten skills, the Design Studio section names each week's skills), `cohort-kb.md` (Week 1 the three; Week 2 the offer kit, lead magnet, funnel, content; Week 3 the video kit with Riverside; Week 6 events and the Value Vault incl. the onboarding roadmap), `faq.md` Q3 and Q47, `mikes-language.md`, `resource-library.md`, `maa-support-onboard`, `maa-support-teach`.
- Docs: `setup-guide.md` (the Week 2 row "my offer kit", a Week 3 video kit row, the Week 6 Value Vault row with the onboarding roadmap), the master plan (§0 row and count, §3 rebuilt for the 10, §5's brand-wiring note, §10, §11), the status report §2f, `SEAM-LOG.md` (the dated ruling: the merges, the kit checkpoint rule, the onboarding roadmap, the video kit contract reused from the editor), `START-HERE.md` (the Week 1 map unchanged; the rest of the Studio rebuilt for the 10 with the video kit in Week 3), the Design Studio `README.md`, the Design System's asset registry (the Video Brand Kit row), the root `README.md`; the dist copies are regenerated by the build.
- Versions: attraction-ai-brain 0.2.4, attraction-conversion-sales 0.1.3, attraction-ai-admin 0.2.2, attraction-youtube-system 0.1.4, attraction-shortform-system 0.1.4, attraction-events-workshops 0.1.2, attraction-lead-magnet 0.2.1, maa-claude-support 0.1.4; realtor-riverside-editor unchanged (read only, by rule).

## [0.5.0] — 2026-10-10

### The Lead Magnet is offer-first (user decision, 2026-10-10, after a live Cowork demo)
- The locked default first magnet is gone. Every member's lead magnet is built from their own unique value proposition, so no two look alike. "Launch my lead magnet plugin" is now a complete Week 2 session in one sitting, with no "come back later" gate: `lm-navigator` reads the offer's Status and, when it is still at seeds, runs the Brain's `attraction-offer` right there (the member never hears a skill name); when the offer is finalized it continues straight into the magnet ("Your offer's built. Now the lead magnet."); then `lm-magnet-ideas` puts exactly three Mike-grounded recommendations in front of the member — generated from the UVP along three lanes (the member's own system as a guide, checklist, or template · the result their agent wants, as a plan · the question agents ask most, answered honestly), each with who it's for, the pain, what in the offer it's built from, and the lesson cited (only where it resolves in the Support KB index) — recommending number one so "yes" works; the member picks; a shape-generic intake of at most five pre-answered questions (`intake-questions.md`); `lm-magnet` writes any shape (`magnet-guide.md` is now a shape catalogue — the member's system guide, a checklist, a plan or template, a questions guide, the fair comparison guide with its fairness, citation, and dating rules kept as one shape, a mini-course outline); `lm-funnel` writes the sales funnel outline (the member-facing name; the saved title `Opt-In Funnel — [Guide Name]` is unchanged because `aa-funnel-design` keys on it). The navigator closes the session with one line naming delivery, bios, and the Google profile.
- Compliance never stops the session early: the navigator reads the gate at Step 1, says once that the basics get set right before the guide is written, builds the offer and the pick anyway (private), and runs `attraction-compliance` immediately before the public document; the magnet writer's hard gate stays.
- House rules: #11 rewritten (the magnet is chosen from the member's UVP — three recommendations, the member picks; no default magnet; no two members' magnets alike; the comparison guide is one shape among many and only when it fits); #1's "never a numbered pick-list" gains its single exception (the three recommendations, still a normal chat message, never an option widget); #2 and #5 now describe the in-session offer build and the folded-in compliance step; every other comparison-guide assumption in `house-rules.md`, `brain-contract.md`, `output-standard.md` (the examples now use the demo member's magnet), `copywriting-kb.md`, `funnel-guide.md`, `lm-delivery`, `lm-gbp`, `lm-profiles`, `lm-design`, and `lm-partnerships` generalized. Triggers: "build my lead magnet for agents", "lead magnet ideas", "which lead magnet should I make", "write the guide agents download", "write my 90-day plan for agents", "my sales funnel outline" added; the comparison-guide phrases removed.

### Cross-plugin sync (the UVP and the magnet feed everything)
- `brain.md`'s quick reference carries two new lines once they exist: `UVP (one line):` (written by `attraction-offer` with `Offer status:` at finalize) and `Live magnet:` (written by `lm-magnet` when the magnet is logged, the URL added by `lm-funnel` when the page goes live — a mirror of `memory/magnets.md → ## Current magnet`, which stays the source of truth). The Brain template `brain.md`, `attraction-brain-setup`'s finalize step, the Brain's `brain-contract.md`, `docs/BRAIN-CONTRACT.md`, the Lead Magnet contract, and the Taylor Brooks demo brain carry them.
- `attraction-offer`'s Close hands straight back when the Lead Magnet plugin started the session (no list of next steps). The template `memory/magnets.md` placeholders read `[Magnet Name]` and its intake block is shape-generic; `yt-leads` and the YouTube contract key on the new placeholder.
- `sf-setup` now reads the offer's `Comment keyword:` as the invitation word it proposes (no Short-Form skill read that field before, although the offer skill said it did); the Short-Form contract names the field. Every other reader of `## Current magnet` (Short-Form, YouTube, Conversion, Events), of `list-growth.md`'s "Calls booked from the funnel" (the Brain's goals, the Admin's and the Conversion scorecards), and of the UVP line (Conversion, Events, the bios) was verified against the exact field names it reads.

### Repo-wide cleanup, Support, Design Studio, docs
- Support: the stack-map's Plugin 3 section and phrase table describe the offer-first session ("build my lead magnet for agents", "lead magnet ideas"); `mikes-language.md`'s cardinal-rules line no longer names a default guide.
- Design Studio: `aa-lead-magnet-design` designs whatever shape the member's offer produced (trigger "design my lead magnet pdf"; `guide-craft.md` gains a shapes section with the comparison guide's layout kept as one shape); `aa-funnel-design` and `copy-formulas.md`, `aa-offer-assets-design`, both `mockup-craft.md` files, and `START-HERE.md` lose the default-guide wording. The dist copies are regenerated by the build.
- Docs: `setup-guide.md` (Week 2 rows — the plugin builds the offer first if it isn't built yet; the Design Studio phrase), the master plan (§3 row, §11, §14 item 10), `BRAIN-CONTRACT.md`, `SEAM-LOG.md` (the dated ruling and the three-recommendation exception), the status report §2e, the README's plugin row.
- Versions: attraction-lead-magnet 0.2.0, attraction-ai-brain 0.2.3, attraction-shortform-system 0.1.3, attraction-youtube-system 0.1.3, maa-claude-support 0.1.3; attraction-conversion-sales, attraction-ai-admin, attraction-events-workshops, and realtor-riverside-editor unchanged (their readers verified, no edits).

## [0.4.0] — 2026-10-10

### The Lead Magnet moves to Week 2 (user decision, 2026-10-10)
- The Lead Magnet plugin runs in Week 2, right after the Partner Offer session, instead of Week 6. The install order is renumbered everywhere (the marketplace entries and their order, the plugin display names, the README, the Setup Guide, the Support stack-map and cohort KB, the master plan, the OS contract): 1 Brain · 2 Support · 3 Lead Magnet (W2) · 4 Short-Form (W3) · 5 Riverside (W3) · 6 YouTube (W4) · 7 Conversion & Sales (W5) · 8 AI Admin (W5) · 9 Events (W6). The Design Studio is unchanged. The Lead Magnet's registry block heading is now `## Lead Magnet (Week 2)` — every reader locates the block as "the Lead Magnet block" (`List tool`, `Live data`); none matched the old heading string.
- Week framing inside the plugin: "Week 6, depends on Week 2's offer" reads "Week 2, runs after the Partner Offer session in the same week" (`brain-contract.md`, `house-rules.md`, `lm-navigator`); the Partner Offer gate is unchanged (three states, "build my offer" first). Traffic sources: the Short-Form (Week 3) and YouTube (Week 4) engines arrive later and plug into the funnel then; until then the link lives in the bios, the Google Business Profile, partnerships, DMs, and the booking page (`lm-funnel`, `lm-delivery`, `lm-magnet`). `lm-analytics` treats `content-performance.md` (Week 3) and `sales-funnel.md` (Week 5) as "not yet, manual numbers first", naming the week.

### Ownership flip: the bios file
- `lm-profiles` (Week 2) now WRITES `identity/profiles.md` first — the five Short-Form headings in `sf-setup`'s order (Instagram · Facebook · TikTok · LinkedIn · YouTube), the bio text inside each aligned to the funnel's CTA, its own extra platforms appended after the five. `sf-setup` (Week 3) is the updater of its five sections: it refreshes the bio text inside them, preserves every extra section and italic update line, never deletes or reorders a heading, and creates the file only if the member skipped the Week 2 session. `yt-setup` still fills the YouTube section in Week 4. Applied in both plugins' contracts and skills, the Brain template (`profiles.md`, `brain.md`), the Brain's `brain-contract.md`, `docs/BRAIN-CONTRACT.md`, the Support stack-map, the master plan §1 and §11, `lm-gbp`, `yt-setup`, and the YouTube contract.

### The Starter Resource becomes the fallback
- The YouTube System's one-page "Questions to Ask Before You Choose a Sponsor" is built by `yt-leads` only when the member skipped the Week 2 lead magnet and `## Current magnet` is still empty; the normal path is the Week 2 guide. "Only when a Week 6 lead magnet exists" now reads "when the lead magnet exists (built in Week 2)" across `yt-leads`, `yt-make-video`, `yt-script`, `yt-seo`, `yt-setup` and its references, `doc-format.md`, `seo-knowledge-base.md`, and the YouTube contract. The Starter Resource mechanics are unchanged.
- Short-Form: `sf-comment-to-dm` reads the live magnet as "built in Week 2 — it normally exists by Week 3"; the GUIDE keyword path is the primary route from Week 3 and the booking-link route the fallback when no magnet exists; the direct call-rung cadence (at most once a month) is unchanged. Conversion and AI Admin: "Calls booked from the funnel" and the live magnet exist from Week 2 (`cv-conversation-starter`, `sales-booking-page`, `sales-scorecard`, `admin-recruiting-scorecard`, both contracts).

### Brain, Support, docs
- Brain: the week rule in the template `brain.md`, `project-instructions.md`, and setup; the template `config.md`, `magnets.md`, `list-growth.md`, `content-pillars.md`, `channel.md`; `drive-map.md`; `attraction-brain-health`'s week map (magnets · list-growth · profiles now Week 2); the `attraction-offer` and `attraction-goals` week lines.
- Support: `stack-map.md` renumbered with its own "Plugin 3 — Lead Magnet (W2)" section and a separate "Plugin 9 — Events (W6)" section (skill counts unchanged); `cohort-kb.md` Week 2 gains the Lead Magnet plug-in after the offer session and Week 6 keeps Events and the Value Vault; `faq.md` Q13, `maa-support-onboard`, `maa-support-cohort`.
- Docs: the Setup Guide (the Week 2 row installs Plugin 3 with "launch my lead magnet plugin" after "build my partner offer"; the checklist; the never-skipped rule now covers the magnet), Playbook 1, `docs/BRAIN-CONTRACT.md`, the master plan (§0, §1, §11, §13 ship dates — the Lead Magnet must be ready for Tue Nov 10, record-ahead by Fri Nov 6; §14), the Taylor Brooks demo brain, the status report §2d, the SEAM-LOG; the Design Studio map, design system, and brand-kit skill where they tied the guide to Week 6 (the dist copies are regenerated by the build).
- Scope note (user, same day): the Honest Brokerage Comparison Guide is no longer the locked first magnet; a follow-up pass redesigns the Lead Magnet flow offer-first. This release added no new "first magnet" mention and reworded the ones it touched to "the first lead magnet (chosen from the member's unique value proposition)".
- Versions: attraction-ai-brain 0.2.2, maa-claude-support 0.1.2, attraction-lead-magnet 0.1.3, attraction-shortform-system 0.1.2, attraction-youtube-system 0.1.2, attraction-conversion-sales 0.1.2, attraction-ai-admin 0.2.1; realtor-riverside-editor stays 0.4.4 (only its marketplace label changed) and attraction-events-workshops stays 0.1.1 (untouched).

## [0.3.3] — 2026-10-09

### Marketplace entry cap
- Cowork caps a plugin's marketplace entry description at 500 characters and warns on sync. The Riverside entry had grown to 526 with the v0.3.1 wording; trimmed to 440 (the trim note lives in the changelog, not the card). Gate check 1 now fails any entry over 500. The Brain's "executable files or settings may differ" notice after v0.3.1 is informational: the hook file changed when the stray key was removed; nothing to fix.

## [0.3.2] — 2026-10-09

### Hyphen-split descriptions (caught by the realtor-side session's detector)
- A folded `description: >` turns a line break into a space, so a wrap that broke on a hyphen changed the text the model reads. Six descriptions carried one: "studio- navigator" (`studio-publish`), "magnet- ideas" (`lm-navigator`, now the real skill name `lm-magnet-ideas`), "magnet- to-call" (`lm-analytics`), "voice- print" (`lm-nurture`), "starting- soon" (`aa-event-design`), "ds- skill" (`aa-style-sheet-design`, now "design skill"). All six re-wrapped without hyphen breaks; the design-system template's two leftover `ds-` mentions from the rename now read design skill. Gate check 8 fails any description with a hyphenated word split by the fold.
- Versions: realtor-riverside-editor 0.4.4, attraction-lead-magnet 0.1.2.

## [0.3.1] — 2026-10-09

### Cowork sync warnings cleared (this marketplace only; the realtor repo is untouched)
- attraction-ai-brain 0.2.1: `hooks.json` carries only the `hooks` key; the explanatory note that used to sit in a `$comment` field lives in `hooks/README.md`. claude.ai's hook schema dropped the unknown field with a warning on every sync; the SessionStart hook itself was always stored and is unchanged.
- realtor-riverside-editor 0.4.3 (the vendored realtor 0.4.2 plus two trims): the `studio-navigator` and `studio-publish` descriptions were 1455 and 1312 characters. claude.ai stores a description cut at 1024, which in Cowork silently dropped the navigator's resume triggers ("finish my video", "pick up where we left off", "continue my edit"). Both rewritten under 1024 characters as folded block scalars with the resume triggers kept; everything else in the plugin is byte-identical to the realtor source apart from the Brain-home rule.
- Gate: check 8 now fails on any description over 1024 (the vendored exemption is gone); new check 15 fails a `hooks.json` with any top-level key other than `hooks`. `vendor-riverside.sh` lists over-limit descriptions after a re-vendor so the trims get re-applied.

## [0.3.0] — 2026-10-09

### Shared document renderer v2 (Brain, Admin, Conversion, Events, Lead Magnet, Short-Form, YouTube)
- `render_doc.py` (byte-identical in all seven plugins; Riverside untouched): real Word styles in the house look (`Title`, `Heading 1`, `Heading 2` — the Word navigation pane and the Google Docs outline now work), a larger type scale (body 11pt at 1.2 line spacing, chapter titles 20pt, part titles 24pt, sub-bands 12.5pt, tables 10pt, cover 30pt), a running header + `Page X of Y` footer from page 2 (cover / title page carries neither), an "In this part" linked chapter list on every part opener, tables with a tinted bold header row that repeats across pages + alternating rows + horizontal hairlines only, callouts as indented accent-bar blocks, keep-with-next on headings / kickers / a label directly above a table and widow control on body text, one optional accent colour (default near-black) used only for the title rule, part kickers, callout bar and table-header tint, and a sub-band cap of 80 characters that warns instead of silently rendering dashes. The structured-text grammar is unchanged — every existing input re-renders without edits.
- `brain-book-spec.md` step 6 passes the member's primary brand colour from `brand-visual.md` as the accent (omitted when none is recorded); the zero-warning rule now includes the sub-band warning. `doc-formatting.md` (Brain, Admin, Conversion, Events) and the YouTube `doc-format.md` describe the v2 look.
- `docs/demo/`: the three demo documents re-rendered as v2 files; `measure_book.py` counts paragraph callouts and estimates pages on the v2 type scale; `BOOK-RENDER-TEST.md` §8 records the before/after.
- Versions: attraction-ai-brain 0.2.0, attraction-ai-admin 0.2.0, maa-claude-support 0.1.1, attraction-conversion-sales 0.1.1, attraction-events-workshops 0.1.1, attraction-lead-magnet 0.1.1, attraction-shortform-system 0.1.1, attraction-youtube-system 0.1.1.

### Book spec + calculator (2026-10-09)
- `brain-book-spec.md`: the per-chapter minimums bind in demo mode exactly as in a real build, no bracket placeholders in a demo, the money chapter always carries the three scenarios. `attraction-rev-share-calculator`: when the member defers ("explain mine to me") it runs the three scenarios on the strictest generic default mechanics instead of stopping — the gap that left the demo Book's Chapter 11 thin.

### Knowledge base moved to a private repo (2026-10-09)
- The 103 lesson transcripts now live in teamsherrard/claude-agent-attraction-knowledge (private) and this repo is public so Cowork can add it as a marketplace without a GitHub connection; `README.md`, the master game plan, the build brief and the Support `source-map.md` point there.


### Scheduled agents: eleven → nine (user decision, 2026-10-08)
- The Agent Movement Watcher is removed as a scheduled agent. Its research-only run is now the Prospect Radar's on-demand news scan (`attraction-prospect-radar` Job 3: "scan agent movement", "what's moving in my market", "refresh my prospect intel"), writing the same seven-column rows to `memory/intel.md` with a `News scan:` run line. No task, no consent card, no `Agent Movement Watcher task` key; the watcher task-prompt reference file is deleted.
- The Weekly Recruiting CEO Review is removed as a scheduled agent. It stays as `admin-recruiting-scorecard`'s CEO mode, run on demand ("run my CEO review", "what happened in recruiting this week"); `admin-attraction-setup` no longer offers it. No task, no `Weekly CEO Review task` / `CEO Review slot` keys; the CEO-review task-prompt reference file is deleted. The Admin owns four scheduled agents.
- Every contract, template, plan, Support, Short-Form, YouTube, Conversion, and demo-brain mention updated; the intel ledger's source is now "the Prospect Radar's news scan (on demand)".

## [0.2.0] — 2026-10-09

### attraction-events-workshops 0.1.0 — first build (new)
- Plugin 9: `ev-navigator`, `ev-strategy`, `ev-live`, `ev-virtual`, `ev-evergreen`, `ev-promo`, `ev-registration`, `ev-runofshow`, `ev-followup`, `ev-analytics`; the events doctrine from lessons 73–77 and Mike's workshop-ops lifecycle; `ghl-workflow-table.md` (Trigger → Action → Outcome); the Post-Event Follow-Up scheduled agent, consent-armed per event.

### Design Studio — all 14 Claude Design skills (`aa-…-design`)
- Week 2: `aa-offer-stack-design`, `aa-offer-assets-design`, `aa-product-mockup-design`, `aa-carousel-design`, `aa-funnel-design`, `aa-lead-magnet-design`. Week 4: no design skill — a thumbnail is a `yt-thumbnail` brief pasted into the member's Brand HQ project. Week 6: `aa-recognition-design`, `aa-event-design`, `aa-playbook-design`, `aa-course-design`, `aa-ebook-design`. Upload files in `design-studio/_dist/` (regenerated by the build; not tracked).

### Docs
- `docs/setup-guide.md` (the Week 1 Setup Guide copy), `docs/playbooks/playbook-1-agent-attraction-brain.md` (Playbook 1 copy), `docs/plans/BOOK-RENDER-TEST.md` + `docs/demo/` (the Brain Book render test and demo brain).

### Brain, Admin, Conversion seams
- Events rows in the OS contract; `admin-pipeline` scans event blocks for request lines; Conversion reads the next event from `memory/events.md`; the Brain template gains the events block, the Events content-log convention, and `03 · Content/Events/` in the drive map.

## [0.1.0] — 2026-10-08

### attraction-ai-brain 0.1.0 — first build
- New marketplace teamsherrard-agent-attraction and Plugin 1, the Agent Attraction Brain (26 skills), built per `docs/plans/01-ai-brain-plugin-gameplan.md`.
- Mechanics forked once from the realtor Brain with new names: `attraction-brain-setup`, `attraction-brain-sync`, `attraction-brain-health`, `attraction-brain-migrate`, `attraction-import`, `attraction-capture`.
- Identity: `attraction-brand-persona`, `attraction-voice-print`, `attraction-voice-proof`, `attraction-story-bank`, `attraction-brand-direction`, `attraction-why-join-me`.
- Targeting and offer: `attraction-persona-map`, `attraction-prospect-radar`, `attraction-top-50`, `attraction-brokerage-model`, `attraction-model-positioning`, `attraction-offer`, `attraction-free-vs-paid`.
- Goals, ops, guardrails: `attraction-goals`, `attraction-execution-framework`, `attraction-rev-share-calculator`, `attraction-leadership-audit`, `attraction-operations`, `attraction-compliance`, `attraction-debrief`.
- Shared: `attraction-doctrine.md`, `persona-doctrine.md`, `brokerage-models.md`, `compliance-doctrine.md`, `brain-contract.md`, rewritten `drive-map.md`, `brain-book-spec.md`, `brain-doc.md`, `project-instructions.md`; `render_doc.py` and the connector layer carried 1:1.

### maa-claude-support 0.1.0 — first build
- Forked from the realtor cohort support plugin with every skill renamed `maa-support-*`; the MAA 6-week calendar, the Agent Attraction OS stack map, the two-desks rule for dual-cohort members, new diagnosis trees, the honest stack cost, an explicitly unset escalation door.
- The lesson knowledge base: 103 cards in `shared/kb/` (one file per vault module, verbatim quotes verified against the transcripts, the Loom link on every card) plus `kb-index.md`; "what did Mike say about…" answers from it and names the lesson to rewatch.

### attraction-shortform-system 0.1.0 — first build
- Forked from the realtor short-form system (`sf-*`): the five pillars Authority · Perspective · Story · Proof · Personality, value-first setup writing `content-pillars.md`, `publishing.md`, `profiles.md`; talking-head scripts with the 30-day calendar, carousels, green-screen, the daily story rotation (`sf-stories`), ideas and the 30-hook bank, the weekly routine, the comment-to-DM ladder with the ManyChat keyword (`sf-comment-to-dm`), optimizer, publish and batch publish through the member's own tool, analytics owning the Weekly Content Performance agent.
- Shared: the short-form attraction doctrine (`mike-frameworks.md`), the Composio data engine and the Notion board spec rewritten for agent attraction (byte-identical with the YouTube plugin).

### attraction-youtube-system 0.1.0 — first build
- Forked from the realtor YouTube system (`yt-*`): the attraction YouTube doctrine from the nine YouTube lessons, channel setup, the 3-lane game plan on the 8-video cycle, ideation, research, outliers, scripts in four formats, the agent interview strategy (`yt-interview`), model breakdowns with a hard data gate (`yt-model-breakdown`), thumbnail briefs for Claude Design (`yt-thumbnail`), SEO, make-video, repurpose with conversation starters, leads, analytics extending the Friday performance agent, coach, consistency, briefing (consent-first, draft-only), board, triggers. Writes content-log rows at script, publish, and repurpose.

### attraction-conversion-sales 0.1.0 — first build (new)
- Built from the Week 5 lessons: the conversion doctrine with the framework lock and the DECISION NEEDED blocks for Mike; `cv-navigator`, Agent Intel, Conversation Starter, DM flow, call prep (owns Call Block Prep), question funnel, enrollment script, presentation, 3-way calls, the Objection Handling Coach (15 objections, 5 modes), the Conversation Coach, follow-up, reactivation (owns Cold-Lead Reactivation), and the six Sales OPS skills.

### attraction-ai-admin 0.1.0 — first build
- Forked from the realtor AI Admin and cut to the organization side: `admin-attraction-setup`, `admin-daily` (the Morning Brief extending the Debrief), `admin-pipeline` (sole writer of stage moves), `admin-follow-up-queue`, `admin-recruiting-scorecard` (the Weekly Recruiting CEO Review), `admin-newsletter`, `admin-va-tasks`, `admin-monthly-review`.

### attraction-lead-magnet 0.1.0 — first build
- Forked from the realtor lead capture plugin for an agent audience (`lm-*`): the Honest Brokerage Comparison Guide locked as the first magnet, magnet ideas, design brief, funnel with the static-form rule, delivery, nurture, partnerships, GBP, profiles (Week 6 updater), analytics.

### realtor-riverside-editor 0.4.2 — vendored
- The same AI Editing Studio as the realtor marketplace, vendored by `scripts/vendor-riverside.sh`, with one added rule in `shared/house-rules.md`: the Studio uses `~/attraction-brain/` when it exists, else `~/realtor-brain/`, and calls that Brain's sync skill.

### Design Studio (Claude Design skill set, not a plugin)
- Week 1 Design Package: `aa-logo-design`, `aa-style-sheet-design`, `aa-brand-kit-design`, the Agent Attraction Design System, START-HERE, and the build in `design-studio/_dist/`.

### Repo
- `docs/BRAIN-CONTRACT.md` (OS-wide ownership, locked vocabularies, request shapes, config registry, 11 scheduled agents), `docs/plans/` (the two game plans, the build brief, the seam log, the status report), `knowledge/transcripts/` (103 lessons + manifest, private), `scripts/check-release.sh` with checks 8–13.

