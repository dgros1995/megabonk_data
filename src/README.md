# bonk.wiki source

- `wiki/*.md` — every page's text. Edit these, then rebuild.
- `build_site.py` — turns `wiki/` into the site in `../docs/` (icons, tables, mobile layout, sitemap). Run `python3 src/build_site.py`.
- `gen_tiers.py`, `gen_weapons.py` — regenerate `wiki/tiers.md` and `wiki/weapons.md` from data (run before the build when that data changes).
- `gen_unlocks.py`, `achparse.py` — rebuilt the quest, challenge and cosmetic pages from the game's asset files (need the game's files and localisation tables; one-off).
- `data/game_data.json` — the item, weapon, tome, character, enemy, map and shop database dumped from the game (v1.0.69).
- `art/` — icons extracted from the game.

Needs Python 3 with `markdown` and `Pillow`.
