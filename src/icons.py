import re,os,shutil
ART=os.path.join(os.path.dirname(os.path.abspath(__file__)),'art')
_art={re.sub(r'[^a-z0-9]','',f[:-4].lower()):f[:-4] for f in os.listdir(ART)}
ITEM_FIX={'Big Bonk':'ItemBonker','Giant Fork':'ItemFork','Pot (Stainless Steel)':'ItemPot','Power Gloves':'ItemGlovesPower','Sucky Magnet':'ItemSuckyHoof',
 "Bob's Light (Lantern)":'ItemBobsLantern','Cursed Gloves':'ItemGlovesCursed','Demonic Soul':'ItemDemonSoul','Gamer Goggles':'GamerLens',
 'Shattered Knowledge':'ItemShatteredWisdom','Slurp Gloves (Blood)':'ItemGlovesBloody','Spiky Shield':'ItemSpikyShieldf','Turbo Skates':'ItemRollerblades',
 'Brass Knuckles':'ItemBrassKnuckle',"Coward's Cloak":'ItemSpeedyCloak','Demonic Blood':'ItemDemonBlood','Moldy Gloves (Poison)':'ItemGlovesPoison',
 'Thunder Mitts':'ItemGlovesLightning','Borgar':'ItemBorgor','Forbidden Juice':'ItemShadowJuice','Tactical Glasses':'ItemTacticalGoggles'}
WEAPONS={'Aegis':'Aegis','Aura':'Aura','Axe':'Axe','Bananarang':'Bananarang','Black Hole':'BlackHole','Blood Magic':'BloodMagic','Bone':'Bone','Bow':'Bow',
 'Chunkers':'Chunkers','Corrupted Sword':'CorruptedSword','Dexecutioner':'Dexecutioner','Dice':'Dice',"Dragon's Breath":'DragonsBreath','Firestaff':'Firestaff',
 'Flamewalker':'Firewalker','Frostwalker':'Frostwalker','Hero Sword':'HeroSword','Katana':'Katana','Lightning Staff':'LightningStaff','Mines':'Mine',
 'Poison Flask':'Poison Flask','Revolver':'Revolver','Scythe':'Scythe','Shotgun':'Shotgun','Slutty Rocket':'SluttyRocket','Sniper Rifle':'Sniper',
 'Space Noodle':'Space Noodle','Sword':'Sword','Tornado':'Tornado','Wireless Dagger':'Bluetooth Knife'}
TOMES={'XP':'XpTome','Luck':'LuckTome','Cursed':'CursedTome','Chaos':'ChaosTome','Precision':'PrecisionTome','Damage':'DamageTome','Cooldown':'CooldownTome',
 'Quantity':'QuantityTome','Size':'SizeTome','Duration':'DurationTome','Projectile Speed':'ProjectileSpeedTOme','Knockback':'KnockbackTome','Shield':'ShieldTome',
 'Health':'HealthTome','Regen':'RegenerationTome','Armor':'ArmorTome','Evasion':'EvasionTome','Bloody':'BloodTOme','Attraction':'AttractionTome',
 'Agility':'SpeedTome','Golden':'GoldenTome','Silver':'SilverTome'}
CHARS={'Dicehead':'Dicehead','Fox':'Fox','Sir Oofie':'Knight','CL4NK':'RobotCowboy','Robinette':'Robinette','Sir Chadwell':'CorruptedKnight','Ninja':'Ninja',
 'Vlad':'BloodMage','Ogre':'Ogre','Megachad':'Megachad','Calcium':'Calcium','Spaceman':'Astronat','Noelle':'Noelle','Amog':'Amog','Athena':'Athena',
 'Bandit':'Bandit','Birdo':'Birdo','Bush':'Bush','Monke':'Monke','Roberto':'Roberto','Tony McZoom':'Hoverguy'}
def item_icon(n):
    if n in ITEM_FIX: return ITEM_FIX[n]
    k=re.sub(r'[^a-z0-9]','',n.lower()); return _art.get('item'+k) or _art.get(k)
USED=set()
def img(f):
    USED.add(f); return f'<img class="ic" src="img/{f}.png" alt="">'
