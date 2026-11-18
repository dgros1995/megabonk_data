# Maps & stages

## Maps and tiers

| Map | Stages | Stage timers | Chests | Shrines | Pots & other | Final boss |
|---|---|---|---|---|---|---|
| Forest | 3 | 10:00, 9:00, 8:00 | ×1 | ×1 | ×1 | Ent (three phases: 9,000 / 8,000 / 10,000 base HP) |
| Desert | 3 | 10:00, 9:00, 8:00 | ×1 | ×1 | ×1 | Pharaoh (three phases, 8,000 base HP each) |
| Graveyard | 1 | 16:00 | ×1.5 | ×2 | ×1.5 (pumpkins instead of pots) | Ghost King (500,000 base HP) |

**Tiers set how many stages you play.** The game ends the tier on stage index = tier index (`MapController.IsTierFinalStage`): Tier 1 is stage 1 only, Tier 2 is stages 1–2, Tier 3 is all three stages. After the tier's last stage comes the final-boss map.

**Tiers also scale enemies** (`RunConfig.GetEnemyHp` / `GetEnemyDamage`):

| Tier | Enemy HP | Enemy damage |
|---|---|---|
| Tier 1 | ×0.80 | ×0.75 |
| Tier 2 | ×0.95 | ×0.95 |
| Tier 3 | ×1.05 | ×1.10 |
| Graveyard (always) | ×1.05 | ×1.10 |

## Stage timelines

Each stage runs a fixed script from the map data. Times count up from the start of the stage. A new enemy type joins the pool every 60 seconds.

**Which miniboss you get:** every miniboss event draws from the map's miniboss list without repeats until the list is used up, then starts over (`SummonerController.EventMiniboss`). Forest: Stone Golem and Chunkham the Terrible. Desert: Sand Golem and Scorpion. Graveyard: Calcium's Dad and Ghostham. So on stage 1 the 3:00 and 8:00 minibosses are always the two different ones, in random order.

### Forest

| Stage 1 (10:00) | Stage 2 (9:00) | Stage 3 (8:00) |
|---|---|---|
| Start: Goblin | Start: Goblin | Start: Goblin |
| 3:00 Miniboss, 30 s | 2:00 Miniboss, 15 s | 1:30 Miniboss, 30 s |
| 4:00 Swarm: Goblins, 30 s | 3:00 Swarm: Goblins, 30 s | 2:30 Swarm: Goblins, 30 s |
| 7:00 Swarm: Strong Goblins, 30 s | 6:00 Swarm: Strong Goblins, 30 s | 4:00 Swarm: Strong Goblins, 30 s |
| 8:00 Miniboss, 30 s | 7:00 Miniboss, 45 s | 5:00 Miniboss, 45 s |
| 10:00 Final swarm | 9:00 Final swarm | 8:00 Final swarm |

Forest enemies: Goblin, Strong Goblin, Goblin Tank, Golem, Slime, Bee, Boomer Spider; minibosses Stone Golem and Chunkham the Terrible.

### Desert

| Stage 1 (10:00) | Stage 2 (9:00) | Stage 3 (8:00) |
|---|---|---|
| Start: Mummy | Start: Mummy | Start: Mummy |
| 3:00 Miniboss, 30 s | 2:00 Miniboss, 30 s | 1:30 Miniboss, 30 s |
| 4:00 Swarm: Mummies, 30 s | 3:00 Swarm: Mummies, 30 s | 2:30 Swarm: Mummies, 30 s |
| 7:00 Swarm: Scorpions, 30 s | 6:00 Swarm: Scorpions, 30 s | 4:00 Swarm: Scorpions, 30 s |
| 8:00 Miniboss, 60 s | 7:00 Miniboss, 30 s | 5:00 Miniboss, 30 s |
| 10:00 Final swarm | 9:00 Final swarm | 8:00 Final swarm |

Desert enemies: Mummy, Mummy Tank, Ancient Mummy, Scorpion, Medium Scorpion, Dusty Skeleton, Armored Dusty Skeleton, Tumblebone, Wisp, Cactus Shooter; minibosses Sand Golem and Scorpion. Desert has sandstorms and Desert Graves (summon fights).

### Graveyard

One 16-minute stage, and it always uses Tier 3 enemy scaling.

