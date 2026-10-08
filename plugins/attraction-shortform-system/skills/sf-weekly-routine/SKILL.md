---
name: sf-weekly-routine
description: >
  The Weekly Routine Planner for the member's short-form attraction engine: three to five Reels a week on
  the 2 attraction · 2 authority · 1 story mix, stories every day, a batch day to plan and record, idea
  capture, one video reposted to every short-form platform, and the daily engagement routine that turns
  comments into conversations. Plans the week from the Brain and checks it in at the end; writes nothing
  to the member's identity and logs nothing itself. Trigger on: "plan my attraction week", "my short-form
  routine for agents", "weekly routine planner", "my attraction posting routine", "set my batch day",
  "how did my attraction week go", "what's my engagement routine", "my content week for my organization",
  or any request to plan or review the weekly short-form rhythm for attracting agents. (Ideas =
  sf-ideas; the 30-day calendar = sf-talkinghead; scheduling = sf-publish.)
---

# The Weekly Routine Planner

Consistency is the whole game. Mike has not missed a week since he joined his brokerage, and that
consistency, not cleverness, is why the engine works (`07-instagram/90`). Most leaders do not fail on
quality; they fail by quitting. This skill makes the week simple and repeatable: what to film, when to
film it, what to post each day, and the fifteen minutes that turn attention into conversations.

**Apply** `${CLAUDE_PLUGIN_ROOT}/shared/house-rules.md` and the advisor stance in
`${CLAUDE_PLUGIN_ROOT}/shared/advisor-playbook.md` (recommend first; one easy question at most).

## Two modes (detect from the message)
- **PLAN** (default) — "plan my attraction week", "set my batch day": build the week.
- **CHECK-IN** — "how did my week go", "did I hit my routine": score the week that just ended and set the
  next one. Runs happily on a Friday or Sunday.

## Step 1 — Load the Brain (the plan comes from here, not from questions)
Read `~/attraction-brain/brain.md` first (pull with **attraction-brain-sync** if the local copy is empty).
Open only:
- `identity/content-pillars.md` — the pillars and the member's realistic weekly number (`sf-setup` writes
  it; if missing, use the defaults below and say which week fills it)
- `identity/goals.md` — the content commitment they set in Week 1 (never ask for a number that is here)
- `identity/operations.md` — working hours, the booking link, when they are usually free to film
- `identity/publishing.md` — the posting tool and connected platforms
- `memory/content-log.md` — what shipped last week, by pillar (the check-in reads this; the plan avoids
  repeats)
- `memory/ideas.md` (tag `shortform`) — their own captured ideas get first claim on this week's slots
- `memory/conversations.md` — any conversation that started from a post last week (the check-in counts it)
- `memory/intel.md` — a dated item worth a Perspective Reel this week
If none of the three to five Reels for the week are scripted yet, say so and point at `sf-ideas` →
`sf-talkinghead`. Never plan a week of unwritten videos as if they existed.

## The rhythm (Mike's, carried whole)
- **Reels: three to five a week** — start at three, work up to five (`07-instagram/88`). The mix every
  week: **2 attraction · 2 authority · 1 story** — attraction = a Perspective, Proof, or Personality Reel;
  authority = an Authority Reel; story = a Story Reel. Static posts can be spliced in for recognition and
  personal moments; they do not replace the Reels.
- **Stories: every day, one to five**, a mix of personal and value; never a day without one
  (`07-instagram/89`). Reels build width and awareness; stories build depth and connection.
- **One video covers every short-form platform** — film for Instagram Reels, repost to TikTok, YouTube
  Shorts, and Facebook Reels (`07-instagram/90`). Editing stays simple: captions are the only mandatory
  edit; raw and genuine outperforms sensory overload.
- **The batch day** — Mike's simple option: **Monday** brainstorm the three to five topics · **Tuesday**
  record them (one to two hours, all in one sitting) · **Wednesday** edit or hand to the editor · post from
  Thursday or schedule the week (`07-instagram/90`). Mike's own version is bi-weekly Saturdays (plan one
  Saturday, record the next, long-form and short-form alternating). Offer the simple option first; fit it
  to `operations.md`.
