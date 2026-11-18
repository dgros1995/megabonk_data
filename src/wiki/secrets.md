# Map secrets & special fights

Hidden objects, one-off bosses and events on each map, from the game's interactable code (`Interactable*` classes), its enemy data and its quest text. Where the code doesn't say where something spawns, this page says so instead of guessing.

## Special fights

| Fight | Where | Base HP | Damage | Speed | What it gives |
|---|---|---|---|---|---|
| **Bush** | Forest: shake the "sus bush" | 10,000 | 45 | 8.5 | Unlocks the Bush character |
| **Bandit** | Desert: find and defeat him (the map has a Bandit statue) | 11,000 | 50 | 10 | Unlocks the Bandit character |
| **Desert Graves** | Desert: "Disturb grave" | Spawns a boss | — | — | A shrine rises where the boss dies |
| **Skeleton King statue** | Desert: touch the statue to summon the undead boss | — | — | — | As Calcium on Desert Tier 2, unlocks the Graveyard |
| **Scorpionussy** | Desert miniboss | 250 | 35 | 7 | Kill it 3 times to unlock Poison Flask |
| **Coffins (Jeff, Mike, Ted, Gary)** | Graveyard: "Open coffin" | 1,100 / 2,250 / 5,500 / 9,000 | 20–35 | 7 | Ghost bosses that can't be executed |
| **Big Bob (Ghost King)** | Graveyard boss room | 500,000 | 40 | 10 | The Graveyard's final boss; lamps in the room can damage him |
| **Spooky Steve** | A ghost; where it spawns isn't in the code I traced | 2,147,483,647 | 2,147,483,647 | 6.5 | Unlocks Roberto (a Cooked quest) |

Spooky Steve's HP and damage are the largest number a 32-bit integer can hold, so he's built to be effectively unkillable and to one-shot you. His knockback resistance is 10 billion.

The Bush and Bandit fights are character fights: they use the character's model and moves.

## Frog eggs

- Breaking an egg ("Break egg") spawns **3 frogs that run away from you** (`InteractableEgg`). They're on the minimap.
- Frogs have 1,000 base HP, deal 1 damage, and are fast: green 9, blue 9.5, red 10.
- **Kill all 3 frogs from the egg to get one chest.** The game keeps a list of the egg's frogs and removes each one as it dies; the chest spawns where the last frog dies, only once that list is empty (`InteractableEgg.OnEnemyReleasedFromPool` → `EffectManager.SpawnChest`).
- Killing them also counts toward the frog hats: find the frogs on Forest stage 1 (green), stage 2 (blue) and stage 3 (red).

## Hidden objects

| Object | Map | What it does |
|---|---|---|
| **Shiny banana** | Forest | Touch it to get the Bananarang straight away (and unlock it for good) |
| **Golden key + cage** | Forest | The Golden key ("I wonder what it opens...") opens Monke's cage. Releasing him unlocks Monke |
| **Hidden present** | Forest | Open it for the Santa hat |
| **Boomboxes** | Forest | Activate all of them to unlock the Boombox shop item (pick your own music) |
| **Tumbleweeds** | Desert | Roll around the map. Breaking one gives Silver and some XP. They're also the only source of the Katana (5% on stage 1) and Shotgun (5% on stage 2) unlocks |
| **Sandstorms** | Desert | Charging a Charge Shrine during a sandstorm unlocks Tornado. Getting carried by a tornado counts toward Birdo's unlock |
| **Gravestones** | Graveyard | Each one gives +10% XP gain and +5% Difficulty, adds score, and can spawn an enemy |
| **Crypt** | Graveyard | Open it with the **Crypt Key**, which drops on the map; the crypt is where you go to fight the final boss. It also has extra chests and pots. Snek is found in it, and opening every chest and pot in it unlocks Pot (Stainless Steel). The key stays in your inventory until you use it, which is why 40% of Graveyard leaderboard runs still list it: they never went to fight the boss. |
| **Pumpkins** | Graveyard | Breakable like pots. Breaking all of them as Roberto unlocks Pumpkin |

## Named bosses and minibosses

The game's own names for its bosses:

| Enemy | In-game name |
|---|---|
| Ent phases 1–3 (Forest final boss) | Lil Bark, Chadbark, Bark Vader |
| Pharaoh phases 1–3 (Desert final boss) | Lil' Anubis, Anubruh, Juge Anubis |
| Ghost King (Graveyard final boss) | Big Bob |
| Pig miniboss (Forest) | Chunkham the Terrible |
| Golem miniboss | Stone Golem |
| Desert scorpion miniboss | Scorpionussy |
| Graveyard minibosses | Ghostham the Dead, Calcium's Dad |
| Greater Ghost | Black Ghost |

## Unused content in the game files

Things in the 1.0.69 files that the game never offers:

| What | Details |
|---|---|
| **A "Hell" map** | Has its own stage data (desert trees, dark rocks, fire effects, columns and walls) and a Moai-only shrine list, but isn't in the game's list of playable maps. The enemy data even has a map flag for it, though no enemy uses it. |
| **Three tomes** | Balance, Gambler and Hoarder exist but are switched off. Hoarder would spawn chests, Gambler would give shrine-style stat offers. |
| **Weeb Headset** | Item code with a tiny charm chance, but no item entry, so it can't drop. |
| **Test enemies** | "Test" and "Test2", one with 2,147,483,647 HP. |

The "Dungeon" map in the files is the Graveyard's crypt, which is real and playable.
