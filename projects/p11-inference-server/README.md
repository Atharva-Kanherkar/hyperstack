# p11 — Toy inference server (batching + KV cache)

| Field | Value |
| --- | --- |
| **Status** | Not started |
| **Stack** | Python / Rust |
| **Demand** | High |
| **Time budget** | 3–5 weeks |

## Theory

Continuous batching, KV cache, throughput vs latency.

## Hand-code scope

Tokenize, cache tensors, dynamic batch scheduler, metrics.

## AI boundaries

Explain vLLM concepts; you reimplement a simplified core.

## Ship target

Bench: req/s and p95 vs naive sequential.

## Related jobs

Zep, Poly, Thesis, ZeroEntropy

## Notes

- Confirm this project ID is active before asking an AI assistant for substantial help.
- Update this README with results, metrics, and time spent when the track is underway.
- Full catalogue: [docs/syllabus.md](../../docs/syllabus.md) · jobs: [docs/jobs.md](../../docs/jobs.md)