ALIAS={re.sub(r'\s*\(.*?\)','',k):v for k,v in ITEM_FIX.items()}
ALIAS.update({'Key':'ItemKey',"Bob's Light":'ItemBobsLantern','Lantern':'ItemBobsLantern','Speed Boi':'Speed boi','Joe\'s Dagger':'JoesDagger','Stainless Steel Pot':'ItemPot'})
BAD={'Pots','Pot','Chests','Ghost','Gold','Silver','Shield','Luck','Damage','Armor','Evasion','Health','Size','Duration','Cooldown','Knockback','Cursed','Bloody','Golden','Regen','Precision','Quantity','Thorns','Agility','Attraction','XP','Chaos','Curse','Head'}
STAT={'Max HP':'HealthTome','HP regen':'RegenerationTome','Evasion':'EvasionTome','Pickup range':'AttractionTome','Crit chance':'PrecisionTome','Crit damage':'Crit Happens','Jump height':'Float',
 'Luck, Difficulty, Armor, Shield, Lifesteal, Thorns, Overheal':'LuckTome','Damage, attack speed, size, duration, projectile speed, knockback, move speed':'DamageTome',
 'Fire, ice, lightning, poison and elite damage':'burn','Gold, XP, chest and silver gain':'GoldenTome','Enemy amount, size, speed, HP, damage and scaling':'Curse','Damage':'DamageTome',
 'Attack speed':'CooldownTome','Size':'SizeTome','Duration':'DurationTome','Projectile speed':'ProjectileSpeedTOme','Crit damage':'Crit Happens',
 'Knockback':'KnockbackTome','Move speed':'SpeedTome','Gold, XP, silver gain':'GoldenTome','Gold, XP, chest, silver gain':'GoldenTome','Elite damage':'Bullseye',
 'Powerup chance':'Stonks','Powerup boost':'Stonks'}
WORLD={'Challenge Shrine':'ChallengeIcon','Boss Curse (Cursed Shrine)':'Curse','Magnet Shrine':'Clock','Greed Shrine':'Gold','Greed Shrines':'Gold',
 'Charge Shrine':'Zap','Charge Shrines':'Zap','Charge Shrine stat offers':'Zap','Chests':'psd_ChestOpen','Chest items':'psd_ChestOpen','Spend gold on chests':'psd_ChestOpen',
 'Level-up offers':'Stonks','Level up':'Stonks','Kill enemies':'skull','Use shrines':'ChallengeIcon','Elite spawns':'Elite','Elite damage':'Elite',
 'Greed Shrine, Boss Curse, Magnet, Challenge':'ChallengeIcon','Coffin (Graveyard)':'Coffin','Final swarm':'skull'}
EXTRA={}
def resolve(n,page_lookup=None):
    n=n.strip()
    if page_lookup:
        f=page_lookup(n)
        if f: return [f]
    out=[]
    if n in EXTRA: return [EXTRA[n]]
    f=ALIAS.get(n) or (item_icon(n) if len(n)>3 and n not in BAD else None)
    if f: return [f]
    base=re.sub(r'\s*\(.*?\)','',n).strip()
    for part in re.split(r',\s*|\s+/\s+|\s+\+\s+|\s+and\s+|\s+&\s+',base):
        part=part.strip().rstrip('.')
        if not part or part in BAD: continue
        f=(ALIAS.get(part) or WEAPONS.get(part) or CHARS.get(part) or
           (TOMES.get(part[:-5]) if part.endswith(' Tome') else None) or
           (item_icon(part) if len(part)>3 else None))
        if f and f not in out: out.append(f)
    return out[:3]
def _sub(body,lookup,generic=True):
    def cell(m):
        nm=m.group(2)
        fs=resolve(nm,lookup) if generic else ([lookup(nm)] if lookup and lookup(nm) else [])
        return m.group(1)+''.join(img(f) for f in fs)+nm+m.group(3) if fs else m.group(0)
    body=re.sub(r'(<tr>\s*<td>(?:<strong>)?)([^<]+?)((?:</strong>)?</td>)',cell,body)
    body=re.sub(r'(<h4[^>]*>)([^<]+?)(</h4>)',cell,body)
    return body
