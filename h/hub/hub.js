/* 공통: 고등 교과서 앱 묶음 — 상단 바, 저장소, 단계 이동 */
(function(){
var P=location.pathname,i=P.indexOf('/h/');
var BASE=i>=0?P.slice(0,i+3):'/h/';
var HUB={base:BASE,cfg:window.HUBCFG||null};
function get(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}}
function put(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
HUB.get=get;HUB.put=put;
HUB.stepKey=function(step){return 'hub_'+HUB.cfg.bid+'_step_'+step};
HUB.stepState=function(step){return get(HUB.stepKey(step))||{}};
HUB.setStep=function(step,patch){var s=HUB.stepState(step),k;for(k in patch)s[k]=patch[k];s.ts=Date.now();put(HUB.stepKey(step),s)};
HUB.url=function(rel){return BASE+rel};
HUB.hubUrl=function(){return BASE+'hub/'+HUB.cfg.bid+'/'};
var BARCSS='#hubbar{position:fixed;top:0;left:0;right:0;height:46px;z-index:50;background:#14395a;color:#fff;display:flex;align-items:center;gap:6px;padding:0 8px;font-family:"Noto Sans KR","Malgun Gothic",sans-serif;box-sizing:border-box}#hubbar.st{position:sticky}#hubbar a{color:#fff;text-decoration:none;font-size:15px;padding:6px 10px;border-radius:8px;white-space:nowrap}#hubbar a.home{background:rgba(255,255,255,.16);font-weight:700}#hubbar a.nv{border:1px solid rgba(255,255,255,.4)}#hubbar a.off{opacity:.3;pointer-events:none}#hubbar .lb{flex:1;min-width:0;text-align:center;font-size:15px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}';
HUB.bar=function(step,opt){
  opt=opt||{};
  var c=HUB.cfg;if(!c)return;
  var all=c.steps,st=all.filter(function(x){return !x.test}),idx=-1,k,cur=null;
  for(k=0;k<all.length;k++)if(all[k].k===step)cur=all[k];
  for(k=0;k<st.length;k++)if(st[k].k===step)idx=k;
  var prev=null,next=null;
  for(k=idx-1;k>=0;k--)if(st[k].href){prev=st[k];break}
  if(idx>=0)for(k=idx+1;k<st.length;k++)if(st[k].href){next=st[k];break}
  var d=document.createElement('div');d.id='hubbar';
  var lab=idx>=0?('<b>'+(idx+1)+'/'+st.length+'</b> '+st[idx].name):(cur?('<b>시험 대비</b> '+cur.name):c.title);
  d.innerHTML='<a class="home" href="'+HUB.hubUrl()+'">허브</a>'+
   '<a class="nv'+(prev?'':' off')+'" '+(prev?'href="'+BASE+prev.href+'"':'')+'>이전</a>'+
   '<span class="lb">'+lab+'</span>'+
   '<a class="nv'+(next?'':' off')+'" '+(next?'href="'+BASE+next.href+'"':'')+'>다음</a>';
  var sty=document.createElement('style');sty.textContent=BARCSS;document.head.appendChild(sty);
  if(opt.sticky)d.className='st';
  document.body.insertBefore(d,document.body.firstChild);
  if(!opt.sticky)document.body.classList.add('hasbar');
};
HUB.last={
  key:function(step){return 'hub_'+HUB.cfg.bid+'_last_'+step},
  get:function(step){return get(this.key(step))},
  set:function(step,o){o=o||{};o.ts=Date.now();put(this.key(step),o)},
  clear:function(step){this.stop();try{localStorage.removeItem(this.key(step))}catch(e){}},
  stop:function(){if(this._h){window.removeEventListener('scroll',this._h);this._h=null}},
  track:function(step,sel,base){
    var me=this,t=null;me.stop();
    me._h=function(){clearTimeout(t);t=setTimeout(function(){
      var els=document.querySelectorAll(sel),i;
      for(i=0;i<els.length;i++)if(els[i].getBoundingClientRect().bottom>70)break;
      if(i>=els.length)i=els.length-1;
      if(i<0)return;
      var o=base();o.a=i;me.set(step,o);
    },250)};
    window.addEventListener('scroll',me._h,{passive:true});
  },
  scrollTo:function(sel,a){
    var els=document.querySelectorAll(sel),el=els[a];
    if(el){el.scrollIntoView({block:'start'});window.scrollBy(0,-58)}
  },
  toast:function(msg,label,fn){
    var d=document.createElement('div');d.className='toast';
    d.innerHTML='<span>'+HUB.esc(msg)+'</span><button type="button">'+HUB.esc(label)+'</button>';
    d.querySelector('button').onclick=function(){d.remove();fn()};
    document.body.appendChild(d);
    setTimeout(function(){if(d.parentNode)d.remove()},9000);
  }
};
HUB.weak={key:function(){return 'hub_'+HUB.cfg.bid+'_weak'},get:function(){return get(this.key())||{}},has:function(c){return !!this.get()[c]},toggle:function(c){var w=this.get();if(w[c])delete w[c];else w[c]=1;put(this.key(),w);return !!w[c]},label:function(on){return on?'약점노트에 담김':'약점노트에 담기'},btn:function(c){var on=this.has(c);return '<button type="button" class="wkb'+(on?' on':'')+'" data-w="'+c+'">'+this.label(on)+'</button>'}};
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.wkb');if(!b)return;var on=HUB.weak.toggle(b.getAttribute('data-w'));b.classList.toggle('on',on);b.textContent=HUB.weak.label(on)});
HUB.esc=function(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')};

/* 기록 동기화: 구글 시트(Apps Script) — 학생번호+이름이 키 */
HUB.sync=(function(){
var S={},UK='hub_sync_user',MK='hub_sync_meta',busy=false;
function pre(){return ['hub_'+HUB.cfg.bid+'_','verb_study_'+(HUB.cfg.vbid||HUB.cfg.bid)+'_']}
function mine(k){var p=pre(),i;for(i=0;i<p.length;i++)if(k.indexOf(p[i])===0)return true;return false}
function keys(){var o=[],i,k;for(i=0;i<localStorage.length;i++){k=localStorage.key(i);if(k&&mine(k))o.push(k)}return o}
function norm(v){try{return JSON.stringify(JSON.parse(v))}catch(e){return null}}
function user(){return get(UK)}
function url(){return HUB.cfg&&HUB.cfg.sync}
function post(body,keep){return fetch(url(),{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body),keepalive:!!keep}).then(function(r){return r.json()}).then(function(r){if(!r||!r.ok)throw new Error('sync');return r})}
function changed(first){var meta=get(MK)||{},ch={},sent={};keys().forEach(function(k){var n=norm(localStorage.getItem(k));if(n===null)return;if(meta[k]!==n){ch[k]={v:JSON.parse(n),t:first?1:Date.now()};sent[k]=n}});return {ch:ch,sent:sent}}
function run(apply,first,keep){
  var u=user();if(!u||!url())return Promise.resolve(false);
  var c=changed(first);
  return post({act:'put',id:u.id,data:c.ch},keep).then(function(r){
    var meta=get(MK)||{},k,rl=false,rem=r.data||{};
    for(k in c.sent)meta[k]=c.sent[k];
    for(k in rem){
      var s=JSON.stringify(rem[k].v);
      if(apply&&norm(localStorage.getItem(k))!==s){try{localStorage.setItem(k,s);rl=true}catch(e){}}
      if(apply||meta[k]===undefined||c.sent[k]!==undefined)meta[k]=s;
    }
    put(MK,meta);
    try{localStorage.setItem('hub_sync_at',String(Date.now()))}catch(e){}
    return rl;
  });
}
function wipe(){keys().forEach(function(k){try{localStorage.removeItem(k)}catch(e){}});try{localStorage.removeItem(MK)}catch(e){}}
S.user=user;
S.login=function(num,name){
  var prev=user(),id=String(num).replace(/\s+/g,'')+'|'+String(name).replace(/\s+/g,'');
  if(prev&&prev.id===id)return Promise.resolve(false);
  var p=prev?run(false):Promise.resolve();
  return p.then(function(){
    if(prev)wipe();
    put(UK,{id:id,num:String(num).replace(/\s+/g,''),name:String(name).replace(/\s+/g,'')});
    try{localStorage.removeItem(MK)}catch(e){}
    return run(true,!prev).catch(function(e){try{localStorage.removeItem(UK)}catch(x){}throw e});
  });
};
S.logout=function(){return run(false).then(function(){wipe();try{localStorage.removeItem(UK)}catch(e){}})};
S.mount=function(el){
  if(!url())return;
  var u=user(),d=document.createElement('div');d.className='sy';
  if(u){
    d.innerHTML='<div class="sy-t"><b>'+HUB.esc(u.name)+'</b> 님의 기록이 저장되고 있어요</div><div class="sy-s">폰을 바꿔도 같은 이름으로 들어오면 이어져요. 학원 공용 폰은 끝날 때 아래 버튼을 눌러 주세요.</div><button type="button" class="sy-b2">다른 이름으로</button><div class="sy-m"></div>';
    d.querySelector('.sy-b2').onclick=function(){var b=this,m=d.querySelector('.sy-m');b.disabled=true;m.textContent='저장하는 중...';S.logout().then(function(){location.reload()},function(){b.disabled=false;m.textContent='저장이 안 됐어요. 인터넷을 확인하고 다시 눌러 주세요.'})};
  }else{
    d.innerHTML='<div class="sy-t">이름을 넣으면 기록이 이어져요</div><div class="sy-s">폰을 바꾸거나 다른 폰에서 열어도 같은 번호와 이름으로 들어오면 풀던 곳부터 이어서 할 수 있어요.</div><div class="sy-f"><input class="sy-n1" inputmode="numeric" placeholder="학생번호" value="6900"><input class="sy-n2" placeholder="이름"><button type="button" class="sy-b">시작</button></div><div class="sy-m"></div>';
    d.querySelector('.sy-b').onclick=function(){
      var b=this,m=d.querySelector('.sy-m'),n1=d.querySelector('.sy-n1').value,n2=d.querySelector('.sy-n2').value;
      if(!/\S/.test(n1)||!/\S/.test(n2)){m.textContent='번호와 이름을 모두 적어 주세요.';return}
      b.disabled=true;m.textContent='기록을 불러오는 중...';
      S.login(n1,n2).then(function(){location.reload()},function(){b.disabled=false;m.textContent='연결이 안 됐어요. 인터넷을 확인하고 다시 눌러 주세요.'});
    };
  }
  el.appendChild(d);
};
function auto(){
  if(!user()||!url())return;
  run(true).then(function(rl){
    if(rl){var t=Number(sessionStorage.getItem('hub_sync_rl')||0);if(Date.now()-t>20000){try{sessionStorage.setItem('hub_sync_rl',String(Date.now()))}catch(e){}location.reload()}}
  }).catch(function(){});
  setInterval(function(){if(!document.hidden)run(false).catch(function(){})},30000);
  document.addEventListener('visibilitychange',function(){if(document.hidden)run(false,false,true).catch(function(){})});
  window.addEventListener('pagehide',function(){run(false,false,true).catch(function(){})});
}
auto();
return S;
})();
window.HUB=HUB;
})();
