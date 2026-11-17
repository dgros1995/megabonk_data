# Characters

Each character has a starting weapon and a passive that grows every time you level up, so a passive matters more the higher your level gets. A 1M-kill run reaches level 3,000 or more.

## All characters

| Character | Starting weapon | Starting stats (game data) | Passive, per level (game data) | Unlock |
| --- | --- | --- | --- | --- |
| Dicehead | Dice | +5% Evasion, +5% Crit, +5 Pickup Range, +5% Gold | **Gamba:** a free random stat each level, worth 0.75 / (1 + (level/50)^1.5) of a Common offer (min 0.06) | Complete 100 quests, then buy |
| Fox | Firestaff | +15% Luck, +5% Evasion, +4% Speed, +4 Pickup Range, +1 Jump Height | **RNG Blessing:** +1.5% Luck | Default |
| Sir Oofie | Sword | +50 HP, +15% Armor, −2% Speed | **Fortified:** +1% Armor | Default |
| CL4NK | Revolver | +50 Shield, −60 HP, +7% Speed, +2 Jump Height, half fall damage | **Crit Happens:** +1% Crit | Clear Forest Tier 1, then buy |
| Robinette | Bow | +5% Gold, +7.5% Speed, +3 Jump Height | **Stonks:** +1% Gold; damage per 1,000 gold carried: +20% (first 10k), +8.5% (to 200k), +6% (to 1M), +3.5% after | Clear Forest Tier 2, then buy |
| Sir Chadwell | Corrupted Sword | +10% Difficulty, +50 HP, +20% Armor, −3% Speed | **Cursed:** +1% Difficulty | Clear Forest Tier 3, then buy |
| Ninja | Katana | +15% Speed, +5% Evasion, +2 Jump Height, half fall damage | **Shadow Step:** +0.5% Evasion; dodges can execute | Clear Desert Tier 1 and own a Katana |
| Vlad | Blood Magic | +5% Lifesteal, +5% Evasion, +4% Speed | **Vampirism:** +1% Lifesteal | Clear Desert Tier 2, then buy |
| Ogre | Axe | +10% Damage, +40 HP, +5% Armor, −6% Speed, −1% Luck | **Warrior:** +1.5% Damage | Unlock the Axe, kill 15,000 Goblins, then buy |
| Megachad | Aura | +20 HP, −5% Speed | **Flexing:** +2.5% Damage per flex; flex cooldown −0.2 s per level | Damage Tome to level 7, then buy |
| Calcium | Bone | +15% Speed, +1.5 Jump Height | **Speed Demon:** +0.7% Damage; +0.5% Damage per 1% speed bonus | Kill 1,000 skeletons, then buy |
| Spaceman | Black Hole | +5% XP, +10 HP, +5 Pickup Range | **Quantum XP Theory:** +1% XP | Complete 6 challenges and unlock the Black Hole |
| Noelle | Frostwalker | +7.5% Speed, +5% Evasion, +3 Jump Height | **Enduring:** +0.7% Size (max 4×); +1.5% damage per frozen enemy (max +300%) | Microwave Ice Crystal 3 times in a row |
| Amog | Poison Flask | +30 HP, +10% Armor, +20% Size, +20% Duration | **Plague:** +1% Poison damage; poison radius 4, +0.05 per level (max 12) | Poison 50,000 enemies with Moldy Cheese |
| Athena | Aegis | +25 HP, +15% Armor, +5 Thorns | **Lockdown:** +2 Thorns; up to +1% damage per level at low HP | Unlock the Aegis and Thorns Tome, then buy |
| Bandit | Dexecutioner | +10% Evasion, +5% Speed | **Flow State:** +1% Attack Speed | Beat the Bandit miniboss in Desert |
| Birdo | Tornado | +1 extra jump, +2 Jump Height, +5% Speed | **Float:** +1% airborne damage | Kill 100 enemies with Tornado while airborne |
| Bush | Sniper Rifle | +10% Evasion, +6 Pickup Range | **Bullseye:** +1% Crit Damage; mark-explosion cooldown −4% per level | Own a Sniper Rifle, beat Sus Bush in Forest |
| Monke | Bananarang | +15% Damage, +35 HP, +2 Jump Height | **Monkey Grip:** +2 HP; wall climbing | Free Monke from the Forest cage |
| Roberto | Scythe | +15% Evasion, +4% Speed | **Hoarder:** a free chest every 60 s, +2.5 s per chest (max 120 s) | Beat Spooky Steve, buy the Scythe, then Roberto |
| Tony McZoom | Wireless Dagger | +30% Speed, +10 Shield, −30 HP, no fall damage | **Shocking:** charges while moving; +2% Pickup Range | Complete 2 challenges and unlock the Wireless Dagger |

Where megabonk.org's per-level numbers differ, the game data wins: Spaceman gets +1% XP per level (not 1.5%), and Calcium's and Noelle's per-level bonuses are 0.7% (not 0.75%).

## Dicehead and Gamba

**Gamba**, from the code (PassiveAbilityGamba.OnLevelup): on every level-up it takes one random stat from the same 18-stat list the Chaos Tome uses ([list](economy.html#which-stats-each-source-can-roll); values in [Stat offer values](economy.html#stat-offer-values)) and applies it at a fraction of its value:

**Gamba multiplier = 0.75 / (1 + (level / 50)^1.5)**, clamped between 0.06 and 1.0.

> **Example:** at level 100, (100 ÷ 50)^1.5 = 2^1.5 = 2.83. So the multiplier is 0.75 ÷ (1 + 2.83) = 0.75 ÷ 3.83 = **0.196**: each level-up's free stat is worth about a fifth of a Common offer. At level 50 it's 0.375; from level 300 on it's stuck at the 0.06 floor.


| Level | 1 | 10 | 25 | 50 | 100 | 150 | 200 | 300+ |
|---|---|---|---|---|---|---|---|---|
| Share of the offer | 75% | 69% | 55% | 37.5% | 20% | 12% | 8% | 6% |

So Gamba is strong early and fades: by level 300 each roll is 6% of an offer, about +0.7% Damage when it rolls Damage. Its late-game value is the sheer number of levels, not the size of each roll. A pickup worth several levels triggers it once per level.

**Dice** rolls 1–6 damage, and every 6 permanently adds crit chance to the weapon (capped at 100 roll-ups a minute). That crit growth is separate from Gamba.

What that means in practice:

- **Weak start.** In 32 recorded runs, 13 died between 3:24 and 4:24.
- **XP and Luck first.** More levels mean more Gamba rolls; more Luck means better offers.
- **Lean into crit.** Dice and Katana both carry crit lines, and crit past 100% overcrits (2 crits ×4, 3 crits ×6.25). On the leaderboard, Dicehead's best runs (1M+) mostly pair Dice with Shotgun.
