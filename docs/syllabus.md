# Hyperstack — Practice Syllabus

Canonical catalogue of 24 hand-coding practice tracks (`p01`–`p24`). Study theory, implement the core yourself, use AI as tutor/reviewer only, and ship a small artifact. Breadth for selection — not a mandate to finish everything.

Printable overview: [paper.html](paper.html) · Job mapping: [jobs.md](jobs.md)

## How to use a track

1. Read the project stub under `projects/pXX-*/README.md`.
2. Study the theory bullets; derive formulas where relevant.
3. Hand-code the listed core; keep AI off the hard path.
4. Ship the artifact; update the project README with results and time spent.

## Demand themes

### Applied AI product engineering

- Agent loops, tool schemas, multi-step reliability
- RAG: chunking, hybrid search, reranking, citation grounding
- Evaluation harnesses and regression gates in CI
- Document / OCR pipelines into structured data
- Context and memory graphs for long-running agents

### Systems × AI infrastructure

- Rust (or C++ / Go) on the critical path, with Python for ML experimentation
- Inference ops: batching, KV cache, vLLM / SGLang-class stacks
- Approximate nearest neighbor / search under latency budgets
- GPU orchestration and experiment schedulers
- Postgres with vectors, or database sandboxes for agents

## Interview process notes

### Common early-stage pattern

1. Founder or recruiter screen (20–60 minutes)
2. Technical round: debugging, pairing, ML+coding, or systems deep-dive
3. Take-home or 2–4 hour onsite mini-project
4. Team consensus and founder close
5. Often a paid trial (1 day–2 weeks) at seed stage

Typical total length: 1–3 weeks. Criterion is closer to “would I want this person shipping with us tomorrow?” than a multi-bar algorithm screen.

### Company-specific public processes

- **Poly:** Intro → project grill → take-home (AI assistance OK if decisions are defensible) → full team → paid onsite work trial
- **Thesis:** Intro (1h) → coding + ML challenge (90m) → paid one-week in-person trial
- **PgDog:** 30m intro → 1–3h technical deep dive → 1–2 week paid contract → full-time
- **Zep:** Founder screen → 2–3 hour team block (may include presentation) → decision call

### Candidate signal

Early YC companies emphasize shipping speed and trade-off defense over LeetCode relative to big tech. A recurring take-home failure mode is over-engineering (e.g. LangGraph + Celery + Redis for a PDF extraction task when a clean MVP + “next steps” README would win). Ask for an hour budget. Where AI is allowed, expect to defend every choice.

## Practice catalogue

### p01. Tool-calling agent from scratch

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Very high |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p01-tool-calling-agent/`](../projects/p01-tool-calling-agent/) |

- **Theory:** ReAct, tool schemas, planning vs reactive loops, failure modes.
- **Hand-code:** HTTP LLM client, JSON tool registry, loop with max steps, sandbox tools (fs/http/sql).
- **AI boundaries:** Explain theory; code review; never write the loop for you.
- **Ship target:** CLI agent + traces + README of tradeoffs.
- **Related jobs:** Mercura, Zep, Vector Legal, Cerenovus, CharacterQuilt

### p02. Multi-agent supervisor with shared scratchpad

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p02-multi-agent-supervisor/`](../projects/p02-multi-agent-supervisor/) |

- **Theory:** Role specialization, handoff protocols, deadlock/loops.
- **Hand-code:** Supervisor router, worker agents, message bus, budget/token caps.
- **AI boundaries:** Critique architecture; generate adversarial test cases.
- **Ship target:** Research→coder→critic pipeline on a real task.
- **Related jobs:** Cerenovus, CharacterQuilt, Mercura

