# Handcode Lab

Personal laboratory for **hand-coding** AI, ML, and systems skills — with AI assistants used as tutors and reviewers, not as authors of the hard parts.

This repository tracks a deliberate practice curriculum aimed at YC-style engineering roles: production agents, retrieval, evals, multimodal systems, inference, and Rust × Python infrastructure. Projects land here as they are built. The goal is durable understanding, not autopiloted demos.

## Principles

1. **Hand-code the core.** Loops, indexes, kernels, parsers, schedulers, and eval scorers are written by the learner.
2. **AI is a tutor.** Explain theory, quiz, review diffs, suggest tests — do not dump finished solutions for the hard path.
3. **Ship artifacts.** Each project ends with something runnable, measured, and documented.
4. **Defend trade-offs.** Especially for take-home style work: prefer a clean MVP plus a “next steps” note over gold-plated architecture.

## Curriculum overview

| ID | Project | Stack | Demand |
| --- | --- | --- | --- |
| [p01](projects/p01-tool-calling-agent/) | Tool-calling agent from scratch | Python | Very high |
| [p02](projects/p02-multi-agent-supervisor/) | Multi-agent supervisor | Python | High |
| [p03](projects/p03-hybrid-rag/) | Hybrid RAG (BM25 + dense + rerank) | Python | Very high |
| [p04](projects/p04-rust-vector-index/) | Tiny vector index (HNSW/IVF) | Rust | High |
| [p05](projects/p05-eval-harness/) | Eval harness with regression gates | Python | Very high |
| [p06](projects/p06-agent-memory-graph/) | Temporal agent memory / context graph | Python (+ Rust later) | High |
| [p07](projects/p07-document-intelligence/) | Document intelligence (OCR → QA) | Python | High |
| [p08](projects/p08-ui-grounding-agent/) | Screenshot / UI grounding agent | Python | High |
| [p09](projects/p09-finetune-eval/) | Fine-tune + evaluate a small model | PyTorch | High |
| [p10](projects/p10-evolutionary-search/) | Mini RL / evolutionary search | Python | Niche-high |
| [p11](projects/p11-inference-server/) | Toy inference server (batching + KV) | Python / Rust | High |
| [p12](projects/p12-cuda-kernel-lite/) | Custom op / fused softmax | CUDA / Triton | Niche-high |
| [p13](projects/p13-rust-llm-gateway/) | Streaming SSE LLM gateway | Rust | High |
| [p14](projects/p14-pyo3-ml-hotpath/) | Python ML in Rust (PyO3) | Rust + Python | Medium |
| [p15](projects/p15-postgres-router/) | Mini Postgres router / pooler | Rust | Medium |
| [p16](projects/p16-gpu-job-queue/) | Distributed GPU experiment queue | Python | High |
| [p17](projects/p17-voice-pipeline/) | STT → LLM → TTS with barge-in | Python | Medium |
| [p18](projects/p18-takehome-simulator/) | YC-style PDF agent take-home drill | Python | Very high |
| [p19](projects/p19-postgres-hybrid-search/) | Postgres / ParadeDB hybrid search | Python + SQL | High |
| [p20](projects/p20-clip-dual-encoder/) | Tiny CLIP-style dual encoder | PyTorch | Medium |
| [p21](projects/p21-agent-redteam/) | Agent red-team / injection suite | Python | High |
| [p22](projects/p22-concurrent-inverted-index/) | Concurrent inverted index | Rust | Niche-high |
| [p23](projects/p23-attention-by-hand/) | Attention + transformer block by hand | NumPy / PyTorch | High |
| [p24](projects/p24-llm-observability/) | LLM app traces, costs, failures | Python | High |

Full writeups: [docs/syllabus.md](docs/syllabus.md) · printable paper: [docs/paper.html](docs/paper.html) · job mapping: [docs/jobs.md](docs/jobs.md)

### Suggested paths (optional)

- **Applied AI engineer:** p01 → p03 → p05 → p07 → p18  
- **Rust × AI infra:** p04 → p13 → p11 → p06 → p15  
- **Research → production ML:** p23 → p09 → p20 → p10 → p16  

## Repository layout

```text
.
├── AGENTS.md / CLAUDE.md / CURSOR.md / …   # AI assistant instructions
├── docs/                                   # Syllabus, jobs, paper layout
├── projects/                               # One folder per practice track
└── README.md
```

Each `projects/pXX-*` directory starts as a stub with a local README describing theory, hand-code scope, AI boundaries, and the ship target. Implementation lands in that folder when work begins.

## Working with AI assistants

This repo is set up so Cursor, Claude Code, Codex, Gemini CLI, and Copilot share the same learning rules:

| File | Audience |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Canonical, tool-agnostic rules |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code |
| [`CURSOR.md`](CURSOR.md) + [`.cursor/rules/`](.cursor/rules/) | Cursor |
| [`GEMINI.md`](GEMINI.md) | Gemini CLI |
| [`CODEX.md`](CODEX.md) | OpenAI Codex |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | GitHub Copilot |

**Non-negotiable:** do not implement the core algorithm or control loop for the active project unless the human has already written a first version and is asking for a review.

## Status

Curriculum defined; project stubs scaffolded. Implementations will appear under `projects/` as practice starts.

## Author

Atharva Kanherkar — learning in public toward production AI / ML / systems roles.

## License

MIT — see [LICENSE](LICENSE).
