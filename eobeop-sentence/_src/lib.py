# -*- coding: utf-8 -*-
import re, json, html, itertools, importlib.util, os
BASE=os.path.dirname(os.path.abspath(__file__))
def load_points(ch):
    sp=importlib.util.spec_from_file_location('dp%d'%ch,f'{BASE}/src/data_ch{ch:02d}_points.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m.P
def src_items(ch):
    """yield (setno, no, item) in book order. no='예제' or '1','2'.."""
    P=load_points(ch); out=[]
    for k in sorted(P):
        v=P[k]; out.append((k,'예제',v['ex'][1]))
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
                for a in re.split(r'\s*/\s*|\s*,\s*|\s*\(또는\s*|\)',ans):
                    if a.strip(): o.append(a.strip())
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
