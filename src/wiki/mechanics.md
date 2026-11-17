# Core math

## How every stat is calculated

Every stat is held as three parts and combined the same way (`StatComponents.GetFinalValue`):

**Final = (base + flat bonuses) × (1 + sum of % bonuses) × (product of × multipliers)**

Which bonus goes in which part is set by its modify type in the code:

| Bracket | Modify type | Where it comes from |
|---|---|---|
| Flat | `Flat` | Items (Gym Sauce, Beer, Forbidden Juice, Clover, Battery…), most tomes (Precision, Luck, Armor, Shield, Health, Cursed…), character starting stats |
| % (additive) | `Addition` | Shrine stat offers (Damage +12%, Size +8%…), Gamba rolls, some tomes (Cooldown, Size, Duration, XP…) |
| × (multiplicative) | `Multiplication` | Damage Tome, Giant Fork's Megacrit, Phantom Shroud's post-evade hit |

So for Damage, the base is 1.0 and items stack inside the flat part: 5 Gym Sauces make it 1.5. Shrine Damage offers then add to the % bracket, and the Damage Tome multiplies everything. **Spreading Damage across all three brackets beats piling it into one.**

### Base values (before character bonuses)

| Stat | Base value |
|---|---|
| Max HP | 100 |
| HP regen | 10 |
| Crit chance | 1% |
| Crit damage | ×1.0 |
| Evasion | 1% |
| Pickup range | 5 |
| Jump height | 7 |
| Luck, Difficulty, Armor, Shield, Lifesteal, Thorns, Overheal | 0 |
| Damage, attack speed, size, duration, projectile speed, knockback, move speed | ×1.0 |
| Fire, ice, lightning, poison and elite damage | ×1.0 |
| Gold, XP, chest and silver gain | ×1.0 |
| Enemy amount, size, speed, HP, damage and scaling | ×1.0 |

### Built-in diminishing returns

Armor and Evasion don't add up in a straight line. Each point is worth a bit less than the one before, so you can never reach 100%.

The stat screen shows them as percentages, but the game stores them as plain numbers: **50% Armor on the stat screen is 0.5 in the formulas below**, and 100% is 1.0.

#### Armor: how much damage it blocks

**Damage blocked = Armor ÷ (Armor + 0.75)**, then × 0.999 so it can never reach 100%.

In words: at 0.75 Armor (75%) you block half of every hit. Each time you double your Armor you close the gap toward 100% a little less.

> **Example:** you have 150% Armor, so A = 1.5.
>
> 1. 1.5 ÷ (1.5 + 0.75) = 1.5 ÷ 2.25 = 0.667.
> 2. You block **67%** of each hit. A 300-damage hit becomes about 100.

| Armor on the stat screen | 25% | 75% | 150% | 300% | 750% |
|---|---|---|---|---|---|
| Damage blocked | 25% | 50% | 67% | 80% | 91% |

Going from 75% to 150% Armor takes you from 50% to 67% blocked. Doubling again to 300% only gets you to 80%.

#### Evasion: chance to dodge a hit

**Dodge chance = Evasion ÷ (Evasion + 1)**, × 0.999.

In words: at 100% Evasion you dodge half of all hits. It's the same curve as Armor, but you need more of it, since the "half" point is 1.0 instead of 0.75.

> **Example:** you have 200% Evasion, so E = 2.0.
>
> 1. 2.0 ÷ (2.0 + 1) = 2 ÷ 3 = 0.667.
> 2. You dodge **67%** of hits, roughly two in every three.

| Evasion on the stat screen | 50% | 100% | 200% | 300% | 1000% |
|---|---|---|---|---|---|
| Chance to dodge | 33% | 50% | 67% | 75% | 91% |

A dodge ignores the whole hit, however big it is. That's why Evasion matters so much late in a final swarm.

#### Max HP

Max HP can't go below 1, however many HP penalties you stack.

#### Item chances that slow down

Many items turn the number of copies you hold into a chance using the same kind of curve: **chance = max × x ÷ (x + k)**, where x = copies × the item's per-copy value. The first copies add a lot; later copies add less and less, and the chance never quite reaches the max.

> **Example:** Dragonfire is 0.15 per copy with k = 0.5.
>
> - 1 copy: x = 0.15, so 0.15 ÷ 0.65 = **23%**.
> - 5 copies: x = 0.75, so 0.75 ÷ 1.25 = **60%**.
> - 10 copies: x = 1.5, so 1.5 ÷ 2.0 = **75%**.

Five copies more than double one copy's chance, but going from 5 to 10 only adds another 15 points. Every such item is in the table under [Proc chances](#proc-chances).

## Weapon damage

**Hit = weapon damage × Damage stat (all three brackets) × crit multiplier × Crit damage**

