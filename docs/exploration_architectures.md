# Explore Agent Architecture

The biggest confusion tech professionals have is applying the correct agent solution because many solutions appears to overlap responsibilities.

We will explore multiple agent architectures to determine fit for our agent workload.

## 1. An agent file with referenced files eg. CLAUDE.md

We create an AGENT.md (i.e. CLUADE.md) file and check how agent will use it to fulfill the user request.
We will check whether it will connect the MUD (check log file) and complete a simple goal: eg. "Find the bakery and list the menu".

We want to use to smallest and least intelligent model and scale up.

### Technical Observations

Using Haiku 4.5 we created a CLAUDE.md with a simple prompt. and told it will need to manage its own local memory via simple markdown files. We provided it with the location of the MUD and the player credentials.

- The agent ignored the CLAUDE.md file and executed my request ("Can you find the bakery and tell me what is on the menu?") by following steps
  - Understand the Context
  - Explore the Directory Structure
  - Search for Bakery
  - Identity the Main Bakery
  - Read the Full File
  - Extract and Parse the Informaiton
  - Synthesize and Present
- After instructed agent to use CLAUDE.md file, it started spining (creating code, multi login to the server) without desired results.
  - It used 160K tokens. It achieved following before I stopped it.
    - Correctly the found the bakery room (#3009).
- It would be better we use coding harness for coding and avoid unnecessary token usage for spinning the code.

#### Using model Fable 5

I tried Anthropic highest paid mode (Fabel) and it completed the task and update data md files as requested in the CLAUDE.md. Here is its output reflecting on its success.

"What made it work this time: Instead of firing commands on fixed timers, the script reads the server's actual output and reacts — a small state machine for login (name → password → press return → menu), then a look-and-decide loop that identifies the current room and picks the next step toward the bakery. It turned out the character was already standing in the bakery from a previous session, so it just confirmed the room and ran list.".