import sys,json
sys.path.insert(0,'/home/claude/via/eobeop-sentence/_src/sx/_w')
from ch06_d import D
o=json.load(open('/home/claude/via/eobeop-sentence/_src/sx/_w/ch06_out_backup.json',encoding='utf-8'))
x={}
for k,(O,pt,rel,st) in D.items():
    ch=o[k]
    for i,v in O.items():
        if isinstance(v,str): ch[i][1]=v
        elif v is not None:
            if v[0] is not None: ch[i][0]=v[0]
            if v[1] is not None: ch[i][1]=v[1]
    e={}
    if pt: e['pt']=pt
    e['rel']=rel
    if st: e['st']=st
    x[k]=e
json.dump(o,open('out/ch06.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(x,open('out2/ch06.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
