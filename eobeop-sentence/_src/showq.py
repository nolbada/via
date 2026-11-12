import sys,re,lib
ch=int(sys.argv[1]); P=lib.load_rest(ch)
for k in sorted(P):
    print(f"\n##### SET {k}  {P[k]['page']}  {P[k]['title']}")
    for kk,no,d in [x for x in lib.src_items(ch,'q') if x[0]==k]:
        print(f"\n[{k},'{no}'] t: {d['t']}\n   ans: {d['ans']}\n   ko : {d['ko']}\n   st : {d['st']}")
