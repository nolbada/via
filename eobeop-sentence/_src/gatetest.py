from playwright.sync_api import sync_playwright
import json
posted=[]
def handler(route):
    body=route.request.post_data or ''
    try: j=json.loads(body)
    except: j={}
    posted.append(j)
    d=j.get('data') or {}
    if d: return route.fulfill(status=200,content_type='application/json',body=json.dumps({'ok':True}))
    now={'sa-p1':{'v':{'s':json.dumps({'o':1})},'t':1},'sa-p2':{'v':{'s':json.dumps({'o':0})},'t':1},'ej-x':{'v':{'s':json.dumps({'o':1})},'t':1}}
    route.fulfill(status=200,content_type='application/json',headers={'access-control-allow-origin':'*'},body=json.dumps({'ok':True,'data':now}))
errs=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':800})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('https://script.google.com/**',handler)
    pg.goto('file:///home/claude/book/app/index.html'); pg.wait_for_timeout(200)
    pg.evaluate("chap(1)"); pg.wait_for_timeout(600)
    print('locked count',pg.evaluate("document.querySelectorAll('.setbtn.lk').length"),'of',pg.evaluate("document.querySelectorAll('.setbtn').length"))
    print('first locked?',pg.evaluate("document.querySelectorAll('.setbtn')[0].classList.contains('lk')"))
    pg.evaluate("document.querySelectorAll('.setbtn')[1].click()"); pg.wait_for_timeout(200)
    print('click locked stays list:',pg.evaluate("!!document.querySelector('.setbtn')"))
    pg.evaluate("document.querySelectorAll('.setbtn')[0].click()"); pg.wait_for_timeout(400)
    print('open set runs:',pg.evaluate("!!document.querySelector('.prompt')"))
    pg.evaluate("localStorage.setItem('ej_teacher','1');chap(1,true)")
    print('teacher locked',pg.evaluate("document.querySelectorAll('.setbtn.lk').length"))
    # teacher page
    pg.goto('file:///home/claude/book/app/sa-t/index.html'); pg.wait_for_timeout(500)
    print('teacher on',pg.evaluate("document.querySelectorAll('.pg.on').length"))
    pg.evaluate("document.querySelector('[data-k=sa-p3]').click()"); pg.wait_for_timeout(200)
    print('posted',[p.get('data') for p in posted if p.get('data')][-1].keys() if any(p.get('data') for p in posted) else None)
    b.close()
print('errs',errs)
