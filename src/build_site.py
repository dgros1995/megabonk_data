import markdown, re, os, html, shutil, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from icons import add_icons, copy_used, USED, img as icon_img, ART
from site_defs import PAGES, STAGE_TABLE

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'wiki')
OUT = os.path.normpath(os.path.join(HERE, '..', 'docs')) if os.path.isdir(os.path.join(HERE, '..', 'docs')) else '/home/claude/megabonk_data/docs'
SITE = 'https://bonk.wiki/'
VERSION = '1.0.69'
import datetime as _dt
UPDATED = _dt.date.today().strftime('%b %-d, %Y')
REPO = 'https://github.com/dgros1995/megabonk_data'
DESC = {
    'index': "Megabonk's real numbers, read from the game's code: every item, weapon, tome and character, the damage and Luck formulas, and how to max a run.",
    'game': "What a Megabonk run is, the goal, the core loop, how maps are generated and what sets the game apart.",
    'mechanics': "How every Megabonk stat is calculated: damage brackets, crits and overcrits, proc chances, armor, evasion and XP per level.",
    'status': "Megabonk status effects from the code: poison, burn, freeze, stun, Bloodmark, charm and execute.",
    'maps': "Megabonk maps, tiers and stage timelines, spawn rates, the final swarm and its ghosts, bosses and Boss Curses.",
    'enemies': "Every Megabonk enemy's base stats and the HP and damage formulas that scale them.",
    'economy': "Megabonk Luck odds, chest prices, free chests, powerups, shrines, Banish/Refresh/Skip and the Silver shop, from the game's code.",
    'items': "Every Megabonk item and exactly what its code does, with stacking and diminishing returns.",
    'weapons': "Every Megabonk weapon's base stats and upgrades, and how each tome changes each weapon.",
    'tomes': "Every Megabonk tome, its per-level value, rarity multipliers and which weapons it affects.",
    'characters': "Every Megabonk character's starting stats, weapon and per-level passive.",
    'max-runs': "A data-backed plan for high-kill Megabonk runs: Luck and chests, Boss Curses, the final swarm and the ghost wall.",
    'secrets': "Megabonk map secrets and special fights: frog eggs, Bush, Bandit, Spooky Steve, Big Bob, coffins, the crypt and hidden objects.",
    'quests': "Every Megabonk quest and what it unlocks: characters, maps, weapons, tomes, items and shop upgrades, with silver rewards.",
    'challenges': "All 55 Megabonk challenges with their exact rules, silver bonus and unlock requirements.",
    'cosmetics': "Every Megabonk hat and skin and how to unlock it.",
    'tiers': "Megabonk item and character tier lists for 500k+ kill runs, based on what top leaderboard runs actually use.",
    'faq': "Megabonk FAQ: how many shrines, chests and Bald Heads a map can have, and what Luck does and doesn't affect.",
}
# icon for each page (nav + title)
PAGE_ICON = {'index': 'Gamba', 'game': 'Tomes2', 'mechanics': 'Stonks', 'status': 'poison', 'maps': 'Challenges1',
             'enemies': 'Curse', 'economy': 'Gold', 'items': 'ItemBobsLantern', 'weapons': 'Weapons', 'tomes': 'tomes',
             'characters': 'Dicehead', 'secrets': 'ItemCryptKey', 'quests': 'allQuests', 'challenges': 'ChallengeIcon', 'cosmetics': 'HatTopHat', 'tiers': 'HatCrown', 'max-runs': 'kill100k', 'faq': 'Bullseye'}
# icons placed on section headings: page -> [(heading prefix, icon)]
HEAD_ICON = {
    'status': [('Poison', 'poison'), ('Burn', 'burn'), ('Freeze', 'ItemIceCube'), ('Stun', 'ItemBonker'), ('Bloodmark', 'Bloodmark'),
               ('Charm', 'ItemPhantomShroud'), ('Execute', 'JoesDagger')],
    'economy': [('How Luck works', 'LuckTome'), ('Chests', 'ItemKey'), ('Pots', 'Gold'), ('Microwave', 'ItemEnergyCore'),
                ('Shady Guy', 'ItemCreditCardRed'), ('Shrines', 'Challenges1'), ('Level-up and shrine', 'Stonks')],
    'mechanics': [('How every stat', 'Stonks'), ('Weapon damage', 'DamageTome'), ('Crits and overcrits', 'Crit Happens'),
                  ('Proc chances', 'ItemLightningOrb'), ('Damage you take', 'ArmorTome'), ('Your base damage', 'Warrior')],
    'maps': [('Timers', 'ItemTimeBracelet'), ('Spawning', 'Curse'), ('The final swarm', 'ItemGhost'), ('Bosses and Boss Curses', 'Curse')],
    'enemies': [('How enemy stats scale', 'Stonks'), ('Every enemy', 'Curse')],
    'max-runs': [('1. ', 'LuckTome'), ('2. ', 'XpTome'), ('2b. ', 'psd_ChestOpen'), ('3. ', 'Curse'), ('4. ', 'kill100k'), ('5. ', 'ItemGhost'), ('5b. ', 'EvasionTome'),
                 ('6. ', 'Challenges1'), ('7. ', 'Dicehead')],
    'secrets': [('Special fights', 'psd_boss'), ('Frog eggs', 'psd_frog'), ('Hidden objects', 'ItemKey'), ('Named bosses', 'skull')],
    'quests': [('Characters', 'Dicehead'), ('Maps', 'Challenges1'), ('Weapons', 'Weapons'), ('Tomes', 'tomes'), ('Items', 'ItemBobsLantern'), ('Shop upgrades', 'Gold'), ('Other quests', 'allQuests'), ('Quests that need', 'ItemCryptKey')],
    'challenges': [('Forest', 'ChallengeIcon'), ('Desert', 'ChallengeIcon'), ('Graveyard', 'ChallengeIcon')],
    'cosmetics': [('Hats', 'HatTopHat'), ('Skins', 'Dicehead')],
    'tiers': [('Characters', 'Dicehead'), ('Items', 'ItemBonker'), ('Weapons and tomes', 'Katana')],
    'faq': [('How many', 'Challenges1'), ('What does Luck', 'LuckTome'), ('Other common', 'Bullseye')],
    'game': [('The goal', 'kill100k'), ('The core loop', 'Gamba'), ('What makes it different', 'Speed Demon'), ('Characters', 'Dicehead'),
             ('How maps are generated', 'Challenges1'), ('How enemies get stronger', 'Curse'), ('Between runs', 'Silver')],
}
MAP_BANNER = {'Forest': 'ForestIconBig', 'Desert': 'DesertIconBig', 'Graveyard': 'GraveyardIconBig'}
PASSIVE_ICON = {'Gamba': 'Gamba', 'RNG Blessing': 'RNG Blessing', 'Fortified': 'Reinforced', 'Crit Happens': 'Crit Happens', 'Stonks': 'Stonks',
                'Cursed': 'Curse', 'Shadow Step': 'Shadowstep', 'Vampirism': 'Vampire', 'Warrior': 'Warrior', 'Flexing': 'Flex',
                'Speed Demon': 'Speed Demon', 'Quantum XP Theory': 'QuantumXp', 'Enduring': 'Enduring', 'Plague': 'Plague', 'Lockdown': 'LockIn',
                'Flow State': 'Flowstate', 'Float': 'Float', 'Bullseye': 'Bullseye', 'Hoarder': 'Hoarder', 'Shocking': 'ZapIcon'}

