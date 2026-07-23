# Warrior (Dummy) — Player State

- **Name/Title:** Dummy the Recruit (level 2)
- **Location:** The Common Square (south of Market Square, south of Temple Square, south of Temple of Midgaard)
- **HP/Mana/Move:** 38/38 H, 100/100 M, 86/86 V (full, no rest needed)
- **AC:** 39/10, Alignment: 201
- **Exp:** 3276 (724 to next level)
- **Gold:** 65 coins
- **Quest points:** 0 (0 quests completed, not on a quest)
- **Status:** standing, hungry, thirsty
- **Age:** 17
- **Inventory:** a piece of meat (looted from beastly fido corpse; unequipped, hunger relief)

## Goal Progress
- Goal 1 (prior): return to starting temple (Temple of Midgaard spawn room). Result: SUCCESS.
- Goal 2: team up with the magician (Smarty) and kill "beastly fido". Result: SUCCESS (2026-07-23).
  - Found beastly fido at The Common Square (route: Temple -> d -> Temple Square -> s -> Market Square -> s -> Common Square).
  - `consider fido` reported "Fairly easy" before engaging.
  - First engagement: script disconnected between batches mid-fight; character appears to have auto-fled while link-dead, landing in Dark Alley (east of Common Square) at full HP with no damage taken. No death occurred.
  - Returned west to Common Square; fido was still/again there; re-engaged with `kill fido`, stunned it, kept attacking within a single connection this time — fido died.
  - Looted corpse: 10 gold coins + a piece of meat. Gold 55 -> 65. Exp 3204 -> 3276 (+72).
  - Smarty (magician) was present in the room during the hunt (seen "linkless"/"has lost her link"/"has arrived" — appeared to be working the same fight from her own session) but no confirmed kill-blow attribution to her; warrior landed the finishing blows.
- Lesson: keep multi-round combat within a single script invocation/connection when possible — reconnecting mid-fight can trigger auto-flee (character survived fine here, but it wastes a round and repositions you).

## Notes
- Room exits from Temple of Midgaard (south end of hall): n, e, s, w, d
  - West: Reading Room
  - East: donation room (small alcove)
  - An ATM (automatic teller machine) is installed in the wall here.
- Character is hungry/thirsty — may want food/drink soon (now carrying a piece of meat to help with hunger).
