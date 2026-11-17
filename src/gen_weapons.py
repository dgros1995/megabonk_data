"""Rebuild wiki/weapons.md: one overview table, a proc-rate ranking, the tome grid and one compact card per weapon."""
import json, re, os, importlib.util
SP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tw', os.path.join(SP, 'tomeweap.py')); tw = importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'game_data.json') if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'game_data.json')) else '/mnt/user-data/uploads/Documents/BonkSeed/probe/game_data-20261116-1539.json'))
old = open(os.path.join(SP, 'wiki/weapons.md')).read()

# hand-written descriptions and upgrade lines, saved from the earlier page
_wt = json.load(open(os.path.join(SP, 'weapon_text.json')))
DESC = _wt['desc']
ROWS = {k: [' ' + x + ' ' for x in v] for k, v in _wt['rows'].items()}

FDT = 0.02  # Unity fixed timestep, the floor on every interval


def g(i, k):
    return d.get(f'unsortedWeapons[{i}].{k}')


W = []
for i in range(d['unsortedWeapons.#']):
    e = g(i, 'eWeapon')
    W.append(dict(e=e, name=tw.NAME.get(e, e), q=g(i, 'projectiles') or 0, cd=g(i, 'endCooldown'), bt=g(i, 'burstTime') or 0,
                  mi=g(i, 'minBurstInterval') or 0, pc=g(i, 'procCoefficient'), pierce=g(i, 'projectileBounces') or 0, aura=g(i, 'isAura'),
                  bounce=g(i, 'canBounce'), dmg=g(i, 'damage')))
W.sort(key=lambda w: w['name'])


def cycle(w, q, aspd=1.0):
    iv = max(w['bt'] / q / aspd, w['mi'] / aspd, FDT) if w['bt'] > 0 else 0
    return max(w['cd'] / aspd + q * iv, FDT)


# how each weapon deals its hits
HIT = {'Aura': ('area', 'every enemy in range, each tick'), 'Frostwalker': ('area', 'every enemy in range, each pulse'),
       'Aegis': ('area', 'blocks, then shockwaves around you'), 'Chunkers': ('contact', 'rocks hit what they touch while orbiting'),
       "Dragon's Breath": ('contact', 'flame cone hits everything in it while it lasts'), 'Space Noodle': ('contact', 'beam hits everything along it while linked'),
       'Flamewalker': ('area', 'fire patches hit what stands in them'), 'Poison Flask': ('area', 'poison pools'), 'Black Hole': ('area', 'pulls and damages everything nearby'),
       'Mines': ('area', 'explode on enemies'), 'Firestaff': ('area', 'fireballs explode'), 'Shotgun': ('area', 'spread blast in front'),
       'Sword': ('area', 'sweep through several'), 'Scythe': ('area', '360° sweep'), 'Katana': ('area', 'slash'), 'Dexecutioner': ('area', 'piercing blade'),
       'Corrupted Sword': ('area', 'front and back slashes'), 'Hero Sword': ('area', 'slash plus a flying slash'), 'Tornado': ('pierce', 'passes through everything'),
       'Bananarang': ('pierce', 'passes through everything, out and back'), 'Blood Magic': ('pierce', 'passes through everything'), 'Bow': ('pierce', 'arrows pierce up to 99'),
       'Lightning Staff': ('bounce', 'chains to more enemies with upgrades'), 'Revolver': ('bounce', 'bullets ricochet'), 'Bone': ('bounce', 'bounces once'),
       'Wireless Dagger': ('bounce', 'homing, bounces once'), 'Slutty Rocket': ('single', 'homing missiles'), 'Dice': ('single', 'one target per die'),
       'Sniper Rifle': ('pierce', 'long-range piercing shot'), 'Axe': ('area', 'spinning axes that linger')}
CONT = {'Aegis', 'Chunkers', "Dragon's Breath", 'Space Noodle', 'Flamewalker'}  # hit timing set by contact, not by the attack cycle


def rate(w, extra_q=0, aspd=1.0):
    if w['q'] == 0:  # aura-type: one tick per cooldown
        return 1 / max(w['cd'] / aspd, FDT)
    q = w['q'] + extra_q
    return q / cycle(w, q, aspd)


def fmt(x):
    return f'{x:.2f}'.rstrip('0').rstrip('.') if x < 10 else f'{x:.1f}'