import json as _j
HATS=_j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'hat_icons.json')))
def _sub2(body,lookup):
    def cell(m):
        nm=m.group(2); f=lookup(nm)
        return m.group(1)+img(f)+nm+m.group(3) if f else m.group(0)
    return re.sub(r'(<td>(?:<strong>)?)([^<]+?)((?:</strong>)?</td>)',cell,body)
def add_icons(slug,body):
    if slug=='quests':
        Q={'Ghost':'ItemGhost','Desert':'DesertIconBig','Graveyard':'GraveyardIconBig','Banish':'Banish2','Refresh':'Refresh2','Skip':'Skip2',
           'Tome slot':'tomes','Weapon slot':'Weapons','Toggler':'toggler','Boombox (pick your music)':'boombox','Challenge milestone':'ChallengeIcon','Achievement only':'allQuests'}
        return _sub(body,Q.get)
    if slug=='challenges':
        def C(n):
            if n.startswith('Speedrunner'): return 'i_Clock'
            if n.startswith('Crypt'): return 'ItemCryptKey'
            return {'oh no':'skull','oh shit':'skull','what the fuck':'skull','The Floor is Lava':'burn','Chonk Mode':'Elite','Swarm':'Curse','Hyper':'Haste',
                    'Turbo Mode':'Stonks','Fragile':'Heart','Pacifist':'nuke','Sticks and stones':'ItemKey','Minimalist':'Weapons','Loot Goblin':'Gold',
                    'Smol Boi':'SizeTome','AFK Gaming':'IdleJuice','Blind':'Bullseye','Weird Controls':'rage'}.get(n,'ChallengeIcon')
        return _sub(body,C,generic=False)
    if slug=='secrets':
        S={'Big Bob (Ghost King)':'psd_boss','Boomboxes':'boombox','Crypt':'ItemCryptKey','Desert Graves':'skull','Golden key + cage':'CageKey',
           'Gravestones':'skull','Hidden present':'HatSanta','Pumpkins':'ItemPumpkin','Sandstorms':'Tornado','Scorpionussy':'psd_boss','Shiny banana':'Bananarang',
           'Skeleton King statue':'psd_boss','Spooky Steve':'skull','Tumbleweeds':'Katana'}
        def SL(n):
            if n in S: return S[n]
            if n.startswith('Coffins'): return 'Coffin'
            if re.search(r'(phases|miniboss|Ghost King|Greater Ghost)',n): return 'psd_boss'
            return None
        return _sub(body,SL)
    if slug=='tiers':
        def T(n):
            if n.startswith('**'): return None
            return CHARS.get(n) or WEAPONS.get(n) or TOMES.get(n) or item_icon(n) or {"Bob's Light (Lantern)":'ItemBobsLantern','Cursed Gloves':'ItemGlovesCursed','Slurp Gloves (Blood)':'ItemGlovesBloody','Moldy Gloves (Poison)':'ItemGlovesPoison','Pot (Stainless Steel)':'ItemPot','Shattered Knowledge':'ItemShatteredWisdom','Turbo Skates':'ItemRollerblades'}.get(n)
        return _sub(body,T)
    if slug=='cosmetics': return _sub(body,lambda n: HATS.get(n) or CHARS.get(n),generic=False)
    if slug=='items': return _sub(body,item_icon)
    if slug=='weapons': return _sub(body,WEAPONS.get)
    if slug=='tomes': return _sub(body,TOMES.get)
    if slug=='characters': return _sub(body,CHARS.get)
    if slug=='game':
        for f in ('ForestIconBig','DesertIconBig','GraveyardIconBig'): USED.add(f)
    if slug in ('enemies','maps'): return body
    EXTRA.clear(); EXTRA.update(WORLD)
    if slug in ('mechanics','economy'): EXTRA.update(STAT)
    return _sub(body,None)
def copy_used(out):
    d=os.path.join(out,'img'); os.makedirs(d,exist_ok=True)
    for f in USED: shutil.copy(os.path.join(ART,f+'.png'),os.path.join(d,f+'.png'))
