import json,sys,re,collections
sys.path.insert(0,'/tmp/claude-0/w3')
ROLES={'주어','동사','목적어','간접목적어','직접목적어','보어','목적격보어','수식어','접속사'}
CL=["명사절","형용사절","부사절"];NF=["to부정사 (명사 역할)","to부정사 (형용사 역할)","to부정사 (부사 역할)","동명사","분사"]
def norm(s):return re.sub(r"[“”\"‘’'\s.,?!]","",s)
def node(n,path,err,i,parent_text=None):
    ch=n['ch'];j=''.join((' ' if (k and not c.get('g')) else '')+c['t'] for k,c in enumerate(ch))
    if parent_text is not None and norm(j)!=norm(parent_text):err.append((i,path,'join!=parent: '+j))
    for k,c in enumerate(ch):
        if c['r'] not in ROLES:err.append((i,path,'bad role %d'%k))
        if not c.get('k'):err.append((i,path,'no k %d'%k))
    x=n['x'];g=x.get('glue')
    if g is not None and ch[g]['r']!='접속사':err.append((i,path,'glue not 접속사'))
    cov=set()
    for r in x['rounds']:
        ci=r['ci'];cov|=set(ci)
        roles=[ch[k]['r'] for k in ci]
        if '동사' not in roles:err.append((i,path,'round w/o verb'))
        sk=[a for a in roles if a not in('수식어','접속사')]
        if any(v>1 for v in collections.Counter(sk).values()):err.append((i,path,'dup role %s'%sk))
        has=roles.__contains__;fm=r['fm']
        exp={1:not(has('보어') or has('목적어') or has('간접목적어')),2:has('보어') and not has('목적어'),3:has('목적어') and not has('간접목적어') and not has('목적격보어'),4:has('간접목적어') and has('직접목적어'),5:has('목적어') and has('목적격보어')}
        if not exp.get(fm):err.append((i,path,'fm %s vs %s'%(fm,roles)))
    allc=set(range(len(ch)))-({g} if g is not None else set())
    if cov!=allc:err.append((i,path,'cover mismatch %s'%sorted(allc-cov)))
    for d in n.get('deep',[]):
        deep(d,n,path,err,i)
def deep(d,parent,path,err,i,depth=0):
    ci=d['ci']
    if ci>=len(parent['ch']):err.append((i,path,'bad ci'));return
    if 'opts' in d and d['opts'] not in(CL,NF):err.append((i,path,'bad opts'))
    if 'opts' in d and not(0<=d['ans']<len(d['opts'])):err.append((i,path,'bad ans'))
    if 'opts' in d and not d.get('why'):err.append((i,path,'no why'))
    node(d['A'],path+'/%d'%ci,err,i,parent['ch'][ci]['t'])
def check(p,basic):
    B={}
    for f in basic:
        for d in json.load(open(f)):B[d['id']]=d
    D=json.load(open(p));err=[]
    for u in D:
        b=B.get(u['id'])
        if not b:err.append((u['id'],'','unknown id'));continue
        for d in u['deep']:deep(d,b,'',err,u['id'])
    return D,err
if __name__=='__main__':
    import glob
    D,e=check(sys.argv[1],sorted(glob.glob('/tmp/claude-0/w3/data/basic_?.json')));print(sys.argv[1],len(D),'units with deep',len(e),'errors')
    for x in e:print('  ',x)
