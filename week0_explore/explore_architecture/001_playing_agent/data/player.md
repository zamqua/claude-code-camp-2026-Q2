# Player State — dummy

- Last updated: 2026-07-15
- Character: dummy (password per CLAUDE.md)
- Stats at last logout: 18H 100M 83V, level ~1 (newbie)
- Condition: hungry (should buy/eat food soon — bread is right here in the bakery)
- Location at logout: The Bakery (north end of the street, only exit: south)

## Completed goals
- 2026-07-15: Found the bakery and listed its menu (danish 7, bread 14, waybread 73).

## Connection notes (for the agent)
- `nc localhost 4000`; protocol detection eats input sent in the first ~3s — wait before sending name.
- Clean login flow: name → password → PRESS RETURN (send blank line) → menu → `1` to enter game.
- If the previous session dropped without `quit`, login reconnects straight into the game (no PRESS RETURN/menu).
- Quit cleanly with `quit` then `0` at the menu.
- Helper script pattern: pipe timed printf lines into nc, strip ANSI with sed.
