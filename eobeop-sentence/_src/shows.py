import sys,re,lib
ch=int(sys.argv[1])
for x in lib.src_items_s(ch):
    d=x['d']
    print(f"\n[{x['setno']},'{x['no']}'] kind={x['kind']} arr={x['arr']}"+(f" hintwords={x['hintwords']}" if x['arr'] else ''))
    print('  t  :',d['t']); print('  ans:',d['ans']); print('  ko :',d['ko']); print('  st :',d['st'])
    if x['kor']: print('  kor:',x['kor'])