CSS = r'''
:root{--bg:#f7f4ee;--panel:#fffdf9;--ink:#1c1915;--muted:#6b645a;--line:#e5ddd0;--accent:#c2410c;--accent-ink:#9a3412;--accent-soft:#fdeee4;--code:#f1ebe1;--zebra:#fbf8f2;--brand:#17130f;--brand-ink:#f5efe6}
@media (prefers-color-scheme:dark){:root{--bg:#12100e;--panel:#1a1714;--ink:#ede7de;--muted:#a59d91;--line:#2d2823;--accent:#fb923c;--accent-ink:#fdba74;--accent-soft:#2b1c12;--code:#25211c;--zebra:#1d1a16;--brand:#0b0907;--brand-ink:#f5efe6}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-padding-top:16px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 "Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-feature-settings:"tnum" 1,"cv11" 1}
img.px,.ic,.hero-bg,.map-banner img,.brand img,.pg-ic,.card img{image-rendering:pixelated}
.wrap{display:flex;min-height:100vh}
nav.side{width:252px;flex:none;border-right:1px solid var(--line);position:sticky;top:0;height:100vh;overflow:auto;background:var(--panel);display:flex;flex-direction:column}
.brand{display:block;background:var(--brand);color:var(--brand-ink);padding:22px 20px 16px;text-decoration:none}
.wm{display:block;font-size:27px;font-weight:850;letter-spacing:-.03em;line-height:1}.wm i{font-style:normal;color:#fb923c}
.brand span{display:block;margin-top:8px;font-size:12.5px;opacity:.72;letter-spacing:.02em}
.links{padding:10px 12px 24px}.grp{margin-top:10px}.grp>b{display:block;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:6px 10px 4px;font-weight:700}.mbtn{display:none}
.suggest{margin-top:48px;padding:14px 16px;border:1px dashed var(--line);border-radius:12px;color:var(--muted);font-size:14.5px}.pager{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:56px}.pager a{display:block;border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:12px 16px;text-decoration:none;color:var(--ink);font-weight:650}.pager a:hover{border-color:var(--accent)}.pager span{display:block;font-size:12.5px;color:var(--muted);font-weight:500}.pager .nx{text-align:right}
.links a{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:9px;color:var(--ink);text-decoration:none;font-size:15px;line-height:1.3}
.links a img{width:22px;height:22px;flex:none}
.links a:hover{background:var(--code)}.links a.on{background:var(--accent-soft);color:var(--accent-ink);font-weight:650}
.side-foot{margin-top:auto;padding:14px 22px 20px;font-size:12.5px;color:var(--muted);border-top:1px solid var(--line)}
.side-foot a{color:var(--muted)}
main{flex:1;min-width:0;padding:40px 52px 72px;max-width:1120px}
.pg-head{display:flex;align-items:center;gap:16px;margin:0 0 6px}
.pg-ic{width:52px;height:52px;flex:none;border-radius:10px;background:var(--brand);padding:6px}
h1{font-size:34px;line-height:1.12;letter-spacing:-.025em;margin:0}
.meta{color:var(--muted);font-size:13.5px;margin:4px 0 22px}
h2{font-size:23px;letter-spacing:-.015em;margin:48px 0 12px;padding-top:14px;border-top:1px solid var(--line);display:flex;align-items:center;gap:10px}
h3{font-size:18.5px;margin:30px 0 8px;display:flex;align-items:center;gap:9px}
h4{font-size:17px;margin:26px 0 6px;display:flex;align-items:center;gap:8px}
h2 .ic,h3 .ic{width:28px;height:28px;margin:0;vertical-align:0}h4 .ic{width:32px;height:32px;margin:0}
a{color:var(--accent);text-underline-offset:2px}strong{font-weight:650}
p,li{max-width:76ch}
.tw{overflow-x:auto;margin:16px 0 20px;border:1px solid var(--line);border-radius:12px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:9px 13px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{background:var(--code);font-weight:650;white-space:nowrap;font-size:13.5px;letter-spacing:.01em}
tbody tr:nth-child(even) td{background:var(--zebra)}tr:last-child td{border-bottom:0}
td.nm{white-space:nowrap}table.dense{font-size:13.5px}table.dense th,table.dense td{padding:8px 8px}table.dense th{white-space:normal}
.ic{width:24px;height:24px;vertical-align:-6px;margin-right:7px}.mthumb{width:40px;height:30px;border-radius:4px;vertical-align:-9px;margin-right:9px;image-rendering:pixelated;object-fit:cover}
code{background:var(--code);padding:1px 5px;border-radius:5px;font-size:.9em;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
ul,ol{padding-left:22px}li{margin:4px 0}
blockquote{margin:14px 0 18px;padding:12px 18px;border-left:3px solid var(--accent);background:var(--panel);border-radius:0 10px 10px 0;max-width:76ch}blockquote p{margin:0 0 6px}blockquote ol,blockquote ul{margin:4px 0 0}
.toc{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin:0 0 8px;font-size:14.5px}
.toc b{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.toc ul{list-style:none;padding:0;margin:8px 0 2px;display:flex;flex-wrap:wrap;gap:4px 16px}.toc li{margin:0}
.toc a{text-decoration:none}.toc a:hover{text-decoration:underline}
.map-banner{display:flex;gap:16px;align-items:flex-start;margin:6px 0 4px}
.map-banner img{width:176px;height:132px;border-radius:10px;flex:none;object-fit:cover;border:1px solid var(--line)}
.map-banner p{margin:0}
.hero{position:relative;border-radius:16px;overflow:hidden;background:var(--brand);color:var(--brand-ink);margin:0 0 28px;min-height:280px;display:flex;align-items:flex-end}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,9,7,.15) 0%,rgba(11,9,7,.85) 78%)}
.hero-in{position:relative;z-index:1;padding:28px 30px 26px;max-width:720px}
.hero-in img{width:min(340px,80%);height:auto;display:block;margin-bottom:14px}
.hero h1{font-size:30px;color:#fff;margin:0 0 8px}
.hero p{margin:0 0 16px;color:#e9e1d6;font-size:16.5px}
.badge{display:inline-block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);border-radius:999px;padding:3px 10px;margin-bottom:12px;color:#fff}
.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:9px 16px;border-radius:999px;background:var(--accent);color:#fff;text-decoration:none;font-weight:650;font-size:14.5px}
.btn.alt{background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.25)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 6px}
.chip{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:13.5px;color:var(--muted)}.chip b{color:var(--ink)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin:14px 0 8px}
.card{display:flex;gap:12px;align-items:flex-start;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px;text-decoration:none;color:var(--ink);transition:border-color .15s,transform .15s}
.card:hover{border-color:var(--accent);transform:translateY(-1px)}
.card img{width:40px;height:40px;flex:none;border-radius:8px;background:var(--brand);padding:4px}
.card b{display:block;color:var(--ink);font-size:15.5px;margin-bottom:2px}.card span{color:var(--muted);font-size:13.5px;line-height:1.45;display:block}
footer{margin-top:64px;color:var(--muted);font-size:13px;border-top:1px solid var(--line);padding-top:18px;display:flex;flex-wrap:wrap;gap:6px 18px}
footer a{color:var(--muted)}
.top{position:fixed;right:18px;bottom:18px;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13px;color:var(--muted);text-decoration:none;box-shadow:0 2px 10px rgba(0,0,0,.08)}
.hbtns{display:none}.scrim{display:none}.dr{display:flex;flex-direction:column;flex:1}
.srch{padding:14px 12px 2px}
.sbox{display:flex;align-items:center;gap:8px;height:38px;padding:0 10px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--muted);cursor:text}
.sbox:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.sbox input{flex:1;min-width:0;border:0;background:none;outline:0;color:var(--ink);font:inherit;font-size:14.5px;-webkit-appearance:none}
.sbox input::-webkit-search-cancel-button{-webkit-appearance:none}
.sbox kbd{font:inherit;font-size:11.5px;border:1px solid var(--line);border-radius:5px;padding:0 6px;line-height:18px}
.sres{padding:8px 10px 24px}.sres ul{list-style:none;margin:0;padding:0}.sres li{margin:0}
.sres a{display:block;padding:8px 10px;border-radius:9px;text-decoration:none;color:var(--ink);line-height:1.35}
.sres a:hover,.sres a:focus{background:var(--code);outline:0}
.sres .sp{display:block;font-size:11.5px;color:var(--muted);letter-spacing:.02em}.sres b{display:block;font-size:14.5px;font-weight:650}
.sres .ss{display:block;font-size:12.5px;color:var(--muted);overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.sres mark{background:var(--accent-soft);color:var(--accent-ink);border-radius:3px;padding:0 1px}.sx{color:var(--muted);font-size:14px;padding:6px 10px;margin:0}
tr:target td{background:var(--accent-soft)!important}h2:target,h3:target{color:var(--accent-ink)}
.toc summary{cursor:pointer;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700;list-style:none;display:flex;align-items:center;gap:8px}
.toc summary::-webkit-details-marker{display:none}.toc summary::after{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg);margin:-3px 0 0 auto;transition:transform .15s}
.toc[open] summary::after{transform:rotate(-135deg);margin-top:3px}.toc summary span{text-transform:none;letter-spacing:0;font-weight:500;opacity:.8}
.rail{display:none}
@media (min-width:1280px){main{display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:44px;max-width:1440px}
.cnt{min-width:0}.cnt>.toc{display:none}
.rail{display:block;position:sticky;top:32px;align-self:start;max-height:calc(100vh - 64px);overflow:auto;font-size:13.5px;padding-top:6px}
.rail b{display:block;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.rail ul{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}.rail li{margin:0}
.rail a{display:block;padding:5px 0 5px 12px;margin-left:-1px;border-left:2px solid transparent;color:var(--muted);text-decoration:none;line-height:1.35}
.rail a:hover{color:var(--ink)}.rail a.on{color:var(--accent-ink);border-left-color:var(--accent);font-weight:600}}
@media (max-width:860px){.wrap{display:block}
nav.side{position:sticky;top:0;z-index:50;width:auto;height:auto;border-right:0;border-bottom:1px solid var(--line);overflow:visible;background:var(--brand)}
.bar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:0 10px 0 16px;height:56px;background:var(--brand)}
.brand{padding:0;background:none;flex:none}.wm{font-size:22px}.brand span{display:none}
.hbtns{display:flex;gap:4px}
.hb{display:flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;border-radius:10px;background:none;color:var(--brand-ink);cursor:pointer}
.hb:active{background:rgba(255,255,255,.1)}.hb .si{width:21px;height:21px}
.mb-i{display:inline-flex;flex-direction:column;justify-content:center;gap:4px;width:18px;height:18px;flex:none}.mb-i i{display:block;height:2px;border-radius:2px;background:currentColor;transition:transform .2s,opacity .2s}
nav.open .mb-i i:nth-child(1){transform:translateY(6px) rotate(45deg)}nav.open .mb-i i:nth-child(2){opacity:0}nav.open .mb-i i:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
.mb-i{width:20px}
.scrim{display:block;position:fixed;left:0;right:0;top:56px;bottom:0;background:rgba(0,0,0,.5);opacity:0;pointer-events:none;transition:opacity .2s}
nav.open .scrim{opacity:1;pointer-events:auto}
.dr{position:fixed;top:56px;right:0;bottom:0;width:min(340px,88vw);overflow-y:auto;overscroll-behavior:contain;background:var(--panel);border-left:1px solid var(--line);transform:translateX(100%);transition:transform .22s ease;visibility:hidden}
nav.open .dr{transform:none;visibility:visible}html.navlock{overflow:hidden}
.srch{padding:14px 14px 4px}.sbox{height:44px}.sbox input{font-size:16px}.sbox kbd{display:none}
.links{padding:4px 10px 16px}.grp{margin-top:12px}.grp>b{padding:4px 10px 4px}
.links a{min-height:44px;font-size:15.5px}
.side-foot{display:block;margin-top:auto}
.pager{margin-top:40px}.pager a{padding:12px 14px;font-size:14.5px}
main{padding:22px 16px 64px;overflow-wrap:break-word}html{scroll-padding-top:68px}h1{font-size:26px}h2{font-size:20px}.pg-ic{width:42px;height:42px}
.hero{min-height:230px}.hero-in{padding:20px 18px}.hero h1{font-size:23px}
.map-banner{flex-direction:column}.map-banner img{width:100%;height:auto;max-width:320px}
.top{display:none;right:14px;bottom:14px;padding:9px 14px}.top.show{display:block}
.toc{padding:0}.toc summary{padding:13px 16px;min-height:46px}.toc ul{display:block;padding:0 16px 12px;margin:0}.toc li{padding:6px 0;border-top:1px solid var(--line)}}
@media (max-width:640px){
.tw{border:0;background:none;overflow:visible}
table[data-m="cards"],table[data-m="cards"] tbody{display:block}
table[data-m="cards"] thead{display:none}
table[data-m="cards"] tr{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;margin:0 0 10px;padding:6px 0}
table[data-m="cards"] td{display:grid;grid-template-columns:38% 1fr;gap:10px;border:0;padding:5px 14px;background:none!important;white-space:normal}
table[data-m="cards"] td::before{content:attr(data-label);color:var(--muted);font-size:12.5px;font-weight:600}
table[data-m="cards"] td:first-child{display:block;font-weight:650;font-size:15.5px;border-bottom:1px solid var(--line);padding:6px 14px 9px;margin-bottom:4px}
table[data-m="cards"] td:first-child::before{display:none}
table[data-m="cards"] td[data-empty]{display:none}
table[data-m="cards"] tr:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
table[data-m="grid"]{font-size:13px}table[data-m="grid"] th,table[data-m="grid"] td{padding:8px 9px}table[data-m="grid"] th{white-space:normal}table[data-m="grid"] td:first-child{white-space:normal;min-width:6.5em;max-width:40vw}table[data-m="grid"] td:first-child .ic{width:20px;height:20px;margin:0;position:absolute;left:9px;top:8px}
table[data-m="grid"] td:first-child:has(.ic){padding-left:35px}
.tw:has(table[data-m="grid"]){overflow-x:auto;border:1px solid var(--line);background:var(--panel)}
table[data-m="grid"] th:first-child,table[data-m="grid"] td:first-child{position:sticky;left:0;background:var(--panel);z-index:1}
table[data-m="grid"] th:first-child{background:var(--code)}
td.nm{white-space:normal}
td code,li code,p code,h2 code,h3 code,h4 code{overflow-wrap:anywhere}
}
@media print{nav.side,.top{display:none}main{padding:0}}
'''


