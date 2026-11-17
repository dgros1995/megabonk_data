import os
"""Generate the tome-vs-weapon sections from the game data + traced WeaponUtility formulas."""
import json
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'game_data.json') if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'game_data.json')) else '/mnt/user-data/uploads/Documents/BonkSeed/probe/game_data-20261116-1539.json'))
NAME = {'BlackHole': "Black Hole", 'BloodMagic': 'Blood Magic', 'CorruptSword': 'Corrupted Sword', 'DragonsBreath': "Dragon's Breath",
        'FireStaff': 'Firestaff', 'HeroSword': 'Hero Sword', 'LightningStaff': 'Lightning Staff', 'Mine': 'Mines', 'PoisonFlask': 'Poison Flask',
        'Rockets': 'Slutty Rocket', 'Sniper': 'Sniper Rifle', 'SpaceNoodle': 'Space Noodle', 'BluetoothDagger': 'Wireless Dagger'}
ICON = {'Aegis': 'Aegis', 'Aura': 'Aura', 'Axe': 'Axe', 'Bananarang': 'Bananarang', 'BlackHole': 'BlackHole', 'BloodMagic': 'BloodMagic', 'Bone': 'Bone',
        'Bow': 'Bow', 'Chunkers': 'Chunkers', 'CorruptSword': 'CorruptedSword', 'Dexecutioner': 'Dexecutioner', 'Dice': 'Dice', 'DragonsBreath': 'DragonsBreath',
        'FireStaff': 'Firestaff', 'Flamewalker': 'Firewalker', 'Frostwalker': 'Frostwalker', 'HeroSword': 'HeroSword', 'Katana': 'Katana',
        'LightningStaff': 'LightningStaff', 'Mine': 'Mine', 'PoisonFlask': 'Poison Flask', 'Revolver': 'Revolver', 'Scythe': 'Scythe', 'Shotgun': 'Shotgun',
        'Rockets': 'SluttyRocket', 'Sniper': 'Sniper', 'SpaceNoodle': 'Space Noodle', 'Sword': 'Sword', 'Tornado': 'Tornado', 'BluetoothDagger': 'Bluetooth Knife'}
# What one extra "projectile" means for each weapon, and how the projectile moves (from the weapon's attack/projectile class)
NOUN = {'Aegis': 'shield', 'Axe': 'axe', 'Bananarang': 'banana', 'BlackHole': 'black hole', 'BloodMagic': 'blood bolt', 'Bone': 'bone', 'Bow': 'arrow',
        'Chunkers': 'orbiting rock', 'CorruptSword': 'slash', 'Dexecutioner': 'blade', 'Dice': 'die', 'FireStaff': 'fireball', 'Flamewalker': 'fire patch',
        'HeroSword': 'slash', 'Katana': 'slash', 'LightningStaff': 'lightning strike', 'Mine': 'mine', 'PoisonFlask': 'flask', 'Revolver': 'bullet',
        'Scythe': 'sweep', 'Shotgun': 'blast', 'Rockets': 'rocket', 'Sniper': 'shot', 'Sword': 'slash', 'Tornado': 'tornado', 'BluetoothDagger': 'dagger'}
# Projectile Speed: does the weapon's damage-dealer travel? (swings, hitscan, strikes, zones and auras don't)
TRAVEL = {'Axe', 'Bananarang', 'BlackHole', 'BloodMagic', 'Bone', 'Bow', 'Chunkers', 'CorruptSword', 'HeroSword', 'Dice', 'FireStaff', 'PoisonFlask',
          'Revolver', 'Rockets', 'Tornado', 'BluetoothDagger'}
SPEEDNOTE = {'Chunkers': 'rocks orbit faster', 'Bananarang': 'flies out and back faster', 'Rockets': 'rockets fly faster',
             'PoisonFlask': 'flasks land sooner', 'BlackHole': 'black holes drift faster', 'Bow': 'arrows fly faster (and Size/Duration slow them down less)'}
NOSPEED = {'Katana': 'a swing, nothing travels', 'Sword': 'a swing', 'Scythe': 'a sweep', 'Dexecutioner': 'a swing', 'Sniper': 'hits instantly',
           'Shotgun': 'hits instantly', 'LightningStaff': 'strikes from above', 'Mine': 'mines sit still', 'Flamewalker': 'fire is left on the ground',
           'Frostwalker': 'an aura', 'Aura': 'an aura', 'DragonsBreath': 'a flame cone', 'SpaceNoodle': 'a beam', 'Aegis': 'a shield around you'}
