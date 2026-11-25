# -*- coding: utf-8 -*-
# d/chNN.js(+add data) -> in/chNN.json : 구조분석(sx) 작성 대상 목록. 서술형(s2) 세트 제외.
import json,glob,re,sys
SD='/home/claude/via/eobeop-sentence/d'; AD='/home/claude/add/data'
def load(f):
    s=open(f,encoding='utf-8').read(); return json.loads(s[s.index('=')+1:].rstrip().rstrip(';'))
for ch in range(1,15):
    out=[]
    for st in load('%s/ch%02d.js'%(SD,ch)):
        if st['id'].endswith('s2'): continue
        for it in st['items']:
            out.append(dict(key='%s|%s'%(st['id'],it['no']),title=st['title']+(' · '+st['sub'] if st.get('sub') else ''),
              chunks=[[c['en'],c['ko'],c['k']] for c in it['chunks']],tr=it['tr'],ans=it['verb']['ok'],pts=it.get('pts')))
    d=json.load(open('%s/add%02d.json'%(AD,ch),encoding='utf-8'))
    for s in d['secs']:
        for it in s['items']:
            out.append(dict(key='add%02d|%d-%s'%(ch,s['n'],it['no']),title='추가문제 POINT %d '%s['n']+s['title'],
              chunks=[[c['en'],c['ko'],c['k']] for c in it['chunks']],tr=it['tr'],ans=it['ans'],pts=None))
    json.dump(out,open('in/ch%02d.json'%ch,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
    print(ch,len(out))
