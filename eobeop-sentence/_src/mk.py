# -*- coding: utf-8 -*-
"""usage: python3 mk.py NN   -> reads author/chNN.py (META, ITEMS) + src/data_chNN_points.py -> data/chNN.json, runs validate"""
import sys, json, re, importlib.util
import lib, validate
def load_author(ch,part='p'):
    sp=importlib.util.spec_from_file_location('au%d%s'%(ch,part),f'{lib.BASE}/author/ch{ch:02d}{"" if part=="p" else "q"}.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def build(ch,part='p'):
    au=load_author(ch,part); P=lib.load_points(ch) if part=='p' else lib.load_rest(ch)
    base=getattr(au,'BASE_SETS',[]); baseids={s['id'] for s in base}
    sets=list(base)
    for k in sorted(P):
        sid=(('p%d'%k) if ch==1 else 'c%02dp%d'%(ch,k)) if part=='p' else 'c%02dq%d'%(ch,k-100)
        if sid in baseids: continue
        meta=au.META[k]; v=P[k]
        page=int(re.sub(r'\D','',v['page']))
        items=[]
        for kk,no,d in [x for x in lib.src_items(ch,part) if x[0]==k]:
            a=au.ITEMS[(k,no)]
            chunks=[]
            for c in a['c']:
                en,ko,kind,lab=c[:4]; dd=dict(en=en,ko=ko,k=kind,lab=lab)
                if len(c)>4 and c[4]: dd['h']=[list(x) for x in c[4]]
                chunks.append(dd)
            f=lib.src_fields(d)
            nt=a['n']
            itd=dict(no=no,chunks=chunks,tr=f['tr'],why=f['why'],ex=f['ex'],st=f['st'],verb=dict(ok=a['v'][0],no=a['v'][1]),note=dict(t=nt[0],lines=list(nt[1:])))
            if a.get('tp'): itd['taps']=[dict(k=x[0],t=x[1]) for x in a['tp']]
            items.append(itd)
        s=dict(id=sid,page=page,title=(v['title'] if part=='q' else 'POINT %d'%k),sub=meta['sub'],prompt=meta['prompt'],pnote=dict(t=meta['pnote'][0],lines=list(meta['pnote'][1:])),items=items)
        for opt in ('taps','cprompt','legend'):
            if opt in meta: s[opt]=meta[opt]
        sets.append(s)
    sets.sort(key=lambda s:int(re.sub(r'\D','',s['id'].split('p')[-1])))
    return sets
if __name__=='__main__':
    a=sys.argv[1]; part='q' if a.endswith('q') else 'p'; ch=int(a.rstrip('q')); sets=build(ch,part)
    json.dump(sets,open(f'{lib.BASE}/data/ch{ch:02d}{"" if part=="p" else "q"}.json','w',encoding='utf-8'),ensure_ascii=False)
    e,w=validate.check(ch,part=part)
    print(f'CH{ch:02d}: sets={len(sets)} items={sum(len(s["items"]) for s in sets)} errors={len(e)} warnings={len(w)}')
    for x in e: print('  ERR',x)
    for x in w: print('  warn',x)
    sys.exit(1 if e else 0)