def page():
    E = {w['e']: tw.effects(w2) for w2 in tw.W for w in [w2]}
    E = {w['e']: tw.effects(w) for w in tw.W}
    out = ['# Weapons', '',
           "Every weapon's numbers from the game's weapon data, how fast each one attacks, and how each tome changes it. Unlock requirements are on [Quests & unlocks](quests.html).", '',
           '## How weapons work', '',
           '- **Upgrades:** each weapon upgrade raises a few of that weapon\'s stat lines by the Common amount × the offer\'s rarity (×1.0 Common up to ×2.0 Legendary). Anvil adds one more line to future offers.',
           '- **Level cap:** 40, plus 10 for the first Pot (Stainless Steel) and 1 less for each extra copy (never below +2).',
           '- **Slots:** 2 to start, up to 4 with the Weapon Slots upgrade. See the [FAQ](faq.html) for 2 vs 3 vs 4.',
           '- **Your stats apply on top:** the weapon\'s damage × your Damage stat, its crit chance + yours, and so on. The tome section below has every formula.', '',
           '### Attack timing (`WeaponUtility.GetWeaponCooldown`)', '',
           'One attack cycle = **cooldown ÷ Attack Speed + projectiles × shot interval**, where the shot interval = max(burst time ÷ projectiles, minimum interval) ÷ Attack Speed.', '',
           'So **more projectiles usually cost no extra time:** the burst is spread over the same burst time, until the shots hit the weapon\'s minimum interval. Attack Speed (Cooldown Tome) shortens everything.', '',
           '## Overview', '',
           "**Attacks/s** is projectiles fired per second at base (Attack Speed 100%, no Quantity). **Proc rolls/s** is attacks/s × proc coefficient: how often the weapon rolls on-hit items like Big Bonk, Lightning Orb and Dragonfire against **one** enemy. Weapons that pierce, bounce or hit an area roll once per enemy hit, so in a crowd they roll many times more.", '',
           '| Weapon | Base dmg | Projectiles | Cooldown | Attacks/s | Proc coef. | Proc rolls/s | Hits |', '|---|---|---|---|---|---|---|---|']
    for w in W:
        r = ROWS.get(w['name'])
        base = r[1].strip() if r else fmt(w['dmg'])
        kind, why = HIT[w['name']]
        if w['name'] in CONT:
            att = 'contact'; pr = '—'
        else:
            a = rate(w); att = fmt(a) + (' ticks' if w['q'] == 0 else ''); pr = fmt(a * w['pc'])
        out.append(f"| {w['name']} | {base} | {w['q'] or '—'} | {fmt(w['cd'])} s | {att} | {fmt(w['pc'])} | {pr} | {kind}: {why} |")
    out += ['', "Proc coefficients come straight from the weapon data (`procCoefficient`). Contact weapons (Aegis, Chunkers, Dragon's Breath, Space Noodle, Flamewalker) roll whenever they touch an enemy, so their rate depends on the crowd, not on a cycle.", '']

    # ranking by proc rolls with a realistic mid-run build
    out += ['## Which weapons roll procs fastest', '',
            'Proc rolls per second against one enemy, at base and with a typical mid-run build of **+4 projectiles (Quantity) and +100% Attack Speed**. Higher means more Big Bonk, Lightning Orb and Dragonfire rolls.', '',
            '| Weapon | At base | +4 projectiles, ×2 Attack Speed | Gain | Notes |', '|---|---|---|---|---|']
    rk = []
    for w in W:
        if w['name'] in CONT:
            continue
        b = rate(w) * w['pc']; m = rate(w, 0 if w['q'] == 0 else 4, 2.0) * w['pc']
        cap = ''
        if w['q'] and w['bt'] > 0 and w['mi'] > 0:
            n = w['bt'] / w['mi']
            cap = f"extra projectiles are free up to {int(n)} per burst" if n < 40 else 'extra projectiles always free'
        elif w['q'] and w['bt'] == 0:
            cap = 'all projectiles fire at once'
        else:
            cap = 'no projectiles: only Attack Speed raises it'
        kind = HIT[w['name']][0]
        if kind in ('area', 'pierce', 'bounce'):
            cap += '; multiplied by enemies hit'
        rk.append((m, b, w['name'], cap))
    for m, b, n, cap in sorted(rk, reverse=True):
        out.append(f'| {n} | {fmt(b)} | {fmt(m)} | ×{fmt(m / b)} | {cap} |')
    out += ['', "**What it means for procs:** Aura and multi-projectile weapons roll the most per enemy, and anything that pierces or hits an area (Bow, Tornado, Bananarang, Blood Magic, Lightning Staff, Shotgun, the swords) rolls once **per enemy it hits**, which in a swarm is far more than the table shows. Quantity is the strongest stat for proc rates on burst weapons, because extra projectiles fit into the same burst.", '']

    # tome grid (from tomeweap)
    sec = re.sub(r'<img class="ic"[^>]*> ', '', tw.weapons_section())
    grid = sec.split('### At a glance')[1].split('### Weapon by weapon')[0]
    formulas = sec.split('The formulas:')[1].split('### At a glance')[0]
    out += ['## How tomes affect weapons', '', 'Every weapon stat is the weapon\'s value combined with yours (`WeaponUtility`):', formulas.rstrip(), '', '### At a glance', grid.rstrip(), '',
            '✓ (cap) = it works until the weapon\'s maximum. Damage, Precision and Size work on every weapon. The cards below give each weapon\'s numbers.', '']

    # cards
    out += ['## Every weapon', '']
    for w in W:
        r = ROWS.get(w['name']); ef = E[w['e']]
        out.append(f"#### {w['name']}")
        out.append('')
        if w['name'] in DESC:
            out.append(f"*{DESC[w['name']].strip()}*")
            out.append('')
        if r:
            out.append(f"- **Base:** {r[1].strip()} damage, {r[2].strip()} cooldown" + (f", {r[3].strip()}" if r[3].strip() != '—' else '') + f", proc coefficient {fmt(w['pc'])}.")
            out.append(f"- **Upgrade lines:** {r[4].strip()}.")
        notes = []
        for t in ['Cooldown', 'Quantity', 'Duration', 'Projectile Speed', 'Knockback']:
            k, txt = ef[t]
            notes.append(f"{t}: {'no effect (' + txt + ')' if k == 'no' else txt}")
        if 'capped' in ef['Size'][1]:
            notes.append('Size: ' + ef['Size'][1])
        out.append('- **Tomes:**')
        out += [f'    - {n}' for n in notes]
        out.append('')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    p = page()
    open(os.path.join(SP, 'wiki/weapons.md'), 'w').write(p)
    print(len(p.splitlines()), 'lines')
