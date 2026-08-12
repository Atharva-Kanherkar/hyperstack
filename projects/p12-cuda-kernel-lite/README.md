# p12 — CUDA/kernels lite: custom op or fused softmax

| Field | Value |
| --- | --- |
| **Status** | Not started |
| **Stack** | CUDA / Triton |
| **Demand** | Niche-high |
| **Time budget** | 2–4 weeks |

## Theory

Memory bandwidth, tiling, warps.

## Hand-code scope

One fused kernel; correctness vs PyTorch; speedup table.

## AI boundaries

Walk GPU model; you write the kernel.

## Ship target

Kernel + correctness tests + speedup writeup.

## Related jobs

Poly, ZeroEntropy, Thesis

## Notes

- Confirm this project ID is active before asking an AI assistant for substantial help.
- Update this README with results, metrics, and time spent when the track is underway.
- Full catalogue: [docs/syllabus.md](../../docs/syllabus.md) · jobs: [docs/jobs.md](../../docs/jobs.md)
