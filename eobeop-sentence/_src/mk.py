# -*- coding: utf-8 -*-
"""usage: python3 mk.py NN   -> reads author/chNN.py (META, ITEMS) + src/data_chNN_points.py -> data/chNN.json, runs validate"""
import sys, json, re, importlib.util
import lib, validate
def load_author(ch):
    sp=importlib.util.spec_from_file_location('au%d'%ch,f'{lib.BASE}/author/ch{ch:02d}.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def build(ch):
    au=load_author(ch); P=lib.load_points(ch)
    base=getattr(au,'BASE_SETS',[]); baseids={s['id'] for s in base}
    sets=list(base)
    for k in sorted(P):
        sid=('p%d'%k) if ch==1 else 'c%02dp%d'%(ch,k)
        if sid in baseids: continue
        meta=au.META[k]; v=P[k]
        page=int(re.sub(r'\D','',v['page']))
        items=[]
        for kk,no,d in [x for x in lib.src_items(ch) if x[0]==k]:
            a=au.ITEMS[(k,no)]
            chunks=[]
            for c in a['c']:
                en,ko,kind,lab=c[:4]; dd=dict(en=en,ko=ko,k=kind,lab=lab)
                if len(c)>4 and c[4]: dd['h']=[list(x) for x in c[4]]
                chunks.append(dd)
            f=lib.src_fields(d)
            nt=a['n']
            items.append(dict(no=no,chunks=chunks,tr=f['tr'],why=f['why'],ex=f['ex'],st=f['st'],verb=dict(ok=a['v'][0],no=a['v'][1]),note=dict(t=nt[0],lines=list(nt[1:]))))
        s=dict(id=sid,page=page,title='POINT %d'%k,sub=meta['sub'],prompt=meta['prompt'],pnote=dict(t=meta['pnote'][0],lines=list(meta['pnote'][1:])),items=items)
        for opt in ('taps','cprompt','legend'):
            if opt in meta: s[opt]=meta[opt]
        sets.append(s)
    sets.sort(key=lambda s:int(re.sub(r'\D','',s['id'].split('p')[-1])))
    return sets
if __name__=='__main__':
    ch=int(sys.argv[1]); sets=build(ch)
    json.dump(sets,open(f'{lib.BASE}/data/ch{ch:02d}.json','w',encoding='utf-8'),ensure_ascii=False)
    e,w=validate.check(ch)
    print(f'CH{ch:02d}: sets={len(sets)} items={sum(len(s["items"]) for s in sets)} errors={len(e)} warnings={len(w)}')
    for x in e: print('  ERR',x)
    for x in w: print('  warn',x)
    sys.exit(1 if e else 0)
