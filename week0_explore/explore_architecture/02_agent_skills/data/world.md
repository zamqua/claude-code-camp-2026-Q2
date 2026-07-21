# World map

Last updated: 2026-07-20 (confirmed guild of swordsmen location and practice yard)

## Rooms

### The Bakery
- Description: small bakery, smells of danish and bread; goods arranged on
  shelves; a small sign on the counter; a baker NPC present.
- Exits: s -> Main Street
- Shop menu (`list`, confirmed 2026-07-15):
  1) A danish pastry — 7 gold (unlimited stock)
  2) A bread — 14 gold (unlimited stock)
  3) A waybread — 73 gold (unlimited stock)

### Main Street
- Description: main street through the City of Midgaard.
- Exits: n -> The Bakery, e -> Market Square, s -> (Armory, per room text —
  not yet visited), w -> (not yet visited)
- Notes: room text explicitly calls out "south of here is the entrance to
  the Armory".

### Market Square
- Description: famous Square of Midgaard; large peculiar statue in the
  middle; roads lead every direction. The Mayor NPC seen here.
- Exits: n -> Temple Square, e -> Main Street (general store/pet shop
  branch, leads toward the Guild of Swordsmen — see below), s -> Common
  Square, w -> Main Street (first room, near the Bakery)

### The Armory (south of Main Street)
- Shop selling armor/helmets/shields; armorer NPC. Dead end — exit n only.

### Main Street (west end, past the first Main Street room)
- Description: "end of the main street of Midgaard" — south is the entrance
  to the Guild of Magic Users, magic shop to the north, city gate to the
  west, street continues east to market square.
- Exits: n (magic shop, unvisited), e -> Main Street (first room),
  s -> The Entrance To The Mages' Guild, w (city gate, unvisited)
- Notes: roaming fidos present; no trouble here.

### ✅ The Entrance To The Mages' Guild — the magician/magic-user guild
Route from Market Square: `w, w, s` (Main Street -> Main Street west end ->
guild entrance).
- Description: "a small, poor lighted room" — the guild's entrance hall.
- Exits: n -> Main Street (west end), s (unexplored — presumably deeper
  into the guild, not yet visited)
- NPCs: a sorcerer guarding the entrance, plus a Peacekeeper; an ATM is
  here too. Neither NPC was hostile just visiting. Confirmed 2026-07-15 —
  wrong guild for this character (a Swordsmen/warrior), but this is where
  a magic-user class would come to practice spells.

### The Temple Square
- Description: marble steps up to the temple gate; Clerics' Guild to the
  west (unvisited — wrong guild); Grunting Boar Inn to the east
  (unvisited); market square to the south.
- Exits: n -> Temple Of Midgaard, e (Grunting Boar Inn, unvisited),
  s -> Market Square, w (Clerics' Guild, unvisited)

### The Temple Of Midgaard
- Description: temple hall; Reading Room to the west, donation room to the
  east; an ATM ("automatic teller machine") is here.
- Exits: n, e, s -> Temple Square, w, d (none explored further)

### The Common Square
- Description: "nasty smell" from the south (likely sewers); poor alley to
  the west, dark alley to the east.
- Exits: n -> Market Square, e -> Dark Alley (DANGEROUS, see below),
  s (unexplored, "nasty smell"), w -> Poor Alley
- Notes: an oozing green gelatinous blob and beastly fidos loiter here;
  none were aggressive when just passing through.

### The Eastern End Of Poor Alley
- Grubby Inn to the south (unvisited); alley continues west.
- Exits: e -> Common Square, s (Grubby Inn, unvisited), w -> Poor Alley

### Poor Alley (west end)
- Dead end at the city wall. A beggar NPC, loose gold, and a "key made of
  a dull metal" were lying on the ground here (not picked up — out of
  scope for the goal being pursued).
- Exits: e -> Eastern End Of Poor Alley, w (city wall, dead end)

### The Dark Alley — ⚠⚠ CONFIRMED HOSTILE, avoid entirely for now
- Description: common square to the west; **Guild of Thieves to the south**
  (found a guild here, but wrong class); alley continues east to "The Dark
  Alley At The Levee".
- Exits: e -> The Dark Alley At The Levee, s (Guild of Thieves, unvisited),
  w -> Common Square
- Incident (2026-07-15), confirmed twice from both entrances (from Common
  Square side, and again from the Levee side): entering this specific room
  triggers an unprompted attack — a mercenary NPC exclaims "Hey! You're
  the fiend that attacked me!!!" and attacks; on the Common Square-side
  entry a Peacekeeper also joined in. This looks like a persistent
  hostile/faction flag tied to the character (not something re-triggered
  by player action each time — happened immediately on room entry both
  times) rather than a one-off random event.
  - Cost: 25->15 HP the first time, then re-entering from the other side
    cost 19->15 HP more and **cost 70 exp** (328->258, confirmed via
    `score` — this is a real setback, not just HP). A `flee` attempt
    inside the room failed silently once (stayed in room, combat
    continued) before a second `flee` succeeded and landed at "The
    Eastern End Of The Alley".
  - **Do not enter this room again without the player's explicit OK** —
    the hostility appears tied to the character itself, so it will likely
    recur every time, and it costs real exp on top of HP.

