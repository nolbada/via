# -*- coding: utf-8 -*-
import re, json, html, itertools, importlib.util, os
BASE=os.path.dirname(os.path.abspath(__file__))
def load_points(ch):
    sp=importlib.util.spec_from_file_location('dp%d'%ch,f'{BASE}/src/data_ch{ch:02d}_points.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m.P
def load_rest(ch):
    sp=importlib.util.spec_from_file_location('dr%d'%ch,f'{BASE}/src/data_ch{ch:02d}_rest.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    txt=open(f'{BASE}/src/data_ch{ch:02d}_rest.py',encoding='utf-8').read()
    mm=re.search(r'문장 연습[^\n]*네모[^\n]*p\.(\d+)',txt); p1=int(mm.group(1)) if mm else 0
    mm=re.search(r'문장 연습[^\n]*밑줄[^\n]*p\.(\d+)',txt); p2=int(mm.group(1)) if mm else p1+1
    return {101:dict(page='p.%d'%p1,title='문장 연습 네모',groups=[('a','',m.BOX)]),102:dict(page='p.%d'%p2,title='문장 연습 밑줄',groups=[('a','',m.UL)])}
def src_items(ch,part='p'):
    """yield (setno, no, item) in book order. no='예제' or '1','2'.."""
    P=load_points(ch) if part=='p' else load_rest(ch); out=[]
    for k in sorted(P):
        v=P[k]
        if 'ex' in v: out.append((k,'예제',v['ex'][1]))
        for g in v['groups']:
            for no,d in g[2]: out.append((k,str(no),d))
    return out
TAG=re.compile(r'</?[SMCAi]>')
def strip_tags(t): return TAG.sub('',t)
def variants(t,ans):
    """possible corrected sentences (plain text)."""
    t=strip_tags(t)
    toks=list(re.finditer(r'\[([^\]|]+)\|([^\]]+)\]|\{\{(.+?)\}\}',t))
    opts=[]
    for m in toks:
        if m.group(1) is not None: opts.append([m.group(1),m.group(2)])
        else:
            x=m.group(3); o=[x]
            if ans and ans!='O':
                pat=r'\s*/\s*|\s*,\s*|\s*\(또는\s*|\)' if '(또는' in ans else r'\s*/\s*|\s*,\s*'
                for a in re.split(pat,ans):
                    a=a.strip()
                    if not a: continue
                    mm=re.fullmatch(r'(\w+)\((\w+)\)',a)
                    if mm: o+= [mm.group(1),mm.group(1)+mm.group(2)]
                    else: o.append(a)
            opts.append(o)
    res=set()
    for combo in itertools.product(*opts) if opts else [()]:
        s='';pos=0
        for m,c in zip(toks,combo):
            s+=t[pos:m.start()]+c;pos=m.end()
        s+=t[pos:]; res.add(s)
    return res
def norm(s):
    s=html.unescape(s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'[\s]+','',s).lower()
def src_fields(item):
    return dict(tr=item['ko'],why=item['why'],ex=item.get('ex',''),st=[list(x) for x in item['st']])