def esc(s):
    return html.escape(s, quote=True)


def head_icons(slug, body):
    rules = HEAD_ICON.get(slug, [])

    def h(m):
        tag, attrs, text = m.group(1), m.group(2), m.group(3)
        plain = re.sub('<[^>]+>', '', text)
        for pre, ic in rules:
            if plain.startswith(pre):
                return f'<{tag}{attrs}>{icon_img(ic)}{text}</{tag}>'
        return m.group(0)
    return re.sub(r'<(h[23])([^>]*)>(.*?)</\1>', h, body)


def map_banners(body):
    # put each map's banner beside the first paragraph after its h3 on the maps page
    for name, ic in MAP_BANNER.items():
        USED.add(ic)
        tag = f'<img src="img/{ic}.png" alt="{name} map" width="176" height="132">'
        new, n = re.subn(rf'(<h3 id="{name.lower()}">{name}</h3>\s*)<p>(.*?)</p>',
                         lambda m: f'{m.group(1)}<div class="map-banner">{tag}<p>{m.group(2)}</p></div>', body, count=1, flags=re.S)
        if n == 0:
            new = body.replace(f'<h3 id="{name.lower()}">{name}</h3>', f'<h3 id="{name.lower()}">{name}</h3><div class="map-banner">{tag}</div>', 1)
        body = new
    return body