### p03. Hybrid RAG: BM25 + embeddings + rerank

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Very high |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p03-hybrid-rag/`](../projects/p03-hybrid-rag/) |

- **Theory:** Chunking, lexical vs dense recall, reciprocal rank fusion, citation grounding.
- **Hand-code:** Tokenizer/BM25, embedding index, fusion + optional cross-encoder rerank, answer with citations.
- **AI boundaries:** Explain IR theory; review retrieval quality; you own the pipeline code.
- **Ship target:** Indexed corpus + query CLI with grounded answers and ablation notes.
- **Related jobs:** Mercura, Rhizome, ZeroEntropy, Vector Legal, Moss

### p04. Tiny vector index (HNSW or IVF)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | High |
| **Time** | 3–4 weeks |
| **Folder** | [`projects/p04-rust-vector-index/`](../projects/p04-rust-vector-index/) |

- **Theory:** ANN trade-offs, graph construction, recall@k vs latency.
- **Hand-code:** Distance kernels, insert/search, optional disk snapshot; criterion benches.
- **AI boundaries:** Walk through HNSW/IVF papers; you implement the index.
- **Ship target:** Crate with recall/latency benches vs brute force.
- **Related jobs:** ZeroEntropy, Moss, Poly, Zep

### p05. Eval harness with regression gates

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Very high |
| **Time** | 1–2 weeks |
| **Folder** | [`projects/p05-eval-harness/`](../projects/p05-eval-harness/) |

- **Theory:** Golden datasets, LLM-as-judge pitfalls, CI for prompts.
- **Hand-code:** Dataset format, scorers (exact/F1/judge), CLI compare, fail CI.
- **AI boundaries:** Suggest judge rubrics; you implement scoring.
- **Ship target:** pytest/CI that blocks prompt regressions.
- **Related jobs:** Mercura, Zep, Vector Legal, Vela

### p06. Temporal agent memory / context graph

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python (+ Rust later) |
| **Demand** | High |
| **Time** | 3–4 weeks |
| **Folder** | [`projects/p06-agent-memory-graph/`](../projects/p06-agent-memory-graph/) |

- **Theory:** Episodic vs semantic memory, entity resolution, forgetting.
- **Hand-code:** Extract entities/events; store graph; retrieve under a latency budget.
- **AI boundaries:** Discuss Graphiti-style designs; you own schema + queries.
- **Ship target:** Memory API with latency budget + ablation.
- **Related jobs:** Zep, Cerenovus, Ardent-adjacent

### p07. Document intelligence pipeline (OCR→structure→QA)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p07-document-intelligence/`](../projects/p07-document-intelligence/) |

- **Theory:** Layout, OCR noise, structured extraction, citations.
- **Hand-code:** PDF ingest, table/section parse, schema extract, grounded QA.
- **AI boundaries:** Help design schemas; you write parsers/tests.
- **Ship target:** PDF→JSON→cited answers; thin editable UI optional.
- **Related jobs:** Rhizome, Vector Legal, Mercura; common take-home shape

### p08. Screenshot / UI grounding agent slice

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 3–4 weeks |
| **Folder** | [`projects/p08-ui-grounding-agent/`](../projects/p08-ui-grounding-agent/) |

- **Theory:** VLM grounding, action spaces, long-horizon planning.
- **Hand-code:** Capture→detect elements→action select→verify loop on a toy app.
- **AI boundaries:** Paper summaries; you implement action selector + evals.
- **Ship target:** Agent completes five scripted UI tasks with success rate.
- **Related jobs:** RamAIn, CharacterQuilt, OnDeck (vision)

### p09. Fine-tune + evaluate a small model end-to-end

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | PyTorch |
| **Demand** | High |
| **Time** | 2–4 weeks |
| **Folder** | [`projects/p09-finetune-eval/`](../projects/p09-finetune-eval/) |

- **Theory:** LoRA/QLoRA, data curation, overfitting, eval vs vibe.
- **Hand-code:** Dataset prep, LoRA train script, eval suite, serve one endpoint.
- **AI boundaries:** Debug loss curves with you; you own training loop edits.
- **Ship target:** Before/after metrics + serving notes.
- **Related jobs:** Zep, Thesis, Poly, OnDeck, Hive

