# Enemies

## How enemy stats scale

**Enemy HP** (`EnemyStats.GetHp`):

base HP × tier multiplier × (1 + time + final swarm + stage + 1.1 × Difficulty) × type × your Enemy HP multiplier

| Part | Value |
|---|---|
| Tier | ×0.80 (T1), ×0.95 (T2), ×1.05 (T3 and Graveyard) |
| Time | +0.10 per minute of the run × Enemy scaling multiplier |
| Final swarm | +(4^(swarm minutes) − 1) |
| Stage | Stage 1: +0. Stage 2: +27 × (1 + 0.45 × Difficulty). Stage 3: +145 × (1 + 0.45 × Difficulty) |
| Type | Elite ×10, challenge ×7, elite challenge ×15; bosses ×2.5 on stage 2, ×5 on stage 3, and ×(1 + 0.16 × Boss Curses) |
| Swarm spawns | ×1.3 more |

**Enemy damage** (`EnemyStats.GetDamage`):

base damage × tier multiplier × (1 + 0.028 per minute × Enemy scaling + (2^(swarm minutes) − 1) + stage + Difficulty) × 1.5 for elites × your Enemy damage multiplier

> **Example:** a Red Ghost (30 base damage) on a Tier 3 run (×1.1), 50 minutes into the run, 12 minutes into a stage 3 final swarm, at 1,040% Difficulty (10.4):
>
> 1. Time: 0.028 × 50 = 1.4
> 2. Final swarm: 2¹² − 1 = 4,095
> 3. Stage 3: +4. Difficulty: +10.4
> 4. 30 × 1.1 × (1 + 1.4 + 4,095 + 4 + 10.4) = 33 × 4,111.8 = **about 135,700 damage per hit**
>
> Almost all of it comes from the final-swarm term, which doubles every minute.


The stage part for damage is +2 on stage 2 and +4 on stage 3.

Worked example, Tier 3, Difficulty 0.5, an ordinary enemy:

| Moment | HP multiplier |
|---|---|
| Stage 1 at 5:00 | 1.05 × (1 + 0.5 + 0.55) = 2.2× |
| Stage 1 at 10:00 (swarm start) | 1.05 × (1 + 1.0 + 0.55) = 2.7× |
| Stage 2 start, run minute 12 | 1.05 × (1 + 1.2 + 33.1 + 0.55) = 37.6× |
| Stage 3 start, run minute 22 | 1.05 × (1 + 2.2 + 177.6 + 0.55) = 190× |

Some special enemies have HP tied to your level instead: (level + 25) × 20, or level + 30.

## Every enemy

Base values from the game's enemy database, before scaling. Credits are what the spawner pays for one; cheaper enemies come in larger numbers.

