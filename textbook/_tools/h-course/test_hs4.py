from playwright.sync_api import sync_playwright
import json
URL="file:///home/claude/via/textbook/g1-geumcheon-mirae/l4/y/index.html"
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":420,"height":900})
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(URL);pg.wait_for_timeout(500)
    ids=pg.evaluate("S.map(s=>s.id)")
    for sid in ids:
        pg.evaluate("play(%s)"%json.dumps(sid))
        for it in range(300):
            pg.wait_for_timeout(80)
            st=pg.evaluate("({ph,si,ni,step:(typeof steps!=='undefined'&&steps&&steps[si])?steps[si].t:null,p:(typeof steps!=='undefined'&&steps&&steps[si])?steps[si].p||0:0})")
            ph=st["ph"]
            if ph=="verb":
                pg.evaluate("GL.forEach(g=>tv(g[0]))")
                pg.wait_for_timeout(900)
                if pg.locator("button.btn:has-text('다음')").count(): pg.locator("button.btn:has-text('다음')").first.click()
            elif ph in("main","node"):
                if pg.locator("#fb .msg.g").count() and not pg.locator(".card button.btn").count(): continue
                if pg.locator(".card button.btn:visible").count() and pg.locator(".pill").first.inner_text()=="정리":
                    pg.locator(".card button.btn:visible").first.click();continue
                t=st["step"]
                if t=="kind": pg.evaluate("document.querySelectorAll('.ck').forEach(b=>{if(b.firstChild.textContent==cur.nodes[ni].kind)b.click()})")
                elif t=="sub": pg.evaluate("document.querySelectorAll('.ck').forEach(b=>{if(b.firstChild.textContent==cur.nodes[ni].sub)b.click()})")
                elif t=="anc": pg.evaluate("tapw((cur.nodes[ni].np||cur.nodes[ni].anc)[0])")
                elif t=="S": pg.evaluate("tapw(cur.nodes[ni].S[0])")
                elif t=="form": pg.evaluate("(()=>{const n=cur.nodes[ni];pickform(document.querySelectorAll('.ck')[0],%d?0:0);})()" % 0) if False else pg.evaluate("(()=>{const n=cur.nodes[ni],s=steps[si];const f=s.p==2?n.form2:n.form;document.querySelectorAll('.ck')[f-1].click()})()")
                elif t=="V": pg.evaluate("cur.nodes[ni].G.forEach(g=>tapw(g[0]))")
                pg.wait_for_timeout(700)
            elif ph=="nf":
                pg.evaluate("cur.nf.forEach(x=>tn(x.g[0]))");pg.wait_for_timeout(300)
                if pg.locator("button.btn:visible").count(): pg.locator("button.btn:visible").first.click()
            elif ph=="nfq":
                pg.evaluate("(()=>{const it=NQ[nqi];const want=it.t=='to'?it.use:it[it.ans];document.querySelectorAll('.ck').forEach(b=>{if(b.firstChild.textContent==want)b.click()})})()")
                pg.wait_for_timeout(200)
                if pg.locator("button.btn:visible").count(): pg.locator("button.btn:visible").first.click()
            elif ph=="fin":
                break
        w=pg.evaluate("wr");print(sid,"ph",pg.evaluate("ph"),"wr",w)
        if sid=="2-5": pg.screenshot(path="x_fin.png",full_page=True)
    print("ERR",errs)
    b.close()
