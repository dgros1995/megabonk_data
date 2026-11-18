# Items

Every item in v1.0.69 and what its code does. Values are per copy unless stated; **n** = copies held. Where an item's chance is shown as a formula like 0.15n / (0.15n + 0.5), it has diminishing returns built in (see [Core math](mechanics.html#proc-chances)). "× proc coefficient" means the weapon that hit scales the chance.

**How item bonuses stack:** almost every plain stat item (Gym Sauce, Beer, Battery, Clover, Forbidden Juice, Oats…) adds to the **flat** part of the stat. They add together, then get multiplied by your % bonuses (shrine offers, Gamba) and by the Damage Tome. See [Core math](mechanics.html).

**Use** marks what an item does for a high-kill run: **Kill**, **Kill (swarm)** (still works deep into the final swarm), **Survive**, **Scale** (levels, XP, luck), **Economy**, **Difficulty** (raises it, meaning more enemies) or **Situational**.

## Legendary (22)

| Item | What the code does | Use |
|---|---|---|
| **Anvil** | Weapon upgrades roll one extra stat line. Max 1. | Scale |
| **Big Bonk** | Big Bonk: 2% chance (+1.5% per extra copy) × proc coefficient to deal 20× (+10× per extra copy) the hit's damage to up to 5 enemies within 6 + copies (max 10). | Kill |
| **Bloody Cleaver** | 50% per copy × proc coefficient to add a Bloodmark stack; each lifesteal proc also adds a stack. | Kill |
| **Chonkplate** | +20% Lifesteal and +75% Overheal per copy (flat). | Survive |
| **Dragonfire** | Two rolls per hit, each 0.15n / (0.15n + 0.5): burn for 3 s, and a fire field (radius 6 × Size). 1 copy 23%, 3 copies 47%, 10 copies 75%. | Kill |
| **Energy Core** | Fires 4 + 2 per extra copy orbs every 4 s, range 70, each dealing 2 × (8 + level) + 8. | Kill |
| **Giant Fork** | +15% crit chance per copy (flat). Separate Megacrit roll: 14% per copy × proc coefficient, multiplying the hit by 4 + 0.15 × copies. | Kill |
| **Golden Ring** | No effect. Not in the normal pool: once you've played 6+ runs, every Legendary roll has a **0.25% chance** to turn into a Golden Ring instead (`ItemUtility.GetRandomItemFromRarity`). Long runs roll thousands of Legendaries, so most end up with one. The ideal item to trade at a Legendary Microwave. | — |
| **Holy Book** | +100 Max HP, +50 HP regen, +25% overheal per copy. Every 1.5 s, deals (8 + level) × 0.5 × the healing you did that tick to every enemy within (5 + copies) × Size. | Survive / Kill |
| **Ice Cube** | Two rolls per hit: freeze 3 s at 0.4n / (0.4n + 0.6) (1 copy 40%, 3 copies 67%); ice burst at 0.2n / (0.2n + 0.5) (1 copy 29%) for 0.4n × hit damage, which can also freeze. | Kill |
| **Joe's Dagger** | On damaging a non-boss (at most every 0.3 s): 1% execute roll. Each execute adds +1% Damage per copy, no cap. Max 10 copies. | Kill |
| **Lightning Orb** | Two rolls per hit, each 0.9 × 0.25n / (0.25n + 0.6): stun for 3 s, and a lightning strike for 0.4n × hit damage on a random enemy within 40 (×Size 8 radius per strike). 1 copy 26%, 3 copies 50%, 10 copies 73%; caps at 90%. | Kill |
| **Overpowered Lamp** | Every hit runs all your on-hit items **one extra time per Lamp** (`ItemInventory.PostDamage` loops 1 + Lamps times). With the max of 2, every on-hit item (Big Bonk, Spicy Meatball, Lightning Orb, Moldy Cheese…) rolls 3 times per hit. In 100% of 500k+ leaderboard runs. | Kill |
| **Pot (Stainless Steel)** | +10 max weapon level for the first copy, 1 less for each copy after, never below +2. | Scale |
| **Power Gloves** | 0.08n / (0.08n + 0.5) × proc coefficient (1 copy 14%): blast for 1.25× damage within 10 + 5n, knocking enemies away. Cooldown 3.2 − 0.2n s. | Kill |
| **Snek** | 4 poison stacks per copy per hit (5 s). 5% per copy × proc coefficient: poison burst for (0.5 + 0.4n) × the hit's damage. | Kill |
| **Soul Harvester** | Each kill fires 2 homing souls (range 50) dealing roughly (8 + level) × copies × 1.75. | Kill |
| **Speed Boi** | When you are hit below 50% HP: time slows to 30% for 8 + 2n s (max 15), damage ×2 meanwhile. 10 s cooldown. | Survive |
| **Spicy Meatball** | 25% × proc coefficient: explosion for 65% of the hit's damage within (3 + copies) × Size, max 8 × Size. | Kill |
| **Sucky Magnet** | Pulls in all XP within range 100. | Scale |
| **Wizard's Hat** | +10 max tome level for the first copy, 1 less for each copy after, never below +2. | Scale |
| **Za Warudo** | Stops one fatal hit by freezing time, then breaks. Max 25 per run. | Survive |

