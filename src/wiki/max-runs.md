# Maxing a run

A plan built on the numbers in this wiki and on what the leaderboard's top runs actually do. The goal is the most kills, which in Megabonk means surviving long in final swarms at high difficulty.

## 0. What 500k+ leaderboard runs do

From the 477 verified **Forest** runs with 500,000+ kills on [Leaderboard.gg](https://megabonk.leaderboard.gg/) (synced by [megabonk.org](https://megabonk.org/leaderboard/), patch 1.0.65, Nov 16, 2026). Graveyard runs are covered separately at the end of this section, because its Bald Heads push stats far past what Forest allows. See the [Tier lists](tiers.html) for the full breakdown.

- **They're long.** The median Forest 500k+ run lasts about **95 minutes** and reaches **level 2,008**. The Forest record is 2,011,436 kills.
- **Characters:** Dicehead (32%) and Fox (32%) are almost two thirds of them, and Dicehead has 25 of the 31 Forest runs past 1M.
- **Weapons:** Katana is in 94%, then Shotgun 52%, Dexecutioner 49%, Dice 37% and Firestaff 32%. Past 1M, 27 of 31 runs use only 2 weapons (see the [FAQ](faq.html)).
- **Tomes:** Chaos 99%, XP 98%, Cursed 97%, then Damage and Luck (about half each).
- **Items every top run has:** Overpowered Lamp, Spicy Meatball, Anvil, Beefy Ring, Giant Fork, Big Bonk, Lightning Orb, Key, Time Bracelet, Wizard's Hat and Credit Card (Green). These are each in 95–100% of them.
- **Za Warudo is the exception.** It shows up in only 1% of these runs, but that is because the leaderboard records the inventory at the end of the run, and each Za Warudo breaks when it saves you. Top runs stack many copies and spend them: in five recorded 1.1M–5.4M runs they held 3 to 21 at a time (the 2.998M Fox record had 21 at 86 minutes, 11 at 6½ hours). One 1.2M run went from 8 copies to none in its last 12 minutes, then died. The 1.1M and 999k end screens show none left.
- **Items they leave out:** Snek 2%, Forbidden Juice 4%, Battery 10%, Dragonfire 15% and Bob's Light 24%. Energy Core, Gas Mask and Gamer Goggles are in almost none. Top players toggle these out of the pool, so chests land on the core items instead.
- **Wizard's Hat stacks into the thousands.** In the long video runs it reached ×360 at 3.8 hours and ×1,264 at 7.3 hours (5.4M Dicehead), and about ×5,950 in the 2.998M Fox run. Each copy past the ninth adds +2 to the tome level cap, which is how those runs had tomes at levels 400–600. The copies come from chests that drop from kills (see [Chests from kills](economy.html#chests-from-kills)): over hours of swarm kills that is thousands of chests. With Luck in the thousands nearly every chest is Legendary, and the other Legendaries are capped (Anvil 1, Overpowered Lamp 2, Joe's Dagger 10, Za Warudo 25 a run) or out of the pool, so Wizard's Hat is what keeps coming.

### Graveyard runs

Graveyard is a single 16-minute stage with twice the shrine slots (28), and any of them can be a **Bald Head** (Balance Shrine): each doubles one stat and halves another, and the doublings stack. The 5.4M run had Powerup boost (shown in-game as Powerup Multiplier) at ×409.6. That's why the records are there:

- **20 runs at 500k+, 13 of them past 1M.** The median one has 1.93M kills, lasts 355 minutes and reaches level 5,405. Every run above the Forest record is on Graveyard, including Tony McZoom's three at the 16,777,216 cap (2²⁴: run stats are stored as floats, and that's the largest whole number a float counts exactly).
- **Two weapons, Shotgun second** in 11 of the 13 runs past 1M. Chaos and Luck tomes are in all 13.
- **Different items:** Wizard's Hat, Overpowered Lamp, Anvil, Spicy Meatball, Credit Card (Green) and Beefy Ring are in all of them, but Pot is in only 15%, Lightning Orb 35% and Big Bonk 50%. Bob's Light (80%) and Ice Cube (95%) are far more common than on Forest.