### p10. Mini RL / evolutionary search for prompts or hparams

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Niche-high |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p10-evolutionary-search/`](../projects/p10-evolutionary-search/) |

- **Theory:** Bandits, evolutionary strategies, reward hacking.
- **Hand-code:** Population, mutate, evaluate, select; log Pareto front.
- **AI boundaries:** Theory quizzes; you implement search.
- **Ship target:** Hill-climb that beats a hand-tuned baseline.
- **Related jobs:** Thesis, KelAI-adjacent

### p11. Toy inference server (batching + KV cache)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python / Rust |
| **Demand** | High |
| **Time** | 3–5 weeks |
| **Folder** | [`projects/p11-inference-server/`](../projects/p11-inference-server/) |

- **Theory:** Continuous batching, KV cache, throughput vs latency.
- **Hand-code:** Tokenize, cache tensors, dynamic batch scheduler, metrics.
- **AI boundaries:** Explain vLLM concepts; you reimplement a simplified core.
- **Ship target:** Bench: req/s and p95 vs naive sequential.
- **Related jobs:** Zep, Poly, Thesis, ZeroEntropy

### p12. CUDA/kernels lite: custom op or fused softmax

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | CUDA / Triton |
| **Demand** | Niche-high |
| **Time** | 2–4 weeks |
| **Folder** | [`projects/p12-cuda-kernel-lite/`](../projects/p12-cuda-kernel-lite/) |

- **Theory:** Memory bandwidth, tiling, warps.
- **Hand-code:** One fused kernel; correctness vs PyTorch; speedup table.
- **AI boundaries:** Walk GPU model; you write the kernel.
- **Ship target:** Kernel + correctness tests + speedup writeup.
- **Related jobs:** Poly, ZeroEntropy, Thesis

### p13. Rust streaming SSE LLM gateway

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | High |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p13-rust-llm-gateway/`](../projects/p13-rust-llm-gateway/) |

- **Theory:** Backpressure, timeouts, retries, auth, cost metering.
- **Hand-code:** axum/hyper proxy, stream parse, rate limits, structured logs.
- **AI boundaries:** API design critique; you write concurrent code.
- **Ship target:** Gateway crate with load-test numbers.
- **Related jobs:** Moss, Zep, Poly, Archil-style systems shops

### p14. Embed Python ML in Rust (PyO3) hot path

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust + Python |
| **Demand** | Medium |
| **Time** | 2 weeks |
| **Folder** | [`projects/p14-pyo3-ml-hotpath/`](../projects/p14-pyo3-ml-hotpath/) |

- **Theory:** FFI, GIL, zero-copy buffers.
- **Hand-code:** Rust service calls model; measure overhead.
- **AI boundaries:** Explain FFI pitfalls; you own unsafe boundaries carefully.
- **Ship target:** Hybrid service with a latency budget.
- **Related jobs:** ZeroEntropy, Poly, Zep

### p15. Postgres-aware mini query router / pooler

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | Medium |
| **Time** | 3–5 weeks |
| **Folder** | [`projects/p15-postgres-router/`](../projects/p15-postgres-router/) |

- **Theory:** Connection pooling, prepared statements, simple shard key.
- **Hand-code:** TCP proxy speaking a Postgres wire subset, or SQL rewrite layer.
- **AI boundaries:** Protocol docs; you implement the state machine.
- **Ship target:** Proxy that routes read/write with tests.
- **Related jobs:** PgDog, Archil, Ardent

### p16. Distributed job queue for GPU experiments

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p16-gpu-job-queue/`](../projects/p16-gpu-job-queue/) |

- **Theory:** Schedulers, idempotency, preemption, artifact store.
- **Hand-code:** Enqueue train jobs, workers, retries, result store.
- **AI boundaries:** Compare to Ray/Slurm concepts; you build a thin version.
- **Ship target:** Local multi-worker trainer orchestrator.
- **Related jobs:** Thesis, Poly, Hive

### p17. Streaming STT → LLM → TTS with barge-in

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Medium |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p17-voice-pipeline/`](../projects/p17-voice-pipeline/) |

- **Theory:** Partial transcripts, VAD, latency budgets, interruption.
- **Hand-code:** WebSocket audio loop, state machine, metrics.
- **AI boundaries:** Architecture review; you own the state machine.
- **Ship target:** Demo call with p95 end-to-end latency report.
- **Related jobs:** Pocket, Moss (retrieval for voice)

### p18. YC-style take-home simulator: PDF agent + thin UI

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | Very high |
| **Time** | 1 weekend drill |
| **Folder** | [`projects/p18-takehome-simulator/`](../projects/p18-takehome-simulator/) |

- **Theory:** Scope control; do not overbuild.
- **Hand-code:** Extract fields from messy PDF; editable table; 4–6h budget.
- **AI boundaries:** Allowed if you can defend every choice live.
- **Ship target:** MVP + README with time spent + next-steps section.
- **Related jobs:** Generic YC AI take-homes; Vector Legal; Mercura

### p19. ParadeDB / Postgres full-text + vectors

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python + SQL |
| **Demand** | High |
| **Time** | 1–2 weeks |
| **Folder** | [`projects/p19-postgres-hybrid-search/`](../projects/p19-postgres-hybrid-search/) |

