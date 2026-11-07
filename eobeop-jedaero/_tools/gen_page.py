#!/usr/bin/env python3
"""usage: gen_page.py content.json  -> writes ../<key>.html (analysis/gc are injected separately)
content.json: {"key":"ch01-p12","label":"p.12","prev":["ch01-p21b","p.21 ◀"]|null,"next":["ch01-p13","p.13 ▶"]|null,
 "groups":[{"bar":"p.12 정답 및 해설","items":[{"sentence":"... <w>wrong</w> ...","from":"noise loudly","to":"noise",
   "tag":"(A)"(optional quick-answer prefix),"correct":"바른문장","interp":"해석","ch":"12","badge":"형용사 vs. 부사(2) 보어 자리 (Chapter 12 POINT 2)",
   "explain":"해설 html (<b> only)"}]}]}"""
import sys,json,re,html,os
COL={'01':'#2563eb','02':'#059669','03':'#dc2626','04':'#7c3aed','05':'#c026d3','06':'#ea580c','07':'#0891b2','08':'#ca8a04','09':'#db2777','10':'#4338ca','11':'#16a34a','12':'#9333ea','13':'#0d9488','14':'#b91c1c'}
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(D)
def e(s): return html.escape(s,quote=False)
def main(cf):
    c=json.load(open(cf,encoding='utf-8'))
    t=open(os.path.join(R,'ch02-p24.html'),encoding='utf-8').read()
    head=t[:t.index('<div class="pagebar">')]
    head=head.replace('CHAPTER 02 · p.24','CHAPTER 01 · '+c['label'])
    head=re.sub(r'<style id="anl-css">.*?</style>','',head,flags=re.S); head=re.sub(r'<style id="gc-css">.*?</style>','',head,flags=re.S)
    assert 'p.24' not in head
    out=[head]; n=0
    for g in c['groups']:
        out.append('<div class="pagebar">📘 %s</div>'%e(g['bar']))
        q=[]
        for i,it in enumerate(g['items'],1):
            pre=it.get('tag') or '%d)'%i
            q.append('%s %s → <b>%s</b>'%(e(pre),e(it['from']),e(it['to'])))
        out.append('<div class="quickbox"><p><b>빠른정답</b><br>%s</p></div>'%' / '.join(q))
        for it in g['items']:
            n+=1
            sent=e(it['sentence']).replace('&lt;w&gt;','<span class="wrong">').replace('&lt;/w&gt;','</span>')
            assert '<span class="wrong">' in sent,(c['key'],n)
            out.append('<div class="card">\n<span class="qnum">문항 %d</span>\n<p class="sentence">%s</p>\n<p class="answerline"><span class="from">%s</span><span class="arrow">→</span><span class="to">%s</span></p>\n<p class="field"><b>바른문장</b> %s</p>\n<p class="interp"><b>해석</b> %s</p>\n<span class="badge" style="background:%s;">%s</span>\n<p class="explain"><b>해설</b> %s</p>\n</div>'%(n,sent,e(it['from']),e(it['to']),e(it['correct']),e(it['interp']),COL[it['ch']],e(it['badge']),it['explain']))
    nav='<div class="nav">'
    nav+=('<a href="%s.html">◀ %s</a>'%tuple(c['prev']) if c.get('prev') else '<a class="off">.</a>')
    nav+='<a class="gray" href="index.html">목록</a>'
    nav+=('<a href="%s.html">%s</a>'%tuple(c['next']) if c.get('next') else '<a class="off">.</a>')
    out.append(nav+'</div>\n</body>\n</html>\n')
    open(os.path.join(R,c['key']+'.html'),'w',encoding='utf-8').write('\n'.join(out)); print('ok',c['key'],n)
main(sys.argv[1])
