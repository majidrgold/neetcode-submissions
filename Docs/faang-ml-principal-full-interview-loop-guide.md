# FAANG interview guide for Lead/Principal AI/ML Engineers — full loop, beyond coding

Coding is one round out of five to seven. This covers the rest of the loop, what to review for each, and a realistic time budget.

---

## 1. What the full loop actually looks like

Loops vary by company, but a Lead/Principal AI/ML Engineer loop typically has 5-7 rounds pulled from this set:

| Round | Typical count | What it's really testing |
|---|---|---|
| Coding / DSA | 1-2 | Baseline problem-solving, communication under pressure |
| ML coding (from-scratch implementation) | 1 | Do you actually understand the math, or just call libraries |
| ML system design | 1-2 | Can you architect a full ML product end-to-end |
| General software system design | 0-1 | Needed if the role touches serving infra, platforms, not just modeling |
| ML breadth/depth ("ML fundamentals") | 1 | Conceptual depth — bias/variance, regularization, evaluation metrics, when to use what |
| Behavioral / leadership | 1-2 | Track record of impact, judgment, and how you operate with and lead others |
| Bar raiser / hiring manager / team match | 1 | Culture fit, role fit, sometimes a mix of the above |

At Principal/Staff level, the **behavioral and system design weight goes up relative to coding** — companies assume you can code and are trying to find out whether you can set technical direction and whether people would want to work for/with you.

---

## 2. Round-by-round: what to review

