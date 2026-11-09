#!/usr/bin/env python3
"""usage: check_daily.py key...   daily/<key>.json 형식·정합성 검사. 문제 있으면 목록 출력(종료코드 1)."""
import sys,json,re,os
D=os.path.dirname(os.path.abspath(__file__))
EMO=re.compile('[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-↪]')
def norm(s): return re.sub(r"[\s ]+",' ',s.replace('’',"'")).strip()
bad=0
for key in sys.argv[1:]:
    b=json.load(open(os.path.join(D,'base',key+'.json'),encoding='utf8')); d=json.load(open(os.path.join(D,'daily',key+'.json'),encoding='utf8'))
    flat=[i for g in b['groups'] for i in g['items']]
    errs=[]
    if len(flat)!=len(d): errs.append('count base=%d daily=%d'%(len(flat),len(d)))
    for n,(it,x) in enumerate(zip(flat,d),1):
        def E(m): errs.append('#%d %s'%(n,m))
        for f in ['dk','ko','gist','fm','mp','ex','exko','tko','bad','badko','altw','alt','altko','why','trend','d']:
            if f not in x: E('missing '+f)
        if any(f not in x for f in ['dk','ko','gist','fm','mp','ex','exko','tko','bad','badko','altw','alt','altko','why','trend','d']): continue
        en=' '.join(c[0] for c in x['dk'])
        if norm(en)!=norm(it['correct']): E('dk English != correct: %r vs %r'%(en[:70],it['correct'][:70]))
        if not 2<=len(x['dk'])<=6 and len(norm(it['correct']).split())>8: E('dk chunks %d'%len(x['dk']))
        if any(len(c)!=2 or not c[0].strip() or not c[1].strip() for c in x['dk']): E('dk empty piece')
        if not 1<=len(x['mp'])<=3 or any(len(r)!=3 or not all(r) for r in x['mp']): E('mp shape')
        if not re.search('[가-힣]',x['exko']): E('exko no korean')
        if not re.search('[가-힣]',x['badko']): E('badko no korean')
        if x['alt'] and not re.search('[가-힣]',x['altko']): E('altko no korean')
        if x['alt'] and not x['altw']: E('altw empty')
        if not x['gist'].endswith('예요.') and not x['gist'].endswith('에요.'): E('gist ending: '+x['gist'][-10:])
        if len(x['d'])<3: E('dict too small')
        if not re.search(r'출제|순위',x['trend']): E('trend format')
        if '<b>' not in x['trend']: E('trend no <b>')
        for k,v in x.items():
            if isinstance(v,(str,list,dict)) and EMO.search(json.dumps(v,ensure_ascii=False)): E('emoji in '+k)
        if not re.search('[가-힣]',x['ko']): E('ko no korean')
        if norm(x['ko'])!=norm(it['interp']) and it['interp']: E('ko != base interp (정상 항목은 base interp 그대로)')
    print(key,'OK' if not errs else 'PROBLEMS')
    for m in errs: print('  ',m)
    bad+=bool(errs)
sys.exit(1 if bad else 0)
