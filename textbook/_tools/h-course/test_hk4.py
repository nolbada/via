from playwright.sync_api import sync_playwright
import json,re,sys
src=open("/home/claude/via/textbook/g1-geumcheon-mirae/l4/e/index.html",encoding="utf8").read()
DATA=json.loads(re.search(r'\nvar DATA=(\[.*?\]);\n',src).group(1))
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":420,"height":900})
    pg.set_default_timeout(3000)
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file:///home/claude/via/textbook/g1-geumcheon-mirae/l4/e/index.html");pg.wait_for_timeout(500)
    pg.click("[data-act=startnext]");pg.wait_for_timeout(300)
    last=None;same=0;wrong_done=set()
    for it in range(4000):
        pg.wait_for_timeout(40)
        txt=pg.inner_text("body")
        if "분석 완료" in txt: print("FIN",txt[:160].replace("\n"," | "));pg.screenshot(path="e_fin.png",full_page=True);break
        m=re.search(r"문장 (\d) / 7",txt);n=int(m.group(1)) if m else None;s=DATA[n-1] if n else None
        sig=(n,txt[-200:]);same=same+1 if sig==last else 0;last=sig
        if same>60:
            print("STALL",n,txt[:500].replace("\n"," | "));pg.screenshot(path="e_stall.png",full_page=True);break
        try:
            L=lambda sel:pg.locator(sel+":visible")
            if L('button.primary:has-text("다음 단계")').count(): L('button.primary:has-text("다음 단계")').first.click()
            elif L('button[data-act="xq"]').count():
                b0=L('button[data-act="xq"]').first;t=b0.get_attribute("data-t");gq=s["gq"]
                if t=="fm":
                    if n not in wrong_done:
                        wrong_done.add(n);w=1 if gq["fm"]!=1 else 2
                        L('button[data-act="xq"][data-t="fm"][data-v="%d"]'%w).first.click()
                    L('button[data-act="xq"][data-t="fm"][data-v="%d"]'%gq["fm"]).first.click()
                else:
                    ci=int(b0.get_attribute("data-ci"));x=[z for z in gq["cl"] if z["ci"]==ci][0]
                    L('button[data-act="xq"][data-ci="%d"][data-v="%s"]'%(ci,x["kind"] if t=="kind" else x["sub"])).first.click()
            elif L('button.tile').count():
                ids=[int(x.get_attribute("data-i")) for x in L('button[data-act="pick"]').all()]
                if ids: L('button[data-act="pick"][data-i="%d"]'%min(ids)).first.click()
            elif L('button[data-act="roleA"]').count():
                k=int(L('button[data-act="roleA"]').first.get_attribute("data-k"))
                L('button[data-act="roleA"][data-r="%s"]'%s["ch"][k]["r"]).first.click()
            elif L('button[data-act="pickK"]').count():
                ks=[int(x.get_attribute("data-k")) for x in L('button[data-act="pickK"]').all()]
                L('button[data-act="pickK"][data-k="%d"]'%min(ks)).first.click()
            elif L('button.primary:not([disabled])').count(): L('button.primary:not([disabled])').first.click()
            elif L('button.opt:not([disabled])').count(): L('button.opt:not([disabled])').first.click()
        except Exception as e: pass
    print("ERR",errs,"it",it);b.close()
