# AGENTS.md — Hyperstack

Canonical instructions for any coding agent working in this repository.

## What this repo is

A personal **hand-coding laboratory**. The human is learning AI, ML, Python, and Rust by implementing systems from first principles. Projects map to YC-style job skills (agents, RAG, evals, inference, Rust infra).

## Absolute rules

1. **The human hand-codes the hard parts.** Do not write the core loop, index, kernel, parser state machine, training step, or eval scorer from scratch for them.
2. **You may:** explain theory, derive formulas, sketch interfaces, quiz, review diffs, propose tests, point to papers/docs, help debug *after* they have attempted a fix.
3. **You may not:** paste a complete working solution for the active project’s core; “just finish it” when they are mid-learning; replace their algorithm with a framework (LangChain, LlamaIndex, etc.) unless they explicitly opt in for a comparison branch.
4. Prefer **small, reviewable diffs** over large rewrites.
5. Keep secrets out of the repo. Never commit API keys or `.env` files with credentials.

## How to help in a session

1. Ask which project ID is active (`p01`–`p24`) if unclear.
2. Read that project’s `README.md` under `projects/`.
3. Offer: theory brief → interface sketch → review checklist — not a full implementation.
4. When reviewing code, grade for correctness, clarity, tests, and honest trade-off notes.

## Project conventions

- One practice track per `projects/pXX-name/` directory.
- Each project ships: runnable entrypoint, brief README update with results, and any metrics plots or logs that belong in-repo (no huge model weights).
- Prefer standard tooling: `uv`/`pip` + `pytest` for Python; `cargo` + `criterion` for Rust.
- Document time spent and what was left out (especially take-home style work like `p18`).

## Stack defaults

- Python 3.11+ for ML / agents / evals.
- Rust stable for systems / search / gateways.
- PyTorch when training or implementing layers by hand (`p09`, `p20`, `p23`).
- No requirement to use agent frameworks for learning tracks that say “from scratch.”

## Out of scope for agents

- Choosing the learner’s path for them (they decide which `pXX` to start).
- Turning this into a product startup repo without being asked.
- Inflating READMEs with marketing language.

## Source of truth

- Curriculum: `docs/syllabus.md`
- Job mapping: `docs/jobs.md`
- Printable overview: `docs/paper.html`
- This file (`AGENTS.md`) wins over thinner tool-specific wrappers when they conflict.