DURNOTE = {'PoisonFlask': 'poison pools last longer', 'BlackHole': 'black holes last longer', 'Mine': 'mines stay armed longer',
           'Flamewalker': 'fire patches burn longer', 'Frostwalker': 'freezes last longer', 'DragonsBreath': 'each breath lasts longer',
           'SpaceNoodle': 'the beam stays linked longer', 'Chunkers': 'rocks orbit longer before resetting', 'Axe': 'axes linger longer',
           'Tornado': 'tornadoes last longer', 'Bananarang': 'bananas fly further before returning'}


def g(i, k):
    return d.get(f'unsortedWeapons[{i}].{k}')


W = []
for i in range(d['unsortedWeapons.#']):
    e = g(i, 'eWeapon')
    ups = [g(i, f'upgradeData.upgradeModifiers[{j}].stat') for j in range(g(i, 'upgradeData.upgradeModifiers.#') or 0)]
    W.append(dict(e=e, name=NAME.get(e, e), dmg=g(i, 'damage'), kb=g(i, 'knockback'), crit=g(i, 'critChance') or 0, proj=g(i, 'projectiles'),
                  dur=g(i, 'attackDuration'), maxdur=g(i, 'maxDuration'), spd=g(i, 'projectileSpeed'), cd=g(i, 'endCooldown'),
                  burst=g(i, 'burstTime'), maxsize=g(i, 'maxSizeMultiplier'), ups=ups))
W.sort(key=lambda w: w['name'])


def fmt(x):
    return f'{x:g}'


def effects(w):
    e = w['e']; out = {}
    out['Damage'] = ('yes', 'multiplies all its damage' + (' (base is the 1–6 roll)' if e == 'Dice' else ''))
    c = w['crit']
    out['Precision'] = ('yes', f'adds to its crit chance' + (f' (starts at {c*100:g}%)' if c else ''))
    if w['cd'] and w['cd'] > 0:
        out['Cooldown'] = ('yes', f"{fmt(w['cd'])} s pause ÷ Attack Speed" + (', and shots inside a burst come faster' if w['burst'] and w['proj'] and w['proj'] > 1 else ''))
    else:
        out['Cooldown'] = ('yes', 'fires its bursts faster (no pause between attacks)')
    if e in ('Aura', 'Frostwalker', 'DragonsBreath', 'SpaceNoodle'):
        out['Cooldown'] = ('yes', {'Aura': 'damage ticks come faster (0.3 s base)', 'Frostwalker': 'pulses come faster (1.25 s base)',
                                   'DragonsBreath': 'breathes more often (2 s base)', 'SpaceNoodle': 'relinks sooner (1 s base)'}[e])
    if e == 'Aegis':
        out['Cooldown'] = ('yes', 'shields come back faster (1.5 s base)')
    if not w['proj']:
        out['Quantity'] = ('no', 'has no projectile count')
    else:
        out['Quantity'] = ('yes', f"+1 {NOUN.get(e, 'projectile')} per Quantity (starts with {w['proj']})")
    ms = w['maxsize']
    out['Size'] = ('yes', 'bigger hit area' + (f', capped at ×{fmt(ms)}' if ms and ms > 1 else ''))
    dur, mx = w['dur'], w['maxdur']
    if e == 'Aegis' or e == 'Aura' or not dur:
        out['Duration'] = ('no', 'nothing timed to lengthen')
    elif mx and mx > 0 and dur >= mx:
        out['Duration'] = ('no', f"its {fmt(dur)} s already sits at its {fmt(mx)} s cap")
    else:
        note = DURNOTE.get(e, 'projectiles live longer, so they travel further')
        if e == 'PoisonFlask':
            note = 'poison pools last longer and poison stacks last longer'
        if mx and mx > 0:
            pct = (mx / dur - 1) * 100
            out['Duration'] = ('capped', f"{note}: {fmt(dur)} s → cap {fmt(mx)} s (cap reached at +{pct:.0f}% Duration)")
        else:
            out['Duration'] = ('yes', f"{note}: {fmt(dur)} s × Duration, no cap")
    if e in TRAVEL:
        out['Projectile Speed'] = ('yes', SPEEDNOTE.get(e, 'faster projectiles') + f" (base {fmt(w['spd'])})")
    else:
        out['Projectile Speed'] = ('no', NOSPEED.get(e, 'nothing travels'))
    if not w['kb']:
        out['Knockback'] = ('no', 'base knockback 0')
    else:
        out['Knockback'] = ('yes', f"base {fmt(w['kb'])} × Knockback")
    return out


