# Weapons

Every weapon's numbers from the game's weapon data, how fast each one attacks, and how each tome changes it. Unlock requirements are on [Quests & unlocks](quests.html).

## How weapons work

- **Upgrades:** each weapon upgrade raises a few of that weapon's stat lines by the Common amount × the offer's rarity (×1.0 Common up to ×2.0 Legendary). Anvil adds one more line to future offers.
- **Level cap:** 40, plus 10 for the first Pot (Stainless Steel) and 1 less for each extra copy (never below +2).
- **Slots:** 2 to start, up to 4 with the Weapon Slots upgrade. See the [FAQ](faq.html) for 2 vs 3 vs 4.
- **Your stats apply on top:** the weapon's damage × your Damage stat, its crit chance + yours, and so on. The tome section below has every formula.

### Attack timing (`WeaponUtility.GetWeaponCooldown`)

One attack cycle = **cooldown ÷ Attack Speed + projectiles × shot interval**, where the shot interval = max(burst time ÷ projectiles, minimum interval) ÷ Attack Speed.

So **more projectiles usually cost no extra time:** the burst is spread over the same burst time, until the shots hit the weapon's minimum interval. Attack Speed (Cooldown Tome) shortens everything.

## Overview

**Attacks/s** is projectiles fired per second at base (Attack Speed 100%, no Quantity). **Proc rolls/s** is attacks/s × proc coefficient: how often the weapon rolls on-hit items like Big Bonk, Lightning Orb and Dragonfire against **one** enemy. Weapons that pierce, bounce or hit an area roll once per enemy hit, so in a crowd they roll many times more.

| Weapon | Base dmg | Projectiles | Cooldown | Attacks/s | Proc coef. | Proc rolls/s | Hits |
|---|---|---|---|---|---|---|---|
| Aegis | 10 | 2 | 1.5 s | contact | 1 | — | area: blocks, then shockwaves around you |
| Aura | 6 | — | 0.3 s | 3.33 ticks | 0.7 | 2.33 | area: every enemy in range, each tick |
| Axe | 6 | 2 | 1.4 s | 1.43 | 0.7 | 1 | area: spinning axes that linger |
| Bananarang | 9 | 1 | 0.8 s | 0.59 | 1 | 0.59 | pierce: passes through everything, out and back |
| Black Hole | 4.5 | 1 | 1 s | 0.4 | 0.7 | 0.28 | area: pulls and damages everything nearby |
| Blood Magic | 9 | 1 | 1.5 s | 0.66 | 1 | 0.66 | pierce: passes through everything |
| Bone | 11 | 1 | 0.4 s | 0.71 | 1 | 0.71 | bounce: bounces once |
| Bow | 9 | 1 | 0.92 s | 1.09 | 1 | 1.09 | pierce: arrows pierce up to 99 |
| Chunkers | 12 | 3 | 1.5 s | contact | 0.8 | — | contact: rocks hit what they touch while orbiting |
| Corrupted Sword | 12 | 1 | 0.8 s | 0.62 | 0.8 | 0.5 | area: front and back slashes |
| Dexecutioner | 9 | 1 | 0.8 s | 0.62 | 1 | 0.62 | area: piercing blade |
| Dice | 0 + roll of 1–6 | 1 | 0.5 s | 0.67 | 1 | 0.67 | single: one target per die |
| Dragon's Breath | 16 | — | 2 s | contact | 0.7 | — | contact: flame cone hits everything in it while it lasts |
| Firestaff | 10 | 1 | 0.5 s | 0.67 | 1 | 0.67 | area: fireballs explode |
| Flamewalker | 5 | 1 | 0 s | contact | 0.8 | — | area: fire patches hit what stands in them |
| Frostwalker | 9 | — | 1.25 s | 0.8 ticks | 0.9 | 0.72 | area: every enemy in range, each pulse |
| Hero Sword | 11 | 1 | 0.75 s | 0.67 | 0.8 | 0.53 | area: slash plus a flying slash |
| Katana | 11 | 1 | 0.4 s | 1.11 | 0.95 | 1.06 | area: slash |
| Lightning Staff | 7 | 1 | 1.1 s | 0.71 | 1 | 0.71 | bounce: chains to more enemies with upgrades |
| Mines | 10 | 1 | 1 s | 0.5 | 0.8 | 0.4 | area: explode on enemies |
| Poison Flask | 1 | 1 | 0.8 s | 0.56 | 0.9 | 0.5 | area: poison pools |
| Revolver | 5 | 6 | 1.4 s | 2.4 | 0.9 | 2.16 | bounce: bullets ricochet |
| Scythe | 11 | 1 | 0.85 s | 0.43 | 0.8 | 0.34 | area: 360° sweep |
| Shotgun | 9 | 1 | 1 s | 0.5 | 1 | 0.5 | area: spread blast in front |
| Slutty Rocket | 11 | 1 | 0.3 s | 0.77 | 1 | 0.77 | single: homing missiles |
| Sniper Rifle | 22 | 1 | 1 s | 0.5 | 1.5 | 0.75 | pierce: long-range piercing shot |
| Space Noodle | 10 | — | 1 s | contact | 0.75 | — | contact: beam hits everything along it while linked |
| Sword | 11 | 1 | 0.75 s | 0.8 | 0.8 | 0.64 | area: sweep through several |
| Tornado | 8 | 1 | 0.8 s | 0.56 | 1 | 0.56 | pierce: passes through everything |
| Wireless Dagger | 9 | 1 | 0.5 s | 0.62 | 0.9 | 0.56 | bounce: homing, bounces once |

