# Luck, chests & shrines

## How Luck works

Every rarity roll that uses Luck goes through the same function (`Rarity.CalculateRarityWeights`):

**weight of a rarity × 1.5^(−steps below the top rarity × 1.5 × ln(1 + Luck))**, then normalised.

In plain terms each step down in rarity is scaled by (1 + Luck)^−0.61. That's about ×1.5 at Luck 100%, ×1.9 at 200% and ×2.3 at 300%. Luck keeps helping but with diminishing returns.

> **Example:** at 0% Luck a chest comes up Legendary 1.6% of the time. At 100% Luck it's 4.7%, about three times as often. Going to 200% only gets you to 8.4%: each extra 100% helps, but a little less than the one before.


Luck is used for **chest items, level-up offers, Moai offers and stat-shrine offers.** It is **not** used for Shady Guy or Microwave rarity: those are rolled at map load with Luck 0.

### Chest item rarity

Base weights: Common 70, Rare 15, Epic 6, Legendary 1.5 (`Rarity.GetItemRarity`). A rarity with every item toggled off is skipped completely.

| Luck | Common | Rare | Epic | Legendary |
|---|---|---|---|---|
| 0% | 75.7% | 16.2% | 6.5% | 1.6% |
| 50% | 68.5% | 18.8% | 9.6% | 3.1% |
| 100% | 62.4% | 20.4% | 12.4% | 4.7% |
| 200% | 52.5% | 22.0% | 17.1% | 8.4% |
| 300% | 44.9% | 22.3% | 20.8% | 12.1% |
| 500% | 33.8% | 21.5% | 25.6% | 19.0% |
| 1000% | 19.2% | 17.7% | 30.4% | 32.7% |

### Level-up offer rarity

Base weights: Common 1.5, Uncommon 0.3, Rare 0.15, Epic 0.04, Legendary 0.0085. The offer's value is multiplied by its rarity (Common ×1.0, Uncommon ×1.2, Rare ×1.4, Epic ×1.6, Legendary ×2.0).

| Luck | Common | Uncommon | Rare | Epic | Legendary |
|---|---|---|---|---|---|
| 0% | 75.1% | 15.0% | 7.5% | 2.0% | 0.4% |
| 50% | 67.1% | 17.2% | 11.0% | 3.7% | 1.0% |
| 100% | 60.2% | 18.3% | 14.0% | 5.7% | 1.8% |
| 200% | 48.8% | 19.0% | 18.6% | 9.7% | 4.0% |
| 300% | 39.9% | 18.6% | 21.6% | 13.4% | 6.6% |
| 500% | 27.6% | 16.4% | 24.4% | 19.4% | 12.2% |
| 1000% | 12.9% | 11.1% | 23.8% | 27.3% | 24.9% |

### Where Luck comes from

| Source | Luck |
|---|---|
| Luck Tome | +8% per level (Common), up to +16% at Legendary |
| Clover | +10% per copy |
| Credit Card (Green) | +2% per chest opened, per copy |
| Fox | +15% to start, +1.5% per level |
| **Pots** | **+0.5% each on stage 1, +0.75% on stage 2, +1% on stage 3; big pots ×1.5** (Forest and Desert only; Graveyard has pumpkins instead) |

Pots are an easy permanent source: a stage-1 map has 40 small and 15 big pots, so breaking all of them gives 40 × 0.5% + 15 × 0.75% = **+31% Luck**.

## Chests

**Price of the next chest** (`MoneyUtility.GetChestPrice`), where n = chests opened so far this run:

(30 × 1.22^n + 35n + 300 × (n − 10) past 10 + 550 × (n − 20) past 20 + 1,200 × (n − 30) past 30 + 2,400 × (n − 30) past 40 + 4,500 × (n − 30) past 50) × Chest price multiplier

