# -*- coding: utf-8 -*-
import sys,re,lib
ch=int(sys.argv[1]); P=lib.load_points(ch)
for k in sorted(P):
    v=P[k]; print(f"\n##### POINT {k}  {v['page']}  {v['title']}\n  rule: {re.sub('<[^>]+>','',v['rule'])}")
    for kk,no,d in [x for x in lib.src_items(ch) if x[0]==k]:
        print(f"\n[{k},'{no}'] t: {d['t']}\n   ans: {d['ans']}\n   ko : {d['ko']}\n   st : {d['st']}")
