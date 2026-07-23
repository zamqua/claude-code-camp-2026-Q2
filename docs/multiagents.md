# What's correct:
- Each agent (magician/, warrior/) has its own data/player.md and data/world.md — different inodes, empty and independent, so memory won't cross-contaminate.
- The skill (mud-player) is duplicated per-agent under each .claude/skills/, and both are discovered separately, namespaced as magician:mud-player and warrior:mud-player (confirmed in the skills listing). So each agent invokes its own copy — that's the right isolation model for Claude Code's directory-scoped skill discovery.
- SKILL.md correctly instructs reading/writing data/player.md and data/world.md relative to the project root (i.e., each agent's own root), not the skill directory.

# One real bug — credential mismatch:
- magician/CLAUDE.md sets credentials to smarty / goodbyemoon.
- But scripts/mud_client.py (identical in both copies) hardcodes defaults --user dummy --pass helloworld, and SKILL.md step 2 explicitly tells the agent "no credential lookup is needed" because it "defaults to this project's MUD instance (account dummy/helloworld)".

That default only matches warrior. If magician's agent follows the skill instructions as written, it will log in as dummy (warrior's account) instead of smarty, silently — likely piloting the wrong character or hitting a login conflict if warrior is connected simultaneously.

Fix: either update magician/.claude/skills/mud-player/scripts/mud_client.py defaults + SKILL.md text to smarty/goodbyemoon, or strip the "no credential lookup needed" claim from both copies and have the skill read credentials from each agent's own CLAUDE.md instead of hardcoding them in the script.

Want me to fix the magician copy's defaults now?