The [Tier lists](tiers.html#graveyard-runs) have the full Graveyard breakdown.

**About versions:** the leaderboard is on patch 1.0.65, and this wiki's code reading is 1.0.69. Sections 4–5b below describe how the 1.0.69 final swarm works. Top runs clearly survive far past the 12-minute wall described there, so treat those sections as how the swarm escalates, not as a hard limit.

## 1. Before the run

- **Toggle the item pool down** to what you'll use (needs the Toggler from the Silver shop). A rarity with everything toggled off drops out of the chest roll entirely, and every chest lands on your short list. During the run, **Banish** removes more ([Banish, Refresh and Skip](economy.html#banish-refresh-and-skip)).
- **Seed scanning:** a Legendary Microwave appears on about 1 Forest stage in 27 (2.5% per Microwave, 1 or 2 per stage), or about 1 Graveyard map in 7 (4, 6 or 8 Microwaves). Bald Heads are 1 in 6 per shrine slot, so 10+ on one Graveyard map is a seed worth keeping. A Legendary Shady Guy is 6.7% per vendor, and its prices are lowest on stage 1 before you open chests (≈ 30 × 8 = 240 gold before any chests). Neither is affected by Luck, so it's pure rerolling.

## 2. Stage 1, 0:00–10:00: build the engine

- **Break every pot.** Each gives +0.5% Luck on stage 1 (big pots +0.75%), permanently: 40 small and 15 big pots make **+31% Luck** from a full stage-1 map. (Graveyard has pumpkins instead of pots.)
- **Tomes:** what top runs take is Chaos, XP and Cursed, plus Damage or Luck (see [Tomes](tomes.html#picking-four)).
- **Chests:** open the first 5–8 straight away (≤ 430 gold each) for early power. Then **hold the rest until Luck is about 100–150%**. A chest's price depends only on how many you've opened, not on time, while Legendary odds go from 1.6% (Luck 0) to 4.7% (100%) and 6–7% (150%). The jump after chest 10 (569 → 952 gold) is the natural place to start being picky.
- **Scripted danger:** the first miniboss at 3:00 (spawns slow to 25% while it's alive); a 30-second swarm at 4:00; another swarm at 7:00; a miniboss at 8:00. Be at full HP and in open ground before 3:00 and 4:00. Most recorded deaths happened between 3:24 and 4:24.

## 2b. Chest volume and Luck: how big runs get 10+ copies

Top leaderboard runs stack the same core items over and over. The leaderboard lists which items a run had, not how many copies, but the code shows why stacking the core pays off:

- **Overpowered Lamp** makes every hit run all your on-hit items once more per Lamp (max 2). That's 3 rolls of everything per hit.
- **Big Bonk at 10 copies:** 2% + 1.5% × 9 = **15.5%** chance per hit (× proc coefficient) to deal **110×** the hit's damage (20× + 10× per extra copy). With 2 Lamps that's three tries per hit.
- **Wizard's Hat and Anvil** raise tome levels and weapon upgrades, which matter more the longer the run goes.

Getting there is a numbers game, and two things decide it:

**1. Open as many chests as you can.** Every chest is a roll, and a chest's price depends only on how many you've opened, not on time. More gold means more rolls.

**2. Max your Luck.** It decides how many of those rolls come up Legendary:

| Luck | Legendary chance per chest | Chests per Legendary (average) |
|---|---|---|
| 0% | 1.6% | 63 |
| 100% | 4.7% | 21 |
| 200% | 8.4% | 12 |
| 300% | 12.1% | 8 |
| 500% | 19.0% | 5 |

At 300% Luck a Legendary comes about every 8 chests; at 0% it's one in 63.

**Then narrow the pool.** This is what top runs do: Bob's Light, Dragonfire, Battery, Snek and others are almost never in a 500k+ run. Keep Za Warudo on: it is a Legendary worth stacking. A Legendary chest picks one of the Legendaries still in your pool. With all 21 droppable Legendaries enabled, 10 copies of Big Bonk takes about 210 Legendary rolls. Toggled down to 3, it takes about 30. Shady Guys add more rolls, and a Microwave clones an item you already have.

## 2c. Five ways to bend the system

**1. Powerup Drop Chance = more free chests.** It multiplies every kill's chance to drop a free chest ([Chests from kills](economy.html#chests-from-kills)). Take it from Charge Shrines, and double it at Bald Heads on Graveyard. Note that powerups themselves stop dropping once a final swarm starts; chests from kills don't.

> **Example:** at 300 kills a second, a free chest drops about every 53 s at ×1 Powerup Drop Chance, every 17 s at ×10 and every 5 s at ×100.

**2. Max Luck until nearly every chest is Legendary.** Luck has diminishing returns, but it never stops helping:

| Luck | 100% | 300% | 1,000% | 3,000% | 10,000% | 40,000% |
|---|---|---|---|---|---|---|
| Legendary chests | 4.7% | 12% | 33% | 58% | 78% | 90% |

Combined with a narrow Legendary pool (toggles and Banish), late chests land on the few Legendaries you want.

**3. Fight from a ledge at the edge of the map.** *(Player technique.)* The map's edge is an invisible wall: nothing spawns or walks in from beyond it. Stand on a high ledge right at the boundary and the swarm can only come at you from the map side, in a cone, instead of from all 360°. Your attacks hit the whole pack at once, and dodging means watching one front instead of every direction. Extra jumps and jump height get you up onto those ledges. Flying ghosts still reach you, but from that same side.

**4. Bank a powerup for the exit.** Powerups have no despawn timer: one lying on the ground stays until you touch it (up to 50 on the map). Magnet only pulls XP, and Pickup Range doesn't pull powerups either (confirmed in-game), so it stays put. Since none drop during the final swarm, leave a **Time** powerup near your ledge or the portal during the stage. When the swarm gets too hot, grab it to freeze every enemy for **12 s × Powerup boost** (48 s at ×4) and walk to the portal.

**5. Stack Boss Curses for boss chests.** Every boss and miniboss drops a free chest when it dies (everywhere except the final-boss map). Each curse adds one miniboss to every miniboss event and one more stage boss:

| Curses | Forest/Desert stage 1 (2 miniboss events + boss) | Graveyard (4 miniboss events + boss) |
|---|---|---|
| 0 | 3 boss chests | 5 boss chests |
| 1 | 6 | 10 |
| 3 | 12 | 20 |
| 5 | 18 | 30 |

The cost: every boss also gets +16% HP per curse, and all of them have to die, so only stack curses when your build kills a miniboss in seconds (section 3).

## 3. Boss Curses: how many

Each curse, for the rest of that stage:

- +1 miniboss at every miniboss event (3:00 and 8:00 on stage 1),
- +1 stage boss,
- every boss ×(1 + 0.16 × curses) HP.

| Curses | Minibosses per event | Stage bosses | HP per boss | Total boss HP vs no curses |
|---|---|---|---|---|
| 0 | 1 | 1 | ×1.00 | ×1.0 |
| 1 | 2 | 2 | ×1.16 | ×2.3 |
| 2 | 3 | 3 | ×1.32 | ×4.0 |
| 3 | 4 | 4 | ×1.48 | ×5.9 |
| 5 | 6 | 6 | ×1.80 | ×10.8 |

Bosses ignore Bob's Light and executes, and Cursed Doll only does 0.7 × (8 + level) to them, so curses are a test of raw weapon damage. **Take curses after the 8:00 miniboss** if you want more stage bosses without doubling the 3:00 and 8:00 fights, and only when your weapons kill a miniboss in a few seconds. On stages 2 and 3, bosses also get ×2.5 and ×5 HP.

## 4. The final swarm: where the kills are

The final swarm starts at the stage boss kill or the timer, whichever comes first, so **killing the boss early starts the farm early**. Inside it:

- Enemies refill toward 400 (first 2 minutes) then 300, at a rate that rises with **Difficulty**: the spawn multiplier is 1 + 0.7 × Difficulty + 0.4 × stage. More Difficulty = faster refill = more kills per minute.
- Enemy HP gains +3 at 1 minute, +15 at 2, +63 at 3, +1,023 at 5. A weak build's damage stops keeping up within a few minutes; a strong one (crit past 200%, Big Bonk, Lightning Orb) keeps the full kill rate up to the 12:00 Red Ghost switch, as the 361k run below did.
- Two things keep killing regardless of HP:
  - **Bob's Light** instantly kills every non-boss in its radius (24% of Forest 500k+ runs keep it in the pool, 80% of Graveyard ones). Cooldown 45 − 3 per copy (5 s at 14 copies); radius 50 + 10 per copy (250 at 20 copies). With a full map of ghosts that's up to hundreds of kills per blast.
  - **Cursed Doll**: each copy keeps 2 enemies cursed, each losing 30% of max HP a second, so about 0.5 kills per second per Doll.

## 5. The ghost wall at 12–13 minutes

The swarm swaps its ghost type on a fixed clock: Greater Ghost at 1:00, **Purple Ghost at 6:00** (not executable, so Joe's Dagger and executes stop working), and **Red Ghost at 12:00**. Counting the short delay after the boss dies, that's roughly 13 minutes after the boss kill.

Red Ghosts are the wall:

- 100 base HP, speed 10 (×1.2 in the swarm = 12), knockback resistance 50, flying, not executable.
- **Bob's Light only kills a Red Ghost 33% of the time** (`KillEnemyTrigger.chanceToOneshotRedGhosts`).
- By 12 minutes enemy damage has gained +4,095: a Red Ghost (30 base damage) hits for about 135,000.

How to get past it:

1. **Cursed Doll count.** Dolls don't care about HP or the Red Ghost exception. Each Doll is about 0.5 kills a second; 30 Dolls ≈ 15 kills a second. Pick up Dolls throughout the run; they're Common and cheap.
2. **Bob's Light at the cap** (14 copies for 5 s). One blast in three still clears Red Ghosts. Most top runs skip it in favour of the core damage items.
3. **Don't get hit.** Shield and Armor (3 Armor blocks 80%) carry you through the first minute or two of Red Ghosts, but their damage doubles every minute. Past that, Evasion and freeze/stun lock are what keep a run alive. See 5b below.
4. **Or leave before 12:00.** Every stage resets the final-swarm clock to 0, so a new stage's swarm starts back at plain Ghosts. On stages 1–3, taking the portal before 12:00 of the swarm and farming the next stage's early swarm avoids the wall entirely, at the cost of the stage HP jump (about 15× from the end of stage 1 to the start of stage 2).

## 5b. Staying alive past 14 minutes

Swarm enemy damage doubles every minute: a Red Ghost hits for about 135,000 at swarm minute 12, 1 million at 15 and 35 million at 20. No HP or shield pool keeps up, so long swarm runs survive by **not getting hit**. The code expects this: three rules in `EnemyStats` only switch on far into a swarm.

| Swarm time | Rule (from the code) | What it means |
|---|---|---|
| 12:00 → | `GetMaxSpeed`: enemy speed cap rises from 90 by +6 per minute (max 250) | Enemies can be sped up further by speed effects late on |
| 20:00 → 50:00 | `GetCapCC`: each enemy can be frozen or stunned at most **15 times**; from 20:00 that limit falls steadily to **0 at 50:00** | Freeze and stun lock work fully until 20:00, fade out between 20 and 50 minutes, and stop working at 50:00 |
| 60:00 → | `GetEvasionAndArmorPenetration`: enemies start to ignore a small slice of your Armor and Evasion | Before 60:00, Evasion and Armor work at full strength |

Also, after any hit you get **0.15 seconds of invulnerability** (`MyPlayer.OnDamage`).

What that means for a build:

1. **Evasion is the defence that scales.** It ignores how big the hit is. Real dodge chance is E / (E + 1) × 0.999: Evasion 1 = 50%, 4 = 80%, 10 = 91%, 20 = 95%, 50 = 98%. The 361k run had 0.62 (38%). Stack Evasion Tome levels, Evasion offers and Evasion items.
2. **Lock the swarm down with freeze and stun** (Ice Cube, Frostwalker, freeze chance, stun items). Until 20:00 every enemy can be locked 15 times; after that each one gets fewer locks.
3. **Knockback and space.** Red Ghosts have knockback resistance 50, so plain knockback barely moves them; keep moving and keep the map thin instead.
4. **Kill what HP doesn't matter for.** Cursed Doll (30% max HP per second) and Bob's Light (1 in 3 on Red Ghosts) keep fewer ghosts in contact range.
5. **Stack Za Warudo.** Each copy blocks one fatal hit by freezing time, then breaks (up to 25 a run). Top runs pick up many and burn through them in the late swarms, which is why almost none still have one when the run ends.

    > **Example:** with 12 copies you can take 12 hits that would have killed you. Each one also freezes the swarm for a moment, so you get time to move out. The 13th fatal hit ends the run unless you have picked up more.
6. **Shield and HP still help early in the Red phase** (a 135k hit at 12:00 is survivable with a big shield), but they stop mattering a couple of minutes later.

How a hit that gets through is reduced (Armor, then other damage reduction) is on [Core math](mechanics.html#damage-you-take).

## 6. Moving between stages

Enemy HP jumps about 15× between the end of stage 1 and the start of stage 2, and about 5× again into stage 3, on top of +10% per run minute. Leave a stage when your damage can take that jump: more Damage Tome levels, Pot and Wizard's Hat level caps, and crit chance past 100% (2 crits = ×4, 3 = ×6.25) are the multipliers that keep up.

## 7. What a 361,000-kill run showed

A recorded Dicehead run on Forest Tier 3 (Nov 16, 2026): 361,487 kills in 64:22, level 1,497, died on the final-boss map. The recorder started at 23:16, so the first stage and a half are missing.

| Final swarm | Ghost phase | Kills per minute |
|---|---|---|
| Stage 3, swarm 0–1 min | Ghost | ~11,700 |
| Stage 3, swarm 1–12 min | Greater, then Purple | 11,300–11,500, steady |
| Stage 3, swarm 12 min | **Red** | **4,800** → left for the final map |
| Final map, swarm 0–12 min | Ghost → Greater → Purple | 11,100–14,500 |
| Final map, swarm 12 min + | **Red** | 7,500 → 4,000 → 1,500, then death at 64:22 |

What it confirms:

- **The ghost wall is real and exactly on the clock.** Kills held at ~11,500 a minute through Ghost, Greater and Purple phases, then fell by more than half the moment Red Ghosts took over, on both maps.
- **Leaving before the wall works.** The run left stage 3 right as Red Ghosts arrived and went on to farm another full 12 minutes on the final map.
- **~11,500 kills a minute looks like the ceiling** at this build's 1,040% Difficulty: the map stayed near the 300-enemy swarm cap and kills matched the refill rate. Total kills are close to *minutes spent in pre-Red swarms × 11,500*.
- **Death was the Red Ghost hit, not damage.** Shield was 68, Max HP 1,363, Armor 0.74 (50% reduction), Evasion 0.62 raw (38%). A Red Ghost at 12+ minutes hits for six figures, so one hit ends it. Survival past 12:00 needs far more evasion and damage, or not being there.
- **Big Bonk did 73% of all damage** (5 copies: 2% + 1.5% per extra copy, at 20× + 10× per extra copy). Lightning Orb, Spicy Meatball, Dragonfire and Grandma's Tonic followed. Cursed Doll (18 copies) was 6th.
- **No Bob's Light.** That's the item that keeps killing Red Ghosts (1 in 3) and everything around them.

**A safe plan for a build like this one:** farm each stage's final swarm until about 11:30 of swarm time, then take the portal before the Red switch. On Tier 3 that's up to four 12-minute farms (three stages plus the final map), about 48 minutes of swarm. At ~11,500 a minute that's roughly 550,000 kills before any Red Ghost phase.

**To go further,** build toward the leaderboard core in section 0: Overpowered Lamp, Big Bonk, Spicy Meatball, Giant Fork, Lightning Orb, Beefy Ring, Wizard's Hat and Anvil. Use Katana, Shotgun or Dexecutioner, and Chaos, XP and Cursed tomes. The top runs built this way last hours, not minutes.