Proc coefficients come straight from the weapon data (`procCoefficient`). Contact weapons (Aegis, Chunkers, Dragon's Breath, Space Noodle, Flamewalker) roll whenever they touch an enemy, so their rate depends on the crowd, not on a cycle.

## Which weapons roll procs fastest

Proc rolls per second against one enemy, at base and with a typical mid-run build of **+4 projectiles (Quantity) and +100% Attack Speed**. Higher means more Big Bonk, Lightning Orb and Dragonfire rolls.

| Weapon | At base | +4 projectiles, ×2 Attack Speed | Gain | Notes |
|---|---|---|---|---|
| Bow | 1.09 | 10.9 | ×10.0 | all projectiles fire at once; multiplied by enemies hit |
| Katana | 1.06 | 10.6 | ×10.0 | extra projectiles are free up to 25 per burst; multiplied by enemies hit |
| Slutty Rocket | 0.77 | 7.69 | ×10.0 | extra projectiles are free up to 10 per burst |
| Revolver | 2.16 | 7.2 | ×3.33 | extra projectiles always free; multiplied by enemies hit |
| Bone | 0.71 | 7.14 | ×10.0 | extra projectiles are free up to 10 per burst; multiplied by enemies hit |
| Lightning Staff | 0.71 | 7.14 | ×10.0 | extra projectiles are free up to 7 per burst; multiplied by enemies hit |
| Firestaff | 0.67 | 6.67 | ×10.0 | extra projectiles are free up to 6 per burst; multiplied by enemies hit |
| Dice | 0.67 | 6.67 | ×10.0 | extra projectiles are free up to 6 per burst |
| Sword | 0.64 | 6.4 | ×10 | extra projectiles are free up to 5 per burst; multiplied by enemies hit |
| Dexecutioner | 0.62 | 6.25 | ×10.0 | extra projectiles are free up to 20 per burst; multiplied by enemies hit |
| Sniper Rifle | 0.75 | 6 | ×8 | extra projectiles are free up to 3 per burst; multiplied by enemies hit |
| Axe | 1 | 6 | ×6 | all projectiles fire at once; multiplied by enemies hit |
| Blood Magic | 0.66 | 5.88 | ×8.94 | extra projectiles are free up to 1 per burst; multiplied by enemies hit |
| Bananarang | 0.59 | 5.88 | ×10.0 | extra projectiles are free up to 9 per burst; multiplied by enemies hit |
| Wireless Dagger | 0.56 | 5.62 | ×10.0 | extra projectiles always free; multiplied by enemies hit |
| Tornado | 0.56 | 5.56 | ×10.0 | extra projectiles are free up to 10 per burst; multiplied by enemies hit |
| Hero Sword | 0.53 | 5.33 | ×10.0 | extra projectiles are free up to 5 per burst; multiplied by enemies hit |
| Poison Flask | 0.5 | 5 | ×10.0 | extra projectiles are free up to 5 per burst; multiplied by enemies hit |
| Corrupted Sword | 0.5 | 5 | ×10.0 | extra projectiles are free up to 5 per burst; multiplied by enemies hit |
| Aura | 2.33 | 4.67 | ×2 | no projectiles: only Attack Speed raises it; multiplied by enemies hit |
| Shotgun | 0.5 | 4.44 | ×8.89 | extra projectiles are free up to 4 per burst; multiplied by enemies hit |
| Mines | 0.4 | 3.56 | ×8.89 | extra projectiles are free up to 4 per burst; multiplied by enemies hit |
| Scythe | 0.34 | 3.4 | ×10 | extra projectiles are free up to 15 per burst; multiplied by enemies hit |
| Black Hole | 0.28 | 2 | ×7.14 | extra projectiles are free up to 3 per burst; multiplied by enemies hit |
| Frostwalker | 0.72 | 1.44 | ×2 | no projectiles: only Attack Speed raises it; multiplied by enemies hit |

**What it means for procs:** Aura and multi-projectile weapons roll the most per enemy, and anything that pierces or hits an area (Bow, Tornado, Bananarang, Blood Magic, Lightning Staff, Shotgun, the swords) rolls once **per enemy it hits**, which in a swarm is far more than the table shows. Quantity is the strongest stat for proc rates on burst weapons, because extra projectiles fit into the same burst.

## How tomes affect weapons

Every weapon stat is the weapon's value combined with yours (`WeaponUtility`):


- **Damage:** every hit × your Damage stat.
- **Precision:** your crit chance + the weapon's own.
- **Cooldown** (Attack Speed): pause = weapon cooldown ÷ Attack Speed; shots inside a burst are spaced burst time ÷ projectiles ÷ Attack Speed.
- **Quantity:** weapon projectiles + yours.
- **Size:** weapon size × yours, capped where the weapon has a cap.
- **Duration:** weapon duration × yours, capped at the weapon's max duration.
- **Projectile Speed:** weapon speed × yours; only matters if something travels.
- **Knockback:** weapon knockback × yours, applied on every hit.

### At a glance


| Weapon | Damage | Precision | Cooldown | Quantity | Size | Duration | Projectile Speed | Knockback |
|---|---|---|---|---|---|---|---|---|
| Aegis | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Aura | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ |
| Axe | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Bananarang | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Black Hole | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Blood Magic | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| Bone | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Bow | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Chunkers | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Corrupted Sword | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Dexecutioner | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Dice | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Dragon's Breath | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| Firestaff | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Flamewalker | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✗ | ✗ |
| Frostwalker | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| Hero Sword | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Katana | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Lightning Staff | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Mines | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ |
| Poison Flask | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Revolver | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Scythe | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Shotgun | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Slutty Rocket | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| Sniper Rifle | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Space Noodle | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| Sword | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Tornado | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |
| Wireless Dagger | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (cap) | ✓ | ✓ |

✓ (cap) = it works until the weapon's maximum. Damage, Precision and Size work on every weapon. The cards below give each weapon's numbers.

## Every weapon

#### Aegis

*Blocks attacks and releases counter shockwaves; adds Thorns to its damage*

- **Base:** 10 damage, 1.5 s cooldown, 2 projectiles, 1 bounce, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +15%, Projectiles +1, Knockback +25%.
- **Tomes:**
    - Cooldown: shields come back faster (1.5 s base)
    - Quantity: +1 shield per Quantity (starts with 2)
    - Duration: no effect (nothing timed to lengthen)
    - Projectile Speed: no effect (a shield around you)
    - Knockback: base 3 × Knockback

#### Aura

*Constant close-range damage*

- **Base:** 6 damage, 0.3 s cooldown, proc coefficient 0.7.
- **Upgrade lines:** Damage +1.4, Size +14%.
- **Tomes:**
    - Cooldown: damage ticks come faster (0.3 s base)
    - Quantity: no effect (has no projectile count)
    - Duration: no effect (nothing timed to lengthen)
    - Projectile Speed: no effect (an aura)
    - Knockback: base 0.5 × Knockback

#### Axe

*Spinning axes that linger*

- **Base:** 6 damage, 1.4 s cooldown, 2 projectiles, proc coefficient 0.7.
- **Upgrade lines:** Damage +1.5, Size +10%, Projectiles +1, Duration +10%.
- **Tomes:**
    - Cooldown: 1.4 s pause ÷ Attack Speed
    - Quantity: +1 axe per Quantity (starts with 2)
    - Duration: axes linger longer: 0.82 s → cap 8 s (cap reached at +876% Duration)
    - Projectile Speed: faster projectiles (base 0.5)
    - Knockback: base 1 × Knockback

#### Bananarang

*Returning banana*

- **Base:** 9 damage, 0.8 s cooldown, pierces all, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +14%, Projectiles +1, Projectile Speed +10%.
- **Tomes:**
    - Cooldown: 0.8 s pause ÷ Attack Speed
    - Quantity: +1 banana per Quantity (starts with 1)
    - Duration: bananas fly further before returning: 3 s → cap 10 s (cap reached at +233% Duration)
    - Projectile Speed: flies out and back faster (base 1)
    - Knockback: base 1 × Knockback

#### Black Hole

*Gravity field that pulls in and damages enemies*

- **Base:** 4.5 damage, 1.0 s cooldown, proc coefficient 0.7.
- **Upgrade lines:** Damage +1.25, Size +13%, Projectiles +1, Duration +0.12.
- **Tomes:**
    - Cooldown: 1 s pause ÷ Attack Speed
    - Quantity: +1 black hole per Quantity (starts with 1)
    - Duration: black holes last longer: 2 s → cap 7 s (cap reached at +250% Duration)
    - Projectile Speed: black holes drift faster (base 20)
    - Knockback: base 6 × Knockback

#### Blood Magic

*5% of kills permanently add Max HP*

- **Base:** 9 damage, 1.5 s cooldown, pierces all, proc coefficient 1.
- **Upgrade lines:** Damage +1.5, Size +15%, Projectiles +1.
- **Tomes:**
    - Cooldown: 1.5 s pause ÷ Attack Speed
    - Quantity: +1 blood bolt per Quantity (starts with 1)
    - Duration: no effect (its 0.75 s already sits at its 0.75 s cap)
    - Projectile Speed: faster projectiles (base 1)
    - Knockback: base 1 × Knockback

#### Bone

*Bouncing projectile, starts with 1 bounce*

- **Base:** 11 damage, 0.4 s cooldown, 1 bounce, 10% crit, proc coefficient 1.
- **Upgrade lines:** Damage +2.5, Projectiles +1, Bounces +1, Crit +12%, Crit Damage +25%, Projectile Speed +0.2.
- **Tomes:**
    - Cooldown: 0.4 s pause ÷ Attack Speed
    - Quantity: +1 bone per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 3 s → cap 10 s (cap reached at +233% Duration)
    - Projectile Speed: faster projectiles (base 0.35)
    - Knockback: base 1.5 × Knockback

#### Bow

*Piercing arrows*

- **Base:** 9 damage, 0.92 s cooldown, pierces 99, proc coefficient 1.
- **Upgrade lines:** Damage +1.75, Projectiles +1, Size +15%, Crit +8%, Crit Damage +18%, Projectile Speed +20%.
- **Tomes:**
    - Cooldown: 0.92 s pause ÷ Attack Speed
    - Quantity: +1 arrow per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 0.5 s → cap 1 s (cap reached at +100% Duration)
    - Projectile Speed: arrows fly faster (and Size/Duration slow them down less) (base 1.5)
    - Knockback: base 0.5 × Knockback

#### Chunkers

*Orbiting rocks*

- **Base:** 12 damage, 1.5 s cooldown, 3 projectiles, proc coefficient 0.8.
- **Upgrade lines:** Damage +3, Size +20%, Projectiles +1, Knockback +25%, Projectile Speed +0.35.
- **Tomes:**
    - Cooldown: 1.5 s pause ÷ Attack Speed
    - Quantity: +1 orbiting rock per Quantity (starts with 3)
    - Duration: rocks orbit longer before resetting: 3 s × Duration, no cap
    - Projectile Speed: rocks orbit faster (base 1.5)
    - Knockback: base 2.5 × Knockback

#### Corrupted Sword

*Front and back slashes; more damage at low HP*

- **Base:** 12 damage, 0.8 s cooldown, proc coefficient 0.8.
- **Upgrade lines:** Damage +2, Size +15%, Projectiles +1, Projectile Speed +4.
- **Tomes:**
    - Cooldown: 0.8 s pause ÷ Attack Speed
    - Quantity: +1 slash per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 0.5 s → cap 5 s (cap reached at +900% Duration)
    - Projectile Speed: faster projectiles (base 30)
    - Knockback: base 2 × Knockback

#### Dexecutioner

*Piercing blade with an execute chance*

- **Base:** 9 damage, 0.8 s cooldown, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +20%, Projectiles +1, Crit +5%.
- **Tomes:**
    - Cooldown: 0.8 s pause ÷ Attack Speed
    - Quantity: +1 blade per Quantity (starts with 1)
    - Duration: no effect (its 0.5 s already sits at its 0.5 s cap)
    - Projectile Speed: no effect (a swing)
    - Knockback: base 1 × Knockback

#### Dice

*Rolls 1–6 damage; each 6 permanently adds Crit Chance*

- **Base:** 0 + roll of 1–6 damage, 0.5 s cooldown, 10% crit, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +15%, Projectiles +1, Crit +10%, Crit Damage +20%, Projectile Speed +0.2.
- **Tomes:**
    - Cooldown: 0.5 s pause ÷ Attack Speed
    - Quantity: +1 die per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 2 s → cap 5 s (cap reached at +150% Duration)
    - Projectile Speed: faster projectiles (base 0.6)
    - Knockback: base 2.5 × Knockback

#### Dragon's Breath

*Rotating flame that targets enemies*

- **Base:** 16 damage, 2.0 s cooldown, 1.5 s duration, proc coefficient 0.7.
- **Upgrade lines:** Damage +4, Size +15%, Duration +0.2.
- **Tomes:**
    - Cooldown: breathes more often (2 s base)
    - Quantity: no effect (has no projectile count)
    - Duration: each breath lasts longer: 1.5 s × Duration, no cap
    - Projectile Speed: no effect (a flame cone)
    - Knockback: base 0.5 × Knockback

#### Firestaff

*Explosive fireballs*

- **Base:** 10 damage, 0.5 s cooldown, proc coefficient 1.
- **Upgrade lines:** Damage +2.5, Size +16%, Projectiles +1, Projectile Speed +20%.
- **Tomes:**
    - Cooldown: 0.5 s pause ÷ Attack Speed
    - Quantity: +1 fireball per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 2 s → cap 5 s (cap reached at +150% Duration)
    - Projectile Speed: faster projectiles (base 0.5)
    - Knockback: base 1 × Knockback

#### Flamewalker

*Damaging fire trail*

- **Base:** 5 damage, none cooldown, proc coefficient 0.8.
- **Upgrade lines:** Damage +2, Size +15%, Projectiles +1, Duration +12%.
- **Tomes:**
    - Cooldown: fires its bursts faster (no pause between attacks)
    - Quantity: +1 fire patch per Quantity (starts with 1)
    - Duration: fire patches burn longer: 1.5 s → cap 8 s (cap reached at +433% Duration)
    - Projectile Speed: no effect (fire is left on the ground)
    - Knockback: no effect (base knockback 0)

#### Frostwalker

*Freezes and damages enemies nearby*

- **Base:** 9 damage, 1.25 s cooldown, proc coefficient 0.9.
- **Upgrade lines:** Damage +2, Size +10%, Duration +0.12.
- **Tomes:**
    - Cooldown: pulses come faster (1.25 s base)
    - Quantity: no effect (has no projectile count)
    - Duration: freezes last longer: 1.6 s × Duration, no cap
    - Projectile Speed: no effect (an aura)
    - Knockback: base 0.5 × Knockback

#### Hero Sword

*Front slash plus a ranged slash*

- **Base:** 11 damage, 0.75 s cooldown, proc coefficient 0.8.
- **Upgrade lines:** None listed.
- **Tomes:**
    - Cooldown: 0.75 s pause ÷ Attack Speed
    - Quantity: +1 slash per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 0.5 s → cap 5 s (cap reached at +900% Duration)
    - Projectile Speed: faster projectiles (base 30)
    - Knockback: base 2 × Knockback

#### Katana

*Fast slashes at the nearest enemy*

- **Base:** 11 damage, 0.4 s cooldown, proc coefficient 0.95.
- **Upgrade lines:** Damage +2.2, Size +20%, Projectiles +1, Crit +8%, Crit Damage +20%.
- **Tomes:**
    - Cooldown: 0.4 s pause ÷ Attack Speed
    - Quantity: +1 slash per Quantity (starts with 1)
    - Duration: no effect (its 0.5 s already sits at its 0.5 s cap)
    - Projectile Speed: no effect (a swing, nothing travels)
    - Knockback: base 1 × Knockback

#### Lightning Staff

*Lightning on nearby enemies; upgrades add chain bounces*

- **Base:** 7 damage, 1.1 s cooldown, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +20%, Projectiles +1, Bounces +1.
- **Tomes:**
    - Cooldown: 1.1 s pause ÷ Attack Speed
    - Quantity: +1 lightning strike per Quantity (starts with 1)
    - Duration: no effect (its 1 s already sits at its 1 s cap)
    - Projectile Speed: no effect (strikes from above)
    - Knockback: base 1 × Knockback

#### Mines

*Proximity mines*

- **Base:** 10 damage, 1.0 s cooldown, proc coefficient 0.8.
- **Upgrade lines:** Damage +3, Size +15%, Projectiles +1, Duration +0.4.
- **Tomes:**
    - Cooldown: 1 s pause ÷ Attack Speed
    - Quantity: +1 mine per Quantity (starts with 1)
    - Duration: mines stay armed longer: 4 s × Duration, no cap
    - Projectile Speed: no effect (mines sit still)
    - Knockback: base 4 × Knockback

#### Poison Flask

*Lasting poison zones*

- **Base:** 1 damage, 0.8 s cooldown, proc coefficient 0.9.
- **Upgrade lines:** Damage +0.5, Size +15%, Projectiles +1, Duration +1, Projectile Speed +2.
- **Tomes:**
    - Cooldown: 0.8 s pause ÷ Attack Speed
    - Quantity: +1 flask per Quantity (starts with 1)
    - Duration: poison pools last longer and poison stacks last longer: 3 s → cap 5 s (cap reached at +67% Duration)
    - Projectile Speed: flasks land sooner (base 16)
    - Knockback: base 1 × Knockback

#### Revolver

*Ricocheting bullets*

- **Base:** 5 damage, 1.4 s cooldown, 6 projectiles, 5% crit, proc coefficient 0.9.
- **Upgrade lines:** Damage +2.5, Projectiles +1, Crit +10%, Crit Damage +20%, Bounces +1, Projectile Speed +20%.
- **Tomes:**
    - Cooldown: 1.4 s pause ÷ Attack Speed, and shots inside a burst come faster
    - Quantity: +1 bullet per Quantity (starts with 6)
    - Duration: projectiles live longer, so they travel further: 1 s → cap 5 s (cap reached at +400% Duration)
    - Projectile Speed: faster projectiles (base 2)
    - Knockback: base 0.4 × Knockback
    - Size: bigger hit area, capped at ×4

#### Scythe

*360° sweep; elite kills charge a stronger attack*

- **Base:** 11 damage, 0.85 s cooldown, proc coefficient 0.8.
- **Upgrade lines:** Damage +1.5, Size +12%, Projectiles +1, Knockback +15%.
- **Tomes:**
    - Cooldown: 0.85 s pause ÷ Attack Speed
    - Quantity: +1 sweep per Quantity (starts with 1)
    - Duration: no effect (its 0.5 s already sits at its 0.5 s cap)
    - Projectile Speed: no effect (a sweep)
    - Knockback: base 1 × Knockback

#### Shotgun

*Spread burst*

- **Base:** 9 damage, 1.0 s cooldown, 5% crit, proc coefficient 1.
- **Upgrade lines:** Damage +3, Projectiles +1, Size +15%, Crit +10%, Crit Damage +20%.
- **Tomes:**
    - Cooldown: 1 s pause ÷ Attack Speed
    - Quantity: +1 blast per Quantity (starts with 1)
    - Duration: no effect (its 0.8 s already sits at its 0.8 s cap)
    - Projectile Speed: no effect (hits instantly)
    - Knockback: base 3 × Knockback

#### Slutty Rocket

*Homing missiles*

- **Base:** 11 damage, 0.3 s cooldown, 5% crit, proc coefficient 1.
- **Upgrade lines:** Damage +2, Projectiles +1, Crit +8%, Projectile Speed +20%.
- **Tomes:**
    - Cooldown: 0.3 s pause ÷ Attack Speed
    - Quantity: +1 rocket per Quantity (starts with 1)
    - Duration: no effect (its 5 s already sits at its 5 s cap)
    - Projectile Speed: rockets fly faster (base 1)
    - Knockback: base 2 × Knockback

#### Sniper Rifle

*Long-range piercing shot*

- **Base:** 22 damage, 1.0 s cooldown, 5% crit, proc coefficient 1.5.
- **Upgrade lines:** Damage +4, Projectiles +1, Size +13%.
- **Tomes:**
    - Cooldown: 1 s pause ÷ Attack Speed
    - Quantity: +1 shot per Quantity (starts with 1)
    - Duration: no effect (its 1 s already sits at its 1 s cap)
    - Projectile Speed: no effect (hits instantly)
    - Knockback: base 4 × Knockback

#### Space Noodle

*Links to an enemy and damages everything in between*

- **Base:** 10 damage, 1.0 s cooldown, proc coefficient 0.75.
- **Upgrade lines:** Damage +2, Size +20%, Duration +0.2.
- **Tomes:**
    - Cooldown: relinks sooner (1 s base)
    - Quantity: no effect (has no projectile count)
    - Duration: the beam stays linked longer: 4 s × Duration, no cap
    - Projectile Speed: no effect (a beam)
    - Knockback: base 0.5 × Knockback

#### Sword

*Sweeping slash through several enemies*

- **Base:** 11 damage, 0.75 s cooldown, proc coefficient 0.8.
- **Upgrade lines:** Damage +2, Size +20%, Projectiles +1, Knockback +25%.
- **Tomes:**
    - Cooldown: 0.75 s pause ÷ Attack Speed
    - Quantity: +1 slash per Quantity (starts with 1)
    - Duration: no effect (its 0.5 s already sits at its 0.5 s cap)
    - Projectile Speed: no effect (a swing)
    - Knockback: base 2 × Knockback

#### Tornado

*Tornadoes that knock enemies back*

- **Base:** 8 damage, 0.8 s cooldown, pierces all, proc coefficient 1.
- **Upgrade lines:** Damage +2, Size +14%, Projectiles +1, Knockback +20%, Projectile Speed +20%.
- **Tomes:**
    - Cooldown: 0.8 s pause ÷ Attack Speed
    - Quantity: +1 tornado per Quantity (starts with 1)
    - Duration: tornadoes last longer: 1.2 s → cap 5 s (cap reached at +317% Duration)
    - Projectile Speed: faster projectiles (base 20)
    - Knockback: base 3 × Knockback

#### Wireless Dagger

*Homing daggers that bounce*

- **Base:** 9 damage, 0.5 s cooldown, 1 bounce, proc coefficient 0.9.
- **Upgrade lines:** Damage +2, Projectiles +1, Bounces +1, Projectile Speed +15%.
- **Tomes:**
    - Cooldown: 0.5 s pause ÷ Attack Speed
    - Quantity: +1 dagger per Quantity (starts with 1)
    - Duration: projectiles live longer, so they travel further: 2.5 s → cap 8 s (cap reached at +220% Duration)
    - Projectile Speed: faster projectiles (base 0.75)
    - Knockback: base 0.4 × Knockback
    - Size: bigger hit area, capped at ×3.5