## Epic (20)

| Item | What the code does | Use |
|---|---|---|
| **Beefy Ring** | +10 Max HP per copy; +0.2% Damage per point of max HP (including shield) per copy. | Kill |
| **Bob (Dead)** | Summons a ghost Bob every 14 units you move; each lasts 10 s × Duration and deals 1.5× damage. | Kill |
| **Bob's Light (Lantern)** | Bob's Light: an explosion that instantly kills every non-boss enemy within 50 + 10n (max 250). Cooldown 45 − 3n s (min 5). Red ghosts only die to it 33% of the time. | Kill (swarm) |
| **Credit Card (Green)** | +2% Luck per chest opened, per copy. Chest prices +10% per copy. | Scale |
| **Cursed Gloves** | +10% Difficulty and Max HP ×0.8 per copy. 0.5 × 0.05n / (0.05n + 0.8) on hit (1 copy 3%): cursed blast for 0.85 × (8 + level) within 4. | Difficulty |
| **Demonic Soul** | +0.1% Damage per kill, up to 1,000 stacks per copy (+100%). | Kill |
| **Eagle Claw** | 0.08n / (0.08n + 0.5) × proc coefficient (1 copy 14%): knock enemies up; +66% damage per copy to airborne enemies. | Situational |
| **Gamer Goggles** | Below 50% HP: up to +100% Damage per copy, more the lower your HP. | Situational |
| **Gas Mask** | +0.5% Armor and +0.5% Overheal per poisoned enemy, up to +40% Armor and +25% Overheal per copy. | Survive |
| **Grandma's Secret Tonic** | +2% crit. 50% × proc coefficient on crits: explosion for 50% of the hit within (3 + copies) × Size, max 8. | Kill |
| **Kevin** | 25% per copy: when you hit, Kevin hits you. Can't kill you; his hits trigger your on-damage items. | Survive |
| **Mirror** | Reflects a hit with brief invulnerability, dealing (1 + 0.25n) × your Damage in a cone. Cooldown max(8 − n, 4) s. | Survive |
| **Quin's Mask** | +20 Thorns per copy. Thorns damage has a 50% chance to explode for 50% within (5 + copies) × Size, max 10. | Situational |
| **Scarf** | +50% Damage per copy while airborne. | Situational |
| **Shattered Knowledge** | XP shards damage enemies they pass through. | Kill |
| **Slurp Gloves (Blood)** | Every 9 s on hit: blood blast for 3.15× damage within 10, adds Bloodmark, heals 7.5% of Max HP. | Survive |
| **Slutty Cannon** | 0.2n / (0.2n + 0.5) × proc coefficient (1 copy 29%): fires a rocket for (1 + 0.4n) × the hit's damage. Max 4 per tick. | Kill |
| **Spiky Shield** | +10% Armor per copy (flat); Thorns = 200 × raw Armor per copy. | Survive |
| **Toxic Barrel** | When you take damage: 5 poison stacks per copy (5 s) to enemies within (7 + n) × Size. 0.25 s cooldown. | Survive |
| **Turbo Skates** | Moving fast adds attack speed, up to +40% per copy. | Kill |

## Rare (21)

