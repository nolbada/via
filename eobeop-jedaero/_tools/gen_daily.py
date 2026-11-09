#!/usr/bin/env python3
"""usage: gen_daily.py [key ...]  base/<key>.json + daily/<key>.json -> <key>.html (데일리어법 방식 해설 페이지)"""
import sys,json,re,html,os,glob
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(D)
e=lambda s:html.escape(s,quote=False)
CSS=open(os.path.join(D,'daily.css'),encoding='utf8').read()
def tk(s): return re.sub(r"([A-Za-z’']+)",lambda m:'<span class="w" data-w="%s">%s</span>'%(m.group(1).lower().replace('’',"'"),m.group(1)),e(s))
FIELDS=['dk','ko','gist','fm','mp','ex','exko','tko','bad','badko','altw','alt','altko','why','trend','d']
def label(it,n):
    m=re.match(r'^(\(?[A-C]\)?|\d+\)|[①-⑤])\s*',it['fr'])
    return (m.group(1) if m else '문항 %d'%n)
def build(key):
    b=json.load(open(os.path.join(D,'base',key+'.json'),encoding='utf8'))
    dj=json.load(open(os.path.join(D,'daily',key+'.json'),encoding='utf8'))
    flat=[i for g in b['groups'] for i in g['items']]
    assert len(flat)==len(dj),(key,len(flat),len(dj))
    m=re.search(r'(CHAPTER \d+ · .*?) 어법변형문제',b['h1']); title=m.group(1)
    out=[]; n=0; dd=[]
    lastbar=None
    for g in b['groups']:
        if g['bar']!=lastbar:
            out.append('<div class="bar">%s</div>'%e(g['bar'])); lastbar=g['bar']
        if g['sub']: out.append('<div class="sub">%s</div>'%e(g['sub']))
        if g['quick']: out.append('<div class="quick">%s</div>'%g['quick'])
        for it in g['items']:
            d=dj[n]; n+=1; dd.append(d)
            for f in FIELDS: assert f in d,(key,n,f)
            qn=label(it,n) if g['sub'] else ('문항 %d'%n if not re.match(r'문항 \d+',it['qn']) else it['qn'])
            r='<div class="item"><div class="num">%s</div>'%e(qn)
            r+='<div class="card"><p class="lbl">문제</p><div class="q">%s<span class="wrong">%s</span>%s</div><div class="mute" style="margin-top:6px">모르는 단어는 눌러서 뜻 확인</div></div>'%(tk(it['pre']),e(it['wr']),tk(it['post']))
            r+='<div class="card" style="margin-top:10px">'
            r+='<div class="sec"><h4>정답</h4><div class="ans"><s>%s</s><i>→</i><b>%s</b></div><span class="badge" style="background:%s;">%s</span></div>'%(e(it['fr']),e(it['to']),it['color'],e(it['badge']))
            r+='<div class="sec"><h4>직독직해</h4><div class="sl">%s</div></div>'%''.join('<div class="r"><b>%s</b><span>%s</span></div>'%(tk(a),e(c)) for a,c in d['dk'])
            r+='<div class="sec"><h4>자연스러운 해석</h4><div class="nat">%s</div></div>'%e(d['ko'])
            r+='<div class="sec"><h4>한 줄 정리</h4><div class="gist">%s</div></div>'%e(d['gist'])
            ph=''.join('<div class="ph"><div class="pl">%s</div><div class="ce">%s</div><div class="ct">%s</div></div>'%(e(h),e(a),e(c)) for h,a,c in d['mp'])
            r+='<div class="post"><div class="lb">오답노트에는 이것만</div><div class="fm">%s</div><div class="mp"><div class="cl"><span>쉬운 예</span><span>이번 문장</span></div>%s<div class="k">쉬운 예 해석 · %s</div><div class="k">이번 문장 해석 · %s</div><div class="bd"><small>틀린 예</small>%s</div><div class="k">%s</div>'%(e(d['fm']).replace(' + ','<i>+</i>'),ph,e(d['exko']),e(d['tko']),e(d['bad']),e(d['badko']))
            if d['alt']: r+='<div class="bd alt"><small>%s 가 맞는 예</small>%s</div><div class="k">%s</div>'%(e(d['altw']),e(d['alt']),e(d['altko']))
            r+='</div></div>'
            r+='<div class="sec"><h4>왜 그럴까요</h4><div class="tx">%s</div></div><div class="sec trend">%s</div>'%(e(d['why']),d['trend'])
            r+='<span class="badge" style="display:none">%s</span><details class="anl"></details>'%e(it['badge'])
            r+='</div></div>'
            out.append(r)
    nav='<div class="navb">'
    nav+=('<a href="%s.html">&laquo; %s</a>'%tuple(b['prev']) if b['prev'] else '<span></span>')
    nav+='<a class="gray" href="index.html">목록</a>'
    nav+=('<a href="%s.html">%s &raquo;</a>'%tuple(b['next']) if b['next'] else '<span></span>')
    nav+='</div>'
    page='''<!doctype html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>해커스 어법 제대로 %s 어법변형문제 정답 및 해설</title>
<style>%s</style>
<style id="ej-hide">html{background:#f6f4ee}body>*{visibility:hidden}</style>
<script src="gate.js" defer></script>
</head>
<body>
<div class="wrap"><div class="hd"><h1>%s</h1><span class="sub">어법변형문제 정답 및 해설</span></div>
%s
%s</div>
<div class="sheet hide" id="sh"></div>
<script>var D=%s;
document.addEventListener("click",function(ev){var w=ev.target.closest&&ev.target.closest(".w");if(!w)return;var it=w.closest(".item"),i=[].indexOf.call(document.querySelectorAll(".item"),it),d=D[i],k=w.dataset.w,v=d[k];
 if(v==null){for(var key in d){if(d[key].indexOf(":")>0&&d[key].split(":")[0].toLowerCase().split(" ").indexOf(k)>-1&&key!=k){v=d[key];break}}}
 var sh=document.getElementById("sh");if(v==null){sh.classList.add("hide");return}
 sh.innerHTML="<b>"+w.textContent+"</b><small>"+v+"</small>";sh.classList.remove("hide");});
document.addEventListener("scroll",function(){document.getElementById("sh").classList.add("hide")},{passive:true});
</script>
</body></html>
'''%(title,CSS,e(title),'\n'.join(out),nav,json.dumps([x['d'] for x in dd],ensure_ascii=False))
    open(os.path.join(R,key+'.html'),'w',encoding='utf8').write(page)
    print('ok',key,n)
if __name__=='__main__':
    for k in (sys.argv[1:] or [os.path.basename(f)[:-5] for f in sorted(glob.glob(os.path.join(D,'daily','*.json')))]): build(k)
