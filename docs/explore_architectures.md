# Explore Agent Architecture

The biggest confusion tech professionals have is applying the correct agent solution because many solutions appears to overlap responsibilities.

We will explore multiple agent architectures to determine fit for our agent workload.

## 1. An agent file with referenced files (eg. CLAUDE.md)

We created [CLAUDE.md](../week0_explore/explore_architecture/001_plain_agent/CLAUDE.md) where we are running the test and check how agent will use it to fulfill the user request.

We will check whether it will connect the MUD and complete a simple goal: eg. "Find the bakery and list the menu".

We want to use to smallest and least intelligent model and scale up.

### Technical Observations

#### Claude Model - Haiku 4.5 (Fastest for quick answers)

1. **Connection:** It first tried bash script but was timing out. It create python script to connect and was able to connect.
2. **Download:** It requested to download pyright-lsp. It was not granted.
3. **Debugging:** It got errors after connection and when asking for items on the menu. It went through multiple iteration, updating the python script until it resolved all the issues.
4. **Success:** It found bakery and displayed the results.

> I restarted the agent and gave the same command. This time it used shell script and was able to find the bakery and list items.

Agent did not update memory files. I asked following question: Why didn't you use data/player.md and data/world.md files for memory?

Agent: You're absolutely right! I should have referenced those files. The CLAUDE.md instructions explicitly say to utilize data/player.md and data/world.md to update work state. Let me check those files and update them with the bakery information.

#### Using Higher models

model Opus 4.8 (Best for everyday, complex tasks · ~2× usage vs Sonnet)

Opus 4.8 took longer than Haiku which I didn't expect but it checked the memory state at the begining and updated the memory files at the end.

Fable 5 followed the same path as Opus but it was getter communicator. It pointed out at the end that `dummy` was hungry and suggest buying a bread as next goal.

### Technical Conclusion

1. Agent behavior is inconsistent.
2. Higher model follows the instructions (create memory files) closely, give better suggestions and summary of their actions.
3. All models created temporary codes to accompolish the given task. This temporary files persists during the session but get deleted when agent restart. We need a resusable solution that persists between sessions.
4. Markdown files (CLAUDE.MD, data/*.md) may not be sufficient for complex player and world state.
5. Coding harness is not the best fit for this architecture by itself.

> It is possible a MUD SDK or MUD manager would provide a more reliable interace. MCP server could expose the MUD SDK as tool for the agent.
