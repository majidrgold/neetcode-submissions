# Interview Prep Plan — Majid Ramezani

*Target roles: Senior/Staff ML & Applied AI Engineer (fraud/integrity, GenAI/agents, forward-deployed, AI platform), plus hedge-fund AI engineering. Warm-up companies first, then FAANG and hedge funds.*

---

## How to use this document

- This file is your **source of truth**. Keep it, and update the checkboxes and dates as you go.
- Keep a separate **tracker spreadsheet** (design below) for problems and stories.
- At each check-in, paste your last ~2 weeks of tracker rows into a chat and we review progress, adjust, and run mocks.
- To have prep context carry across separate chats, Projects (keeps chats + files together) and memory (recalls context between chats) help — both are paid features. Check claude.ai/pricing for what's current. Without them, this document + tracker is enough; just paste rows at each check-in.

---

## Level & target read

- Realistic level: **Senior, stretch to Staff** (~L5–L6 Google, E5–E6 Meta).
- **Coding is the bottleneck** — most trainable thing here, responds directly to reps. Protected time; don't let reading crowd it out.
- Design and behavioral are mostly repackaging work you've already done.

---

## Weekly time budget (~10–12 hrs/week)

| Area | Hours | Notes |
|---|---|---|
| Coding | ~6 | 5 days/week, timed, talk aloud |
| Design & concepts | ~3 | 1 system design + reading |
| Stories / resume / apps / networking | ~2 | |
| Weak-spots log | ~10 min after every session | Non-negotiable |

If a checkpoint slips, **extend the phase and delay FAANG applications** — don't rush your best shots.

---

## The coding fear — how this plan handles it

You reach for the right structure already (per-key state, timestamp comparison in the login problem). What's missing is **fluency**, not knowledge. Fluency responds to reps. Scaffolding built in:

1. **Confidence-first ordering** — start with patterns you can win at (arrays/hashing, two pointers) before graphs/DP.
2. **Easier on-ramp** — do a couple of Easy problems per new topic before Mediums.
3. **More review** — every missed/hinted problem gets redone at 2 days, 1 week, 3 weeks (spaced repetition).
4. **25-minute cap** — stuck at 25 min → read hint/solution, then re-solve from scratch next day. No grinding.
5. **Trace one example by hand before saying "done."** This alone catches most bugs (it would have caught the empty-`counter` bug in your first attempt).
6. **Rewrite from memory** the next day. Re-deriving beats re-reading.

---

## Platform & problem set

- **NeetCode 150** as the menu (pattern-grouped — right for rebuilding fluency).
- Don't aim to finish all 150 in 8 weeks. At ~6 hrs/week with review, ~**70 fresh problems** is realistic and plenty.
- **Do topics in site order.** Priority: Arrays & Hashing → Two Pointers → Sliding Window → Stack → Binary Search → Trees → Heap → Intervals → Graphs (BFS/DFS) → Backtracking → 1-D DP.
- **Skip most Easy** after 1–2 per topic. **Defer Hards.**
- **Defer low-yield topics:** Advanced Graphs, Bit Manipulation, Math & Geometry, 2-D DP — only if time remains.
- **Add design-style problems** (resemble your real work): LRU cache, rate limiter, hit counter, logger rate limiter. Check whether NeetCode covers them free (some are LeetCode Premium).
- Finished early? Timed **mixed sets** from the rest of the 150.

---

## Tracker spreadsheet design

**Tab 1 — Problems**

| Date | Problem | Link | Pattern | Time (min) | Result (solo / hint / unsolved) | Where I got stuck | Key insight | Next review |
|---|---|---|---|---|---|---|---|---|

- Cap each attempt at 25 min.
- Review anything missed/hinted at **2 days / 1 week / 3 weeks**.
- Track **patterns**, not just problem counts.

**Tab 2 — Weak-spots log:** one line per session — the pattern or concept that tripped you, so you know what to drill next.

**Tab 3 — Stories & design:** your 6 behavioral stories + a log of each system-design session (prompt, how it went, what to fix).

---

## 8-Week Plan

