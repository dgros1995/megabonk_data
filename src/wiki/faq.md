# FAQ & map limits

Quick answers, each traced to the game's code and data.

## How many of each thing can a map have?

All of these come from the game files: the map generator's spawn lists (`RandomObjectPlacer`, `SpawnInteractables`) and each map's settings. Graveyard multiplies shrines by 2, chests by 1.5 and everything else by 1.5 (rounded).

| Thing | Forest / Desert, per stage | Graveyard | Notes |
|---|---|---|---|
| **Shrine slots** | **14** | **28** | Each slot picks one type at random, every type equally likely (below). |
| Chests | **46** × Chest amount stat | 69 | |
| Charge Shrines | 15 (+2 per Beacon on later stages) | 22 | |
| Greed Shrines | 8 | 12 | |
| Pots | 40 small + 15 big = 55 (+8 small and +2 big per Pumpkin on later stages) | none | |
| Silver pots | 6 small + 1 big | 12 small + 2 big | |
| Pumpkins | — | 75 small + 30 big = 105 | Breakable like pots. |
| Microwaves | 1 or 2 | 4, 6 or 8 | Graveyard rolls 3, 4 or 5, then × 1.5 and rounds to the nearest even number on a tie (4.5 → 4, 7.5 → 8), the same rounding that turns 22.5 Gravestones into 22. |
| Gravestones | — | 22 | |
| Crypt (inside the Graveyard) | — | 6 chests, 16–20 pots | Counted on scanned maps; the crypt's contents aren't in the map data. |

**Which shrine types can fill a slot:**

| Map | Shrine types (each equally likely) | Average per type |
|---|---|---|
| Forest, Desert | Shady Guy, Moai, Boss Curse, Magnet, Challenge | 2.8 of 14 |
| Graveyard | the same five + Bald Heads (Balance Shrine) | 4.7 of 28 |

- **Boss Curse shrines only appear once you've played more than 2 runs** (the code skips them while your run count is 2 or lower). Until then, the other types share the slots.
- **Bald Heads are not weighted.** They're one of six equally likely types, so an average Graveyard map has about 4–5. Maps with 10+ (like the record runs' 11 and 13) are the lucky end, which is what seed scanning looks for.
- **Since the slots are shared,** a map with many Shady Guys has fewer of everything else.

## What does Luck affect?

| Thing | Uses Luck? | How |
|---|---|---|
| Chest items | **Yes, full** | Chest rarity table in [Luck, chests & shrines](economy.html) |
| Level-up offers | **Yes, full** | Offer rarity table |
| Charge Shrine stat offers | **Yes, full** | Same function as level-up offers |
| Moai items | **Yes, full** | |
| Shady Guy vendor rarity | **No** | Rolled at map load with Luck 0: Common 53%, Rare 27%, Epic 13%, Legendary 7% |
| Shady Guy item rarity | **Yes, at half strength** | Each item slot rolls a chest rarity with **Luck × 0.5**, and keeps whichever is higher: that roll or the vendor's rarity. So a Common vendor can still show Rare, Epic or Legendary items when your Luck is high. |
| Microwave rarity | **No** | Rolled at map load: Common 75%, Rare 15%, Epic 7.5%, Legendary 2.5% |
| Balance Shrine (Bald Heads) | **No** | Its trades (one stat ×2, another ×0.5) don't read Luck |
| Greed Shrine, Boss Curse, Magnet, Challenge | **No** | |
| Pot drops | Not by Luck. Pots *give* Luck (+0.5% each on stage 1) | |

## Is it better to run 2, 3 or 4 weapon slots?

You start with **2 weapon slots** and **2 tome slots**. Each kind gets up to 2 more from the Weapon Slots and Tome Slots shop upgrades (unlocked at 25 and 45 quests for weapons, 35 and 55 for tomes). Bought slots stay until you refund them, so you can switch between 2, 3 and 4 between runs.