### The Dark Alley At The Levee
- Description: alley continues east/west; levee to the south.
- Exits: e -> The Eastern End Of The Alley (confirmed), s -> The Levee,
  w -> The Dark Alley (hostile, see above — confirmed by walking it)
- Notes: a Peacekeeper stands here but did NOT attack — the hostility
  is scoped to The Dark Alley room specifically, not this one. Safe.

### The Levee
- Description: river flows west; low bank, river enterable; a retired
  captain here selling boats. `south` requires owning a boat ("You need
  a boat to go there.") — not pursued, unlikely to lead to a guild and
  we only have 5 gold.
- Exits: n -> The Dark Alley At The Levee, s (boat-gated, unexplored)

### The Eastern End Of The Alley
- Description: city wall blocks further movement east; a small warehouse
  is directly south (dead end — see The Deserted Warehouse below).
- Exits: s -> The Deserted Warehouse, w -> The Dark Alley At The Levee
  (safe, confirmed)
- Notes: no hostiles present; safe to rest here.

### The Deserted Warehouse
- Description: old ship items; a sailor NPC ("waiting to help you") and a
  harmless joke mob ("An odif yltsaeb", a backwards-fido). No guild, no
  hostility. Dead end.
- Exits: n -> The Eastern End Of The Alley

## ⚠ Structural finding: the Levee/alley pocket is a dead end
The Dark Alley At The Levee / The Levee / The Eastern End Of The Alley /
The Deserted Warehouse form a small cluster with **no exit back to the
rest of Midgaard except through the hostile Dark Alley** (its `w` exit to
Common Square). There is no way to reach the city gate, east Market
Square, or anywhere else from this pocket without walking back through
the room that has twice attacked this character and cost exp. Confirm
with the player before paying that cost again, or consider whether
fighting it out (rather than fleeing) is preferable once HP is fuller.

### Market Square east branch: Main Street (general store / pet shop)
- Description: general store to the north, Pet Shop to the south, main
  street continues east/west.
- Exits: n (general store, unvisited), e -> Main Street (Guild of
  Swordsmen branch, below), s (Pet Shop, unvisited), w -> Market Square

### Main Street (east end — Guild of Swordsmen branch)
- Description: weapon shop to the north, **Guild of Swordsmen to the
  south**, town exit to the east (leaves Midgaard), market square to the
  west.
- Exits: n (weapon shop, unvisited), e (leaves town, unvisited),
  s -> The Entrance Hall To The Guild Of Swordsmen, w -> Main Street
  (general store/pet shop branch)
- Notes: a cityguard and roaming fidos here; no trouble.

### ✅ The Guild of Swordsmen — THE correct guild for this character
Route from Market Square: `e, e, s` (Main Street -> Main Street -> Guild
entrance), then `e, s` again to reach the actual practice room.
- **The Entrance Hall To The Guild Of Swordsmen**: ATM machine, a knight
  guarding the entrance, bar to the east, main street to the north.
  `practice` does NOT work here ("You can only practice skills in your
  guild.") despite the name — this room doesn't count.
  - Exits: n -> Main Street, e -> The Bar Of Swordsmen
- **The Bar Of Swordsmen**: trashed furniture, a bulletin board, a waiter
  NPC. Yard to the south, entrance hall to the west.
  - Exits: s -> The Tournament And Practice Yard, w -> Entrance Hall
- **The Tournament And Practice Yard**: THE actual practice room —
  "Your guildmaster is standing here sharpening an axe." A well leads
  down (unexplored). This is where `practice kick` must be run.
  - Exits: n -> Bar Of Swordsmen, d (well, unexplored)
  - Confirmed 2026-07-15: `practice kick` here returns "You do not seem
    to be able to practice now." — blocked by 0 practice sessions
    (same root cause found via the `practice` command at the very start
    of the session), NOT a wrong-location issue. Sessions are gained by
    leveling up; nothing to do here until the character levels.

## Unvisited but referenced
- Clerics' Guild (west of Temple Square) — wrong guild
- Guild of Thieves (south of Dark Alley) — wrong guild
- Grunting Boar Inn (east of Temple Square)
- Grubby Inn (south of Eastern End Of Poor Alley)
- Magic shop (north of west Main Street)
- City gate (west of west Main Street)
- General store / Pet Shop / weapon shop (Market Square east branch)
- Town exit east of the Guild of Swordsmen branch (leaves Midgaard)
- Well down from The Tournament And Practice Yard

## Note on "The Dark Alley" hostility (revised)
Earlier notes flagged this room as having a persistent hostile flag after
two attacks. A third pass through it later in the same session (both
directions) produced **no attack at all** — HP/exp were unaffected. This
looks like a random/occasional aggro event rather than a permanent flag.
Still worth being cautious there, but it is not a guaranteed-hostile
choke point.

## General notes
- Starting room on character creation/first login was The Bakery.
- On reconnect (socket closed without `quit`), the character resumes
  exactly where left off, in whatever room it last stood in.
