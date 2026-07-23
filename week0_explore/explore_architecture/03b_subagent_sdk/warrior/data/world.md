# Warrior — World Map / Knowledge

## Temple Of Midgaard (spawn/starting room)
- Description: southern end of the temple hall; giant marble blocks, ancient wall paintings of Gods, giants, peasants. Large steps lead down through the grand temple gate to the temple square below.
- Exits: n, e, s, w, d
  - West -> Reading Room
  - East -> donation room (small alcove)
  - Down -> Temple Square
  - (n, s not yet explored)
- Features: automatic teller machine (ATM) installed in the wall here.
- This is the character's login/spawn point — reconnecting via mud_client.py drops the character here (or wherever they last logged out).

## Other known rooms

### Temple Square (down from Temple Of Midgaard)
- Description: temple square; fountain; huge marble steps lead up to temple gate.
- Exits: n e s w
  - Up -> Temple Of Midgaard
  - West -> Clerics' Guild entrance
  - East -> old Grunting Boar Inn
  - South -> Market Square
- NPCs seen: cityguard, an oozing green gelatinous blob (wanders).

### Market Square (south of Temple Square)
- Description: "the famous Square of Midgaard"; large peculiar statue in the middle. Roads lead in every direction.
- Exits: n e s w
  - North -> Temple Square
  - South -> Common Square
  - East/West -> main street (not yet explored)
- NPCs seen: a Peacekeeper, green gelatinous blob (wanders through).

### The Common Square (south of Market Square)
- Description: common square with people passing; nasty smell from the south.
- Exits: n e s w
  - North -> Market Square
  - West -> poor alley (not yet explored)
  - East -> Dark Alley
  - South -> (nasty smell, not yet explored — possibly sewer/slum area)
- NPCs/mobs seen: cityguard, a Peacekeeper.
- **"beastly fido" spawns here** — mucking through the garbage. Considered "Fairly easy" for a level 2 warrior. Killed here 2026-07-23; drops a corpse with a small pile of gold coins (10) and a piece of meat.

### Dark Alley (east of Common Square)
- Description: dark alley; Guild of Thieves to the south; alley continues east.
- Exits: e s w
  - West -> Common Square
  - South -> Guild of Thieves
  - East -> (not yet explored)
- NPCs seen: a mercenary (waiting for a job).

## Session notes
- Reconnecting via mud_client.py mid-combat (across separate script invocations) appears to trigger an auto-flee while link-dead — character was moved from Common Square to the adjacent Dark Alley at full HP with no damage. Prefer completing a fight within one script invocation/connection rather than splitting it across multiple `printf | python3 mud_client.py` calls.
