# CURSOR.md

Project instructions for Cursor.

## Shared rules

Follow **[AGENTS.md](./AGENTS.md)**. Cursor-specific scoped rules live in [`.cursor/rules/`](.cursor/rules/).

## Cursor workflow

- Use Agent mode for navigation, reviews, scaffolding *interfaces*, and test suggestions.
- Do **not** use Agent mode to generate the full core algorithm for an active learning project.
- Prefer applying `.cursor/rules/handcode-lab.mdc` (always on) over ad-hoc chat-only norms.
- When editing under `projects/pXX-*`, keep changes inside that project unless shared docs must update.

## File map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Canonical learning rules |
| `.cursor/rules/handcode-lab.mdc` | Always-applied Cursor rule |
| `docs/syllabus.md` | Full practice catalogue |
| `projects/` | Implementations |

## Anti-patterns

- Replacing a from-scratch track with a heavy framework by default.
- Committing large model weights or datasets.
- Expanding scope across multiple `pXX` folders in one unfocused change.
