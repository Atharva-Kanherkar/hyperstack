# Hyperstack — YC Jobs Mapping

Sample of Work at a Startup / YC openings (around August 2026) mapped to Hyperstack practice tracks. Compensations and openings change; verify on the live listings before applying.

Primary portal: [workatastartup.com](https://www.workatastartup.com/)

## Openings → projects

| Company | Role | Stack signal | Location / pay (listed) | Why relevant | Suggested tracks |
| --- | --- | --- | --- | --- | --- |
| Mercura (W25) | AI/LLM Engineer | Python, agents, RAG, FastAPI/React+ | EU / growth · YC listing | Agentic systems, hybrid retrieval, production evals | p01, p03, p05, p07, p18, p21, p24 |
| Zep AI (W24) | Applied Research / Senior AI Eng | Python + Rust/C++/Go, PyTorch, vLLM/SGLang | Remote-friendly seed · senior band | Agent memory; research to production | p01, p05, p06, p09, p11, p13, p14, p21, p24 |
| Poly (S22) | AI Research / Platform (AI Infra) | Python, Rust, PyTorch, CUDA | SF in-person · $150–350K + equity | Multimodal search; Rust encouraged | p04, p09, p11, p12, p13, p14, p16, p20, p23 |
| Thesis (F25) | Member of Technical Staff | Python, Rust, PyTorch, RL, GPU orchestration | SF · $120–170K + equity | Autonomous AI R&D; evolutionary search | p09, p10, p11, p12, p16, p23 |
| ZeroEntropy (W25) | Founding Engineer | Rust/C++, Python, CUDA, k8s, IR/rerankers | SF · founding equity | Retrieval engine in Rust + ML rerankers | p03, p04, p11, p12, p14, p22 |
| Moss | Backend / retrieval infra | Rust retrieval core; multi-cloud edge | Senior/Staff | Sub-10ms semantic search for voice AI | p03, p04, p13, p17, p22 |
| Rhizome AI (W26) | Founding Full Stack AI Eng | Next.js, FastAPI, Postgres/ParadeDB, agents | LatAm remote (PT overlap) · $60–120K + equity | Life-science RAG + regulatory agents | p03, p07, p19, p24 |
| RamAIn (W26) | Founding AI/ML Research Eng | Computer-use agents, multimodal, planning | Early W26 · founding | UI/screenshot agents; vector-search DNA | p04, p08, p20 |
| OnDeck AI (S25) | Founding ML Engineer | Vision / general visual tasks | Vancouver · $130–250K CAD + equity | Novel applied vision systems | p08, p09, p20, p23 |
| Vector Legal (W26) | Founding AI Engineer | TS + agents, OCR, eval harnesses | YC W26 · founding | Document agents with regression evals | p01, p05, p07, p18 |
| Cerenovus (S26) | Founding Engineer | Python, TS/React; Rust plus; Claude agents | SF in-person · $100–200K + room/board (summer) | Multi-agent ingestion → knowledge graphs | p01, p02, p06 |
| CharacterQuilt (P26) | MTS, Agent Systems | Computer-use / agent systems | NYC · $250–350K | Enterprise computer-use agents | p01, p02, p08, p21 |
| KelAI (P26) | Applied AI Engineer | ML + quant/alpha systems | NYC · $130–215K | Autonomous alpha / quant AI wedge | p10 |
| Pocket (W26) | Research Eng — Voice Intelligence | Voice ML + product stack | SF · $200–300K | Real-world voice intelligence | p17 |
| PgDog (P25) | Founding Software Engineer | Rust, Postgres sharding/load-balance | SF / CA / OR remote · $150–225K + 1–3% | Pure Rust systems; AI data-plane adjacent | p15, p19 |
| Archil (F24) | Founding Distributed Systems Eng | Rust, TCP/IP, Unix; some Go/k8s | SF in-person · $150–250K + equity | Distributed storage volumes in Rust | p13, p15 |
| Dioxus Labs (S23) | Founding Rust Engineer | Rust full-stack, linkers, WGPU, local AI FT | SF in-person · $125–150K + equity | Deep Rust; optional local-first finetune | p09, p13 |
| Vela (W26) | Member of Technical Staff | ML / AI recruiting product | SF · $120–300K | AI product eng with ML ownership | p05 |
| Ardent (P26) | Founding Eng — Product (Staff) | DB sandboxes for agents | SF · $150–200K | Agent-facing data/infra primitives | p06, p15 |
| Hive (S14) | Senior SWE, Machine Learning | Production ML | CA / remote CA · $124–188K CAD | Later-stage applied production ML | p09, p16 |

## Projects → companies (reverse index)

- **p01 (Tool-calling agent from scratch):** Mercura, Zep, Vector Legal, Cerenovus, CharacterQuilt
- **p02 (Multi-agent supervisor with shared scratchpad):** Cerenovus, CharacterQuilt, Mercura
- **p03 (Hybrid RAG: BM25 + embeddings + rerank):** Mercura, Rhizome, ZeroEntropy, Vector Legal, Moss
- **p04 (Tiny vector index (HNSW or IVF)):** ZeroEntropy, Moss, Poly, Zep, RamAIn
- **p05 (Eval harness with regression gates):** Mercura, Zep, Vector Legal, Vela
- **p06 (Temporal agent memory / context graph):** Zep, Cerenovus, Ardent
- **p07 (Document intelligence pipeline (OCR→structure→QA)):** Rhizome, Vector Legal, Mercura
- **p08 (Screenshot / UI grounding agent slice):** RamAIn, CharacterQuilt, OnDeck
- **p09 (Fine-tune + evaluate a small model end-to-end):** Zep, Thesis, Poly, OnDeck, Hive, Dioxus Labs
- **p10 (Mini RL / evolutionary search for prompts or hparams):** Thesis, KelAI
- **p11 (Toy inference server (batching + KV cache)):** Zep, Poly, Thesis, ZeroEntropy
- **p12 (CUDA/kernels lite: custom op or fused softmax):** Poly, ZeroEntropy, Thesis
- **p13 (Rust streaming SSE LLM gateway):** Moss, Zep, Poly, Archil, Dioxus Labs
- **p14 (Embed Python ML in Rust (PyO3) hot path):** ZeroEntropy, Poly, Zep
- **p15 (Postgres-aware mini query router / pooler):** PgDog, Archil, Ardent
- **p16 (Distributed job queue for GPU experiments):** Thesis, Poly, Hive
- **p17 (Streaming STT → LLM → TTS with barge-in):** Pocket, Moss
- **p18 (YC-style take-home simulator: PDF agent + thin UI):** Vector Legal, Mercura, generic YC AI take-homes
- **p19 (ParadeDB / Postgres full-text + vectors):** Rhizome, PgDog
- **p20 (CLIP-style dual encoder from scratch (tiny)):** Poly, OnDeck, RamAIn
- **p21 (Red-team suite for agents (prompt injection + tool abuse)):** Mercura, Zep, CharacterQuilt
- **p22 (Concurrent inverted index snippets in Rust):** ZeroEntropy, Moss
- **p23 (Implement attention + transformer block by hand):** Poly, Thesis, OnDeck
- **p24 (Observability for LLM apps (traces, costs, failures)):** Mercura, Zep, Rhizome

## Path → role flavor

| Path | Tracks | Role flavor |
| --- | --- | --- |
| A — Applied AI engineer | p01 → p03 → p05 → p07 → p18 | Mercura / Rhizome / Vector Legal |
| B — Rust × AI infrastructure | p04 → p13 → p11 → p06 → p15 | ZeroEntropy / Moss / Poly / Zep systems |
| C — Research → production ML | p23 → p09 → p20 → p10 → p16 | Thesis / OnDeck / Poly research-engineer |

## Notes

- Pure algorithmic interview drills appear less often than at large product companies.
- Founders commonly screen for shipping speed, debugging instinct, and defending trade-offs.
- For take-homes: prefer a clean MVP plus a “next steps” note over gold-plated architecture.
