"""Generate quests.md, cosmetics.md and challenges.md from the parsed game data."""
import json, re, os, struct
import achparse as A

SP = os.path.dirname(os.path.abspath(__file__))
ACH = json.load(open(os.path.join(SP, 'achievements_raw.json')))
UNL = json.load(open(os.path.join(SP, 'ach_unlocks.json')))
CH = json.load(open(os.path.join(SP, 'challenges.json')))
ART = set(f[:-4] for f in os.listdir(os.path.join(SP, 'art')))
DIFF = ['Easy', 'Medium', 'Hard', 'Cooked']
SILVER = [1, 2, 4, 8]
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())

items = re.findall(r'^\| \*\*(.+?)\*\* \|', open(os.path.join(SP, 'wiki/items.md')).read(), re.M)
ITEM_NAME = {norm(x): x for x in items}
ITEM_NAME.update({'glovepoison': 'Moldy Gloves (Poison)', 'bobslantern': "Bob's Light (Lantern)", 'glovecurse': 'Cursed Gloves',
                  'shatteredwisdom': 'Shattered Knowledge', 'rollerblades': 'Turbo Skates', 'pot': 'Pot (Stainless Steel)',
                  'borgar': 'Borgar', 'brassknuckles': 'Brass Knuckles', 'gloveblood': 'Slurp Gloves (Blood)', 'glovepower': 'Power Gloves',
                  'glovelightning': 'Thunder Mitts', 'tacticalglasses': 'Tactical Glasses', 'suckymagnet': 'Sucky Magnet', 'demonicblood': 'Demonic Blood',
                  'demonicsoul': 'Demonic Soul', 'speedboi': 'Speed Boi', 'gamergoggles': 'Gamer Goggles', 'cowardscloak': "Coward's Cloak",
                  'forbiddenjuice': 'Forbidden Juice', 'giantfork': 'Giant Fork', 'spikyshield': 'Spiky Shield', 'bossbuster': 'Boss Buster'})
WEAPON_NAME = {'BlackHole': 'Black Hole', 'BloodMagic': 'Blood Magic', 'CorruptSword': 'Corrupted Sword', 'DragonsBreath': "Dragon's Breath",
               'FireStaff': 'Firestaff', 'HeroSword': 'Hero Sword', 'LightningStaff': 'Lightning Staff', 'Mine': 'Mines', 'PoisonFlask': 'Poison Flask',
               'Rockets': 'Slutty Rocket', 'Sniper': 'Sniper Rifle', 'SpaceNoodle': 'Space Noodle', 'BluetoothDagger': 'Wireless Dagger'}
CHAR_NAME = {'Cl4nk': 'CL4NK', 'SirChadwell': 'Sir Chadwell', 'TonyMcZoom': 'Tony McZoom', 'SirOofie': 'Sir Oofie'}
TOME_NAME = {'Blood': 'Bloody', 'Xp': 'XP'}
SHOP_NAME = {'Banish': 'Banish', 'Boombox': 'Boombox (pick your music)', 'Refresh': 'Refresh', 'Skip': 'Skip', 'Toggler': 'Toggler',
             'Tomes': 'Tome slot', 'Weapons': 'Weapon slot'}
EXTRA = {'a_desert': ('Map', 'Desert'), 'a_graveyard': ('Map', 'Graveyard'), 'a_weaponSlots2': ('Shop upgrade', 'Weapons'),
         'a_tomeSlots2': ('Shop upgrade', 'Tomes'), 'a_challenges1': ('Other', 'Challenge milestone'), 'a_challenges2': ('Other', 'Challenge milestone'),
         'a_challenges3': ('Other', 'Challenge milestone'), 'a_challenges4': ('Other', 'Challenge milestone'), 'a_wallHugger': ('Other', 'Achievement only')}


def fill(a):
    kv = dict(a['keys'])

    def rep(m):
        k = m.group(1)
        if k == 'value':
            return f"{a['target']:,}" if a['target'] else (f"{a['targetF']:g}" if a['targetF'] else (a['targetS'] or ''))
        return kv.get(k) or k
    s = re.sub(r'\{(\w+)\}', rep, a['desc'] or '').strip()
    s = s.replace('Kll ', 'Kill ').replace(' a Epic', ' an Epic').replace('using Amog', 'as Amog')
    return s[0].upper() + s[1:] if s else s


