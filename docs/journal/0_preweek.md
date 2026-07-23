# Preweek Technical Documentation

## Technical Goal

Explore coding agent (LLM + harness (eg. Claude Code)) to play tblMUD. Improve agent using skills and memory (player and world markdown files) and observe agent player achievements, misdirections, and token usage.

We tried following architectures:

1. Simple CLAUDE.md file and directly giving instruction to calude-code to play.
2. Add skill to play the MUD.
3. Add memory files (eg. player.md and world.md)
4. Create subagents and let multiple agents play together. Let's claude-code load agent text files.
5. Add code to launch sub agents to play the MUD. It is similar to set 4 but instead of having claude-code load subagents, we will use code to launch the subagents and give them instructions.

## Technical Uncertainity

## Technical Observations

- AI Agent (from now on simply Agent) is unpredictable in terms of carrying the commands for given task unless the prompt is detailed. When prompted to 'find the bakery and display the menu items', it just searched existing files and grep for the bakery items.
- Skills and memory files made Agent better in accomplising task in shorter time.
- Higher model are better in comprehending the task but still failed in accomplising difficult task (Find the massive Minatour and defeat it").
- Agent played quite enough to achieve certain level in the game but failed to accomplice difficult tasks. It wandered around through the game and burned the huge amount of tokens.
- Agent lacks the comprehension of the game. For example, it didn't keep track of hunger, thirst, and loss of movements (move score) until it was too late. This was improved by adding a task in the skill to monitor the move score and rest when it is at certain point.
- Run multiple agents to play together. Need more exploration.
- 
## Technical Conclusions

Agent can play MUD good enough to achieve certain level using skills and memory files but it can't level up continously without getting stuck or burning all the tokens.

## Key Takeway

We need better insight in the agent activities and custom harness to play complex game like MUD.