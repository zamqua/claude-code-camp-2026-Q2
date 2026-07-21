---
name: mud-player
description: Plays a CircleMUD/tbaMUD-family MUD server on the player's behalf toward a stated in-game goal (leveling up, finding or buying an item, exploring an area, completing a quest, earning gold, surviving/fleeing danger, etc.), by scripting a raw socket connection that logs in and sends game commands. Use this skill any time the player states or implies a goal to pursue inside the MUD — including casual phrasing like "go kill some rats", "see what's south of here", "get me a better weapon", "keep grinding until level 3" — even without the words "MUD" or "skill". Also use it to check in on standing progress by reading the persisted player/world memory. Do not use it for questions about MUD server administration, world-building/olc, or C source code of the MUD itself — those are different tasks.
---

# MUD Player

Play a CircleMUD-derived MUD (tbaMUD) toward a goal the player gives you, by
driving the game through raw socket commands and tracking what you learn
across sessions so you don't have to relearn the map or the character's
state from scratch every time.

## Why this shape

MUDs are stateful, real-time, and text-only: the only way to act is to send
a line of text and read what comes back, and the world keeps existing
whether or not you're connected. That means two things drive the design
here:

1. **Talk to the socket through the bundled script, not ad hoc `nc`.** The
   login handshake has several branches (fresh login vs. an
   already-linkdead character reconnecting; see
   `references/connection-notes.md`) and the game prompt needs a way to
   know when a response has finished arriving. The script
   (`scripts/mud_client.py`) already handles this — reinventing it inline
   with raw `nc`/`telnet` calls each turn just re-solves the same problem
   worse and burns turns on protocol noise instead of the player's goal.
2. **Persist what you learn, because the world doesn't reset.** Character
   stats, inventory, and the map are real and durable on the server side.
   Re-discovering them every session wastes moves and risks contradicting
   what's actually true. `data/player.md` and `data/world.md` (at the
   project root) are the memory for this — read them before acting, write
   back what changed after.

## Workflow

1. **Load memory.** Read `data/player.md` and `data/world.md` if they
   exist (paths are relative to the project root, not the skill
   directory). They tell you the character's last known stats/location/
   inventory and the map of rooms already explored. If they don't exist
   yet, this is the first run — start from an empty map and figure out the
   starting room from the game's own output.

2. **Act in small batches, not one giant script.** Send a handful of
   commands (e.g. a few moves, then `look`), inspect the output, and decide
   the next batch — rather than queuing up dozens of commands blind. The
   world can respond unexpectedly (a mob attacks, an exit is blocked, you
   die of hunger) and blind batching wastes moves correcting course after
   the fact. Run the script like this:

   ```
   printf 'look\nnorth\nlook\n' | python3 .claude/skills/mud-player/scripts/mud_client.py
   ```

   The script defaults to this project's MUD instance
   (`localhost:4000`, account `dummy`/`helloworld`) so no credential
   lookup is needed. Pass `--host`/`--port`/`--user`/`--pass` only if you
   need to point at a different server or account. Each line piped to
   stdin is one game command, sent in order, waiting for the game's
   prompt between each. The output is labeled per command so you can tell
   which response belongs to which action.

3. **Read `references/connection-notes.md` once per session** if you
   haven't already — it covers the login branches, the prompt format
   (`NNH NNM NNV (flags) >`), and why the client deliberately does *not*
   send `quit` unless you tell it to (closing the socket just leaves the
   character link-dead in place, so the next run picks up exactly where
   you left off — sending `quit` instead logs out to the character menu,
   which is only useful when the player is done for the session).

4. **Update memory after every batch of actions**, not just at the end —
   if the session gets interrupted, partial progress should still be
   captured:
   - `data/player.md`: current room, HP/mana/move, level/exp, inventory,
     equipped gear, gold, the active goal, and progress toward it.
   - `data/world.md`: rooms visited (name, brief description, exits, and
     where each exit leads if known), notable NPCs/shops, and anything
     learned that would save time on a future run (e.g. "the baker sells
     bread for 2 gold", "the armory is south of Main Street").

   Keep both files terse and structured (headings/bullets) — they're
   working memory for you, not a narrative for the player.

5. **Know when to stop.** Report back to the player once the stated goal is
   reached, or if you hit something that needs their judgment call (character
   about to die, goal seems impossible, ambiguous instructions). Don't keep
   grinding past the goal "just in case."

6. **Monitor movement points and rest proactively.** Movement exhaustion is a
   critical bottleneck in sewer/confined areas. After every action:
   - Check current movement points via `score`
   - If movement ≤ 20: **Display a warning** to the player ("⚠️ Movement LOW (X/86) - building buffer")
   - If movement ≤ 10: **Automatically rest** with `sleep` command, then wait for recovery
   - Only resume navigation when movement is ≥ 30 points
   - Plan multi-room routes only when starting with ≥ 50 movement

   This prevents exhaustion traps where low movement recovery makes escape impossible.

## Reference

- `references/connection-notes.md` — login handshake branches, prompt
  format, reconnect behavior, and script usage details. Read this before
  the first script invocation of a session.
- `references/tbamud-commands.md` — common tbaMUD/CircleMUD command
  vocabulary (movement, combat, inventory, shops, communication) for
  building command batches.
