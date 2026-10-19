from playwright.sync_api import sync_playwright
import json,re,sys
import sys
L_,DAY=sys.argv[1],sys.argv[2]
P="file:///tmp/claude-0/w3/out/mid/dongah-yun/l%s/basic/index.html"%L_
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":420,"height":900});pg.set_default_timeout(3000)
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(P);pg.wait_for_timeout(500);pg.click("[data-act=start][data-day='%s']"%DAY);pg.wait_for_timeout(300)
    last=None;same=0;wrong=set();shots={};seen=[]
    L=lambda sel:pg.locator(sel+":visible")
    for it in range(9000):
        pg.wait_for_timeout(40);txt=pg.inner_text("body")
        if "분석 완료" in txt: print("FIN",txt[:140].replace("\n"," | "));break
        m=re.search(r"문장 (\d+) / \d+",txt);n=int(m.group(1)) if m else None
        sig=(n,txt[-220:]);same=same+1 if sig==last else 0;last=sig
        if same>80: print("STALL",n,txt[:700].replace("\n"," | "));pg.screenshot(path="stall_%s_%s.png"%(L_,DAY),full_page=True);break
        try:
            if "엑스레이 분석" in txt:
                e=pg.evaluate("(function(){var C=__X.C();return __X.xSeq(C.s)[C.xi];})()");key=(n,e["t"],e.get("r"))
                if key not in seen: seen.append(key)
                if L('[data-act=xnext]').count(): 
                    shots[key]=1
                    L('[data-act=xnext]').first.click();continue
                if e["t"]=="verb":
                    v=pg.evaluate("__X.xVerbs(__X.C().s)");nv=pg.evaluate("__X.C().s.ch.length")
                    if ("w",n) not in wrong:
                        wrong.add(("w",n));w=[i for i in range(nv) if i not in v][0];L('[data-act=xw][data-i="%d"]'%w).first.click()
                    elif len(v)==1: L('[data-act=xw][data-i="%d"]'%v[0]).first.click()
                    else:
                        sel=pg.evaluate("__X.C().xs.sel")
                        for i in v:
                            if i not in sel: L('[data-act=xw][data-i="%d"]'%i).first.click();break
                        else: L('[data-act=xchk]').first.click()
                elif e["t"]=="glue":
                    g=pg.evaluate("__X.C().s.x.glue");L('[data-act=xw][data-i="%d"]:not([disabled])'%g).first.click()
                elif e["t"]=="pat":
                    fm=pg.evaluate("__X.C().s.x.rounds[%d].fm"%e["r"])-1
                    if ("p",n,e["r"]) not in wrong:
                        wrong.add(("p",n,e["r"]));w=0 if fm!=0 else 1;L('[data-act=xp][data-i="%d"]'%w).first.click()
                    L('[data-act=xp][data-i="%d"]'%fm).first.click()
                elif e["t"]=="pair":
                    md=pg.evaluate("__X.C().xs.md");fm=pg.evaluate("__X.C().s.x.rounds[%d].fm"%e["r"])-1
                    sk=pg.evaluate("(function(){var C=__X.C();return __X.xSkel(C.s,%d).map(function(i){return C.s.ch[i].r});})()"%e["r"]);tok=pg.evaluate("__X.XPAT[%d].tok.map(function(x){return x[1]})"%fm)
                    for j,r in enumerate(sk):
                        if str(j) not in md:
                            L('[data-act=xmu][data-i="%d"]'%j).first.click();pg.wait_for_timeout(60)
                            if ("m",n,e["r"]) not in wrong:
                                wrong.add(("m",n,e["r"]));wi=[k for k,x in enumerate(tok) if x!=r][0];L('[data-act=xmt][data-i="%d"]'%wi).first.click();pg.wait_for_timeout(60);break
                            L('[data-act=xmt][data-i="%d"]'%tok.index(r)).first.click();break
                continue
            if L('button.tile').count():
                ids=[int(x.get_attribute("data-i")) for x in L('button[data-act="pick"]').all()]
                if ids: L('button[data-act="pick"][data-i="%d"]'%min(ids)).first.click()
            elif L('button[data-act="roleA"]').count():
                k=int(L('button[data-act="roleA"]').first.get_attribute("data-k"));r=pg.evaluate("__X.C().s.ch[%d].r"%k);L('button[data-act="roleA"][data-r="%s"]'%r).first.click()
            elif L('button[data-act="pickK"]').count():
                ks=[int(x.get_attribute("data-k")) for x in L('button[data-act="pickK"]').all()];L('button[data-act="pickK"][data-k="%d"]'%min(ks)).first.click()
            elif L('button.primary:not([disabled])').count(): L('button.primary:not([disabled])').first.click()
            elif L('button.opt:not([disabled])').count(): L('button.opt:not([disabled])').first.click()
        except Exception as ex: pass
    print("L",L_,"D",DAY,"ERR",errs,"it",it,"seen",seen);b.close()