def unlock_name(a):
    k, v = UNL.get(a['internal']) or EXTRA.get(a['internal'], ('Other', ''))
    if k == 'Item':
        return k, ITEM_NAME.get(norm(v), v)
    if k == 'Weapon':
        return k, WEAPON_NAME.get(v, v)
    if k == 'Character':
        return k, CHAR_NAME.get(v, v)
    if k == 'Tome':
        return k, TOME_NAME.get(v, v) + ' Tome'
    if k == 'Shop upgrade':
        return k, SHOP_NAME.get(v, v)
    return k, v


def quests_md():
    rows = {}
    for a in ACH:
        if not a['enabled'] or a['type'] in (6, 7):
            continue
        k, nm = unlock_name(a)
        rows.setdefault(k, []).append((nm, fill(a), a['difficulty']))
    order = ['Character', 'Map', 'Weapon', 'Tome', 'Item', 'Shop upgrade', 'Other']
    title = {'Character': 'Characters', 'Map': 'Maps', 'Weapon': 'Weapons', 'Tome': 'Tomes', 'Item': 'Items', 'Shop upgrade': 'Shop upgrades', 'Other': 'Other quests'}
    n = sum(len(v) for v in rows.values())
    out = ['# Quests & unlocks', '',
           f"Every quest in the game ({n} here, plus the 22 hat quests and 112 skin quests on [Hats & skins](cosmetics.html)), read from the game's quest data and its English text. Each quest unlocks the thing in the first column once it's done.", '',
           "**These are the Steam achievements.** The game unlocks the matching Steam achievement for every quest you finish (`SteamAchievementsManager.CheckAchievements`), and pulls Steam achievements back in as finished quests (`MyAchievements.SyncToSteamAchievements`). The 117 quests here plus the 22 hat quests make 139, the number Steam lists. Skin quests aren't Steam achievements.", '',
           "**Quest rewards:** finishing a quest also pays Silver by its difficulty (`MyAchievement.GetSilverReward`): **Easy 1, Medium 2, Hard 4, Cooked 8**.", '',
           "**Quest count unlocks:** several shop upgrades unlock from the total number of quests you've finished: Refresh at 20, Weapon slot at 25 and 45, Skip at 30, Tome slot at 35 and 55, Banish at 40, and Dicehead at 100.", '']
    for k in order:
        if k not in rows:
            continue
        out += [f'## {title[k]}', '', '| Unlocks | Quest | Difficulty |', '|---|---|---|']
        for nm, q, dfc in sorted(rows[k], key=lambda r: (r[2], r[0])):
            out.append(f'| {nm} | {q} | {DIFF[dfc]} ({SILVER[dfc]} silver) |')
        out.append('')
    out += ['## Quests that need a secret', '',
            'Some quests point at hidden things on the maps: the banana, the boomboxes, the present, the frogs, the Monke cage, Bush, Bandit and Spooky Steve. See [Map secrets & special fights](secrets.html) for what each one is and what the code does.']
    return '\n'.join(out) + '\n'


HAT_ICON = {'CheeseHat': 'HatCheese', 'Clown': 'HatClown', 'CrownHat': 'HatCrown', 'SantaHat': 'HatSanta', 'FrogHat1': 'HatFrogGreen',
            'FrogHat2': 'HatFrogBlue', 'FrogHat3': 'HatFrogRed', 'GlassesHat': 'HatGlasses', 'Headset': 'HatHeadset', 'KevinHat': 'HatKevin',
            'MedievalHat': 'HatMedieval', 'MicrowaveHat': 'HatMicrowave', 'PilotHat': 'HatPilot', 'PotHat': 'HatPot', 'ShadyHatBlack': 'HatShadyBlack',
            'ShadyHatBlue': 'HatShadyBlue', 'ShadyHatPink': 'HatShadyPink', 'ShadyHatYellow': 'HatShadyGold', 'Sheriff': 'HatSheriff', 'TopHat': 'HatTopHat',
            'TopHatLong': 'HatTophatLong', 'WizardHat': 'HatWizard'}
