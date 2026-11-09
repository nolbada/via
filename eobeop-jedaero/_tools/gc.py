#!/usr/bin/env python3
"""모든 해설 페이지의 각 항목 해설 아래에 그래머콕 개념 링크 버튼(+돌아올 자리 앵커)을 넣는다. 여러 번 돌려도 안전."""
import re,glob,os,json,html,urllib.parse
GC='https://nolbada.github.io/via-mid/m/grammarcock/'
BASE='https://nolbada.github.io/via/eobeop-jedaero/'
MAP={
'1.1':['099','099-H1'],'1.2':['099'],'1.3':['099'],'1.4':['099','099-H1'],'1.5':['080','099'],'1.6':['097-H1','099-H1'],
'2.1':['055-H1','054'],'2.2':['057','054'],'2.3':['098-H1','041'],
'3.1':['073','074'],'3.2':['075-H1'],'3.3':['080','074'],
'4.1':['011','059'],'4.2':['013-H1'],'4.3':['001-H2'],'4.4':['096'],
'5.1':['088','087'],'5.2':['042','087'],'5.3':['090-2'],
'6.1':['001-H1','026'],'6.2':['066'],'6.3':['066','067'],'6.4':['026-H2'],'6.5':['026-H1'],'6.6':['026-H1','061'],
'7.1':['001-H1','068'],'7.2':['030-H1','031'],'7.3':['068'],'7.4':['068','070'],'7.5':['072','072-H1'],
'8.1':['037-H1','037'],'8.2':['037-H1','037'],'8.3':['037-H1','037'],
'9.1':['093-H1','040'],'9.2':['093','093-H1'],'9.3':['039','085'],
'10.1':['078','080'],'10.2':['078'],'10.3':['086','086-H1'],'10.4':['085','085-H1'],'10.5':['084'],
'11.1':['004','047'],'11.2':['046','046-H1'],'11.3':['048-H1','047'],'11.4':['047'],'11.5':['049','050'],
'12.1':['051-H2','051-H1'],'12.2':['028'],'12.3':['051-H1'],'12.4':['051-H1','062–063'],'12.5':['062–063','051-H2'],
'13.1':['033','034'],'13.2':['034'],'13.3':['034-H1','035'],
'14.1':['097','097-H1'],'14.2':['097'],'14.3':['094','095'],
}
# 그래머콕 개념 이름
s=open(os.path.expanduser('/home/claude/via-mid/m/grammarcock/index.html'),encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = ')
D,_=json.JSONDecoder().raw_decode(s[i:])
NAME={x['num']:x['name'] for x in D}
for v in MAP.values():
    for n in v: assert n in NAME,n
def norm(t): return re.sub(r'[\s:·()/\-\d]','',re.sub(r'\(Chapter.*?\)','',t))
BADGE=re.compile(r'<span class="badge"[^>]*>(.*?)</span>',re.S)
def refs_in(t): return ['%d.%d'%(int(a),int(b)) for a,b in re.findall(r'Chapter\s*(\d+)\s*POINT\s*(\d+)',t)]
def build_nameidx():
    idx={}
    for f in glob.glob('ch0*-p*.html'):
        for m in BADGE.finditer(open(f,encoding='utf-8').read()):
            t=re.sub(r'\s+',' ',re.sub('<.*?>','',m.group(1)))
            for part in re.split(r'\s*[/①②③]\s*(?=\d?\)?)',t):
                r=refs_in(part)
                if len(r)==1:
                    nm=norm(re.sub(r'^\d\)\s*','',part))
                    if nm: idx[nm]=r[0]
    return idx
NIDX=None
FALL=[('전치사뒤동명사','6.4'),('수식어가사이에있는','1.1'),('명사와대명사','11.1')]
CSS='''<style id="gc-css">
.gc{margin:12px 0 4px;scroll-margin-top:12px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.gc .gl{font-size:12.5px;color:#64748b;font-weight:bold}
.gc a{display:inline-block;background:#244138;color:#fff !important;text-decoration:none;font-weight:bold;font-size:14px;padding:7px 12px;border-radius:999px}
</style>'''
def run(page):
    global NIDX
    if NIDX is None: NIDX=build_nameidx()
    s=open(page,encoding='utf-8').read()
    s=re.sub(r'<div class="gc" id="gc\d+">.*?</div>','',s,flags=re.S)
    s=re.sub(r'<style id="gc-css">.*?</style>','',s,flags=re.S)
    key=os.path.basename(page)[:-5]
    out=[];pos=0;k=0;added=0
    for m in re.finditer(r'<details class="anl">',s):
        pre=s[pos:m.start()]; out.append(pre)
        # 이 항목의 해설 영역에서 가장 가까운 앞 배지
        bs=list(BADGE.finditer(s[:m.start()]))
        refs=[]
        if bs:
            t=re.sub(r'\s+',' ',re.sub('<.*?>','',bs[-1].group(1)))
            refs=refs_in(t)
            if not refs:
                nm=norm(t.split('·')[-1])
                for kk,v in FALL:
                    if kk in re.sub(r'[\s:·()/\-\d]','',t): refs=[v];break
                for kk,v in ([] if refs else NIDX.items()):
                    if nm and (nm==kk or nm in kk or kk in nm): refs=[v];break
        nums=[]
        for r in refs:
            for n in MAP.get(r,[]):
                if n not in nums: nums.append(n)
        nums=nums[:3]
        if nums:
            back=urllib.parse.quote(BASE+key+'.html#gc%d'%k,safe='')
            links=''.join('<a href="%s?c=%s&amp;back=%s">%s</a>'%(GC,urllib.parse.quote(n),back,html.escape(NAME[n])) for n in nums)
            out.append('<div class="gc" id="gc%d"><span class="gl">그래머콕 개념</span>%s</div>'%(k,links)); added+=1
        pos=m.start(); k+=1
    out.append(s[pos:]); s=''.join(out)
    if '.navb{' not in s: s=s.replace('</head>',CSS+'\n</head>',1)
    open(page,'w',encoding='utf-8').write(s)
    return k,added
if __name__=='__main__':
    tot=0;ad=0;miss=[]
    for f in sorted(glob.glob('ch0*-p*.html')):
        k,a=run(f); tot+=k; ad+=a
        if a<k: miss.append((f,k-a))
    print('items',tot,'linked',ad,'unlinked',miss)
