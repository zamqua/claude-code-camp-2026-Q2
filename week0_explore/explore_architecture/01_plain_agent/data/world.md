# World Knowledge — Midgaard (zone 30)

## Known rooms and connections
- **The Temple Of Midgaard (3001)** — spawn/entry area. Exits: n (altar), e (donation), s (Temple Square), w (Reading Room), d
- **The Temple Square (3005)** — n: Temple, e: Grunting Boar Inn, s: Market Square, w: Clerics' Guild (guarded — knight templar blocks non-members going north)
- **Market Square (3014)** — n: Temple Square, e: Main St (3015), s: Common Square, w: Main St (3013)
- **Main Street (3013)** — n: **The Bakery (3009)**, e: Market Square, s: Armory, w: Main St (3012)
- **The Bakery (3009)** — only exit: s. NPCs: the baker, 2 cityguards

## Route: Temple → Bakery
`s, s, w, n`

## Bakery menu (verified in-game via `list`)
| # | Item | Cost |
|---|------|------|
| 1 | A danish pastry | 7 |
| 2 | A bread | 14 |
| 3 | A waybread | 73 |
All unlimited stock. Shop commands: `list`, `buy <item>`.

## Gameplay gotchas learned
- Login flow: name → password → PRESS RETURN → menu → `1` to enter. If already connected, server says "Reconnecting." and drops straight into the game (no menu — sending `1` gives "Huh!?!").
- Character position **persists across sessions** — always `look` first, never assume you start at the Temple.
- If you send a wrong name at the login prompt, the server starts new-character creation ("Did I get that right, X (Y/N)?") — answer `no` to back out.
- Blind timed command scripts desync easily; drive interaction off actual server output.
