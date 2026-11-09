#!/bin/bash
# usage: build_daily.sh [key...]  (eobeop-jedaero 폴더에서 실행)
cd "$(dirname "$0")/.." || exit 1
python3 _tools/gen_daily.py "$@" && python3 _tools/gc.py && python3 - <<'P'
import glob,re
for f in glob.glob('ch0*-p*.html'):
    s=open(f,encoding='utf8').read()
    if 'daily.css' in s or '.navb{' in s:
        t=s.replace('<details class="anl"></details>','')
        t=re.sub(r'<span class="badge" style="display:none">.*?</span>','',t)
        if t!=s: open(f,'w',encoding='utf8').write(t)
P
