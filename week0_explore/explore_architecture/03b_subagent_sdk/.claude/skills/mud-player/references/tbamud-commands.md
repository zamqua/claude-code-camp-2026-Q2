# tbaMUD / CircleMUD command vocabulary

Standard DikuMUD-family commands. Not exhaustive — the game accepts many
more (type `help` or `commands` in-game for the full list) — but this
covers what you'll need for most goals without spending a command batch
just to look it up.

## Movement
`north`/`n`, `south`/`s`, `east`/`e`, `west`/`w`, `up`/`u`, `down`/`d`.
Exits for the current room are listed in the room description, e.g.
`[ Exits: n e s w ]`.

## Observation
- `look` (`l`) — redescribe the current room.
- `look <thing>` / `examine <thing>` — inspect an object, NPC, or exit in
  more detail.
- `score` (`sc`) — HP/mana/move, level, exp, gold, alignment, hunger/thirst.
- `inventory` (`i`) — items carried.
- `equipment` (`eq`) — items worn/wielded.
- `who` — players currently online.

## Items
- `get <item>` / `get <item> <container>` — pick up.
- `drop <item>` — drop.
- `wear <item>` — put on armor/clothing.
- `wield <item>` — ready a weapon.
- `remove <item>` — take off worn/wielded gear.
- `give <item> <person>` — hand off an item.

## Shops
- `list` — see what a shopkeeper sells (must be in a shop room).
- `buy <item>` — purchase.
- `sell <item>` — sell.
- `value <item>` — check what a shop would pay for an item.

## Combat
- `kill <target>` (`k`) — initiate combat.
- `flee` — attempt to escape combat.
- `consider <target>` — gauge how dangerous a target is before engaging.
- Combat is real-time (server "pulses"); expect several rounds of
  automatic output after `kill` before the prompt settles — this is why
  the client script waits for an idle gap rather than a fixed delay.

## Communication
- `say <message>` — speak to the current room.
- `tell <person> <message>` — private message.
- `emote <action>` — perform a visible action.

## Session
- `save` — force-save character state (state also saves periodically and
  on disconnect).
- `quit` — log out to the character menu. Only send this when the
  player's goal for the session is actually done — see
  `connection-notes.md` for why the script doesn't send it automatically.

## Useful checks before acting
- `consider <target>` before `kill`ing something unfamiliar.
- `look` after any move to confirm the room and update `data/world.md`.
- `score` periodically to catch low HP or hunger/thirst before it becomes
  an emergency.
