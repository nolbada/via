# -*- coding: utf-8 -*-
import sys, json, re, html
import lib
KINDS={'','S','M','V','C'}
def check(ch, path=None, part='p'):
    path=path or f'{lib.BASE}/data/ch{ch:02d}{"" if part=="p" else "q"}.json'
    errs=[];warn=[]
    try: sets=json.load(open(path,encoding='utf-8'))
    except Exception as e: return [f'JSON load fail: {e}'],[]
    src=lib.src_items(ch,part)
    got={}
    for s in sets:
        for k in ('id','page','title','sub','prompt','pnote','items'):
            if k not in s: errs.append(f'set {s.get("id")} missing {k}')
        pn=s.get('pnote',{})
        if not pn.get('t') or not pn.get('lines'): errs.append(f'set {s.get("id")} pnote empty')
        for it in s['items']: got[(s['id'],it['no'])]=(s,it)
    # expected set ids
    setid=(lambda k: ('p%d'%k) if ch==1 else 'c%02dp%d'%(ch,k)) if part=='p' else (lambda k: 'c%02dq%d'%(ch,k-100))
    exp=[(setid(k),no,d) for k,no,d in src]
    if len(got)!=len(exp): errs.append(f'count {len(got)} != source {len(exp)}')
    for sid,no,d in exp:
        key=(sid,no); tag=f'{sid}/{no}'
        if key not in got: errs.append(f'{tag}: missing'); continue
        s,it=got[key]
        f=lib.src_fields(d)
        for fld in ('tr','why'):
            if it.get(fld)!=f[fld]: errs.append(f'{tag}: {fld} differs from source')
        if (it.get('ex') or '')!=f['ex']: errs.append(f'{tag}: ex differs from source')
        if [list(x) for x in it.get('st',[])]!=f['st']: errs.append(f'{tag}: st differs from source')
        ch_=it.get('chunks',[])
        if not ch_: errs.append(f'{tag}: no chunks'); continue
        joined=lib.norm(' '.join(c['en'] for c in ch_))
        vs={lib.norm(v) for v in lib.variants(d['t'],d['ans'])}
        if joined not in vs: errs.append(f'{tag}: chunk text != sentence. got "{" ".join(c["en"] for c in ch_)}"')
        for c in ch_:
            if c.get('k','') not in KINDS: errs.append(f'{tag}: bad kind {c.get("k")}')
            if not c.get('en','').strip(): errs.append(f'{tag}: empty en')
            if not c.get('ko','').strip(): errs.append(f'{tag}: empty ko for "{c.get("en")}"')
            if re.search(r'[A-Za-z]',c.get('ko','')): warn.append(f'{tag}: latin in ko "{c["ko"]}"')
            if c.get('k') in ('S','M','V','C') and not c.get('lab'): errs.append(f'{tag}: no label for "{c["en"]}"')
            if c.get('k','')=='' and len(c['en'].split())<=2 and c is not ch_[-1] and c['en'] not in ch_[0]['en'] : warn.append(f'{tag}: tiny plain chunk "{c["en"]}"')
        vk=it.get('verb',{})
        ok,no_=vk.get('ok'),vk.get('no')
        if not ok or not no_ or ok==no_: errs.append(f'{tag}: verb pair bad {vk}')
        else:
            vch=[c for c in ch_ if c['k']=='V']
            if not vch: errs.append(f'{tag}: no V chunk')
            elif not any(re.search(r'(?<![\w])'+re.escape(ok)+r'(?![\w])',c['en']) for c in vch): errs.append(f'{tag}: verb.ok "{ok}" not found in V chunk')
        tk=[x['k'] for x in (it.get('taps') or s.get('taps',[]))] or ['S']
        if not any(c['k'] in tk for c in ch_): errs.append(f'{tag}: no chunk of tap kind {tk}')
        for c in ch_:
            pos=0
            for hh in c.get('h',[]):
                i=c['en'].find(hh[0],pos)
                if i<0 or hh[1] not in ('s','c','v'): warn.append(f'{tag}: bad h {hh} in "{c["en"]}"')
                else: pos=i+len(hh[0])
        n=it.get('note',{})
        if not n.get('t') or not n.get('lines'): errs.append(f'{tag}: note empty')
        # S/M/C tags from source must be covered
        t=d['t']
        for kind in 'SMC':
            for m in re.finditer(r'<%s>(.*?)</%s>'%(kind,kind),t):
                txt=lib.norm(m.group(1))
                if not any(((c['k']==kind) or (kind=='C' and any(x[1]=='c' for x in c.get('h',[])))) and txt and txt in lib.norm(c['en']) for c in ch_): warn.append(f'{tag}: source <{kind}> "{m.group(1)}" not in a {kind} chunk')
    for s in sets:
        ids={it['no'] for it in s['items']}
        if len(ids)!=len(s['items']): errs.append(f'{s["id"]}: duplicate no')
    return errs,warn
if __name__=='__main__':
    tot=0
    for a in sys.argv[1:]:
        part='q' if a.endswith('q') else 'p'; ch=int(a.rstrip('q')); e,w=check(ch,part=part)
        print(f'== CH{ch:02d}: {len(e)} errors, {len(w)} warnings')
        for x in e: print('  ERR',x)
        for x in w[:40]: print('  warn',x)
        tot+=len(e)
    sys.exit(1 if tot else 0)
