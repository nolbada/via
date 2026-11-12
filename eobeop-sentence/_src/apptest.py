from playwright.sync_api import sync_playwright
import sys,json
errs=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':800})
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.goto('file:///home/claude/book/app/index.html'); pg.wait_for_timeout(300)
    n=pg.evaluate("META.length"); print('chapters',n)
    # walk every set / item automatically
    total=0
    for c in pg.evaluate("META.map(x=>x.n)"):
        pg.evaluate(f"chap({c})")
        ns=pg.evaluate(f"META.filter(x=>x.n=={c})[0].sets.length")
        for si in range(ns):
            pg.evaluate(f"load({c},function(s){{run({c},{si},0)}})"); pg.wait_for_timeout(150)
            cntI=pg.evaluate(f"DB[{c}][{si}].items.length")
            for i in range(cntI):
                pg.evaluate(f"run({c},{si},{i})")
                # solve: tap steps
                for _ in range(6):
                    prompt=pg.inner_text('.prompt')
                    if pg.query_selector('.opt'): break
                    idxs=pg.evaluate("""(function(){return null})()""")
                    # click correct chunks via data
                    kinds=pg.evaluate(f"(function(){{var set=DB[{c}][{si}],it=set.items[{i}];var taps=it.taps||set.taps||[{{k:'S'}},{{k:'M'}}];return taps.map(function(t){{return it.chunks.map(function(x,j){{return x.k==t.k?j:-1}}).filter(function(j){{return j>=0}})}})}})()")
                    for grp in kinds:
                        for j in grp: pg.evaluate(f"document.querySelectorAll('.ch')[{j}].click()")
                    break
                ok=pg.evaluate(f"DB[{c}][{si}].items[{i}].verb.ok")
                btns=pg.query_selector_all('.opt')
                if not btns: errs.append(f'ch{c} set{si} item{i}: no options shown'); continue
                for bt in btns:
                    if bt.inner_text()==ok: bt.click()
                pg.wait_for_timeout(30)
                if not pg.query_selector('.chips2'): errs.append(f'ch{c} set{si} item{i}: reveal failed')
                total+=1
    print('items solved',total); print('errors',errs[:10])
    pg.evaluate("run(1,0,0)"); pg.screenshot(path='/home/claude/w/app1.png')
    b.close()