| Time | Event |
|---|---|
| Start | Ghosts |
| 3:00 | Miniboss |
| 4:00 | Swarm: Ghosts |
| 7:00 | Miniboss |
| 8:00 | Swarm: Greater Ghosts |
| 10:00 | Miniboss |
| 11:00 | Swarm: Purple Ghosts |
| 13:00 | Miniboss |
| 14:00 | Swarm: Red Ghosts |
| 16:00 | Final swarm |

Graveyard specials:

- **Bald Heads** is the game's name for the **Balance Shrine** (`InteractableShrineBalance`). It offers stat trades built from a doubled stat (×2) and a halved one (×0.5).
- **Coffins** start a boss-ghost fight with the Grave Ghosts (1,100 / 2,250 / 5,500 / 9,000 base HP, can't be executed).
- **Gravestones** give +10% XP gain and +5% Difficulty when used (22 per map).
- More of everything: 1.5× chests, 2× shrine slots, 1.5× Charge and Greed Shrines. Instead of pots it has 105 pumpkins, plus 4, 6 or 8 Microwaves ([map limits](faq.html)).

## Timers

| Timer | Resets | Used for |
|---|---|---|
| Stage timer | Every stage | The stage script and the spawn ramp |
| Run (difficulty) timer | Only on a new run; pauses on the final-boss map | Enemy HP +10% and damage +2.8% per minute |
| Final-swarm timer | Every stage; only runs during the final swarm | Final-swarm HP and damage, ghost tiers |

So time scaling carries across stages: an enemy on stage 2 at run minute 15 gets +150% HP from time alone.

## Spawning

**Enemies wanted on the map during a stage** (`StageSummoner.GetNumTargetEnemies`):

(5 + 200 × stage progress) × (1 + 0.7 × Difficulty + 0.4 × stage index) × Enemy amount

Stage progress runs from 0 to 1 over the stage timer, so the field fills from 5 to 205 × the multiplier. The hard cap is **550 enemies**.

**During the final swarm** (`SwarmSummoner.GetNumTargetEnemies`): min(2.5 per second of swarm, cap) × the same multiplier. The cap is **400 for the first 2 minutes, then 300**.

During a mid-stage swarm event, normal spawns stop and the swarm enemy spawns instead; during a miniboss event normal spawns slow to 25%.

## The final swarm

It starts when the stage boss dies or the stage timer runs out, whichever comes first (after a short grace period).

- **Enemy HP gains +(4^(swarm minutes) − 1)** and damage **+(2^(swarm minutes) − 1)**, on top of everything else. Swarm spawns also get ×1.3 HP and ×1.2 speed.

| Minutes into the swarm | 1 | 2 | 3 | 5 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|
| HP bonus | +3 | +15 | +63 | +1,023 | +4,095 | +65,535 | +1.0M | +16.8M |
| Damage bonus | +1 | +3 | +7 | +31 | +63 | +255 | +1,023 | +4,095 |

- **The swarm enemy changes on a fixed clock** (`SwarmSummoner.TickExtra`):

| Swarm time | Ghost | Base HP | Base damage | Speed | Can be executed | Knockback resistance |
|---|---|---|---|---|---|---|
| 0:00 | Ghost | 10 | 10 | 6 | Yes | 0 |
| 1:00 | Greater Ghost | 20 | 13 | 7 | Yes | 1 |
| 6:00 | Purple Ghost | 40 | 20 | 8 | No | 5 |
| 12:00 | Red Ghost | 100 | 30 | 10 | No | 50 |

The 12:00 switch is the "ghost wall" players hit around 12–13 minutes. See [Maxing a run](max-runs.html).

## Bosses and Boss Curses

- Using a **Boss Curse shrine** adds 1 to a counter on the stage's game manager (`GameManager.bossCurses`). Nothing in the code carries it over, and recorded runs matched a per-stage count (2 curses → 3 Chunkhams on stage 1; 5 curses → 6 Stone Golems on stage 2).
- **Every miniboss event spawns 1 + curses minibosses**, and **the stage boss spawns as 1 + curses bosses**.
- **Every boss has its HP multiplied by 1 + 0.16 × curses.**
- Boss HP also gets a stage multiplier: ×2.5 on stage 2 and ×5 on stage 3.
- Bosses can't be killed by Bob's Light or executes; Cursed Doll only does 0.7 × (8 + level) to them.