### A. Coding (DSA)
Already covered in your NeetCode 150 cheatsheet — review that. At this level, the differentiator is communication and code quality, not raw difficulty (see your other guide's Section 2 communication framework).

### B. ML coding (from-scratch)
Already covered in your ML/FAANG coding guide — the from-scratch implementations list (logistic regression, k-means, softmax, attention, etc.) and NumPy vectorization fluency.

### C. ML system design
This is the round most senior candidates under-prepare for because it has no LeetCode-equivalent grind path. Review:

- **A repeatable framework**, e.g.:
  1. Clarify the problem & business objective (what does "success" mean — engagement, revenue, safety?)
  2. Define the ML objective as a concrete prediction task (classification, ranking, regression — be precise: "predict click probability" not "improve engagement")
  3. Data — sources, labeling strategy, class imbalance, freshness/staleness
  4. Feature engineering — what signals matter, how to avoid leakage
  5. Model choice — start simple (baseline), justify complexity increase, discuss alternatives and trade-offs
  6. Training infra — data/model parallelism if scale demands it, how you'd handle retraining cadence
  7. Offline evaluation — metrics (AUC, precision/recall, NDCG for ranking, etc.) and why those over others
  8. Online evaluation — A/B testing design, guardrail metrics, ramp-up strategy
  9. Serving — latency constraints, batch vs real-time inference, caching
  10. Monitoring — drift detection, feedback loops, retraining triggers
- **Classic prompts to rehearse**: design a feed ranking system, a fraud/anomaly detection system, a search relevance model, a recommendation system, a content moderation system, an ad click-through-rate predictor, a chatbot/LLM-based assistant pipeline (retrieval-augmented generation specifics if relevant to the role).
- **Practice narrating trade-offs**, not reciting a checklist — interviewers actively probe "why not X instead," and a memorized structure without justification reads as shallow.

### D. General software system design (if applicable)
Needed if the role is ML infra/platform-adjacent (model serving platforms, feature stores, training pipelines) rather than pure applied modeling. Review:
- Load balancing, caching, database choice (SQL vs NoSQL) and sharding/partitioning
- CAP theorem trade-offs, consistency models
- Queueing systems for async processing (relevant for training pipelines, batch inference)
- Designing for scale: back-of-envelope estimation (QPS, storage, bandwidth) — practice doing this fast and out loud
- Standard prompts: design a URL shortener, design a rate limiter, design a distributed cache, design a notification system — the generic system design canon, since some loops include one such round even for ML titles to test general engineering judgment

### E. ML breadth/depth ("ML fundamentals")
A conceptual round, sometimes folded into the ML coding or system design round rather than standalone. Review:
- **Bias-variance tradeoff**, overfitting/underfitting, and every regularization technique's actual mechanism (L1 vs L2 — why L1 induces sparsity, dropout, early stopping, data augmentation)
- **Evaluation metrics and when each is appropriate**: precision/recall/F1 vs accuracy (class imbalance), ROC-AUC vs PR-AUC (when positive class is rare), calibration, ranking metrics (NDCG, MRR)
- **Classic algorithm comparisons**: when to use tree ensembles vs neural nets vs linear models, and why — this is a "judgment" question, not a "can you name the algorithm" question
- **Deep learning fundamentals**: vanishing/exploding gradients and their fixes (batch norm, residual connections, gradient clipping), optimizer differences (SGD vs Adam vs RMSprop — what problem each solves), why transformers replaced RNNs for most sequence tasks
- **LLM-specific depth if relevant to the role**: pretraining vs fine-tuning vs RLHF/DPO, retrieval-augmented generation, hallucination mitigation, context window trade-offs, quantization/distillation for serving efficiency
- **Statistics fundamentals**: hypothesis testing, p-values and their common misinterpretation, confidence intervals, sampling bias
- Be ready to defend past project decisions with this vocabulary — interviewers often pull fundamentals questions directly from your resume ("you mention you used XGBoost here — why not a neural net?").

### F. Behavioral / leadership
This is the round most technical candidates most under-invest in, and it often has *equal or greater weight* than coding at Principal level. Review:
- **A structured story bank** (STAR: Situation, Task, Action, Result), 8-12 stories minimum, each mappable to multiple themes so you're not caught flat-footed by phrasing you didn't anticipate:
  - A time you drove technical direction across teams without formal authority
  - A significant failure or mistake, and what you changed afterward (never one you can't own honestly)
  - Resolving a technical disagreement with a peer or your own manager
  - Mentoring someone and how you measured its effect
  - Navigating ambiguous or conflicting priorities/stakeholders
  - Pushing back on a decision you disagreed with — and how it resolved either way
  - A time you had to sacrifice short-term speed for long-term quality (or vice versa), and how you justified it
  - Handling an production incident or major technical risk
- **Company-specific leadership principles**: if interviewing at Amazon specifically, know all 16 Leadership Principles and map 2+ stories to each of the heavily-weighted ones (Ownership, Dive Deep, Deliver Results, Have Backbone/Disagree and Commit). Other companies have their own equivalents (Google's Googleyness/leadership, Meta's "move fast," etc.) — check current company career pages for verbatim current values, since these get revised.
- **Practice concision** — a STAR answer should be 90 seconds to 2 minutes, not a 10-minute narrative. Senior candidates often ramble because they have more stories to tell; interviewers need the *point*, not the whole history.

### G. Bar raiser / hiring manager / team-fit round
Often a blend — expect a mix of behavioral and "why this role/company," plus sometimes a lighter technical discussion. Review your own "why this move" narrative explicitly — vague answers here ("I just want a new challenge") read poorly at senior levels where a deliberate career narrative is expected.

### H. LLM / GenAI depth (increasingly its own round, not a footnote)
This used to be a subtopic inside "ML fundamentals." At most companies in 2026 it's effectively its own bar — folded into ML system design, ML breadth, *or* a dedicated GenAI round, but tested deeply regardless of which bucket it lands in. Treat it as a first-class prep area, not an afterthought.

**Architecture & pretraining**
- Transformer internals well enough to derive, not just recite: self-attention, multi-head attention, positional encoding (absolute vs rotary/RoPE vs ALiBi), layer norm placement (pre-norm vs post-norm), why residual connections matter at depth.
- Pretraining objectives: causal LM (next-token prediction) vs masked LM, and why decoder-only architectures came to dominate general-purpose LLMs.
- Scaling laws — the general shape of the relationship between model size, data size, compute, and loss (Chinchilla-style "compute-optimal" reasoning), and why it matters for deciding model size vs data size trade-offs.
- Tokenization: BPE/sentencepiece basics, why tokenization choices affect multilingual performance, cost, and context-length math.
- Mixture-of-experts at a conceptual level (sparse activation, routing) if targeting a role at a lab actively shipping MoE models.

**Post-training / alignment — know the full pipeline, not just the buzzwords**
- Supervised fine-tuning (SFT): what it actually does (behavior cloning on curated demonstrations) vs pretraining.
- RLHF: reward model training from human preference pairs, then policy optimization (PPO) against that reward model — know the actual mechanics, not just "humans give feedback."
- DPO (Direct Preference Optimization) and why it emerged as a simpler alternative to RLHF (directly optimizes on preference pairs without training a separate reward model or running RL) — be ready to discuss the trade-offs versus RLHF, not just define it.
- RLAIF / Constitutional AI style approaches — using model-generated critiques/preferences instead of (or alongside) human ones, and the trade-offs (scale vs quality).
- Know when each stage is even necessary — a lot of interview signal comes from correctly recommending *skipping* RLHF/DPO for a use case where SFT alone suffices.

**Fine-tuning mechanics — the practical, "how would you actually do this" layer**
- Full fine-tuning vs parameter-efficient fine-tuning (PEFT): why full fine-tuning is often infeasible at scale (memory for optimizer states, gradients, activations — be ready to do rough back-of-envelope memory math).
- **LoRA** (Low-Rank Adaptation): the mechanism (freezing base weights, injecting small trainable low-rank matrices), why it works, and its main hyperparameters (rank, alpha, which layers to target).
- **QLoRA**: LoRA combined with quantizing the frozen base model — know roughly how this cuts memory further and where the trade-offs are (quantization error vs memory savings).
- Other PEFT variants worth recognizing by name even if not implementing: prefix tuning, adapters, IA³.
- Catastrophic forgetting — what it is, and mitigations (lower learning rates, replay of original data, PEFT itself as a partial mitigation since base weights stay frozen).
- Data curation for fine-tuning: quality over quantity, deduplication, the risk of fine-tuning on synthetic/model-generated data without verification (model collapse concerns).

**Prompt engineering — treat this as a real technical skill to discuss with precision, not a soft skill**
- Zero-shot vs few-shot prompting, and when few-shot examples actually help vs just burn context.
- Chain-of-thought prompting — why it improves performance on multi-step reasoning tasks, and its limits (doesn't fix a model's underlying capability gaps, can be unfaithful to the model's real reasoning).
- Structured output techniques (JSON mode, function calling/tool schemas) and their reliability trade-offs vs post-hoc parsing.
- System prompt design, and where prompting stops being sufficient and fine-tuning or RAG becomes the right tool instead — this is a common system design probe: "the user wants X, would you prompt-engineer this or fine-tune?"
- Prompt injection as a security concern if the role touches agents or tool-use — know it exists and the general mitigation posture (input/output validation, privilege separation), even if you're not expected to solve it fully live.

**RAG (Retrieval-Augmented Generation) — expect this to come up in system design regardless of role**
- The full pipeline: chunking strategy, embedding model choice, vector store/index (approximate nearest neighbor — know roughly how HNSW or IVF work at a conceptual level), retrieval, re-ranking, and generation with retrieved context.
- Why RAG exists: reduces hallucination, allows knowledge updates without retraining, handles proprietary/private data the base model never saw.
- Failure modes to be ready to diagnose: poor chunking losing context, retrieval returning irrelevant passages, the model ignoring retrieved context ("still hallucinating despite RAG"), stale indexes.
- Hybrid search (dense + sparse/BM25) and when pure semantic search underperforms keyword matching (rare terms, IDs, exact phrase matches).

**Agents & tool use — the newest area, and increasingly asked about at senior levels**
- The basic agent loop: plan → act (call a tool) → observe → repeat, and where this can fail (looping, hallucinated tool calls, compounding errors across steps).
- Function calling / tool schemas and their reliability limitations.
- Multi-agent patterns at a conceptual level (orchestrator/worker patterns) if relevant to the role — know the trade-off of added complexity vs capability gain, don't reach for multi-agent by default.

**Evaluation — a frequent, under-prepared topic**
- Why standard ML metrics (accuracy, F1) often don't apply directly to open-ended generation.
- Benchmark suites (MMLU, HellaSwag, HumanEval, etc.) and their known limitations (contamination, saturation, not reflecting real-world task performance).
- **LLM-as-judge** evaluation: using a stronger model to grade outputs — know its biases (position bias, verbosity bias, self-preference bias) and why human eval is still needed alongside it.
- Hallucination measurement approaches, and the distinction between "factually wrong" and "unfaithful to provided context" (relevant when RAG is in the loop).
- Online evaluation for LLM products: A/B testing challenges specific to generative outputs (non-deterministic outputs, harder-to-define success metrics than click-through rate).

**Inference & serving efficiency — comes up especially at infra-adjacent roles**
- KV-cache mechanics and why it's the dominant memory cost at inference time for long contexts.
- Quantization (int8/int4, GPTQ/AWQ-style approaches) — accuracy vs latency/memory trade-offs.
- Speculative decoding — using a small draft model to propose tokens a larger model verifies, for latency reduction — know the core idea even if not implementing it.
- Batching strategies (continuous/dynamic batching) for serving throughput.

**Staying current — this area moves faster than any textbook**
- Follow a small, high-signal set of sources rather than trying to read everything: the arXiv cs.CL/cs.LG new-submissions feed filtered to your subfield, a couple of labs' technical blogs (Anthropic, OpenAI, Google DeepMind, Meta AI), and one or two well-regarded independent newsletters/aggregators.
- For interviews specifically, being able to discuss **one or two recent papers or model releases in real depth** (actual mechanism, not just headline capability) reads far better than vague familiarity with many. Pick what's relevant to the target team and go deep on that.
- Expect interviewers to sometimes ask "what's a recent paper/development you found interesting and why" — have a genuine, specific answer ready, not a generic one.

---

## 3. Non-round preparation that matters at this level

- **Resume**: at Principal level your resume should read in terms of *scope and impact* (systems owned, teams influenced, business metrics moved), not just technologies used. Recruiters and hiring managers screen for this before the loop even starts.
- **Know the team/product you're interviewing for**, not just the company. At senior levels you're expected to have researched what the team actually builds and can ask informed questions about their specific technical challenges.
- **Negotiation prep**: total comp benchmarking (base/bonus/equity/refreshers), leveling calibration (Principal/Staff titles vary wildly by company — L7 at Google ≠ Principal at Amazon in scope), and having competing offers or a clear walk-away number if you can arrange it. This is worth real research time — the leverage difference between an unprepared and prepared negotiation at this level is often six figures in equity alone.
- **References**, if requested at final stages — line these up in advance so it's not a scramble.

---

## 4. Realistic time budget

This depends heavily on your starting point — how recently you've done DSA grinding, and how much you've actually *practiced* ML system design and behavioral out loud versus just "knowing the material." Ranges below assume you're already a competent working ML/AI engineer (i.e., not learning ML fundamentals from zero) and are preparing while employed full-time.

| Prep intensity | Total calendar time | Weekly hours | Best for |
|---|---|---|---|
| **Light refresh** | 2-3 weeks | 8-10 hrs/wk | You interview often / recently did a loop, just need to re-sharpen |
| **Standard** | 6-8 weeks | 10-15 hrs/wk | Typical case — haven't interviewed in 1-2+ years, need real practice reps |
| **Deep prep** | 10-12 weeks | 12-18 hrs/wk | Career pivot, targeting a notably higher level than current, or first FAANG attempt |

**Suggested allocation within a standard 6-8 week plan:**

- **Weeks 1-2 — Foundations refresh**: re-derive/re-implement the ML-from-scratch list until fluent; review DSA patterns from the cheatsheet; skim ML fundamentals topics and note weak spots.
- **Weeks 3-4 — System design + story building**: build your ML system design template and run 3-4 full mock designs; draft your 8-12 behavioral stories in STAR format and tighten them to ~90 seconds each.
- **Weeks 5-6 — Timed practice + mocks**: timed coding problems (25-35 min each) daily or every other day; at least 2-3 mock interviews with another senior engineer covering system design and behavioral, specifically for feedback on *communication*, which self-practice can't give you.
- **Weeks 7-8 (if deep prep) — Company-specific tailoring + polish**: research target companies' specific leadership principles/values, tailor 2-3 stories per company, do a couple of full-loop dry runs back to back to build stamina (real onsite loops are 4-6 hours in one day).

**Time-boxing rule of thumb**: allocate roughly equal weekly hours to (a) coding/ML-implementation drilling, (b) system design practice, and (c) behavioral story-building — technical candidates systematically under-allocate to (c), and it shows in the loop.

---

## 5. Logistics for interview day(s)

- Loops are often a full day (4-6 back-to-back rounds) — treat the week before as a taper, not a cram; being sharp beats knowing one more algorithm.
- Prepare 3-5 thoughtful questions **per round type** to ask interviewers — generic questions ("what's the culture like") read worse at senior levels than specific ones ("how does the team currently handle model retraining cadence for the ranking system").
- For virtual loops: test your setup (whiteboard tool, screen share, IDE) the day before, not minutes before.
- Eat and hydrate between rounds — cognitive fatigue is real across a 5+ hour loop and is one of the most common reasons strong candidates underperform on their last 1-2 rounds.

---

## 6. Resources to read/study, by round

Books cost money and time — this list is deliberately short. Each entry earns its place for a specific round rather than being generic "good to know."

### ML system design
- **"Machine Learning System Design Interview" — Ali Aminian & Alex Xu.** Near-essential. A 7-step framework plus 10 fully worked examples (feed ranking, recommendation systems, similar listings, people-you-may-know, etc.), built specifically around this interview format. Read this before running your own mock designs — it gives you the vocabulary and structure to practice against.
- **"Generative AI System Design Interview" — Ali Aminian & Hao Sheng.** The companion volume, covering GenAI-specific systems (RAG, chatbots, text-to-image, personalized headshot/video generation). Worth it if the role touches LLMs/GenAI at all, which most AI-track roles now do. Treat it as a framework-and-reference read rather than something to absorb cover-to-cover — some case studies repeat structure across chapters.
- **ByteByteGo newsletter/blog** (bytebytego.com) — same authors, free ongoing content, good for staying current between reading the books and your interview date.

### General software system design
- **"System Design Interview – An Insider's Guide" Vol. 1 & 2 — Alex Xu.** The standard reference. Read Vol. 1 in full if your role is ML-infra/platform-adjacent; Vol. 2 for more advanced/distributed-systems-heavy prompts. Skippable if your target role is purely applied modeling with no serving/infra ownership.
- **"Designing Data-Intensive Applications" — Martin Kleppmann.** Denser and more foundational than the interview-prep books — not interview-format, but builds the actual mental model (replication, partitioning, consistency, consensus) that the interview-prep books assume you have. Worth it if you have the deep-prep time budget; skip if you're on the light-refresh timeline.

### DSA / coding
- Your NeetCode 150 cheatsheet (already covered) + the neetcode.io platform itself for structured, categorized practice with video explanations.
- **"Cracking the Coding Interview" — Gayle Laakmann McDowell.** Older but still a solid drill book if you want problems with worked solutions in book form rather than a platform.

### ML fundamentals / breadth
- **"Designing Machine Learning Systems" — Chip Huyen.** Broader than the interview-format books — covers the full ML production lifecycle (data, training, deployment, monitoring) with real engineering judgment, not just interview scripts. Excellent for the ML breadth/depth round and for genuinely being better at the job, not just passing the interview.
- **"Deep Learning" — Goodfellow, Bengio, Courville.** The reference text if your fundamentals on backprop, optimization, or regularization theory are rusty. Dense — use it to look up specific topics rather than reading linearly under time pressure.
- **Stanford CS229 (Andrew Ng) / CS231n / CS224n lecture notes** — free, and the fastest way to refresh a specific fundamental (e.g. "why does L1 induce sparsity") without buying a book for one topic.

### LLM / GenAI / prompt engineering / fine-tuning
- **"Generative AI System Design Interview" — Ali Aminian & Hao Sheng.** (Already listed above — it's the primary interview-format resource for this whole area.)
- **Hugging Face NLP Course** (huggingface.co/course, free) — hands-on and current on transformers, fine-tuning, and the PEFT library (LoRA/QLoRA in practice, not just theory). One of the fastest ways to go from "knows the concept" to "has actually run it."
- **"Attention Is All You Need"** and the **original RLHF paper (InstructGPT, Ouyang et al.)** and the **DPO paper (Rafailov et al.)** — read these three directly rather than only secondhand summaries; interviewers at this level sometimes probe details that only show up in the actual papers.
- **Lil'Log (Lilian Weng's blog)** — consistently excellent, technically deep explainer posts on exactly this cluster of topics (RAG, agents, prompt engineering, diffusion models) — a very high signal-to-time-cost resource.
- **Anthropic, OpenAI, Google DeepMind technical blogs/model cards** — for staying current on what labs are actually shipping and how they describe their own training pipelines; also useful for having a genuine "recent development I found interesting" answer ready.
- **arXiv cs.CL (Computation and Language) new-submissions feed**, filtered/skimmed rather than read in full — pick 1-2 papers relevant to your target team to go deep on rather than trying to track everything.
- **LangChain / LlamaIndex documentation** — even if you won't use these specific frameworks day-to-day, their docs are a fast, concrete way to understand RAG pipeline components (chunking, retrievers, re-rankers) if you're coming from a more classical-ML background.

### Behavioral / leadership
- **Company career-page leadership principles/values pages, read verbatim, close to interview date** — Amazon's 16 Leadership Principles especially; these get revised, so don't rely on memory from a prior job search.
- **"The Manager's Path" — Camille Fournier.** Not interview-prep per se, but sharpens the vocabulary for talking about technical leadership, mentoring, and cross-team influence — useful for building out your STAR story bank with the right framing.

### Mock practice platforms
- **Pramp / interviewing.io** — free or low-cost peer mock interviews for coding and system design, useful specifically because self-practice can't surface communication issues.
- **exponent (tryexponent.com)** — has ML-specific and system-design-specific mock interview content and courses.

### MLOps / production infrastructure (ML Engineer & platform tracks)
- **"Designing Machine Learning Systems" — Chip Huyen.** (Already listed above — also the best single resource bridging ML theory and this operational layer.)
- **Official docs over books here**: Docker's official "Get Started" guide, Kubernetes' official concepts docs, and your target cloud provider's ML platform docs (AWS SageMaker, GCP Vertex AI, or Azure ML) — this area changes fast enough that vendor docs beat books.
- **MLflow and/or Weights & Biases documentation** — enough to speak concretely about experiment tracking and model registries even if you haven't used the exact tool your target company runs.
- **"Made With ML" (madewithml.com, free)** — a well-regarded, current, hands-on walkthrough of the full MLOps lifecycle (data, training, deployment, monitoring) with real code, not just slides.

### Data engineering
- **Airflow and Spark official "getting started" docs** — enough to reason about DAG-based orchestration and distributed data processing in an interview even if you're not a data engineer by trade.
- **SQL practice** (any standard platform — LeetCode's SQL section, StrataScratch) if it's been a while — this remains a baseline screen even for ML-titled roles.

### Forward Deployed Engineer specific
- **Palantir's own public FDE/Foundry materials and blog posts** — since Palantir originated the role, their own description of what FDEs actually do is a more reliable prep source than third-party summaries.
- **Anthropic's Model Context Protocol documentation** (modelcontextprotocol.io) — directly relevant if targeting an FDE/Applied AI Engineer role at Anthropic specifically, since MCP-based tooling is called out explicitly in their FDE job descriptions.
- **Practice source, not a book**: write out 3-5 deliberately vague, one-paragraph "client problem" prompts yourself (or have a peer write them) and time-box a 20-minute decomposition response — this specific format has no equivalent grind platform, so you have to construct the practice yourself.

### A reasonable reading order given a standard 6-8 week timeline
1. Skim "Designing Machine Learning Systems" (Huyen) early — weeks 1-2 — for fundamentals refresh and framing.
2. Read "Machine Learning System Design Interview" (Aminian & Xu) in weeks 2-3, before you start running mock ML system designs.
3. Read "Generative AI System Design Interview" and work through the Hugging Face NLP Course's fine-tuning/PEFT sections in weeks 3-4 — this is no longer optional for most AI-track roles.
4. Pull from Alex Xu's "System Design Interview" only for topics you're weak on, as a reference rather than cover-to-cover, if the role needs general system design at all.
5. Use CS229/231n/224n notes, Goodfellow et al., and Lil'Log posts as lookup references throughout, not a linear read.
6. In your final 1-2 weeks, pick one recent paper or model release relevant to your target team and go genuinely deep on it — this is higher-yield than broad shallow reading right before the loop.

---

## 7. Role-specific gaps: ML Engineer vs AI Engineer vs Forward Deployed Engineer

Everything above assumes a fairly traditional "ML/AI Engineer at a big tech company" loop. Checking against current postings surfaces real gaps depending on which of these three titles you're actually targeting — the titles increasingly point at genuinely different day-to-day work, not just different names for the same job.

### The honest 2026 distinction between the titles
- **ML Engineer** — closer to classical production ML: owns the path from prototype to a dependable learning system (data pipelines, feature engineering, training/retraining, deployment, monitoring). Skews toward algorithmic depth and operational scalability of *trained models*.
- **AI Engineer** — increasingly means **building applications on top of foundation models** via APIs, RAG, and agentic workflows, rather than training models from scratch. Full-stack in practice: backend orchestration, some frontend (chat UX, streaming responses, citations), product instinct, and evaluation rigor. If you're prepping for this track, everything in Section H (LLM/GenAI depth) matters *more* than classical ML theory — and there's a real skills gap most ML-trained candidates haven't closed yet (see below).
- **Forward Deployed Engineer (FDE)** — a genuinely different job, not a coding-interview variant. You embed directly with a customer, translate ambiguous business problems into technical roadmaps, and ship production code inside the client's environment — often solo or in a very small team, under time pressure, with no clean spec. Pioneered by Palantir, now a formal track at Anthropic, OpenAI, Scale AI, and others.

### Gap 1 — MLOps / production infrastructure (missing from the guide, and it's table stakes for ML Engineer)
This whole layer was absent above. If targeting ML Engineer or infra-flavored roles, review:
- **Containerization & orchestration**: Docker fundamentals, Kubernetes basics (pods, deployments, services) — these show up by name in the majority of current postings, not as a nice-to-have.
- **Cloud platform fluency in at least one of AWS/GCP/Azure**: managed ML services (SageMaker, Vertex AI, Azure ML), storage/compute basics, IAM fundamentals. Azure and AWS currently dominate postings roughly 2:1 combined over GCP — pick based on your target company, not a general preference.
- **CI/CD for ML specifically**: what changes vs standard software CI/CD — data validation steps, model validation gates before deploy, canary/shadow deployment for models.
- **Feature stores, model registries, experiment tracking**: know what problem each solves (Feast-style feature stores for train/serve consistency, MLflow/Weights & Biases for experiment tracking and model versioning) even if you haven't used the exact tool the target company uses.
- **GPU scheduling and distributed training basics**: data parallelism vs model parallelism vs pipeline parallelism at a conceptual level, mixed-precision training, and why these matter once a single GPU can't hold the model or the batch you need.
- **Observability for ML systems specifically**: this is explicitly called out as the overlap zone between ML Engineer and AI Engineer in 2026 — both roles are expected to be able to measure model behavior in production (drift detection, prediction logging, eval pipelines running continuously, not just once at launch).

### Gap 2 — Data engineering fundamentals (also missing above)
Multiple current postings for ML Engineer roles list this as a baseline requirement, not a specialization:
- ETL/ELT pipeline design, batch vs streaming data processing
- Basic fluency with a pipeline orchestrator (Airflow-style DAGs) and a distributed processing framework (Spark) at the "can reason about it in an interview" level, even if you won't hand-write Spark jobs day to day
- Data warehousing concepts and SQL — still a baseline screen for ML-adjacent roles, not something you can skip because the title says "ML" not "data"

### Gap 3 — Full-stack / product skills for the AI Engineer (applied) track
If targeting the applied/product AI Engineer track specifically, the gap is usually the opposite direction from Gaps 1-2 — less classical ML theory, more:
- **Orchestration frameworks in practice**: LangChain, LlamaIndex, or equivalent — not just RAG theory, but having actually wired up a retriever + generator pipeline.
- **Basic frontend/UX fluency for chat-based products**: streaming responses, handling partial/incremental output, citation UI patterns — this shows up explicitly in current postings for this track.
- **Product instinct and eval rigor together** — the ability to define what "good" looks like for a feature with no ground-truth labels, then build the eval harness to measure it, is called out repeatedly as the actual differentiator hiring managers screen for in this track.
- **Vector databases** as an infrastructure choice (not just a RAG concept) — pgvector vs a dedicated vector DB (Pinecone, Weaviate, Milvus) and the trade-offs (operational simplicity vs scale/features).

### Gap 4 — Forward Deployed Engineer: a genuinely different interview and prep track
Don't prep for an FDE loop the same way as a standard ML/AI Engineer loop — the format and the skill being tested are different:
- **Interview format is distinct**: typically (1) behavioral/fit interviews weighted toward ownership and communication, (2) a technical deep dive on coding/system design, and (3) a **decomposition case study** — an intentionally ambiguous, open-ended customer problem where you're evaluated on how you break it down, not on reaching one "correct" answer. The expected approach: ask clarifying questions, decompose into solvable chunks, propose a simple MVP first, iterate — explicitly resist the urge to jump straight to a polished solution.
- **"T-shaped" profile is the explicit hiring bar**: broad enough to be dangerous across the stack (data engineering, backend, some ML/LLM integration, basic frontend) plus real depth in at least one area — generalist breadth is a *feature* here, not a liability, unlike a narrower IC role.
- **Client-facing communication is graded as a hard skill**, not a soft one — practice explaining technical trade-offs to a non-technical stakeholder concisely, and practice translating a vague business ask ("we want to use AI for compliance") into a concrete technical scope before writing any code.
- **Security and deployment-environment awareness matters concretely**: familiarity with at least one cloud provider, basic security posture (data residency, access control, working inside a client's VPC/on-prem environment) comes up as a real screen, especially at defense-adjacent or regulated-industry-focused companies.
- **LLM-specific FDE work at AI labs** (Anthropic, OpenAI) skews toward: building orchestration layers around a foundation model, RAG pipelines, agent workflows, and — at Anthropic specifically — hands-on familiarity with the **Model Context Protocol (MCP)**, since FDEs there are described as building custom tooling using it directly.
- **Prior consulting or founder experience is explicitly valued** — postings for this track frequently list "former technical founder" or "software engineer with consulting experience" as directly relevant background, more so than for standard IC roles. If you have that background, foreground it; if you don't, be ready to demonstrate the underlying skill (working autonomously in an unfamiliar codebase/domain, owning outcomes end-to-end) through project stories even without the literal title on your resume.
- **Prep accordingly**: practice mock "decomposition" case studies specifically (an ambiguous one-paragraph prompt, no follow-up allowed beyond what you ask for) — this is a distinct drill from both LeetCode and standard ML system design, and most candidates haven't practiced it at all going in.

### What this means for your prep plan
Before deepening prep further, get precise about *which* of these three tracks you're actually interviewing for — the postings themselves increasingly disambiguate this even when the title alone doesn't ("AI Engineer" hides at least five distinct reqs in current job market data: applied/product AI engineer, ML engineer, MLOps/platform engineer, applied AI engineer doing RAG/evals/agents, and infra-flavored ML engineer). Read the actual posting's responsibilities section, not just the title, and weight Sections 2-6 above (classical loop) vs this section (infra/product/FDE gaps) accordingly.

---

## Quick summary checklist

- [ ] Comfortable with NeetCode-level DSA and can communicate through it fluently
- [ ] Can implement core ML algorithms from scratch, vectorized, from memory
- [ ] Have a memorized, flexible ML system design framework and have run 3+ mock designs
- [ ] Can explain the full post-training pipeline (SFT → RLHF/DPO) and LoRA/QLoRA mechanics without notes
- [ ] Can walk through a RAG pipeline end-to-end and name its common failure modes
- [ ] Have identified which specific track you're targeting (ML Engineer / applied AI Engineer / MLOps-platform / Forward Deployed Engineer) from the actual posting responsibilities, not just the title
- [ ] If ML Engineer or infra-adjacent: comfortable discussing Docker/Kubernetes basics, at least one cloud platform's ML services, and CI/CD-for-ML concepts
- [ ] If applied/product AI Engineer: have actually built (not just read about) a RAG pipeline with a real orchestration framework, and can define an eval harness for a feature with no ground-truth labels
- [ ] If Forward Deployed Engineer: have practiced at least 2-3 open-ended "decomposition" case studies (ambiguous prompt, self-directed clarifying questions, MVP-first approach)
- [ ] Have one recent paper or model release you can discuss in genuine depth, not just by headline
- [ ] Have 8-12 STAR stories covering the full theme list, each under 2 minutes
- [ ] Know target companies' specific leadership principles/values verbatim
- [ ] Have researched the specific team/product, not just the company
- [ ] Have done at least 2-3 live mock interviews with feedback from another senior engineer
- [ ] Have comp benchmarks and a negotiation plan ready before an offer arrives, not after
- [ ] Have a short list of good questions prepared per round type
