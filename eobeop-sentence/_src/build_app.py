# -*- coding: utf-8 -*-
"""usage: python3 build_app.py [outdir]  -> app files for all chapters that have data/chNN.json"""
import json, os, sys, shutil, glob, re
import lib
out=sys.argv[1] if len(sys.argv)>1 else f'{lib.BASE}/app'
CH=json.load(open(f'{lib.BASE}/chapters.json',encoding='utf-8'))
os.makedirs(out+'/d',exist_ok=True)
meta=[];files=[]
for n in range(1,15):
    p=f'{lib.BASE}/data/ch{n:02d}.json'
    if not os.path.exists(p): continue
    sets=json.load(open(p,encoding='utf-8'))
    open(f'{out}/d/ch{n:02d}.js','w',encoding='utf-8').write('window.DB['+str(n)+']='+json.dumps(sets,ensure_ascii=False,separators=(',',':'))+';')
    files.append(f'./d/ch{n:02d}.js')
    meta.append(dict(n=n,t=CH[str(n)],sets=[dict(id=s['id'],title=s['title'],sub=s['sub'],page=s['page'],n=len(s['items'])) for s in sets]))
t=open(f'{lib.BASE}/template3.html',encoding='utf-8').read().replace('__META__',json.dumps(meta,ensure_ascii=False,separators=(',',':')))
open(out+'/index.html','w',encoding='utf-8').write(t)
ver=sys.argv[2] if len(sys.argv)>2 else 'v3'
sw=f"""var C='eobeop-sent-{ver}';
var F=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png',{','.join(repr(f) for f in files)}];
self.addEventListener('install',function(e){{e.waitUntil(caches.open(C).then(function(c){{return c.addAll(F)}}));self.skipWaiting()}});
self.addEventListener('activate',function(e){{e.waitUntil(caches.keys().then(function(k){{return Promise.all(k.filter(function(x){{return x!==C}}).map(function(x){{return caches.delete(x)}}))}}));self.clients.claim()}});
self.addEventListener('fetch',function(e){{e.respondWith(fetch(e.request).then(function(r){{var cp=r.clone();caches.open(C).then(function(c){{c.put(e.request,cp)}});return r}}).catch(function(){{return caches.match(e.request)}}))}});
"""
open(out+'/sw.js','w',encoding='utf-8').write(sw)
for f in ('manifest.webmanifest','icon-192.png','icon-512.png'):
    shutil.copy(f'/home/claude/via/eobeop-sentence/{f}',f'{out}/{f}')
print('app built:',len(meta),'chapters ->',out)
