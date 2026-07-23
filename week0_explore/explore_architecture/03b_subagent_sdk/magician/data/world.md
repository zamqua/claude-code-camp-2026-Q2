# World Map — Magician's Knowledge

## The Temple Of Midgaard (starting/spawn room)
- Description: southern end of the temple hall; giant marble blocks,
  ancient wall paintings of Gods, giants, peasants. Large steps lead
  down through the grand temple gate to the temple square below.
- Exits: n, e, s, w, d (down)
  - w -> Reading Room
  - e -> donation room (small alcove)
  - d -> descends toward temple square (via steps)
  - s -> Temple Square (confirmed)
- Features: automatic teller machine (ATM) in the wall.
- This is the character's login/spawn point.

## Temple Square
- South of Temple Of Midgaard.
- Description: marble steps up to temple gate; Clerics' Guild to the
  west; old Grunting Boar Inn to the east; market square just south.
  A large fountain is here.
- Exits: n (-> Temple Of Midgaard), e, s (-> Market Square), w (-> Clerics' Guild)
- Watch for: "An oozing green gelatinous blob" seen sucking debris here
  (not considered/engaged — unclear danger).

## Market Square
- South of Temple Square.
- Description: famous Square of Midgaard, large statue in the middle;
  roads lead every direction; north to temple square, south to common
  square, east/west main street.
- Exits: n (-> Temple Square), e, s (-> Common Square), w
- A Peacekeeper NPC patrols here (jumps in at first sign of trouble —
  avoid starting fights in this room).

## The Common Square
- South of Market Square.
- Description: common square, people passing; poor alley to the west,
  dark alley to the east; nasty smell from the south (-> The Dump).
- Exits: n (-> Market Square), e (dark alley), s (-> The Dump), w (poor alley)
- Notable: **"beastly fido" mob spawns/wanders here** — killed here
  2026-07-23 by the warrior (Dummy) before the magician arrived;
  corpse yielded gold + a piece of meat (looted by warrior, corpse now
  empty).
- Danger: a **cityguard** stands here — `consider` returns "Are you
  mad!?" (extremely dangerous, do not provoke). A Peacekeeper also
  passes through.

## The Dump
- South of The Common Square.
- Description: garbage dump; large junction of pipes visible, entrance
  to the sewer system.
- Exits: n (-> Common Square), d (-> sewer system, unexplored)

## Main Street (east segment)
- West of Market Square.
- Description: main street through the City of Midgaard; Armory to the
  south, bakery to the north; market square to the east.
- Exits: n (-> bakery), e (-> Market Square), s (-> Armory), w

## Main Street (west end)
- West of the above Main Street segment.
- Description: end of the main street; magic shop to the north; city
  gate to the west; street continues east.
- Exits: n (-> magic shop), e (-> Main Street east segment),
  s (-> Guild of Magic Users entrance), w (-> city gate)
- Notable: a "beastly fido" (respawn) seen mucking through garbage
  here 2026-07-23.

## The Entrance To The Mages' Guild
- South of Main Street (west end).
- Description: small, poorly lit entrance hall.
- Exits: n (-> Main Street west end), s (-> The Mages' Bar)
- Features: automatic teller machine (ATM) in the wall.
- A sorcerer guards the entrance (not engaged/considered).

## The Mages' Bar
- South of The Entrance To The Mages' Guild.
- Description: mystical bar; illusions of fine furniture, floating
  images.
- Exits: n (-> guild entrance), e (-> Mages' Laboratory)
- Features: bulletin board. A "waiter" NPC present.
- Practicing does NOT work here ("You can only practice skills in
  your guild") despite being inside the guild building.

## The Mages' Laboratory
- East of The Mages' Bar.
- Description: magical experiments lab; oaken tables with pipes/
  flasks, pentagrams on the floor, a blackboard.
- Exits: w (-> Mages' Bar)
- **This is the guildmaster/practice room** — "Your guildmaster is
  studying a spellbook..." — `practice <spell>` (no quotes around the
  spell name) works here. Command syntax that failed: quoted
  `practice 'magic missile'` -> "You do not know of that spell."
  Correct syntax: `practice magic missile` (no quotes).

## Notes
- Magic missile practice attempted at Temple Of Midgaard ->
  "You can only practice skills in your guild." Mage guild location
  found 2026-07-23: reached via Temple -> s -> Temple Square -> s ->
  Market Square -> w -> Main Street (east) -> w -> Main Street (west
  end) -> s -> Guild Entrance -> s -> Mages' Bar -> e -> Mages'
  Laboratory (practice here).
- Practice progression seen: not learned -> average -> superb (superb
  appears to be the max for a level-1 spell); 3 practice sessions
  consumed magic missile from 0 to max, 1 session left unspent (no
  other known spells yet).
