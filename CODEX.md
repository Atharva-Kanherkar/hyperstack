# CODEX.md

Project instructions for OpenAI Codex / Codex CLI.

Follow **[AGENTS.md](./AGENTS.md)** as the primary policy file.

## Codex notes

- Nested `AGENTS.md` files (if added under a project later) override root guidance for that subtree.
- When generating code, default to stubs, type signatures, and failing tests — not complete solutions for the learning core.
- Prefer `apply_patch`-sized edits confined to the active `projects/pXX-*` directory.
