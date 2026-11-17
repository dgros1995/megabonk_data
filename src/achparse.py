import pickle, struct, re, json
SP = '/tmp/claude-0/-home-claude/820accf7-f8f7-58c4-a390-8f4a6ae1f721/scratchpad/'
by = pickle.load(open(SP + 'mb_raw.pkl', 'rb'))
guid, keys, text = pickle.load(open(SP + 'loc.pkl', 'rb'))


class R:
    def __init__(s, b): s.b = b; s.p = 0
    def al(s): s.p = (s.p + 3) & ~3
    def i32(s): v = struct.unpack_from('<i', s.b, s.p)[0]; s.p += 4; return v
    def f32(s): v = struct.unpack_from('<f', s.b, s.p)[0]; s.p += 4; return v
    def i64(s): v = struct.unpack_from('<q', s.b, s.p)[0]; s.p += 8; return v
    def u8(s): v = s.b[s.p]; s.p += 1; return v
    def str(s):
        n = s.i32(); v = s.b[s.p:s.p + n].decode('utf8', 'replace'); s.p += n; s.al(); return v
    def pptr(s): return (s.i32(), s.i64())
    def header(s):
        s.pptr(); s.u8(); s.al(); s.pptr(); return s.str()
    def locstr(s):
        tbl = s.str(); kid = s.i64(); key = s.str(); s.i32(); s.u8(); s.al(); n = s.i32()
        assert n == 0, ('locals', n)
        return (tbl, kid, key)


def loc(ls):
    tbl, kid, key = ls
    t = guid.get(tbl, tbl)
    return text.get(t, {}).get(kid) if kid else None


def achievement(b):
    r = R(b); name = r.header()
    ln = r.locstr(); ld = r.locstr()
    en = r.u8(); hid = r.u8(); r.al(); r.i32()
    a = dict(asset=name, enabled=bool(en), hidden=bool(hid), internal=r.str(), stat=r.str(), target=r.i32(), targetF=r.f32(), targetS=r.str())
    r.pptr(); a['sort'] = r.i32(); a['difficulty'] = r.i32(); a['type'] = r.i32()
    n = r.i32(); ks = []
    for _ in range(n):
        k = r.str(); lv = r.locstr(); ks.append((k, loc(lv)))
    a['keys'] = ks; a['iter'] = r.i32(); a['useIter'] = bool(r.u8()); r.al()
    a['name'] = loc(ln); a['desc'] = loc(ld)
    a['rest'] = len(b) - r.p
    return a


if __name__ == '__main__':
    out = []; bad = 0
    for pid, b in by['MyAchievement']:
        try:
            a = achievement(b); a['pid'] = pid; out.append(a)
        except Exception as e:
            bad += 1; print('ERR', pid, e)
    print(len(out), 'bad', bad)
    json.dump(out, open(SP + 'achievements_raw.json', 'w'), indent=1, ensure_ascii=False)
    for a in out[:8]: print(a)
