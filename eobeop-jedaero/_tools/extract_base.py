import re,glob,json,html,difflib
def txt(s): return html.unescape(re.sub(r'<[^>]+>','',s))
ABBR=['U.S.','p.m.','a.m.','Mr.','Mrs.','Ms.','Dr.','St.','vs.','e.g.','i.e.','No.']
def sents(t):
    for i,a in enumerate(ABBR): t=t.replace(a,'\x01%d\x02'%i)
    out=re.split(r'(?<=[.?!])["”’]?\s+(?=[A-Z“"‘\x03])',t)
    def un(x):
        for i,a in enumerate(ABBR): x=x.replace('\x01%d\x02'%i,a)
        return x
    return [un(x) for x in out]
tot=0;warn=[]
def best(x,cs):
    w=x.replace('\x03','').replace('\x04','')
    r=[(difflib.SequenceMatcher(None,w,c).ratio(),c) for c in cs]
    sc,c=max(r)
    if sc<0.6: warn.append(('LOW',round(sc,2),w[:50]))
    return c
for f in sorted(glob.glob('ch0*-p*.html')):
    s=open(f,encoding='utf8').read(); key=f[:-5]
    h1=txt(re.search(r'<h1>(.*?)</h1>',s).group(1))
    nav=re.search(r'<div class="nav">(.*?)</div>\s*<script',s,re.S) or re.search(r'<div class="nav">(.*?)</div>',s)
    prev=nxt=None
    for h,t in re.findall(r'<a [^>]*href="([^"]+)">([^<]*)</a>',nav.group(1)):
        if h=='index.html': continue
        if '◀' in t: prev=[h[:-5],t.replace('◀','').strip()]
        else: nxt=[h[:-5],t.replace('▶','').strip()]
    body=s[s.index('<div class="pagebar">'):]
    toks=re.findall(r'<div class="pagebar">.*?</div>|<div class="quickbox">.*?</div>|<div class="card">.*?(?=<div class="card">|<div class="pagebar">|<div class="nav">)',body,re.S)
    groups=[];bar='';qq=[];gcur=None
    # pre-collect quickboxes after each pagebar
    for tk in toks:
        if tk.startswith('<div class="pagebar"'):
            bar=txt(tk).replace('📘','').strip(); qq=[]; gcur=None
        elif tk.startswith('<div class="quickbox"'):
            qq.append(re.search(r'<p>(.*?)</p>',tk,re.S).group(1))
        else:
            c=tk
            ans=[]
            AL=list(re.finditer(r'<p class="answerline"><span class="from">(.*?)</span><span class="arrow">→</span><span class="to">(.*?)</span></p>',c,re.S))
            for i,m in enumerate(AL):
                seg=c[m.end(): AL[i+1].start() if i+1<len(AL) else len(c)]
                b=re.search(r'<span class="badge" style="background:(#[0-9a-f]+);">(.*?)</span>',seg,re.S); e_=re.search(r'<p class="explain"><b>해설</b>(.*?)</p>',seg,re.S)
                ans.append((m.group(1),m.group(2),b.group(1),b.group(2),e_.group(1)))
            sent=re.search(r'<p class="sentence">(.*?)</p>',c,re.S).group(1)
            fld=txt(re.search(r'<p class="field"><b>[^<]*</b>(.*?)</p>',c,re.S).group(1)).strip()
            ip=txt(re.search(r'<p class="interp"><b>[^<]*</b>(.*?)</p>',c,re.S).group(1)).strip()
            qn=re.search(r'<span class="qnum">(.*?)</span>',c).group(1)
            assert ans,(f,qn)
            if len(ans)==1 and sent.count('class="wrong"')==1:
                m=re.search(r'<span class="wrong">(.*?)</span>',sent); a,w,b=sent.partition(m.group(0))
                it=dict(pre=html.unescape(a),wr=html.unescape(m.group(1)),post=html.unescape(b),fr=html.unescape(ans[0][0]),to=html.unescape(ans[0][1]),correct=fld,interp=ip,color=ans[0][2],badge=txt(ans[0][3]),explain=ans[0][4].strip(),qn=qn)
                if gcur is None or gcur['bar']!=bar or gcur.get('sub'):
                    gcur=dict(bar=bar,sub='',quick=qq[0] if qq else '',items=[]); groups.append(gcur)
                gcur['items'].append(it)
            else:
                # passage card: one item per answerline
                g=dict(bar=bar,sub=qn,quick=qq.pop(0) if qq else '',items=[]); groups.append(g); gcur=None
                marked=re.sub(r'<span class="wrong">(.*?)</span>',lambda m:'\x03'+m.group(1)+'\x04',sent); marked=html.unescape(marked)
                ws=sents(marked); cs=sents(fld)
                if len(ws)!=len(cs): warn.append((f,qn,len(ws),len(cs)))
                k=0
                for (fr,to,col,bd,ex) in ans:
                    # k-th wrong marker
                    cnt=0;si=None
                    for i,x in enumerate(ws):
                        n=x.count('\x03')
                        if cnt+n>k: si=i;local=k-cnt;break
                        cnt+=n
                    x=ws[si]; parts=re.split(r'(\x03.*?\x04)',x); out=[];j=0;pre='';post='';wr=''
                    for p in parts:
                        if p.startswith('\x03'):
                            if j==local: wr=p[1:-1]; out.append('\x05')
                            else: out.append(p[1:-1])
                            j+=1
                        else: out.append(p)
                    t=''.join(out); pre,_,post=t.partition('\x05')
                    g['items'].append(dict(pre=pre,wr=wr,post=post,fr=html.unescape(fr),to=html.unescape(to),correct=best(x,cs),interp='',color=col,badge=txt(bd),explain=ex.strip(),qn=qn))
                    k+=1
    n=sum(len(g['items']) for g in groups); tot+=n
    assert n==s.count('class="answerline"'),(f,n,s.count('class="answerline"'))
    json.dump(dict(key=key,h1=h1,prev=prev,next=nxt,groups=groups),open('_tools/base/%s.json'%key,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print(tot,warn)