def passive_icons(body):
    def p(m):
        n = m.group(1)
        ic = PASSIVE_ICON.get(n)
        return f'<strong>{icon_img(ic)}{n}:</strong>' if ic else m.group(0)
    return re.sub(r'<strong>([A-Za-z ]+):</strong>', p, body)


JS = '(function(){\nvar d=document,n=d.getElementById(\'nav\'),mb=n.querySelector(\'.mbtn\'),sb=n.querySelector(\'.sbtn\'),q=d.getElementById(\'q\'),R=d.getElementById(\'sres\'),L=d.getElementById(\'links\'),mq=matchMedia(\'(max-width:860px)\');\nfunction set(o){n.classList.toggle(\'open\',o);mb.setAttribute(\'aria-expanded\',o);d.documentElement.classList.toggle(\'navlock\',o&&mq.matches)}\nmb.addEventListener(\'click\',function(){set(!n.classList.contains(\'open\'))});\nsb.addEventListener(\'click\',function(){set(true);setTimeout(function(){q.focus()},60)});\nn.querySelector(\'.scrim\').addEventListener(\'click\',function(){set(false)});\nd.addEventListener(\'keydown\',function(e){\n if(e.key===\'Escape\'){if(q.value){q.value=\'\';run()}else set(false);if(d.activeElement===q&&!mq.matches)q.blur()}\n else if(e.key===\'/\'&&!/INPUT|TEXTAREA/.test(d.activeElement.tagName)){e.preventDefault();if(mq.matches)set(true);q.focus()}});\nn.addEventListener(\'click\',function(e){var a=e.target.closest(\'a\');if(a&&(L.contains(a)||R.contains(a)))set(false)});\nvar t=d.querySelector(\'.top\');function sc(){t.classList.toggle(\'show\',scrollY>600)}addEventListener(\'scroll\',sc,{passive:true});sc();\nvar IX=null,ld=false;\nfunction load(){if(ld)return;ld=true;fetch(\'search.json\').then(function(r){return r.json()}).then(function(j){IX=j;for(var i=0;i<j.length;i++){var e=j[i];e._n=e.h.toLowerCase();e._p=e.p.toLowerCase();e._t=e.t.toLowerCase()}run()}).catch(function(){ld=false})}\nfunction esc(s){return s.replace(/[&<>"]/g,function(c){return{\'&\':\'&amp;\',\'<\':\'&lt;\',\'>\':\'&gt;\',\'"\':\'&quot;\'}[c]})}\nfunction hl(s,ws){var o=esc(s);ws.forEach(function(w){if(w.length<2)return;o=o.replace(new RegExp(\'(\'+w.replace(/[.*+?^${}()|[\\]\\\\]/g,\'\\\\$&\')+\')\',\'ig\'),\'<mark>$1</mark>\')});return o}\nfunction snip(e,ws){var i=-1;for(var k=0;k<ws.length&&i<0;k++)i=e._t.indexOf(ws[k]);if(i<0)return e.t.slice(0,110)+(e.t.length>110?\'…\':\'\');var s=Math.max(0,i-45),x=e.t.slice(s,s+130);return (s>0?\'…\':\'\')+x+(s+130<e.t.length?\'…\':\'\')}\nfunction run(){\n var v=q.value.trim().toLowerCase();\n if(!v){R.hidden=true;L.hidden=false;R.innerHTML=\'\';return}\n L.hidden=true;R.hidden=false;\n if(!IX){load();R.innerHTML=\'<p class="sx">Loading…</p>\';return}\n var ws=v.split(/\\s+/),out=[];\n for(var i=0;i<IX.length;i++){var e=IX[i],s=0,ok=true;\n  for(var k=0;k<ws.length;k++){var w=ws[k],m=0;\n   if(e._n===v)m=60;else if(e._n.indexOf(w)===0)m=24;else if(e._n.indexOf(w)>=0)m=14;\n   if(e._p.indexOf(w)>=0)m+=6;if(!m&&e._t.indexOf(w)>=0)m=1+Math.min(3,e._t.split(w).length-1)*.5;\n   if(!m){ok=false;break}s+=m}\n  if(ok){if(e.k===\'r\')s+=2;out.push([s,e])}}\n out.sort(function(a,b){return b[0]-a[0]});out=out.slice(0,14);\n if(!out.length){R.innerHTML=\'<p class="sx">No results for “\'+esc(q.value.trim())+\'”.</p>\';return}\n R.innerHTML=\'<ul>\'+out.map(function(o){var e=o[1];return \'<li><a href="\'+e.u+\'"><span class="sp">\'+esc(e.p)+(e.s?\' › \'+esc(e.s):\'\')+\'</span><b>\'+hl(e.h,ws)+\'</b><span class="ss">\'+hl(snip(e,ws),ws)+\'</span></a></li>\'}).join(\'\')+\'</ul>\';\n}\nq.addEventListener(\'focus\',load);q.addEventListener(\'input\',run);\nq.addEventListener(\'keydown\',function(e){var as=R.querySelectorAll(\'a\');if(!as.length)return;if(e.key===\'Enter\'){e.preventDefault();as[0].click()}else if(e.key===\'ArrowDown\'){e.preventDefault();as[0].focus()}});\nR.addEventListener(\'keydown\',function(e){var as=[].slice.call(R.querySelectorAll(\'a\')),i=as.indexOf(d.activeElement);if(i<0)return;if(e.key===\'ArrowDown\'){e.preventDefault();(as[i+1]||as[i]).focus()}else if(e.key===\'ArrowUp\'){e.preventDefault();(i?as[i-1]:q).focus()}});\nvar rl=d.querySelector(\'.rail\');if(rl&&\'IntersectionObserver\' in window){var ra={};rl.querySelectorAll(\'a\').forEach(function(a){ra[a.getAttribute(\'href\').slice(1)]=a});var hs=[].slice.call(d.querySelectorAll(\'main h2[id]\')).filter(function(h){return ra[h.id]});\n function spy(){var cur=hs[0];for(var i=0;i<hs.length;i++){if(hs[i].getBoundingClientRect().top<120)cur=hs[i]}for(var k in ra)ra[k].classList.toggle(\'on\',cur&&k===cur.id)}addEventListener(\'scroll\',spy,{passive:true});spy()}\n})()\n'
ICON_SEARCH = '<svg class="si" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m20 20-4.6-4.6"/></svg>'


