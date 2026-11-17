# Megabonk Data: the numbers behind the game

A wiki of how Megabonk actually works, read straight from the game's code. Every formula here comes from Megabonk v1.0.69's compiled code (GameAssembly.dll, decompiled with Il2CppDumper and a disassembler) and from the game's own item, weapon, tome, character, enemy and map database, dumped from memory. Nothing is guessed from videos or wikis unless a line says so.

Updated DATE · Game version 1.0.69

## What's in here

| Page | What it covers |
|---|---|
| [How the game works](game.html) | What a run is, the goal, the core loop, how maps are generated and what sets Megabonk apart |
| [Core math](mechanics.html) | How every stat is calculated, the three damage brackets, crits and overcrits, proc chances, armor, evasion, XP per level |
| [Status effects](status.html) | Poison, burn, freeze, stun, Bloodmark, charm, execute |
| [Maps & stages](maps.html) | Forest, Desert and Graveyard; tiers; every stage's timeline; spawn rates; the final swarm and its ghosts; bosses and Boss Curses |
| [Enemies](enemies.html) | Every enemy's base stats, and the HP and damage formulas that scale them |
| [Map secrets & fights](secrets.html) | Frog eggs, Bush, Bandit, Spooky Steve, Big Bob, coffins, the crypt and every hidden object |
| [Luck, chests & shrines](economy.html) | Luck odds, chest prices, free chests from kills, powerups, pots, Microwaves, Shady Guys, every shrine, Banish/Refresh/Skip and the Silver shop |
| [Items](items.html) | Every item with what its code does |
| [Weapons](weapons.html) | Base stats, attacks per second, proc rates, and how every tome changes every weapon |
| [Tomes](tomes.html) | Every tome, rarity multipliers, the per-level values, and which weapons each tome affects |
| [Characters](characters.html) | Starting stats, per-level passives, how Dicehead's Gamba really scales |
| [FAQ & map limits](faq.html) | How many shrines, Bald Heads and chests a map can have; what Luck does and doesn't affect |
| [Quests & unlocks](quests.html) | Every quest, what it unlocks and the Silver it pays |
| [Challenges](challenges.html) | All 55 challenges with exact rules, Silver bonus and requirements |
| [Hats & skins](cosmetics.html) | All 22 hats and 112 skins and how to get them |
| [Tier lists](tiers.html) | Items and characters ranked by what 500k+ leaderboard runs actually use |
| [Maxing a run](max-runs.html) | A short strategy built on the data: luck and chests, Boss Curses, the final swarm and the 12–13 minute ghost wall |

## The ten facts that matter most

1. **Damage comes in three brackets that multiply:** items add to a flat bracket, shrine stat offers add to a % bracket, and the Damage Tome is its own multiplier. ([Core math](mechanics.html))
2. **Crit chance past 100% overcrits,** and the multiplier grows quadratically: 1 crit ×2, 2 ×4, 3 ×6.25, 4 ×9.
3. **Most proc items have diminishing returns built in.** Dragonfire, Ice Cube, Lightning Orb, Power Gloves and Key use x / (x + k), so the 10th copy adds far less than the first.
4. **Enemy HP in the final swarm multiplies by 4 every minute,** and their damage doubles every minute. Damage alone stops keeping up around 12:00; long runs get past it with stacked on-hit items (Overpowered Lamp, Big Bonk), percent-HP damage (Cursed Doll), Za Warudo and Evasion.
5. **The ghost wall is a code switch.** The final swarm swaps in tougher ghosts at 1, 6 and 12 minutes. At 12:00 come Red Ghosts: 100 base HP, speed 10, can't be executed, and Bob's Light only kills them a third of the time.
6. **Stage 2 enemies start at about 30× base HP and stage 3 at about 150×.** Time adds +10% HP per minute of the whole run.
7. **Every boss and miniboss drops a free chest, and each Boss Curse adds one more of each:** one more miniboss per miniboss event and one more stage boss, each 16% tougher. That's +3 free chests per curse on a Forest stage.
8. **Chest prices depend only on how many chests you've opened,** never on time: 30, 72, 115 … 569 at 10, then a jump to 952 at chest 11.
9. **Luck has diminishing returns but no ceiling.** Legendary chests go from 1.6% at 0 Luck to 4.7% at 100%, 33% at 1,000% and 90% at 40,000%, which long Graveyard runs reach.
10. **Dicehead's Gamba fades:** each level-up's free stat is worth 75% of a Common offer at level 1, 37.5% at level 50 and only 6% from level 300 on.

## How to read the numbers

- **n** means the number of copies of an item you hold.
- **Proc coefficient** is a per-weapon number that scales most on-hit chances (from the weapon data: Sniper Rifle 1.5; Bow, Bone, Dice, Firestaff and others 1.0; Katana 0.95; Revolver, Wireless Dagger, Frostwalker, Poison Flask 0.9; the swords, Chunkers, Mines, Flamewalker 0.8; Space Noodle 0.75; Axe, Aura, Black Hole, Dragon's Breath 0.7).
- **Base damage** is a separate player number, 8 + your level, used by many items and status effects instead of your weapon's damage.
- **Luck 1.0 = 100%.** The game stores percentages as fractions.
- Where something was only partly traced in the code, the page says so.