| Enemy | Map | HP | Damage | Speed | Credits | Flying | Elite? | Executable | Knockback res. | Special attacks |
|---|---|---|---|---|---|---|---|---|---|---|
| Goblin | Forest | 7 | 15 | 5.0 | 1 | | ✓ | ✓ | 0 | |
| Strong Goblin | Forest | 15 | 25 | 5.5 | 1.25 | | ✓ | ✓ | 0 | |
| Goblin Tank | Forest | 40 | 30 | 5.0 | 2 | | ✓ | ✓ | 1 | |
| Golem | Forest | 20 | 20 | 5.0 | 1.5 | | ✓ | ✓ | 1 | |
| Slime | Forest | 6 | 8 | 6.5 | 0.75 | | ✓ | ✓ | 0 | |
| Bee | Forest | 10 | 15 | 6.5 | 1 | ✓ | ✓ | ✓ | 0 | |
| Boomer Spider | Forest | 18 | 30 | 6.0 | 1.5 | | ✓ | ✓ | 0 | Explodes |
| Stone Golem (miniboss) | Forest | 250 | 40 | 6.0 | 40 | | ✓ | ✓ | 4 | Stone attacks |
| Chunkham the Terrible (miniboss; "Pig" in the game files) | Forest | 250 | 40 | 6.0 | 40 | | ✓ | ✓ | 3 | Slam, mud splash |
| Mummy | Desert | 8 | 13 | 5.5 | 1 | | ✓ | ✓ | 0 | |
| Mummy Tank | Desert | 45 | 30 | 5.0 | 2 | | ✓ | ✓ | 1 | |
| Ancient Mummy | Desert | 70 | 40 | 5.0 | 2.5 | | ✓ | ✓ | 1 | |
| Scorpion | Desert | 16 | 20 | 7.0 | 1.2 | | ✓ | ✓ | 0 | |
| Medium Scorpion | Desert | 30 | 30 | 6.5 | 1.1 | | ✓ | ✓ | 0 | |
| Dusty Skeleton | Desert | 16 | 22 | 6.5 | 2 | | ✓ | ✓ | 0 | |
| Armored Dusty Skeleton | Desert | 25 | 16 | 4.5 | 3 | | ✓ | ✓ | 0 | |
| Tumblebone | Desert | 7 | 9 | 11.0 | 1 | | ✓ | ✓ | 0 | |
| Wisp | Desert | 8 | 13 | 7.5 | 1 | ✓ | ✓ | ✓ | 0 | |
| Cactus Shooter | Desert | 15 | 30 | 5.0 | 1 | | ✓ | ✓ | 0 | Projectile |
| Sand Golem (miniboss) | Desert | 250 | 40 | 6.0 | 40 | | ✓ | ✓ | 4 | Stone attacks |
| Scorpion (miniboss) | Desert | 250 | 35 | 7.0 | 40 | | ✓ | ✓ | 3.5 | Spikes |
| Ghost | Graveyard | 10 | 10 | 6.0 | 1 | ✓ | ✓ | ✓ | 0 | |
| Greater Ghost | Graveyard | 20 | 13 | 7.0 | 1.5 | ✓ | ✓ | ✓ | 1 | |
| Purple Ghost | Graveyard | 40 | 20 | 8.0 | 1.5 | ✓ | ✓ | ✗ | 5 | |
| Red Ghost | Graveyard | 100 | 30 | 10.0 | 1.5 | ✓ | ✓ | ✗ | 50 | |
| Head | Graveyard | 12 | 8 | 7.0 | 1 | ✓ | ✓ | ✓ | 0 | |
| Zombie | Graveyard | 12 | 20 | 6.5 | 1 | | ✓ | ✓ | 0 | |
| Ghostham (miniboss) | Graveyard | 320 | 45 | 6.5 | 40 | ✓ | ✗ | ✓ | 3 | Slam, mud splash |
| Calcium Dad (miniboss) | Graveyard | 320 | 40 | 8.0 | 40 | | ✓ | ✓ | 4 | Bone pillars, laser |
| Grave Ghosts 1–4 (coffin fight) | Graveyard | 1,100 / 2,250 / 5,500 / 9,000 | 20–35 | 7.0 | 1 | ✓ | ✗ | ✗ | 1–4 | |
| Skeleton | Forest, Graveyard | 20 | 20 | 5.5 | 1 | | ✓ | ✓ | 0 | |
| Armored Skeleton | Forest, Graveyard | 30 | 25 | 4.0 | 1.5 | | ✓ | ✓ | 0 | |
| Ghoul | Forest, Graveyard | 9 | 12 | 9.0 | 1 | | ✓ | ✓ | 0 | |
| Golden / XP Skeleton | Special | 50 | 25 | 6.0 | 10 | | ✗ | ✓ | 0 | |
| Ent (final boss, 3 phases) | Forest | 9,000 / 8,000 / 10,000 | 40 / 40 / 22 | 7 / 7 / 3 | 40 | | ✗ | ✓ | 2 / 2 / 999 | Root attacks |
| Pharaoh (final boss, 3 phases) | Desert | 8,000 each | 40 | 7 / 7 / 3 | 40 | | ✗ | ✓ | 2 / 2 / 999 | Lasers, pillars |
| Ghost King (final boss) | Graveyard | 500,000 | 40 | 10.0 | 40 | ✓ | ✗ | ✗ | 999 | Darkness, roots, spikes |
| Bandit (character fight) | Desert | 11,000 | 50 | 10.0 | 40 | | ✗ | ✓ | 4 | |
| Bush (character fight) | Forest | 10,000 | 45 | 8.5 | 40 | | ✗ | ✓ | 2 | |
| Frogs (egg event) | Any | 1,000 | 1 | 9–10 | 99 | | ✗ | ✓ | 1 | |

Elite enemies are ×10 HP and ×1.5 damage. "Executable" ✗ means executes deal 2% of max HP instead of killing. Skeleton, Armored Skeleton and Ghoul are listed for both Forest and Graveyard in the enemy data's map flags.

**XP per kill:** every enemy in the data is worth **1 XP**, and elites 10 (× your XP gain). Tougher enemies don't give more XP, so kill count is what levels you.

### When each enemy can join