def name_cells(body):
    return re.sub(r'(<tr>\s*)<td>(<strong>)?(<img class="(?:ic|mthumb)")', r'\1<td class="nm">\2\3', body)


def toc(body):
    hs = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(hs) < 4:
        return ''
    items = ''.join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in hs)
    return (f'<details class="toc" id="toc"><summary>On this page <span>{len(hs)} sections</span></summary><ul>{items}</ul></details>'
            '<script>if(!matchMedia("(max-width:860px)").matches)document.getElementById("toc").open=true</script>')


def rail(body):
    hs = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(hs) < 4:
        return ''
    items = ''.join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in hs)
    return f'<aside class="rail" aria-label="On this page"><b>On this page</b><ul>{items}</ul></aside>'


def home(body):
    # hero
    USED.update(['ForestIconBig'])
    hero = f'''<section class="hero"><img class="hero-bg" src="img/ForestIconBig.png" alt=""><div class="hero-in">
<span class="badge">Unofficial fan wiki</span><img src="img/logo.png" alt="Megabonk" width="340" height="76"><h1>The numbers behind the game</h1>
<p>Every item, weapon, tome and character, and the formulas that run them, read straight from Megabonk's code.</p>
<div class="btns"><a class="btn" href="game.html">New here? How the game works</a><a class="btn alt" href="max-runs.html">Maxing a run</a></div></div></section>
<div class="chips"><span class="chip"><b>85</b> items</span><span class="chip"><b>30</b> weapons</span><span class="chip"><b>22</b> tomes</span><span class="chip"><b>21</b> characters</span><span class="chip"><b>3</b> maps</span><span class="chip">Game <b>v{VERSION}</b></span></div>'''
    body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, count=1, flags=re.S)
    # replace the "What's in here" table with cards
    m = re.search(r'(<h2 id="whats-in-here">.*?</h2>\s*)<div class="tw"><table>(.*?)</table></div>', body, re.S)
    if m:
        cards = []
        for href, name, desc in re.findall(r'<tr>\s*<td><a href="([^"]+)">([^<]+)</a></td>\s*<td>(.*?)</td>\s*</tr>', m.group(2), re.S):
            slug = href.replace('.html', '')
            ic = PAGE_ICON.get(slug, 'Gamba'); USED.add(ic)
            cards.append(f'<a class="card" href="{href}"><img src="img/{ic}.png" alt=""><div><b>{name}</b><span>{desc}</span></div></a>')
        body = body.replace(m.group(0), m.group(1) + '<div class="cards">' + ''.join(cards) + '</div>')
    return hero + body


