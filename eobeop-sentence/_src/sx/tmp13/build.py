import json,sys,importlib.util
base='/home/claude/via/eobeop-sentence/_src/sx/'
S={};X={}
for f in ('d1','d2','d3'):
    sp=importlib.util.spec_from_file_location(f,base+'tmp13/%s.py'%f);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    S.update(m.S);X.update(m.X)
inn=json.load(open(base+'in/ch13.json'));out=json.load(open(base+'out/ch13.json'))
import shutil;shutil.copy(base+'out/ch13.json',base+'tmp13/ch13_orig.json')
# fix q2|3 chunk3
S['c13q2|3'][3]=("its rivals in the market.","than 뒤 : its rivals (offer) 생략")
for it in inn:
    k=it['key']
    for i,v in S.get(k,{}).items(): out[k][i]=[v[0],v[1]]
json.dump(out,open(base+'out/ch13.json','w'),ensure_ascii=False,indent=1)
o2={}
for it in inn:
    k=it['key'];x=X.get(k,{});d={}
    if 'pt' in x:d['pt']=x['pt']
    d['rel']=x.get('rel',[])
    if 'st' in x:d['st']=x['st']
    o2[k]=d
json.dump(o2,open(base+'out2/ch13.json','w'),ensure_ascii=False,indent=1)
print(len(o2))
