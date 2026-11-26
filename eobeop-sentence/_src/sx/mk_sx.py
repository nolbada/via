# -*- coding: utf-8 -*-
# 검사: python3 mk_sx.py NN  (out/chNN.json vs in/chNN.json)
import json,re,sys,os
def strip(m):
    m=re.sub(r'\{o\|[^}]*\}','',m); m=re.sub(r'  +',' ',m).replace(' .','.').replace(' ,',',')
    return re.sub(r'\{[avcpk]\|([^}]*)\}',r'\1',m).replace('【','').replace('】','').strip()
def check(ch):
    inn=json.load(open('in/ch%02d.json'%ch,encoding='utf-8'))
    f='out/ch%02d.json'%ch
    if not os.path.exists(f): return ['out 파일 없음'],0
    out=json.load(open(f,encoding='utf-8')); errs=[]; warn=0
    keys={x['key'] for x in inn}
    for k in out:
        if k not in keys: errs.append('모르는 키 %s'%k)
    for it in inn:
        k=it['key']; sx=out.get(k)
        if sx is None: errs.append('%s 누락'%k); continue
        if len(sx)!=len(it['chunks']): errs.append('%s 덩어리 수 %d != %d'%(k,len(sx),len(it['chunks']))); continue
        depth=0; nv=0
        for i,((m,n),c) in enumerate(zip(sx,it['chunks'])):
            if strip(m)!=c[0]: errs.append('%s #%d 영어 불일치: %r vs %r'%(k,i,strip(m),c[0]))
            if re.search(r'\{[^avcpok]|\{[avcpok][^|]|\{[avcpok]\|[^}]*$',m): errs.append('%s #%d 태그 깨짐 %r'%(k,i,m))
            depth+=m.count('【')-m.count('】')
            if depth<0: errs.append('%s #%d 】가 먼저 나옴'%(k,i))
            nv+=len(re.findall(r'\{[av]\|',m))
            if n and ('→' in n or '➔' in n or '->' in n): errs.append('%s #%d 메모에 화살표 금지'%(k,i))
            if n and len(n)>(62 if n.startswith('!') else 42): errs.append('%s #%d 메모 너무 김(%d자)'%(k,i,len(n)))
            if n and re.search(r'[\U0001F300-\U0001FAFF]',n): errs.append('%s 이모지'%k)
        if depth!=0: errs.append('%s 【 】 짝 안 맞음'%k)
        if nv==0: errs.append('%s 동사 표시({v|}/{a|}) 없음'%k)
        if not any('{a|' in m for m,_ in sx) and it['ans'] not in ('○',''): errs.append('%s 정답 표시({a|}) 없음'%k)
    f2='out2/ch%02d.json'%ch
    if os.path.exists(f2):
        o2=json.load(open(f2,encoding='utf-8'))
        for it in inn:
            k=it['key']; x=o2.get(k)
            if x is None: errs.append('%s out2 누락'%k); continue
            n=len(it['chunks'])
            pt=x.get('pt')
            if pt is None:
                if it['ans']!='○': errs.append('%s pt(어법분석) 없음'%k)
            elif not(isinstance(pt,list) and len(pt)==2 and pt[0] and pt[1]): errs.append('%s pt 형식 [오답,규칙]'%k)
            elif len(pt[1])>46: errs.append('%s pt 규칙 너무 김'%k)
            for r in x.get('rel',[]):
                if not(isinstance(r,list) and len(r)>=3 and isinstance(r[0],int) and isinstance(r[1],int) and 0<=r[0]<n and 0<=r[1]<n and r[0]!=r[1] and r[2] in('mod','par','eq')): errs.append('%s rel 형식 오류 %r'%(k,r))
                elif len(r)>3 and len(r[3])>14: errs.append('%s rel 라벨 너무 김'%k)
            st=x.get('st')
            if st is not None:
                if not(isinstance(st,list) and len(st)==2 and isinstance(st[1],list) and 2<=len(st[1])<=4 and len(st[0])<=30): errs.append('%s st 형식 [제목,[2~4줄]]'%k)
                elif any(len(l)>56 or '→' in l for l in st[1]): errs.append('%s st 줄 너무 김/화살표'%k)
        for k in o2:
            if k not in keys: errs.append('out2 모르는 키 %s'%k)
    return errs,len(inn)
if __name__=='__main__':
    tot=0
    for a in sys.argv[1:]:
        e,n=check(int(a)); tot+=len(e)
        print('CH%s: %d문항 errors=%d'%(a,n,len(e)))
        for x in e[:40]: print('  ',x)
    print('총 errors',tot)