### Phase 1 — Foundation & warm-up (Weeks 1–2)
**Coding:** Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search. 6–8 problems/week. Rewrite each from memory 2 days later. Refresh Python: `collections` (`deque`, `Counter`, `defaultdict`), `heapq`, `bisect`.
**Design/concepts:** agentic patterns (supervisor vs. hierarchical, ReAct, reflection); LLM eval basics (golden sets, LLM-as-judge, shadow mode). Fills the Google FDE gaps.
**Assets:** finalize NF resume, update LinkedIn, write 6 stories with defensible metrics.
**Applications:** apply to 10–15 **warm-up** companies (roles you'd genuinely take).
**Checkpoint:** basic sliding-window or hash-map Medium in 25 min, unaided.

### Phase 2 — Build range (Weeks 3–4)
**Coding:** Intervals, Heaps/top-K, BFS/DFS & graphs, Trees, basic recursion. 8–10 problems/week + one 45-min mock (I play interviewer).
**Design:** one full ML system design/week — fraud/integrity detection first, then RAG platform over enterprise docs.
**Build:** one weekend — small project with Google ADK or LangGraph + an MCP tool + tracing + a cost/latency report. Add to resume **only after it exists.**
**Networking:** start asking for referrals at target companies.
**Checkpoint:** 2 of 3 Mediums in 30 min; clean design structure (clarify → assumptions → approach → tradeoffs → monitoring).

### Phase 3 — Target applications (Weeks 5–6)
**Coding:** Backtracking, basic 1-D DP, design-style problems (LRU cache, rate limiter, hit counter). Timed **mixed sets of 2 problems in 50 min** (real rounds are usually 2).
**Design:** agent + eval design (advertiser-support style) + a Meta-style ranking/classification design. Two full mocks/week.
**Applications:** apply to **Meta, Google, Amazon, hedge funds**, with referrals. Apply ~70% ready — scheduling gives a 2–4 week buffer. For hedge funds, **ask the recruiter what the loop includes** before extra prep (some add probability/stats).
**Checkpoint:** fresh Medium in 25–30 min, communicating while coding.

### Phase 4 — Loops (Weeks 7–8)
Full mock loops: 2 coding + 1 design + 1 behavioral, back to back. Every session ends with a weak-spots review. Feed warm-up interview feedback back in. **Don't learn new topics — sharpen what you have.**

---

## Reading list — with resources

Read **selectively and in this order.** Books are skim/selective; coding is protected. Don't read passively — after a first pass, close the book, design the system aloud or on paper, then compare.

### 1. ML System Design Interview — Ali Aminian & Alex Xu  *(highest value)*
Most direct prep for Meta and any fraud/integrity role. Do the **harmful-content detection** and **ad-click prediction** chapters first — they match your background. Internalize the framework: business objective → ML task framing → data → features → model → offline/online eval → serving → monitoring.
**Supplement with:**
- Chip Huyen, *Designing Machine Learning Systems* (book) — best companion for data/serving/monitoring depth.
- Eugene Yan's blog (eugeneyan.com) — applied ML case studies, recsys & eval.
- Meta/Google engineering blogs on integrity & ranking (search their eng blogs for "integrity", "spam", "ranking").

### 2. Generative AI System Design Interview — Ali Aminian & Hamid Nazeri  *(skim)*
You already build these. Pull out the framework + any pattern you haven't used. Won't cover agents/MCP/evals in depth — supplement:
- **Anthropic, "Building Effective Agents"** (anthropic.com/engineering/building-effective-agents) — the clearest agent-pattern reference.
- **Google Agent Development Kit (ADK) docs** (google.github.io/adk-docs) — for the FDE roles.
- **LangGraph docs** (langchain-ai.github.io/langgraph) — supervisor/hierarchical/ReAct patterns.
- **Model Context Protocol docs** (modelcontextprotocol.io) — you already do MCP; skim to speak to it crisply.
- Eval depth: search "LLM-as-a-judge" limitations, and read up on offline vs. shadow vs. A/B testing for LLM systems.

### 3. System Design Interview, Vol. 1 — Alex Xu  *(selective)*
Senior loops often include one general distributed-systems round; the Google Ads and hedge-fund platform roles lean on it. **Do these chapters:** rate limiter, key-value store, notification system, news feed, chat system. Skip the rest unless time remains.
**Supplement with:**
- **ByteByteGo** (Xu's own videos/newsletter) — visual reinforcement of the book.
- **"System Design Primer"** GitHub repo (github.com/donnemartin/system-design-primer) — free, broad reference.
- **Grokking the Modern System Design Interview** (DesignGurus) — optional, if you want more worked examples.

### Coding — beyond NeetCode (since coding is the priority)
- **NeetCode.io** — primary. Watch the pattern explainer, then solve unaided.
- **"Grokking the Coding Interview" (DesignGurus)** — organizes problems by pattern; good if you want more reps per pattern.
- **Sean Prashad's Leetcode Patterns** list — free, pattern-tagged problem set for extra volume.
- **Tech Interview Handbook** (techinterviewhandbook.org) — free cheatsheets on what to study and how.
- Optional book: *Elements of Programming Interviews in Python* — deeper, only if you want a reference text.

---

## Rules that keep this working

- **Timed always.** Untimed practice doesn't fix rustiness.
- **Talk out loud**, even alone.
- **Trace one example by hand** before "done."
- **Track patterns, not counts.**
- Checkpoint slips → **extend the phase, delay the application**, don't rush.

---

## Start today

1. NeetCode: **Contains Duplicate** / **Valid Anagram** (easy on-ramp), then **Two Sum**.
2. Do **LeetCode 1604** (Alert Using Same Key-Card 3+ Times in One Hour) — near-identical to the login-events problem.
3. Tomorrow: rewrite the **login-events solution from memory**, no looking.
4. Set up the tracker spreadsheet (3 tabs above).
5. Send answers to the **GenAI system design** and **behavioral** questions when ready → full evaluation → plan adjustment.

---

## Application list (fill in as you go)

**Warm-up (Weeks 1–2):**
- [ ] ...

**Targets (Weeks 5–6):**
- [ ] Meta — ML Engineer (integrity/fraud)
- [ ] Google — FDE III GenAI / SWE GenAI-ML
- [ ] Amazon — Applied Scientist / ML Engineer
- [ ] Hedge funds — AI/platform engineer (ask recruiter about loop)

---

## Progress checkpoints

- [ ] **End Wk 2:** basic sliding-window/hash-map Medium in 25 min unaided
- [ ] **End Wk 4:** 2 of 3 Mediums in 30 min; clean design structure
- [ ] **End Wk 6:** fresh Medium in 25–30 min while talking; targets applied to
- [ ] **End Wk 8:** full mock loop completed and reviewed
