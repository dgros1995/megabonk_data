# Status effects

All debuffs tick **2 times per second** (`DebuffUtility.debuffTicksPerSecond = 2`). Their length in ticks is round(2 × duration × Duration multiplier). Re-applying a debuff lengthens it only if the new duration is longer than what's left; the two never add up.

## Poison

- **Damage per tick = stacks × Damage × Poison damage**, never less than 1 per stack. Two ticks a second.

> **Example:** an enemy has 10 poison stacks, your Damage stat is ×2.0 and your Poison damage is ×1.0. Each tick deals 10 × 2.0 × 1.0 = **20**, twice a second, so 40 damage per second for as long as the stacks last.

- **No stack cap.** Every application adds stacks.
- Not affected by crits, weapon damage or boss damage. Reduced by enemy armor; boosted by Elite damage against elites.
- Can't trigger on-hit items (proc coefficient 0).

| Source | Stacks added | How long the poison lasts |
|---|---|---|
| Moldy Cheese | 40% chance per copy per hit (each full 100% is a guaranteed stack) | 5 s |
| Snek | 4 per copy per hit | 5 s |
| Toxic Barrel | 5 per copy to enemies near you, when you get hit | 5 s |
| Moldy Gloves | 10 per copy to enemies within 15, once every 8.5 s | — |
| Plague (Amog) | Spreads poison from dying enemies; +1% poison damage per level | — |
| Poison Flask | Weapon: leaves poison zones | — |

**The duration is how long the poison keeps ticking** (× your Duration stat). Each new application adds its stacks and restarts the clock if its duration is longer than what's left, so an enemy you keep hitting stays poisoned and its stacks keep growing. Stop hitting it and all its stacks wear off together when the timer runs out.

> **Example:** Snek ×2 adds 8 stacks per hit. Hit an enemy 3 times in a second and it has 24 stacks, and the 5 s clock restarts on each hit. If you stop, the 24 stacks keep ticking for 5 more seconds, then vanish.

## Burn

- One hit **every second** (every other tick) for (8 + level) × Damage × 0.85.
- Lasts 3 s × Duration from Dragonfire. Doesn't stack: one burn per enemy.

## Freeze

- 3 s from Ice Cube; 2.5 + 0.1 per copy (max 6) from Ice Crystal.
- The freeze slow value is 0.3. Noelle gets +1.5% damage per frozen enemy.

## Stun

- 3 s from Lightning Orb and Thunder Mitts.

## Bloodmark

- Stacks on an enemy. Each stack is worth **0.75 × (8 + level) × Damage**.
- When the stored damage is at least the enemy's current HP, the mark pops and deals all of it at once: effectively an execute that scales with stacks.
- Sources: Bloody Cleaver (50% per copy, plus every lifesteal proc), Unstable Transfusion (35% per copy), Slurp Gloves.

## Charm

- Weeb Headset: 0.1 × 0.02n / (0.02n + 4) chance (tiny), lasts 5 + 1.5n s. The item's code exists, but it isn't in the game's item list in 1.0.69, so it can't drop.

## Execute

- Executable non-boss enemies die outright. Bosses and non-executable enemies (Purple and Red Ghosts, Graveyard boss ghosts, some others) take 2% of max HP instead.
