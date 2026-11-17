"""Tier lists page from the Leaderboard.gg data (via megabonk.org), patch 1.0.65, 497 runs at 500k+ kills."""
import re, os
SP = os.path.dirname(os.path.abspath(__file__))
SHARE = dict(x.split(':') for x in """spicymeatball:100 overpoweredlamp:100 anvil:100 beefyring:99 bigbonk:99 giantfork:99 lightningorb:98 key:97 timebracelet:97 wizardshat:97 creditcardgreen:95 echoshard:93 unstabletransfusion:93 feathers:92 goldenshield:91 electricplug:91 moldycheese:91 pot:91 backpack:91 beacon:90 cowardscloak:90 goldenglove:89 gymsauce:89 clover:89 campfire:89 wrench:89 thundermitts:89 phantomshroud:88 curseddoll:88 creditcardred:88 oats:88 slipperyring:88 borgar:87 idlejuice:87 mirror:86 medkit:86 icecube:83 holybook:82 chonkplate:81 beer:81 kevin:80 slurpgloves:79 soulharvester:70 joesdagger:62 suckymagnet:48 oldmask:45 powergloves:42 grandmassecrettonic:30 scarf:30 sluttycannon:24 bobslight:24 goldenring:21 spikyshield:18 skuleg:15 dragonfire:15 battery:10 cursedgrabbies:6 demonicsoul:5 demonicblood:4 forbiddenjuice:4 snek:2 bloodycleaver:2 turboskates:2 bossbuster:2 brassknuckles:1 goldensneakers:1 eagleclaw:1 turbosocks:1 bobdead:1 tacticalglasses:1 pumpkin:1 demonicblade:1 ghost:1 icecrystal:1 zawarudo:1 cactus:1 leechingcrystal:1 toxicbarrel:0 quinsmask:0 shatteredknowledge:0 gamergoggles:0 gasmask:0 moldygloves:0 energycore:0""".split())
SHARE = {k: int(v) for k, v in SHARE.items()}
items = re.findall(r'^\| \*\*(.+?)\*\* \|', open(os.path.join(SP, 'wiki/items.md')).read(), re.M)
norm = lambda s: re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', s.lower()))
NAME = {norm(x): x for x in items}
NAME.update({'bobslight': "Bob's Light (Lantern)", 'cursedgrabbies': 'Cursed Gloves', 'slurpgloves': 'Slurp Gloves (Blood)', 'moldygloves': 'Moldy Gloves (Poison)',
             'pot': 'Pot (Stainless Steel)', 'creditcardgreen': 'Credit Card (Green)', 'creditcardred': 'Credit Card (Red)', 'bobdead': 'Bob (Dead)',
             'shatteredknowledge': 'Shattered Knowledge', 'turboskates': 'Turbo Skates', 'demonicblade': 'Demon Blade'})

