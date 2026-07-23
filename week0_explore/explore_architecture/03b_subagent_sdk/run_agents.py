"""Interactive REPL for the magician/warrior MUD subagents, defined via AgentDefinition
instead of .claude/agents/*.md.

Usage:
    python3 run_agents.py
Then type goals at the "You:" prompt (e.g. "magician: grind to level 3").
Type "exit"/"quit" or press Ctrl+D to stop.
"""

import asyncio
from pathlib import Path

from claude_agent_sdk import (
    AgentDefinition,
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    Message,
    ResultMessage,
    TaskNotificationMessage,
    TextBlock,
    ToolUseBlock,
)

PROJECT_ROOT = Path(__file__).parent

MAGICIAN = AgentDefinition(
    description=(
        'Plays the "magician" character on this project\'s tbaMUD server toward a stated '
        "in-game goal (leveling up, finding or buying an item, exploring, questing, earning "
        "gold, surviving/fleeing danger, etc.). Use whenever the player directs the magician "
        'specifically, or says "magician" / "the mage" / "smarty" alongside a MUD goal.'
    ),
    prompt="""You are the Player Journey Agent for the **magician** character on this
project's tbaMUD server. The player gives you a goal; play the character
toward it using the mud-player skill.

## Mud connection

- Server: `localhost:4000`
- Account: `smarty` / `goodbyemoon` — pass these as `--user smarty --pass
  goodbyemoon` to the mud-player skill's script. Never substitute another
  character's credentials, even if the skill or its script shows a
  different example.

## Memory

You start in the shared parent working directory, not inside `magician/`,
so use these paths exactly (not the bare `data/player.md` /
`data/world.md` the skill's own docs describe — those assume the skill's
own project root, which for this character is the `magician/` subfolder):

- `magician/data/player.md` — this character's stats/location/inventory/
  goal progress.
- `magician/data/world.md` — the map and world knowledge this character
  has discovered.

Read both before acting; update them after every batch of actions, per the
mud-player skill's workflow.""",
    skills=["mud-player"],
)

WARRIOR = AgentDefinition(
    description=(
        'Plays the "warrior" character on this project\'s tbaMUD server toward a stated '
        "in-game goal (leveling up, finding or buying an item, exploring, questing, earning "
        "gold, surviving/fleeing danger, etc.). Use whenever the player directs the warrior "
        'specifically, or says "warrior" / "the fighter" / "dummy" alongside a MUD goal.'
    ),
    prompt="""You are the Player Journey Agent for the **warrior** character on this
project's tbaMUD server. The player gives you a goal; play the character
toward it using the mud-player skill.

## Mud connection

- Server: `localhost:4000`
- Account: `dummy` / `helloworld` — pass these as `--user dummy --pass
  helloworld` to the mud-player skill's script. Never substitute another
  character's credentials, even if the skill or its script shows a
  different example.

## Memory

You start in the shared parent working directory, not inside `warrior/`,
so use these paths exactly (not the bare `data/player.md` /
`data/world.md` the skill's own docs describe — those assume the skill's
own project root, which for this character is the `warrior/` subfolder):

- `warrior/data/player.md` — this character's stats/location/inventory/
  goal progress.
- `warrior/data/world.md` — the map and world knowledge this character
  has discovered.

Read both before acting; update them after every batch of actions, per the
mud-player skill's workflow.""",
    skills=["mud-player"],
)


def render(message: Message) -> None:
    """Print an SDK message in human-readable form, skipping internal noise
    (init/rate-limit/thinking-token SystemMessages, raw tool-result payloads)."""
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock) and block.text:
                print(f"Claude: {block.text}")
            elif isinstance(block, ToolUseBlock):
                if block.name == "Agent":
                    subagent = block.input.get("subagent_type", "?")
                    desc = block.input.get("description", "")
                    print(f"  -> delegating to '{subagent}': {desc}")
                else:
                    print(f"  -> using tool: {block.name}")
    elif isinstance(message, TaskNotificationMessage):
        if message.status == "completed":
            print(f"  <- subagent finished: {message.summary}")
        else:
            print(f"  <- subagent task {message.status}")
    elif isinstance(message, ResultMessage):
        if message.is_error:
            print(f"[error] {message.result or message.errors}")
        elif message.total_cost_usd is not None:
            print(f"({message.duration_ms}ms, ${message.total_cost_usd:.4f})")


async def main() -> None:
    options = ClaudeAgentOptions(
        cwd=str(PROJECT_ROOT),
        agents={"magician": MAGICIAN, "warrior": WARRIOR},
        allowed_tools=["Agent"],
    )

    print("Magician/warrior MUD agent runner. Type a goal, or 'exit' to quit.\n")

    async with ClaudeSDKClient(options=options) as client:
        while True:
            try:
                goal = await asyncio.to_thread(input, "You: ")
            except EOFError:
                print()
                break

            goal = goal.strip()
            if not goal:
                continue
            if goal.lower() in {"exit", "quit"}:
                break

            await client.query(goal)
            async for message in client.receive_response():
                render(message)
            print()


if __name__ == "__main__":
    asyncio.run(main())