- Weapon damage is the weapon's own Damage stat (base plus its upgrade lines). Aegis adds your Thorns to it.
- Crit chance = your Crit chance + the weapon's Crit chance.
- On-hit items can add per-attack modifiers just before the hit (Boss Buster +15% to elites and bosses, Tactical Glasses +20% above 90% HP, Eagle Claw to airborne enemies, Giant Fork's Megacrit, Phantom Shroud).
- **Execute** (Dexecutioner, Ninja, Joe's Dagger): normal enemies that can be executed die outright; bosses, and enemies flagged as not executable (Purple and Red Ghosts, Graveyard boss ghosts), take 2% of their max HP instead.

### Crits and overcrits

The game rolls how many crits a hit gets: one guaranteed crit for each full 100% of crit chance, plus one more with the leftover chance. 230% = 2 crits, with a 30% chance of 3.

| Crits on the hit | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Multiplier | ×1 | ×2 | ×4 | ×6.25 | ×9 | ×12.25 | ×16 |

The formula is (1 + crits ÷ 2)², except that one crit is ×2. That multiplier is then multiplied by Crit damage (base ×1.0).

> **Example:** you have 230% crit chance.
>
> 1. The full 200% gives 2 guaranteed crits. The leftover 30% is the chance of a third.
> 2. 70% of hits get 2 crits: (1 + 2 ÷ 2)² = 2² = **×4**.
> 3. 30% of hits get 3 crits: (1 + 3 ÷ 2)² = 2.5² = **×6.25**.
> 4. On average: 0.7 × 4 + 0.3 × 6.25 = **×4.68**, before Crit damage.

| Crit chance | 100% | 150% | 200% | 250% | 300% | 400% |
|---|---|---|---|---|---|---|
| Average multiplier | ×2 | ×3 | ×4 | ×5.1 | ×6.25 | ×9 |

## Proc chances

Every on-hit roll is **chance × the weapon's proc coefficient** (`ItemUtility.TryProc`). Where an item's chance can pass 100% (Moldy Cheese, Snek, Unstable Transfusion, Bloody Cleaver, Golden Glove), each full 100% is a guaranteed proc and only the leftover is rolled.

> **Example:** you hold 5 Dragonfire (60%, from the table below) and hit with the Axe, whose proc coefficient is 0.7. Each Axe hit has 60% × 0.7 = **42%** to proc. The same 5 Dragonfire on a Sniper Rifle (1.5) would be 60% × 1.5 = 90%. Each weapon's proc coefficient is on the [Weapons](weapons.html) page.

Items whose chance slows down with more copies:

| Item | Formula | 1 | 2 | 3 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|---|
| Dragonfire (fire field, burn) | 0.15n / (0.15n + 0.5) | 23% | 37% | 47% | 60% | 75% | 86% |
| Ice Cube (ice burst) | 0.2n / (0.2n + 0.5) | 29% | 44% | 55% | 67% | 80% | 89% |
| Ice Cube (freeze) | 0.4n / (0.4n + 0.6) | 40% | 57% | 67% | 77% | 87% | 93% |
| Lightning Orb (strike, stun) | 0.9 × 0.25n / (0.25n + 0.6) | 26% | 41% | 50% | 61% | 73% | 80% |
| Slutty Cannon | 0.2n / (0.2n + 0.5) | 29% | 44% | 55% | 67% | 80% | 89% |
| Power Gloves, Eagle Claw | 0.08n / (0.08n + 0.5) | 14% | 24% | 32% | 44% | 62% | 76% |
| Ice Crystal | 0.075n / (0.075n + 0.75) | 9% | 17% | 23% | 33% | 50% | 67% |
| Key (free chest) | 0.1n / (0.1n + 1) | 9% | 17% | 23% | 33% | 50% | 67% |
| Cursed Gloves | 0.5 × 0.05n / (0.05n + 0.8) | 3% | 6% | 8% | 12% | 19% | 28% |

Damage from poison, burn ticks, Bloodmark pops and other secondary effects has proc coefficient 0, so it never triggers on-hit items.

## Damage you take

**Damage taken = enemy damage × (1 − armor reduction) × (1 − damage reduction)**, minimum 1.

> **Example:** a ghost hits for 1,000. You have 150% Armor (67% blocked) and no other damage reduction. You take 1,000 × (1 − 0.67) = **330**.

- Against boss attacks your armor counts **half**; against the final boss it counts **75%**. Some attacks ignore armor.
- **Evasion** is a chance to dodge a hit entirely.
- **Shield** is a separate pool, taken from the Shield stat as a whole number.
- **Overheal** cap = Max HP × Overheal.
- **Lifesteal** works like crits: one guaranteed heal per full 100%, plus a chance for one more.

## Your base damage

Many items and effects don't use your weapon's damage. They use a player number called base damage: **8 + your character level**, recalculated every level-up. Burn, Cursed Doll (against bosses), Holy Book, Energy Core, Soul Harvester, the elemental gloves and Bloodmark all scale with it, together with your Damage stat.

## Levels and XP

XP needed to go from level L to L + 1 (`XpUtility`): **5 + 5.325 × L^1.065** (level 1 → 2 is 7). The level cap is **9,999**.

| Level | 10 | 100 | 500 | 1,000 | 2,000 | 5,000 | 9,999 |
|---|---|---|---|---|---|---|---|
| XP for the next level | 67 | 723 | 3,993 | 8,348 | 17,460 | 46,320 | 96,894 |
| Total XP to get here | 377 | 35,642 | 970,036 | 4.0M | 16.9M | 112M | 469M |

In words: each level costs a little more than the one before, growing slightly faster than straight-line. Going from level 1,000 to 2,000 takes about 3× the XP it took to reach 1,000 in the first place.

> **Example:** a run at level 2,000 has collected about 16.9 million XP. Reaching 4,000 needs about 70 million in total, roughly 4× as much again.

**XP per kill:** each enemy has its own XP value in the enemy data, multiplied by your XP gain. **Elites give 10× XP.** Every kill also drops 1 gold (× your gold gain).