- **Idea capture** — ideas come from conversations, coaching calls, and the questions agents ask; capture
  them the moment they land (the Brain's capture skill, tag `shortform`) and let AI fill the other half.
  Mike: about half his ideas are AI-assisted, half are his own from experience, and the member should know
  their audience better than any prompt (`07-instagram/90`).
- **The engagement routine (15 minutes a day, same time every day)** — reply to every comment with a
  question within the day · answer every DM the same day · tag the agents you feature so they reshare it
  (their story reaches a whole new audience, `07-instagram/89`) · reshare agents' screenshots of your calls
  and wins (`06-content-framework/38`) · one interactive story element a day (poll, question box, "ask me
  anything") · leave real comments on five agents' posts in your lane, never a negative one, ever
  (`05-big-picture/36`). Every conversation that starts here is handed to `sf-comment-to-dm`.
- **Leaders create leaders** — encourage the agents in the organization to post and tag the member; their
  combined reach is the multiplier (`07-instagram/90`).

## Step 2 — PLAN: the week (use these exact section names)
- **THE WEEK AT A GLANCE** — one table, Monday to Sunday: day · what posts (the Reel's working title and
  pillar, or "stories only") · the story prompt for that day · the engagement slot · minutes. Mike's sample
  calendar (`07-instagram/90`) is the default shape: Mon value (Authority) · Tue recognition (Proof) · Wed
  leadership insight (Perspective) · Thu culture or event recap (Proof or Personality) · Fri personal or
  opinion (Story or Perspective). Rebalance to the 2·2·1 mix and to their realistic number.
- **THE BATCH BLOCK** — the day, the start time, the length (one to two hours), the three to five titles
  in film order, the one setup (phone at eye level, natural light, one outfit). Point at `sf-batch-publish`
  for a full film-day run sheet when they have more than five.
- **THE DAILY STORY HABIT** — seven prompts, one per day, from `sf-stories`' four categories (behind the
  scenes of leading · agent wins · personal · opportunity); each under ten words; one interactive element.
- **THE ENGAGEMENT ROUTINE** — the fifteen-minute checklist above, with the time of day they will do it.
- **THE CHECK-IN TABLE** — empty, for Friday: Reels filmed · Reels posted · story days · comments replied
  · DMs answered · conversations started · calls booked.
- **ONE CALENDAR BLOCK** — offer once to put the batch block and the daily engagement slot on their
  calendar (Google Calendar or Outlook, per the Brain's connector). Only with a yes; never silently.

## Step 3 — CHECK-IN: score the week and set the next one
Read `memory/content-log.md` (rows this week, by pillar), `memory/conversations.md` (rows with Channel =
DM or comment this week), and, if `sf-analytics` has written one, the latest block in
`memory/content-performance.md`. Report, plainly:
- the check-in table filled in from the log (never from memory or guesswork; a number you cannot see is
  "not logged yet")
- the mix they actually posted vs 2·2·1, and the pillar that went missing
- the one thing that started a conversation this week (name the post)
- **THE ONE CHANGE** for next week (exactly one), then the next week's plan (Step 2)
Encourage. A thin week is data, not failure.

## What this skill never does
- Writes nothing to `identity/` and nothing to `memory/content-log.md`. Rows are written by the skills
  that make and ship the content (`sf-talkinghead`, `sf-stories`, `sf-carousel`, `sf-publish`). Calendar
  events are the only thing it creates, with a yes.
- Never posts, schedules, or sends. Never asks for the niche, the avatar, the hours, or the weekly number
  when the Brain has them.

## Step 4 — Save
Deliver in chat. Offer to save per `${CLAUDE_PLUGIN_ROOT}/shared/output-standard.md`: render to `.docx`
(`shared/render_doc.py`) → `03 · Content/Short-Form/`, named `[YYYY-MM-DD] · Weekly Routine`. If a save
fails, say so, keep it visible, retry once, stop. Close: *"block the batch day before you close this; a
filming day that isn't on the calendar doesn't happen."*

## Quality checklist
- [ ] Brain loaded; weekly number, hours, and pillars taken from it, not asked
- [ ] Three to five Reels on the 2·2·1 mix; stories every day; one batch block; one video to all platforms
- [ ] The fifteen-minute engagement routine with a time of day; agents tagged and reshared
- [ ] Check-in scored from the log, not from memory; exactly one change for next week
- [ ] Nothing written to identity or the content log; calendar block only with a yes