TIERS = [
    ('S', 'Core: in every top run', ['spicymeatball', 'overpoweredlamp', 'anvil', 'beefyring', 'giantfork', 'bigbonk', 'wizardshat', 'zawarudo', 'lightningorb', 'key', 'creditcardgreen', 'timebracelet']),
    ('A', 'In about 90% of top runs', ['unstabletransfusion', 'backpack', 'moldycheese', 'curseddoll', 'pot', 'clover', 'gymsauce', 'creditcardred', 'phantomshroud', 'slipperyring', 'echoshard', 'beacon', 'wrench', 'goldenglove', 'goldenshield']),
    ('B', 'Usually kept', ['icecube', 'beer', 'holybook', 'mirror', 'idlejuice', 'thundermitts', 'electricplug', 'feathers', 'cowardscloak', 'campfire', 'soulharvester', 'joesdagger', 'chonkplate', 'kevin', 'slurpgloves', 'oats', 'medkit', 'borgar']),
    ('C', 'Situational', ['suckymagnet', 'oldmask', 'powergloves', 'grandmassecrettonic', 'scarf', 'sluttycannon', 'spikyshield', 'skuleg', 'goldenring']),
    ('D', 'Usually toggled off', ['bobslight', 'dragonfire', 'battery', 'forbiddenjuice', 'snek', 'energycore', 'bloodycleaver', 'demonicsoul', 'demonicblood', 'turboskates',
                                 'brassknuckles', 'bossbuster', 'tacticalglasses', 'eagleclaw', 'gasmask', 'gamergoggles', 'quinsmask', 'toxicbarrel', 'shatteredknowledge',
                                 'moldygloves', 'icecrystal', 'cactus', 'leechingcrystal', 'ghost', 'turbosocks', 'pumpkin', 'bobdead', 'demonicblade', 'goldensneakers', 'cursedgrabbies']),
]
CHARS = [
    ('S', [('Dicehead', 151, 25, '1,327,059'), ('Fox', 155, 3, '1,054,293')]),
    ('A', [('Athena', 5, 2, '2,011,436')]),
    ('B', [('Megachad', 9, 1, '1,002,389'), ('Roberto', 15, 0, '964,828'), ('Tony McZoom', 15, 0, '933,873'), ('Sir Chadwell', 11, 0, '929,343')]),
    ('C', [('Spaceman', 8, 0, '886,139'), ('Noelle', 4, 0, '844,601'), ('Bush', 10, 0, '842,949'), ('Calcium', 11, 0, '833,202'), ('CL4NK', 14, 0, '829,552'),
           ('Ogre', 7, 0, '824,297'), ('Amog', 9, 0, '819,538'), ('Robinette', 14, 0, '808,231'), ('Bandit', 8, 0, '804,146')]),
    ('D', [('Monke', 10, 0, '784,506'), ('Birdo', 2, 0, '778,624'), ('Ninja', 6, 0, '778,251'), ('Sir Oofie', 5, 0, '759,745'), ('Vlad', 8, 0, '748,050')]),
]
GY = {k: int(v) for k, v in (x.split(':') for x in """wizardshat:100 overpoweredlamp:100 anvil:100 spicymeatball:100 creditcardgreen:100 beefyring:100 curseddoll:95 icecube:95 giantfork:90 joesdagger:90 cowardscloak:90 unstabletransfusion:90 mirror:90 beer:85 creditcardred:85 campfire:85 moldycheese:80 scarf:80 slurpgloves:80 bobslight:80 beacon:80 grandmassecrettonic:80 backpack:80 thundermitts:80 timebracelet:70 key:70 bigbonk:50 lightningorb:35 pot:15""".split())}
GYCHARS = [('Tony McZoom', '3 runs, all at 16,777,216 (the counter cap)'), ('Birdo', '5,831,537'), ('Dicehead', '5,447,698'), ('Calcium', '3,422,325'), ('Monke', '3,381,706'),
           ('Fox', '2,998,109'), ('Amog', '2,290,332'), ('Athena', '1,932,277'), ('Bush', '1,691,403')]


