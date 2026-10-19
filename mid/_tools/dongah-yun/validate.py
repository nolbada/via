import json,sys,re
ROLES={'주어','동사','목적어','간접목적어','직접목적어','보어','목적격보어','수식어','접속사'}
units={u['id']:u for u in json.load(open('/tmp/claude-0/w3/units.json'))}
def norm(s):return s.replace('’',"'").replace('‘',"'")
def check(path):
    D=json.load(open(path));err=[]
    for d in D:
        i=d.get('id');u=units.get(i)
        if not u:err.append((i,'unknown id'));continue
        if d.get('en')!=u['en']:err.append((i,'en differs from units'))
        ch=d['ch'];j=''.join((' ' if (n and not c.get('g')) else '')+c['t'] for n,c in enumerate(ch))
        if norm(j)!=norm(d['en']):err.append((i,'join!=en: '+j))
        for n,c in enumerate(ch):
            if c['r'] not in ROLES:err.append((i,'bad role %d'%n))
            if not c.get('k'):err.append((i,'no k %d'%n))
        ko=d.get('ko','')
        if not ko:err.append((i,'no ko'))
        x=d.get('x',{});rs=x.get('rounds')
        if not rs:err.append((i,'no rounds'));continue
        g=x.get('glue')
        if g is not None and ch[g]['r']!='접속사':err.append((i,'glue not 접속사'))
        if g is None and any(c['r']=='접속사' for c in ch):err.append((i,'접속사 present but glue null'))
        cov=set()
        for r in rs:
            ci=r['ci'];cov|=set(ci)
            if ci!=sorted(ci):err.append((i,'ci unsorted'))
            roles=[ch[k]['r'] for k in ci];fm=r['fm']
            if roles.count('동사')<1:err.append((i,'round w/o verb'))
            has=lambda t:t in roles
            exp={1:not(has('보어') or has('목적어') or has('간접목적어')),2:has('보어') and not has('목적어'),3:has('목적어') and not has('간접목적어') and not has('목적격보어'),4:has('간접목적어') and has('직접목적어'),5:has('목적어') and has('목적격보어')}
            if fm not in exp or not exp[fm]:
                # allow 직접목적어-only etc
                err.append((i,'fm %s vs roles %s'%(fm,roles)))
        allc=set(range(len(ch)))-({g} if g is not None else set())
        if cov!=allc:err.append((i,'rounds cover mismatch missing=%s'%sorted(allc-cov)))
    return D,err
if __name__=='__main__':
    for p in sys.argv[1:]:
        D,e=check(p);print(p,len(D),'units',len(e),'errors')
        for x in e:print('  ',x)
