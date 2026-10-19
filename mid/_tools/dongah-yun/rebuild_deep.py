import json,glob,sys
sys.path.insert(0,'/tmp/claude-0/w3')
from build_basic import build
D=[];DM={}
for p in sorted(glob.glob('/tmp/claude-0/w3/data/basic_?.json')):D+=json.load(open(p))
for p in sorted(glob.glob('/tmp/claude-0/w3/data/deep_?.json')):
    for u in json.load(open(p)):DM[u['id']]=u['deep']
for L in (7,8):
    d=[x for x in D if x['id'].startswith('%d-'%L)]
    print(L,build(L,d,'/tmp/claude-0/w3/out/mid/dongah-yun/l%d/adv/index.html'%L,'%d과 핵심 문장 분석 (심화)'%L,'vsig-mid-dy-l%d-adv-v1'%L,deepmap=DM),sum(1 for x in d if DM.get(x['id'])))
