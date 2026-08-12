# Projects

One practice track per folder. Each starts as a stub README; implementation lands here when work begins.

| ID | Folder | Title | Demand |
| --- | --- | --- | --- |
| p01 | [p01-tool-calling-agent](p01-tool-calling-agent/) | Tool-calling agent from scratch | Very high |
| p02 | [p02-multi-agent-supervisor](p02-multi-agent-supervisor/) | Multi-agent supervisor with shared scratchpad | High |
| p03 | [p03-hybrid-rag](p03-hybrid-rag/) | Hybrid RAG: BM25 + embeddings + rerank | Very high |
| p04 | [p04-rust-vector-index](p04-rust-vector-index/) | Tiny vector index (HNSW or IVF) | High |
| p05 | [p05-eval-harness](p05-eval-harness/) | Eval harness with regression gates | Very high |
| p06 | [p06-agent-memory-graph](p06-agent-memory-graph/) | Temporal agent memory / context graph | High |
| p07 | [p07-document-intelligence](p07-document-intelligence/) | Document intelligence pipeline (OCR→structure→QA) | High |
| p08 | [p08-ui-grounding-agent](p08-ui-grounding-agent/) | Screenshot / UI grounding agent slice | High |
| p09 | [p09-finetune-eval](p09-finetune-eval/) | Fine-tune + evaluate a small model end-to-end | High |
| p10 | [p10-evolutionary-search](p10-evolutionary-search/) | Mini RL / evolutionary search for prompts or hparams | Niche-high |
| p11 | [p11-inference-server](p11-inference-server/) | Toy inference server (batching + KV cache) | High |
| p12 | [p12-cuda-kernel-lite](p12-cuda-kernel-lite/) | CUDA/kernels lite: custom op or fused softmax | Niche-high |
| p13 | [p13-rust-llm-gateway](p13-rust-llm-gateway/) | Rust streaming SSE LLM gateway | High |
| p14 | [p14-pyo3-ml-hotpath](p14-pyo3-ml-hotpath/) | Embed Python ML in Rust (PyO3) hot path | Medium |
| p15 | [p15-postgres-router](p15-postgres-router/) | Postgres-aware mini query router / pooler | Medium |
| p16 | [p16-gpu-job-queue](p16-gpu-job-queue/) | Distributed job queue for GPU experiments | High |
| p17 | [p17-voice-pipeline](p17-voice-pipeline/) | Streaming STT → LLM → TTS with barge-in | Medium |
| p18 | [p18-takehome-simulator](p18-takehome-simulator/) | YC-style take-home simulator: PDF agent + thin UI | Very high |
| p19 | [p19-postgres-hybrid-search](p19-postgres-hybrid-search/) | ParadeDB / Postgres full-text + vectors | High |
| p20 | [p20-clip-dual-encoder](p20-clip-dual-encoder/) | CLIP-style dual encoder from scratch (tiny) | Medium |
| p21 | [p21-agent-redteam](p21-agent-redteam/) | Red-team suite for agents (prompt injection + tool abuse) | High |
| p22 | [p22-concurrent-inverted-index](p22-concurrent-inverted-index/) | Concurrent inverted index snippets in Rust | Niche-high |
| p23 | [p23-attention-by-hand](p23-attention-by-hand/) | Implement attention + transformer block by hand | High |
| p24 | [p24-llm-observability](p24-llm-observability/) | Observability for LLM apps (traces, costs, failures) | High |

See [docs/syllabus.md](../docs/syllabus.md) for full writeups and [docs/jobs.md](../docs/jobs.md) for company mapping.

**Rule:** hand-code the core; AI tutors and reviews only. See root [AGENTS.md](../AGENTS.md).
