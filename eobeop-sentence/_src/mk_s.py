# -*- coding: utf-8 -*-
"""usage: python3 mk_s.py NN  -> author/chNNs.py + src/data_chNN_rest.py -> data/chNNs.json (짧은 지문 / 내신 서술형), runs validation"""
import sys, json, re, importlib.util, html
import lib
KINDS={'','S','M','V','C'}
def load_author(ch):
    sp=importlib.util.spec_from_file_location('aus%d'%ch,f'{lib.BASE}/author/ch{ch:02d}s.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def sid(ch,setno): return 'c%02ds%d'%(ch,setno-200)
def all_points():
    out={}
    for c in range(1,15):
        try: P=lib.load_points(c)
        except Exception: continue
        for k in P: out[f'{c}.{k}']=True
    return out
def build(ch):
    au=load_author(ch); src=lib.src_items_s(ch); pg=lib._pages_s(ch)
    sets=[]
    for setno,title,page in ((201,'짧은 지문 연습 제대로',pg[0]),(202,'내신 서술형 대비 제대로',pg[1])):
        meta=au.META[setno]; items=[]
        for x in [y for y in src if y['setno']==setno]:
            a=au.ITEMS[(setno,x['no'])]; d=x['d']
            chunks=[]
            for c in a['c']:
                en,ko,kind,lab=c[:4]; dd=dict(en=en,ko=ko,k=kind,lab=lab)
                if len(c)>4 and c[4]: dd['h']=[list(z) for z in c[4]]
                chunks.append(dd)
            f=lib.src_fields(d); nt=a['n']
            it=dict(no=x['no'],chunks=chunks,tr=f['tr'],why=f['why'],ex=f['ex'],st=f['st'],verb=dict(ok=a['v'][0],no=a['v'][1]),note=dict(t=nt[0],lines=list(nt[1:])))
            if a.get('tp'): it['taps']=[dict(k=z[0],t=z[1]) for z in a['tp']]
            if x['ctx']: it['ctx']=x['ctx']
            if x['kor']: it['kor']=x['kor']
            if a.get('pts'): it['pts']=list(a['pts'])
            if x['arr']:
                seq=a.get('seq')
                if seq:
                    od=dict(pool=lib.pool_order(list(seq)+list(a.get('extra',[])),sid(ch,setno)+x['no']),seq=list(seq))
                    if a.get('fix'): od['fix']=a['fix']
                    it['order']=od
            items.append(it)
        s=dict(id=sid(ch,setno),page=page,title=title,sub=meta['sub'],prompt=meta['prompt'],pnote=dict(t=meta['pnote'][0],lines=list(meta['pnote'][1:])),items=items)
        if 'cprompt' in meta: s['cprompt']=meta['cprompt']
        sets.append(s)
    return sets
def check(ch,sets):
    errs=[];warn=[]
    src=lib.src_items_s(ch); got={}
    PTS=all_points()
    for s in sets:
        pn=s.get('pnote',{})
        if not pn.get('t') or not pn.get('lines'): errs.append(f'set {s["id"]} pnote empty')
        if not s.get('sub') or not s.get('prompt'): errs.append(f'set {s["id"]} sub/prompt empty')
        for it in s['items']: got[(s['id'],it['no'])]=(s,it)
    if len(got)!=len(src): errs.append(f'count {len(got)} != source {len(src)}')
    for x in src:
        tag=f"{sid(ch,x['setno'])}/{x['no']}"; key=(sid(ch,x['setno']),x['no'])
        if key not in got: errs.append(f'{tag}: missing'); continue
        s,it=got[key]; d=x['d']; f=lib.src_fields(d)
        for fld in ('tr','why'):
            if it.get(fld)!=f[fld]: errs.append(f'{tag}: {fld} differs from source')
        if (it.get('ex') or '')!=f['ex']: errs.append(f'{tag}: ex differs from source')
        if [list(z) for z in it.get('st',[])]!=f['st']: errs.append(f'{tag}: st differs from source')
        ch_=it.get('chunks',[])
        if not ch_: errs.append(f'{tag}: no chunks'); continue
        joined=lib.norm(' '.join(c['en'] for c in ch_))
        vs=lib.plain_variants(d['t'],d['ans'])
        if joined not in vs: errs.append(f'{tag}: chunk text != sentence. got "{" ".join(c["en"] for c in ch_)}" | expected one of {sorted(vs)[:3]}')
        for c in ch_:
            if c.get('k','') not in KINDS: errs.append(f'{tag}: bad kind {c.get("k")}')
            if not c.get('en','').strip(): errs.append(f'{tag}: empty en')
            if not c.get('ko','').strip(): errs.append(f'{tag}: empty ko for "{c.get("en")}"')
            if re.search(r'[A-Za-z]',c.get('ko','')): errs.append(f'{tag}: latin in ko "{c["ko"]}"')
            if c.get('k') in ('S','M','V','C') and not c.get('lab'): errs.append(f'{tag}: no label for "{c["en"]}"')
            if c.get('k','')=='' and c.get('lab'): warn.append(f'{tag}: label on plain chunk "{c["en"]}"')
            pos=0
            for hh in c.get('h',[]):
                i=c['en'].find(hh[0],pos)
                if i<0 or hh[1] not in ('s','c','v'): errs.append(f'{tag}: bad h {hh} in "{c["en"]}"')
                else: pos=i+len(hh[0])
        vk=it.get('verb',{}); ok,no_=vk.get('ok'),vk.get('no')
        if not ok or not no_ or ok==no_: errs.append(f'{tag}: verb pair bad {vk}')
        else:
            vch=[c for c in ch_ if c['k']=='V']
            if not vch: errs.append(f'{tag}: no V chunk')
            elif not any(re.search(r'(?<![\w])'+re.escape(ok)+r'(?![\w])',c['en']) for c in vch): errs.append(f'{tag}: verb.ok "{ok}" not found in V chunk')
        tk=[z['k'] for z in (it.get('taps') or s.get('taps',[]))] or ['S']
        if not any(c['k'] in tk for c in ch_): errs.append(f'{tag}: no chunk of tap kind {tk}')
        n=it.get('note',{})
        if not n.get('t') or not n.get('lines'): errs.append(f'{tag}: note empty')
        for p in it.get('pts',[]):
            if p not in PTS: errs.append(f'{tag}: pts "{p}" does not exist')
        if x['arr']:
            od=it.get('order')
            if not od: errs.append(f'{tag}: arrangement item needs seq (order)')
            else:
                a=sorted(w.lower() for w in x['hintwords']); b=sorted(w.lower() for w in od['pool'])
                if a!=b: errs.append(f'{tag}: seq {od["seq"]} is not a permutation of hint words {x["hintwords"]}')
                ans=lib.norm(' '.join(od['seq']))  # order check: each unit found in answer sentence in order (stem match)
                sent=' '.join(c['en'] for c in ch_).lower(); pos=0; okc=True; changed=[]
                for w in od['seq']:
                    wl=w.lower(); i=sent.find(wl,pos)
                    if i<0:
                        changed.append(w); st_=wl[:max(3,len(wl)-3)]; i=sent.find(st_,pos)
                        if i>=0: pos=i+len(st_)
                    else: pos=i+len(wl)
                if not okc: errs.append(f'{tag}: seq order does not follow answer sentence')
                if changed and not od.get('fix'): errs.append(f'{tag}: units {changed} change form; add fix text')
        elif it.get('order'): errs.append(f'{tag}: order given for a non-arrangement item')
    return errs,warn
if __name__=='__main__':
    ch=int(sys.argv[1]); sets=build(ch)
    json.dump(sets,open(f'{lib.BASE}/data/ch{ch:02d}s.json','w',encoding='utf-8'),ensure_ascii=False)
    e,w=check(ch,sets)
    print(f'CH{ch:02d}s: sets={len(sets)} items={sum(len(s["items"]) for s in sets)} errors={len(e)} warnings={len(w)}')
    for x in e: print('  ERR',x)
    for x in w: print('  warn',x)
    sys.exit(1 if e else 0)