- **Theory:** DB-native search vs external vector DB.
- **Hand-code:** Schema, hybrid SQL queries, ranking, explain plans.
- **AI boundaries:** SQL review; you write indexes/queries.
- **Ship target:** SQL notebook + API wrapping hybrid search.
- **Related jobs:** Rhizome (ParadeDB), PgDog-adjacent data path

### p20. CLIP-style dual encoder from scratch (tiny)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | PyTorch |
| **Demand** | Medium |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p20-clip-dual-encoder/`](../projects/p20-clip-dual-encoder/) |

- **Theory:** Contrastive loss, temperature, dual towers.
- **Hand-code:** Train on a tiny image-text set; retrieval eval.
- **AI boundaries:** Derive loss with you; you implement forward/backward pieces.
- **Ship target:** Trained toy model + R@1 / R@5.
- **Related jobs:** Poly, OnDeck, RamAIn

### p21. Red-team suite for agents (prompt injection + tool abuse)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 1–2 weeks |
| **Folder** | [`projects/p21-agent-redteam/`](../projects/p21-agent-redteam/) |

- **Theory:** Indirect injection, confused deputy, allowlists.
- **Hand-code:** Attack corpus, sandbox policy, metrics of blocked/allowed.
- **AI boundaries:** Brainstorm attacks; you implement harness.
- **Ship target:** Security eval report + mitigations.
- **Related jobs:** Any agent company (Mercura, Zep, CharacterQuilt)

### p22. Concurrent inverted index snippets in Rust

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | Niche-high |
| **Time** | 2–3 weeks |
| **Folder** | [`projects/p22-concurrent-inverted-index/`](../projects/p22-concurrent-inverted-index/) |

- **Theory:** Concurrency, practical memory ordering.
- **Hand-code:** Concurrent postings updates; snapshot readers.
- **AI boundaries:** Review unsafe; you minimize it.
- **Ship target:** Concurrent index with loom/stress tests.
- **Related jobs:** ZeroEntropy, Moss

### p23. Implement attention + transformer block by hand

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | NumPy / PyTorch |
| **Demand** | High |
| **Time** | 1–2 weeks |
| **Folder** | [`projects/p23-attention-by-hand/`](../projects/p23-attention-by-hand/) |

- **Theory:** QKV, scaled dot-product, causal mask, layernorm.
- **Hand-code:** No nn.MultiheadAttention until your version matches.
- **AI boundaries:** Derive shapes; quiz; refuse to dump the full solution.
- **Ship target:** Notebook proving parity vs reference.
- **Related jobs:** Poly (explicit equations), Thesis, OnDeck

### p24. Observability for LLM apps (traces, costs, failures)

| | |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python |
| **Demand** | High |
| **Time** | 1–2 weeks |
| **Folder** | [`projects/p24-llm-observability/`](../projects/p24-llm-observability/) |

- **Theory:** OpenTelemetry concepts, SLOs for non-determinism.
- **Hand-code:** Span every LLM/tool call; cost meter; failure taxonomy.
- **AI boundaries:** Suggest dashboards; you instrument code.
- **Ship target:** Trace viewer or Grafana-ready metrics.
- **Related jobs:** Mercura, Zep, Rhizome (Logfire etc.)

## Suggested shortlists

Optional starting bundles only.

- **Path A — Applied AI engineer:** p01 → p03 → p05 → p07 → p18 (Mercura / Rhizome / Vector Legal style)
- **Path B — Rust × AI infrastructure:** p04 → p13 → p11 → p06 → p15 (ZeroEntropy / Moss / Poly / Zep systems bar)
- **Path C — Research → production ML:** p23 → p09 → p20 → p10 → p16 (Thesis / OnDeck / Poly research-engineer flavor)

## Sources

- [Y Combinator Work at a Startup](https://www.workatastartup.com/)
- Public company job pages on ycombinator.com (Mercura, Poly, Thesis, Zep AI, Rhizome AI, RamAIn, OnDeck AI, Vector Legal, Cerenovus, PgDog, Dioxus Labs, and others), retrieved August 2026
- Standout, [How to Interview at a YC Startup](https://standout.work/blog/how-to-interview-at-a-yc-startup)
- Candidate write-ups on fast YC loops and take-home over-engineering (community posts, 2023–2026)