SKIN_CHAR = {'Amog': 'Amog', 'Astro': 'Spaceman', 'Athena': 'Athena', 'Bandit': 'Bandit', 'bandit': 'Bandit', 'Birdo': 'Birdo', 'Blood': 'Vlad',
             'Calcium': 'Calcium', 'Clank': 'CL4NK', 'Corrupted': 'Sir Chadwell', 'Dicehead': 'Dicehead', 'Fox': 'Fox', 'Bush': 'Bush', 'Hover': 'Tony McZoom',
             'Knight': 'Sir Oofie', 'Megachad': 'Megachad', 'Monke': 'Monke', 'Ninja': 'Ninja', 'Noelle': 'Noelle', 'Ogre': 'Ogre', 'Ghost': 'Roberto',
             'Robinette': 'Robinette'}


def find_ach_pid(b, pids):
    for p in range(0, len(b) - 12, 4):
        fid, pid = struct.unpack_from('<iq', b, p)
        if fid == 0 and pid in pids:
            return pid


def first_locs(b):
    out = []; i = 0; r = A.R(b)
    while True:
        i = b.find(b'GUID:', i)
        if i < 0:
            return out
        r.p = i - 4
        try:
            out.append(A.loc(r.locstr()))
        except Exception:
            out.append(None)
        i += 5


def cosmetics_md():
    byp = {a['pid']: a for a in ACH}
    out = ['# Hats & skins', '', "Every hat and skin and how to unlock it, read from the game's hat and skin data. Hats and skins are cosmetic only: none of them change stats.", '',
           '## Hats', '', '| Hat | How to unlock | Difficulty | In-game text |', '|---|---|---|---|']
    hats = []
    for pid, b in A.by['HatData']:
        nm = A.R(b).header(); ap = find_ach_pid(b, byp); txt = [x for x in first_locs(b) if x]
        a = byp.get(ap)
        hats.append((txt[0] if txt else nm, fill(a) if a else '', a['difficulty'] if a else 0, txt[1] if len(txt) > 1 else '', HAT_ICON.get(nm)))
    for name, how, d, flav, ic in sorted(hats, key=lambda h: (h[2], h[0])):
        out.append(f'| {name} | {how} | {DIFF[d]} | {flav} |')
    HAT_NAME_ICON.update({h[0]: h[4] for h in hats if h[4]})
    out += ['', '## Skins', '', "Every character has a Default skin plus five or six more. Skin quests follow a pattern:", '',
            '- **Kills:** kill 15,000 enemies as that character (some characters have extra kill skins at 50,000, 100,000 or 500,000).',
            '- **Speedrun:** beat the first stage boss in under 6 minutes as that character.',
            '- **Final boss:** kill a final boss on Tier 3 as that character.',
            "- **Crypt (Spooky skin):** finish the Graveyard's first crypt under a time limit that depends on the character (16–24 s).",
            "- **Gold:** get the character to Rank 100.", '',
            '| Character | Skin | How to unlock |', '|---|---|---|']
    rows = []
    for pid, b in A.by['SkinData']:
        nm = A.R(b).header(); ap = find_ach_pid(b, byp); txt = [x for x in first_locs(b) if x]
        a = byp.get(ap)
        if not a:
            continue
        ch = next((v for k, v in SKIN_CHAR.items() if nm.startswith(k)), nm)
        rows.append((ch, txt[0] if txt else nm, fill(a), a['internal']))
    kind = lambda i: ['Kills', 'Extra', 'Speedrun', 'FinalBoss', 'Crypt', 'Gold', 'Kevin'].index(next((k for k in ['Kills', 'Extra', 'Speedrun', 'FinalBoss', 'Crypt', 'Gold', 'Kevin'] if k in i), 'Kevin'))
    for ch, sk, how, i in sorted(rows, key=lambda r: (r[0], kind(r[3]), r[3])):
        out.append(f'| {ch} | {sk} | {how} |')
    return '\n'.join(out) + '\n'