GROUPS = [('Start', ['index', 'game']),
          ('How it works', ['mechanics', 'status', 'economy', 'maps', 'enemies']),
          ('Gear', ['items', 'weapons', 'tomes', 'characters']),
          ('Runs', ['tiers', 'max-runs', 'secrets']),
          ('Unlocks', ['quests', 'challenges', 'cosmetics']),
          ('Reference', ['faq'])]
TITLE = {s: t for s, t, _ in PAGES}
ORDER = [s for _, ss in GROUPS for s in ss]


def href(s):
    return './' if s == 'index' else s + '.html'


def nav(slug):
    out = []
    for g, ss in GROUPS:
        links = ''
        for s in ss:
            ic = PAGE_ICON[s]; USED.add(ic)
            cur = ' class="on" aria-current="page"' if s == slug else ''
            links += f'<a href="{href(s)}"{cur}><img src="img/{ic}.png" alt="" width="22" height="22">{esc(TITLE[s])}</a>'
        out.append(f'<div class="grp"><b>{g}</b>{links}</div>')
    return ''.join(out)


def pager(slug):
    i = ORDER.index(slug)
    prv = ORDER[i - 1] if i > 0 else None
    nxt = ORDER[i + 1] if i + 1 < len(ORDER) else None
    a = f'<a class="pv" href="{href(prv)}"><span>← Previous</span>{esc(TITLE[prv])}</a>' if prv else '<span></span>'
    b = f'<a class="nx" href="{href(nxt)}"><span>Next →</span>{esc(TITLE[nxt])}</a>' if nxt else '<span></span>'
    return f'<nav class="pager" aria-label="Previous and next page">{a}{b}</nav>'


def page(slug, title, body, desc):
    url = SITE + ('' if slug == 'index' else slug + '.html')
    full = 'bonk.wiki · Unofficial Megabonk data wiki' if slug == 'index' else f'{title} · bonk.wiki (Megabonk)'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#17130f"><link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="bonk.wiki"><meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style></head><body><div class="wrap"><nav class="side" id="nav" aria-label="Site"><div class="bar"><a class="brand" href="./"><b class="wm">bonk<i>.wiki</i></b><span>Unofficial Megabonk data wiki · v{VERSION}</span></a>
