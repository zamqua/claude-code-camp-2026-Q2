# Connection notes

These are empirical notes from probing a tbaMUD server directly (raw
sockets), since the login sequence has a couple of branches that aren't
obvious from a single happy-path run.

## Login handshake

1. Server sends a banner ending in `By what name do you wish to be known? `
   — send the username.
2. Server sends `Password: ` — send the password.
3. What comes next depends on whether the character is already "in" the
   world (link-dead from a previous session that didn't `quit`) or fully
   logged out:
   - **Fresh login**: server sends a message ending in `*** PRESS RETURN: `.
     Send a blank line, then a menu appears ending in `Make your choice: `.
     Send `1` to enter the game.
   - **Reconnect** (character was left link-dead, i.e. the previous
     session's socket was just closed without `quit`): server sends
     `Reconnecting.` and drops straight into the game — no menu, no
     `PRESS RETURN`, no room description auto-printed. Send `look` as your
     first command if you need to see where you are.

`scripts/mud_client.py` already detects and handles both branches — you
don't need to special-case this yourself, just be aware the `=== LOGIN ===`
output block you see in a given run may be short (reconnect) or longer
(fresh login through the menu).

## The game prompt

Once in-game, every response ends with a status line of the form:

```
21H 100M 83V (news) (motd) >
```

(current hit/mana/move points, then flags, then `>`). The script waits for
a pause in incoming data (not a fixed sleep) before considering a command's
response finished, so slow responses (e.g. combat rounds firing in the
background) are still captured — but if a single command triggers an
unusually long chain of automatic output, increase `--max-wait` and
`--idle-timeout` rather than assuming the response is complete.

## Why the script never sends `quit` automatically

Sending `quit` walks the character back to the character-selection menu —
useful when the player is done for the session, but wrong if you're just
between batches of commands within the same task. Simply closing the
socket (which happens automatically at the end of every script run) leaves
the character link-dead *in place* in the game world; reconnecting resumes
instantly via the "Reconnecting." path above, with the character exactly
where you left it. If the player's goal is complete and they want to log
out properly, include `quit` as the last command in your final batch.

## Script usage

```
printf '<cmd1>\n<cmd2>\n...\n' | python3 ${CLAUDE_SKILL_DIR}/scripts/mud_client.py \
  --user <username> --pass <password> \
  [--host <host>] [--port <port>] [--idle-timeout 1.5] [--max-wait 10] [--raw]
```

- This skill is shared across every character/agent, so it never hardcodes
  an account: `--user`/`--pass` are required, sourced from the calling
  project's own `CLAUDE.md`. Defaults to `localhost:4000` — only pass
  `--host`/`--port` to target a different server.
- `${CLAUDE_SKILL_DIR}` resolves to this skill's own directory no matter
  which agent's working directory the command runs from.
- One command per line on stdin, sent in order.
- Output is split into labeled blocks: `=== LOGIN ===` (one or more, for
  the handshake) followed by `=== COMMAND: <cmd> ===` for each command,
  in order.
- ANSI color codes and telnet negotiation bytes are stripped by default
  for readability; pass `--raw` to see the untouched bytes if you need to
  debug something the stripped view is hiding.
- An empty command (blank line) is valid input (e.g. for "press any key to
  continue" prompts mid-game) — don't strip blank lines out of your batch
  if you actually need to send one.