**What the code does with slots** (`InventoryUtility.GetRandomUpgrades`, `CanUnlockItem`): every level-up offer is drawn from one pool, made of the weapons and tomes you own plus new weapons and tomes. New ones are only offered while you have an empty slot of that kind. So:

- **Fewer weapon slots:** once they're full, no new weapons are offered. Your pool is smaller, so each weapon and tome you own comes up more often.
- **More weapon slots:** the pool is bigger, and early levels are spread across more weapons.

**For the very top runs, 2.** This is what the leaderboard shows (patch 1.0.65):

| Kills | Runs | 2 weapons | 3 weapons | 4 weapons |
|---|---|---|---|---|
| Under 500k | 239 | 9% | 5% | 85% |
| 500k–1M | 456 | 19% | 19% | 62% |
| 1M+ | 44 | 86% | 7% | 7% |
| 2M+ | 10 | 100% | — | — |

Four weapons wins the 500k range. Past 1M almost everyone runs two, and Shotgun is the second weapon in 8 of the top 10 runs. It isn't a Graveyard effect: on Forest alone, 27 of the 31 runs past 1M use 2 weapons.

**Why 2 wins the longest runs:**

- **Weapons don't really max out.** The base cap is level 40, but each Pot (Stainless Steel) raises it (+10, +9, +8 … down to +2 per copy). Top runs stack Pots, so the cap keeps rising and every weapon offer is still worth taking.

    > **Example:** the 1.1M Dicehead run had 18 Pots. That's +10 +9 +8 +7 +6 +5 +4 +3 +2 for the first nine, then +2 for each of the other nine: +72, for a cap of 112. Its two weapons ended at levels 111 and 112.

- **Two weapons get every upgrade.** Weapon offers are split between the weapons you own. With 4 weapons, each one gets about half the levels it would get with 2, so the two that do the work fall behind.
- **A smaller offer pool.** Each level-up draws from the weapons and tomes you own. Fewer weapons means the offers land on your main weapon and your key tomes more often.

**When 4 is better:** runs up to about 1M kills. There, 4 weapons give more hits and more on-hit rolls, and the run ends before 2 fully-fed weapons pull ahead. The [Weapons](weapons.html) page ranks every weapon by proc rolls per second.

**Tome slots:** half of the 2M+ runs use only 3 tomes, for the same reason. Below 1M, almost every run uses 4.


## Other common questions

**What's the highest kill count possible?** 16,777,216. The top three leaderboard runs all stop at exactly that number. The game keeps run stats, kills included, as 32-bit floats (`RunStats` stores a `Dictionary<string, float>`), and 16,777,216 = 2²⁴ is the largest whole number a float counts exactly. Past it, adding 1 kill doesn't change the number, so the counter stops there.

**Does a chest get more expensive if I wait?** No. The price depends only on how many chests you've opened this run.

**Do Boss Curses carry over to the next stage?** No. The counter lives on each stage's game manager.

**Is the final swarm different on each map?** No. Every map's final swarm uses the same ghosts on the same clock: Ghost, Greater Ghost at 1:00, Purple at 6:00, Red at 12:00.

**Does leaving a stage reset the final swarm?** Yes. The final-swarm clock resets every stage, so the next stage's swarm starts with plain Ghosts again. The run clock (+10% enemy HP per minute) does not reset.

**What's the most enemies that can be on the map?** 550 normally; 400 for the first 2 minutes of a final swarm, then 300.

**Does Difficulty make enemies tougher, or just more of them?** Both. It adds 1.1 × Difficulty to enemy HP, 1 × Difficulty to their damage, and 0.7 × Difficulty to the spawn multiplier.

**How many stages does each tier have?** Tier 1: one, Tier 2: two, Tier 3: three, then the final-boss map. Graveyard is a single 16-minute stage.

**Can Bob's Light or executes kill bosses?** No. Bob's Light skips bosses; executes deal 2% of a boss's max HP.
