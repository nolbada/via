#!/usr/bin/env python3
"""usage: inject.py page.html analysis.json
analysis.json = list aligned with <p class="answerline"> order; each item:
{"en":"sentence with [[뼈대]] markers","key":"한글 뼈대문장","form":"3형식","ref":[["I","s"],["like","v"],["apples","o"]],"refrel":"I ≠ apples",
 "me":[["A number of movies today","s"],["feature","v"],...],"merel":"movies ≠ effects",
 "easy":[["먼저 뼈대부터:","Movies feature effects","영화들이 ..."],...,["한 줄 요약"]],
 "notes":["html","html",...]}"""
import sys,json,re,html
RN={"s":"주어","v":"동사","o":"목적어","c":"보어","io":"간접목적어","do":"직접목적어","oc":"목적격보어","x":"덧붙는 말"}
CSS="""<style id="anl-css">
.anl{margin:14px 0 4px;border:1px solid #cbd5e1;border-radius:10px;background:#f8fafc;}
.anl>summary{cursor:pointer;font-weight:bold;font-size:15.5px;padding:10px 14px;color:#1e3a5f;}
.anl .in{padding:4px 14px 14px;font-size:16px;}
.anl .en{font-size:17.5px;line-height:1.8;margin:6px 0;}
.anl mark{background:linear-gradient(transparent 38%,rgba(255,214,0,.6) 38%,rgba(255,214,0,.6) 92%,transparent 92%);color:inherit;padding:0 2px;}
.anl .lab{display:block;font-size:12.5px;color:#64748b;font-weight:bold;margin:12px 0 4px;letter-spacing:.04em;}
.anl .form{display:inline-block;font-size:13px;font-weight:bold;color:#1d4ed8;background:#e0e9fb;border-radius:999px;padding:1px 10px;}
.anl .mrow{display:flex;flex-wrap:wrap;align-items:center;gap:4px 5px;margin:4px 0;}
.anl .mlab{font-size:12.5px;color:#64748b;width:48px;flex:none;}
.anl .rc{display:inline-flex;flex-direction:column;align-items:center;line-height:1.15;border-radius:7px;padding:3px 8px 2px;font-size:14px;}
.anl .rc i{font-style:normal;font-size:10px;opacity:.85;}
.anl .rc.s{background:#dbeafe;color:#1e40af}.anl .rc.v{background:#dfe5ee;color:#1e293b}.anl .rc.o{background:#dcfce7;color:#166534}.anl .rc.c{background:#ffedd5;color:#9a3412}.anl .rc.io{background:#cffafe;color:#155e75}.anl .rc.do{background:#ecfccb;color:#3f6212}.anl .rc.oc{background:#fef3c7;color:#92400e}.anl .rc.x{background:#e5e7eb;color:#374151}
.anl .rel{font-size:12.5px;color:#64748b;}
.anl .easy{border:1px solid #e2e8f0;border-radius:8px;background:#fff;padding:8px 12px;}
.anl .easy p{margin:0 0 8px;font-size:15.5px;}.anl .easy .q{font-size:13px;color:#64748b;}.anl .easy .e{font-weight:bold;display:block;}
.anl .easy p.sum{border-top:1px dashed #cbd5e1;padding-top:8px;margin:0;font-weight:bold;}
.anl .note{background:#fff4e8;border:2px dashed #c2410c;border-radius:10px;padding:10px 14px;margin-top:14px;}
.anl .note .tag{display:inline-block;background:#c2410c;color:#fff;font-weight:bold;font-size:13px;padding:2px 10px;border-radius:999px;}
.anl .note .hint{font-size:13px;color:#7c4a1d;margin:4px 0 2px;}
.anl .note ol{margin:4px 0 8px;padding-left:22px;font-size:15.5px;}
.anl .note label{display:flex;align-items:center;gap:8px;font-size:14px;color:#7c4a1d;cursor:pointer;}
.anl .note input{width:20px;height:20px;}
</style>"""
JS="""<script id="anl-js">
(function(){var p=location.pathname.split('/').pop();document.querySelectorAll('.anl input[data-nt]').forEach(function(c){var k='nt:'+p+':'+c.dataset.nt;try{c.checked=localStorage.getItem(k)==='1';}catch(e){}c.onchange=function(){try{localStorage.setItem(k,c.checked?'1':'0');}catch(e){}};});})();
</script>"""
def esc(s): return html.escape(s,quote=False)
def chips(a): return ''.join('<span class="rc %s">%s<i>%s</i></span>'%(r,esc(t),RN[r]) for t,r in a)
def en(s): return re.sub(r'\[\[(.+?)\]\]',lambda m:'<mark>%s</mark>'%esc(m.group(1)),esc(s).replace('[[','[[')) if '[[' in s else esc(s)
def block(a,i):
    en_s=re.sub(r'\[\[(.+?)\]\]',lambda m:'\x00'+m.group(1)+'\x01',a['en'])
    en_s=esc(en_s).replace('\x00','<mark>').replace('\x01','</mark>')
    h='<details class="anl"><summary>🔍 문장 분석 · 노트정리</summary><div class="in">'
    h+='<div class="en">%s</div>'%en_s
    h+='<span class="lab">뼈대 (노란 줄)</span><div>%s</div>'%esc(a['key'])
    h+='<span class="lab">문형</span><span class="form">%s</span>'%esc(a['form'])
    if a.get('ref'): h+='<div class="mrow"><span class="mlab">닮은꼴</span>%s<span class="rel">%s</span></div>'%(chips(a['ref']),esc(a.get('refrel','')))
    h+='<div class="mrow"><span class="mlab">이 문장</span>%s<span class="rel">%s</span></div>'%(chips(a['me']),esc(a.get('merel','')))
    h+='<span class="lab">풀어보기</span><div class="easy">'
    for t in a['easy']:
        h+=('<p><span class="q">%s</span><span class="e">%s</span>%s</p>'%(esc(t[0]),esc(t[1]),esc(t[2])) if len(t)>1 else '<p class="sum">%s</p>'%esc(t[0]))
    h+='</div><div class="note"><span class="tag">✍ 노트정리</span><div class="hint">알고 있어도 노트에 한 번만 직접 쓰세요.</div><ol>'+''.join('<li>%s</li>'%n for n in a['notes'])+'</ol>'
    h+='<label><input type="checkbox" data-nt="%d"> 노트에 썼어요</label></div></div></details>'%i
    return h
def run(page,jf):
    s=open(page,encoding='utf-8').read()
    data=json.load(open(jf,encoding='utf-8'))
    s=re.sub(r'<details class="anl">.*?</details>','',s,flags=re.S)
    s=re.sub(r'<style id="anl-css">.*?</style>','',s,flags=re.S); s=re.sub(r'<script id="anl-js">.*?</script>','',s,flags=re.S)
    na=s.count('class="answerline"'); assert na==len(data),(page,na,len(data))
    parts=re.split(r'(<p class="explain">.*?</p>)',s,flags=re.S)
    # explain paragraphs align with answerlines in order
    ne=(len(parts)-1)//2; assert ne==na,(page,'explain',ne,na)
    out=[];k=0
    for j,p in enumerate(parts):
        out.append(p)
        if j%2==1: out.append(block(data[k],k)); k+=1
    s=''.join(out)
    s=s.replace('</head>',CSS+'\n</head>',1).replace('</body>',JS+'\n</body>',1)
    open(page,'w',encoding='utf-8').write(s)
    print('ok',page,na)
if __name__=='__main__': run(sys.argv[1],sys.argv[2])
