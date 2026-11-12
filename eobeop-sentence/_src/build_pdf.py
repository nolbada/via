# -*- coding: utf-8 -*-
"""usage: python3 build_pdf.py NN [YYMMDD]  -> out/<date>_어법제대로_CHNN_문장분석_v1.pdf (+ .html)"""
import sys, json, html, re, os
import lib
E=html.escape
CH=json.load(open(f'{lib.BASE}/chapters.json',encoding='utf-8'))
DEF_LEG=[('s','주어 · 핵심'),('m','건너뛸 수식어'),('v','정답 자리'),('c','단서 · 연결')]
def mark(en,h):
    en=E(en)
    if not h: return en
    out='';pos=0
    for sub,cls in h:
        s=E(sub);i=en.find(s,pos)
        if i<0: continue
        out+=en[pos:i]+f'<span class="m{cls}">{s}</span>';pos=i+len(s)
    return out+en[pos:]
def chunk(c):
    k=c['k'];h=c.get('h')
    cls=k if not h else k+' hh'
    en=mark(c['en'],h)
    if k=='M': en='【 '+en+' 】'
    lab=E(c['lab']) if c['lab'] else '&nbsp;'
    return f'<div class="ch {cls}"><div class="lab">{lab}</div><div class="en">{en}</div><div class="ko">{E(c["ko"])}</div></div>'
def sent(it):
    chs='<span class="sl">/</span>'.join(chunk(c) for c in it['chunks'])
    no=it['no']; ex=no=='예제'
    chips=''.join(f'<span class="chip {c}"><em>{E(l)}</em>{E(t)}</span>' for c,l,t in it['st'])
    exb=f'<div class="exb"><b>함께 알아둘 것</b> {it["ex"]}</div>' if it['ex'] else ''
    nt=it['note']; ls=''.join(f'<div class="nl">{E(x)}</div>' for x in nt['lines'])
    return f'''<div class="sb"><div class="hd"><span class="no {'ex' if ex else ''}">{'예제' if ex else no}</span></div>
<div class="line">{chs}</div><div class="chips">{chips}</div>
<div class="tr"><b>해석</b> {E(it['tr'])}</div><div class="wy">{it['why']}</div>{exb}
<div class="note"><div class="nh"><span class="nt">꼭 정리해야 할 사항</span><span class="nti">{E(nt['t'])}</span><span class="nwh">교재 문장 옆에 쓰기</span></div>{ls}</div></div>'''
def pnote(s):
    q=s['pnote']; ls=''.join(f'<div class="nl">{E(x)}</div>' for x in q['lines'])
    isq=bool(re.search(r'q\d$',s['id']))
    return f'<div class="note pn"><div class="nh"><span class="nt">{"정리 노트" if isq else "POINT 노트"}</span><span class="nti">{E(q["t"])}</span><span class="nwh">{"교재 이 쪽 위에 쓰기" if isq else "교재 POINT 옆에 쓰기"}</span></div>{ls}</div>'
def page(ch,s,items,first):
    leg=s.get('legend') or DEF_LEG
    lg=''.join(f'<span class="cc {c}">{E(l)}</span>' for c,l in leg)
    return f'''<section class="pg"><div class="top"><div class="brand">비타민 영어클리닉</div><div class="ttl">해커스 어법 제대로 · CH.{ch:02d} {E(CH[str(ch)])} · 문장 분석</div><div class="pn2">p.{s['page']}</div></div>
<div class="pt">{E(s['title'])}  {E(s['sub'])}</div>
<div class="legend">{lg}</div>
{pnote(s) if first else ''}{''.join(sent(i) for i in items)}</section>'''
CSS=open(f'{lib.BASE}/pdf.css',encoding='utf-8').read()
def build(ch,date):
    sets=json.load(open(f'{lib.BASE}/data/ch{ch:02d}.json',encoding='utf-8'))
    pq=f'{lib.BASE}/data/ch{ch:02d}q.json'
    if os.path.exists(pq): sets+=json.load(open(pq,encoding='utf-8'))
    pages=[]
    for s in sets:
        its=s['items']; per=3
        cuts=[(a,min(a+per,len(its))) for a in range(0,len(its),per)]
        for j,(a,b) in enumerate(cuts): pages.append(page(ch,s,its[a:b],j==0))
    doc=f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    base=f'{lib.BASE}/out/{date}_어법제대로_CH{ch:02d}_문장분석_v1'
    open(base+'.html','w',encoding='utf-8').write(doc)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(); pg.goto('file://'+base+'.html'); pg.wait_for_timeout(300)
        pg.pdf(path=base+'.pdf',format='A4',print_background=True,margin={'top':'8mm','bottom':'8mm','left':'11mm','right':'11mm'}); b.close()
    return base+'.pdf',len(pages)
if __name__=='__main__':
    date=sys.argv[2] if len(sys.argv)>2 else '261113'
    p,n=build(int(sys.argv[1]),date); print(p,n,'pages')