A stage starts with one enemy type (Goblin on Forest, Mummy on Desert, Ghost on Graveyard). Every 60 seconds another one from the map's list joins the spawn pool, picked at random from those whose earliest time has passed (`SummonerController.TryAddNewEnemyCard`):

| Map | From the start | After 1:30 | After 3:00 | After 6:00 | After 7:00 | After 12:00 |
|---|---|---|---|---|---|---|
| Forest | Strong Goblin, Slime, Bee, Boomer Spider, Skeleton, Ghoul | Golem, Armored Skeleton | Goblin Tank | — | — | — |
| Desert | Scorpion, Dusty Skeleton, Tumblebone, Wisp, Cactus Shooter | Armored Dusty Skeleton | Mummy Tank, Medium Scorpion | Ancient Mummy | — | — |
| Graveyard | Head, Zombie, Skeleton, Ghoul | Armored Skeleton | Greater Ghost | — | Purple Ghost | Red Ghost |

So the Graveyard's normal spawns, not just its swarm events, start sending Purple Ghosts at 7:00 and Red Ghosts at 12:00 of the 16-minute stage.

## Boss attacks

From each boss's attack list in the enemy data. **Damage** is a multiple of the boss's normal hit (which scales like any enemy's damage). **Cooldown** is how long before that attack can repeat; **gap** is the minimum pause before the boss starts its next special attack.

### Ent (Forest final boss)

| Attack | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Continuous roots (chase you along the ground) | 15 s, ×1.0 | 13 s, ×1.0 | 13 s, ×0.85 |
| Three lines of roots | 8 s, ×1.0 | off | 8 s, ×0.85 |
| Single line of roots | 12 s, ×1.0 | 12 s, ×1.0 | 12 s, ×0.85 |
| Predictive root (aims where you're going) | 12 s, ×1.0 | 12 s, ×1.0 | 12 s, ×0.85 |
| Close burst (only within 15 of the boss) | 10 s, ×1.0 | 10 s, ×1.0 | 10 s, ×0.85 |
| Gap between attacks | 3 s | 2.5 s | 2.25 s |

Wind-ups get shorter each phase (about 1 s, then 0.85–0.9 s, then 0.7–0.8 s), and the root areas get wider. Phase 3 is slow on its feet (speed 3 instead of 7) but attacks the most often.

### Pharaoh (Desert final boss)

| Attack | Cooldown | Damage | Notes |
|---|---|---|---|
| Disco lasers | 25 s | ×0.15 per hit | Lasts 14–15 s |
| Targeted laser | 40 s / 30 s / 45 s by phase | ×0.05 per hit | Lasts 8 s, then 5 s of recovery |
| Predictive pillars | 15 s | ×0.75 | Several pillars aimed ahead of you |
| Pillar circles | 15 s | ×0.75 | Rings of pillars |

The gap between attacks shrinks each phase: 6–8 s, then 3.5–5 s, then 2–3 s. Phase 3 moves at speed 3.

### Ghost King (Graveyard final boss, "Big Bob")

| Attack | Cooldown | Damage | Notes |
|---|---|---|---|
| Darkness | 30–50 s | ×1.0 | First one 15 s into the fight; 6.5 s wind-up |
| Ghost roots | 15–30 s | ×0.85 | Chases you along the ground |
| Ghost spikes | 15–30 s | ×0.8 | Several at once, 1.5 s wind-up |

### Character fights and minibosses

| Boss | Attack | Cooldown | Damage |
|---|---|---|---|
| Bandit | Dash strike (within 15) | 10 s | ×0.8 |
| Bush | Sniper shot (any range) | 12 s | ×0.8, 2.5 s recovery after |
| Ghostham | Slam (within 14), mud splash, predictive mud splash | 5 s each | ×1.0 / ×0.7 / ×0.7 |
| Stone Golem (Forest) | Close stone attack (within 17), continuous stones | 8 s / 16 s | ×1.0 / ×0.75 |
| Chunkham (Forest) | Slam (within 14), mud splash, predictive mud splash | 5 s each | ×1.0 / ×0.7 / ×0.7 |
| Sand Golem (Desert) | Stone attack (within 17), continuous stones | 8 s / 16 s | ×1.0 / ×0.75 |
| Scorpion (Desert) | Spike volley, predictive spikes, hitscan spikes | 16 s / 12 s / 12 s | ×0.8 / ×1.0 / ×0.8 |
| Calcium's Dad (Graveyard) | Predictive bone pillars, pillar circles, targeted laser | 15 s / 15 s / 40 s | ×0.75 / ×0.75 / ×0.05 per hit |