<div class="hbtns"><button class="hb sbtn" type="button" aria-label="Search">{ICON_SEARCH}</button><button class="hb mbtn" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Menu"><span class="mb-i" aria-hidden="true"><i></i><i></i><i></i></span></button></div></div>
<div class="scrim"></div><div class="dr" id="drawer"><div class="srch" role="search"><label class="sbox">{ICON_SEARCH}<input id="q" type="search" placeholder="Search the wiki" autocomplete="off" spellcheck="false" aria-label="Search the wiki"><kbd>/</kbd></label></div>
<div class="sres" id="sres" hidden></div><div class="links" id="links">{nav(slug)}</div><div class="side-foot">Fan-made. Numbers from the game's code.<br><a href="{REPO}">Source on GitHub</a></div></div></nav>
<main id="top"><div class="cnt">{body}<p class="suggest">Spotted a mistake or something missing? <a href="{edit_url(slug)}" target="_blank" rel="noopener">Suggest an edit</a> (opens a GitHub issue).</p>{pager(slug) if slug in ORDER else ''}<footer><span>Fan-made guide, not affiliated with the developers of Megabonk. Game art © its developers.</span><span>Numbers read from game v{VERSION}; they can change with patches.</span><span>Updated {UPDATED}</span><a href="{REPO}">GitHub</a></footer></div>{rail(body)}</main></div>
<a class="top" href="#top" aria-label="Back to top">↑ Top</a><script>{JS}</script></body></html>'''


def edit_url(slug):
    from urllib.parse import quote
    t = TITLE.get(slug, slug)
    return f'{REPO}/issues/new?template=suggest-edit.yml&title={quote("[Edit] " + t)}&page={quote(t + " (" + SITE + ("" if slug == "index" else slug + ".html") + ")")}'


def title_block(slug, body):
    if slug == 'index':
        return home(body)
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    ic = PAGE_ICON[slug]; USED.add(ic)
    h1 = m.group(1) if m else ''
    head = f'<div class="pg-head"><img class="pg-ic" src="img/{ic}.png" alt="" width="52" height="52"><h1>{h1}</h1></div><p class="meta">Game v{VERSION} · updated {UPDATED} · <a href="{edit_url(slug)}" target="_blank" rel="noopener">Suggest an edit</a></p>'
    rest = body.replace(m.group(0), '', 1) if m else body
    return head + toc(rest) + rest


def assets():
    os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
    logo = Image.open(os.path.join(ART, 'MegabonkLogo.png')).convert('RGBA')
    bb = logo.getbbox(); logo = logo.crop(bb)
    l2 = logo.copy(); l2.thumbnail((680, 200), Image.LANCZOS); l2.save(os.path.join(OUT, 'img', 'logo.png'), optimize=True)
    dice = Image.open(os.path.join(ART, 'Dice.png')).convert('RGBA')
    dice.resize((64, 64), Image.NEAREST).save(os.path.join(OUT, 'favicon.png'))
    bg = Image.new('RGBA', (180, 180), (23, 19, 15, 255)); bg.alpha_composite(dice.resize((150, 150), Image.NEAREST), (15, 15))
    bg.convert('RGB').save(os.path.join(OUT, 'apple-touch-icon.png'))
    # social share image
    W, H = 1200, 630
    forest = Image.open(os.path.join(ART, 'ForestIconBig.png')).convert('RGB')
    s = max(W / forest.width, H / forest.height)
    f = forest.resize((int(forest.width * s) + 1, int(forest.height * s) + 1), Image.NEAREST)
    f = f.crop(((f.width - W) // 2, (f.height - H) // 2, (f.width - W) // 2 + W, (f.height - H) // 2 + H)).convert('RGBA')
    shade = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(shade)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=(11, 9, 7, int(90 + 150 * y / H)))
    f.alpha_composite(shade)
    l3 = logo.copy(); l3.thumbnail((760, 200), Image.LANCZOS); f.alpha_composite(l3, ((W - l3.width) // 2, 150))
    fnt = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf', 54)
    fnt2 = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Medium.otf', 30)
    d = ImageDraw.Draw(f)
    for txt, fo, y, col in [('The numbers behind the game', fnt, 380, (255, 255, 255)),
                            ('Items · weapons · tomes · formulas — read from the code', fnt2, 460, (233, 225, 214)),
                            ('bonk.wiki · unofficial fan wiki', fnt2, 540, (251, 146, 60))]:
        w = d.textlength(txt, font=fo); d.text(((W - w) / 2, y), txt, font=fo, fill=col)
    f.convert('RGB').save(os.path.join(OUT, 'og.png'), optimize=True)


def extras():
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
    import datetime
    today = datetime.date.today().isoformat()
    urls = ''.join(f'<url><loc>{SITE}{"" if s == "index" else s + ".html"}</loc><lastmod>{today}</lastmod></url>' for s, _, _ in PAGES)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    body = f'<div class="pg-head"><img class="pg-ic" src="img/Curse.png" alt="" width="52" height="52"><h1>Page not found</h1></div><p class="meta">That page bonked.</p><p>Try the <a href="./">home page</a> or pick a section from the menu.</p>'
    USED.add('Curse')
    open(os.path.join(OUT, '404.html'), 'w').write(page('404', 'Page not found', body, DESC['index']).replace('<link rel="canonical" href="https://bonk.wiki/404.html">', ''))


def mobile_tables(body):
    """Tag each table so phones can show wide ones as stacked cards (labels from the header) and keep numeric grids scrollable."""
    def one(m):
        tb = m.group(0)
        heads = [html.unescape(re.sub('<[^>]+>', '', h)).strip() for h in re.findall(r'<th[^>]*>(.*?)</th>', tb, re.S)]
        n = len(heads)
        cells = [re.sub('<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', tb, re.S)]
        numeric_heads = n > 2 and sum(bool(re.match(r'^[\d×%.,+−\- ]+$', h)) or h.endswith('%') for h in heads[1:]) >= (n - 1) * 0.6
        rows = [[html.unescape(re.sub('<[^>]+>', '', c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)] for r in re.findall(r'<tr[^>]*>(.*?)</tr>', tb, re.S)]
        rows = [r for r in rows if r]
        rest = [c for r in rows for c in r[1:]]
        checks = rest and sum(c in ('✓', '✗', '—', '') or c.startswith(('✓', '✗')) for c in rest) > len(rest) * 0.6
        isnum = lambda c: bool(re.match(r'^[×x~≈+−\-]?[\d.,]+(%|×| ?[kKM])?( \w{1,8})?$|^—$', c))
        numeric = n <= 6 and len(rows) > 0 and all(sum(isnum(r[j]) for r in rows if j < len(r)) >= len(rows) * 0.7 for j in range(1, n))
        cavg = [sum(len(r[j]) for r in rows if j < len(r)) / max(1, len(rows)) for j in range(n)]
        colmax = max(cavg, default=0)
        restmax = max(cavg[1:], default=0)
        if (n <= 3 and colmax < 45) or numeric_heads or ((checks or numeric) and restmax < 30):
            cls = 'grid'
        else:
            cls = 'cards'
        def row(rm):
            i = [0]
            def cell(cm):
                lab = heads[i[0]] if i[0] < n else ''
                i[0] += 1
                inner = cm.group(2) if cls == 'grid' else f'<span class="cv">{cm.group(2)}</span>'
                empty = ' data-empty' if not re.sub('<[^>]+>', '', cm.group(2)).strip() and '<img' not in cm.group(2) else ''
                return f'<td{cm.group(1)} data-label="{html.escape(lab, quote=True)}"{empty}>{inner}</td>'
            return re.sub(r'<td([^>]*)>(.*?)</td>', cell, rm.group(0), flags=re.S)
        tb = re.sub(r'<tr>.*?</tr>', row, tb, flags=re.S)
        return tb.replace('<table', f'<table data-m="{cls}"', 1)
    return re.sub(r'<table.*?</table>', one, body, flags=re.S)


def slugify(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).lower()
    s = re.sub(r"['’]", '', s)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def row_ids(body):
    """Give each table row an id from its first cell, so search can link straight to it."""
    seen = set(re.findall(r'id="([^"]+)"', body))
    def one(m):
        first = re.search(r'<td[^>]*>(.*?)</td>', m.group(0), re.S)
        if not first:
            return m.group(0)
        name = re.sub(r'\s*\(.*?\)', '', re.sub(r'<[^>]+>', '', first.group(1))).strip()
        sid = 'r-' + slugify(name)
        if len(sid) < 4 or len(name) > 40 or sid in seen:
            return m.group(0)
        seen.add(sid)
        return m.group(0).replace('<tr>', f'<tr id="{sid}">', 1)
    return re.sub(r'<tbody>.*?</tbody>', lambda tb: re.sub(r'<tr>.*?</tr>', one, tb.group(0), flags=re.S), body, flags=re.S)


def txt(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'</(td|th)>', ' · ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'\s+', ' ', html.unescape(h))
    return re.sub(r'(\s*·\s*)+', ' · ', h).strip(' ·')


def index_page(slug, title, body):
    """Search entries: the page, each h2/h3 section, and each named table row."""
    url = href(slug).replace('./', '')
    out = []
    parts = re.split(r'(<h[23] id="[^"]+">.*?</h[23]>)', body, flags=re.S)
    intro = txt(re.sub(r'<div class="pg-head">.*?</div>|<p class="meta">.*?</p>|<section class="hero">.*?</section>|<div class="chips">.*?</div>', ' ', parts[0], flags=re.S))
    out.append({'k': 'p', 'p': title, 'h': title, 's': '', 'u': url or './', 't': intro[:400]})
    h2 = ''
    for i in range(1, len(parts), 2):
        m = re.match(r'<h([23]) id="([^"]+)">(.*?)</h[23]>', parts[i], re.S)
        lvl, hid, ht = m.group(1), m.group(2), txt(m.group(3))
        if lvl == '2':
            h2 = ht
        sec = parts[i + 1]
        out.append({'k': 's', 'p': title, 'h': ht, 's': '' if lvl == '2' else h2, 'u': f'{url}#{hid}', 't': txt(re.sub(r'<table.*?</table>', ' ', sec, flags=re.S))[:600]})
        for rid, row in re.findall(r'<tr id="([^"]+)">(.*?)</tr>', sec, re.S):
            cells = [txt(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
            out.append({'k': 'r', 'p': title, 'h': cells[0], 's': ht, 'u': f'{url}#{rid}', 't': ' · '.join(c for c in cells[1:] if c)[:300]})
    return out


def build():
    assets()
    INDEX = []
    for slug, title, fn in PAGES:
        md = open(os.path.join(SRC, fn), encoding='utf-8').read()
        md = md.replace('Nov 16, 2026 · @David\n', '')
        md = re.sub(r'^Updated DATE · Game version 1\.0\.69\n', '', md, flags=re.M)
        md = re.sub(r'&#91;embedded content:[^\n]*\n', STAGE_TABLE + '\n', md)
        md = md.replace('<p class="hero">', '<p class="hero-maps">')
        body = markdown.markdown(md, extensions=['tables', 'sane_lists', 'toc'])
        if slug == 'game':
            body = re.sub(r'<p class="hero-maps">.*?</p>', '', body, flags=re.S)
            body = body.replace('<h2 id="how-maps-are-generated">', '<div class="map-banner" style="margin-top:28px">'
                                '<img src="img/ForestIconBig.png" alt="Forest" width="176" height="132"><img src="img/DesertIconBig.png" alt="Desert" width="176" height="132">'
                                '<img src="img/GraveyardIconBig.png" alt="Graveyard" width="176" height="132"></div><h2 id="how-maps-are-generated">', 1)
            USED.update(MAP_BANNER.values())
        body = add_icons(slug, body)
        body = head_icons(slug, body)
        if slug == 'maps':
            body = map_banners(body)
            for nm, ic in MAP_BANNER.items():
                body = body.replace(f'<tr>\n<td>{nm}</td>', f'<tr>\n<td class="nm"><img class="mthumb" src="img/{ic}.png" alt="" width="40" height="30">{nm}</td>', 1)
        if slug == 'characters':
            body = passive_icons(body)
        body = body.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
        body = name_cells(body)
        body = re.sub(r'<table>(\s*<thead>\s*<tr>(?:\s*<th[^>]*>(?:(?!</tr>).)*?</th>){9,}\s*</tr>)', r'<table class="dense">\1', body, flags=re.S)
        body = mobile_tables(body)
        body = row_ids(body)
        body = title_block(slug, body)
        INDEX.extend(index_page(slug, title, body.split('<details class="toc"')[0] + body.split('</details>', 1)[-1] if '<details class="toc"' in body else body))
        open(os.path.join(OUT, slug + '.html'), 'w', encoding='utf-8').write(page(slug, title, body, DESC[slug]))
    json.dump(INDEX, open(os.path.join(OUT, 'search.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    extras()
    copy_used(OUT)
    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    open(os.path.join(os.path.dirname(OUT), 'README.md'), 'w').write(
        '# Megabonk Data\n\nA data-driven Megabonk guide: exact item, tome, weapon and character numbers, and the game\'s real formulas read from its code (v1.0.69).\n\n'
        'Live site: https://bonk.wiki/\n\nSource pages and build scripts are in `src/` (`python3 src/build_site.py` rebuilds `docs/`). Suggest changes with the "Suggest an edit" link on any page.\n\nFan-made; not affiliated with the developers of Megabonk. Game art belongs to its developers.\n')


build()
