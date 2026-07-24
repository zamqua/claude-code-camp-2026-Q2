---
title: Week 1 — Baseline MUD Agent (boukensha)
epic: BKN-1
status: in-development
foundation: hybrid (Ruby MudManager over MCP + Python harness)
backends: pluggable LLM providers/models
updated: 2026-07-24T00:00:00.000Z
---
# Week 1 — Baseline Agent (`boukensha`)

A reusable agent harness that plays a tbaMUD. This is the execution checklist for
epic **BKN-1**. Architecture diagram: [boukensha.excalidraw](../architecture/boukensha.excalidraw).
Full rationale: `nimbalyst-local/plans/hey-cuddly-turtle.md`.

Target layout: `week1_baseline/boukensha/` (Python) + a Ruby MCP tool server.

## Reuse (don't rebuild)
- `week0_explore/mud_manager/lib/mud_manager/session.rb` — threaded telnet Session + login.
- `week0_explore/mud_manager/lib/mud_manager/primitives.rb` — ~60 typed command primitives.
- `week0_explore/explore_architecture/03b_subagent_sdk/run_agents.py` — loop pattern.
- `week0_explore/explore_architecture/02_agent_skills/.claude/skills/mud-player/references/` — connection + command notes.

## Build order & checklist

- [ ] **BKN-11 — Hybrid bridge: Ruby MCP tool server.** Wrap `MudManager` in an MCP stdio server over one persistent `Session`. *(First: everything else calls tools through it.)*
- [ ] **BKN-3 — Tool registry.** `@register` decorator → name→schema→callable; fold MCP tools in.
- [ ] **BKN-4 — Backends.** `Backend` protocol + `AnthropicBackend` (model id selects Opus/Haiku/Fable).
- [ ] **BKN-2 — Agentic loop.** `Agent.run(goal)`: observe → think → act → persist.
- [ ] **BKN-9 — Context management.** Token accounting + compaction of old turns at a set limit.
- [ ] **BKN-5 — Structured logs.** JSONL per run: turns, tool calls, tokens, errors → `~/.boukensha/logs/`.
- [ ] **BKN-10 — Config directory.** `~/.boukensha/config.toml` (model, MUD host/port + creds, token limit); creds config-driven (fixes the multiagents.md mismatch).
- [ ] **BKN-6 — DSL / SDK surface.** `from boukensha import Agent` public API in `__init__.py`.
- [ ] **BKN-7 — Global binary.** `boukensha` console entry point in `pyproject.toml`; `pipx install -e`.
- [ ] **BKN-8 — CLI model flag.** `boukensha play --model … --goal …`.

## Verification
1. MUD up: `cd week0_explore/infrastructure && docker compose up -d` (port 4000).
2. Ruby MCP server standalone → call `look` via an MCP client → real room text returns.
3. End-to-end: `boukensha play --model claude-haiku-4-5 --goal "explore north and report the room"`.
4. Backend swap: rerun with `--model claude-opus-4-8`, no code change.
5. Compaction: long grind goal → logs show a compaction event before the token limit; run continues.
6. `~/.boukensha/config.toml` created; `~/.boukensha/logs/<run>.jsonl` has per-turn token/tool records.
7. SDK: `from boukensha import Agent` runs a goal programmatically.
8. All BKN tasks closed; this checklist fully ticked; board session at `complete`.
