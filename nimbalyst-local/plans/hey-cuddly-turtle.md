# Plan: Managing the `week1_baseline` MUD Agent with Nimbalyst

## Context

**Why this exists.** `week0_explore/` proved out five ways to get an LLM to play a tbaMUD, and the journals (`docs/journal/0_preweek.md`, `docs/explore_architectures.md`) all reached the same conclusion: *the coding harness alone is not enough — we need a custom harness with better observability, persistent state, and a reliable MUD interface.* `week1_baseline/` is the empty placeholder where that custom harness ("**boukensha**", 冒険者 = adventurer — matching the empty `.boukensha/` dir) gets built.

**What this plan is.** The user is new to Nimbalyst. This plan has two jobs:
1. **Primary — set up Nimbalyst to *manage* the work**: turn the 9 baseline components into a tracked, visible, executable body of work (plan doc + tracker + kanban board + architecture diagram).
2. **Secondary — define the baseline agent architecture** so the tracked tasks have real technical substance to point at.

**Decisions locked in:** Hybrid foundation (Ruby `MudManager` = MUD/tool layer over MCP; Python = agent harness). Full Nimbalyst setup. "Multiple backends" = pluggable **LLM providers/models**.

**Reuse, don't rebuild.** These already exist and are the substrate:
- `week0_explore/mud_manager/lib/mud_manager/session.rb` — threaded telnet session + login handshake.
- `week0_explore/mud_manager/lib/mud_manager/primitives.rb` — ~60-method typed command DSL returning `Command` structs (explicitly designed to be "wrapped as tool calls").
- `week0_explore/explore_architecture/03b_subagent_sdk/run_agents.py` — existing `claude-agent-sdk` loop/`AgentDefinition` pattern.
- `week0_explore/explore_architecture/02_agent_skills/.claude/skills/mud-player/` — connection notes + command reference to fold into system prompt/tool docs.

---

## Part A — Nimbalyst work-management setup

Execution order. Each item names the Nimbalyst tool/skill used (all are new-to-you surfaces, hence the one-liners).

1. **Working plan doc** — run the `planning:design` skill to generate `docs/plans/week1-baseline.md` (YAML frontmatter + per-component checklist). `docs/plans/` already exists and is empty. This becomes the execution checklist the build session drives against via `planning:implement`.

2. **Tracker epic + 9 tasks** — use `tracker_*` tools:
  - `tracker_set_issue_key_prefix` → `BKN` (boukensha), so items render as `BKN-1` chips.
  - One **epic**: "Baseline MUD agent (boukensha)".
  - Nine **task** items, one per component (list in Part B), each linked to its target files via `tracker_link_file` and to the build session via `tracker_link_session`.

3. **Kanban board** — `mcp__nimbalyst__update_session_meta` drives each session's phase (`planning → implementing → validating → complete`). For parallel work, spin off focused sub-sessions with the `planning:launch-new-session` skill (e.g. one session for the Ruby MCP tool-server, one for the Python harness).

4. **Architecture diagram** — an Excalidraw file `docs/architecture/boukensha.excalidraw` (via `excalidraw` skill / `excalidraw_import_mermaid`) showing the hybrid flow: LLM backend ↔ Python harness (loop + tool registry + context manager + logger) ↔ MCP ↔ Ruby `MudManager` ↔ MUD socket.

5. **(Optional) State model** — the journals flagged markdown memory as too weak for complex player/world state. If that bites, model it with the `datamodellm` skill (`.datamodel`) instead of `player.md`/`world.md`. Left optional for week1.

---

## Part B — Baseline agent architecture (the 9 components)

Target layout: `week1_baseline/boukensha/`. Each component below is one tracker task.

| # | Component | Approach | Key files |
| --- | --- | --- | --- |
| 1 | **Agentic loop** | Python `observe → think → act → persist` loop; evolve from `run_agents.py` into a standalone `Agent.run(goal)`. | `boukensha/core/loop.py` |
| 2 | **Tool registry + tools** | `@register` decorator building a name→schema→callable map; tools are thin wrappers over `MudManager::Primitives` reached over MCP. | `boukensha/tools/registry.py`, `tools/mud.py` |
| 3 | **Multiple LLM backends** | `Backend` protocol (`complete(messages, tools) -> response`); `AnthropicBackend` first (Opus/Haiku/Fable via model id). Pluggable for other providers. | `boukensha/backends/base.py`, `backends/anthropic.py` |
| 4 | **Logs** | Structured JSONL per run: each loop turn, tool call + result, token usage, errors. Directly addresses the journals' "need better insight into agent activities." | `boukensha/obs/logger.py`, writes to `~/.boukensha/logs/` |
| 5 | **DSL / SDK usage** | Clean importable API: `from boukensha import Agent; Agent(backend=...).run(goal)`. Public surface in `__init__.py`. | `boukensha/__init__.py` |
| 6 | **Global binary** | `boukensha` console entry point (`[project.scripts]` in `pyproject.toml`); `pipx install -e` → on PATH. | `week1_baseline/pyproject.toml`, `boukensha/cli.py` |
| 7 | **Optional CLI model flag** | `boukensha play --model claude-opus-4-8 --goal "reach level 3"`; resolves to the backend/model. | `boukensha/cli.py` |
| 8 | **Context management / compaction** | Track token count against a configured limit; when exceeded, summarize older turns into a compact memory block (keep system + recent turns verbatim). Fixes the "burns all tokens" failure. | `boukensha/core/context.py` |
| 9 | **Config directory** | `~/.boukensha/` (XDG-aware): `config.toml` (default model, MUD host/port, token limit, log level) + `logs/`. Created on first run. | `boukensha/config.py` |

**Hybrid bridge (the one new integration piece).** Wrap `MudManager` in a small **Ruby MCP stdio server** exposing the primitives as MCP tools over a single persistent `Session` (so the MUD connection stays alive between turns and characters stay link-alive, per the connection notes). The Python harness connects as an MCP client and folds those tools into its registry (component 2). This is the journals' own recommendation: *"MCP server could expose the MUD SDK as tool for the agent."*
- New: `week0_explore/mud_manager/bin/mcp_server.rb` (or `week1_baseline/mud-mcp/`).
- Fix carried over from `docs/multiagents.md`: the `dummy/helloworld` vs `smarty/goodbyemoon` credential mismatch — make credentials config-driven (component 9), never hardcoded.

---

## Verification

1. **MUD up:** `cd week0_explore/infrastructure && docker compose up -d`, confirm port 4000 (`week0_explore/HOW_TO_PLAY.md`).
2. **Tool layer:** start the Ruby MCP server standalone; call a primitive (e.g. `look`) via an MCP client and confirm real MUD output returns.
3. **Loop end-to-end:** `boukensha play --model claude-haiku-4-5 --goal "explore north and report the room"` → agent connects, issues tool calls, and the goal completes.
4. **Backend swap:** rerun with `--model claude-opus-4-8`; confirm no code change needed (component 3).
5. **Compaction:** run a long grind goal; confirm logs show a compaction event before the token limit and the run continues instead of dying (component 8).
6. **Logs + config:** confirm `~/.boukensha/config.toml` was created and `~/.boukensha/logs/<run>.jsonl` has per-turn token/tool records.
7. **SDK:** in a Python REPL, `from boukensha import Agent` and run a goal programmatically (component 5).
8. **Nimbalyst artifacts:** `docs/plans/week1-baseline.md` exists with all 9 checked off on completion; `BKN-1..9` tracker tasks closed; board session at `complete`; architecture diagram renders.
