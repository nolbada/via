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
window.HUB=HUB;
})();
