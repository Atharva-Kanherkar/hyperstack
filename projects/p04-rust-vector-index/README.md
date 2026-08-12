# p04 — Tiny vector index (HNSW or IVF)

| Field | Value |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | High |
| **Time budget** | 3–4 weeks |

## Theory

ANN trade-offs, graph construction, recall@k vs latency.

## Hand-code scope

Distance kernels, insert/search, optional disk snapshot; criterion benches.

## AI boundaries

Walk through HNSW/IVF papers; you implement the index.

## Ship target

Crate with recall/latency benches vs brute force.

## Related jobs

ZeroEntropy, Moss, Poly, Zep

## Notes

- Confirm this project ID is active before asking an AI assistant for substantial help.
- Update this README with results, metrics, and time spent when the track is underway.
- Full catalogue: [docs/syllabus.md](../../docs/syllabus.md) · jobs: [docs/jobs.md](../../docs/jobs.md)
