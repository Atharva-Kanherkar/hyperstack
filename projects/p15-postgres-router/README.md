# p15 — Postgres-aware mini query router / pooler

| Field | Value |
| --- | --- |
| **Status** | Not started |
| **Stack** | Rust |
| **Demand** | Medium |
| **Time budget** | 3–5 weeks |

## Theory

Connection pooling, prepared statements, simple shard key.

## Hand-code scope

TCP proxy speaking a Postgres wire subset, or SQL rewrite layer.

## AI boundaries

Protocol docs; you implement the state machine.

## Ship target

Proxy that routes read/write with tests.

## Related jobs

PgDog, Archil, Ardent

## Notes

- Confirm this project ID is active before asking an AI assistant for substantial help.
- Update this README with results, metrics, and time spent when the track is underway.
- Full catalogue: [docs/syllabus.md](../../docs/syllabus.md) · jobs: [docs/jobs.md](../../docs/jobs.md)