TOMES = ['Damage', 'Precision', 'Cooldown', 'Quantity', 'Size', 'Duration', 'Projectile Speed', 'Knockback']
MARK = {'yes': '✓', 'no': '✗', 'capped': '✓ (cap)'}


def icon(e, size=28):
    return f'<img class="ic" src="img/{ICON[e]}.png" alt="" width="{size}" height="{size}">'


def tomes_section():
    s = ['## Which weapons each tome affects', '',
         'Every weapon reads its stats through the same functions (`WeaponUtility`), each one weapon value × your stat. Whether a tome does anything depends on whether the weapon has that value and uses it. Tomes not listed here (XP, Luck, Cursed, Health, Shield, Armor, Evasion, Regen, Bloody, Thorns, Attraction, Agility, Golden, Silver) don\'t change weapons directly; Thorns is the exception for Aegis, whose blocks add your Thorns to their damage.', '',
         '| Tome | Affects | Doesn\'t affect |', '|---|---|---|']
    E = {w['e']: effects(w) for w in W}
    for t in TOMES:
        yes = [w['name'] for w in W if E[w['e']][t][0] != 'no']
        no = [f"{w['name']} ({E[w['e']][t][1]})" for w in W if E[w['e']][t][0] == 'no']
        ys = 'All weapons' if not no else ', '.join(yes)
        s.append(f"| **{t}** | {ys} | {'; '.join(no) if no else '—'} |")
    s += ['', 'Duration is capped per weapon: a weapon whose attack already lasts its maximum gains nothing (see [Weapons](weapons.html) for each cap). Size is capped only on Revolver (×4) and Wireless Dagger (×3.5).', '']
    return '\n'.join(s)


def weapons_section():
    E = {w['e']: effects(w) for w in W}
    s = ['## How each tome changes each weapon', '',
         'All values are from the weapon data and the code that reads them (`WeaponUtility.GetDuration`, `GetAttackSizeMultiplier`, `GetProjectileSpeed`, `GetAttackQuantity`, `GetWeaponCooldown`, `GetDamageContainer`). The formulas:', '',
         '- **Damage:** every hit × your Damage stat.',
         '- **Precision:** your crit chance + the weapon\'s own.',
         '- **Cooldown** (Attack Speed): pause = weapon cooldown ÷ Attack Speed; shots inside a burst are spaced burst time ÷ projectiles ÷ Attack Speed.',
         '- **Quantity:** weapon projectiles + yours.',
         '- **Size:** weapon size × yours, capped where the weapon has a cap.',
         '- **Duration:** weapon duration × yours, capped at the weapon\'s max duration.',
         '- **Projectile Speed:** weapon speed × yours; only matters if something travels.',
         '- **Knockback:** weapon knockback × yours, applied on every hit.', '',
         '### At a glance', '',
         '| Weapon | ' + ' | '.join(TOMES) + ' |', '|---|' + '---|' * len(TOMES)]
    for w in W:
        s.append(f"| {icon(w['e'], 20)} {w['name']} | " + ' | '.join(MARK[E[w['e']][t][0]] for t in TOMES) + ' |')
    s += ['', '### Weapon by weapon', '']
    for w in W:
        ef = E[w['e']]
        s.append(f"#### {icon(w['e'])} {w['name']}")
        s.append('')
        for t in TOMES:
            k, txt = ef[t]
            s.append(f"- **{t}:** {'no effect: ' if k == 'no' else ''}{txt}.")
        s.append('')
    return '\n'.join(s)


if __name__ == '__main__':
    open('gen_tome_weapons.md', 'w').write(tomes_section())
    open('gen_weapon_tomes.md', 'w').write(weapons_section())
    print(tomes_section()[:3000])