HAT_NAME_ICON = {}
MOD_TEXT = {
    'Chonk Mode': 'Enemies ×2 size, ×2 HP, ×1.5 damage, ×0.85 speed',
    'Hard': 'Enemies ×1.25 HP, damage and speed', 'Harder': 'Enemies ×1.5 HP, damage and speed', 'Hardest': 'Enemies ×2 HP, damage and speed',
    'Hyper': '×2 XP and gold; enemies scale ×4 faster with time', 'Swarm': '×2 enemies, ×1.5 enemy speed, ×0.75 XP',
    'Turbo': 'Chests cost 96% less; enemies scale ×5 faster with time', 'Smol boi': '×0.8 damage, move speed and size',
    'No Items': 'No items (chest amount ×0)', 'Minimalist': '1 weapon slot and 1 tome slot', 'No XP': "Can't gain XP or level up",
    'No Weapons': 'No weapons', 'No Movement': "Can't move or jump", 'No Damage': 'Die on any damage or enemy touch', 'Blind': 'Thick fog',
    'Inverted Controls': 'Inverted controls', 'Lava': 'Lava periodically covers most of the map', 'Crypt': 'Escape the crypt in time'}


def challenges_md():
    out = ['# Challenges', '',
           "Challenges are special runs with a rule change, picked from the Challenges menu per map and tier. All 55 are below, read from the game's challenge data (`ChallengeData`).", '',
           '- **Reward:** a challenge run earns more Silver. The run\'s silver multiplier is the tier\'s normal multiplier **plus (challenge bonus − 1)** (`RunConfig.GetSilverMultiplier`), so a ×1.5 challenge adds +0.5 and a ×2.0 adds +1.0.',
           '- **Unlocking:** each challenge shows once your total completed challenges reach its requirement (`ChallengeData.CanShow`, stat `challengesCompleted`), and some also need the one before it.',
           '- Challenge runs are not uploaded to the online leaderboards.',
           "- **Win condition:** most challenges are won by killing all the tier's bosses. AFK Gaming only needs you to reach the final swarm, and Crypt Escape needs you to escape the first crypt.", '']
    for mp in ['Forest', 'Desert', 'Graveyard']:
        for tier in range(3):
            cs = [c for c in CH if c['map'] == mp and c['tier'] == tier]
            if not cs:
                continue
            out += [f'## {mp} Tier {tier + 1}' if mp != 'Graveyard' else '## Graveyard', '',
                    '| Challenge | Rule | Silver bonus | Needs | Suggested by |', '|---|---|---|---|---|']
            for c in sorted(cs, key=lambda c: (c['req'], c['silver'], c['name'])):
                rules = []
                for m in c['mods']:
                    if 'minutes' in m:
                        mins = m['minutes']; rules.append(f"Win within {int(mins)}:{int(round((mins % 1) * 60)):02d}")
                    elif m['name'] == 'Crypt':
                        tl = next((a['target'] for a in ACH if a['asset'] == c['asset']), None)
                        rules.append(f'Escape the first crypt within {tl} s' if tl else 'Escape the first crypt in time')
                    else:
                        rules.append(MOD_TEXT.get(m['name'], m['name']))
                if c['win'] == 'Reach the final swarm':
                    rules.append('win by reaching the final swarm')
                need = []
                if c['req']:
                    need.append(f"{c['req']} challenge{'s' if c['req'] > 1 else ''} done")
                if c['pre']:
                    need.append(f"“{c['pre']}”")
                out.append(f"| {c['name']} | {'; '.join(rules)} | ×{c['silver']:g} | {', '.join(need) or '—'} | {c['author'] or '—'} |")
            out.append('')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    open(os.path.join(SP, 'wiki/quests.md'), 'w').write(quests_md())
    open(os.path.join(SP, 'wiki/cosmetics.md'), 'w').write(cosmetics_md())
    open(os.path.join(SP, 'wiki/challenges.md'), 'w').write(challenges_md())
    json.dump(HAT_NAME_ICON, open(os.path.join(SP, 'hat_icons.json'), 'w'))
    for f in ['quests', 'cosmetics', 'challenges']:
        t = open(os.path.join(SP, f'wiki/{f}.md')).read(); print(f, t.count('\n| ') - t.count('\n|---'))