| Item | What the code does | Use |
|---|---|---|
| **Backpack** | +1 projectile per copy. | Kill |
| **Beacon** | +2 Charge Shrines on later stages per copy; charged shrines heal 2.5% per tick within 8 + 2n. | Scale |
| **Beer** | +20% Damage and −5% Max HP per copy. | Kill |
| **Brass Knuckles** | +25% damage per copy to enemies within 8 + 2n. | Kill |
| **Campfire** | Standing still 0.6 s lights a camp: +1,100 HP regen per minute per copy. | Survive |
| **Coward's Cloak** | +5% move speed per copy; +30% speed bursts when hit (2 stacks per copy). | Survive |
| **Credit Card (Red)** | +2.5% Damage per chest opened, per copy. | Kill |
| **Demon Blade** | +1% crit. 25% per copy on damaging: heal (needs lifesteal to be allowed). | Survive |
| **Demonic Blood** | +0.5 Max HP per kill, up to 200 stacks per copy. | Survive |
| **Echo Shard** | Kills can drop an extra XP shard (logic outside the item class). | Scale |
| **Electric Plug** | When hit: shocks 6 + 4n enemies within 12 + 4 × Size (per copy) for 0.8× damage. | Survive |
| **Feathers** | +1 jump and +15% jump height per copy; jumping boosts speed by 2.2 per copy. | Situational |
| **Golden Shield** | Taking damage drops 6 gold per copy. | Economy |
| **Golden Sneakers** | Gold per metre moved: 0.1 + 0.05 per extra copy. | Economy |
| **Idle Juice** | Standing still adds +4% Damage each second, up to +100% per copy. | Kill |
| **Leeching Crystal** | +50 Max HP and −50% HP regen per copy. | Survive |
| **Moldy Gloves (Poison)** | Every 8.5 s on hit: poison cloud for 1.5 × (8 + level) within 15, 10 stacks per copy. | Kill |
| **Phantom Shroud** | +5% Evasion per copy. After an evade, the next attack deals ×(2 + 0.5n) plus a speed burst; lasts 3 + 0.5n s. | Kill |
| **Pumpkin** | +8 pots on later stages and +18% pot rewards per copy. | Economy |
| **Thunder Mitts** | Every 10 s on hit: lightning for 3× damage within 8, stunning 3 s. | Kill |
| **Unstable Transfusion** | 35% per copy × proc coefficient to add a Bloodmark stack (each full 100% is a guaranteed stack). | Kill |

## Common (22)

| Item | What the code does | Use |
|---|---|---|
| **Battery** | +8% attack speed per copy (flat). | Kill |
| **Borgar** | 2% (+1% per copy) per kill to drop a Borgar healing 8% + 10 HP. | Survive |
| **Boss Buster** | +15% damage per copy to elites and bosses. | Kill |
| **Cactus** | When hit: fires 2 spikes per copy, each 5 per copy + Thorns. | Survive |
| **Clover** | +10% Luck per copy. | Scale |
| **Cursed Doll** | Every second, each copy curses up to 2 enemies (5 new per check). Cursed non-bosses lose 30% of their MAX HP per second, so they die in 4 s whatever their HP. Against bosses it deals only 0.7 × (8 + level). | Kill (swarm) |
| **Forbidden Juice** | +10% crit chance per copy (flat). | Kill |
| **Ghost** | Using an interactable summons 6 ghosts per copy for 30 s × Duration. | Situational |
| **Golden Glove** | 15% per copy for extra gold from kills; each full 100% is guaranteed. | Economy |
| **Gym Sauce** | +10% Damage per copy (flat bracket). | Kill |
| **Ice Crystal** | 0.075n / (0.075n + 0.75) × proc coefficient (1 copy 9%, 10 copies 50%): freeze for 2.5 + 0.1n s (max 6). | Kill |
| **Key** | Free-chest chance 0.1n / (0.1n + 1): 1 key 9%, 3 keys 23%, 10 keys 50%. | Economy |
| **Medkit** | +45 HP regen per copy. | Survive |
| **Moldy Cheese** | 40% per copy to add a poison stack (5 s); each full 100% is a guaranteed stack, only the leftover is scaled by proc coefficient. | Kill |
| **Oats** | +25 Max HP per copy. | Survive |
| **Old Mask** | +15% elite spawn chance per copy. | Difficulty |
| **Skuleg** | +7% Difficulty per copy (flat). | Difficulty |
| **Slippery Ring** | +15% raw Evasion per copy. Real evasion = E / (E + 1): 1 ring 13%, 3 rings 31%, 7 rings 51%. | Survive |
| **Tactical Glasses** | +20% damage per copy to enemies above 90% HP. | Kill |
| **Time Bracelet** | +8% XP gain per copy. | Scale |
| **Turbo Socks** | +15% move speed per copy. | Situational |
| **Wrench** | Charge Shrines charge 4% faster and give 7.5% more per copy. | Scale |

**Not in the item list:** Weeb Headset has code (a tiny charm chance) but no item entry in 1.0.69, so it can't drop. **Crypt Key** is a quest item that opens the Graveyard crypt ([Map secrets](secrets.html)).

## What the code changes about common advice

- **Cursed Doll is the late-swarm engine.** It ignores enemy HP entirely (30% of max HP per second on non-bosses), so it keeps killing when the final swarm's HP bonus reaches thousands. Against bosses it's weak.
- **Bob's Light is the other one.** It instantly kills every non-boss in its radius; stack copies to reach the 5 s cooldown (14 copies) and 250 radius (20 copies).
- **Proc items fall off.** Dragonfire, Ice Cube, Lightning Orb and Power Gloves give much less per copy after the first few. Lightning Orb caps at 90%.
- **Moldy Cheese and Snek don't fall off.** Moldy Cheese's chance passes 100% into guaranteed extra stacks, and Snek's 4 stacks per copy are always applied.
- **Execute items stop working at 6:00 of the final swarm,** when Purple and then Red Ghosts (not executable) take over.