def md():
    out = ['# Tier lists', '',
           "Ranked for one goal: **topping the kill leaderboard**, with runs of 500,000+ kills. The rankings come from what the best runs actually use, from the verified runs on [Leaderboard.gg](https://megabonk.leaderboard.gg/) (synced by [megabonk.org](https://megabonk.org/leaderboard/)), patch 1.0.65, snapshot of Nov 16, 2026. The game code on the other pages explains *why*.", '',
           "**Forest and Graveyard are ranked separately.** Graveyard's Bald Heads (Balance Shrines) double a stat each time, and a Graveyard map has up to 28 shrine slots, so Graveyard runs reach numbers Forest can't. The main lists use the **477 Forest runs at 500k+**. Graveyard has [its own section](#graveyard-runs).", '',
           "- The leaderboard keeps **one run per player per character**, so characters fewer people play have fewer runs. Character tiers weigh the best results and 1M+ runs, not just counts.",
           "- The leaderboard lists **which items a run had, not how many copies**. Item tiers show how often top runs keep each item in their pool. An item almost no top run has was usually toggled out on purpose. **Except Za Warudo:** each copy breaks when it saves you, so top runs stack many and have spent them all by the end. Its 1% is an undercount, and it is ranked by use, not by that number.",
           "- The median Forest 500k+ run lasts about 95 minutes and reaches level 2,008.", '',
           '## Characters (Forest)', '', '| Character | Tier | Runs at 500k+ | Runs at 1M+ | Best run |', '|---|---|---|---|---|']
    for t, cs in CHARS:
        for n, a, b, best in cs:
            out.append(f'| {n} | **{t}** | {a} | {b} | {best} |')
    out += ['', "Dicehead and Fox are 64% of Forest 500k+ runs, and Dicehead has 25 of the 31 Forest runs past 1M. Athena holds the Forest record (2,011,436).", '',
            '## Items (Forest)', '']
    for t, desc, keys in TIERS:
        out += [f'### {t} tier ({desc[0].lower() + desc[1:]})', '', '| Item | In Forest 500k+ runs |', '|---|---|']
        for k in sorted(keys, key=lambda k: -(100 if k == 'zawarudo' else SHARE.get(k, 0))):
            out.append(f'| {NAME.get(k, k)} | ' + ('1% at the end (all used up; see above)' if k == 'zawarudo' else f'{SHARE.get(k, 0)}%') + ' |')
        out.append('')
    out += ['Why the S tier wins, from the code:', '',
            '- **Overpowered Lamp** makes every hit run all your on-hit items one extra time per Lamp (max 2), so everything rolls 3 times per hit.',
            '- **Big Bonk, Spicy Meatball, Lightning Orb and Giant Fork** all multiply off the hit, so they scale with everything else.',
            "- **Wizard's Hat and Anvil** raise tome levels and weapon upgrades. That matters more the longer the run goes, and these runs go for hours.",
            "- **Za Warudo** blocks one fatal hit per copy (max 25 a run). Each copy is a second chance in the late swarms, and they are spent as you go.",
            '- **Key, Credit Card (Green) and Time Bracelet** mean more chests, more Luck and more levels, so more rolls at the core.', '',
            '## Weapons and tomes (Forest)', '',
            '| Weapon | In Forest 500k+ runs |', '|---|---|', '| Katana | 94% |', '| Shotgun | 52% |', '| Dexecutioner | 49% |', '| Dice | 37% |', '| Firestaff | 32% |', '| Axe | 10% |', "| Dragon's Breath | 9% |", '',
            '| Tome | In Forest 500k+ runs |', '|---|---|', '| Chaos | 99% |', '| XP | 98% |', '| Cursed | 97% |', '| Damage | 51% |', '| Luck | 48% |', '| Precision | 4% |', '',
            'The [Weapons](weapons.html) page has the attack and proc rates behind these picks; [Maxing a run](max-runs.html) turns them into a plan.']
    out += ['', '## Graveyard runs', '',
            'Graveyard is a single 16-minute stage with twice the shrine slots (28), and any of them can be a **Bald Head** (Balance Shrine). Each one doubles a stat and halves another, so the doublings stack: the 5.4M run had Powerup boost (shown in-game as Powerup Multiplier) at ×409.6. Graveyard runs go much longer and much higher, so they are kept apart from the Forest lists above.', '',
            '| | Forest | Graveyard |', '|---|---|---|', '| Runs at 500k+ | 477 | 20 |', '| Runs at 1M+ | 31 | 13 |', '| Median 500k+ run | 695,107 kills, 95 min, level 2,008 | 1,932,277 kills, 355 min, level 5,405 |', '| Best run | 2,011,436 | 16,777,216 (the counter cap) |', '',
            '**The Forest record is 2,011,436; every run above it is on Graveyard.** Tony McZoom holds #1–3, all stopped at 16,777,216 (2²⁴), the most a 32-bit float can count to exactly. Run stats are stored as floats, so that\'s the kill counter\'s ceiling.', '',
            '### Best Graveyard run per character (1M+)', '', '| Character | Best run |', '|---|---|']
    out += [f'| {n} | {b} |' for n, b in GYCHARS]
    out += ['', '### How Graveyard builds differ', '',
            '- **Two weapons, Shotgun second.** 11 of the 13 runs past 1M use exactly 2 weapons, and 11 of 13 include Shotgun.',
            '- **Chaos and Luck tomes in all 13**, XP in 11. Cursed is in only 30% of Graveyard 500k+ runs (97% on Forest), and 3 tomes instead of 4 is common (30%).',
            '- **Items in every Graveyard 500k+ run:** Wizard\'s Hat, Overpowered Lamp, Anvil, Spicy Meatball, Credit Card (Green) and Beefy Ring.',
            '- **Items far less common than on Forest:** Pot (Stainless Steel) is in only 15% (91% on Forest), Lightning Orb 35% (98%), Big Bonk 50% (99%), Key and Time Bracelet 70% (97%).',
            '- **More common than on Forest:** Bob\'s Light 80% (24%), Scarf 80% (30%), Grandma\'s Secret Tonic 80% (30%), Ice Cube 95% (83%), Joe\'s Dagger 90% (62%).', '',
            'Graveyard is 20 runs, so treat these as a picture of the record runs rather than a ranking.']
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    open(os.path.join(SP, 'wiki/tiers.md'), 'w').write(md())
    miss = [k for _, _, ks in TIERS for k in ks if k not in NAME]
    allk = set(k for _, _, ks in TIERS for k in ks)
    print('unnamed', miss, 'unplaced', [k for k in SHARE if k not in allk])
