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
    if not p1:
        mm=re.search(r'문장 연습\(p\.(\d+)~(\d+)\)',txt)
        if mm: p1,p2=int(mm.group(1)),int(mm.group(2))
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

# ================= 짧은 지문 연습 / 내신 서술형 대비 (part 's') =================
import random as _random
def _src_module(ch):
    sp=importlib.util.spec_from_file_location('dr%d'%ch,f'{BASE}/src/data_ch{ch:02d}_rest.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def _pages_s(ch):
    txt=open(f'{BASE}/src/data_ch{ch:02d}_rest.py',encoding='utf-8').read()
    a=re.search(r'^# -+ 지문 연습[^\n]*p\.(\d+)',txt,re.M); b=re.search(r'^# -+ 서술형[^\n]*p\.(\d+)',txt,re.M)
    if not a: a=re.search(r'지문 연습\(p\.(\d+)\)',txt)
    if not b: b=re.search(r'서술형\(p\.(\d+)\)',txt)
    return (int(a.group(1)) if a else 0, int(b.group(1)) if b else 0)
LAB=re.compile(r'[①-⑩ⓐ-ⓩ]')
def _marker_label(t):
    m=re.search(r'<A>\((\w)\)</A>',t)
    if m: return '('+m.group(1)+')'
    m=re.search(r'\(\(([①-⑩ⓐ-ⓩ])\|',t)
    if m: return m.group(1)
    return ''
def render_plain(t):
    """sentence as the textbook shows it (HTML-escaped text, ___ for blanks)."""
    t=re.sub(r'</?[SMCAi]>','',t) if False else t
    t=re.sub(r'<A>(\([A-Z]\))</A>',r'\1',t)
    t=re.sub(r'</?[SMCi]>','',t)
    t=re.sub(r'\(\(([①-⑩ⓐ-ⓩ])\|([^)]*)\)\)',lambda m:m.group(1)+' '+m.group(2),t)
    t=re.sub(r'<<[nw]\|[^>]*>>','___',t)
    t=re.sub(r'\[([^\]|]+)\|([^\]]+)\]',r'\1 / \2',t)
    t=re.sub(r'\{\{(.+?)\}\}',r'\1',t)
    return html.escape(html.unescape(t).replace('’',"'"),quote=False).replace("'",'’')
def plain_variants(t,ans):
    """all acceptable corrected sentences (normalised) for part s. tolerant: corrections drawn from ans tokens."""
    t=re.sub(r'</?[SMCAi]>','',t)
    toks=list(re.finditer(r'\[([^\]|]+)\|([^\]]+)\]|\(\(([①-⑩ⓐ-ⓩ])\|([^)]*)\)\)|<<[nw]\|(.*?)>>|\{\{(.+?)\}\}',t))
    corr=[]
    a=(ans or '').strip()
    if a and a!='O':
        for part in re.split(r'\s*[,/]\s*|\s*→\s*|\s*;\s*',a):
            part=part.strip()
            if not part: continue
            if '|' in part: part=part.split('|',1)[1].strip()
            if part and not re.fullmatch(r'[①-⑩ⓐ-ⓩ]',part): corr.append(part)
    opts=[]
    for m in toks:
        if m.group(1) is not None: opts.append([m.group(1),m.group(2)]+corr)
        elif m.group(4) is not None: opts.append([m.group(4)]+corr)
        elif m.group(5) is not None: opts.append([m.group(5)])
        else: opts.append([m.group(6)]+corr)
    res=set()
    for combo in itertools.product(*opts) if opts else [()]:
        s='';pos=0
        for m,c in zip(toks,combo): s+=t[pos:m.start()]+c;pos=m.end()
        s+=t[pos:]; res.add(norm(s))
    return res
def src_items_s(ch):
    """yield dict(setno,no,d,kind,ctx,kor,arr) for 짧은 지문(201) / 서술형(202) in book order."""
    m=_src_module(ch); out=[]
    for pi,(label,instr,items,ansl) in enumerate(m.PASS,1):
        kind='pass-f' if '틀린' in instr else 'pass-c'
        texts=[(no,d) for no,d in items]
        for j,(no,d) in enumerate(texts):
            lab=_marker_label(d['t']) or str(j+1)
            parts=[]
            for j2,(n2,d2) in enumerate(texts):
                s=render_plain(d2['t'])
                parts.append('<u>'+s+'</u>' if j2==j else s)
            out.append(dict(setno=201,no=f'{pi}-{lab}',d=d,kind=kind,ctx=' '.join(parts),kor=None,arr=False,label=label))
    def block(items,pre):
        for j,(no,d) in enumerate(items):
            parts=[]
            for j2,(n2,d2) in enumerate(items):
                s=render_plain(d2['t']); parts.append('<u>'+s+'</u>' if j2==j else s)
            yield j,no,d,' '.join(parts)
    for n,d in m.FILL:
        hint=html.unescape(d.get('hint','') or '')
        arr=('<<w|' in d['t']) and bool(re.fullmatch(r'\(.*\)',hint.strip())) and not re.search(r'조건|사용|단어',hint)
        kor=(d.get('pre','') or '')+((' '+d['hint']) if d.get('hint') else '')
        out.append(dict(setno=202,no=str(n),d=d,kind='fill-w' if '<<w|' in d['t'] else 'fill-n',ctx=render_plain(d['t']),kor=kor,arr=arr,
                        hintwords=[w.strip() for w in hint.strip()[1:-1].split(',')] if arr else None))
    for tag,items in (('7',m.F7),('8',m.F8)):
        for j,no,d,ctx in block(items,tag):
            out.append(dict(setno=202,no=f'{tag}-{no}',d=d,kind='f'+tag,ctx=ctx,kor=None,arr=False))
    return out
def pool_order(words,seed):
    w=list(words); r=_random.Random(seed)
    for _ in range(20):
        r.shuffle(w)
        if w!=list(words) or len(w)<2: break
    return w