> **Example:** the price of your 12th chest (you've opened n = 11).
>
> 1. 30 × 1.22¹¹ = 30 × 8.91 = 267
> 2. 35 × 11 = 385
> 3. You're past 10 chests, so add 300 × (11 − 10) = 300
> 4. Total: 267 + 385 + 300 = **952 gold**, up from 569 for the chest before. That jump at chest 11 is the first big price step.


The count only resets on a new run. It never goes up with time or stage, so a chest left closed costs the same later.

| Chests opened | 0 | 1 | 3 | 5 | 8 | 10 | 11 | 15 | 20 | 25 | 30 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Next price | 30 | 72 | 159 | 256 | 427 | 569 | 952 | 2,617 | 5,301 | 12,451 | 24,243 | 118,811 |

(The 40+ and 50+ terms count from 30, not from 40 and 50, which is why prices explode past 40.)

**Free chests:** Key gives 0.1n / (0.1n + 1) chance per chest (1 key 9%, 10 keys 50%). Roberto's Hoarder passive spawns one every 60 s.

### Chests from kills

Enemies also drop chests, and these are **free**: the chest opens when you walk over it, with no gold cost (`EffectManager.CheckChestSpawn`, `OpenChest`; confirmed in-game). Each kill rolls:

**chance = 0.05% × Powerup Drop Chance × 2 × min(1, seconds since the last kill-chest ÷ 420)**, doubled for elites.

In words: right after a chest drops, the chance is 0. It climbs back over the next 7 minutes to a maximum of 0.1% per kill (× your Powerup Drop Chance). The more you kill, the sooner one of those rolls hits, so the wait gets shorter as your kill rate grows. On stage 1 the first elite you kill always drops a chest.

> **Example:** you kill 300 enemies a second.
>
> - With Powerup Drop Chance at 1×, the expected wait is about **53 seconds** per chest.
> - At 10× (reachable on Graveyard with Bald Heads), it's about **17 seconds**, roughly 3–4 free chests a minute.
> - At 1,000 kills a second and 10×, about 9 seconds: around 400 chests an hour.
>
> (Expected wait ≈ √(420 ÷ (kills per second × 0.0005 × Powerup Drop Chance)) seconds.)

That's how multi-hour runs open thousands of chests, and why their Wizard's Hat counts reach the thousands.

**More free chests, ranked by effect:**

1. **Powerup Drop Chance** multiplies every roll. Raise it with Charge Shrine offers (+5% per Common offer) and, on Graveyard, Bald Head doublings.
2. **Kill rate.** The wait shrinks with the square root of kills per second, so 4× the kills halves it.
3. **Elites** roll at double chance, but they're rare: each enemy that can be elite has a **0.6% × Elite spawns** chance to spawn as one (`EnemyStats.GetEliteChance`). Old Mask and Charge Shrine "Elite spawns" offers add +15% each to that stat, so even 10 Old Masks only make 1.5% of enemies elite. That shortens the wait by well under 1%.
4. **Other free chests:** bosses, the first elite on stage 1, frog eggs, Challenge Shrines, and Roberto's Hoarder passive.

Keys don't add chests. They give a chance for a chest you'd pay for to open free, and chests from kills are already free.

## Powerups

Kills can also drop powerups (`PickupManager`). Each kill rolls: **the enemy's base chance × Powerup Drop Chance × a 2-minute ramp** that starts at 0 after each powerup and reaches full after 120 s. **Powerups never drop during a final swarm**, and only a limited number can be on the map at once.

Every powerup's strength and length scale with **Powerup boost** (base ×1.0; Bald Heads can double it):

| Powerup | What it does (at Powerup boost ×1) |
|---|---|
| Nuke | Explosion with radius 150 |
| Time | Freezes enemies for 12 s |
| Haste | ×1.75 movement speed for 20 s |
| Rage | ×1.5 damage for 15 s |
| Shield | Shield for 15 s |
| Stonks | ×2 gold for 15 s |
| Magnet | Pulls in all XP |

> **Example:** at Powerup boost ×4, a Time pickup freezes enemies for 48 s and a Nuke's radius is 600.

## Pots

Pots drop gold, XP, HP or silver, plus the Luck above. Pumpkin adds 8 pots on later stages and +18% pot rewards per copy.

## Microwave

- Rarity rolled at map load with Luck 0: **Common 75%, Rare 15%, Epic 7.5%, Legendary 2.5%** per Microwave. How many Microwaves a map has depends on the map: **1 or 2 per stage on Forest and Desert; 4, 6 or 8 on Graveyard** ([map limits](faq.html)). So a Legendary one shows up on about 1 Forest stage in 27, but about 1 Graveyard map in 7.

> **Example:** each Microwave has a 97.5% chance of *not* being Legendary. With 2 Microwaves: 1 − 0.975² = 4.9%, about 1 in 20. With 6 on Graveyard: 1 − 0.975⁶ = 14%, about 1 in 7.
- **Costs the current chest price** each use.
- Copies one item of its rarity and takes an item of that rarity you own in exchange. **Uses: Common 3, Rare 2, Epic 2, Legendary 1** (`InteractableMicrowave.GetUses`).

## Shady Guy

- Vendor rarity rolled at map load with Luck 0: **Common 53.3%, Rare 26.7%, Epic 13.3%, Legendary 6.7%**.
- **Item price ≈ 30 × 1.22^(0.65 × chests opened) × stage number × rarity multiplier** (Common ×1, Rare ×2, Epic ×4, Legendary ×8), times the chest price multiplier, with a random spread per slot.

> **Example:** a Rare item on stage 2 after you've opened 10 chests: 30 × 1.22^(0.65 × 10) = 30 × 3.64 = 109, × 2 for stage 2, × 2 for Rare = about **437 gold** (before the random spread).

- Shady Guy prices rise with the chests you've opened and with each stage, so shops are cheapest on stage 1 before you open chests.

## Shrines

| Shrine | What it does |
|---|---|
| Charge Shrine | Stand in the zone to charge it; rewards a choice of **3 stat offers** (Luck-weighted rarity) from the Charge Shrine list below (`EncounterData.GetOffers`). Wrench speeds charging 4% and adds 7.5% per copy; Beacon adds 2 per copy on later stages. |
| Moai | Offers items (Luck-weighted). |
| Greed Shrine | **+5% Difficulty**, permanently, and drops gold worth 10% of your next chest's price. |
| Boss Curse (Cursed Shrine) | +1 Boss Curse: one more miniboss per miniboss event, one more stage boss, bosses +16% HP each. Only spawns once you've played more than 2 runs. |
| Magnet Shrine | Pulls in all XP on the map. |
| Challenge Shrine | Spawns a challenge fight; rewards on completion. Challenge enemies have ×7 HP (×15 if also elite). |
| Balance Shrine ("Bald Heads", Graveyard) | Offers stat trades: one stat ×2, another ×0.5. See below. |
| Gravestone (Graveyard) | **+10% XP gain and +5% Difficulty**, permanently. Can also spawn an enemy. |
| Coffin (Graveyard) | Starts the Grave Ghost boss fight. |

### Which stats each source can roll

Stat offers are drawn from three fixed lists in the code (`EncounterUtility`):

| Stat | Charge Shrines | Bald Heads (×2 / ×0.5) | Chaos Tome, Dicehead's Gamba |
|---|---|---|---|
| Max HP, HP regen, Shield, Thorns, Armor, Evasion | ✓ | ✓ | ✓ |
| Size, Duration, Projectile speed, Damage, Attack speed | ✓ | ✓ | ✓ |
| Lifesteal, Crit chance, Crit damage, Elite damage, Knockback, Move speed | ✓ | ✓ | ✓ |
| Projectiles (Quantity) | ✓ | — | ✓ |
| Jump height, Pickup range | ✓ | ✓ | — |
| Luck, Gold gain, XP gain | ✓ | ✓ | — |
| **Powerup Drop Chance**, Powerup boost | ✓ | ✓ | — |
| **Elite spawns** | ✓ | — | — |
| Difficulty, Extra jumps | ✓ | — | — |
| Fall damage reduction | — | ✓ | — |

**Bald Heads (Balance Shrines)** each offer trades built from two different stats on their list: one is **multiplied by 2**, the other by 0.5. These are multipliers, so they stack: four doublings of the same stat make it ×16.

> **Example:** a run that doubles Powerup Drop Chance 3 times and never halves it has ×8. At 300 kills a second that cuts the wait for a free chest from about 53 seconds to about 19 (see [Chests from kills](#chests-from-kills)).

Things Bald Heads **can't** roll in the 1.0.69 code: Elite spawns, Projectiles, Difficulty and Extra jumps. Elite spawns come from Charge Shrines (+15% per Common offer) and Old Mask (+15% per copy).

## Banish, Refresh and Skip

These are bought in the Silver shop and used on level-up and chest screens:

- **Refresh** rerolls a level-up's offers. **Skip** passes on a level-up. **Banish** removes an offered item, weapon or tome from the pool for the rest of the run.
- **Charges per run** = the shop level you bought (up to 6), plus one free extra each once you've played enough runs: Skip at 3 runs, Refresh at 6, Banish at 9 (`PlayerInventory.InitSkipRefreshBanish`).
- **Each use also costs gold**, rising with uses this run: the 1st is free, then 5, 25, 50, 85, 140, 235… (5 × 2^(n−1) + 15 × (n−1) for the n-th paid use). Late in a run that's pocket change.

Banishing is how long runs keep the Legendary pool narrow: every banished Legendary means more chest rolls land on the ones you kept.

## Silver shop

Permanent upgrades bought with Silver (`ShopItemData`). Price of level L = round(base × growth^L) + L × step.

| Upgrade | Levels | Prices per level | Total | Unlocked by |
|---|---|---|---|---|
| Weapon slots | 2 (2 → 4 slots) | 25, 125 | 150 | 25 quests |
| Tome slots | 2 (2 → 4 slots) | 35, 135 | 170 | 35 quests |
| Refresh | 6 | 8, 15, 24, 33, 43, 55 | 178 | 20 quests |
| Skip | 6 | 8, 15, 24, 33, 43, 55 | 178 | 30 quests |
| Banish | 6 | 8, 15, 24, 33, 43, 55 | 178 | 40 quests |
| Silver gain | 20 (+2.5% each) | 5, 11, 18, 25 … 368, 442 | 2,666 | Default |
| Toggler | 1 | 50 | 50 | 40 unlocks purchased |
| Boombox | 1 | 5 | 5 | Activate the Forest boomboxes |

Slots, Refresh, Skip and Banish can be refunded; Silver gain, Toggler and Boombox can't. **Toggler** is what lets you switch items off in the item pool before a run: the toggle buttons only work once you own it (`MyAchievements.CanToggleActivation`).

## Stat offer values

When a shrine or other stat offer gives you a stat, this is the Common amount. Higher rarities multiply it (the offer's rarity multiplier).

- **% bonus** stats raise that stat by a percentage, like +12% Damage. These add up with your other % bonuses ([Core math](mechanics.html)).
- **Added directly** stats add a fixed amount to the total, like +15 Max HP, or +5 points of Crit chance.

| Stat | Common offer | How it adds |
|---|---|---|
| Damage | +12% | % bonus |
| Attack speed | +6% | % bonus |
| Size | +8% | % bonus |
| Duration | +8% | % bonus |
| Projectile speed | +10% | % bonus |
| Crit damage | +10% | % bonus |
| Elite damage | +10% | % bonus |
| Knockback | +10% | % bonus |
| Move speed | +8% | % bonus |
| Jump height | +10% | % bonus |
| Pickup range | +20% | % bonus |
| Gold, XP, silver gain | +7.5% | % bonus |
| Elite spawns | +15% | % bonus |
| Powerup boost | +10% | % bonus |
| Powerup chance | +5% | % bonus |
| Max HP | +15 | added directly |
| HP regen | +20 | added directly |
| Shield | +5 | added directly |
| Thorns | +5 | added directly |
| Projectiles | +1 | added directly |
| Projectile bounces | +1 | added directly |
| Extra jumps | +1 | added directly |
| Crit chance | +5% | added directly |
| Luck | +5% | added directly |
| Armor | +5% | added directly |
| Evasion | +5% | added directly |
| Lifesteal | +6% | added directly |
| Difficulty | +8% | added directly |
| Fall damage reduction | +10% | added directly |
